# Bug ID MDEV-24545-READ_UNCOMMITTED

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-24545
Original isolation level: REPEATABLE READ
Tested isolation level:   READ UNCOMMITTED
Description:              Second SELECT NEXTVAL is in the global scope, and should find the sequence S1.


## Details
 * Database: mariadb-10.3.28
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
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  SELECT * FROM t1;
     - Transaction: conn_0
     - Output: []
     - Executed order: 2
     - Affected rows / Warnings: 0 / 0
 * Instruction #3:
     - Instruction:  CREATE SEQUENCE s1 ENGINE=InnoDB;
     - Transaction: conn_1
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 0 / 0
 * Instruction #4:
     - Instruction:  FLUSH TABLES;
     - Transaction: conn_1
     - Output: None
     - Executed order: 4
     - Affected rows / Warnings: 0 / 0
 * Instruction #5:
     - Instruction:  SELECT NEXTVAL(s1);
     - Transaction: conn_0
     - Output: ERROR: 1146 (42S02): Table 'testdb.s1' doesn't exist
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #6:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 5
     - Affected rows / Warnings: 0 / 0
 * Instruction #7:
     - Instruction:  SELECT NEXTVAL(s1);
     - Transaction: conn_0
     - Output: ERROR: 1146 (42S02): Table 'testdb.s1' doesn't exist
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0

 * Container logs:
   No logs available.
