import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "tidb-29947"
LINK = "https://github.com/pingcap/tidb/issues/29947"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(db_config.DatabaseType.TIDB, "5.2.1")


def get_description(isolation_level: IsolationLevel):
    return f"""
Link:                     {LINK}
Original isolation level: {ORIGINAL_ISOLATION_LEVEL}
Tested isolation level:   {isolation_level}
"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> delete from t_tir89b where t_tir89b.c_3pcik >= t_tir89b.c_sroc_c;
        conn_0> select * from (select count(*) over (partition by ref_0.c_0b6nxb order by ref_0.c_3pcik) as c0 from t_tir89b as ref_0) as subq_0 where subq_0.c0 <> 1;
        """,
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> start transaction;
        conn_0> delete from t_tir89b where t_tir89b.c_3pcik >= t_tir89b.c_sroc_c;
        conn_0> select * from (select count(*) over (partition by ref_0.c_0b6nxb order by ref_0.c_3pcik) as c0 from t_tir89b as ref_0) as subq_0 where subq_0.c0 <> 1;
        conn_0> commit;
        """,
    ]
