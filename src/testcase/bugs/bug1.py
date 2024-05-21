"""
Bug reported here: https://bugs.mysql.com/bug.php?id=107066
Taken from here:   https://github.com/JZuming/TxCheck/blob/main/docs/mysql_bugs.md
Setup:             mysql_bk_1.sql
"""

import testcase.pase_testcase as parse_testcase
import testcase.testcase as testcase_types
import database.config as db_config

RUN1 = """
conn_1> START TRANSACTION;
conn_0> START TRANSACTION;
conn_1> insert into t_zcfqb (wkey, pkey, c_dl_pmd, c_avevqc, c_sqqbbd, c_2wz8nc, c_qyxu0, c_slu2bd) values
          (182, 264000, null, 'biiumc', null, 'dwzl6d', 93.90, null);
conn_0> insert into t_zcfqb (wkey, c_rvm_p, c_avevqc, c_ywxlqb, c_sqqbbd, c_2wz8nc, c_qyxu0, c_ph8nh)
          select
              121 as c0,
              ref_0.c_h1m_zb as c1,
              ref_0.c_gsbzrd as c2,
              ref_0.c_hdnifc as c3,
              (select wkey from t_nvues order by wkey limit 1 offset 5)
                 as c4,
              ref_0.c_h1m_zb as c5,
              ref_0.c_hdnifc as c6,
              ref_0.c_h1m_zb as c7
            from
              t_nvues as ref_0
            where (0 <> 0)
              or (ref_0.wkey is not NULL);
conn_0> select pkey from t_zcfqb where wkey = 121;
conn_1> ROLLBACK;
conn_0> COMMIT;
"""

RUN2 = """
conn_0> START TRANSACTION;
conn_0> insert into t_zcfqb (wkey, c_rvm_p, c_avevqc, c_ywxlqb, c_sqqbbd, c_2wz8nc, c_qyxu0, c_ph8nh)
          select
              121 as c0,
              ref_0.c_h1m_zb as c1,
              ref_0.c_gsbzrd as c2,
              ref_0.c_hdnifc as c3,
              (select wkey from t_nvues order by wkey limit 1 offset 5)
                 as c4,
              ref_0.c_h1m_zb as c5,
              ref_0.c_hdnifc as c6,
              ref_0.c_h1m_zb as c7
            from
              t_nvues as ref_0
            where (0 <> 0)
              or (ref_0.wkey is not NULL);
conn_0> select pkey from t_zcfqb where wkey = 121;
conn_0> COMMIT;
"""


def get_setup_instructions():
    data = open("data/sql/mysql_bk_1.sql").read()
    setup_instructions = testcase_types.Instruction(None, data)
    return [setup_instructions]

def run():
    pre_run = get_setup_instructions()
    instructions_1 = parse_testcase.parse_instructions(RUN1)
    instructions_2 = parse_testcase.parse_instructions(RUN2)

    test1 = testcase_types.Testcase(
        "Scenario 1",
        instructions=instructions_1,
        db_and_type=db_config.DatabaseTypeAndVersion(db_config.DatabaseType.MYSQL, "8.0.23"),
        pre_run_instructions=pre_run
    )

    test2 = testcase_types.Testcase(
        "Scenario 2",
        instructions=instructions_2,
        db_and_type=db_config.DatabaseTypeAndVersion(db_config.DatabaseType.MYSQL, "8.0.23"),
        pre_run_instructions=pre_run
    )

    print(f"Running first test...")
    test1.run()
    print(f"Running second test...")
    test2.run()

