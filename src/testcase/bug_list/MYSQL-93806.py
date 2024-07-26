import database.config as db_config
from testcase.helpers import IsolationLevel

ORIGINAL_ISOLATION_LEVEL = IsolationLevel.REPEATABLE_READ
BUG_ID = "MYSQL-93806"
LINK = "https://bugs.mysql.com/bug.php?id=93806"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MYSQL, "8.0.12"
)

SETUP_SQL_SCRIPT = """
create table t(id int primary key, a int)engine=innodb;
insert into t values(1,1),(5,5);
"""

DESCRIPTION = "Exclusive range locks are created when using ON DUPLICATE KEY UPDATE (and the update takes place)"


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> begin;
        conn_0> insert into t values(5,5) ON DUPLICATE KEY UPDATE a=a+1;
        
        conn_1> begin;
        conn_1> insert into t values(4, 4);
        
        conn_0> commit;
        conn_1> commit;
        """,
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> begin;
        conn_0> insert into t values(6,6) ON DUPLICATE KEY UPDATE a=a+1;
        
        conn_1> begin;
        conn_1> insert into t values(4, 4);
        
        conn_0> commit;
        conn_1> commit;
        """,
    ]
