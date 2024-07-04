import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "MDEV-29398"
LINK = "https://jira.mariadb.org/browse/MDEV-29398"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MARIADB, "10.8.3"
)

DESCRIPTION = "Sometimes a different number of results are returned by SELECT."

# Need to restart the server after each request.
KILL_SERVER_AFTER_TESTCASE = False


def get_scenarios(isolation_level: IsolationLevel):
    op = f"""
        conn_0> select  
            t_tu__yc.wkey as c0, 
            t_tu__yc.pkey as c1, 
            t_tu__yc.c_q03lu as c2, 
            t_tu__yc.c_y2uw as c3, 
            t_tu__yc.c_1f41gb as c4, 
            t_tu__yc.c_9daz8b as c5, 
            t_tu__yc.c_joc9kb as c6, 
            t_tu__yc.c_ndt7r as c7, 
            t_tu__yc.c_dsdveb as c8
            from t_tu__yc
                where t_tu__yc.c_q03lu not in (
                    select  
                        PERCENT_RANK() over (partition by ref_0.c_50oqyb,ref_0.c_dbhvpc order by ref_0.c_ss3rcd,ref_0.c_zib3db) as c0
                    from 
                    t_8_h22c as ref_0
                );
    """
    return (
        [
            f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> START TRANSACTION;
        {op * 100}
        conn_0> COMMIT;
        """
        ]
        * 5
    )
