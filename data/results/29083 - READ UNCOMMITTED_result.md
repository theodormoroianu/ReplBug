# Bug ID 29083 - READ UNCOMMITTED

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-29083
Original isolation level: READ COMMITTED
Tested isolation level:   READ UNCOMMITTED


## Details
 * Database: mariadb-10.8.3
 * Number of scenarios: 2
 * Initial setup script: /home/theodor/Projects/MasterThesis/data/sql/mysql_bk_5.sql

## Results
### Scenario 0
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
     - TID: 1
     - Output: None
 * Instruction #2:
     - SQL:  START TRANSACTION;
     - TID: 0
     - Output: None
 * Instruction #3:
     - SQL:  START TRANSACTION;
     - TID: 1
     - Output: None
 * Instruction #4:
     - SQL:  delete from t_euhshb;
     - TID: 1
     - Output: None
 * Instruction #5:
     - SQL:  ROLLBACK;
     - TID: 1
     - Output: None
 * Instruction #6:
     - SQL:  insert into t_7sdcgd values (91, 167000, case when exists ( select * from (t_eu...
     - TID: 0
     - Output: None
 * Instruction #7:
     - SQL:  select * from t_7sdcgd where wkey = 91;
     - TID: 0
     - Output: [(91, 167000, 2.0, 96, 71.64, '1c08ld')]
 * Instruction #8:
     - SQL:  COMMIT;
     - TID: 0
     - Output: None

### Scenario 1
 * Instruction #0:
     - SQL:  insert into t_7sdcgd values (91, 167000, case when exists ( select * from (t_eu...
     - TID: 0
     - Output: Error: 1242 (21000): Subquery returns more than 1 row
 * Instruction #1:
     - SQL:  select * from t_7sdcgd where wkey = 91;
     - TID: 0
     - Output: Skipped due to previous error.