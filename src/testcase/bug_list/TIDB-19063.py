import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-19063"
LINK = "https://github.com/pingcap/tidb/issues/19063"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.TIDB, "bdc59e6e.tikv"
)

DESCRIPTION = """Duplicate key is ignored in insert The insert statement should fail."""

SETUP_SQL_SCRIPT = """
create table t ( c_int int, c_string varchar(40) collate utf8mb4_bin , primary key (c_string), unique key (c_int));
;
"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> begin;
        conn_0> replace into t values (22, 'gold witch'), (24, 'gray singer'), (21, 'silver sight');
        conn_0> commit;
        conn_0> begin;
        conn_0> insert into t values (21,'black warlock'), (22, 'dark sloth'), (21,  'cyan song') on duplicate key update c_int = c_int + 1, c_string = concat(c_int, ':', c_string);
        conn_0> commit;
        conn_0> select * from t;
        conn_0> drop table t;
        """,
        """
        conn_0> replace into t values (22, 'gold witch'), (24, 'gray singer'), (21, 'silver sight');
        conn_0> insert into t values (21,'black warlock'), (22, 'dark sloth'), (21,  'cyan song') on duplicate key update c_int = c_int + 1, c_string = concat(c_int, ':', c_string);
        conn_0> select * from t;
        conn_0> drop table t;
        """,
    ]
