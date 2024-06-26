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
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  BEGIN;
     - TID: 0
     - Output: None
 * Instruction #2:
     - SQL:  SELECT * FROM t WHERE RAND('t');
     - TID: 0
     - Output: [(2,), (1,)]
 * Instruction #3:
     - SQL:  COMMIT;
     - TID: 0
     - Output: None

 * Container logs:
   No logs available.