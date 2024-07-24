import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-24195"
LINK = "https://github.com/pingcap/tidb/issues/24195"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.TIDB, "v6.4.0.tikv"
)

DESCRIPTION = """Query in optimistic transaction returns rows with same PK"""

SETUP_SQL_SCRIPT = """
create table t (a int, b int, primary key (a, b) /*T![clustered_index] nonclustered */);
insert into t values (1, 10);
"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> begin optimistic;
        conn_0> insert into t values (1, 10);
        conn_0> select * from t;
        conn_0> commit;
        """,
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> begin pessimistic;
        conn_0> insert into t values (1, 10);
        conn_0> select * from t;
        conn_0> commit;
        """,
        """
        conn_0> insert into t values (1, 10);
        conn_0> select * from t;
        """,
    ]
