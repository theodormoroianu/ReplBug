# Bug ID MDEV-28140-READ_UNCOMMITTED

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-28140
Original isolation level: REPEATABLE READ
Tested isolation level:   READ UNCOMMITTED
Description:              The second and third scenarios (SELECT and DELETE) should fail like the first one (UPDATE) does.


## Details
 * Database: mariadb-10.8.3
 * Number of scenarios: 3
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  BEGIN;
     - TID: 0
     - Output: None
 * Instruction #2:
     - SQL:  UPDATE t SET c2 = 'test' WHERE c1;
     - TID: 0
     - Output: ERROR: 1292 (22007): Truncated incorrect DOUBLE value: ''
 * Instruction #3:
     - SQL:  COMMIT;
     - TID: 0
     - Output: Skipped due to previous error.

 * Container logs:
   No logs available.

### Scenario 1
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  BEGIN;
     - TID: 0
     - Output: None
 * Instruction #2:
     - SQL:  SELECT * FROM t WHERE c1;
     - TID: 0
     - Output: []
 * Instruction #3:
     - SQL:  COMMIT;
     - TID: 0
     - Output: None

 * Container logs:
   No logs available.

### Scenario 2
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  BEGIN;
     - TID: 0
     - Output: None
 * Instruction #2:
     - SQL:  DELETE FROM t WHERE c1;
     - TID: 0
     - Output: None
 * Instruction #3:
     - SQL:  COMMIT;
     - TID: 0
     - Output: None

 * Container logs:
   No logs available.
