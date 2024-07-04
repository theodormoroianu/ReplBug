import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "MDEV-28142"
LINK = "https://jira.mariadb.org/browse/MDEV-28142"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MARIADB, "10.7.3"
)

SETUP_SQL_SCRIPT = """
CREATE TABLE t (c1 TEXT);
INSERT INTO t VALUES ('a');
"""

DESCRIPTION = "Should not throw an error on the third scenario."


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> start transaction;
        conn_0> UPDATE t SET c1 = 'b' WHERE CAST(IF('a', '1', 1) AS SIGNED);
        conn_0> SELECT * FROM t;
        conn_0> COMMIT;
        """
    ]
