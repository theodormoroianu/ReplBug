import enum
from typing import Callable, Union
import database.config as db_config


class IsolationLevel(enum.Enum):
    """
    Enum class for the isolation levels supported by the MySQL database.
    """

    REPEATABLE_READ = "REPEATABLE READ"
    READ_COMMITTED = "READ COMMITTED"
    READ_UNCOMMITTED = "READ UNCOMMITTED"
    SERIALIZABLE = "SERIALIZABLE"


def isolation_levels_for_db_and_version(
    db_and_version: db_config.DatabaseTypeAndVersion,
):
    """
    Returns the isolation levels supported by the given database.

    :param database: The database for which to return the supported isolation levels.
    :return: A list of isolation levels supported by the given database.
    """
    if db_and_version.database_type == db_config.DatabaseType.TIDB:
        return [
            IsolationLevel.REPEATABLE_READ,
            IsolationLevel.READ_COMMITTED,
        ]
    else:
        return [
            IsolationLevel.REPEATABLE_READ,
            IsolationLevel.READ_COMMITTED,
            IsolationLevel.READ_UNCOMMITTED,
            IsolationLevel.SERIALIZABLE,
        ]


# Default isolation level for the MySQL database.
DEFAULT_ISOLATION_LEVEL = IsolationLevel.REPEATABLE_READ
# Timeout for a transaction to wait for a lock
MYSQL_CONNECTION_LOCK_WAIT_TIMEOUT_S = 3
# Time between dispatching two consecutive instructions to (possibly different)
# processes.
MYSQL_CONNECTION_GAP_BETWEEN_INSTRUCTIONS_S = 0.3
# Timeout duration for waiting for a process running a transaction
# to finish (and return None on its output queue).
MYSQL_CONNECTION_TRANSACTION_WAIT_TIMEOUT_S = 10


class Instruction:
    """
    Represents a single instruction to be run in a testcase
    """

    def __init__(
        self,
        transaction_id: Union[int, None],
        instruction_nr: Union[int, None],
        instruction: str,
    ):
        """
        Initialize the instruction.

        :param transaction_id: The id of the transaction to which the instruction belongs.
        :param instruction_nr: The number of the instruction in the testcase (all transactions).
        :param instruction: The SQL command to run, as a string.
        """
        self.transaction_id = transaction_id
        self.instruction = instruction
        self.output = None
        # When the instruction was sent to the process for execution
        self.dispatched_time = None
        # When the instruction was executed (output received)
        self.executed_time = None
        # If a previous instruction in the same transaction failed
        self.previous_instruction_failed = False
        # The number of the instruction in the testcase (all transactions)
        self.instruction_nr = instruction_nr
        # The number of affected rows
        self.nr_affected_rows = None
        # The number of warnings
        self.nr_warnings = None

    def __repr__(self):
        return f"Instruction(transaction_id={self.transaction_id}, instruction={self.instruction})"
