import context
import testcase.bug as bug
import database.config as db_config
from .helpers import *

#################################################################################################
# Bug reported here: https://jira.mariadb.org/browse/MDEV-29083                                 #
# Taken from here:   https://github.com/JZuming/TxCheck/blob/main/docs/mariadb_bugs.md          #
# Setup:             mysql_bk_5.sql                                                             #
#################################################################################################

ORIGINAL_ISOLATION_LEVEL = IsolationLevel.READ_COMMITTED

description = """
Link:                     https://jira.mariadb.org/browse/MDEV-29083
Original isolation level: READ COMMITTED
Tested isolation level:   %s
"""


def get_bug_runner(isolation_level: IsolationLevel):
    scenario_0 = f"""
    conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
    conn_1> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
    conn_0> START TRANSACTION;
    conn_1> START TRANSACTION;
    conn_1> delete from t_euhshb;
    conn_1> ROLLBACK;
    conn_0> insert into t_7sdcgd values
    (91, 167000, case when exists (
    select *
    from
    (t_euhshb as ref_0
    inner join t_euhshb as ref_1
    on (ref_0.pkey = ref_1.wkey ))
    where ref_1.wkey = (
    select
    ref_0.c_oyg4yd as c0
    from
    t_euhshb as ref_2)
    ) then 1
    else 2 end
    , 96, 71.64, '1c08ld');
    conn_0> select * from t_7sdcgd where wkey = 91;
    conn_0> COMMIT;
    """

    scenario_1 = """
    conn_0> insert into t_7sdcgd values
    (91, 167000, case when exists (
    select *
    from
    (t_euhshb as ref_0
    inner join t_euhshb as ref_1
    on (ref_0.pkey = ref_1.wkey ))
    where ref_1.wkey = (
    select
    ref_0.c_oyg4yd as c0
    from
    t_euhshb as ref_2)
    ) then 1
    else 2 end
    , 96, 71.64, '1c08ld');
    conn_0> select * from t_7sdcgd where wkey = 91;
    """

    setup_sql_script = (
        context.Context.get_context().data_folder_path / "sql" / "mysql_bk_5.sql"
    )
    bug_runner = bug.Bug(
        bug_id=f"29083_{isolation_level.name}",
        description=description % isolation_level.value,
        db_and_type=db_config.DatabaseTypeAndVersion(
            db_config.DatabaseType.MARIADB, "10.8.3"
        ),
        scenarios=[scenario_0, scenario_1],
        setup_sql_script=setup_sql_script,
    )
    return bug_runner


def get_bug_scenarios():
    scenarios = {
        f"bug5_{i.name}": get_bug_runner(i)
        for i in IsolationLevel
        if i != ORIGINAL_ISOLATION_LEVEL
    }
    scenarios["bug5"] = get_bug_runner(ORIGINAL_ISOLATION_LEVEL)
    return scenarios
