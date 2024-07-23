import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-37653"
LINK = "https://github.com/pingcap/tidb/issues/37653"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(db_config.DatabaseType.TIDB, "v6.2.0")

DESCRIPTION = """TiDB locks the record which is filtered by the non-index condition"""

SETUP_SQL_SCRIPT = """
create table t1(id1 int, id2 int, id3 int, PRIMARY KEY(id1), UNIQUE KEY udx_id2 (id2));
INSERT INTO t1 VALUES(1,1,1);
"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> begin pessimistic;
        conn_0> select * from t1 where id1 = 1 and id2 = 2 for update;
        conn_1> begin pessimistic;
        conn_1> select * from t1 where id1 = 1 for update;
        conn_1> commit;
        conn_0> commit;
        """,
    ]
