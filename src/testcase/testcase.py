from typing import Callable, List, Dict
import logging
import mysql.connector
import mysql.connector.cursor

import database.config as db_config
import database.provide_database_server as db_provider

class Instruction:
    """
    Represents a single instruction to be run in a testcase
    """
    def __init__(self, transaction_id: int, instruction: str, expects_output: bool, validator: Callable[[str], bool] = None):
        self.transaction_id = transaction_id
        self.instruction = instruction
        self.validator = validator
        self.expects_output = expects_output


class Testcase:
    """
    Represents a single testcase
    """
    def __init__(
            self,
            name: str,
            nr_transactions: int,
            instructions: List[Instruction],
            db_and_type: db_config.DatabaseTypeAndVersion):
        self.name = name
        self.nr_transactions = nr_transactions
        self.instructions = instructions
        self.db_and_type = db_and_type

    def run(self):
        """
        Runs the testcase
        """
        logging.info(f"Running testcase {self.name} on {self.db_and_type}")
        with db_provider.DatabaseProvider(self.db_and_type) as provider:
            conn = provider.database_connection.to_connection()
            
            transaction_to_cursor: Dict[int, mysql.connector.cursor.CursorBase] = {}

            for instruction in self.instructions:
                if instruction.transaction_id not in transaction_to_cursor:
                    transaction_to_cursor[instruction.transaction_id] = conn.cursor()

                cursor = transaction_to_cursor[instruction.transaction_id]
                cursor.execute(instruction.instruction)
                if instruction.expects_output:
                    output = cursor.fetchall()
                    print(f"Output for transaction {instruction.transaction_id}: {output}")
                