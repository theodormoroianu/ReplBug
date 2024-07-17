import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-20881"
LINK = "https://github.com/pingcap/tidb/issues/20881"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(db_config.DatabaseType.TIDB, "v4.0.4")

DESCRIPTION = """The insert should block until the other transaction is committed, but it doesn't."""

SETUP_SQL_SCRIPT = """
create table t (a char(10) collate utf8mb4_unicode_ci, b char(20) collate utf8mb4_general_ci, c int, primary key (a, b, c));

"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> begin;
        conn_0> insert into t values ("$", "c", 20);
        conn_0> select * from t;
        """,
    ]
