import database.config as db_config
from testcase.helpers import IsolationLevel

ORIGINAL_ISOLATION_LEVEL = IsolationLevel.REPEATABLE_READ
BUG_ID = "MYSQL-95049"
LINK = "https://bugs.mysql.com/bug.php?id=95049"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MYSQL, "8.0.39"
)

SETUP_SQL_SCRIPT = """
CREATE TABLE person (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id)) ENGINE=InnoDB;
INSERT INTO person (name, age) VALUES ('John Lin', 29);
"""

DESCRIPTION = (
    "Locks are relased on rollback, even though documentation specifies they shouldn't."
)


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};

        conn_0> begin;
        conn_0> SAVEPOINT somepoint;
        conn_0> UPDATE person SET age = 30 WHERE id = 1;
        conn_0> ROLLBACK TO somepoint;

        conn_1> begin;
        conn_1> UPDATE person SET age = 40 WHERE id = 1;

        conn_0> commit;
        """,
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};

        conn_0> begin;
        conn_0> UPDATE person SET age = 30 WHERE id = 1;

        conn_1> begin;
        conn_1> UPDATE person SET age = 40 WHERE id = 1;

        conn_0> commit;
        conn_1> commit;
        """,
    ]
