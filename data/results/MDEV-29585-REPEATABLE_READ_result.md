# Bug ID MDEV-29585-REPEATABLE_READ

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-29585
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ


## Details
 * Database: mariadb-10.8.3
 * Number of scenarios: 1
 * Initial setup script: No

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
 * Instruction #1:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
 * Instruction #2:
     - Instruction:  CREATE TABLE `t_rry5a` ( `wkey` int(11) DEFAULT NULL, `pkey` int(11) NOT NULL, ...
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
 * Instruction #3:
     - Instruction:  insert into t_rry5a (wkey, pkey, c_t4jlkc, c_bhsf6d) values (1052, 5800000, 1, ...
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
 * Instruction #4:
     - Instruction:  WITH cte_0 AS (select ref_0.wkey as c0, ref_0.pkey as c1, ref_0.c_t4jlkc as c2,...
     - Transaction: conn_0
     - Output: [(1052, 5800000, 1, None, 100.0, None)]
     - Executed order: 4
 * Instruction #5:
     - Instruction:  WITH cte_0 AS (select ref_0.wkey as c0, ref_0.pkey as c1, ref_0.c_t4jlkc as c2,...
     - Transaction: conn_0
     - Output: [(1052, 5800000, 1, None, None, None)]
     - Executed order: 5
 * Instruction #6:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 6

 * Container logs:
   No logs available.
