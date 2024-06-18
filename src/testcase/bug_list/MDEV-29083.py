import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

# https://github.com/JZuming/TxCheck/blob/main/docs/mariadb_bugs.md

ORIGINAL_ISOLATION_LEVEL = IsolationLevel.READ_COMMITTED
BUG_ID = "MDEV-29083"
LINK = "https://jira.mariadb.org/browse/MDEV-29083"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MARIADB, "10.8.3"
)


def get_description(isolation_level: IsolationLevel):
    return f"""
Link:                     https://jira.mariadb.org/browse/MDEV-29083
Original isolation level: READ COMMITTED
Tested isolation level:   {isolation_level}
"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
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
    """,
        f"""
    conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
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
    """,
    ]
