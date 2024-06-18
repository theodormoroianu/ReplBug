import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

# https://github.com/JZuming/TxCheck/blob/main/docs/mariadb_bugs.md

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "MDEV-29123"
LINK = "https://jira.mariadb.org/browse/MDEV-29123"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MARIADB, "10.8.3"
)


def get_description(isolation_level: IsolationLevel):
    return f"""
Link:                     https://jira.mariadb.org/browse/MDEV-29123
Original isolation level: REPETABLE READ
Tested isolation level:   {isolation_level}
"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
    conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
    conn_1> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
    conn_1> START TRANSACTION;

    conn_0> START TRANSACTION;

    conn_1> insert into t_4rbssc (wkey, pkey, c_qrgwb, c_8u7ipc, c_mqgwfb, c_7j_zjb) values
    (225, 489000, null, 11.49, 89, 63);

    conn_1> ROLLBACK;

    conn_0> select *
    from
    t_4rbssc
    where t_4rbssc.wkey = 4 and t_4rbssc.c_sbxs3c not in (
    select
    count(ref_0.c_baxlp) over (partition by ref_0.c_lba4ac order by ref_0.c_baxlp) as c0
    from
    t__w2gab as ref_0);

    conn_0> COMMIT;
    """,
        f"""
    conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};

    conn_0> START TRANSACTION;

    conn_0> select *
    from
    t_4rbssc
    where t_4rbssc.wkey = 4 and t_4rbssc.c_sbxs3c not in (
    select
    count(ref_0.c_baxlp) over (partition by ref_0.c_lba4ac order by ref_0.c_baxlp) as c0
    from
    t__w2gab as ref_0);

    conn_0> COMMIT;
    """,
    ]
