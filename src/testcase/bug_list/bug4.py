import context
import testcase.bug as bug
import database.config as db_config

#################################################################################################
# Bug reported here: https://bugs.mysql.com/bug.php?id=107887                                   #
# Taken from here:   https://github.com/JZuming/TxCheck/blob/main/docs/mysql_bugs.md            #
# Setup:             mysql_bk_1.sql                                                             #
#################################################################################################

def bug4():
    scenario_0 = """
    conn_0> SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
    conn_1> SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;

    conn_0> START TRANSACTION;
    conn_1> START TRANSACTION;
    conn_1> insert into t_cqieb values
    (141, 210000, 41.72, 56, 76, null, 32.6, null, 11, 12, 74),
    (141, 211000, 41.73, 87, 84, null, 11.2, 79.63, null, 58, 4),
    (141, 212000, 41.73, 87, 84, null, 11.2, 79.63, null, 58, 4),
    (141, 213000, null, null, null, null, null, null, null, null, null);
    conn_1> ROLLBACK;
    conn_0> update t_cqieb set
    wkey = 116 
    where t_cqieb.c_rejdnc not in (
    select
        subq_0.c0 as c0
        from
        (select
                ref_8.c_myvn4d as c0
            from
                t_b9lvzc as ref_8
            where ref_8.c_lszpl < ref_8.c_t41kdd) as subq_0
        where subq_0.c0 < (  
        select
                ref_9.c_1xf8oc as c0
            from
                (t_b9lvzc as ref_9
                left outer join t_b9lvzc as ref_10
                on (ref_9.c_t41kdd = ref_10.wkey ))
            where ref_9.c_t41kdd <> ref_10.pkey)
        order by c0 asc);
    conn_0> select * from t_cqieb where wkey = 116;
    conn_0> COMMIT;
    """

    scenario_1 = """
    conn_0> START TRANSACTION;
    conn_0> update t_cqieb set
    wkey = 116 
    where t_cqieb.c_rejdnc not in (
    select
        subq_0.c0 as c0
        from
        (select
                ref_8.c_myvn4d as c0
            from
                t_b9lvzc as ref_8
            where ref_8.c_lszpl < ref_8.c_t41kdd) as subq_0
        where subq_0.c0 < (  
        select
                ref_9.c_1xf8oc as c0
            from
                (t_b9lvzc as ref_9
                left outer join t_b9lvzc as ref_10
                on (ref_9.c_t41kdd = ref_10.wkey ))
            where ref_9.c_t41kdd <> ref_10.pkey)
        order by c0 asc);
    conn_0> select * from t_cqieb where wkey = 116;
    conn_0> COMMIT;
    """

    setup_sql_script = context.Context.get_context().data_folder_path / "sql" / "mysql_bk_4.sql"
    bug_runner = bug.Bug(
        bug_id="107887",
        description="https://bugs.mysql.com/bug.php?id=107887",
        db_and_type=db_config.DatabaseTypeAndVersion(db_config.DatabaseType.MYSQL, "8.0.23"),
        scenarios=[scenario_0, scenario_1],
        setup_sql_script=setup_sql_script
    )
    bug_runner.run()