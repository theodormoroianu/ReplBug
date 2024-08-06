import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

# taken from  DT2

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-28095"
LINK = "https://github.com/pingcap/tidb/issues/28095"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.TIDB, "v6.4.0.tikv"
)

SETUP_SQL_SCRIPT = """
drop table if exists t;
create table t(a varchar(20));
insert into t values ('abc'), ('def');
"""

DESCRIPTION = "Should not throw an error on the third scenario."


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> update t set a = 'test' where cast(a as decimal);
        """,
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> start transaction;
        conn_0> update t set a = 'test' where cast(a as decimal);
        conn_0> rollback;
        """,
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> start transaction;
        conn_0> update t set a = 'xyz';
        conn_0> update t set a = 'test' where cast(a as decimal);
        conn_0> rollback;
        """,
    ]
