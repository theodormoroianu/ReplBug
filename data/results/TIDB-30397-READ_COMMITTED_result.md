# Bug ID TIDB-30397-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/30397
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED


## Details
 * Database: tidb-v5.4.0
 * Number of scenarios: 2
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  update t_berydd set c_cdqetd = t_berydd.c_ioru4c;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
 * Instruction #1:
     - Instruction:  select count(c_mp6ko) from t_berydd;
     - Transaction: conn_0
     - Output: [(39,)]
     - Executed order: 1

 * Container logs:
   > [2024/07/01 15:13:02.211 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=33] [user=root] [host=]
   > [2024/07/01 15:13:02.215 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=33] [schemaVersion=79] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/07/01 15:13:02.216 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:104, Type:drop schema, State:none, SchemaState:queueing, SchemaID:99, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:13:02.215 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:13:02.216 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:104, Type:drop schema, State:none, SchemaState:queueing, SchemaID:99, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:13:02.215 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/01 15:13:02.216 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:104, Type:drop schema, State:none, SchemaState:queueing, SchemaID:99, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:13:02.215 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:13:02.217 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=79] [neededSchemaVersion=80] ["start time"=94.077µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:13:02.220 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=80] ["take time"=2.263719ms] [job="ID:104, Type:drop schema, State:running, SchemaState:write only, SchemaID:99, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:13:02.215 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:13:02.220 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:104, Type:drop schema, State:running, SchemaState:write only, SchemaID:99, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:13:02.215 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:13:02.221 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=80] [neededSchemaVersion=81] ["start time"=82.274µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:13:02.223 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=81] ["take time"=2.210289ms] [job="ID:104, Type:drop schema, State:running, SchemaState:delete only, SchemaID:99, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:13:02.215 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:13:02.223 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:104, Type:drop schema, State:running, SchemaState:delete only, SchemaID:99, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:13:02.215 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:13:02.225 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=81] [neededSchemaVersion=82] ["start time"=112.655µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:13:02.227 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=82] ["take time"=3.104127ms] [job="ID:104, Type:drop schema, State:done, SchemaState:queueing, SchemaID:99, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:13:02.215 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:13:02.228 +00:00] [INFO] [delete_range.go:107] ["[ddl] add job into delete-range table"] [jobID=104] [jobType="drop schema"]
   > [2024/07/01 15:13:02.228 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:104, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:99, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:13:02.215 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:13:02.229 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=104]
   > [2024/07/01 15:13:02.229 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:13:02.230 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=33] [schemaVersion=82] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/07/01 15:13:02.232 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:106, Type:create schema, State:none, SchemaState:queueing, SchemaID:105, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:13:02.231 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:13:02.232 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:106, Type:create schema, State:none, SchemaState:queueing, SchemaID:105, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:13:02.231 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/01 15:13:02.232 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:106, Type:create schema, State:none, SchemaState:queueing, SchemaID:105, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:13:02.231 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:13:02.233 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=82] [neededSchemaVersion=83] ["start time"=163.361µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:13:02.235 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=83] ["take time"=2.270981ms] [job="ID:106, Type:create schema, State:done, SchemaState:public, SchemaID:105, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:13:02.231 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:13:02.236 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:106, Type:create schema, State:synced, SchemaState:public, SchemaID:105, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:13:02.231 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:13:02.237 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=106]
   > [2024/07/01 15:13:02.237 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:13:02.243 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=33] [schemaVersion=83] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_berydd`\n--\n\nDROP TABLE IF EXISTS `t_berydd`;"] [user=root@127.0.0.1]
   > [2024/07/01 15:13:02.244 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=33] [schemaVersion=83] [cur_db=testdb] [sql="CREATE TABLE `t_berydd` (\n  `c_ymgvrd` int(11) DEFAULT NULL,\n  `c_ee5vqb` int(11) DEFAULT NULL,\n  `c_xsjoqb` int(11) DEFAULT NULL,\n  `c_xqizm` text DEFAULT NULL,\n  `c__3lu4b` int(11) DEFAULT NULL,\n  `c_mp6ko` double DEFAULT NULL,\n  `c_ndnhmc` double DEFAULT NULL,\n  `c_cdqetd` double DEFAULT NULL,\n  `c_ioru4c` double NOT NULL,\n  PRIMARY KEY (`c_ioru4c`) /*T![clustered_index] NONCLUSTERED */,\n  KEY `t_c1q7y` (`c_ymgvrd`,`c_ee5vqb`,`c_xsjoqb`,`c_mp6ko`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/07/01 15:13:02.246 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:108, Type:create table, State:none, SchemaState:queueing, SchemaID:105, TableID:107, RowCount:0, ArgLen:1, start time: 2024-07-01 15:13:02.245 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:13:02.246 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:108, Type:create table, State:none, SchemaState:queueing, SchemaID:105, TableID:107, RowCount:0, ArgLen:1, start time: 2024-07-01 15:13:02.245 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_berydd` (\n  `c_ymgvrd` int(11) DEFAULT NULL,\n  `c_ee5vqb` int(11) DEFAULT NULL,\n  `c_xsjoqb` int(11) DEFAULT NULL,\n  `c_xqizm` text DEFAULT NULL,\n  `c__3lu4b` int(11) DEFAULT NULL,\n  `c_mp6ko` double DEFAULT NULL,\n  `c_ndnhmc` double DEFAULT NULL,\n  `c_cdqetd` double DEFAULT NULL,\n  `c_ioru4c` double NOT NULL,\n  PRIMARY KEY (`c_ioru4c`) /*T![clustered_index] NONCLUSTERED */,\n  KEY `t_c1q7y` (`c_ymgvrd`,`c_ee5vqb`,`c_xsjoqb`,`c_mp6ko`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/01 15:13:02.247 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:108, Type:create table, State:none, SchemaState:queueing, SchemaID:105, TableID:107, RowCount:0, ArgLen:0, start time: 2024-07-01 15:13:02.245 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:13:02.249 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=83] [neededSchemaVersion=84] ["start time"=640.241µs] [phyTblIDs="[107]"] [actionTypes="[8]"]
   > [2024/07/01 15:13:02.251 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=84] ["take time"=2.267908ms] [job="ID:108, Type:create table, State:done, SchemaState:public, SchemaID:105, TableID:107, RowCount:0, ArgLen:1, start time: 2024-07-01 15:13:02.245 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:13:02.252 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:108, Type:create table, State:synced, SchemaState:public, SchemaID:105, TableID:107, RowCount:0, ArgLen:0, start time: 2024-07-01 15:13:02.245 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:13:02.254 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=108]
   > [2024/07/01 15:13:02.254 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:13:02.254 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=74] ["first split key"=74800000000000006b]
   > [2024/07/01 15:13:02.254 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=74] ["first at"=74800000000000006b] ["first new region left"="{Id:74 StartKey:7480000000000000ff6500000000000000f8 EndKey:7480000000000000ff6b00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:75 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/01 15:13:02.254 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[74]"]
   > [2024/07/01 15:13:02.254 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=33] [schemaVersion=84] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_berydd` DISABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/07/01 15:13:02.256 +00:00] [WARN] [2pc.go:1596] ["schemaLeaseChecker is not set for this transaction"] [sessionID=33] [startTS=450847514887716865] [commitTS=450847514887716866]
   > [2024/07/01 15:13:02.260 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=33] [schemaVersion=84] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_berydd` ENABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/07/01 15:13:02.260 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=33] [schemaVersion=84] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_kqoy4`\n--\n\nDROP TABLE IF EXISTS `t_kqoy4`;"] [user=root@127.0.0.1]
   > [2024/07/01 15:13:02.261 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=33] [schemaVersion=84] [cur_db=testdb] [sql="CREATE TABLE `t_kqoy4` (\n  `c_embscb` int(11) DEFAULT NULL,\n  `c_gi3pxb` text DEFAULT NULL,\n  `c_fif_7c` text DEFAULT NULL,\n  `c_scsjqb` double DEFAULT NULL,\n  `c_cxqb1` text DEFAULT NULL,\n  `c_w1ibr` int(11) DEFAULT NULL,\n  `c_0lknib` double DEFAULT NULL,\n  `c_qfdzbd` double NOT NULL,\n  `c_7kdcs` double DEFAULT NULL,\n  PRIMARY KEY (`c_qfdzbd`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/07/01 15:13:02.262 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:110, Type:create table, State:none, SchemaState:queueing, SchemaID:105, TableID:109, RowCount:0, ArgLen:1, start time: 2024-07-01 15:13:02.262 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:13:02.263 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:110, Type:create table, State:none, SchemaState:queueing, SchemaID:105, TableID:109, RowCount:0, ArgLen:1, start time: 2024-07-01 15:13:02.262 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_kqoy4` (\n  `c_embscb` int(11) DEFAULT NULL,\n  `c_gi3pxb` text DEFAULT NULL,\n  `c_fif_7c` text DEFAULT NULL,\n  `c_scsjqb` double DEFAULT NULL,\n  `c_cxqb1` text DEFAULT NULL,\n  `c_w1ibr` int(11) DEFAULT NULL,\n  `c_0lknib` double DEFAULT NULL,\n  `c_qfdzbd` double NOT NULL,\n  `c_7kdcs` double DEFAULT NULL,\n  PRIMARY KEY (`c_qfdzbd`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/01 15:13:02.263 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:110, Type:create table, State:none, SchemaState:queueing, SchemaID:105, TableID:109, RowCount:0, ArgLen:0, start time: 2024-07-01 15:13:02.262 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:13:02.266 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=84] [neededSchemaVersion=85] ["start time"=514.596µs] [phyTblIDs="[109]"] [actionTypes="[8]"]
   > [2024/07/01 15:13:02.267 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=85] ["take time"=2.290118ms] [job="ID:110, Type:create table, State:done, SchemaState:public, SchemaID:105, TableID:109, RowCount:0, ArgLen:1, start time: 2024-07-01 15:13:02.262 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:13:02.269 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:110, Type:create table, State:synced, SchemaState:public, SchemaID:105, TableID:109, RowCount:0, ArgLen:0, start time: 2024-07-01 15:13:02.262 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:13:02.270 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=110]
   > [2024/07/01 15:13:02.270 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:13:02.270 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=76] ["first split key"=74800000000000006d]
   > [2024/07/01 15:13:02.271 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=76] ["first at"=74800000000000006d] ["first new region left"="{Id:76 StartKey:7480000000000000ff6b00000000000000f8 EndKey:7480000000000000ff6d00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:77 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/01 15:13:02.271 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[76]"]
   > [2024/07/01 15:13:02.271 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=33] [schemaVersion=85] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_kqoy4` DISABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/07/01 15:13:02.272 +00:00] [WARN] [2pc.go:1596] ["schemaLeaseChecker is not set for this transaction"] [sessionID=33] [startTS=450847514891911169] [commitTS=450847514891911170]
   > [2024/07/01 15:13:02.274 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=33] [schemaVersion=85] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_kqoy4` ENABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/07/01 15:13:03.379 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=35] [user=root] [host=]

### Scenario 1
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
 * Instruction #1:
     - Instruction:  start transaction;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
 * Instruction #2:
     - Instruction:  update t_berydd set c_cdqetd = t_berydd.c_ioru4c;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
 * Instruction #3:
     - Instruction:  select count(c_mp6ko) from t_berydd;
     - Transaction: conn_0
     - Output: [(36,)]
     - Executed order: 3
 * Instruction #4:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4

 * Container logs:
   > [2024/07/01 15:13:05.738 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=39] [user=root] [host=]
   > [2024/07/01 15:13:05.742 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=39] [schemaVersion=93] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/07/01 15:13:05.743 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:117, Type:drop schema, State:none, SchemaState:queueing, SchemaID:112, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:13:05.742 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:13:05.743 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:117, Type:drop schema, State:none, SchemaState:queueing, SchemaID:112, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:13:05.742 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/01 15:13:05.743 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:117, Type:drop schema, State:none, SchemaState:queueing, SchemaID:112, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:13:05.742 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:13:05.744 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=93] [neededSchemaVersion=94] ["start time"=99.805µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:13:05.746 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=94] ["take time"=2.298639ms] [job="ID:117, Type:drop schema, State:running, SchemaState:write only, SchemaID:112, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:13:05.742 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:13:05.747 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:117, Type:drop schema, State:running, SchemaState:write only, SchemaID:112, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:13:05.742 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:13:05.748 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=94] [neededSchemaVersion=95] ["start time"=99.595µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:13:05.750 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=95] ["take time"=2.193736ms] [job="ID:117, Type:drop schema, State:running, SchemaState:delete only, SchemaID:112, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:13:05.742 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:13:05.750 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:117, Type:drop schema, State:running, SchemaState:delete only, SchemaID:112, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:13:05.742 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:13:05.751 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=95] [neededSchemaVersion=96] ["start time"=59.645µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:13:05.753 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=96] ["take time"=2.248283ms] [job="ID:117, Type:drop schema, State:done, SchemaState:queueing, SchemaID:112, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:13:05.742 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:13:05.754 +00:00] [INFO] [delete_range.go:107] ["[ddl] add job into delete-range table"] [jobID=117] [jobType="drop schema"]
   > [2024/07/01 15:13:05.754 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:117, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:112, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:13:05.742 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:13:05.755 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=117]
   > [2024/07/01 15:13:05.755 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:13:05.756 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=39] [schemaVersion=96] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/07/01 15:13:05.758 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:119, Type:create schema, State:none, SchemaState:queueing, SchemaID:118, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:13:05.757 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:13:05.758 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:119, Type:create schema, State:none, SchemaState:queueing, SchemaID:118, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:13:05.757 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/01 15:13:05.758 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:119, Type:create schema, State:none, SchemaState:queueing, SchemaID:118, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:13:05.757 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:13:05.760 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=96] [neededSchemaVersion=97] ["start time"=158.891µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:13:05.762 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=97] ["take time"=2.264626ms] [job="ID:119, Type:create schema, State:done, SchemaState:public, SchemaID:118, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:13:05.757 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:13:05.762 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:119, Type:create schema, State:synced, SchemaState:public, SchemaID:118, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:13:05.757 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:13:05.763 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=119]
   > [2024/07/01 15:13:05.763 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:13:05.769 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=39] [schemaVersion=97] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_berydd`\n--\n\nDROP TABLE IF EXISTS `t_berydd`;"] [user=root@127.0.0.1]
   > [2024/07/01 15:13:05.770 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=39] [schemaVersion=97] [cur_db=testdb] [sql="CREATE TABLE `t_berydd` (\n  `c_ymgvrd` int(11) DEFAULT NULL,\n  `c_ee5vqb` int(11) DEFAULT NULL,\n  `c_xsjoqb` int(11) DEFAULT NULL,\n  `c_xqizm` text DEFAULT NULL,\n  `c__3lu4b` int(11) DEFAULT NULL,\n  `c_mp6ko` double DEFAULT NULL,\n  `c_ndnhmc` double DEFAULT NULL,\n  `c_cdqetd` double DEFAULT NULL,\n  `c_ioru4c` double NOT NULL,\n  PRIMARY KEY (`c_ioru4c`) /*T![clustered_index] NONCLUSTERED */,\n  KEY `t_c1q7y` (`c_ymgvrd`,`c_ee5vqb`,`c_xsjoqb`,`c_mp6ko`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/07/01 15:13:05.772 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:121, Type:create table, State:none, SchemaState:queueing, SchemaID:118, TableID:120, RowCount:0, ArgLen:1, start time: 2024-07-01 15:13:05.771 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:13:05.772 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:121, Type:create table, State:none, SchemaState:queueing, SchemaID:118, TableID:120, RowCount:0, ArgLen:1, start time: 2024-07-01 15:13:05.771 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_berydd` (\n  `c_ymgvrd` int(11) DEFAULT NULL,\n  `c_ee5vqb` int(11) DEFAULT NULL,\n  `c_xsjoqb` int(11) DEFAULT NULL,\n  `c_xqizm` text DEFAULT NULL,\n  `c__3lu4b` int(11) DEFAULT NULL,\n  `c_mp6ko` double DEFAULT NULL,\n  `c_ndnhmc` double DEFAULT NULL,\n  `c_cdqetd` double DEFAULT NULL,\n  `c_ioru4c` double NOT NULL,\n  PRIMARY KEY (`c_ioru4c`) /*T![clustered_index] NONCLUSTERED */,\n  KEY `t_c1q7y` (`c_ymgvrd`,`c_ee5vqb`,`c_xsjoqb`,`c_mp6ko`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/01 15:13:05.772 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:121, Type:create table, State:none, SchemaState:queueing, SchemaID:118, TableID:120, RowCount:0, ArgLen:0, start time: 2024-07-01 15:13:05.771 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:13:05.775 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=97] [neededSchemaVersion=98] ["start time"=775.665µs] [phyTblIDs="[120]"] [actionTypes="[8]"]
   > [2024/07/01 15:13:05.777 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=98] ["take time"=2.274054ms] [job="ID:121, Type:create table, State:done, SchemaState:public, SchemaID:118, TableID:120, RowCount:0, ArgLen:1, start time: 2024-07-01 15:13:05.771 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:13:05.778 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:121, Type:create table, State:synced, SchemaState:public, SchemaID:118, TableID:120, RowCount:0, ArgLen:0, start time: 2024-07-01 15:13:05.771 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:13:05.780 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=121]
   > [2024/07/01 15:13:05.780 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:13:05.780 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=80] ["first split key"=748000000000000078]
   > [2024/07/01 15:13:05.781 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=80] ["first at"=748000000000000078] ["first new region left"="{Id:80 StartKey:7480000000000000ff7200000000000000f8 EndKey:7480000000000000ff7800000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:81 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/01 15:13:05.781 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[80]"]
   > [2024/07/01 15:13:05.781 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=39] [schemaVersion=98] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_berydd` DISABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/07/01 15:13:05.783 +00:00] [WARN] [2pc.go:1596] ["schemaLeaseChecker is not set for this transaction"] [sessionID=39] [startTS=450847515812036609] [commitTS=450847515812298752]
   > [2024/07/01 15:13:05.786 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=39] [schemaVersion=98] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_berydd` ENABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/07/01 15:13:05.786 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=39] [schemaVersion=98] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_kqoy4`\n--\n\nDROP TABLE IF EXISTS `t_kqoy4`;"] [user=root@127.0.0.1]
   > [2024/07/01 15:13:05.787 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=39] [schemaVersion=98] [cur_db=testdb] [sql="CREATE TABLE `t_kqoy4` (\n  `c_embscb` int(11) DEFAULT NULL,\n  `c_gi3pxb` text DEFAULT NULL,\n  `c_fif_7c` text DEFAULT NULL,\n  `c_scsjqb` double DEFAULT NULL,\n  `c_cxqb1` text DEFAULT NULL,\n  `c_w1ibr` int(11) DEFAULT NULL,\n  `c_0lknib` double DEFAULT NULL,\n  `c_qfdzbd` double NOT NULL,\n  `c_7kdcs` double DEFAULT NULL,\n  PRIMARY KEY (`c_qfdzbd`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/07/01 15:13:05.788 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:123, Type:create table, State:none, SchemaState:queueing, SchemaID:118, TableID:122, RowCount:0, ArgLen:1, start time: 2024-07-01 15:13:05.788 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:13:05.788 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:123, Type:create table, State:none, SchemaState:queueing, SchemaID:118, TableID:122, RowCount:0, ArgLen:1, start time: 2024-07-01 15:13:05.788 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_kqoy4` (\n  `c_embscb` int(11) DEFAULT NULL,\n  `c_gi3pxb` text DEFAULT NULL,\n  `c_fif_7c` text DEFAULT NULL,\n  `c_scsjqb` double DEFAULT NULL,\n  `c_cxqb1` text DEFAULT NULL,\n  `c_w1ibr` int(11) DEFAULT NULL,\n  `c_0lknib` double DEFAULT NULL,\n  `c_qfdzbd` double NOT NULL,\n  `c_7kdcs` double DEFAULT NULL,\n  PRIMARY KEY (`c_qfdzbd`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/01 15:13:05.789 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:123, Type:create table, State:none, SchemaState:queueing, SchemaID:118, TableID:122, RowCount:0, ArgLen:0, start time: 2024-07-01 15:13:05.788 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:13:05.792 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=98] [neededSchemaVersion=99] ["start time"=521.161µs] [phyTblIDs="[122]"] [actionTypes="[8]"]
   > [2024/07/01 15:13:05.793 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=99] ["take time"=2.272867ms] [job="ID:123, Type:create table, State:done, SchemaState:public, SchemaID:118, TableID:122, RowCount:0, ArgLen:1, start time: 2024-07-01 15:13:05.788 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:13:05.794 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:123, Type:create table, State:synced, SchemaState:public, SchemaID:118, TableID:122, RowCount:0, ArgLen:0, start time: 2024-07-01 15:13:05.788 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:13:05.796 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=123]
   > [2024/07/01 15:13:05.796 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:13:05.796 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=82] ["first split key"=74800000000000007a]
   > [2024/07/01 15:13:05.797 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=82] ["first at"=74800000000000007a] ["first new region left"="{Id:82 StartKey:7480000000000000ff7800000000000000f8 EndKey:7480000000000000ff7a00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:83 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/01 15:13:05.797 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[82]"]
   > [2024/07/01 15:13:05.797 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=39] [schemaVersion=99] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_kqoy4` DISABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/07/01 15:13:05.798 +00:00] [WARN] [2pc.go:1596] ["schemaLeaseChecker is not set for this transaction"] [sessionID=39] [startTS=450847515816230913] [commitTS=450847515816230914]
   > [2024/07/01 15:13:05.800 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=39] [schemaVersion=99] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_kqoy4` ENABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/07/01 15:13:06.865 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=41] [user=root] [host=]
   > [2024/07/01 15:13:06.888 +00:00] [INFO] [set.go:139] ["set global var"] [conn=41] [name=tx_isolation] [val=READ-COMMITTED]
