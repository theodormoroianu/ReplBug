import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-36581"
LINK = "https://github.com/pingcap/tidb/issues/36581"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(db_config.DatabaseType.TIDB, "v6.1.0")

DESCRIPTION = """Issuing autocommit=on instructions makes rollback fail"""

SETUP_SQL_SCRIPT = """
create table test(a int);
insert into test values (590);
"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> set autocommit = ON;
        conn_0> begin;
        conn_0> select * from test;
        conn_0> update test set a=a+1;
        conn_0> select * from test;
        conn_0> set autocommit=ON;
        conn_0> rollback;
        conn_0> select * from test;
        """,
    ]
