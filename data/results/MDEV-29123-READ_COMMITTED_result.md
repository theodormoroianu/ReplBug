# Bug ID MDEV-29123-READ_COMMITTED

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-29123
Original isolation level: REPETABLE READ
Tested isolation level:   IsolationLevel.READ_COMMITTED


## Details
 * Database: mariadb-10.8.3
 * Number of scenarios: 2
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
 * Instruction #1:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
     - Transaction: conn_1
     - Output: None
     - Executed order: 1
 * Instruction #2:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_1
     - Output: None
     - Executed order: 2
 * Instruction #3:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
 * Instruction #4:
     - Instruction:  insert into t_4rbssc (wkey, pkey, c_qrgwb, c_8u7ipc, c_mqgwfb, c_7j_zjb) values...
     - Transaction: conn_1
     - Output: None
     - Executed order: 4
 * Instruction #5:
     - Instruction:  ROLLBACK;
     - Transaction: conn_1
     - Output: None
     - Executed order: 5
 * Instruction #6:
     - Instruction:  select * from t_4rbssc where t_4rbssc.wkey = 4 and t_4rbssc.c_sbxs3c not in ( s...
     - Transaction: conn_0
     - Output: [(4, 34000, '4bquu', 'entwob', 87, 84.64, 93, 5, 'glalkc', 47), (4, 36000, '_wacsb', '3_7us', 100, 91.97, 77, 51, 'mf8txb', 79), (4, 37000, 'obkbfb', 'ku0pmd', 74, 97.73, 47, 41, None, 19), (4, 38000, 'yzdmqb', 'sfxi_c', 66, 22.93, 79, 96, 'xjkqb', 56)]
     - Executed order: 6
 * Instruction #7:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 7

 * Container logs:
   No logs available.

### Scenario 1
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
 * Instruction #1:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
 * Instruction #2:
     - Instruction:  select * from t_4rbssc where t_4rbssc.wkey = 4 and t_4rbssc.c_sbxs3c not in ( s...
     - Transaction: conn_0
     - Output: [(4, 35000, '2w5lsc', None, 6, 42.97, 86, 1, 'evgzfc', 77), (4, 36000, '_wacsb', '3_7us', 100, 91.97, 77, 51, 'mf8txb', 79), (4, 37000, 'obkbfb', 'ku0pmd', 74, 97.73, 47, 41, None, 19), (4, 38000, 'yzdmqb', 'sfxi_c', 66, 22.93, 79, 96, 'xjkqb', 56)]
     - Executed order: 2
 * Instruction #3:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3

 * Container logs:
   No logs available.
