import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-30410"
LINK = "https://github.com/pingcap/tidb/issues/30410"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(db_config.DatabaseType.TIDB, "v5.2.1")

DESCRIPTION = """Lazy constraint check causes data inconsistency."""

SETUP_SQL_SCRIPT = """
drop table if exists t;
create table t (c0 int, c1 varchar(20), c2 varchar(20), unique key(c0), key(c2));
insert into t (c0, c1, c2) values (1, null, 'green');
"""

# We are messing with the timeout of the DBMS, so kill the server after usage to avoid complications.
KILL_SERVER_AFTER_TESTCASE = True


def get_scenarios(isolation_level: IsolationLevel):
    # There is a gap of 0.3s between transactions, so we just add a few "nop" statements to make sure the gap is large enough.
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        
        conn_0> set tidb_constraint_check_in_place=0;
        conn_0> begin optimistic;
        conn_0> insert into t (c0, c1, c2) values (1, 'red', 'white');
        conn_0> delete from t where c1 is null;
        conn_0> update t set c2 = 'green' where c2 between 'purple' and 'white';
        conn_0> commit;
        conn_0> admin check table t;
        """
    ]
