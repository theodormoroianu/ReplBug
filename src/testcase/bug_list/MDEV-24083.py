import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

# From DT2

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "MDEV-24083"
LINK = "https://jira.mariadb.org/browse/MDEV-24083"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MARIADB, "10.1.48"
)

DESCRIPTION = "DDL should be allowed in read-only transactions."


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> START TRANSACTION READ ONLY;
        conn_0> CREATE TEMPORARY TABLE t (id int unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,val int unsigned NOT NULL);
        conn_0> INSERT INTO t (val) VALUES (22),(96),(47),(5),(22);
        conn_0> SELECT * FROM t;
        conn_0> DROP TEMPORARY TABLE t;
        conn_0> COMMIT;
    """,
    ]
