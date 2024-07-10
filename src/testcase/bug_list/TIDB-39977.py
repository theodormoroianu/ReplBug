import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-39977"
LINK = "https://github.com/pingcap/tidb/issues/39977"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(db_config.DatabaseType.TIDB, "v6.4.0")

DESCRIPTION = """Gets warnings when running in a transaction."""

SETUP_SQL_SCRIPT = """
CREATE TABLE t(c0 DECIMAL, c1 BLOB(79));
INSERT INTO t(c0, c1) VALUES (NULL, ' '), (-2, 'oCK');
"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> BEGIN;
        conn_0> DELETE FROM t;
        conn_0> SELECT /*+ STREAM_AGG()*/c0 FROM t WHERE c1 FOR UPDATE; -- Warning
        conn_0> COMMIT;
        """,
        """
        conn_0> DELETE FROM t;
        conn_0> SELECT /*+ STREAM_AGG()*/c0 FROM t WHERE c1 FOR UPDATE; -- Warning
        """,
    ]
