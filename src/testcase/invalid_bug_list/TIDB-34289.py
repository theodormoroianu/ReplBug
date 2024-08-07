import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-34289"
LINK = "https://github.com/pingcap/tidb/issues/34289"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(db_config.DatabaseType.TIDB, "v5.4.0")

DESCRIPTION = """The name of tables and handles are not parsed in DEBUG table."""

SETUP_SQL_SCRIPT = """
create table t(id int primary key, v int);
insert into t values(1, 1);
"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET SESSION TRANSACTION ISOLATION LEVEL {isolation_level.value};

        conn_0> prepare s from 'select * from t where id=1 for update';
        conn_0> begin;

        conn_1> alter table t add column v2 int;
        
        conn_0> select * from t where id=1 for update;
        conn_0> execute s;
        """,
    ]
