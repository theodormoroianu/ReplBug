# Bug ID MDEV-29120 - READ UNCOMMITTED

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-29120
Original isolation level: REPETABLE READ
Tested isolation level:   READ UNCOMMITTED


## Details
 * Database: mysql-8.0.35
 * Number of scenarios: 1
 * Initial setup script: /home/theodor/Projects/MasterThesis/data/sql/mysql_bk_6.sql

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
     - SQL:  insert into t_yynypc (wkey, pkey, c_acfajc) values (89, 188000, 40), (89, 18900...
     - TID: 1
     - Output: None
 * Instruction #5:
     - SQL:  delete from t_qrsdpb where exists ( select ref_0.c_bkmkf as c2 from t_zefkic as...
     - TID: 0
     - Output: Error: 1205 (HY000): Lock wait timeout exceeded; try restarting transaction
 * Instruction #6:
     - SQL:  update t_zefkic set wkey = 99;
     - TID: 1
     - Output: Skipped due to previous error.
 * Instruction #7:
     - SQL:  ROLLBACK;
     - TID: 0
     - Output: Skipped due to previous error.
 * Instruction #8:
     - SQL:  ROLLBACK;
     - TID: 1
     - Output: Skipped due to previous error.