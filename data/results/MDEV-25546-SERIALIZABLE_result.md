# Bug ID MDEV-25546-SERIALIZABLE

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-25546
Original isolation level: REPEATABLE READ
Tested isolation level:   SERIALIZABLE
Description:              The first partition is empty, but data is placed in the second partition instead.


## Details
 * Database: mariadb-10.3.34
 * Number of scenarios: 1
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 0 / 0
 * Instruction #1:
     - Instruction:  start transaction;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  replace into t1 select seq from seq_1_to_80;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 160 / 0
 * Instruction #3:
     - Instruction:  replace into t1 select seq from seq_1_to_70;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 140 / 0
 * Instruction #4:
     - Instruction:  replace into t1 select seq from seq_1_to_60;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows / Warnings: 120 / 0
 * Instruction #5:
     - Instruction:  select partition_name, table_rows from information_schema.partitions where tabl...
     - Transaction: conn_0
     - Output: [('p0', 150), ('p1', 60), ('pn', 90)]
     - Executed order: 5
     - Affected rows / Warnings: 3 / 0
 * Instruction #6:
     - Instruction:  rollback;
     - Transaction: conn_0
     - Output: None
     - Executed order: 6
     - Affected rows / Warnings: 0 / 0
 * Instruction #7:
     - Instruction:  select partition_name, table_rows from information_schema.partitions where tabl...
     - Transaction: conn_0
     - Output: [('p0', 0), ('p1', 0), ('pn', 90)]
     - Executed order: 7
     - Affected rows / Warnings: 3 / 0
 * Instruction #8:
     - Instruction:  replace into t1 select seq from seq_1_to_10;
     - Transaction: conn_0
     - Output: None
     - Executed order: 8
     - Affected rows / Warnings: 20 / 0
 * Instruction #9:
     - Instruction:  select partition_name, table_rows from information_schema.partitions where tabl...
     - Transaction: conn_0
     - Output: [('p0', 0), ('p1', 10), ('pn', 90)]
     - Executed order: 9
     - Affected rows / Warnings: 3 / 0

 * Container logs:
   No logs available.
