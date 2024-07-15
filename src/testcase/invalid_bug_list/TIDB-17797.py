import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-17797"
LINK = "https://github.com/pingcap/tidb/issues/17797"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.TIDB, "v4.0.0-beta.2.tikv"
)
DESCRIPTION = """The error message is not correct."""

SETUP_SQL_SCRIPT = """
CREATE TABLE t1 (
 id int not null primary key auto_increment,
 t varchar(100)
);
INSERT INTO t1 VALUES (1, 'acdc'), (2, 'afddfdc');
"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> BEGIN PESSIMISTIC;
        conn_1> BEGIN PESSIMISTIC;

        conn_0> UPDATE t1 SET t='new...' WHERE id = 1;
        conn_1> UPDATE t1 SET t='newval' WHERE id = 1;
        """,
    ]
