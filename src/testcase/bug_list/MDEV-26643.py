import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

# From DT2

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "MDEV-26643"
LINK = "https://jira.mariadb.org/browse/MDEV-26643"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MARIADB, "10.5.12"
)
SETUP_SQL_SCRIPT = """
drop table if exists t;
create table t(a int, b int);
insert into t values(null, 1), (2, 2), (null, null), (null, 3), (4, null);
"""
DESCRIPTION = "The first row should be 20, but is 1 (not updated)"


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> begin;
        conn_0> update t set a = 10 where 1;
        conn_1> begin;
        conn_1> update t set b = 20 where a;
        conn_0> commit;
        conn_1> commit;
        conn_2> select * from t;
    """,
    ]
