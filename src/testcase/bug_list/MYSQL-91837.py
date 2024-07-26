import database.config as db_config
from testcase.helpers import IsolationLevel

ORIGINAL_ISOLATION_LEVEL = IsolationLevel.REPEATABLE_READ
BUG_ID = "MYSQL-91837"
LINK = "https://bugs.mysql.com/bug.php?id=91837"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MYSQL, "5.7.22"
)

SETUP_SQL_SCRIPT = """
create table xatable(a int primary key);
"""

DESCRIPTION = "transaction start date is not expressed in session time zone"

CREATE_NEW_SERVER_FOR_TESTCASE = True


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> begin;
        conn_0> select * from mysql.innodb_table_stats LIMIT 1;
        
        conn_1> SELECT SLEEP(2);
        conn_1> select trx_started from information_schema.innodb_trx;
        conn_1> select count(*) from information_schema.innodb_trx where trx_started < date_sub(now(), interval 1 second);
        conn_1> set session time_zone = '-09:00';
        conn_1> select trx_started from information_schema.innodb_trx;
        conn_1> select count(*) from information_schema.innodb_trx where trx_started < date_sub(now(), interval 1 second);
        """,
    ]
