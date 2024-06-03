from typing import Callable, List, Dict, Union
import logging
import mysql.connector
import mysql.connector.cursor

import database.config as db_config
import database.provide_db_container as db_provider


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

    def run(self):
        """
        Runs the testcase
        """
        logging.info(f"Running testcase {self.name} on {self.db_and_type}")
        with db_provider.DatabaseProvider(self.db_and_type) as provider:
            conn = provider.db_connection.to_connection()
            conn.cursor().execute("drop database if exists testdb;")
            conn.cursor().execute("create database testdb;")
            conn.cursor().execute("use testdb;")

            if self.pre_run_instructions:
                logging.info("Running pre-run instructions...")
                # try:
                for instruction in self.pre_run_instructions:
                    assert instruction.transaction_id == None
                    cursor = conn.cursor()
                    it = cursor.execute(instruction.instruction, multi=True)
                    for cur in it:
                        if cur.with_rows:
                            output = cur.fetchall()
                            instruction.output = output
                            print(f"Output for pre-run instruction: {output}")
                # except SQLException as e:
                #     logging.error(f"Error running pre-run instructions: {e}")
                #     print(f"Error running pre-run instructions: {e}")
                #     input("Press enter to continue...")
                #     raise e
            conn.commit()
            conn.close()

            # Mapping from transaction id to cursor / connection object
            transaction_to_connection: Dict[int, mysql.connector.MySQLConnection] = {}

            logging.info("Running instructions...")
            for instruction_idx, instruction in enumerate(self.instructions):
                assert instruction.transaction_id is not None
                logging.info(f"Running instruction: {instruction.instruction}")
                if instruction.transaction_id not in transaction_to_connection:
                    # create a new concurent connection for the transaction
                    new_conn = provider.db_connection.to_connection()
                    new_conn.cursor().execute("use testdb;")
                    # set timeout of 3 seconds for lock wait
                    new_conn.cursor().execute(
                        "SET SESSION innodb_lock_wait_timeout = 3"
                    )
                    transaction_to_connection[instruction.transaction_id] = new_conn

                try:
                    conn = transaction_to_connection[instruction.transaction_id]
                    # Check if conn is still connected
                    conn.ping()

                    cursor = conn.cursor()
                    cursor.execute(instruction.instruction)
                    if cursor.with_rows:
                        output = cursor.fetchall()
                        instruction.output = output
                        logging.debug(
                            f"Output for transaction {instruction.transaction_id}: {output}"
                        )
                except mysql.connector.errors.DatabaseError as e:
                    logging.error(f"Error running instruction: {e}")
                    print(f"Error running instruction: {e}")
                    # save error as the output of the instruction
                    instruction.output = f"Error: {e}"
                    # stop the loop, as we are no longer interested in running the rest of the instructions
                    for instr in self.instructions[instruction_idx + 1 :]:
                        instr.output = "Skipped due to previous error."
                    break
                except Exception as e:
                    logging.error(f"Error running instruction: {e}")
                    print(f"Error running instruction: {e}")
                    print(f"Instruction: {instruction.instruction}")
                    # print stack trace of exception
                    import traceback

                    traceback.print_exc()
                    raise e
