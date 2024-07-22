import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "MDEV-24545"
LINK = "https://jira.mariadb.org/browse/MDEV-24545"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MARIADB, "10.3.28"
)
SETUP_SQL_SCRIPT = """
CREATE TABLE t1 (a INT) ENGINE=InnoDB;
"""

CREATE_NEW_SERVER_FOR_TESTCASE = True

DESCRIPTION = (
    "Second SELECT NEXTVAL is in the global scope, and should find the sequence S1."
)


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> START TRANSACTION;
        conn_0> SELECT * FROM t1;

        conn_1> CREATE SEQUENCE s1 ENGINE=InnoDB;
        conn_1> FLUSH TABLES;

        conn_0> SELECT NEXTVAL(s1);
        conn_0> COMMIT;

        conn_0> SELECT NEXTVAL(s1);
        """,
    ]
