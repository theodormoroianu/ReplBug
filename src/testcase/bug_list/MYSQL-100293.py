import database.config as db_config
from testcase.helpers import IsolationLevel

ORIGINAL_ISOLATION_LEVEL = IsolationLevel.REPEATABLE_READ
BUG_ID = "MYSQL-100293"
LINK = "https://bugs.mysql.com/bug.php?id=100293"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MYSQL, "5.7.31"
)

DESCRIPTION = "The SERIALIZABLE transactions are not blocked for query cache"
CREATE_NEW_SERVER_FOR_TESTCASE = True
CUSTOM_SERVER_ARGS = ["--query-cache-type=1"]


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> CREATE TABLE t(c1 INT);
        conn_0> INSERT INTO t VALUES(1),(2);

        conn_0> BEGIN;
        conn_0> SELECT * FROM t;
        conn_0> COMMIT;

        conn_0> flush status;
        conn_0> SHOW STATUS LIKE "Qcache_hits";

        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> SET SESSION TRANSACTION ISOLATION LEVEL {isolation_level.value};

        conn_0> BEGIN;
        conn_0> SELECT * FROM t;
        conn_0> SHOW STATUS LIKE "Qcache_hits";

        conn_1> INSERT INTO t VALUES(3);
        conn_0> COMMIT;
        """,
    ]
