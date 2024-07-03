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
    ):
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
                    for instr in self.instructions_to_run:
                        instr.output = "Skipped due to error in pre-run instructions."
                    self.runned_instructions = self.instructions_to_run
                    return
            conn.close()
            time.sleep(1)

            # Mapping from transaction id to the transaction process
            transaction_id_to_process: Dict[int, TransactionProcess] = {}
            # Queues for the instructions to run and the output of the instructions
            transaction_id_to_instructions_queue: Dict[
                int, multiprocessing.Queue[Instruction]
            ] = {}
            transaction_id_to_output_queue: Dict[
                int, multiprocessing.Queue[Instruction]
            ] = {}

            logging.info("Running instructions...")
            for instruction_idx, instruction in enumerate(self.instructions_to_run):
                assert instruction.instruction_nr == instruction_idx
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
                instruction.dispatched_time = time.time()
                transaction_id_to_instructions_queue[instruction.transaction_id].put(
                    copy.deepcopy(instruction)
                )

                # Sleep for the gap between operations
                time.sleep(MYSQL_CONNECTION_GAP_BETWEEN_INSTRUCTIONS_S)

            # Now that we sent all the instructions, we:
            # - send None to the instruction queues to signal the end of the instructions
            # - retrieve the output of the instructions
            # - mark any instruction for which we don't have output as failed with timeout
            for (
                _,
                instructions_q,
            ) in transaction_id_to_instructions_queue.items():
                instructions_q.put(None)

            # Wait for the output of the instructions
            output_queues_to_process = list(transaction_id_to_output_queue.values())

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
                            self.runned_instructions[
                                runned_instruction.instruction_nr
                            ] = runned_instruction
                        except:
                            non_empty_queues.append(output_q)
                            break

                if non_empty_queues == []:
                    # All queues are empty
                    break
                output_queues_to_process = non_empty_queues
                time.sleep(1)

            for instruction_nr in range(len(self.instructions_to_run)):
                if self.runned_instructions[instruction_nr] is None:
                    self.runned_instructions[instruction_nr] = copy.deepcopy(
                        self.instructions_to_run[instruction_nr]
                    )
                    self.runned_instructions[instruction_nr].output = (
                        "ERROR: Timeout for this transaction."
                    )

            # kill all the processes
            for _, process in transaction_id_to_process.items():
                process.terminate()

            for _, process in transaction_id_to_process.items():
                process.join()

            # Get the container's logs (for finding stuff like crashes)
            self.db_server_logs = provider.get_logs()
