import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "MDEV-16675"
LINK = "https://jira.mariadb.org/browse/MDEV-16675"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MARIADB, "10.3.8-debug"
)
SETUP_SQL_SCRIPT = """
CREATE TABLE t1(id INT PRIMARY KEY, a INT, b CHAR(1), UNIQUE KEY u(a,b)) ENGINE=InnoDB;
"""

DESCRIPTION = "In this test, there is no conflict, and the DELETE statement should not convert the implicit lock into an explicit one. But, the function lock_rec_convert_impl_to_expl_for_trx() is being invoked during the test."


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> BEGIN;
        conn_0> INSERT INTO t1 VALUES(1,1,'a'),(2,9999,'b'),(3,10000,'c'),(4,4,'d');
        conn_0> COMMIT;
    """,
    ]
