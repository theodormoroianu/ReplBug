# Bug ID MYSQL-107066-READ_COMMITTED

## Description

Link:                     https://bugs.mysql.com/bug.php?id=107066
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED


## Details
 * Database: mysql-8.0.23
 * Number of scenarios: 2
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
 * Instruction #1:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
     - Transaction: conn_1
     - Output: None
     - Executed order: 1
 * Instruction #2:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_1
     - Output: None
     - Executed order: 2
 * Instruction #3:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
 * Instruction #4:
     - Instruction:  insert into t_zcfqb (wkey, pkey, c_dl_pmd, c_avevqc, c_sqqbbd, c_2wz8nc, c_qyxu...
     - Transaction: conn_1
     - Output: None
     - Executed order: 4
 * Instruction #5:
     - Instruction:  insert into t_zcfqb (wkey, c_rvm_p, c_avevqc, c_ywxlqb, c_sqqbbd, c_2wz8nc, c_q...
     - Transaction: conn_0
     - Output: None
     - Executed order: 5
 * Instruction #6:
     - Instruction:  select pkey from t_zcfqb where wkey = 121;
     - Transaction: conn_0
     - Output: [(264001,), (264002,), (264003,), (264004,), (264005,), (264006,), (264007,), (264008,), (264009,), (264010,), (264011,), (264012,), (264013,), (264014,), (264015,), (264016,), (264017,), (264018,), (264019,), (264020,), (264021,), (264022,), (264023,), (264024,), (264025,), (264026,), (264027,), (264028,), (264029,), (264030,), (264031,), (264032,), (264033,), (264034,), (264035,), (264036,), (264037,), (264038,), (264039,), (264040,), (264041,), (264042,), (264043,), (264044,), (264045,), (264046,), (264047,), (264048,), (264049,)]
     - Executed order: 6
 * Instruction #7:
     - Instruction:  ROLLBACK;
     - Transaction: conn_1
     - Output: None
     - Executed order: 7
 * Instruction #8:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 8

 * Container logs:
   No logs available.

### Scenario 1
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
 * Instruction #1:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
 * Instruction #2:
     - Instruction:  insert into t_zcfqb (wkey, c_rvm_p, c_avevqc, c_ywxlqb, c_sqqbbd, c_2wz8nc, c_q...
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
 * Instruction #3:
     - Instruction:  select pkey from t_zcfqb where wkey = 121;
     - Transaction: conn_0
     - Output: [(77001,), (77002,), (77003,), (77004,), (77005,), (77006,), (77007,), (77008,), (77009,), (77010,), (77011,), (77012,), (77013,), (77014,), (77015,), (77016,), (77017,), (77018,), (77019,), (77020,), (77021,), (77022,), (77023,), (77024,), (77025,), (77026,), (77027,), (77028,), (77029,), (77030,), (77031,), (77032,), (77033,), (77034,), (77035,), (77036,), (77037,), (77038,), (77039,), (77040,), (77041,), (77042,), (77043,), (77044,), (77045,), (77046,), (77047,), (77048,), (77049,)]
     - Executed order: 3
 * Instruction #4:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4

 * Container logs:
   No logs available.
