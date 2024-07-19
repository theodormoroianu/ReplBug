import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "MDEV-14868"
LINK = "https://jira.mariadb.org/browse/MDEV-14868"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MARIADB, "10.2.12-encrypted-logs"
)
SETUP_SQL_SCRIPT = """
CREATE TABLE t (a TEXT) ENGINE = InnoDB;
"""

DESCRIPTION = "Rollbacks make the server crash."


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> BEGIN;
        conn_0> INSERT INTO t VALUES (REPEAT('a', 20000));
        conn_0> SAVEPOINT sp;
        conn_0> INSERT INTO t VALUES (REPEAT('a', 20000));
        conn_0> ROLLBACK TO sp;
        conn_0> COMMIT;
        """
    ]
