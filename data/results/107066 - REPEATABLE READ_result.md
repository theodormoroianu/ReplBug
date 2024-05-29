# Bug ID 107066 - REPEATABLE READ

## Description

Link:                     https://bugs.mysql.com/bug.php?id=107066
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ


## Details
 * Database: mysql-8.0.23
 * Number of scenarios: 2
 * Initial setup script: /home/theodor/Projects/MasterThesis/data/sql/mysql_bk_1.sql

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
     - SQL:  START TRANSACTION;
     - TID: 0
     - Output: None
 * Instruction #4:
     - SQL:  insert into t_zcfqb (wkey, pkey, c_dl_pmd, c_avevqc, c_sqqbbd, c_2wz8nc, c_qyxu...
     - TID: 1
     - Output: None
 * Instruction #5:
     - SQL:  insert into t_zcfqb (wkey, c_rvm_p, c_avevqc, c_ywxlqb, c_sqqbbd, c_2wz8nc, c_q...
     - TID: 0
     - Output: None
 * Instruction #6:
     - SQL:  select pkey from t_zcfqb where wkey = 121;
     - TID: 0
     - Output: Error: 1205 (HY000): Lock wait timeout exceeded; try restarting transaction
 * Instruction #7:
     - SQL:  ROLLBACK;
     - TID: 1
     - Output: Skipped due to previous error.
 * Instruction #8:
     - SQL:  COMMIT;
     - TID: 0
     - Output: Skipped due to previous error.

### Scenario 1
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  START TRANSACTION;
     - TID: 0
     - Output: None
 * Instruction #2:
     - SQL:  insert into t_zcfqb (wkey, c_rvm_p, c_avevqc, c_ywxlqb, c_sqqbbd, c_2wz8nc, c_q...
     - TID: 0
     - Output: None
 * Instruction #3:
     - SQL:  select pkey from t_zcfqb where wkey = 121;
     - TID: 0
     - Output: [(77001,), (77002,), (77003,), (77004,), (77005,), (77006,), (77007,), (77008,), (77009,), (77010,), (77011,), (77012,), (77013,), (77014,), (77015,), (77016,), (77017,), (77018,), (77019,), (77020,), (77021,), (77022,), (77023,), (77024,), (77025,), (77026,), (77027,), (77028,), (77029,), (77030,), (77031,), (77032,), (77033,), (77034,), (77035,), (77036,), (77037,), (77038,), (77039,), (77040,), (77041,), (77042,), (77043,), (77044,), (77045,), (77046,), (77047,), (77048,), (77049,)]
 * Instruction #4:
     - SQL:  COMMIT;
     - TID: 0
     - Output: None
