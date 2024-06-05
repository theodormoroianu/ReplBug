# Bug ID MDEV-29123-READ_COMMITTED

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-29123
Original isolation level: REPETABLE READ
Tested isolation level:   IsolationLevel.READ_COMMITTED


## Details
 * Database: mariadb-debug-10.8.3
 * Number of scenarios: 2
 * Initial setup script: /home/theodor/Projects/MasterThesis/data/sql/MDEV-29123_mysql_bk.sql

## Results
### Scenario 0
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
     - TID: 1
     - Output: None
 * Instruction #2:
     - SQL:  START TRANSACTION;
     - TID: 1
     - Output: None
 * Instruction #3:
     - SQL:  START TRANSACTION;
     - TID: 0
     - Output: None
 * Instruction #4:
     - SQL:  insert into t_4rbssc (wkey, pkey, c_qrgwb, c_8u7ipc, c_mqgwfb, c_7j_zjb) values...
     - TID: 1
     - Output: None
 * Instruction #5:
     - SQL:  ROLLBACK;
     - TID: 1
     - Output: None
 * Instruction #6:
     - SQL:  select * from t_4rbssc where t_4rbssc.wkey = 4 and t_4rbssc.c_sbxs3c not in ( s...
     - TID: 0
     - Output: [(4, 34000, '4bquu', 'entwob', 87, 84.64, 93, 5, 'glalkc', 47), (4, 36000, '_wacsb', '3_7us', 100, 91.97, 77, 51, 'mf8txb', 79), (4, 37000, 'obkbfb', 'ku0pmd', 74, 97.73, 47, 41, None, 19), (4, 38000, 'yzdmqb', 'sfxi_c', 66, 22.93, 79, 96, 'xjkqb', 56)]
 * Instruction #7:
     - SQL:  COMMIT;
     - TID: 0
     - Output: None

 * Container logs:
   No logs available.

### Scenario 1
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  START TRANSACTION;
     - TID: 0
     - Output: None
 * Instruction #2:
     - SQL:  select * from t_4rbssc where t_4rbssc.wkey = 4 and t_4rbssc.c_sbxs3c not in ( s...
     - TID: 0
     - Output: [(4, 35000, '2w5lsc', None, 6, 42.97, 86, 1, 'evgzfc', 77), (4, 36000, '_wacsb', '3_7us', 100, 91.97, 77, 51, 'mf8txb', 79), (4, 37000, 'obkbfb', 'ku0pmd', 74, 97.73, 47, 41, None, 19), (4, 38000, 'yzdmqb', 'sfxi_c', 66, 22.93, 79, 96, 'xjkqb', 56)]
 * Instruction #3:
     - SQL:  COMMIT;
     - TID: 0
     - Output: None

 * Container logs:
   No logs available.
