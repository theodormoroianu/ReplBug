# Bug ID MDEV-28142-READ_UNCOMMITTED

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-28142
Original isolation level: REPEATABLE READ
Tested isolation level:   READ UNCOMMITTED
Description:              Should not throw an error on the third scenario.


## Details
 * Database: mariadb-10.7.3
 * Number of scenarios: 1
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 0 / 0
 * Instruction #1:
     - Instruction:  start transaction;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  UPDATE t SET c1 = 'b' WHERE CAST(IF('a', '1', 1) AS SIGNED);
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 1 / 1
 * Instruction #3:
     - Instruction:  SELECT * FROM t;
     - Transaction: conn_0
     - Output: [('b',)]
     - Executed order: 3
     - Affected rows / Warnings: 1 / 0
 * Instruction #4:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows / Warnings: 0 / 0

 * Container logs:
   No logs available.
