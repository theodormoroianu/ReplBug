import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-30633"
LINK = "https://github.com/pingcap/tidb/issues/30633"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(db_config.DatabaseType.TIDB, "v5.4.0")

DESCRIPTION = """Looses connection to the server."""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> WITH
            cte_0 AS (select
                1 as c13
            from
                ((t_jzzvlc as ref_0
                inner join ((t_j2g80b as ref_1
                    cross join t_k6hp_ as ref_2)
                    inner join t_k6hp_ as ref_3
                        on (ref_2.c0 = ref_3.c0 ))
                    on (ref_0.c_ulqme = ref_1.c_u2kce))
                    cross join t_jzzvlc as ref_4))
            select
                ref_15.c13 as c0
            from
                cte_0 as ref_15
            ;
        """,
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> start transaction;
        conn_0> WITH
            cte_0 AS (select
                1 as c13
            from
                ((t_jzzvlc as ref_0
                inner join ((t_j2g80b as ref_1
                    cross join t_k6hp_ as ref_2)
                    inner join t_k6hp_ as ref_3
                        on (ref_2.c0 = ref_3.c0 ))
                    on (ref_0.c_ulqme = ref_1.c_u2kce))
                    cross join t_jzzvlc as ref_4))
            select
                ref_15.c13 as c0
            from
                cte_0 as ref_15
            ;
        conn_0> commit;
        """,
    ]
