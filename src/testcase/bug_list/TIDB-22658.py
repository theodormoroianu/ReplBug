import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-22658"
LINK = "https://github.com/pingcap/tidb/issues/22658"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.TIDB, "v4.0.0-beta.2.tikv"
)

DESCRIPTION = """read only transactions are read/write"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> CREATE TABLE t1 (a int);
        conn_0> start transaction read only;
        conn_0> insert into t1 values (1);
        """,
    ]
