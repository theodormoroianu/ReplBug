import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "MDEV-18044"
LINK = "https://jira.mariadb.org/browse/MDEV-16675"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MARIADB, "10.3.8-debug"
)
SETUP_SQL_SCRIPT = """
CREATE TABLE t1 (
  id INT NOT NULL AUTO_INCREMENT,
  f varchar(64) DEFAULT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB;
 
INSERT INTO t1 VALUES (1, 'guid 1');
INSERT INTO t1 VALUES (2, 'guid 1');
INSERT INTO t1 VALUES (3, 'guid 2');
 
CREATE PROCEDURE pr1()
BEGIN
  SELECT 1 IN ( SELECT id FROM t1 WHERE f = 'guid 1' );
  SELECT 2;
END;
 
CREATE PROCEDURE pr2()
BEGIN
  IF
    1 IN ( SELECT id FROM t1 WHERE f = 'guid 1' )
  THEN
    SELECT 2;
  END IF;
END;
"""

CREATE_NEW_SERVER_FOR_TESTCASE = True

DESCRIPTION = "Adding an IF statement unecessarily adds a row lock."


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> BEGIN;
        conn_0> CALL pr2();
        conn_1> show engine innodb status;
        conn_0> COMMIT;
        """,
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> BEGIN;
        conn_0> CALL pr1();
        conn_1> show engine innodb status;
        conn_0> COMMIT;
        """,
    ]
