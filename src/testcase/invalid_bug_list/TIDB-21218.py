import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-21218"
LINK = "https://github.com/pingcap/tidb/issues/21218"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.TIDB, "v4.0.0-beta.2.tikv"
)

DESCRIPTION = """The second select should output the same table as the first one, but it doesn't."""

SETUP_SQL_SCRIPT = """
drop table if exists t;
create table t(id int, v int, val int, primary key(id, v));
insert into t values(1, 1, 1);
"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> begin pessimistic;
        conn_1> begin pessimistic;
        
        conn_0> select * from t where id = 1 and v = 1 for update;
        conn_1> insert into t values(1, 1, 2);
        conn_0> update t set v = 2 where id = 1 and v = 1;
        
        conn_0> commit;
        conn_1> commit;

        conn_2> SELECT * FROM t;
        """,
    ]
