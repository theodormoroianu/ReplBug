# Bug ID MDEV-26642-REPEATABLE_READ

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-26642
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              The last select does not respect the update (a should always be 10).


## Details
 * Database: mariadb-10.6.17
 * Number of scenarios: 1
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 0 / 0
 * Instruction #1:
     - Instruction:  begin;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  select * from t;
     - Transaction: conn_0
     - Output: [(0, 0), (1, 1), (2, 2)]
     - Executed order: 2
     - Affected rows / Warnings: 3 / 0
 * Instruction #3:
     - Instruction:  begin;
     - Transaction: conn_1
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 0 / 0
 * Instruction #4:
     - Instruction:  update t set a = 10 where b = 1;
     - Transaction: conn_1
     - Output: None
     - Executed order: 4
     - Affected rows / Warnings: 1 / 0
 * Instruction #5:
     - Instruction:  commit;
     - Transaction: conn_1
     - Output: None
     - Executed order: 5
     - Affected rows / Warnings: 0 / 0
 * Instruction #6:
     - Instruction:  select * from t;
     - Transaction: conn_0
     - Output: [(0, 0), (1, 1), (2, 2)]
     - Executed order: 6
     - Affected rows / Warnings: 3 / 0
 * Instruction #7:
     - Instruction:  update t set a = 10 where true;
     - Transaction: conn_0
     - Output: None
     - Executed order: 7
     - Affected rows / Warnings: 2 / 0
 * Instruction #8:
     - Instruction:  select * from t;
     - Transaction: conn_0
     - Output: [(10, 0), (1, 1), (10, 2)]
     - Executed order: 8
     - Affected rows / Warnings: 3 / 0
 * Instruction #9:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: None
     - Executed order: 9
     - Affected rows / Warnings: 0 / 0

 * Container logs:
   No logs available.
