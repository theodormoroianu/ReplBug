# Bug ID MYSQL-100328-REPEATABLE_READ

## Description

Link:                     https://bugs.mysql.com/bug.php?id=100328
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              UPDATE does not update all records.


## Details
 * Database: mysql-5.7.22
 * Number of scenarios: 1
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
     - Instruction:  select * from t;
     - Transaction: conn_0
     - Output: [(1, 0), (2, 1), (3, 2)]
     - Executed order: 2
     - Affected rows: 3
 * Instruction #3:
     - Instruction:  begin;
     - Transaction: conn_1
     - Output: None
     - Executed order: 3
     - Affected rows: 0
 * Instruction #4:
     - Instruction:  update t set a = 10 where b = 1;
     - Transaction: conn_1
     - Output: None
     - Executed order: 4
     - Affected rows: 1
 * Instruction #5:
     - Instruction:  select * from t;
     - Transaction: conn_1
     - Output: [(1, 0), (10, 1), (3, 2)]
     - Executed order: 5
     - Affected rows: 3
 * Instruction #6:
     - Instruction:  commit;
     - Transaction: conn_1
     - Output: None
     - Executed order: 6
     - Affected rows: 0
 * Instruction #7:
     - Instruction:  select * from t;
     - Transaction: conn_0
     - Output: [(1, 0), (2, 1), (3, 2)]
     - Executed order: 7
     - Affected rows: 3
 * Instruction #8:
     - Instruction:  update t set a = 10 where a;
     - Transaction: conn_0
     - Output: None
     - Executed order: 8
     - Affected rows: 2
 * Instruction #9:
     - Instruction:  select * from t;
     - Transaction: conn_0
     - Output: [(10, 0), (2, 1), (10, 2)]
     - Executed order: 9
     - Affected rows: 3

 * Container logs:
   No logs available.
