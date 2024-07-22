# Bug ID MDEV-21650-READ_UNCOMMITTED

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-21650
Original isolation level: REPEATABLE READ
Tested isolation level:   READ UNCOMMITTED
Description:              Setting sql_mode='ORACLE' makes MariaDB miss some required locks.


## Details
 * Database: mariadb-b615d275-debug
 * Number of scenarios: 1
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  CREATE TABLE t1 (s DATE, e DATE, PERIOD FOR app(s,e)) ENGINE=InnoDB;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 0 / 0
 * Instruction #1:
     - Instruction:  ALTER TABLE t1 ADD row_start BIGINT UNSIGNED AS ROW START, ADD row_end BIGINT U...
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 1
 * Instruction #2:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
     - Transaction: conn_0
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
     - Instruction:  INSERT INTO t1 (s,e) VALUES ('2021-07-04','2024-08-18');
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows / Warnings: 1 / 0
 * Instruction #5:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_1
     - Output: None
     - Executed order: 5
     - Affected rows / Warnings: 0 / 0
 * Instruction #6:
     - Instruction:  INSERT INTO t1 (s,e) VALUES ('2018-06-01','2021-09-15');
     - Transaction: conn_1
     - Output: None
     - Executed order: 6
     - Affected rows / Warnings: 1 / 0
 * Instruction #7:
     - Instruction:  SELECT * FROM t1 FOR SYSTEM_TIME AS OF NOW();
     - Transaction: conn_0
     - Output: ERROR: 4129 (HY000): TRX_ID 198 not found in `mysql.transaction_registry`
     - Executed order: 7
     - Affected rows / Warnings: 0 / 0
 * Instruction #8:
     - Instruction:  SET innodb_lock_wait_timeout= 1, lock_wait_timeout= 1;
     - Transaction: conn_1
     - Output: None
     - Executed order: 8
     - Affected rows / Warnings: 0 / 0
 * Instruction #9:
     - Instruction:  ALTER TABLE xx;
     - Transaction: conn_1
     - Output: ERROR: 1146 (42S02): Table 'testdb.xx' doesn't exist
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #10:
     - Instruction:  DROP TABLE t1;
     - Transaction: conn_0
     - Output: None
     - Executed order: 9
     - Affected rows / Warnings: 0 / 0

 * Container logs:
   No logs available.
