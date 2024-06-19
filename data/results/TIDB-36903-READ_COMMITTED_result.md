# Bug ID TIDB-36903-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/36903
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED


## Details
 * Database: tidb-v6.1.0
 * Number of scenarios: 2
 * Initial setup script: /home/theodor/Projects/MasterThesis/data/sql/TIDB-36903_mysql_bk.sql

## Results
### Scenario 0
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  insert into t_vwvgdc (wkey, pkey, c_rdsfbc) values (155, 228000, 99.50);
     - TID: 0
     - Output: None
 * Instruction #2:
     - SQL:  select ref_4.pkey as c0 from t_vwvgdc as ref_4 where 0 <> 0 union select ref_5....
     - TID: 0
     - Output: [(15000,), (17000,), (66000,), (67000,), (65000,), (21000,), (25000,), (37000,), (62000,), (39000,), (63000,), (16000,), (74000,), (20000,), (19000,), (64000,), (69000,), (73000,), (41000,), (72000,), (40000,), (27000,), (71000,), (26000,), (42000,), (38000,), (228000,), (70000,), (68000,), (18000,)]

 * Container logs:
   > [2024/06/19 09:30:45.254 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/06/19 09:30:45.258 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=417] [schemaVersion=57] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/06/19 09:30:45.260 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:90, Type:drop schema, State:none, SchemaState:queueing, SchemaID:85, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:45.259 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/19 09:30:45.260 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:90, Type:drop schema, State:none, SchemaState:queueing, SchemaID:85, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:45.259 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/06/19 09:30:45.260 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:90, Type:drop schema, State:none, SchemaState:queueing, SchemaID:85, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:45.259 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:45.261 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=57] [neededSchemaVersion=58] ["start time"=123.761µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 09:30:45.263 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=58] ["take time"=2.211548ms] [job="ID:90, Type:drop schema, State:running, SchemaState:write only, SchemaID:85, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:45.259 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:45.263 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:90, Type:drop schema, State:running, SchemaState:write only, SchemaID:85, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:45.259 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:45.265 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=58] [neededSchemaVersion=59] ["start time"=109.512µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 09:30:45.266 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=59] ["take time"=2.021787ms] [job="ID:90, Type:drop schema, State:running, SchemaState:delete only, SchemaID:85, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:45.259 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:45.267 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:90, Type:drop schema, State:running, SchemaState:delete only, SchemaID:85, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:45.259 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:45.268 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=59] [neededSchemaVersion=60] ["start time"=86.255µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 09:30:45.270 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=60] ["take time"=2.242138ms] [job="ID:90, Type:drop schema, State:done, SchemaState:queueing, SchemaID:85, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:45.259 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:45.270 +00:00] [INFO] [delete_range.go:103] ["[ddl] add job into delete-range table"] [jobID=90] [jobType="drop schema"]
   > [2024/06/19 09:30:45.271 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:90, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:85, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:45.259 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:45.272 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=90]
   > [2024/06/19 09:30:45.272 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/19 09:30:45.273 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=417] [schemaVersion=60] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/06/19 09:30:45.275 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:92, Type:create schema, State:none, SchemaState:queueing, SchemaID:91, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 09:30:45.274 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/19 09:30:45.275 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:92, Type:create schema, State:none, SchemaState:queueing, SchemaID:91, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 09:30:45.274 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/19 09:30:45.276 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:92, Type:create schema, State:none, SchemaState:queueing, SchemaID:91, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:45.274 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:45.277 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=60] [neededSchemaVersion=61] ["start time"=148.764µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 09:30:45.279 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=61] ["take time"=2.253243ms] [job="ID:92, Type:create schema, State:done, SchemaState:public, SchemaID:91, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 09:30:45.274 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:45.280 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:92, Type:create schema, State:synced, SchemaState:public, SchemaID:91, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:45.274 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:45.281 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=92]
   > [2024/06/19 09:30:45.281 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/19 09:30:45.288 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=417] [schemaVersion=61] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_5mspyb`\n--\n\nDROP TABLE IF EXISTS `t_5mspyb`;"] [user=root@%]
   > [2024/06/19 09:30:45.289 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=417] [schemaVersion=61] [cur_db=testdb] [sql="CREATE TABLE `t_5mspyb` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_dugmmc` int(11) DEFAULT NULL,\n  `c_q0rdv` text DEFAULT NULL,\n  `c_0bhxq` int(11) DEFAULT NULL,\n  `c_qpz_v` text DEFAULT NULL,\n  `c_rgl8pc` double DEFAULT NULL,\n  `c_yisj0d` int(11) DEFAULT NULL,\n  `c_n9hfnb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/06/19 09:30:45.291 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:94, Type:create table, State:none, SchemaState:queueing, SchemaID:91, TableID:93, RowCount:0, ArgLen:1, start time: 2024-06-19 09:30:45.29 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/19 09:30:45.291 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:94, Type:create table, State:none, SchemaState:queueing, SchemaID:91, TableID:93, RowCount:0, ArgLen:1, start time: 2024-06-19 09:30:45.29 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_5mspyb` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_dugmmc` int(11) DEFAULT NULL,\n  `c_q0rdv` text DEFAULT NULL,\n  `c_0bhxq` int(11) DEFAULT NULL,\n  `c_qpz_v` text DEFAULT NULL,\n  `c_rgl8pc` double DEFAULT NULL,\n  `c_yisj0d` int(11) DEFAULT NULL,\n  `c_n9hfnb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/19 09:30:45.292 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:94, Type:create table, State:none, SchemaState:queueing, SchemaID:91, TableID:93, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:45.29 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:45.295 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=61] [neededSchemaVersion=62] ["start time"=537.225µs] [phyTblIDs="[93]"] [actionTypes="[8]"]
   > [2024/06/19 09:30:45.297 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=62] ["take time"=2.301295ms] [job="ID:94, Type:create table, State:done, SchemaState:public, SchemaID:91, TableID:93, RowCount:0, ArgLen:1, start time: 2024-06-19 09:30:45.29 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:45.298 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:94, Type:create table, State:synced, SchemaState:public, SchemaID:91, TableID:93, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:45.29 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:45.300 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=94]
   > [2024/06/19 09:30:45.300 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/19 09:30:45.300 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=74] ["first split key"=74800000000000005d]
   > [2024/06/19 09:30:45.301 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=74] ["first at"=74800000000000005d] ["first new region left"="{Id:74 StartKey:7480000000000000ff5700000000000000f8 EndKey:7480000000000000ff5d00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:75 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/19 09:30:45.301 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[74]"]
   > [2024/06/19 09:30:45.301 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=417] [schemaVersion=62] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_5mspyb` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:30:45.306 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=417] [schemaVersion=62] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_5mspyb` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:30:45.307 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=417] [schemaVersion=62] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_vwvgdc`\n--\n\nDROP TABLE IF EXISTS `t_vwvgdc`;"] [user=root@%]
   > [2024/06/19 09:30:45.308 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=417] [schemaVersion=62] [cur_db=testdb] [sql="CREATE TABLE `t_vwvgdc` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_rdsfbc` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_8dsy1c` (`wkey`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/06/19 09:30:45.310 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:96, Type:create table, State:none, SchemaState:queueing, SchemaID:91, TableID:95, RowCount:0, ArgLen:1, start time: 2024-06-19 09:30:45.309 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/19 09:30:45.310 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:96, Type:create table, State:none, SchemaState:queueing, SchemaID:91, TableID:95, RowCount:0, ArgLen:1, start time: 2024-06-19 09:30:45.309 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_vwvgdc` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_rdsfbc` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_8dsy1c` (`wkey`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/19 09:30:45.311 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:96, Type:create table, State:none, SchemaState:queueing, SchemaID:91, TableID:95, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:45.309 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:45.313 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=62] [neededSchemaVersion=63] ["start time"=518.297µs] [phyTblIDs="[95]"] [actionTypes="[8]"]
   > [2024/06/19 09:30:45.315 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=63] ["take time"=2.080524ms] [job="ID:96, Type:create table, State:done, SchemaState:public, SchemaID:91, TableID:95, RowCount:0, ArgLen:1, start time: 2024-06-19 09:30:45.309 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:45.316 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:96, Type:create table, State:synced, SchemaState:public, SchemaID:91, TableID:95, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:45.309 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:45.317 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=96]
   > [2024/06/19 09:30:45.317 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/19 09:30:45.317 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=76] ["first split key"=74800000000000005f]
   > [2024/06/19 09:30:45.318 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=76] ["first at"=74800000000000005f] ["first new region left"="{Id:76 StartKey:7480000000000000ff5d00000000000000f8 EndKey:7480000000000000ff5f00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:77 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/19 09:30:45.318 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[76]"]
   > [2024/06/19 09:30:45.318 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=417] [schemaVersion=63] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_vwvgdc` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:30:45.322 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=417] [schemaVersion=63] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_vwvgdc` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:30:46.340 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/06/19 09:30:46.355 +00:00] [INFO] [set.go:147] ["set global var"] [conn=419] [name=tx_isolation] [val=READ-COMMITTED]

