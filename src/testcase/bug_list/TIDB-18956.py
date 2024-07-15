import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import DEFAULT_ISOLATION_LEVEL, IsolationLevel

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "TIDB-18956"
LINK = "https://github.com/pingcap/tidb/issues/18956"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.TIDB, "v4.0.4.tikv"
)

DESCRIPTION = """Delete should not report any error."""

SETUP_SQL_SCRIPT = """
create table t (
    c_int       int,
    c_double    double,
    c_decimal   decimal(12, 6),
    c_string    varchar(40),
    c_datetime  datetime,
    c_timestamp timestamp,
    c_enum      enum ('a', 'b', 'c', 'd', 'e'),
    c_set       set ('1', '2', '3', '4', '5'),
    c_json      json,
    primary key (c_int),
    unique key (c_string),
    key (c_enum),
    key (c_set),
    key (c_timestamp),
    key (c_datetime),
    key (c_decimal)
);
insert into t (`c_int`, `c_double`, `c_decimal`, `c_string`, `c_datetime`, `c_timestamp`, `c_enum`, `c_set`, `c_json`) values
  (2, 0.029523, 74.040000, 'gold mistress', '2020-01-02 00:00:00', '2019-12-25 03:24:58', 'c', '1,3,5', '{\"datetime\": \"2019-12-26 13:00:00\", \"enum\": \"d\", \"int\": 3, \"set\": \"1,4,5\", \"str\": \"gray koala\"}')
, (4, 0.924873, 35.020000, 'gray witch', '2019-12-26 17:00:00', '2020-01-05 13:01:59', 'd', '1', '{\"datetime\": \"2019-12-30 19:00:00\", \"enum\": \"d\", \"int\": 4, \"set\": \"1,5\", \"str\": \"violet head\"}')
, (5, 0.268598, 59.660000, 'pink fly', '2020-01-04 12:00:00', '2020-01-06 05:33:43', 'd', '1,3,4,5', '{\"datetime\": \"2020-01-04 06:00:00\", \"enum\": \"c\", \"int\": 10, \"set\": \"\", \"str\": \"gold fly\"}')
, (6, 0.551611, 70.960000, 'azure bard', '2020-01-06 02:00:00', '2020-01-07 13:20:29', 'd', '3,4,5', '{\"datetime\": \"2019-12-30 21:00:00\", \"enum\": \"b\", \"int\": 4, \"set\": \"2,5\", \"str\": \"dark kangaroo\"}')
, (7, 0.197616, 9.090000, 'dark curtain', '2020-01-06 02:00:00', '2019-12-30 05:50:54', 'e', '1,2,4', '{\"datetime\": \"2019-12-31 05:00:00\", \"enum\": \"b\", \"int\": 17, \"set\": \"3\", \"str\": \"dark jester\"}')
, (8, 0.515967, 28.090000, 'cyan crown', '2019-12-29 09:00:00', '2019-12-30 00:17:50', 'e', '1,2,3,4,5', '{\"datetime\": \"2020-01-02 22:00:00\", \"enum\": \"d\", \"int\": 19, \"set\": \"4\", \"str\": \"black seer\"}')
, (9, 0.688223, 5.000000, 'gold bard', '2020-01-01 06:00:00', '2019-12-26 14:17:18', 'e', '3', '{\"datetime\": \"2019-12-27 11:00:00\", \"enum\": \"c\", \"int\": 9, \"set\": \"2\", \"str\": \"ivory paladin\"}')
, (10, 0.460531, 11.080000, 'brown cat', '2020-01-01 08:00:00', '2019-12-31 16:51:26', 'd', '2', '{\"datetime\": \"2019-12-28 11:00:00\", \"enum\": \"c\", \"int\": 20, \"set\": \"3\", \"str\": \"crimson tooth\"}')
, (11, 0.360937, 4.630000, 'yellow master', '2019-12-31 15:00:00', '2019-12-31 06:12:42', 'c', '', '{\"datetime\": \"2019-12-29 13:00:00\", \"enum\": \"d\", \"int\": 17, \"set\": \"2,5\", \"str\": \"cyan spider\"}')
, (12, 0.745632, 58.540000, 'yellow kangaroo', '2020-01-01 18:00:00', '2020-01-02 15:50:29', 'b', '1,3', '{\"datetime\": \"2019-12-31 17:00:00\", \"enum\": \"a\", \"int\": 20, \"set\": \"3,4\", \"str\": \"light song\"}')
, (13, 0.203077, 4.870000, 'light fly', '2020-01-03 10:00:00', '2020-01-01 03:05:33', 'c', '1,5', '{\"datetime\": \"2020-01-02 12:00:00\", \"enum\": \"c\", \"int\": 15, \"set\": \"1,3,4,5\", \"str\": \"navy carpet\"}')
, (14, 0.622945, 99.270000, 'white kangaroo', '2019-12-29 13:00:00', '2019-12-26 22:21:32', 'a', '1,2,3,5', '{\"datetime\": \"2019-12-28 03:00:00\", \"enum\": \"b\", \"int\": 18, \"set\": \"2,4,5\", \"str\": \"carnelian kangaroo\"}')
, (15, 0.663324, 17.760000, 'orange kangaroo', '2020-01-01 00:00:00', '2019-12-28 12:57:30', 'c', '1', '{\"datetime\": \"2019-12-25 19:00:00\", \"enum\": \"d\", \"int\": 1, \"set\": \"2,3\", \"str\": \"cream roach\"}')
, (16, 0.218067, 25.030000, 'cyan watcher', '2020-01-01 10:00:00', '2019-12-31 10:36:08', 'd', '3,4,5', '{\"datetime\": \"2019-12-30 03:00:00\", \"enum\": \"d\", \"int\": 3, \"set\": \"4\", \"str\": \"green trader\"}');
"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> begin;
        conn_0> update t set c_decimal = c_decimal + 5 where c_decimal <= 20;
        conn_0> insert into t values (5, 0.157960, 67.26, 'brown cat', '2019-12-28 15:00:00', '2020-01-07 07:22:43', 'c', '1', '{{"int":13,"str":"ivory vulture","datetime":"2019-12-31 05:00:00","enum":"b","set":"3,5"}}');
        conn_0> delete from t where c_int = 5;
        conn_0> rollback;
        """,
    ]
