# Bug ID MDEV-29585-REPEATABLE_READ

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-29585
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ


## Details
 * Database: mariadb-debug-10.10.1
 * Number of scenarios: 1
 * Initial setup script: /home/theodor/Projects/MasterThesis/data/sql/MDEV-29585_mysql_bk.sql

## Results
### Scenario 0
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  START TRANSACTION;
     - TID: 0
     - Output: None
 * Instruction #2:
     - SQL:  CREATE TABLE `t_rry5a` ( `wkey` int(11) DEFAULT NULL, `pkey` int(11) NOT NULL, ...
     - TID: 0
     - Output: None
 * Instruction #3:
     - SQL:  insert into t_rry5a (wkey, pkey, c_t4jlkc, c_bhsf6d) values (1052, 5800000, 1, ...
     - TID: 0
     - Output: None
 * Instruction #4:
     - SQL:  WITH cte_0 AS (select ref_0.wkey as c0, ref_0.pkey as c1, ref_0.c_t4jlkc as c2,...
     - TID: 0
     - Output: [(1052, 5800000, 1, None, 100.0, None)]
 * Instruction #5:
     - SQL:  WITH cte_0 AS (select ref_0.wkey as c0, ref_0.pkey as c1, ref_0.c_t4jlkc as c2,...
     - TID: 0
     - Output: [(1052, 5800000, 1, None, None, None)]
 * Instruction #6:
     - SQL:  COMMIT;
     - TID: 0
     - Output: None

 * Container logs:
   No logs available.
