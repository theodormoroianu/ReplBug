import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-27156"
LINK = "https://github.com/pingcap/tidb/issues/27156"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.TIDB, "v5.2.0-alpha-26237b35.tikv"
)

DESCRIPTION = """Playing with lock_wait_timeout and txn_mode makes the same commit succeed / fail."""

SETUP_SQL_SCRIPT = """
create table t2(c1 int primary key, c2 int, c3 int, c4 int, key k2(c2), key k3(c3)) partition by hash(c1) partitions 10;
insert into t2 values (1,1,1,1),(2,2,2,2),(3,3,3,3),(4,4,4,4);
"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> set autocommit = 0;
        conn_0> set innodb_lock_wait_timeout = 0;
        conn_0> set tidb_txn_mode = pessimistic;

        conn_1> set autocommit = 0;
        conn_1> set innodb_lock_wait_timeout = 0;
        conn_1> set tidb_txn_mode = pessimistic;

        conn_2> set autocommit = 0;
        conn_2> set tidb_txn_mode = optimistic;

        conn_0> select * from t2 where c4 > 2 for update;

        conn_1> insert into t2 values(5,5,5,5);
        conn_1> update t2 set c4 = c4 + 1 where c3 = 3;
        conn_1> select c1, c3 from t2 where c3 = 4 for update nowait;

        conn_2> update t2 set c4 = c4 * 10 where c4 = 4;
        conn_0> commit;
        conn_2> commit;
        """
    ]
