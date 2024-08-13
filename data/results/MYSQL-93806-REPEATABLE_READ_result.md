# Bug ID MYSQL-93806-REPEATABLE_READ

## Description

Link:                     https://bugs.mysql.com/bug.php?id=93806
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              Exclusive range locks are created when using ON DUPLICATE KEY UPDATE (and the update takes place)


## Details
 * Database: mysql-8.0.12
 * Number of scenarios: 2
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
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
     - Instruction:  insert into t values(5,5) ON DUPLICATE KEY UPDATE a=a+1;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows: 2
 * Instruction #3:
     - Instruction:  begin;
     - Transaction: conn_1
     - Output: None
     - Executed order: 3
     - Affected rows: 0
 * Instruction #4:
     - Instruction:  insert into t values(4, 4);
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

### Scenario 1
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
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
     - Instruction:  insert into t values(6,6) ON DUPLICATE KEY UPDATE a=a+1;
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
     - Instruction:  insert into t values(4, 4);
     - Transaction: conn_1
     - Output: None
     - Executed order: 4
     - Affected rows: 1
 * Instruction #5:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: None
     - Executed order: 5
     - Affected rows: 0
 * Instruction #6:
     - Instruction:  commit;
     - Transaction: conn_1
     - Output: None
     - Executed order: 6
     - Affected rows: 0

 * Container logs:
   No logs available.
