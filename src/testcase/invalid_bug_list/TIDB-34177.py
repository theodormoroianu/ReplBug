import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

# taken from  DT2

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-34177"
LINK = "https://github.com/pingcap/tidb/issues/34177"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(db_config.DatabaseType.TIDB, "v6.0.0")


SETUP_SQL_SCRIPT = """
DROP TABLE IF EXISTS t;
CREATE TABLE t (c1 VARCHAR(14));
INSERT IGNORE INTO t(c1) VALUES ('test');
"""

DESCRIPTION = """Error on the first scenario"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> BEGIN;
        conn_0> DELETE FROM t WHERE (CAST(('123abc') AS DOUBLE)) IS NULL;
        conn_0> COMMIT;
        """,
    ]
