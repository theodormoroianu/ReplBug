import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

# taken from  https://github.com/JZuming/TxCheck/blob/main/docs/tidb_bugs.md

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-36903"
LINK = "https://github.com/pingcap/tidb/issues/36903"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(db_config.DatabaseType.TIDB, "v6.1.0")

description = """The two tests give a different result."""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> insert into t_vwvgdc (wkey, pkey, c_rdsfbc) values (155, 228000, 99.50);
        conn_0> select
                  ref_4.pkey as c0
                from
                  t_vwvgdc as ref_4
                where 0 <> 0
              union
              select
                  ref_5.pkey as c0
                from
                  t_vwvgdc as ref_5;
        """,
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> BEGIN OPTIMISTIC;
        conn_0> insert into t_vwvgdc (wkey, pkey, c_rdsfbc) values (155, 228000, 99.50);
        conn_0> select
                        ref_4.pkey as c0
                        from
                        t_vwvgdc as ref_4
                        where 0 <> 0
                union
                select
                        ref_5.pkey as c0
                        from
                        t_vwvgdc as ref_5;
        conn_0> commit;
        """,
    ]
