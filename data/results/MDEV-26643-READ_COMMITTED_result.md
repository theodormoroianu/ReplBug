# Bug ID MDEV-26643-READ_COMMITTED

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-26643
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              The first row should be 20, but is 1 (not updated)


## Details
 * Database: mariadb-10.5.12
 * Number of scenarios: 1
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  begin;
     - TID: 0
     - Output: None
 * Instruction #2:
     - SQL:  update t set a = 10 where 1;
     - TID: 0
     - Output: None
 * Instruction #3:
     - SQL:  begin;
     - TID: 1
     - Output: None
 * Instruction #4:
     - SQL:  update t set b = 20 where a;
     - TID: 1
     - Output: None
 * Instruction #5:
     - SQL:  commit;
     - TID: 0
     - Output: None
 * Instruction #6:
     - SQL:  commit;
     - TID: 1
     - Output: None
 * Instruction #7:
     - SQL:  select * from t;
     - TID: 2
     - Output: [(10, 1), (10, 20), (10, 20), (10, 20), (10, 20)]

 * Container logs:
   No logs available.