### Scenario 1
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  BEGIN OPTIMISTIC;
     - TID: 0
     - Output: None
 * Instruction #2:
     - SQL:  insert into t_vwvgdc (wkey, pkey, c_rdsfbc) values (155, 228000, 99.50);
     - TID: 0
     - Output: None
 * Instruction #3:
     - SQL:  select ref_4.pkey as c0 from t_vwvgdc as ref_4 where 0 <> 0 union select ref_5....
     - TID: 0
     - Output: []
 * Instruction #4:
     - SQL:  commit;
     - TID: 0
     - Output: None

 * Container logs:
   > [2024/06/19 09:30:48.838 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/06/19 09:30:48.841 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=423] [schemaVersion=71] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/06/19 09:30:48.842 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:103, Type:drop schema, State:none, SchemaState:queueing, SchemaID:98, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:48.841 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/19 09:30:48.842 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:103, Type:drop schema, State:none, SchemaState:queueing, SchemaID:98, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:48.841 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/06/19 09:30:48.842 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:103, Type:drop schema, State:none, SchemaState:queueing, SchemaID:98, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:48.841 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:48.843 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=71] [neededSchemaVersion=72] ["start time"=92.96µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 09:30:48.845 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=72] ["take time"=2.200023ms] [job="ID:103, Type:drop schema, State:running, SchemaState:write only, SchemaID:98, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:48.841 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:48.845 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:103, Type:drop schema, State:running, SchemaState:write only, SchemaID:98, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:48.841 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:48.846 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=72] [neededSchemaVersion=73] ["start time"=68.515µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 09:30:48.849 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=73] ["take time"=2.443074ms] [job="ID:103, Type:drop schema, State:running, SchemaState:delete only, SchemaID:98, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:48.841 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:48.849 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:103, Type:drop schema, State:running, SchemaState:delete only, SchemaID:98, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:48.841 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:48.850 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=73] [neededSchemaVersion=74] ["start time"=91.493µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 09:30:48.852 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=74] ["take time"=2.242138ms] [job="ID:103, Type:drop schema, State:done, SchemaState:queueing, SchemaID:98, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:48.841 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:48.852 +00:00] [INFO] [delete_range.go:103] ["[ddl] add job into delete-range table"] [jobID=103] [jobType="drop schema"]
   > [2024/06/19 09:30:48.852 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:103, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:98, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:48.841 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:48.853 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=103]
   > [2024/06/19 09:30:48.853 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/19 09:30:48.855 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=423] [schemaVersion=74] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/06/19 09:30:48.857 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:105, Type:create schema, State:none, SchemaState:queueing, SchemaID:104, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 09:30:48.856 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/19 09:30:48.857 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:105, Type:create schema, State:none, SchemaState:queueing, SchemaID:104, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 09:30:48.856 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/19 09:30:48.857 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:105, Type:create schema, State:none, SchemaState:queueing, SchemaID:104, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:48.856 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:48.858 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=74] [neededSchemaVersion=75] ["start time"=156.586µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 09:30:48.860 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=75] ["take time"=2.252544ms] [job="ID:105, Type:create schema, State:done, SchemaState:public, SchemaID:104, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 09:30:48.856 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:48.861 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:105, Type:create schema, State:synced, SchemaState:public, SchemaID:104, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:48.856 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:48.862 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=105]
   > [2024/06/19 09:30:48.862 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/19 09:30:48.869 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=423] [schemaVersion=75] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_5mspyb`\n--\n\nDROP TABLE IF EXISTS `t_5mspyb`;"] [user=root@%]
   > [2024/06/19 09:30:48.869 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=423] [schemaVersion=75] [cur_db=testdb] [sql="CREATE TABLE `t_5mspyb` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_dugmmc` int(11) DEFAULT NULL,\n  `c_q0rdv` text DEFAULT NULL,\n  `c_0bhxq` int(11) DEFAULT NULL,\n  `c_qpz_v` text DEFAULT NULL,\n  `c_rgl8pc` double DEFAULT NULL,\n  `c_yisj0d` int(11) DEFAULT NULL,\n  `c_n9hfnb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/06/19 09:30:48.871 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:107, Type:create table, State:none, SchemaState:queueing, SchemaID:104, TableID:106, RowCount:0, ArgLen:1, start time: 2024-06-19 09:30:48.87 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/19 09:30:48.872 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:107, Type:create table, State:none, SchemaState:queueing, SchemaID:104, TableID:106, RowCount:0, ArgLen:1, start time: 2024-06-19 09:30:48.87 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_5mspyb` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_dugmmc` int(11) DEFAULT NULL,\n  `c_q0rdv` text DEFAULT NULL,\n  `c_0bhxq` int(11) DEFAULT NULL,\n  `c_qpz_v` text DEFAULT NULL,\n  `c_rgl8pc` double DEFAULT NULL,\n  `c_yisj0d` int(11) DEFAULT NULL,\n  `c_n9hfnb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/19 09:30:48.872 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:107, Type:create table, State:none, SchemaState:queueing, SchemaID:104, TableID:106, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:48.87 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:48.875 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=75] [neededSchemaVersion=76] ["start time"=600.362µs] [phyTblIDs="[106]"] [actionTypes="[8]"]
   > [2024/06/19 09:30:48.877 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=76] ["take time"=2.270425ms] [job="ID:107, Type:create table, State:done, SchemaState:public, SchemaID:104, TableID:106, RowCount:0, ArgLen:1, start time: 2024-06-19 09:30:48.87 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:48.878 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:107, Type:create table, State:synced, SchemaState:public, SchemaID:104, TableID:106, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:48.87 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:48.880 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=107]
   > [2024/06/19 09:30:48.880 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/19 09:30:48.880 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=80] ["first split key"=74800000000000006a]
   > [2024/06/19 09:30:48.881 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=80] ["first at"=74800000000000006a] ["first new region left"="{Id:80 StartKey:7480000000000000ff6400000000000000f8 EndKey:7480000000000000ff6a00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:81 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/19 09:30:48.881 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[80]"]
   > [2024/06/19 09:30:48.881 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=423] [schemaVersion=76] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_5mspyb` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:30:48.885 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=423] [schemaVersion=76] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_5mspyb` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:30:48.886 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=423] [schemaVersion=76] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_vwvgdc`\n--\n\nDROP TABLE IF EXISTS `t_vwvgdc`;"] [user=root@%]
   > [2024/06/19 09:30:48.886 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=423] [schemaVersion=76] [cur_db=testdb] [sql="CREATE TABLE `t_vwvgdc` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_rdsfbc` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_8dsy1c` (`wkey`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/06/19 09:30:48.888 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:109, Type:create table, State:none, SchemaState:queueing, SchemaID:104, TableID:108, RowCount:0, ArgLen:1, start time: 2024-06-19 09:30:48.887 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/19 09:30:48.888 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:109, Type:create table, State:none, SchemaState:queueing, SchemaID:104, TableID:108, RowCount:0, ArgLen:1, start time: 2024-06-19 09:30:48.887 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_vwvgdc` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_rdsfbc` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_8dsy1c` (`wkey`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/19 09:30:48.889 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:109, Type:create table, State:none, SchemaState:queueing, SchemaID:104, TableID:108, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:48.887 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:48.890 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=76] [neededSchemaVersion=77] ["start time"=289.076µs] [phyTblIDs="[108]"] [actionTypes="[8]"]
   > [2024/06/19 09:30:48.892 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=77] ["take time"=2.043438ms] [job="ID:109, Type:create table, State:done, SchemaState:public, SchemaID:104, TableID:108, RowCount:0, ArgLen:1, start time: 2024-06-19 09:30:48.887 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:48.893 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:109, Type:create table, State:synced, SchemaState:public, SchemaID:104, TableID:108, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:48.887 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:48.894 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=109]
   > [2024/06/19 09:30:48.894 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/19 09:30:48.894 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=82] ["first split key"=74800000000000006c]
   > [2024/06/19 09:30:48.895 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=82] ["first at"=74800000000000006c] ["first new region left"="{Id:82 StartKey:7480000000000000ff6a00000000000000f8 EndKey:7480000000000000ff6c00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:83 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/19 09:30:48.895 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[82]"]
   > [2024/06/19 09:30:48.895 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=423] [schemaVersion=77] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_vwvgdc` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:30:48.898 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=423] [schemaVersion=77] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_vwvgdc` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:30:49.923 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/06/19 09:30:49.936 +00:00] [INFO] [set.go:147] ["set global var"] [conn=425] [name=tx_isolation] [val=READ-COMMITTED]
