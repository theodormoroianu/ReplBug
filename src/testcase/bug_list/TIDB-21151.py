import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-21151"
LINK = "https://github.com/pingcap/tidb/issues/21151"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.TIDB, "v4.0.8.tikv"
)

DESCRIPTION = """Gets warnings when running in a transaction."""

SETUP_SQL_SCRIPT = """
create table t (id int primary key, value int, a int not null, b int not null,
    index ia (a),  index ib (b));

insert into t values (1, 10, 2, 0), (2, 10, 4, 4), (3, 10, 0, 2), (4, 10, 0, 0);
"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL repeatable read;
        conn_0> SET TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> BEGIN;
        conn_0> select /*+ NO_INDEX_MERGE() */ * from t where a > 3 or b > 3;
        conn_0> select /*+ USE_INDEX_MERGE(t, ia, ib) */ * from t where a > 3 or b > 3;

        conn_1> BEGIN;
        conn_1> update t set value = 11 where id = 2;
        conn_1> COMMIT;

        conn_0> select /*+ NO_INDEX_MERGE() */ * from t where a > 3 or b > 3;
        conn_0> select /*+ USE_INDEX_MERGE(t, ia, ib) */ * from t where a > 3 or b > 3;

        conn_0> COMMIT;
        """,
    ]
