import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-21498"
LINK = "https://github.com/pingcap/tidb/issues/21498"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.TIDB, "3a32bd2d.tikv"
)

DESCRIPTION = """transaction sees inconsistent data when there are concurrent DDLs"""

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

        conn_0> begin;
        conn_0> explain select * from t where v = 10;
        conn_0> select * from t where v = 10;

        conn_1> alter table t drop index iv;
        conn_1> update t set v = 11 where id = 1;

        conn_0> explain select * from t where v = 10;
        conn_0> select * from t where v = 10;
        conn_0> select * from t where id = 1;
        """
    ]
