import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-30626"
LINK = "https://github.com/pingcap/tidb/issues/30626"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(db_config.DatabaseType.TIDB, "v5.4.0")

description = """Looses connection to the server."""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> start transaction;
        conn_0> insert into t_cvooz values
        (81, case when trim('p9u_9c') <= (
            select
                'vnsgnd' as c0
            from
                (t_ljlaub as ref_3
                cross join t_ljlaub as ref_4
                )
            ) then 87 else 26 end
        , 44.67, 60, null);
        conn_0> commit;
        """,
    ]
