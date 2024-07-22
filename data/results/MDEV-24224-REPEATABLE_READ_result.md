# Bug ID MDEV-24224-REPEATABLE_READ

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-24224
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              Delete statement creates unnecessary gap lock ('gap before rec' present in innodb status).


## Details
 * Database: mariadb-10.5.8
 * Number of scenarios: 2
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
     - Instruction:  SET GLOBAL INNODB_STATUS_OUTPUT_LOCKS = 'ON';
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  BEGIN;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 0 / 0
 * Instruction #3:
     - Instruction:  DELETE FROM test WHERE TEST1 = 'A.123a' and TEST2 = 'C' and TEST3 = 3;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 0 / 0
 * Instruction #4:
     - Instruction:  SHOW ENGINE INNODB STATUS;
     - Transaction: conn_0
     - Output: [('InnoDB', '', "\n=====================================\n2024-07-22 07:45:14 0x7f72a3f69700 INNODB MONITOR OUTPUT\n=====================================\nPer second averages calculated from the last 2 seconds\n-----------------\nBACKGROUND THREAD\n-----------------\nsrv_master_thread loops: 1 srv_active, 0 srv_shutdown, 2 srv_idle\nsrv_master_thread log flush and writes: 3\n----------\nSEMAPHORES\n----------\nOS WAIT ARRAY INFO: reservation count 5\nOS WAIT ARRAY INFO: signal count 2\nRW-shared spins 0, rounds 0, OS waits 0\nRW-excl spins 0, rounds 0, OS waits 0\nRW-sx spins 0, rounds 0, OS waits 0\nSpin rounds per wait: 0.00 RW-shared, 0.00 RW-excl, 0.00 RW-sx\n------------\nTRANSACTIONS\n------------\nTrx id counter 37\nPurge done for trx's n:o < 36 undo n:o < 0 state: running\nHistory list length 16\nLIST OF TRANSACTIONS FOR EACH SESSION:\n---TRANSACTION 36, ACTIVE 0 sec\n2 lock struct(s), heap size 1128, 1 row lock(s)\nMySQL thread id 5, OS thread handle 140130353846016, query id 24 10.88.0.100 root starting\nSHOW ENGINE INNODB STATUS\nTABLE LOCK table `testdb`.`test` trx id 36 lock mode IX\nRECORD LOCKS space id 5 page no 4 n bits 72 index IDX_TEST of table `testdb`.`test` trx id 36 lock_mode X locks gap before rec\nRecord lock, heap no 3 PHYSICAL RECORD: n_fields 4; compact format; info bits 0\n 0: len 5; hex 422e343536; asc B.456;;\n 1: len 1; hex 43; asc C;;\n 2: len 8; hex 8000000000000003; asc         ;;\n 3: len 6; hex 000000000201; asc       ;;\n\n---TRANSACTION 421605073228024, not started\n0 lock struct(s), heap size 1128, 0 row lock(s)\n--------\nFILE I/O\n--------\nI/O thread 0 state: (null) ((null))\nI/O thread 1 state: (null) ((null))\nI/O thread 2 state: (null) ((null))\nI/O thread 3 state: (null) ((null))\nI/O thread 4 state: (null) ((null))\nI/O thread 5 state: (null) ((null))\nI/O thread 6 state: (null) ((null))\nI/O thread 7 state: (null) ((null))\nI/O thread 8 state: (null) ((null))\nI/O thread 9 state: (null) ((null))\nPending normal aio reads:\nPending flushes (fsync) log: 0; buffer pool: 0\n191 OS file reads, 11 OS file writes, 15 OS fsyncs\n0.00 reads/s, 27291 avg bytes/read, 0.00 writes/s, 0.00 fsyncs/s\n-------------------------------------\nINSERT BUFFER AND ADAPTIVE HASH INDEX\n-------------------------------------\nIbuf: size 1, free list len 0, seg size 2, 0 merges\nmerged operations:\n insert 0, delete mark 0, delete 0\ndiscarded operations:\n insert 0, delete mark 0, delete 0\n0.00 hash searches/s, 136.93 non-hash searches/s\n---\nLOG\n---\nLog sequence number 51756\nLog flushed up to   51756\nPages flushed up to 45142\nLast checkpoint at  45130\n0 pending log flushes, 0 pending chkp writes\n12 log i/o's done, 6.00 log i/o's/second\n----------------------\nBUFFER POOL AND MEMORY\n----------------------\nTotal large memory allocated 167772160\nDictionary memory allocated 863808\nBuffer pool size   8065\nFree buffers       7752\nDatabase pages     313\nOld database pages 0\nModified db pages  162\nPercent of dirty pages(LRU & free pages): 2.008\nMax dirty pages percent: 90.000\nPending reads 0\nPending writes: LRU 0, flush list 0\nPages made young 0, not young 0\n0.00 youngs/s, 0.00 non-youngs/s\nPages read 176, created 137, written 0\n87.96 reads/s, 68.47 creates/s, 0.00 writes/s\nBuffer pool hit rate 902 / 1000, young-making rate 0 / 1000 not 0 / 1000\nPages read ahead 0.00/s, evicted without access 0.00/s, Random read ahead 0.00/s\nLRU len: 313, unzip_LRU len: 0\nI/O sum[0]:cur[0], unzip sum[0]:cur[0]\n--------------\nROW OPERATIONS\n--------------\n0 read views open inside InnoDB\nProcess ID=0, Main thread ID=0, state: sleeping\nNumber of rows inserted 2, updated 0, deleted 0, read 0\n1.00 inserts/s, 0.00 updates/s, 0.00 deletes/s, 0.00 reads/s\nNumber of system rows inserted 0, updated 0, deleted 0, read 0\n0.00 inserts/s, 0.00 updates/s, 0.00 deletes/s, 0.00 reads/s\n----------------------------\nEND OF INNODB MONITOR OUTPUT\n============================\n")]
     - Executed order: 4
     - Affected rows / Warnings: 1 / 0
 * Instruction #5:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 5
     - Affected rows / Warnings: 0 / 0
 * Instruction #6:
     - Instruction:  SELECT * FROM test;
     - Transaction: conn_0
     - Output: [('row_a', 'A.123', 'C', 3), ('row_a', 'B.456', 'C', 3)]
     - Executed order: 6
     - Affected rows / Warnings: 2 / 0

 * Container logs:
   No logs available.

