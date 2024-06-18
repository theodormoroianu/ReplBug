import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-30804"
LINK = "https://github.com/pingcap/tidb/issues/30804"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(db_config.DatabaseType.TIDB, "v5.4.0")

description = """Looses connection to the server."""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> start transaction;
        conn_0> WITH
            cte_0 AS (
            select distinct
                avg(0) over w_ap1h0c as c2
            from
                (select 
                    ref_0.c7 as c3,
                    ref_0.c1 as c10
                    from
                    t_ai_sq as ref_0
                    ) as subq_0
            window w_ap1h0c as ( partition by subq_0.c3 order by (subq_0.c3 - case when subq_0.c10 in (
                        select null as c0) then subq_0.c3 else subq_0.c3 end ) desc))
            select 1;
        conn_0> select 1;
        conn_0> commit;
        """,
    ]
