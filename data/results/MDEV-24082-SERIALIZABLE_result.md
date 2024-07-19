# Bug ID MDEV-24082-SERIALIZABLE

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-24082
Original isolation level: REPEATABLE READ
Tested isolation level:   SERIALIZABLE
Description:              This fails with 'Cannot execute statement in a READ ONLY transaction', despite only attempting to update the temporary table. However, if you modify the UPDATE to use a subquery instead of a join, it works.


## Details
 * Database: mariadb-10.1.38
 * Number of scenarios: 2
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
     - Instruction:  BEGIN;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  CREATE TEMPORARY TABLE t (id int unsigned NOT NULL PRIMARY KEY,flag tinyint NOT...
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 0 / 0
 * Instruction #3:
     - Instruction:  INSERT INTO t (id) VALUES (1),(2),(3),(4),(5);
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 5 / 0
 * Instruction #4:
     - Instruction:  START TRANSACTION READ ONLY;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows / Warnings: 0 / 0
 * Instruction #5:
     - Instruction:  UPDATE t INNER JOIN p USING (id) SET t.flag=1;
     - Transaction: conn_0
     - Output: ERROR: 1792 (25006): Cannot execute statement in a READ ONLY transaction.
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #6:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 5
     - Affected rows / Warnings: 0 / 0

 * Container logs:
   No logs available.

### Scenario 1
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 0 / 0
 * Instruction #1:
     - Instruction:  BEGIN;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  CREATE TEMPORARY TABLE t (id int unsigned NOT NULL PRIMARY KEY,flag tinyint NOT...
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 0 / 0
 * Instruction #3:
     - Instruction:  INSERT INTO t (id) VALUES (1),(2),(3),(4),(5);
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 5 / 0
 * Instruction #4:
     - Instruction:  START TRANSACTION READ ONLY;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows / Warnings: 0 / 0
 * Instruction #5:
     - Instruction:  UPDATE t SET t.flag=1 WHERE id IN (SELECT id FROM p);
     - Transaction: conn_0
     - Output: None
     - Executed order: 5
     - Affected rows / Warnings: 1 / 0
 * Instruction #6:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 6
     - Affected rows / Warnings: 0 / 0

 * Container logs:
   No logs available.
