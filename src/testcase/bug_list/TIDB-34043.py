import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

# taken from  https://github.com/JZuming/TxCheck/blob/main/docs/tidb_bugs.md

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-34043"
LINK = "https://github.com/pingcap/tidb/issues/34043"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(db_config.DatabaseType.TIDB, "v6.1.0")

description = """Looses connection to the server."""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> start transaction;
        conn_0> select
            ref_0.c_lmpznc as c5
            from
            t_zb_m5 as ref_0
            where (ref_0.c_mu4_e in (
                    select distinct
                        ref_2.pkey > ref_2.c_c23g6c as c0
                        from
                        (t_wzgyvd as ref_2
                            cross join t_wzgyvd as ref_3
                            )
                        where EXISTS (
                                select  
                                    ref_4.c__gkztd as c0,
                                    ref_2.pkey as c1
                                from 
                                    t_wzgyvd as ref_4
                                where EXISTS (
                                    select  
                                        ref_5.c_pqvmnd as c10
                                    from
                                        t_wzgyvd as ref_5
                                    where (ref_5.c_hysvi < (
                                            select
                                                ref_3.c_oswlic as c0
                                                from
                                                t_wzgyvd as ref_6
                                                where ref_4.c_dm4wqb in (
                                                select
                                                        'o5sq1c' as c0
                                                    from
                                                        t_zb_m5 as ref_7
                                                    where ref_7.wkey = ref_7.pkey
                                                    )
                                            ) or ref_2.c_c23g6c < ref_4.wkey)))
                    ));
        conn_0> commit;
        """,
    ]
