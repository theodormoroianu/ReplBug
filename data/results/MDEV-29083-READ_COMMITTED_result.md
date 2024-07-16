# Bug ID MDEV-29083-READ_COMMITTED

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-29083
Original isolation level: READ COMMITTED
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
     - Affected rows / Warnings: 0 / 0
 * Instruction #1:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
     - Transaction: conn_1
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 0 / 0
 * Instruction #3:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_1
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 0 / 0
 * Instruction #4:
     - Instruction:  delete from t_euhshb;
     - Transaction: conn_1
     - Output: None
     - Executed order: 4
     - Affected rows / Warnings: 41 / 0
 * Instruction #5:
     - Instruction:  ROLLBACK;
     - Transaction: conn_1
     - Output: None
     - Executed order: 5
     - Affected rows / Warnings: 0 / 0
 * Instruction #6:
     - Instruction:  insert into t_7sdcgd values (91, 167000, case when exists ( select * from (t_eu...
     - Transaction: conn_0
     - Output: None
     - Executed order: 6
     - Affected rows / Warnings: 1 / 0
 * Instruction #7:
     - Instruction:  select * from t_7sdcgd where wkey = 91;
     - Transaction: conn_0
     - Output: [(91, 167000, 2.0, 96, 71.64, '1c08ld')]
     - Executed order: 7
     - Affected rows / Warnings: 1 / 0
 * Instruction #8:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 8
     - Affected rows / Warnings: 0 / 0

 * Container logs:
   No logs available.

### Scenario 1
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 0 / 0
 * Instruction #1:
     - Instruction:  insert into t_7sdcgd values (91, 167000, case when exists ( select * from (t_eu...
     - Transaction: conn_0
     - Output: ERROR: 1242 (21000): Subquery returns more than 1 row
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #2:
     - Instruction:  select * from t_7sdcgd where wkey = 91;
     - Transaction: conn_0
     - Output: []
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0

 * Container logs:
   No logs available.
