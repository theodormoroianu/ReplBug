# Bug ID MDEV-16024-REPEATABLE_READ

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-16024
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              The begin_transaction actually marks the end of the transaction, not the begin.


## Details
 * Database: mariadb-10.3.6
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
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  set @ts = now(6);
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 0 / 0
 * Instruction #3:
     - Instruction:  insert into t1 values(1);
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 1 / 0
 * Instruction #4:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows / Warnings: 0 / 0
 * Instruction #5:
     - Instruction:  select @ts;
     - Transaction: conn_0
     - Output: [('2024-07-18 12:26:18.908192',)]
     - Executed order: 5
     - Affected rows / Warnings: 1 / 0
 * Instruction #6:
     - Instruction:  select * from mysql.transaction_registry;
     - Transaction: conn_0
     - Output: [(29, 30, datetime.datetime(2024, 7, 18, 12, 26, 19, 508960), datetime.datetime(2024, 7, 18, 12, 26, 19, 509399), 'REPEATABLE-READ')]
     - Executed order: 6
     - Affected rows / Warnings: 1 / 0
 * Instruction #7:
     - Instruction:  select (select begin_timestamp from mysql.transaction_registry) < @ts;
     - Transaction: conn_0
     - Output: [(0,)]
     - Executed order: 7
     - Affected rows / Warnings: 1 / 0

 * Container logs:
   No logs available.
