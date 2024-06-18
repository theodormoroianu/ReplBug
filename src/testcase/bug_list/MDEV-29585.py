import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

# https://github.com/JZuming/TxCheck/blob/main/docs/mariadb_bugs.md

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "MDEV-29585"
LINK = "https://jira.mariadb.org/browse/MDEV-29585"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MARIADB, "10.8.3"
)


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
    conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
    conn_0> START TRANSACTION;
    conn_0> CREATE TABLE `t_rry5a` (
        `wkey` int(11) DEFAULT NULL,
        `pkey` int(11) NOT NULL,
        `c_t4jlkc` int(11) DEFAULT NULL,
        `c_a047t` text DEFAULT NULL,
        `c_bhsf6d` double DEFAULT NULL,
        `c_t9_mu` int(11) DEFAULT NULL,
        PRIMARY KEY (`pkey`)
        );
    conn_0> insert into t_rry5a (wkey, pkey, c_t4jlkc, c_bhsf6d) values
        (1052, 5800000, 1, 100);
    conn_0> WITH
        cte_0 AS (select
            ref_0.wkey as c0,
            ref_0.pkey as c1,
            ref_0.c_t4jlkc as c2,
            ref_0.c_a047t as c3,
            ref_0.c_bhsf6d as c4,
            ref_0.c_t9_mu as c5
        from
            t_rry5a as ref_0)
        select
            ref_2.c0 as c0,
            ref_2.c1 as c1,
            ref_2.c2 as c2,
            ref_2.c3 as c3,
            ref_2.c4 as c4,
            ref_2.c5 as c5
        from
            cte_0 as ref_2
        where exists (
            select
                    FIRST_VALUE(ref_2.c4) over (partition by ref_2.c1) as c0
            );
    conn_0> 
        WITH
        cte_0 AS (select
            ref_0.wkey as c0,
            ref_0.pkey as c1,
            ref_0.c_t4jlkc as c2,
            ref_0.c_a047t as c3,
            ref_0.c_bhsf6d as c4,
            ref_0.c_t9_mu as c5
        from
            t_rry5a as ref_0)
        select
            ref_2.c0 as c0,
            ref_2.c1 as c1,
            ref_2.c2 as c2,
            ref_2.c3 as c3,
            ref_2.c4 as c4,
            ref_2.c5 as c5
        from
            cte_0 as ref_2
        where exists (
            select
                    FIRST_VALUE(ref_2.c4) over (partition by ref_2.c1) as c0
            ) or 17 <> 0;
    conn_0> COMMIT;
    """,
    ]
