import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-20535"
LINK = "https://github.com/pingcap/tidb/issues/20535"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.TIDB, "v4.0.4.tikv"
)

DESCRIPTION = """The insert should block until the other transaction is committed, but it doesn't."""

SETUP_SQL_SCRIPT = """
create table t2(k int, kk int, val int, primary key(k, kk));
insert into t2 values(1, 1, 1);
"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> begin;
        conn_1> begin;
        conn_0> delete from t2 where k = 1;
        conn_1> insert into t2 values(1, 1, 2);
        """,
    ]
