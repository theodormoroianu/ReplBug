import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-19585"
LINK = "https://github.com/pingcap/tidb/issues/19585"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.TIDB, "b0c3fe7b.tikv"
)

DESCRIPTION = """The second select should output the same table as the first one, but it doesn't."""

SETUP_SQL_SCRIPT = """
create table t1  (c_int int, primary key (c_int)) partition by range (c_int) (partition p0 values less than (10), partition p1 values less than maxvalue) ;
insert into t1 (c_int) values (1);
"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> begin;
        conn_0> insert into t1 values (10);
        conn_0> update t1 set c_int = c_int + 10 where c_int in (1, 11);
        conn_0> commit;
        conn_0> select * from t1 order by c_int;
        """,
        """
        conn_0> insert into t1 values (10);
        conn_0> update t1 set c_int = c_int + 10 where c_int in (1, 11);
        conn_0> select * from t1 order by c_int;
        """,
    ]
