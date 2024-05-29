# Bug ID 107898 - READ UNCOMMITTED

## Description

Link:                     https://bugs.mysql.com/bug.php?id=107898
Original isolation level: READ COMMITTED
Tested isolation level:   READ UNCOMMITTED


## Details
 * Database: mysql-8.0.23
 * Number of scenarios: 2
 * Initial setup script: /home/theodor/Projects/MasterThesis/data/sql/mysql_bk_2.sql

## Results
### Scenario 0
 * Instruction #0:
     - SQL:  SET LOCAL TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  SET LOCAL TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
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
     - Output: [(12, 70000, 18, 87.87, 'wkf9h', None, 76.7), (12, 71000, 37, 5.2, 'npgb8', None, 95.63), (12, 72000, 48, 83.8, 'xhx3rb', None, 51.53), (12, 73000, 30, 5.4, 'yfdncd', None, 33.34), (12, 74000, 82, 10.2, 'jmvq9d', None, 63.46), (12, 75000, 94, 57.76, 'l1ei4c', None, 58.27)]
 * Instruction #5:
     - SQL:  commit;
     - TID: 0
     - Output: None

### Scenario 1
 * Instruction #0:
     - SQL:  SET LOCAL TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
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
