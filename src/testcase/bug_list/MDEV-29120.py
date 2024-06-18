import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

# https://github.com/JZuming/TxCheck/blob/main/docs/mariadb_bugs.md

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "MDEV-29120"
LINK = "https://jira.mariadb.org/browse/MDEV-29120"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MARIADB, "10.8.3", False
)


def get_description(isolation_level: IsolationLevel):
    return f"""
Link:                     https://jira.mariadb.org/browse/MDEV-29120
Original isolation level: REPETABLE READ
Tested isolation level:   {isolation_level}
"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
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
    ]
