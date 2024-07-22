import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "MDEV-25297"
LINK = "https://jira.mariadb.org/browse/MDEV-25297"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MARIADB, "356c1496-debug"
)
SETUP_SQL_SCRIPT = """
CREATE TABLE t1(id INT PRIMARY KEY, a INT, b CHAR(1), UNIQUE KEY u(a,b)) ENGINE=InnoDB;
"""

DESCRIPTION = "A rollback makes the database crash."


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> BEGIN;
        conn_0> SET sql_mode='';
        conn_0> SET unique_checks=0;
        conn_0> SET foreign_key_checks=0;
        conn_0> CREATE TABLE ti (b INT,c INT,e INT,id INT,KEY (b),KEY (e),PRIMARY KEY(id));
        conn_0> INSERT INTO ti VALUES(0,0,0,0);
        conn_0> ALTER TABLE ti CHANGE COLUMN c c BINARY (1);
        conn_0> XA START 'a';
        conn_0> CREATE TEMPORARY TABLE t(a INT);
        conn_0> INSERT INTO t VALUES(1);
        conn_0> SAVEPOINT a3;
        conn_0> CREATE OR REPLACE TEMPORARY TABLE t (a INT,b INT);
        conn_0> INSERT INTO t VALUES(0,0);
        conn_0> INSERT INTO ti VALUES(0,0,0,0);
        conn_0> ROLLBACK TO SAVEPOINT a3;
        conn_0> COMMIT;
        """,
        """
        conn_0> SET sql_mode='';
        conn_0> SET unique_checks=0;
        conn_0> SET foreign_key_checks=0;
        conn_0> CREATE TABLE ti (b INT,c INT,e INT,id INT,KEY (b),KEY (e),PRIMARY KEY(id));
        conn_0> INSERT INTO ti VALUES(0,0,0,0);
        conn_0> ALTER TABLE ti CHANGE COLUMN c c BINARY (1);
        conn_0> XA START 'a';
        conn_0> CREATE TEMPORARY TABLE t(a INT);
        conn_0> INSERT INTO t VALUES(1);
        conn_0> SAVEPOINT a3;
        conn_0> CREATE OR REPLACE TEMPORARY TABLE t (a INT,b INT);
        conn_0> INSERT INTO t VALUES(0,0);
        conn_0> INSERT INTO ti VALUES(0,0,0,0);
        conn_0> ROLLBACK TO SAVEPOINT a3;
        """,
    ]
