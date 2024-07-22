import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "MDEV-24224"
LINK = "https://jira.mariadb.org/browse/MDEV-24224"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MARIADB, "10.5.8"
)
SETUP_SQL_SCRIPT = """
CREATE TABLE `test` (
	ID varchar(40) NOT NULL,
	TEST1 varchar(40) DEFAULT NULL,
	TEST2 varchar(15) NOT NULL,
	TEST3 bigint(20) DEFAULT NULL,
	KEY `IDX_TEST` (TEST1, TEST2, TEST3) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;
 
INSERT INTO test (ID, TEST1, TEST2, TEST3) VALUES ('row_a', 'A.123', 'C', 3);
INSERT INTO test (ID, TEST1, TEST2, TEST3) VALUES ('row_a', 'B.456', 'C', 3);
"""

CREATE_NEW_SERVER_FOR_TESTCASE = True

DESCRIPTION = "Delete statement creates unnecessary gap lock ('gap before rec' present in innodb status)."


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> SET GLOBAL INNODB_STATUS_OUTPUT_LOCKS = 'ON';
        conn_0> BEGIN;
        conn_0> DELETE FROM test WHERE TEST1 = 'A.123a' and TEST2 = 'C' and TEST3 = 3;
        conn_0> SHOW ENGINE INNODB STATUS;
        conn_0> COMMIT;
        conn_0> SELECT * FROM test;
        """,
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> SET GLOBAL INNODB_STATUS_OUTPUT_LOCKS = 'ON';
        conn_0> BEGIN; 
        conn_0> DELETE FROM test WHERE TEST1 = 'G.123a' and TEST2 = 'X' and TEST3 = 31;
        conn_0> SHOW ENGINE INNODB STATUS;
        conn_0> COMMIT;
        conn_0> SELECT * FROM test;
        """,
    ]
