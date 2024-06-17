# Bug ID MDEV-29243-SERIALIZABLE

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-29243
Original isolation level: REPEATABLE READ
Tested isolation level:   SERIALIZABLE


## Details
 * Database: mariadb-debug-10.8.3
 * Number of scenarios: 1
 * Initial setup script: /home/theodor/Projects/MasterThesis/data/sql/MDEV-29243_mysql_bk.sql

## Results
### Scenario 0
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
     - TID: 1
     - Output: None
 * Instruction #2:
     - SQL:  START TRANSACTION;
     - TID: 1
     - Output: None
 * Instruction #3:
     - SQL:  START TRANSACTION;
     - TID: 0
     - Output: None
 * Instruction #4:
     - SQL:  delete from t_swbayb;
     - TID: 1
     - Output: None
 * Instruction #5:
     - SQL:  insert into t_swbayb (wkey, pkey) values (88, 74000);
     - TID: 0
     - Output: None
 * Instruction #6:
     - SQL:  insert into t_8fjoxb (wkey, pkey, c_yecif) values (110, 115000, case when exist...
     - TID: 1
     - Output: None
 * Instruction #7:
     - SQL:  insert into t_swbayb (wkey, pkey, c_ywdp4d) values (90, 83000, 'vyenkd');
     - TID: 0
     - Output: None
 * Instruction #8:
     - SQL:  COMMIT;
     - TID: 0
     - Output: None
 * Instruction #9:
     - SQL:  COMMIT;
     - TID: 1
     - Output: None

 * Container logs:
   No logs available.
