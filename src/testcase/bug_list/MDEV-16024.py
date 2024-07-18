import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

# From DT2

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "MDEV-16024"
LINK = "https://jira.mariadb.org/browse/MDEV-16024"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MARIADB, "10.3.6"
)

DESCRIPTION = (
    "The begin_transaction actually marks the end of the transaction, not the begin."
)

SETUP_SQL_SCRIPT = """
create or replace table t1 (
    x int(11) default null,
    row_start bigint(20) unsigned generated always as row start invisible,
    row_end bigint(20) unsigned generated always as row end invisible,
    period for system_time (row_start, row_end)
) engine=innodb with system versioning;
"""

CREATE_NEW_SERVER_FOR_TESTCASE = True


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> START TRANSACTION;
        conn_0> set @ts = now(6);
        conn_0> insert into t1 values(1);
        conn_0> commit;

        conn_0> select @ts;
        conn_0> select * from mysql.transaction_registry;
        conn_0> select (select begin_timestamp from mysql.transaction_registry) < @ts;
        """
    ]
