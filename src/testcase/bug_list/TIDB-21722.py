import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-21722"
LINK = "https://github.com/pingcap/tidb/issues/21722"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.TIDB, "49b926ed"
)

DESCRIPTION = """execute DDL statement in transaction reports 'invalid transaction'."""


def get_scenarios(isolation_level: IsolationLevel):
    # There is a gap of 0.3s between transactions, so we just add a few "nop" statements to make sure the gap is large enough.
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> create table t (c_int int, c_str varchar(40));
        conn_0> insert into t values (1, 'quizzical hofstadter');
        conn_0> begin;
        conn_0> select c_int from t where c_str is not null for update;
        conn_0> alter table t add index idx_4 (c_str);
        """
    ]
