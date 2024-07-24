import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-39851"
LINK = "https://github.com/pingcap/tidb/issues/39851"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.TIDB, "v6.4.0.tikv"
)

DESCRIPTION = """Select does not throw errors when running concurently."""

SETUP_SQL_SCRIPT = """
CREATE TABLE t (c1 INT, c2 INT);
INSERT INTO t VALUES (1, 1);
"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> BEGIN;
        conn_1> BEGIN;
        conn_0> SELECT c1 FROM t WHERE c2 FOR UPDATE;
        conn_1> SELECT /*+ INL_JOIN(t)*/c1 FROM t WHERE c2<=c1 FOR UPDATE;
        conn_0> COMMIT;
        conn_1> COMMIT;
        """,
        """
        conn_0> SELECT /*+ INL_JOIN(t)*/c1 FROM t WHERE c2<=c1 FOR UPDATE;
        """,
        """
        conn_0> BEGIN;
        conn_0> SELECT /*+ INL_JOIN(t)*/c1 FROM t WHERE c2<=c1 FOR UPDATE;
        """,
    ]
