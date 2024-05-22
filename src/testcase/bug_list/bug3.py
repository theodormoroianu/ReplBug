import context
import testcase.bug as bug
import database.config as db_config

#################################################################################################
# Bug reported here: https://bugs.mysql.com/bug.php?id=108528                                   #
# Taken from here:   https://github.com/JZuming/TxCheck/blob/main/docs/mysql_bugs.md            #
# Setup:             mysql_bk_1.sql                                                             #
#################################################################################################

def bug3():
    scenario_0 = """
    T0> SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ;
    T1> SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ;

    T1> START TRANSACTION;
    T1> update t_g6ckkb set wkey = 162;
    T0> START TRANSACTION;
    T0> select * from t_g6ckkb;
    T1> COMMIT;
    T0> select * from t_rpjlsd where t_rpjlsd.c_pfd8ab <= (select min(wkey) from t_g6ckkb); 
    T0> update t_rpjlsd set wkey = 63 where t_rpjlsd.c_pfd8ab <= (select min(wkey) from t_g6ckkb);
    T0> select * from t_rpjlsd where wkey = 63;
    T0> COMMIT;
    """
    scenario_0 = scenario_0.replace("T0>", "conn_0>")
    scenario_0 = scenario_0.replace("T1>", "conn_1>")

    setup_sql_script = context.Context.get_context().data_folder_path / "sql" / "mysql_bk_3.sql"
    bug_runner = bug.Bug(
        bug_id="108528",
        description="https://bugs.mysql.com/bug.php?id=108528",
        db_and_type=db_config.DatabaseTypeAndVersion(db_config.DatabaseType.MYSQL, "8.0.23"),
        scenarios=[scenario_0],
        setup_sql_script=setup_sql_script
    )
    bug_runner.run()