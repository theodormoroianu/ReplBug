import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-20002"
LINK = "https://github.com/pingcap/tidb/issues/20002"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.TIDB, "fa6baa9f.tikv"
)

DESCRIPTION = """admin check table t should work"""

SETUP_SQL_SCRIPT = """
set @@tidb_enable_clustered_index = 1;
create table t ( c_int int, c_str varchar(40), c_datetime datetime, primary key(c_str) , unique key(c_int), unique key(c_datetime)  );
insert into t values (1, 'laughing hertz', '2020-04-27 20:29:30'), (2, 'sharp yalow', '2020-04-01 05:53:36'), (3, 'pedantic hoover', '2020-03-10 11:49:00');

"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> begin;
        conn_0> update t set c_str = 'amazing herschel' where c_int = 3;
        conn_0> select c_int, c_str, c_datetime from t where c_datetime between '2020-01-09 22:00:28' and '2020-04-08 15:12:37';
        conn_0> commit;
        conn_0> admin check table t;
        conn_0> select * from t where c_datetime = '2020-03-10 11:49:00';
        """,
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> update t set c_str = 'amazing herschel' where c_int = 3;
        conn_0> select c_int, c_str, c_datetime from t where c_datetime between '2020-01-09 22:00:28' and '2020-04-08 15:12:37';
        conn_0> admin check table t;
        conn_0> select * from t where c_datetime = '2020-03-10 11:49:00';
        """,
    ]
