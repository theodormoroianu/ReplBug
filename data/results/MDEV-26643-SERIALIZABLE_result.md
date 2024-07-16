# Bug ID MDEV-26643-SERIALIZABLE

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-26643
Original isolation level: REPEATABLE READ
Tested isolation level:   SERIALIZABLE
Description:              The first row should be 20, but is 1 (not updated)


## Details
 * Database: mariadb-10.5.12
 * Number of scenarios: 1
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
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
     - Instruction:  update t set a = 10 where 1;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 5 / 0
 * Instruction #3:
     - Instruction:  begin;
     - Transaction: conn_1
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 0 / 0
 * Instruction #4:
     - Instruction:  update t set b = 20 where a;
     - Transaction: conn_1
     - Output: None
     - Executed order: 4
     - Affected rows / Warnings: 5 / 0
 * Instruction #5:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: None
     - Executed order: 5
     - Affected rows / Warnings: 0 / 0
 * Instruction #6:
     - Instruction:  commit;
     - Transaction: conn_1
     - Output: None
     - Executed order: 6
     - Affected rows / Warnings: 0 / 0
 * Instruction #7:
     - Instruction:  select * from t;
     - Transaction: conn_2
     - Output: [(10, 20), (10, 20), (10, 20), (10, 20), (10, 20)]
     - Executed order: 7
     - Affected rows / Warnings: 5 / 0

 * Container logs:
   No logs available.
