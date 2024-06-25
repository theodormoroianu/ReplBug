# Bug ID MDEV-27992-SERIALIZABLE

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-27992
Original isolation level: REPEATABLE READ
Tested isolation level:   SERIALIZABLE
Description:              The delete from conn_1 should block, wait for conn_0 to commit, and then delete everything. But it doesn't.


## Details
 * Database: mariadb-10.7.3
 * Number of scenarios: 1
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  BEGIN;
     - TID: 0
     - Output: None
 * Instruction #2:
     - SQL:  BEGIN;
     - TID: 1
     - Output: None
 * Instruction #3:
     - SQL:  UPDATE t SET c1 = 5, c2 = 5;
     - TID: 0
     - Output: None
 * Instruction #4:
     - SQL:  DELETE FROM t;
     - TID: 1
     - Output: None
 * Instruction #5:
     - SQL:  UPDATE t SET c1 = 3;
     - TID: 0
     - Output: None
 * Instruction #6:
     - SQL:  COMMIT;
     - TID: 0
     - Output: None
 * Instruction #7:
     - SQL:  SELECT * FROM t FOR UPDATE;
     - TID: 1
     - Output: [(3, 5)]
 * Instruction #8:
     - SQL:  ROLLBACK;
     - TID: 1
     - Output: None

 * Container logs:
   No logs available.
