import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-20692"
LINK = "https://github.com/pingcap/tidb/issues/20692"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.TIDB, "v4.0.0-beta.2.tikv"
)

DESCRIPTION = """The update should block, but it doesn't."""

SETUP_SQL_SCRIPT = """
create table t (id int primary key, v int, vv int, vvv int, unique key u0(id, v, vv));
insert into t values(1, 1, 1, 1);
"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> begin;
        conn_1> begin;
        conn_2> begin;
        conn_0> delete from t where id = 1 and v = 1 and vv = 1;
        conn_1> insert into t values(1, 2, 3, 4);
        conn_2> update t set id = 10, v = 20, vv = 30, vvv = 40 where id = 1 and v = 2 and vv = 3;
        conn_0> commit;
        conn_2> commit;
        conn_1> commit;
        """,
    ]
