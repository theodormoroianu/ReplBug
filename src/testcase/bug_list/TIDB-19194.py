import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-19194"
LINK = "https://github.com/pingcap/tidb/issues/19194"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.TIDB, "v4.0.4.tikv"
)

DESCRIPTION = """The second replace should behave like the first one, but it doesn't."""

SETUP_SQL_SCRIPT = """
create table t (c_int int, c_str varchar(40), primary key (c_int));
insert into t values (1, 'Alice');
"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> begin;
        conn_0> insert into t values (1, 'Bob'), (1, 'Carol');
        conn_0> replace into t values (1, 'Dave');
        conn_0> commit;
        conn_0> replace into t values (1, 'Dave');
        """,
    ]
