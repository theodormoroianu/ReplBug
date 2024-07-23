import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-20975"
LINK = "https://github.com/pingcap/tidb/issues/20975"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.TIDB, "fa6baa9f.tikv"
)

DESCRIPTION = """Unexpected "Information schema is changed" when commits"""

SETUP_SQL_SCRIPT = """
create table t1(a int);
insert into t1 values (1);
"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> begin pessimistic;
        conn_0> update t1 set a=a;
        conn_1> create table t2(a int);
        conn_0> commit;
        """,
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> update t1 set a=a;
        conn_1> create table t2(a int);
        """,
    ]
