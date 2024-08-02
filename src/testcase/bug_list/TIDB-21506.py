import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-21506"
LINK = "https://github.com/pingcap/tidb/issues/21506"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.TIDB, "v4.0.7.tikv"
)

DESCRIPTION = """Inserting data twice when another transaction is updating the data does not fail."""

SETUP_SQL_SCRIPT = """
create table t1 (id int primary key, v int);
create table t2 (id int primary key, v int);
insert into t1 values (1, 10), (2, 20);
"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET SESSION TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> begin;
        conn_0> insert into t2 select * from t1;
        conn_1> update t1 set id = id + 2;
        conn_0> insert into t2 select * from t1; -- succeed
        conn_0> select * from t2; -- (1, 10), (2, 20), (3, 10), (4, 20)
        conn_0> commit;
        conn_2> select * from t1;
        conn_2> select * from t2;
        """,
    ]
