import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "MDEV-29494"
LINK = "https://jira.mariadb.org/browse/MDEV-29494"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MARIADB, "10.10.1"
)

DESCRIPTION = "The server should crash."

# Need to restart the server after each request.
KILL_SERVER_AFTER_TESTCASE = True


def get_scenarios(isolation_level: IsolationLevel):
    return (
        [
            f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> START TRANSACTION;
        conn_0> select  
                subq_0.c0 as c0
            from 
                (select  
                    ref_0.c_s7edob as c0
                    from 
                    t_dmvax as ref_0
                    where ref_0.c_s7edob not in (
                    select  
                        ref_1.c_wwyiz as c0
                        from 
                        t_dmvax as ref_1)
                    ) as subq_0
            where subq_0.c0 = ( 
                select  
                    ref_3.c_wwyiz as c0
                    from 
                    (t_dmvax as ref_2
                        cross join t_dmvax as ref_3)
                union
                select  
                    ref_4.c_wwyiz as c0
                    from 
                    t_dmvax as ref_4);
        conn_0> COMMIT;
        """
        ]
        * 10
    )
