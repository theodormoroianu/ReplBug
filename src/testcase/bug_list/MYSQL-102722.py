import database.config as db_config
from testcase.helpers import IsolationLevel

ORIGINAL_ISOLATION_LEVEL = IsolationLevel.REPEATABLE_READ
BUG_ID = "MYSQL-102722"
LINK = "https://bugs.mysql.com/bug.php?id=102722"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MYSQL, "8.0.26"
)

SETUP_SQL_SCRIPT = """
create table ts(a int primary key, b int, c int, d int, index(b,c));
insert into ts values(1,1,1,1),(2,2,2,2),(3,3,3,3),(4,4,4,4),(5,5,5,5),(6,6,6,6),(7,7,7,7),(8,8,8,8),(9,9,9,9);
"""

DESCRIPTION = "Locks on secondary indexes are not released even though the secondary indexes are unmatched when index_condition_pushdown=off"


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> SET SESSION TRANSACTION ISOLATION LEVEL {isolation_level.value};

        conn_0> show variables like '%isolation%';

        conn_0> SET @@optimizer_switch='index_condition_pushdown=off';

        conn_0> begin;
        conn_0> select b,c,d from ts where b>=5 and b<8 and c=7 for update;
        conn_0> select INDEX_NAME,LOCK_TYPE,LOCK_MODE,LOCK_STATUS,LOCK_DATA from performance_schema.data_locks;
        conn_0> commit;
        
        conn_0> SET @@optimizer_switch='index_condition_pushdown=on';

        conn_0> begin;
        conn_0> select b,c,d from ts where b>=5 and b<8 and c=7 for update;
        conn_0> select INDEX_NAME,LOCK_TYPE,LOCK_MODE,LOCK_STATUS,LOCK_DATA from performance_schema.data_locks;
        conn_0> commit;
        """,
    ]
