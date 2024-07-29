# Bug ID MYSQL-114389-READ_COMMITTED

## Description

Link:                     https://bugs.mysql.com/bug.php?id=114389
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              Last SELECT should see no data (because of the update right before it).


## Details
 * Database: mysql-8.0.12
 * Number of scenarios: 1
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
     - Instruction:  BEGIN;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows: 0
 * Instruction #2:
     - Instruction:  BEGIN;
     - Transaction: conn_1
     - Output: None
     - Executed order: 2
     - Affected rows: 0
 * Instruction #3:
     - Instruction:  UPDATE t SET b = 222, c = 333;
     - Transaction: conn_1
     - Output: None
     - Executed order: 3
     - Affected rows: 1
 * Instruction #4:
     - Instruction:  COMMIT;
     - Transaction: conn_1
     - Output: None
     - Executed order: 4
     - Affected rows: 0
 * Instruction #5:
     - Instruction:  BEGIN;
     - Transaction: conn_2
     - Output: None
     - Executed order: 5
     - Affected rows: 0
 * Instruction #6:
     - Instruction:  SELECT pkId, b, c FROM t;
     - Transaction: conn_2
     - Output: [(8, 222, 333)]
     - Executed order: 6
     - Affected rows: 1
 * Instruction #7:
     - Instruction:  UPDATE t SET a = 40 WHERE a = 44;
     - Transaction: conn_0
     - Output: None
     - Executed order: 7
     - Affected rows: 1
 * Instruction #8:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 8
     - Affected rows: 0
 * Instruction #9:
     - Instruction:  UPDATE t SET b = 888, c = 999;
     - Transaction: conn_2
     - Output: None
     - Executed order: 9
     - Affected rows: 1
 * Instruction #10:
     - Instruction:  SELECT pkId, b, c FROM t where b = 854 or c = 333 order by b;
     - Transaction: conn_2
     - Output: []
     - Executed order: 10
     - Affected rows: 0
 * Instruction #11:
     - Instruction:  COMMIT;
     - Transaction: conn_2
     - Output: None
     - Executed order: 11
     - Affected rows: 0

 * Container logs:
   No logs available.
