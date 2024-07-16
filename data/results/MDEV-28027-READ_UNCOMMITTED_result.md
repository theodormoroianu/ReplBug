# Bug ID MDEV-28027-READ_UNCOMMITTED

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-28027
Original isolation level: REPEATABLE READ
Tested isolation level:   READ UNCOMMITTED
Description:              Mismatch between MySQL and MariaDB: in Mariadb, RAND('t') is true only if >= 0.5. Record 1 is skipped.


## Details
 * Database: mariadb-10.8.3
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
     - Instruction:  BEGIN;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  SELECT * FROM t WHERE RAND('t');
     - Transaction: conn_0
     - Output: [(2,), (1,)]
     - Executed order: 2
     - Affected rows / Warnings: 2 / 1
 * Instruction #3:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 0 / 0

 * Container logs:
   No logs available.
