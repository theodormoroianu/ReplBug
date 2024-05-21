import testcase.bugs.bug1 as bug1
import database.config as db_config
import database.provide_database_server as db_provider


def my_test():
    with db_provider.DatabaseProvider(db_provider.DatabaseTypeAndVersion(db_config.DatabaseType.MYSQL, "8.0.28")) as provider:
        conn = provider.database_connection.to_connection()
        conn.cursor().execute("create database testdb;")
        conn.cursor().execute("use testdb;")
        results = conn.cursor().execute("""
CREATE TABLE `t_zcfqb` (
  `wkey` int(11) DEFAULT NULL,
  `pkey` int(11) NOT NULL AUTO_INCREMENT,
  `c_rvm_p` text DEFAULT NULL,
  `c_dl_pmd` int(11) DEFAULT NULL,
  `c_avevqc` text DEFAULT NULL,
  `c_ywxlqb` double DEFAULT NULL,
  `c_sqqbbd` int(11) DEFAULT NULL,
  `c_2wz8nc` text DEFAULT NULL,
  `c_qyxu0` double DEFAULT NULL,
  `c_slu2bd` int(11) DEFAULT NULL,
  `c_ph8nh` text DEFAULT NULL,
  PRIMARY KEY (`pkey`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=77001;
""", multi=True)
        for cur in results:
            print('cursor:', cur)
            if cur.with_rows:
                print('result:', cur.fetchall())
    
        conn.commit()

        conn2 = provider.database_connection.to_connection()
        conn2.cursor().execute("use testdb;")
        cursor = conn2.cursor()
        cursor.execute("select * from `t_zcfqb`;")
        print(cursor.fetchall())
        

def test():
    # my_test()
    bug1.run()