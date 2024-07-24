import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-21470"
LINK = "https://github.com/pingcap/tidb/issues/21470"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.TIDB, "c9288d24"
)

DESCRIPTION = """Amending transaction accepts DDLs that changes column types but gives wrong result"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> set @@global.tidb_enable_change_column_type=true;
        conn_0> create table t (id int primary key, v varchar(10));
        conn_0> begin pessimistic;
        conn_0> insert into t values (1, "123456789");
        conn_1> alter table t modify column v varchar(5);
        conn_0> select sleep(5);
        conn_0> commit;
        conn_0> select * from t;
        """,
        """
        conn_0> set @@global.tidb_enable_change_column_type=true;
        conn_0> create table t (id int primary key, v varchar(10));
        conn_0> insert into t values (1, "123456789");
        conn_1> alter table t modify column v varchar(5);
        conn_0> select sleep(5);
        conn_0> select * from t;
        """,
    ]
