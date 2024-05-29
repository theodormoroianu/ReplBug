import enum


class IsolationLevel(enum.Enum):
    """
    Enum class for the isolation levels supported by the MySQL database.
    """
    REPEATABLE_READ = "REPEATABLE READ"
    READ_COMMITTED = "READ COMMITTED"
    READ_UNCOMMITTED = "READ UNCOMMITTED"
    SERIALIZABLE = "SERIALIZABLE"

# Default isolation level for the MySQL database.
DEFAULT_ISOLATION_LEVEL = IsolationLevel.REPEATABLE_READ