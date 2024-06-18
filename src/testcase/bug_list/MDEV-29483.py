import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

# https://github.com/JZuming/TxCheck/blob/main/docs/mariadb_bugs.md

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "MDEV-29483"
LINK = "https://jira.mariadb.org/browse/MDEV-29483"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MARIADB, "10.8.3", False
)


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
    conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
    conn_0> select  
        coalesce(subq_0.c0,
            LAST_VALUE(
              subq_0.c0) over (partition by subq_0.c1 order by subq_0.c2,subq_0.c0)) as c1 
      from 
        (select  
              ref_0.c_0m1mlc as c0, 
              ref_0.c__dk7dc as c1, 
              ref_0.c_evw_ic as c2
            from 
              t_di9mld as ref_0
            ) as subq_0
      where (subq_0.c1 = subq_0.c1) or subq_0.c0 in (
          select distinct 
              ref_3.c_0m1mlc as c0
            from 
              (t_di9mld as ref_2
                cross join t_di9mld as ref_3
                )
            );
    """,
    ]
