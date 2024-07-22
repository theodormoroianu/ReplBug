import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "MDEV-28944"
LINK = "https://jira.mariadb.org/browse/MDEV-28944"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MARIADB, "cb1f08bd-debug"
)

DESCRIPTION = (
    "The server crashes during an XA transaction rollback after a table is altered."
)

SETUP_SQL_SCRIPT = """
"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> CREATE TABLE t (a INT) ENGINE=MyISAM;
        conn_0> INSERT INTO t VALUES (1);

        conn_1> XA START 'xid';
        conn_1> SELECT * FROM t;

        conn_0> ALTER TABLE t NOWAIT ADD KEY (a);

        conn_1> UPDATE t SET a = 2;
        conn_1> XA END 'xid';
        conn_1> XA ROLLBACK 'xid';

        conn_0> DROP TABLE t;
        """
    ]
