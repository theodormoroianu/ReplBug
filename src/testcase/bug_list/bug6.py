import context
import testcase.bug as bug
import database.config as db_config
from .helpers import *

#################################################################################################
# Bug reported here: https://jira.mariadb.org/browse/MDEV-29120                                 #
# Taken from here:   https://github.com/JZuming/TxCheck/blob/main/docs/mariadb_bugs.md          #
# Setup:             mysql_bk_6.sql                                                             #
#################################################################################################

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
bug_id = "MDEV-29120"

description = """
Link:                     https://jira.mariadb.org/browse/MDEV-29120
Original isolation level: REPETABLE READ
Tested isolation level:   %s
"""


def get_bug_runner(isolation_level: IsolationLevel):
    scenario_0 = f"""
    conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
    conn_1> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};

    conn_0> START TRANSACTION;
    conn_1> START TRANSACTION;

    conn_1> insert into t_yynypc (wkey, pkey, c_acfajc) values
    (89, 188000, 40),
    (89, 189000, 5),
    (89, 190000, 49),
    (89, 191000, 39),
    (89, 192000, 50),
    (97, 227000, 86),
    (97, 228000, 19),
    (97, 229000, 3),
    (97, 230000, 9);

    conn_0> delete from t_qrsdpb where
        exists (
        select
        ref_0.c_bkmkf as c2
        from
        t_zefkic as ref_0
        where t_qrsdpb.c_hhsy0b not in (
        select
        ref_3.wkey as c0
        from
        (t_yynypc as ref_2
        left outer join t_zefkic as ref_3
        on (ref_2.wkey = ref_3.wkey ))
        where ref_3.pkey >= ref_2.wkey));

    conn_1> update t_zefkic set wkey = 99;

    conn_0> ROLLBACK;

    conn_1> ROLLBACK;
    """

    setup_sql_script = (
        context.Context.get_context().data_folder_path / "sql" / "mysql_bk_6.sql"
    )
    bug_runner = bug.Bug(
        bug_id=f"{bug_id}_{isolation_level.name}",
        description=description % isolation_level.value,
        db_and_type=db_config.DatabaseTypeAndVersion(
            db_config.DatabaseType.MARIADB_DEBUG, "10.8.3"
        ),
        scenarios=[scenario_0],
        setup_sql_script=setup_sql_script,
    )
    return bug_runner


def get_bug_scenarios():
    scenarios = {
        f"bug6_{i.name}": get_bug_runner(i)
        for i in IsolationLevel
        if i != ORIGINAL_ISOLATION_LEVEL
    }
    scenarios["bug6"] = get_bug_runner(ORIGINAL_ISOLATION_LEVEL)
    return scenarios
