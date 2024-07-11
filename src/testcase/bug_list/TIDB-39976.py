import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-39976"
LINK = "https://github.com/pingcap/tidb/issues/39976"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.TIDB, "v6.4.0.tikv"
)

DESCRIPTION = """Reports error instead of warning when running in a transaction."""

SETUP_SQL_SCRIPT = """
CREATE TABLE t(c0 TEXT(284));
"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> BEGIN;
        conn_0> REPLACE INTO t VALUES ('G6y*k]88]');
        conn_0> DELETE FROM t WHERE CAST(TIDB_VERSION() AS DATE);
        conn_0> COMMIT;
        """,
        """
        conn_0> REPLACE INTO t VALUES ('G6y*k]88]');
        conn_0> DELETE FROM t WHERE CAST(TIDB_VERSION() AS DATE);
        """,
    ]
