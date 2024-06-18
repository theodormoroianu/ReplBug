import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-30587"
LINK = "https://github.com/pingcap/tidb/issues/30587"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.TIDB, "v5.4.0", False
)

description = """Looses connection to the server."""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> start transaction;
        conn_0> insert into t_i9_d6 values (0, 1);
        conn_0> insert into t_yva4kd
        select
            null as c0,
            null as c1,
            null as c2,
            null as c3, 
            case when (
            EXISTS (
                select 1   
                from        
                    t_d_6mnc as ref_10
                where 
                    EXISTS (
                    select 1      
                        from                
                        t_d_6mnc as ref_11
                        where ref_10.c6 not like 'gi5m%b')))
            then null else 61.40 end as c4, 
            null as c5, 
            null as c6, 
            null as c7
        from 
            t_i9_d6 as ref_2
        where (('wntar' || '8kgpd')) like 'p_r0u';
        conn_0> commit;
        """,
    ]
