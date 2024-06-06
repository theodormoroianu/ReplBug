import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-30289"
LINK = "https://github.com/pingcap/tidb/issues/30289"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(db_config.DatabaseType.TIDB, "5.2.1")


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> insert into t_p2n_bb values (2, 35);
        conn_0> delete from t_p2n_bb where exists (select 1 from t_aqzphd);
        """,
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> start transaction;
        conn_0> insert into t_p2n_bb values (2, 35);
        conn_0> delete from t_p2n_bb where exists (select 1 from t_aqzphd);
        conn_0> commit;
        """,
    ]
