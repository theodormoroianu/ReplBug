import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

# taken from  DT2

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-31405"
LINK = "https://github.com/pingcap/tidb/issues/31405"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(db_config.DatabaseType.TIDB, "v5.3.0")


SETUP_SQL_SCRIPT = """
DROP TABLE IF EXISTS t0;
CREATE TABLE t0(c0 DECIMAL);
"""

DESCRIPTION = """Error on the first scenario"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> BEGIN;
        conn_0> INSERT INTO t0 VALUES(1.0);
        conn_0> UPDATE t0 SET c0 = c0 + 1 WHERE c0 > 'a';
        conn_0> COMMIT;
        """,
    ]
