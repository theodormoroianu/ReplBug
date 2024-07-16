"""
This module exposes a class able to run a single testcase of a bug.

Basically, this class receives:
 - A list of instructions to initialize the database.
 - A list of instructions to run concurrently, for each instruction the transaction
   id being provided.

After the "run" method is called, the object will contain in the "runned_instructions"
attribute the result of the instructions.
"""

import copy
from typing import List, Dict, Optional
import logging
import mysql.connector
import mysql.connector.cursor
import multiprocessing
import time

import database.config as db_config
import database.provide_db_container as db_provider
from testcase.helpers import (
    MYSQL_CONNECTION_GAP_BETWEEN_INSTRUCTIONS_S,
    MYSQL_CONNECTION_TRANSACTION_WAIT_TIMEOUT_S,
    Instruction,
)
from testcase.transaction_runner import TransactionProcess


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
        kill_server_after_testcase: bool = False,
    ):
        """
        Creates a new testcase runner.

        :param name: The name of the testcase (mostly bug ID + isolation level).
        :param instructions: The instructions to run concurrently.
        :param db_and_type: The database and the version on which the bug should be replicable.
        :param pre_run_instructions: The instructions to run before the main instructions (initialization).
        :param kill_server_after_testcase: If the server should be stopped after running the test.
        """
        self.name = name
        # Instructions we have to run on separate InstructionProcess processes.
        self.instructions_to_run = instructions
        # The result of the instructions. If None, the instruction is not run yet.
        self.runned_instructions: List[Optional[Instruction]] = [
            None for _ in instructions
        ]
        self.db_and_type = db_and_type
        self.pre_run_instructions = pre_run_instructions
        self.db_server_logs = None
        self.kill_server_after_testcase = kill_server_after_testcase

        # Mapping from transaction id to the transaction process
        self.transaction_id_to_process: Dict[int, TransactionProcess] = {}
        # Queues for the instructions to run and the output of the instructions
        self.transaction_id_to_instructions_queue: Dict[
            int, multiprocessing.Queue[Instruction]
        ] = {}
        self.transaction_id_to_output_queue: Dict[
            int, multiprocessing.Queue[Instruction]
        ] = {}

    def _run_setup_instructions(self, db_connection: db_config.DatabaseConnection):
        """
        Runs the DB initialization and the pre-run instructions (if present).
        """
        logging.info("Initializing the database...")
        conn = db_connection.to_connection(autocommit=True)
        conn.cursor().execute("drop database if exists testdb;")
        conn.cursor().execute("create database testdb;")
        conn.cursor().execute("use testdb;")

        if not self.pre_run_instructions:
            conn.close()
            return

        logging.info("Running pre-run instructions...")
        try:
            for instruction in self.pre_run_instructions:
                assert (
                    instruction.transaction_id == None
                ), "Should be a pre-run instruction."
                cursor = conn.cursor()
                it = cursor.execute(instruction.sql_instruction_content, multi=True)
                for cur in it or []:
                    if cur.with_rows:
                        output = cur.fetchall()
                        instruction.output = output
                        print(f"Output for pre-run instruction: {output}")
        except mysql.connector.errors.DatabaseError as e:
            logging.error(f"Error running pre-run instructions: {e}")
            for instr in self.instructions_to_run:
                instr.output = "Skipped due to error in pre-run instructions."
            self.runned_instructions = self.instructions_to_run
            return
        conn.close()

    def _dispatch_instructions_to_processes(
        self, db_connection: db_config.DatabaseConnection
    ):
        """
        Send the instructions, each to its own process.
        If the process doesn't exist yet, it gets created.
        The instructions are sent in the order they are provided, with according waiting time.
        """
        logging.info("Running instructions...")
        for instruction_idx, instruction in enumerate(self.instructions_to_run):
            assert instruction.instruction_nr == instruction_idx
            assert instruction.transaction_id is not None
            logging.info(f"Running instruction: {instruction.sql_instruction_content}")

            # If it's the first instruction from this transaction, start a new process
            # for it.
            if instruction.transaction_id not in self.transaction_id_to_process:
                instructions_q = multiprocessing.Queue()
                output_q = multiprocessing.Queue()
                transaction_process = TransactionProcess(
                    db_connection, instructions_q, output_q
                )
                transaction_process.start()
                self.transaction_id_to_process[instruction.transaction_id] = (
                    transaction_process
                )
                self.transaction_id_to_instructions_queue[
                    instruction.transaction_id
                ] = instructions_q
                self.transaction_id_to_output_queue[instruction.transaction_id] = (
                    output_q
                )

            # Add the instruction to the corresponding process
            instruction.dispatched_time = time.time()
            self.transaction_id_to_instructions_queue[instruction.transaction_id].put(
                copy.deepcopy(instruction)
            )

            # Sleep for the gap between operations
            time.sleep(MYSQL_CONNECTION_GAP_BETWEEN_INSTRUCTIONS_S)

    def _wait_for_instructions_to_finish(self):
        """
        Waits for the instruction processes to finish, or for a timeout.
        """
        output_queues_to_process = list(self.transaction_id_to_output_queue.values())

        for _ in range(MYSQL_CONNECTION_TRANSACTION_WAIT_TIMEOUT_S):
            non_empty_queues = []
            for output_q in output_queues_to_process:
                # Get as many outputs from the queue as possible
                while True:
                    try:
                        runned_instruction = output_q.get(block=False)
                        # gracefully finish the process
                        if runned_instruction is None:
                            break
                        self.runned_instructions[runned_instruction.instruction_nr] = (
                            runned_instruction
                        )
                    except Exception:
                        non_empty_queues.append(output_q)
                        break

            if non_empty_queues == []:
                # All queues are empty
                break

            output_queues_to_process = non_empty_queues
            time.sleep(1)

    def _mark_instructions_not_executed(self):
        """
        Some instructions won't get executed (e.g. if the DB server crashes).
        We mark them as failed.
        """
        for instruction_nr in range(len(self.instructions_to_run)):
            # The instruction isn't run yet
            if self.runned_instructions[instruction_nr] is None:
                # Deep copy the instruction, and mark the output as an error
                self.runned_instructions[instruction_nr] = copy.deepcopy(
                    self.instructions_to_run[instruction_nr]
                )
                self.runned_instructions[instruction_nr].output = (
                    "ERROR: Timeout for this transaction."
                )

    def _send_none_to_instruction_queues(self):
        """
        This method sends None to the instruction queues to signal the end of the instructions.
        There are 2 `None` sent for each transaction process:
            * One to signal the end of the instructions.
            * One to signal the end of the process.

        We need to send 2 `None` to the instruction queues to ensure that the processes don't close their
        SQL connections before all the instructions are executed.
        """
        for (
            _,
            instructions_q,
        ) in self.transaction_id_to_instructions_queue.items():
            instructions_q.put(None)

    def run(self):
        """
        Spins a container with the required DB, runs the concurent transactions and
        extracts the result.
        """
        logging.info(
            f"Running testcase {self.name} on {self.db_and_type}, kill server after: {self.kill_server_after_testcase}"
        )
        with db_provider.DatabaseProvider(
            self.db_and_type, self.kill_server_after_testcase
        ) as provider:
            # Reset the environment before running the testcase, in case
            # it is not the first run.
            self._run_setup_instructions(provider.db_connection)
            time.sleep(1)

            # Dispatch the instructions to the processes.
            self._dispatch_instructions_to_processes(provider.db_connection)

            # Now that we sent all the instructions, we:
            # - retrieve the output of the instructions
            # - mark any instruction for which we don't have output as failed with timeout
            # - send None to the instruction queues to signal the end of the instructions

            # Tell the processes that we don't have any more instructions.
            self._send_none_to_instruction_queues()

            time.sleep(0.1)

            # Wait for the output of the instructions.
            self._wait_for_instructions_to_finish()

            # Mark the instructions that didn't finish as failed
            self._mark_instructions_not_executed()

            # Send None to terminate the processes gracefully
            self._send_none_to_instruction_queues()
            time.sleep(0.1)

            # kill all the processes
            for _, process in self.transaction_id_to_process.items():
                process.terminate()
            for _, process in self.transaction_id_to_process.items():
                process.join()

            # Get the container's logs (for finding stuff like crashes)
            self.db_server_logs = provider.get_logs()
