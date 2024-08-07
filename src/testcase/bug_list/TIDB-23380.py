import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-23380"
LINK = "https://github.com/pingcap/tidb/issues/23380"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.TIDB, "9c48b24c.tikv"
)

DESCRIPTION = """processlist.txnstart is missing when tidb_snapshot is set"""

SETUP_SQL_SCRIPT = """
create table t (id int primary key, v int, index iv (v));
insert into t values (1, 10), (2, 20), (3, 30), (4, 40);
"""


def get_scenarios(isolation_level: IsolationLevel):
    # There is a gap of 0.3s between transactions, so we just add a few "nop" statements to make sure the gap is large enough.
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> SET TRANSACTION ISOLATION LEVEL {isolation_level.value};

        conn_0> set tidb_snapshot=now();
        conn_0> begin;
        conn_0> select txnstart from information_schema.processlist;
        """
    ]
