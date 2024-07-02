import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

# https://github.com/JZuming/TxCheck/blob/main/docs/mariadb_bugs.md

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "MDEV-29118"
LINK = "https://jira.mariadb.org/browse/MDEV-29118"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MARIADB, "10.8.3"
)

DESCRIPTION = "This makes MariaDB crash."


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
    conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
    conn_1> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
    conn_0> START TRANSACTION;

    conn_0> delete from t_davsbd;

    conn_1> START TRANSACTION;

    conn_1> insert into t_iqij_c (wkey, pkey, c_svp9sc, c_anyvkb) values
    (115, 222000, ASCII('w_3pab'), null),
    (115, 223000, CHAR_LENGTH(
    case when ((select wkey from t_j4mbqd order by wkey limit 1 offset 34)
    in (select ref_0.pkey as c0 from t_davsbd as ref_0))
    then 'k0hpvb' else 'sss' end), null);

    conn_0> update t_j4mbqd set wkey = 190;

    conn_0> ROLLBACK;

    conn_1> ROLLBACK;
    """
    ]
