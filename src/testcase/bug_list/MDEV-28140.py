import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

# From DT2

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "MDEV-28140"
LINK = "https://jira.mariadb.org/browse/MDEV-28140"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MARIADB, "10.8.3"
)
SETUP_SQL_SCRIPT = """
CREATE TABLE t(c1 BLOB NOT NULL, c2 TEXT);
INSERT IGNORE INTO t VALUES (NULL, NULL), (NULL, 'abc');
"""

DESCRIPTION = "The second and third scenarios (SELECT and DELETE) should fail like the first one (UPDATE) does."


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> BEGIN;
        conn_0> UPDATE t SET c2 = 'test' WHERE c1;
        conn_0> COMMIT;
    """,
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> BEGIN;
        conn_0> SELECT * FROM t WHERE c1;
        conn_0> COMMIT;
    """,
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> BEGIN;
        conn_0> DELETE FROM t WHERE c1;
        conn_0> COMMIT;
    """,
    ]
