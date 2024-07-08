# Bug ID MYSQL-104245-READ_COMMITTED

## Description

Link:                     https://bugs.mysql.com/bug.php?id=104245
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              There are 10 row locks despite only having 5 items in the table.


## Details
 * Database: mysql-5.7.34
 * Number of scenarios: 1
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
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
     - Instruction:  INSERT IGNORE INTO t1 (c2, c3, c4, c5) values (1,1,1,1),(1,1,1,1),(1,1,1,1),(1,...
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 0 / 5
 * Instruction #3:
     - Instruction:  SHOW ENGINE INNODB STATUS;
     - Transaction: conn_0
     - Output: [('InnoDB', '', "\n=====================================\n2024-07-08 14:35:27 0x7f900e3ad700 INNODB MONITOR OUTPUT\n=====================================\nPer second averages calculated from the last 4 seconds\n-----------------\nBACKGROUND THREAD\n-----------------\nsrv_master_thread loops: 5 srv_active, 0 srv_shutdown, 1 srv_idle\nsrv_master_thread log flush and writes: 6\n----------\nSEMAPHORES\n----------\nOS WAIT ARRAY INFO: reservation count 2\nOS WAIT ARRAY INFO: signal count 2\nRW-shared spins 0, rounds 7, OS waits 2\nRW-excl spins 0, rounds 0, OS waits 0\nRW-sx spins 0, rounds 0, OS waits 0\nSpin rounds per wait: 7.00 RW-shared, 0.00 RW-excl, 0.00 RW-sx\n------------\nTRANSACTIONS\n------------\nTrx id counter 1831\nPurge done for trx's n:o < 1828 undo n:o < 0 state: running but idle\nHistory list length 9\nLIST OF TRANSACTIONS FOR EACH SESSION:\n---TRANSACTION 1830, ACTIVE 0 sec\n5 lock struct(s), heap size 1136, 10 row lock(s)\nMySQL thread id 7, OS thread handle 140256690755328, query id 78 10.88.0.11 root starting\nSHOW ENGINE INNODB STATUS\n--------\nFILE I/O\n--------\nI/O thread 0 state: waiting for completed aio requests (insert buffer thread)\nI/O thread 1 state: waiting for completed aio requests (log thread)\nI/O thread 2 state: waiting for completed aio requests (read thread)\nI/O thread 3 state: waiting for completed aio requests (read thread)\nI/O thread 4 state: waiting for completed aio requests (read thread)\nI/O thread 5 state: waiting for completed aio requests (read thread)\nI/O thread 6 state: waiting for completed aio requests (write thread)\nI/O thread 7 state: waiting for completed aio requests (write thread)\nI/O thread 8 state: waiting for completed aio requests (write thread)\nI/O thread 9 state: waiting for completed aio requests (write thread)\nPending normal aio reads: [0, 0, 0, 0] , aio writes: [0, 0, 0, 0] ,\n ibuf aio reads:, log i/o's:, sync i/o's:\nPending flushes (fsync) log: 0; buffer pool: 0\n434 OS file reads, 108 OS file writes, 43 OS fsyncs\n0.25 reads/s, 16384 avg bytes/read, 21.49 writes/s, 8.00 fsyncs/s\n-------------------------------------\nINSERT BUFFER AND ADAPTIVE HASH INDEX\n-------------------------------------\nIbuf: size 1, free list len 0, seg size 2, 0 merges\nmerged operations:\n insert 0, delete mark 0, delete 0\ndiscarded operations:\n insert 0, delete mark 0, delete 0\nHash table size 34679, node heap has 0 buffer(s)\nHash table size 34679, node heap has 0 buffer(s)\nHash table size 34679, node heap has 0 buffer(s)\nHash table size 34679, node heap has 0 buffer(s)\nHash table size 34679, node heap has 0 buffer(s)\nHash table size 34679, node heap has 0 buffer(s)\nHash table size 34679, node heap has 0 buffer(s)\nHash table size 34679, node heap has 0 buffer(s)\n0.00 hash searches/s, 41.24 non-hash searches/s\n---\nLOG\n---\nLog sequence number 12696515\nLog flushed up to   12696515\nPages flushed up to 12672873\nLast checkpoint at  12672770\n0 pending log flushes, 0 pending chkp writes\n32 log i/o's done, 5.00 log i/o's/second\n----------------------\nBUFFER POOL AND MEMORY\n----------------------\nTotal large memory allocated 137428992\nDictionary memory allocated 110064\nBuffer pool size   8192\nFree buffers       7725\nDatabase pages     467\nOld database pages 0\nModified db pages  44\nPending reads      0\nPending writes: LRU 0, flush list 0, single page 0\nPages made young 0, not young 0\n0.00 youngs/s, 0.00 non-youngs/s\nPages read 409, created 58, written 58\n0.00 reads/s, 0.00 creates/s, 0.00 writes/s\nBuffer pool hit rate 999 / 1000, young-making rate 0 / 1000 not 0 / 1000\nPages read ahead 0.00/s, evicted without access 0.00/s, Random read ahead 0.00/s\nLRU len: 467, unzip_LRU len: 0\nI/O sum[0]:cur[0], unzip sum[0]:cur[0]\n--------------\nROW OPERATIONS\n--------------\n0 queries inside InnoDB, 0 queries in queue\n0 read views open inside InnoDB\nProcess ID=1, Main thread ID=140256160515840, state: sleeping\nNumber of rows inserted 3, updated 0, deleted 0, read 9\n0.50 inserts/s, 0.00 updates/s, 0.00 deletes/s, 0.25 reads/s\n----------------------------\nEND OF INNODB MONITOR OUTPUT\n============================\n")]
     - Executed order: 3
     - Affected rows / Warnings: 1 / 0
 * Instruction #4:
     - Instruction:  SELECT * FROM t1;
     - Transaction: conn_0
     - Output: [(1, 1, 1, 1, 1)]
     - Executed order: 4
     - Affected rows / Warnings: 1 / 0
 * Instruction #5:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 5
     - Affected rows / Warnings: 0 / 0

 * Container logs:
   No logs available.
