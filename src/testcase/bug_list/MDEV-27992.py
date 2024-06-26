import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

# From DT2

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "MDEV-27992"
LINK = "https://jira.mariadb.org/browse/MDEV-27992"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MARIADB, "10.7.3"
)
SETUP_SQL_SCRIPT = """
DROP TABLE IF EXISTS t;
CREATE TABLE t(c1 INT PRIMARY KEY, c2 INT);
INSERT INTO t(c1) VALUES (8);
"""
DESCRIPTION = "The delete from conn_1 should block, wait for conn_0 to commit, and then delete everything. But it doesn't."


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> BEGIN;
        conn_1> BEGIN;
        conn_0> UPDATE t SET c1 = 5, c2 = 5;
        conn_1> DELETE FROM t;
        conn_0> UPDATE t SET c1 = 3;
        conn_0> COMMIT;
        conn_1> SELECT * FROM t FOR UPDATE;
        conn_1> ROLLBACK;
    """,
    ]
