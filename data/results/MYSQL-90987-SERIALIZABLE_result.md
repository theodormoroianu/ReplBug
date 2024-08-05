# Bug ID MYSQL-90987-SERIALIZABLE

## Description

Link:                     https://bugs.mysql.com/bug.php?id=90987
Original isolation level: REPEATABLE READ
Tested isolation level:   SERIALIZABLE
Description:              Using a parition index causes deadlocks


## Details
 * Database: mysql-5.7.17
 * Number of scenarios: 2
 * Initial setup script: No

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows: 0
 * Instruction #1:
     - Instruction:  create table t4 (a int unsigned auto_increment , b int, c int, key(b), primary ...
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows: 0
 * Instruction #2:
     - Instruction:  insert into t4(b,c) values(1,11),(2,22),(3,33),(4,44),(5,55),(6,66),(7,77),(8,8...
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows: 9
 * Instruction #3:
     - Instruction:  begin;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows: 0
 * Instruction #4:
     - Instruction:  update t4 set c=c+1 where b=3;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows: 1
 * Instruction #5:
     - Instruction:  begin;
     - Transaction: conn_1
     - Output: None
     - Executed order: 5
     - Affected rows: 0
 * Instruction #6:
     - Instruction:  update t4 set c=c+1 where b=2;
     - Transaction: conn_1
     - Output: ERROR: 1205 (HY000): Lock wait timeout exceeded; try restarting transaction
     - Executed order: Not executed
     - Affected rows: -1

 * Container logs:
   No logs available.

### Scenario 1
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows: 0
 * Instruction #1:
     - Instruction:  create table t4 (a int unsigned auto_increment , b int, c int, key(b), primary ...
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows: 0
 * Instruction #2:
     - Instruction:  insert into t4(b,c) values(1,11),(2,22),(3,33),(4,44),(5,55),(6,66),(7,77),(8,8...
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows: 9
 * Instruction #3:
     - Instruction:  begin;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows: 0
 * Instruction #4:
     - Instruction:  update t4 set c=c+1 where b=3;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows: 1
 * Instruction #5:
     - Instruction:  begin;
     - Transaction: conn_1
     - Output: None
     - Executed order: 5
     - Affected rows: 0
 * Instruction #6:
     - Instruction:  update t4 set c=c+1 where b=2;
     - Transaction: conn_1
     - Output: None
     - Executed order: 6
     - Affected rows: 1

 * Container logs:
   No logs available.
