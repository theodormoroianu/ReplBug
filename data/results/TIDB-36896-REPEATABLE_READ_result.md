# Bug ID TIDB-36896-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/36896
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              Causes a stack overflow and crashes the server.


## Details
 * Database: tidb-v6.1.0
 * Number of scenarios: 2
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  WITH cte_0 AS (select ref_0.wkey as c0, ref_0.pkey as c1, ref_0.c_rrbxh as c2, ...
     - Transaction: conn_0
     - Output: ERROR: 2013 (HY000): Lost connection to MySQL server during query
     - Executed order: Not executed

 * Container logs:
   > [2024/07/02 13:50:58.479 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/07/02 13:50:58.482 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=32] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/02 13:50:58.483 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=32] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/02 13:50:58.485 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:66, Type:create schema, State:none, SchemaState:queueing, SchemaID:65, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 13:50:58.484 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 13:50:58.485 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:66, Type:create schema, State:none, SchemaState:queueing, SchemaID:65, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 13:50:58.484 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/02 13:50:58.486 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:create schema, State:none, SchemaState:queueing, SchemaID:65, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:50:58.484 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:50:58.487 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=32] [neededSchemaVersion=33] ["start time"=154.141µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 13:50:58.489 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=33] ["take time"=2.216922ms] [job="ID:66, Type:create schema, State:done, SchemaState:public, SchemaID:65, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 13:50:58.484 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:50:58.489 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:create schema, State:synced, SchemaState:public, SchemaID:65, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:50:58.484 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:50:58.490 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=66]
   > [2024/07/02 13:50:58.490 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 13:50:58.495 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=33] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_2el7jd`\n--\n\nDROP TABLE IF EXISTS `t_2el7jd`;"] [user=root@%]
   > [2024/07/02 13:50:58.495 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=33] [cur_db=testdb] [sql="CREATE TABLE `t_2el7jd` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_hzkgf` text DEFAULT NULL,\n  `c_si87c` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_alxrj` (`wkey`,`pkey`,`c_si87c`),\n  KEY `t_za4dpb` (`pkey`,`c_si87c`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/07/02 13:50:58.497 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:68, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:67, RowCount:0, ArgLen:1, start time: 2024-07-02 13:50:58.496 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 13:50:58.497 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:68, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:67, RowCount:0, ArgLen:1, start time: 2024-07-02 13:50:58.496 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_2el7jd` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_hzkgf` text DEFAULT NULL,\n  `c_si87c` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_alxrj` (`wkey`,`pkey`,`c_si87c`),\n  KEY `t_za4dpb` (`pkey`,`c_si87c`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/02 13:50:58.497 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:68, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:67, RowCount:0, ArgLen:0, start time: 2024-07-02 13:50:58.496 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:50:58.499 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=33] [neededSchemaVersion=34] ["start time"=398.518µs] [phyTblIDs="[67]"] [actionTypes="[8]"]
   > [2024/07/02 13:50:58.501 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=34] ["take time"=2.263088ms] [job="ID:68, Type:create table, State:done, SchemaState:public, SchemaID:65, TableID:67, RowCount:0, ArgLen:1, start time: 2024-07-02 13:50:58.496 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:50:58.501 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:68, Type:create table, State:synced, SchemaState:public, SchemaID:65, TableID:67, RowCount:0, ArgLen:0, start time: 2024-07-02 13:50:58.496 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:50:58.502 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=68]
   > [2024/07/02 13:50:58.502 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 13:50:58.502 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=60] ["first split key"=748000000000000043]
   > [2024/07/02 13:50:58.502 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=34] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_2el7jd` DISABLE KEYS */;"] [user=root@%]
   > [2024/07/02 13:50:58.504 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=34] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_2el7jd` ENABLE KEYS */;"] [user=root@%]
   > [2024/07/02 13:50:58.504 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=34] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_p7c1bd`\n--\n\nDROP TABLE IF EXISTS `t_p7c1bd`;"] [user=root@%]
   > [2024/07/02 13:50:58.504 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=34] [cur_db=testdb] [sql="CREATE TABLE `t_p7c1bd` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_rrbxh` text DEFAULT NULL,\n  `c_c5cvkb` int(11) DEFAULT NULL,\n  `c_ag5ccc` int(11) DEFAULT NULL,\n  `c_qo4qvc` text DEFAULT NULL,\n  `c_lhs3h` int(11) DEFAULT NULL,\n  `c_8dah2b` int(11) DEFAULT NULL,\n  `c_eg6xsc` int(11) DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_s0z7f` (`c_ag5ccc`,`c_8dah2b`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/07/02 13:50:58.505 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=62] ["first at"=748000000000000043] ["first new region left"="{Id:62 StartKey:7480000000000000ff3f00000000000000f8 EndKey:7480000000000000ff4300000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:63 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/02 13:50:58.505 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[62]"]
   > [2024/07/02 13:50:58.505 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:70, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:69, RowCount:0, ArgLen:1, start time: 2024-07-02 13:50:58.505 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 13:50:58.505 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:70, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:69, RowCount:0, ArgLen:1, start time: 2024-07-02 13:50:58.505 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_p7c1bd` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_rrbxh` text DEFAULT NULL,\n  `c_c5cvkb` int(11) DEFAULT NULL,\n  `c_ag5ccc` int(11) DEFAULT NULL,\n  `c_qo4qvc` text DEFAULT NULL,\n  `c_lhs3h` int(11) DEFAULT NULL,\n  `c_8dah2b` int(11) DEFAULT NULL,\n  `c_eg6xsc` int(11) DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_s0z7f` (`c_ag5ccc`,`c_8dah2b`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/02 13:50:58.506 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:70, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:69, RowCount:0, ArgLen:0, start time: 2024-07-02 13:50:58.505 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:50:58.507 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=34] [neededSchemaVersion=35] ["start time"=374.213µs] [phyTblIDs="[69]"] [actionTypes="[8]"]
   > [2024/07/02 13:50:58.509 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=35] ["take time"=2.090997ms] [job="ID:70, Type:create table, State:done, SchemaState:public, SchemaID:65, TableID:69, RowCount:0, ArgLen:1, start time: 2024-07-02 13:50:58.505 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:50:58.510 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:70, Type:create table, State:synced, SchemaState:public, SchemaID:65, TableID:69, RowCount:0, ArgLen:0, start time: 2024-07-02 13:50:58.505 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:50:58.511 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=70]
   > [2024/07/02 13:50:58.511 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 13:50:58.511 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=62] ["first split key"=748000000000000045]
   > [2024/07/02 13:50:58.512 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=35] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_p7c1bd` DISABLE KEYS */;"] [user=root@%]
   > [2024/07/02 13:50:58.514 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=64] ["first at"=748000000000000045] ["first new region left"="{Id:64 StartKey:7480000000000000ff4300000000000000f8 EndKey:7480000000000000ff4500000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:65 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/02 13:50:58.514 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[64]"]
   > [2024/07/02 13:50:58.516 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=35] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_p7c1bd` ENABLE KEYS */;"] [user=root@%]
   > [2024/07/02 13:50:59.556 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > runtime: goroutine stack exceeds 1000000000-byte limit
   > runtime: sp=0xc031d60378 stack=[0xc031d60000, 0xc051d60000]
   > fatal error: stack overflow
   > runtime stack:
   > runtime.throw({0x3b631a0?, 0x59e90a0?})
   > 	/usr/local/go/src/runtime/panic.go:1047 +0x5d fp=0x7f5879c7c888 sp=0x7f5879c7c858 pc=0x13c659d
   > runtime.newstack()
   > 	/usr/local/go/src/runtime/stack.go:1103 +0x5cc fp=0x7f5879c7ca40 sp=0x7f5879c7c888 pc=0x13e15ec
   > runtime.morestack()
   > 	/usr/local/go/src/runtime/asm_amd64.s:570 +0x8b fp=0x7f5879c7ca48 sp=0x7f5879c7ca40 pc=0x13fa60b
   > goroutine 5301 [running]:
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60?, 0xc0119e6000?}, {0x40dbf60?, 0xc0119fe660?})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:183 +0x12c fp=0xc031d60388 sp=0xc031d60380 pc=0x1fb386c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d603c0 sp=0xc031d60388 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d603f8 sp=0xc031d603c0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60430 sp=0xc031d603f8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60468 sp=0xc031d60430 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d604a0 sp=0xc031d60468 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d604d8 sp=0xc031d604a0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60510 sp=0xc031d604d8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60548 sp=0xc031d60510 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60580 sp=0xc031d60548 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d605b8 sp=0xc031d60580 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d605f0 sp=0xc031d605b8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60628 sp=0xc031d605f0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60660 sp=0xc031d60628 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60698 sp=0xc031d60660 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d606d0 sp=0xc031d60698 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60708 sp=0xc031d606d0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60740 sp=0xc031d60708 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60778 sp=0xc031d60740 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d607b0 sp=0xc031d60778 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d607e8 sp=0xc031d607b0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60820 sp=0xc031d607e8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60858 sp=0xc031d60820 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60890 sp=0xc031d60858 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d608c8 sp=0xc031d60890 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60900 sp=0xc031d608c8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60938 sp=0xc031d60900 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60970 sp=0xc031d60938 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d609a8 sp=0xc031d60970 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d609e0 sp=0xc031d609a8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60a18 sp=0xc031d609e0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60a50 sp=0xc031d60a18 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60a88 sp=0xc031d60a50 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60ac0 sp=0xc031d60a88 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60af8 sp=0xc031d60ac0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60b30 sp=0xc031d60af8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60b68 sp=0xc031d60b30 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60ba0 sp=0xc031d60b68 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60bd8 sp=0xc031d60ba0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60c10 sp=0xc031d60bd8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60c48 sp=0xc031d60c10 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60c80 sp=0xc031d60c48 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60cb8 sp=0xc031d60c80 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60cf0 sp=0xc031d60cb8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60d28 sp=0xc031d60cf0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60d60 sp=0xc031d60d28 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60d98 sp=0xc031d60d60 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60dd0 sp=0xc031d60d98 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60e08 sp=0xc031d60dd0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60e40 sp=0xc031d60e08 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60e78 sp=0xc031d60e40 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60eb0 sp=0xc031d60e78 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60ee8 sp=0xc031d60eb0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60f20 sp=0xc031d60ee8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60f58 sp=0xc031d60f20 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60f90 sp=0xc031d60f58 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d60fc8 sp=0xc031d60f90 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d61000 sp=0xc031d60fc8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d61038 sp=0xc031d61000 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d61070 sp=0xc031d61038 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d610a8 sp=0xc031d61070 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d610e0 sp=0xc031d610a8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d61118 sp=0xc031d610e0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d61150 sp=0xc031d61118 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d61188 sp=0xc031d61150 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d611c0 sp=0xc031d61188 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d611f8 sp=0xc031d611c0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d61230 sp=0xc031d611f8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d61268 sp=0xc031d61230 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d612a0 sp=0xc031d61268 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d612d8 sp=0xc031d612a0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d61310 sp=0xc031d612d8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d61348 sp=0xc031d61310 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d61380 sp=0xc031d61348 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d613b8 sp=0xc031d61380 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d613f0 sp=0xc031d613b8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d61428 sp=0xc031d613f0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d61460 sp=0xc031d61428 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d61498 sp=0xc031d61460 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d614d0 sp=0xc031d61498 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d61508 sp=0xc031d614d0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d61540 sp=0xc031d61508 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d61578 sp=0xc031d61540 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d615b0 sp=0xc031d61578 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d615e8 sp=0xc031d615b0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d61620 sp=0xc031d615e8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d61658 sp=0xc031d61620 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d61690 sp=0xc031d61658 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d616c8 sp=0xc031d61690 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d61700 sp=0xc031d616c8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d61738 sp=0xc031d61700 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d61770 sp=0xc031d61738 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d617a8 sp=0xc031d61770 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d617e0 sp=0xc031d617a8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d61818 sp=0xc031d617e0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d61850 sp=0xc031d61818 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d61888 sp=0xc031d61850 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d618c0 sp=0xc031d61888 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119e6000}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d618f8 sp=0xc031d618c0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc0119c9f80}, {0x40dbf60, 0xc0119fe660})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc031d61930 sp=0xc031d618f8 pc=0x1fb3805
   > ...additional frames elided...
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:272 +0x67e
   > goroutine 1 [chan receive]:
   > runtime.gopark(0xc010e89920?, 0xc010c77db0?, 0xbf?, 0xa1?, 0x38a15e0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010c77d30 sp=0xc010c77d10 pc=0x13c9516
   > runtime.chanrecv(0xc0112c7320, 0xc010c77e20, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc010c77dc0 sp=0xc010c77d30 pc=0x13934bb
   > runtime.chanrecv1(0xc000984270?, 0x0?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc010c77de8 sp=0xc010c77dc0 pc=0x1392fb8
   > github.com/pingcap/tidb/server.(*Server).Run(0xc000984270)
   > 	/go/src/github.com/pingcap/tidb/server/server.go:365 +0x1f0 fp=0xc010c77e40 sp=0xc010c77de8 pc=0x3257ff0
   > main.main()
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:220 +0x5b9 fp=0xc010c77f80 sp=0xc010c77e40 pc=0x3438919
   > runtime.main()
   > 	/usr/local/go/src/runtime/proc.go:250 +0x212 fp=0xc010c77fe0 sp=0xc010c77f80 pc=0x13c9152
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010c77fe8 sp=0xc010c77fe0 pc=0x13fc6e1
   > goroutine 2 [force gc (idle)]:
   > runtime.gopark(0x0?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008efb0 sp=0xc00008ef90 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.forcegchelper()
   > 	/usr/local/go/src/runtime/proc.go:302 +0xad fp=0xc00008efe0 sp=0xc00008efb0 pc=0x13c93ad
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008efe8 sp=0xc00008efe0 pc=0x13fc6e1
   > created by runtime.init.6
   > 	/usr/local/go/src/runtime/proc.go:290 +0x25
   > goroutine 3 [GC sweep wait]:
   > runtime.gopark(0x1?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008f790 sp=0xc00008f770 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.bgsweep(0x0?)
   > 	/usr/local/go/src/runtime/mgcsweep.go:297 +0xd7 fp=0xc00008f7c8 sp=0xc00008f790 pc=0x13b2337
   > runtime.gcenable.func1()
   > 	/usr/local/go/src/runtime/mgc.go:178 +0x26 fp=0xc00008f7e0 sp=0xc00008f7c8 pc=0x13a6e06
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008f7e8 sp=0xc00008f7e0 pc=0x13fc6e1
   > created by runtime.gcenable
   > 	/usr/local/go/src/runtime/mgc.go:178 +0x6b
   > goroutine 4 [GC scavenge wait]:
   > runtime.gopark(0xc0000c0000?, 0x40acc30?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008ff70 sp=0xc00008ff50 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.(*scavengerState).park(0x60385e0)
   > 	/usr/local/go/src/runtime/mgcscavenge.go:389 +0x53 fp=0xc00008ffa0 sp=0xc00008ff70 pc=0x13b0313
   > runtime.bgscavenge(0x0?)
   > 	/usr/local/go/src/runtime/mgcscavenge.go:622 +0x65 fp=0xc00008ffc8 sp=0xc00008ffa0 pc=0x13b0925
   > runtime.gcenable.func2()
   > 	/usr/local/go/src/runtime/mgc.go:179 +0x26 fp=0xc00008ffe0 sp=0xc00008ffc8 pc=0x13a6da6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008ffe8 sp=0xc00008ffe0 pc=0x13fc6e1
   > created by runtime.gcenable
   > 	/usr/local/go/src/runtime/mgc.go:179 +0xaa
   > goroutine 18 [finalizer wait]:
   > runtime.gopark(0x6039860?, 0xc0001024e0?, 0x0?, 0x0?, 0xc00008e770?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008e628 sp=0xc00008e608 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.runfinq()
   > 	/usr/local/go/src/runtime/mfinal.go:180 +0x10f fp=0xc00008e7e0 sp=0xc00008e628 pc=0x13a5f0f
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008e7e8 sp=0xc00008e7e0 pc=0x13fc6e1
   > created by runtime.createfing
   > 	/usr/local/go/src/runtime/mfinal.go:157 +0x45
   > goroutine 19 [GC worker (idle)]:
   > runtime.gopark(0x0?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008a750 sp=0xc00008a730 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008a7e0 sp=0xc00008a750 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008a7e8 sp=0xc00008a7e0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 20 [GC worker (idle)]:
   > runtime.gopark(0x26572176cb8d?, 0x3?, 0x50?, 0xbd?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008af50 sp=0xc00008af30 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008afe0 sp=0xc00008af50 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008afe8 sp=0xc00008afe0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 5 [GC worker (idle)]:
   > runtime.gopark(0x265721770792?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000090750 sp=0xc000090730 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0000907e0 sp=0xc000090750 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000907e8 sp=0xc0000907e0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 34 [GC worker (idle)]:
   > runtime.gopark(0x265721771837?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004aa750 sp=0xc0004aa730 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0004aa7e0 sp=0xc0004aa750 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004aa7e8 sp=0xc0004aa7e0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 35 [GC worker (idle)]:
   > runtime.gopark(0x2657216c5c5f?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004aaf50 sp=0xc0004aaf30 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0004aafe0 sp=0xc0004aaf50 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004aafe8 sp=0xc0004aafe0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 36 [GC worker (idle)]:
   > runtime.gopark(0x606d020?, 0x1?, 0x51?, 0x91?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004ab750 sp=0xc0004ab730 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0004ab7e0 sp=0xc0004ab750 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004ab7e8 sp=0xc0004ab7e0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 37 [GC worker (idle)]:
   > runtime.gopark(0x26572176f6ee?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004abf50 sp=0xc0004abf30 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0004abfe0 sp=0xc0004abf50 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004abfe8 sp=0xc0004abfe0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 21 [GC worker (idle)]:
   > runtime.gopark(0x265721770034?, 0x3?, 0x93?, 0x99?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008b750 sp=0xc00008b730 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008b7e0 sp=0xc00008b750 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008b7e8 sp=0xc00008b7e0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 38 [GC worker (idle)]:
   > runtime.gopark(0x2657216c5c5f?, 0x1?, 0x43?, 0xd?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004ac750 sp=0xc0004ac730 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0004ac7e0 sp=0xc0004ac750 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004ac7e8 sp=0xc0004ac7e0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 6 [GC worker (idle)]:
   > runtime.gopark(0x26570f4047a5?, 0x3?, 0xa9?, 0x6e?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000090f50 sp=0xc000090f30 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc000090fe0 sp=0xc000090f50 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000090fe8 sp=0xc000090fe0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 39 [GC worker (idle)]:
   > runtime.gopark(0x2657216c4f46?, 0x3?, 0x60?, 0x25?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004acf50 sp=0xc0004acf30 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0004acfe0 sp=0xc0004acf50 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004acfe8 sp=0xc0004acfe0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 40 [GC worker (idle)]:
   > runtime.gopark(0x2657216c5c5f?, 0x3?, 0xa3?, 0x7?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004ad750 sp=0xc0004ad730 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0004ad7e0 sp=0xc0004ad750 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004ad7e8 sp=0xc0004ad7e0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 22 [GC worker (idle)]:
   > runtime.gopark(0x2657217710d9?, 0x3?, 0x55?, 0xae?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008bf50 sp=0xc00008bf30 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008bfe0 sp=0xc00008bf50 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008bfe8 sp=0xc00008bfe0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 41 [GC worker (idle)]:
   > runtime.gopark(0x2657216c68ec?, 0x3?, 0xc?, 0x87?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004adf50 sp=0xc0004adf30 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0004adfe0 sp=0xc0004adf50 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004adfe8 sp=0xc0004adfe0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 7 [GC worker (idle)]:
   > runtime.gopark(0x265721770034?, 0x1?, 0xaa?, 0x87?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000091750 sp=0xc000091730 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0000917e0 sp=0xc000091750 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000917e8 sp=0xc0000917e0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 42 [GC worker (idle)]:
   > runtime.gopark(0x2657218977e7?, 0x1?, 0x5a?, 0xb?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004a6750 sp=0xc0004a6730 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0004a67e0 sp=0xc0004a6750 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004a67e8 sp=0xc0004a67e0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 5346 [chan receive]:
   > runtime.gopark(0xc0005a8c88?, 0x13d1800?, 0x70?, 0x66?, 0xc00023a820?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0005a8c80 sp=0xc0005a8c60 pc=0x13c9516
   > runtime.chanrecv(0xc0119e6d80, 0xc0005a8d68, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc0005a8d10 sp=0xc0005a8c80 pc=0x13934bb
   > runtime.chanrecv2(0xc01083bc00?, 0x40d68d0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc0005a8d38 sp=0xc0005a8d10 pc=0x1392ff8
   > github.com/pingcap/tidb/executor.(*UnionExec).Next(0xc01083bc00, {0x40d68d0, 0xc010546960}, 0xc0114b00f0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1702 +0x85 fp=0xc0005a8da0 sp=0xc0005a8d38 pc=0x30425c5
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc010546960}, {0x40d9ea0, 0xc01083bc00}, 0xc0114b00f0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc0005a8ee0 sp=0xc0005a8da0 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*HashAggExec).fetchChildData(0xc010d8e200, {0x40d68d0, 0xc010546960}, 0xc010546960?)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:798 +0x1be fp=0xc0005a8fb0 sp=0xc0005a8ee0 pc=0x2fbc0fe
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func3()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:835 +0x32 fp=0xc0005a8fe0 sp=0xc0005a8fb0 pc=0x2fbce72
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0005a8fe8 sp=0xc0005a8fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:835 +0xea
   > goroutine 11 [chan receive]:
   > runtime.gopark(0xc00008d6d8?, 0x13cf37b?, 0x20?, 0xd7?, 0x13e6de5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008d6c8 sp=0xc00008d6a8 pc=0x13c9516
   > runtime.chanrecv(0xc0002fd1a0, 0xc00008d7a0, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc00008d758 sp=0xc00008d6c8 pc=0x13934bb
   > runtime.chanrecv2(0x6fc23ac00?, 0x0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc00008d780 sp=0xc00008d758 pc=0x1392ff8
   > github.com/golang/glog.(*loggingT).flushDaemon(0x0?)
   > 	/go/pkg/mod/github.com/golang/glog@v1.0.0/glog.go:882 +0x6a fp=0xc00008d7c8 sp=0xc00008d780 pc=0x2482faa
   > github.com/golang/glog.init.0.func1()
   > 	/go/pkg/mod/github.com/golang/glog@v1.0.0/glog.go:410 +0x26 fp=0xc00008d7e0 sp=0xc00008d7c8 pc=0x2480906
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008d7e8 sp=0xc00008d7e0 pc=0x13fc6e1
   > created by github.com/golang/glog.init.0
   > 	/go/pkg/mod/github.com/golang/glog@v1.0.0/glog.go:410 +0x1bf
   > goroutine 12 [select]:
   > runtime.gopark(0xc00008cf88?, 0x3?, 0x98?, 0xe5?, 0xc00008cf72?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008cdf8 sp=0xc00008cdd8 pc=0x13c9516
   > runtime.selectgo(0xc00008cf88, 0xc00008cf6c, 0xc00046e700?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00008cf38 sp=0xc00008cdf8 pc=0x13d9bdc
   > go.opencensus.io/stats/view.(*worker).start(0xc00046e700)
   > 	/go/pkg/mod/go.opencensus.io@v0.23.0/stats/view/worker.go:276 +0xad fp=0xc00008cfc8 sp=0xc00008cf38 pc=0x2b9244d
   > go.opencensus.io/stats/view.init.0.func1()
   > 	/go/pkg/mod/go.opencensus.io@v0.23.0/stats/view/worker.go:34 +0x26 fp=0xc00008cfe0 sp=0xc00008cfc8 pc=0x2b916c6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008cfe8 sp=0xc00008cfe0 pc=0x13fc6e1
   > created by go.opencensus.io/stats/view.init.0
   > 	/go/pkg/mod/go.opencensus.io@v0.23.0/stats/view/worker.go:34 +0x8d
   > goroutine 278 [select]:
   > runtime.gopark(0xc00009cf30?, 0x3?, 0x8?, 0x0?, 0xc00009cf0a?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00009cd90 sp=0xc00009cd70 pc=0x13c9516
   > runtime.selectgo(0xc00009cf30, 0xc00009cf04, 0xc00008e718?, 0x0, 0x3?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00009ced0 sp=0xc00009cd90 pc=0x13d9bdc
   > github.com/pingcap/tidb/util/cpuprofile.(*parallelCPUProfiler).profilingLoop(0xc0000c4360)
   > 	/go/src/github.com/pingcap/tidb/util/cpuprofile/cpuprofile.go:166 +0x105 fp=0xc00009cf78 sp=0xc00009ced0 pc=0x25951c5
   > github.com/pingcap/tidb/util/cpuprofile.(*parallelCPUProfiler).profilingLoop-fm()
   > 	<autogenerated>:1 +0x26 fp=0xc00009cf90 sp=0xc00009cf78 pc=0x2596e66
   > github.com/pingcap/tidb/util.WithRecovery(0xc00009cfa6?, 0xc000d98120?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc00009cfc0 sp=0xc00009cf90 pc=0x208e513
   > github.com/pingcap/tidb/util/cpuprofile.(*parallelCPUProfiler).start.func1()
   > 	/go/src/github.com/pingcap/tidb/util/cpuprofile/cpuprofile.go:113 +0x28 fp=0xc00009cfe0 sp=0xc00009cfc0 pc=0x2594da8
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00009cfe8 sp=0xc00009cfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/util/cpuprofile.(*parallelCPUProfiler).start
   > 	/go/src/github.com/pingcap/tidb/util/cpuprofile/cpuprofile.go:113 +0x176
   > goroutine 279 [chan receive]:
   > runtime.gopark(0xc00012c3c0?, 0x13cf374?, 0x38?, 0xde?, 0x13e6de5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000d5dde0 sp=0xc000d5ddc0 pc=0x13c9516
   > runtime.chanrecv(0xc0009c0600, 0x0, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000d5de70 sp=0xc000d5dde0 pc=0x13934bb
   > runtime.chanrecv1(0x5f5e100?, 0x3b88785?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc000d5de98 sp=0xc000d5de70 pc=0x1392fb8
   > github.com/pingcap/tidb/util/systimemon.StartMonitor(0x3c82178, 0x3c817e0, 0xc000d8f560)
   > 	/go/src/github.com/pingcap/tidb/util/systimemon/systime_mon.go:32 +0x185 fp=0xc000d5dfb8 sp=0xc000d5de98 pc=0x3433bc5
   > main.setupMetrics.func3()
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:716 +0x31 fp=0xc000d5dfe0 sp=0xc000d5dfb8 pc=0x343c391
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000d5dfe8 sp=0xc000d5dfe0 pc=0x13fc6e1
   > created by main.setupMetrics
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:716 +0x115
   > goroutine 280 [select]:
   > runtime.gopark(0xc000ddf780?, 0x2?, 0x8?, 0x0?, 0xc000ddf74c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000ddf5d0 sp=0xc000ddf5b0 pc=0x13c9516
   > runtime.selectgo(0xc000ddf780, 0xc000ddf748, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000ddf710 sp=0xc000ddf5d0 pc=0x13d9bdc
   > github.com/pingcap/badger.(*DB).updateSize(0x0?, 0xc000dc61e0)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/db.go:1039 +0x105 fp=0xc000ddf7c0 sp=0xc000ddf710 pc=0x33233a5
   > github.com/pingcap/badger.Open.func5()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/db.go:328 +0x2a fp=0xc000ddf7e0 sp=0xc000ddf7c0 pc=0x331d46a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000ddf7e8 sp=0xc000ddf7e0 pc=0x13fc6e1
   > created by github.com/pingcap/badger.Open
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/db.go:328 +0xf5c
   > goroutine 281 [select]:
   > runtime.gopark(0xc000ddff88?, 0x2?, 0x10?, 0x0?, 0xc000ddff64?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000ddfde8 sp=0xc000ddfdc8 pc=0x13c9516
   > runtime.selectgo(0xc000ddff88, 0xc000ddff60, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000ddff28 sp=0xc000ddfde8 pc=0x13d9bdc
   > github.com/pingcap/badger/epoch.(*ResourceManager).collectLoop(0x0?, 0xc000dc6210)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/epoch/manager.go:101 +0xd3 fp=0xc000ddffc0 sp=0xc000ddff28 pc=0x3299693
   > github.com/pingcap/badger/epoch.NewResourceManager.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/epoch/manager.go:79 +0x2a fp=0xc000ddffe0 sp=0xc000ddffc0 pc=0x329942a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000ddffe8 sp=0xc000ddffe0 pc=0x13fc6e1
   > created by github.com/pingcap/badger/epoch.NewResourceManager
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/epoch/manager.go:79 +0xdd
   > goroutine 282 [select]:
   > runtime.gopark(0xc00009de68?, 0x2?, 0x8?, 0x21?, 0xc00009de3c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00009dcc0 sp=0xc00009dca0 pc=0x13c9516
   > runtime.selectgo(0xc00009de68, 0xc00009de38, 0x0?, 0x1, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00009de00 sp=0xc00009dcc0 pc=0x13d9bdc
   > github.com/pingcap/badger.Open.func4()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/db.go:342 +0x155 fp=0xc00009dfe0 sp=0xc00009de00 pc=0x331d3f5
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00009dfe8 sp=0xc00009dfe0 pc=0x13fc6e1
   > created by github.com/pingcap/badger.Open
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/db.go:339 +0x11f8
   > goroutine 43 [select]:
   > runtime.gopark(0xc0004a7f08?, 0x2?, 0x0?, 0x0?, 0xc0004a7ee4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004a7d68 sp=0xc0004a7d48 pc=0x13c9516
   > runtime.selectgo(0xc0004a7f08, 0xc0004a7ee0, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0004a7ea8 sp=0xc0004a7d68 pc=0x13d9bdc
   > github.com/pingcap/badger.(*blobGCHandler).run(0xc000c30040, 0xc000d52048)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/blob.go:468 +0xd6 fp=0xc0004a7fc0 sp=0xc0004a7ea8 pc=0x33117f6
   > github.com/pingcap/badger.(*blobManager).Open.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/blob.go:292 +0x2a fp=0xc0004a7fe0 sp=0xc0004a7fc0 pc=0x33104aa
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004a7fe8 sp=0xc0004a7fe0 pc=0x13fc6e1
   > created by github.com/pingcap/badger.(*blobManager).Open
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/blob.go:292 +0x5bd
   > goroutine 44 [select]:
   > runtime.gopark(0xc0004a8760?, 0x2?, 0x0?, 0x30?, 0xc0004a872c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004a8598 sp=0xc0004a8578 pc=0x13c9516
   > runtime.selectgo(0xc0004a8760, 0xc0004a8728, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0004a86d8 sp=0xc0004a8598 pc=0x13d9bdc
   > github.com/pingcap/badger.(*levelsController).runWorker(0xc00018fdc0, 0xc000d52078, 0x0)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/levels.go:212 +0x1fb fp=0xc0004a87b8 sp=0xc0004a86d8 pc=0x332b8db
   > github.com/pingcap/badger.(*levelsController).startCompact.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/levels.go:180 +0x2e fp=0xc0004a87e0 sp=0xc0004a87b8 pc=0x332b6ae
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004a87e8 sp=0xc0004a87e0 pc=0x13fc6e1
   > created by github.com/pingcap/badger.(*levelsController).startCompact
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/levels.go:180 +0x65
   > goroutine 45 [select]:
   > runtime.gopark(0xc0004a8f60?, 0x2?, 0x0?, 0x30?, 0xc0004a8f2c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004a8d98 sp=0xc0004a8d78 pc=0x13c9516
   > runtime.selectgo(0xc0004a8f60, 0xc0004a8f28, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0004a8ed8 sp=0xc0004a8d98 pc=0x13d9bdc
   > github.com/pingcap/badger.(*levelsController).runWorker(0xc00018fdc0, 0xc000d52078, 0x0)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/levels.go:212 +0x1fb fp=0xc0004a8fb8 sp=0xc0004a8ed8 pc=0x332b8db
   > github.com/pingcap/badger.(*levelsController).startCompact.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/levels.go:180 +0x2e fp=0xc0004a8fe0 sp=0xc0004a8fb8 pc=0x332b6ae
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004a8fe8 sp=0xc0004a8fe0 pc=0x13fc6e1
   > created by github.com/pingcap/badger.(*levelsController).startCompact
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/levels.go:180 +0x65
   > goroutine 46 [select]:
   > runtime.gopark(0xc0004a9760?, 0x2?, 0x0?, 0x30?, 0xc0004a972c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004a9598 sp=0xc0004a9578 pc=0x13c9516
   > runtime.selectgo(0xc0004a9760, 0xc0004a9728, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0004a96d8 sp=0xc0004a9598 pc=0x13d9bdc
   > github.com/pingcap/badger.(*levelsController).runWorker(0xc00018fdc0, 0xc000d52078, 0x1)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/levels.go:212 +0x1fb fp=0xc0004a97b8 sp=0xc0004a96d8 pc=0x332b8db
   > github.com/pingcap/badger.(*levelsController).startCompact.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/levels.go:180 +0x2e fp=0xc0004a97e0 sp=0xc0004a97b8 pc=0x332b6ae
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004a97e8 sp=0xc0004a97e0 pc=0x13fc6e1
   > created by github.com/pingcap/badger.(*levelsController).startCompact
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/levels.go:180 +0x65
   > goroutine 47 [chan receive]:
   > runtime.gopark(0x0?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00009fac0 sp=0xc00009faa0 pc=0x13c9516
   > runtime.chanrecv(0xc000d98d80, 0xc00009fc60, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc00009fb50 sp=0xc00009fac0 pc=0x13934bb
   > runtime.chanrecv2(0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc00009fb78 sp=0xc00009fb50 pc=0x1392ff8
   > github.com/pingcap/badger.(*DB).runFlushMemTable(0xc000dbe900, 0x0?)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/db.go:920 +0xdd fp=0xc00009ffc0 sp=0xc00009fb78 pc=0x3321e5d
   > github.com/pingcap/badger.Open.func6()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/db.go:361 +0x2a fp=0xc00009ffe0 sp=0xc00009ffc0 pc=0x331d26a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00009ffe8 sp=0xc00009ffe0 pc=0x13fc6e1
   > created by github.com/pingcap/badger.Open
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/db.go:361 +0x158d
   > goroutine 283 [select]:
   > runtime.gopark(0xc0000a1f78?, 0x3?, 0x25?, 0x28?, 0xc0000a1f32?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0000a1d98 sp=0xc0000a1d78 pc=0x13c9516
   > runtime.selectgo(0xc0000a1f78, 0xc0000a1f2c, 0x1?, 0x0, 0xc000af1040?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0000a1ed8 sp=0xc0000a1d98 pc=0x13d9bdc
   > github.com/pingcap/badger.(*writeWorker).runWriteVLog(0xc00014b100, 0xc000d520d8)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/writer.go:94 +0x137 fp=0xc0000a1fc0 sp=0xc0000a1ed8 pc=0x333b817
   > github.com/pingcap/badger.startWriteWorker.func2()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/writer.go:64 +0x2a fp=0xc0000a1fe0 sp=0xc0000a1fc0 pc=0x333b2ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000a1fe8 sp=0xc0000a1fe0 pc=0x13fc6e1
   > created by github.com/pingcap/badger.startWriteWorker
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/writer.go:64 +0x1f9
   > goroutine 284 [chan receive, locked to thread]:
   > runtime.gopark(0xc0000a2e98?, 0x1464528?, 0xf?, 0x0?, 0x1?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0000a2e68 sp=0xc0000a2e48 pc=0x13c9516
   > runtime.chanrecv(0xc0009c01e0, 0xc0000a2f88, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc0000a2ef8 sp=0xc0000a2e68 pc=0x13934bb
   > runtime.chanrecv2(0xc000db7320?, 0x3ef86300ded5c171?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc0000a2f20 sp=0xc0000a2ef8 pc=0x1392ff8
   > github.com/pingcap/badger.(*writeWorker).runWriteLSM(0xc00014b100, 0xc000dc6018?)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/writer.go:141 +0x15e fp=0xc0000a2fc0 sp=0xc0000a2f20 pc=0x333be5e
   > github.com/pingcap/badger.startWriteWorker.func3()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/writer.go:65 +0x2a fp=0xc0000a2fe0 sp=0xc0000a2fc0 pc=0x333b28a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000a2fe8 sp=0xc0000a2fe0 pc=0x13fc6e1
   > created by github.com/pingcap/badger.startWriteWorker
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/writer.go:65 +0x24d
   > goroutine 285 [chan receive]:
   > runtime.gopark(0x0?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000525ea8 sp=0xc000525e88 pc=0x13c9516
   > runtime.chanrecv(0xc0009c0240, 0xc000525f88, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000525f38 sp=0xc000525ea8 pc=0x13934bb
   > runtime.chanrecv2(0xc000dea060?, 0x0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc000525f60 sp=0xc000525f38 pc=0x1392ff8
   > github.com/pingcap/badger.(*writeWorker).runMergeLSM(0x0?, 0x0?)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/writer.go:154 +0x9b fp=0xc000525fc0 sp=0xc000525f60 pc=0x333bfdb
   > github.com/pingcap/badger.startWriteWorker.func4()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/writer.go:66 +0x2a fp=0xc000525fe0 sp=0xc000525fc0 pc=0x333b22a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000525fe8 sp=0xc000525fe0 pc=0x13fc6e1
   > created by github.com/pingcap/badger.startWriteWorker
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/writer.go:66 +0x2a5
   > goroutine 286 [select]:
   > runtime.gopark(0xc0000a3f88?, 0x2?, 0x0?, 0x0?, 0xc0000a3f4c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0000a3da0 sp=0xc0000a3d80 pc=0x13c9516
   > runtime.selectgo(0xc0000a3f88, 0xc0000a3f48, 0xc010ba5890?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0000a3ee0 sp=0xc0000a3da0 pc=0x13d9bdc
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.writeDBWorker.run({0xc0009c0300?, 0xc000c30240?})
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:96 +0x145 fp=0xc0000a3fc0 sp=0xc0000a3ee0 pc=0x338c745
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*dbWriter).Open.func1()
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:202 +0x2a fp=0xc0000a3fe0 sp=0xc0000a3fc0 pc=0x338d2ca
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000a3fe8 sp=0xc0000a3fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*dbWriter).Open
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:199 +0xc5
   > goroutine 287 [select]:
   > runtime.gopark(0xc000d59e70?, 0x2?, 0x90?, 0x9e?, 0xc000d59e1c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000d59c58 sp=0xc000d59c38 pc=0x13c9516
   > runtime.selectgo(0xc000d59e70, 0xc000d59e18, 0x13?, 0x0, 0xc00fd76700?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000d59d98 sp=0xc000d59c58 pc=0x13d9bdc
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.writeLockWorker.run({0xc0009c0360?, 0xc000c30240?})
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:148 +0x15f fp=0xc000d59fc0 sp=0xc000d59d98 pc=0x338cd1f
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*dbWriter).Open.func2()
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:209 +0x2a fp=0xc000d59fe0 sp=0xc000d59fc0 pc=0x338d26a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000d59fe8 sp=0xc000d59fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*dbWriter).Open
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:206 +0x159
   > goroutine 288 [select]:
   > runtime.gopark(0xc000ddd718?, 0x2?, 0x0?, 0x0?, 0xc000ddd704?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000ddd588 sp=0xc000ddd568 pc=0x13c9516
   > runtime.selectgo(0xc000ddd718, 0xc000ddd700, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000ddd6c8 sp=0xc000ddd588 pc=0x13d9bdc
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*MVCCStore).runUpdateSafePointLoop(0xc000c6c880)
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:1705 +0x217 fp=0xc000ddd7c8 sp=0xc000ddd6c8 pc=0x337e3d7
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.NewMVCCStore.func1()
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:86 +0x26 fp=0xc000ddd7e0 sp=0xc000ddd7c8 pc=0x336f0a6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000ddd7e8 sp=0xc000ddd7e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.NewMVCCStore
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:86 +0x337
   > goroutine 289 [select]:
   > runtime.gopark(0xc000dddfb0?, 0x2?, 0x0?, 0x0?, 0xc000dddf9c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000ddde28 sp=0xc000ddde08 pc=0x13c9516
   > runtime.selectgo(0xc000dddfb0, 0xc000dddf98, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000dddf68 sp=0xc000ddde28 pc=0x13d9bdc
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*MVCCStore).StartDeadlockDetection.func1()
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:1378 +0x7b fp=0xc000dddfe0 sp=0xc000dddf68 pc=0x337b11b
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000dddfe8 sp=0xc000dddfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*MVCCStore).StartDeadlockDetection
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:1376 +0xb6
   > goroutine 306 [select]:
   > runtime.gopark(0xc0057f2f78?, 0x2?, 0x0?, 0x0?, 0xc0057f2f3c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0057f2dc0 sp=0xc0057f2da0 pc=0x13c9516
   > runtime.selectgo(0xc0057f2f78, 0xc0057f2f38, 0xc000de0fb0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0057f2f00 sp=0xc0057f2dc0 pc=0x13d9bdc
   > github.com/tikv/client-go/v2/oracle/oracles.(*pdOracle).updateTS(0xc000cfad20, {0x40d6860, 0xc000120008}, 0xc000dc6018?)
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.1-0.20220311043619-5042c6f2aaa6/oracle/oracles/pd.go:229 +0x128 fp=0xc0057f2fb0 sp=0xc0057f2f00 pc=0x1e576a8
   > github.com/tikv/client-go/v2/oracle/oracles.NewPdOracle.func1()
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.1-0.20220311043619-5042c6f2aaa6/oracle/oracles/pd.go:77 +0x32 fp=0xc0057f2fe0 sp=0xc0057f2fb0 pc=0x1e568d2
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0057f2fe8 sp=0xc0057f2fe0 pc=0x13fc6e1
   > created by github.com/tikv/client-go/v2/oracle/oracles.NewPdOracle
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.1-0.20220311043619-5042c6f2aaa6/oracle/oracles/pd.go:77 +0x119
   > goroutine 307 [select]:
   > runtime.gopark(0xc000de1f78?, 0x3?, 0x10?, 0x0?, 0xc000de1f5a?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000de1de0 sp=0xc000de1dc0 pc=0x13c9516
   > runtime.selectgo(0xc000de1f78, 0xc000de1f54, 0x1000000020002?, 0x0, 0xc00043b0a8?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000de1f20 sp=0xc000de1de0 pc=0x13d9bdc
   > github.com/tikv/client-go/v2/internal/locate.(*RegionCache).asyncCheckAndResolveLoop(0xc000c6d200, 0xc000d520d8?)
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.1-0.20220311043619-5042c6f2aaa6/internal/locate/region_cache.go:423 +0xd1 fp=0xc000de1fc0 sp=0xc000de1f20 pc=0x1e25c11
   > github.com/tikv/client-go/v2/internal/locate.NewRegionCache.func1()
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.1-0.20220311043619-5042c6f2aaa6/internal/locate/region_cache.go:394 +0x2a fp=0xc000de1fe0 sp=0xc000de1fc0 pc=0x1e2588a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000de1fe8 sp=0xc000de1fe0 pc=0x13fc6e1
   > created by github.com/tikv/client-go/v2/internal/locate.NewRegionCache
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.1-0.20220311043619-5042c6f2aaa6/internal/locate/region_cache.go:394 +0x2e6
   > goroutine 308 [select]:
   > runtime.gopark(0xc000d56f10?, 0x2?, 0x0?, 0x30?, 0xc000d56eac?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000d56d10 sp=0xc000d56cf0 pc=0x13c9516
   > runtime.selectgo(0xc000d56f10, 0xc000d56ea8, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000d56e50 sp=0xc000d56d10 pc=0x13d9bdc
   > github.com/tikv/client-go/v2/tikv.(*KVStore).runSafePointChecker(0xc000230500)
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.1-0.20220311043619-5042c6f2aaa6/tikv/kv.go:234 +0x12b fp=0xc000d56fc8 sp=0xc000d56e50 pc=0x1e9a70b
   > github.com/tikv/client-go/v2/tikv.NewKVStore.func1()
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.1-0.20220311043619-5042c6f2aaa6/tikv/kv.go:189 +0x26 fp=0xc000d56fe0 sp=0xc000d56fc8 pc=0x1e9a506
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000d56fe8 sp=0xc000d56fe0 pc=0x13fc6e1
   > created by github.com/tikv/client-go/v2/tikv.NewKVStore
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.1-0.20220311043619-5042c6f2aaa6/tikv/kv.go:189 +0x416
   > goroutine 309 [select]:
   > runtime.gopark(0xc0057ecf80?, 0x2?, 0x20?, 0xd0?, 0xc0057ecf44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0057ecdc8 sp=0xc0057ecda8 pc=0x13c9516
   > runtime.selectgo(0xc0057ecf80, 0xc0057ecf40, 0xc000d36080?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0057ecf08 sp=0xc0057ecdc8 pc=0x13d9bdc
   > github.com/tikv/client-go/v2/tikv.(*KVStore).safeTSUpdater(0xc000230500)
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.1-0.20220311043619-5042c6f2aaa6/tikv/kv.go:521 +0x165 fp=0xc0057ecfc8 sp=0xc0057ecf08 pc=0x1e9c6e5
   > github.com/tikv/client-go/v2/tikv.NewKVStore.func2()
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.1-0.20220311043619-5042c6f2aaa6/tikv/kv.go:190 +0x26 fp=0xc0057ecfe0 sp=0xc0057ecfc8 pc=0x1e9a4a6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0057ecfe8 sp=0xc0057ecfe0 pc=0x13fc6e1
   > created by github.com/tikv/client-go/v2/tikv.NewKVStore
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.1-0.20220311043619-5042c6f2aaa6/tikv/kv.go:190 +0x456
   > goroutine 310 [select]:
   > runtime.gopark(0xc000de0798?, 0x2?, 0x6a?, 0xd3?, 0xc000de076c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000de05e8 sp=0xc000de05c8 pc=0x13c9516
   > runtime.selectgo(0xc000de0798, 0xc000de0768, 0x200000?, 0x0, 0x7?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000de0728 sp=0xc000de05e8 pc=0x13d9bdc
   > github.com/dgraph-io/ristretto.(*defaultPolicy).processItems(0xc000c31600)
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.1.0/policy.go:102 +0x91 fp=0xc000de07c8 sp=0xc000de0728 pc=0x248a7b1
   > github.com/dgraph-io/ristretto.newDefaultPolicy.func1()
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.1.0/policy.go:86 +0x26 fp=0xc000de07e0 sp=0xc000de07c8 pc=0x248a666
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000de07e8 sp=0xc000de07e0 pc=0x13fc6e1
   > created by github.com/dgraph-io/ristretto.newDefaultPolicy
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.1.0/policy.go:86 +0x156
   > goroutine 311 [select]:
   > runtime.gopark(0xc000109f88?, 0x3?, 0x0?, 0x0?, 0xc000109f32?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000109da8 sp=0xc000109d88 pc=0x13c9516
   > runtime.selectgo(0xc000109f88, 0xc000109f2c, 0xc000c31600?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000109ee8 sp=0xc000109da8 pc=0x13d9bdc
   > github.com/dgraph-io/ristretto.(*Cache).processItems(0xc000c6d280)
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.1.0/cache.go:452 +0x15e fp=0xc000109fc8 sp=0xc000109ee8 pc=0x2488cfe
   > github.com/dgraph-io/ristretto.NewCache.func5()
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.1.0/cache.go:207 +0x26 fp=0xc000109fe0 sp=0xc000109fc8 pc=0x2487da6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000109fe8 sp=0xc000109fe0 pc=0x13fc6e1
   > created by github.com/dgraph-io/ristretto.NewCache
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.1.0/cache.go:207 +0x6a5
   > goroutine 5349 [select]:
   > runtime.gopark(0xc00fe36f28?, 0x2?, 0x0?, 0xe0?, 0xc00fe36eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fe36d58 sp=0xc00fe36d38 pc=0x13c9516
   > runtime.selectgo(0xc00fe36f28, 0xc00fe36ee8, 0x3b67af1?, 0x0, 0xc000ce79b0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fe36e98 sp=0xc00fe36d58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc0114b8180, {0x4134ba0, 0xc0113a58c0}, 0xc0114a01a0, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc00fe36fa8 sp=0xc00fe36e98 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc00fe36fe0 sp=0xc00fe36fa8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fe36fe8 sp=0xc00fe36fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 749 [select]:
   > runtime.gopark(0xc00ffc3778?, 0x2?, 0x0?, 0x0?, 0xc00ffc36ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00ffc3558 sp=0xc00ffc3538 pc=0x13c9516
   > runtime.selectgo(0xc00ffc3778, 0xc00ffc36e8, 0x3b67af1?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00ffc3698 sp=0xc00ffc3558 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc00ff7e840, {0x40d68d0?, 0xc010546960?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc00ffc37b8 sp=0xc00ffc3698 pc=0x30ecdf4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc00ffc37e0 sp=0xc00ffc37b8 pc=0x30ec08e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00ffc37e8 sp=0xc00ffc37e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 671 [chan receive]:
   > runtime.gopark(0x606d020?, 0xc00faa5f20?, 0x28?, 0xa3?, 0x40ee3a0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00faa5ea0 sp=0xc00faa5e80 pc=0x13c9516
   > runtime.chanrecv(0xc000cee420, 0xc00faa5fa0, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc00faa5f30 sp=0xc00faa5ea0 pc=0x13934bb
   > runtime.chanrecv1(0x0?, 0xc00fd1cfc0?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc00faa5f58 sp=0xc00faa5f30 pc=0x1392fb8
   > github.com/pingcap/tidb/util/signal.SetupSignalHandler.func1()
   > 	/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:38 +0x4f fp=0xc00faa5fe0 sp=0xc00faa5f58 pc=0x343388f
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00faa5fe8 sp=0xc00faa5fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/util/signal.SetupSignalHandler
   > 	/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:35 +0xb6
   > goroutine 563 [select]:
   > runtime.gopark(0xc0057cdf38?, 0x2?, 0x5?, 0x0?, 0xc0057cdefc?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0057cdd50 sp=0xc0057cdd30 pc=0x13c9516
   > runtime.selectgo(0xc0057cdf38, 0xc0057cdef8, 0x1?, 0x0, 0x2?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0057cde90 sp=0xc0057cdd50 pc=0x13d9bdc
   > github.com/pingcap/tidb/ddl.(*ddl).limitDDLJobs(0xc010bbc700)
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl_worker.go:269 +0x173 fp=0xc0057cdfc8 sp=0xc0057cde90 pc=0x2717a13
   > github.com/pingcap/tidb/ddl.(*ddl).Start.func2()
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:381 +0x26 fp=0xc0057cdfe0 sp=0xc0057cdfc8 pc=0x26d42c6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0057cdfe8 sp=0xc0057cdfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/ddl.(*ddl).Start
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:381 +0x2aa
   > goroutine 657 [select]:
   > runtime.gopark(0xc00fc04f28?, 0x2?, 0x4?, 0x30?, 0xc00fc04ed4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fc04d48 sp=0xc00fc04d28 pc=0x13c9516
   > runtime.selectgo(0xc00fc04f28, 0xc00fc04ed0, 0x9?, 0x0, 0x15?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fc04e88 sp=0xc00fc04d48 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).TelemetryReportLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1185 +0x11c fp=0xc00fc04fe0 sp=0xc00fc04e88 pc=0x279663c
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fc04fe8 sp=0xc00fc04fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).TelemetryReportLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1177 +0x285
   > goroutine 699 [chan receive]:
   > runtime.gopark(0xc0005b4c00?, 0xc00fe12a00?, 0xb0?, 0x29?, 0xc010adf440?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fbb4af8 sp=0xc00fbb4ad8 pc=0x13c9516
   > runtime.chanrecv(0xc010adefc0, 0xc00fbb4bd8, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc00fbb4b88 sp=0xc00fbb4af8 pc=0x13934bb
   > runtime.chanrecv1(0xc00fb52c60?, 0x40d68d0?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc00fbb4bb0 sp=0xc00fbb4b88 pc=0x1392fb8
   > github.com/pingcap/tidb/executor.(*ProjectionExec).parallelExecute(0xc00fb52c60, {0x40d68d0?, 0xc010546960?}, 0xc00fe126e0)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:218 +0x92 fp=0xc00fbb4bf8 sp=0xc00fbb4bb0 pc=0x30eb612
   > github.com/pingcap/tidb/executor.(*ProjectionExec).Next(0xc00fb52c60, {0x40d68d0, 0xc010546960}, 0x0?)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:182 +0x78 fp=0xc00fbb4c30 sp=0xc00fbb4bf8 pc=0x30eb338
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc010546960}, {0x40d9720, 0xc00fb52c60}, 0xc00fe126e0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc00fbb4d70 sp=0xc00fbb4c30 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*recordSet).Next(0xc00fe12640, {0x40d68d0?, 0xc010546960?}, 0xc00fe126e0)
   > 	/go/src/github.com/pingcap/tidb/executor/adapter.go:149 +0xbf fp=0xc00fbb4e00 sp=0xc00fbb4d70 pc=0x2fa45ff
   > github.com/pingcap/tidb/session.(*execStmtResult).Next(0xc010546930?, {0x40d68d0?, 0xc010546960?}, 0xc00fdae000?)
   > 	<autogenerated>:1 +0x34 fp=0xc00fbb4e30 sp=0xc00fbb4e00 pc=0x31b8c94
   > github.com/pingcap/tidb/server.(*tidbResultSet).Next(0x60384e0?, {0x40d68d0?, 0xc010546960?}, 0x40ee040?)
   > 	/go/src/github.com/pingcap/tidb/server/driver_tidb.go:317 +0x2b fp=0xc00fbb4e60 sp=0xc00fbb4e30 pc=0x323ac6b
   > github.com/pingcap/tidb/server.(*clientConn).writeChunks(0xc0107803c0, {0x40d68d0, 0xc010546960}, {0x40dff58, 0xc00fe12690}, 0x0, 0xfbb?)
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:2185 +0x15e fp=0xc00fbb4f20 sp=0xc00fbb4e60 pc=0x3231d7e
   > github.com/pingcap/tidb/server.(*clientConn).writeResultset(0xc0107803c0, {0x40d68d0, 0xc010546960}, {0x40dff58, 0xc00fe12690}, 0xc0?, 0x2, 0xc0057d1088?)
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:2136 +0x23e fp=0xc00fbb4fd0 sp=0xc00fbb4f20 pc=0x323157e
   > github.com/pingcap/tidb/server.(*clientConn).handleStmt(0xc0107803c0, {0x40d6828, 0xc00fdae6c0}, {0x40e9b80, 0xc00fd69560}, {0x606b430, 0x0, 0x0}, 0x1)
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:2014 +0x3c8 fp=0xc00fbb5098 sp=0xc00fbb4fd0 pc=0x32302c8
   > github.com/pingcap/tidb/server.(*clientConn).handleQuery(0xc0107803c0, {0x40d6828, 0xc00fdae6c0}, {0xc00fb44001, 0x44c})
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:1850 +0x774 fp=0xc00fbb5260 sp=0xc00fbb5098 pc=0x322ea14
   > github.com/pingcap/tidb/server.(*clientConn).dispatch(0xc0107803c0, {0x40d68d0?, 0xc0104de0c0?}, {0xc00fb44000, 0x44d, 0x44d})
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:1345 +0x1025 fp=0xc00fbb5650 sp=0xc00fbb5260 pc=0x322a305
   > github.com/pingcap/tidb/server.(*clientConn).Run(0xc0107803c0, {0x40d68d0, 0xc0104de0c0})
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:1095 +0x253 fp=0xc00fbb5c58 sp=0xc00fbb5650 pc=0x3226c53
   > github.com/pingcap/tidb/server.(*Server).onConn(0xc000984270, 0xc0107803c0)
   > 	/go/src/github.com/pingcap/tidb/server/server.go:551 +0x6c5 fp=0xc00fbb5fc0 sp=0xc00fbb5c58 pc=0x3259da5
   > github.com/pingcap/tidb/server.(*Server).startNetworkListener.func2()
   > 	/go/src/github.com/pingcap/tidb/server/server.go:448 +0x2a fp=0xc00fbb5fe0 sp=0xc00fbb5fc0 pc=0x3258c2a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fbb5fe8 sp=0xc00fbb5fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/server.(*Server).startNetworkListener
   > 	/go/src/github.com/pingcap/tidb/server/server.go:448 +0x5ca
   > goroutine 776 [select]:
   > runtime.gopark(0xc00fc02f28?, 0x2?, 0x0?, 0x0?, 0xc00fc02eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fc02d58 sp=0xc00fc02d38 pc=0x13c9516
   > runtime.selectgo(0xc00fc02f28, 0xc00fc02ee8, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fc02e98 sp=0xc00fc02d58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc000581800, {0x4134ba0, 0xc0113a58c0}, 0xc00ff766f0, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc00fc02fa8 sp=0xc00fc02e98 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc00fc02fe0 sp=0xc00fc02fa8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fc02fe8 sp=0xc00fc02fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 690 [select]:
   > runtime.gopark(0xc00faa3768?, 0x4?, 0x3?, 0x30?, 0xc00faa36e8?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00faa3548 sp=0xc00faa3528 pc=0x13c9516
   > runtime.selectgo(0xc00faa3768, 0xc00faa36e0, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00faa3688 sp=0xc00faa3548 pc=0x13d9bdc
   > github.com/pingcap/tidb/util/topsql/reporter.(*RemoteTopSQLReporter).collectWorker(0xc0000ca700)
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:175 +0x18e fp=0xc00faa37c8 sp=0xc00faa3688 pc=0x25a162e
   > github.com/pingcap/tidb/util/topsql/reporter.(*RemoteTopSQLReporter).Start.func1()
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:110 +0x26 fp=0xc00faa37e0 sp=0xc00faa37c8 pc=0x25a11c6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00faa37e8 sp=0xc00faa37e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/util/topsql/reporter.(*RemoteTopSQLReporter).Start
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:110 +0x6a
   > goroutine 660 [select]:
   > runtime.gopark(0xc00fa95f18?, 0x7?, 0x45?, 0x0?, 0xc00fa95afa?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fa95958 sp=0xc00fa95938 pc=0x13c9516
   > runtime.selectgo(0xc00fa95f18, 0xc00fa95aec, 0x7f5878697400?, 0x0, 0x7f58787fffff?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fa95a98 sp=0xc00fa95958 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).updateStatsWorker(0xc010bc6640, {0x4134ba0?, 0xc0113a4480?}, {0x40e2a10, 0xc010658540})
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1429 +0x27c fp=0xc00fa95fa8 sp=0xc00fa95a98 pc=0x2798fdc
   > github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop.func3()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1304 +0x36 fp=0xc00fa95fe0 sp=0xc00fa95fa8 pc=0x27974b6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fa95fe8 sp=0xc00fa95fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1304 +0x29a
   > goroutine 669 [select, locked to thread]:
   > runtime.gopark(0xc00ffbe7a8?, 0x2?, 0x16?, 0x95?, 0xc00ffbe7a4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00ffbe618 sp=0xc00ffbe5f8 pc=0x13c9516
   > runtime.selectgo(0xc00ffbe7a8, 0xc00ffbe7a0, 0x0?, 0x0, 0xc010c46600?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00ffbe758 sp=0xc00ffbe618 pc=0x13d9bdc
   > runtime.ensureSigM.func1()
   > 	/usr/local/go/src/runtime/signal_unix.go:995 +0x1b0 fp=0xc00ffbe7e0 sp=0xc00ffbe758 pc=0x13de070
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00ffbe7e8 sp=0xc00ffbe7e0 pc=0x13fc6e1
   > created by runtime.ensureSigM
   > 	/usr/local/go/src/runtime/signal_unix.go:978 +0xbd
   > goroutine 564 [select]:
   > runtime.gopark(0xc000d57f90?, 0x2?, 0x1?, 0x0?, 0xc000d57f6c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000d57df0 sp=0xc000d57dd0 pc=0x13c9516
   > runtime.selectgo(0xc000d57f90, 0xc000d57f68, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000d57f30 sp=0xc000d57df0 pc=0x13d9bdc
   > github.com/pingcap/tidb/ddl.(*delRange).startEmulator(0xc010d19e60)
   > 	/go/src/github.com/pingcap/tidb/ddl/delete_range.go:140 +0x125 fp=0xc000d57fc8 sp=0xc000d57f30 pc=0x271fb25
   > github.com/pingcap/tidb/ddl.(*delRange).start.func1()
   > 	/go/src/github.com/pingcap/tidb/ddl/delete_range.go:122 +0x26 fp=0xc000d57fe0 sp=0xc000d57fc8 pc=0x271f8e6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000d57fe8 sp=0xc000d57fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/ddl.(*delRange).start
   > 	/go/src/github.com/pingcap/tidb/ddl/delete_range.go:122 +0x6d
   > goroutine 706 [select]:
   > runtime.gopark(0xc0057f1d68?, 0x2?, 0x48?, 0x59?, 0xc0057f1d54?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0057f1be0 sp=0xc0057f1bc0 pc=0x13c9516
   > runtime.selectgo(0xc0057f1d68, 0xc0057f1d50, 0xc0113ac040?, 0x0, 0xc0057f1d88?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0057f1d20 sp=0xc0057f1be0 pc=0x13d9bdc
   > github.com/soheilhy/cmux.muxListener.Accept(...)
   > 	/go/pkg/mod/github.com/soheilhy/cmux@v0.1.5/cmux.go:262
   > github.com/soheilhy/cmux.(*muxListener).Accept(0x40ba820?)
   > 	<autogenerated>:1 +0x7e fp=0xc0057f1d98 sp=0xc0057f1d20 pc=0x31ece5e
   > google.golang.org/grpc.(*Server).Serve(0xc000562540, {0x40d5e60, 0xc0006adf40})
   > 	/go/pkg/mod/google.golang.org/grpc@v1.44.0/server.go:779 +0x362 fp=0xc0057f1eb0 sp=0xc0057f1d98 pc=0x199d262
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer.func1()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:464 +0x37 fp=0xc0057f1f90 sp=0xc0057f1eb0 pc=0x3250357
   > github.com/pingcap/tidb/util.WithRecovery(0x40d6860?, 0xc000d8dce0?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc0057f1fc0 sp=0xc0057f1f90 pc=0x208e513
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer.func5()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:463 +0x28 fp=0xc0057f1fe0 sp=0xc0057f1fc0 pc=0x32502e8
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0057f1fe8 sp=0xc0057f1fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:463 +0x438
   > goroutine 670 [syscall]:
   > runtime.notetsleepg(0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/lock_futex.go:236 +0x34 fp=0xc00faa6fa0 sp=0xc00faa6f68 pc=0x1398cd4
   > os/signal.signal_recv()
   > 	/usr/local/go/src/runtime/sigqueue.go:152 +0x2f fp=0xc00faa6fc0 sp=0xc00faa6fa0 pc=0x13f86cf
   > os/signal.loop()
   > 	/usr/local/go/src/os/signal/signal_unix.go:23 +0x19 fp=0xc00faa6fe0 sp=0xc00faa6fc0 pc=0x2ecc1f9
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00faa6fe8 sp=0xc00faa6fe0 pc=0x13fc6e1
   > created by os/signal.Notify.func1.1
   > 	/usr/local/go/src/os/signal/signal.go:151 +0x2a
   > goroutine 778 [select]:
   > runtime.gopark(0xc00ffc4f28?, 0x2?, 0x0?, 0x0?, 0xc00ffc4eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00ffc4d58 sp=0xc00ffc4d38 pc=0x13c9516
   > runtime.selectgo(0xc00ffc4f28, 0xc00ffc4ee8, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00ffc4e98 sp=0xc00ffc4d58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc000581980, {0x4134ba0, 0xc0113a58c0}, 0xc00ff766f0, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc00ffc4fa8 sp=0xc00ffc4e98 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc00ffc4fe0 sp=0xc00ffc4fa8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00ffc4fe8 sp=0xc00ffc4fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 748 [select]:
   > runtime.gopark(0xc00ffbef78?, 0x2?, 0xe0?, 0xa7?, 0xc00ffbeeec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00ffbed58 sp=0xc00ffbed38 pc=0x13c9516
   > runtime.selectgo(0xc00ffbef78, 0xc00ffbeee8, 0x3b67af1?, 0x0, 0xc01033e7f8?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00ffbee98 sp=0xc00ffbed58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc00ff7e800, {0x40d68d0?, 0xc010546960?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc00ffbefb8 sp=0xc00ffbee98 pc=0x30ecdf4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc00ffbefe0 sp=0xc00ffbefb8 pc=0x30ec08e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00ffbefe8 sp=0xc00ffbefe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 664 [select]:
   > runtime.gopark(0xc000bdbd48?, 0x3?, 0x3?, 0x0?, 0xc000bdbcd2?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000bdbb50 sp=0xc000bdbb30 pc=0x13c9516
   > runtime.selectgo(0xc000bdbd48, 0xc000bdbccc, 0x0?, 0x0, 0xc0004a74d8?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000bdbc90 sp=0xc000bdbb50 pc=0x13d9bdc
   > github.com/pingcap/tidb/statistics/handle.(*Handle).drainColTask(0xc000b0fd40, 0xc010b1d500)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:294 +0xe5 fp=0xc000bdbd88 sp=0xc000bdbc90 pc=0x2612705
   > github.com/pingcap/tidb/statistics/handle.(*Handle).HandleOneTask(0xc000b0fd40, 0x2?, 0xc000bdbf40, {0x7f5879963fd8, 0xc0113a4b40}, 0xc010f034a0?)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:181 +0xc5 fp=0xc000bdbee8 sp=0xc000bdbd88 pc=0x2610fe5
   > github.com/pingcap/tidb/statistics/handle.(*Handle).SubLoadWorker(0xc000b0fd40, {0x4134ba0?, 0xc0113a4b40}, 0x249c8a6?, 0xc01026c240?)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:154 +0x11b fp=0xc000bdbfa8 sp=0xc000bdbee8 pc=0x2610b3b
   > github.com/pingcap/tidb/domain.(*Domain).StartLoadStatsSubWorkers.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1318 +0x36 fp=0xc000bdbfe0 sp=0xc000bdbfa8 pc=0x27977b6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000bdbfe8 sp=0xc000bdbfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).StartLoadStatsSubWorkers
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1318 +0x172
   > goroutine 594 [select]:
   > runtime.gopark(0xc0006b5e90?, 0x3?, 0x4?, 0x30?, 0xc0006b5e02?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0006b5c70 sp=0xc0006b5c50 pc=0x13c9516
   > runtime.selectgo(0xc0006b5e90, 0xc0006b5dfc, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0006b5db0 sp=0xc0006b5c70 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).globalBindHandleWorkerLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1114 +0x16f fp=0xc0006b5fe0 sp=0xc0006b5db0 pc=0x279564f
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0006b5fe8 sp=0xc0006b5fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).globalBindHandleWorkerLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1101 +0xad
   > goroutine 777 [select]:
   > runtime.gopark(0xc00fc00728?, 0x2?, 0x0?, 0x0?, 0xc00fc006ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fc00558 sp=0xc00fc00538 pc=0x13c9516
   > runtime.selectgo(0xc00fc00728, 0xc00fc006e8, 0x3b67af1?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fc00698 sp=0xc00fc00558 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc0005818c0, {0x4134ba0, 0xc0113a58c0}, 0xc00ff766f0, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc00fc007a8 sp=0xc00fc00698 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc00fc007e0 sp=0xc00fc007a8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fc007e8 sp=0xc00fc007e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 661 [select]:
   > runtime.gopark(0xc000ddcf78?, 0x2?, 0x0?, 0x30?, 0xc000ddcf4c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000ddcdd0 sp=0xc000ddcdb0 pc=0x13c9516
   > runtime.selectgo(0xc000ddcf78, 0xc000ddcf48, 0x30ecc00?, 0x0, 0xc000ddce58?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000ddcf10 sp=0xc000ddcdd0 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).autoAnalyzeWorker(0xc010bc6640, {0x40e2a10, 0xc010658540})
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1487 +0x105 fp=0xc000ddcfb8 sp=0xc000ddcf10 pc=0x2799f45
   > github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop.func4()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1307 +0x2e fp=0xc000ddcfe0 sp=0xc000ddcfb8 pc=0x279744e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000ddcfe8 sp=0xc000ddcfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1307 +0x31a
   > goroutine 573 [select]:
   > runtime.gopark(0xc00010a678?, 0x3?, 0x4?, 0x30?, 0xc00010a5f2?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00010a478 sp=0xc00010a458 pc=0x13c9516
   > runtime.selectgo(0xc00010a678, 0xc00010a5ec, 0x139a501?, 0x0, 0x2758626?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00010a5b8 sp=0xc00010a478 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).topologySyncerKeeper(0xc010bc6640)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:561 +0x165 fp=0xc00010a7c8 sp=0xc00010a5b8 pc=0x2790645
   > github.com/pingcap/tidb/domain.(*Domain).Init.func14()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:872 +0x26 fp=0xc00010a7e0 sp=0xc00010a7c8 pc=0x2793866
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00010a7e8 sp=0xc00010a7e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:872 +0xfbd
   > goroutine 569 [select]:
   > runtime.gopark(0xc00fa37f50?, 0x4?, 0x4?, 0x30?, 0xc00fa37d00?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fa37b78 sp=0xc00fa37b58 pc=0x13c9516
   > runtime.selectgo(0xc00fa37f50, 0xc00fa37cf8, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fa37cb8 sp=0xc00fa37b78 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).loadSchemaInLoop(0xc010bc6640, {0x40d6828, 0xc010ba9200}, 0x0?)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:593 +0x1aa fp=0xc00fa37fb0 sp=0xc00fa37cb8 pc=0x2790e2a
   > github.com/pingcap/tidb/domain.(*Domain).Init.func10()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:864 +0x32 fp=0xc00fa37fe0 sp=0xc00fa37fb0 pc=0x27939f2
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fa37fe8 sp=0xc00fa37fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:864 +0xe6b
   > goroutine 572 [select]:
   > runtime.gopark(0xc000104eb0?, 0x2?, 0x20?, 0x2f?, 0xc000104e7c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000d5cce8 sp=0xc000d5ccc8 pc=0x13c9516
   > runtime.selectgo(0xc000d5ceb0, 0xc000104e78, 0x88?, 0x0, 0x90?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000d5ce28 sp=0xc000d5cce8 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).globalConfigSyncerKeeper(0xc010bc6640)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:538 +0xf5 fp=0xc000d5cfc8 sp=0xc000d5ce28 pc=0x2790155
   > github.com/pingcap/tidb/domain.(*Domain).Init.func13()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:869 +0x26 fp=0xc000d5cfe0 sp=0xc000d5cfc8 pc=0x27938c6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000d5cfe8 sp=0xc000d5cfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:869 +0xf5c
   > goroutine 571 [select]:
   > runtime.gopark(0xc0001056f8?, 0x3?, 0x4?, 0x30?, 0xc000105682?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000105508 sp=0xc0001054e8 pc=0x13c9516
   > runtime.selectgo(0xc0001056f8, 0xc00010567c, 0xc01070dd40?, 0x0, 0x7f5879496ad8?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000105648 sp=0xc000105508 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).infoSyncerKeeper(0xc010bc6640)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:515 +0x165 fp=0xc0001057c8 sp=0xc000105648 pc=0x278fb85
   > github.com/pingcap/tidb/domain.(*Domain).Init.func12()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:868 +0x26 fp=0xc0001057e0 sp=0xc0001057c8 pc=0x2793926
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0001057e8 sp=0xc0001057e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:868 +0xf15
   > goroutine 570 [select]:
   > runtime.gopark(0xc000104778?, 0x3?, 0x4?, 0x30?, 0xc000104712?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000104560 sp=0xc000104540 pc=0x13c9516
   > runtime.selectgo(0xc000104778, 0xc00010470c, 0x2?, 0x0, 0xc010c5a000?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0001046a0 sp=0xc000104560 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).topNSlowQueryLoop(0xc010bc6640)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:483 +0x194 fp=0xc0001047c8 sp=0xc0001046a0 pc=0x278f654
   > github.com/pingcap/tidb/domain.(*Domain).Init.func11()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:867 +0x26 fp=0xc0001047e0 sp=0xc0001047c8 pc=0x2793986
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0001047e8 sp=0xc0001047e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:867 +0xed2
   > goroutine 780 [select]:
   > runtime.gopark(0xc00ffbf728?, 0x2?, 0xa0?, 0x1b?, 0xc00ffbf6ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00ffbf558 sp=0xc00ffbf538 pc=0x13c9516
   > runtime.selectgo(0xc00ffbf728, 0xc00ffbf6e8, 0x3b67af1?, 0x0, 0x139805d?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00ffbf698 sp=0xc00ffbf558 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc000581b00, {0x4134ba0, 0xc0113a58c0}, 0xc00ff766f0, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc00ffbf7a8 sp=0xc00ffbf698 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc00ffbf7e0 sp=0xc00ffbf7a8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00ffbf7e8 sp=0xc00ffbf7e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 779 [select]:
   > runtime.gopark(0xc00ffc5f28?, 0x2?, 0xc7?, 0x95?, 0xc00ffc5eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00ffc5d58 sp=0xc00ffc5d38 pc=0x13c9516
   > runtime.selectgo(0xc00ffc5f28, 0xc00ffc5ee8, 0xc00ffc5ed8?, 0x0, 0xc00ffed808?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00ffc5e98 sp=0xc00ffc5d58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc000581a40, {0x4134ba0, 0xc0113a58c0}, 0xc00ff766f0, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc00ffc5fa8 sp=0xc00ffc5e98 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc00ffc5fe0 sp=0xc00ffc5fa8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00ffc5fe8 sp=0xc00ffc5fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 568 [select]:
   > runtime.gopark(0xc00fde5de8?, 0x2?, 0x4?, 0x30?, 0xc00fde5d4c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fde5bd0 sp=0xc00fde5bb0 pc=0x13c9516
   > runtime.selectgo(0xc00fde5de8, 0xc00fde5d48, 0xc010de1680?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fde5d10 sp=0xc00fde5bd0 pc=0x13d9bdc
   > github.com/pingcap/tidb/ddl.(*ddl).PollTiFlashRoutine(0xc010bbc700)
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl_tiflash_api.go:577 +0x273 fp=0xc00fde5f98 sp=0xc00fde5d10 pc=0x27159b3
   > github.com/pingcap/tidb/ddl.(*ddl).PollTiFlashRoutine-fm()
   > 	<autogenerated>:1 +0x26 fp=0xc00fde5fb0 sp=0xc00fde5f98 pc=0x2768c06
   > github.com/pingcap/tidb/util.(*WaitGroupWrapper).Run.func1()
   > 	/go/src/github.com/pingcap/tidb/util/wait_group_wrapper.go:33 +0x5a fp=0xc00fde5fe0 sp=0xc00fde5fb0 pc=0x209361a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fde5fe8 sp=0xc00fde5fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/util.(*WaitGroupWrapper).Run
   > 	/go/src/github.com/pingcap/tidb/util/wait_group_wrapper.go:31 +0x85
   > goroutine 666 [select]:
   > runtime.gopark(0xc000bdcd48?, 0x3?, 0x3?, 0x0?, 0xc000bdccd2?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000bdcb50 sp=0xc000bdcb30 pc=0x13c9516
   > runtime.selectgo(0xc000bdcd48, 0xc000bdcccc, 0x0?, 0x0, 0xc00fc01cc8?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000bdcc90 sp=0xc000bdcb50 pc=0x13d9bdc
   > github.com/pingcap/tidb/statistics/handle.(*Handle).drainColTask(0xc000b0fd40, 0xc010b1d500)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:294 +0xe5 fp=0xc000bdcd88 sp=0xc000bdcc90 pc=0x2612705
   > github.com/pingcap/tidb/statistics/handle.(*Handle).HandleOneTask(0xc000b0fd40, 0x0?, 0xc000bdcf40, {0x7f5879963fd8, 0xc0113a4fc0}, 0xc010382210?)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:181 +0xc5 fp=0xc000bdcee8 sp=0xc000bdcd88 pc=0x2610fe5
   > github.com/pingcap/tidb/statistics/handle.(*Handle).SubLoadWorker(0xc000b0fd40, {0x4134ba0?, 0xc0113a4fc0}, 0xc0006a4210?, 0xc00fc01fb8?)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:154 +0x11b fp=0xc000bdcfa8 sp=0xc000bdcee8 pc=0x2610b3b
   > github.com/pingcap/tidb/domain.(*Domain).StartLoadStatsSubWorkers.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1318 +0x36 fp=0xc000bdcfe0 sp=0xc000bdcfa8 pc=0x27977b6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000bdcfe8 sp=0xc000bdcfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).StartLoadStatsSubWorkers
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1318 +0x172
   > goroutine 566 [select]:
   > runtime.gopark(0xc00fa33f58?, 0x4?, 0xab?, 0x42?, 0xc00fa33da8?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fa33bf8 sp=0xc00fa33bd8 pc=0x13c9516
   > runtime.selectgo(0xc00fa33f58, 0xc00fa33da0, 0xc000d5ae38?, 0x0, 0x1?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fa33d38 sp=0xc00fa33bf8 pc=0x13d9bdc
   > github.com/pingcap/tidb/ddl.(*worker).start(0xc010d05ec0, 0xc010bb1a00)
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl_worker.go:184 +0x318 fp=0xc00fa33fc0 sp=0xc00fa33d38 pc=0x27168b8
   > github.com/pingcap/tidb/ddl.(*ddl).Start.func3()
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:399 +0x2a fp=0xc00fa33fe0 sp=0xc00fa33fc0 pc=0x26d426a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fa33fe8 sp=0xc00fa33fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/ddl.(*ddl).Start
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:399 +0x58e
   > goroutine 565 [select]:
   > runtime.gopark(0xc00f9fbf58?, 0x4?, 0xab?, 0x42?, 0xc00f9fbda8?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00f9fbbf8 sp=0xc00f9fbbd8 pc=0x13c9516
   > runtime.selectgo(0xc00f9fbf58, 0xc00f9fbda0, 0xc0004dce38?, 0x0, 0x1?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00f9fbd38 sp=0xc00f9fbbf8 pc=0x13d9bdc
   > github.com/pingcap/tidb/ddl.(*worker).start(0xc010d05e00, 0xc010bb1a00)
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl_worker.go:184 +0x318 fp=0xc00f9fbfc0 sp=0xc00f9fbd38 pc=0x27168b8
   > github.com/pingcap/tidb/ddl.(*ddl).Start.func3()
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:399 +0x2a fp=0xc00f9fbfe0 sp=0xc00f9fbfc0 pc=0x26d426a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00f9fbfe8 sp=0xc00f9fbfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/ddl.(*ddl).Start
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:399 +0x58e
   > goroutine 691 [select]:
   > runtime.gopark(0xc00faa4f90?, 0x2?, 0x0?, 0x92?, 0xc00faa4f3c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0057f0d90 sp=0xc0057f0d70 pc=0x13c9516
   > runtime.selectgo(0xc0057f0f90, 0xc00faa4f38, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0057f0ed0 sp=0xc0057f0d90 pc=0x13d9bdc
   > github.com/pingcap/tidb/util/topsql/reporter.(*RemoteTopSQLReporter).reportWorker(0xc0000ca700)
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:261 +0xfd fp=0xc0057f0fc8 sp=0xc0057f0ed0 pc=0x25a231d
   > github.com/pingcap/tidb/util/topsql/reporter.(*RemoteTopSQLReporter).Start.func2()
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:111 +0x26 fp=0xc0057f0fe0 sp=0xc0057f0fc8 pc=0x25a1166
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0057f0fe8 sp=0xc0057f0fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/util/topsql/reporter.(*RemoteTopSQLReporter).Start
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:111 +0xaa
   > goroutine 667 [select]:
   > runtime.gopark(0xc0004a9fa8?, 0x2?, 0x0?, 0x30?, 0xc0004a9f7c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004a9e00 sp=0xc0004a9de0 pc=0x13c9516
   > runtime.selectgo(0xc0004a9fa8, 0xc0004a9f78, 0xc010469040?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0004a9f40 sp=0xc0004a9e00 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).PlanReplayerLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1236 +0xf6 fp=0xc0004a9fe0 sp=0xc0004a9f40 pc=0x2796e36
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004a9fe8 sp=0xc0004a9fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).PlanReplayerLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1227 +0x6c
   > goroutine 665 [select]:
   > runtime.gopark(0xc000bdad48?, 0x3?, 0x3?, 0x0?, 0xc000bdacd2?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000bdab50 sp=0xc000bdab30 pc=0x13c9516
   > runtime.selectgo(0xc000bdad48, 0xc000bdaccc, 0x1?, 0x0, 0x313fb85?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000bdac90 sp=0xc000bdab50 pc=0x13d9bdc
   > github.com/pingcap/tidb/statistics/handle.(*Handle).drainColTask(0xc000b0fd40, 0xc010b1d500)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:294 +0xe5 fp=0xc000bdad88 sp=0xc000bdac90 pc=0x2612705
   > github.com/pingcap/tidb/statistics/handle.(*Handle).HandleOneTask(0xc000b0fd40, 0xc010469b00?, 0xc000bdaf40, {0x7f5879963fd8, 0xc0113a4d80}, 0xc01044dde0?)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:181 +0xc5 fp=0xc000bdaee8 sp=0xc000bdad88 pc=0x2610fe5
   > github.com/pingcap/tidb/statistics/handle.(*Handle).SubLoadWorker(0xc000b0fd40, {0x4134ba0?, 0xc0113a4d80}, 0x40d6860?, 0xc000120008?)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:154 +0x11b fp=0xc000bdafa8 sp=0xc000bdaee8 pc=0x2610b3b
   > github.com/pingcap/tidb/domain.(*Domain).StartLoadStatsSubWorkers.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1318 +0x36 fp=0xc000bdafe0 sp=0xc000bdafa8 pc=0x27977b6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000bdafe8 sp=0xc000bdafe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).StartLoadStatsSubWorkers
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1318 +0x172
   > goroutine 694 [IO wait]:
   > runtime.gopark(0xc000578a90?, 0xc000bb9878?, 0x0?, 0x0?, 0xc000bb98c8?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000bb9858 sp=0xc000bb9838 pc=0x13c9516
   > runtime.netpollblock(0xc000578a90?, 0xb?, 0x0?)
   > 	/usr/local/go/src/runtime/netpoll.go:526 +0xf7 fp=0xc000bb9890 sp=0xc000bb9858 pc=0x13c18f7
   > internal/poll.runtime_pollWait(0x7f5879c22d90, 0x72)
   > 	/usr/local/go/src/runtime/netpoll.go:305 +0x89 fp=0xc000bb98b0 sp=0xc000bb9890 pc=0x13f5d09
   > internal/poll.(*pollDesc).wait(0xc010227980?, 0xd0?, 0x0)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:84 +0x32 fp=0xc000bb98d8 sp=0xc000bb98b0 pc=0x1473092
   > internal/poll.(*pollDesc).waitRead(...)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:89
   > internal/poll.(*FD).Accept(0xc010227980)
   > 	/usr/local/go/src/internal/poll/fd_unix.go:614 +0x234 fp=0xc000bb9970 sp=0xc000bb98d8 pc=0x1478494
   > net.(*netFD).accept(0xc010227980)
   > 	/usr/local/go/src/net/fd_unix.go:172 +0x35 fp=0xc000bb9a28 sp=0xc000bb9970 pc=0x1597315
   > net.(*TCPListener).accept(0xc010fc91d0)
   > 	/usr/local/go/src/net/tcpsock_posix.go:142 +0x28 fp=0xc000bb9a58 sp=0xc000bb9a28 pc=0x15b3288
   > net.(*TCPListener).Accept(0xc010fc91d0)
   > 	/usr/local/go/src/net/tcpsock.go:288 +0x3d fp=0xc000bb9a88 sp=0xc000bb9a58 pc=0x15b22fd
   > github.com/soheilhy/cmux.(*cMux).Serve(0xc00fd39680)
   > 	/go/pkg/mod/github.com/soheilhy/cmux@v0.1.5/cmux.go:170 +0xa9 fp=0xc000bb9b18 sp=0xc000bb9a88 pc=0x31eb249
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer(0xc000984270, 0xc00068b080)
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:473 +0x4f7 fp=0xc000bb9c90 sp=0xc000bb9b18 pc=0x324fe57
   > github.com/pingcap/tidb/server.(*Server).startHTTPServer(0xc000984270)
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:446 +0x1610 fp=0xc000bb9fc8 sp=0xc000bb9c90 pc=0x324f250
   > github.com/pingcap/tidb/server.(*Server).startStatusHTTP.func1()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:62 +0x26 fp=0xc000bb9fe0 sp=0xc000bb9fc8 pc=0x324b8c6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000bb9fe8 sp=0xc000bb9fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/server.(*Server).startStatusHTTP
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:62 +0x56
   > goroutine 693 [select]:
   > runtime.gopark(0xc00fc03f90?, 0x2?, 0x18?, 0x92?, 0xc00fc03f6c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fc03df0 sp=0xc00fc03dd0 pc=0x13c9516
   > runtime.selectgo(0xc00fc03f90, 0xc00fc03f68, 0x3b?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fc03f30 sp=0xc00fc03df0 pc=0x13d9bdc
   > github.com/pingcap/tidb/util/topsql/stmtstats.(*aggregator).run(0xc0001cf4d0)
   > 	/go/src/github.com/pingcap/tidb/util/topsql/stmtstats/aggregator.go:67 +0xff fp=0xc00fc03fc8 sp=0xc00fc03f30 pc=0x1fbf99f
   > github.com/pingcap/tidb/util/topsql/stmtstats.(*aggregator).start.func1()
   > 	/go/src/github.com/pingcap/tidb/util/topsql/stmtstats/aggregator.go:56 +0x26 fp=0xc00fc03fe0 sp=0xc00fc03fc8 pc=0x1fbf866
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fc03fe8 sp=0xc00fc03fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/util/topsql/stmtstats.(*aggregator).start
   > 	/go/src/github.com/pingcap/tidb/util/topsql/stmtstats/aggregator.go:56 +0xd6
   > goroutine 692 [select]:
   > runtime.gopark(0xc00faa4748?, 0x3?, 0x3?, 0x30?, 0xc00faa46e2?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00faa4550 sp=0xc00faa4530 pc=0x13c9516
   > runtime.selectgo(0xc00faa4748, 0xc00faa46dc, 0x0?, 0x0, 0x3?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00faa4690 sp=0xc00faa4550 pc=0x13d9bdc
   > github.com/pingcap/tidb/util/topsql/reporter.(*SingleTargetDataSink).run(0xc00014d1d0)
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/single_target.go:116 +0x12f fp=0xc00faa4790 sp=0xc00faa4690 pc=0x25a34af
   > github.com/pingcap/tidb/util/topsql/reporter.(*SingleTargetDataSink).recoverRun(0xc00014d1d0)
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/single_target.go:98 +0x65 fp=0xc00faa47c8 sp=0xc00faa4790 pc=0x25a30e5
   > github.com/pingcap/tidb/util/topsql/reporter.(*SingleTargetDataSink).Start.func1()
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/single_target.go:82 +0x26 fp=0xc00faa47e0 sp=0xc00faa47c8 pc=0x25a3046
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00faa47e8 sp=0xc00faa47e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/util/topsql/reporter.(*SingleTargetDataSink).Start
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/single_target.go:82 +0x2ab
   > goroutine 673 [select]:
   > runtime.gopark(0xc00faa3f80?, 0x3?, 0x3?, 0x30?, 0xc00faa3f42?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00faa3dc8 sp=0xc00faa3da8 pc=0x13c9516
   > runtime.selectgo(0xc00faa3f80, 0xc00faa3f3c, 0x2757893?, 0x0, 0xc0101910e0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00faa3f08 sp=0xc00faa3dc8 pc=0x13d9bdc
   > github.com/pingcap/tidb/util/topsql/collector.(*SQLCPUCollector).collectSQLCPULoop(0xc00014d180)
   > 	/go/src/github.com/pingcap/tidb/util/topsql/collector/cpu.go:121 +0x1a5 fp=0xc00faa3fc8 sp=0xc00faa3f08 pc=0x25974a5
   > github.com/pingcap/tidb/util/topsql/collector.(*SQLCPUCollector).Start.func1()
   > 	/go/src/github.com/pingcap/tidb/util/topsql/collector/cpu.go:83 +0x26 fp=0xc00faa3fe0 sp=0xc00faa3fc8 pc=0x25971c6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00faa3fe8 sp=0xc00faa3fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/util/topsql/collector.(*SQLCPUCollector).Start
   > 	/go/src/github.com/pingcap/tidb/util/topsql/collector/cpu.go:83 +0xca
   > goroutine 747 [chan receive]:
   > runtime.gopark(0xc01083f860?, 0xc010c30820?, 0x6d?, 0xcb?, 0xc000bbf2d0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000bbf228 sp=0xc000bbf208 pc=0x13c9516
   > runtime.chanrecv(0xc010c1e960, 0xc000bbf300, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000bbf2b8 sp=0xc000bbf228 pc=0x13934bb
   > runtime.chanrecv2(0xc010d8e800?, 0x40d68d0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc000bbf2e0 sp=0xc000bbf2b8 pc=0x1392ff8
   > github.com/pingcap/tidb/executor.(*HashAggExec).parallelExec(0xc010d8e800, {0x40d68d0?, 0xc010546960?}, 0xc00fdbaff0)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:888 +0x89 fp=0xc000bbf318 sp=0xc000bbf2e0 pc=0x2fbcf29
   > github.com/pingcap/tidb/executor.(*HashAggExec).Next(0x40d68d0?, {0x40d68d0?, 0xc010546960?}, 0x7f5879110f01?)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:768 +0x76 fp=0xc000bbf348 sp=0xc000bbf318 pc=0x2fbbeb6
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc010546960}, {0x40d9120, 0xc010d8e800}, 0xc00fdbaff0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc000bbf488 sp=0xc000bbf348 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*SortExec).fetchRowChunks(0xc00fb52a20, {0x40d68d0, 0xc010546960})
   > 	/go/src/github.com/pingcap/tidb/executor/sort.go:195 +0x596 fp=0xc000bbf5e8 sp=0xc000bbf488 pc=0x3135156
   > github.com/pingcap/tidb/executor.(*SortExec).Next(0xc00fb52a20, {0x40d68d0, 0xc010546960}, 0xc00fdbaf50)
   > 	/go/src/github.com/pingcap/tidb/executor/sort.go:113 +0x325 fp=0xc000bbf660 sp=0xc000bbf5e8 pc=0x31346c5
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc010546960}, {0x40d9c20, 0xc00fb52a20}, 0xc00fdbaf50)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc000bbf7a0 sp=0xc000bbf660 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*MaxOneRowExec).Next(0xc00fdc1570, {0x40d68d0, 0xc010546960}, 0xc00fdbaf50)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1518 +0xa8 fp=0xc000bbf7f0 sp=0xc000bbf7a0 pc=0x30413a8
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc010546960}, {0x40d94a0, 0xc00fdc1570}, 0xc00fdbaf50)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc000bbf930 sp=0xc000bbf7f0 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*SelectionExec).Next(0xc000985e10, {0x40d68d0, 0xc010546960}, 0xc00fb558b0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1394 +0xed fp=0xc000bbf9c0 sp=0xc000bbf930 pc=0x304012d
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc010546960}, {0x40d9960, 0xc000985e10}, 0xc00fb558b0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc000bbfb00 sp=0xc000bbf9c0 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*NestedLoopApplyExec).fetchAllInners(0xc000715dc0, {0x40d68d0, 0xc010546960})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:979 +0x346 fp=0xc000bbfbf8 sp=0xc000bbfb00 pc=0x30b2966
   > github.com/pingcap/tidb/executor.(*NestedLoopApplyExec).Next(0xc000715dc0, {0x40d68d0, 0xc010546960}, 0xc00fe12730)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:1032 +0x5b6 fp=0xc000bbfd58 sp=0xc000bbfbf8 pc=0x30b32b6
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc010546960}, {0x40d9560, 0xc000715dc0}, 0xc00fe12730)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc000bbfe98 sp=0xc000bbfd58 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*projectionInputFetcher).run(0xc00fb52ce0, {0x40d68d0, 0xc010546960})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:381 +0x2f0 fp=0xc000bbffb8 sp=0xc000bbfe98 pc=0x30ec890
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:272 +0x2e fp=0xc000bbffe0 sp=0xc000bbffb8 pc=0x30ec0ee
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000bbffe8 sp=0xc000bbffe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:272 +0x67e
   > goroutine 672 [chan receive]:
   > runtime.gopark(0xc0101ad020?, 0x0?, 0x28?, 0x0?, 0x1?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00ffc4660 sp=0xc00ffc4640 pc=0x13c9516
   > runtime.chanrecv(0xc000cee480, 0xc00ffc4780, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc00ffc46f0 sp=0xc00ffc4660 pc=0x13934bb
   > runtime.chanrecv1(0x2757893?, 0x40d6898?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc00ffc4718 sp=0xc00ffc46f0 pc=0x1392fb8
   > github.com/pingcap/tidb/util/signal.SetupSignalHandler.func2()
   > 	/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:54 +0x45 fp=0xc00ffc47e0 sp=0xc00ffc4718 pc=0x3433665
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00ffc47e8 sp=0xc00ffc47e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/util/signal.SetupSignalHandler
   > 	/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:53 +0x19f
   > goroutine 5283 [chan receive]:
   > runtime.gopark(0xc010daac88?, 0x13d1800?, 0x20?, 0x6c?, 0xc010c30ea0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010daac80 sp=0xc010daac60 pc=0x13c9516
   > runtime.chanrecv(0xc0119fe540, 0xc010daad68, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc010daad10 sp=0xc010daac80 pc=0x13934bb
   > runtime.chanrecv2(0xc01083bd00?, 0x40d68d0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc010daad38 sp=0xc010daad10 pc=0x1392ff8
   > github.com/pingcap/tidb/executor.(*UnionExec).Next(0xc01083bd00, {0x40d68d0, 0xc010546960}, 0xc0119c1b30)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1702 +0x85 fp=0xc010daada0 sp=0xc010daad38 pc=0x30425c5
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc010546960}, {0x40d9ea0, 0xc01083bd00}, 0xc0119c1b30)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc010daaee0 sp=0xc010daada0 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*HashAggExec).fetchChildData(0xc010d8e400, {0x40d68d0, 0xc010546960}, 0xc0113add80?)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:798 +0x1be fp=0xc010daafb0 sp=0xc010daaee0 pc=0x2fbc0fe
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func3()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:835 +0x32 fp=0xc010daafe0 sp=0xc010daafb0 pc=0x2fbce72
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010daafe8 sp=0xc010daafe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:835 +0xea
   > goroutine 5306 [select]:
   > runtime.gopark(0xc0106cb778?, 0x2?, 0xe0?, 0x26?, 0xc0106cb6ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0106cb558 sp=0xc0106cb538 pc=0x13c9516
   > runtime.selectgo(0xc0106cb778, 0xc0106cb6e8, 0x3b67af1?, 0x0, 0x30420ef?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0106cb698 sp=0xc0106cb558 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc00ff0da80, {0x40d68d0?, 0xc010546960?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc0106cb7b8 sp=0xc0106cb698 pc=0x30ecdf4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc0106cb7e0 sp=0xc0106cb7b8 pc=0x30ec08e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0106cb7e8 sp=0xc0106cb7e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 668 [select]:
   > runtime.gopark(0xc000bc7eb0?, 0x2?, 0x18?, 0x0?, 0xc000bc7e5c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000bc7cc8 sp=0xc000bc7ca8 pc=0x13c9516
   > runtime.selectgo(0xc000bc7eb0, 0xc000bc7e58, 0xc000984270?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000bc7e08 sp=0xc000bc7cc8 pc=0x13d9bdc
   > github.com/pingcap/tidb/util/expensivequery.(*Handle).Run(0xc010bc03f0)
   > 	/go/src/github.com/pingcap/tidb/util/expensivequery/expensivequery.go:61 +0x198 fp=0xc000bc7fc8 sp=0xc000bc7e08 pc=0x27866f8
   > main.createServer.func1()
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:695 +0x26 fp=0xc000bc7fe0 sp=0xc000bc7fc8 pc=0x343c186
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000bc7fe8 sp=0xc000bc7fe0 pc=0x13fc6e1
   > created by main.createServer
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:695 +0x44a
   > goroutine 595 [select]:
   > runtime.gopark(0xc0006b6728?, 0x2?, 0x4?, 0x30?, 0xc0006b66d4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0006b6548 sp=0xc0006b6528 pc=0x13c9516
   > runtime.selectgo(0xc0006b6728, 0xc0006b66d0, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0006b6688 sp=0xc0006b6548 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).handleEvolvePlanTasksLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1151 +0x107 fp=0xc0006b67e0 sp=0xc0006b6688 pc=0x2795ee7
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0006b67e8 sp=0xc0006b67e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).handleEvolvePlanTasksLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1144 +0xe5
   > goroutine 662 [select]:
   > runtime.gopark(0xc000521d48?, 0x3?, 0x3?, 0x0?, 0xc000521cd2?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000521b50 sp=0xc000521b30 pc=0x13c9516
   > runtime.selectgo(0xc000521d48, 0xc000521ccc, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000521c90 sp=0xc000521b50 pc=0x13d9bdc
   > github.com/pingcap/tidb/statistics/handle.(*Handle).drainColTask(0xc000b0fd40, 0xc010b1d500)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:294 +0xe5 fp=0xc000521d88 sp=0xc000521c90 pc=0x2612705
   > github.com/pingcap/tidb/statistics/handle.(*Handle).HandleOneTask(0xc000b0fd40, 0x0?, 0xc000521f40, {0x7f5879963fd8, 0xc0113a46c0}, 0x0?)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:181 +0xc5 fp=0xc000521ee8 sp=0xc000521d88 pc=0x2610fe5
   > github.com/pingcap/tidb/statistics/handle.(*Handle).SubLoadWorker(0xc000b0fd40, {0x4134ba0?, 0xc0113a46c0}, 0x40d68d0?, 0xc010382510?)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:154 +0x11b fp=0xc000521fa8 sp=0xc000521ee8 pc=0x2610b3b
   > github.com/pingcap/tidb/domain.(*Domain).StartLoadStatsSubWorkers.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1318 +0x36 fp=0xc000521fe0 sp=0xc000521fa8 pc=0x27977b6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000521fe8 sp=0xc000521fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).StartLoadStatsSubWorkers
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1318 +0x172
   > goroutine 5359 [semacquire]:
   > runtime.gopark(0x0?, 0x0?, 0xe0?, 0xc1?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01150d6b8 sp=0xc01150d698 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc0114a0198, 0x0?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc01150d720 sp=0xc01150d6b8 pc=0x13dae5e
   > sync.runtime_Semacquire(0x0?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc01150d750 sp=0xc01150d720 pc=0x13f7f65
   > sync.(*WaitGroup).Wait(0x0?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc01150d778 sp=0xc01150d750 pc=0x140b312
   > github.com/pingcap/tidb/executor.(*HashAggExec).waitAllWorkersAndCloseFinalOutputCh(0xc010d8e200, {0xc01150d7b8, 0x3, 0x0?})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:827 +0x35 fp=0xc01150d798 sp=0xc01150d778 pc=0x2fbc5b5
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func6()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:864 +0x5a fp=0xc01150d7e0 sp=0xc01150d798 pc=0x2fbcc1a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01150d7e8 sp=0xc01150d7e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:864 +0x54d
   > goroutine 583 [select]:
   > runtime.gopark(0xc000ddc718?, 0x3?, 0x0?, 0x30?, 0xc000ddc69a?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000ddc4d8 sp=0xc000ddc4b8 pc=0x13c9516
   > runtime.selectgo(0xc000ddc718, 0xc000ddc694, 0xc0002fd860?, 0x0, 0xc01136b200?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000ddc618 sp=0xc000ddc4d8 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).LoadPrivilegeLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:982 +0x145 fp=0xc000ddc7e0 sp=0xc000ddc618 pc=0x2794465
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000ddc7e8 sp=0xc000ddc7e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).LoadPrivilegeLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:973 +0x205
   > goroutine 775 [chan receive]:
   > runtime.gopark(0xc00fde9760?, 0x13d1800?, 0x20?, 0xc0?, 0xc00ffd1040?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fde9758 sp=0xc00fde9738 pc=0x13c9516
   > runtime.chanrecv(0xc011b55680, 0xc00fde9840, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc00fde97e8 sp=0xc00fde9758 pc=0x13934bb
   > runtime.chanrecv2(0xc01083bf00?, 0x40d68d0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc00fde9810 sp=0xc00fde97e8 pc=0x1392ff8
   > github.com/pingcap/tidb/executor.(*UnionExec).Next(0xc01083bf00, {0x40d68d0, 0xc010546960}, 0xc00fdba6e0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1702 +0x85 fp=0xc00fde9878 sp=0xc00fde9810 pc=0x30425c5
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc010546960}, {0x40d9ea0, 0xc01083bf00}, 0xc00fdba6e0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc00fde99b8 sp=0xc00fde9878 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*MaxOneRowExec).Next(0xc00fdc12d0, {0x40d68d0, 0xc010546960}, 0xc00fdba6e0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1518 +0xa8 fp=0xc00fde9a08 sp=0xc00fde99b8 pc=0x30413a8
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc010546960}, {0x40d94a0, 0xc00fdc12d0}, 0xc00fdba6e0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc00fde9b48 sp=0xc00fde9a08 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*NestedLoopApplyExec).fetchAllInners(0xc000715c00, {0x40d68d0, 0xc010546960})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:979 +0x346 fp=0xc00fde9c40 sp=0xc00fde9b48 pc=0x30b2966
   > github.com/pingcap/tidb/executor.(*NestedLoopApplyExec).Next(0xc000715c00, {0x40d68d0, 0xc010546960}, 0xc00fdba7d0)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:1032 +0x5b6 fp=0xc00fde9da0 sp=0xc00fde9c40 pc=0x30b32b6
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc010546960}, {0x40d9560, 0xc000715c00}, 0xc00fdba7d0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc00fde9ee0 sp=0xc00fde9da0 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*HashAggExec).fetchChildData(0xc010d8e800, {0x40d68d0, 0xc010546960}, 0xc00fc077b8?)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:798 +0x1be fp=0xc00fde9fb0 sp=0xc00fde9ee0 pc=0x2fbc0fe
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func3()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:835 +0x32 fp=0xc00fde9fe0 sp=0xc00fde9fb0 pc=0x2fbce72
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fde9fe8 sp=0xc00fde9fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:835 +0xea
   > goroutine 663 [select]:
   > runtime.gopark(0xc000520d48?, 0x3?, 0x3?, 0x0?, 0xc000520cd2?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000520b50 sp=0xc000520b30 pc=0x13c9516
   > runtime.selectgo(0xc000520d48, 0xc000520ccc, 0x1d655b6?, 0x0, 0xc000d13180?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000520c90 sp=0xc000520b50 pc=0x13d9bdc
   > github.com/pingcap/tidb/statistics/handle.(*Handle).drainColTask(0xc000b0fd40, 0xc010b1d500)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:294 +0xe5 fp=0xc000520d88 sp=0xc000520c90 pc=0x2612705
   > github.com/pingcap/tidb/statistics/handle.(*Handle).HandleOneTask(0xc000b0fd40, 0xc0110ff240?, 0xc000520f40, {0x7f5879963fd8, 0xc0113a4900}, 0xc010c52ca0?)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:181 +0xc5 fp=0xc000520ee8 sp=0xc000520d88 pc=0x2610fe5
   > github.com/pingcap/tidb/statistics/handle.(*Handle).SubLoadWorker(0xc000b0fd40, {0x4134ba0?, 0xc0113a4900}, 0x0?, 0xc00ffc1ec0?)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:154 +0x11b fp=0xc000520fa8 sp=0xc000520ee8 pc=0x2610b3b
   > github.com/pingcap/tidb/domain.(*Domain).StartLoadStatsSubWorkers.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1318 +0x36 fp=0xc000520fe0 sp=0xc000520fa8 pc=0x27977b6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000520fe8 sp=0xc000520fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).StartLoadStatsSubWorkers
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1318 +0x172
   > goroutine 707 [select]:
   > runtime.gopark(0xc0005a4d38?, 0x2?, 0x4?, 0x0?, 0xc0005a4d24?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0005a4bb0 sp=0xc0005a4b90 pc=0x13c9516
   > runtime.selectgo(0xc0005a4d38, 0xc0005a4d20, 0xc0005a4d01?, 0x0, 0x139a507?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0005a4cf0 sp=0xc0005a4bb0 pc=0x13d9bdc
   > github.com/soheilhy/cmux.muxListener.Accept(...)
   > 	/go/pkg/mod/github.com/soheilhy/cmux@v0.1.5/cmux.go:262
   > github.com/soheilhy/cmux.(*muxListener).Accept(0x59083d0?)
   > 	<autogenerated>:1 +0x7e fp=0xc0005a4d68 sp=0xc0005a4cf0 pc=0x31ece5e
   > net/http.(*onceCloseListener).Accept(0x40d6860?)
   > 	<autogenerated>:1 +0x2a fp=0xc0005a4d80 sp=0xc0005a4d68 pc=0x16ee8ea
   > net/http.(*Server).Serve(0xc010366f00, {0x40d5e60, 0xc0006adf20})
   > 	/usr/local/go/src/net/http/server.go:3070 +0x385 fp=0xc0005a4eb0 sp=0xc0005a4d80 pc=0x16c4bc5
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer.func2()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:469 +0x37 fp=0xc0005a4f90 sp=0xc0005a4eb0 pc=0x32500f7
   > github.com/pingcap/tidb/util.WithRecovery(0x40d6860?, 0xc000120008?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc0005a4fc0 sp=0xc0005a4f90 pc=0x208e513
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer.func6()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:468 +0x28 fp=0xc0005a4fe0 sp=0xc0005a4fc0 pc=0x3250088
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0005a4fe8 sp=0xc0005a4fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:468 +0x4ea
   > goroutine 659 [select]:
   > runtime.gopark(0xc000bcbd48?, 0x2?, 0x80?, 0x44?, 0xc000bcbc94?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000bcbb08 sp=0xc000bcbae8 pc=0x13c9516
   > runtime.selectgo(0xc000bcbd48, 0xc000bcbc90, 0x60384e0?, 0x0, 0x1?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000bcbc48 sp=0xc000bcbb08 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).loadStatsWorker(0xc010bc6640)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1359 +0x485 fp=0xc000bcbfc8 sp=0xc000bcbc48 pc=0x2797fe5
   > github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1292 +0x26 fp=0xc000bcbfe0 sp=0xc000bcbfc8 pc=0x2797566
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000bcbfe8 sp=0xc000bcbfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1292 +0x10a
   > goroutine 587 [select]:
   > runtime.gopark(0xc00faa0718?, 0x3?, 0x4?, 0x30?, 0xc00faa068a?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00faa04c8 sp=0xc00faa04a8 pc=0x13c9516
   > runtime.selectgo(0xc00faa0718, 0xc00faa0684, 0x0?, 0x0, 0x13c9516?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00faa0608 sp=0xc00faa04c8 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).LoadSysVarCacheLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1032 +0x145 fp=0xc00faa07e0 sp=0xc00faa0608 pc=0x2794ca5
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00faa07e8 sp=0xc00faa07e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).LoadSysVarCacheLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1023 +0x172
   > goroutine 658 [select]:
   > runtime.gopark(0xc00fc07fa8?, 0x2?, 0x0?, 0x30?, 0xc00fc07f84?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fc07e08 sp=0xc00fc07de8 pc=0x13c9516
   > runtime.selectgo(0xc00fc07fa8, 0xc00fc07f80, 0xc000691800?, 0x0, 0xc011098e70?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fc07f48 sp=0xc00fc07e08 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).TelemetryRotateSubWindowLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1214 +0xcc fp=0xc00fc07fe0 sp=0xc00fc07f48 pc=0x2796b4c
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fc07fe8 sp=0xc00fc07fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).TelemetryRotateSubWindowLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1207 +0x8f
   > goroutine 5348 [select]:
   > runtime.gopark(0xc01061e728?, 0x2?, 0x60?, 0x6f?, 0xc01061e6ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01061e558 sp=0xc01061e538 pc=0x13c9516
   > runtime.selectgo(0xc01061e728, 0xc01061e6e8, 0x3b67af1?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01061e698 sp=0xc01061e558 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc0114b80c0, {0x4134ba0, 0xc0113a58c0}, 0xc0114a01a0, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc01061e7a8 sp=0xc01061e698 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc01061e7e0 sp=0xc01061e7a8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01061e7e8 sp=0xc01061e7e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 695 [IO wait]:
   > runtime.gopark(0x18?, 0xc000580400?, 0x0?, 0xe0?, 0xc000bd7b70?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000bd7b00 sp=0xc000bd7ae0 pc=0x13c9516
   > runtime.netpollblock(0x14?, 0x24f6d45?, 0x0?)
   > 	/usr/local/go/src/runtime/netpoll.go:526 +0xf7 fp=0xc000bd7b38 sp=0xc000bd7b00 pc=0x13c18f7
   > internal/poll.runtime_pollWait(0x7f5879c22f70, 0x72)
   > 	/usr/local/go/src/runtime/netpoll.go:305 +0x89 fp=0xc000bd7b58 sp=0xc000bd7b38 pc=0x13f5d09
   > internal/poll.(*pollDesc).wait(0xc010227780?, 0xc000bd7d20?, 0x0)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:84 +0x32 fp=0xc000bd7b80 sp=0xc000bd7b58 pc=0x1473092
   > internal/poll.(*pollDesc).waitRead(...)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:89
   > internal/poll.(*FD).Accept(0xc010227780)
   > 	/usr/local/go/src/internal/poll/fd_unix.go:614 +0x234 fp=0xc000bd7c18 sp=0xc000bd7b80 pc=0x1478494
   > net.(*netFD).accept(0xc010227780)
   > 	/usr/local/go/src/net/fd_unix.go:172 +0x35 fp=0xc000bd7cd0 sp=0xc000bd7c18 pc=0x1597315
   > net.(*TCPListener).accept(0xc010fc91b8)
   > 	/usr/local/go/src/net/tcpsock_posix.go:142 +0x28 fp=0xc000bd7d00 sp=0xc000bd7cd0 pc=0x15b3288
   > net.(*TCPListener).Accept(0xc010fc91b8)
   > 	/usr/local/go/src/net/tcpsock.go:288 +0x3d fp=0xc000bd7d30 sp=0xc000bd7d00 pc=0x15b22fd
   > github.com/pingcap/tidb/server.(*Server).startNetworkListener(0xc000984270, {0x40d4c30, 0xc010fc91b8}, 0x0, 0xc000b784e0?)
   > 	/go/src/github.com/pingcap/tidb/server/server.go:378 +0xa6 fp=0xc000bd7fa8 sp=0xc000bd7d30 pc=0x32581c6
   > github.com/pingcap/tidb/server.(*Server).Run.func1()
   > 	/go/src/github.com/pingcap/tidb/server/server.go:363 +0x34 fp=0xc000bd7fe0 sp=0xc000bd7fa8 pc=0x32580f4
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000bd7fe8 sp=0xc000bd7fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/server.(*Server).Run
   > 	/go/src/github.com/pingcap/tidb/server/server.go:363 +0x145
   > goroutine 696 [IO wait]:
   > runtime.gopark(0x8?, 0xc0005a5b28?, 0x0?, 0x0?, 0xc0005a5b78?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0005a5b08 sp=0xc0005a5ae8 pc=0x13c9516
   > runtime.netpollblock(0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/netpoll.go:526 +0xf7 fp=0xc0005a5b40 sp=0xc0005a5b08 pc=0x13c18f7
   > internal/poll.runtime_pollWait(0x7f5879c22e80, 0x72)
   > 	/usr/local/go/src/runtime/netpoll.go:305 +0x89 fp=0xc0005a5b60 sp=0xc0005a5b40 pc=0x13f5d09
   > internal/poll.(*pollDesc).wait(0xc010227800?, 0x13a3201?, 0x0)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:84 +0x32 fp=0xc0005a5b88 sp=0xc0005a5b60 pc=0x1473092
   > internal/poll.(*pollDesc).waitRead(...)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:89
   > internal/poll.(*FD).Accept(0xc010227800)
   > 	/usr/local/go/src/internal/poll/fd_unix.go:614 +0x234 fp=0xc0005a5c20 sp=0xc0005a5b88 pc=0x1478494
   > net.(*netFD).accept(0xc010227800)
   > 	/usr/local/go/src/net/fd_unix.go:172 +0x35 fp=0xc0005a5cd8 sp=0xc0005a5c20 pc=0x1597315
   > net.(*UnixListener).accept(0xc00faa5558?)
   > 	/usr/local/go/src/net/unixsock_posix.go:166 +0x1c fp=0xc0005a5d00 sp=0xc0005a5cd8 pc=0x15b9c1c
   > net.(*UnixListener).Accept(0xc0004d2480)
   > 	/usr/local/go/src/net/unixsock.go:260 +0x3d fp=0xc0005a5d30 sp=0xc0005a5d00 pc=0x15b82bd
   > github.com/pingcap/tidb/server.(*Server).startNetworkListener(0xc000984270, {0x40d4c60, 0xc0004d2480}, 0x1, 0xc00faa5538?)
   > 	/go/src/github.com/pingcap/tidb/server/server.go:378 +0xa6 fp=0xc0005a5fa8 sp=0xc0005a5d30 pc=0x32581c6
   > github.com/pingcap/tidb/server.(*Server).Run.func2()
   > 	/go/src/github.com/pingcap/tidb/server/server.go:364 +0x37 fp=0xc0005a5fe0 sp=0xc0005a5fa8 pc=0x3258097
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0005a5fe8 sp=0xc0005a5fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/server.(*Server).Run
   > 	/go/src/github.com/pingcap/tidb/server/server.go:364 +0x1db
   > goroutine 5290 [select]:
   > runtime.gopark(0xc00fc01f00?, 0x2?, 0x60?, 0xa0?, 0xc00fc01e44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fc01c48 sp=0xc00fc01c28 pc=0x13c9516
   > runtime.selectgo(0xc00fc01f00, 0xc00fc01e40, 0xc00fc01de8?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fc01d88 sp=0xc00fc01c48 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc0119b3400, {0x4134ba0, 0xc0113a58c0})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc00fc01f30 sp=0xc00fc01d88 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc0119b3400, {0x4134ba0, 0xc0113a58c0}, 0xc011d020a0)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc00fc01fb0 sp=0xc00fc01f30 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc00fc01fe0 sp=0xc00fc01fb0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fc01fe8 sp=0xc00fc01fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 752 [select]:
   > runtime.gopark(0xc00ffc2778?, 0x2?, 0xd8?, 0x3f?, 0xc00ffc26ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00ffc2558 sp=0xc00ffc2538 pc=0x13c9516
   > runtime.selectgo(0xc00ffc2778, 0xc00ffc26e8, 0x3b67af1?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00ffc2698 sp=0xc00ffc2558 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc00ff7e900, {0x40d68d0?, 0xc010546960?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc00ffc27b8 sp=0xc00ffc2698 pc=0x30ecdf4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc00ffc27e0 sp=0xc00ffc27b8 pc=0x30ec08e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00ffc27e8 sp=0xc00ffc27e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 751 [select]:
   > runtime.gopark(0xc00ffc5778?, 0x2?, 0x0?, 0x0?, 0xc00ffc56ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00ffc5558 sp=0xc00ffc5538 pc=0x13c9516
   > runtime.selectgo(0xc00ffc5778, 0xc00ffc56e8, 0x3b67af1?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00ffc5698 sp=0xc00ffc5558 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc00ff7e8c0, {0x40d68d0?, 0xc010546960?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc00ffc57b8 sp=0xc00ffc5698 pc=0x30ecdf4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc00ffc57e0 sp=0xc00ffc57b8 pc=0x30ec08e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00ffc57e8 sp=0xc00ffc57e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 750 [select]:
   > runtime.gopark(0xc00ffc3f78?, 0x2?, 0x0?, 0x0?, 0xc00ffc3eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00ffc3d58 sp=0xc00ffc3d38 pc=0x13c9516
   > runtime.selectgo(0xc00ffc3f78, 0xc00ffc3ee8, 0x3b67af1?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00ffc3e98 sp=0xc00ffc3d58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc00ff7e880, {0x40d68d0?, 0xc010546960?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc00ffc3fb8 sp=0xc00ffc3e98 pc=0x30ecdf4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc00ffc3fe0 sp=0xc00ffc3fb8 pc=0x30ec08e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00ffc3fe8 sp=0xc00ffc3fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 5289 [semacquire]:
   > runtime.gopark(0x2fb8f3f?, 0xc0106cc728?, 0xa0?, 0xf4?, 0x60384e0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0106cc690 sp=0xc0106cc670 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc011d02098, 0xc0?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc0106cc6f8 sp=0xc0106cc690 pc=0x13dae5e
   > sync.runtime_Semacquire(0xc011b88c60?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc0106cc728 sp=0xc0106cc6f8 pc=0x13f7f65
   > sync.(*WaitGroup).Wait(0xc01183f0c0?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc0106cc750 sp=0xc0106cc728 pc=0x140b312
   > github.com/pingcap/tidb/executor.(*HashAggExec).waitPartialWorkerAndCloseOutputChs(0xc010d8e400, 0x13d0505?)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:815 +0x25 fp=0xc0106cc798 sp=0xc0106cc750 pc=0x2fbc465
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:844 +0x45 fp=0xc0106cc7e0 sp=0xc0106cc798 pc=0x2fbcd85
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0106cc7e8 sp=0xc0106cc7e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:843 +0x2e5
   > goroutine 5200 [chan receive]:
   > runtime.gopark(0xc0119bb590?, 0xc0006b81a0?, 0x6d?, 0xcb?, 0xc011c07448?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc011c073a0 sp=0xc011c07380 pc=0x13c9516
   > runtime.chanrecv(0xc0119c3e60, 0xc011c07478, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc011c07430 sp=0xc011c073a0 pc=0x13934bb
   > runtime.chanrecv2(0xc010d8e400?, 0x40d68d0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc011c07458 sp=0xc011c07430 pc=0x1392ff8
   > github.com/pingcap/tidb/executor.(*HashAggExec).parallelExec(0xc010d8e400, {0x40d68d0?, 0xc010546960?}, 0xc011d002d0)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:888 +0x89 fp=0xc011c07490 sp=0xc011c07458 pc=0x2fbcf29
   > github.com/pingcap/tidb/executor.(*HashAggExec).Next(0x40d68d0?, {0x40d68d0?, 0xc010546960?}, 0xc011c07520?)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:768 +0x76 fp=0xc011c074c0 sp=0xc011c07490 pc=0x2fbbeb6
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc010546960}, {0x40d9120, 0xc010d8e400}, 0xc011d002d0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc011c07600 sp=0xc011c074c0 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*MaxOneRowExec).Next(0xc00fdc1260, {0x40d68d0, 0xc010546960}, 0xc011d002d0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1518 +0xa8 fp=0xc011c07650 sp=0xc011c07600 pc=0x30413a8
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc010546960}, {0x40d94a0, 0xc00fdc1260}, 0xc011d002d0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc011c07790 sp=0xc011c07650 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*SelectionExec).Next(0xc000985d40, {0x40d68d0, 0xc010546960}, 0xc011860d20)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1394 +0xed fp=0xc011c07820 sp=0xc011c07790 pc=0x304012d
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc010546960}, {0x40d9960, 0xc000985d40}, 0xc011860d20)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc011c07960 sp=0xc011c07820 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*NestedLoopApplyExec).fetchAllInners(0xc000715a40, {0x40d68d0, 0xc010546960})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:979 +0x346 fp=0xc011c07a58 sp=0xc011c07960 pc=0x30b2966
   > github.com/pingcap/tidb/executor.(*NestedLoopApplyExec).Next(0xc000715a40, {0x40d68d0, 0xc010546960}, 0xc011860dc0)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:1032 +0x5b6 fp=0xc011c07bb8 sp=0xc011c07a58 pc=0x30b32b6
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc010546960}, {0x40d9560, 0xc000715a40}, 0xc011860dc0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc011c07cf8 sp=0xc011c07bb8 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*ProjectionExec).unParallelExecute(0xc00fb52900, {0x40d68d0?, 0xc010546960?}, 0xc011b76550)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:194 +0xb8 fp=0xc011c07d48 sp=0xc011c07cf8 pc=0x30eb458
   > github.com/pingcap/tidb/executor.(*ProjectionExec).Next(0xc00fb52900, {0x40d68d0, 0xc010546960}, 0xc0108e3f0c?)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:180 +0x5a fp=0xc011c07d80 sp=0xc011c07d48 pc=0x30eb31a
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc010546960}, {0x40d9720, 0xc00fb52900}, 0xc011b76550)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc011c07ec0 sp=0xc011c07d80 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*UnionExec).resultPuller(0xc01083bf00, {0x40d68d0, 0xc010546960}, 0x1)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1673 +0x48f fp=0xc011c07fb0 sp=0xc011c07ec0 pc=0x30420ef
   > github.com/pingcap/tidb/executor.(*UnionExec).initialize.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1623 +0x32 fp=0xc011c07fe0 sp=0xc011c07fb0 pc=0x3041c32
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc011c07fe8 sp=0xc011c07fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*UnionExec).initialize
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1623 +0x233
   > goroutine 781 [semacquire]:
   > runtime.gopark(0xc0101a2ea0?, 0xc000adaf60?, 0xc0?, 0x60?, 0x13?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00ffbfe90 sp=0xc00ffbfe70 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc00ff766f8, 0x0?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc00ffbfef8 sp=0xc00ffbfe90 pc=0x13dae5e
   > sync.runtime_Semacquire(0xc000adb500?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc00ffbff28 sp=0xc00ffbfef8 pc=0x13f7f65
   > sync.(*WaitGroup).Wait(0x40d68d0?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc00ffbff50 sp=0xc00ffbff28 pc=0x140b312
   > github.com/pingcap/tidb/executor.(*HashAggExec).waitPartialWorkerAndCloseOutputChs(0xc010d8e800, 0xc00ffbffd0?)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:815 +0x25 fp=0xc00ffbff98 sp=0xc00ffbff50 pc=0x2fbc465
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:844 +0x45 fp=0xc00ffbffe0 sp=0xc00ffbff98 pc=0x2fbcd85
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00ffbffe8 sp=0xc00ffbffe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:843 +0x2e5
   > goroutine 782 [select]:
   > runtime.gopark(0xc00ffc2f00?, 0x2?, 0x37?, 0x47?, 0xc00ffc2e44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00ffc2c48 sp=0xc00ffc2c28 pc=0x13c9516
   > runtime.selectgo(0xc00ffc2f00, 0xc00ffc2e40, 0x2?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00ffc2d88 sp=0xc00ffc2c48 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc000581c00, {0x4134ba0, 0xc0113a58c0})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc00ffc2f30 sp=0xc00ffc2d88 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc000581c00, {0x4134ba0, 0xc0113a58c0}, 0xc00ff76700)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc00ffc2fb0 sp=0xc00ffc2f30 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc00ffc2fe0 sp=0xc00ffc2fb0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00ffc2fe8 sp=0xc00ffc2fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 783 [select]:
   > runtime.gopark(0xc00faa5700?, 0x2?, 0x37?, 0x47?, 0xc00faa5644?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00faa5448 sp=0xc00faa5428 pc=0x13c9516
   > runtime.selectgo(0xc00faa5700, 0xc00faa5640, 0x0?, 0x0, 0xc00faa55d0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00faa5588 sp=0xc00faa5448 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc000581cc0, {0x4134ba0, 0xc0113a58c0})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc00faa5730 sp=0xc00faa5588 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc000581cc0, {0x4134ba0, 0xc0113a58c0}, 0xc00ff76700)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc00faa57b0 sp=0xc00faa5730 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc00faa57e0 sp=0xc00faa57b0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00faa57e8 sp=0xc00faa57e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 784 [select]:
   > runtime.gopark(0xc00faa1f00?, 0x2?, 0x37?, 0x47?, 0xc00faa1e44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00faa1c48 sp=0xc00faa1c28 pc=0x13c9516
   > runtime.selectgo(0xc00faa1f00, 0xc00faa1e40, 0x375f940?, 0x0, 0x203000?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00faa1d88 sp=0xc00faa1c48 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc000581d80, {0x4134ba0, 0xc0113a58c0})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc00faa1f30 sp=0xc00faa1d88 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc000581d80, {0x4134ba0, 0xc0113a58c0}, 0xc00ff76700)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc00faa1fb0 sp=0xc00faa1f30 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc00faa1fe0 sp=0xc00faa1fb0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00faa1fe8 sp=0xc00faa1fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 785 [select]:
   > runtime.gopark(0xc00faa2f00?, 0x2?, 0x37?, 0x47?, 0xc00faa2e44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00faa2c48 sp=0xc00faa2c28 pc=0x13c9516
   > runtime.selectgo(0xc00faa2f00, 0xc00faa2e40, 0x375f940?, 0x0, 0x203004?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00faa2d88 sp=0xc00faa2c48 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc000581e40, {0x4134ba0, 0xc0113a58c0})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc00faa2f30 sp=0xc00faa2d88 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc000581e40, {0x4134ba0, 0xc0113a58c0}, 0xc00ff76700)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc00faa2fb0 sp=0xc00faa2f30 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc00faa2fe0 sp=0xc00faa2fb0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00faa2fe8 sp=0xc00faa2fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 786 [select]:
   > runtime.gopark(0xc00faa2700?, 0x2?, 0x37?, 0x47?, 0xc00faa2644?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000bd8c48 sp=0xc000bd8c28 pc=0x13c9516
   > runtime.selectgo(0xc000bd8f00, 0xc00faa2640, 0x375f940?, 0x0, 0x203003?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000bd8d88 sp=0xc000bd8c48 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc000581f00, {0x4134ba0, 0xc0113a58c0})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc000bd8f30 sp=0xc000bd8d88 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc000581f00, {0x4134ba0, 0xc0113a58c0}, 0xc00ff76700)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc000bd8fb0 sp=0xc000bd8f30 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc000bd8fe0 sp=0xc000bd8fb0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000bd8fe8 sp=0xc000bd8fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 787 [semacquire]:
   > runtime.gopark(0x0?, 0x0?, 0x40?, 0xf1?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00faa7ed8 sp=0xc00faa7eb8 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc00ff76708, 0xf8?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc00faa7f40 sp=0xc00faa7ed8 pc=0x13dae5e
   > sync.runtime_Semacquire(0x0?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc00faa7f70 sp=0xc00faa7f40 pc=0x13f7f65
   > sync.(*WaitGroup).Wait(0xc00faa7f40?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc00faa7f98 sp=0xc00faa7f70 pc=0x140b312
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:856 +0x45 fp=0xc00faa7fe0 sp=0xc00faa7f98 pc=0x2fbcc85
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00faa7fe8 sp=0xc00faa7fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:855 +0x4c5
   > goroutine 788 [semacquire]:
   > runtime.gopark(0x0?, 0x0?, 0xc0?, 0x63?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00faa0eb8 sp=0xc00faa0e98 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc00ff766e8, 0x0?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc00faa0f20 sp=0xc00faa0eb8 pc=0x13dae5e
   > sync.runtime_Semacquire(0x0?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc00faa0f50 sp=0xc00faa0f20 pc=0x13f7f65
   > sync.(*WaitGroup).Wait(0x0?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc00faa0f78 sp=0xc00faa0f50 pc=0x140b312
   > github.com/pingcap/tidb/executor.(*HashAggExec).waitAllWorkersAndCloseFinalOutputCh(0xc010d8e800, {0xc00faa0fb8, 0x3, 0xc00faa0fd0?})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:827 +0x35 fp=0xc00faa0f98 sp=0xc00faa0f78 pc=0x2fbc5b5
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func6()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:864 +0x5a fp=0xc00faa0fe0 sp=0xc00faa0f98 pc=0x2fbcc1a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00faa0fe8 sp=0xc00faa0fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:864 +0x54d
   > goroutine 5303 [select]:
   > runtime.gopark(0xc00fe5c778?, 0x2?, 0x88?, 0x33?, 0xc00fe5c6ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fe5c558 sp=0xc00fe5c538 pc=0x13c9516
   > runtime.selectgo(0xc00fe5c778, 0xc00fe5c6e8, 0x3b67af1?, 0x0, 0x3041e97?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fe5c698 sp=0xc00fe5c558 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc00ff0d9c0, {0x40d68d0?, 0xc010546960?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc00fe5c7b8 sp=0xc00fe5c698 pc=0x30ecdf4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc00fe5c7e0 sp=0xc00fe5c7b8 pc=0x30ec08e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fe5c7e8 sp=0xc00fe5c7e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 5355 [select]:
   > runtime.gopark(0xc0006b7f00?, 0x2?, 0x8?, 0x0?, 0xc0006b7e44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0006b7c48 sp=0xc0006b7c28 pc=0x13c9516
   > runtime.selectgo(0xc0006b7f00, 0xc0006b7e40, 0x2?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0006b7d88 sp=0xc0006b7c48 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc0114b8580, {0x4134ba0, 0xc0113a58c0})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc0006b7f30 sp=0xc0006b7d88 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc0114b8580, {0x4134ba0, 0xc0113a58c0}, 0xc0114a01b0)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc0006b7fb0 sp=0xc0006b7f30 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc0006b7fe0 sp=0xc0006b7fb0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0006b7fe8 sp=0xc0006b7fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 5356 [select]:
   > runtime.gopark(0xc0106cbf00?, 0x2?, 0x60?, 0xa0?, 0xc0106cbe44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0106cbc48 sp=0xc0106cbc28 pc=0x13c9516
   > runtime.selectgo(0xc0106cbf00, 0xc0106cbe40, 0x2?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0106cbd88 sp=0xc0106cbc48 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc0114b8640, {0x4134ba0, 0xc0113a58c0})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc0106cbf30 sp=0xc0106cbd88 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc0114b8640, {0x4134ba0, 0xc0113a58c0}, 0xc0114a01b0)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc0106cbfb0 sp=0xc0106cbf30 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc0106cbfe0 sp=0xc0106cbfb0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0106cbfe8 sp=0xc0106cbfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 5292 [select]:
   > runtime.gopark(0xc0106c8f00?, 0x2?, 0x60?, 0xa0?, 0xc0106c8e44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0106c8c48 sp=0xc0106c8c28 pc=0x13c9516
   > runtime.selectgo(0xc0106c8f00, 0xc0106c8e40, 0x59a5d72?, 0x0, 0x1?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0106c8d88 sp=0xc0106c8c48 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc0119b3580, {0x4134ba0, 0xc0113a58c0})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc0106c8f30 sp=0xc0106c8d88 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc0119b3580, {0x4134ba0, 0xc0113a58c0}, 0xc011d020a0)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc0106c8fb0 sp=0xc0106c8f30 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc0106c8fe0 sp=0xc0106c8fb0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0106c8fe8 sp=0xc0106c8fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 5358 [semacquire]:
   > runtime.gopark(0x0?, 0x0?, 0x80?, 0x99?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01150ced8 sp=0xc01150ceb8 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc0114a01b8, 0x0?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc01150cf40 sp=0xc01150ced8 pc=0x13dae5e
   > sync.runtime_Semacquire(0x0?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc01150cf70 sp=0xc01150cf40 pc=0x13f7f65
   > sync.(*WaitGroup).Wait(0x0?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc01150cf98 sp=0xc01150cf70 pc=0x140b312
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:856 +0x45 fp=0xc01150cfe0 sp=0xc01150cf98 pc=0x2fbcc85
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01150cfe8 sp=0xc01150cfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:855 +0x4c5
   > goroutine 5284 [select]:
   > runtime.gopark(0xc00ff65f28?, 0x2?, 0x60?, 0x5e?, 0xc00ff65eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00ff65d58 sp=0xc00ff65d38 pc=0x13c9516
   > runtime.selectgo(0xc00ff65f28, 0xc00ff65ee8, 0x13?, 0x0, 0xc000ce7a70?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00ff65e98 sp=0xc00ff65d58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc0119b3000, {0x4134ba0, 0xc0113a58c0}, 0xc011d02090, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc00ff65fa8 sp=0xc00ff65e98 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc00ff65fe0 sp=0xc00ff65fa8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00ff65fe8 sp=0xc00ff65fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 5330 [chan receive]:
   > runtime.gopark(0x355a760?, 0xc011ba9d20?, 0xe0?, 0xaa?, 0xc011bb7a40?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc011ba9c48 sp=0xc011ba9c28 pc=0x13c9516
   > runtime.chanrecv(0xc011bb75c0, 0xc011ba9d28, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc011ba9cd8 sp=0xc011ba9c48 pc=0x13934bb
   > runtime.chanrecv1(0xc00fb527e0?, 0x40d68d0?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc011ba9d00 sp=0xc011ba9cd8 pc=0x1392fb8
   > github.com/pingcap/tidb/executor.(*ProjectionExec).parallelExecute(0xc00fb527e0, {0x40d68d0?, 0xc010546960?}, 0xc011d00370)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:218 +0x92 fp=0xc011ba9d48 sp=0xc011ba9d00 pc=0x30eb612
   > github.com/pingcap/tidb/executor.(*ProjectionExec).Next(0xc00fb527e0, {0x40d68d0, 0xc010546960}, 0xc011ba9f0c?)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:182 +0x78 fp=0xc011ba9d80 sp=0xc011ba9d48 pc=0x30eb338
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc010546960}, {0x40d9720, 0xc00fb527e0}, 0xc011d00370)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc011ba9ec0 sp=0xc011ba9d80 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*UnionExec).resultPuller(0xc01083bd00, {0x40d68d0, 0xc010546960}, 0x1)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1673 +0x48f fp=0xc011ba9fb0 sp=0xc011ba9ec0 pc=0x30420ef
   > github.com/pingcap/tidb/executor.(*UnionExec).initialize.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1623 +0x32 fp=0xc011ba9fe0 sp=0xc011ba9fb0 pc=0x3041c32
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc011ba9fe8 sp=0xc011ba9fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*UnionExec).initialize
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1623 +0x233
   > goroutine 5288 [select]:
   > runtime.gopark(0xc00fe5f728?, 0x2?, 0x48?, 0x2a?, 0xc00fe5f6ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fe5f558 sp=0xc00fe5f538 pc=0x13c9516
   > runtime.selectgo(0xc00fe5f728, 0xc00fe5f6e8, 0x1fb5126?, 0x0, 0xc00fe5f708?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fe5f698 sp=0xc00fe5f558 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc0119b3300, {0x4134ba0, 0xc0113a58c0}, 0xc011d02090, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc00fe5f7a8 sp=0xc00fe5f698 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc00fe5f7e0 sp=0xc00fe5f7a8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fe5f7e8 sp=0xc00fe5f7e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 5286 [select]:
   > runtime.gopark(0xc00fed3f28?, 0x2?, 0xc0?, 0x63?, 0xc00fed3eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fed3d58 sp=0xc00fed3d38 pc=0x13c9516
   > runtime.selectgo(0xc00fed3f28, 0xc00fed3ee8, 0x60384e0?, 0x0, 0xc00feea6a8?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fed3e98 sp=0xc00fed3d58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc0119b3180, {0x4134ba0, 0xc0113a58c0}, 0xc011d02090, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc00fed3fa8 sp=0xc00fed3e98 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc00fed3fe0 sp=0xc00fed3fa8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fed3fe8 sp=0xc00fed3fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 5294 [select]:
   > runtime.gopark(0xc0106cff00?, 0x2?, 0x8?, 0x0?, 0xc0106cfe44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0106cfc48 sp=0xc0106cfc28 pc=0x13c9516
   > runtime.selectgo(0xc0106cff00, 0xc0106cfe40, 0xc0106cff0c?, 0x0, 0x1fb5214?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0106cfd88 sp=0xc0106cfc48 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc0119b3700, {0x4134ba0, 0xc0113a58c0})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc0106cff30 sp=0xc0106cfd88 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc0119b3700, {0x4134ba0, 0xc0113a58c0}, 0xc011d020a0)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc0106cffb0 sp=0xc0106cff30 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc0106cffe0 sp=0xc0106cffb0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0106cffe8 sp=0xc0106cffe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 5293 [select]:
   > runtime.gopark(0xc01150af00?, 0x2?, 0x0?, 0x0?, 0xc01150ae44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01150ac48 sp=0xc01150ac28 pc=0x13c9516
   > runtime.selectgo(0xc01150af00, 0xc01150ae40, 0x60384e0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01150ad88 sp=0xc01150ac48 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc0119b3640, {0x4134ba0, 0xc0113a58c0})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc01150af30 sp=0xc01150ad88 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc0119b3640, {0x4134ba0, 0xc0113a58c0}, 0xc011d020a0)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc01150afb0 sp=0xc01150af30 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc01150afe0 sp=0xc01150afb0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01150afe8 sp=0xc01150afe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 5354 [select]:
   > runtime.gopark(0xc0106cf700?, 0x2?, 0x8?, 0x0?, 0xc0106cf644?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0106cf448 sp=0xc0106cf428 pc=0x13c9516
   > runtime.selectgo(0xc0106cf700, 0xc0106cf640, 0x2?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0106cf588 sp=0xc0106cf448 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc0114b84c0, {0x4134ba0, 0xc0113a58c0})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc0106cf730 sp=0xc0106cf588 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc0114b84c0, {0x4134ba0, 0xc0113a58c0}, 0xc0114a01b0)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc0106cf7b0 sp=0xc0106cf730 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc0106cf7e0 sp=0xc0106cf7b0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0106cf7e8 sp=0xc0106cf7e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 5199 [chan receive]:
   > runtime.gopark(0xc0114ac8a0?, 0xc0100c21a0?, 0x6d?, 0xcb?, 0xc0108df448?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0108df3a0 sp=0xc0108df380 pc=0x13c9516
   > runtime.chanrecv(0xc0114b6000, 0xc0108df478, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc0108df430 sp=0xc0108df3a0 pc=0x13934bb
   > runtime.chanrecv2(0xc010d8e200?, 0x40d68d0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc0108df458 sp=0xc0108df430 pc=0x1392ff8
   > github.com/pingcap/tidb/executor.(*HashAggExec).parallelExec(0xc010d8e200, {0x40d68d0?, 0xc010546960?}, 0xc0114b0870)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:888 +0x89 fp=0xc0108df490 sp=0xc0108df458 pc=0x2fbcf29
   > github.com/pingcap/tidb/executor.(*HashAggExec).Next(0x40d68d0?, {0x40d68d0?, 0xc010546960?}, 0xc0108df540?)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:768 +0x76 fp=0xc0108df4c0 sp=0xc0108df490 pc=0x2fbbeb6
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc010546960}, {0x40d9120, 0xc010d8e200}, 0xc0114b0870)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc0108df600 sp=0xc0108df4c0 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*MaxOneRowExec).Next(0xc00fdc0a10, {0x40d68d0, 0xc010546960}, 0xc0114b0870)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1518 +0xa8 fp=0xc0108df650 sp=0xc0108df600 pc=0x30413a8
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc010546960}, {0x40d94a0, 0xc00fdc0a10}, 0xc0114b0870)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc0108df790 sp=0xc0108df650 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*SelectionExec).Next(0xc000985930, {0x40d68d0, 0xc010546960}, 0xc011b766e0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1394 +0xed fp=0xc0108df820 sp=0xc0108df790 pc=0x304012d
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc010546960}, {0x40d9960, 0xc000985930}, 0xc011b766e0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc0108df960 sp=0xc0108df820 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*NestedLoopApplyExec).fetchAllInners(0xc000715880, {0x40d68d0, 0xc010546960})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:979 +0x346 fp=0xc0108dfa58 sp=0xc0108df960 pc=0x30b2966
   > github.com/pingcap/tidb/executor.(*NestedLoopApplyExec).Next(0xc000715880, {0x40d68d0, 0xc010546960}, 0xc011b76730)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:1032 +0x5b6 fp=0xc0108dfbb8 sp=0xc0108dfa58 pc=0x30b32b6
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc010546960}, {0x40d9560, 0xc000715880}, 0xc011b76730)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc0108dfcf8 sp=0xc0108dfbb8 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*ProjectionExec).unParallelExecute(0xc00fb525a0, {0x40d68d0?, 0xc010546960?}, 0xc011b76500)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:194 +0xb8 fp=0xc0108dfd48 sp=0xc0108dfcf8 pc=0x30eb458
   > github.com/pingcap/tidb/executor.(*ProjectionExec).Next(0xc00fb525a0, {0x40d68d0, 0xc010546960}, 0xc0108dff0c?)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:180 +0x5a fp=0xc0108dfd80 sp=0xc0108dfd48 pc=0x30eb31a
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc010546960}, {0x40d9720, 0xc00fb525a0}, 0xc011b76500)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc0108dfec0 sp=0xc0108dfd80 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*UnionExec).resultPuller(0xc01083bf00, {0x40d68d0, 0xc010546960}, 0x0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1673 +0x48f fp=0xc0108dffb0 sp=0xc0108dfec0 pc=0x30420ef
   > github.com/pingcap/tidb/executor.(*UnionExec).initialize.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1623 +0x32 fp=0xc0108dffe0 sp=0xc0108dffb0 pc=0x3041c32
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0108dffe8 sp=0xc0108dffe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*UnionExec).initialize
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1623 +0x233
   > goroutine 5323 [semacquire]:
   > runtime.gopark(0x105dfd6f8fc8?, 0x0?, 0x20?, 0x4?, 0xc0119e6f00?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fbf9558 sp=0xc00fbf9538 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc0057ac3a4, 0xe0?, 0x3, 0x1)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc00fbf95c0 sp=0xc00fbf9558 pc=0x13dae5e
   > sync.runtime_SemacquireMutex(0x139a1bf?, 0x60?, 0x50?)
   > 	/usr/local/go/src/runtime/sema.go:77 +0x25 fp=0xc00fbf95f0 sp=0xc00fbf95c0 pc=0x13f8085
   > sync.(*Mutex).lockSlow(0xc0057ac3a0)
   > 	/usr/local/go/src/sync/mutex.go:171 +0x165 fp=0xc00fbf9640 sp=0xc00fbf95f0 pc=0x1409825
   > sync.(*Mutex).Lock(...)
   > 	/usr/local/go/src/sync/mutex.go:90
   > github.com/pingcap/tidb/util/memory.(*Tracker).FallbackOldAndSetNewAction(0xc0057ac390, {0x40dbc60?, 0xc0118619f0?})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:162 +0x68 fp=0xc00fbf9698 sp=0xc00fbf9640 pc=0x1fb3308
   > github.com/pingcap/tidb/store/copr.(*CopClient).Send(0xc01030c0f0, {0x40d68d0, 0xc010546960}, 0xc0107dd400, {0x3565ba0?, 0xc00fe9c090?}, 0xc011a68680)
   > 	/go/src/github.com/pingcap/tidb/store/copr/coprocessor.go:137 +0x857 fp=0xc00fbf9860 sp=0xc00fbf9698 pc=0x249aff7
   > github.com/pingcap/tidb/distsql.Select({0x40d68d0, 0xc010546960}, {0x4134ba0?, 0xc0113a58c0}, 0xc0107dd400, {0xc00fb54e60, 0x9, 0x9}, 0xc00fb54eb0)
   > 	/go/src/github.com/pingcap/tidb/distsql/distsql.go:101 +0x5bf fp=0xc00fbf99a0 sp=0xc00fbf9860 pc=0x26aa0df
   > github.com/pingcap/tidb/distsql.SelectWithRuntimeStats({0x40d68d0?, 0xc010546960?}, {0x4134ba0?, 0xc0113a58c0?}, 0xc00fbf9a60?, {0xc00fb54e60?, 0x8?, 0x35d4e20?}, 0x1?, {0xc011864a68, ...}, ...)
   > 	/go/src/github.com/pingcap/tidb/distsql/distsql.go:150 +0x45 fp=0xc00fbf99f8 sp=0xc00fbf99a0 pc=0x26aaa65
   > github.com/pingcap/tidb/executor.selectResultHook.SelectResult({0x1?}, {0x40d68d0?, 0xc010546960?}, {0x4134ba0?, 0xc0113a58c0?}, 0x203004?, {0xc00fb54e60?, 0x203004?, 0xc01100e2d0?}, 0xc00fb54eb0, ...)
   > 	/go/src/github.com/pingcap/tidb/executor/table_reader.go:53 +0xf0 fp=0xc00fbf9a70 sp=0xc00fbf99f8 pc=0x313eb90
   > github.com/pingcap/tidb/executor.(*TableReaderExecutor).buildResp(0xc0105ce780, {0x40d68d0, 0xc010546960}, {0xc0005bb830?, 0xc000dea060?, 0x3a22656c646e6168?})
   > 	/go/src/github.com/pingcap/tidb/executor/table_reader.go:300 +0x3d6 fp=0xc00fbf9c38 sp=0xc00fbf9a70 pc=0x3140456
   > github.com/pingcap/tidb/executor.(*TableReaderExecutor).Open(0xc0105ce780, {0x40d68d0, 0xc010546960})
   > 	/go/src/github.com/pingcap/tidb/executor/table_reader.go:199 +0xa99 fp=0xc00fbf9d50 sp=0xc00fbf9c38 pc=0x313f6d9
   > github.com/pingcap/tidb/executor.(*baseExecutor).Open(...)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:185
   > github.com/pingcap/tidb/executor.(*SelectionExec).Open(0xc000985790?, {0x40d68d0?, 0xc010546960?})
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1338 +0xa2 fp=0xc00fbf9d90 sp=0xc00fbf9d50 pc=0x303fbe2
   > github.com/pingcap/tidb/executor.(*CTEExec).Open(0xc010894a00, {0x40d68d0, 0xc010546960})
   > 	/go/src/github.com/pingcap/tidb/executor/cte.go:109 +0xf2 fp=0xc00fbf9e40 sp=0xc00fbf9d90 pc=0x3022212
   > github.com/pingcap/tidb/executor.(*baseExecutor).Open(...)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:185
   > github.com/pingcap/tidb/executor.(*SelectionExec).Open(0xc000985860?, {0x40d68d0?, 0xc010546960?})
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1338 +0xa2 fp=0xc00fbf9e80 sp=0xc00fbf9e40 pc=0x303fbe2
   > github.com/pingcap/tidb/executor.(*baseExecutor).Open(...)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:185
   > github.com/pingcap/tidb/executor.(*ProjectionExec).Open(0xc00fb52360?, {0x40d68d0?, 0xc010546960?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:87 +0xa2 fp=0xc00fbf9ec0 sp=0xc00fbf9e80 pc=0x30eb022
   > github.com/pingcap/tidb/executor.(*UnionExec).resultPuller(0xc01083bc00, {0x40d68d0, 0xc010546960}, 0x1)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1656 +0x237 fp=0xc00fbf9fb0 sp=0xc00fbf9ec0 pc=0x3041e97
   > github.com/pingcap/tidb/executor.(*UnionExec).initialize.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1623 +0x32 fp=0xc00fbf9fe0 sp=0xc00fbf9fb0 pc=0x3041c32
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fbf9fe8 sp=0xc00fbf9fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*UnionExec).initialize
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1623 +0x233
   > goroutine 5201 [semacquire]:
   > runtime.gopark(0xc0104b81a0?, 0x0?, 0x0?, 0x66?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0106caef0 sp=0xc0106caed0 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc01083bfd0, 0xaf?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc0106caf58 sp=0xc0106caef0 pc=0x13dae5e
   > sync.runtime_Semacquire(0xc011874a20?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc0106caf88 sp=0xc0106caf58 pc=0x13f7f65
   > sync.(*WaitGroup).Wait(0x30ec08e?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc0106cafb0 sp=0xc0106caf88 pc=0x140b312
   > github.com/pingcap/tidb/executor.(*UnionExec).waitAllFinished(0xc01083bf00)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1595 +0x2a fp=0xc0106cafc8 sp=0xc0106cafb0 pc=0x30415ea
   > github.com/pingcap/tidb/executor.(*UnionExec).initialize.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1629 +0x26 fp=0xc0106cafe0 sp=0xc0106cafc8 pc=0x3041bc6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0106cafe8 sp=0xc0106cafe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*UnionExec).initialize
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1629 +0x40b
   > goroutine 5357 [select]:
   > runtime.gopark(0xc00ff1ef00?, 0x2?, 0x0?, 0x0?, 0xc00ff1ee44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00ff1ec48 sp=0xc00ff1ec28 pc=0x13c9516
   > runtime.selectgo(0xc00ff1ef00, 0xc00ff1ee40, 0x1392a11?, 0x0, 0x40d68d0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00ff1ed88 sp=0xc00ff1ec48 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc0114b8700, {0x4134ba0, 0xc0113a58c0})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc00ff1ef30 sp=0xc00ff1ed88 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc0114b8700, {0x4134ba0, 0xc0113a58c0}, 0xc0114a01b0)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc00ff1efb0 sp=0xc00ff1ef30 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc00ff1efe0 sp=0xc00ff1efb0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00ff1efe8 sp=0xc00ff1efe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 5324 [semacquire]:
   > runtime.gopark(0x0?, 0x1?, 0x80?, 0xb3?, 0xc01177f8c0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0101ec6f0 sp=0xc0101ec6d0 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc01083bcd0, 0x78?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc0101ec758 sp=0xc0101ec6f0 pc=0x13dae5e
   > sync.runtime_Semacquire(0x14?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc0101ec788 sp=0xc0101ec758 pc=0x13f7f65
   > sync.(*WaitGroup).Wait(0x10000c01083bc00?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc0101ec7b0 sp=0xc0101ec788 pc=0x140b312
   > github.com/pingcap/tidb/executor.(*UnionExec).waitAllFinished(0xc01083bc00)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1595 +0x2a fp=0xc0101ec7c8 sp=0xc0101ec7b0 pc=0x30415ea
   > github.com/pingcap/tidb/executor.(*UnionExec).initialize.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1629 +0x26 fp=0xc0101ec7e0 sp=0xc0101ec7c8 pc=0x3041bc6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0101ec7e8 sp=0xc0101ec7e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*UnionExec).initialize
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1629 +0x40b
   > goroutine 5304 [select]:
   > runtime.gopark(0xc00fc04778?, 0x2?, 0x8?, 0xe?, 0xc00fc046ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fc04558 sp=0xc00fc04538 pc=0x13c9516
   > runtime.selectgo(0xc00fc04778, 0xc00fc046e8, 0x3b67af1?, 0x0, 0x30420ef?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fc04698 sp=0xc00fc04558 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc00ff0da00, {0x40d68d0?, 0xc010546960?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc00fc047b8 sp=0xc00fc04698 pc=0x30ecdf4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc00fc047e0 sp=0xc00fc047b8 pc=0x30ec08e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fc047e8 sp=0xc00fc047e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 5351 [select]:
   > runtime.gopark(0xc01150c728?, 0x2?, 0x0?, 0x0?, 0xc01150c6ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01150c558 sp=0xc01150c538 pc=0x13c9516
   > runtime.selectgo(0xc01150c728, 0xc01150c6e8, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01150c698 sp=0xc01150c558 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc0114b8300, {0x4134ba0, 0xc0113a58c0}, 0xc0114a01a0, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc01150c7a8 sp=0xc01150c698 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc01150c7e0 sp=0xc01150c7a8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01150c7e8 sp=0xc01150c7e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 5331 [semacquire]:
   > runtime.gopark(0xc0057ac060?, 0x13fa50e?, 0x0?, 0x6?, 0x60384e0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc011511ef0 sp=0xc011511ed0 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc01083bdd0, 0x60?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc011511f58 sp=0xc011511ef0 pc=0x13dae5e
   > sync.runtime_Semacquire(0xc011864100?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc011511f88 sp=0xc011511f58 pc=0x13f7f65
   > sync.(*WaitGroup).Wait(0x4134ba0?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc011511fb0 sp=0xc011511f88 pc=0x140b312
   > github.com/pingcap/tidb/executor.(*UnionExec).waitAllFinished(0xc01083bd00)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1595 +0x2a fp=0xc011511fc8 sp=0xc011511fb0 pc=0x30415ea
   > github.com/pingcap/tidb/executor.(*UnionExec).initialize.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1629 +0x26 fp=0xc011511fe0 sp=0xc011511fc8 pc=0x3041bc6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc011511fe8 sp=0xc011511fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*UnionExec).initialize
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1629 +0x40b
   > goroutine 5347 [select]:
   > runtime.gopark(0xc00fed6f28?, 0x2?, 0xc7?, 0x95?, 0xc00fed6eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fed6d58 sp=0xc00fed6d38 pc=0x13c9516
   > runtime.selectgo(0xc00fed6f28, 0xc00fed6ee8, 0x3b67af1?, 0x0, 0xc011a1c558?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fed6e98 sp=0xc00fed6d58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc0114b8000, {0x4134ba0, 0xc0113a58c0}, 0xc0114a01a0, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc00fed6fa8 sp=0xc00fed6e98 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc00fed6fe0 sp=0xc00fed6fa8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fed6fe8 sp=0xc00fed6fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 5287 [select]:
   > runtime.gopark(0xc0104c2f28?, 0x2?, 0x20?, 0x89?, 0xc0104c2eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0104c2d58 sp=0xc0104c2d38 pc=0x13c9516
   > runtime.selectgo(0xc0104c2f28, 0xc0104c2ee8, 0x40d9960?, 0x0, 0xc01187ab90?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0104c2e98 sp=0xc0104c2d58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc0119b3240, {0x4134ba0, 0xc0113a58c0}, 0xc011d02090, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc0104c2fa8 sp=0xc0104c2e98 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc0104c2fe0 sp=0xc0104c2fa8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0104c2fe8 sp=0xc0104c2fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 5295 [semacquire]:
   > runtime.gopark(0xc00fb52480?, 0xc01187a870?, 0x60?, 0xec?, 0x1000000040d9ea0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00ff21ed8 sp=0xc00ff21eb8 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc011d020a8, 0x20?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc00ff21f40 sp=0xc00ff21ed8 pc=0x13dae5e
   > sync.runtime_Semacquire(0xc0119c5700?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc00ff21f70 sp=0xc00ff21f40 pc=0x13f7f65
   > sync.(*WaitGroup).Wait(0xc00ff21f68?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc00ff21f98 sp=0xc00ff21f70 pc=0x140b312
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:856 +0x45 fp=0xc00ff21fe0 sp=0xc00ff21f98 pc=0x2fbcc85
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00ff21fe8 sp=0xc00ff21fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:855 +0x4c5
   > goroutine 5353 [select]:
   > runtime.gopark(0xc01061f700?, 0x2?, 0x60?, 0xa0?, 0xc01061f644?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01061f448 sp=0xc01061f428 pc=0x13c9516
   > runtime.selectgo(0xc01061f700, 0xc01061f640, 0x2?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01061f588 sp=0xc01061f448 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc0114b8400, {0x4134ba0, 0xc0113a58c0})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc01061f730 sp=0xc01061f588 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc0114b8400, {0x4134ba0, 0xc0113a58c0}, 0xc0114a01b0)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc01061f7b0 sp=0xc01061f730 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc01061f7e0 sp=0xc01061f7b0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01061f7e8 sp=0xc01061f7e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 5296 [semacquire]:
   > runtime.gopark(0xc01149b9a8?, 0xc00faa2700?, 0xa0?, 0xeb?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00faa26b8 sp=0xc00faa2698 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc011d02088, 0x1?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc00faa2720 sp=0xc00faa26b8 pc=0x13dae5e
   > sync.runtime_Semacquire(0x100000001?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc00faa2750 sp=0xc00faa2720 pc=0x13f7f65
   > sync.(*WaitGroup).Wait(0xc011b89260?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc00faa2778 sp=0xc00faa2750 pc=0x140b312
   > github.com/pingcap/tidb/executor.(*HashAggExec).waitAllWorkersAndCloseFinalOutputCh(0xc010d8e400, {0xc00faa27b8, 0x3, 0x0?})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:827 +0x35 fp=0xc00faa2798 sp=0xc00faa2778 pc=0x2fbc5b5
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func6()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:864 +0x5a fp=0xc00faa27e0 sp=0xc00faa2798 pc=0x2fbcc1a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00faa27e8 sp=0xc00faa27e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:864 +0x54d
   > goroutine 5305 [select]:
   > runtime.gopark(0xc00fe37778?, 0x2?, 0xd6?, 0xf6?, 0xc00fe376ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fe37558 sp=0xc00fe37538 pc=0x13c9516
   > runtime.selectgo(0xc00fe37778, 0xc00fe376e8, 0x3b67af1?, 0x0, 0xc00fe37708?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fe37698 sp=0xc00fe37558 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc00ff0da40, {0x40d68d0?, 0xc010546960?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc00fe377b8 sp=0xc00fe37698 pc=0x30ecdf4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc00fe377e0 sp=0xc00fe377b8 pc=0x30ec08e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fe377e8 sp=0xc00fe377e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 5285 [select]:
   > runtime.gopark(0xc00ff67728?, 0x2?, 0x71?, 0xe6?, 0xc00ff676ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00ff67558 sp=0xc00ff67538 pc=0x13c9516
   > runtime.selectgo(0xc00ff67728, 0xc00ff676e8, 0xc0106018a0?, 0x0, 0x3041e97?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00ff67698 sp=0xc00ff67558 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc0119b30c0, {0x4134ba0, 0xc0113a58c0}, 0xc011d02090, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc00ff677a8 sp=0xc00ff67698 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc00ff677e0 sp=0xc00ff677a8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00ff677e8 sp=0xc00ff677e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 5350 [select]:
   > runtime.gopark(0xc010620f28?, 0x2?, 0xb8?, 0xd?, 0xc010620eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010620d58 sp=0xc010620d38 pc=0x13c9516
   > runtime.selectgo(0xc010620f28, 0xc010620ee8, 0x3b67af1?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010620e98 sp=0xc010620d58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc0114b8240, {0x4134ba0, 0xc0113a58c0}, 0xc0114a01a0, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc010620fa8 sp=0xc010620e98 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc010620fe0 sp=0xc010620fa8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010620fe8 sp=0xc010620fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 5291 [select]:
   > runtime.gopark(0xc00ff69f00?, 0x2?, 0x8?, 0x0?, 0xc00ff69e44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00ff69c48 sp=0xc00ff69c28 pc=0x13c9516
   > runtime.selectgo(0xc00ff69f00, 0xc00ff69e40, 0xc00ff69de8?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00ff69d88 sp=0xc00ff69c48 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc0119b34c0, {0x4134ba0, 0xc0113a58c0})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc00ff69f30 sp=0xc00ff69d88 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc0119b34c0, {0x4134ba0, 0xc0113a58c0}, 0xc011d020a0)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc00ff69fb0 sp=0xc00ff69f30 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc00ff69fe0 sp=0xc00ff69fb0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00ff69fe8 sp=0xc00ff69fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 5352 [semacquire]:
   > runtime.gopark(0x30ed008?, 0xc0106cef78?, 0x0?, 0x49?, 0x3b67af1?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0106cee90 sp=0xc0106cee70 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc0114a01a8, 0x0?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc0106ceef8 sp=0xc0106cee90 pc=0x13dae5e
   > sync.runtime_Semacquire(0x6036560?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc0106cef28 sp=0xc0106ceef8 pc=0x13f7f65
   > sync.(*WaitGroup).Wait(0xc0105fb280?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc0106cef50 sp=0xc0106cef28 pc=0x140b312
   > github.com/pingcap/tidb/executor.(*HashAggExec).waitPartialWorkerAndCloseOutputChs(0xc010d8e200, 0x13d0505?)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:815 +0x25 fp=0xc0106cef98 sp=0xc0106cef50 pc=0x2fbc465
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:844 +0x45 fp=0xc0106cefe0 sp=0xc0106cef98 pc=0x2fbcd85
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0106cefe8 sp=0xc0106cefe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:843 +0x2e5
   > goroutine 5302 [select]:
   > runtime.gopark(0xc0104c1f78?, 0x2?, 0x60?, 0x69?, 0xc0104c1eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0104c1d58 sp=0xc0104c1d38 pc=0x13c9516
   > runtime.selectgo(0xc0104c1f78, 0xc0104c1ee8, 0x3b67af1?, 0x0, 0xc011842370?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0104c1e98 sp=0xc0104c1d58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc00ff0d980, {0x40d68d0?, 0xc010546960?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc0104c1fb8 sp=0xc0104c1e98 pc=0x30ecdf4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc0104c1fe0 sp=0xc0104c1fb8 pc=0x30ec08e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0104c1fe8 sp=0xc0104c1fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b

### Scenario 1
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
 * Instruction #1:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
 * Instruction #2:
     - Instruction:  WITH cte_0 AS (select ref_0.wkey as c0, ref_0.pkey as c1, ref_0.c_rrbxh as c2, ...
     - Transaction: conn_0
     - Output: ERROR: 2013 (HY000): Lost connection to MySQL server during query
     - Executed order: Not executed
 * Instruction #3:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: ERROR: MySQL Connection not available.
     - Executed order: Not executed

 * Container logs:
   > [2024/07/02 13:51:02.465 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/07/02 13:51:02.468 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=32] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/02 13:51:02.468 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=32] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/02 13:51:02.470 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:66, Type:create schema, State:none, SchemaState:queueing, SchemaID:65, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 13:51:02.469 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 13:51:02.470 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:66, Type:create schema, State:none, SchemaState:queueing, SchemaID:65, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 13:51:02.469 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/02 13:51:02.470 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:create schema, State:none, SchemaState:queueing, SchemaID:65, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:51:02.469 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:51:02.471 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=32] [neededSchemaVersion=33] ["start time"=146.389µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 13:51:02.473 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=33] ["take time"=2.230121ms] [job="ID:66, Type:create schema, State:done, SchemaState:public, SchemaID:65, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 13:51:02.469 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:51:02.474 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:create schema, State:synced, SchemaState:public, SchemaID:65, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:51:02.469 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:51:02.475 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=66]
   > [2024/07/02 13:51:02.475 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 13:51:02.478 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=33] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_2el7jd`\n--\n\nDROP TABLE IF EXISTS `t_2el7jd`;"] [user=root@%]
   > [2024/07/02 13:51:02.478 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=33] [cur_db=testdb] [sql="CREATE TABLE `t_2el7jd` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_hzkgf` text DEFAULT NULL,\n  `c_si87c` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_alxrj` (`wkey`,`pkey`,`c_si87c`),\n  KEY `t_za4dpb` (`pkey`,`c_si87c`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/07/02 13:51:02.479 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:68, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:67, RowCount:0, ArgLen:1, start time: 2024-07-02 13:51:02.478 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 13:51:02.479 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:68, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:67, RowCount:0, ArgLen:1, start time: 2024-07-02 13:51:02.478 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_2el7jd` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_hzkgf` text DEFAULT NULL,\n  `c_si87c` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_alxrj` (`wkey`,`pkey`,`c_si87c`),\n  KEY `t_za4dpb` (`pkey`,`c_si87c`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/02 13:51:02.479 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:68, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:67, RowCount:0, ArgLen:0, start time: 2024-07-02 13:51:02.478 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:51:02.481 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=33] [neededSchemaVersion=34] ["start time"=458.093µs] [phyTblIDs="[67]"] [actionTypes="[8]"]
   > [2024/07/02 13:51:02.482 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=34] ["take time"=2.258059ms] [job="ID:68, Type:create table, State:done, SchemaState:public, SchemaID:65, TableID:67, RowCount:0, ArgLen:1, start time: 2024-07-02 13:51:02.478 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:51:02.483 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:68, Type:create table, State:synced, SchemaState:public, SchemaID:65, TableID:67, RowCount:0, ArgLen:0, start time: 2024-07-02 13:51:02.478 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:51:02.484 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=68]
   > [2024/07/02 13:51:02.484 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 13:51:02.484 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=60] ["first split key"=748000000000000043]
   > [2024/07/02 13:51:02.484 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=34] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_2el7jd` DISABLE KEYS */;"] [user=root@%]
   > [2024/07/02 13:51:02.487 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=62] ["first at"=748000000000000043] ["first new region left"="{Id:62 StartKey:7480000000000000ff3f00000000000000f8 EndKey:7480000000000000ff4300000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:63 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/02 13:51:02.487 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[62]"]
   > [2024/07/02 13:51:02.488 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=34] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_2el7jd` ENABLE KEYS */;"] [user=root@%]
   > [2024/07/02 13:51:02.488 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=34] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_p7c1bd`\n--\n\nDROP TABLE IF EXISTS `t_p7c1bd`;"] [user=root@%]
   > [2024/07/02 13:51:02.489 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=34] [cur_db=testdb] [sql="CREATE TABLE `t_p7c1bd` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_rrbxh` text DEFAULT NULL,\n  `c_c5cvkb` int(11) DEFAULT NULL,\n  `c_ag5ccc` int(11) DEFAULT NULL,\n  `c_qo4qvc` text DEFAULT NULL,\n  `c_lhs3h` int(11) DEFAULT NULL,\n  `c_8dah2b` int(11) DEFAULT NULL,\n  `c_eg6xsc` int(11) DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_s0z7f` (`c_ag5ccc`,`c_8dah2b`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/07/02 13:51:02.491 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:70, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:69, RowCount:0, ArgLen:1, start time: 2024-07-02 13:51:02.49 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 13:51:02.491 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:70, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:69, RowCount:0, ArgLen:1, start time: 2024-07-02 13:51:02.49 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_p7c1bd` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_rrbxh` text DEFAULT NULL,\n  `c_c5cvkb` int(11) DEFAULT NULL,\n  `c_ag5ccc` int(11) DEFAULT NULL,\n  `c_qo4qvc` text DEFAULT NULL,\n  `c_lhs3h` int(11) DEFAULT NULL,\n  `c_8dah2b` int(11) DEFAULT NULL,\n  `c_eg6xsc` int(11) DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_s0z7f` (`c_ag5ccc`,`c_8dah2b`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/02 13:51:02.492 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:70, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:69, RowCount:0, ArgLen:0, start time: 2024-07-02 13:51:02.49 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:51:02.494 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=34] [neededSchemaVersion=35] ["start time"=709.385µs] [phyTblIDs="[69]"] [actionTypes="[8]"]
   > [2024/07/02 13:51:02.496 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=35] ["take time"=2.545598ms] [job="ID:70, Type:create table, State:done, SchemaState:public, SchemaID:65, TableID:69, RowCount:0, ArgLen:1, start time: 2024-07-02 13:51:02.49 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:51:02.497 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:70, Type:create table, State:synced, SchemaState:public, SchemaID:65, TableID:69, RowCount:0, ArgLen:0, start time: 2024-07-02 13:51:02.49 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:51:02.499 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=70]
   > [2024/07/02 13:51:02.499 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 13:51:02.499 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=64] ["first split key"=748000000000000045]
   > [2024/07/02 13:51:02.500 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=64] ["first at"=748000000000000045] ["first new region left"="{Id:64 StartKey:7480000000000000ff4300000000000000f8 EndKey:7480000000000000ff4500000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:65 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/02 13:51:02.500 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[64]"]
   > [2024/07/02 13:51:02.500 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=35] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_p7c1bd` DISABLE KEYS */;"] [user=root@%]
   > [2024/07/02 13:51:02.506 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=35] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_p7c1bd` ENABLE KEYS */;"] [user=root@%]
   > [2024/07/02 13:51:03.535 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/07/02 13:51:03.547 +00:00] [INFO] [set.go:147] ["set global var"] [conn=407] [name=tx_isolation] [val=REPEATABLE-READ]
   > runtime: goroutine stack exceeds 1000000000-byte limit
   > runtime: sp=0xc0338e0378 stack=[0xc0338e0000, 0xc0538e0000]
   > fatal error: stack overflow
   > runtime stack:
   > runtime.throw({0x3b631a0?, 0x59e90a0?})
   > 	/usr/local/go/src/runtime/panic.go:1047 +0x5d fp=0x7f3c58581888 sp=0x7f3c58581858 pc=0x13c659d
   > runtime.newstack()
   > 	/usr/local/go/src/runtime/stack.go:1103 +0x5cc fp=0x7f3c58581a40 sp=0x7f3c58581888 pc=0x13e15ec
   > runtime.morestack()
   > 	/usr/local/go/src/runtime/asm_amd64.s:570 +0x8b fp=0x7f3c58581a48 sp=0x7f3c58581a40 pc=0x13fa60b
   > goroutine 6635 [running]:
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60?, 0xc01377ac60?}, {0x40dbf60?, 0xc01377b7a0?})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:183 +0x12c fp=0xc0338e0388 sp=0xc0338e0380 pc=0x1fb386c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e03c0 sp=0xc0338e0388 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e03f8 sp=0xc0338e03c0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0430 sp=0xc0338e03f8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0468 sp=0xc0338e0430 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e04a0 sp=0xc0338e0468 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e04d8 sp=0xc0338e04a0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0510 sp=0xc0338e04d8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0548 sp=0xc0338e0510 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0580 sp=0xc0338e0548 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e05b8 sp=0xc0338e0580 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e05f0 sp=0xc0338e05b8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0628 sp=0xc0338e05f0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0660 sp=0xc0338e0628 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0698 sp=0xc0338e0660 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e06d0 sp=0xc0338e0698 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0708 sp=0xc0338e06d0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0740 sp=0xc0338e0708 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0778 sp=0xc0338e0740 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e07b0 sp=0xc0338e0778 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e07e8 sp=0xc0338e07b0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0820 sp=0xc0338e07e8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0858 sp=0xc0338e0820 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0890 sp=0xc0338e0858 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e08c8 sp=0xc0338e0890 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0900 sp=0xc0338e08c8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0938 sp=0xc0338e0900 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0970 sp=0xc0338e0938 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e09a8 sp=0xc0338e0970 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e09e0 sp=0xc0338e09a8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0a18 sp=0xc0338e09e0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0a50 sp=0xc0338e0a18 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0a88 sp=0xc0338e0a50 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0ac0 sp=0xc0338e0a88 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0af8 sp=0xc0338e0ac0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0b30 sp=0xc0338e0af8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0b68 sp=0xc0338e0b30 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0ba0 sp=0xc0338e0b68 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0bd8 sp=0xc0338e0ba0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0c10 sp=0xc0338e0bd8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0c48 sp=0xc0338e0c10 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0c80 sp=0xc0338e0c48 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0cb8 sp=0xc0338e0c80 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0cf0 sp=0xc0338e0cb8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0d28 sp=0xc0338e0cf0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0d60 sp=0xc0338e0d28 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0d98 sp=0xc0338e0d60 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0dd0 sp=0xc0338e0d98 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0e08 sp=0xc0338e0dd0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0e40 sp=0xc0338e0e08 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0e78 sp=0xc0338e0e40 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0eb0 sp=0xc0338e0e78 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0ee8 sp=0xc0338e0eb0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0f20 sp=0xc0338e0ee8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0f58 sp=0xc0338e0f20 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0f90 sp=0xc0338e0f58 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e0fc8 sp=0xc0338e0f90 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e1000 sp=0xc0338e0fc8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e1038 sp=0xc0338e1000 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e1070 sp=0xc0338e1038 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e10a8 sp=0xc0338e1070 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e10e0 sp=0xc0338e10a8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e1118 sp=0xc0338e10e0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e1150 sp=0xc0338e1118 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e1188 sp=0xc0338e1150 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e11c0 sp=0xc0338e1188 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e11f8 sp=0xc0338e11c0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e1230 sp=0xc0338e11f8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e1268 sp=0xc0338e1230 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e12a0 sp=0xc0338e1268 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e12d8 sp=0xc0338e12a0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e1310 sp=0xc0338e12d8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e1348 sp=0xc0338e1310 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e1380 sp=0xc0338e1348 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e13b8 sp=0xc0338e1380 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e13f0 sp=0xc0338e13b8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e1428 sp=0xc0338e13f0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e1460 sp=0xc0338e1428 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e1498 sp=0xc0338e1460 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e14d0 sp=0xc0338e1498 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e1508 sp=0xc0338e14d0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e1540 sp=0xc0338e1508 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e1578 sp=0xc0338e1540 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e15b0 sp=0xc0338e1578 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e15e8 sp=0xc0338e15b0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e1620 sp=0xc0338e15e8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e1658 sp=0xc0338e1620 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e1690 sp=0xc0338e1658 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e16c8 sp=0xc0338e1690 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e1700 sp=0xc0338e16c8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e1738 sp=0xc0338e1700 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e1770 sp=0xc0338e1738 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e17a8 sp=0xc0338e1770 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e17e0 sp=0xc0338e17a8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e1818 sp=0xc0338e17e0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e1850 sp=0xc0338e1818 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e1888 sp=0xc0338e1850 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e18c0 sp=0xc0338e1888 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377ac60}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e18f8 sp=0xc0338e18c0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc01377acc0}, {0x40dbf60, 0xc01377b7a0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0338e1930 sp=0xc0338e18f8 pc=0x1fb3805
   > ...additional frames elided...
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:272 +0x67e
   > goroutine 1 [chan receive]:
   > runtime.gopark(0xc000d80280?, 0xc000ed3db0?, 0xbf?, 0xa1?, 0x38a15e0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000ed3d30 sp=0xc000ed3d10 pc=0x13c9516
   > runtime.chanrecv(0xc010fb79e0, 0xc000ed3e20, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000ed3dc0 sp=0xc000ed3d30 pc=0x13934bb
   > runtime.chanrecv1(0xc011778270?, 0x0?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc000ed3de8 sp=0xc000ed3dc0 pc=0x1392fb8
   > github.com/pingcap/tidb/server.(*Server).Run(0xc011778270)
   > 	/go/src/github.com/pingcap/tidb/server/server.go:365 +0x1f0 fp=0xc000ed3e40 sp=0xc000ed3de8 pc=0x3257ff0
   > main.main()
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:220 +0x5b9 fp=0xc000ed3f80 sp=0xc000ed3e40 pc=0x3438919
   > runtime.main()
   > 	/usr/local/go/src/runtime/proc.go:250 +0x212 fp=0xc000ed3fe0 sp=0xc000ed3f80 pc=0x13c9152
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000ed3fe8 sp=0xc000ed3fe0 pc=0x13fc6e1
   > goroutine 2 [force gc (idle)]:
   > runtime.gopark(0x0?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008efb0 sp=0xc00008ef90 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.forcegchelper()
   > 	/usr/local/go/src/runtime/proc.go:302 +0xad fp=0xc00008efe0 sp=0xc00008efb0 pc=0x13c93ad
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008efe8 sp=0xc00008efe0 pc=0x13fc6e1
   > created by runtime.init.6
   > 	/usr/local/go/src/runtime/proc.go:290 +0x25
   > goroutine 3 [GC sweep wait]:
   > runtime.gopark(0x1?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008f790 sp=0xc00008f770 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.bgsweep(0x0?)
   > 	/usr/local/go/src/runtime/mgcsweep.go:297 +0xd7 fp=0xc00008f7c8 sp=0xc00008f790 pc=0x13b2337
   > runtime.gcenable.func1()
   > 	/usr/local/go/src/runtime/mgc.go:178 +0x26 fp=0xc00008f7e0 sp=0xc00008f7c8 pc=0x13a6e06
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008f7e8 sp=0xc00008f7e0 pc=0x13fc6e1
   > created by runtime.gcenable
   > 	/usr/local/go/src/runtime/mgc.go:178 +0x6b
   > goroutine 4 [GC scavenge wait]:
   > runtime.gopark(0xc0000b8000?, 0x40acc30?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008ff70 sp=0xc00008ff50 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.(*scavengerState).park(0x60385e0)
   > 	/usr/local/go/src/runtime/mgcscavenge.go:389 +0x53 fp=0xc00008ffa0 sp=0xc00008ff70 pc=0x13b0313
   > runtime.bgscavenge(0x0?)
   > 	/usr/local/go/src/runtime/mgcscavenge.go:622 +0x65 fp=0xc00008ffc8 sp=0xc00008ffa0 pc=0x13b0925
   > runtime.gcenable.func2()
   > 	/usr/local/go/src/runtime/mgc.go:179 +0x26 fp=0xc00008ffe0 sp=0xc00008ffc8 pc=0x13a6da6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008ffe8 sp=0xc00008ffe0 pc=0x13fc6e1
   > created by runtime.gcenable
   > 	/usr/local/go/src/runtime/mgc.go:179 +0xaa
   > goroutine 18 [finalizer wait]:
   > runtime.gopark(0x6039860?, 0xc0001024e0?, 0x0?, 0x0?, 0xc00008e770?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008e628 sp=0xc00008e608 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.runfinq()
   > 	/usr/local/go/src/runtime/mfinal.go:180 +0x10f fp=0xc00008e7e0 sp=0xc00008e628 pc=0x13a5f0f
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008e7e8 sp=0xc00008e7e0 pc=0x13fc6e1
   > created by runtime.createfing
   > 	/usr/local/go/src/runtime/mfinal.go:157 +0x45
   > goroutine 19 [GC worker (idle)]:
   > runtime.gopark(0x0?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008a750 sp=0xc00008a730 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008a7e0 sp=0xc00008a750 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008a7e8 sp=0xc00008a7e0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 20 [GC worker (idle)]:
   > runtime.gopark(0x2657fb9fc915?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008af50 sp=0xc00008af30 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008afe0 sp=0xc00008af50 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008afe8 sp=0xc00008afe0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 5 [GC worker (idle)]:
   > runtime.gopark(0x2657fbcbbf74?, 0x1?, 0xdc?, 0x8?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000090750 sp=0xc000090730 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0000907e0 sp=0xc000090750 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000907e8 sp=0xc0000907e0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 34 [GC worker (idle)]:
   > runtime.gopark(0x2657fbcc437f?, 0x1?, 0xf4?, 0x16?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004aa750 sp=0xc0004aa730 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0004aa7e0 sp=0xc0004aa750 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004aa7e8 sp=0xc0004aa7e0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 35 [GC worker (idle)]:
   > runtime.gopark(0x2657fbcbf8be?, 0x1?, 0xb5?, 0x4a?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004aaf50 sp=0xc0004aaf30 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0004aafe0 sp=0xc0004aaf50 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004aafe8 sp=0xc0004aafe0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 36 [GC worker (idle)]:
   > runtime.gopark(0x2657fbcc48f4?, 0x1?, 0x60?, 0xa3?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004ab750 sp=0xc0004ab730 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0004ab7e0 sp=0xc0004ab750 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004ab7e8 sp=0xc0004ab7e0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 37 [GC worker (idle)]:
   > runtime.gopark(0x2657fbcbbf74?, 0x3?, 0x47?, 0x9?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004abf50 sp=0xc0004abf30 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0004abfe0 sp=0xc0004abf50 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004abfe8 sp=0xc0004abfe0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 6 [GC worker (idle)]:
   > runtime.gopark(0x2657fbcbed8f?, 0x3?, 0xc3?, 0xb7?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000090f50 sp=0xc000090f30 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc000090fe0 sp=0xc000090f50 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000090fe8 sp=0xc000090fe0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 7 [GC worker (idle)]:
   > runtime.gopark(0x2657fbcbe7d4?, 0x3?, 0x21?, 0x6a?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000091750 sp=0xc000091730 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0000917e0 sp=0xc000091750 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000917e8 sp=0xc0000917e0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 8 [GC worker (idle)]:
   > runtime.gopark(0x606d020?, 0x1?, 0x19?, 0x1d?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000091f50 sp=0xc000091f30 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc000091fe0 sp=0xc000091f50 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000091fe8 sp=0xc000091fe0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 21 [GC worker (idle)]:
   > runtime.gopark(0x2657fbcc48f4?, 0x3?, 0xa3?, 0x7?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008b750 sp=0xc00008b730 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008b7e0 sp=0xc00008b750 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008b7e8 sp=0xc00008b7e0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 38 [GC worker (idle)]:
   > runtime.gopark(0x2657fbcbbf74?, 0x3?, 0x2a?, 0x7?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004ac750 sp=0xc0004ac730 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0004ac7e0 sp=0xc0004ac750 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004ac7e8 sp=0xc0004ac7e0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 39 [GC worker (idle)]:
   > runtime.gopark(0x2657fbcc48f4?, 0x3?, 0xf5?, 0x85?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004acf50 sp=0xc0004acf30 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0004acfe0 sp=0xc0004acf50 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004acfe8 sp=0xc0004acfe0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 50 [GC worker (idle)]:
   > runtime.gopark(0x2657fbcc5f0d?, 0x3?, 0xa5?, 0x7b?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004a6750 sp=0xc0004a6730 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0004a67e0 sp=0xc0004a6750 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004a67e8 sp=0xc0004a67e0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 40 [GC worker (idle)]:
   > runtime.gopark(0x2657fbcbbf74?, 0x3?, 0xbc?, 0xe?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004ad750 sp=0xc0004ad730 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0004ad7e0 sp=0xc0004ad750 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004ad7e8 sp=0xc0004ad7e0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 9 [GC worker (idle)]:
   > runtime.gopark(0x2657fbcbbf74?, 0x1?, 0xa8?, 0xaa?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0000ca750 sp=0xc0000ca730 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0000ca7e0 sp=0xc0000ca750 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000ca7e8 sp=0xc0000ca7e0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 13 [select]:
   > runtime.gopark(0xc0004a9788?, 0x3?, 0xb8?, 0x6e?, 0xc0004a9772?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004a95f8 sp=0xc0004a95d8 pc=0x13c9516
   > runtime.selectgo(0xc0004a9788, 0xc0004a976c, 0xc0009af000?, 0x0, 0xc0004a9788?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0004a9738 sp=0xc0004a95f8 pc=0x13d9bdc
   > go.opencensus.io/stats/view.(*worker).start(0xc0009af000)
   > 	/go/pkg/mod/go.opencensus.io@v0.23.0/stats/view/worker.go:276 +0xad fp=0xc0004a97c8 sp=0xc0004a9738 pc=0x2b9244d
   > go.opencensus.io/stats/view.init.0.func1()
   > 	/go/pkg/mod/go.opencensus.io@v0.23.0/stats/view/worker.go:34 +0x26 fp=0xc0004a97e0 sp=0xc0004a97c8 pc=0x2b916c6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004a97e8 sp=0xc0004a97e0 pc=0x13fc6e1
   > created by go.opencensus.io/stats/view.init.0
   > 	/go/pkg/mod/go.opencensus.io@v0.23.0/stats/view/worker.go:34 +0x8d
   > goroutine 24 [chan receive]:
   > runtime.gopark(0xc0004a8ed8?, 0x13cf37b?, 0x20?, 0x8f?, 0x13e6de5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004a8ec8 sp=0xc0004a8ea8 pc=0x13c9516
   > runtime.chanrecv(0xc0004ee060, 0xc0004a8fa0, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc0004a8f58 sp=0xc0004a8ec8 pc=0x13934bb
   > runtime.chanrecv2(0x6fc23ac00?, 0x0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc0004a8f80 sp=0xc0004a8f58 pc=0x1392ff8
   > github.com/golang/glog.(*loggingT).flushDaemon(0x0?)
   > 	/go/pkg/mod/github.com/golang/glog@v1.0.0/glog.go:882 +0x6a fp=0xc0004a8fc8 sp=0xc0004a8f80 pc=0x2482faa
   > github.com/golang/glog.init.0.func1()
   > 	/go/pkg/mod/github.com/golang/glog@v1.0.0/glog.go:410 +0x26 fp=0xc0004a8fe0 sp=0xc0004a8fc8 pc=0x2480906
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004a8fe8 sp=0xc0004a8fe0 pc=0x13fc6e1
   > created by github.com/golang/glog.init.0
   > 	/go/pkg/mod/github.com/golang/glog@v1.0.0/glog.go:410 +0x1bf
   > goroutine 249 [select]:
   > runtime.gopark(0xc00009cf30?, 0x3?, 0x0?, 0x0?, 0xc00009cf0a?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00009cd90 sp=0xc00009cd70 pc=0x13c9516
   > runtime.selectgo(0xc00009cf30, 0xc00009cf04, 0x0?, 0x0, 0x3?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00009ced0 sp=0xc00009cd90 pc=0x13d9bdc
   > github.com/pingcap/tidb/util/cpuprofile.(*parallelCPUProfiler).profilingLoop(0xc0004418c0)
   > 	/go/src/github.com/pingcap/tidb/util/cpuprofile/cpuprofile.go:166 +0x105 fp=0xc00009cf78 sp=0xc00009ced0 pc=0x25951c5
   > github.com/pingcap/tidb/util/cpuprofile.(*parallelCPUProfiler).profilingLoop-fm()
   > 	<autogenerated>:1 +0x26 fp=0xc00009cf90 sp=0xc00009cf78 pc=0x2596e66
   > github.com/pingcap/tidb/util.WithRecovery(0x0?, 0xc000dc7d40?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc00009cfc0 sp=0xc00009cf90 pc=0x208e513
   > github.com/pingcap/tidb/util/cpuprofile.(*parallelCPUProfiler).start.func1()
   > 	/go/src/github.com/pingcap/tidb/util/cpuprofile/cpuprofile.go:113 +0x28 fp=0xc00009cfe0 sp=0xc00009cfc0 pc=0x2594da8
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00009cfe8 sp=0xc00009cfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/util/cpuprofile.(*parallelCPUProfiler).start
   > 	/go/src/github.com/pingcap/tidb/util/cpuprofile/cpuprofile.go:113 +0x176
   > goroutine 143 [chan receive]:
   > runtime.gopark(0xc000e94060?, 0x13cf374?, 0x38?, 0x3e?, 0x13e6de5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0000a3de0 sp=0xc0000a3dc0 pc=0x13c9516
   > runtime.chanrecv(0xc0004ee120, 0x0, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc0000a3e70 sp=0xc0000a3de0 pc=0x13934bb
   > runtime.chanrecv1(0x5f5e100?, 0x3b88785?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc0000a3e98 sp=0xc0000a3e70 pc=0x1392fb8
   > github.com/pingcap/tidb/util/systimemon.StartMonitor(0x3c82178, 0x3c817e0, 0xc000dca6b0)
   > 	/go/src/github.com/pingcap/tidb/util/systimemon/systime_mon.go:32 +0x185 fp=0xc0000a3fb8 sp=0xc0000a3e98 pc=0x3433bc5
   > main.setupMetrics.func3()
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:716 +0x31 fp=0xc0000a3fe0 sp=0xc0000a3fb8 pc=0x343c391
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000a3fe8 sp=0xc0000a3fe0 pc=0x13fc6e1
   > created by main.setupMetrics
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:716 +0x115
   > goroutine 144 [select]:
   > runtime.gopark(0xc0004a9f80?, 0x2?, 0x8?, 0x0?, 0xc0004a9f4c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004a9dd0 sp=0xc0004a9db0 pc=0x13c9516
   > runtime.selectgo(0xc0004a9f80, 0xc0004a9f48, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0004a9f10 sp=0xc0004a9dd0 pc=0x13d9bdc
   > github.com/pingcap/badger.(*DB).updateSize(0x0?, 0xc000dc4960)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/db.go:1039 +0x105 fp=0xc0004a9fc0 sp=0xc0004a9f10 pc=0x33233a5
   > github.com/pingcap/badger.Open.func5()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/db.go:328 +0x2a fp=0xc0004a9fe0 sp=0xc0004a9fc0 pc=0x331d46a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004a9fe8 sp=0xc0004a9fe0 pc=0x13fc6e1
   > created by github.com/pingcap/badger.Open
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/db.go:328 +0xf5c
   > goroutine 145 [select]:
   > runtime.gopark(0xc0004adf88?, 0x2?, 0x2?, 0x0?, 0xc0004adf64?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004adde8 sp=0xc0004addc8 pc=0x13c9516
   > runtime.selectgo(0xc0004adf88, 0xc0004adf60, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0004adf28 sp=0xc0004adde8 pc=0x13d9bdc
   > github.com/pingcap/badger/epoch.(*ResourceManager).collectLoop(0x0?, 0xc000dc4990)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/epoch/manager.go:101 +0xd3 fp=0xc0004adfc0 sp=0xc0004adf28 pc=0x3299693
   > github.com/pingcap/badger/epoch.NewResourceManager.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/epoch/manager.go:79 +0x2a fp=0xc0004adfe0 sp=0xc0004adfc0 pc=0x329942a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004adfe8 sp=0xc0004adfe0 pc=0x13fc6e1
   > created by github.com/pingcap/badger/epoch.NewResourceManager
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/epoch/manager.go:79 +0xdd
   > goroutine 258 [select]:
   > runtime.gopark(0xc000ebae68?, 0x2?, 0x8?, 0x71?, 0xc000ebae3c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000ebacc0 sp=0xc000ebaca0 pc=0x13c9516
   > runtime.selectgo(0xc000ebae68, 0xc000ebae38, 0x0?, 0x1, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000ebae00 sp=0xc000ebacc0 pc=0x13d9bdc
   > github.com/pingcap/badger.Open.func4()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/db.go:342 +0x155 fp=0xc000ebafe0 sp=0xc000ebae00 pc=0x331d3f5
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000ebafe8 sp=0xc000ebafe0 pc=0x13fc6e1
   > created by github.com/pingcap/badger.Open
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/db.go:339 +0x11f8
   > goroutine 274 [select]:
   > runtime.gopark(0xc0004a7708?, 0x2?, 0x0?, 0x0?, 0xc0004a76e4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004a7568 sp=0xc0004a7548 pc=0x13c9516
   > runtime.selectgo(0xc0004a7708, 0xc0004a76e0, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0004a76a8 sp=0xc0004a7568 pc=0x13d9bdc
   > github.com/pingcap/badger.(*blobGCHandler).run(0xc000d3e180, 0xc000012228)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/blob.go:468 +0xd6 fp=0xc0004a77c0 sp=0xc0004a76a8 pc=0x33117f6
   > github.com/pingcap/badger.(*blobManager).Open.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/blob.go:292 +0x2a fp=0xc0004a77e0 sp=0xc0004a77c0 pc=0x33104aa
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004a77e8 sp=0xc0004a77e0 pc=0x13fc6e1
   > created by github.com/pingcap/badger.(*blobManager).Open
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/blob.go:292 +0x5bd
   > goroutine 275 [select]:
   > runtime.gopark(0xc0004a7f60?, 0x2?, 0x4?, 0x30?, 0xc0004a7f2c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004a7d98 sp=0xc0004a7d78 pc=0x13c9516
   > runtime.selectgo(0xc0004a7f60, 0xc0004a7f28, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0004a7ed8 sp=0xc0004a7d98 pc=0x13d9bdc
   > github.com/pingcap/badger.(*levelsController).runWorker(0xc000dbc1c0, 0xc000012258, 0x0)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/levels.go:212 +0x1fb fp=0xc0004a7fb8 sp=0xc0004a7ed8 pc=0x332b8db
   > github.com/pingcap/badger.(*levelsController).startCompact.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/levels.go:180 +0x2e fp=0xc0004a7fe0 sp=0xc0004a7fb8 pc=0x332b6ae
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004a7fe8 sp=0xc0004a7fe0 pc=0x13fc6e1
   > created by github.com/pingcap/badger.(*levelsController).startCompact
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/levels.go:180 +0x65
   > goroutine 276 [select]:
   > runtime.gopark(0xc0004a8760?, 0x2?, 0x4?, 0x30?, 0xc0004a872c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004a8598 sp=0xc0004a8578 pc=0x13c9516
   > runtime.selectgo(0xc0004a8760, 0xc0004a8728, 0x0?, 0x0, 0xc0004a8701?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0004a86d8 sp=0xc0004a8598 pc=0x13d9bdc
   > github.com/pingcap/badger.(*levelsController).runWorker(0xc000dbc1c0, 0xc000012258, 0x0)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/levels.go:212 +0x1fb fp=0xc0004a87b8 sp=0xc0004a86d8 pc=0x332b8db
   > github.com/pingcap/badger.(*levelsController).startCompact.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/levels.go:180 +0x2e fp=0xc0004a87e0 sp=0xc0004a87b8 pc=0x332b6ae
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004a87e8 sp=0xc0004a87e0 pc=0x13fc6e1
   > created by github.com/pingcap/badger.(*levelsController).startCompact
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/levels.go:180 +0x65
   > goroutine 277 [select]:
   > runtime.gopark(0xc00008bf60?, 0x2?, 0x4?, 0x30?, 0xc00008bf2c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008bd98 sp=0xc00008bd78 pc=0x13c9516
   > runtime.selectgo(0xc00008bf60, 0xc00008bf28, 0x0?, 0x0, 0xf4240?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00008bed8 sp=0xc00008bd98 pc=0x13d9bdc
   > github.com/pingcap/badger.(*levelsController).runWorker(0xc000dbc1c0, 0xc000012258, 0x1)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/levels.go:212 +0x1fb fp=0xc00008bfb8 sp=0xc00008bed8 pc=0x332b8db
   > github.com/pingcap/badger.(*levelsController).startCompact.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/levels.go:180 +0x2e fp=0xc00008bfe0 sp=0xc00008bfb8 pc=0x332b6ae
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008bfe8 sp=0xc00008bfe0 pc=0x13fc6e1
   > created by github.com/pingcap/badger.(*levelsController).startCompact
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/levels.go:180 +0x65
   > goroutine 278 [chan receive]:
   > runtime.gopark(0x0?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00009eac0 sp=0xc00009eaa0 pc=0x13c9516
   > runtime.chanrecv(0xc000ddc960, 0xc00009ec60, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc00009eb50 sp=0xc00009eac0 pc=0x13934bb
   > runtime.chanrecv2(0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc00009eb78 sp=0xc00009eb50 pc=0x1392ff8
   > github.com/pingcap/badger.(*DB).runFlushMemTable(0xc000eb0000, 0x0?)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/db.go:920 +0xdd fp=0xc00009efc0 sp=0xc00009eb78 pc=0x3321e5d
   > github.com/pingcap/badger.Open.func6()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/db.go:361 +0x2a fp=0xc00009efe0 sp=0xc00009efc0 pc=0x331d26a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00009efe8 sp=0xc00009efe0 pc=0x13fc6e1
   > created by github.com/pingcap/badger.Open
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/db.go:361 +0x158d
   > goroutine 750 [select]:
   > runtime.gopark(0xc0000cc700?, 0x2?, 0x8?, 0x0?, 0xc0000cc644?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0000cc448 sp=0xc0000cc428 pc=0x13c9516
   > runtime.selectgo(0xc0000cc700, 0xc0000cc640, 0x1e9cc75?, 0x0, 0x40d6828?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0000cc588 sp=0xc0000cc448 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc011c29d80, {0x4134ba0, 0xc000560900})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc0000cc730 sp=0xc0000cc588 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc011c29d80, {0x4134ba0, 0xc000560900}, 0xc011e02480)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc0000cc7b0 sp=0xc0000cc730 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc0000cc7e0 sp=0xc0000cc7b0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000cc7e8 sp=0xc0000cc7e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 757 [select]:
   > runtime.gopark(0xc00059e778?, 0x2?, 0xb8?, 0x75?, 0xc00059e6ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00059e558 sp=0xc00059e538 pc=0x13c9516
   > runtime.selectgo(0xc00059e778, 0xc00059e6e8, 0x3b67af1?, 0x0, 0x40ee3a0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00059e698 sp=0xc00059e558 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc011d82980, {0x40d68d0?, 0xc011c4f170?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc00059e7b8 sp=0xc00059e698 pc=0x30ecdf4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc00059e7e0 sp=0xc00059e7b8 pc=0x30ec08e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00059e7e8 sp=0xc00059e7e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 259 [select]:
   > runtime.gopark(0xc00052ff78?, 0x3?, 0x25?, 0x28?, 0xc00052ff32?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00052fd98 sp=0xc00052fd78 pc=0x13c9516
   > runtime.selectgo(0xc00052ff78, 0xc00052ff2c, 0x1?, 0x0, 0xc000f411e0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00052fed8 sp=0xc00052fd98 pc=0x13d9bdc
   > github.com/pingcap/badger.(*writeWorker).runWriteVLog(0xc000f82080, 0xc0007b8180)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/writer.go:94 +0x137 fp=0xc00052ffc0 sp=0xc00052fed8 pc=0x333b817
   > github.com/pingcap/badger.startWriteWorker.func2()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/writer.go:64 +0x2a fp=0xc00052ffe0 sp=0xc00052ffc0 pc=0x333b2ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00052ffe8 sp=0xc00052ffe0 pc=0x13fc6e1
   > created by github.com/pingcap/badger.startWriteWorker
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/writer.go:64 +0x1f9
   > goroutine 260 [chan receive, locked to thread]:
   > runtime.gopark(0xc000eb4e98?, 0x1464528?, 0xf?, 0x0?, 0x1?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000eb4e68 sp=0xc000eb4e48 pc=0x13c9516
   > runtime.chanrecv(0xc0004ee660, 0xc000eb4f88, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000eb4ef8 sp=0xc000eb4e68 pc=0x13934bb
   > runtime.chanrecv2(0xc000e48d80?, 0x3f1591508ea791ef?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc000eb4f20 sp=0xc000eb4ef8 pc=0x1392ff8
   > github.com/pingcap/badger.(*writeWorker).runWriteLSM(0xc000f82080, 0x0?)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/writer.go:141 +0x15e fp=0xc000eb4fc0 sp=0xc000eb4f20 pc=0x333be5e
   > github.com/pingcap/badger.startWriteWorker.func3()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/writer.go:65 +0x2a fp=0xc000eb4fe0 sp=0xc000eb4fc0 pc=0x333b28a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000eb4fe8 sp=0xc000eb4fe0 pc=0x13fc6e1
   > created by github.com/pingcap/badger.startWriteWorker
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/writer.go:65 +0x24d
   > goroutine 261 [chan receive]:
   > runtime.gopark(0x0?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000eb8ea8 sp=0xc000eb8e88 pc=0x13c9516
   > runtime.chanrecv(0xc0004ee6c0, 0xc000eb8f88, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000eb8f38 sp=0xc000eb8ea8 pc=0x13934bb
   > runtime.chanrecv2(0xc0008ba0e0?, 0x0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc000eb8f60 sp=0xc000eb8f38 pc=0x1392ff8
   > github.com/pingcap/badger.(*writeWorker).runMergeLSM(0x0?, 0x0?)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/writer.go:154 +0x9b fp=0xc000eb8fc0 sp=0xc000eb8f60 pc=0x333bfdb
   > github.com/pingcap/badger.startWriteWorker.func4()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/writer.go:66 +0x2a fp=0xc000eb8fe0 sp=0xc000eb8fc0 pc=0x333b22a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000eb8fe8 sp=0xc000eb8fe0 pc=0x13fc6e1
   > created by github.com/pingcap/badger.startWriteWorker
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/writer.go:66 +0x2a5
   > goroutine 262 [select]:
   > runtime.gopark(0xc000eb5f88?, 0x2?, 0x0?, 0x0?, 0xc000eb5f4c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000eb5da0 sp=0xc000eb5d80 pc=0x13c9516
   > runtime.selectgo(0xc000eb5f88, 0xc000eb5f48, 0xc000015428?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000eb5ee0 sp=0xc000eb5da0 pc=0x13d9bdc
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.writeDBWorker.run({0xc0004ee780?, 0xc0001631c0?})
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:96 +0x145 fp=0xc000eb5fc0 sp=0xc000eb5ee0 pc=0x338c745
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*dbWriter).Open.func1()
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:202 +0x2a fp=0xc000eb5fe0 sp=0xc000eb5fc0 pc=0x338d2ca
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000eb5fe8 sp=0xc000eb5fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*dbWriter).Open
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:199 +0xc5
   > goroutine 263 [select]:
   > runtime.gopark(0xc000eb7e70?, 0x2?, 0x90?, 0x7e?, 0xc000eb7e1c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000eb7c58 sp=0xc000eb7c38 pc=0x13c9516
   > runtime.selectgo(0xc000eb7e70, 0xc000eb7e18, 0x13?, 0x0, 0xc010f90a80?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000eb7d98 sp=0xc000eb7c58 pc=0x13d9bdc
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.writeLockWorker.run({0xc0004ee7e0?, 0xc0001631c0?})
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:148 +0x15f fp=0xc000eb7fc0 sp=0xc000eb7d98 pc=0x338cd1f
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*dbWriter).Open.func2()
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:209 +0x2a fp=0xc000eb7fe0 sp=0xc000eb7fc0 pc=0x338d26a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000eb7fe8 sp=0xc000eb7fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*dbWriter).Open
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:206 +0x159
   > goroutine 264 [select]:
   > runtime.gopark(0xc0000caf18?, 0x2?, 0x0?, 0x0?, 0xc0000caf04?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0000cad88 sp=0xc0000cad68 pc=0x13c9516
   > runtime.selectgo(0xc0000caf18, 0xc0000caf00, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0000caec8 sp=0xc0000cad88 pc=0x13d9bdc
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*MVCCStore).runUpdateSafePointLoop(0xc000d68380)
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:1705 +0x217 fp=0xc0000cafc8 sp=0xc0000caec8 pc=0x337e3d7
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.NewMVCCStore.func1()
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:86 +0x26 fp=0xc0000cafe0 sp=0xc0000cafc8 pc=0x336f0a6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000cafe8 sp=0xc0000cafe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.NewMVCCStore
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:86 +0x337
   > goroutine 265 [select]:
   > runtime.gopark(0xc0000cb7b0?, 0x2?, 0x0?, 0x0?, 0xc0000cb79c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0000cb628 sp=0xc0000cb608 pc=0x13c9516
   > runtime.selectgo(0xc0000cb7b0, 0xc0000cb798, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0000cb768 sp=0xc0000cb628 pc=0x13d9bdc
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*MVCCStore).StartDeadlockDetection.func1()
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:1378 +0x7b fp=0xc0000cb7e0 sp=0xc0000cb768 pc=0x337b11b
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000cb7e8 sp=0xc0000cb7e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*MVCCStore).StartDeadlockDetection
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:1376 +0xb6
   > goroutine 266 [select]:
   > runtime.gopark(0xc000528f78?, 0x2?, 0x8?, 0x0?, 0xc000528f3c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000528dc0 sp=0xc000528da0 pc=0x13c9516
   > runtime.selectgo(0xc000528f78, 0xc000528f38, 0xc0000c87b0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000528f00 sp=0xc000528dc0 pc=0x13d9bdc
   > github.com/tikv/client-go/v2/oracle/oracles.(*pdOracle).updateTS(0xc000e4aa80, {0x40d6860, 0xc000120008}, 0x0?)
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.1-0.20220311043619-5042c6f2aaa6/oracle/oracles/pd.go:229 +0x128 fp=0xc000528fb0 sp=0xc000528f00 pc=0x1e576a8
   > github.com/tikv/client-go/v2/oracle/oracles.NewPdOracle.func1()
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.1-0.20220311043619-5042c6f2aaa6/oracle/oracles/pd.go:77 +0x32 fp=0xc000528fe0 sp=0xc000528fb0 pc=0x1e568d2
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000528fe8 sp=0xc000528fe0 pc=0x13fc6e1
   > created by github.com/tikv/client-go/v2/oracle/oracles.NewPdOracle
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.1-0.20220311043619-5042c6f2aaa6/oracle/oracles/pd.go:77 +0x119
   > goroutine 267 [select]:
   > runtime.gopark(0xc0000cdf78?, 0x3?, 0x0?, 0x0?, 0xc0000cdf5a?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0000cdde0 sp=0xc0000cddc0 pc=0x13c9516
   > runtime.selectgo(0xc0000cdf78, 0xc0000cdf54, 0x100020002?, 0x0, 0xc00043b3e8?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0000cdf20 sp=0xc0000cdde0 pc=0x13d9bdc
   > github.com/tikv/client-go/v2/internal/locate.(*RegionCache).asyncCheckAndResolveLoop(0xc000d68d00, 0xc0007b8180?)
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.1-0.20220311043619-5042c6f2aaa6/internal/locate/region_cache.go:423 +0xd1 fp=0xc0000cdfc0 sp=0xc0000cdf20 pc=0x1e25c11
   > github.com/tikv/client-go/v2/internal/locate.NewRegionCache.func1()
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.1-0.20220311043619-5042c6f2aaa6/internal/locate/region_cache.go:394 +0x2a fp=0xc0000cdfe0 sp=0xc0000cdfc0 pc=0x1e2588a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000cdfe8 sp=0xc0000cdfe0 pc=0x13fc6e1
   > created by github.com/tikv/client-go/v2/internal/locate.NewRegionCache
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.1-0.20220311043619-5042c6f2aaa6/internal/locate/region_cache.go:394 +0x2e6
   > goroutine 268 [select]:
   > runtime.gopark(0xc00009ff10?, 0x2?, 0x11?, 0x30?, 0xc00009feac?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00009fd10 sp=0xc00009fcf0 pc=0x13c9516
   > runtime.selectgo(0xc00009ff10, 0xc00009fea8, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00009fe50 sp=0xc00009fd10 pc=0x13d9bdc
   > github.com/tikv/client-go/v2/tikv.(*KVStore).runSafePointChecker(0xc000d40000)
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.1-0.20220311043619-5042c6f2aaa6/tikv/kv.go:234 +0x12b fp=0xc00009ffc8 sp=0xc00009fe50 pc=0x1e9a70b
   > github.com/tikv/client-go/v2/tikv.NewKVStore.func1()
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.1-0.20220311043619-5042c6f2aaa6/tikv/kv.go:189 +0x26 fp=0xc00009ffe0 sp=0xc00009ffc8 pc=0x1e9a506
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00009ffe8 sp=0xc00009ffe0 pc=0x13fc6e1
   > created by github.com/tikv/client-go/v2/tikv.NewKVStore
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.1-0.20220311043619-5042c6f2aaa6/tikv/kv.go:189 +0x416
   > goroutine 269 [select]:
   > runtime.gopark(0xc000f9ef80?, 0x2?, 0x20?, 0xd0?, 0xc000f9ef44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000f9edc8 sp=0xc000f9eda8 pc=0x13c9516
   > runtime.selectgo(0xc000f9ef80, 0xc000f9ef40, 0xc000372840?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000f9ef08 sp=0xc000f9edc8 pc=0x13d9bdc
   > github.com/tikv/client-go/v2/tikv.(*KVStore).safeTSUpdater(0xc000d40000)
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.1-0.20220311043619-5042c6f2aaa6/tikv/kv.go:521 +0x165 fp=0xc000f9efc8 sp=0xc000f9ef08 pc=0x1e9c6e5
   > github.com/tikv/client-go/v2/tikv.NewKVStore.func2()
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.1-0.20220311043619-5042c6f2aaa6/tikv/kv.go:190 +0x26 fp=0xc000f9efe0 sp=0xc000f9efc8 pc=0x1e9a4a6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000f9efe8 sp=0xc000f9efe0 pc=0x13fc6e1
   > created by github.com/tikv/client-go/v2/tikv.NewKVStore
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.1-0.20220311043619-5042c6f2aaa6/tikv/kv.go:190 +0x456
   > goroutine 270 [select]:
   > runtime.gopark(0xc0005a2798?, 0x2?, 0x0?, 0x0?, 0xc0005a276c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0005a25e8 sp=0xc0005a25c8 pc=0x13c9516
   > runtime.selectgo(0xc0005a2798, 0xc0005a2768, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0005a2728 sp=0xc0005a25e8 pc=0x13d9bdc
   > github.com/dgraph-io/ristretto.(*defaultPolicy).processItems(0xc000d8e080)
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.1.0/policy.go:102 +0x91 fp=0xc0005a27c8 sp=0xc0005a2728 pc=0x248a7b1
   > github.com/dgraph-io/ristretto.newDefaultPolicy.func1()
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.1.0/policy.go:86 +0x26 fp=0xc0005a27e0 sp=0xc0005a27c8 pc=0x248a666
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0005a27e8 sp=0xc0005a27e0 pc=0x13fc6e1
   > created by github.com/dgraph-io/ristretto.newDefaultPolicy
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.1.0/policy.go:86 +0x156
   > goroutine 271 [select]:
   > runtime.gopark(0xc0005a2f88?, 0x3?, 0x8?, 0x71?, 0xc0005a2f32?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0005a2da8 sp=0xc0005a2d88 pc=0x13c9516
   > runtime.selectgo(0xc0005a2f88, 0xc0005a2f2c, 0xc000d8e080?, 0x0, 0x1?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0005a2ee8 sp=0xc0005a2da8 pc=0x13d9bdc
   > github.com/dgraph-io/ristretto.(*Cache).processItems(0xc000d68d80)
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.1.0/cache.go:452 +0x15e fp=0xc0005a2fc8 sp=0xc0005a2ee8 pc=0x2488cfe
   > github.com/dgraph-io/ristretto.NewCache.func5()
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.1.0/cache.go:207 +0x26 fp=0xc0005a2fe0 sp=0xc0005a2fc8 pc=0x2487da6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0005a2fe8 sp=0xc0005a2fe0 pc=0x13fc6e1
   > created by github.com/dgraph-io/ristretto.NewCache
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.1.0/cache.go:207 +0x6a5
   > goroutine 607 [chan receive]:
   > runtime.gopark(0x606d020?, 0xc00059ef20?, 0x28?, 0xa3?, 0x139805d?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00059eea0 sp=0xc00059ee80 pc=0x13c9516
   > runtime.chanrecv(0xc0117708a0, 0xc00059efa0, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc00059ef30 sp=0xc00059eea0 pc=0x13934bb
   > runtime.chanrecv1(0x0?, 0x2610c40?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc00059ef58 sp=0xc00059ef30 pc=0x1392fb8
   > github.com/pingcap/tidb/util/signal.SetupSignalHandler.func1()
   > 	/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:38 +0x4f fp=0xc00059efe0 sp=0xc00059ef58 pc=0x343388f
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00059efe8 sp=0xc00059efe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/util/signal.SetupSignalHandler
   > 	/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:35 +0xb6
   > goroutine 6680 [semacquire]:
   > runtime.gopark(0x9469a691?, 0xc1991f5214f85217?, 0x60?, 0x4c?, 0xc000572060?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc011e46ed8 sp=0xc011e46eb8 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc0138021b8, 0xc0?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc011e46f40 sp=0xc011e46ed8 pc=0x13dae5e
   > sync.runtime_Semacquire(0xc1991f5214f84544?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc011e46f70 sp=0xc011e46f40 pc=0x13f7f65
   > sync.(*WaitGroup).Wait(0xc011e46fd0?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc011e46f98 sp=0xc011e46f70 pc=0x140b312
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:856 +0x45 fp=0xc011e46fe0 sp=0xc011e46f98 pc=0x2fbcc85
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc011e46fe8 sp=0xc011e46fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:855 +0x4c5
   > goroutine 518 [select]:
   > runtime.gopark(0xc00fda1f38?, 0x2?, 0x5?, 0x0?, 0xc00fda1efc?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fda1d50 sp=0xc00fda1d30 pc=0x13c9516
   > runtime.selectgo(0xc00fda1f38, 0xc00fda1ef8, 0x1?, 0x0, 0x2?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fda1e90 sp=0xc00fda1d50 pc=0x13d9bdc
   > github.com/pingcap/tidb/ddl.(*ddl).limitDDLJobs(0xc010bdb180)
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl_worker.go:269 +0x173 fp=0xc00fda1fc8 sp=0xc00fda1e90 pc=0x2717a13
   > github.com/pingcap/tidb/ddl.(*ddl).Start.func2()
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:381 +0x26 fp=0xc00fda1fe0 sp=0xc00fda1fc8 pc=0x26d42c6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fda1fe8 sp=0xc00fda1fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/ddl.(*ddl).Start
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:381 +0x2aa
   > goroutine 6624 [select]:
   > runtime.gopark(0xc0127ec700?, 0x2?, 0x60?, 0xbf?, 0xc0127ec644?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0127ec448 sp=0xc0127ec428 pc=0x13c9516
   > runtime.selectgo(0xc0127ec700, 0xc0127ec640, 0xc0127ec5e8?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0127ec588 sp=0xc0127ec448 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc01367a300, {0x4134ba0, 0xc000560900})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc0127ec730 sp=0xc0127ec588 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc01367a300, {0x4134ba0, 0xc000560900}, 0xc01346f6f0)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc0127ec7b0 sp=0xc0127ec730 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc0127ec7e0 sp=0xc0127ec7b0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0127ec7e8 sp=0xc0127ec7e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 606 [syscall]:
   > runtime.notetsleepg(0x13d0505?, 0xc010355a40?)
   > 	/usr/local/go/src/runtime/lock_futex.go:236 +0x34 fp=0xc0000ccfa0 sp=0xc0000ccf68 pc=0x1398cd4
   > os/signal.signal_recv()
   > 	/usr/local/go/src/runtime/sigqueue.go:152 +0x2f fp=0xc0000ccfc0 sp=0xc0000ccfa0 pc=0x13f86cf
   > os/signal.loop()
   > 	/usr/local/go/src/os/signal/signal_unix.go:23 +0x19 fp=0xc0000ccfe0 sp=0xc0000ccfc0 pc=0x2ecc1f9
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000ccfe8 sp=0xc0000ccfe0 pc=0x13fc6e1
   > created by os/signal.Notify.func1.1
   > 	/usr/local/go/src/os/signal/signal.go:151 +0x2a
   > goroutine 584 [select]:
   > runtime.gopark(0xc00053ad38?, 0x2?, 0x4?, 0x0?, 0xc00053ad24?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00053abb0 sp=0xc00053ab90 pc=0x13c9516
   > runtime.selectgo(0xc00053ad38, 0xc00053ad20, 0xc00053ad01?, 0x0, 0x139a507?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00053acf0 sp=0xc00053abb0 pc=0x13d9bdc
   > github.com/soheilhy/cmux.muxListener.Accept(...)
   > 	/go/pkg/mod/github.com/soheilhy/cmux@v0.1.5/cmux.go:262
   > github.com/soheilhy/cmux.(*muxListener).Accept(0x59083d0?)
   > 	<autogenerated>:1 +0x7e fp=0xc00053ad68 sp=0xc00053acf0 pc=0x31ece5e
   > net/http.(*onceCloseListener).Accept(0x40d6860?)
   > 	<autogenerated>:1 +0x2a fp=0xc00053ad80 sp=0xc00053ad68 pc=0x16ee8ea
   > net/http.(*Server).Serve(0xc0116000f0, {0x40d5e60, 0xc01167e1e0})
   > 	/usr/local/go/src/net/http/server.go:3070 +0x385 fp=0xc00053aeb0 sp=0xc00053ad80 pc=0x16c4bc5
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer.func2()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:469 +0x37 fp=0xc00053af90 sp=0xc00053aeb0 pc=0x32500f7
   > github.com/pingcap/tidb/util.WithRecovery(0x40d6860?, 0xc000120008?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc00053afc0 sp=0xc00053af90 pc=0x208e513
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer.func6()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:468 +0x28 fp=0xc00053afe0 sp=0xc00053afc0 pc=0x3250088
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00053afe8 sp=0xc00053afe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:468 +0x4ea
   > goroutine 752 [select]:
   > runtime.gopark(0xc01135df00?, 0x2?, 0x60?, 0x68?, 0xc01135de44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01135dc48 sp=0xc01135dc28 pc=0x13c9516
   > runtime.selectgo(0xc01135df00, 0xc01135de40, 0x375f940?, 0x0, 0x203004?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01135dd88 sp=0xc01135dc48 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc011c29f00, {0x4134ba0, 0xc000560900})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc01135df30 sp=0xc01135dd88 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc011c29f00, {0x4134ba0, 0xc000560900}, 0xc011e02480)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc01135dfb0 sp=0xc01135df30 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc01135dfe0 sp=0xc01135dfb0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01135dfe8 sp=0xc01135dfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 520 [select]:
   > runtime.gopark(0xc010e15f58?, 0x4?, 0xab?, 0x42?, 0xc010e15da8?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010e15bf8 sp=0xc010e15bd8 pc=0x13c9516
   > runtime.selectgo(0xc010e15f58, 0xc010e15da0, 0xc000541e38?, 0x0, 0x1?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010e15d38 sp=0xc010e15bf8 pc=0x13d9bdc
   > github.com/pingcap/tidb/ddl.(*worker).start(0xc010f426c0, 0xc01089eb60)
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl_worker.go:184 +0x318 fp=0xc010e15fc0 sp=0xc010e15d38 pc=0x27168b8
   > github.com/pingcap/tidb/ddl.(*ddl).Start.func3()
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:399 +0x2a fp=0xc010e15fe0 sp=0xc010e15fc0 pc=0x26d426a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010e15fe8 sp=0xc010e15fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/ddl.(*ddl).Start
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:399 +0x58e
   > goroutine 6622 [select]:
   > runtime.gopark(0xc012698f00?, 0x2?, 0x8?, 0x0?, 0xc012698e44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc012698c48 sp=0xc012698c28 pc=0x13c9516
   > runtime.selectgo(0xc012698f00, 0xc012698e40, 0x60384e0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc012698d88 sp=0xc012698c48 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc01367a180, {0x4134ba0, 0xc000560900})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc012698f30 sp=0xc012698d88 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc01367a180, {0x4134ba0, 0xc000560900}, 0xc01346f6f0)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc012698fb0 sp=0xc012698f30 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc012698fe0 sp=0xc012698fb0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc012698fe8 sp=0xc012698fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 524 [select]:
   > runtime.gopark(0xc010e11f50?, 0x4?, 0x10?, 0x0?, 0xc010e11d00?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010e11b78 sp=0xc010e11b58 pc=0x13c9516
   > runtime.selectgo(0xc010e11f50, 0xc010e11cf8, 0x203004?, 0x0, 0x203004?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010e11cb8 sp=0xc010e11b78 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).loadSchemaInLoop(0xc0108952c0, {0x40d6828, 0xc010be0ec0}, 0xc00059fd00?)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:593 +0x1aa fp=0xc010e11fb0 sp=0xc010e11cb8 pc=0x2790e2a
   > github.com/pingcap/tidb/domain.(*Domain).Init.func10()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:864 +0x32 fp=0xc010e11fe0 sp=0xc010e11fb0 pc=0x27939f2
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010e11fe8 sp=0xc010e11fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:864 +0xe6b
   > goroutine 770 [semacquire]:
   > runtime.gopark(0x40ee3a0?, 0xc0005deec0?, 0x0?, 0x78?, 0xc011360fd0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc011360eb8 sp=0xc011360e98 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc011e02468, 0x60?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc011360f20 sp=0xc011360eb8 pc=0x13dae5e
   > sync.runtime_Semacquire(0xc01180a680?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc011360f50 sp=0xc011360f20 pc=0x13f7f65
   > sync.(*WaitGroup).Wait(0xc0119f8640?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc011360f78 sp=0xc011360f50 pc=0x140b312
   > github.com/pingcap/tidb/executor.(*HashAggExec).waitAllWorkersAndCloseFinalOutputCh(0xc010e21200, {0xc011360fb8, 0x3, 0x30ec08e?})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:827 +0x35 fp=0xc011360f98 sp=0xc011360f78 pc=0x2fbc5b5
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func6()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:864 +0x5a fp=0xc011360fe0 sp=0xc011360f98 pc=0x2fbcc1a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc011360fe8 sp=0xc011360fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:864 +0x54d
   > goroutine 745 [select]:
   > runtime.gopark(0xc011360728?, 0x2?, 0x8?, 0x0?, 0xc0113606ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc011360558 sp=0xc011360538 pc=0x13c9516
   > runtime.selectgo(0xc011360728, 0xc0113606e8, 0x40d91e0?, 0x0, 0xc00057a300?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc011360698 sp=0xc011360558 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc011c29a40, {0x4134ba0, 0xc000560900}, 0xc011e02470, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc0113607a8 sp=0xc011360698 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc0113607e0 sp=0xc0113607a8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0113607e8 sp=0xc0113607e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 62 [chan receive]:
   > runtime.gopark(0x0?, 0x142b1f1?, 0x98?, 0x16?, 0x1e8bd97?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0005a1660 sp=0xc0005a1640 pc=0x13c9516
   > runtime.chanrecv(0xc0116a6b40, 0xc0005a1780, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc0005a16f0 sp=0xc0005a1660 pc=0x13934bb
   > runtime.chanrecv1(0xc0008bb300?, 0x0?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc0005a1718 sp=0xc0005a16f0 pc=0x1392fb8
   > github.com/pingcap/tidb/util/signal.SetupSignalHandler.func2()
   > 	/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:54 +0x45 fp=0xc0005a17e0 sp=0xc0005a1718 pc=0x3433665
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0005a17e8 sp=0xc0005a17e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/util/signal.SetupSignalHandler
   > 	/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:53 +0x19f
   > goroutine 523 [select]:
   > runtime.gopark(0xc01241dde8?, 0x2?, 0x4?, 0x30?, 0xc01241dd4c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01241dbd0 sp=0xc01241dbb0 pc=0x13c9516
   > runtime.selectgo(0xc01241dde8, 0xc01241dd48, 0xc01258a900?, 0x0, 0xc0005a3da8?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01241dd10 sp=0xc01241dbd0 pc=0x13d9bdc
   > github.com/pingcap/tidb/ddl.(*ddl).PollTiFlashRoutine(0xc010bdb180)
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl_tiflash_api.go:577 +0x273 fp=0xc01241df98 sp=0xc01241dd10 pc=0x27159b3
   > github.com/pingcap/tidb/ddl.(*ddl).PollTiFlashRoutine-fm()
   > 	<autogenerated>:1 +0x26 fp=0xc01241dfb0 sp=0xc01241df98 pc=0x2768c06
   > github.com/pingcap/tidb/util.(*WaitGroupWrapper).Run.func1()
   > 	/go/src/github.com/pingcap/tidb/util/wait_group_wrapper.go:33 +0x5a fp=0xc01241dfe0 sp=0xc01241dfb0 pc=0x209361a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01241dfe8 sp=0xc01241dfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/util.(*WaitGroupWrapper).Run
   > 	/go/src/github.com/pingcap/tidb/util/wait_group_wrapper.go:31 +0x85
   > goroutine 747 [semacquire]:
   > runtime.gopark(0xc011552600?, 0xc011a73e60?, 0x60?, 0x4f?, 0x1?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01135d690 sp=0xc01135d670 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc011e02478, 0x1?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc01135d6f8 sp=0xc01135d690 pc=0x13dae5e
   > sync.runtime_Semacquire(0x303000000000000?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc01135d728 sp=0xc01135d6f8 pc=0x13f7f65
   > sync.(*WaitGroup).Wait(0x0?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc01135d750 sp=0xc01135d728 pc=0x140b312
   > github.com/pingcap/tidb/executor.(*HashAggExec).waitPartialWorkerAndCloseOutputChs(0xc010e21200, 0x1e81d60?)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:815 +0x25 fp=0xc01135d798 sp=0xc01135d750 pc=0x2fbc465
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:844 +0x45 fp=0xc01135d7e0 sp=0xc01135d798 pc=0x2fbcd85
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01135d7e8 sp=0xc01135d7e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:843 +0x2e5
   > goroutine 6681 [semacquire]:
   > runtime.gopark(0xc011924708?, 0xc000580801?, 0x20?, 0xb3?, 0x13fa50e?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0119246b8 sp=0xc011924698 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc013802198, 0x80?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc011924720 sp=0xc0119246b8 pc=0x13dae5e
   > sync.runtime_Semacquire(0xc013630a40?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc011924750 sp=0xc011924720 pc=0x13f7f65
   > sync.(*WaitGroup).Wait(0x946a1be1?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc011924778 sp=0xc011924750 pc=0x140b312
   > github.com/pingcap/tidb/executor.(*HashAggExec).waitAllWorkersAndCloseFinalOutputCh(0xc010e20e00, {0xc0119247b8, 0x3, 0x4134ba0?})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:827 +0x35 fp=0xc011924798 sp=0xc011924778 pc=0x2fbc5b5
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func6()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:864 +0x5a fp=0xc0119247e0 sp=0xc011924798 pc=0x2fbcc1a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0119247e8 sp=0xc0119247e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:864 +0x54d
   > goroutine 748 [select]:
   > runtime.gopark(0xc00059df00?, 0x2?, 0xe0?, 0xa0?, 0xc00059de44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00059dc48 sp=0xc00059dc28 pc=0x13c9516
   > runtime.selectgo(0xc00059df00, 0xc00059de40, 0xc000d02840?, 0x0, 0x12?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00059dd88 sp=0xc00059dc48 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc011c29c00, {0x4134ba0, 0xc000560900})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc00059df30 sp=0xc00059dd88 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc011c29c00, {0x4134ba0, 0xc000560900}, 0xc011e02480)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc00059dfb0 sp=0xc00059df30 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc00059dfe0 sp=0xc00059dfb0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00059dfe8 sp=0xc00059dfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 751 [select]:
   > runtime.gopark(0xc0000c8700?, 0x2?, 0x0?, 0x30?, 0xc0000c8644?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0000c8448 sp=0xc0000c8428 pc=0x13c9516
   > runtime.selectgo(0xc0000c8700, 0xc0000c8640, 0x13c9516?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0000c8588 sp=0xc0000c8448 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc011c29e40, {0x4134ba0, 0xc000560900})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc0000c8730 sp=0xc0000c8588 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc011c29e40, {0x4134ba0, 0xc000560900}, 0xc011e02480)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc0000c87b0 sp=0xc0000c8730 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc0000c87e0 sp=0xc0000c87b0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000c87e8 sp=0xc0000c87e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 746 [select]:
   > runtime.gopark(0xc01135cf28?, 0x2?, 0x28?, 0x93?, 0xc01135ceec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01135cd58 sp=0xc01135cd38 pc=0x13c9516
   > runtime.selectgo(0xc01135cf28, 0xc01135cee8, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01135ce98 sp=0xc01135cd58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc011c29b00, {0x4134ba0, 0xc000560900}, 0xc011e02470, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc01135cfa8 sp=0xc01135ce98 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc01135cfe0 sp=0xc01135cfa8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01135cfe8 sp=0xc01135cfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 618 [select]:
   > runtime.gopark(0xc000d4dd48?, 0x2?, 0x40?, 0x1d?, 0xc000d4dc94?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000d4db08 sp=0xc000d4dae8 pc=0x13c9516
   > runtime.selectgo(0xc000d4dd48, 0xc000d4dc90, 0x60384e0?, 0x0, 0x1?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000d4dc48 sp=0xc000d4db08 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).loadStatsWorker(0xc0108952c0)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1359 +0x485 fp=0xc000d4dfc8 sp=0xc000d4dc48 pc=0x2797fe5
   > github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1292 +0x26 fp=0xc000d4dfe0 sp=0xc000d4dfc8 pc=0x2797566
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000d4dfe8 sp=0xc000d4dfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1292 +0x10a
   > goroutine 583 [select]:
   > runtime.gopark(0xc00053fd68?, 0x2?, 0xdc?, 0x2a?, 0xc00053fd54?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00053fbe0 sp=0xc00053fbc0 pc=0x13c9516
   > runtime.selectgo(0xc00053fd68, 0xc00053fd50, 0xc000536680?, 0x0, 0xc00053fd88?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00053fd20 sp=0xc00053fbe0 pc=0x13d9bdc
   > github.com/soheilhy/cmux.muxListener.Accept(...)
   > 	/go/pkg/mod/github.com/soheilhy/cmux@v0.1.5/cmux.go:262
   > github.com/soheilhy/cmux.(*muxListener).Accept(0x40ba820?)
   > 	<autogenerated>:1 +0x7e fp=0xc00053fd98 sp=0xc00053fd20 pc=0x31ece5e
   > google.golang.org/grpc.(*Server).Serve(0xc01164c540, {0x40d5e60, 0xc01167e200})
   > 	/go/pkg/mod/google.golang.org/grpc@v1.44.0/server.go:779 +0x362 fp=0xc00053feb0 sp=0xc00053fd98 pc=0x199d262
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer.func1()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:464 +0x37 fp=0xc00053ff90 sp=0xc00053feb0 pc=0x3250357
   > github.com/pingcap/tidb/util.WithRecovery(0x40d6860?, 0xc010eb9d40?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc00053ffc0 sp=0xc00053ff90 pc=0x208e513
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer.func5()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:463 +0x28 fp=0xc00053ffe0 sp=0xc00053ffc0 pc=0x32502e8
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00053ffe8 sp=0xc00053ffe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:463 +0x438
   > goroutine 753 [semacquire]:
   > runtime.gopark(0xc01135f700?, 0x140b312?, 0xa0?, 0x88?, 0x2?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01135f6d8 sp=0xc01135f6b8 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc011e02488, 0x1?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc01135f740 sp=0xc01135f6d8 pc=0x13dae5e
   > sync.runtime_Semacquire(0xc010fdccb0?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc01135f770 sp=0xc01135f740 pc=0x13f7f65
   > sync.(*WaitGroup).Wait(0xc010fb7b60?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc01135f798 sp=0xc01135f770 pc=0x140b312
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:856 +0x45 fp=0xc01135f7e0 sp=0xc01135f798 pc=0x2fbcc85
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01135f7e8 sp=0xc01135f7e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:855 +0x4c5
   > goroutine 6619 [semacquire]:
   > runtime.gopark(0x2fb8f3f?, 0xc01269bf28?, 0x80?, 0x61?, 0x60384e0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01269be90 sp=0xc01269be70 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc01346f6e8, 0x0?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc01269bef8 sp=0xc01269be90 pc=0x13dae5e
   > sync.runtime_Semacquire(0xc01320bbc0?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc01269bf28 sp=0xc01269bef8 pc=0x13f7f65
   > sync.(*WaitGroup).Wait(0xc01359b000?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc01269bf50 sp=0xc01269bf28 pc=0x140b312
   > github.com/pingcap/tidb/executor.(*HashAggExec).waitPartialWorkerAndCloseOutputChs(0xc010e21000, 0x13d0505?)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:815 +0x25 fp=0xc01269bf98 sp=0xc01269bf50 pc=0x2fbc465
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:844 +0x45 fp=0xc01269bfe0 sp=0xc01269bf98 pc=0x2fbcd85
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01269bfe8 sp=0xc01269bfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:843 +0x2e5
   > goroutine 749 [select]:
   > runtime.gopark(0xc0000c6f00?, 0x2?, 0x65?, 0x54?, 0xc0000c6e44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0000c6c48 sp=0xc0000c6c28 pc=0x13c9516
   > runtime.selectgo(0xc0000c6f00, 0xc0000c6e40, 0x1d0c5f18?, 0x0, 0x13af425?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0000c6d88 sp=0xc0000c6c48 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc011c29cc0, {0x4134ba0, 0xc000560900})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc0000c6f30 sp=0xc0000c6d88 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc011c29cc0, {0x4134ba0, 0xc000560900}, 0xc011e02480)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc0000c6fb0 sp=0xc0000c6f30 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc0000c6fe0 sp=0xc0000c6fb0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000c6fe8 sp=0xc0000c6fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 519 [select]:
   > runtime.gopark(0xc000ebbf90?, 0x2?, 0x0?, 0x0?, 0xc000ebbf6c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000ebbdf0 sp=0xc000ebbdd0 pc=0x13c9516
   > runtime.selectgo(0xc000ebbf90, 0xc000ebbf68, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000ebbf30 sp=0xc000ebbdf0 pc=0x13d9bdc
   > github.com/pingcap/tidb/ddl.(*delRange).startEmulator(0xc010f47d40)
   > 	/go/src/github.com/pingcap/tidb/ddl/delete_range.go:140 +0x125 fp=0xc000ebbfc8 sp=0xc000ebbf30 pc=0x271fb25
   > github.com/pingcap/tidb/ddl.(*delRange).start.func1()
   > 	/go/src/github.com/pingcap/tidb/ddl/delete_range.go:122 +0x26 fp=0xc000ebbfe0 sp=0xc000ebbfc8 pc=0x271f8e6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000ebbfe8 sp=0xc000ebbfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/ddl.(*delRange).start
   > 	/go/src/github.com/pingcap/tidb/ddl/delete_range.go:122 +0x6d
   > goroutine 6616 [select]:
   > runtime.gopark(0xc01264a728?, 0x2?, 0xdc?, 0xad?, 0xc01264a6ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01264a558 sp=0xc01264a538 pc=0x13c9516
   > runtime.selectgo(0xc01264a728, 0xc01264a6e8, 0x60384e0?, 0x0, 0xc0127427b0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01264a698 sp=0xc01264a558 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc01343bd80, {0x4134ba0, 0xc000560900}, 0xc01346f6e0, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc01264a7a8 sp=0xc01264a698 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc01264a7e0 sp=0xc01264a7a8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01264a7e8 sp=0xc01264a7e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 63 [select]:
   > runtime.gopark(0xc0005a3f80?, 0x3?, 0x40?, 0x0?, 0xc0005a3f42?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0005a3dc8 sp=0xc0005a3da8 pc=0x13c9516
   > runtime.selectgo(0xc0005a3f80, 0xc0005a3f3c, 0x2757893?, 0x0, 0xc010086360?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0005a3f08 sp=0xc0005a3dc8 pc=0x13d9bdc
   > github.com/pingcap/tidb/util/topsql/collector.(*SQLCPUCollector).collectSQLCPULoop(0xc0000c5270)
   > 	/go/src/github.com/pingcap/tidb/util/topsql/collector/cpu.go:121 +0x1a5 fp=0xc0005a3fc8 sp=0xc0005a3f08 pc=0x25974a5
   > github.com/pingcap/tidb/util/topsql/collector.(*SQLCPUCollector).Start.func1()
   > 	/go/src/github.com/pingcap/tidb/util/topsql/collector/cpu.go:83 +0x26 fp=0xc0005a3fe0 sp=0xc0005a3fc8 pc=0x25971c6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0005a3fe8 sp=0xc0005a3fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/util/topsql/collector.(*SQLCPUCollector).Start
   > 	/go/src/github.com/pingcap/tidb/util/topsql/collector/cpu.go:83 +0xca
   > goroutine 617 [select]:
   > runtime.gopark(0xc010c417a8?, 0x2?, 0x4?, 0x30?, 0xc010c41784?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010c41608 sp=0xc010c415e8 pc=0x13c9516
   > runtime.selectgo(0xc010c417a8, 0xc010c41780, 0xc0117760c0?, 0x0, 0xc01115efa8?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010c41748 sp=0xc010c41608 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).TelemetryRotateSubWindowLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1214 +0xcc fp=0xc010c417e0 sp=0xc010c41748 pc=0x2796b4c
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010c417e8 sp=0xc010c417e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).TelemetryRotateSubWindowLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1207 +0x8f
   > goroutine 521 [select]:
   > runtime.gopark(0xc000dedf58?, 0x4?, 0xab?, 0x42?, 0xc000dedda8?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000dedbf8 sp=0xc000dedbd8 pc=0x13c9516
   > runtime.selectgo(0xc000dedf58, 0xc000dedda0, 0xc000f9fe38?, 0x0, 0x1?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000dedd38 sp=0xc000dedbf8 pc=0x13d9bdc
   > github.com/pingcap/tidb/ddl.(*worker).start(0xc010f42600, 0xc01089eb60)
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl_worker.go:184 +0x318 fp=0xc000dedfc0 sp=0xc000dedd38 pc=0x27168b8
   > github.com/pingcap/tidb/ddl.(*ddl).Start.func3()
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:399 +0x2a fp=0xc000dedfe0 sp=0xc000dedfc0 pc=0x26d426a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000dedfe8 sp=0xc000dedfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/ddl.(*ddl).Start
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:399 +0x58e
   > goroutine 744 [select]:
   > runtime.gopark(0xc01135ff28?, 0x2?, 0xb8?, 0xfd?, 0xc01135feec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01135fd58 sp=0xc01135fd38 pc=0x13c9516
   > runtime.selectgo(0xc01135ff28, 0xc01135fee8, 0x18?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01135fe98 sp=0xc01135fd58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc011c29980, {0x4134ba0, 0xc000560900}, 0xc011e02470, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc01135ffa8 sp=0xc01135fe98 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc01135ffe0 sp=0xc01135ffa8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01135ffe8 sp=0xc01135ffe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 756 [select]:
   > runtime.gopark(0xc00008df78?, 0x2?, 0x0?, 0x0?, 0xc00008deec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008dd58 sp=0xc00008dd38 pc=0x13c9516
   > runtime.selectgo(0xc00008df78, 0xc00008dee8, 0x3b67af1?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00008de98 sp=0xc00008dd58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc011d82940, {0x40d68d0?, 0xc011c4f170?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc00008dfb8 sp=0xc00008de98 pc=0x30ecdf4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc00008dfe0 sp=0xc00008dfb8 pc=0x30ec08e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008dfe8 sp=0xc00008dfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 525 [select]:
   > runtime.gopark(0xc0000c8f78?, 0x3?, 0x10?, 0x0?, 0xc0000c8f12?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0000c8d60 sp=0xc0000c8d40 pc=0x13c9516
   > runtime.selectgo(0xc0000c8f78, 0xc0000c8f0c, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0000c8ea0 sp=0xc0000c8d60 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).topNSlowQueryLoop(0xc0108952c0)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:483 +0x194 fp=0xc0000c8fc8 sp=0xc0000c8ea0 pc=0x278f654
   > github.com/pingcap/tidb/domain.(*Domain).Init.func11()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:867 +0x26 fp=0xc0000c8fe0 sp=0xc0000c8fc8 pc=0x2793986
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000c8fe8 sp=0xc0000c8fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:867 +0xed2
   > goroutine 526 [select]:
   > runtime.gopark(0xc0004a6ef8?, 0x3?, 0x8?, 0x0?, 0xc0004a6e82?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004a6d08 sp=0xc0004a6ce8 pc=0x13c9516
   > runtime.selectgo(0xc0004a6ef8, 0xc0004a6e7c, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0004a6e48 sp=0xc0004a6d08 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).infoSyncerKeeper(0xc0108952c0)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:515 +0x165 fp=0xc0004a6fc8 sp=0xc0004a6e48 pc=0x278fb85
   > github.com/pingcap/tidb/domain.(*Domain).Init.func12()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:868 +0x26 fp=0xc0004a6fe0 sp=0xc0004a6fc8 pc=0x2793926
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004a6fe8 sp=0xc0004a6fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:868 +0xf15
   > goroutine 527 [select]:
   > runtime.gopark(0xc010c426b0?, 0x2?, 0x0?, 0x0?, 0xc010c4267c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010c424e8 sp=0xc010c424c8 pc=0x13c9516
   > runtime.selectgo(0xc010c426b0, 0xc010c42678, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010c42628 sp=0xc010c424e8 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).globalConfigSyncerKeeper(0xc0108952c0)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:538 +0xf5 fp=0xc010c427c8 sp=0xc010c42628 pc=0x2790155
   > github.com/pingcap/tidb/domain.(*Domain).Init.func13()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:869 +0x26 fp=0xc010c427e0 sp=0xc010c427c8 pc=0x27938c6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010c427e8 sp=0xc010c427e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:869 +0xf5c
   > goroutine 528 [select]:
   > runtime.gopark(0xc010c42e78?, 0x3?, 0x4?, 0x30?, 0xc010c42df2?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000f9fc78 sp=0xc000f9fc58 pc=0x13c9516
   > runtime.selectgo(0xc000f9fe78, 0xc010c42dec, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000f9fdb8 sp=0xc000f9fc78 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).topologySyncerKeeper(0xc0108952c0)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:561 +0x165 fp=0xc000f9ffc8 sp=0xc000f9fdb8 pc=0x2790645
   > github.com/pingcap/tidb/domain.(*Domain).Init.func14()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:872 +0x26 fp=0xc000f9ffe0 sp=0xc000f9ffc8 pc=0x2793866
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000f9ffe8 sp=0xc000f9ffe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:872 +0xfbd
   > goroutine 616 [select]:
   > runtime.gopark(0xc0000c9728?, 0x2?, 0x4?, 0x30?, 0xc0000c96d4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0000c9548 sp=0xc0000c9528 pc=0x13c9516
   > runtime.selectgo(0xc0000c9728, 0xc0000c96d0, 0x9?, 0x0, 0x15?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0000c9688 sp=0xc0000c9548 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).TelemetryReportLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1185 +0x11c fp=0xc0000c97e0 sp=0xc0000c9688 pc=0x279663c
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000c97e8 sp=0xc0000c97e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).TelemetryReportLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1177 +0x285
   > goroutine 483 [select]:
   > runtime.gopark(0xc00053de90?, 0x3?, 0x4?, 0x30?, 0xc00053de02?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00053dc70 sp=0xc00053dc50 pc=0x13c9516
   > runtime.selectgo(0xc00053de90, 0xc00053ddfc, 0x10?, 0x0, 0x1?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00053ddb0 sp=0xc00053dc70 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).globalBindHandleWorkerLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1114 +0x16f fp=0xc00053dfe0 sp=0xc00053ddb0 pc=0x279564f
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00053dfe8 sp=0xc00053dfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).globalBindHandleWorkerLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1101 +0xad
   > goroutine 484 [select]:
   > runtime.gopark(0xc010c45728?, 0x2?, 0x4?, 0x30?, 0xc010c456d4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010c45548 sp=0xc010c45528 pc=0x13c9516
   > runtime.selectgo(0xc010c45728, 0xc010c456d0, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010c45688 sp=0xc010c45548 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).handleEvolvePlanTasksLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1151 +0x107 fp=0xc010c457e0 sp=0xc010c45688 pc=0x2795ee7
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010c457e8 sp=0xc010c457e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).handleEvolvePlanTasksLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1144 +0xe5
   > goroutine 561 [select]:
   > runtime.gopark(0xc010c45f18?, 0x3?, 0x0?, 0x30?, 0xc010c45e8a?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010c45cc8 sp=0xc010c45ca8 pc=0x13c9516
   > runtime.selectgo(0xc010c45f18, 0xc010c45e84, 0x1?, 0x0, 0x13c9516?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010c45e08 sp=0xc010c45cc8 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).LoadSysVarCacheLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1032 +0x145 fp=0xc010c45fe0 sp=0xc010c45e08 pc=0x2794ca5
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010c45fe8 sp=0xc010c45fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).LoadSysVarCacheLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1023 +0x172
   > goroutine 619 [select]:
   > runtime.gopark(0xc01050df18?, 0x7?, 0x45?, 0x0?, 0xc01050dafa?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01050d958 sp=0xc01050d938 pc=0x13c9516
   > runtime.selectgo(0xc01050df18, 0xc01050daec, 0x0?, 0x0, 0x1?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01050da98 sp=0xc01050d958 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).updateStatsWorker(0xc0108952c0, {0x4134ba0?, 0xc00fed1d40?}, {0x40e2a10, 0xc0113d8dc0})
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1429 +0x27c fp=0xc01050dfa8 sp=0xc01050da98 pc=0x2798fdc
   > github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop.func3()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1304 +0x36 fp=0xc01050dfe0 sp=0xc01050dfa8 pc=0x27974b6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01050dfe8 sp=0xc01050dfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1304 +0x29a
   > goroutine 6625 [semacquire]:
   > runtime.gopark(0xc010eb8720?, 0xc1991f520d9a3bb6?, 0xa0?, 0xf1?, 0xc000572060?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0124796d8 sp=0xc0124796b8 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc01346f6f8, 0x31?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc012479740 sp=0xc0124796d8 pc=0x13dae5e
   > sync.runtime_Semacquire(0xc1991f520da5c889?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc012479770 sp=0xc012479740 pc=0x13f7f65
   > sync.(*WaitGroup).Wait(0xc0124797d0?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc012479798 sp=0xc012479770 pc=0x140b312
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:856 +0x45 fp=0xc0124797e0 sp=0xc012479798 pc=0x2fbcc85
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0124797e8 sp=0xc0124797e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:855 +0x4c5
   > goroutine 540 [select]:
   > runtime.gopark(0xc010c40718?, 0x3?, 0x4?, 0x30?, 0xc010c4069a?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010c404d8 sp=0xc010c404b8 pc=0x13c9516
   > runtime.selectgo(0xc010c40718, 0xc010c40694, 0xc010355b60?, 0x0, 0xc0005ba060?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010c40618 sp=0xc010c404d8 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).LoadPrivilegeLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:982 +0x145 fp=0xc010c407e0 sp=0xc010c40618 pc=0x2794465
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010c407e8 sp=0xc010c407e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).LoadPrivilegeLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:973 +0x205
   > goroutine 620 [select]:
   > runtime.gopark(0xc010c41f78?, 0x2?, 0x0?, 0x30?, 0xc010c41f4c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010c41dd0 sp=0xc010c41db0 pc=0x13c9516
   > runtime.selectgo(0xc010c41f78, 0xc010c41f48, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010c41f10 sp=0xc010c41dd0 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).autoAnalyzeWorker(0xc0108952c0, {0x40e2a10, 0xc0113d8dc0})
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1487 +0x105 fp=0xc010c41fb8 sp=0xc010c41f10 pc=0x2799f45
   > github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop.func4()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1307 +0x2e fp=0xc010c41fe0 sp=0xc010c41fb8 pc=0x279744e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010c41fe8 sp=0xc010c41fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1307 +0x31a
   > goroutine 621 [select]:
   > runtime.gopark(0xc00052bd48?, 0x3?, 0x3?, 0x0?, 0xc00052bcd2?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00052bb50 sp=0xc00052bb30 pc=0x13c9516
   > runtime.selectgo(0xc00052bd48, 0xc00052bccc, 0x0?, 0x0, 0xc00fa5dcd8?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00052bc90 sp=0xc00052bb50 pc=0x13d9bdc
   > github.com/pingcap/tidb/statistics/handle.(*Handle).drainColTask(0xc011782000, 0xc010b969c0)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:294 +0xe5 fp=0xc00052bd88 sp=0xc00052bc90 pc=0x2612705
   > github.com/pingcap/tidb/statistics/handle.(*Handle).HandleOneTask(0xc011782000, 0x0?, 0xc00052bf40, {0x7f3c581a34c8, 0xc01178e000}, 0x0?)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:181 +0xc5 fp=0xc00052bee8 sp=0xc00052bd88 pc=0x2610fe5
   > github.com/pingcap/tidb/statistics/handle.(*Handle).SubLoadWorker(0xc011782000, {0x4134ba0?, 0xc01178e000}, 0x40d68d0?, 0xc010933620?)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:154 +0x11b fp=0xc00052bfa8 sp=0xc00052bee8 pc=0x2610b3b
   > github.com/pingcap/tidb/domain.(*Domain).StartLoadStatsSubWorkers.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1318 +0x36 fp=0xc00052bfe0 sp=0xc00052bfa8 pc=0x27977b6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00052bfe8 sp=0xc00052bfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).StartLoadStatsSubWorkers
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1318 +0x172
   > goroutine 622 [select]:
   > runtime.gopark(0xc00052cd48?, 0x3?, 0x3?, 0x0?, 0xc00052ccd2?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00052cb50 sp=0xc00052cb30 pc=0x13c9516
   > runtime.selectgo(0xc00052cd48, 0xc00052cccc, 0x0?, 0x0, 0x13a71c6?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00052cc90 sp=0xc00052cb50 pc=0x13d9bdc
   > github.com/pingcap/tidb/statistics/handle.(*Handle).drainColTask(0xc011782000, 0xc010b969c0)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:294 +0xe5 fp=0xc00052cd88 sp=0xc00052cc90 pc=0x2612705
   > github.com/pingcap/tidb/statistics/handle.(*Handle).HandleOneTask(0xc011782000, 0x0?, 0xc00052cf40, {0x7f3c581a34c8, 0xc01178e240}, 0xc010932960?)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:181 +0xc5 fp=0xc00052cee8 sp=0xc00052cd88 pc=0x2610fe5
   > github.com/pingcap/tidb/statistics/handle.(*Handle).SubLoadWorker(0xc011782000, {0x4134ba0?, 0xc01178e240}, 0xc010946210?, 0xc00059efb8?)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:154 +0x11b fp=0xc00052cfa8 sp=0xc00052cee8 pc=0x2610b3b
   > github.com/pingcap/tidb/domain.(*Domain).StartLoadStatsSubWorkers.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1318 +0x36 fp=0xc00052cfe0 sp=0xc00052cfa8 pc=0x27977b6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00052cfe8 sp=0xc00052cfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).StartLoadStatsSubWorkers
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1318 +0x172
   > goroutine 623 [select]:
   > runtime.gopark(0xc000f9bd48?, 0x3?, 0x3?, 0x0?, 0xc000f9bcd2?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000f9bb50 sp=0xc000f9bb30 pc=0x13c9516
   > runtime.selectgo(0xc000f9bd48, 0xc000f9bccc, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000f9bc90 sp=0xc000f9bb50 pc=0x13d9bdc
   > github.com/pingcap/tidb/statistics/handle.(*Handle).drainColTask(0xc011782000, 0xc010b969c0)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:294 +0xe5 fp=0xc000f9bd88 sp=0xc000f9bc90 pc=0x2612705
   > github.com/pingcap/tidb/statistics/handle.(*Handle).HandleOneTask(0xc011782000, 0x35d5ce0?, 0xc000f9bf40, {0x7f3c581a34c8, 0xc01178e480}, 0x0?)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:181 +0xc5 fp=0xc000f9bee8 sp=0xc000f9bd88 pc=0x2610fe5
   > github.com/pingcap/tidb/statistics/handle.(*Handle).SubLoadWorker(0xc011782000, {0x4134ba0?, 0xc01178e480}, 0x0?, 0xc00059d538?)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:154 +0x11b fp=0xc000f9bfa8 sp=0xc000f9bee8 pc=0x2610b3b
   > github.com/pingcap/tidb/domain.(*Domain).StartLoadStatsSubWorkers.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1318 +0x36 fp=0xc000f9bfe0 sp=0xc000f9bfa8 pc=0x27977b6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000f9bfe8 sp=0xc000f9bfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).StartLoadStatsSubWorkers
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1318 +0x172
   > goroutine 624 [select]:
   > runtime.gopark(0xc00009dd48?, 0x3?, 0x3?, 0x0?, 0xc00009dcd2?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00009db50 sp=0xc00009db30 pc=0x13c9516
   > runtime.selectgo(0xc00009dd48, 0xc00009dccc, 0x149?, 0x0, 0x8?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00009dc90 sp=0xc00009db50 pc=0x13d9bdc
   > github.com/pingcap/tidb/statistics/handle.(*Handle).drainColTask(0xc011782000, 0xc010b969c0)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:294 +0xe5 fp=0xc00009dd88 sp=0xc00009dc90 pc=0x2612705
   > github.com/pingcap/tidb/statistics/handle.(*Handle).HandleOneTask(0xc011782000, 0x60384e0?, 0xc00009df40, {0x7f3c581a34c8, 0xc01178e6c0}, 0xc00059df90?)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:181 +0xc5 fp=0xc00009dee8 sp=0xc00009dd88 pc=0x2610fe5
   > github.com/pingcap/tidb/statistics/handle.(*Handle).SubLoadWorker(0xc011782000, {0x4134ba0?, 0xc01178e6c0}, 0xc01064ca80?, 0xc00059dd38?)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:154 +0x11b fp=0xc00009dfa8 sp=0xc00009dee8 pc=0x2610b3b
   > github.com/pingcap/tidb/domain.(*Domain).StartLoadStatsSubWorkers.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1318 +0x36 fp=0xc00009dfe0 sp=0xc00009dfa8 pc=0x27977b6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00009dfe8 sp=0xc00009dfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).StartLoadStatsSubWorkers
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1318 +0x172
   > goroutine 625 [select]:
   > runtime.gopark(0xc000635d48?, 0x3?, 0x3?, 0x0?, 0xc000635cd2?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000635b50 sp=0xc000635b30 pc=0x13c9516
   > runtime.selectgo(0xc000635d48, 0xc000635ccc, 0x149?, 0x0, 0x8?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000635c90 sp=0xc000635b50 pc=0x13d9bdc
   > github.com/pingcap/tidb/statistics/handle.(*Handle).drainColTask(0xc011782000, 0xc010b969c0)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:294 +0xe5 fp=0xc000635d88 sp=0xc000635c90 pc=0x2612705
   > github.com/pingcap/tidb/statistics/handle.(*Handle).HandleOneTask(0xc011782000, 0x60384e0?, 0xc000635f40, {0x7f3c581a34c8, 0xc01178e900}, 0xc00059c790?)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:181 +0xc5 fp=0xc000635ee8 sp=0xc000635d88 pc=0x2610fe5
   > github.com/pingcap/tidb/statistics/handle.(*Handle).SubLoadWorker(0xc011782000, {0x4134ba0?, 0xc01178e900}, 0xc0103ad200?, 0xc00059c538?)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:154 +0x11b fp=0xc000635fa8 sp=0xc000635ee8 pc=0x2610b3b
   > github.com/pingcap/tidb/domain.(*Domain).StartLoadStatsSubWorkers.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1318 +0x36 fp=0xc000635fe0 sp=0xc000635fa8 pc=0x27977b6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000635fe8 sp=0xc000635fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).StartLoadStatsSubWorkers
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1318 +0x172
   > goroutine 626 [select]:
   > runtime.gopark(0xc010c43fa8?, 0x2?, 0x0?, 0x30?, 0xc010c43f7c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010c43e00 sp=0xc010c43de0 pc=0x13c9516
   > runtime.selectgo(0xc010c43fa8, 0xc010c43f78, 0x40d68d0?, 0x0, 0x30319d7?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010c43f40 sp=0xc010c43e00 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).PlanReplayerLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1236 +0xf6 fp=0xc010c43fe0 sp=0xc010c43f40 pc=0x2796e36
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010c43fe8 sp=0xc010c43fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).PlanReplayerLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1227 +0x6c
   > goroutine 6613 [chan receive]:
   > runtime.gopark(0xc010d20f00?, 0xc0118a6840?, 0x20?, 0x45?, 0xc00052ace8?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00052ac80 sp=0xc00052ac60 pc=0x13c9516
   > runtime.chanrecv(0xc01377aea0, 0xc00052ad68, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc00052ad10 sp=0xc00052ac80 pc=0x13934bb
   > runtime.chanrecv2(0xc011c4f140?, 0x3710340?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc00052ad38 sp=0xc00052ad10 pc=0x1392ff8
   > github.com/pingcap/tidb/executor.(*UnionExec).Next(0xc010cf9000, {0x40d68d0, 0xc011c4f170}, 0xc01367c0a0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1702 +0x85 fp=0xc00052ada0 sp=0xc00052ad38 pc=0x30425c5
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc011c4f170}, {0x40d9ea0, 0xc010cf9000}, 0xc01367c0a0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc00052aee0 sp=0xc00052ada0 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*HashAggExec).fetchChildData(0xc010e21000, {0x40d68d0, 0xc011c4f170}, 0xc01350fd40?)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:798 +0x1be fp=0xc00052afb0 sp=0xc00052aee0 pc=0x2fbc0fe
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func3()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:835 +0x32 fp=0xc00052afe0 sp=0xc00052afb0 pc=0x2fbce72
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00052afe8 sp=0xc00052afe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:835 +0xea
   > goroutine 627 [select]:
   > runtime.gopark(0xc00fda5eb0?, 0x2?, 0x3?, 0x0?, 0xc00fda5e5c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fda5cc8 sp=0xc00fda5ca8 pc=0x13c9516
   > runtime.selectgo(0xc00fda5eb0, 0xc00fda5e58, 0xc011778270?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fda5e08 sp=0xc00fda5cc8 pc=0x13d9bdc
   > github.com/pingcap/tidb/util/expensivequery.(*Handle).Run(0xc010be83c0)
   > 	/go/src/github.com/pingcap/tidb/util/expensivequery/expensivequery.go:61 +0x198 fp=0xc00fda5fc8 sp=0xc00fda5e08 pc=0x27866f8
   > main.createServer.func1()
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:695 +0x26 fp=0xc00fda5fe0 sp=0xc00fda5fc8 pc=0x343c186
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fda5fe8 sp=0xc00fda5fe0 pc=0x13fc6e1
   > created by main.createServer
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:695 +0x44a
   > goroutine 628 [select, locked to thread]:
   > runtime.gopark(0xc0000cd7a8?, 0x2?, 0x0?, 0x0?, 0xc0000cd7a4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0000cd618 sp=0xc0000cd5f8 pc=0x13c9516
   > runtime.selectgo(0xc0000cd7a8, 0xc0000cd7a0, 0x0?, 0x0, 0xc010c04b80?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0000cd758 sp=0xc0000cd618 pc=0x13d9bdc
   > runtime.ensureSigM.func1()
   > 	/usr/local/go/src/runtime/signal_unix.go:995 +0x1b0 fp=0xc0000cd7e0 sp=0xc0000cd758 pc=0x13de070
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000cd7e8 sp=0xc0000cd7e0 pc=0x13fc6e1
   > created by runtime.ensureSigM
   > 	/usr/local/go/src/runtime/signal_unix.go:978 +0xbd
   > goroutine 64 [select]:
   > runtime.gopark(0xc00059ff68?, 0x4?, 0x0?, 0x30?, 0xc00059fee8?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00059fd48 sp=0xc00059fd28 pc=0x13c9516
   > runtime.selectgo(0xc00059ff68, 0xc00059fee0, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00059fe88 sp=0xc00059fd48 pc=0x13d9bdc
   > github.com/pingcap/tidb/util/topsql/reporter.(*RemoteTopSQLReporter).collectWorker(0xc000292c00)
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:175 +0x18e fp=0xc00059ffc8 sp=0xc00059fe88 pc=0x25a162e
   > github.com/pingcap/tidb/util/topsql/reporter.(*RemoteTopSQLReporter).Start.func1()
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:110 +0x26 fp=0xc00059ffe0 sp=0xc00059ffc8 pc=0x25a11c6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00059ffe8 sp=0xc00059ffe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/util/topsql/reporter.(*RemoteTopSQLReporter).Start
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:110 +0x6a
   > goroutine 65 [select]:
   > runtime.gopark(0xc0005a3790?, 0x2?, 0x0?, 0x30?, 0xc0005a373c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0005a3590 sp=0xc0005a3570 pc=0x13c9516
   > runtime.selectgo(0xc0005a3790, 0xc0005a3738, 0x40d6860?, 0x0, 0x60384e0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0005a36d0 sp=0xc0005a3590 pc=0x13d9bdc
   > github.com/pingcap/tidb/util/topsql/reporter.(*RemoteTopSQLReporter).reportWorker(0xc000292c00)
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:261 +0xfd fp=0xc0005a37c8 sp=0xc0005a36d0 pc=0x25a231d
   > github.com/pingcap/tidb/util/topsql/reporter.(*RemoteTopSQLReporter).Start.func2()
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:111 +0x26 fp=0xc0005a37e0 sp=0xc0005a37c8 pc=0x25a1166
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0005a37e8 sp=0xc0005a37e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/util/topsql/reporter.(*RemoteTopSQLReporter).Start
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:111 +0xaa
   > goroutine 658 [select]:
   > runtime.gopark(0xc00fa5c748?, 0x3?, 0x4?, 0x30?, 0xc00fa5c6e2?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fa5c550 sp=0xc00fa5c530 pc=0x13c9516
   > runtime.selectgo(0xc00fa5c748, 0xc00fa5c6dc, 0xe?, 0x0, 0x2?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fa5c690 sp=0xc00fa5c550 pc=0x13d9bdc
   > github.com/pingcap/tidb/util/topsql/reporter.(*SingleTargetDataSink).run(0xc0000c52c0)
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/single_target.go:116 +0x12f fp=0xc00fa5c790 sp=0xc00fa5c690 pc=0x25a34af
   > github.com/pingcap/tidb/util/topsql/reporter.(*SingleTargetDataSink).recoverRun(0xc0000c52c0)
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/single_target.go:98 +0x65 fp=0xc00fa5c7c8 sp=0xc00fa5c790 pc=0x25a30e5
   > github.com/pingcap/tidb/util/topsql/reporter.(*SingleTargetDataSink).Start.func1()
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/single_target.go:82 +0x26 fp=0xc00fa5c7e0 sp=0xc00fa5c7c8 pc=0x25a3046
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fa5c7e8 sp=0xc00fa5c7e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/util/topsql/reporter.(*SingleTargetDataSink).Start
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/single_target.go:82 +0x2ab
   > goroutine 659 [select]:
   > runtime.gopark(0xc00008cf90?, 0x2?, 0x18?, 0x92?, 0xc00008cf6c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008cdf0 sp=0xc00008cdd0 pc=0x13c9516
   > runtime.selectgo(0xc00008cf90, 0xc00008cf68, 0xf?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00008cf30 sp=0xc00008cdf0 pc=0x13d9bdc
   > github.com/pingcap/tidb/util/topsql/stmtstats.(*aggregator).run(0xc0003050e0)
   > 	/go/src/github.com/pingcap/tidb/util/topsql/stmtstats/aggregator.go:67 +0xff fp=0xc00008cfc8 sp=0xc00008cf30 pc=0x1fbf99f
   > github.com/pingcap/tidb/util/topsql/stmtstats.(*aggregator).start.func1()
   > 	/go/src/github.com/pingcap/tidb/util/topsql/stmtstats/aggregator.go:56 +0x26 fp=0xc00008cfe0 sp=0xc00008cfc8 pc=0x1fbf866
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008cfe8 sp=0xc00008cfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/util/topsql/stmtstats.(*aggregator).start
   > 	/go/src/github.com/pingcap/tidb/util/topsql/stmtstats/aggregator.go:56 +0xd6
   > goroutine 660 [IO wait]:
   > runtime.gopark(0xc010ebbc70?, 0xc0003d3878?, 0x0?, 0x0?, 0xc0003d38c8?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0003d3858 sp=0xc0003d3838 pc=0x13c9516
   > runtime.netpollblock(0xc010ebbc70?, 0x2?, 0x0?)
   > 	/usr/local/go/src/runtime/netpoll.go:526 +0xf7 fp=0xc0003d3890 sp=0xc0003d3858 pc=0x13c18f7
   > internal/poll.runtime_pollWait(0x7f3c58c22d90, 0x72)
   > 	/usr/local/go/src/runtime/netpoll.go:305 +0x89 fp=0xc0003d38b0 sp=0xc0003d3890 pc=0x13f5d09
   > internal/poll.(*pollDesc).wait(0xc0113cee00?, 0xd0?, 0x0)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:84 +0x32 fp=0xc0003d38d8 sp=0xc0003d38b0 pc=0x1473092
   > internal/poll.(*pollDesc).waitRead(...)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:89
   > internal/poll.(*FD).Accept(0xc0113cee00)
   > 	/usr/local/go/src/internal/poll/fd_unix.go:614 +0x234 fp=0xc0003d3970 sp=0xc0003d38d8 pc=0x1478494
   > net.(*netFD).accept(0xc0113cee00)
   > 	/usr/local/go/src/net/fd_unix.go:172 +0x35 fp=0xc0003d3a28 sp=0xc0003d3970 pc=0x1597315
   > net.(*TCPListener).accept(0xc011331c80)
   > 	/usr/local/go/src/net/tcpsock_posix.go:142 +0x28 fp=0xc0003d3a58 sp=0xc0003d3a28 pc=0x15b3288
   > net.(*TCPListener).Accept(0xc011331c80)
   > 	/usr/local/go/src/net/tcpsock.go:288 +0x3d fp=0xc0003d3a88 sp=0xc0003d3a58 pc=0x15b22fd
   > github.com/soheilhy/cmux.(*cMux).Serve(0xc011660820)
   > 	/go/pkg/mod/github.com/soheilhy/cmux@v0.1.5/cmux.go:170 +0xa9 fp=0xc0003d3b18 sp=0xc0003d3a88 pc=0x31eb249
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer(0xc011778270, 0xc000629200)
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:473 +0x4f7 fp=0xc0003d3c90 sp=0xc0003d3b18 pc=0x324fe57
   > github.com/pingcap/tidb/server.(*Server).startHTTPServer(0xc011778270)
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:446 +0x1610 fp=0xc0003d3fc8 sp=0xc0003d3c90 pc=0x324f250
   > github.com/pingcap/tidb/server.(*Server).startStatusHTTP.func1()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:62 +0x26 fp=0xc0003d3fe0 sp=0xc0003d3fc8 pc=0x324b8c6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0003d3fe8 sp=0xc0003d3fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/server.(*Server).startStatusHTTP
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:62 +0x56
   > goroutine 661 [IO wait]:
   > runtime.gopark(0x18?, 0xc000502c00?, 0xf8?, 0xc4?, 0xc00052db70?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00052db00 sp=0xc00052dae0 pc=0x13c9516
   > runtime.netpollblock(0x14?, 0x24f6d45?, 0x0?)
   > 	/usr/local/go/src/runtime/netpoll.go:526 +0xf7 fp=0xc00052db38 sp=0xc00052db00 pc=0x13c18f7
   > internal/poll.runtime_pollWait(0x7f3c58c22f70, 0x72)
   > 	/usr/local/go/src/runtime/netpoll.go:305 +0x89 fp=0xc00052db58 sp=0xc00052db38 pc=0x13f5d09
   > internal/poll.(*pollDesc).wait(0xc0113cec00?, 0xc00052dd20?, 0x0)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:84 +0x32 fp=0xc00052db80 sp=0xc00052db58 pc=0x1473092
   > internal/poll.(*pollDesc).waitRead(...)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:89
   > internal/poll.(*FD).Accept(0xc0113cec00)
   > 	/usr/local/go/src/internal/poll/fd_unix.go:614 +0x234 fp=0xc00052dc18 sp=0xc00052db80 pc=0x1478494
   > net.(*netFD).accept(0xc0113cec00)
   > 	/usr/local/go/src/net/fd_unix.go:172 +0x35 fp=0xc00052dcd0 sp=0xc00052dc18 pc=0x1597315
   > net.(*TCPListener).accept(0xc011331c68)
   > 	/usr/local/go/src/net/tcpsock_posix.go:142 +0x28 fp=0xc00052dd00 sp=0xc00052dcd0 pc=0x15b3288
   > net.(*TCPListener).Accept(0xc011331c68)
   > 	/usr/local/go/src/net/tcpsock.go:288 +0x3d fp=0xc00052dd30 sp=0xc00052dd00 pc=0x15b22fd
   > github.com/pingcap/tidb/server.(*Server).startNetworkListener(0xc011778270, {0x40d4c30, 0xc011331c68}, 0x0, 0x0?)
   > 	/go/src/github.com/pingcap/tidb/server/server.go:378 +0xa6 fp=0xc00052dfa8 sp=0xc00052dd30 pc=0x32581c6
   > github.com/pingcap/tidb/server.(*Server).Run.func1()
   > 	/go/src/github.com/pingcap/tidb/server/server.go:363 +0x34 fp=0xc00052dfe0 sp=0xc00052dfa8 pc=0x32580f4
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00052dfe8 sp=0xc00052dfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/server.(*Server).Run
   > 	/go/src/github.com/pingcap/tidb/server/server.go:363 +0x145
   > goroutine 662 [IO wait]:
   > runtime.gopark(0x0?, 0x0?, 0x0?, 0x0?, 0xc000f99b78?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000f99b08 sp=0xc000f99ae8 pc=0x13c9516
   > runtime.netpollblock(0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/netpoll.go:526 +0xf7 fp=0xc000f99b40 sp=0xc000f99b08 pc=0x13c18f7
   > internal/poll.runtime_pollWait(0x7f3c58c22e80, 0x72)
   > 	/usr/local/go/src/runtime/netpoll.go:305 +0x89 fp=0xc000f99b60 sp=0xc000f99b40 pc=0x13f5d09
   > internal/poll.(*pollDesc).wait(0xc0113cec80?, 0x1?, 0x0)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:84 +0x32 fp=0xc000f99b88 sp=0xc000f99b60 pc=0x1473092
   > internal/poll.(*pollDesc).waitRead(...)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:89
   > internal/poll.(*FD).Accept(0xc0113cec80)
   > 	/usr/local/go/src/internal/poll/fd_unix.go:614 +0x234 fp=0xc000f99c20 sp=0xc000f99b88 pc=0x1478494
   > net.(*netFD).accept(0xc0113cec80)
   > 	/usr/local/go/src/net/fd_unix.go:172 +0x35 fp=0xc000f99cd8 sp=0xc000f99c20 pc=0x1597315
   > net.(*UnixListener).accept(0x0?)
   > 	/usr/local/go/src/net/unixsock_posix.go:166 +0x1c fp=0xc000f99d00 sp=0xc000f99cd8 pc=0x15b9c1c
   > net.(*UnixListener).Accept(0xc011777cb0)
   > 	/usr/local/go/src/net/unixsock.go:260 +0x3d fp=0xc000f99d30 sp=0xc000f99d00 pc=0x15b82bd
   > github.com/pingcap/tidb/server.(*Server).startNetworkListener(0xc011778270, {0x40d4c60, 0xc011777cb0}, 0x1, 0x0?)
   > 	/go/src/github.com/pingcap/tidb/server/server.go:378 +0xa6 fp=0xc000f99fa8 sp=0xc000f99d30 pc=0x32581c6
   > github.com/pingcap/tidb/server.(*Server).Run.func2()
   > 	/go/src/github.com/pingcap/tidb/server/server.go:364 +0x37 fp=0xc000f99fe0 sp=0xc000f99fa8 pc=0x3258097
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000f99fe8 sp=0xc000f99fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/server.(*Server).Run
   > 	/go/src/github.com/pingcap/tidb/server/server.go:364 +0x1db
   > goroutine 742 [select]:
   > runtime.gopark(0xc011361728?, 0x2?, 0x0?, 0x0?, 0xc0113616ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc011361558 sp=0xc011361538 pc=0x13c9516
   > runtime.selectgo(0xc011361728, 0xc0113616e8, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc011361698 sp=0xc011361558 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc011c29800, {0x4134ba0, 0xc000560900}, 0xc011e02470, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc0113617a8 sp=0xc011361698 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc0113617e0 sp=0xc0113617a8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0113617e8 sp=0xc0113617e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 6618 [select]:
   > runtime.gopark(0xc00059cf28?, 0x2?, 0x2f?, 0xf9?, 0xc00059ceec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00059cd58 sp=0xc00059cd38 pc=0x13c9516
   > runtime.selectgo(0xc00059cf28, 0xc00059cee8, 0x60384e0?, 0x0, 0xc01344ba40?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00059ce98 sp=0xc00059cd58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc01343bf00, {0x4134ba0, 0xc000560900}, 0xc01346f6e0, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc00059cfa8 sp=0xc00059ce98 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc00059cfe0 sp=0xc00059cfa8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00059cfe8 sp=0xc00059cfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 512 [chan receive]:
   > runtime.gopark(0xc011e04fc0?, 0xc011044340?, 0x6d?, 0xcb?, 0xc011b332d0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc011b33228 sp=0xc011b33208 pc=0x13c9516
   > runtime.chanrecv(0xc011b56300, 0xc011b33300, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc011b332b8 sp=0xc011b33228 pc=0x13934bb
   > runtime.chanrecv2(0xc010e21200?, 0x40d68d0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc011b332e0 sp=0xc011b332b8 pc=0x1392ff8
   > github.com/pingcap/tidb/executor.(*HashAggExec).parallelExec(0xc010e21200, {0x40d68d0?, 0xc011c4f170?}, 0xc011b58be0)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:888 +0x89 fp=0xc011b33318 sp=0xc011b332e0 pc=0x2fbcf29
   > github.com/pingcap/tidb/executor.(*HashAggExec).Next(0x40d68d0?, {0x40d68d0?, 0xc011c4f170?}, 0x7f3c5896b001?)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:768 +0x76 fp=0xc011b33348 sp=0xc011b33318 pc=0x2fbbeb6
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc011c4f170}, {0x40d9120, 0xc010e21200}, 0xc011b58be0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc011b33488 sp=0xc011b33348 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*SortExec).fetchRowChunks(0xc011d8b200, {0x40d68d0, 0xc011c4f170})
   > 	/go/src/github.com/pingcap/tidb/executor/sort.go:195 +0x596 fp=0xc011b335e8 sp=0xc011b33488 pc=0x3135156
   > github.com/pingcap/tidb/executor.(*SortExec).Next(0xc011d8b200, {0x40d68d0, 0xc011c4f170}, 0xc011b58b40)
   > 	/go/src/github.com/pingcap/tidb/executor/sort.go:113 +0x325 fp=0xc011b33660 sp=0xc011b335e8 pc=0x31346c5
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc011c4f170}, {0x40d9c20, 0xc011d8b200}, 0xc011b58b40)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc011b337a0 sp=0xc011b33660 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*MaxOneRowExec).Next(0xc011d8f810, {0x40d68d0, 0xc011c4f170}, 0xc011b58b40)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1518 +0xa8 fp=0xc011b337f0 sp=0xc011b337a0 pc=0x30413a8
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc011c4f170}, {0x40d94a0, 0xc011d8f810}, 0xc011b58b40)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc011b33930 sp=0xc011b337f0 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*SelectionExec).Next(0xc010c4b860, {0x40d68d0, 0xc011c4f170}, 0xc011d96870)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1394 +0xed fp=0xc011b339c0 sp=0xc011b33930 pc=0x304012d
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc011c4f170}, {0x40d9960, 0xc010c4b860}, 0xc011d96870)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc011b33b00 sp=0xc011b339c0 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*NestedLoopApplyExec).fetchAllInners(0xc01164d180, {0x40d68d0, 0xc011c4f170})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:979 +0x346 fp=0xc011b33bf8 sp=0xc011b33b00 pc=0x30b2966
   > github.com/pingcap/tidb/executor.(*NestedLoopApplyExec).Next(0xc01164d180, {0x40d68d0, 0xc011c4f170}, 0xc011d976d0)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:1032 +0x5b6 fp=0xc011b33d58 sp=0xc011b33bf8 pc=0x30b32b6
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc011c4f170}, {0x40d9560, 0xc01164d180}, 0xc011d976d0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc011b33e98 sp=0xc011b33d58 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*projectionInputFetcher).run(0xc011d8b4c0, {0x40d68d0, 0xc011c4f170})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:381 +0x2f0 fp=0xc011b33fb8 sp=0xc011b33e98 pc=0x30ec890
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:272 +0x2e fp=0xc011b33fe0 sp=0xc011b33fb8 pc=0x30ec0ee
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc011b33fe8 sp=0xc011b33fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:272 +0x67e
   > goroutine 6444 [chan receive]:
   > runtime.gopark(0xc0136e0c88?, 0x13d1800?, 0xa0?, 0xc0?, 0xc011044d00?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0136e0c80 sp=0xc0136e0c60 pc=0x13c9516
   > runtime.chanrecv(0xc01380e6c0, 0xc0136e0d68, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc0136e0d10 sp=0xc0136e0c80 pc=0x13934bb
   > runtime.chanrecv2(0xc010cf8f00?, 0x40d68d0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc0136e0d38 sp=0xc0136e0d10 pc=0x1392ff8
   > github.com/pingcap/tidb/executor.(*UnionExec).Next(0xc010cf8f00, {0x40d68d0, 0xc011c4f170}, 0xc01380a0f0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1702 +0x85 fp=0xc0136e0da0 sp=0xc0136e0d38 pc=0x30425c5
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc011c4f170}, {0x40d9ea0, 0xc010cf8f00}, 0xc01380a0f0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc0136e0ee0 sp=0xc0136e0da0 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*HashAggExec).fetchChildData(0xc010e20e00, {0x40d68d0, 0xc011c4f170}, 0xc011c4f170?)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:798 +0x1be fp=0xc0136e0fb0 sp=0xc0136e0ee0 pc=0x2fbc0fe
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func3()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:835 +0x32 fp=0xc0136e0fe0 sp=0xc0136e0fb0 pc=0x2fbce72
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0136e0fe8 sp=0xc0136e0fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:835 +0xea
   > goroutine 743 [select]:
   > runtime.gopark(0xc011361f28?, 0x2?, 0x0?, 0x0?, 0xc011361eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc011361d58 sp=0xc011361d38 pc=0x13c9516
   > runtime.selectgo(0xc011361f28, 0xc011361ee8, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc011361e98 sp=0xc011361d58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc011c298c0, {0x4134ba0, 0xc000560900}, 0xc011e02470, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc011361fa8 sp=0xc011361e98 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc011361fe0 sp=0xc011361fa8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc011361fe8 sp=0xc011361fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 755 [select]:
   > runtime.gopark(0xc00059d778?, 0x2?, 0xc0?, 0x69?, 0xc00059d6ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00059d558 sp=0xc00059d538 pc=0x13c9516
   > runtime.selectgo(0xc00059d778, 0xc00059d6e8, 0x3b67af1?, 0x0, 0x139805d?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00059d698 sp=0xc00059d558 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc011d82900, {0x40d68d0?, 0xc011c4f170?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc00059d7b8 sp=0xc00059d698 pc=0x30ecdf4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc00059d7e0 sp=0xc00059d7b8 pc=0x30ec08e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00059d7e8 sp=0xc00059d7e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 754 [select]:
   > runtime.gopark(0xc00059c778?, 0x2?, 0xc0?, 0x69?, 0xc00059c6ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00059c558 sp=0xc00059c538 pc=0x13c9516
   > runtime.selectgo(0xc00059c778, 0xc00059c6e8, 0x3b67af1?, 0x0, 0x139805d?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00059c698 sp=0xc00059c558 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc011d828c0, {0x40d68d0?, 0xc011c4f170?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc00059c7b8 sp=0xc00059c698 pc=0x30ecdf4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc00059c7e0 sp=0xc00059c7b8 pc=0x30ec08e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00059c7e8 sp=0xc00059c7e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 513 [select]:
   > runtime.gopark(0xc0005a0f78?, 0x2?, 0x40?, 0xd?, 0xc0005a0eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0005a0d58 sp=0xc0005a0d38 pc=0x13c9516
   > runtime.selectgo(0xc0005a0f78, 0xc0005a0ee8, 0x3b67af1?, 0x0, 0x40d5e60?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0005a0e98 sp=0xc0005a0d58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc011d82880, {0x40d68d0?, 0xc011c4f170?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc0005a0fb8 sp=0xc0005a0e98 pc=0x30ecdf4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc0005a0fe0 sp=0xc0005a0fb8 pc=0x30ec08e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0005a0fe8 sp=0xc0005a0fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 741 [chan receive]:
   > runtime.gopark(0xc011b35760?, 0x13d1800?, 0x70?, 0x8d?, 0xc0117a6ea0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc011b35758 sp=0xc011b35738 pc=0x13c9516
   > runtime.chanrecv(0xc01347b9e0, 0xc011b35840, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc011b357e8 sp=0xc011b35758 pc=0x13934bb
   > runtime.chanrecv2(0xc010cf9100?, 0x40d68d0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc011b35810 sp=0xc011b357e8 pc=0x1392ff8
   > github.com/pingcap/tidb/executor.(*UnionExec).Next(0xc010cf9100, {0x40d68d0, 0xc011c4f170}, 0xc011b582d0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1702 +0x85 fp=0xc011b35878 sp=0xc011b35810 pc=0x30425c5
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc011c4f170}, {0x40d9ea0, 0xc010cf9100}, 0xc011b582d0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc011b359b8 sp=0xc011b35878 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*MaxOneRowExec).Next(0xc011d8f570, {0x40d68d0, 0xc011c4f170}, 0xc011b582d0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1518 +0xa8 fp=0xc011b35a08 sp=0xc011b359b8 pc=0x30413a8
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc011c4f170}, {0x40d94a0, 0xc011d8f570}, 0xc011b582d0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc011b35b48 sp=0xc011b35a08 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*NestedLoopApplyExec).fetchAllInners(0xc01164cfc0, {0x40d68d0, 0xc011c4f170})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:979 +0x346 fp=0xc011b35c40 sp=0xc011b35b48 pc=0x30b2966
   > github.com/pingcap/tidb/executor.(*NestedLoopApplyExec).Next(0xc01164cfc0, {0x40d68d0, 0xc011c4f170}, 0xc011b583c0)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:1032 +0x5b6 fp=0xc011b35da0 sp=0xc011b35c40 pc=0x30b32b6
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc011c4f170}, {0x40d9560, 0xc01164cfc0}, 0xc011b583c0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc011b35ee0 sp=0xc011b35da0 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*HashAggExec).fetchChildData(0xc010e21200, {0x40d68d0, 0xc011c4f170}, 0xc000120008?)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:798 +0x1be fp=0xc011b35fb0 sp=0xc011b35ee0 pc=0x2fbc0fe
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func3()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:835 +0x32 fp=0xc011b35fe0 sp=0xc011b35fb0 pc=0x2fbce72
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc011b35fe8 sp=0xc011b35fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:835 +0xea
   > goroutine 713 [chan receive]:
   > runtime.gopark(0xc011d31860?, 0xc011d979a0?, 0x50?, 0x79?, 0xc011d84e40?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc011d44af8 sp=0xc011d44ad8 pc=0x13c9516
   > runtime.chanrecv(0xc011d849c0, 0xc011d44bd8, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc011d44b88 sp=0xc011d44af8 pc=0x13934bb
   > runtime.chanrecv1(0xc011d8b440?, 0x40d68d0?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc011d44bb0 sp=0xc011d44b88 pc=0x1392fb8
   > github.com/pingcap/tidb/executor.(*ProjectionExec).parallelExecute(0xc011d8b440, {0x40d68d0?, 0xc011c4f170?}, 0xc011d97680)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:218 +0x92 fp=0xc011d44bf8 sp=0xc011d44bb0 pc=0x30eb612
   > github.com/pingcap/tidb/executor.(*ProjectionExec).Next(0xc011d8b440, {0x40d68d0, 0xc011c4f170}, 0x0?)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:182 +0x78 fp=0xc011d44c30 sp=0xc011d44bf8 pc=0x30eb338
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc011c4f170}, {0x40d9720, 0xc011d8b440}, 0xc011d97680)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc011d44d70 sp=0xc011d44c30 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*recordSet).Next(0xc011d975e0, {0x40d68d0?, 0xc011c4f170?}, 0xc011d97680)
   > 	/go/src/github.com/pingcap/tidb/executor/adapter.go:149 +0xbf fp=0xc011d44e00 sp=0xc011d44d70 pc=0x2fa45ff
   > github.com/pingcap/tidb/session.(*execStmtResult).Next(0xc011c4f140?, {0x40d68d0?, 0xc011c4f170?}, 0xc011c0ae00?)
   > 	<autogenerated>:1 +0x34 fp=0xc011d44e30 sp=0xc011d44e00 pc=0x31b8c94
   > github.com/pingcap/tidb/server.(*tidbResultSet).Next(0x1060384e0?, {0x40d68d0?, 0xc011c4f170?}, 0x40ee040?)
   > 	/go/src/github.com/pingcap/tidb/server/driver_tidb.go:317 +0x2b fp=0xc011d44e60 sp=0xc011d44e30 pc=0x323ac6b
   > github.com/pingcap/tidb/server.(*clientConn).writeChunks(0xc010ccf180, {0x40d68d0, 0xc011c4f170}, {0x40dff58, 0xc011d97630}, 0x0, 0x11d4?)
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:2185 +0x15e fp=0xc011d44f20 sp=0xc011d44e60 pc=0x3231d7e
   > github.com/pingcap/tidb/server.(*clientConn).writeResultset(0xc010ccf180, {0x40d68d0, 0xc011c4f170}, {0x40dff58, 0xc011d97630}, 0x0?, 0x3, 0xc010c7d088?)
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:2136 +0x23e fp=0xc011d44fd0 sp=0xc011d44f20 pc=0x323157e
   > github.com/pingcap/tidb/server.(*clientConn).handleStmt(0xc010ccf180, {0x40d6828, 0xc0116959c0}, {0x40e9b80, 0xc00055d560}, {0x606b430, 0x0, 0x0}, 0x1)
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:2014 +0x3c8 fp=0xc011d45098 sp=0xc011d44fd0 pc=0x32302c8
   > github.com/pingcap/tidb/server.(*clientConn).handleQuery(0xc010ccf180, {0x40d6828, 0xc0116959c0}, {0xc000165b01, 0x44c})
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:1850 +0x774 fp=0xc011d45260 sp=0xc011d45098 pc=0x322ea14
   > github.com/pingcap/tidb/server.(*clientConn).dispatch(0xc010ccf180, {0x40d68d0?, 0xc010cb7740?}, {0xc000165b00, 0x44d, 0x44d})
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:1345 +0x1025 fp=0xc011d45650 sp=0xc011d45260 pc=0x322a305
   > github.com/pingcap/tidb/server.(*clientConn).Run(0xc010ccf180, {0x40d68d0, 0xc010cb7740})
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:1095 +0x253 fp=0xc011d45c58 sp=0xc011d45650 pc=0x3226c53
   > github.com/pingcap/tidb/server.(*Server).onConn(0xc011778270, 0xc010ccf180)
   > 	/go/src/github.com/pingcap/tidb/server/server.go:551 +0x6c5 fp=0xc011d45fc0 sp=0xc011d45c58 pc=0x3259da5
   > github.com/pingcap/tidb/server.(*Server).startNetworkListener.func2()
   > 	/go/src/github.com/pingcap/tidb/server/server.go:448 +0x2a fp=0xc011d45fe0 sp=0xc011d45fc0 pc=0x3258c2a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc011d45fe8 sp=0xc011d45fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/server.(*Server).startNetworkListener
   > 	/go/src/github.com/pingcap/tidb/server/server.go:448 +0x5ca
   > goroutine 6614 [select]:
   > runtime.gopark(0xc0000a2f28?, 0x2?, 0x10?, 0x0?, 0xc0000a2eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0000a2d58 sp=0xc0000a2d38 pc=0x13c9516
   > runtime.selectgo(0xc0000a2f28, 0xc0000a2ee8, 0x60384e0?, 0x0, 0xc0136cdf90?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0000a2e98 sp=0xc0000a2d58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc01343bc00, {0x4134ba0, 0xc000560900}, 0xc01346f6e0, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc0000a2fa8 sp=0xc0000a2e98 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc0000a2fe0 sp=0xc0000a2fa8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000a2fe8 sp=0xc0000a2fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 6679 [select]:
   > runtime.gopark(0xc011855f00?, 0x2?, 0x30?, 0xc6?, 0xc011855e44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc011855c48 sp=0xc011855c28 pc=0x13c9516
   > runtime.selectgo(0xc011855f00, 0xc011855e40, 0x1392a11?, 0x0, 0xc011855e70?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc011855d88 sp=0xc011855c48 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc013810700, {0x4134ba0, 0xc000560900})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc011855f30 sp=0xc011855d88 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc013810700, {0x4134ba0, 0xc000560900}, 0xc0138021b0)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc011855fb0 sp=0xc011855f30 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc011855fe0 sp=0xc011855fb0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc011855fe8 sp=0xc011855fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 6447 [select]:
   > runtime.gopark(0xc01201ef28?, 0x2?, 0xb8?, 0xed?, 0xc01201eeec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01201ed58 sp=0xc01201ed38 pc=0x13c9516
   > runtime.selectgo(0xc01201ef28, 0xc01201eee8, 0x3b67af1?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01201ee98 sp=0xc01201ed58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc013810180, {0x4134ba0, 0xc000560900}, 0xc0138021a0, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc01201efa8 sp=0xc01201ee98 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc01201efe0 sp=0xc01201efa8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01201efe8 sp=0xc01201efe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 6449 [select]:
   > runtime.gopark(0xc011926f28?, 0x2?, 0xc7?, 0x95?, 0xc011926eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc011926d58 sp=0xc011926d38 pc=0x13c9516
   > runtime.selectgo(0xc011926f28, 0xc011926ee8, 0xc011926f10?, 0x0, 0xc012a5ff80?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc011926e98 sp=0xc011926d58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc013810300, {0x4134ba0, 0xc000560900}, 0xc0138021a0, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc011926fa8 sp=0xc011926e98 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc011926fe0 sp=0xc011926fa8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc011926fe8 sp=0xc011926fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 6639 [select]:
   > runtime.gopark(0xc011876778?, 0x2?, 0xbb?, 0xe8?, 0xc0118766ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc011876558 sp=0xc011876538 pc=0x13c9516
   > runtime.selectgo(0xc011876778, 0xc0118766e8, 0x3b67af1?, 0x0, 0xc011876708?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc011876698 sp=0xc011876558 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc01350ff80, {0x40d68d0?, 0xc011c4f170?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc0118767b8 sp=0xc011876698 pc=0x30ecdf4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc0118767e0 sp=0xc0118767b8 pc=0x30ec08e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0118767e8 sp=0xc0118767e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 6638 [select]:
   > runtime.gopark(0xc011877f78?, 0x2?, 0x8?, 0x30?, 0xc011877eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc011877d58 sp=0xc011877d38 pc=0x13c9516
   > runtime.selectgo(0xc011877f78, 0xc011877ee8, 0x3b67af1?, 0x0, 0xc01187a000?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc011877e98 sp=0xc011877d58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc01350ff40, {0x40d68d0?, 0xc011c4f170?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc011877fb8 sp=0xc011877e98 pc=0x30ecdf4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc011877fe0 sp=0xc011877fb8 pc=0x30ec08e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc011877fe8 sp=0xc011877fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 6640 [select]:
   > runtime.gopark(0xc00fa5cf78?, 0x2?, 0x78?, 0xcd?, 0xc00fa5ceec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fa5cd58 sp=0xc00fa5cd38 pc=0x13c9516
   > runtime.selectgo(0xc00fa5cf78, 0xc00fa5cee8, 0x3b67af1?, 0x0, 0x40ee3a0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fa5ce98 sp=0xc00fa5cd58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc01350ffc0, {0x40d68d0?, 0xc011c4f170?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc00fa5cfb8 sp=0xc00fa5ce98 pc=0x30ecdf4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc00fa5cfe0 sp=0xc00fa5cfb8 pc=0x30ec08e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fa5cfe8 sp=0xc00fa5cfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 6598 [chan receive]:
   > runtime.gopark(0xc0138068a0?, 0xc0006ac820?, 0x6d?, 0xcb?, 0xc012f9b448?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc012f9b3a0 sp=0xc012f9b380 pc=0x13c9516
   > runtime.chanrecv(0xc01380e000, 0xc012f9b478, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc012f9b430 sp=0xc012f9b3a0 pc=0x13934bb
   > runtime.chanrecv2(0xc010e20e00?, 0x40d68d0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc012f9b458 sp=0xc012f9b430 pc=0x1392ff8
   > github.com/pingcap/tidb/executor.(*HashAggExec).parallelExec(0xc010e20e00, {0x40d68d0?, 0xc011c4f170?}, 0xc01380a870)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:888 +0x89 fp=0xc012f9b490 sp=0xc012f9b458 pc=0x2fbcf29
   > github.com/pingcap/tidb/executor.(*HashAggExec).Next(0x40d68d0?, {0x40d68d0?, 0xc011c4f170?}, 0xc012f9b540?)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:768 +0x76 fp=0xc012f9b4c0 sp=0xc012f9b490 pc=0x2fbbeb6
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc011c4f170}, {0x40d9120, 0xc010e20e00}, 0xc01380a870)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc012f9b600 sp=0xc012f9b4c0 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*MaxOneRowExec).Next(0xc011d8ecb0, {0x40d68d0, 0xc011c4f170}, 0xc01380a870)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1518 +0xa8 fp=0xc012f9b650 sp=0xc012f9b600 pc=0x30413a8
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc011c4f170}, {0x40d94a0, 0xc011d8ecb0}, 0xc01380a870)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc012f9b790 sp=0xc012f9b650 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*SelectionExec).Next(0xc010c4b380, {0x40d68d0, 0xc011c4f170}, 0xc012ad9130)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1394 +0xed fp=0xc012f9b820 sp=0xc012f9b790 pc=0x304012d
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc011c4f170}, {0x40d9960, 0xc010c4b380}, 0xc012ad9130)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc012f9b960 sp=0xc012f9b820 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*NestedLoopApplyExec).fetchAllInners(0xc01164cc40, {0x40d68d0, 0xc011c4f170})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:979 +0x346 fp=0xc012f9ba58 sp=0xc012f9b960 pc=0x30b2966
   > github.com/pingcap/tidb/executor.(*NestedLoopApplyExec).Next(0xc01164cc40, {0x40d68d0, 0xc011c4f170}, 0xc012ad9180)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:1032 +0x5b6 fp=0xc012f9bbb8 sp=0xc012f9ba58 pc=0x30b32b6
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc011c4f170}, {0x40d9560, 0xc01164cc40}, 0xc012ad9180)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc012f9bcf8 sp=0xc012f9bbb8 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*ProjectionExec).unParallelExecute(0xc011d8ad80, {0x40d68d0?, 0xc011c4f170?}, 0xc012ad8f50)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:194 +0xb8 fp=0xc012f9bd48 sp=0xc012f9bcf8 pc=0x30eb458
   > github.com/pingcap/tidb/executor.(*ProjectionExec).Next(0xc011d8ad80, {0x40d68d0, 0xc011c4f170}, 0xc012f9bf0c?)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:180 +0x5a fp=0xc012f9bd80 sp=0xc012f9bd48 pc=0x30eb31a
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc011c4f170}, {0x40d9720, 0xc011d8ad80}, 0xc012ad8f50)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc012f9bec0 sp=0xc012f9bd80 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*UnionExec).resultPuller(0xc010cf9100, {0x40d68d0, 0xc011c4f170}, 0x0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1673 +0x48f fp=0xc012f9bfb0 sp=0xc012f9bec0 pc=0x30420ef
   > github.com/pingcap/tidb/executor.(*UnionExec).initialize.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1623 +0x32 fp=0xc012f9bfe0 sp=0xc012f9bfb0 pc=0x3041c32
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc012f9bfe8 sp=0xc012f9bfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*UnionExec).initialize
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1623 +0x233
   > goroutine 6615 [select]:
   > runtime.gopark(0xc012046728?, 0x2?, 0x7b?, 0x82?, 0xc0120466ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc012046558 sp=0xc012046538 pc=0x13c9516
   > runtime.selectgo(0xc012046728, 0xc0120466e8, 0x60384e0?, 0x0, 0xc01253dc20?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc012046698 sp=0xc012046558 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc01343bcc0, {0x4134ba0, 0xc000560900}, 0xc01346f6e0, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc0120467a8 sp=0xc012046698 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc0120467e0 sp=0xc0120467a8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0120467e8 sp=0xc0120467e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 6621 [select]:
   > runtime.gopark(0xc011929f00?, 0x2?, 0x8?, 0x0?, 0xc011929e44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc011929c48 sp=0xc011929c28 pc=0x13c9516
   > runtime.selectgo(0xc011929f00, 0xc011929e40, 0x4?, 0x0, 0xc00054d110?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc011929d88 sp=0xc011929c48 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc01367a0c0, {0x4134ba0, 0xc000560900})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc011929f30 sp=0xc011929d88 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc01367a0c0, {0x4134ba0, 0xc000560900}, 0xc01346f6f0)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc011929fb0 sp=0xc011929f30 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc011929fe0 sp=0xc011929fb0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc011929fe8 sp=0xc011929fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 6682 [semacquire]:
   > runtime.gopark(0x105fef25b178?, 0x0?, 0x40?, 0xab?, 0xc01322ccc0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc012423558 sp=0xc012423538 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc0005723a4, 0xe0?, 0x3, 0x1)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc0124235c0 sp=0xc012423558 pc=0x13dae5e
   > sync.runtime_SemacquireMutex(0x139a1bf?, 0x60?, 0x50?)
   > 	/usr/local/go/src/runtime/sema.go:77 +0x25 fp=0xc0124235f0 sp=0xc0124235c0 pc=0x13f8085
   > sync.(*Mutex).lockSlow(0xc0005723a0)
   > 	/usr/local/go/src/sync/mutex.go:171 +0x165 fp=0xc012423640 sp=0xc0124235f0 pc=0x1409825
   > sync.(*Mutex).Lock(...)
   > 	/usr/local/go/src/sync/mutex.go:90
   > github.com/pingcap/tidb/util/memory.(*Tracker).FallbackOldAndSetNewAction(0xc000572390, {0x40dbc60?, 0xc0136dd860?})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:162 +0x68 fp=0xc012423698 sp=0xc012423640 pc=0x1fb3308
   > github.com/pingcap/tidb/store/copr.(*CopClient).Send(0xc011a41530, {0x40d68d0, 0xc011c4f170}, 0xc01185f000, {0x3565ba0?, 0xc0003ff8f0?}, 0xc0131faec0)
   > 	/go/src/github.com/pingcap/tidb/store/copr/coprocessor.go:137 +0x857 fp=0xc012423860 sp=0xc012423698 pc=0x249aff7
   > github.com/pingcap/tidb/distsql.Select({0x40d68d0, 0xc011c4f170}, {0x4134ba0?, 0xc000560900}, 0xc01185f000, {0xc011d81e00, 0x9, 0x9}, 0xc011d81e50)
   > 	/go/src/github.com/pingcap/tidb/distsql/distsql.go:101 +0x5bf fp=0xc0124239a0 sp=0xc012423860 pc=0x26aa0df
   > github.com/pingcap/tidb/distsql.SelectWithRuntimeStats({0x40d68d0?, 0xc011c4f170?}, {0x4134ba0?, 0xc000560900?}, 0xc012423a60?, {0xc011d81e00?, 0x8?, 0x35d4e20?}, 0x1?, {0xc0135d1750, ...}, ...)
   > 	/go/src/github.com/pingcap/tidb/distsql/distsql.go:150 +0x45 fp=0xc0124239f8 sp=0xc0124239a0 pc=0x26aaa65
   > github.com/pingcap/tidb/executor.selectResultHook.SelectResult({0x1?}, {0x40d68d0?, 0xc011c4f170?}, {0x4134ba0?, 0xc000560900?}, 0x13bfab0?, {0xc011d81e00?, 0x100?, 0x1?}, 0xc011d81e50, ...)
   > 	/go/src/github.com/pingcap/tidb/executor/table_reader.go:53 +0xf0 fp=0xc012423a70 sp=0xc0124239f8 pc=0x313eb90
   > github.com/pingcap/tidb/executor.(*TableReaderExecutor).buildResp(0xc0107b7b00, {0x40d68d0, 0xc011c4f170}, {0xc011010f28?, 0x8?, 0xc01240f564?})
   > 	/go/src/github.com/pingcap/tidb/executor/table_reader.go:300 +0x3d6 fp=0xc012423c38 sp=0xc012423a70 pc=0x3140456
   > github.com/pingcap/tidb/executor.(*TableReaderExecutor).Open(0xc0107b7b00, {0x40d68d0, 0xc011c4f170})
   > 	/go/src/github.com/pingcap/tidb/executor/table_reader.go:199 +0xa99 fp=0xc012423d50 sp=0xc012423c38 pc=0x313f6d9
   > github.com/pingcap/tidb/executor.(*baseExecutor).Open(...)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:185
   > github.com/pingcap/tidb/executor.(*SelectionExec).Open(0xc010c4b1e0?, {0x40d68d0?, 0xc011c4f170?})
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1338 +0xa2 fp=0xc012423d90 sp=0xc012423d50 pc=0x303fbe2
   > github.com/pingcap/tidb/executor.(*CTEExec).Open(0xc011b03a40, {0x40d68d0, 0xc011c4f170})
   > 	/go/src/github.com/pingcap/tidb/executor/cte.go:109 +0xf2 fp=0xc012423e40 sp=0xc012423d90 pc=0x3022212
   > github.com/pingcap/tidb/executor.(*baseExecutor).Open(...)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:185
   > github.com/pingcap/tidb/executor.(*SelectionExec).Open(0xc010c4b2b0?, {0x40d68d0?, 0xc011c4f170?})
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1338 +0xa2 fp=0xc012423e80 sp=0xc012423e40 pc=0x303fbe2
   > github.com/pingcap/tidb/executor.(*baseExecutor).Open(...)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:185
   > github.com/pingcap/tidb/executor.(*ProjectionExec).Open(0xc011d8ab40?, {0x40d68d0?, 0xc011c4f170?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:87 +0xa2 fp=0xc012423ec0 sp=0xc012423e80 pc=0x30eb022
   > github.com/pingcap/tidb/executor.(*UnionExec).resultPuller(0xc010cf8f00, {0x40d68d0, 0xc011c4f170}, 0x0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1656 +0x237 fp=0xc012423fb0 sp=0xc012423ec0 pc=0x3041e97
   > github.com/pingcap/tidb/executor.(*UnionExec).initialize.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1623 +0x32 fp=0xc012423fe0 sp=0xc012423fb0 pc=0x3041c32
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc012423fe8 sp=0xc012423fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*UnionExec).initialize
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1623 +0x233
   > goroutine 6677 [select]:
   > runtime.gopark(0xc011925f00?, 0x2?, 0xe0?, 0xa0?, 0xc011925e44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc011925c48 sp=0xc011925c28 pc=0x13c9516
   > runtime.selectgo(0xc011925f00, 0xc011925e40, 0x3980?, 0x0, 0x6043ac0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc011925d88 sp=0xc011925c48 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc013810580, {0x4134ba0, 0xc000560900})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc011925f30 sp=0xc011925d88 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc013810580, {0x4134ba0, 0xc000560900}, 0xc0138021b0)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc011925fb0 sp=0xc011925f30 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc011925fe0 sp=0xc011925fb0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc011925fe8 sp=0xc011925fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 6623 [select]:
   > runtime.gopark(0xc011872700?, 0x2?, 0x0?, 0x0?, 0xc011872644?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc011872448 sp=0xc011872428 pc=0x13c9516
   > runtime.selectgo(0xc011872700, 0xc011872640, 0x1392a11?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc011872588 sp=0xc011872448 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc01367a240, {0x4134ba0, 0xc000560900})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc011872730 sp=0xc011872588 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc01367a240, {0x4134ba0, 0xc000560900}, 0xc01346f6f0)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc0118727b0 sp=0xc011872730 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc0118727e0 sp=0xc0118727b0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0118727e8 sp=0xc0118727e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 6620 [select]:
   > runtime.gopark(0xc011928700?, 0x2?, 0x0?, 0x0?, 0xc011928644?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc011928448 sp=0xc011928428 pc=0x13c9516
   > runtime.selectgo(0xc011928700, 0xc011928640, 0xc0119285e8?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc011928588 sp=0xc011928448 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc01367a000, {0x4134ba0, 0xc000560900})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc011928730 sp=0xc011928588 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc01367a000, {0x4134ba0, 0xc000560900}, 0xc01346f6f0)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc0119287b0 sp=0xc011928730 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc0119287e0 sp=0xc0119287b0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0119287e8 sp=0xc0119287e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 6658 [semacquire]:
   > runtime.gopark(0xc0134eeb08?, 0x0?, 0x20?, 0x9f?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc011e47eb8 sp=0xc011e47e98 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc01346f6d8, 0xe5?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc011e47f20 sp=0xc011e47eb8 pc=0x13dae5e
   > sync.runtime_Semacquire(0x100010000?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc011e47f50 sp=0xc011e47f20 pc=0x13f7f65
   > sync.(*WaitGroup).Wait(0xc1991f52159f439b?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc011e47f78 sp=0xc011e47f50 pc=0x140b312
   > github.com/pingcap/tidb/executor.(*HashAggExec).waitAllWorkersAndCloseFinalOutputCh(0xc010e21000, {0xc011e47fb8, 0x3, 0xc01359b700?})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:827 +0x35 fp=0xc011e47f98 sp=0xc011e47f78 pc=0x2fbc5b5
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func6()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:864 +0x5a fp=0xc011e47fe0 sp=0xc011e47f98 pc=0x2fbcc1a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc011e47fe8 sp=0xc011e47fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:864 +0x54d
   > goroutine 6632 [semacquire]:
   > runtime.gopark(0xc000572060?, 0x0?, 0x0?, 0x46?, 0x60384e0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0126966f0 sp=0xc0126966d0 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc010cf90d0, 0x60?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc012696758 sp=0xc0126966f0 pc=0x13dae5e
   > sync.runtime_Semacquire(0xc012b9b900?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc012696788 sp=0xc012696758 pc=0x13f7f65
   > sync.(*WaitGroup).Wait(0x4134ba0?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc0126967b0 sp=0xc012696788 pc=0x140b312
   > github.com/pingcap/tidb/executor.(*UnionExec).waitAllFinished(0xc010cf9000)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1595 +0x2a fp=0xc0126967c8 sp=0xc0126967b0 pc=0x30415ea
   > github.com/pingcap/tidb/executor.(*UnionExec).initialize.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1629 +0x26 fp=0xc0126967e0 sp=0xc0126967c8 pc=0x3041bc6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0126967e8 sp=0xc0126967e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*UnionExec).initialize
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1629 +0x40b
   > goroutine 6636 [select]:
   > runtime.gopark(0xc000f9af78?, 0x2?, 0xa0?, 0xad?, 0xc000f9aeec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000f9ad58 sp=0xc000f9ad38 pc=0x13c9516
   > runtime.selectgo(0xc000f9af78, 0xc000f9aee8, 0xc000560900?, 0x0, 0x30420ef?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000f9ae98 sp=0xc000f9ad58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc01350fec0, {0x40d68d0?, 0xc011c4f170?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc000f9afb8 sp=0xc000f9ae98 pc=0x30ecdf4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc000f9afe0 sp=0xc000f9afb8 pc=0x30ec08e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000f9afe8 sp=0xc000f9afe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 6637 [select]:
   > runtime.gopark(0xc0006c2778?, 0x2?, 0xf6?, 0x42?, 0xc0006c26ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0006c2558 sp=0xc0006c2538 pc=0x13c9516
   > runtime.selectgo(0xc0006c2778, 0xc0006c26e8, 0x3b67af1?, 0x0, 0xc0118375c0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0006c2698 sp=0xc0006c2558 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc01350ff00, {0x40d68d0?, 0xc011c4f170?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc0006c27b8 sp=0xc0006c2698 pc=0x30ecdf4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc0006c27e0 sp=0xc0006c27b8 pc=0x30ec08e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0006c27e8 sp=0xc0006c27e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 6600 [semacquire]:
   > runtime.gopark(0x40d9ea0?, 0x0?, 0xe0?, 0x50?, 0x249ca01?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0118736f0 sp=0xc0118736d0 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc010cf91d0, 0x60?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc011873758 sp=0xc0118736f0 pc=0x13dae5e
   > sync.runtime_Semacquire(0xc012e00cc0?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc011873788 sp=0xc011873758 pc=0x13f7f65
   > sync.(*WaitGroup).Wait(0x30ec08e?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc0118737b0 sp=0xc011873788 pc=0x140b312
   > github.com/pingcap/tidb/executor.(*UnionExec).waitAllFinished(0xc010cf9100)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1595 +0x2a fp=0xc0118737c8 sp=0xc0118737b0 pc=0x30415ea
   > github.com/pingcap/tidb/executor.(*UnionExec).initialize.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1629 +0x26 fp=0xc0118737e0 sp=0xc0118737c8 pc=0x3041bc6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0118737e8 sp=0xc0118737e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*UnionExec).initialize
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1629 +0x40b
   > goroutine 6678 [select]:
   > runtime.gopark(0xc0006c1700?, 0x2?, 0xe0?, 0xa0?, 0xc0006c1644?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0006c1448 sp=0xc0006c1428 pc=0x13c9516
   > runtime.selectgo(0xc0006c1700, 0xc0006c1640, 0x4?, 0x0, 0xc00054d110?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0006c1588 sp=0xc0006c1448 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc013810640, {0x4134ba0, 0xc000560900})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc0006c1730 sp=0xc0006c1588 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc013810640, {0x4134ba0, 0xc000560900}, 0xc0138021b0)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc0006c17b0 sp=0xc0006c1730 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc0006c17e0 sp=0xc0006c17b0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0006c17e8 sp=0xc0006c17e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 6599 [chan receive]:
   > runtime.gopark(0xc013782390?, 0xc01240b040?, 0x6d?, 0xcb?, 0xc013719448?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0137193a0 sp=0xc013719380 pc=0x13c9516
   > runtime.chanrecv(0xc012adefc0, 0xc013719478, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc013719430 sp=0xc0137193a0 pc=0x13934bb
   > runtime.chanrecv2(0xc010e21000?, 0x40d68d0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc013719458 sp=0xc013719430 pc=0x1392ff8
   > github.com/pingcap/tidb/executor.(*HashAggExec).parallelExec(0xc010e21000, {0x40d68d0?, 0xc011c4f170?}, 0xc01367c780)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:888 +0x89 fp=0xc013719490 sp=0xc013719458 pc=0x2fbcf29
   > github.com/pingcap/tidb/executor.(*HashAggExec).Next(0x40d68d0?, {0x40d68d0?, 0xc011c4f170?}, 0x0?)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:768 +0x76 fp=0xc0137194c0 sp=0xc013719490 pc=0x2fbbeb6
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc011c4f170}, {0x40d9120, 0xc010e21000}, 0xc01367c780)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc013719600 sp=0xc0137194c0 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*MaxOneRowExec).Next(0xc011d8f500, {0x40d68d0, 0xc011c4f170}, 0xc01367c780)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1518 +0xa8 fp=0xc013719650 sp=0xc013719600 pc=0x30413a8
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc011c4f170}, {0x40d94a0, 0xc011d8f500}, 0xc01367c780)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc013719790 sp=0xc013719650 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*SelectionExec).Next(0xc010c4b790, {0x40d68d0, 0xc011c4f170}, 0xc013769ae0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1394 +0xed fp=0xc013719820 sp=0xc013719790 pc=0x304012d
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc011c4f170}, {0x40d9960, 0xc010c4b790}, 0xc013769ae0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc013719960 sp=0xc013719820 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*NestedLoopApplyExec).fetchAllInners(0xc01164ce00, {0x40d68d0, 0xc011c4f170})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:979 +0x346 fp=0xc013719a58 sp=0xc013719960 pc=0x30b2966
   > github.com/pingcap/tidb/executor.(*NestedLoopApplyExec).Next(0xc01164ce00, {0x40d68d0, 0xc011c4f170}, 0xc013769b80)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:1032 +0x5b6 fp=0xc013719bb8 sp=0xc013719a58 pc=0x30b32b6
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc011c4f170}, {0x40d9560, 0xc01164ce00}, 0xc013769b80)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc013719cf8 sp=0xc013719bb8 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*ProjectionExec).unParallelExecute(0xc011d8b0e0, {0x40d68d0?, 0xc011c4f170?}, 0xc012ad8fa0)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:194 +0xb8 fp=0xc013719d48 sp=0xc013719cf8 pc=0x30eb458
   > github.com/pingcap/tidb/executor.(*ProjectionExec).Next(0xc011d8b0e0, {0x40d68d0, 0xc011c4f170}, 0xc0132bbf0c?)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:180 +0x5a fp=0xc013719d80 sp=0xc013719d48 pc=0x30eb31a
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc011c4f170}, {0x40d9720, 0xc011d8b0e0}, 0xc012ad8fa0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc013719ec0 sp=0xc013719d80 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*UnionExec).resultPuller(0xc010cf9100, {0x40d68d0, 0xc011c4f170}, 0x1)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1673 +0x48f fp=0xc013719fb0 sp=0xc013719ec0 pc=0x30420ef
   > github.com/pingcap/tidb/executor.(*UnionExec).initialize.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1623 +0x32 fp=0xc013719fe0 sp=0xc013719fb0 pc=0x3041c32
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc013719fe8 sp=0xc013719fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*UnionExec).initialize
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1623 +0x233
   > goroutine 6617 [select]:
   > runtime.gopark(0xc011878728?, 0x2?, 0x20?, 0x4a?, 0xc0118786ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc011878558 sp=0xc011878538 pc=0x13c9516
   > runtime.selectgo(0xc011878728, 0xc0118786e8, 0x60384e0?, 0x0, 0xc0006a5308?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc011878698 sp=0xc011878558 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc01343be40, {0x4134ba0, 0xc000560900}, 0xc01346f6e0, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc0118787a8 sp=0xc011878698 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc0118787e0 sp=0xc0118787a8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0118787e8 sp=0xc0118787e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 6676 [select]:
   > runtime.gopark(0xc011e44f00?, 0x2?, 0x8?, 0x0?, 0xc011e44e44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc011e44c48 sp=0xc011e44c28 pc=0x13c9516
   > runtime.selectgo(0xc011e44f00, 0xc011e44e40, 0xc011e44f0c?, 0x0, 0x1fb5214?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc011e44d88 sp=0xc011e44c48 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc0138104c0, {0x4134ba0, 0xc000560900})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc011e44f30 sp=0xc011e44d88 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc0138104c0, {0x4134ba0, 0xc000560900}, 0xc0138021b0)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc011e44fb0 sp=0xc011e44f30 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc011e44fe0 sp=0xc011e44fb0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc011e44fe8 sp=0xc011e44fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 6446 [select]:
   > runtime.gopark(0xc010fe7f28?, 0x2?, 0x90?, 0x7d?, 0xc010fe7eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010fe7d58 sp=0xc010fe7d38 pc=0x13c9516
   > runtime.selectgo(0xc010fe7f28, 0xc010fe7ee8, 0x3b67af1?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010fe7e98 sp=0xc010fe7d58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc0138100c0, {0x4134ba0, 0xc000560900}, 0xc0138021a0, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc010fe7fa8 sp=0xc010fe7e98 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc010fe7fe0 sp=0xc010fe7fa8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010fe7fe8 sp=0xc010fe7fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 6674 [semacquire]:
   > runtime.gopark(0x2fb8f3f?, 0x0?, 0x0?, 0x35?, 0x60384e0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01240c690 sp=0xc01240c670 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc0138021a8, 0x20?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc01240c6f8 sp=0xc01240c690 pc=0x13dae5e
   > sync.runtime_Semacquire(0x2fbbce5?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc01240c728 sp=0xc01240c6f8 pc=0x13f7f65
   > sync.(*WaitGroup).Wait(0xc01377e300?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc01240c750 sp=0xc01240c728 pc=0x140b312
   > github.com/pingcap/tidb/executor.(*HashAggExec).waitPartialWorkerAndCloseOutputChs(0xc010e20e00, 0xc01240c7d0?)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:815 +0x25 fp=0xc01240c798 sp=0xc01240c750 pc=0x2fbc465
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:844 +0x45 fp=0xc01240c7e0 sp=0xc01240c798 pc=0x2fbcd85
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01240c7e8 sp=0xc01240c7e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:843 +0x2e5
   > goroutine 6675 [select]:
   > runtime.gopark(0xc011874700?, 0x2?, 0xe0?, 0xa0?, 0xc011874644?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc011874448 sp=0xc011874428 pc=0x13c9516
   > runtime.selectgo(0xc011874700, 0xc011874640, 0x60384e0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc011874588 sp=0xc011874448 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc013810400, {0x4134ba0, 0xc000560900})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc011874730 sp=0xc011874588 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc013810400, {0x4134ba0, 0xc000560900}, 0xc0138021b0)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc0118747b0 sp=0xc011874730 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc0118747e0 sp=0xc0118747b0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0118747e8 sp=0xc0118747e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 6631 [chan receive]:
   > runtime.gopark(0x355a760?, 0xc0136c3d20?, 0xb0?, 0x24?, 0xc01377b740?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0136c3c48 sp=0xc0136c3c28 pc=0x13c9516
   > runtime.chanrecv(0xc01377b3e0, 0xc0136c3d28, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc0136c3cd8 sp=0xc0136c3c48 pc=0x13934bb
   > runtime.chanrecv1(0xc0136c3d38?, 0x142ce14?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc0136c3d00 sp=0xc0136c3cd8 pc=0x1392fb8
   > github.com/pingcap/tidb/executor.(*ProjectionExec).parallelExecute(0xc011d8afc0, {0x40d68d0?, 0xc011c4f170?}, 0xc013769e00)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:218 +0x92 fp=0xc0136c3d48 sp=0xc0136c3d00 pc=0x30eb612
   > github.com/pingcap/tidb/executor.(*ProjectionExec).Next(0xc011d8afc0, {0x40d68d0, 0xc011c4f170}, 0xc0136c3f0c?)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:182 +0x78 fp=0xc0136c3d80 sp=0xc0136c3d48 pc=0x30eb338
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc011c4f170}, {0x40d9720, 0xc011d8afc0}, 0xc013769e00)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc0136c3ec0 sp=0xc0136c3d80 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*UnionExec).resultPuller(0xc010cf9000, {0x40d68d0, 0xc011c4f170}, 0x1)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1673 +0x48f fp=0xc0136c3fb0 sp=0xc0136c3ec0 pc=0x30420ef
   > github.com/pingcap/tidb/executor.(*UnionExec).initialize.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1623 +0x32 fp=0xc0136c3fe0 sp=0xc0136c3fb0 pc=0x3041c32
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0136c3fe8 sp=0xc0136c3fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*UnionExec).initialize
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1623 +0x233
   > goroutine 6448 [select]:
   > runtime.gopark(0xc010fe6f28?, 0x2?, 0xb4?, 0xec?, 0xc010fe6eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010fe6d58 sp=0xc010fe6d38 pc=0x13c9516
   > runtime.selectgo(0xc010fe6f28, 0xc010fe6ee8, 0x3b67af1?, 0x0, 0xc0127427e0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010fe6e98 sp=0xc010fe6d58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc013810240, {0x4134ba0, 0xc000560900}, 0xc0138021a0, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc010fe6fa8 sp=0xc010fe6e98 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc010fe6fe0 sp=0xc010fe6fa8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010fe6fe8 sp=0xc010fe6fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 6445 [select]:
   > runtime.gopark(0xc011872f28?, 0x2?, 0xc9?, 0xd6?, 0xc011872eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc011872d58 sp=0xc011872d38 pc=0x13c9516
   > runtime.selectgo(0xc011872f28, 0xc011872ee8, 0x3b67af1?, 0x0, 0xc011872f08?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc011872e98 sp=0xc011872d58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc013810000, {0x4134ba0, 0xc000560900}, 0xc0138021a0, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc011872fa8 sp=0xc011872e98 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc011872fe0 sp=0xc011872fa8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc011872fe8 sp=0xc011872fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 6684 [semacquire]:
   > runtime.gopark(0x1000000040d9ea0?, 0x1?, 0x0?, 0x75?, 0x100000001?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0006c1ef0 sp=0xc0006c1ed0 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc010cf8fd0, 0xe0?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc0006c1f58 sp=0xc0006c1ef0 pc=0x13dae5e
   > sync.runtime_Semacquire(0xc0135da000?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc0006c1f88 sp=0xc0006c1f58 pc=0x13f7f65
   > sync.(*WaitGroup).Wait(0xc010cf8f00?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc0006c1fb0 sp=0xc0006c1f88 pc=0x140b312
   > github.com/pingcap/tidb/executor.(*UnionExec).waitAllFinished(0xc010cf8f00)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1595 +0x2a fp=0xc0006c1fc8 sp=0xc0006c1fb0 pc=0x30415ea
   > github.com/pingcap/tidb/executor.(*UnionExec).initialize.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1629 +0x26 fp=0xc0006c1fe0 sp=0xc0006c1fc8 pc=0x3041bc6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0006c1fe8 sp=0xc0006c1fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*UnionExec).initialize
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1629 +0x40b
