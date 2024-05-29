# Bug ID 108528 - SERIALIZABLE

## Description

Link:                     https://bugs.mysql.com/bug.php?id=108528
Original isolation level: REPEATABLE READ
Tested isolation level:   SERIALIZABLE


## Details
 * Database: mysql-8.0.23
 * Number of scenarios: 1
 * Initial setup script: /home/theodor/Projects/MasterThesis/data/sql/mysql_bk_3.sql

## Results
### Scenario 0
 * Instruction #0:
     - SQL:  SET SESSION TRANSACTION ISOLATION LEVEL SERIALIZABLE;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  SET SESSION TRANSACTION ISOLATION LEVEL SERIALIZABLE;
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
     - Output: Error: 1205 (HY000): Lock wait timeout exceeded; try restarting transaction
 * Instruction #6:
     - SQL:  COMMIT;
     - TID: 1
     - Output: Skipped due to previous error.
 * Instruction #7:
     - SQL:  select * from t_rpjlsd where t_rpjlsd.c_pfd8ab <= (select min(wkey) from t_g6ck...
     - TID: 0
     - Output: Skipped due to previous error.
 * Instruction #8:
     - SQL:  update t_rpjlsd set wkey = 63 where t_rpjlsd.c_pfd8ab <= (select min(wkey) from...
     - TID: 0
     - Output: Skipped due to previous error.
 * Instruction #9:
     - SQL:  select * from t_rpjlsd where wkey = 63;
     - TID: 0
     - Output: Skipped due to previous error.
 * Instruction #10:
     - SQL:  COMMIT;
     - TID: 0
     - Output: Skipped due to previous error.
