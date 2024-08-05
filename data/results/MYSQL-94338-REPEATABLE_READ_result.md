# Bug ID MYSQL-94338-REPEATABLE_READ

## Description

Link:                     https://bugs.mysql.com/bug.php?id=94338
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              Dirty read-like behavior in transaction


## Details
 * Database: mysql-5.7.25
 * Number of scenarios: 1
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows: 0
 * Instruction #1:
     - Instruction:  SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_1
     - Output: None
     - Executed order: 1
     - Affected rows: 0
 * Instruction #2:
     - Instruction:  ANALYZE TABLE t1, t2;
     - Transaction: conn_0
     - Output: [('testdb.t1', 'analyze', 'status', 'OK'), ('testdb.t2', 'analyze', 'status', 'OK')]
     - Executed order: 2
     - Affected rows: 2
 * Instruction #3:
     - Instruction:  BEGIN;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows: 0
 * Instruction #4:
     - Instruction:  BEGIN;
     - Transaction: conn_1
     - Output: None
     - Executed order: 4
     - Affected rows: 0
 * Instruction #5:
     - Instruction:  SELECT t1.b_id FROM t1 WHERE ( t1.a_id = 1 AND IFNULL(1 = ( SELECT state FROM t...
     - Transaction: conn_0
     - Output: []
     - Executed order: 5
     - Affected rows: 0
 * Instruction #6:
     - Instruction:  INSERT INTO t2 (a_id, b_id, c_code, c_id, state) VALUES (1,22,'B',10,1), (1,23,...
     - Transaction: conn_1
     - Output: None
     - Executed order: 6
     - Affected rows: 91
 * Instruction #7:
     - Instruction:  SELECT t1.b_id FROM t1 WHERE ( t1.a_id = 1 AND IFNULL(1 = ( SELECT state FROM t...
     - Transaction: conn_0
     - Output: [(19,)]
     - Executed order: 7
     - Affected rows: 1
 * Instruction #8:
     - Instruction:  COMMIT;
     - Transaction: conn_1
     - Output: None
     - Executed order: 8
     - Affected rows: 0
 * Instruction #9:
     - Instruction:  SELECT t1.b_id FROM t1 WHERE ( t1.a_id = 1 AND IFNULL(1 = ( SELECT state FROM t...
     - Transaction: conn_0
     - Output: [(19,)]
     - Executed order: 9
     - Affected rows: 1

 * Container logs:
   No logs available.
