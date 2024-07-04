import context
import testcase.bug as bug
import database.config as db_config
from testcase.helpers import *

ORIGINAL_ISOLATION_LEVEL = DEFAULT_ISOLATION_LEVEL
BUG_ID = "MDEV-29400"
LINK = "https://jira.mariadb.org/browse/MDEV-29400"
DB_AND_VERSION = db_config.DatabaseTypeAndVersion(
    db_config.DatabaseType.MARIADB, "10.8.3"
)

DESCRIPTION = "Sometimes a different number of results are returned by SELECT."

# Need to restart the server after each request.
KILL_SERVER_AFTER_TESTCASE = True

op = """

"""


def get_scenarios(isolation_level: IsolationLevel):
    return [
        f"""
        conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL {isolation_level.value};
        conn_0> START TRANSACTION;
        conn_0> insert into t_nva8p (wkey, pkey, c_k6oesd, c_zwobic) values 
                (69, 41000, case when exists (
                    select  
                        subq_0.c0 as c0, 
                        subq_0.c3 as c1, 
                        subq_0.c1 as c2, 
                        subq_0.c0 as c3
                    from 
                        (select distinct 
                            ref_0.c_sygi8d as c0, 
                            ref_0.c_edvqhb as c1, 
                            ref_0.c_sygi8d as c2, 
                            ref_0.c_ans1a as c3
                            from 
                            t__d8k3c as ref_0
                            ) as subq_0
                    where instr(
                        subq_0.c1,
                        subq_0.c1) < FIELD(
                        subq_0.c1,
                        nullif('h7hmnc',
                            subq_0.c1),
                        subq_0.c1,
                        subq_0.c1)) then 86.38 else 24.15 end
                , 52.43);
        conn_0> COMMIT;
        """
    ]
