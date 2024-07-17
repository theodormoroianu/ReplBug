import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-20773"
LINK = "https://github.com/pingcap/tidb/issues/20773"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.TIDB, "v4.0.8.tikv"
)

DESCRIPTION = """The update should block, but it doesn't."""

SETUP_SQL_SCRIPT = """
create table t (id int primary key, c_str varchar(20));
insert into t values (1, '0001'), (2, '0002'), (3, null), (4, '0003'), (5, null);
"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> begin;
        conn_0> insert into t values (6, '0004');
        conn_0> insert into t values (7, null);
        conn_1> alter table t add c_str_new varchar(20);
        conn_0> update t set c_str = '0005' where id = 1;
        conn_0> update t set c_str = null where id = 2;
        conn_0> update t set c_str = '0006' where id = 3;
        conn_0> delete from t where id = 4;
        conn_0> delete from t where id = 5;
        conn_0> commit;
        """,
    ]
