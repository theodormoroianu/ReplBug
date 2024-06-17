import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

# https://github.com/JZuming/TxCheck/blob/main/docs/mariadb_bugs.md

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "MDEV-29232"
LINK = "https://jira.mariadb.org/browse/MDEV-29232"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MARIADB_DEBUG, "10.8.3"
)


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
    conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
    conn_0> START TRANSACTION;
    conn_0> select case when case when PI() in (
          select  
              85.45 as c0
            from 
              t_g2kscc as ref_0
            where (ref_0.pkey <= ( 
                  select  
                      ref_1.wkey as c0
                    from 
                      t_g2kscc as ref_1)) 
              ) then 60 else 10 end
         not in (
      select  
            ref_4.c_tlumg as c0
          from 
            t_d0pt_c as ref_4
        ) then 65.4 else 44.96 end;
    """
    ]
