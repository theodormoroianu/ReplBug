# Bug ID MDEV-18044-REPEATABLE_READ

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-16675
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              Adding an IF statement unecessarily adds a row lock.


## Details
 * Database: mariadb-10.3.8-debug
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
     - Instruction:  BEGIN;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  CALL pr2();
     - Transaction: conn_0
     - Output: [(2,)]
     - Executed order: 2
     - Affected rows / Warnings: 1 / 0
 * Instruction #3:
     - Instruction:  show engine innodb status;
     - Transaction: conn_1
     - Output: [('InnoDB', '', "\n=====================================\n2024-07-19 11:39:13 0x7f7b4574f700 INNODB MONITOR OUTPUT\n=====================================\nPer second averages calculated from the last 3 seconds\n-----------------\nBACKGROUND THREAD\n-----------------\nsrv_master_thread loops: 1 srv_active, 0 srv_shutdown, 1 srv_idle\nsrv_master_thread log flush and writes: 2\n----------\nSEMAPHORES\n----------\n-------------\nRW-LATCH INFO\n-------------\nTotal number of rw-locks 16441\nOS WAIT ARRAY INFO: reservation count 51\nOS WAIT ARRAY INFO: signal count 48\nRW-shared spins 0, rounds 63, OS waits 16\nRW-excl spins 0, rounds 371, OS waits 4\nRW-sx spins 0, rounds 0, OS waits 0\nSpin rounds per wait: 63.00 RW-shared, 371.00 RW-excl, 0.00 RW-sx\n------------\nTRANSACTIONS\n------------\nTrx id counter 39\nPurge done for trx's n:o < 39 undo n:o < 0 state: running but idle\nHistory list length 17\nTotal number of lock structs in row lock hash table 1\nLIST OF TRANSACTIONS FOR EACH SESSION:\n---TRANSACTION 421642383663800, not started\n0 lock struct(s), heap size 1160, 0 row lock(s)\n---TRANSACTION 421642383661976, not started\n0 lock struct(s), heap size 1160, 0 row lock(s)\n--------\nFILE I/O\n--------\nI/O thread 0 state: waiting for completed aio requests (insert buffer thread)\nI/O thread 1 state: waiting for completed aio requests (log thread)\nI/O thread 2 state: waiting for completed aio requests (read thread)\nI/O thread 3 state: waiting for completed aio requests (read thread)\nI/O thread 4 state: waiting for completed aio requests (read thread)\nI/O thread 5 state: waiting for completed aio requests (read thread)\nI/O thread 6 state: waiting for completed aio requests (write thread)\nI/O thread 7 state: waiting for completed aio requests (write thread)\nI/O thread 8 state: waiting for completed aio requests (write thread)\nI/O thread 9 state: waiting for completed aio requests (write thread)\nPending normal aio reads: [0, 0, 0, 0] , aio writes: [0, 0, 0, 0] ,\n ibuf aio reads:, log i/o's:, sync i/o's:\nPending flushes (fsync) log: 0; buffer pool: 0\n192 OS file reads, 177 OS file writes, 18 OS fsyncs\n63.98 reads/s, 27234 avg bytes/read, 58.98 writes/s, 6.00 fsyncs/s\n-------------------------------------\nINSERT BUFFER AND ADAPTIVE HASH INDEX\n-------------------------------------\nIbuf: size 1, free list len 0, seg size 2, 0 merges\nmerged operations:\n insert 0, delete mark 0, delete 0\ndiscarded operations:\n insert 0, delete mark 0, delete 0\nHash table size 34679, node heap has 0 buffer(s)\nHash table size 34679, node heap has 0 buffer(s)\nHash table size 34679, node heap has 0 buffer(s)\nHash table size 34679, node heap has 0 buffer(s)\nHash table size 34679, node heap has 0 buffer(s)\nHash table size 34679, node heap has 0 buffer(s)\nHash table size 34679, node heap has 0 buffer(s)\nHash table size 34679, node heap has 0 buffer(s)\n0.00 hash searches/s, 72.64 non-hash searches/s\n---\nLOG\n---\nLog sequence number 1639743\nLog flushed up to   1639743\nPages flushed up to 1639743\nLast checkpoint at  1639640\n0 pending log flushes, 0 pending chkp writes\n18 log i/o's done, 6.00 log i/o's/second\n----------------------\nBUFFER POOL AND MEMORY\n----------------------\nTotal large memory allocated 174063616\nDictionary memory allocated 77534\nBuffer pool size   8192\nFree buffers       7878\nDatabase pages     314\nOld database pages 0\nModified db pages  0\nPercent of dirty pages(LRU & free pages): 0.000\nMax dirty pages percent: 75.000\nPending reads 0\nPending writes: LRU 0, flush list 0, single page 0\nPages made young 0, not young 0\n0.00 youngs/s, 0.00 non-youngs/s\nPages read 176, created 138, written 163\n58.65 reads/s, 45.98 creates/s, 54.32 writes/s\nBuffer pool hit rate 902 / 1000, young-making rate 0 / 1000 not 0 / 1000\nPages read ahead 0.00/s, evicted without access 0.00/s, Random read ahead 0.00/s\nLRU len: 314, unzip_LRU len: 0\nI/O sum[0]:cur[0], unzip sum[0]:cur[0]\n--------------\nROW OPERATIONS\n--------------\n0 queries inside InnoDB, 0 queries in queue\n0 read views open inside InnoDB\nProcess ID=1, Main thread ID=140167044138752, state: sleeping\nNumber of rows inserted 3, updated 0, deleted 0, read 1\n1.00 inserts/s, 0.00 updates/s, 0.00 deletes/s, 0.33 reads/s\nNumber of system rows inserted 0, updated 0, deleted 0, read 0\n0.00 inserts/s, 0.00 updates/s, 0.00 deletes/s, 0.00 reads/s\n----------------------------\nEND OF INNODB MONITOR OUTPUT\n============================\n")]
     - Executed order: 3
     - Affected rows / Warnings: 1 / 0
 * Instruction #4:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: ERROR: MySQL Connection not available.
     - Executed order: Not executed
     - Affected rows / Warnings: 1 / 0

 * Container logs:
   > 2024-07-19 11:39:11 0 [Warning] lock_rec_convert_impl_to_expl_for_trx was called for index 18, trx 33
   > 2024-07-19 11:39:11 0 [Warning] lock_rec_convert_impl_to_expl_for_trx was called for index 18, trx 33
   > 2024-07-19 11:39:11 0 [Warning] lock_rec_convert_impl_to_expl_for_trx was called for index 19, trx 37
   > 2024-07-19 11:39:11 0 [Warning] lock_rec_convert_impl_to_expl_for_trx was called for index 19, trx 37
   > 2024-07-19 11:39:11 0 [Warning] lock_rec_convert_impl_to_expl_for_trx was called for index 19, trx 37
   > 2024-07-19 11:39:11 0 [Warning] lock_rec_convert_impl_to_expl_for_trx was called for index 19, trx 37
   > 2024-07-19 11:39:11 0 [Warning] lock_rec_convert_impl_to_expl_for_trx was called for index 19, trx 37
   > 2024-07-19 11:39:11 0 [Warning] lock_rec_convert_impl_to_expl_for_trx was called for index 19, trx 37
   > 2024-07-19 11:39:13 10 [Warning] Aborted connection 10 to db: 'testdb' user: 'root' host: '' (Got an error reading communication packets)

