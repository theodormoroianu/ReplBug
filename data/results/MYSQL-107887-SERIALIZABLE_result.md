# Bug ID MYSQL-107887-SERIALIZABLE

## Description

Link:                     https://bugs.mysql.com/bug.php?id=107887
Original isolation level: READ COMMITTED
Tested isolation level:   SERIALIZABLE


## Details
 * Database: mysql-8.0.23
 * Number of scenarios: 2
 * Initial setup script: /home/theodor/Projects/MasterThesis/data/sql/MYSQL-107887_mysql_bk.sql

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
     - TID: 0
     - Output: None
 * Instruction #3:
     - SQL:  START TRANSACTION;
     - TID: 1
     - Output: None
 * Instruction #4:
     - SQL:  insert into t_cqieb values (141, 210000, 41.72, 56, 76, null, 32.6, null, 11, 1...
     - TID: 1
     - Output: None
 * Instruction #5:
     - SQL:  ROLLBACK;
     - TID: 1
     - Output: None
 * Instruction #6:
     - SQL:  update t_cqieb set wkey = 116 where t_cqieb.c_rejdnc not in ( select subq_0.c0 ...
     - TID: 0
     - Output: None
 * Instruction #7:
     - SQL:  select * from t_cqieb where wkey = 116;
     - TID: 0
     - Output: [(116, 15000, 42.63, 27, 85, 19, None, None, 54.97, 25, 49), (116, 16000, 31.55, 59, 90, 84, None, None, 50.66, 87, 93), (116, 17000, 23.2, 98, 21, 16, None, None, 59.85, 84, 66), (116, 18000, 11.81, 46, 7, 79, None, None, 68.98, 47, 47), (116, 19000, 95.31, 14, 71, 2, None, None, 33.39, 50, 7), (116, 20000, 63.37, 90, 50, 13, None, None, 15.92, 8, 91), (116, 21000, 7.5, 81, 34, 52, None, None, 46.26, 14, 17), (116, 22000, None, 82, 65, 52, None, None, 51.44, 23, 44), (116, 23000, None, 71, 7, 93, 9.45, 76.89, None, 99, 87), (116, 24000, 70.78, 97, 12, 92, 34.26, 63.38, 68.8, 30, 7), (116, 25000, 6.34, 69, 62, 19, 8.84, 41.67, 64.44, 54, 51), (116, 26000, 22.75, 23, 52, 84, 19.1, None, None, 35, 88), (116, 27000, 66.45, 53, 24, 73, 2.99, 88.18, 78.63, 7, 21), (116, 28000, 43.32, 6, 32, 16, 94.92, 5.36, 53.85, 61, 63), (116, 29000, 58.99, 11, 88, 36, None, 60.13, 71.18, 34, 99), (116, 34000, 38.56, 66, 46, 39, 32.13, 69.18, 98.71, 86, 41), (116, 35000, 88.28, 44, 28, 90, 39.77, 66.84, 12.67, 76, 100), (116, 36000, 58.65, 96, 9, 12, 62.27, 17.29, 2147483648.1, 70, 39), (116, 47000, 51.65, 49, 31, 88, 74.95, 40.75, None, 8, 79), (116, 48000, 76.6, 6, 4, 80, 16.88, 2147483648.1, None, 50, 43), (116, 49000, 18.35, 92, 4, 52, 7.59, 12.63, None, 94, 40), (116, 50000, 59.1, 27, 82, 38, 7.3, 90.74, None, 81, 75), (116, 51000, None, 88, 54, 49, 24.62, 75.2, None, 44, 44), (116, 52000, 50.85, 68, 54, 49, 58.59, 55.84, None, 5, 6), (116, 53000, 34.49, 55, 20, 10, 19.37, 35.59, None, 96, 66), (116, 54000, None, 4, 77, 8, None, None, None, 23, 50), (116, 55000, None, 48, 48, 44, None, None, 39.65, 91, 65), (116, 56000, None, 58, 23, 85, None, None, None, 63, 85), (116, 57000, None, 89, 65, 86, None, None, None, 7, 45), (116, 58000, None, 29, 43, 30, None, None, 47.66, 79, 62), (116, 59000, None, 93, 8, 86, None, None, 93.1, 44, 59), (116, 75000, 90.32, 95, 16, 96, 44.26, 68.44, 53.35, 74, 67), (116, 76000, 37.23, 85, 10, 100, 98.99, None, 25.8, 82, 8), (116, 77000, 75.92, 59, 83, 31, 55.31, 15.89, None, 40, 68), (116, 78000, 9.49, 39, 35, 11, None, 52.68, 60.82, 4, 68), (116, 79000, None, 87, 24, 1, 21.39, 38.37, 24.47, 22, 92), (116, 80000, 99.81, 49, 21, 57, 15.22, None, None, 70, 84), (116, 81000, 96.86, 68, 98, 86, 33.98, 24.4, 31.39, 5, 6), (116, 82000, 44.51, 20, 22, 59, 90.67, 63.3, 43.95, 100, 75)]
 * Instruction #8:
     - SQL:  COMMIT;
     - TID: 0
     - Output: None

 * Container logs:
   No logs available.

### Scenario 1
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  START TRANSACTION;
     - TID: 0
     - Output: None
 * Instruction #2:
     - SQL:  update t_cqieb set wkey = 116 where t_cqieb.c_rejdnc not in ( select subq_0.c0 ...
     - TID: 0
     - Output: None
 * Instruction #3:
     - SQL:  select * from t_cqieb where wkey = 116;
     - TID: 0
     - Output: []
 * Instruction #4:
     - SQL:  COMMIT;
     - TID: 0
     - Output: None

 * Container logs:
   No logs available.
