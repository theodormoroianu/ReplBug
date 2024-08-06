# Bug ID MYSQL-100293-REPEATABLE_READ

## Description

Link:                     https://bugs.mysql.com/bug.php?id=100293
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              The SERIALIZABLE transactions are not blocked for query cache


## Details
 * Database: mysql-5.7.31
 * Number of scenarios: 1
 * Initial setup script: No

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  CREATE TABLE t(c1 INT);
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows: 0
 * Instruction #1:
     - Instruction:  INSERT INTO t VALUES(1),(2);
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows: 2
 * Instruction #2:
     - Instruction:  BEGIN;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows: 0
 * Instruction #3:
     - Instruction:  SELECT * FROM t;
     - Transaction: conn_0
     - Output: [(1,), (2,)]
     - Executed order: 3
     - Affected rows: 2
 * Instruction #4:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows: 0
 * Instruction #5:
     - Instruction:  flush status;
     - Transaction: conn_0
     - Output: None
     - Executed order: 5
     - Affected rows: 0
 * Instruction #6:
     - Instruction:  SHOW STATUS LIKE "Qcache_hits";
     - Transaction: conn_0
     - Output: [('Qcache_hits', '0')]
     - Executed order: 6
     - Affected rows: 1
 * Instruction #7:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 7
     - Affected rows: 0
 * Instruction #8:
     - Instruction:  SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 8
     - Affected rows: 0
 * Instruction #9:
     - Instruction:  BEGIN;
     - Transaction: conn_0
     - Output: None
     - Executed order: 9
     - Affected rows: 0
 * Instruction #10:
     - Instruction:  SELECT * FROM t;
     - Transaction: conn_0
     - Output: [(1,), (2,)]
     - Executed order: 10
     - Affected rows: 2
 * Instruction #11:
     - Instruction:  SHOW STATUS LIKE "Qcache_hits";
     - Transaction: conn_0
     - Output: [('Qcache_hits', '1')]
     - Executed order: 11
     - Affected rows: 1
 * Instruction #12:
     - Instruction:  INSERT INTO t VALUES(3);
     - Transaction: conn_1
     - Output: None
     - Executed order: 12
     - Affected rows: 1
 * Instruction #13:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 13
     - Affected rows: 0

 * Container logs:
   No logs available.
