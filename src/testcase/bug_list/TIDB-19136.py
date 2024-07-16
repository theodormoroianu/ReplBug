import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-19136"
LINK = "https://github.com/pingcap/tidb/issues/19136"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.TIDB, "v4.0.4.tikv"
)

DESCRIPTION = """Duplicate key is ignored in insert The insert statement should fail."""

SETUP_SQL_SCRIPT = """
create table t ( c_int int, c_str varchar(40), primary key(c_int, c_str) );
"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> begin;
        conn_0> insert into t values (1, 'amazing almeida'), (2, 'boring bardeen'), (3, 'busy wescoff');
        conn_0> select c_int, (select t1.c_int from t t1 where t1.c_int = 3 and t1.c_int > t.c_int order by t1.c_int limit 1) x from t;
        conn_0> commit;
        conn_0> select c_int, (select t1.c_int from t t1 where t1.c_int = 3 and t1.c_int > t.c_int order by t1.c_int limit 1) x from t;
        """,
    ]
