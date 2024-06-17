# Bug ID MDEV-29565-REPEATABLE_READ

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-29565
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ


## Details
 * Database: mariadb-debug-10.10.1
 * Number of scenarios: 1
 * Initial setup script: /home/theodor/Projects/MasterThesis/data/sql/MDEV-29565_mysql_bk.sql

## Results
### Scenario 0
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - TID: 1
     - Output: None
 * Instruction #2:
     - SQL:  START TRANSACTION;
     - TID: 1
     - Output: None
 * Instruction #3:
     - SQL:  update t_g6ckkb set wkey = 162;
     - TID: 1
     - Output: None
 * Instruction #4:
     - SQL:  START TRANSACTION;
     - TID: 0
     - Output: None
 * Instruction #5:
     - SQL:  select * from t_g6ckkb;
     - TID: 0
     - Output: [(20, 234000, None, 'aarauc', 'btldnb', 37.9, '7wa_b', None, 32.5), (56, 327000, 65, 'kavsib', 'ga9slb', 54.9, None, 'xlbvfd', 79.9)]
 * Instruction #6:
     - SQL:  COMMIT;
     - TID: 1
     - Output: None
 * Instruction #7:
     - SQL:  select * from t_rpjlsd where t_rpjlsd.c_pfd8ab <= (select min(wkey) from t_g6ck...
     - TID: 0
     - Output: [(43, 243000, 30, None, 8, None, 70, None, 'awnrab', 39.83)]
 * Instruction #8:
     - SQL:  update t_rpjlsd set wkey = 63 where t_rpjlsd.c_pfd8ab <= (select min(wkey) from...
     - TID: 0
     - Output: None
 * Instruction #9:
     - SQL:  select * from t_rpjlsd where wkey = 63;
     - TID: 0
     - Output: [(63, 243000, 30, None, 8, None, 70, None, 'awnrab', 39.83), (63, 332000, 68, '_pqr1c', 53, '9g7bt', None, 75, 'tb1ugc', 7.62)]
 * Instruction #10:
     - SQL:  COMMIT;
     - TID: 0
     - Output: None

 * Container logs:
   No logs available.
