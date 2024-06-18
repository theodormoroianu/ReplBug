from typing import Callable, List, Dict, Tuple, Union
import logging
import mysql.connector
import mysql.connector.cursor
import multiprocessing
from queue import Queue
import time

import database.config as db_config
import database.provide_db_container as db_provider

# Timeout for a transaction to wait for a lock
LOCK_WAIT_TIMEOUT = 3
# Time between concurent operations
OPERATIONS_GAP = 0.3
# Timeout for receiving the output of the instructions
OUTPUT_TIMEOUT = 10


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


class TransactionProcess(multiprocessing.Process):
    def __init__(
        self,
        conn: db_config.DatabaseConnection,
        instructions_to_run_queue: Queue[Tuple[int, str]],
        instruction_output_queue: Queue[Tuple[int, str]],
    ):
        """
        Initialize the transaction process, which will run the instructions.

        :param conn: The connection to the database.
        :param instructions_to_run_queue: The queue with the instructions to run: (instruction nr, instruction).\
            the instruction nr is the order of the instruction in ALL OF THE INSTRUCTIONS for that testcase.
        :param instruction_output_queue: The queue where the output of the instructions will be put: (instruction nr, output).
        """
        super().__init__()
        self.conn = conn
        self.instructions_to_run_queue = instructions_to_run_queue
        self.instruction_output_queue = instruction_output_queue

    def run(self):
        connection = self.conn.to_connection(autocommit=True)

        # Pick database and set timeout
        connection.cursor().execute("use testdb;")

        # set timeout of 3 seconds for lock wait
        connection.cursor().execute(
            f"SET SESSION innodb_lock_wait_timeout = {LOCK_WAIT_TIMEOUT};"
        )

        # Flag to indicate if an error was encountered by one of the operations in this thread
        self.encountered_error = False

        # Run instructions as they come
        while True:
            instruction_tuple = self.instructions_to_run_queue.get()
            if instruction_tuple is None:
                # Quit the process
                break
            instruction_nr, instruction_str = instruction_tuple
            if self.encountered_error:
                # Skip the instruction if an error was encountered
                output = "Skipped due to previous error."
            else:
                try:
                    cursor = connection.cursor()
                    cursor.execute(instruction_str)
                    output = None
                    if cursor.with_rows:
                        output = cursor.fetchall()
                except mysql.connector.errors.OperationalError as e:
                    self.encountered_error = True
                    output = f"ERROR: {e}"
                except mysql.connector.errors.DatabaseError as e:
                    self.encountered_error = True
                    output = f"ERROR: {e}"
                except Exception as e:
                    self.encountered_error = True
                    output = f"ERROR: {e}"

            # Send the result
            self.instruction_output_queue.put((instruction_nr, output))

        self.instruction_output_queue.put(None)
        connection.close()


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

            # Mapping from transaction id to the transaction process
            transaction_id_to_process: Dict[int, TransactionProcess] = {}
            # Queues for the instructions to run and the output of the instructions
            transaction_id_to_instructions_queue: Dict[
                int, multiprocessing.Queue[Tuple[int, str]]
            ] = {}
            transaction_id_to_output_queue: Dict[
                int, multiprocessing.Queue[Tuple[int, str]]
            ] = {}

            logging.info("Running instructions...")
            for instruction_idx, instruction in enumerate(self.instructions):
                assert instruction.transaction_id is not None
                logging.info(f"Running instruction: {instruction.instruction}")

                # If it's the first instruction from this transaction, start a new process
                # for it.
                if instruction.transaction_id not in transaction_id_to_process:
                    instructions_q = multiprocessing.Queue()
                    output_q = multiprocessing.Queue()
                    transaction_process = TransactionProcess(
                        provider.db_connection, instructions_q, output_q
                    )
                    transaction_process.start()
                    transaction_id_to_process[instruction.transaction_id] = (
                        transaction_process
                    )
                    transaction_id_to_instructions_queue[instruction.transaction_id] = (
                        instructions_q
                    )
                    transaction_id_to_output_queue[instruction.transaction_id] = (
                        output_q
                    )

                # Add the instruction to the corresponding process
                transaction_id_to_instructions_queue[instruction.transaction_id].put(
                    (instruction_idx, instruction.instruction)
                )

                # Sleep for the gap between operations
                time.sleep(OPERATIONS_GAP)

            # Now that we sent all the instructions, we:
            # - send None to the instruction queues to signal the end of the instructions
            # - retrieve the output of the instructions
            # - mark any instruction for which we don't have output as failed with timeout
            for (
                _,
                instructions_q,
            ) in transaction_id_to_instructions_queue.items():
                instructions_q.put(None)

            # First mark all instructions as timeout, and then overwrite the ones that have output
            for instruction in self.instructions:
                instruction.output = "ERROR: Timeout for this transaction."

            # Wait for the output of the instructions
            output_queues_to_process = list(transaction_id_to_output_queue.values())

            for _ in range(OUTPUT_TIMEOUT):
                non_empty_queues = []
                for output_q in output_queues_to_process:
                    # Get as many outputs from the queue as possible
                    while True:
                        try:
                            output = output_q.get(block=False)
                            # gracefully finish the process
                            if output is None:
                                break
                            # if we got an output, mark the instruction as successful
                            instruction_idx, output = output
                            self.instructions[instruction_idx].output = output
                        except:
                            non_empty_queues.append(output_q)
                            break

                if non_empty_queues == []:
                    # All queues are empty
                    break
                output_queues_to_process = non_empty_queues
                time.sleep(1)

            # kill all the processes
            for _, process in transaction_id_to_process.items():
                process.terminate()

            for _, process in transaction_id_to_process.items():
                process.join()

            # Get the container's logs (for finding stuff like crashes)
            self.db_server_logs = provider.get_logs()
