import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-30412"
LINK = "https://github.com/pingcap/tidb/issues/30412"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(db_config.DatabaseType.TIDB, "v5.4.0")

description = """In the second case, the insert fails, even though it should not."""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> delete from t_xkzvqb;
        conn_0> insert into t_rxrf9c values
            (41, case when EXISTS (
                select distinct
                    ref_0.c2 as c2
                from
                    t_f32hfd as ref_0
                ) then 1 else 0 end
            , 74.4, 31);
        conn_0> select * from t_rxrf9c; 
        """,
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> start transaction;
        conn_0> delete from t_xkzvqb;
        conn_0> insert into t_rxrf9c values
            (41, case when EXISTS (
                select distinct
                    ref_0.c2 as c2
                from
                    t_f32hfd as ref_0
                ) then 1 else 0 end
            , 74.4, 31); 
        conn_0> commit;
        conn_0> select * from t_rxrf9c; 
        """,
    ]
