# Bug ID MYSQL-92558-READ_UNCOMMITTED

## Description

Link:                     https://bugs.mysql.com/bug.php?id=92558
Original isolation level: REPEATABLE READ
Tested isolation level:   READ UNCOMMITTED
Description:              The 'trx_is_read_only' flag is not set on implicit read-only transactions.


## Details
 * Database: mysql-8.0.12
 * Number of scenarios: 1
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows: 0
 * Instruction #1:
     - Instruction:  SET GLOBAL innodb_monitor_enable = 'trx_rw_commits';
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows: 0
 * Instruction #2:
     - Instruction:  SET GLOBAL innodb_monitor_enable = 'trx_ro_commits';
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows: 0
 * Instruction #3:
     - Instruction:  SET GLOBAL innodb_monitor_enable = 'trx_nl_ro_commits';
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows: 0
 * Instruction #4:
     - Instruction:  SET GLOBAL innodb_monitor_enable = 'trx_commits_insert_update';
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows: 0
 * Instruction #5:
     - Instruction:  SELECT name, comment, status, count FROM information_schema.innodb_metrics  WHE...
     - Transaction: conn_0
     - Output: [('trx_rw_commits', 'Number of read-write transactions  committed', 'enabled', 0), ('trx_ro_commits', 'Number of read-only transactions committed', 'enabled', 0), ('trx_nl_ro_commits', 'Number of non-locking auto-commit read-only transactions committed', 'enabled', 0), ('trx_commits_insert_update', 'Number of transactions committed with inserts and updates', 'enabled', 0)]
     - Executed order: 5
     - Affected rows: 4
 * Instruction #6:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 6
     - Affected rows: 0
 * Instruction #7:
     - Instruction:  select count(*) from t;
     - Transaction: conn_0
     - Output: [(1,)]
     - Executed order: 7
     - Affected rows: 1
 * Instruction #8:
     - Instruction:  select trx_is_read_only from information_schema.innodb_trx;
     - Transaction: conn_0
     - Output: [(0,)]
     - Executed order: 8
     - Affected rows: 1
 * Instruction #9:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 9
     - Affected rows: 0
 * Instruction #10:
     - Instruction:  SELECT name, comment, status, count FROM information_schema.innodb_metrics  WHE...
     - Transaction: conn_0
     - Output: [('trx_rw_commits', 'Number of read-write transactions  committed', 'enabled', 0), ('trx_ro_commits', 'Number of read-only transactions committed', 'enabled', 1), ('trx_nl_ro_commits', 'Number of non-locking auto-commit read-only transactions committed', 'enabled', 0), ('trx_commits_insert_update', 'Number of transactions committed with inserts and updates', 'enabled', 0)]
     - Executed order: 10
     - Affected rows: 4
 * Instruction #11:
     - Instruction:  START TRANSACTION READ ONLY;
     - Transaction: conn_0
     - Output: None
     - Executed order: 11
     - Affected rows: 0
 * Instruction #12:
     - Instruction:  select count(*) from t;
     - Transaction: conn_0
     - Output: [(1,)]
     - Executed order: 12
     - Affected rows: 1
 * Instruction #13:
     - Instruction:  select trx_is_read_only from information_schema.innodb_trx;
     - Transaction: conn_0
     - Output: [(1,)]
     - Executed order: 13
     - Affected rows: 1
 * Instruction #14:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 14
     - Affected rows: 0
 * Instruction #15:
     - Instruction:  SELECT name, comment, status, count FROM information_schema.innodb_metrics  WHE...
     - Transaction: conn_0
     - Output: [('trx_rw_commits', 'Number of read-write transactions  committed', 'enabled', 0), ('trx_ro_commits', 'Number of read-only transactions committed', 'enabled', 2), ('trx_nl_ro_commits', 'Number of non-locking auto-commit read-only transactions committed', 'enabled', 0), ('trx_commits_insert_update', 'Number of transactions committed with inserts and updates', 'enabled', 0)]
     - Executed order: 15
     - Affected rows: 4

 * Container logs:
   No logs available.
