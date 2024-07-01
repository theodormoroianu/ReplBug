import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

# From DT2

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "MDEV-28040"
LINK = "https://jira.mariadb.org/browse/MDEV-28140"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MARIADB, "10.8.3"
)
SETUP_SQL_SCRIPT = """
CREATE TABLE t(c1 BLOB NOT NULL, c2 TEXT);
INSERT IGNORE INTO t VALUES (NULL, NULL), (NULL, 'aaa');
"""

DESCRIPTION = "The locks are not released in a timely manner. This does not seem to be a bug though."


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> BEGIN;
        conn_0> UPDATE t SET c2='test' WHERE c1;
        conn_1> BEGIN;
        conn_1> UPDATE t SET c2 = 'def';
        conn_0> COMMIT;
        conn_1> COMMIT;
        """,
    ]
