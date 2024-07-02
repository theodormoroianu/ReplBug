import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

# taken from  https://github.com/JZuming/TxCheck/blob/main/docs/tidb_bugs.md

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-34222"
LINK = "https://github.com/pingcap/tidb/issues/34222"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(db_config.DatabaseType.TIDB, "v6.1.0")

DESCRIPTION = """Second scenario fails with "BIGING UNSIGNED value out of range" """


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> delete from t_xa9msd;
        conn_0> select * from t_xa9msd as ref_0
                where (63 & 72) - case when ref_0.wkey is NULL then 66 else 100 end > 88;
        """,
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> START TRANSACTION;
        conn_0> delete from t_xa9msd;
        conn_0> select * from t_xa9msd as ref_0
                where (63 & 72) - case when ref_0.wkey is NULL then 66 else 100 end > 88;
        conn_0> commit;
        """,
    ]
