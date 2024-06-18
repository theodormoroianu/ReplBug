import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "MDEV-29243"
LINK = "https://jira.mariadb.org/browse/MDEV-29243"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MARIADB, "10.8.3", False
)

expected_bug_description = "The bug causes a crash of the MariaDB server"


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
    conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
    conn_1> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
    conn_1> START TRANSACTION;
    conn_0> START TRANSACTION;
    conn_1> delete from t_swbayb;
    conn_0> insert into t_swbayb (wkey, pkey) values (88, 74000);
    conn_1> insert into t_8fjoxb (wkey, pkey, c_yecif) values
      (110, 115000, case when exists (
      select
      ref_0.wkey as c14
      from
      t_swbayb as ref_0
      where (ref_0.pkey > (
      select distinct
      ref_1.wkey as c0
      from
      t_swbayb as ref_1
      ))) then 'vxg_w' else null end
      );

    conn_0> insert into t_swbayb (wkey, pkey, c_ywdp4d) values (90, 83000, 'vyenkd');
    conn_0> COMMIT;
    conn_1> COMMIT;
    """
    ]
