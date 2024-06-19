import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

# taken from  https://github.com/JZuming/TxCheck/blob/main/docs/tidb_bugs.md

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-34041"
LINK = "https://github.com/pingcap/tidb/issues/34041"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(db_config.DatabaseType.TIDB, "v6.1.0")

DESCRIPTION = """Looses connection to the server."""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> insert into t_3nyn_c values (52, 91, 89.98, 47, 27, 0, '4nj9nb', 91);
        conn_0> delete from t_3nyn_c where (t_3nyn_c.wkey % t_3nyn_c.c_9kited) is NULL;
        """,
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> start transaction;
        conn_0> insert into t_3nyn_c values (52, 91, 89.98, 47, 27, 0, '4nj9nb', 91);
        conn_0> delete from t_3nyn_c where (t_3nyn_c.wkey % t_3nyn_c.c_9kited) is NULL;
        conn_0> commit;
        """,
    ]
