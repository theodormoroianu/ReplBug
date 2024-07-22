import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "MDEV-25546"
LINK = "https://jira.mariadb.org/browse/MDEV-25546"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MARIADB, "10.3.34"
)
SETUP_SQL_SCRIPT = """
create or replace table t1 (pk int primary key) with system versioning
partition by system_time limit 100 (
  partition p0 history,
  partition p1 history,
  partition pn current);

insert into t1 select seq from seq_1_to_90;
"""

DESCRIPTION = (
    "The first partition is empty, but data is placed in the second partition instead."
)


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> start transaction;
        conn_0> replace into t1 select seq from seq_1_to_80;
        conn_0> replace into t1 select seq from seq_1_to_70;
        conn_0> replace into t1 select seq from seq_1_to_60;

        conn_0> select partition_name, table_rows
                from information_schema.partitions
                where table_name = 't1'; 
        conn_0> rollback;

        conn_0> select partition_name, table_rows
                from information_schema.partitions
                where table_name = 't1';

        conn_0> replace into t1 select seq from seq_1_to_10;
        conn_0> select partition_name, table_rows
                from information_schema.partitions
                where table_name = 't1';
        """,
    ]
