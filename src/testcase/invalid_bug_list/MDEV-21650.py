import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "MDEV-21650"
LINK = "https://jira.mariadb.org/browse/MDEV-21650"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MARIADB, "b615d275-debug"
)
SETUP_SQL_SCRIPT = """
"""

DESCRIPTION = "Setting sql_mode='ORACLE' makes MariaDB miss some required locks."


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""

        conn_0> CREATE TABLE t1 (s DATE, e DATE, PERIOD FOR app(s,e)) ENGINE=InnoDB;
        conn_0> ALTER TABLE t1
            ADD row_start BIGINT UNSIGNED AS ROW START,
            ADD row_end BIGINT UNSIGNED AS ROW END,
            ADD PERIOD FOR SYSTEM_TIME(row_start,row_end),
            WITH SYSTEM VERSIONING,
            ADD PERIOD IF NOT EXISTS FOR app(x,y);


        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        
        conn_0> START TRANSACTION;
        conn_0> INSERT INTO t1 (s,e) VALUES ('2021-07-04','2024-08-18');
        
        conn_1> START TRANSACTION;
        conn_1> INSERT INTO t1 (s,e) VALUES ('2018-06-01','2021-09-15');
        
        conn_0> SELECT * FROM t1 FOR SYSTEM_TIME AS OF NOW();
        
        conn_1> SET innodb_lock_wait_timeout= 1, lock_wait_timeout= 1;
        conn_1> ALTER TABLE xx;
        
        conn_0> DROP TABLE t1;
        """,
    ]
