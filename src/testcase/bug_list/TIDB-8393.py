import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-8393"
LINK = "https://github.com/pingcap/tidb/issues/8393"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(db_config.DatabaseType.TIDB, "v6.4.0")

DESCRIPTION = """Variable set in transaction is not rolled back."""

SETUP_SQL_SCRIPT = """
create table t(a bigint, b bigint);
"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> begin;
        conn_0> set @a = 100;
        conn_0> insert into t values(1, 1);
        conn_0> rollback;
        conn_0> select @a;
        """,
    ]
