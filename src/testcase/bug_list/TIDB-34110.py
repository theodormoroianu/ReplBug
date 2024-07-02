import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

# taken from  https://github.com/JZuming/TxCheck/blob/main/docs/tidb_bugs.md

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-34110"
LINK = "https://github.com/pingcap/tidb/issues/34110"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(db_config.DatabaseType.TIDB, "v6.1.0")

DESCRIPTION = (
    """Rollback not handled properly, the two scenarios should give the same result"""
)


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_1> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_1> BEGIN OPTIMISTIC;
        conn_0> BEGIN OPTIMISTIC;
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
        """,
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> BEGIN OPTIMISTIC;
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
        """,
    ]
