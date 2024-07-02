# Bug ID MDEV-28040-READ_UNCOMMITTED

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-28140
Original isolation level: REPEATABLE READ
Tested isolation level:   READ UNCOMMITTED
Description:              The locks are not released in a timely manner. This does not seem to be a bug though.


## Details
 * Database: mariadb-10.8.3
 * Number of scenarios: 1
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
 * Instruction #1:
     - Instruction:  BEGIN;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
 * Instruction #2:
     - Instruction:  UPDATE t SET c2='test' WHERE c1;
     - Transaction: conn_0
     - Output: ERROR: 1292 (22007): Truncated incorrect DOUBLE value: ''
     - Executed order: Not executed
 * Instruction #3:
     - Instruction:  BEGIN;
     - Transaction: conn_1
     - Output: None
     - Executed order: 2
 * Instruction #4:
     - Instruction:  UPDATE t SET c2 = 'def';
     - Transaction: conn_1
     - Output: None
     - Executed order: 4
 * Instruction #5:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
 * Instruction #6:
     - Instruction:  COMMIT;
     - Transaction: conn_1
     - Output: None
     - Executed order: 5

 * Container logs:
   No logs available.
