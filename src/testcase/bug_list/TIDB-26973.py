import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-26973"
LINK = "https://github.com/pingcap/tidb/issues/26973"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.TIDB, "v5.2.0-alpha-1a54708a7.tikv"
)

DESCRIPTION = """The name of tables and handles are not parsed in DEBUG table."""

SETUP_SQL_SCRIPT = """
create table t (a int primary key, b int) partition by range(a) (PARTITION p0 VALUES LESS THAN (2), PARTITION p1 VALUES LESS THAN (4),
    PARTITION p2 VALUES LESS THAN (MAXVALUE));
insert into t values (1, 10), (2, 20), (3, 30);
"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET SESSION TRANSACTION ISOLATION LEVEL {isolation_level.value};

        conn_0> begin;
        conn_1> begin;

        conn_0> update t set a=10 where a=1;
        conn_1> update t set b=11 where a=2;

        conn_0> update t set b=12 where a=2;
        conn_1> update t set b=13 where a=1;

        conn_0> SELECT * FROM INFORMATION_SCHEMA.DEADLOCKS;
        """,
    ]
