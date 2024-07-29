import database.config as db_config
from testcase.helpers import IsolationLevel

ORIGINAL_ISOLATION_LEVEL = IsolationLevel.REPEATABLE_READ
BUG_ID = "MYSQL-114389"
LINK = "https://bugs.mysql.com/bug.php?id=114389"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MYSQL, "8.0.12"
)

SETUP_SQL_SCRIPT = """
CREATE TABLE t(pkId integer, a INT PRIMARY KEY, b INT, c INT);
ALTER TABLE t ADD INDEX t_index(a);
INSERT INTO t (pkId,a,b,c) values (8,44,1,2);
"""

DESCRIPTION = "Last SELECT should see no data (because of the update right before it)."


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        
        conn_0> BEGIN;

        conn_1> BEGIN;
        conn_1> UPDATE t SET b = 222, c = 333;
        conn_1> COMMIT;

        conn_2> BEGIN;
        conn_2> SELECT pkId, b, c FROM t;

        conn_0> UPDATE t SET a = 40 WHERE a = 44;
        conn_0> COMMIT;
        
        conn_2> UPDATE t SET b = 888, c = 999;
        conn_2> SELECT pkId, b, c FROM t where b = 854 or c = 333 order by b;
        conn_2> COMMIT;
        """
    ]
