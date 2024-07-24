"""
This module handle a single transaction run.
"""

import time
import multiprocessing
import mysql.connector
from queue import Queue

import database.config as db_config
from testcase.helpers import (
    MYSQL_CONNECTION_LOCK_WAIT_TIMEOUT_S,
    Instruction,
    SuppressStderr,
)


class TransactionProcess(multiprocessing.Process):
    """
    This class represents a transaction process, which will run the instructions.

    The instructions are taken from the `instructions_to_run_queue` and the results are put in the
    `instruction_output_queue`.

    For stopping the process, two `None` instructions should be put in the `instructions_to_run_queue`:
        * The first `None` instruction will stop the process from waiting for new instructions.
        * The second `None` instruction will stop the process (which in particular closes the SQL connection).

    Two `None` instructions are needed because we don't want to close the connection before all the
    concurent processes are done executing their instructions.
    """

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

        # Ask the connector to fetch warnings.
        # This should not be required, but it seems that the connector does not fetch
        # warnings by default.
        connection.get_warnings = True

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
                # Stop waiting for instructions
                break
            if self.encountered_error:
                instruction.previous_instruction_failed = True

            try:
                cursor = connection.cursor()
                # Need to supress stderr because the mysql connector prints warnings to stderr,
                # and there is no documented way to disable this.
                with SuppressStderr():
                    cursor.execute(instruction.sql_instruction_content)
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
            if cursor.warning_count:
                cursor.fetchwarnings()
                instruction.warnings = cursor.warnings
                if not instruction.warnings:
                    # If for some reason the warnings are not fetched,
                    # we still want to know that there were warnings
                    instruction.warnings = [f"Warning count: {cursor.warning_count}"]
            instruction.nr_affected_rows = cursor.rowcount

            # Send the result
            self.instruction_output_queue.put(instruction)

        self.instruction_output_queue.put(None)
        instruction = self.instructions_to_run_queue.get()
        assert instruction is None, "The second instruction should be None"
        connection.close()
