import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

# https://github.com/JZuming/TxCheck/blob/main/docs/mariadb_bugs.md

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "MDEV-29399"
LINK = "https://jira.mariadb.org/browse/MDEV-29399"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MARIADB, "10.8.3", False
)


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
    conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
    conn_0> START TRANSACTION;
    conn_2> START TRANSACTION;
    conn_0> update t_j_eqsc set wkey = 37, c_fm792b = PI();
    conn_0> COMMIT;
    conn_1> START TRANSACTION;
    conn_2> insert into t_j_eqsc (wkey, pkey) values (79, 162000);
    conn_2> ROLLBACK;
    conn_1> select * from t_j_eqsc
    where t_j_eqsc.c_fm792b not in (
    select PI() as c0 from t_xqlwp as ref_0);
    conn_1> COMMIT;
    """,
        f"""
    conn_0> update t_j_eqsc set wkey = 37, c_fm792b = PI();
    conn_0> select * from t_j_eqsc
    where t_j_eqsc.c_fm792b not in (
    select PI() as c0 from t_xqlwp as ref_0);
    """,
    ]
