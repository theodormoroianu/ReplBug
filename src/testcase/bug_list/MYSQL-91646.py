import database.config as db_config
from testcase.helpers import IsolationLevel

ORIGINAL_ISOLATION_LEVEL = IsolationLevel.REPEATABLE_READ
BUG_ID = "MYSQL-91646"
LINK = "https://bugs.mysql.com/bug.php?id=91646"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MYSQL, "5.7.22"
)

SETUP_SQL_SCRIPT = """
create table xatable(a int primary key);
"""

DESCRIPTION = "When super_read_only is true, all xa commands will still return OK, but normal transactions return ERROR when doing 'commit'."


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> xa start '1';
        conn_0> insert into xatable values (1);
        conn_0> xa end '1';

        conn_1> set global super_read_only=on;

        conn_0> xa prepare '1';
        conn_0> xa commit '1';
        """,
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> set global super_read_only=off;
        conn_0> begin;
        conn_0> insert into xatable values(11);

        conn_1> set global super_read_only=on;

        conn_0> commit; -- throws an error

        conn_1> set global super_read_only=off;

        conn_0> commit;
        """,
    ]
