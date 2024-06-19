# Bug ID TIDB-36896-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/36896
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED


## Details
 * Database: tidb-v6.1.0
 * Number of scenarios: 1
 * Initial setup script: /home/theodor/Projects/MasterThesis/data/sql/TIDB-36896_mysql_bk.sql

## Results
### Scenario 0
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  START TRANSACTION;
     - TID: 0
     - Output: None
 * Instruction #2:
     - SQL:  WITH cte_0 AS (select ref_0.wkey as c0, ref_0.pkey as c1, ref_0.c_rrbxh as c2, ...
     - TID: 0
     - Output: ERROR: 2013 (HY000): Lost connection to MySQL server during query
 * Instruction #3:
     - SQL:  commit;
     - TID: 0
     - Output: Skipped due to previous error.

 * Container logs:
   > [2024/06/19 08:57:26.464 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/06/19 08:57:26.467 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=43] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/06/19 08:57:26.468 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:77, Type:drop schema, State:none, SchemaState:queueing, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:57:26.467 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/19 08:57:26.468 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:77, Type:drop schema, State:none, SchemaState:queueing, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:57:26.467 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/06/19 08:57:26.469 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:none, SchemaState:queueing, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:57:26.467 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:57:26.470 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=43] [neededSchemaVersion=44] ["start time"=74.731µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 08:57:26.472 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=44] ["take time"=2.13821ms] [job="ID:77, Type:drop schema, State:running, SchemaState:write only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:57:26.467 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:57:26.472 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:running, SchemaState:write only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:57:26.467 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:57:26.473 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=44] [neededSchemaVersion=45] ["start time"=81.995µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 08:57:26.475 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=45] ["take time"=2.278663ms] [job="ID:77, Type:drop schema, State:running, SchemaState:delete only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:57:26.467 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:57:26.475 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:running, SchemaState:delete only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:57:26.467 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:57:26.476 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=45] [neededSchemaVersion=46] ["start time"=93.518µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 08:57:26.478 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=46] ["take time"=2.155322ms] [job="ID:77, Type:drop schema, State:done, SchemaState:queueing, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:57:26.467 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:57:26.479 +00:00] [INFO] [delete_range.go:103] ["[ddl] add job into delete-range table"] [jobID=77] [jobType="drop schema"]
   > [2024/06/19 08:57:26.479 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:57:26.467 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:57:26.480 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=77]
   > [2024/06/19 08:57:26.480 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/19 08:57:26.481 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=46] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/06/19 08:57:26.483 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:79, Type:create schema, State:none, SchemaState:queueing, SchemaID:78, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 08:57:26.482 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/19 08:57:26.483 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:79, Type:create schema, State:none, SchemaState:queueing, SchemaID:78, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 08:57:26.482 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/19 08:57:26.483 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:79, Type:create schema, State:none, SchemaState:queueing, SchemaID:78, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:57:26.482 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:57:26.485 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=46] [neededSchemaVersion=47] ["start time"=141.011µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 08:57:26.487 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=47] ["take time"=2.313514ms] [job="ID:79, Type:create schema, State:done, SchemaState:public, SchemaID:78, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 08:57:26.482 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:57:26.488 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:79, Type:create schema, State:synced, SchemaState:public, SchemaID:78, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:57:26.482 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:57:26.488 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=79]
   > [2024/06/19 08:57:26.488 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/19 08:57:26.494 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=47] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_2el7jd`\n--\n\nDROP TABLE IF EXISTS `t_2el7jd`;"] [user=root@%]
   > [2024/06/19 08:57:26.495 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=47] [cur_db=testdb] [sql="CREATE TABLE `t_2el7jd` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_hzkgf` text DEFAULT NULL,\n  `c_si87c` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_alxrj` (`wkey`,`pkey`,`c_si87c`),\n  KEY `t_za4dpb` (`pkey`,`c_si87c`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/06/19 08:57:26.497 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:81, Type:create table, State:none, SchemaState:queueing, SchemaID:78, TableID:80, RowCount:0, ArgLen:1, start time: 2024-06-19 08:57:26.496 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/19 08:57:26.497 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:81, Type:create table, State:none, SchemaState:queueing, SchemaID:78, TableID:80, RowCount:0, ArgLen:1, start time: 2024-06-19 08:57:26.496 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_2el7jd` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_hzkgf` text DEFAULT NULL,\n  `c_si87c` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_alxrj` (`wkey`,`pkey`,`c_si87c`),\n  KEY `t_za4dpb` (`pkey`,`c_si87c`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/19 08:57:26.497 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:81, Type:create table, State:none, SchemaState:queueing, SchemaID:78, TableID:80, RowCount:0, ArgLen:0, start time: 2024-06-19 08:57:26.496 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:57:26.499 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=47] [neededSchemaVersion=48] ["start time"=388.251µs] [phyTblIDs="[80]"] [actionTypes="[8]"]
   > [2024/06/19 08:57:26.501 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=48] ["take time"=2.07207ms] [job="ID:81, Type:create table, State:done, SchemaState:public, SchemaID:78, TableID:80, RowCount:0, ArgLen:1, start time: 2024-06-19 08:57:26.496 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:57:26.502 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:81, Type:create table, State:synced, SchemaState:public, SchemaID:78, TableID:80, RowCount:0, ArgLen:0, start time: 2024-06-19 08:57:26.496 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:57:26.503 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=81]
   > [2024/06/19 08:57:26.503 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/19 08:57:26.503 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=68] ["first split key"=748000000000000050]
   > [2024/06/19 08:57:26.504 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=68] ["first at"=748000000000000050] ["first new region left"="{Id:68 StartKey:7480000000000000ff4a00000000000000f8 EndKey:7480000000000000ff5000000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:69 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/19 08:57:26.504 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[68]"]
   > [2024/06/19 08:57:26.504 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=48] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_2el7jd` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/19 08:57:26.507 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=48] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_2el7jd` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/19 08:57:26.507 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=48] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_p7c1bd`\n--\n\nDROP TABLE IF EXISTS `t_p7c1bd`;"] [user=root@%]
   > [2024/06/19 08:57:26.508 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=48] [cur_db=testdb] [sql="CREATE TABLE `t_p7c1bd` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_rrbxh` text DEFAULT NULL,\n  `c_c5cvkb` int(11) DEFAULT NULL,\n  `c_ag5ccc` int(11) DEFAULT NULL,\n  `c_qo4qvc` text DEFAULT NULL,\n  `c_lhs3h` int(11) DEFAULT NULL,\n  `c_8dah2b` int(11) DEFAULT NULL,\n  `c_eg6xsc` int(11) DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_s0z7f` (`c_ag5ccc`,`c_8dah2b`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/06/19 08:57:26.509 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:83, Type:create table, State:none, SchemaState:queueing, SchemaID:78, TableID:82, RowCount:0, ArgLen:1, start time: 2024-06-19 08:57:26.509 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/19 08:57:26.510 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:83, Type:create table, State:none, SchemaState:queueing, SchemaID:78, TableID:82, RowCount:0, ArgLen:1, start time: 2024-06-19 08:57:26.509 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_p7c1bd` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_rrbxh` text DEFAULT NULL,\n  `c_c5cvkb` int(11) DEFAULT NULL,\n  `c_ag5ccc` int(11) DEFAULT NULL,\n  `c_qo4qvc` text DEFAULT NULL,\n  `c_lhs3h` int(11) DEFAULT NULL,\n  `c_8dah2b` int(11) DEFAULT NULL,\n  `c_eg6xsc` int(11) DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_s0z7f` (`c_ag5ccc`,`c_8dah2b`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/19 08:57:26.510 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:83, Type:create table, State:none, SchemaState:queueing, SchemaID:78, TableID:82, RowCount:0, ArgLen:0, start time: 2024-06-19 08:57:26.509 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:57:26.513 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=48] [neededSchemaVersion=49] ["start time"=669.295µs] [phyTblIDs="[82]"] [actionTypes="[8]"]
   > [2024/06/19 08:57:26.514 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=49] ["take time"=2.267907ms] [job="ID:83, Type:create table, State:done, SchemaState:public, SchemaID:78, TableID:82, RowCount:0, ArgLen:1, start time: 2024-06-19 08:57:26.509 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:57:26.515 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:83, Type:create table, State:synced, SchemaState:public, SchemaID:78, TableID:82, RowCount:0, ArgLen:0, start time: 2024-06-19 08:57:26.509 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:57:26.517 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=83]
   > [2024/06/19 08:57:26.517 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/19 08:57:26.517 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=70] ["first split key"=748000000000000052]
   > [2024/06/19 08:57:26.517 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=70] ["first at"=748000000000000052] ["first new region left"="{Id:70 StartKey:7480000000000000ff5000000000000000f8 EndKey:7480000000000000ff5200000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:71 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/19 08:57:26.517 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[70]"]
   > [2024/06/19 08:57:26.518 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=49] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_p7c1bd` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/19 08:57:26.523 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=49] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_p7c1bd` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/19 08:57:27.549 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/06/19 08:57:27.560 +00:00] [INFO] [set.go:147] ["set global var"] [conn=413] [name=tx_isolation] [val=READ-COMMITTED]
   > runtime: goroutine stack exceeds 1000000000-byte limit
   > runtime: sp=0xc03e600368 stack=[0xc03e600000, 0xc05e600000]
   > fatal error: stack overflow
   > runtime stack:
   > runtime.throw({0x3b631a0?, 0x59e90a0?})
   > 	/usr/local/go/src/runtime/panic.go:1047 +0x5d fp=0x7f4c073dc888 sp=0x7f4c073dc858 pc=0x13c659d
   > runtime.newstack()
   > 	/usr/local/go/src/runtime/stack.go:1103 +0x5cc fp=0x7f4c073dca40 sp=0x7f4c073dc888 pc=0x13e15ec
   > runtime.morestack()
   > 	/usr/local/go/src/runtime/asm_amd64.s:570 +0x8b fp=0x7f4c073dca48 sp=0x7f4c073dca40 pc=0x13fa60b
   > goroutine 121912 [running]:
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60?, 0xc012806060?}, {0x40dbf60?, 0xc012806360?})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:183 +0x12c fp=0xc03e600378 sp=0xc03e600370 pc=0x1fb386c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e6003b0 sp=0xc03e600378 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e6003e8 sp=0xc03e6003b0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600420 sp=0xc03e6003e8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600458 sp=0xc03e600420 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600490 sp=0xc03e600458 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e6004c8 sp=0xc03e600490 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600500 sp=0xc03e6004c8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600538 sp=0xc03e600500 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600570 sp=0xc03e600538 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e6005a8 sp=0xc03e600570 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e6005e0 sp=0xc03e6005a8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600618 sp=0xc03e6005e0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600650 sp=0xc03e600618 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600688 sp=0xc03e600650 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e6006c0 sp=0xc03e600688 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e6006f8 sp=0xc03e6006c0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600730 sp=0xc03e6006f8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600768 sp=0xc03e600730 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e6007a0 sp=0xc03e600768 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e6007d8 sp=0xc03e6007a0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600810 sp=0xc03e6007d8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600848 sp=0xc03e600810 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600880 sp=0xc03e600848 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e6008b8 sp=0xc03e600880 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e6008f0 sp=0xc03e6008b8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600928 sp=0xc03e6008f0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600960 sp=0xc03e600928 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600998 sp=0xc03e600960 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e6009d0 sp=0xc03e600998 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600a08 sp=0xc03e6009d0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600a40 sp=0xc03e600a08 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600a78 sp=0xc03e600a40 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600ab0 sp=0xc03e600a78 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600ae8 sp=0xc03e600ab0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600b20 sp=0xc03e600ae8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600b58 sp=0xc03e600b20 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600b90 sp=0xc03e600b58 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600bc8 sp=0xc03e600b90 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600c00 sp=0xc03e600bc8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600c38 sp=0xc03e600c00 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600c70 sp=0xc03e600c38 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600ca8 sp=0xc03e600c70 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600ce0 sp=0xc03e600ca8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600d18 sp=0xc03e600ce0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600d50 sp=0xc03e600d18 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600d88 sp=0xc03e600d50 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600dc0 sp=0xc03e600d88 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600df8 sp=0xc03e600dc0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600e30 sp=0xc03e600df8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600e68 sp=0xc03e600e30 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600ea0 sp=0xc03e600e68 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600ed8 sp=0xc03e600ea0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600f10 sp=0xc03e600ed8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600f48 sp=0xc03e600f10 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600f80 sp=0xc03e600f48 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600fb8 sp=0xc03e600f80 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e600ff0 sp=0xc03e600fb8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e601028 sp=0xc03e600ff0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e601060 sp=0xc03e601028 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e601098 sp=0xc03e601060 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e6010d0 sp=0xc03e601098 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e601108 sp=0xc03e6010d0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e601140 sp=0xc03e601108 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e601178 sp=0xc03e601140 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e6011b0 sp=0xc03e601178 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e6011e8 sp=0xc03e6011b0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e601220 sp=0xc03e6011e8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e601258 sp=0xc03e601220 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e601290 sp=0xc03e601258 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e6012c8 sp=0xc03e601290 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e601300 sp=0xc03e6012c8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e601338 sp=0xc03e601300 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e601370 sp=0xc03e601338 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e6013a8 sp=0xc03e601370 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e6013e0 sp=0xc03e6013a8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e601418 sp=0xc03e6013e0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e601450 sp=0xc03e601418 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e601488 sp=0xc03e601450 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e6014c0 sp=0xc03e601488 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e6014f8 sp=0xc03e6014c0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e601530 sp=0xc03e6014f8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e601568 sp=0xc03e601530 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e6015a0 sp=0xc03e601568 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e6015d8 sp=0xc03e6015a0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e601610 sp=0xc03e6015d8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e601648 sp=0xc03e601610 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e601680 sp=0xc03e601648 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e6016b8 sp=0xc03e601680 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e6016f0 sp=0xc03e6016b8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e601728 sp=0xc03e6016f0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e601760 sp=0xc03e601728 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e601798 sp=0xc03e601760 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e6017d0 sp=0xc03e601798 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e601808 sp=0xc03e6017d0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e601840 sp=0xc03e601808 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e601878 sp=0xc03e601840 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e6018b0 sp=0xc03e601878 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806060}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e6018e8 sp=0xc03e6018b0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbf60, 0xc012806000}, {0x40dbf60, 0xc012806360})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03e601920 sp=0xc03e6018e8 pc=0x1fb3805
   > ...additional frames elided...
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:272 +0x67e
   > goroutine 1 [chan receive]:
   > runtime.gopark(0xc011367b40?, 0xc011407db0?, 0xbf?, 0xa1?, 0x38a15e0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc017644d30 sp=0xc017644d10 pc=0x13c9516
   > runtime.chanrecv(0xc010d18a80, 0xc011407e20, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc017644dc0 sp=0xc017644d30 pc=0x13934bb
   > runtime.chanrecv1(0xc0104e2410?, 0x0?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc017644de8 sp=0xc017644dc0 pc=0x1392fb8
   > github.com/pingcap/tidb/server.(*Server).Run(0xc0104e2410)
   > 	/go/src/github.com/pingcap/tidb/server/server.go:365 +0x1f0 fp=0xc017644e40 sp=0xc017644de8 pc=0x3257ff0
   > main.main()
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:220 +0x5b9 fp=0xc017644f80 sp=0xc017644e40 pc=0x3438919
   > runtime.main()
   > 	/usr/local/go/src/runtime/proc.go:250 +0x212 fp=0xc017644fe0 sp=0xc017644f80 pc=0x13c9152
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc017644fe8 sp=0xc017644fe0 pc=0x13fc6e1
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
   > goroutine 18 [GC sweep wait]:
   > runtime.gopark(0x1?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008a790 sp=0xc00008a770 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.bgsweep(0x0?)
   > 	/usr/local/go/src/runtime/mgcsweep.go:297 +0xd7 fp=0xc00008a7c8 sp=0xc00008a790 pc=0x13b2337
   > runtime.gcenable.func1()
   > 	/usr/local/go/src/runtime/mgc.go:178 +0x26 fp=0xc00008a7e0 sp=0xc00008a7c8 pc=0x13a6e06
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008a7e8 sp=0xc00008a7e0 pc=0x13fc6e1
   > created by runtime.gcenable
   > 	/usr/local/go/src/runtime/mgc.go:178 +0x6b
   > goroutine 19 [GC scavenge wait]:
   > runtime.gopark(0xc00010e000?, 0x40acc30?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008af70 sp=0xc00008af50 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.(*scavengerState).park(0x60385e0)
   > 	/usr/local/go/src/runtime/mgcscavenge.go:389 +0x53 fp=0xc00008afa0 sp=0xc00008af70 pc=0x13b0313
   > runtime.bgscavenge(0x0?)
   > 	/usr/local/go/src/runtime/mgcscavenge.go:622 +0x65 fp=0xc00008afc8 sp=0xc00008afa0 pc=0x13b0925
   > runtime.gcenable.func2()
   > 	/usr/local/go/src/runtime/mgc.go:179 +0x26 fp=0xc00008afe0 sp=0xc00008afc8 pc=0x13a6da6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008afe8 sp=0xc00008afe0 pc=0x13fc6e1
   > created by runtime.gcenable
   > 	/usr/local/go/src/runtime/mgc.go:179 +0xaa
   > goroutine 3 [finalizer wait]:
   > runtime.gopark(0x6039860?, 0xc000007520?, 0x0?, 0x0?, 0xc00008e770?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008e628 sp=0xc00008e608 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.runfinq()
   > 	/usr/local/go/src/runtime/mfinal.go:180 +0x10f fp=0xc00008e7e0 sp=0xc00008e628 pc=0x13a5f0f
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008e7e8 sp=0xc00008e7e0 pc=0x13fc6e1
   > created by runtime.createfing
   > 	/usr/local/go/src/runtime/mfinal.go:157 +0x45
   > goroutine 4 [GC worker (idle)]:
   > runtime.gopark(0x0?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008f750 sp=0xc00008f730 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008f7e0 sp=0xc00008f750 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008f7e8 sp=0xc00008f7e0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 34 [GC worker (idle)]:
   > runtime.gopark(0x3808a0ab1e9?, 0x1?, 0x1e?, 0x43?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004c2750 sp=0xc0004c2730 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0004c27e0 sp=0xc0004c2750 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004c27e8 sp=0xc0004c27e0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 35 [GC worker (idle)]:
   > runtime.gopark(0x606d020?, 0x1?, 0xb0?, 0xb1?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004c2f50 sp=0xc0004c2f30 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0004c2fe0 sp=0xc0004c2f50 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004c2fe8 sp=0xc0004c2fe0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 5 [GC worker (idle)]:
   > runtime.gopark(0x3808a0ab1e9?, 0x1?, 0x54?, 0xa8?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008ff50 sp=0xc00008ff30 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008ffe0 sp=0xc00008ff50 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008ffe8 sp=0xc00008ffe0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 20 [GC worker (idle)]:
   > runtime.gopark(0x3808a0ab1e9?, 0x3?, 0x60?, 0x25?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008b750 sp=0xc00008b730 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008b7e0 sp=0xc00008b750 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008b7e8 sp=0xc00008b7e0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 6 [GC worker (idle)]:
   > runtime.gopark(0x3808a0aa8a2?, 0xc00005b160?, 0x18?, 0x14?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000090750 sp=0xc000090730 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0000907e0 sp=0xc000090750 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000907e8 sp=0xc0000907e0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 36 [GC worker (idle)]:
   > runtime.gopark(0x3808a0662a0?, 0x1?, 0xdd?, 0x87?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004c3750 sp=0xc0004c3730 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0004c37e0 sp=0xc0004c3750 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004c37e8 sp=0xc0004c37e0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 21 [GC worker (idle)]:
   > runtime.gopark(0x3808a0662a0?, 0x3?, 0x5e?, 0x7?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008bf50 sp=0xc00008bf30 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008bfe0 sp=0xc00008bf50 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008bfe8 sp=0xc00008bfe0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 37 [GC worker (idle)]:
   > runtime.gopark(0x3808a0a97b8?, 0x3?, 0xd6?, 0x2?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004c3f50 sp=0xc0004c3f30 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0004c3fe0 sp=0xc0004c3f50 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004c3fe8 sp=0xc0004c3fe0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 22 [GC worker (idle)]:
   > runtime.gopark(0x3808a0662a0?, 0x3?, 0x31?, 0x1a?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008c750 sp=0xc00008c730 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008c7e0 sp=0xc00008c750 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008c7e8 sp=0xc00008c7e0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 7 [GC worker (idle)]:
   > runtime.gopark(0x3808a0ab75e?, 0x3?, 0x31?, 0x11?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000090f50 sp=0xc000090f30 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc000090fe0 sp=0xc000090f50 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000090fe8 sp=0xc000090fe0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 38 [GC worker (idle)]:
   > runtime.gopark(0x380899347e1?, 0x3?, 0x42?, 0xe0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004c4750 sp=0xc0004c4730 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0004c47e0 sp=0xc0004c4750 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004c47e8 sp=0xc0004c47e0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 23 [GC worker (idle)]:
   > runtime.gopark(0x3808a0662a0?, 0x1?, 0x50?, 0x75?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008cf50 sp=0xc00008cf30 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008cfe0 sp=0xc00008cf50 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008cfe8 sp=0xc00008cfe0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 39 [GC worker (idle)]:
   > runtime.gopark(0x3808a0662a0?, 0x3?, 0x6a?, 0x91?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004c4f50 sp=0xc0004c4f30 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0004c4fe0 sp=0xc0004c4f50 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004c4fe8 sp=0xc0004c4fe0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 40 [GC worker (idle)]:
   > runtime.gopark(0x3808a0662a0?, 0x1?, 0xf2?, 0x6e?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004c5750 sp=0xc0004c5730 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0004c57e0 sp=0xc0004c5750 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004c57e8 sp=0xc0004c57e0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 24 [GC worker (idle)]:
   > runtime.gopark(0x3808a0abf01?, 0x1?, 0x29?, 0xca?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008d750 sp=0xc00008d730 pc=0x13c9516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008d7e0 sp=0xc00008d750 pc=0x13a8f51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008d7e8 sp=0xc00008d7e0 pc=0x13fc6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 588 [chan receive]:
   > runtime.gopark(0xc010604c40?, 0x40d6898?, 0x88?, 0xce?, 0x30ed206?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00ff1ce60 sp=0xc00ff1ce40 pc=0x13c9516
   > runtime.chanrecv(0xc000619b00, 0xc00ff1cf80, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc00ff1cef0 sp=0xc00ff1ce60 pc=0x13934bb
   > runtime.chanrecv1(0x0?, 0x30ed1e0?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc00ff1cf18 sp=0xc00ff1cef0 pc=0x1392fb8
   > github.com/pingcap/tidb/util/signal.SetupSignalHandler.func2()
   > 	/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:54 +0x45 fp=0xc00ff1cfe0 sp=0xc00ff1cf18 pc=0x3433665
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00ff1cfe8 sp=0xc00ff1cfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/util/signal.SetupSignalHandler
   > 	/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:53 +0x19f
   > goroutine 10 [chan receive]:
   > runtime.gopark(0xc0004bfed8?, 0x13cf37b?, 0x20?, 0xff?, 0x13e6de5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004bfec8 sp=0xc0004bfea8 pc=0x13c9516
   > runtime.chanrecv(0xc00060e0c0, 0xc0004bffa0, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc0004bff58 sp=0xc0004bfec8 pc=0x13934bb
   > runtime.chanrecv2(0x6fc23ac00?, 0x0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc0004bff80 sp=0xc0004bff58 pc=0x1392ff8
   > github.com/golang/glog.(*loggingT).flushDaemon(0x0?)
   > 	/go/pkg/mod/github.com/golang/glog@v1.0.0/glog.go:882 +0x6a fp=0xc0004bffc8 sp=0xc0004bff80 pc=0x2482faa
   > github.com/golang/glog.init.0.func1()
   > 	/go/pkg/mod/github.com/golang/glog@v1.0.0/glog.go:410 +0x26 fp=0xc0004bffe0 sp=0xc0004bffc8 pc=0x2480906
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004bffe8 sp=0xc0004bffe0 pc=0x13fc6e1
   > created by github.com/golang/glog.init.0
   > 	/go/pkg/mod/github.com/golang/glog@v1.0.0/glog.go:410 +0x1bf
   > goroutine 11 [select]:
   > runtime.gopark(0xc0004bf788?, 0x3?, 0x48?, 0xd8?, 0xc0004bf772?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004bf5f8 sp=0xc0004bf5d8 pc=0x13c9516
   > runtime.selectgo(0xc0004bf788, 0xc0004bf76c, 0xc0009c5000?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0004bf738 sp=0xc0004bf5f8 pc=0x13d9bdc
   > go.opencensus.io/stats/view.(*worker).start(0xc0009c5000)
   > 	/go/pkg/mod/go.opencensus.io@v0.23.0/stats/view/worker.go:276 +0xad fp=0xc0004bf7c8 sp=0xc0004bf738 pc=0x2b9244d
   > go.opencensus.io/stats/view.init.0.func1()
   > 	/go/pkg/mod/go.opencensus.io@v0.23.0/stats/view/worker.go:34 +0x26 fp=0xc0004bf7e0 sp=0xc0004bf7c8 pc=0x2b916c6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004bf7e8 sp=0xc0004bf7e0 pc=0x13fc6e1
   > created by go.opencensus.io/stats/view.init.0
   > 	/go/pkg/mod/go.opencensus.io@v0.23.0/stats/view/worker.go:34 +0x8d
   > goroutine 296 [select]:
   > runtime.gopark(0xc000fe5f58?, 0x4?, 0xab?, 0x42?, 0xc000fe5da8?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000fe5bf8 sp=0xc000fe5bd8 pc=0x13c9516
   > runtime.selectgo(0xc000fe5f58, 0xc000fe5da0, 0xc000f4be38?, 0x0, 0x1?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000fe5d38 sp=0xc000fe5bf8 pc=0x13d9bdc
   > github.com/pingcap/tidb/ddl.(*worker).start(0xc010d3a6c0, 0xc010d46270)
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl_worker.go:184 +0x318 fp=0xc000fe5fc0 sp=0xc000fe5d38 pc=0x27168b8
   > github.com/pingcap/tidb/ddl.(*ddl).Start.func3()
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:399 +0x2a fp=0xc000fe5fe0 sp=0xc000fe5fc0 pc=0x26d426a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000fe5fe8 sp=0xc000fe5fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/ddl.(*ddl).Start
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:399 +0x58e
   > goroutine 251 [select]:
   > runtime.gopark(0xc0004c1730?, 0x3?, 0x11?, 0x0?, 0xc0004c170a?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004c1590 sp=0xc0004c1570 pc=0x13c9516
   > runtime.selectgo(0xc0004c1730, 0xc0004c1704, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0004c16d0 sp=0xc0004c1590 pc=0x13d9bdc
   > github.com/pingcap/tidb/util/cpuprofile.(*parallelCPUProfiler).profilingLoop(0xc0005bf980)
   > 	/go/src/github.com/pingcap/tidb/util/cpuprofile/cpuprofile.go:166 +0x105 fp=0xc0004c1778 sp=0xc0004c16d0 pc=0x25951c5
   > github.com/pingcap/tidb/util/cpuprofile.(*parallelCPUProfiler).profilingLoop-fm()
   > 	<autogenerated>:1 +0x26 fp=0xc0004c1790 sp=0xc0004c1778 pc=0x2596e66
   > github.com/pingcap/tidb/util.WithRecovery(0x0?, 0x0?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc0004c17c0 sp=0xc0004c1790 pc=0x208e513
   > github.com/pingcap/tidb/util/cpuprofile.(*parallelCPUProfiler).start.func1()
   > 	/go/src/github.com/pingcap/tidb/util/cpuprofile/cpuprofile.go:113 +0x28 fp=0xc0004c17e0 sp=0xc0004c17c0 pc=0x2594da8
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004c17e8 sp=0xc0004c17e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/util/cpuprofile.(*parallelCPUProfiler).start
   > 	/go/src/github.com/pingcap/tidb/util/cpuprofile/cpuprofile.go:113 +0x176
   > goroutine 252 [chan receive]:
   > runtime.gopark(0xc000114480?, 0x13cf374?, 0x38?, 0xfe?, 0x13e6de5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00009fde0 sp=0xc00009fdc0 pc=0x13c9516
   > runtime.chanrecv(0xc000114420, 0x0, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc00009fe70 sp=0xc00009fde0 pc=0x13934bb
   > runtime.chanrecv1(0x5f5e100?, 0x3b88785?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc00009fe98 sp=0xc00009fe70 pc=0x1392fb8
   > github.com/pingcap/tidb/util/systimemon.StartMonitor(0x3c82178, 0x3c817e0, 0xc000ec9880)
   > 	/go/src/github.com/pingcap/tidb/util/systimemon/systime_mon.go:32 +0x185 fp=0xc00009ffb8 sp=0xc00009fe98 pc=0x3433bc5
   > main.setupMetrics.func3()
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:716 +0x31 fp=0xc00009ffe0 sp=0xc00009ffb8 pc=0x343c391
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00009ffe8 sp=0xc00009ffe0 pc=0x13fc6e1
   > created by main.setupMetrics
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:716 +0x115
   > goroutine 253 [select]:
   > runtime.gopark(0xc0004c5f80?, 0x2?, 0x8?, 0x0?, 0xc0004c5f4c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004c5dd0 sp=0xc0004c5db0 pc=0x13c9516
   > runtime.selectgo(0xc0004c5f80, 0xc0004c5f48, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0004c5f10 sp=0xc0004c5dd0 pc=0x13d9bdc
   > github.com/pingcap/badger.(*DB).updateSize(0x0?, 0xc000013ce0)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/db.go:1039 +0x105 fp=0xc0004c5fc0 sp=0xc0004c5f10 pc=0x33233a5
   > github.com/pingcap/badger.Open.func5()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/db.go:328 +0x2a fp=0xc0004c5fe0 sp=0xc0004c5fc0 pc=0x331d46a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004c5fe8 sp=0xc0004c5fe0 pc=0x13fc6e1
   > created by github.com/pingcap/badger.Open
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/db.go:328 +0xf5c
   > goroutine 254 [select]:
   > runtime.gopark(0xc0004be788?, 0x2?, 0x2?, 0x0?, 0xc0004be764?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004be5e8 sp=0xc0004be5c8 pc=0x13c9516
   > runtime.selectgo(0xc0004be788, 0xc0004be760, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0004be728 sp=0xc0004be5e8 pc=0x13d9bdc
   > github.com/pingcap/badger/epoch.(*ResourceManager).collectLoop(0x0?, 0xc000013d10)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/epoch/manager.go:101 +0xd3 fp=0xc0004be7c0 sp=0xc0004be728 pc=0x3299693
   > github.com/pingcap/badger/epoch.NewResourceManager.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/epoch/manager.go:79 +0x2a fp=0xc0004be7e0 sp=0xc0004be7c0 pc=0x329942a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004be7e8 sp=0xc0004be7e0 pc=0x13fc6e1
   > created by github.com/pingcap/badger/epoch.NewResourceManager
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/epoch/manager.go:79 +0xdd
   > goroutine 255 [select]:
   > runtime.gopark(0xc00035be68?, 0x2?, 0x18?, 0x3f?, 0xc00035be3c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00035bcc0 sp=0xc00035bca0 pc=0x13c9516
   > runtime.selectgo(0xc00035be68, 0xc00035be38, 0x0?, 0x1, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00035be00 sp=0xc00035bcc0 pc=0x13d9bdc
   > github.com/pingcap/badger.Open.func4()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/db.go:342 +0x155 fp=0xc00035bfe0 sp=0xc00035be00 pc=0x331d3f5
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00035bfe8 sp=0xc00035bfe0 pc=0x13fc6e1
   > created by github.com/pingcap/badger.Open
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/db.go:339 +0x11f8
   > goroutine 116 [select]:
   > runtime.gopark(0xc00033af08?, 0x2?, 0x0?, 0x0?, 0xc00033aee4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00033ad68 sp=0xc00033ad48 pc=0x13c9516
   > runtime.selectgo(0xc00033af08, 0xc00033aee0, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00033aea8 sp=0xc00033ad68 pc=0x13d9bdc
   > github.com/pingcap/badger.(*blobGCHandler).run(0xc000e061c0, 0xc000124558)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/blob.go:468 +0xd6 fp=0xc00033afc0 sp=0xc00033aea8 pc=0x33117f6
   > github.com/pingcap/badger.(*blobManager).Open.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/blob.go:292 +0x2a fp=0xc00033afe0 sp=0xc00033afc0 pc=0x33104aa
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00033afe8 sp=0xc00033afe0 pc=0x13fc6e1
   > created by github.com/pingcap/badger.(*blobManager).Open
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/blob.go:292 +0x5bd
   > goroutine 117 [select]:
   > runtime.gopark(0xc00033b760?, 0x2?, 0x6?, 0x30?, 0xc00033b72c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00033b598 sp=0xc00033b578 pc=0x13c9516
   > runtime.selectgo(0xc00033b760, 0xc00033b728, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00033b6d8 sp=0xc00033b598 pc=0x13d9bdc
   > github.com/pingcap/badger.(*levelsController).runWorker(0xc000ecc1c0, 0xc0001245a0, 0x0)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/levels.go:212 +0x1fb fp=0xc00033b7b8 sp=0xc00033b6d8 pc=0x332b8db
   > github.com/pingcap/badger.(*levelsController).startCompact.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/levels.go:180 +0x2e fp=0xc00033b7e0 sp=0xc00033b7b8 pc=0x332b6ae
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00033b7e8 sp=0xc00033b7e0 pc=0x13fc6e1
   > created by github.com/pingcap/badger.(*levelsController).startCompact
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/levels.go:180 +0x65
   > goroutine 118 [select]:
   > runtime.gopark(0xc00033bf60?, 0x2?, 0x6?, 0x30?, 0xc00033bf2c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00033bd98 sp=0xc00033bd78 pc=0x13c9516
   > runtime.selectgo(0xc00033bf60, 0xc00033bf28, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00033bed8 sp=0xc00033bd98 pc=0x13d9bdc
   > github.com/pingcap/badger.(*levelsController).runWorker(0xc000ecc1c0, 0xc0001245a0, 0x0)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/levels.go:212 +0x1fb fp=0xc00033bfb8 sp=0xc00033bed8 pc=0x332b8db
   > github.com/pingcap/badger.(*levelsController).startCompact.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/levels.go:180 +0x2e fp=0xc00033bfe0 sp=0xc00033bfb8 pc=0x332b6ae
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00033bfe8 sp=0xc00033bfe0 pc=0x13fc6e1
   > created by github.com/pingcap/badger.(*levelsController).startCompact
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/levels.go:180 +0x65
   > goroutine 119 [select]:
   > runtime.gopark(0xc0004bef60?, 0x2?, 0x6?, 0x30?, 0xc0004bef2c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004bed98 sp=0xc0004bed78 pc=0x13c9516
   > runtime.selectgo(0xc0004bef60, 0xc0004bef28, 0x0?, 0x0, 0xf4240?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0004beed8 sp=0xc0004bed98 pc=0x13d9bdc
   > github.com/pingcap/badger.(*levelsController).runWorker(0xc000ecc1c0, 0xc0001245a0, 0x1)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/levels.go:212 +0x1fb fp=0xc0004befb8 sp=0xc0004beed8 pc=0x332b8db
   > github.com/pingcap/badger.(*levelsController).startCompact.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/levels.go:180 +0x2e fp=0xc0004befe0 sp=0xc0004befb8 pc=0x332b6ae
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004befe8 sp=0xc0004befe0 pc=0x13fc6e1
   > created by github.com/pingcap/badger.(*levelsController).startCompact
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/levels.go:180 +0x65
   > goroutine 120 [chan receive]:
   > runtime.gopark(0x0?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00009eac0 sp=0xc00009eaa0 pc=0x13c9516
   > runtime.chanrecv(0xc000edf0e0, 0xc00009ec60, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc00009eb50 sp=0xc00009eac0 pc=0x13934bb
   > runtime.chanrecv2(0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc00009eb78 sp=0xc00009eb50 pc=0x1392ff8
   > github.com/pingcap/badger.(*DB).runFlushMemTable(0xc000efe000, 0xc000ec9880?)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/db.go:920 +0xdd fp=0xc00009efc0 sp=0xc00009eb78 pc=0x3321e5d
   > github.com/pingcap/badger.Open.func6()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/db.go:361 +0x2a fp=0xc00009efe0 sp=0xc00009efc0 pc=0x331d26a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00009efe8 sp=0xc00009efe0 pc=0x13fc6e1
   > created by github.com/pingcap/badger.Open
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/db.go:361 +0x158d
   > goroutine 84 [select]:
   > runtime.gopark(0xc0000a1f78?, 0x3?, 0x25?, 0x28?, 0xc0000a1f32?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0000a1d98 sp=0xc0000a1d78 pc=0x13c9516
   > runtime.selectgo(0xc0000a1f78, 0xc0000a1f2c, 0x1?, 0x0, 0xc001041a00?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0000a1ed8 sp=0xc0000a1d98 pc=0x13d9bdc
   > github.com/pingcap/badger.(*writeWorker).runWriteVLog(0xc000a0c760, 0xc0004f2180)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/writer.go:94 +0x137 fp=0xc0000a1fc0 sp=0xc0000a1ed8 pc=0x333b817
   > github.com/pingcap/badger.startWriteWorker.func2()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/writer.go:64 +0x2a fp=0xc0000a1fe0 sp=0xc0000a1fc0 pc=0x333b2ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000a1fe8 sp=0xc0000a1fe0 pc=0x13fc6e1
   > created by github.com/pingcap/badger.startWriteWorker
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/writer.go:64 +0x1f9
   > goroutine 85 [chan receive, locked to thread]:
   > runtime.gopark(0xc0000a2e98?, 0x1464528?, 0xf?, 0x0?, 0x1?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0000a2e68 sp=0xc0000a2e48 pc=0x13c9516
   > runtime.chanrecv(0xc000114900, 0xc0000a2f88, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc0000a2ef8 sp=0xc0000a2e68 pc=0x13934bb
   > runtime.chanrecv2(0xc000d498c0?, 0x3ef08d40f0b60b14?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc0000a2f20 sp=0xc0000a2ef8 pc=0x1392ff8
   > github.com/pingcap/badger.(*writeWorker).runWriteLSM(0xc000a0c760, 0xc00045e270?)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/writer.go:141 +0x15e fp=0xc0000a2fc0 sp=0xc0000a2f20 pc=0x333be5e
   > github.com/pingcap/badger.startWriteWorker.func3()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/writer.go:65 +0x2a fp=0xc0000a2fe0 sp=0xc0000a2fc0 pc=0x333b28a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000a2fe8 sp=0xc0000a2fe0 pc=0x13fc6e1
   > created by github.com/pingcap/badger.startWriteWorker
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/writer.go:65 +0x24d
   > goroutine 86 [chan receive]:
   > runtime.gopark(0xc00116dd18?, 0xc00116dd18?, 0x18?, 0xdd?, 0xc00116dd18?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000354ea8 sp=0xc000354e88 pc=0x13c9516
   > runtime.chanrecv(0xc000114960, 0xc000354f88, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000354f38 sp=0xc000354ea8 pc=0x13934bb
   > runtime.chanrecv2(0xc000e420a0?, 0x0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc000354f60 sp=0xc000354f38 pc=0x1392ff8
   > github.com/pingcap/badger.(*writeWorker).runMergeLSM(0x0?, 0x0?)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/writer.go:154 +0x9b fp=0xc000354fc0 sp=0xc000354f60 pc=0x333bfdb
   > github.com/pingcap/badger.startWriteWorker.func4()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/writer.go:66 +0x2a fp=0xc000354fe0 sp=0xc000354fc0 pc=0x333b22a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000354fe8 sp=0xc000354fe0 pc=0x13fc6e1
   > created by github.com/pingcap/badger.startWriteWorker
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20220314162537-ab58fbf40580/writer.go:66 +0x2a5
   > goroutine 87 [select]:
   > runtime.gopark(0xc0000a3f88?, 0x2?, 0x0?, 0x0?, 0xc0000a3f4c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0000a3da0 sp=0xc0000a3d80 pc=0x13c9516
   > runtime.selectgo(0xc0000a3f88, 0xc0000a3f48, 0xc0107af5e0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0000a3ee0 sp=0xc0000a3da0 pc=0x13d9bdc
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.writeDBWorker.run({0xc000114a20?, 0xc000e062c0?})
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:96 +0x145 fp=0xc0000a3fc0 sp=0xc0000a3ee0 pc=0x338c745
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*dbWriter).Open.func1()
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:202 +0x2a fp=0xc0000a3fe0 sp=0xc0000a3fc0 pc=0x338d2ca
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000a3fe8 sp=0xc0000a3fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*dbWriter).Open
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:199 +0xc5
   > goroutine 88 [select]:
   > runtime.gopark(0xc000358e70?, 0x2?, 0x90?, 0x8e?, 0xc000358e1c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000358c58 sp=0xc000358c38 pc=0x13c9516
   > runtime.selectgo(0xc000358e70, 0xc000358e18, 0x13?, 0x0, 0xc0134c1100?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000358d98 sp=0xc000358c58 pc=0x13d9bdc
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.writeLockWorker.run({0xc000114a80?, 0xc000e062c0?})
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:148 +0x15f fp=0xc000358fc0 sp=0xc000358d98 pc=0x338cd1f
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*dbWriter).Open.func2()
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:209 +0x2a fp=0xc000358fe0 sp=0xc000358fc0 pc=0x338d26a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000358fe8 sp=0xc000358fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*dbWriter).Open
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:206 +0x159
   > goroutine 89 [select]:
   > runtime.gopark(0xc000335f18?, 0x2?, 0x20?, 0xd0?, 0xc000335f04?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000335d88 sp=0xc000335d68 pc=0x13c9516
   > runtime.selectgo(0xc000335f18, 0xc000335f00, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000335ec8 sp=0xc000335d88 pc=0x13d9bdc
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*MVCCStore).runUpdateSafePointLoop(0xc000e40380)
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:1705 +0x217 fp=0xc000335fc8 sp=0xc000335ec8 pc=0x337e3d7
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.NewMVCCStore.func1()
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:86 +0x26 fp=0xc000335fe0 sp=0xc000335fc8 pc=0x336f0a6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000335fe8 sp=0xc000335fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.NewMVCCStore
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:86 +0x337
   > goroutine 90 [select]:
   > runtime.gopark(0xc0003367b0?, 0x2?, 0x0?, 0x0?, 0xc00033679c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000336628 sp=0xc000336608 pc=0x13c9516
   > runtime.selectgo(0xc0003367b0, 0xc000336798, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000336768 sp=0xc000336628 pc=0x13d9bdc
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*MVCCStore).StartDeadlockDetection.func1()
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:1378 +0x7b fp=0xc0003367e0 sp=0xc000336768 pc=0x337b11b
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0003367e8 sp=0xc0003367e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*MVCCStore).StartDeadlockDetection
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:1376 +0xb6
   > goroutine 91 [select]:
   > runtime.gopark(0xc010d8ef78?, 0x2?, 0x8?, 0x0?, 0xc010d8ef3c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010d8edc0 sp=0xc010d8eda0 pc=0x13c9516
   > runtime.selectgo(0xc010d8ef78, 0xc010d8ef38, 0xc0003387b0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010d8ef00 sp=0xc010d8edc0 pc=0x13d9bdc
   > github.com/tikv/client-go/v2/oracle/oracles.(*pdOracle).updateTS(0xc000ec2af0, {0x40d6860, 0xc000058058}, 0xc00045e270?)
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.1-0.20220311043619-5042c6f2aaa6/oracle/oracles/pd.go:229 +0x128 fp=0xc010d8efb0 sp=0xc010d8ef00 pc=0x1e576a8
   > github.com/tikv/client-go/v2/oracle/oracles.NewPdOracle.func1()
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.1-0.20220311043619-5042c6f2aaa6/oracle/oracles/pd.go:77 +0x32 fp=0xc010d8efe0 sp=0xc010d8efb0 pc=0x1e568d2
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010d8efe8 sp=0xc010d8efe0 pc=0x13fc6e1
   > created by github.com/tikv/client-go/v2/oracle/oracles.NewPdOracle
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.1-0.20220311043619-5042c6f2aaa6/oracle/oracles/pd.go:77 +0x119
   > goroutine 92 [select]:
   > runtime.gopark(0xc000339f78?, 0x3?, 0x0?, 0x0?, 0xc000339f5a?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000339de0 sp=0xc000339dc0 pc=0x13c9516
   > runtime.selectgo(0xc000339f78, 0xc000339f54, 0x1000200000001?, 0x0, 0xc000884038?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000339f20 sp=0xc000339de0 pc=0x13d9bdc
   > github.com/tikv/client-go/v2/internal/locate.(*RegionCache).asyncCheckAndResolveLoop(0xc000e40d00, 0xc0004f2180?)
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.1-0.20220311043619-5042c6f2aaa6/internal/locate/region_cache.go:423 +0xd1 fp=0xc000339fc0 sp=0xc000339f20 pc=0x1e25c11
   > github.com/tikv/client-go/v2/internal/locate.NewRegionCache.func1()
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.1-0.20220311043619-5042c6f2aaa6/internal/locate/region_cache.go:394 +0x2a fp=0xc000339fe0 sp=0xc000339fc0 pc=0x1e2588a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000339fe8 sp=0xc000339fe0 pc=0x13fc6e1
   > created by github.com/tikv/client-go/v2/internal/locate.NewRegionCache
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.1-0.20220311043619-5042c6f2aaa6/internal/locate/region_cache.go:394 +0x2e6
   > goroutine 93 [select]:
   > runtime.gopark(0xc000359f10?, 0x2?, 0x6?, 0x30?, 0xc000359eac?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000359d10 sp=0xc000359cf0 pc=0x13c9516
   > runtime.selectgo(0xc000359f10, 0xc000359ea8, 0x0?, 0x0, 0x60384e0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000359e50 sp=0xc000359d10 pc=0x13d9bdc
   > github.com/tikv/client-go/v2/tikv.(*KVStore).runSafePointChecker(0xc000156000)
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.1-0.20220311043619-5042c6f2aaa6/tikv/kv.go:234 +0x12b fp=0xc000359fc8 sp=0xc000359e50 pc=0x1e9a70b
   > github.com/tikv/client-go/v2/tikv.NewKVStore.func1()
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.1-0.20220311043619-5042c6f2aaa6/tikv/kv.go:189 +0x26 fp=0xc000359fe0 sp=0xc000359fc8 pc=0x1e9a506
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000359fe8 sp=0xc000359fe0 pc=0x13fc6e1
   > created by github.com/tikv/client-go/v2/tikv.NewKVStore
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.1-0.20220311043619-5042c6f2aaa6/tikv/kv.go:189 +0x416
   > goroutine 94 [select]:
   > runtime.gopark(0xc000337780?, 0x2?, 0x0?, 0x0?, 0xc000337744?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0003375c8 sp=0xc0003375a8 pc=0x13c9516
   > runtime.selectgo(0xc000337780, 0xc000337740, 0xc0000fa840?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000337708 sp=0xc0003375c8 pc=0x13d9bdc
   > github.com/tikv/client-go/v2/tikv.(*KVStore).safeTSUpdater(0xc000156000)
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.1-0.20220311043619-5042c6f2aaa6/tikv/kv.go:521 +0x165 fp=0xc0003377c8 sp=0xc000337708 pc=0x1e9c6e5
   > github.com/tikv/client-go/v2/tikv.NewKVStore.func2()
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.1-0.20220311043619-5042c6f2aaa6/tikv/kv.go:190 +0x26 fp=0xc0003377e0 sp=0xc0003377c8 pc=0x1e9a4a6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0003377e8 sp=0xc0003377e0 pc=0x13fc6e1
   > created by github.com/tikv/client-go/v2/tikv.NewKVStore
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.1-0.20220311043619-5042c6f2aaa6/tikv/kv.go:190 +0x456
   > goroutine 95 [select]:
   > runtime.gopark(0xc000337f98?, 0x2?, 0x90?, 0x7e?, 0xc000337f6c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000337de8 sp=0xc000337dc8 pc=0x13c9516
   > runtime.selectgo(0xc000337f98, 0xc000337f68, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000337f28 sp=0xc000337de8 pc=0x13d9bdc
   > github.com/dgraph-io/ristretto.(*defaultPolicy).processItems(0xc000e07000)
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.1.0/policy.go:102 +0x91 fp=0xc000337fc8 sp=0xc000337f28 pc=0x248a7b1
   > github.com/dgraph-io/ristretto.newDefaultPolicy.func1()
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.1.0/policy.go:86 +0x26 fp=0xc000337fe0 sp=0xc000337fc8 pc=0x248a666
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000337fe8 sp=0xc000337fe0 pc=0x13fc6e1
   > created by github.com/dgraph-io/ristretto.newDefaultPolicy
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.1.0/policy.go:86 +0x156
   > goroutine 96 [select]:
   > runtime.gopark(0xc000dc2788?, 0x3?, 0x90?, 0x70?, 0xc000dc2732?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000dc25a8 sp=0xc000dc2588 pc=0x13c9516
   > runtime.selectgo(0xc000dc2788, 0xc000dc272c, 0xc000e07000?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000dc26e8 sp=0xc000dc25a8 pc=0x13d9bdc
   > github.com/dgraph-io/ristretto.(*Cache).processItems(0xc000e40d80)
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.1.0/cache.go:452 +0x15e fp=0xc000dc27c8 sp=0xc000dc26e8 pc=0x2488cfe
   > github.com/dgraph-io/ristretto.NewCache.func5()
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.1.0/cache.go:207 +0x26 fp=0xc000dc27e0 sp=0xc000dc27c8 pc=0x2487da6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000dc27e8 sp=0xc000dc27e0 pc=0x13fc6e1
   > created by github.com/dgraph-io/ristretto.NewCache
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.1.0/cache.go:207 +0x6a5
   > goroutine 94655 [select]:
   > runtime.gopark(0xc000f8bf00?, 0x2?, 0x16?, 0x95?, 0xc000f8be44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000f8bc48 sp=0xc000f8bc28 pc=0x13c9516
   > runtime.selectgo(0xc000f8bf00, 0xc000f8be40, 0xc000f8bde8?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000f8bd88 sp=0xc000f8bc48 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc0144fd4c0, {0x4134ba0, 0xc0114b7d40})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc000f8bf30 sp=0xc000f8bd88 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc0144fd4c0, {0x4134ba0, 0xc0114b7d40}, 0xc018208590)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc000f8bfb0 sp=0xc000f8bf30 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc000f8bfe0 sp=0xc000f8bfb0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000f8bfe8 sp=0xc000f8bfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 610 [select]:
   > runtime.gopark(0xc0117f7d48?, 0x2?, 0x60?, 0x51?, 0xc0117f7c94?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01ddc9b08 sp=0xc01ddc9ae8 pc=0x13c9516
   > runtime.selectgo(0xc01ddc9d48, 0xc0117f7c90, 0xc018d6a620?, 0x0, 0x1?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01ddc9c48 sp=0xc01ddc9b08 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).loadStatsWorker(0xc010d0a140)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1359 +0x485 fp=0xc01ddc9fc8 sp=0xc01ddc9c48 pc=0x2797fe5
   > github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1292 +0x26 fp=0xc01ddc9fe0 sp=0xc01ddc9fc8 pc=0x2797566
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01ddc9fe8 sp=0xc01ddc9fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1292 +0x10a
   > goroutine 613 [select]:
   > runtime.gopark(0xc000357d48?, 0x3?, 0x3?, 0x0?, 0xc000357cd2?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000357b50 sp=0xc000357b30 pc=0x13c9516
   > runtime.selectgo(0xc000357d48, 0xc000357ccc, 0x5?, 0x0, 0x1?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000357c90 sp=0xc000357b50 pc=0x13d9bdc
   > github.com/pingcap/tidb/statistics/handle.(*Handle).drainColTask(0xc0100dc000, 0xc010d180c0)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:294 +0xe5 fp=0xc000357d88 sp=0xc000357c90 pc=0x2612705
   > github.com/pingcap/tidb/statistics/handle.(*Handle).HandleOneTask(0xc0100dc000, 0x0?, 0xc000357f40, {0x7f4c0848dc78, 0xc0000f26c0}, 0x0?)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:181 +0xc5 fp=0xc000357ee8 sp=0xc000357d88 pc=0x2610fe5
   > github.com/pingcap/tidb/statistics/handle.(*Handle).SubLoadWorker(0xc0100dc000, {0x4134ba0?, 0xc0000f26c0}, 0xc0009caff0?, 0xc0009cb020?)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:154 +0x11b fp=0xc000357fa8 sp=0xc000357ee8 pc=0x2610b3b
   > github.com/pingcap/tidb/domain.(*Domain).StartLoadStatsSubWorkers.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1318 +0x36 fp=0xc000357fe0 sp=0xc000357fa8 pc=0x27977b6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000357fe8 sp=0xc000357fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).StartLoadStatsSubWorkers
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1318 +0x172
   > goroutine 576 [select]:
   > runtime.gopark(0xc000dc3728?, 0x2?, 0x0?, 0x30?, 0xc000dc36d4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000dc3548 sp=0xc000dc3528 pc=0x13c9516
   > runtime.selectgo(0xc000dc3728, 0xc000dc36d0, 0x9?, 0x0, 0x15?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000dc3688 sp=0xc000dc3548 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).TelemetryReportLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1185 +0x11c fp=0xc000dc37e0 sp=0xc000dc3688 pc=0x279663c
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000dc37e8 sp=0xc000dc37e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).TelemetryReportLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1177 +0x285
   > goroutine 293 [select]:
   > runtime.gopark(0xc012c51f38?, 0x2?, 0x5?, 0x0?, 0xc012c51efc?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01cce7d50 sp=0xc01cce7d30 pc=0x13c9516
   > runtime.selectgo(0xc01cce7f38, 0xc012c51ef8, 0x1?, 0x0, 0x2?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01cce7e90 sp=0xc01cce7d50 pc=0x13d9bdc
   > github.com/pingcap/tidb/ddl.(*ddl).limitDDLJobs(0xc010d1e200)
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl_worker.go:269 +0x173 fp=0xc01cce7fc8 sp=0xc01cce7e90 pc=0x2717a13
   > github.com/pingcap/tidb/ddl.(*ddl).Start.func2()
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:381 +0x26 fp=0xc01cce7fe0 sp=0xc01cce7fc8 pc=0x26d42c6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01cce7fe8 sp=0xc01cce7fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/ddl.(*ddl).Start
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:381 +0x2aa
   > goroutine 94651 [select]:
   > runtime.gopark(0xc001023f28?, 0x2?, 0x63?, 0x33?, 0xc001023eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc001023d58 sp=0xc001023d38 pc=0x13c9516
   > runtime.selectgo(0xc001023f28, 0xc001023ee8, 0x35b8622bf?, 0x0, 0xc194c53ddc5e6173?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc001023e98 sp=0xc001023d58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc0144fd240, {0x4134ba0, 0xc0114b7d40}, 0xc018208580, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc001023fa8 sp=0xc001023e98 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc001023fe0 sp=0xc001023fa8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc001023fe8 sp=0xc001023fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 615 [select]:
   > runtime.gopark(0xc000575d48?, 0x3?, 0x3?, 0x0?, 0xc000575cd2?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000575b50 sp=0xc000575b30 pc=0x13c9516
   > runtime.selectgo(0xc000575d48, 0xc000575ccc, 0x0?, 0x0, 0xc0005abe00?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000575c90 sp=0xc000575b50 pc=0x13d9bdc
   > github.com/pingcap/tidb/statistics/handle.(*Handle).drainColTask(0xc0100dc000, 0xc010d180c0)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:294 +0xe5 fp=0xc000575d88 sp=0xc000575c90 pc=0x2612705
   > github.com/pingcap/tidb/statistics/handle.(*Handle).HandleOneTask(0xc0100dc000, 0xc00061ca00?, 0xc000575f40, {0x7f4c0848dc78, 0xc0000f2b40}, 0x0?)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:181 +0xc5 fp=0xc000575ee8 sp=0xc000575d88 pc=0x2610fe5
   > github.com/pingcap/tidb/statistics/handle.(*Handle).SubLoadWorker(0xc0100dc000, {0x4134ba0?, 0xc0000f2b40}, 0x0?, 0x0?)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:154 +0x11b fp=0xc000575fa8 sp=0xc000575ee8 pc=0x2610b3b
   > github.com/pingcap/tidb/domain.(*Domain).StartLoadStatsSubWorkers.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1318 +0x36 fp=0xc000575fe0 sp=0xc000575fa8 pc=0x27977b6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000575fe8 sp=0xc000575fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).StartLoadStatsSubWorkers
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1318 +0x172
   > goroutine 616 [select]:
   > runtime.gopark(0xc010d8fd48?, 0x3?, 0x3?, 0x0?, 0xc010d8fcd2?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010d8fb50 sp=0xc010d8fb30 pc=0x13c9516
   > runtime.selectgo(0xc010d8fd48, 0xc010d8fccc, 0x40f5e70?, 0x0, 0x40f5ef8?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010d8fc90 sp=0xc010d8fb50 pc=0x13d9bdc
   > github.com/pingcap/tidb/statistics/handle.(*Handle).drainColTask(0xc0100dc000, 0xc010d180c0)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:294 +0xe5 fp=0xc010d8fd88 sp=0xc010d8fc90 pc=0x2612705
   > github.com/pingcap/tidb/statistics/handle.(*Handle).HandleOneTask(0xc0100dc000, 0xc0009db440?, 0xc010d8ff40, {0x7f4c0848dc78, 0xc0000f2fc0}, 0xc0009db680?)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:181 +0xc5 fp=0xc010d8fee8 sp=0xc010d8fd88 pc=0x2610fe5
   > github.com/pingcap/tidb/statistics/handle.(*Handle).SubLoadWorker(0xc0100dc000, {0x4134ba0?, 0xc0000f2fc0}, 0xc0009dbd40?, 0xc0009dbd70?)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:154 +0x11b fp=0xc010d8ffa8 sp=0xc010d8fee8 pc=0x2610b3b
   > github.com/pingcap/tidb/domain.(*Domain).StartLoadStatsSubWorkers.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1318 +0x36 fp=0xc010d8ffe0 sp=0xc010d8ffa8 pc=0x27977b6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010d8ffe8 sp=0xc010d8ffe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).StartLoadStatsSubWorkers
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1318 +0x172
   > goroutine 121914 [select]:
   > runtime.gopark(0xc000645f78?, 0x2?, 0x80?, 0x96?, 0xc000645eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000645d58 sp=0xc000645d38 pc=0x13c9516
   > runtime.selectgo(0xc000645f78, 0xc000645ee8, 0x3b67af1?, 0x0, 0x3041f62?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000645e98 sp=0xc000645d58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc01943a540, {0x40d68d0?, 0xc01ac388a0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc000645fb8 sp=0xc000645e98 pc=0x30ecdf4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc000645fe0 sp=0xc000645fb8 pc=0x30ec08e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000645fe8 sp=0xc000645fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 577 [select]:
   > runtime.gopark(0xc00ff1c7a8?, 0x2?, 0x4?, 0x30?, 0xc00ff1c784?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00ff1c608 sp=0xc00ff1c5e8 pc=0x13c9516
   > runtime.selectgo(0xc00ff1c7a8, 0xc00ff1c780, 0xc000de4960?, 0x0, 0xc000056cd8?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00ff1c748 sp=0xc00ff1c608 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).TelemetryRotateSubWindowLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1214 +0xcc fp=0xc00ff1c7e0 sp=0xc00ff1c748 pc=0x2796b4c
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00ff1c7e8 sp=0xc00ff1c7e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).TelemetryRotateSubWindowLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1207 +0x8f
   > goroutine 121916 [select]:
   > runtime.gopark(0xc0009d9f78?, 0x2?, 0x6c?, 0xd2?, 0xc0009d9eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0009d9d58 sp=0xc0009d9d38 pc=0x13c9516
   > runtime.selectgo(0xc0009d9f78, 0xc0009d9ee8, 0x3b67af1?, 0x0, 0xc194c53e4a606e65?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0009d9e98 sp=0xc0009d9d58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc01943a5c0, {0x40d68d0?, 0xc01ac388a0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc0009d9fb8 sp=0xc0009d9e98 pc=0x30ecdf4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc0009d9fe0 sp=0xc0009d9fb8 pc=0x30ec08e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0009d9fe8 sp=0xc0009d9fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 611 [select]:
   > runtime.gopark(0xc01299bf18?, 0x7?, 0x26?, 0xed?, 0xc01299bafa?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01ddaf958 sp=0xc01ddaf938 pc=0x13c9516
   > runtime.selectgo(0xc01ddaff18, 0xc01299baec, 0xc018d6a620?, 0x0, 0x7f4c071fffff?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01ddafa98 sp=0xc01ddaf958 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).updateStatsWorker(0xc010d0a140, {0x4134ba0?, 0xc0000f2480?}, {0x40e2a10, 0xc00ffc1180})
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1429 +0x27c fp=0xc01ddaffa8 sp=0xc01ddafa98 pc=0x2798fdc
   > github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop.func3()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1304 +0x36 fp=0xc01ddaffe0 sp=0xc01ddaffa8 pc=0x27974b6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01ddaffe8 sp=0xc01ddaffe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1304 +0x29a
   > goroutine 618 [select]:
   > runtime.gopark(0xc0009cd7a8?, 0x2?, 0x4?, 0x30?, 0xc0009cd77c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0009cd600 sp=0xc0009cd5e0 pc=0x13c9516
   > runtime.selectgo(0xc0009cd7a8, 0xc0009cd778, 0xc000a07620?, 0x0, 0xc000a076b0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0009cd740 sp=0xc0009cd600 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).PlanReplayerLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1236 +0xf6 fp=0xc0009cd7e0 sp=0xc0009cd740 pc=0x2796e36
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0009cd7e8 sp=0xc0009cd7e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).PlanReplayerLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1227 +0x6c
   > goroutine 614 [select]:
   > runtime.gopark(0xc00035ad48?, 0x3?, 0x3?, 0x0?, 0xc00035acd2?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00035ab50 sp=0xc00035ab30 pc=0x13c9516
   > runtime.selectgo(0xc00035ad48, 0xc00035accc, 0xc0005a9400?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00035ac90 sp=0xc00035ab50 pc=0x13d9bdc
   > github.com/pingcap/tidb/statistics/handle.(*Handle).drainColTask(0xc0100dc000, 0xc010d180c0)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:294 +0xe5 fp=0xc00035ad88 sp=0xc00035ac90 pc=0x2612705
   > github.com/pingcap/tidb/statistics/handle.(*Handle).HandleOneTask(0xc0100dc000, 0x0?, 0xc00035af40, {0x7f4c0848dc78, 0xc0000f2900}, 0xc0005aa140?)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:181 +0xc5 fp=0xc00035aee8 sp=0xc00035ad88 pc=0x2610fe5
   > github.com/pingcap/tidb/statistics/handle.(*Handle).SubLoadWorker(0xc0100dc000, {0x4134ba0?, 0xc0000f2900}, 0x0?, 0x0?)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:154 +0x11b fp=0xc00035afa8 sp=0xc00035aee8 pc=0x2610b3b
   > github.com/pingcap/tidb/domain.(*Domain).StartLoadStatsSubWorkers.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1318 +0x36 fp=0xc00035afe0 sp=0xc00035afa8 pc=0x27977b6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00035afe8 sp=0xc00035afe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).StartLoadStatsSubWorkers
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1318 +0x172
   > goroutine 585 [select]:
   > runtime.gopark(0xc000dbf718?, 0x3?, 0x0?, 0x30?, 0xc000dbf68a?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000dbf4c8 sp=0xc000dbf4a8 pc=0x13c9516
   > runtime.selectgo(0xc000dbf718, 0xc000dbf684, 0xc000dbf788?, 0x0, 0x13c9516?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000dbf608 sp=0xc000dbf4c8 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).LoadSysVarCacheLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1032 +0x145 fp=0xc000dbf7e0 sp=0xc000dbf608 pc=0x2794ca5
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000dbf7e8 sp=0xc000dbf7e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).LoadSysVarCacheLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1023 +0x172
   > goroutine 545 [syscall]:
   > runtime.notetsleepg(0x13d0505?, 0xc000dbffd0?)
   > 	/usr/local/go/src/runtime/lock_futex.go:236 +0x34 fp=0xc000dbffa0 sp=0xc000dbff68 pc=0x1398cd4
   > os/signal.signal_recv()
   > 	/usr/local/go/src/runtime/sigqueue.go:152 +0x2f fp=0xc000dbffc0 sp=0xc000dbffa0 pc=0x13f86cf
   > os/signal.loop()
   > 	/usr/local/go/src/os/signal/signal_unix.go:23 +0x19 fp=0xc000dbffe0 sp=0xc000dbffc0 pc=0x2ecc1f9
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000dbffe8 sp=0xc000dbffe0 pc=0x13fc6e1
   > created by os/signal.Notify.func1.1
   > 	/usr/local/go/src/os/signal/signal.go:151 +0x2a
   > goroutine 595 [select]:
   > runtime.gopark(0xc000dc0f18?, 0x3?, 0x4?, 0x30?, 0xc000dc0e9a?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000356cd8 sp=0xc000356cb8 pc=0x13c9516
   > runtime.selectgo(0xc000356f18, 0xc000dc0e94, 0xc000c3ede0?, 0x0, 0xc000b9ff20?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000356e18 sp=0xc000356cd8 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).LoadPrivilegeLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:982 +0x145 fp=0xc000356fe0 sp=0xc000356e18 pc=0x2794465
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000356fe8 sp=0xc000356fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).LoadPrivilegeLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:973 +0x205
   > goroutine 612 [select]:
   > runtime.gopark(0xc0117f3f78?, 0x2?, 0x4?, 0x30?, 0xc0117f3f4c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01bd4ddd0 sp=0xc01bd4ddb0 pc=0x13c9516
   > runtime.selectgo(0xc01bd4df78, 0xc0117f3f48, 0xc018d6a620?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01bd4df10 sp=0xc01bd4ddd0 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).autoAnalyzeWorker(0xc010d0a140, {0x40e2a10, 0xc00ffc1180})
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1487 +0x105 fp=0xc01bd4dfb8 sp=0xc01bd4df10 pc=0x2799f45
   > github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop.func4()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1307 +0x2e fp=0xc01bd4dfe0 sp=0xc01bd4dfb8 pc=0x279744e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01bd4dfe8 sp=0xc01bd4dfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1307 +0x31a
   > goroutine 652 [chan receive]:
   > runtime.gopark(0xc0112d74a0?, 0xc010030aa0?, 0x50?, 0xa?, 0xc010293da0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000fe8af8 sp=0xc000fe8ad8 pc=0x13c9516
   > runtime.chanrecv(0xc00fcedc20, 0xc00ffeebd8, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000fe8b88 sp=0xc000fe8af8 pc=0x13934bb
   > runtime.chanrecv1(0xc010008b40?, 0x40d68d0?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc000fe8bb0 sp=0xc000fe8b88 pc=0x1392fb8
   > github.com/pingcap/tidb/executor.(*ProjectionExec).parallelExecute(0xc010008b40, {0x40d68d0?, 0xc010570240?}, 0xc010030780)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:218 +0x92 fp=0xc000fe8bf8 sp=0xc000fe8bb0 pc=0x30eb612
   > github.com/pingcap/tidb/executor.(*ProjectionExec).Next(0xc010008b40, {0x40d68d0, 0xc010570240}, 0x0?)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:182 +0x78 fp=0xc000fe8c30 sp=0xc000fe8bf8 pc=0x30eb338
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc010570240}, {0x40d9720, 0xc010008b40}, 0xc010030780)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc000fe8d70 sp=0xc000fe8c30 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*recordSet).Next(0xc0100306e0, {0x40d68d0?, 0xc010570240?}, 0xc010030780)
   > 	/go/src/github.com/pingcap/tidb/executor/adapter.go:149 +0xbf fp=0xc000fe8e00 sp=0xc000fe8d70 pc=0x2fa45ff
   > github.com/pingcap/tidb/session.(*execStmtResult).Next(0xc010570210?, {0x40d68d0?, 0xc010570240?}, 0xc0000fabc0?)
   > 	<autogenerated>:1 +0x34 fp=0xc000fe8e30 sp=0xc000fe8e00 pc=0x31b8c94
   > github.com/pingcap/tidb/server.(*tidbResultSet).Next(0x60384e0?, {0x40d68d0?, 0xc010570240?}, 0x40ee040?)
   > 	/go/src/github.com/pingcap/tidb/server/driver_tidb.go:317 +0x2b fp=0xc000fe8e60 sp=0xc000fe8e30 pc=0x323ac6b
   > github.com/pingcap/tidb/server.(*clientConn).writeChunks(0xc010858000, {0x40d68d0, 0xc010570240}, {0x40dff58, 0xc010030730}, 0x0, 0xffe?)
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:2185 +0x15e fp=0xc000fe8f20 sp=0xc000fe8e60 pc=0x3231d7e
   > github.com/pingcap/tidb/server.(*clientConn).writeResultset(0xc010858000, {0x40d68d0, 0xc010570240}, {0x40dff58, 0xc010030730}, 0x40?, 0x3, 0xc00fadd088?)
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:2136 +0x23e fp=0xc000fe8fd0 sp=0xc000fe8f20 pc=0x323157e
   > github.com/pingcap/tidb/server.(*clientConn).handleStmt(0xc010858000, {0x40d6828, 0xc0101d6040}, {0x40e9b80, 0xc00fe5a240}, {0x606b430, 0x0, 0x0}, 0x1)
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:2014 +0x3c8 fp=0xc000fe9098 sp=0xc000fe8fd0 pc=0x32302c8
   > github.com/pingcap/tidb/server.(*clientConn).handleQuery(0xc010858000, {0x40d6828, 0xc0101d6040}, {0xc00fe9b681, 0x44c})
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:1850 +0x774 fp=0xc000fe9260 sp=0xc000fe9098 pc=0x322ea14
   > github.com/pingcap/tidb/server.(*clientConn).dispatch(0xc010858000, {0x40d68d0?, 0xc01061a0c0?}, {0xc00fe9b680, 0x44d, 0x44d})
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:1345 +0x1025 fp=0xc000fe9650 sp=0xc000fe9260 pc=0x322a305
   > github.com/pingcap/tidb/server.(*clientConn).Run(0xc010858000, {0x40d68d0, 0xc01061a0c0})
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:1095 +0x253 fp=0xc000fe9c58 sp=0xc000fe9650 pc=0x3226c53
   > github.com/pingcap/tidb/server.(*Server).onConn(0xc0104e2410, 0xc010858000)
   > 	/go/src/github.com/pingcap/tidb/server/server.go:551 +0x6c5 fp=0xc000fe9fc0 sp=0xc000fe9c58 pc=0x3259da5
   > github.com/pingcap/tidb/server.(*Server).startNetworkListener.func2()
   > 	/go/src/github.com/pingcap/tidb/server/server.go:448 +0x2a fp=0xc000fe9fe0 sp=0xc000fe9fc0 pc=0x3258c2a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000fe9fe8 sp=0xc000fe9fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/server.(*Server).startNetworkListener
   > 	/go/src/github.com/pingcap/tidb/server/server.go:448 +0x5ca
   > goroutine 619 [select]:
   > runtime.gopark(0xc0117f3eb0?, 0x2?, 0x27?, 0x0?, 0xc0117f3e5c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0117f3cc8 sp=0xc0117f3ca8 pc=0x13c9516
   > runtime.selectgo(0xc0117f3eb0, 0xc0117f3e58, 0xc0104e2410?, 0x0, 0xc000a1a900?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0117f3e08 sp=0xc0117f3cc8 pc=0x13d9bdc
   > github.com/pingcap/tidb/util/expensivequery.(*Handle).Run(0xc010d1c048)
   > 	/go/src/github.com/pingcap/tidb/util/expensivequery/expensivequery.go:61 +0x198 fp=0xc0117f3fc8 sp=0xc0117f3e08 pc=0x27866f8
   > main.createServer.func1()
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:695 +0x26 fp=0xc0117f3fe0 sp=0xc0117f3fc8 pc=0x343c186
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0117f3fe8 sp=0xc0117f3fe0 pc=0x13fc6e1
   > created by main.createServer
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:695 +0x44a
   > goroutine 295 [select]:
   > runtime.gopark(0xc011811f58?, 0x4?, 0xab?, 0x42?, 0xc011811da8?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc011811bf8 sp=0xc011811bd8 pc=0x13c9516
   > runtime.selectgo(0xc011811f58, 0xc011811da0, 0xc000f4ce38?, 0x0, 0x1?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc011811d38 sp=0xc011811bf8 pc=0x13d9bdc
   > github.com/pingcap/tidb/ddl.(*worker).start(0xc010d3a600, 0xc010d46270)
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl_worker.go:184 +0x318 fp=0xc011811fc0 sp=0xc011811d38 pc=0x27168b8
   > github.com/pingcap/tidb/ddl.(*ddl).Start.func3()
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:399 +0x2a fp=0xc011811fe0 sp=0xc011811fc0 pc=0x26d426a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc011811fe8 sp=0xc011811fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/ddl.(*ddl).Start
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:399 +0x58e
   > goroutine 97586 [select]:
   > runtime.gopark(0xc000635f78?, 0x2?, 0x2?, 0x0?, 0xc000635eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000635d58 sp=0xc000635d38 pc=0x13c9516
   > runtime.selectgo(0xc000635f78, 0xc000635ee8, 0x3b67af1?, 0x0, 0xc0003cddd0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000635e98 sp=0xc000635d58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc012e656c0, {0x40d68d0?, 0xc01ac388a0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc000635fb8 sp=0xc000635e98 pc=0x30ecdf4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc000635fe0 sp=0xc000635fb8 pc=0x30ec08e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000635fe8 sp=0xc000635fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 617 [select]:
   > runtime.gopark(0xc000f4ed48?, 0x3?, 0x3?, 0x0?, 0xc000f4ecd2?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000f4eb50 sp=0xc000f4eb30 pc=0x13c9516
   > runtime.selectgo(0xc000f4ed48, 0xc000f4eccc, 0xc0009e1b00?, 0x0, 0xc0009e1b60?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000f4ec90 sp=0xc000f4eb50 pc=0x13d9bdc
   > github.com/pingcap/tidb/statistics/handle.(*Handle).drainColTask(0xc0100dc000, 0xc010d180c0)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:294 +0xe5 fp=0xc000f4ed88 sp=0xc000f4ec90 pc=0x2612705
   > github.com/pingcap/tidb/statistics/handle.(*Handle).HandleOneTask(0xc0100dc000, 0xc0009e87e0?, 0xc000f4ef40, {0x7f4c0848dc78, 0xc0000f3200}, 0xc0009e8c60?)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:181 +0xc5 fp=0xc000f4eee8 sp=0xc000f4ed88 pc=0x2610fe5
   > github.com/pingcap/tidb/statistics/handle.(*Handle).SubLoadWorker(0xc0100dc000, {0x4134ba0?, 0xc0000f3200}, 0xc0009e99e0?, 0xc0009e9a10?)
   > 	/go/src/github.com/pingcap/tidb/statistics/handle/handle_hist.go:154 +0x11b fp=0xc000f4efa8 sp=0xc000f4eee8 pc=0x2610b3b
   > github.com/pingcap/tidb/domain.(*Domain).StartLoadStatsSubWorkers.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1318 +0x36 fp=0xc000f4efe0 sp=0xc000f4efa8 pc=0x27977b6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000f4efe8 sp=0xc000f4efe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).StartLoadStatsSubWorkers
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1318 +0x172
   > goroutine 620 [select, locked to thread]:
   > runtime.gopark(0xc000dc3fa8?, 0x2?, 0x0?, 0x0?, 0xc000dc3fa4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000dc3e18 sp=0xc000dc3df8 pc=0x13c9516
   > runtime.selectgo(0xc000dc3fa8, 0xc000dc3fa0, 0x0?, 0x0, 0xc010c39a80?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000dc3f58 sp=0xc000dc3e18 pc=0x13d9bdc
   > runtime.ensureSigM.func1()
   > 	/usr/local/go/src/runtime/signal_unix.go:995 +0x1b0 fp=0xc000dc3fe0 sp=0xc000dc3f58 pc=0x13de070
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000dc3fe8 sp=0xc000dc3fe0 pc=0x13fc6e1
   > created by runtime.ensureSigM
   > 	/usr/local/go/src/runtime/signal_unix.go:978 +0xbd
   > goroutine 111496 [select]:
   > runtime.gopark(0xc016af5f00?, 0x2?, 0x20?, 0x0?, 0xc016af5e44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc016af5c48 sp=0xc016af5c28 pc=0x13c9516
   > runtime.selectgo(0xc016af5f00, 0xc016af5e40, 0x6042a48?, 0x0, 0x13db115?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc016af5d88 sp=0xc016af5c48 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc01c7bd400, {0x4134ba0, 0xc0144ce240})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc016af5f30 sp=0xc016af5d88 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc01c7bd400, {0x4134ba0, 0xc0144ce240}, 0xc01942d610)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc016af5fb0 sp=0xc016af5f30 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc016af5fe0 sp=0xc016af5fb0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc016af5fe8 sp=0xc016af5fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 123572 [select]:
   > runtime.gopark(0xc000646f28?, 0x2?, 0x2?, 0x0?, 0xc000646eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000646d58 sp=0xc000646d38 pc=0x13c9516
   > runtime.selectgo(0xc000646f28, 0xc000646ee8, 0xc000646f10?, 0x0, 0xc000f03c20?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000646e98 sp=0xc000646d58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc01071ab00, {0x4134ba0, 0xc0114b7d40}, 0xc0179bdf10, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc000646fa8 sp=0xc000646e98 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc000646fe0 sp=0xc000646fa8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000646fe8 sp=0xc000646fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 294 [select]:
   > runtime.gopark(0xc012817f90?, 0x2?, 0x0?, 0x0?, 0xc012817f6c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0117f7df0 sp=0xc0117f7dd0 pc=0x13c9516
   > runtime.selectgo(0xc0117f7f90, 0xc012817f68, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0117f7f30 sp=0xc0117f7df0 pc=0x13d9bdc
   > github.com/pingcap/tidb/ddl.(*delRange).startEmulator(0xc00057dce0)
   > 	/go/src/github.com/pingcap/tidb/ddl/delete_range.go:140 +0x125 fp=0xc0117f7fc8 sp=0xc0117f7f30 pc=0x271fb25
   > github.com/pingcap/tidb/ddl.(*delRange).start.func1()
   > 	/go/src/github.com/pingcap/tidb/ddl/delete_range.go:122 +0x26 fp=0xc0117f7fe0 sp=0xc0117f7fc8 pc=0x271f8e6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0117f7fe8 sp=0xc0117f7fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/ddl.(*delRange).start
   > 	/go/src/github.com/pingcap/tidb/ddl/delete_range.go:122 +0x6d
   > goroutine 626 [chan receive]:
   > runtime.gopark(0x606d020?, 0xc00ff1df20?, 0x28?, 0xa3?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00ff1dea0 sp=0xc00ff1de80 pc=0x13c9516
   > runtime.chanrecv(0xc0109d5860, 0xc00ff1dfa0, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc00ff1df30 sp=0xc00ff1dea0 pc=0x13934bb
   > runtime.chanrecv1(0xc01094eab0?, 0x0?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc00ff1df58 sp=0xc00ff1df30 pc=0x1392fb8
   > github.com/pingcap/tidb/util/signal.SetupSignalHandler.func1()
   > 	/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:38 +0x4f fp=0xc00ff1dfe0 sp=0xc00ff1df58 pc=0x343388f
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00ff1dfe8 sp=0xc00ff1dfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/util/signal.SetupSignalHandler
   > 	/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:35 +0xb6
   > goroutine 298 [select]:
   > runtime.gopark(0xc010d99de8?, 0x2?, 0x4?, 0x30?, 0xc010d99d4c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010d99bd0 sp=0xc010d99bb0 pc=0x13c9516
   > runtime.selectgo(0xc010d99de8, 0xc010d99d48, 0xc01938e6c0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010d99d10 sp=0xc010d99bd0 pc=0x13d9bdc
   > github.com/pingcap/tidb/ddl.(*ddl).PollTiFlashRoutine(0xc010d1e200)
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl_tiflash_api.go:577 +0x273 fp=0xc010d99f98 sp=0xc010d99d10 pc=0x27159b3
   > github.com/pingcap/tidb/ddl.(*ddl).PollTiFlashRoutine-fm()
   > 	<autogenerated>:1 +0x26 fp=0xc010d99fb0 sp=0xc010d99f98 pc=0x2768c06
   > github.com/pingcap/tidb/util.(*WaitGroupWrapper).Run.func1()
   > 	/go/src/github.com/pingcap/tidb/util/wait_group_wrapper.go:33 +0x5a fp=0xc010d99fe0 sp=0xc010d99fb0 pc=0x209361a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010d99fe8 sp=0xc010d99fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/util.(*WaitGroupWrapper).Run
   > 	/go/src/github.com/pingcap/tidb/util/wait_group_wrapper.go:31 +0x85
   > goroutine 299 [select]:
   > runtime.gopark(0xc00ffe7f50?, 0x4?, 0x4?, 0x30?, 0xc00ffe7d00?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01e035b78 sp=0xc01e035b58 pc=0x13c9516
   > runtime.selectgo(0xc01e035f50, 0xc00ffe7cf8, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01e035cb8 sp=0xc01e035b78 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).loadSchemaInLoop(0xc010d0a140, {0x40d6828, 0xc00057e1c0}, 0xc00ff1ad38?)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:593 +0x1aa fp=0xc01e035fb0 sp=0xc01e035cb8 pc=0x2790e2a
   > github.com/pingcap/tidb/domain.(*Domain).Init.func10()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:864 +0x32 fp=0xc01e035fe0 sp=0xc01e035fb0 pc=0x27939f2
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01e035fe8 sp=0xc01e035fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:864 +0xe6b
   > goroutine 300 [select]:
   > runtime.gopark(0xc000dc0778?, 0x3?, 0x4?, 0x30?, 0xc000dc0712?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000dc0560 sp=0xc000dc0540 pc=0x13c9516
   > runtime.selectgo(0xc000dc0778, 0xc000dc070c, 0x2?, 0x0, 0xc00fc2abc0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000dc06a0 sp=0xc000dc0560 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).topNSlowQueryLoop(0xc010d0a140)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:483 +0x194 fp=0xc000dc07c8 sp=0xc000dc06a0 pc=0x278f654
   > github.com/pingcap/tidb/domain.(*Domain).Init.func11()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:867 +0x26 fp=0xc000dc07e0 sp=0xc000dc07c8 pc=0x2793986
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000dc07e8 sp=0xc000dc07e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:867 +0xed2
   > goroutine 301 [select]:
   > runtime.gopark(0xc000dc5ef8?, 0x3?, 0x4?, 0x30?, 0xc000dc5e82?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000dc5d08 sp=0xc000dc5ce8 pc=0x13c9516
   > runtime.selectgo(0xc000dc5ef8, 0xc000dc5e7c, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000dc5e48 sp=0xc000dc5d08 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).infoSyncerKeeper(0xc010d0a140)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:515 +0x165 fp=0xc000dc5fc8 sp=0xc000dc5e48 pc=0x278fb85
   > github.com/pingcap/tidb/domain.(*Domain).Init.func12()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:868 +0x26 fp=0xc000dc5fe0 sp=0xc000dc5fc8 pc=0x2793926
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000dc5fe8 sp=0xc000dc5fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:868 +0xf15
   > goroutine 302 [select]:
   > runtime.gopark(0xc000dc1eb0?, 0x2?, 0x20?, 0x2f?, 0xc000dc1e7c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000f4bce8 sp=0xc000f4bcc8 pc=0x13c9516
   > runtime.selectgo(0xc000f4beb0, 0xc000dc1e78, 0x1?, 0x0, 0x9?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000f4be28 sp=0xc000f4bce8 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).globalConfigSyncerKeeper(0xc010d0a140)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:538 +0xf5 fp=0xc000f4bfc8 sp=0xc000f4be28 pc=0x2790155
   > github.com/pingcap/tidb/domain.(*Domain).Init.func13()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:869 +0x26 fp=0xc000f4bfe0 sp=0xc000f4bfc8 pc=0x27938c6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000f4bfe8 sp=0xc000f4bfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:869 +0xf5c
   > goroutine 303 [select]:
   > runtime.gopark(0xc000dc4e78?, 0x3?, 0x4?, 0x30?, 0xc000dc4df2?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000f4dc78 sp=0xc000f4dc58 pc=0x13c9516
   > runtime.selectgo(0xc000f4de78, 0xc000dc4dec, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000f4ddb8 sp=0xc000f4dc78 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).topologySyncerKeeper(0xc010d0a140)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:561 +0x165 fp=0xc000f4dfc8 sp=0xc000f4ddb8 pc=0x2790645
   > github.com/pingcap/tidb/domain.(*Domain).Init.func14()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:872 +0x26 fp=0xc000f4dfe0 sp=0xc000f4dfc8 pc=0x2793866
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000f4dfe8 sp=0xc000f4dfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:872 +0xfbd
   > goroutine 537 [select]:
   > runtime.gopark(0xc015d3cf28?, 0x2?, 0x6?, 0x30?, 0xc015d3ced4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc015d3cd48 sp=0xc015d3cd28 pc=0x13c9516
   > runtime.selectgo(0xc015d3cf28, 0xc015d3ced0, 0xc010d26d80?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc015d3ce88 sp=0xc015d3cd48 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).handleEvolvePlanTasksLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1151 +0x107 fp=0xc015d3cfe0 sp=0xc015d3ce88 pc=0x2795ee7
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc015d3cfe8 sp=0xc015d3cfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).handleEvolvePlanTasksLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1144 +0xe5
   > goroutine 97587 [select]:
   > runtime.gopark(0xc011572f78?, 0x2?, 0x0?, 0x0?, 0xc011572eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc011572d58 sp=0xc011572d38 pc=0x13c9516
   > runtime.selectgo(0xc011572f78, 0xc011572ee8, 0x3b67af1?, 0x0, 0x5?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc011572e98 sp=0xc011572d58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc012e65700, {0x40d68d0?, 0xc01ac388a0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc011572fb8 sp=0xc011572e98 pc=0x30ecdf4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc011572fe0 sp=0xc011572fb8 pc=0x30ec08e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc011572fe8 sp=0xc011572fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 111491 [select]:
   > runtime.gopark(0xc016af2f28?, 0x2?, 0x0?, 0x0?, 0xc016af2eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc016af2d58 sp=0xc016af2d38 pc=0x13c9516
   > runtime.selectgo(0xc016af2f28, 0xc016af2ee8, 0x48?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc016af2e98 sp=0xc016af2d58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc01c7bd0c0, {0x4134ba0, 0xc0144ce240}, 0xc01942d600, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc016af2fa8 sp=0xc016af2e98 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc016af2fe0 sp=0xc016af2fa8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc016af2fe8 sp=0xc016af2fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 536 [select]:
   > runtime.gopark(0xc01180de90?, 0x3?, 0x30?, 0xd8?, 0xc01180de02?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01bd4bc70 sp=0xc01bd4bc50 pc=0x13c9516
   > runtime.selectgo(0xc01bd4be90, 0xc01180ddfc, 0x3b47e2c?, 0x0, 0x1?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01bd4bdb0 sp=0xc01bd4bc70 pc=0x13d9bdc
   > github.com/pingcap/tidb/domain.(*Domain).globalBindHandleWorkerLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1114 +0x16f fp=0xc01bd4bfe0 sp=0xc01bd4bdb0 pc=0x279564f
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01bd4bfe8 sp=0xc01bd4bfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).globalBindHandleWorkerLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1101 +0xad
   > goroutine 111490 [select]:
   > runtime.gopark(0xc000647f28?, 0x2?, 0xc7?, 0x95?, 0xc000647eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000647d58 sp=0xc000647d38 pc=0x13c9516
   > runtime.selectgo(0xc000647f28, 0xc000647ee8, 0xc000647ed8?, 0x0, 0xc01c43efe8?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000647e98 sp=0xc000647d58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc01c7bd000, {0x4134ba0, 0xc0144ce240}, 0xc01942d600, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc000647fa8 sp=0xc000647e98 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc000647fe0 sp=0xc000647fa8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000647fe8 sp=0xc000647fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 591 [select]:
   > runtime.gopark(0xc000336f90?, 0x2?, 0xd0?, 0x6d?, 0xc000336f3c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000336d90 sp=0xc000336d70 pc=0x13c9516
   > runtime.selectgo(0xc000336f90, 0xc000336f38, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000336ed0 sp=0xc000336d90 pc=0x13d9bdc
   > github.com/pingcap/tidb/util/topsql/reporter.(*RemoteTopSQLReporter).reportWorker(0xc0000d8c00)
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:261 +0xfd fp=0xc000336fc8 sp=0xc000336ed0 pc=0x25a231d
   > github.com/pingcap/tidb/util/topsql/reporter.(*RemoteTopSQLReporter).Start.func2()
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:111 +0x26 fp=0xc000336fe0 sp=0xc000336fc8 pc=0x25a1166
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000336fe8 sp=0xc000336fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/util/topsql/reporter.(*RemoteTopSQLReporter).Start
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:111 +0xaa
   > goroutine 589 [select]:
   > runtime.gopark(0xc000335780?, 0x3?, 0x10?, 0x0?, 0xc000335742?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0003355c8 sp=0xc0003355a8 pc=0x13c9516
   > runtime.selectgo(0xc000335780, 0xc00033573c, 0x0?, 0x0, 0xc000335758?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000335708 sp=0xc0003355c8 pc=0x13d9bdc
   > github.com/pingcap/tidb/util/topsql/collector.(*SQLCPUCollector).collectSQLCPULoop(0xc0005a1130)
   > 	/go/src/github.com/pingcap/tidb/util/topsql/collector/cpu.go:121 +0x1a5 fp=0xc0003357c8 sp=0xc000335708 pc=0x25974a5
   > github.com/pingcap/tidb/util/topsql/collector.(*SQLCPUCollector).Start.func1()
   > 	/go/src/github.com/pingcap/tidb/util/topsql/collector/cpu.go:83 +0x26 fp=0xc0003357e0 sp=0xc0003357c8 pc=0x25971c6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0003357e8 sp=0xc0003357e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/util/topsql/collector.(*SQLCPUCollector).Start
   > 	/go/src/github.com/pingcap/tidb/util/topsql/collector/cpu.go:83 +0xca
   > goroutine 590 [select]:
   > runtime.gopark(0xc000338f68?, 0x4?, 0x8?, 0x0?, 0xc000338ee8?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000338d48 sp=0xc000338d28 pc=0x13c9516
   > runtime.selectgo(0xc000338f68, 0xc000338ee0, 0xc010f44ec0?, 0x0, 0xc010f44fc0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000338e88 sp=0xc000338d48 pc=0x13d9bdc
   > github.com/pingcap/tidb/util/topsql/reporter.(*RemoteTopSQLReporter).collectWorker(0xc0000d8c00)
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:175 +0x18e fp=0xc000338fc8 sp=0xc000338e88 pc=0x25a162e
   > github.com/pingcap/tidb/util/topsql/reporter.(*RemoteTopSQLReporter).Start.func1()
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:110 +0x26 fp=0xc000338fe0 sp=0xc000338fc8 pc=0x25a11c6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000338fe8 sp=0xc000338fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/util/topsql/reporter.(*RemoteTopSQLReporter).Start
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:110 +0x6a
   > goroutine 592 [select]:
   > runtime.gopark(0xc0009cc748?, 0x3?, 0x0?, 0x30?, 0xc0009cc6e2?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0009cc550 sp=0xc0009cc530 pc=0x13c9516
   > runtime.selectgo(0xc0009cc748, 0xc0009cc6dc, 0xc0009db200?, 0x0, 0xc0009cc6d8?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0009cc690 sp=0xc0009cc550 pc=0x13d9bdc
   > github.com/pingcap/tidb/util/topsql/reporter.(*SingleTargetDataSink).run(0xc0005a1180)
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/single_target.go:116 +0x12f fp=0xc0009cc790 sp=0xc0009cc690 pc=0x25a34af
   > github.com/pingcap/tidb/util/topsql/reporter.(*SingleTargetDataSink).recoverRun(0xc0005a1180)
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/single_target.go:98 +0x65 fp=0xc0009cc7c8 sp=0xc0009cc790 pc=0x25a30e5
   > github.com/pingcap/tidb/util/topsql/reporter.(*SingleTargetDataSink).Start.func1()
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/single_target.go:82 +0x26 fp=0xc0009cc7e0 sp=0xc0009cc7c8 pc=0x25a3046
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0009cc7e8 sp=0xc0009cc7e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/util/topsql/reporter.(*SingleTargetDataSink).Start
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/single_target.go:82 +0x2ab
   > goroutine 593 [select]:
   > runtime.gopark(0xc0009caf90?, 0x2?, 0x18?, 0x92?, 0xc0009caf6c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0009cadf0 sp=0xc0009cadd0 pc=0x13c9516
   > runtime.selectgo(0xc0009caf90, 0xc0009caf68, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0009caf30 sp=0xc0009cadf0 pc=0x13d9bdc
   > github.com/pingcap/tidb/util/topsql/stmtstats.(*aggregator).run(0xc00019f200)
   > 	/go/src/github.com/pingcap/tidb/util/topsql/stmtstats/aggregator.go:67 +0xff fp=0xc0009cafc8 sp=0xc0009caf30 pc=0x1fbf99f
   > github.com/pingcap/tidb/util/topsql/stmtstats.(*aggregator).start.func1()
   > 	/go/src/github.com/pingcap/tidb/util/topsql/stmtstats/aggregator.go:56 +0x26 fp=0xc0009cafe0 sp=0xc0009cafc8 pc=0x1fbf866
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0009cafe8 sp=0xc0009cafe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/util/topsql/stmtstats.(*aggregator).start
   > 	/go/src/github.com/pingcap/tidb/util/topsql/stmtstats/aggregator.go:56 +0xd6
   > goroutine 642 [IO wait]:
   > runtime.gopark(0xc0107571e0?, 0xc010d9d878?, 0x0?, 0x0?, 0xc010d9d8c8?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010d9d858 sp=0xc010d9d838 pc=0x13c9516
   > runtime.netpollblock(0xc0107571e0?, 0x2?, 0x0?)
   > 	/usr/local/go/src/runtime/netpoll.go:526 +0xf7 fp=0xc010d9d890 sp=0xc010d9d858 pc=0x13c18f7
   > internal/poll.runtime_pollWait(0x7f4c08825dc8, 0x72)
   > 	/usr/local/go/src/runtime/netpoll.go:305 +0x89 fp=0xc010d9d8b0 sp=0xc010d9d890 pc=0x13f5d09
   > internal/poll.(*pollDesc).wait(0xc0114b4900?, 0xd0?, 0x0)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:84 +0x32 fp=0xc010d9d8d8 sp=0xc010d9d8b0 pc=0x1473092
   > internal/poll.(*pollDesc).waitRead(...)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:89
   > internal/poll.(*FD).Accept(0xc0114b4900)
   > 	/usr/local/go/src/internal/poll/fd_unix.go:614 +0x234 fp=0xc010d9d970 sp=0xc010d9d8d8 pc=0x1478494
   > net.(*netFD).accept(0xc0114b4900)
   > 	/usr/local/go/src/net/fd_unix.go:172 +0x35 fp=0xc010d9da28 sp=0xc010d9d970 pc=0x1597315
   > net.(*TCPListener).accept(0xc00ffcacc0)
   > 	/usr/local/go/src/net/tcpsock_posix.go:142 +0x28 fp=0xc010d9da58 sp=0xc010d9da28 pc=0x15b3288
   > net.(*TCPListener).Accept(0xc00ffcacc0)
   > 	/usr/local/go/src/net/tcpsock.go:288 +0x3d fp=0xc010d9da88 sp=0xc010d9da58 pc=0x15b22fd
   > github.com/soheilhy/cmux.(*cMux).Serve(0xc000eb8fa0)
   > 	/go/pkg/mod/github.com/soheilhy/cmux@v0.1.5/cmux.go:170 +0xa9 fp=0xc010d9db18 sp=0xc010d9da88 pc=0x31eb249
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer(0xc0104e2410, 0xc00062cd80)
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:473 +0x4f7 fp=0xc010d9dc90 sp=0xc010d9db18 pc=0x324fe57
   > github.com/pingcap/tidb/server.(*Server).startHTTPServer(0xc0104e2410)
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:446 +0x1610 fp=0xc010d9dfc8 sp=0xc010d9dc90 pc=0x324f250
   > github.com/pingcap/tidb/server.(*Server).startStatusHTTP.func1()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:62 +0x26 fp=0xc010d9dfe0 sp=0xc010d9dfc8 pc=0x324b8c6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010d9dfe8 sp=0xc010d9dfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/server.(*Server).startStatusHTTP
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:62 +0x56
   > goroutine 643 [IO wait]:
   > runtime.gopark(0x18?, 0xc000b0c000?, 0x40?, 0x94?, 0xc000576b70?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000576b00 sp=0xc000576ae0 pc=0x13c9516
   > runtime.netpollblock(0x14?, 0x24f6d45?, 0x0?)
   > 	/usr/local/go/src/runtime/netpoll.go:526 +0xf7 fp=0xc000576b38 sp=0xc000576b00 pc=0x13c18f7
   > internal/poll.runtime_pollWait(0x7f4c08825fa8, 0x72)
   > 	/usr/local/go/src/runtime/netpoll.go:305 +0x89 fp=0xc000576b58 sp=0xc000576b38 pc=0x13f5d09
   > internal/poll.(*pollDesc).wait(0xc0114b4700?, 0xc000576d20?, 0x0)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:84 +0x32 fp=0xc000576b80 sp=0xc000576b58 pc=0x1473092
   > internal/poll.(*pollDesc).waitRead(...)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:89
   > internal/poll.(*FD).Accept(0xc0114b4700)
   > 	/usr/local/go/src/internal/poll/fd_unix.go:614 +0x234 fp=0xc000576c18 sp=0xc000576b80 pc=0x1478494
   > net.(*netFD).accept(0xc0114b4700)
   > 	/usr/local/go/src/net/fd_unix.go:172 +0x35 fp=0xc000576cd0 sp=0xc000576c18 pc=0x1597315
   > net.(*TCPListener).accept(0xc00ffcaca8)
   > 	/usr/local/go/src/net/tcpsock_posix.go:142 +0x28 fp=0xc000576d00 sp=0xc000576cd0 pc=0x15b3288
   > net.(*TCPListener).Accept(0xc00ffcaca8)
   > 	/usr/local/go/src/net/tcpsock.go:288 +0x3d fp=0xc000576d30 sp=0xc000576d00 pc=0x15b22fd
   > github.com/pingcap/tidb/server.(*Server).startNetworkListener(0xc0104e2410, {0x40d4c30, 0xc00ffcaca8}, 0x0, 0xc010d46270?)
   > 	/go/src/github.com/pingcap/tidb/server/server.go:378 +0xa6 fp=0xc000576fa8 sp=0xc000576d30 pc=0x32581c6
   > github.com/pingcap/tidb/server.(*Server).Run.func1()
   > 	/go/src/github.com/pingcap/tidb/server/server.go:363 +0x34 fp=0xc000576fe0 sp=0xc000576fa8 pc=0x32580f4
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000576fe8 sp=0xc000576fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/server.(*Server).Run
   > 	/go/src/github.com/pingcap/tidb/server/server.go:363 +0x145
   > goroutine 644 [IO wait]:
   > runtime.gopark(0x0?, 0x0?, 0x0?, 0x0?, 0xc010d90b78?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010d90b08 sp=0xc010d90ae8 pc=0x13c9516
   > runtime.netpollblock(0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/netpoll.go:526 +0xf7 fp=0xc010d90b40 sp=0xc010d90b08 pc=0x13c18f7
   > internal/poll.runtime_pollWait(0x7f4c08825eb8, 0x72)
   > 	/usr/local/go/src/runtime/netpoll.go:305 +0x89 fp=0xc010d90b60 sp=0xc010d90b40 pc=0x13f5d09
   > internal/poll.(*pollDesc).wait(0xc0114b4780?, 0x13a3201?, 0x0)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:84 +0x32 fp=0xc010d90b88 sp=0xc010d90b60 pc=0x1473092
   > internal/poll.(*pollDesc).waitRead(...)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:89
   > internal/poll.(*FD).Accept(0xc0114b4780)
   > 	/usr/local/go/src/internal/poll/fd_unix.go:614 +0x234 fp=0xc010d90c20 sp=0xc010d90b88 pc=0x1478494
   > net.(*netFD).accept(0xc0114b4780)
   > 	/usr/local/go/src/net/fd_unix.go:172 +0x35 fp=0xc010d90cd8 sp=0xc010d90c20 pc=0x1597315
   > net.(*UnixListener).accept(0xc00033a548?)
   > 	/usr/local/go/src/net/unixsock_posix.go:166 +0x1c fp=0xc010d90d00 sp=0xc010d90cd8 pc=0x15b9c1c
   > net.(*UnixListener).Accept(0xc000de85d0)
   > 	/usr/local/go/src/net/unixsock.go:260 +0x3d fp=0xc010d90d30 sp=0xc010d90d00 pc=0x15b82bd
   > github.com/pingcap/tidb/server.(*Server).startNetworkListener(0xc0104e2410, {0x40d4c60, 0xc000de85d0}, 0x1, 0xc00033a538?)
   > 	/go/src/github.com/pingcap/tidb/server/server.go:378 +0xa6 fp=0xc010d90fa8 sp=0xc010d90d30 pc=0x32581c6
   > github.com/pingcap/tidb/server.(*Server).Run.func2()
   > 	/go/src/github.com/pingcap/tidb/server/server.go:364 +0x37 fp=0xc010d90fe0 sp=0xc010d90fa8 pc=0x3258097
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010d90fe8 sp=0xc010d90fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/server.(*Server).Run
   > 	/go/src/github.com/pingcap/tidb/server/server.go:364 +0x1db
   > goroutine 661 [select]:
   > runtime.gopark(0xc000577d68?, 0x2?, 0xdc?, 0x2a?, 0xc000577d54?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000577be0 sp=0xc000577bc0 pc=0x13c9516
   > runtime.selectgo(0xc000577d68, 0xc000577d50, 0xc00ffc9440?, 0x0, 0xc000577d88?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000577d20 sp=0xc000577be0 pc=0x13d9bdc
   > github.com/soheilhy/cmux.muxListener.Accept(...)
   > 	/go/pkg/mod/github.com/soheilhy/cmux@v0.1.5/cmux.go:262
   > github.com/soheilhy/cmux.(*muxListener).Accept(0x40ba820?)
   > 	<autogenerated>:1 +0x7e fp=0xc000577d98 sp=0xc000577d20 pc=0x31ece5e
   > google.golang.org/grpc.(*Server).Serve(0xc0100c28c0, {0x40d5e60, 0xc0114b0860})
   > 	/go/pkg/mod/google.golang.org/grpc@v1.44.0/server.go:779 +0x362 fp=0xc000577eb0 sp=0xc000577d98 pc=0x199d262
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer.func1()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:464 +0x37 fp=0xc000577f90 sp=0xc000577eb0 pc=0x3250357
   > github.com/pingcap/tidb/util.WithRecovery(0x324b8c6?, 0xc00fc0a4e0?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc000577fc0 sp=0xc000577f90 pc=0x208e513
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer.func5()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:463 +0x28 fp=0xc000577fe0 sp=0xc000577fc0 pc=0x32502e8
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000577fe8 sp=0xc000577fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:463 +0x438
   > goroutine 662 [select]:
   > runtime.gopark(0xc010d94d38?, 0x2?, 0x4?, 0x0?, 0xc010d94d24?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010d94bb0 sp=0xc010d94b90 pc=0x13c9516
   > runtime.selectgo(0xc010d94d38, 0xc010d94d20, 0xc010d94d01?, 0x0, 0x139a507?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010d94cf0 sp=0xc010d94bb0 pc=0x13d9bdc
   > github.com/soheilhy/cmux.muxListener.Accept(...)
   > 	/go/pkg/mod/github.com/soheilhy/cmux@v0.1.5/cmux.go:262
   > github.com/soheilhy/cmux.(*muxListener).Accept(0x59083d0?)
   > 	<autogenerated>:1 +0x7e fp=0xc010d94d68 sp=0xc010d94cf0 pc=0x31ece5e
   > net/http.(*onceCloseListener).Accept(0x40d6860?)
   > 	<autogenerated>:1 +0x2a fp=0xc010d94d80 sp=0xc010d94d68 pc=0x16ee8ea
   > net/http.(*Server).Serve(0xc010d4fa40, {0x40d5e60, 0xc0114b0840})
   > 	/usr/local/go/src/net/http/server.go:3070 +0x385 fp=0xc010d94eb0 sp=0xc010d94d80 pc=0x16c4bc5
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer.func2()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:469 +0x37 fp=0xc010d94f90 sp=0xc010d94eb0 pc=0x32500f7
   > github.com/pingcap/tidb/util.WithRecovery(0x40d6860?, 0xc000058058?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc010d94fc0 sp=0xc010d94f90 pc=0x208e513
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer.func6()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:468 +0x28 fp=0xc010d94fe0 sp=0xc010d94fc0 pc=0x3250088
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010d94fe8 sp=0xc010d94fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:468 +0x4ea
   > goroutine 95076 [semacquire]:
   > runtime.gopark(0x0?, 0x1?, 0xa0?, 0x94?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00062eeb8 sp=0xc00062ee98 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc018208578, 0x40?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc00062ef20 sp=0xc00062eeb8 pc=0x13dae5e
   > sync.runtime_Semacquire(0xc0142a9400?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc00062ef50 sp=0xc00062ef20 pc=0x13f7f65
   > sync.(*WaitGroup).Wait(0x35b123d05?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc00062ef78 sp=0xc00062ef50 pc=0x140b312
   > github.com/pingcap/tidb/executor.(*HashAggExec).waitAllWorkersAndCloseFinalOutputCh(0xc010d43400, {0xc00062efb8, 0x3, 0x4134ba0?})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:827 +0x35 fp=0xc00062ef98 sp=0xc00062ef78 pc=0x2fbc5b5
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func6()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:864 +0x5a fp=0xc00062efe0 sp=0xc00062ef98 pc=0x2fbcc1a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00062efe8 sp=0xc00062efe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:864 +0x54d
   > goroutine 94647 [chan receive]:
   > runtime.gopark(0xc01c2ef760?, 0x13d1800?, 0xc0?, 0xc3?, 0xc000468b60?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01c2ef758 sp=0xc01c2ef738 pc=0x13c9516
   > runtime.chanrecv(0xc013f236e0, 0xc01c2ef840, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc01c2ef7e8 sp=0xc01c2ef758 pc=0x13934bb
   > runtime.chanrecv2(0xc000733e00?, 0x40d68d0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc01c2ef810 sp=0xc01c2ef7e8 pc=0x1392ff8
   > github.com/pingcap/tidb/executor.(*UnionExec).Next(0xc000733e00, {0x40d68d0, 0xc010570240}, 0xc01926c140)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1702 +0x85 fp=0xc01c2ef878 sp=0xc01c2ef810 pc=0x30425c5
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc010570240}, {0x40d9ea0, 0xc000733e00}, 0xc01926c140)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc01c2ef9b8 sp=0xc01c2ef878 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*MaxOneRowExec).Next(0xc0100122a0, {0x40d68d0, 0xc010570240}, 0xc01926c140)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1518 +0xa8 fp=0xc01c2efa08 sp=0xc01c2ef9b8 pc=0x30413a8
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc010570240}, {0x40d94a0, 0xc0100122a0}, 0xc01926c140)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc01c2efb48 sp=0xc01c2efa08 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*NestedLoopApplyExec).fetchAllInners(0xc000361340, {0x40d68d0, 0xc010570240})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:979 +0x346 fp=0xc01c2efc40 sp=0xc01c2efb48 pc=0x30b2966
   > github.com/pingcap/tidb/executor.(*NestedLoopApplyExec).Next(0xc000361340, {0x40d68d0, 0xc010570240}, 0xc01926c230)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:1032 +0x5b6 fp=0xc01c2efda0 sp=0xc01c2efc40 pc=0x30b32b6
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc010570240}, {0x40d9560, 0xc000361340}, 0xc01926c230)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc01c2efee0 sp=0xc01c2efda0 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*HashAggExec).fetchChildData(0xc010d43400, {0x40d68d0, 0xc010570240}, 0x60384e0?)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:798 +0x1be fp=0xc01c2effb0 sp=0xc01c2efee0 pc=0x2fbc0fe
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func3()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:835 +0x32 fp=0xc01c2effe0 sp=0xc01c2effb0 pc=0x2fbce72
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01c2effe8 sp=0xc01c2effe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:835 +0xea
   > goroutine 123576 [select]:
   > runtime.gopark(0xc0009dff00?, 0x2?, 0xa0?, 0x4b?, 0xc0009dfe44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0009dfc48 sp=0xc0009dfc28 pc=0x13c9516
   > runtime.selectgo(0xc0009dff00, 0xc0009dfe40, 0x2c40?, 0x0, 0x6042d80?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0009dfd88 sp=0xc0009dfc48 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc01071ad80, {0x4134ba0, 0xc0114b7d40})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc0009dff30 sp=0xc0009dfd88 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc01071ad80, {0x4134ba0, 0xc0114b7d40}, 0xc0179bdf20)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc0009dffb0 sp=0xc0009dff30 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc0009dffe0 sp=0xc0009dffb0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0009dffe8 sp=0xc0009dffe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 745 [chan receive]:
   > runtime.gopark(0xc018f1b290?, 0xc00fbbe680?, 0x6d?, 0xcb?, 0xc01c5df2d0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01e4ff228 sp=0xc01e4ff208 pc=0x13c9516
   > runtime.chanrecv(0xc019c50120, 0xc01c5df300, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc01e4ff2b8 sp=0xc01e4ff228 pc=0x13934bb
   > runtime.chanrecv2(0xc010d43400?, 0x40d68d0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc01e4ff2e0 sp=0xc01e4ff2b8 pc=0x1392ff8
   > github.com/pingcap/tidb/executor.(*HashAggExec).parallelExec(0xc010d43400, {0x40d68d0?, 0xc010570240?}, 0xc01926caa0)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:888 +0x89 fp=0xc01e4ff318 sp=0xc01e4ff2e0 pc=0x2fbcf29
   > github.com/pingcap/tidb/executor.(*HashAggExec).Next(0x40d68d0?, {0x40d68d0?, 0xc010570240?}, 0x7f4c0770a201?)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:768 +0x76 fp=0xc01e4ff348 sp=0xc01e4ff318 pc=0x2fbbeb6
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc010570240}, {0x40d9120, 0xc010d43400}, 0xc01926caa0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc01e4ff488 sp=0xc01e4ff348 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*SortExec).fetchRowChunks(0xc010008900, {0x40d68d0, 0xc010570240})
   > 	/go/src/github.com/pingcap/tidb/executor/sort.go:195 +0x596 fp=0xc01e4ff5e8 sp=0xc01e4ff488 pc=0x3135156
   > github.com/pingcap/tidb/executor.(*SortExec).Next(0xc010008900, {0x40d68d0, 0xc010570240}, 0xc01926ca00)
   > 	/go/src/github.com/pingcap/tidb/executor/sort.go:113 +0x325 fp=0xc01e4ff660 sp=0xc01e4ff5e8 pc=0x31346c5
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc010570240}, {0x40d9c20, 0xc010008900}, 0xc01926ca00)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc01e4ff7a0 sp=0xc01e4ff660 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*MaxOneRowExec).Next(0xc010012540, {0x40d68d0, 0xc010570240}, 0xc01926ca00)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1518 +0xa8 fp=0xc01e4ff7f0 sp=0xc01e4ff7a0 pc=0x30413a8
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc010570240}, {0x40d94a0, 0xc010012540}, 0xc01926ca00)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc01e4ff930 sp=0xc01e4ff7f0 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*SelectionExec).Next(0xc00ff45d40, {0x40d68d0, 0xc010570240}, 0xc01000b950)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1394 +0xed fp=0xc01e4ff9c0 sp=0xc01e4ff930 pc=0x304012d
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc010570240}, {0x40d9960, 0xc00ff45d40}, 0xc01000b950)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc01e4ffb00 sp=0xc01e4ff9c0 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*NestedLoopApplyExec).fetchAllInners(0xc000361500, {0x40d68d0, 0xc010570240})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:979 +0x346 fp=0xc01e4ffbf8 sp=0xc01e4ffb00 pc=0x30b2966
   > github.com/pingcap/tidb/executor.(*NestedLoopApplyExec).Next(0xc000361500, {0x40d68d0, 0xc010570240}, 0xc0100307d0)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:1032 +0x5b6 fp=0xc01e4ffd58 sp=0xc01e4ffbf8 pc=0x30b32b6
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc010570240}, {0x40d9560, 0xc000361500}, 0xc0100307d0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc01e4ffe98 sp=0xc01e4ffd58 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*projectionInputFetcher).run(0xc010008bc0, {0x40d68d0, 0xc010570240})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:381 +0x2f0 fp=0xc01e4fffb8 sp=0xc01e4ffe98 pc=0x30ec890
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:272 +0x2e fp=0xc01e4fffe0 sp=0xc01e4fffb8 pc=0x30ec0ee
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01e4fffe8 sp=0xc01e4fffe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:272 +0x67e
   > goroutine 746 [select]:
   > runtime.gopark(0xc0009ca778?, 0x2?, 0x0?, 0x0?, 0xc0009ca6ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0009ca558 sp=0xc0009ca538 pc=0x13c9516
   > runtime.selectgo(0xc0009ca778, 0xc0009ca6e8, 0x3b67af1?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0009ca698 sp=0xc0009ca558 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc0103653c0, {0x40d68d0?, 0xc010570240?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc0009ca7b8 sp=0xc0009ca698 pc=0x30ecdf4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc0009ca7e0 sp=0xc0009ca7b8 pc=0x30ec08e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0009ca7e8 sp=0xc0009ca7e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 747 [select]:
   > runtime.gopark(0xc0009ccf78?, 0x2?, 0xc0?, 0x80?, 0xc0009cceec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0009ccd58 sp=0xc0009ccd38 pc=0x13c9516
   > runtime.selectgo(0xc0009ccf78, 0xc0009ccee8, 0x3b67af1?, 0x0, 0x139805d?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0009cce98 sp=0xc0009ccd58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc010365440, {0x40d68d0?, 0xc010570240?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc0009ccfb8 sp=0xc0009cce98 pc=0x30ecdf4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc0009ccfe0 sp=0xc0009ccfb8 pc=0x30ec08e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0009ccfe8 sp=0xc0009ccfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 748 [select]:
   > runtime.gopark(0xc0009cb778?, 0x2?, 0xc0?, 0x80?, 0xc0009cb6ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0009cb558 sp=0xc0009cb538 pc=0x13c9516
   > runtime.selectgo(0xc0009cb778, 0xc0009cb6e8, 0x3b67af1?, 0x0, 0x139805d?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0009cb698 sp=0xc0009cb558 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc010365480, {0x40d68d0?, 0xc010570240?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc0009cb7b8 sp=0xc0009cb698 pc=0x30ecdf4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc0009cb7e0 sp=0xc0009cb7b8 pc=0x30ec08e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0009cb7e8 sp=0xc0009cb7e0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 749 [select]:
   > runtime.gopark(0xc0009cbf78?, 0x2?, 0xc0?, 0x80?, 0xc0009cbeec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000579d58 sp=0xc000579d38 pc=0x13c9516
   > runtime.selectgo(0xc000579f78, 0xc0009cbee8, 0x3b67af1?, 0x0, 0x139805d?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000579e98 sp=0xc000579d58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc0103654c0, {0x40d68d0?, 0xc010570240?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc000579fb8 sp=0xc000579e98 pc=0x30ecdf4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc000579fe0 sp=0xc000579fb8 pc=0x30ec08e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000579fe8 sp=0xc000579fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 750 [select]:
   > runtime.gopark(0xc0009cdf78?, 0x2?, 0x68?, 0x6?, 0xc0009cdeec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0009cdd58 sp=0xc0009cdd38 pc=0x13c9516
   > runtime.selectgo(0xc0009cdf78, 0xc0009cdee8, 0x3b67af1?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0009cde98 sp=0xc0009cdd58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc010365500, {0x40d68d0?, 0xc010570240?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc0009cdfb8 sp=0xc0009cde98 pc=0x30ecdf4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc0009cdfe0 sp=0xc0009cdfb8 pc=0x30ec08e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0009cdfe8 sp=0xc0009cdfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 121973 [semacquire]:
   > runtime.gopark(0x6043200?, 0xc010e33980?, 0xa0?, 0x4b?, 0xc0185f2ed8?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0185f2e90 sp=0xc0185f2e70 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc013efd458, 0xb8?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc0185f2ef8 sp=0xc0185f2e90 pc=0x13dae5e
   > sync.runtime_Semacquire(0x1?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc0185f2f28 sp=0xc0185f2ef8 pc=0x13f7f65
   > sync.(*WaitGroup).Wait(0x1000000000001?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc0185f2f50 sp=0xc0185f2f28 pc=0x140b312
   > github.com/pingcap/tidb/executor.(*HashAggExec).waitPartialWorkerAndCloseOutputChs(0xc010d42e00, 0x13d0505?)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:815 +0x25 fp=0xc0185f2f98 sp=0xc0185f2f50 pc=0x2fbc465
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:844 +0x45 fp=0xc0185f2fe0 sp=0xc0185f2f98 pc=0x2fbcd85
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0185f2fe8 sp=0xc0185f2fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:843 +0x2e5
   > goroutine 111495 [semacquire]:
   > runtime.gopark(0x2fb8f3f?, 0xc000d77f28?, 0x60?, 0xc6?, 0x60384e0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000d77e90 sp=0xc000d77e70 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc01942d608, 0x0?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc000d77ef8 sp=0xc000d77e90 pc=0x13dae5e
   > sync.runtime_Semacquire(0xc01bea2c00?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc000d77f28 sp=0xc000d77ef8 pc=0x13f7f65
   > sync.(*WaitGroup).Wait(0xc01a307b00?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc000d77f50 sp=0xc000d77f28 pc=0x140b312
   > github.com/pingcap/tidb/executor.(*HashAggExec).waitPartialWorkerAndCloseOutputChs(0xc010d43800, 0x13d0505?)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:815 +0x25 fp=0xc000d77f98 sp=0xc000d77f50 pc=0x2fbc465
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:844 +0x45 fp=0xc000d77fe0 sp=0xc000d77f98 pc=0x2fbcd85
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000d77fe8 sp=0xc000d77fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:843 +0x2e5
   > goroutine 121978 [select]:
   > runtime.gopark(0xc00f95bf00?, 0x2?, 0x3?, 0x0?, 0xc00f95be44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00f95bc48 sp=0xc00f95bc28 pc=0x13c9516
   > runtime.selectgo(0xc00f95bf00, 0xc00f95be40, 0xc00f95bde8?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00f95bd88 sp=0xc00f95bc48 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc0102f0700, {0x4134ba0, 0xc0144ce240})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc00f95bf30 sp=0xc00f95bd88 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc0102f0700, {0x4134ba0, 0xc0144ce240}, 0xc013efd460)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc00f95bfb0 sp=0xc00f95bf30 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc00f95bfe0 sp=0xc00f95bfb0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00f95bfe8 sp=0xc00f95bfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 121971 [select]:
   > runtime.gopark(0xc000d65f28?, 0x2?, 0x0?, 0x0?, 0xc000d65eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000d65d58 sp=0xc000d65d38 pc=0x13c9516
   > runtime.selectgo(0xc000d65f28, 0xc000d65ee8, 0xc018e89a30?, 0x0, 0x3041e97?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000d65e98 sp=0xc000d65d58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc0102f0240, {0x4134ba0, 0xc0144ce240}, 0xc013efd450, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc000d65fa8 sp=0xc000d65e98 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc000d65fe0 sp=0xc000d65fa8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000d65fe8 sp=0xc000d65fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 123520 [semacquire]:
   > runtime.gopark(0x1f8025e84fc?, 0x0?, 0xc0?, 0x3b?, 0xc013cb9ce0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01ddcb558 sp=0xc01ddcb538 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc000df43a4, 0xe0?, 0x3, 0x1)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc01ddcb5c0 sp=0xc01ddcb558 pc=0x13dae5e
   > sync.runtime_SemacquireMutex(0x139a1bf?, 0x60?, 0x50?)
   > 	/usr/local/go/src/runtime/sema.go:77 +0x25 fp=0xc01ddcb5f0 sp=0xc01ddcb5c0 pc=0x13f8085
   > sync.(*Mutex).lockSlow(0xc000df43a0)
   > 	/usr/local/go/src/sync/mutex.go:171 +0x165 fp=0xc01ddcb640 sp=0xc01ddcb5f0 pc=0x1409825
   > sync.(*Mutex).Lock(...)
   > 	/usr/local/go/src/sync/mutex.go:90
   > github.com/pingcap/tidb/util/memory.(*Tracker).FallbackOldAndSetNewAction(0xc000df4390, {0x40dbc60?, 0xc013eb35e0?})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:162 +0x68 fp=0xc01ddcb698 sp=0xc01ddcb640 pc=0x1fb3308
   > github.com/pingcap/tidb/store/copr.(*CopClient).Send(0xc01050c0d0, {0x40d68d0, 0xc010570240}, 0xc01435ce00, {0x3565ba0?, 0xc00045e330?}, 0xc019534f00)
   > 	/go/src/github.com/pingcap/tidb/store/copr/coprocessor.go:137 +0x857 fp=0xc01ddcb860 sp=0xc01ddcb698 pc=0x249aff7
   > github.com/pingcap/tidb/distsql.Select({0x40d68d0, 0xc010570240}, {0x4134ba0?, 0xc0114b7d40}, 0xc01435ce00, {0xc01000af00, 0x9, 0x9}, 0xc01000af50)
   > 	/go/src/github.com/pingcap/tidb/distsql/distsql.go:101 +0x5bf fp=0xc01ddcb9a0 sp=0xc01ddcb860 pc=0x26aa0df
   > github.com/pingcap/tidb/distsql.SelectWithRuntimeStats({0x40d68d0?, 0xc010570240?}, {0x4134ba0?, 0xc0114b7d40?}, 0xc01ddcba60?, {0xc01000af00?, 0x8?, 0x35d4e20?}, 0x1?, {0xc0180804a0, ...}, ...)
   > 	/go/src/github.com/pingcap/tidb/distsql/distsql.go:150 +0x45 fp=0xc01ddcb9f8 sp=0xc01ddcb9a0 pc=0x26aaa65
   > github.com/pingcap/tidb/executor.selectResultHook.SelectResult({0x1?}, {0x40d68d0?, 0xc010570240?}, {0x4134ba0?, 0xc0114b7d40?}, 0x40dbf60?, {0xc01000af00?, 0xc013094600?, 0xc01437a000?}, 0xc01000af50, ...)
   > 	/go/src/github.com/pingcap/tidb/executor/table_reader.go:53 +0xf0 fp=0xc01ddcba70 sp=0xc01ddcb9f8 pc=0x313eb90
   > github.com/pingcap/tidb/executor.(*TableReaderExecutor).buildResp(0xc0104e8780, {0x40d68d0, 0xc010570240}, {0xc01076fbc8?, 0x3?, 0x0?})
   > 	/go/src/github.com/pingcap/tidb/executor/table_reader.go:300 +0x3d6 fp=0xc01ddcbc38 sp=0xc01ddcba70 pc=0x3140456
   > github.com/pingcap/tidb/executor.(*TableReaderExecutor).Open(0xc0104e8780, {0x40d68d0, 0xc010570240})
   > 	/go/src/github.com/pingcap/tidb/executor/table_reader.go:199 +0xa99 fp=0xc01ddcbd50 sp=0xc01ddcbc38 pc=0x313f6d9
   > github.com/pingcap/tidb/executor.(*baseExecutor).Open(...)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:185
   > github.com/pingcap/tidb/executor.(*SelectionExec).Open(0xc00ff456c0?, {0x40d68d0?, 0xc010570240?})
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1338 +0xa2 fp=0xc01ddcbd90 sp=0xc01ddcbd50 pc=0x303fbe2
   > github.com/pingcap/tidb/executor.(*CTEExec).Open(0xc0112a4f00, {0x40d68d0, 0xc010570240})
   > 	/go/src/github.com/pingcap/tidb/executor/cte.go:109 +0xf2 fp=0xc01ddcbe40 sp=0xc01ddcbd90 pc=0x3022212
   > github.com/pingcap/tidb/executor.(*baseExecutor).Open(...)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:185
   > github.com/pingcap/tidb/executor.(*SelectionExec).Open(0xc00ff45790?, {0x40d68d0?, 0xc010570240?})
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1338 +0xa2 fp=0xc01ddcbe80 sp=0xc01ddcbe40 pc=0x303fbe2
   > github.com/pingcap/tidb/executor.(*baseExecutor).Open(...)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:185
   > github.com/pingcap/tidb/executor.(*ProjectionExec).Open(0xc010008240?, {0x40d68d0?, 0xc010570240?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:87 +0xa2 fp=0xc01ddcbec0 sp=0xc01ddcbe80 pc=0x30eb022
   > github.com/pingcap/tidb/executor.(*UnionExec).resultPuller(0xc000733c00, {0x40d68d0, 0xc010570240}, 0x0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1656 +0x237 fp=0xc01ddcbfb0 sp=0xc01ddcbec0 pc=0x3041e97
   > github.com/pingcap/tidb/executor.(*UnionExec).initialize.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1623 +0x32 fp=0xc01ddcbfe0 sp=0xc01ddcbfb0 pc=0x3041c32
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01ddcbfe8 sp=0xc01ddcbfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*UnionExec).initialize
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1623 +0x233
   > goroutine 111497 [select]:
   > runtime.gopark(0xc00086df00?, 0x2?, 0x16?, 0x95?, 0xc00086de44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00086dc48 sp=0xc00086dc28 pc=0x13c9516
   > runtime.selectgo(0xc00086df00, 0xc00086de40, 0x2?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00086dd88 sp=0xc00086dc48 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc01c7bd4c0, {0x4134ba0, 0xc0144ce240})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc00086df30 sp=0xc00086dd88 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc01c7bd4c0, {0x4134ba0, 0xc0144ce240}, 0xc01942d610)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc00086dfb0 sp=0xc00086df30 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc00086dfe0 sp=0xc00086dfb0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00086dfe8 sp=0xc00086dfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 94650 [select]:
   > runtime.gopark(0xc015d3ef28?, 0x2?, 0xb5?, 0x32?, 0xc015d3eeec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc015d3ed58 sp=0xc015d3ed38 pc=0x13c9516
   > runtime.selectgo(0xc015d3ef28, 0xc015d3eee8, 0x35b8652c3?, 0x0, 0xc194c53ddc5e8fd4?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc015d3ee98 sp=0xc015d3ed58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc0144fd180, {0x4134ba0, 0xc0114b7d40}, 0xc018208580, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc015d3efa8 sp=0xc015d3ee98 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc015d3efe0 sp=0xc015d3efa8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc015d3efe8 sp=0xc015d3efe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 94657 [select]:
   > runtime.gopark(0xc000f85f00?, 0x2?, 0x3?, 0x0?, 0xc000f85e44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000f85c48 sp=0xc000f85c28 pc=0x13c9516
   > runtime.selectgo(0xc000f85f00, 0xc000f85e40, 0xc000f85dc0?, 0x0, 0x606b430?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000f85d88 sp=0xc000f85c48 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc0144fd640, {0x4134ba0, 0xc0114b7d40})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc000f85f30 sp=0xc000f85d88 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc0144fd640, {0x4134ba0, 0xc0114b7d40}, 0xc018208590)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc000f85fb0 sp=0xc000f85f30 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc000f85fe0 sp=0xc000f85fb0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000f85fe8 sp=0xc000f85fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 111498 [select]:
   > runtime.gopark(0xc0169aff00?, 0x2?, 0x20?, 0x0?, 0xc0169afe44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0169afc48 sp=0xc0169afc28 pc=0x13c9516
   > runtime.selectgo(0xc0169aff00, 0xc0169afe40, 0x2?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0169afd88 sp=0xc0169afc48 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc01c7bd580, {0x4134ba0, 0xc0144ce240})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc0169aff30 sp=0xc0169afd88 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc01c7bd580, {0x4134ba0, 0xc0144ce240}, 0xc01942d610)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc0169affb0 sp=0xc0169aff30 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc0169affe0 sp=0xc0169affb0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0169affe8 sp=0xc0169affe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 121970 [select]:
   > runtime.gopark(0xc0180c3f28?, 0x2?, 0x0?, 0x0?, 0xc0180c3eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0180c3d58 sp=0xc0180c3d38 pc=0x13c9516
   > runtime.selectgo(0xc0180c3f28, 0xc0180c3ee8, 0x48?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0180c3e98 sp=0xc0180c3d58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc0102f0180, {0x4134ba0, 0xc0144ce240}, 0xc013efd450, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc0180c3fa8 sp=0xc0180c3e98 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc0180c3fe0 sp=0xc0180c3fa8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0180c3fe8 sp=0xc0180c3fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 95075 [semacquire]:
   > runtime.gopark(0x640bedbaa5c0000?, 0x94c53ddbeb240e?, 0xa0?, 0xc2?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00f95aed8 sp=0xc00f95aeb8 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc018208598, 0x80?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc00f95af40 sp=0xc00f95aed8 pc=0x13dae5e
   > sync.runtime_Semacquire(0x140b285?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc00f95af70 sp=0xc00f95af40 pc=0x13f7f65
   > sync.(*WaitGroup).Wait(0xc00f95af20?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc00f95af98 sp=0xc00f95af70 pc=0x140b312
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:856 +0x45 fp=0xc00f95afe0 sp=0xc00f95af98 pc=0x2fbcc85
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00f95afe8 sp=0xc00f95afe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:855 +0x4c5
   > goroutine 121979 [semacquire]:
   > runtime.gopark(0x2fbbe0d?, 0x0?, 0x0?, 0x69?, 0x60384e0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0009dded8 sp=0xc0009ddeb8 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc013efd468, 0xc0?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc0009ddf40 sp=0xc0009dded8 pc=0x13dae5e
   > sync.runtime_Semacquire(0xc00fa1b240?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc0009ddf70 sp=0xc0009ddf40 pc=0x13f7f65
   > sync.(*WaitGroup).Wait(0xc0009ddf68?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc0009ddf98 sp=0xc0009ddf70 pc=0x140b312
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:856 +0x45 fp=0xc0009ddfe0 sp=0xc0009ddf98 pc=0x2fbcc85
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0009ddfe8 sp=0xc0009ddfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:855 +0x4c5
   > goroutine 123579 [semacquire]:
   > runtime.gopark(0x2fbc1e8?, 0x40d68d0?, 0x40?, 0xc5?, 0x40d9ea0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01335ded8 sp=0xc01335deb8 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc0179bdf28, 0xf8?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc01335df40 sp=0xc01335ded8 pc=0x13dae5e
   > sync.runtime_Semacquire(0xc0179bd260?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc01335df70 sp=0xc01335df40 pc=0x13f7f65
   > sync.(*WaitGroup).Wait(0xc01335df60?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc01335df98 sp=0xc01335df70 pc=0x140b312
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:856 +0x45 fp=0xc01335dfe0 sp=0xc01335df98 pc=0x2fbcc85
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01335dfe8 sp=0xc01335dfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:855 +0x4c5
   > goroutine 94652 [select]:
   > runtime.gopark(0xc000a63f28?, 0x2?, 0x73?, 0xed?, 0xc000a63eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000a63d58 sp=0xc000a63d38 pc=0x13c9516
   > runtime.selectgo(0xc000a63f28, 0xc000a63ee8, 0x35b86de72?, 0x0, 0xc194c53ddc5f1d6c?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000a63e98 sp=0xc000a63d58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc0144fd300, {0x4134ba0, 0xc0114b7d40}, 0xc018208580, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc000a63fa8 sp=0xc000a63e98 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc000a63fe0 sp=0xc000a63fa8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000a63fe8 sp=0xc000a63fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 97589 [select]:
   > runtime.gopark(0xc000a6cf78?, 0x2?, 0x40?, 0x2?, 0xc000a6ceec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000a6cd58 sp=0xc000a6cd38 pc=0x13c9516
   > runtime.selectgo(0xc000a6cf78, 0xc000a6cee8, 0x3b67af1?, 0x0, 0xc01a5731d0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000a6ce98 sp=0xc000a6cd58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc012e65780, {0x40d68d0?, 0xc01ac388a0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc000a6cfb8 sp=0xc000a6ce98 pc=0x30ecdf4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc000a6cfe0 sp=0xc000a6cfb8 pc=0x30ec08e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000a6cfe8 sp=0xc000a6cfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 95074 [select]:
   > runtime.gopark(0xc00fb12f00?, 0x2?, 0x3?, 0x0?, 0xc00fb12e44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fb12c48 sp=0xc00fb12c28 pc=0x13c9516
   > runtime.selectgo(0xc00fb12f00, 0xc00fb12e40, 0x4?, 0x0, 0xc0102910b0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fb12d88 sp=0xc00fb12c48 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc0144fd700, {0x4134ba0, 0xc0114b7d40})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc00fb12f30 sp=0xc00fb12d88 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc0144fd700, {0x4134ba0, 0xc0114b7d40}, 0xc018208590)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc00fb12fb0 sp=0xc00fb12f30 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc00fb12fe0 sp=0xc00fb12fb0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fb12fe8 sp=0xc00fb12fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 97590 [select]:
   > runtime.gopark(0xc0009eaf78?, 0x2?, 0x0?, 0x0?, 0xc0009eaeec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0009ead58 sp=0xc0009ead38 pc=0x13c9516
   > runtime.selectgo(0xc0009eaf78, 0xc0009eaee8, 0x3b67af1?, 0x0, 0x3041e97?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0009eae98 sp=0xc0009ead58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc012e657c0, {0x40d68d0?, 0xc01ac388a0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc0009eafb8 sp=0xc0009eae98 pc=0x30ecdf4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc0009eafe0 sp=0xc0009eafb8 pc=0x30ec08e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0009eafe8 sp=0xc0009eafe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 121913 [select]:
   > runtime.gopark(0xc000d5cf78?, 0x2?, 0xc8?, 0x37?, 0xc000d5ceec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000d5cd58 sp=0xc000d5cd38 pc=0x13c9516
   > runtime.selectgo(0xc000d5cf78, 0xc000d5cee8, 0x3b67af1?, 0x0, 0xc194c53e497981d7?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000d5ce98 sp=0xc000d5cd58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc01943a500, {0x40d68d0?, 0xc01ac388a0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc000d5cfb8 sp=0xc000d5ce98 pc=0x30ecdf4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc000d5cfe0 sp=0xc000d5cfb8 pc=0x30ec08e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000d5cfe8 sp=0xc000d5cfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 121915 [select]:
   > runtime.gopark(0xc00fb1ef78?, 0x2?, 0x70?, 0x77?, 0xc00fb1eeec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fb1ed58 sp=0xc00fb1ed38 pc=0x13c9516
   > runtime.selectgo(0xc00fb1ef78, 0xc00fb1eee8, 0x3b67af1?, 0x0, 0xc010f02720?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fb1ee98 sp=0xc00fb1ed58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc01943a580, {0x40d68d0?, 0xc01ac388a0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc00fb1efb8 sp=0xc00fb1ee98 pc=0x30ecdf4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc00fb1efe0 sp=0xc00fb1efb8 pc=0x30ec08e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fb1efe8 sp=0xc00fb1efe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 121903 [chan receive]:
   > runtime.gopark(0xc016af3c88?, 0x13d1800?, 0xf0?, 0x84?, 0xc01017e1a0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc016af3c80 sp=0xc016af3c60 pc=0x13c9516
   > runtime.chanrecv(0xc012ae2ba0, 0xc016af3d68, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc016af3d10 sp=0xc016af3c80 pc=0x13934bb
   > runtime.chanrecv2(0xc015450c00?, 0x40d68d0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc016af3d38 sp=0xc016af3d10 pc=0x1392ff8
   > github.com/pingcap/tidb/executor.(*UnionExec).Next(0xc015450c00, {0x40d68d0, 0xc01ac388a0}, 0xc012e44370)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1702 +0x85 fp=0xc016af3da0 sp=0xc016af3d38 pc=0x30425c5
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc01ac388a0}, {0x40d9ea0, 0xc015450c00}, 0xc012e44370)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc016af3ee0 sp=0xc016af3da0 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*HashAggExec).fetchChildData(0xc010d42e00, {0x40d68d0, 0xc01ac388a0}, 0xc014d569f0?)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:798 +0x1be fp=0xc016af3fb0 sp=0xc016af3ee0 pc=0x2fbc0fe
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func3()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:835 +0x32 fp=0xc016af3fe0 sp=0xc016af3fb0 pc=0x2fbce72
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc016af3fe8 sp=0xc016af3fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:835 +0xea
   > goroutine 121983 [semacquire]:
   > runtime.gopark(0xc010483320?, 0x3001d3d08?, 0xc0?, 0x9e?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000a62ef0 sp=0xc000a62ed0 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc015450cd0, 0x70?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc000a62f58 sp=0xc000a62ef0 pc=0x13dae5e
   > sync.runtime_Semacquire(0xc000a62fd0?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc000a62f88 sp=0xc000a62f58 pc=0x13f7f65
   > sync.(*WaitGroup).Wait(0x3ba51f270?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc000a62fb0 sp=0xc000a62f88 pc=0x140b312
   > github.com/pingcap/tidb/executor.(*UnionExec).waitAllFinished(0xc015450c00)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1595 +0x2a fp=0xc000a62fc8 sp=0xc000a62fb0 pc=0x30415ea
   > github.com/pingcap/tidb/executor.(*UnionExec).initialize.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1629 +0x26 fp=0xc000a62fe0 sp=0xc000a62fc8 pc=0x3041bc6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000a62fe8 sp=0xc000a62fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*UnionExec).initialize
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1629 +0x40b
   > goroutine 97537 [chan receive]:
   > runtime.gopark(0xc01c7f3410?, 0xc01017eea0?, 0x6d?, 0xcb?, 0xc01c91f2d0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01e28f228 sp=0xc01e28f208 pc=0x13c9516
   > runtime.chanrecv(0xc01b7ff140, 0xc01c91f300, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc01e28f2b8 sp=0xc01e28f228 pc=0x13934bb
   > runtime.chanrecv2(0xc010d43800?, 0x40d68d0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc01e28f2e0 sp=0xc01e28f2b8 pc=0x1392ff8
   > github.com/pingcap/tidb/executor.(*HashAggExec).parallelExec(0xc010d43800, {0x40d68d0?, 0xc01ac388a0?}, 0xc019c9db80)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:888 +0x89 fp=0xc01e28f318 sp=0xc01e28f2e0 pc=0x2fbcf29
   > github.com/pingcap/tidb/executor.(*HashAggExec).Next(0x40d68d0?, {0x40d68d0?, 0xc01ac388a0?}, 0x7f4c07bb0701?)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:768 +0x76 fp=0xc01e28f348 sp=0xc01e28f318 pc=0x2fbbeb6
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc01ac388a0}, {0x40d9120, 0xc010d43800}, 0xc019c9db80)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc01e28f488 sp=0xc01e28f348 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*SortExec).fetchRowChunks(0xc015909c20, {0x40d68d0, 0xc01ac388a0})
   > 	/go/src/github.com/pingcap/tidb/executor/sort.go:195 +0x596 fp=0xc01e28f5e8 sp=0xc01e28f488 pc=0x3135156
   > github.com/pingcap/tidb/executor.(*SortExec).Next(0xc015909c20, {0x40d68d0, 0xc01ac388a0}, 0xc019c9dae0)
   > 	/go/src/github.com/pingcap/tidb/executor/sort.go:113 +0x325 fp=0xc01e28f660 sp=0xc01e28f5e8 pc=0x31346c5
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc01ac388a0}, {0x40d9c20, 0xc015909c20}, 0xc019c9dae0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc01e28f7a0 sp=0xc01e28f660 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*MaxOneRowExec).Next(0xc0167f25b0, {0x40d68d0, 0xc01ac388a0}, 0xc019c9dae0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1518 +0xa8 fp=0xc01e28f7f0 sp=0xc01e28f7a0 pc=0x30413a8
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc01ac388a0}, {0x40d94a0, 0xc0167f25b0}, 0xc019c9dae0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc01e28f930 sp=0xc01e28f7f0 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*SelectionExec).Next(0xc01589f520, {0x40d68d0, 0xc01ac388a0}, 0xc01a9b62d0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1394 +0xed fp=0xc01e28f9c0 sp=0xc01e28f930 pc=0x304012d
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc01ac388a0}, {0x40d9960, 0xc01589f520}, 0xc01a9b62d0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc01e28fb00 sp=0xc01e28f9c0 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*NestedLoopApplyExec).fetchAllInners(0xc01131ba40, {0x40d68d0, 0xc01ac388a0})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:979 +0x346 fp=0xc01e28fbf8 sp=0xc01e28fb00 pc=0x30b2966
   > github.com/pingcap/tidb/executor.(*NestedLoopApplyExec).Next(0xc01131ba40, {0x40d68d0, 0xc01ac388a0}, 0xc01a9b7360)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:1032 +0x5b6 fp=0xc01e28fd58 sp=0xc01e28fbf8 pc=0x30b32b6
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc01ac388a0}, {0x40d9560, 0xc01131ba40}, 0xc01a9b7360)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc01e28fe98 sp=0xc01e28fd58 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*projectionInputFetcher).run(0xc015909ee0, {0x40d68d0, 0xc01ac388a0})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:381 +0x2f0 fp=0xc01e28ffb8 sp=0xc01e28fe98 pc=0x30ec890
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:272 +0x2e fp=0xc01e28ffe0 sp=0xc01e28ffb8 pc=0x30ec0ee
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01e28ffe8 sp=0xc01e28ffe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:272 +0x67e
   > goroutine 94649 [select]:
   > runtime.gopark(0xc0003e5f28?, 0x2?, 0x9a?, 0x92?, 0xc0003e5eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0003e5d58 sp=0xc0003e5d38 pc=0x13c9516
   > runtime.selectgo(0xc0003e5f28, 0xc0003e5ee8, 0x35b8681b0?, 0x0, 0xc194c53ddc5ec24d?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0003e5e98 sp=0xc0003e5d58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc0144fd0c0, {0x4134ba0, 0xc0114b7d40}, 0xc018208580, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc0003e5fa8 sp=0xc0003e5e98 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc0003e5fe0 sp=0xc0003e5fa8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0003e5fe8 sp=0xc0003e5fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 123448 [semacquire]:
   > runtime.gopark(0x2?, 0x0?, 0x0?, 0xc?, 0x249cacc?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000d95ef0 sp=0xc000d95ed0 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc000733ed0, 0x50?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc000d95f58 sp=0xc000d95ef0 pc=0x13dae5e
   > sync.runtime_Semacquire(0xc01b0c9200?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc000d95f88 sp=0xc000d95f58 pc=0x13f7f65
   > sync.(*WaitGroup).Wait(0x30ec08e?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc000d95fb0 sp=0xc000d95f88 pc=0x140b312
   > github.com/pingcap/tidb/executor.(*UnionExec).waitAllFinished(0xc000733e00)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1595 +0x2a fp=0xc000d95fc8 sp=0xc000d95fb0 pc=0x30415ea
   > github.com/pingcap/tidb/executor.(*UnionExec).initialize.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1629 +0x26 fp=0xc000d95fe0 sp=0xc000d95fc8 pc=0x3041bc6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000d95fe8 sp=0xc000d95fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*UnionExec).initialize
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1629 +0x40b
   > goroutine 97588 [select]:
   > runtime.gopark(0xc000648f78?, 0x2?, 0xb0?, 0x35?, 0xc000648eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000648d58 sp=0xc000648d38 pc=0x13c9516
   > runtime.selectgo(0xc000648f78, 0xc000648ee8, 0x3b67af1?, 0x0, 0xc194c53df52e6563?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000648e98 sp=0xc000648d58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc012e65740, {0x40d68d0?, 0xc01ac388a0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc000648fb8 sp=0xc000648e98 pc=0x30ecdf4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc000648fe0 sp=0xc000648fb8 pc=0x30ec08e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000648fe8 sp=0xc000648fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 121484 [chan receive]:
   > runtime.gopark(0xc014de6450?, 0xc010324820?, 0x6d?, 0xcb?, 0xc00feb3448?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00feb33a0 sp=0xc00feb3380 pc=0x13c9516
   > runtime.chanrecv(0xc012ae2480, 0xc00feb3478, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc00feb3430 sp=0xc00feb33a0 pc=0x13934bb
   > runtime.chanrecv2(0xc010d42e00?, 0x40d68d0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc00feb3458 sp=0xc00feb3430 pc=0x1392ff8
   > github.com/pingcap/tidb/executor.(*HashAggExec).parallelExec(0xc010d42e00, {0x40d68d0?, 0xc01ac388a0?}, 0xc012e44c30)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:888 +0x89 fp=0xc00feb3490 sp=0xc00feb3458 pc=0x2fbcf29
   > github.com/pingcap/tidb/executor.(*HashAggExec).Next(0x40d68d0?, {0x40d68d0?, 0xc01ac388a0?}, 0xc00feb3540?)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:768 +0x76 fp=0xc00feb34c0 sp=0xc00feb3490 pc=0x2fbbeb6
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc01ac388a0}, {0x40d9120, 0xc010d42e00}, 0xc012e44c30)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc00feb3600 sp=0xc00feb34c0 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*MaxOneRowExec).Next(0xc0169d7a40, {0x40d68d0, 0xc01ac388a0}, 0xc012e44c30)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1518 +0xa8 fp=0xc00feb3650 sp=0xc00feb3600 pc=0x30413a8
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc01ac388a0}, {0x40d94a0, 0xc0169d7a40}, 0xc012e44c30)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc00feb3790 sp=0xc00feb3650 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*SelectionExec).Next(0xc01589f040, {0x40d68d0, 0xc01ac388a0}, 0xc012a1cff0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1394 +0xed fp=0xc00feb3820 sp=0xc00feb3790 pc=0x304012d
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc01ac388a0}, {0x40d9960, 0xc01589f040}, 0xc012a1cff0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc00feb3960 sp=0xc00feb3820 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*NestedLoopApplyExec).fetchAllInners(0xc01131b500, {0x40d68d0, 0xc01ac388a0})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:979 +0x346 fp=0xc00feb3a58 sp=0xc00feb3960 pc=0x30b2966
   > github.com/pingcap/tidb/executor.(*NestedLoopApplyExec).Next(0xc01131b500, {0x40d68d0, 0xc01ac388a0}, 0xc012a1d0e0)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:1032 +0x5b6 fp=0xc00feb3bb8 sp=0xc00feb3a58 pc=0x30b32b6
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc01ac388a0}, {0x40d9560, 0xc01131b500}, 0xc012a1d0e0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc00feb3cf8 sp=0xc00feb3bb8 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*ProjectionExec).unParallelExecute(0xc0159097a0, {0x40d68d0?, 0xc01ac388a0?}, 0xc012a1ce10)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:194 +0xb8 fp=0xc00feb3d48 sp=0xc00feb3cf8 pc=0x30eb458
   > github.com/pingcap/tidb/executor.(*ProjectionExec).Next(0xc0159097a0, {0x40d68d0, 0xc01ac388a0}, 0xc00feb3f0c?)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:180 +0x5a fp=0xc00feb3d80 sp=0xc00feb3d48 pc=0x30eb31a
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc01ac388a0}, {0x40d9720, 0xc0159097a0}, 0xc012a1ce10)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc00feb3ec0 sp=0xc00feb3d80 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*UnionExec).resultPuller(0xc015450e00, {0x40d68d0, 0xc01ac388a0}, 0x0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1673 +0x48f fp=0xc00feb3fb0 sp=0xc00feb3ec0 pc=0x30420ef
   > github.com/pingcap/tidb/executor.(*UnionExec).initialize.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1623 +0x32 fp=0xc00feb3fe0 sp=0xc00feb3fb0 pc=0x3041c32
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00feb3fe8 sp=0xc00feb3fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*UnionExec).initialize
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1623 +0x233
   > goroutine 111492 [select]:
   > runtime.gopark(0xc00089bf28?, 0x2?, 0x2?, 0x0?, 0xc00089beec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00089bd58 sp=0xc00089bd38 pc=0x13c9516
   > runtime.selectgo(0xc00089bf28, 0xc00089bee8, 0x13?, 0x0, 0xc01c492288?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00089be98 sp=0xc00089bd58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc01c7bd180, {0x4134ba0, 0xc0144ce240}, 0xc01942d600, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc00089bfa8 sp=0xc00089be98 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc00089bfe0 sp=0xc00089bfa8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00089bfe8 sp=0xc00089bfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 123578 [select]:
   > runtime.gopark(0xc013358f00?, 0x2?, 0x0?, 0x0?, 0xc013358e44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc013358c48 sp=0xc013358c28 pc=0x13c9516
   > runtime.selectgo(0xc013358f00, 0xc013358e40, 0xc013358de8?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc013358d88 sp=0xc013358c48 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc01071af00, {0x4134ba0, 0xc0114b7d40})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc013358f30 sp=0xc013358d88 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc01071af00, {0x4134ba0, 0xc0114b7d40}, 0xc0179bdf20)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc013358fb0 sp=0xc013358f30 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc013358fe0 sp=0xc013358fb0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc013358fe8 sp=0xc013358fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 121980 [semacquire]:
   > runtime.gopark(0xc194c53e44391ca7?, 0x3ba967395?, 0x20?, 0x61?, 0xc0160c0f20?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0160c0eb8 sp=0xc0160c0e98 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc013efd448, 0xf4?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc0160c0f20 sp=0xc0160c0eb8 pc=0x13dae5e
   > sync.runtime_Semacquire(0xc00fbe0900?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc0160c0f50 sp=0xc0160c0f20 pc=0x13f7f65
   > sync.(*WaitGroup).Wait(0xc194c53e44391ca7?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc0160c0f78 sp=0xc0160c0f50 pc=0x140b312
   > github.com/pingcap/tidb/executor.(*HashAggExec).waitAllWorkersAndCloseFinalOutputCh(0xc010d42e00, {0xc0160c0fb8, 0x3, 0xc00fa1b300?})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:827 +0x35 fp=0xc0160c0f98 sp=0xc0160c0f78 pc=0x2fbc5b5
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func6()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:864 +0x5a fp=0xc0160c0fe0 sp=0xc0160c0f98 pc=0x2fbcc1a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0160c0fe8 sp=0xc0160c0fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:864 +0x54d
   > goroutine 123586 [semacquire]:
   > runtime.gopark(0xc000df4060?, 0x0?, 0xe0?, 0x4d?, 0x60384e0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000f89ef0 sp=0xc000f89ed0 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc000733cd0, 0x60?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc000f89f58 sp=0xc000f89ef0 pc=0x13dae5e
   > sync.runtime_Semacquire(0xc0179bd270?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc000f89f88 sp=0xc000f89f58 pc=0x13f7f65
   > sync.(*WaitGroup).Wait(0x4134ba0?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc000f89fb0 sp=0xc000f89f88 pc=0x140b312
   > github.com/pingcap/tidb/executor.(*UnionExec).waitAllFinished(0xc000733c00)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1595 +0x2a fp=0xc000f89fc8 sp=0xc000f89fb0 pc=0x30415ea
   > github.com/pingcap/tidb/executor.(*UnionExec).initialize.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1629 +0x26 fp=0xc000f89fe0 sp=0xc000f89fc8 pc=0x3041bc6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000f89fe8 sp=0xc000f89fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*UnionExec).initialize
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1629 +0x40b
   > goroutine 94656 [select]:
   > runtime.gopark(0xc00fd63f00?, 0x2?, 0x0?, 0x6f?, 0xc00fd63e44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fd63c48 sp=0xc00fd63c28 pc=0x13c9516
   > runtime.selectgo(0xc00fd63f00, 0xc00fd63e40, 0xc00fd63de8?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fd63d88 sp=0xc00fd63c48 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc0144fd580, {0x4134ba0, 0xc0114b7d40})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc00fd63f30 sp=0xc00fd63d88 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc0144fd580, {0x4134ba0, 0xc0114b7d40}, 0xc018208590)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc00fd63fb0 sp=0xc00fd63f30 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc00fd63fe0 sp=0xc00fd63fb0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fd63fe8 sp=0xc00fd63fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 94648 [select]:
   > runtime.gopark(0xc00064af28?, 0x2?, 0x81?, 0xa?, 0xc00064aeec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00064ad58 sp=0xc00064ad38 pc=0x13c9516
   > runtime.selectgo(0xc00064af28, 0xc00064aee8, 0x36085fa69?, 0x0, 0xc194c53de15e3b4c?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00064ae98 sp=0xc00064ad58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc0144fd000, {0x4134ba0, 0xc0114b7d40}, 0xc018208580, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc00064afa8 sp=0xc00064ae98 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc00064afe0 sp=0xc00064afa8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00064afe8 sp=0xc00064afe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 123569 [select]:
   > runtime.gopark(0xc01753df28?, 0x2?, 0xe5?, 0x1e?, 0xc01753deec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01753dd58 sp=0xc01753dd38 pc=0x13c9516
   > runtime.selectgo(0xc01753df28, 0xc01753dee8, 0x3b67af1?, 0x0, 0xc01753df08?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01753de98 sp=0xc01753dd58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc01071a8c0, {0x4134ba0, 0xc0114b7d40}, 0xc0179bdf10, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc01753dfa8 sp=0xc01753de98 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc01753dfe0 sp=0xc01753dfa8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01753dfe8 sp=0xc01753dfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 121905 [select]:
   > runtime.gopark(0xc0185f3f28?, 0x2?, 0xaf?, 0x5f?, 0xc0185f3eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0185f3d58 sp=0xc0185f3d38 pc=0x13c9516
   > runtime.selectgo(0xc0185f3f28, 0xc0185f3ee8, 0x3b67af1?, 0x0, 0xc194c53e46c5fbee?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0185f3e98 sp=0xc0185f3d58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc0102f00c0, {0x4134ba0, 0xc0144ce240}, 0xc013efd450, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc0185f3fa8 sp=0xc0185f3e98 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc0185f3fe0 sp=0xc0185f3fa8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0185f3fe8 sp=0xc0185f3fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 123571 [select]:
   > runtime.gopark(0xc0009eff28?, 0x2?, 0x0?, 0x0?, 0xc0009efeec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0009efd58 sp=0xc0009efd38 pc=0x13c9516
   > runtime.selectgo(0xc0009eff28, 0xc0009efee8, 0x3b67af1?, 0x0, 0x3041e97?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0009efe98 sp=0xc0009efd58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc01071aa40, {0x4134ba0, 0xc0114b7d40}, 0xc0179bdf10, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc0009effa8 sp=0xc0009efe98 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc0009effe0 sp=0xc0009effa8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0009effe8 sp=0xc0009effe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 111500 [select]:
   > runtime.gopark(0xc0175c0f00?, 0x2?, 0x3?, 0x0?, 0xc0175c0e44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0175c0c48 sp=0xc0175c0c28 pc=0x13c9516
   > runtime.selectgo(0xc0175c0f00, 0xc0175c0e40, 0x2?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0175c0d88 sp=0xc0175c0c48 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc01c7bd700, {0x4134ba0, 0xc0144ce240})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc0175c0f30 sp=0xc0175c0d88 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc01c7bd700, {0x4134ba0, 0xc0144ce240}, 0xc01942d610)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc0175c0fb0 sp=0xc0175c0f30 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc0175c0fe0 sp=0xc0175c0fb0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0175c0fe8 sp=0xc0175c0fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 121917 [select]:
   > runtime.gopark(0xc0175c1f78?, 0x2?, 0x8?, 0x28?, 0xc0175c1eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0175c1d58 sp=0xc0175c1d38 pc=0x13c9516
   > runtime.selectgo(0xc0175c1f78, 0xc0175c1ee8, 0x3b67af1?, 0x0, 0xc0003433f8?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0175c1e98 sp=0xc0175c1d58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc01943a600, {0x40d68d0?, 0xc01ac388a0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc0175c1fb8 sp=0xc0175c1e98 pc=0x30ecdf4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc0175c1fe0 sp=0xc0175c1fb8 pc=0x30ec08e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0175c1fe8 sp=0xc0175c1fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 123574 [select]:
   > runtime.gopark(0xc00fb15f00?, 0x2?, 0x3?, 0x0?, 0xc00fb15e44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fb15c48 sp=0xc00fb15c28 pc=0x13c9516
   > runtime.selectgo(0xc00fb15f00, 0xc00fb15e40, 0xc0141194f0?, 0x0, 0x606b430?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fb15d88 sp=0xc00fb15c48 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc01071ac00, {0x4134ba0, 0xc0114b7d40})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc00fb15f30 sp=0xc00fb15d88 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc01071ac00, {0x4134ba0, 0xc0114b7d40}, 0xc0179bdf20)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc00fb15fb0 sp=0xc00fb15f30 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc00fb15fe0 sp=0xc00fb15fb0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fb15fe8 sp=0xc00fb15fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 94654 [select]:
   > runtime.gopark(0xc010b0bf00?, 0x2?, 0x3?, 0x0?, 0xc010b0be44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010b0bc48 sp=0xc010b0bc28 pc=0x13c9516
   > runtime.selectgo(0xc010b0bf00, 0xc010b0be40, 0x1400?, 0x0, 0x6041540?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010b0bd88 sp=0xc010b0bc48 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc0144fd400, {0x4134ba0, 0xc0114b7d40})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc010b0bf30 sp=0xc010b0bd88 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc0144fd400, {0x4134ba0, 0xc0114b7d40}, 0xc018208590)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc010b0bfb0 sp=0xc010b0bf30 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc010b0bfe0 sp=0xc010b0bfb0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010b0bfe8 sp=0xc010b0bfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 121977 [select]:
   > runtime.gopark(0xc0167c2f00?, 0x2?, 0x16?, 0x95?, 0xc0167c2e44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0167c2c48 sp=0xc0167c2c28 pc=0x13c9516
   > runtime.selectgo(0xc0167c2f00, 0xc0167c2e40, 0x13c9600?, 0x0, 0x5?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0167c2d88 sp=0xc0167c2c48 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc0102f0640, {0x4134ba0, 0xc0144ce240})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc0167c2f30 sp=0xc0167c2d88 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc0102f0640, {0x4134ba0, 0xc0144ce240}, 0xc013efd460)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc0167c2fb0 sp=0xc0167c2f30 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc0167c2fe0 sp=0xc0167c2fb0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0167c2fe8 sp=0xc0167c2fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 123577 [select]:
   > runtime.gopark(0xc017b71f00?, 0x2?, 0x16?, 0x95?, 0xc017b71e44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc017b71c48 sp=0xc017b71c28 pc=0x13c9516
   > runtime.selectgo(0xc017b71f00, 0xc017b71e40, 0xc017b71de8?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc017b71d88 sp=0xc017b71c48 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc01071ae40, {0x4134ba0, 0xc0114b7d40})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc017b71f30 sp=0xc017b71d88 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc01071ae40, {0x4134ba0, 0xc0114b7d40}, 0xc0179bdf20)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc017b71fb0 sp=0xc017b71f30 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc017b71fe0 sp=0xc017b71fb0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc017b71fe8 sp=0xc017b71fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 111457 [chan receive]:
   > runtime.gopark(0xc01c2eb760?, 0x13d1800?, 0xb0?, 0xa1?, 0xc0105b1860?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01c2eb758 sp=0xc01c2eb738 pc=0x13c9516
   > runtime.chanrecv(0xc0127ae960, 0xc01c2eb840, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc01c2eb7e8 sp=0xc01c2eb758 pc=0x13934bb
   > runtime.chanrecv2(0xc015450e00?, 0x40d68d0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc01c2eb810 sp=0xc01c2eb7e8 pc=0x1392ff8
   > github.com/pingcap/tidb/executor.(*UnionExec).Next(0xc015450e00, {0x40d68d0, 0xc01ac388a0}, 0xc019c9d180)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1702 +0x85 fp=0xc01c2eb878 sp=0xc01c2eb810 pc=0x30425c5
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc01ac388a0}, {0x40d9ea0, 0xc015450e00}, 0xc019c9d180)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc01c2eb9b8 sp=0xc01c2eb878 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*MaxOneRowExec).Next(0xc0167f2310, {0x40d68d0, 0xc01ac388a0}, 0xc019c9d180)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1518 +0xa8 fp=0xc01c2eba08 sp=0xc01c2eb9b8 pc=0x30413a8
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc01ac388a0}, {0x40d94a0, 0xc0167f2310}, 0xc019c9d180)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc01c2ebb48 sp=0xc01c2eba08 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*NestedLoopApplyExec).fetchAllInners(0xc01131b880, {0x40d68d0, 0xc01ac388a0})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:979 +0x346 fp=0xc01c2ebc40 sp=0xc01c2ebb48 pc=0x30b2966
   > github.com/pingcap/tidb/executor.(*NestedLoopApplyExec).Next(0xc01131b880, {0x40d68d0, 0xc01ac388a0}, 0xc019c9d270)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:1032 +0x5b6 fp=0xc01c2ebda0 sp=0xc01c2ebc40 pc=0x30b32b6
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc01ac388a0}, {0x40d9560, 0xc01131b880}, 0xc019c9d270)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc01c2ebee0 sp=0xc01c2ebda0 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*HashAggExec).fetchChildData(0xc010d43800, {0x40d68d0, 0xc01ac388a0}, 0xc01ac388a0?)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:798 +0x1be fp=0xc01c2ebfb0 sp=0xc01c2ebee0 pc=0x2fbc0fe
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func3()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:835 +0x32 fp=0xc01c2ebfe0 sp=0xc01c2ebfb0 pc=0x2fbce72
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01c2ebfe8 sp=0xc01c2ebfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:835 +0xea
   > goroutine 123567 [chan receive]:
   > runtime.gopark(0xc000632c88?, 0x13d1800?, 0xc0?, 0x49?, 0xc0108f5040?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000632c80 sp=0xc000632c60 pc=0x13c9516
   > runtime.chanrecv(0xc013cb9b60, 0xc000632d68, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000632d10 sp=0xc000632c80 pc=0x13934bb
   > runtime.chanrecv2(0xc000733c00?, 0x40d68d0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc000632d38 sp=0xc000632d10 pc=0x1392ff8
   > github.com/pingcap/tidb/executor.(*UnionExec).Next(0xc000733c00, {0x40d68d0, 0xc010570240}, 0xc013cc0370)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1702 +0x85 fp=0xc000632da0 sp=0xc000632d38 pc=0x30425c5
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc010570240}, {0x40d9ea0, 0xc000733c00}, 0xc013cc0370)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc000632ee0 sp=0xc000632da0 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*HashAggExec).fetchChildData(0xc010d43000, {0x40d68d0, 0xc010570240}, 0xc010570240?)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:798 +0x1be fp=0xc000632fb0 sp=0xc000632ee0 pc=0x2fbc0fe
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func3()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:835 +0x32 fp=0xc000632fe0 sp=0xc000632fb0 pc=0x2fbce72
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000632fe8 sp=0xc000632fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:835 +0xea
   > goroutine 121974 [select]:
   > runtime.gopark(0xc01753af00?, 0x2?, 0x0?, 0x0?, 0xc01753ae44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01753ac48 sp=0xc01753ac28 pc=0x13c9516
   > runtime.selectgo(0xc01753af00, 0xc01753ae40, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01753ad88 sp=0xc01753ac48 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc0102f0400, {0x4134ba0, 0xc0144ce240})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc01753af30 sp=0xc01753ad88 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc0102f0400, {0x4134ba0, 0xc0144ce240}, 0xc013efd460)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc01753afb0 sp=0xc01753af30 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc01753afe0 sp=0xc01753afb0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01753afe8 sp=0xc01753afe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 111501 [semacquire]:
   > runtime.gopark(0xfbbe0d?, 0x0?, 0x80?, 0xbc?, 0x33?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0009d2ed8 sp=0xc0009d2eb8 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc01942d618, 0x0?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc0009d2f40 sp=0xc0009d2ed8 pc=0x13dae5e
   > sync.runtime_Semacquire(0x2fbc5dd?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc0009d2f70 sp=0xc0009d2f40 pc=0x13f7f65
   > sync.(*WaitGroup).Wait(0xc010d42e00?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc0009d2f98 sp=0xc0009d2f70 pc=0x140b312
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:856 +0x45 fp=0xc0009d2fe0 sp=0xc0009d2f98 pc=0x2fbcc85
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0009d2fe8 sp=0xc0009d2fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:855 +0x4c5
   > goroutine 94926 [chan receive]:
   > runtime.gopark(0xc013ad10e0?, 0xc01a9b7630?, 0xe0?, 0x75?, 0xc012a4f080?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc012652af8 sp=0xc012652ad8 pc=0x13c9516
   > runtime.chanrecv(0xc012a4e900, 0xc01639cbd8, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc012652b88 sp=0xc012652af8 pc=0x13934bb
   > runtime.chanrecv1(0xc015909e60?, 0x40d68d0?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc012652bb0 sp=0xc012652b88 pc=0x1392fb8
   > github.com/pingcap/tidb/executor.(*ProjectionExec).parallelExecute(0xc015909e60, {0x40d68d0?, 0xc01ac388a0?}, 0xc01a9b7310)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:218 +0x92 fp=0xc012652bf8 sp=0xc012652bb0 pc=0x30eb612
   > github.com/pingcap/tidb/executor.(*ProjectionExec).Next(0xc015909e60, {0x40d68d0, 0xc01ac388a0}, 0x0?)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:182 +0x78 fp=0xc012652c30 sp=0xc012652bf8 pc=0x30eb338
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc01ac388a0}, {0x40d9720, 0xc015909e60}, 0xc01a9b7310)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc012652d70 sp=0xc012652c30 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*recordSet).Next(0xc01a9b71d0, {0x40d68d0?, 0xc01ac388a0?}, 0xc01a9b7310)
   > 	/go/src/github.com/pingcap/tidb/executor/adapter.go:149 +0xbf fp=0xc012652e00 sp=0xc012652d70 pc=0x2fa45ff
   > github.com/pingcap/tidb/session.(*execStmtResult).Next(0xc01ac38870?, {0x40d68d0?, 0xc01ac388a0?}, 0xc01be9df40?)
   > 	<autogenerated>:1 +0x34 fp=0xc012652e30 sp=0xc012652e00 pc=0x31b8c94
   > github.com/pingcap/tidb/server.(*tidbResultSet).Next(0x60384e0?, {0x40d68d0?, 0xc01ac388a0?}, 0x40ee040?)
   > 	/go/src/github.com/pingcap/tidb/server/driver_tidb.go:317 +0x2b fp=0xc012652e60 sp=0xc012652e30 pc=0x323ac6b
   > github.com/pingcap/tidb/server.(*clientConn).writeChunks(0xc013f05b80, {0x40d68d0, 0xc01ac388a0}, {0x40dff58, 0xc01a9b72c0}, 0x0, 0x1639?)
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:2185 +0x15e fp=0xc012652f20 sp=0xc012652e60 pc=0x3231d7e
   > github.com/pingcap/tidb/server.(*clientConn).writeResultset(0xc013f05b80, {0x40d68d0, 0xc01ac388a0}, {0x40dff58, 0xc01a9b72c0}, 0xc0?, 0x3, 0xc014731088?)
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:2136 +0x23e fp=0xc012652fd0 sp=0xc012652f20 pc=0x323157e
   > github.com/pingcap/tidb/server.(*clientConn).handleStmt(0xc013f05b80, {0x40d6828, 0xc011ff28c0}, {0x40e9b80, 0xc0156787e0}, {0x606b430, 0x0, 0x0}, 0x1)
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:2014 +0x3c8 fp=0xc012653098 sp=0xc012652fd0 pc=0x32302c8
   > github.com/pingcap/tidb/server.(*clientConn).handleQuery(0xc013f05b80, {0x40d6828, 0xc011ff28c0}, {0xc0156d8481, 0x44c})
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:1850 +0x774 fp=0xc012653260 sp=0xc012653098 pc=0x322ea14
   > github.com/pingcap/tidb/server.(*clientConn).dispatch(0xc013f05b80, {0x40d68d0?, 0xc018b9ad50?}, {0xc0156d8480, 0x44d, 0x44d})
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:1345 +0x1025 fp=0xc012653650 sp=0xc012653260 pc=0x322a305
   > github.com/pingcap/tidb/server.(*clientConn).Run(0xc013f05b80, {0x40d68d0, 0xc018b9ad50})
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:1095 +0x253 fp=0xc012653c58 sp=0xc012653650 pc=0x3226c53
   > github.com/pingcap/tidb/server.(*Server).onConn(0xc0104e2410, 0xc013f05b80)
   > 	/go/src/github.com/pingcap/tidb/server/server.go:551 +0x6c5 fp=0xc012653fc0 sp=0xc012653c58 pc=0x3259da5
   > github.com/pingcap/tidb/server.(*Server).startNetworkListener.func2()
   > 	/go/src/github.com/pingcap/tidb/server/server.go:448 +0x2a fp=0xc012653fe0 sp=0xc012653fc0 pc=0x3258c2a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc012653fe8 sp=0xc012653fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/server.(*Server).startNetworkListener
   > 	/go/src/github.com/pingcap/tidb/server/server.go:448 +0x5ca
   > goroutine 111494 [select]:
   > runtime.gopark(0xc0160bff28?, 0x2?, 0xfe?, 0x20?, 0xc0160bfeec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0160bfd58 sp=0xc0160bfd38 pc=0x13c9516
   > runtime.selectgo(0xc0160bff28, 0xc0160bfee8, 0x3999b1771?, 0x0, 0xc194c53e1ed88c6b?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0160bfe98 sp=0xc0160bfd58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc01c7bd300, {0x4134ba0, 0xc0144ce240}, 0xc01942d600, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc0160bffa8 sp=0xc0160bfe98 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc0160bffe0 sp=0xc0160bffa8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0160bffe8 sp=0xc0160bffe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 121972 [select]:
   > runtime.gopark(0xc01335af28?, 0x2?, 0x80?, 0x96?, 0xc01335aeec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01335ad58 sp=0xc01335ad38 pc=0x13c9516
   > runtime.selectgo(0xc01335af28, 0xc01335aee8, 0xc01335ae01?, 0x0, 0x3041f62?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01335ae98 sp=0xc01335ad58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc0102f0300, {0x4134ba0, 0xc0144ce240}, 0xc013efd450, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc01335afa8 sp=0xc01335ae98 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc01335afe0 sp=0xc01335afa8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01335afe8 sp=0xc01335afe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 94653 [semacquire]:
   > runtime.gopark(0x1393185?, 0x35596e0?, 0xc0?, 0xa3?, 0x1fb5126?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fb1be90 sp=0xc00fb1be70 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc018208588, 0x40?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc00fb1bef8 sp=0xc00fb1be90 pc=0x13dae5e
   > sync.runtime_Semacquire(0x38032f46afb?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc00fb1bf28 sp=0xc00fb1bef8 pc=0x13f7f65
   > sync.(*WaitGroup).Wait(0x0?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc00fb1bf50 sp=0xc00fb1bf28 pc=0x140b312
   > github.com/pingcap/tidb/executor.(*HashAggExec).waitPartialWorkerAndCloseOutputChs(0xc010d43400, 0x13d0505?)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:815 +0x25 fp=0xc00fb1bf98 sp=0xc00fb1bf50 pc=0x2fbc465
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:844 +0x45 fp=0xc00fb1bfe0 sp=0xc00fb1bf98 pc=0x2fbcd85
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fb1bfe8 sp=0xc00fb1bfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:843 +0x2e5
   > goroutine 111502 [semacquire]:
   > runtime.gopark(0xc194c53e25a1f500?, 0x3a0647e01?, 0xc0?, 0xcc?, 0xc01c2e6f20?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01c2e6eb8 sp=0xc01c2e6e98 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc01942d5f8, 0xa0?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc01c2e6f20 sp=0xc01c2e6eb8 pc=0x13dae5e
   > sync.runtime_Semacquire(0xc01c86c300?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc01c2e6f50 sp=0xc01c2e6f20 pc=0x13f7f65
   > sync.(*WaitGroup).Wait(0x3a092c252?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc01c2e6f78 sp=0xc01c2e6f50 pc=0x140b312
   > github.com/pingcap/tidb/executor.(*HashAggExec).waitAllWorkersAndCloseFinalOutputCh(0xc010d43800, {0xc01c2e6fb8, 0x3, 0x4134ba0?})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:827 +0x35 fp=0xc01c2e6f98 sp=0xc01c2e6f78 pc=0x2fbc5b5
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func6()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:864 +0x5a fp=0xc01c2e6fe0 sp=0xc01c2e6f98 pc=0x2fbcc1a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01c2e6fe8 sp=0xc01c2e6fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:864 +0x54d
   > goroutine 123447 [runnable]:
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60?, 0xc0148ab770?}, {0x40dbf60?, 0xc013e56c00?})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:183 +0x12c fp=0xc01e7e3a80 sp=0xc01e7e3a78 pc=0x1fb386c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc01484b090}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e3ab8 sp=0xc01e7e3a80 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc0147afcc0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e3af0 sp=0xc01e7e3ab8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc01484a550}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e3b28 sp=0xc01e7e3af0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc014771ef0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e3b60 sp=0xc01e7e3b28 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc014665e50}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e3b98 sp=0xc01e7e3b60 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc0146649b0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e3bd0 sp=0xc01e7e3b98 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc0147b05a0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e3c08 sp=0xc01e7e3bd0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc014804b40}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e3c40 sp=0xc01e7e3c08 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc014166230}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e3c78 sp=0xc01e7e3c40 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc014804050}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e3cb0 sp=0xc01e7e3c78 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc01462d950}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e3ce8 sp=0xc01e7e3cb0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc01462cb40}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e3d20 sp=0xc01e7e3ce8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc014726cd0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e3d58 sp=0xc01e7e3d20 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc013f95f40}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e3d90 sp=0xc01e7e3d58 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc013f94aa0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e3dc8 sp=0xc01e7e3d90 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc014525680}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e3e00 sp=0xc01e7e3dc8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc0145240f0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e3e38 sp=0xc01e7e3e00 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc01457caf0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e3e70 sp=0xc01e7e3e38 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc014591db0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e3ea8 sp=0xc01e7e3e70 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc0146aec80}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e3ee0 sp=0xc01e7e3ea8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc0146d7770}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e3f18 sp=0xc01e7e3ee0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc0141338b0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e3f50 sp=0xc01e7e3f18 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc014132c80}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e3f88 sp=0xc01e7e3f50 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc0144eb630}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e3fc0 sp=0xc01e7e3f88 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc0144ea0f0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e3ff8 sp=0xc01e7e3fc0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc01445b630}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4030 sp=0xc01e7e3ff8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc01454e7d0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4068 sp=0xc01e7e4030 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc01445ad70}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e40a0 sp=0xc01e7e4068 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc014404f00}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e40d8 sp=0xc01e7e40a0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc014005b80}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4110 sp=0xc01e7e40d8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc014004f00}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4148 sp=0xc01e7e4110 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc014494cd0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4180 sp=0xc01e7e4148 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc014004500}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e41b8 sp=0xc01e7e4180 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc01413eeb0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e41f0 sp=0xc01e7e41b8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc01452f4f0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4228 sp=0xc01e7e41f0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc0143af9a0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4260 sp=0xc01e7e4228 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc014311e50}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4298 sp=0xc01e7e4260 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc01442bb80}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e42d0 sp=0xc01e7e4298 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc0143f7ae0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4308 sp=0xc01e7e42d0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc0143f64b0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4340 sp=0xc01e7e4308 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc0142c59a0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4378 sp=0xc01e7e4340 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc01442a5a0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e43b0 sp=0xc01e7e4378 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc014089ae0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e43e8 sp=0xc01e7e43b0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc0142c4d20}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4420 sp=0xc01e7e43e8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc014303ae0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4458 sp=0xc01e7e4420 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc014383090}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4490 sp=0xc01e7e4458 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc014363e50}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e44c8 sp=0xc01e7e4490 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc01430e050}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4500 sp=0xc01e7e44c8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc014302d70}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4538 sp=0xc01e7e4500 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc014302050}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4570 sp=0xc01e7e4538 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc014382320}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e45a8 sp=0xc01e7e4570 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc0141ffcc0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e45e0 sp=0xc01e7e45a8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc01428c820}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4618 sp=0xc01e7e45e0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc0141d35e0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4650 sp=0xc01e7e4618 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc0141ff270}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4688 sp=0xc01e7e4650 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc0141d2000}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e46c0 sp=0xc01e7e4688 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc0141199a0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e46f8 sp=0xc01e7e46c0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc0142004b0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4730 sp=0xc01e7e46f8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc014118550}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4768 sp=0xc01e7e4730 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc01404ab40}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e47a0 sp=0xc01e7e4768 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc013eb3950}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e47d8 sp=0xc01e7e47a0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc013cc03c0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4810 sp=0xc01e7e47d8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc013af0f00}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4848 sp=0xc01e7e4810 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc0140f79a0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4880 sp=0xc01e7e4848 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc0140f7220}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e48b8 sp=0xc01e7e4880 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc013c4fa90}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e48f0 sp=0xc01e7e48b8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc013c4e5f0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4928 sp=0xc01e7e48f0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc013e81a40}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4960 sp=0xc01e7e4928 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc013f7ea00}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4998 sp=0xc01e7e4960 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc011aecaa0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e49d0 sp=0xc01e7e4998 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc014081770}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4a08 sp=0xc01e7e49d0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc013e80ff0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4a40 sp=0xc01e7e4a08 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc013dd9f40}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4a78 sp=0xc01e7e4a40 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc013dd9270}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4ab0 sp=0xc01e7e4a78 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc013ed5d60}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4ae8 sp=0xc01e7e4ab0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc013ed49b0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4b20 sp=0xc01e7e4ae8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc013cf75e0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4b58 sp=0xc01e7e4b20 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc013cd34f0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4b90 sp=0xc01e7e4b58 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc013f4bef0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4bc8 sp=0xc01e7e4b90 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc013f4aaa0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4c00 sp=0xc01e7e4bc8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc013e8a500}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4c38 sp=0xc01e7e4c00 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc013d1eb90}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4c70 sp=0xc01e7e4c38 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc013e599a0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4ca8 sp=0xc01e7e4c70 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc013e585a0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4ce0 sp=0xc01e7e4ca8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc013bc4a00}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4d18 sp=0xc01e7e4ce0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc013ab0690}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4d50 sp=0xc01e7e4d18 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc013a3ff90}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4d88 sp=0xc01e7e4d50 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc013b570e0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4dc0 sp=0xc01e7e4d88 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc013b56370}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4df8 sp=0xc01e7e4dc0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc013cc9220}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4e30 sp=0xc01e7e4df8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc01399b8b0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4e68 sp=0xc01e7e4e30 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc013a00780}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4ea0 sp=0xc01e7e4e68 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc013da3ef0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4ed8 sp=0xc01e7e4ea0 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc013da2a00}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4f10 sp=0xc01e7e4ed8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc013d19a40}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4f48 sp=0xc01e7e4f10 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc01387ad70}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4f80 sp=0xc01e7e4f48 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc013ba98b0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4fb8 sp=0xc01e7e4f80 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc013be1ef0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e4ff0 sp=0xc01e7e4fb8 pc=0x1fb3805
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x40dbc60, 0xc013c402d0}, {0x40dbf60, 0xc013e56c00})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc01e7e5028 sp=0xc01e7e4ff0 pc=0x1fb3805
   > ...additional frames elided...
   > created by github.com/pingcap/tidb/executor.(*UnionExec).initialize
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1623 +0x233
   > goroutine 121485 [semacquire]:
   > runtime.gopark(0x1f79bcb23c4?, 0x13a4953?, 0x0?, 0x80?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01c51f720 sp=0xc01c51f700 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc01a695814, 0xa8?, 0x3, 0x1)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc01c51f788 sp=0xc01c51f720 pc=0x13dae5e
   > sync.runtime_SemacquireMutex(0x606d020?, 0x4?, 0xc01278a000?)
   > 	/usr/local/go/src/runtime/sema.go:77 +0x25 fp=0xc01c51f7b8 sp=0xc01c51f788 pc=0x13f8085
   > sync.(*Mutex).lockSlow(0xc01a695810)
   > 	/usr/local/go/src/sync/mutex.go:171 +0x165 fp=0xc01c51f808 sp=0xc01c51f7b8 pc=0x1409825
   > sync.(*Mutex).Lock(...)
   > 	/usr/local/go/src/sync/mutex.go:90
   > github.com/pingcap/tidb/util/cteutil.(*StorageRC).Lock(0x142ce14?)
   > 	/go/src/github.com/pingcap/tidb/util/cteutil/storage.go:209 +0x31 fp=0xc01c51f820 sp=0xc01c51f808 pc=0x2f77ab1
   > github.com/pingcap/tidb/executor.(*CTEExec).Next(0xc014cefcc0, {0x40d68d0, 0xc01ac388a0}, 0xc012a76af0)
   > 	/go/src/github.com/pingcap/tidb/executor/cte.go:149 +0xa8 fp=0xc01c51f898 sp=0xc01c51f820 pc=0x3022a08
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc01ac388a0}, {0x40d8d60, 0xc014cefcc0}, 0xc012a76af0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc01c51f9d8 sp=0xc01c51f898 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*NestedLoopApplyExec).fetchSelectedOuterRow(0xc01131b6c0, {0x40d68d0, 0xc01ac388a0}, 0xc012a76be0)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:929 +0xc9 fp=0xc01c51fa58 sp=0xc01c51f9d8 pc=0x30b22e9
   > github.com/pingcap/tidb/executor.(*NestedLoopApplyExec).Next(0xc01131b6c0, {0x40d68d0, 0xc01ac388a0}, 0xc012a76be0)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:1007 +0x1a8 fp=0xc01c51fbb8 sp=0xc01c51fa58 pc=0x30b2ea8
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc01ac388a0}, {0x40d9560, 0xc01131b6c0}, 0xc012a76be0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc01c51fcf8 sp=0xc01c51fbb8 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*ProjectionExec).unParallelExecute(0xc015909b00, {0x40d68d0?, 0xc01ac388a0?}, 0xc012a1ce60)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:194 +0xb8 fp=0xc01c51fd48 sp=0xc01c51fcf8 pc=0x30eb458
   > github.com/pingcap/tidb/executor.(*ProjectionExec).Next(0xc015909b00, {0x40d68d0, 0xc01ac388a0}, 0xc010431f0c?)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:180 +0x5a fp=0xc01c51fd80 sp=0xc01c51fd48 pc=0x30eb31a
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc01ac388a0}, {0x40d9720, 0xc015909b00}, 0xc012a1ce60)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc01c51fec0 sp=0xc01c51fd80 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*UnionExec).resultPuller(0xc015450e00, {0x40d68d0, 0xc01ac388a0}, 0x1)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1673 +0x48f fp=0xc01c51ffb0 sp=0xc01c51fec0 pc=0x30420ef
   > github.com/pingcap/tidb/executor.(*UnionExec).initialize.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1623 +0x32 fp=0xc01c51ffe0 sp=0xc01c51ffb0 pc=0x3041c32
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01c51ffe8 sp=0xc01c51ffe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*UnionExec).initialize
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1623 +0x233
   > goroutine 121904 [select]:
   > runtime.gopark(0xc016570f28?, 0x2?, 0x2?, 0x0?, 0xc016570eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc016570d58 sp=0xc016570d38 pc=0x13c9516
   > runtime.selectgo(0xc016570f28, 0xc016570ee8, 0x13?, 0x0, 0xc01674e1c8?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc016570e98 sp=0xc016570d58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc0102f0000, {0x4134ba0, 0xc0144ce240}, 0xc013efd450, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc016570fa8 sp=0xc016570e98 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc016570fe0 sp=0xc016570fa8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc016570fe8 sp=0xc016570fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 123573 [semacquire]:
   > runtime.gopark(0x0?, 0xc000f4fed0?, 0x80?, 0x8a?, 0x3f98823db?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000f4fe90 sp=0xc000f4fe70 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc0179bdf18, 0xd5?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc000f4fef8 sp=0xc000f4fe90 pc=0x13dae5e
   > sync.runtime_Semacquire(0x2fbbcf4?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc000f4ff28 sp=0xc000f4fef8 pc=0x13f7f65
   > sync.(*WaitGroup).Wait(0xc01068fe40?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc000f4ff50 sp=0xc000f4ff28 pc=0x140b312
   > github.com/pingcap/tidb/executor.(*HashAggExec).waitPartialWorkerAndCloseOutputChs(0xc010d43000, 0x13d0505?)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:815 +0x25 fp=0xc000f4ff98 sp=0xc000f4ff50 pc=0x2fbc465
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:844 +0x45 fp=0xc000f4ffe0 sp=0xc000f4ff98 pc=0x2fbcd85
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000f4ffe8 sp=0xc000f4ffe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:843 +0x2e5
   > goroutine 111493 [select]:
   > runtime.gopark(0xc015d2cf28?, 0x2?, 0xc8?, 0x11?, 0xc015d2ceec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc015d2cd58 sp=0xc015d2cd38 pc=0x13c9516
   > runtime.selectgo(0xc015d2cf28, 0xc015d2cee8, 0xc015d2cf10?, 0x0, 0xc01b127500?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc015d2ce98 sp=0xc015d2cd58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc01c7bd240, {0x4134ba0, 0xc0144ce240}, 0xc01942d600, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc015d2cfa8 sp=0xc015d2ce98 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc015d2cfe0 sp=0xc015d2cfa8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc015d2cfe8 sp=0xc015d2cfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 111499 [select]:
   > runtime.gopark(0xc017a3bf00?, 0x2?, 0x16?, 0x95?, 0xc017a3be44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc017a3bc48 sp=0xc017a3bc28 pc=0x13c9516
   > runtime.selectgo(0xc017a3bf00, 0xc017a3be40, 0x2?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc017a3bd88 sp=0xc017a3bc48 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc01c7bd640, {0x4134ba0, 0xc0144ce240})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc017a3bf30 sp=0xc017a3bd88 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc01c7bd640, {0x4134ba0, 0xc0144ce240}, 0xc01942d610)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc017a3bfb0 sp=0xc017a3bf30 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc017a3bfe0 sp=0xc017a3bfb0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc017a3bfe8 sp=0xc017a3bfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 123580 [semacquire]:
   > runtime.gopark(0xc000f86f08?, 0xc000b1a000?, 0x80?, 0x19?, 0x13fa50e?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000f86eb8 sp=0xc000f86e98 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc0179bdf08, 0xce?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc000f86f20 sp=0xc000f86eb8 pc=0x13dae5e
   > sync.runtime_Semacquire(0xc0101391e0?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc000f86f50 sp=0xc000f86f20 pc=0x13f7f65
   > sync.(*WaitGroup).Wait(0xc000f86fa0?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc000f86f78 sp=0xc000f86f50 pc=0x140b312
   > github.com/pingcap/tidb/executor.(*HashAggExec).waitAllWorkersAndCloseFinalOutputCh(0xc010d43000, {0xc000f86fb8, 0x3, 0xc013f890e0?})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:827 +0x35 fp=0xc000f86f98 sp=0xc000f86f78 pc=0x2fbc5b5
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func6()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:864 +0x5a fp=0xc000f86fe0 sp=0xc000f86f98 pc=0x2fbcc1a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000f86fe8 sp=0xc000f86fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:864 +0x54d
   > goroutine 121975 [select]:
   > runtime.gopark(0xc000bccf00?, 0x2?, 0x0?, 0x25?, 0xc000bcce44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000bccc48 sp=0xc000bccc28 pc=0x13c9516
   > runtime.selectgo(0xc000bccf00, 0xc000bcce40, 0x0?, 0x0, 0xc000bccdc0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000bccd88 sp=0xc000bccc48 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc0102f04c0, {0x4134ba0, 0xc0144ce240})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc000bccf30 sp=0xc000bccd88 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc0102f04c0, {0x4134ba0, 0xc0144ce240}, 0xc013efd460)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc000bccfb0 sp=0xc000bccf30 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc000bccfe0 sp=0xc000bccfb0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000bccfe8 sp=0xc000bccfe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 123575 [select]:
   > runtime.gopark(0xc0167c3f00?, 0x2?, 0x3?, 0x0?, 0xc0167c3e44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0167c3c48 sp=0xc0167c3c28 pc=0x13c9516
   > runtime.selectgo(0xc0167c3f00, 0xc0167c3e40, 0xc013c4e820?, 0x0, 0x606b430?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0167c3d88 sp=0xc0167c3c48 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc01071acc0, {0x4134ba0, 0xc0114b7d40})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc0167c3f30 sp=0xc0167c3d88 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc01071acc0, {0x4134ba0, 0xc0114b7d40}, 0xc0179bdf20)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc0167c3fb0 sp=0xc0167c3f30 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc0167c3fe0 sp=0xc0167c3fb0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0167c3fe8 sp=0xc0167c3fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 123446 [chan receive]:
   > runtime.gopark(0xc017afd080?, 0xc0169c0820?, 0x6d?, 0xcb?, 0xc01c55f448?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01c55f3a0 sp=0xc01c55f380 pc=0x13c9516
   > runtime.chanrecv(0xc013f08420, 0xc01c55f478, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc01c55f430 sp=0xc01c55f3a0 pc=0x13934bb
   > runtime.chanrecv2(0xc010d43000?, 0x40d68d0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc01c55f458 sp=0xc01c55f430 pc=0x1392ff8
   > github.com/pingcap/tidb/executor.(*HashAggExec).parallelExec(0xc010d43000, {0x40d68d0?, 0xc010570240?}, 0xc013cc0be0)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:888 +0x89 fp=0xc01c55f490 sp=0xc01c55f458 pc=0x2fbcf29
   > github.com/pingcap/tidb/executor.(*HashAggExec).Next(0x40d68d0?, {0x40d68d0?, 0xc010570240?}, 0xc01c55f540?)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:768 +0x76 fp=0xc01c55f4c0 sp=0xc01c55f490 pc=0x2fbbeb6
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc010570240}, {0x40d9120, 0xc010d43000}, 0xc013cc0be0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc01c55f600 sp=0xc01c55f4c0 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*MaxOneRowExec).Next(0xc0100019d0, {0x40d68d0, 0xc010570240}, 0xc013cc0be0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1518 +0xa8 fp=0xc01c55f650 sp=0xc01c55f600 pc=0x30413a8
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc010570240}, {0x40d94a0, 0xc0100019d0}, 0xc013cc0be0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc01c55f790 sp=0xc01c55f650 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*SelectionExec).Next(0xc00ff45860, {0x40d68d0, 0xc010570240}, 0xc013af1c20)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1394 +0xed fp=0xc01c55f820 sp=0xc01c55f790 pc=0x304012d
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc010570240}, {0x40d9960, 0xc00ff45860}, 0xc013af1c20)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc01c55f960 sp=0xc01c55f820 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*NestedLoopApplyExec).fetchAllInners(0xc000360fc0, {0x40d68d0, 0xc010570240})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:979 +0x346 fp=0xc01c55fa58 sp=0xc01c55f960 pc=0x30b2966
   > github.com/pingcap/tidb/executor.(*NestedLoopApplyExec).Next(0xc000360fc0, {0x40d68d0, 0xc010570240}, 0xc013af1c70)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:1032 +0x5b6 fp=0xc01c55fbb8 sp=0xc01c55fa58 pc=0x30b32b6
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc010570240}, {0x40d9560, 0xc000360fc0}, 0xc013af1c70)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc01c55fcf8 sp=0xc01c55fbb8 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*ProjectionExec).unParallelExecute(0xc010008480, {0x40d68d0?, 0xc010570240?}, 0xc013af1a40)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:194 +0xb8 fp=0xc01c55fd48 sp=0xc01c55fcf8 pc=0x30eb458
   > github.com/pingcap/tidb/executor.(*ProjectionExec).Next(0xc010008480, {0x40d68d0, 0xc010570240}, 0xc01c55ff0c?)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:180 +0x5a fp=0xc01c55fd80 sp=0xc01c55fd48 pc=0x30eb31a
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc010570240}, {0x40d9720, 0xc010008480}, 0xc013af1a40)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc01c55fec0 sp=0xc01c55fd80 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*UnionExec).resultPuller(0xc000733e00, {0x40d68d0, 0xc010570240}, 0x0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1673 +0x48f fp=0xc01c55ffb0 sp=0xc01c55fec0 pc=0x30420ef
   > github.com/pingcap/tidb/executor.(*UnionExec).initialize.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1623 +0x32 fp=0xc01c55ffe0 sp=0xc01c55ffb0 pc=0x3041c32
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01c55ffe8 sp=0xc01c55ffe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*UnionExec).initialize
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1623 +0x233
   > goroutine 123570 [select]:
   > runtime.gopark(0xc015cd0f28?, 0x2?, 0x0?, 0x0?, 0xc015cd0eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc015cd0d58 sp=0xc015cd0d38 pc=0x13c9516
   > runtime.selectgo(0xc015cd0f28, 0xc015cd0ee8, 0x3b67af1?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc015cd0e98 sp=0xc015cd0d58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc01071a980, {0x4134ba0, 0xc0114b7d40}, 0xc0179bdf10, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc015cd0fa8 sp=0xc015cd0e98 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc015cd0fe0 sp=0xc015cd0fa8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc015cd0fe8 sp=0xc015cd0fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 121981 [chan receive]:
   > runtime.gopark(0xc00fe443c0?, 0xc012af75e0?, 0x90?, 0x75?, 0xc012762060?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010a79c48 sp=0xc010a79c28 pc=0x13c9516
   > runtime.chanrecv(0xc0125e57a0, 0xc010a79d28, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc010a79cd8 sp=0xc010a79c48 pc=0x13934bb
   > runtime.chanrecv1(0xc015909560?, 0x40d68d0?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc010a79d00 sp=0xc010a79cd8 pc=0x1392fb8
   > github.com/pingcap/tidb/executor.(*ProjectionExec).parallelExecute(0xc015909560, {0x40d68d0?, 0xc01ac388a0?}, 0xc012e44c80)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:218 +0x92 fp=0xc010a79d48 sp=0xc010a79d00 pc=0x30eb612
   > github.com/pingcap/tidb/executor.(*ProjectionExec).Next(0xc015909560, {0x40d68d0, 0xc01ac388a0}, 0xc010a79f0c?)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:182 +0x78 fp=0xc010a79d80 sp=0xc010a79d48 pc=0x30eb338
   > github.com/pingcap/tidb/executor.Next({0x40d68d0, 0xc01ac388a0}, {0x40d9720, 0xc015909560}, 0xc012e44c80)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:302 +0x496 fp=0xc010a79ec0 sp=0xc010a79d80 pc=0x3038e96
   > github.com/pingcap/tidb/executor.(*UnionExec).resultPuller(0xc015450c00, {0x40d68d0, 0xc01ac388a0}, 0x0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1673 +0x48f fp=0xc010a79fb0 sp=0xc010a79ec0 pc=0x30420ef
   > github.com/pingcap/tidb/executor.(*UnionExec).initialize.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1623 +0x32 fp=0xc010a79fe0 sp=0xc010a79fb0 pc=0x3041c32
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010a79fe8 sp=0xc010a79fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*UnionExec).initialize
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1623 +0x233
   > goroutine 121976 [select]:
   > runtime.gopark(0xc00fa45f00?, 0x2?, 0x0?, 0x79?, 0xc00fa45e44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fa45c48 sp=0xc00fa45c28 pc=0x13c9516
   > runtime.selectgo(0xc00fa45f00, 0xc00fa45e40, 0x0?, 0x0, 0xc00fa45dc0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fa45d88 sp=0xc00fa45c48 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).getPartialInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:628
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).consumeIntermData(0xc0102f0580, {0x4134ba0, 0xc0144ce240})
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:649 +0x107 fp=0xc00fa45f30 sp=0xc00fa45d88 pc=0x2fba627
   > github.com/pingcap/tidb/executor.(*HashAggFinalWorker).run(0xc0102f0580, {0x4134ba0, 0xc0144ce240}, 0xc013efd460)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:756 +0xbc fp=0xc00fa45fb0 sp=0xc00fa45f30 pc=0x2fbbc1c
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x32 fp=0xc00fa45fe0 sp=0xc00fa45fb0 pc=0x2fbcd12
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fa45fe8 sp=0xc00fa45fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:853 +0x33b
   > goroutine 123568 [select]:
   > runtime.gopark(0xc000d92f28?, 0x2?, 0x2?, 0x0?, 0xc000d92eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000d92d58 sp=0xc000d92d38 pc=0x13c9516
   > runtime.selectgo(0xc000d92f28, 0xc000d92ee8, 0x3b67af1?, 0x0, 0xc0101aad50?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000d92e98 sp=0xc000d92d58 pc=0x13d9bdc
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).getChildInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:441
   > github.com/pingcap/tidb/executor.(*HashAggPartialWorker).run(0xc01071a800, {0x4134ba0, 0xc0114b7d40}, 0xc0179bdf10, 0x5)
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:481 +0x1e7 fp=0xc000d92fa8 sp=0xc000d92e98 pc=0x2fb8c07
   > github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x36 fp=0xc000d92fe0 sp=0xc000d92fa8 pc=0x2fbce16
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000d92fe8 sp=0xc000d92fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*HashAggExec).prepare4ParallelExec
   > 	/go/src/github.com/pingcap/tidb/executor/aggregate.go:841 +0x149
   > goroutine 121486 [semacquire]:
   > runtime.gopark(0xc01a5000c0?, 0x0?, 0x40?, 0x8b?, 0x1000000010000?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000630ef0 sp=0xc000630ed0 pc=0x13c9516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc015450ed0, 0xa0?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc000630f58 sp=0xc000630ef0 pc=0x13dae5e
   > sync.runtime_Semacquire(0xc01e68e720?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc000630f88 sp=0xc000630f58 pc=0x13f7f65
   > sync.(*WaitGroup).Wait(0x30ec08e?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc000630fb0 sp=0xc000630f88 pc=0x140b312
   > github.com/pingcap/tidb/executor.(*UnionExec).waitAllFinished(0xc015450e00)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1595 +0x2a fp=0xc000630fc8 sp=0xc000630fb0 pc=0x30415ea
   > github.com/pingcap/tidb/executor.(*UnionExec).initialize.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1629 +0x26 fp=0xc000630fe0 sp=0xc000630fc8 pc=0x3041bc6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000630fe8 sp=0xc000630fe0 pc=0x13fc6e1
   > created by github.com/pingcap/tidb/executor.(*UnionExec).initialize
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:1629 +0x40b
