import context
import testcase.bug as bug
import database.config as db_config

#################################################################################################
# Bug reported here: https://bugs.mysql.com/bug.php?id=107066                                   #
# Taken from here:   https://github.com/JZuming/TxCheck/blob/main/docs/mysql_bugs.md            #
# Setup:             mysql_bk_1.sql                                                             #
#################################################################################################

def bug1():
    scenario_0 = """
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
    scenario_1 = """
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
    setup_sql_script = context.Context.get_context().data_folder_path / "sql" / "mysql_bk_1.sql"
    bug_runner = bug.Bug(
        bug_id="107066",
        description="First bug I analyze",
        db_and_type=db_config.DatabaseTypeAndVersion(db_config.DatabaseType.MYSQL, "8.0.23"),
        scenarios=[scenario_0, scenario_1],
        setup_sql_script=setup_sql_script
    )
    bug_runner.run()