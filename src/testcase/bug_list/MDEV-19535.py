import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "MDEV-19535"
LINK = "https://jira.mariadb.org/browse/MDEV-19535"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MARIADB, "10.4.5"
)
SETUP_SQL_SCRIPT = """
"""

DESCRIPTION = "Setting sql_mode='ORACLE' makes MariaDB miss some required locks."


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> SET sql_mode='';
        conn_0> CREATE TABLE t1 (a INT NOT NULL PRIMARY KEY) engine=innodb;
        conn_0> INSERT INTO t1 VALUES (1);
        conn_0> START TRANSACTION;
        conn_0> SELECT a AS a_con1 FROM t1 INTO @a FOR UPDATE;

        conn_1> SET sql_mode='';
        conn_1> START TRANSACTION;
        conn_1> SELECT a AS a_con2 FROM t1 INTO @a FOR UPDATE;

        conn_0> UPDATE t1 SET a=a+100;
        conn_0> COMMIT;
        
        conn_1> SELECT a AS con2 FROM t1;
        conn_1> COMMIT;
        """,
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> SET sql_mode='ORACLE';
        conn_0> CREATE TABLE t1 (a INT NOT NULL PRIMARY KEY) engine=innodb;
        conn_0> INSERT INTO t1 VALUES (1);
        conn_0> START TRANSACTION;
        conn_0> SELECT a AS a_con1 FROM t1 INTO @a FOR UPDATE;

        conn_1> SET sql_mode='ORACLE';
        conn_1> START TRANSACTION;
        conn_1> SELECT a AS a_con2 FROM t1 INTO @a FOR UPDATE;

        conn_0> UPDATE t1 SET a=a+100;
        conn_0> COMMIT;
        
        conn_1> SELECT a AS con2 FROM t1;
        conn_1> COMMIT;
        """,
    ]
