import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-34978"
LINK = "https://github.com/pingcap/tidb/issues/34978"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.TIDB, "v6.4.0.tikv"
)

SETUP_SQL_SCRIPT = """
create table t (id int primary key, c int not null);
insert into t values (1, 1), (2, 2);
"""

DESCRIPTION = (
    """A SELECT throws an error after a DML operation in another transaction."""
)


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        
        conn_0> begin;

        conn_1> alter table t drop column c;
        conn_1> insert into t values (3);

        conn_0> select * from t for update;
        """,
    ]
