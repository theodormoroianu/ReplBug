import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "MDEV-25457"
LINK = "https://jira.mariadb.org/browse/MDEV-25457"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MARIADB, "10.2.37-debug"
)
SETUP_SQL_SCRIPT = """
"""

DESCRIPTION = "An update makes the DB server crash."


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> CREATE TEMPORARY TABLE t (a INT) ENGINE=InnoDB;
        conn_0> INSERT INTO t VALUES (1);
        conn_0> START TRANSACTION READ ONLY;
        conn_0> UPDATE t SET a = NULL;
        conn_0> ROLLBACK;
        """,
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> CREATE TEMPORARY TABLE t (a INT) ENGINE=InnoDB;
        conn_0> INSERT INTO t VALUES (1);
        conn_0> UPDATE t SET a = NULL;
        """,
    ]
