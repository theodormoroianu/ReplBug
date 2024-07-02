import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

# taken from  https://github.com/JZuming/TxCheck/blob/main/docs/tidb_bugs.md

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-38150"
LINK = "https://github.com/pingcap/tidb/issues/38150"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(db_config.DatabaseType.TIDB, "v6.3.0")

DESCRIPTION = """The first select should return the same number of rows as the second select, but it does not."""


def get_scenarios(isolation_level: IsolationLevel):
    op = """
    conn_0> select
            t_cp0sl.wkey as c0,
            t_cp0sl.pkey as c1,
            t_cp0sl.c_1_kgbc as c2,
            t_cp0sl.c_dw8ly as c3
            from
            t_cp0sl
            where t_cp0sl.c_1_kgbc not in (
                select
                    subq_0.c0 as c0
                    from
                    (select
                            ref_0.c_p5i5kc as c0,
                            ref_0.wkey as c1
                        from
                            t_d0c_g as ref_0
                        window w_9grx2d as ( partition by ref_0.pkey order by ref_0.c_eephud desc)) as subq_0
                    where 77 not in (
                    select
                        1 as c0
                        from
                        t_d0c_g as ref_1));

        conn_0> update t_cp0sl set
            wkey = 59
            where t_cp0sl.c_1_kgbc not in (
                select
                    subq_0.c0 as c0
                    from
                    (select
                            ref_0.c_p5i5kc as c0,
                            ref_0.wkey as c1
                        from
                            t_d0c_g as ref_0
                        window w_9grx2d as ( partition by ref_0.pkey order by ref_0.c_eephud desc)) as subq_0
                    where 77 not in (
                    select
                        1 as c0
                        from
                        t_d0c_g as ref_1));
        
        conn_0> select
        t_cp0sl.wkey as c0,
        t_cp0sl.pkey as c1,
        t_cp0sl.c_1_kgbc as c2,
        t_cp0sl.c_dw8ly as c3
        from
        t_cp0sl
        where wkey = 59;
    """
    return [
        op,
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> START TRANSACTION;
        {op}
        conn_0> COMMIT;
        """,
    ]
