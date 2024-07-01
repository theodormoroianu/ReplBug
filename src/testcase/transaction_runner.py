"""
This module handle a single transaction run.
"""

import time
import multiprocessing
import mysql.connector
from queue import Queue

import database.config as db_config
from testcase.helpers import MYSQL_CONNECTION_LOCK_WAIT_TIMEOUT_S, Instruction


class TransactionProcess(multiprocessing.Process):
    def __init__(
        self,
        conn: db_config.DatabaseConnection,
        instructions_to_run_queue: Queue[Instruction],
        instruction_output_queue: Queue[Instruction],
    ):
        """
        Initialize the transaction process, which will run the instructions.

        :param conn: The connection to the database.
        :param instructions_to_run_queue: The queue with the instructions to run
        :param instruction_output_queue: The queue with the executed instructions.
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
            f"SET SESSION innodb_lock_wait_timeout = {MYSQL_CONNECTION_LOCK_WAIT_TIMEOUT_S};"
        )

        # Flag to indicate if an error was encountered by one of the operations in this thread
        self.encountered_error = False

        # Run instructions as they come
        while True:
            instruction = self.instructions_to_run_queue.get()
            if instruction is None:
                # Quit the process
                break
            if self.encountered_error:
                instruction.previous_instruction_failed = True

            try:
                cursor = connection.cursor()
                cursor.execute(instruction.instruction)
                instruction.executed_time = time.time()
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

            instruction.output = output

            # Send the result
            self.instruction_output_queue.put(instruction)

        self.instruction_output_queue.put(None)
        connection.close()
