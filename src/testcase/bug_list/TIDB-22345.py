import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-22345"
LINK = "https://github.com/pingcap/tidb/issues/22345"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.TIDB, "v4.0.0-beta.2.tikv"
)

DESCRIPTION = """"Select For Update" in decorrelated subquery return WriteConflictError in pessimistic mode."""

SETUP_SQL_SCRIPT = """
create table t(id int primary key, v int);
insert into t values(1, 10), (2, 20);
"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> begin pessimistic;
        conn_0> select * from t;
        conn_1> update t set v = v * 10;
        conn_0> select (select v from t where id = 2 for update) from dual;
        """,
    ]
