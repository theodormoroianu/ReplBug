import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-30361"
LINK = "https://github.com/pingcap/tidb/issues/30361"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(db_config.DatabaseType.TIDB, "v5.4.0")

DESCRIPTION = "The two resulting tables are different."


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> start transaction;
        conn_1> start transaction;
        conn_0> select ref_14.c_qpjzzd as c1 from t_q_zw9c as ref_14 order by c1 desc;
        conn_0> delete from t_q_zw9c;
        conn_0> commit;
        conn_1> select ref_14.c_qpjzzd as c1 from t_q_zw9c as ref_14 order by c1 desc;
        conn_1> commit; 
        """,
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> start transaction;
        conn_1> start transaction;
        conn_0> select ref_14.c_qpjzzd as c1 from t_q_zw9c as ref_14;
        conn_0> delete from t_q_zw9c;
        conn_0> commit;
        conn_1> select ref_14.c_qpjzzd as c1 from t_q_zw9c as ref_14;
        conn_1> commit; 
        """,
    ]
