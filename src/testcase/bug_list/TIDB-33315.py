import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

# taken from  DT2

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-33315"
LINK = "https://github.com/pingcap/tidb/issues/33315"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(db_config.DatabaseType.TIDB, "v5.4.0")

SETUP_SQL_SCRIPT = """
CREATE TABLE t (c1 INT PRIMARY KEY, c2 INT);
INSERT INTO t (c1, c2) VALUES (1, 1);
"""

DESCRIPTION = "conn 1 should get an empty set"


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> BEGIN PESSIMISTIC;
        conn_0> UPDATE t SET c1=2, c2=2;
        conn_1> BEGIN PESSIMISTIC;
        conn_1> DELETE FROM t;
        conn_0> COMMIT;
        conn_1> SELECT * FROM t;
        conn_1> COMMIT;
        """
    ]
