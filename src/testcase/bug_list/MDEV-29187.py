import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "MDEV-29187"
LINK = "https://jira.mariadb.org/browse/MDEV-29187"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MARIADB, "10.7.3"
)

DESCRIPTION = "The TID of the transaction rolled back is off by one."

SETUP_SQL_SCRIPT = """
create table t1 (id int primary key, f1 int);
insert into t1 values (1,1), (2,2);
"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> begin;
        conn_0> update t1 set f1 = 3 where id = 1; 
        conn_1> begin;
        conn_1> update t1 set f1 = 4 where id = 2;
        conn_0> update t1 set f1 = 3 where id = 2; 
        conn_1> update t1 set f1 = 5 where id = 1;
        conn_2> show engine innodb status;
        """
    ]
