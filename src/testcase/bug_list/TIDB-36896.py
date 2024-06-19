import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

# taken from  https://github.com/JZuming/TxCheck/blob/main/docs/tidb_bugs.md

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-36896"
LINK = "https://github.com/pingcap/tidb/issues/36896"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(db_config.DatabaseType.TIDB, "v6.1.0")

DESCRIPTION = """Looses connection to the server."""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> START TRANSACTION;
        conn_0> WITH cte_0 AS (select  
                ref_0.wkey as c0, 
                ref_0.pkey as c1, 
                ref_0.c_rrbxh as c2, 
                ref_0.c_c5cvkb as c3, 
                ref_0.c_ag5ccc as c4, 
                ref_0.c_qo4qvc as c5, 
                ref_0.c_lhs3h as c6, 
                ref_0.c_8dah2b as c7, 
                ref_0.c_eg6xsc as c8
                from 
                t_p7c1bd as ref_0
                )
                select  
                ref_3.wkey as c0, 
                ref_3.pkey as c1, 
                ref_3.c_hzkgf as c2, 
                ref_3.c_si87c as c3
                from 
                t_2el7jd as ref_3
                where ref_3.c_hzkgf <= ( 
                select distinct 
                        ref_6.c_hzkgf as c0
                from 
                        t_2el7jd as ref_6
                where case when 1 < ( 
                        select  
                                ref_6.wkey as c0
                                from 
                                t_2el7jd as ref_7
                                where ref_3.c_si87c > ( 
                                select  
                                        ref_7.c_si87c as c0
                                from 
                                        cte_0 as ref_8
                                where ref_8.c4 not in (
                                        ref_8.c0, ref_8.c3)
                                union
                                select  
                                        ref_6.c_si87c as c0
                                from 
                                        t_2el7jd as ref_9
                                where 27 > 86)
                        union all
                        select  
                                ref_10.c0 as c0
                                from 
                                cte_0 as ref_10
                                where ref_6.pkey < ( 
                                select  
                                        ref_10.c7 as c0
                                from 
                                        t_p7c1bd as ref_11
                                where 0 <> 0
                                window w_5kmydb as ( partition by ref_6.pkey order by ref_3.c_hzkgf asc)
                                union
                                select  
                                        ref_6.wkey as c0
                                from 
                                        cte_0 as ref_12
                                where (select count(c_hzkgf) from t_2el7jd)
                                        <= 32)
                        ) then FIELD(
                        ref_6.c_hzkgf,
                        ref_3.c_hzkgf,
                        ref_6.c_hzkgf,
                        ref_3.c_hzkgf) else 33 end
                        <= 31
                order by c0 asc);
        conn_0> commit;
        """,
    ]
