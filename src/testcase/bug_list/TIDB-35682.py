import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-35682"
LINK = "https://github.com/pingcap/tidb/issues/35682"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.TIDB, "v6.4.0.tikv"
)

DESCRIPTION = """Instruction that failed due to timeout still holds locks."""

SETUP_SQL_SCRIPT = """
drop table if exists t, t2;
create table t (id int primary key, v int, idx int unique);
insert into t values (1, 10, 1), (2, 20, 2);
"""

# We are messing with the timeout of the DBMS, so kill the server after usage to avoid complications.
KILL_SERVER_AFTER_TESTCASE = True


def get_scenarios(isolation_level: IsolationLevel):
    # There is a gap of 0.3s between transactions, so we just add a few "nop" statements to make sure the gap is large enough.
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};

        conn_0> begin;
        conn_0> select @@tidb_current_ts;

        conn_1> begin;
        conn_1> update t set v = v + 1 where id = 1;

        conn_0> set @@innodb_lock_wait_timeout = 1;
        conn_0> select * from t where idx = 1 for update;
        conn_0> select @@tidb_current_ts;
        conn_0> select @@tidb_current_ts;
        conn_0> select @@tidb_current_ts;
        
        conn_0> select * from t where idx = 2 for update;

        conn_1> commit;

        conn_2> begin;
        
        conn_2> select * from t where idx = 1 for update;
        conn_2> rollback;

        conn_0> rollback;

        """
    ]