### Scenario 1
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 0 / 0
 * Instruction #1:
     - Instruction:  BEGIN;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  CALL pr1();
     - Transaction: conn_0
     - Output: [(1,)]
     - Executed order: 2
     - Affected rows / Warnings: 1 / 0
 * Instruction #3:
     - Instruction:  show engine innodb status;
     - Transaction: conn_1
     - Output: [('InnoDB', '', "\n=====================================\n2024-07-19 11:39:17 0x7fb157a7b700 INNODB MONITOR OUTPUT\n=====================================\nPer second averages calculated from the last 2 seconds\n-----------------\nBACKGROUND THREAD\n-----------------\nsrv_master_thread loops: 1 srv_active, 0 srv_shutdown, 1 srv_idle\nsrv_master_thread log flush and writes: 2\n----------\nSEMAPHORES\n----------\n-------------\nRW-LATCH INFO\n-------------\nTotal number of rw-locks 16441\nOS WAIT ARRAY INFO: reservation count 48\nOS WAIT ARRAY INFO: signal count 50\nRW-shared spins 0, rounds 65, OS waits 12\nRW-excl spins 0, rounds 457, OS waits 8\nRW-sx spins 0, rounds 0, OS waits 0\nSpin rounds per wait: 65.00 RW-shared, 457.00 RW-excl, 0.00 RW-sx\n------------\nTRANSACTIONS\n------------\nTrx id counter 39\nPurge done for trx's n:o < 39 undo n:o < 0 state: running but idle\nHistory list length 17\nTotal number of lock structs in row lock hash table 0\nLIST OF TRANSACTIONS FOR EACH SESSION:\n---TRANSACTION 421874618081976, not started\n0 lock struct(s), heap size 1160, 0 row lock(s)\n---TRANSACTION 421874618080152, not started\n0 lock struct(s), heap size 1160, 0 row lock(s)\n--------\nFILE I/O\n--------\nI/O thread 0 state: waiting for completed aio requests (insert buffer thread)\nI/O thread 1 state: waiting for completed aio requests (log thread)\nI/O thread 2 state: waiting for completed aio requests (read thread)\nI/O thread 3 state: waiting for completed aio requests (read thread)\nI/O thread 4 state: waiting for completed aio requests (read thread)\nI/O thread 5 state: waiting for completed aio requests (read thread)\nI/O thread 6 state: waiting for completed aio requests (write thread)\nI/O thread 7 state: waiting for completed aio requests (write thread)\nI/O thread 8 state: waiting for completed aio requests (write thread)\nI/O thread 9 state: waiting for completed aio requests (write thread)\nPending normal aio reads: [0, 0, 0, 0] , aio writes: [0, 0, 0, 0] ,\n ibuf aio reads:, log i/o's:, sync i/o's:\nPending flushes (fsync) log: 0; buffer pool: 0\n192 OS file reads, 177 OS file writes, 18 OS fsyncs\n63.98 reads/s, 27234 avg bytes/read, 58.98 writes/s, 6.00 fsyncs/s\n-------------------------------------\nINSERT BUFFER AND ADAPTIVE HASH INDEX\n-------------------------------------\nIbuf: size 1, free list len 0, seg size 2, 0 merges\nmerged operations:\n insert 0, delete mark 0, delete 0\ndiscarded operations:\n insert 0, delete mark 0, delete 0\nHash table size 34679, node heap has 0 buffer(s)\nHash table size 34679, node heap has 0 buffer(s)\nHash table size 34679, node heap has 0 buffer(s)\nHash table size 34679, node heap has 0 buffer(s)\nHash table size 34679, node heap has 0 buffer(s)\nHash table size 34679, node heap has 0 buffer(s)\nHash table size 34679, node heap has 0 buffer(s)\nHash table size 34679, node heap has 0 buffer(s)\n0.00 hash searches/s, 108.95 non-hash searches/s\n---\nLOG\n---\nLog sequence number 1639743\nLog flushed up to   1639743\nPages flushed up to 1639743\nLast checkpoint at  1639640\n0 pending log flushes, 0 pending chkp writes\n18 log i/o's done, 9.00 log i/o's/second\n----------------------\nBUFFER POOL AND MEMORY\n----------------------\nTotal large memory allocated 174063616\nDictionary memory allocated 77534\nBuffer pool size   8192\nFree buffers       7878\nDatabase pages     314\nOld database pages 0\nModified db pages  0\nPercent of dirty pages(LRU & free pages): 0.000\nMax dirty pages percent: 75.000\nPending reads 0\nPending writes: LRU 0, flush list 0, single page 0\nPages made young 0, not young 0\n0.00 youngs/s, 0.00 non-youngs/s\nPages read 176, created 138, written 163\n87.96 reads/s, 68.97 creates/s, 81.46 writes/s\nBuffer pool hit rate 902 / 1000, young-making rate 0 / 1000 not 0 / 1000\nPages read ahead 0.00/s, evicted without access 0.00/s, Random read ahead 0.00/s\nLRU len: 314, unzip_LRU len: 0\nI/O sum[0]:cur[0], unzip sum[0]:cur[0]\n--------------\nROW OPERATIONS\n--------------\n0 queries inside InnoDB, 0 queries in queue\n1 read views open inside InnoDB\nProcess ID=1, Main thread ID=140399278556928, state: sleeping\nNumber of rows inserted 3, updated 0, deleted 0, read 1\n1.50 inserts/s, 0.00 updates/s, 0.00 deletes/s, 0.50 reads/s\nNumber of system rows inserted 0, updated 0, deleted 0, read 0\n0.00 inserts/s, 0.00 updates/s, 0.00 deletes/s, 0.00 reads/s\n----------------------------\nEND OF INNODB MONITOR OUTPUT\n============================\n")]
     - Executed order: 3
     - Affected rows / Warnings: 1 / 0
 * Instruction #4:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: ERROR: MySQL Connection not available.
     - Executed order: Not executed
     - Affected rows / Warnings: 1 / 0

 * Container logs:
   > 2024-07-19 11:39:15 0 [Warning] lock_rec_convert_impl_to_expl_for_trx was called for index 18, trx 33
   > 2024-07-19 11:39:15 0 [Warning] lock_rec_convert_impl_to_expl_for_trx was called for index 18, trx 33
   > 2024-07-19 11:39:15 0 [Warning] lock_rec_convert_impl_to_expl_for_trx was called for index 19, trx 37
   > 2024-07-19 11:39:15 0 [Warning] lock_rec_convert_impl_to_expl_for_trx was called for index 19, trx 37
   > 2024-07-19 11:39:15 0 [Warning] lock_rec_convert_impl_to_expl_for_trx was called for index 19, trx 37
   > 2024-07-19 11:39:15 0 [Warning] lock_rec_convert_impl_to_expl_for_trx was called for index 19, trx 37
   > 2024-07-19 11:39:15 0 [Warning] lock_rec_convert_impl_to_expl_for_trx was called for index 19, trx 37
   > 2024-07-19 11:39:15 0 [Warning] lock_rec_convert_impl_to_expl_for_trx was called for index 19, trx 37
   > 2024-07-19 11:39:18 10 [Warning] Aborted connection 10 to db: 'testdb' user: 'root' host: '' (Got an error reading communication packets)
