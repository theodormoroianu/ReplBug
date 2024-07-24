import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-23179"
LINK = "https://github.com/pingcap/tidb/issues/23179"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.TIDB, "v4.0.11"
)

DESCRIPTION = """point-get + pessimistic txn + overflow in secondary index may panic"""

SETUP_SQL_SCRIPT = """
create table t(k tinyint, v int, unique key(k));
"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> begin pessimistic;
        conn_0> update t set v = 100 where k = -200;
        """,
        """
        conn_0> update t set v = 100 where k = -200;
        """,
    ]
