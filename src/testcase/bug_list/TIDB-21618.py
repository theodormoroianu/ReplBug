import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-21618"
LINK = "https://github.com/pingcap/tidb/issues/21618"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.TIDB, "v6.4.0.tikv"
)

DESCRIPTION = """pessimistic lock doesn't work on the partition for subquery/joins"""

SETUP_SQL_SCRIPT = """
create table t (c_int int, d_int int, primary key (c_int), key(d_int)) partition by hash (c_int) partitions 4 ;
insert into t values (1, 2);
"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> begin pessimistic;
        conn_0> select * from t where d_int in (select d_int from t where c_int = 1) for update;

        conn_1> begin pessimistic;
        conn_1> select * from t where d_int = 2 for update;

        conn_0> COMMIT;
        conn_1> COMMIT;
        """,
    ]
