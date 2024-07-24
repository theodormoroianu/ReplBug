import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-21284"
LINK = "https://github.com/pingcap/tidb/issues/21284"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(db_config.DatabaseType.TIDB, "v4.0.8")

DESCRIPTION = """transaction retry may cause panic"""

SETUP_SQL_SCRIPT = """
create table t (a int);
insert into t values (1);
"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> set @@tidb_disable_txn_auto_retry=0;
        conn_0> set autocommit=0;
        conn_0> select * from t;
        conn_0> SET SQL_SELECT_LIMIT=DEFAULT;
        conn_1> update t set a=2;
        conn_0> update t set a=3;
        conn_0> commit;
        """,
        """
        conn_0> set @@tidb_disable_txn_auto_retry=0;
        conn_0> select * from t;
        conn_0> SET SQL_SELECT_LIMIT=DEFAULT;
        conn_1> update t set a=2;
        conn_0> update t set a=3;
        """,
    ]
