# Bug ID MYSQL-91837-REPEATABLE_READ

## Description

Link:                     https://bugs.mysql.com/bug.php?id=91837
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              transaction start date is not expressed in session time zone


## Details
 * Database: mysql-5.7.22
 * Number of scenarios: 1
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows: 0
 * Instruction #1:
     - Instruction:  begin;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows: 0
 * Instruction #2:
     - Instruction:  select * from mysql.innodb_table_stats LIMIT 1;
     - Transaction: conn_0
     - Output: [('mysql', 'gtid_executed', datetime.datetime(2024, 7, 26, 11, 39, 26), 0, 1, 0)]
     - Executed order: 2
     - Affected rows: 1
 * Instruction #3:
     - Instruction:  SELECT SLEEP(2);
     - Transaction: conn_1
     - Output: [(0,)]
     - Executed order: 3
     - Affected rows: 1
 * Instruction #4:
     - Instruction:  select trx_started from information_schema.innodb_trx;
     - Transaction: conn_1
     - Output: [(datetime.datetime(2024, 7, 26, 11, 39, 38),)]
     - Executed order: 4
     - Affected rows: 1
 * Instruction #5:
     - Instruction:  select count(*) from information_schema.innodb_trx where trx_started < date_sub...
     - Transaction: conn_1
     - Output: [(1,)]
     - Executed order: 5
     - Affected rows: 1
 * Instruction #6:
     - Instruction:  set session time_zone = '-09:00';
     - Transaction: conn_1
     - Output: None
     - Executed order: 6
     - Affected rows: 0
 * Instruction #7:
     - Instruction:  select trx_started from information_schema.innodb_trx;
     - Transaction: conn_1
     - Output: [(datetime.datetime(2024, 7, 26, 11, 39, 38),)]
     - Executed order: 7
     - Affected rows: 1
 * Instruction #8:
     - Instruction:  select count(*) from information_schema.innodb_trx where trx_started < date_sub...
     - Transaction: conn_1
     - Output: [(0,)]
     - Executed order: 8
     - Affected rows: 1

 * Container logs:
   No logs available.
