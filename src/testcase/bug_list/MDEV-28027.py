import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

# From DT2

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "MDEV-28027"
LINK = "https://jira.mariadb.org/browse/MDEV-28027"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MARIADB, "10.8.3"
)
SETUP_SQL_SCRIPT = """
DROP TABLE IF EXISTS t;
CREATE TABLE t(c1 INT);
INSERT INTO t(c1) VALUES (3), (2), (1);
"""

DESCRIPTION = "Mismatch between MySQL and MariaDB: in Mariadb, RAND('t') is true only if >= 0.5. Record 1 is skipped."


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> BEGIN;
        conn_0> SELECT * FROM t WHERE RAND('t');
        conn_0> COMMIT;
    """,
    ]
