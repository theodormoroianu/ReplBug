import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

# taken from  https://github.com/JZuming/TxCheck/blob/main/docs/tidb_bugs.md

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-36928"
LINK = "https://github.com/pingcap/tidb/issues/36928"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(db_config.DatabaseType.TIDB, "v6.1.0")

description = """The two tests give a different result."""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> delete from t_pjxdzd;
        conn_0> select * from t_kkdrvd
        where LOG(t_kkdrvd.c_4wxknd) not in (
          select 1 from t_pjxdzd as ref_0
            where 10 between (null % CRC32('lcc8id' || 'n_5gbd'))
                      and case when ref_0.wkey is NULL then 49 else (49 / 45) end);
        conn_0> update t_kkdrvd set
          wkey = 92
        where LOG(t_kkdrvd.c_4wxknd) not in (
          select 1 from t_pjxdzd as ref_0
            where 10 between (null % CRC32('lcc8id' || 'n_5gbd'))
                      and case when ref_0.wkey is NULL then 49 else (49 / 45) end);
        """,
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> BEGIN OPTIMISTIC;
        conn_0> delete from t_pjxdzd;
        conn_0> select * from t_kkdrvd
        where LOG(t_kkdrvd.c_4wxknd) not in (
        select 1 from t_pjxdzd as ref_0
            where 10 between (null % CRC32('lcc8id' || 'n_5gbd'))
                    and case when ref_0.wkey is NULL then 49 else (49 / 45) end);
        conn_0> update t_kkdrvd set
        wkey = 92
        where LOG(t_kkdrvd.c_4wxknd) not in (
        select 1 from t_pjxdzd as ref_0
            where 10 between (null % CRC32('lcc8id' || 'n_5gbd'))
                    and case when ref_0.wkey is NULL then 49 else (49 / 45) end);
        conn_0> COMMIT;
        """,
    ]
