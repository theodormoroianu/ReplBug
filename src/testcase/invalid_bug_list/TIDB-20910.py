import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-20910"
LINK = "https://github.com/pingcap/tidb/issues/20910"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.TIDB, "45571c5e"
)

DESCRIPTION = """admin check table t should work"""

SETUP_SQL_SCRIPT = """
create table t (id int auto_increment primary key, c int);
insert into t (id, c) values (1, 2), (3, 4);
"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> begin;
        conn_1> alter table t add unique index uk(c);
        conn_0> update t set c = 2 where id = 3;
        conn_0> commit;
        conn_1> admin check table t;
        """,
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_1> alter table t add unique index uk(c);
        conn_0> update t set c = 2 where id = 3;
        conn_1> admin check table t;
        """,
    ]
