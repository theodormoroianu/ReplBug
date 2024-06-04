import context
import testcase.bug as bug
import database.config as db_config
from .helpers import *

#################################################################################################
# Bug reported here: https://bugs.mysql.com/bug.php?id=107066                                   #
# Taken from here:   https://github.com/JZuming/TxCheck/blob/main/docs/mysql_bugs.md            #
# Setup:             mysql_bk_1.sql                                                             #
#################################################################################################

ORIGINAL_ISOLATION_LEVEL = IsolationLevel.REPEATABLE_READ

description = """
Link:                     https://bugs.mysql.com/bug.php?id=107066
Original isolation level: REPEATABLE READ
Tested isolation level:   %s
"""


def get_bug_runner(isolation_level: IsolationLevel):
    scenario_0 = f"""
    conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
    conn_1> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
    conn_1> START TRANSACTION;
    conn_0> START TRANSACTION;
    conn_1> insert into t_zcfqb (wkey, pkey, c_dl_pmd, c_avevqc, c_sqqbbd, c_2wz8nc, c_qyxu0, c_slu2bd) values
            (182, 264000, null, 'biiumc', null, 'dwzl6d', 93.90, null);
    conn_0> insert into t_zcfqb (wkey, c_rvm_p, c_avevqc, c_ywxlqb, c_sqqbbd, c_2wz8nc, c_qyxu0, c_ph8nh)
            select
                121 as c0,
                ref_0.c_h1m_zb as c1,
                ref_0.c_gsbzrd as c2,
                ref_0.c_hdnifc as c3,
                (select wkey from t_nvues order by wkey limit 1 offset 5)
                    as c4,
                ref_0.c_h1m_zb as c5,
                ref_0.c_hdnifc as c6,
                ref_0.c_h1m_zb as c7
                from
                t_nvues as ref_0
                where (0 <> 0)
                or (ref_0.wkey is not NULL);
    conn_0> select pkey from t_zcfqb where wkey = 121;
    conn_1> ROLLBACK;
    conn_0> COMMIT;
    """
    scenario_1 = f"""
    conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
    conn_0> START TRANSACTION;
    conn_0> insert into t_zcfqb (wkey, c_rvm_p, c_avevqc, c_ywxlqb, c_sqqbbd, c_2wz8nc, c_qyxu0, c_ph8nh)
            select
                121 as c0,
                ref_0.c_h1m_zb as c1,
                ref_0.c_gsbzrd as c2,
                ref_0.c_hdnifc as c3,
                (select wkey from t_nvues order by wkey limit 1 offset 5)
                    as c4,
                ref_0.c_h1m_zb as c5,
                ref_0.c_hdnifc as c6,
                ref_0.c_h1m_zb as c7
                from
                t_nvues as ref_0
                where (0 <> 0)
                or (ref_0.wkey is not NULL);
    conn_0> select pkey from t_zcfqb where wkey = 121;
    conn_0> COMMIT;
    """
    setup_sql_script = (
        context.Context.get_context().data_folder_path / "sql" / "mysql_bk_1.sql"
    )
    bug_runner = bug.Bug(
        bug_id=f"107066_{isolation_level.name}",
        description=description % (isolation_level.value),
        db_and_type=db_config.DatabaseTypeAndVersion(
            db_config.DatabaseType.MYSQL, "8.0.23"
        ),
        scenarios=[scenario_0, scenario_1],
        setup_sql_script=setup_sql_script,
    )
    return bug_runner


def get_bug_scenarios():
    scenarios = {
        f"bug1_{i.name}": get_bug_runner(i)
        for i in IsolationLevel
        if i != ORIGINAL_ISOLATION_LEVEL
    }
    scenarios["bug1"] = get_bug_runner(ORIGINAL_ISOLATION_LEVEL)
    return scenarios
