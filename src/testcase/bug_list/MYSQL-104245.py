import database.config as db_config
from testcase.helpers import IsolationLevel

ORIGINAL_ISOLATION_LEVEL = IsolationLevel.REPEATABLE_READ
BUG_ID = "MYSQL-104245"
LINK = "https://bugs.mysql.com/bug.php?id=104245"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MYSQL, "5.7.34"
)

SETUP_SQL_SCRIPT = """
CREATE TABLE `t1` (
  `c1` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `c2` bigint(20) NOT NULL,
  `c3` bigint(20) NOT NULL,
  `c4` bigint(20) NOT NULL,
  `c5` bigint(20) NOT NULL,
  PRIMARY KEY (`c1`),
  UNIQUE KEY `UNIQUE_KEY` (`c2`,`c3`,`c4`)
) ENGINE=InnoDB ;
INSERT IGNORE INTO t1 (c2, c3, c4, c5) values (1,1,1,1);
"""

DESCRIPTION = "There are 10 row locks despite only having 5 items in the table."


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
    conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
    conn_0> START TRANSACTION;
    conn_0> INSERT IGNORE INTO t1 (c2, c3, c4, c5) values (1,1,1,1),(1,1,1,1),(1,1,1,1),(1,1,1,1),(1,1,1,1);
    conn_0> SHOW ENGINE INNODB STATUS;
    conn_0> SELECT * FROM t1;
    conn_0> COMMIT;
    """,
    ]
