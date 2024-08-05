import database.config as db_config
from testcase.helpers import IsolationLevel

ORIGINAL_ISOLATION_LEVEL = IsolationLevel.REPEATABLE_READ
BUG_ID = "MYSQL-90987"
LINK = "https://bugs.mysql.com/bug.php?id=90987"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MYSQL, "5.7.17"
)

DESCRIPTION = "Using a parition index causes deadlocks"


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> create table t4 (a int unsigned auto_increment , b int, c int, key(b), primary key(a,b)) PARTITION BY LIST (b)(partition p0 values in (0,1, 2 ,3, 4), partition p1 values in(5,6,7,8,9,10));
        conn_0>  insert into t4(b,c) values(1,11),(2,22),(3,33),(4,44),(5,55),(6,66),(7,77),(8,88),(9,99);

        conn_0> begin;
        conn_0> update t4 set c=c+1 where b=3;

        conn_1> begin;
        conn_1> update t4 set c=c+1 where b=2;
        """,
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> create table t4 (a int unsigned auto_increment , b int, c int, key(b), primary key(a,b));
        conn_0>  insert into t4(b,c) values(1,11),(2,22),(3,33),(4,44),(5,55),(6,66),(7,77),(8,88),(9,99);

        conn_0> begin;
        conn_0> update t4 set c=c+1 where b=3;

        conn_1> begin;
        conn_1> update t4 set c=c+1 where b=2;
        """,
    ]
