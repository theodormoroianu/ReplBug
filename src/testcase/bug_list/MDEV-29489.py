import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

# https://github.com/JZuming/TxCheck/blob/main/docs/mariadb_bugs.md

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "MDEV-29489"
LINK = "https://jira.mariadb.org/browse/MDEV-29489"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MARIADB, "10.10.1"
)

DESCRIPTION = "MariaDB crashes."


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
    conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
    conn_1> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
    conn_1> START TRANSACTION;
    conn_0> START TRANSACTION;
    conn_1> update t_yfrkzd set wkey = 80;
    conn_1> delete from t_yfrkzd
        where
        t_yfrkzd.c_n1makd between t_yfrkzd.c_n1makd and t_yfrkzd.wkey;
    conn_0> delete from t_ywo4_b
        where
        t_ywo4_b.c_hlsgr not in (
        select
        ref_0.pkey as c0
        from
        (t_yfrkzd as ref_0
        inner join (select
        ref_1.wkey as c0
        from
        t_yfrkzd as ref_1
        ) as subq_0
        on (ref_0.wkey = subq_0.c0 )));
    conn_1> delete from t_yfrkzd
        where
        (t_yfrkzd.c_aob5e not in (
        select
        ref_1.c_k4lijb as c0
        from
        t_ywo4_b as ref_1));
    conn_1> ROLLBACK;
    conn_0> ROLLBACK;
    """,
    ]
