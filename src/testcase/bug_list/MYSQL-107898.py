import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

#################################################################################################
# Bug reported here: https://bugs.mysql.com/bug.php?id=107898                                   #
# Taken from here:   https://github.com/JZuming/TxCheck/blob/main/docs/mysql_bugs.md            #
# Setup:             mysql_bk_2.sql                                                             #
#################################################################################################

ORIGINAL_ISOLATION_LEVEL = IsolationLevel.READ_COMMITTED
BUG_ID = "MYSQL-107898"
LINK = "https://bugs.mysql.com/bug.php?id=107898"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MYSQL, "8.0.23"
)


DESCRIPTION = "The two returned tables should be equal."


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
    conn_0> SET LOCAL TRANSACTION ISOLATION LEVEL {isolation_level.value}; 
    conn_1> SET LOCAL TRANSACTION ISOLATION LEVEL {isolation_level.value};

    conn_0> START TRANSACTION;
    conn_1> START TRANSACTION; 
    conn_1> delete from t_8fhx8c;
    conn_1> ROLLBACK;

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
    """,
        f"""
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
    """,
    ]
