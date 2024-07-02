import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-30397"
LINK = "https://github.com/pingcap/tidb/issues/30397"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(db_config.DatabaseType.TIDB, "v5.4.0")

DESCRIPTION = "The two resulting tables are different."


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> update t_berydd set c_cdqetd = t_berydd.c_ioru4c;
        conn_0> select count(c_mp6ko) from t_berydd;
        """,
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> start transaction;
        conn_0> update t_berydd set c_cdqetd = t_berydd.c_ioru4c;
        conn_0> select count(c_mp6ko) from t_berydd;
        conn_0> commit;
        """,
    ]
