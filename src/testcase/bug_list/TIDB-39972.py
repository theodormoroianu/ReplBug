import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-39972"
LINK = "https://github.com/pingcap/tidb/issues/39972"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.TIDB, "v6.4.0.tikv"
)

DESCRIPTION = """UPDATE statement with CAST() reports an error in the transaction."""

SETUP_SQL_SCRIPT = """
CREATE TABLE t(c0 INT);
INSERT IGNORE INTO t VALUES (2);
"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> BEGIN;
        conn_0> DELETE FROM t WHERE TRUE;
        conn_0> UPDATE t SET c0=0 WHERE (CAST('a' AS SIGNED)); -- report an error
        conn_0> COMMIT;
        """,
        """
        conn_0> DELETE FROM t WHERE TRUE;
        conn_0> UPDATE t SET c0=0 WHERE (CAST('a' AS SIGNED)); -- report an error
        """,
    ]
