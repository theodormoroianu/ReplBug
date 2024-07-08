# Bug ID MDEV-24083-READ_UNCOMMITTED

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-24083
Original isolation level: REPEATABLE READ
Tested isolation level:   READ UNCOMMITTED
Description:              DDL should be allowed in read-only transactions.


## Details
 * Database: mariadb-10.1.48
 * Number of scenarios: 1
 * Initial setup script: No

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 0 / 0
 * Instruction #1:
     - Instruction:  START TRANSACTION READ ONLY;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  CREATE TEMPORARY TABLE t (id int unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,v...
     - Transaction: conn_0
     - Output: ERROR: 1792 (25006): Cannot execute statement in a READ ONLY transaction.
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #3:
     - Instruction:  INSERT INTO t (val) VALUES (22),(96),(47),(5),(22);
     - Transaction: conn_0
     - Output: ERROR: 1792 (25006): Cannot execute statement in a READ ONLY transaction.
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #4:
     - Instruction:  SELECT * FROM t;
     - Transaction: conn_0
     - Output: ERROR: 1146 (42S02): Table 'testdb.t' doesn't exist
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #5:
     - Instruction:  DROP TEMPORARY TABLE t;
     - Transaction: conn_0
     - Output: ERROR: 1792 (25006): Cannot execute statement in a READ ONLY transaction.
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #6:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 0 / 0

 * Container logs:
   No logs available.
