from typing import Callable, List, Dict, Union
import logging
import mysql.connector
import mysql.connector.cursor
import threading
from queue import Queue
import time

import database.config as db_config
import database.provide_db_container as db_provider

# Timeout for a transaction to wait for a lock
LOCK_WAIT_TIMEOUT = 5
# Time between concurent operations
OPERATIONS_GAP = 0.2


class Instruction:
    """
    Represents a single instruction to be run in a testcase
    """

    def __init__(
        self,
        transaction_id: Union[int, None],
        instruction: str,
        validator: Callable[[str], bool] = None,
    ):
        self.transaction_id = transaction_id
        self.instruction = instruction
        self.validator = validator
        self.output = None

    def __repr__(self):
        return f"Instruction(transaction_id={self.transaction_id}, instruction={self.instruction})"


class TransactionThread(threading.Thread):
    def __init__(self, conn: db_config.DatabaseConnection):
        super().__init__()
        self.connection = conn.to_connection(autocommit=True)

        # Pick database and set timeout
        self.connection.cursor().execute("use testdb;")
        # set timeout of 3 seconds for lock wait
        self.connection.cursor().execute(
            f"SET SESSION innodb_lock_wait_timeout = {LOCK_WAIT_TIMEOUT};"
        )
        self.instructions: Queue[Instruction] = Queue()
        # Flag to indicate if an error was encountered by one of the operations in this thread
        self.encountered_error = False

    def run(self):
        while True:
            instruction = self.instructions.get()
            if instruction is None:
                break
            try:
                cursor = self.connection.cursor()
                cursor.execute(instruction.instruction)
                if cursor.with_rows:
                    output = cursor.fetchall()
                    instruction.output = output
                    logging.debug(
                        f"Output for transaction {instruction.transaction_id}: {output}"
                    )
            except mysql.connector.errors.OperationalError as e:
                logging.error(f"Error running instruction: {e}")
                self.encountered_error = True
                # save error as the output of the instruction
                instruction.output = f"Error: {e}"
            except mysql.connector.errors.DatabaseError as e:
                logging.error(f"Error running instruction: {e}")
                self.encountered_error = True
                # save error as the output of the instruction
                instruction.output = f"Error: {e}"
            except Exception as e:
                logging.error(f"Error running instruction: {e}")
                print(f"Error running instruction: {e}")
                print(f"Instruction: {instruction.instruction}")
                # print stack trace of exception
                import traceback

                traceback.print_exc()
                raise e

            self.instructions.task_done()
        self.connection.close()


class TestcaseRunner:
    """
    Represents a single testcase
    """

    def __init__(
        self,
        name: str,
        instructions: List[Instruction],
        db_and_type: db_config.DatabaseTypeAndVersion,
        pre_run_instructions: List[Instruction] = None,
    ):
        self.name = name
        self.instructions = instructions
        self.db_and_type = db_and_type
        self.pre_run_instructions = pre_run_instructions
        self.db_server_logs = None

    def run(self):
        """
        Spins a container with the required DB, runs the concurent transactions and
        extracts the result.
        """
        logging.info(f"Running testcase {self.name} on {self.db_and_type}")
        with db_provider.DatabaseProvider(self.db_and_type) as provider:
            # Reset the environment before running the testcase, in case
            # it is not the first run.
            conn = provider.db_connection.to_connection(autocommit=True)
            conn.cursor().execute("drop database if exists testdb;")
            conn.cursor().execute("create database testdb;")
            conn.cursor().execute("use testdb;")

            if self.pre_run_instructions:
                logging.info("Running pre-run instructions...")
                try:
                    for instruction in self.pre_run_instructions:
                        assert (
                            instruction.transaction_id == None
                        ), "Should be a pre-run instruction."
                        cursor = conn.cursor()
                        it = cursor.execute(instruction.instruction, multi=True)
                        for cur in it or []:
                            if cur.with_rows:
                                output = cur.fetchall()
                                instruction.output = output
                                print(f"Output for pre-run instruction: {output}")
                except mysql.connector.errors.DatabaseError as e:
                    logging.error(f"Error running pre-run instructions: {e}")
                    for instr in self.instructions:
                        instr.output = "Skipped due to error in pre-run instructions."
                    return
            conn.close()
            time.sleep(1)

            # Mapping from transaction id to cursor / connection object
            transaction_id_to_thread: Dict[int, TransactionThread] = {}

            logging.info("Running instructions...")
            for instruction_idx, instruction in enumerate(self.instructions):
                assert instruction.transaction_id is not None
                logging.info(f"Running instruction: {instruction.instruction}")
                if instruction.transaction_id not in transaction_id_to_thread:
                    # create a new concurent connection for the transaction
                    trx_thread = TransactionThread(provider.db_connection)
                    trx_thread.start()
                    transaction_id_to_thread[instruction.transaction_id] = trx_thread

                # Sleep for the gap between operations
                time.sleep(OPERATIONS_GAP)

                # Check if any thread reported and error
                for thread in transaction_id_to_thread.values():
                    if thread.encountered_error:
                        instruction.output = "Skipped due to previous error."
                        break
                else:
                    # Add the instruction to the corresponding thread
                    trx_thread = transaction_id_to_thread[instruction.transaction_id]
                    trx_thread.instructions.put(instruction)

            # Stop all threads
            for thread in transaction_id_to_thread.values():
                thread.instructions.put(None)
            for thread in transaction_id_to_thread.values():
                thread.join()

            # Get the container's logs (for finding stuff like crashes)
            self.db_server_logs = provider.get_logs()
