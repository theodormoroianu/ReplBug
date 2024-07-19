# Bug ID MDEV-19535-READ_UNCOMMITTED

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-19535
Original isolation level: REPEATABLE READ
Tested isolation level:   READ UNCOMMITTED
Description:              Setting sql_mode='ORACLE' makes MariaDB miss some required locks.


## Details
 * Database: mariadb-10.4.5
 * Number of scenarios: 2
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 0 / 0
 * Instruction #1:
     - Instruction:  SET sql_mode='';
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  CREATE TABLE t1 (a INT NOT NULL PRIMARY KEY) engine=innodb;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 0 / 0
 * Instruction #3:
     - Instruction:  INSERT INTO t1 VALUES (1);
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 1 / 0
 * Instruction #4:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows / Warnings: 0 / 0
 * Instruction #5:
     - Instruction:  SELECT a AS a_con1 FROM t1 INTO @a FOR UPDATE;
     - Transaction: conn_0
     - Output: None
     - Executed order: 5
     - Affected rows / Warnings: 1 / 1
 * Instruction #6:
     - Instruction:  SET sql_mode='';
     - Transaction: conn_1
     - Output: None
     - Executed order: 6
     - Affected rows / Warnings: 0 / 0
 * Instruction #7:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_1
     - Output: None
     - Executed order: 7
     - Affected rows / Warnings: 0 / 0
 * Instruction #8:
     - Instruction:  SELECT a AS a_con2 FROM t1 INTO @a FOR UPDATE;
     - Transaction: conn_1
     - Output: None
     - Executed order: 9
     - Affected rows / Warnings: 1 / 1
 * Instruction #9:
     - Instruction:  UPDATE t1 SET a=a+100;
     - Transaction: conn_0
     - Output: None
     - Executed order: 8
     - Affected rows / Warnings: 1 / 0
 * Instruction #10:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 10
     - Affected rows / Warnings: 0 / 0
 * Instruction #11:
     - Instruction:  SELECT a AS con2 FROM t1;
     - Transaction: conn_1
     - Output: [(101,)]
     - Executed order: 11
     - Affected rows / Warnings: 1 / 0
 * Instruction #12:
     - Instruction:  COMMIT;
     - Transaction: conn_1
     - Output: None
     - Executed order: 12
     - Affected rows / Warnings: 0 / 0

 * Container logs:
   No logs available.

### Scenario 1
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 0 / 0
 * Instruction #1:
     - Instruction:  SET sql_mode='ORACLE';
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  CREATE TABLE t1 (a INT NOT NULL PRIMARY KEY) engine=innodb;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 0 / 0
 * Instruction #3:
     - Instruction:  INSERT INTO t1 VALUES (1);
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 1 / 0
 * Instruction #4:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows / Warnings: 0 / 0
 * Instruction #5:
     - Instruction:  SELECT a AS a_con1 FROM t1 INTO @a FOR UPDATE;
     - Transaction: conn_0
     - Output: None
     - Executed order: 5
     - Affected rows / Warnings: 1 / 1
 * Instruction #6:
     - Instruction:  SET sql_mode='ORACLE';
     - Transaction: conn_1
     - Output: None
     - Executed order: 6
     - Affected rows / Warnings: 0 / 0
 * Instruction #7:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_1
     - Output: None
     - Executed order: 7
     - Affected rows / Warnings: 0 / 0
 * Instruction #8:
     - Instruction:  SELECT a AS a_con2 FROM t1 INTO @a FOR UPDATE;
     - Transaction: conn_1
     - Output: None
     - Executed order: 8
     - Affected rows / Warnings: 1 / 1
 * Instruction #9:
     - Instruction:  UPDATE t1 SET a=a+100;
     - Transaction: conn_0
     - Output: None
     - Executed order: 9
     - Affected rows / Warnings: 1 / 0
 * Instruction #10:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 10
     - Affected rows / Warnings: 0 / 0
 * Instruction #11:
     - Instruction:  SELECT a AS con2 FROM t1;
     - Transaction: conn_1
     - Output: [(101,)]
     - Executed order: 11
     - Affected rows / Warnings: 1 / 0
 * Instruction #12:
     - Instruction:  COMMIT;
     - Transaction: conn_1
     - Output: None
     - Executed order: 12
     - Affected rows / Warnings: 0 / 0

 * Container logs:
   No logs available.
