import database.config as db_config
from testcase.helpers import IsolationLevel

ORIGINAL_ISOLATION_LEVEL = IsolationLevel.REPEATABLE_READ
BUG_ID = "MYSQL-100328"
LINK = "https://bugs.mysql.com/bug.php?id=100328"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MYSQL, "5.7.22"
)

SETUP_SQL_SCRIPT = """
create table t(a int, b int) engine=innodb;
insert into t values (1, 0), (2, 1), (3, 2);
"""

DESCRIPTION = "UPDATE does not update all records."

CREATE_NEW_SERVER_FOR_TESTCASE = True


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> begin;
        conn_0> select * from t;

        conn_1> begin;
        conn_1> update t set a = 10 where b = 1;
        conn_1> commit;

        conn_0> select * from t;
        conn_0> update t set a = 10 where a;
        conn_0> select * from t;
        """,
    ]
