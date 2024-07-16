# Bug ID MDEV-29243-REPEATABLE_READ

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-29243
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              The bug causes a crash of the MariaDB server


## Details
 * Database: mariadb-10.8.3
 * Number of scenarios: 1
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 0 / 0
 * Instruction #1:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_1
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_1
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 0 / 0
 * Instruction #3:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 0 / 0
 * Instruction #4:
     - Instruction:  delete from t_swbayb;
     - Transaction: conn_1
     - Output: None
     - Executed order: 4
     - Affected rows / Warnings: 28 / 0
 * Instruction #5:
     - Instruction:  insert into t_swbayb (wkey, pkey) values (88, 74000);
     - Transaction: conn_0
     - Output: None
     - Executed order: 6
     - Affected rows / Warnings: 1 / 0
 * Instruction #6:
     - Instruction:  insert into t_8fjoxb (wkey, pkey, c_yecif) values (110, 115000, case when exist...
     - Transaction: conn_1
     - Output: None
     - Executed order: 5
     - Affected rows / Warnings: 1 / 0
 * Instruction #7:
     - Instruction:  insert into t_swbayb (wkey, pkey, c_ywdp4d) values (90, 83000, 'vyenkd');
     - Transaction: conn_0
     - Output: None
     - Executed order: 7
     - Affected rows / Warnings: 1 / 0
 * Instruction #8:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 9
     - Affected rows / Warnings: 0 / 0
 * Instruction #9:
     - Instruction:  COMMIT;
     - Transaction: conn_1
     - Output: None
     - Executed order: 8
     - Affected rows / Warnings: 0 / 0

 * Container logs:
   No logs available.
