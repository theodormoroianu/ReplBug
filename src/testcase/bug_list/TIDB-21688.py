import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-21688"
LINK = "https://github.com/pingcap/tidb/issues/21688"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.TIDB, "v4.0.7.tikv"
)

DESCRIPTION = """Locking is different depending on whether the queried column is part of a point or a table scan."""

SETUP_SQL_SCRIPT = """
drop table if exists t;
create table t (k1 int, k2 int, v int, unique key (k1));
insert into t values (1, 1, null), (2, 2, 2);
"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> begin;
        conn_1> begin;
        conn_0> update t set v = 10 where (k1, v) in ((1, null)); -- 0 row affected (point get)
        conn_1> update t set v = 11 where (k1, v) in ((1, null)); -- blocked
        conn_0> commit;
        conn_1> commit;
        """,
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> begin;
        conn_1> begin;
        conn_0> update t set v = 10 where (k2, v) in ((1, null)); -- 0 row affected (table scan)
        conn_1> update t set v = 11 where (k2, v) in ((1, null)); -- won't be blocked
        conn_0> commit;
        conn_1> commit;
        """,
    ]