### Scenario 1
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 0 / 0
 * Instruction #1:
     - Instruction:  SET GLOBAL INNODB_STATUS_OUTPUT_LOCKS = 'ON';
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  BEGIN;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 0 / 0
 * Instruction #3:
     - Instruction:  DELETE FROM test WHERE TEST1 = 'G.123a' and TEST2 = 'X' and TEST3 = 31;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 0 / 0
 * Instruction #4:
     - Instruction:  SHOW ENGINE INNODB STATUS;
     - Transaction: conn_0
     - Output: [('InnoDB', '', "\n=====================================\n2024-07-22 07:45:23 0x7f6e9ffff700 INNODB MONITOR OUTPUT\n=====================================\nPer second averages calculated from the last 2 seconds\n-----------------\nBACKGROUND THREAD\n-----------------\nsrv_master_thread loops: 1 srv_active, 0 srv_shutdown, 2 srv_idle\nsrv_master_thread log flush and writes: 3\n----------\nSEMAPHORES\n----------\nOS WAIT ARRAY INFO: reservation count 8\nOS WAIT ARRAY INFO: signal count 5\nRW-shared spins 1, rounds 4, OS waits 0\nRW-excl spins 0, rounds 0, OS waits 0\nRW-sx spins 0, rounds 0, OS waits 0\nSpin rounds per wait: 4.00 RW-shared, 0.00 RW-excl, 0.00 RW-sx\n------------\nTRANSACTIONS\n------------\nTrx id counter 37\nPurge done for trx's n:o < 36 undo n:o < 0 state: running\nHistory list length 16\nLIST OF TRANSACTIONS FOR EACH SESSION:\n---TRANSACTION 36, ACTIVE 0 sec\n2 lock struct(s), heap size 1128, 1 row lock(s)\nMySQL thread id 5, OS thread handle 140113107482368, query id 24 10.88.0.101 root starting\nSHOW ENGINE INNODB STATUS\nTABLE LOCK table `testdb`.`test` trx id 36 lock mode IX\nRECORD LOCKS space id 5 page no 4 n bits 72 index IDX_TEST of table `testdb`.`test` trx id 36 lock_mode X\nRecord lock, heap no 1 PHYSICAL RECORD: n_fields 1; compact format; info bits 0\n 0: len 8; hex 73757072656d756d; asc supremum;;\n\n---TRANSACTION 421587826249976, not started\n0 lock struct(s), heap size 1128, 0 row lock(s)\n--------\nFILE I/O\n--------\nI/O thread 0 state: (null) ((null))\nI/O thread 1 state: (null) ((null))\nI/O thread 2 state: (null) ((null))\nI/O thread 3 state: (null) ((null))\nI/O thread 4 state: (null) ((null))\nI/O thread 5 state: (null) ((null))\nI/O thread 6 state: (null) ((null))\nI/O thread 7 state: (null) ((null))\nI/O thread 8 state: (null) ((null))\nI/O thread 9 state: (null) ((null))\nPending normal aio reads:\nPending flushes (fsync) log: 0; buffer pool: 0\n191 OS file reads, 11 OS file writes, 15 OS fsyncs\n0.00 reads/s, 27291 avg bytes/read, 0.00 writes/s, 0.00 fsyncs/s\n-------------------------------------\nINSERT BUFFER AND ADAPTIVE HASH INDEX\n-------------------------------------\nIbuf: size 1, free list len 0, seg size 2, 0 merges\nmerged operations:\n insert 0, delete mark 0, delete 0\ndiscarded operations:\n insert 0, delete mark 0, delete 0\n0.00 hash searches/s, 136.93 non-hash searches/s\n---\nLOG\n---\nLog sequence number 51756\nLog flushed up to   51756\nPages flushed up to 45142\nLast checkpoint at  45130\n0 pending log flushes, 0 pending chkp writes\n12 log i/o's done, 6.00 log i/o's/second\n----------------------\nBUFFER POOL AND MEMORY\n----------------------\nTotal large memory allocated 167772160\nDictionary memory allocated 863808\nBuffer pool size   8065\nFree buffers       7752\nDatabase pages     313\nOld database pages 0\nModified db pages  162\nPercent of dirty pages(LRU & free pages): 2.008\nMax dirty pages percent: 90.000\nPending reads 0\nPending writes: LRU 0, flush list 0\nPages made young 0, not young 0\n0.00 youngs/s, 0.00 non-youngs/s\nPages read 176, created 137, written 0\n87.96 reads/s, 68.47 creates/s, 0.00 writes/s\nBuffer pool hit rate 902 / 1000, young-making rate 0 / 1000 not 0 / 1000\nPages read ahead 0.00/s, evicted without access 0.00/s, Random read ahead 0.00/s\nLRU len: 313, unzip_LRU len: 0\nI/O sum[0]:cur[0], unzip sum[0]:cur[0]\n--------------\nROW OPERATIONS\n--------------\n0 read views open inside InnoDB\nProcess ID=0, Main thread ID=0, state: sleeping\nNumber of rows inserted 2, updated 0, deleted 0, read 0\n1.00 inserts/s, 0.00 updates/s, 0.00 deletes/s, 0.00 reads/s\nNumber of system rows inserted 0, updated 0, deleted 0, read 0\n0.00 inserts/s, 0.00 updates/s, 0.00 deletes/s, 0.00 reads/s\n----------------------------\nEND OF INNODB MONITOR OUTPUT\n============================\n")]
     - Executed order: 4
     - Affected rows / Warnings: 1 / 0
 * Instruction #5:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 5
     - Affected rows / Warnings: 0 / 0
 * Instruction #6:
     - Instruction:  SELECT * FROM test;
     - Transaction: conn_0
     - Output: [('row_a', 'A.123', 'C', 3), ('row_a', 'B.456', 'C', 3)]
     - Executed order: 6
     - Affected rows / Warnings: 2 / 0

 * Container logs:
   No logs available.
