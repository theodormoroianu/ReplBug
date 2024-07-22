# Bug ID MDEV-29187-REPEATABLE_READ

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-29187
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              The TID of the transaction rolled back is off by one.


## Details
 * Database: mariadb-10.7.3
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
     - Instruction:  begin;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  update t1 set f1 = 3 where id = 1;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 1 / 0
 * Instruction #3:
     - Instruction:  begin;
     - Transaction: conn_1
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 0 / 0
 * Instruction #4:
     - Instruction:  update t1 set f1 = 4 where id = 2;
     - Transaction: conn_1
     - Output: None
     - Executed order: 4
     - Affected rows / Warnings: 1 / 0
 * Instruction #5:
     - Instruction:  update t1 set f1 = 3 where id = 2;
     - Transaction: conn_0
     - Output: None
     - Executed order: 5
     - Affected rows / Warnings: 1 / 0
 * Instruction #6:
     - Instruction:  update t1 set f1 = 5 where id = 1;
     - Transaction: conn_1
     - Output: ERROR: 1213 (40001): Deadlock found when trying to get lock; try restarting transaction
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #7:
     - Instruction:  show engine innodb status;
     - Transaction: conn_2
     - Output: [('InnoDB', '', "\n=====================================\n2024-07-22 15:13:29 0x7f53dc0b2700 INNODB MONITOR OUTPUT\n=====================================\nPer second averages calculated from the last 3 seconds\n-----------------\nBACKGROUND THREAD\n-----------------\nsrv_master_thread loops: 0 srv_active, 0 srv_shutdown, 4 srv_idle\nsrv_master_thread log flush and writes: 4\n----------\nSEMAPHORES\n----------\n------------------------\nLATEST DETECTED DEADLOCK\n------------------------\n2024-07-22 15:13:29 0x7f53dc0fd700\n*** (1) TRANSACTION:\nTRANSACTION 25, ACTIVE 1 sec starting index read\nmysql tables in use 1, locked 1\nLOCK WAIT 3 lock struct(s), heap size 1128, 2 row lock(s), undo log entries 1\nMariaDB thread id 6, OS thread handle 139998151038720, query id 30 10.88.0.172 root Updating\nupdate t1 set f1 = 5 where id = 1\n*** WAITING FOR THIS LOCK TO BE GRANTED:\nRECORD LOCKS space id 5 page no 3 n bits 8 index PRIMARY of table `testdb`.`t1` trx id 25 lock_mode X locks rec but not gap waiting\nRecord lock, heap no 2 PHYSICAL RECORD: n_fields 4; compact format; info bits 0\n 0: len 4; hex 80000001; asc     ;;\n 1: len 6; hex 000000000018; asc       ;;\n 2: len 7; hex 07000001390110; asc     9  ;;\n 3: len 4; hex 80000003; asc     ;;\n\n*** CONFLICTING WITH:\nRECORD LOCKS space id 5 page no 3 n bits 8 index PRIMARY of table `testdb`.`t1` trx id 24 lock_mode X locks rec but not gap\nRecord lock, heap no 2 PHYSICAL RECORD: n_fields 4; compact format; info bits 0\n 0: len 4; hex 80000001; asc     ;;\n 1: len 6; hex 000000000018; asc       ;;\n 2: len 7; hex 07000001390110; asc     9  ;;\n 3: len 4; hex 80000003; asc     ;;\n\n\n*** (2) TRANSACTION:\nTRANSACTION 24, ACTIVE 1 sec starting index read\nmysql tables in use 1, locked 1\nLOCK WAIT 3 lock struct(s), heap size 1128, 2 row lock(s), undo log entries 1\nMariaDB thread id 5, OS thread handle 139998151345920, query id 29 10.88.0.172 root Updating\nupdate t1 set f1 = 3 where id = 2\n*** WAITING FOR THIS LOCK TO BE GRANTED:\nRECORD LOCKS space id 5 page no 3 n bits 8 index PRIMARY of table `testdb`.`t1` trx id 24 lock_mode X locks rec but not gap waiting\nRecord lock, heap no 3 PHYSICAL RECORD: n_fields 4; compact format; info bits 0\n 0: len 4; hex 80000002; asc     ;;\n 1: len 6; hex 000000000019; asc       ;;\n 2: len 7; hex 080000013a0110; asc     :  ;;\n 3: len 4; hex 80000004; asc     ;;\n\n*** CONFLICTING WITH:\nRECORD LOCKS space id 5 page no 3 n bits 8 index PRIMARY of table `testdb`.`t1` trx id 25 lock_mode X locks rec but not gap\nRecord lock, heap no 3 PHYSICAL RECORD: n_fields 4; compact format; info bits 0\n 0: len 4; hex 80000002; asc     ;;\n 1: len 6; hex 000000000019; asc       ;;\n 2: len 7; hex 080000013a0110; asc     :  ;;\n 3: len 4; hex 80000004; asc     ;;\n\n*** WE ROLL BACK TRANSACTION (0)\n------------\nTRANSACTIONS\n------------\nTrx id counter 27\nPurge done for trx's n:o < 27 undo n:o < 0 state: running\nHistory list length 11\nLIST OF TRANSACTIONS FOR EACH SESSION:\n---TRANSACTION (0x7f53c3a02230), not started\n0 lock struct(s), heap size 1128, 0 row lock(s)\n---TRANSACTION 24, ACTIVE 1 sec\n3 lock struct(s), heap size 1128, 2 row lock(s), undo log entries 2\nMariaDB thread id 5, OS thread handle 139998151345920, query id 29 10.88.0.172 root \n--------\nFILE I/O\n--------\nPending flushes (fsync) log: 0; buffer pool: 0\n169 OS file reads, 9 OS file writes, 11 OS fsyncs\n0.00 reads/s, 28323 avg bytes/read, 0.00 writes/s, 0.00 fsyncs/s\n-------------------------------------\nINSERT BUFFER AND ADAPTIVE HASH INDEX\n-------------------------------------\nIbuf: size 1, free list len 0, seg size 2, 0 merges\nmerged operations:\n insert 0, delete mark 0, delete 0\ndiscarded operations:\n insert 0, delete mark 0, delete 0\n0.00 hash searches/s, 0.00 non-hash searches/s\n---\nLOG\n---\nLog sequence number 45630\nLog flushed up to   45494\nPages flushed up to 42197\nLast checkpoint at  42185\n0 pending log flushes, 0 pending chkp writes\n11 log i/o's done, 3.67 log i/o's/second\n----------------------\nBUFFER POOL AND MEMORY\n----------------------\nTotal large memory allocated 167772160\nDictionary memory allocated 857464\nBuffer pool size   8112\nFree buffers       7819\nDatabase pages     293\nOld database pages 0\nModified db pages  26\nPercent of dirty pages(LRU & free pages): 0.320\nMax dirty pages percent: 90.000\nPending reads 0\nPending writes: LRU 0, flush list 0\nPages made young 0, not young 0\n0.00 youngs/s, 0.00 non-youngs/s\nPages read 155, created 138, written 0\n51.65 reads/s, 45.98 creates/s, 0.00 writes/s\nBuffer pool hit rate 907 / 1000, young-making rate 0 / 1000 not 0 / 1000\nPages read ahead 0.00/s, evicted without access 0.00/s, Random read ahead 0.00/s\nLRU len: 293, unzip_LRU len: 0\nI/O sum[0]:cur[3], unzip sum[0]:cur[0]\n--------------\nROW OPERATIONS\n--------------\n0 read views open inside InnoDB\nProcess ID=0, Main thread ID=0, state: sleeping\nNumber of rows inserted 2, updated 3, deleted 0, read 3\n0.67 inserts/s, 1.00 updates/s, 0.00 deletes/s, 1.00 reads/s\nNumber of system rows inserted 0, updated 0, deleted 0, read 0\n0.00 inserts/s, 0.00 updates/s, 0.00 deletes/s, 0.00 reads/s\n----------------------------\nEND OF INNODB MONITOR OUTPUT\n============================\n")]
     - Executed order: 6
     - Affected rows / Warnings: 1 / 0

 * Container logs:
   No logs available.
