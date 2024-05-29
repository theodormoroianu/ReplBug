import context
import testcase.bug as bug
import database.config as db_config
from .helpers import *

#################################################################################################
# Bug reported here: https://bugs.mysql.com/bug.php?id=107898                                   #
# Taken from here:   https://github.com/JZuming/TxCheck/blob/main/docs/mysql_bugs.md            #
# Setup:             mysql_bk_2.sql                                                             #
#################################################################################################

ORIGINAL_ISOLATION_LEVEL = IsolationLevel.READ_COMMITTED

description = """
Link:                     https://bugs.mysql.com/bug.php?id=107898
Original isolation level: READ COMMITTED
Tested isolation level:   %s
"""

def get_bug_runner(isolation_level: IsolationLevel):
    scenario_0 = f"""
    conn_0> SET LOCAL TRANSACTION ISOLATION LEVEL {isolation_level.value}; 
    conn_1> SET LOCAL TRANSACTION ISOLATION LEVEL {isolation_level.value};

    conn_0> START TRANSACTION;
    conn_1> START TRANSACTION; 

    delete from t_8fhx8c;

    ROLLBACK;

    conn_0> select *
    from
        t_8fhx8c as ref_1
    where ref_1.c_0byzvd not in (
        select
            nullif(19, 19) as c0
        from
            (select
                ref_2.c_zov5kd as c0
                from
                t_8fhx8c as ref_2
                ) as subq_0
        window w_u6cwrd as (partition by subq_0.c0));

    conn_0> commit;
    """
    scenario_1 = f"""
    conn_0> SET LOCAL TRANSACTION ISOLATION LEVEL {isolation_level.value}; 
    conn_0> START TRANSACTION;
    conn_0> select *
    from
        t_8fhx8c as ref_1
    where ref_1.c_0byzvd not in (
        select
            nullif(19, 19) as c0
        from
            (select
                ref_2.c_zov5kd as c0
                from
                t_8fhx8c as ref_2
                ) as subq_0
        window w_u6cwrd as (partition by subq_0.c0));
    conn_0> COMMIT;
    """
    setup_sql_script = context.Context.get_context().data_folder_path / "sql" / "mysql_bk_2.sql"
    bug_runner = bug.Bug(
        bug_id=f"107898 - {isolation_level.value}",
        description=description % isolation_level.value,
        db_and_type=db_config.DatabaseTypeAndVersion(db_config.DatabaseType.MYSQL, "8.0.23"),
        scenarios=[scenario_0, scenario_1],
        setup_sql_script=setup_sql_script
    )
    return bug_runner

def get_bug_scenarios():
    scenarios = {
        f"bug2_{i.name}": get_bug_runner(i) for i in IsolationLevel
        if i != ORIGINAL_ISOLATION_LEVEL
    }
    scenarios["bug2"] = get_bug_runner(ORIGINAL_ISOLATION_LEVEL)
    return scenarios