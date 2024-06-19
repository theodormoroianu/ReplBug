import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

# taken from  https://github.com/JZuming/TxCheck/blob/main/docs/tidb_bugs.md

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-38167"
LINK = "https://github.com/pingcap/tidb/issues/38167"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(db_config.DatabaseType.TIDB, "v6.3.0")

DESCRIPTION = """The database crashes."""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> START TRANSACTION;
        conn_0> update t_emmxx set
            wkey = 308
            where 1 <= (case when t_emmxx.c_oh0c3 is not NULL then 28 else case when exists (
                    select
                        ref_2.c_sq6jnb as c3
                        from
                        t_jpylcc as ref_2
                        ) then (
                        select
                            86 as c0
                            from
                            t_jpylcc as ref_3
                            where (t_emmxx.c_ayjy0c in (
                                select
                                    ref_5.wkey as c0
                                    from
                                    t_jpylcc as ref_5))
                            or (t_emmxx.c_ayjy0c < (
                                select
                                    t_emmxx.c_pmt6sc as c0
                                    from
                                    t_jpylcc as ref_11))
                        ) else 1 end
                    end
                );

        conn_0> select 1;
        conn_0> COMMIT;
        """,
    ]
