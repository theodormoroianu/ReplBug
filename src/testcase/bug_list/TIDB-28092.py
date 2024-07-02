import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

# taken from  DT2

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-28092"
LINK = "https://github.com/pingcap/tidb/issues/28092"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(db_config.DatabaseType.TIDB, "v5.2.1")

SETUP_SQL_SCRIPT = """
create table t(a blob not null, b text);
insert ignore into t values (null, null), (null, 'abc');
"""

DESCRIPTION = "Should not throw an error. This is actually not transaction-related (see comments on the issue)."


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> begin;
        conn_0> update t set b = 'test' where a;
        conn_0> rollback;
        """,
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};        
        conn_0> begin;
        conn_0> update t set b = 'def';
        conn_0> update t set b = 'test' where a;
        conn_0> rollback;
        """,
    ]
