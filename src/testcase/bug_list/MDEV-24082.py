import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "MDEV-24082"
LINK = "https://jira.mariadb.org/browse/MDEV-24082"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MARIADB, "10.1.38"
)
SETUP_SQL_SCRIPT = """
CREATE TABLE p (id int unsigned NOT NULL PRIMARY KEY);
INSERT INTO p VALUES (2);
"""

DESCRIPTION = "This fails with 'Cannot execute statement in a READ ONLY transaction', despite only attempting to update the temporary table. However, if you modify the UPDATE to use a subquery instead of a join, it works."


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> BEGIN;
        conn_0> CREATE TEMPORARY TABLE t (id int unsigned NOT NULL PRIMARY KEY,flag tinyint NOT NULL DEFAULT 0);
        conn_0> INSERT INTO t (id) VALUES (1),(2),(3),(4),(5);
        conn_0> START TRANSACTION READ ONLY;
        conn_0> UPDATE t INNER JOIN p USING (id) SET t.flag=1;
        conn_0> COMMIT;
        """,
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> BEGIN;
        conn_0> CREATE TEMPORARY TABLE t (id int unsigned NOT NULL PRIMARY KEY,flag tinyint NOT NULL DEFAULT 0);
        conn_0> INSERT INTO t (id) VALUES (1),(2),(3),(4),(5);
        conn_0> START TRANSACTION READ ONLY;
        conn_0> UPDATE t SET t.flag=1 WHERE id IN (SELECT id FROM p);
        conn_0> COMMIT;
        """,
    ]
