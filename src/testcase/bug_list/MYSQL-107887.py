import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

ORIGINAL_ISOLATION_LEVEL = IsolationLevel.READ_COMMITTED
BUG_ID = "MYSQL-107887"
LINK = "https://bugs.mysql.com/bug.php?id=107887"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MYSQL, "8.0.23"
)

DESCRIPTION = "The two returned tables should be equal."


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
    conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
    conn_1> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};

    conn_0> START TRANSACTION;
    conn_1> START TRANSACTION;
    conn_1> insert into t_cqieb values
    (141, 210000, 41.72, 56, 76, null, 32.6, null, 11, 12, 74),
    (141, 211000, 41.73, 87, 84, null, 11.2, 79.63, null, 58, 4),
    (141, 212000, 41.73, 87, 84, null, 11.2, 79.63, null, 58, 4),
    (141, 213000, null, null, null, null, null, null, null, null, null);
    conn_1> ROLLBACK;
    conn_0> update t_cqieb set
    wkey = 116 
    where t_cqieb.c_rejdnc not in (
    select
        subq_0.c0 as c0
        from
        (select
                ref_8.c_myvn4d as c0
            from
                t_b9lvzc as ref_8
            where ref_8.c_lszpl < ref_8.c_t41kdd) as subq_0
        where subq_0.c0 < (  
        select
                ref_9.c_1xf8oc as c0
            from
                (t_b9lvzc as ref_9
                left outer join t_b9lvzc as ref_10
                on (ref_9.c_t41kdd = ref_10.wkey ))
            where ref_9.c_t41kdd <> ref_10.pkey)
        order by c0 asc);
    conn_0> select * from t_cqieb where wkey = 116;
    conn_0> COMMIT;
    """,
        f"""
    conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
    conn_0> START TRANSACTION;
    conn_0> update t_cqieb set
    wkey = 116 
    where t_cqieb.c_rejdnc not in (
    select
        subq_0.c0 as c0
        from
        (select
                ref_8.c_myvn4d as c0
            from
                t_b9lvzc as ref_8
            where ref_8.c_lszpl < ref_8.c_t41kdd) as subq_0
        where subq_0.c0 < (  
        select
                ref_9.c_1xf8oc as c0
            from
                (t_b9lvzc as ref_9
                left outer join t_b9lvzc as ref_10
                on (ref_9.c_t41kdd = ref_10.wkey ))
            where ref_9.c_t41kdd <> ref_10.pkey)
        order by c0 asc);
    conn_0> select * from t_cqieb where wkey = 116;
    conn_0> COMMIT;
    """,
    ]
