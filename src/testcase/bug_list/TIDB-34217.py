import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

# taken from  https://github.com/JZuming/TxCheck/blob/main/docs/tidb_bugs.md

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-34217"
LINK = "https://github.com/pingcap/tidb/issues/34217"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(db_config.DatabaseType.TIDB, "v6.1.0")

DESCRIPTION = """Looses connection to the server."""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> update t__ti1_d set
                wkey = 37
                where (case when 0 <> 0 then abs(
                        case when t__ti1_d.wkey > (
                                select
                                    t__ti1_d.c_azzk8c as c0
                                from
                                    t_yexe_d as ref_0
                                where 10 >= (select count(c_vqpj9c) from t_yexe_d)
                                window w_80pxn as ( partition by t__ti1_d.pkey order by ref_0.c_px23g desc)
                                order by c0 desc
                        ) then 1 else 20 end
                    ) else 1 end * 53) > 1; 

        conn_0> select * from t__ti1_d;
        """,
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> START TRANSACTION;
        conn_0> update t__ti1_d set
                wkey = 37
                where (case when 0 <> 0 then abs(
                        case when t__ti1_d.wkey > (
                                select
                                    t__ti1_d.c_azzk8c as c0
                                from
                                    t_yexe_d as ref_0
                                where 10 >= (select count(c_vqpj9c) from t_yexe_d)
                                window w_80pxn as ( partition by t__ti1_d.pkey order by ref_0.c_px23g desc)
                                order by c0 desc
                        ) then 1 else 20 end
                    ) else 1 end * 53) > 1; 

        conn_0> select * from t__ti1_d;
        conn_0> COMMIT;
        """,
    ]
