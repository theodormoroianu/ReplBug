# Bug ID 107898 - SERIALIZABLE

## Description

Link:                     https://bugs.mysql.com/bug.php?id=107898
Original isolation level: READ COMMITTED
Tested isolation level:   SERIALIZABLE


## Details
 * Database: mysql-8.0.23
 * Number of scenarios: 2
 * Initial setup script: /home/theodor/Projects/MasterThesis/data/sql/mysql_bk_2.sql

## Results
### Scenario 0
 * Instruction #0:
     - SQL:  SET LOCAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  SET LOCAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
     - TID: 1
     - Output: None
 * Instruction #2:
     - SQL:  START TRANSACTION;
     - TID: 0
     - Output: None
 * Instruction #3:
     - SQL:  START TRANSACTION; delete from t_8fhx8c; ROLLBACK;
     - TID: 1
     - Output: None
 * Instruction #4:
     - SQL:  select * from t_8fhx8c as ref_1 where ref_1.c_0byzvd not in ( select nullif(19,...
     - TID: 0
     - Output: [(2, 14000, 97, 84.74, 'wa2sbb', 95, 89.41), (2, 15000, 86, 21.11, 'zronkb', 55, 45.8), (2, 16000, 14, 19.5, 'c2gzzd', 32, 85.98), (2, 17000, 23, 33.44, 'mobljd', 66, 23.38), (3, 18000, 50, None, 'pturvb', 12, 80.12), (3, 19000, 12, 3.67, 'if_bxd', 1, 52.88), (3, 20000, 43, 23.93, None, 20, 9.64), (3, 21000, 66, 53.85, 'n_wqod', 1, 86.49), (3, 22000, 35, 32.75, '0mbqjc', 44, 66.48), (4, 23000, 14, None, 'ucm2td', 8, 35.2), (4, 24000, 46, 29.29, 'tkrorb', 13, 23.69), (4, 25000, 57, 58.4, 'la5xxd', 42, 80.53), (4, 26000, 11, 71.71, 'emyb3b', 32, 19.24), (4, 27000, 18, 16.46, 'cuf0n', 62, 91.78), (4, 28000, 90, 80.69, 'cgded', 75, 66.99), (4, 29000, 42, 4.37, 'yuhutd', 61, 11.3), (4, 30000, 63, 97.37, 'shdmzb', 3, 44.82), (10, 59000, 33, 5.21, None, None, 81.83), (10, 60000, 95, 35.57, None, None, 26.78), (10, 61000, 24, 13.46, None, None, 97.26), (10, 62000, 35, 84.89, None, None, 44.5), (10, 63000, 83, 69.34, None, None, 14.19), (10, 64000, 26, 29.59, None, None, 60.27), (11, 65000, 8, None, '8ppsvb', 84, 97.47), (11, 66000, 55, None, 'naaqhd', 38, 4.17), (11, 67000, 78, None, 'sm4vmb', 60, 98.6), (12, 68000, 98, 24.37, 'y9oowb', None, 79.54), (12, 69000, 97, 50.1, 'qqabc', None, 62.34), (12, 70000, 18, 87.87, 'wkf9h', None, 76.7), (12, 71000, 37, 5.2, 'npgb8', None, 95.63), (12, 72000, 48, 83.8, 'xhx3rb', None, 51.53), (12, 73000, 30, 5.4, 'yfdncd', None, 33.34), (12, 74000, 82, 10.2, 'jmvq9d', None, 63.46), (12, 75000, 94, 57.76, 'l1ei4c', None, 58.27)]
 * Instruction #5:
     - SQL:  commit;
     - TID: 0
     - Output: None

### Scenario 1
 * Instruction #0:
     - SQL:  SET LOCAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  START TRANSACTION;
     - TID: 0
     - Output: None
 * Instruction #2:
     - SQL:  select * from t_8fhx8c as ref_1 where ref_1.c_0byzvd not in ( select nullif(19,...
     - TID: 0
     - Output: []
 * Instruction #3:
     - SQL:  COMMIT;
     - TID: 0
     - Output: None
