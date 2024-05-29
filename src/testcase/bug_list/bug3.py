import context
import testcase.bug as bug
import database.config as db_config
from .helpers import *


#################################################################################################
# Bug reported here: https://bugs.mysql.com/bug.php?id=108528                                   #
# Taken from here:   https://github.com/JZuming/TxCheck/blob/main/docs/mysql_bugs.md            #
# Setup:             mysql_bk_3.sql                                                             #
#################################################################################################

ORIGINAL_ISOLATION_LEVEL = IsolationLevel.REPEATABLE_READ

description = """
Link:                     https://bugs.mysql.com/bug.php?id=108528
Original isolation level: REPEATABLE READ
Tested isolation level:   %s
"""

def get_bug_runner(isolation_level: IsolationLevel):
    # default is repetable reads
    scenario_0 = f"""
    T0> SET SESSION TRANSACTION ISOLATION LEVEL {isolation_level.value};
    T1> SET SESSION TRANSACTION ISOLATION LEVEL {isolation_level.value};

    T1> START TRANSACTION;
    T1> update t_g6ckkb set wkey = 162;
    T0> START TRANSACTION;
    T0> select * from t_g6ckkb;
    T1> COMMIT;
    T0> select * from t_rpjlsd where t_rpjlsd.c_pfd8ab <= (select min(wkey) from t_g6ckkb); 
    T0> update t_rpjlsd set wkey = 63 where t_rpjlsd.c_pfd8ab <= (select min(wkey) from t_g6ckkb);
    T0> select * from t_rpjlsd where wkey = 63;
    T0> COMMIT;
    """
    scenario_0 = scenario_0.replace("T0>", "conn_0>")
    scenario_0 = scenario_0.replace("T1>", "conn_1>")

    setup_sql_script = context.Context.get_context().data_folder_path / "sql" / "mysql_bk_3.sql"
    bug_runner = bug.Bug(
        bug_id=f"108528 - {isolation_level.value}",
        description=description % isolation_level.value,
        db_and_type=db_config.DatabaseTypeAndVersion(db_config.DatabaseType.MYSQL, "8.0.23"),
        scenarios=[scenario_0],
        setup_sql_script=setup_sql_script
    )
    return bug_runner

def get_bug_scenarios():
    scenarios = {
        f"bug3_{i.name}": get_bug_runner(i) for i in IsolationLevel
        if i != ORIGINAL_ISOLATION_LEVEL
    }
    scenarios["bug3"] = get_bug_runner(ORIGINAL_ISOLATION_LEVEL)
    return scenarios
