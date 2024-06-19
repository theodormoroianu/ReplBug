import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

# taken from  https://github.com/JZuming/TxCheck/blob/main/docs/tidb_bugs.md

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-38170"
LINK = "https://github.com/pingcap/tidb/issues/38170"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(db_config.DatabaseType.TIDB, "v6.3.0")

description = """It doesn't always output the same number of items."""


def get_scenarios(isolation_level: IsolationLevel):
    instruction = """
    conn_0> WITH 
    cte_0 AS (select distinct 
        ref_0.wkey as c0, 
        ref_0.pkey as c1, 
        ref_0.c_xhsndb as c2
    from 
        t_dnmxh as ref_0
    where (1 <= ( 
        select  
                ref_1.pkey not in (
                        select  
                                ref_5.wkey as c0
                            from 
                                t_dnmxh as ref_5
                            where (ref_5.wkey < ( 
                                select  
                                    ref_6.pkey as c0
                                    from 
                                    t_cqmg3b as ref_6
                                    where 88 between 96 and 76)) 
                            ) as c0
            from 
                (t_cqmg3b as ref_1
                left outer join t_dnmxh as ref_2
                on (ref_1.wkey = ref_2.wkey ))
            where ref_0.c_xhsndb is NULL
            union
            select  
                33 <= 91 as c0
            from 
                t_cqmg3b as ref_8
            ))), 
    cte_1 AS (select  
        ref_9.wkey as c0, 
        ref_9.pkey as c1, 
        ref_9.c_anpf_c as c2, 
        ref_9.c_b_fp_c as c3, 
        ref_9.c_ndccfb as c4, 
        ref_9.c_8rswc as c5
    from 
        t_cqmg3b as ref_9)
    select  
        ref_10.c0 as c0, 
        ref_10.c1 as c1, 
        ref_10.c2 as c2
    from 
        cte_0 as ref_10
    where case when 56 < 50 then case when 100 in (
            select distinct 
                ref_11.c4 as c0
                from 
                cte_1 as ref_11
                where (ref_11.c4 > ( 
                    select  
                        ref_13.pkey as c0
                        from 
                        t_dnmxh as ref_13
                        where (ref_13.wkey > ( 
                            select distinct 
                                ref_11.c1 as c0
                            from 
                                cte_0 as ref_14)) 
                        )) 
                or (1 = 1)) then null else null end
            else '7mxv6' end
        not like 'ki4%vc';
    """
    return (
        [
            f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> START TRANSACTION;
        {instruction}
        conn_0> COMMIT;
        """,
        ]
        * 5
    )
