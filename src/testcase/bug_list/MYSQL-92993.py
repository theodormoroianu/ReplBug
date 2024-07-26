import database.config as db_config
from testcase.helpers import IsolationLevel

ORIGINAL_ISOLATION_LEVEL = IsolationLevel.REPEATABLE_READ
BUG_ID = "MYSQL-92993"
LINK = "https://bugs.mysql.com/bug.php?id=92993"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MYSQL, "8.0.13-debug"
)

SETUP_SQL_SCRIPT = """
"""

DESCRIPTION = "Running 'xa rollback' makes the database crash."

CREATE_NEW_SERVER_FOR_TESTCASE = True


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> SET GLOBAL general_log=ON;
        conn_0> create table t1(a1 int)partition by range (a1) (partition p0 values less than (3),partition p1 values less than (6),partition p2 values less than (9));
        conn_0> drop table mysql.general_log;
        conn_0> xa start 'test1';
        conn_0> INSERT INTO t1 VALUES();
        conn_0> XA END 'test1';
        conn_0> XA PREPARE 'test1';
        conn_0> SET @@global.log_output='TABLE';
        conn_0> xa rollback 'tx1';
        """,
    ]
