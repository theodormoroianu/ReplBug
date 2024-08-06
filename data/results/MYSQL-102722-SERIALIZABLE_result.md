# Bug ID MYSQL-102722-SERIALIZABLE

## Description

Link:                     https://bugs.mysql.com/bug.php?id=102722
Original isolation level: REPEATABLE READ
Tested isolation level:   SERIALIZABLE
Description:              Locks on secondary indexes are not released even though the secondary indexes are unmatched when index_condition_pushdown=off


## Details
 * Database: mysql-8.0.26
 * Number of scenarios: 1
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows: 0
 * Instruction #1:
     - Instruction:  SET SESSION TRANSACTION ISOLATION LEVEL SERIALIZABLE;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows: 0
 * Instruction #2:
     - Instruction:  show variables like '%isolation%';
     - Transaction: conn_0
     - Output: [('transaction_isolation', 'SERIALIZABLE')]
     - Executed order: 2
     - Affected rows: 1
 * Instruction #3:
     - Instruction:  SET @@optimizer_switch='index_condition_pushdown=off';
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows: 0
 * Instruction #4:
     - Instruction:  begin;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows: 0
 * Instruction #5:
     - Instruction:  select b,c,d from ts where b>=5 and b<8 and c=7 for update;
     - Transaction: conn_0
     - Output: [(7, 7, 7)]
     - Executed order: 5
     - Affected rows: 1
 * Instruction #6:
     - Instruction:  select INDEX_NAME,LOCK_TYPE,LOCK_MODE,LOCK_STATUS,LOCK_DATA from performance_sc...
     - Transaction: conn_0
     - Output: [(None, 'TABLE', 'IX', 'GRANTED', None), ('b', 'RECORD', 'X', 'GRANTED', '6, 6, 6'), ('b', 'RECORD', 'X', 'GRANTED', '7, 7, 7'), ('b', 'RECORD', 'X', 'GRANTED', '8, 8, 8'), ('PRIMARY', 'RECORD', 'X,REC_NOT_GAP', 'GRANTED', '6'), ('PRIMARY', 'RECORD', 'X,REC_NOT_GAP', 'GRANTED', '7'), ('PRIMARY', 'RECORD', 'X,REC_NOT_GAP', 'GRANTED', '8')]
     - Executed order: 6
     - Affected rows: 7
 * Instruction #7:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: None
     - Executed order: 7
     - Affected rows: 0
 * Instruction #8:
     - Instruction:  SET @@optimizer_switch='index_condition_pushdown=on';
     - Transaction: conn_0
     - Output: None
     - Executed order: 8
     - Affected rows: 0
 * Instruction #9:
     - Instruction:  begin;
     - Transaction: conn_0
     - Output: None
     - Executed order: 9
     - Affected rows: 0
 * Instruction #10:
     - Instruction:  select b,c,d from ts where b>=5 and b<8 and c=7 for update;
     - Transaction: conn_0
     - Output: [(7, 7, 7)]
     - Executed order: 10
     - Affected rows: 1
 * Instruction #11:
     - Instruction:  select INDEX_NAME,LOCK_TYPE,LOCK_MODE,LOCK_STATUS,LOCK_DATA from performance_sc...
     - Transaction: conn_0
     - Output: [(None, 'TABLE', 'IX', 'GRANTED', None), ('b', 'RECORD', 'X', 'GRANTED', '6, 6, 6'), ('b', 'RECORD', 'X', 'GRANTED', '7, 7, 7'), ('b', 'RECORD', 'X', 'GRANTED', '8, 8, 8'), ('PRIMARY', 'RECORD', 'X,REC_NOT_GAP', 'GRANTED', '7')]
     - Executed order: 11
     - Affected rows: 5
 * Instruction #12:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: None
     - Executed order: 12
     - Affected rows: 0

 * Container logs:
   No logs available.
