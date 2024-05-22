import context
import testcase.bug as bug
import database.config as db_config

#################################################################################################
# Bug reported here: https://bugs.mysql.com/bug.php?id=107898                                   #
# Taken from here:   https://github.com/JZuming/TxCheck/blob/main/docs/mysql_bugs.md            #
# Setup:             mysql_bk_2.sql                                                             #
#################################################################################################

def bug2():
    scenario_0 = """
    conn_0> SET LOCAL TRANSACTION ISOLATION LEVEL READ COMMITTED; 
    conn_1> SET LOCAL TRANSACTION ISOLATION LEVEL READ COMMITTED;

    conn_0> START TRANSACTION;
    conn_1> START TRANSACTION; 

    delete from t_8fhx8c;

    ROLLBACK;

    conn_0> select *
    from
        t_8fhx8c as ref_1
    where ref_1.c_0byzvd not in (
        select
            nullif(19, 19) as c0
        from
            (select
                ref_2.c_zov5kd as c0
                from
                t_8fhx8c as ref_2
                ) as subq_0
        window w_u6cwrd as (partition by subq_0.c0));

    conn_0> commit;
    """
    scenario_1 = """
    conn_0> START TRANSACTION;
    conn_0> select *
    from
        t_8fhx8c as ref_1
    where ref_1.c_0byzvd not in (
        select
            nullif(19, 19) as c0
        from
            (select
                ref_2.c_zov5kd as c0
                from
                t_8fhx8c as ref_2
                ) as subq_0
        window w_u6cwrd as (partition by subq_0.c0));
    conn_0> COMMIT;
    """
    setup_sql_script = context.Context.get_context().data_folder_path / "sql" / "mysql_bk_2.sql"
    bug_runner = bug.Bug(
        bug_id="107898",
        description="https://bugs.mysql.com/bug.php?id=107898",
        db_and_type=db_config.DatabaseTypeAndVersion(db_config.DatabaseType.MYSQL, "8.0.23"),
        scenarios=[scenario_0, scenario_1],
        setup_sql_script=setup_sql_script
    )
    bug_runner.run()