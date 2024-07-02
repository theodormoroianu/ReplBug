# Bug ID TIDB-36896-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/36896
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
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
     - Output: ERROR: Timeout for this transaction.
     - Executed order: Not executed

 * Container logs:
   > [2024/07/02 13:51:07.320 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/07/02 13:51:07.323 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=32] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/02 13:51:07.323 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=32] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/02 13:51:07.325 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:66, Type:create schema, State:none, SchemaState:queueing, SchemaID:65, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 13:51:07.324 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 13:51:07.325 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:66, Type:create schema, State:none, SchemaState:queueing, SchemaID:65, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 13:51:07.324 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/02 13:51:07.325 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:create schema, State:none, SchemaState:queueing, SchemaID:65, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:51:07.324 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:51:07.326 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=32] [neededSchemaVersion=33] ["start time"=125.715µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 13:51:07.328 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=33] ["take time"=2.191289ms] [job="ID:66, Type:create schema, State:done, SchemaState:public, SchemaID:65, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 13:51:07.324 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:51:07.329 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:create schema, State:synced, SchemaState:public, SchemaID:65, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:51:07.324 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:51:07.329 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=66]
   > [2024/07/02 13:51:07.329 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 13:51:07.335 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=33] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_2el7jd`\n--\n\nDROP TABLE IF EXISTS `t_2el7jd`;"] [user=root@%]
   > [2024/07/02 13:51:07.335 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=33] [cur_db=testdb] [sql="CREATE TABLE `t_2el7jd` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_hzkgf` text DEFAULT NULL,\n  `c_si87c` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_alxrj` (`wkey`,`pkey`,`c_si87c`),\n  KEY `t_za4dpb` (`pkey`,`c_si87c`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/07/02 13:51:07.337 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:68, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:67, RowCount:0, ArgLen:1, start time: 2024-07-02 13:51:07.336 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 13:51:07.337 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:68, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:67, RowCount:0, ArgLen:1, start time: 2024-07-02 13:51:07.336 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_2el7jd` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_hzkgf` text DEFAULT NULL,\n  `c_si87c` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_alxrj` (`wkey`,`pkey`,`c_si87c`),\n  KEY `t_za4dpb` (`pkey`,`c_si87c`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/02 13:51:07.338 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:68, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:67, RowCount:0, ArgLen:0, start time: 2024-07-02 13:51:07.336 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:51:07.340 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=33] [neededSchemaVersion=34] ["start time"=372.258µs] [phyTblIDs="[67]"] [actionTypes="[8]"]
   > [2024/07/02 13:51:07.341 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=34] ["take time"=2.264623ms] [job="ID:68, Type:create table, State:done, SchemaState:public, SchemaID:65, TableID:67, RowCount:0, ArgLen:1, start time: 2024-07-02 13:51:07.336 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:51:07.342 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:68, Type:create table, State:synced, SchemaState:public, SchemaID:65, TableID:67, RowCount:0, ArgLen:0, start time: 2024-07-02 13:51:07.336 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:51:07.344 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=68]
   > [2024/07/02 13:51:07.344 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 13:51:07.344 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=60] ["first split key"=748000000000000043]
   > [2024/07/02 13:51:07.344 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=34] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_2el7jd` DISABLE KEYS */;"] [user=root@%]
   > [2024/07/02 13:51:07.347 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=62] ["first at"=748000000000000043] ["first new region left"="{Id:62 StartKey:7480000000000000ff3f00000000000000f8 EndKey:7480000000000000ff4300000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:63 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/02 13:51:07.347 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[62]"]
   > [2024/07/02 13:51:07.348 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=34] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_2el7jd` ENABLE KEYS */;"] [user=root@%]
   > [2024/07/02 13:51:07.348 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=34] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_p7c1bd`\n--\n\nDROP TABLE IF EXISTS `t_p7c1bd`;"] [user=root@%]
   > [2024/07/02 13:51:07.349 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=34] [cur_db=testdb] [sql="CREATE TABLE `t_p7c1bd` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_rrbxh` text DEFAULT NULL,\n  `c_c5cvkb` int(11) DEFAULT NULL,\n  `c_ag5ccc` int(11) DEFAULT NULL,\n  `c_qo4qvc` text DEFAULT NULL,\n  `c_lhs3h` int(11) DEFAULT NULL,\n  `c_8dah2b` int(11) DEFAULT NULL,\n  `c_eg6xsc` int(11) DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_s0z7f` (`c_ag5ccc`,`c_8dah2b`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/07/02 13:51:07.351 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:70, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:69, RowCount:0, ArgLen:1, start time: 2024-07-02 13:51:07.35 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 13:51:07.351 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:70, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:69, RowCount:0, ArgLen:1, start time: 2024-07-02 13:51:07.35 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_p7c1bd` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_rrbxh` text DEFAULT NULL,\n  `c_c5cvkb` int(11) DEFAULT NULL,\n  `c_ag5ccc` int(11) DEFAULT NULL,\n  `c_qo4qvc` text DEFAULT NULL,\n  `c_lhs3h` int(11) DEFAULT NULL,\n  `c_8dah2b` int(11) DEFAULT NULL,\n  `c_eg6xsc` int(11) DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_s0z7f` (`c_ag5ccc`,`c_8dah2b`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/02 13:51:07.351 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:70, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:69, RowCount:0, ArgLen:0, start time: 2024-07-02 13:51:07.35 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:51:07.353 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=34] [neededSchemaVersion=35] ["start time"=487.845µs] [phyTblIDs="[69]"] [actionTypes="[8]"]
   > [2024/07/02 13:51:07.355 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=35] ["take time"=2.27042ms] [job="ID:70, Type:create table, State:done, SchemaState:public, SchemaID:65, TableID:69, RowCount:0, ArgLen:1, start time: 2024-07-02 13:51:07.35 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:51:07.356 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:70, Type:create table, State:synced, SchemaState:public, SchemaID:65, TableID:69, RowCount:0, ArgLen:0, start time: 2024-07-02 13:51:07.35 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:51:07.357 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=70]
   > [2024/07/02 13:51:07.358 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 13:51:07.358 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=64] ["first split key"=748000000000000045]
   > [2024/07/02 13:51:07.358 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=64] ["first at"=748000000000000045] ["first new region left"="{Id:64 StartKey:7480000000000000ff4300000000000000f8 EndKey:7480000000000000ff4500000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:65 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/02 13:51:07.358 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[64]"]
   > [2024/07/02 13:51:07.358 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=35] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_p7c1bd` DISABLE KEYS */;"] [user=root@%]
   > [2024/07/02 13:51:07.363 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=35] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_p7c1bd` ENABLE KEYS */;"] [user=root@%]
   > [2024/07/02 13:51:08.391 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]

### Scenario 1
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
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
     - Output: ERROR: Timeout for this transaction.
     - Executed order: Not executed
 * Instruction #3:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: ERROR: Timeout for this transaction.
     - Executed order: Not executed

 * Container logs:
   > [2024/07/02 13:51:19.033 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/07/02 13:51:19.035 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=43] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/02 13:51:19.036 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:77, Type:drop schema, State:none, SchemaState:queueing, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:51:19.036 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 13:51:19.036 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:77, Type:drop schema, State:none, SchemaState:queueing, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:51:19.036 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/02 13:51:19.037 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:none, SchemaState:queueing, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:51:19.036 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:51:19.038 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=43] [neededSchemaVersion=44] ["start time"=53.359µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 13:51:19.040 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=44] ["take time"=2.184445ms] [job="ID:77, Type:drop schema, State:running, SchemaState:write only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:51:19.036 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:51:19.040 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:running, SchemaState:write only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:51:19.036 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:51:19.041 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=44] [neededSchemaVersion=45] ["start time"=90.515µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 13:51:19.043 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=45] ["take time"=2.353463ms] [job="ID:77, Type:drop schema, State:running, SchemaState:delete only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:51:19.036 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:51:19.043 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:running, SchemaState:delete only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:51:19.036 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:51:19.044 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=45] [neededSchemaVersion=46] ["start time"=83.321µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 13:51:19.046 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=46] ["take time"=2.240388ms] [job="ID:77, Type:drop schema, State:done, SchemaState:queueing, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:51:19.036 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:51:19.047 +00:00] [INFO] [delete_range.go:103] ["[ddl] add job into delete-range table"] [jobID=77] [jobType="drop schema"]
   > [2024/07/02 13:51:19.047 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:51:19.036 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:51:19.048 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=77]
   > [2024/07/02 13:51:19.048 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 13:51:19.049 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=46] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/02 13:51:19.050 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:79, Type:create schema, State:none, SchemaState:queueing, SchemaID:78, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 13:51:19.049 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 13:51:19.050 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:79, Type:create schema, State:none, SchemaState:queueing, SchemaID:78, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 13:51:19.049 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/02 13:51:19.050 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:79, Type:create schema, State:none, SchemaState:queueing, SchemaID:78, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:51:19.049 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:51:19.051 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=46] [neededSchemaVersion=47] ["start time"=80.388µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 13:51:19.053 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=47] ["take time"=2.193455ms] [job="ID:79, Type:create schema, State:done, SchemaState:public, SchemaID:78, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 13:51:19.049 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:51:19.054 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:79, Type:create schema, State:synced, SchemaState:public, SchemaID:78, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:51:19.049 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:51:19.054 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=79]
   > [2024/07/02 13:51:19.054 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 13:51:19.060 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=47] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_2el7jd`\n--\n\nDROP TABLE IF EXISTS `t_2el7jd`;"] [user=root@%]
   > [2024/07/02 13:51:19.060 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=47] [cur_db=testdb] [sql="CREATE TABLE `t_2el7jd` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_hzkgf` text DEFAULT NULL,\n  `c_si87c` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_alxrj` (`wkey`,`pkey`,`c_si87c`),\n  KEY `t_za4dpb` (`pkey`,`c_si87c`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/07/02 13:51:19.061 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:81, Type:create table, State:none, SchemaState:queueing, SchemaID:78, TableID:80, RowCount:0, ArgLen:1, start time: 2024-07-02 13:51:19.061 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 13:51:19.061 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:81, Type:create table, State:none, SchemaState:queueing, SchemaID:78, TableID:80, RowCount:0, ArgLen:1, start time: 2024-07-02 13:51:19.061 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_2el7jd` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_hzkgf` text DEFAULT NULL,\n  `c_si87c` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_alxrj` (`wkey`,`pkey`,`c_si87c`),\n  KEY `t_za4dpb` (`pkey`,`c_si87c`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/02 13:51:19.062 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:81, Type:create table, State:none, SchemaState:queueing, SchemaID:78, TableID:80, RowCount:0, ArgLen:0, start time: 2024-07-02 13:51:19.061 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:51:19.063 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=47] [neededSchemaVersion=48] ["start time"=394.048µs] [phyTblIDs="[80]"] [actionTypes="[8]"]
   > [2024/07/02 13:51:19.065 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=48] ["take time"=2.048673ms] [job="ID:81, Type:create table, State:done, SchemaState:public, SchemaID:78, TableID:80, RowCount:0, ArgLen:1, start time: 2024-07-02 13:51:19.061 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:51:19.066 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:81, Type:create table, State:synced, SchemaState:public, SchemaID:78, TableID:80, RowCount:0, ArgLen:0, start time: 2024-07-02 13:51:19.061 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:51:19.067 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=81]
   > [2024/07/02 13:51:19.067 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 13:51:19.067 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=68] ["first split key"=748000000000000050]
   > [2024/07/02 13:51:19.068 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=68] ["first at"=748000000000000050] ["first new region left"="{Id:68 StartKey:7480000000000000ff4a00000000000000f8 EndKey:7480000000000000ff5000000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:69 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/02 13:51:19.068 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[68]"]
   > [2024/07/02 13:51:19.068 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=48] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_2el7jd` DISABLE KEYS */;"] [user=root@%]
   > [2024/07/02 13:51:19.071 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=48] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_2el7jd` ENABLE KEYS */;"] [user=root@%]
   > [2024/07/02 13:51:19.071 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=48] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_p7c1bd`\n--\n\nDROP TABLE IF EXISTS `t_p7c1bd`;"] [user=root@%]
   > [2024/07/02 13:51:19.072 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=48] [cur_db=testdb] [sql="CREATE TABLE `t_p7c1bd` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_rrbxh` text DEFAULT NULL,\n  `c_c5cvkb` int(11) DEFAULT NULL,\n  `c_ag5ccc` int(11) DEFAULT NULL,\n  `c_qo4qvc` text DEFAULT NULL,\n  `c_lhs3h` int(11) DEFAULT NULL,\n  `c_8dah2b` int(11) DEFAULT NULL,\n  `c_eg6xsc` int(11) DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_s0z7f` (`c_ag5ccc`,`c_8dah2b`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/07/02 13:51:19.073 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:83, Type:create table, State:none, SchemaState:queueing, SchemaID:78, TableID:82, RowCount:0, ArgLen:1, start time: 2024-07-02 13:51:19.072 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 13:51:19.073 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:83, Type:create table, State:none, SchemaState:queueing, SchemaID:78, TableID:82, RowCount:0, ArgLen:1, start time: 2024-07-02 13:51:19.072 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_p7c1bd` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_rrbxh` text DEFAULT NULL,\n  `c_c5cvkb` int(11) DEFAULT NULL,\n  `c_ag5ccc` int(11) DEFAULT NULL,\n  `c_qo4qvc` text DEFAULT NULL,\n  `c_lhs3h` int(11) DEFAULT NULL,\n  `c_8dah2b` int(11) DEFAULT NULL,\n  `c_eg6xsc` int(11) DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_s0z7f` (`c_ag5ccc`,`c_8dah2b`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/02 13:51:19.073 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:83, Type:create table, State:none, SchemaState:queueing, SchemaID:78, TableID:82, RowCount:0, ArgLen:0, start time: 2024-07-02 13:51:19.072 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:51:19.075 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=48] [neededSchemaVersion=49] ["start time"=493.712µs] [phyTblIDs="[82]"] [actionTypes="[8]"]
   > [2024/07/02 13:51:19.077 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=49] ["take time"=2.148267ms] [job="ID:83, Type:create table, State:done, SchemaState:public, SchemaID:78, TableID:82, RowCount:0, ArgLen:1, start time: 2024-07-02 13:51:19.072 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:51:19.078 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:83, Type:create table, State:synced, SchemaState:public, SchemaID:78, TableID:82, RowCount:0, ArgLen:0, start time: 2024-07-02 13:51:19.072 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:51:19.080 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=83]
   > [2024/07/02 13:51:19.080 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 13:51:19.080 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=70] ["first split key"=748000000000000052]
   > [2024/07/02 13:51:19.080 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=70] ["first at"=748000000000000052] ["first new region left"="{Id:70 StartKey:7480000000000000ff5000000000000000f8 EndKey:7480000000000000ff5200000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:71 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/02 13:51:19.080 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[70]"]
   > [2024/07/02 13:51:19.080 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=49] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_p7c1bd` DISABLE KEYS */;"] [user=root@%]
   > [2024/07/02 13:51:19.084 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=49] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_p7c1bd` ENABLE KEYS */;"] [user=root@%]
   > [2024/07/02 13:51:20.115 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/07/02 13:51:20.125 +00:00] [INFO] [set.go:147] ["set global var"] [conn=413] [name=tx_isolation] [val=READ-COMMITTED]
