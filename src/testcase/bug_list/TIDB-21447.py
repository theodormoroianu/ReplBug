import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-21447"
LINK = "https://github.com/pingcap/tidb/issues/21447"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.TIDB, "v4.0.8.tikv"
)

DESCRIPTION = (
    """read using different executors in transaction result in different results"""
)

SETUP_SQL_SCRIPT = """
CREATE TABLE `t1` ( `id` int(11) primary key, `name` varchar(20) DEFAULT NULL );
insert into t1 values(1,'abc');
"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> begin;
        conn_1> begin;
        conn_1> select * from t1 where id  = 1; -- the result is "1 abc" before the update commit in t1
        conn_0> UPDATE t1 SET name='xyz' WHERE id=1;
        conn_0> commit;
        conn_1> UPDATE t1 SET name='xyz' WHERE id=1; -- update the same row with same value using point get
        conn_1> select * from t1;               -- the result is "1, abc"
        conn_1> select * from t1 where id = 1 ; -- the result is "1, xyz"
        conn_1> commit;
        """,
        """
        conn_1> select * from t1 where id  = 1; -- the result is "1 abc" before the update commit in t1
        conn_0> UPDATE t1 SET name='xyz' WHERE id=1;
        conn_1> UPDATE t1 SET name='xyz' WHERE id=1; -- update the same row with same value using point get
        conn_1> select * from t1;               -- the result is "1, abc"
        conn_1> select * from t1 where id = 1 ; -- the result is "1, xyz"
        """,
    ]
