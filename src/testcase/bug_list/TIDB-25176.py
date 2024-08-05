import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-25176"
LINK = "https://github.com/pingcap/tidb/issues/25176"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.TIDB, "v4.0.7.tikv"
)

DESCRIPTION = """Setting tidb_snapshot breaks the isolation guarantees."""

SETUP_SQL_SCRIPT = """
create table test.ttt (id int primary key, a int);
insert into test.ttt values (1, 1);
"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET SESSION TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> begin;
        
        conn_1> update test.ttt set a=2 where id=1;

        conn_0> set @@tidb_snapshot=TIMESTAMP(NOW());

        conn_0> select a from test.ttt where id=1;
        conn_0> select a from test.ttt where id=1 for update;
        conn_0> select a from test.ttt where id=1;

        conn_0> commit;
        """,
    ]
