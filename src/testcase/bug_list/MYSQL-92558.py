import database.config as db_config
from testcase.helpers import IsolationLevel

ORIGINAL_ISOLATION_LEVEL = IsolationLevel.REPEATABLE_READ
BUG_ID = "MYSQL-92558"
LINK = "https://bugs.mysql.com/bug.php?id=92558"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MYSQL, "8.0.12"
)

SETUP_SQL_SCRIPT = """
create table t (i int);
insert into t values (1);
"""

DESCRIPTION = (
    "The 'trx_is_read_only' flag is not set on implicit read-only transactions."
)

CREATE_NEW_SERVER_FOR_TESTCASE = True


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> SET GLOBAL innodb_monitor_enable = 'trx_rw_commits';
        conn_0> SET GLOBAL innodb_monitor_enable = 'trx_ro_commits';
        conn_0> SET GLOBAL innodb_monitor_enable = 'trx_nl_ro_commits';
        conn_0> SET GLOBAL innodb_monitor_enable = 'trx_commits_insert_update';

        conn_0> SELECT name, comment, status, count FROM information_schema.innodb_metrics   WHERE name like 'trx%comm%';

        conn_0> START TRANSACTION;
        conn_0> select count(*) from t;

        conn_0> select trx_is_read_only from information_schema.innodb_trx;

        conn_0> COMMIT;

        conn_0> SELECT name, comment, status, count FROM information_schema.innodb_metrics   WHERE name like 'trx%comm%';
        
        conn_0> START TRANSACTION READ ONLY;
        conn_0> select count(*) from t;

        conn_0> select trx_is_read_only from information_schema.innodb_trx;

        conn_0> COMMIT;

        conn_0> SELECT name, comment, status, count FROM information_schema.innodb_metrics   WHERE name like 'trx%comm%';

        """,
    ]
