# Bug ID MDEV-27992-REPEATABLE_READ

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-27992
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              The delete from conn_1 should block, wait for conn_0 to commit, and then delete everything. But it doesn't.


## Details
 * Database: mariadb-10.7.3
 * Number of scenarios: 1
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
 * Instruction #1:
     - Instruction:  BEGIN;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
 * Instruction #2:
     - Instruction:  BEGIN;
     - Transaction: conn_1
     - Output: None
     - Executed order: 2
 * Instruction #3:
     - Instruction:  UPDATE t SET c1 = 5, c2 = 5;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
 * Instruction #4:
     - Instruction:  DELETE FROM t;
     - Transaction: conn_1
     - Output: None
     - Executed order: 5
 * Instruction #5:
     - Instruction:  UPDATE t SET c1 = 3;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
 * Instruction #6:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 6
 * Instruction #7:
     - Instruction:  SELECT * FROM t FOR UPDATE;
     - Transaction: conn_1
     - Output: [(3, 5)]
     - Executed order: 7
 * Instruction #8:
     - Instruction:  ROLLBACK;
     - Transaction: conn_1
     - Output: None
     - Executed order: 8

 * Container logs:
   No logs available.
