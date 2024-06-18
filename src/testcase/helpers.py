import enum
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
