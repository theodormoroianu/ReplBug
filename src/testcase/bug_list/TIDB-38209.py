import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

# taken from  https://github.com/JZuming/TxCheck/blob/main/docs/tidb_bugs.md

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-38209"
LINK = "https://github.com/pingcap/tidb/issues/38209"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(db_config.DatabaseType.TIDB, "v6.3.0")

DESCRIPTION = """Error on the first scenario"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> update t_smmcv set wkey = 501;
        conn_0> select *
            from
            t_kb1xh
            where 100 <= case when t_kb1xh.c_bihued = (
                        select distinct
                            '1kkruc' as c0
                            from
                            t_smmcv as ref_13
                        ) then 101 else 57 end;
        """,
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> START TRANSACTION;
        conn_0> update t_smmcv set wkey = 501;
        conn_0> select *
            from
            t_kb1xh
            where 100 <= case when t_kb1xh.c_bihued = (
                        select distinct
                            '1kkruc' as c0
                            from
                            t_smmcv as ref_13
                        ) then 101 else 57 end;
        conn_0> COMMIT;
        """,
    ]
