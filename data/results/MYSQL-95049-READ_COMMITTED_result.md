# Bug ID MYSQL-95049-READ_COMMITTED

## Description

Link:                     https://bugs.mysql.com/bug.php?id=95049
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              Locks are relased on rollback, even though documentation specifies they shouldn't.


## Details
 * Database: mysql-8.0.39
 * Number of scenarios: 2
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows: 0
 * Instruction #1:
     - Instruction:  begin;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows: 0
 * Instruction #2:
     - Instruction:  SAVEPOINT somepoint;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows: 0
 * Instruction #3:
     - Instruction:  UPDATE person SET age = 30 WHERE id = 1;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows: 1
 * Instruction #4:
     - Instruction:  ROLLBACK TO somepoint;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows: 0
 * Instruction #5:
     - Instruction:  begin;
     - Transaction: conn_1
     - Output: None
     - Executed order: 5
     - Affected rows: 0
 * Instruction #6:
     - Instruction:  UPDATE person SET age = 40 WHERE id = 1;
     - Transaction: conn_1
     - Output: None
     - Executed order: 6
     - Affected rows: 1
 * Instruction #7:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: None
     - Executed order: 7
     - Affected rows: 0

 * Container logs:
   No logs available.

### Scenario 1
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows: 0
 * Instruction #1:
     - Instruction:  begin;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows: 0
 * Instruction #2:
     - Instruction:  UPDATE person SET age = 30 WHERE id = 1;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows: 1
 * Instruction #3:
     - Instruction:  begin;
     - Transaction: conn_1
     - Output: None
     - Executed order: 3
     - Affected rows: 0
 * Instruction #4:
     - Instruction:  UPDATE person SET age = 40 WHERE id = 1;
     - Transaction: conn_1
     - Output: None
     - Executed order: 5
     - Affected rows: 1
 * Instruction #5:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows: 0
 * Instruction #6:
     - Instruction:  commit;
     - Transaction: conn_1
     - Output: None
     - Executed order: 6
     - Affected rows: 0

 * Container logs:
   No logs available.
