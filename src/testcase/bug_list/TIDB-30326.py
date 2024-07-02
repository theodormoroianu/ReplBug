import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-30326"
LINK = "https://github.com/pingcap/tidb/issues/30326"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(db_config.DatabaseType.TIDB, "v5.4.0")


DESCRIPTION = "The server crashes."


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> begin;
        conn_0> WITH
            cte_0 AS (select
                1 as c1,
                (FIRST_VALUE(1) over (partition by subq_0.c0) < 1) as c3,
                (select c4 from t_cpsvpb) as c7,
                1 as c11
            from
                (select
                    ref_0.c_13sfid as c0
                    from
                    t_x7zqmd as ref_0
                    where 0 <> 0) as subq_0)
            select 1
            from
                ((t_037irb as ref_6 cross join cte_0 as ref_7)
                inner join (t_037irb as ref_8 inner join cte_0 as ref_9 on (ref_8.c_nrh3o = ref_9.c11 ))
                on (ref_7.c1 = ref_8.c_j9alg ));
        """,
    ]
