import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "MDEV-21516"
LINK = "https://jira.mariadb.org/browse/MDEV-21516"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MARIADB, "10.6.0-debug"
)
SETUP_SQL_SCRIPT = """
"""

DESCRIPTION = "MariaDB crashes."


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};

        conn_0> SET @save_limit = @@innodb_limit_optimistic_insert_debug;

        conn_0> create table t1(a serial, b geometry not null, spatial index(b)) engine=innodb;
        conn_0> SET GLOBAL innodb_limit_optimistic_insert_debug = 2;
        conn_0> begin;
        conn_0> insert into t1 select seq, Point(1,1) from seq_1_to_5;
        conn_0> rollback;

        conn_0> check table t1;
        conn_0> drop table t1;

        conn_0> SET GLOBAL innodb_limit_optimistic_insert_debug = @save_limit;
    """,
    ]
