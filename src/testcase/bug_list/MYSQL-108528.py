import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

ORIGINAL_ISOLATION_LEVEL = IsolationLevel.REPEATABLE_READ
BUG_ID = "MYSQL-108528"
LINK = "https://bugs.mysql.com/bug.php?id=108528"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MYSQL, "8.0.23"
)


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
    conn_0> SET SESSION TRANSACTION ISOLATION LEVEL {isolation_level.value};
    conn_1> SET SESSION TRANSACTION ISOLATION LEVEL {isolation_level.value};

    conn_1> START TRANSACTION;
    conn_1> update t_g6ckkb set wkey = 162;
    conn_0> START TRANSACTION;
    conn_0> select * from t_g6ckkb;
    conn_1> COMMIT;
    conn_0> select * from t_rpjlsd where t_rpjlsd.c_pfd8ab <= (select min(wkey) from t_g6ckkb); 
    conn_0> update t_rpjlsd set wkey = 63 where t_rpjlsd.c_pfd8ab <= (select min(wkey) from t_g6ckkb);
    conn_0> select * from t_rpjlsd where wkey = 63;
    conn_0> COMMIT;
    """
    ]
