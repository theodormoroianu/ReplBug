# Bug ID TIDB-30397-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/30397
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ


## Details
 * Database: tidb-5.4.0
 * Number of scenarios: 2
 * Initial setup script: /home/theodor/Projects/MasterThesis/data/sql/TIDB-30397_mysql_bk.sql

## Results
### Scenario 0
 * Instruction #0:
     - SQL:  update t_berydd set c_cdqetd = t_berydd.c_ioru4c;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  select count(c_mp6ko) from t_berydd;
     - TID: 0
     - Output: [(39,)]

 * Container logs:
   > [2024/06/18 11:59:09.981 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=30] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/06/18 11:59:09.982 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=30] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/06/18 11:59:09.984 +00:00] [INFO] [ddl_worker.go:322] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:62, Type:create schema, State:none, SchemaState:queueing, SchemaID:61, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 11:59:09.983 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 11:59:09.984 +00:00] [INFO] [ddl.go:571] ["[ddl] start DDL job"] [job="ID:62, Type:create schema, State:none, SchemaState:queueing, SchemaID:61, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 11:59:09.983 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/18 11:59:09.984 +00:00] [INFO] [ddl_worker.go:729] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:62, Type:create schema, State:none, SchemaState:queueing, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:59:09.983 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:59:09.985 +00:00] [INFO] [domain.go:138] ["diff load InfoSchema success"] [currentSchemaVersion=30] [neededSchemaVersion=31] ["start time"=98.477µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 11:59:09.987 +00:00] [INFO] [ddl_worker.go:932] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=31] ["take time"=2.24144ms] [job="ID:62, Type:create schema, State:done, SchemaState:public, SchemaID:61, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 11:59:09.983 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:59:09.988 +00:00] [INFO] [ddl_worker.go:428] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:62, Type:create schema, State:synced, SchemaState:public, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:59:09.983 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:59:09.988 +00:00] [INFO] [ddl.go:634] ["[ddl] DDL job is finished"] [jobID=62]
   > [2024/06/18 11:59:09.988 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 11:59:10.001 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=31] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_berydd`\n--\n\nDROP TABLE IF EXISTS `t_berydd`;"] [user=root@%]
   > [2024/06/18 11:59:10.002 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=31] [cur_db=testdb] [sql="CREATE TABLE `t_berydd` (\n  `c_ymgvrd` int(11) DEFAULT NULL,\n  `c_ee5vqb` int(11) DEFAULT NULL,\n  `c_xsjoqb` int(11) DEFAULT NULL,\n  `c_xqizm` text DEFAULT NULL,\n  `c__3lu4b` int(11) DEFAULT NULL,\n  `c_mp6ko` double DEFAULT NULL,\n  `c_ndnhmc` double DEFAULT NULL,\n  `c_cdqetd` double DEFAULT NULL,\n  `c_ioru4c` double NOT NULL,\n  PRIMARY KEY (`c_ioru4c`) /*T![clustered_index] NONCLUSTERED */,\n  KEY `t_c1q7y` (`c_ymgvrd`,`c_ee5vqb`,`c_xsjoqb`,`c_mp6ko`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/06/18 11:59:10.003 +00:00] [INFO] [ddl_worker.go:322] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:64, Type:create table, State:none, SchemaState:queueing, SchemaID:61, TableID:63, RowCount:0, ArgLen:1, start time: 2024-06-18 11:59:10.002 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 11:59:10.003 +00:00] [INFO] [ddl.go:571] ["[ddl] start DDL job"] [job="ID:64, Type:create table, State:none, SchemaState:queueing, SchemaID:61, TableID:63, RowCount:0, ArgLen:1, start time: 2024-06-18 11:59:10.002 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_berydd` (\n  `c_ymgvrd` int(11) DEFAULT NULL,\n  `c_ee5vqb` int(11) DEFAULT NULL,\n  `c_xsjoqb` int(11) DEFAULT NULL,\n  `c_xqizm` text DEFAULT NULL,\n  `c__3lu4b` int(11) DEFAULT NULL,\n  `c_mp6ko` double DEFAULT NULL,\n  `c_ndnhmc` double DEFAULT NULL,\n  `c_cdqetd` double DEFAULT NULL,\n  `c_ioru4c` double NOT NULL,\n  PRIMARY KEY (`c_ioru4c`) /*T![clustered_index] NONCLUSTERED */,\n  KEY `t_c1q7y` (`c_ymgvrd`,`c_ee5vqb`,`c_xsjoqb`,`c_mp6ko`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/18 11:59:10.004 +00:00] [INFO] [ddl_worker.go:729] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:64, Type:create table, State:none, SchemaState:queueing, SchemaID:61, TableID:63, RowCount:0, ArgLen:0, start time: 2024-06-18 11:59:10.002 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:59:10.006 +00:00] [INFO] [domain.go:138] ["diff load InfoSchema success"] [currentSchemaVersion=31] [neededSchemaVersion=32] ["start time"=706.941µs] [phyTblIDs="[63]"] [actionTypes="[8]"]
   > [2024/06/18 11:59:10.008 +00:00] [INFO] [ddl_worker.go:932] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=32] ["take time"=2.311002ms] [job="ID:64, Type:create table, State:done, SchemaState:public, SchemaID:61, TableID:63, RowCount:0, ArgLen:1, start time: 2024-06-18 11:59:10.002 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:59:10.010 +00:00] [INFO] [ddl_worker.go:428] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:64, Type:create table, State:synced, SchemaState:public, SchemaID:61, TableID:63, RowCount:0, ArgLen:0, start time: 2024-06-18 11:59:10.002 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:59:10.012 +00:00] [INFO] [ddl.go:634] ["[ddl] DDL job is finished"] [jobID=64]
   > [2024/06/18 11:59:10.012 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 11:59:10.012 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=56] ["first split key"=74800000000000003f]
   > [2024/06/18 11:59:10.012 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=32] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_berydd` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/18 11:59:10.014 +00:00] [WARN] [2pc.go:1651] ["schemaLeaseChecker is not set for this transaction"] [sessionID=5] [startTS=450550025424470017] [commitTS=450550025424470018]
   > [2024/06/18 11:59:10.015 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=58] ["first at"=74800000000000003f] ["first new region left"="{Id:58 StartKey:7480000000000000ff3b00000000000000f8 EndKey:7480000000000000ff3f00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:59 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/18 11:59:10.015 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[58]"]
   > [2024/06/18 11:59:10.018 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=32] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_berydd` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/18 11:59:10.018 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=32] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_kqoy4`\n--\n\nDROP TABLE IF EXISTS `t_kqoy4`;"] [user=root@%]
   > [2024/06/18 11:59:10.019 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=32] [cur_db=testdb] [sql="CREATE TABLE `t_kqoy4` (\n  `c_embscb` int(11) DEFAULT NULL,\n  `c_gi3pxb` text DEFAULT NULL,\n  `c_fif_7c` text DEFAULT NULL,\n  `c_scsjqb` double DEFAULT NULL,\n  `c_cxqb1` text DEFAULT NULL,\n  `c_w1ibr` int(11) DEFAULT NULL,\n  `c_0lknib` double DEFAULT NULL,\n  `c_qfdzbd` double NOT NULL,\n  `c_7kdcs` double DEFAULT NULL,\n  PRIMARY KEY (`c_qfdzbd`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/06/18 11:59:10.021 +00:00] [INFO] [ddl_worker.go:322] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:66, Type:create table, State:none, SchemaState:queueing, SchemaID:61, TableID:65, RowCount:0, ArgLen:1, start time: 2024-06-18 11:59:10.02 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 11:59:10.021 +00:00] [INFO] [ddl.go:571] ["[ddl] start DDL job"] [job="ID:66, Type:create table, State:none, SchemaState:queueing, SchemaID:61, TableID:65, RowCount:0, ArgLen:1, start time: 2024-06-18 11:59:10.02 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_kqoy4` (\n  `c_embscb` int(11) DEFAULT NULL,\n  `c_gi3pxb` text DEFAULT NULL,\n  `c_fif_7c` text DEFAULT NULL,\n  `c_scsjqb` double DEFAULT NULL,\n  `c_cxqb1` text DEFAULT NULL,\n  `c_w1ibr` int(11) DEFAULT NULL,\n  `c_0lknib` double DEFAULT NULL,\n  `c_qfdzbd` double NOT NULL,\n  `c_7kdcs` double DEFAULT NULL,\n  PRIMARY KEY (`c_qfdzbd`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/18 11:59:10.022 +00:00] [INFO] [ddl_worker.go:729] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:create table, State:none, SchemaState:queueing, SchemaID:61, TableID:65, RowCount:0, ArgLen:0, start time: 2024-06-18 11:59:10.02 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:59:10.024 +00:00] [INFO] [domain.go:138] ["diff load InfoSchema success"] [currentSchemaVersion=32] [neededSchemaVersion=33] ["start time"=565.79µs] [phyTblIDs="[65]"] [actionTypes="[8]"]
   > [2024/06/18 11:59:10.026 +00:00] [INFO] [ddl_worker.go:932] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=33] ["take time"=2.226493ms] [job="ID:66, Type:create table, State:done, SchemaState:public, SchemaID:61, TableID:65, RowCount:0, ArgLen:1, start time: 2024-06-18 11:59:10.02 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:59:10.027 +00:00] [INFO] [ddl_worker.go:428] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:create table, State:synced, SchemaState:public, SchemaID:61, TableID:65, RowCount:0, ArgLen:0, start time: 2024-06-18 11:59:10.02 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:59:10.029 +00:00] [INFO] [ddl.go:634] ["[ddl] DDL job is finished"] [jobID=66]
   > [2024/06/18 11:59:10.029 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 11:59:10.029 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=60] ["first split key"=748000000000000041]
   > [2024/06/18 11:59:10.029 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=60] ["first at"=748000000000000041] ["first new region left"="{Id:60 StartKey:7480000000000000ff3f00000000000000f8 EndKey:7480000000000000ff4100000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:61 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/18 11:59:10.029 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[60]"]
   > [2024/06/18 11:59:10.029 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=33] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_kqoy4` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/18 11:59:10.031 +00:00] [WARN] [2pc.go:1651] ["schemaLeaseChecker is not set for this transaction"] [sessionID=5] [startTS=450550025428664322] [commitTS=450550025428926464]
   > [2024/06/18 11:59:10.033 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=33] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_kqoy4` ENABLE KEYS */;"] [user=root@%]

### Scenario 1
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  start transaction;
     - TID: 0
     - Output: None
 * Instruction #2:
     - SQL:  update t_berydd set c_cdqetd = t_berydd.c_ioru4c;
     - TID: 0
     - Output: None
 * Instruction #3:
     - SQL:  select count(c_mp6ko) from t_berydd;
     - TID: 0
     - Output: [(36,)]
 * Instruction #4:
     - SQL:  commit;
     - TID: 0
     - Output: None

 * Container logs:
   > [2024/06/18 11:59:13.073 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=41] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/06/18 11:59:13.074 +00:00] [INFO] [ddl_worker.go:322] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:73, Type:drop schema, State:none, SchemaState:queueing, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:59:13.073 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 11:59:13.074 +00:00] [INFO] [ddl.go:571] ["[ddl] start DDL job"] [job="ID:73, Type:drop schema, State:none, SchemaState:queueing, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:59:13.073 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/06/18 11:59:13.074 +00:00] [INFO] [ddl_worker.go:729] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:73, Type:drop schema, State:none, SchemaState:queueing, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:59:13.073 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:59:13.075 +00:00] [INFO] [domain.go:138] ["diff load InfoSchema success"] [currentSchemaVersion=41] [neededSchemaVersion=42] ["start time"=91.772µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 11:59:13.078 +00:00] [INFO] [ddl_worker.go:932] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=42] ["take time"=2.275243ms] [job="ID:73, Type:drop schema, State:running, SchemaState:write only, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:59:13.073 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:59:13.078 +00:00] [INFO] [ddl_worker.go:729] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:73, Type:drop schema, State:running, SchemaState:write only, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:59:13.073 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:59:13.079 +00:00] [INFO] [domain.go:138] ["diff load InfoSchema success"] [currentSchemaVersion=42] [neededSchemaVersion=43] ["start time"=78.851µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 11:59:13.081 +00:00] [INFO] [ddl_worker.go:932] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=43] ["take time"=2.215458ms] [job="ID:73, Type:drop schema, State:running, SchemaState:delete only, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:59:13.073 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:59:13.081 +00:00] [INFO] [ddl_worker.go:729] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:73, Type:drop schema, State:running, SchemaState:delete only, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:59:13.073 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:59:13.082 +00:00] [INFO] [domain.go:138] ["diff load InfoSchema success"] [currentSchemaVersion=43] [neededSchemaVersion=44] ["start time"=84.509µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 11:59:13.084 +00:00] [INFO] [ddl_worker.go:932] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=44] ["take time"=2.455086ms] [job="ID:73, Type:drop schema, State:done, SchemaState:queueing, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:59:13.073 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:59:13.085 +00:00] [INFO] [delete_range.go:107] ["[ddl] add job into delete-range table"] [jobID=73] [jobType="drop schema"]
   > [2024/06/18 11:59:13.085 +00:00] [INFO] [ddl_worker.go:428] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:73, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:59:13.073 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:59:13.086 +00:00] [INFO] [ddl.go:634] ["[ddl] DDL job is finished"] [jobID=73]
   > [2024/06/18 11:59:13.086 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 11:59:13.087 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=44] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/06/18 11:59:13.089 +00:00] [INFO] [ddl_worker.go:322] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:75, Type:create schema, State:none, SchemaState:queueing, SchemaID:74, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 11:59:13.088 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 11:59:13.089 +00:00] [INFO] [ddl.go:571] ["[ddl] start DDL job"] [job="ID:75, Type:create schema, State:none, SchemaState:queueing, SchemaID:74, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 11:59:13.088 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/18 11:59:13.089 +00:00] [INFO] [ddl_worker.go:729] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:75, Type:create schema, State:none, SchemaState:queueing, SchemaID:74, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:59:13.088 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:59:13.090 +00:00] [INFO] [domain.go:138] ["diff load InfoSchema success"] [currentSchemaVersion=44] [neededSchemaVersion=45] ["start time"=153.513µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 11:59:13.092 +00:00] [INFO] [ddl_worker.go:932] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=45] ["take time"=2.229217ms] [job="ID:75, Type:create schema, State:done, SchemaState:public, SchemaID:74, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 11:59:13.088 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:59:13.093 +00:00] [INFO] [ddl_worker.go:428] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:75, Type:create schema, State:synced, SchemaState:public, SchemaID:74, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:59:13.088 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:59:13.093 +00:00] [INFO] [ddl.go:634] ["[ddl] DDL job is finished"] [jobID=75]
   > [2024/06/18 11:59:13.093 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 11:59:13.097 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=45] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_berydd`\n--\n\nDROP TABLE IF EXISTS `t_berydd`;"] [user=root@%]
   > [2024/06/18 11:59:13.098 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=45] [cur_db=testdb] [sql="CREATE TABLE `t_berydd` (\n  `c_ymgvrd` int(11) DEFAULT NULL,\n  `c_ee5vqb` int(11) DEFAULT NULL,\n  `c_xsjoqb` int(11) DEFAULT NULL,\n  `c_xqizm` text DEFAULT NULL,\n  `c__3lu4b` int(11) DEFAULT NULL,\n  `c_mp6ko` double DEFAULT NULL,\n  `c_ndnhmc` double DEFAULT NULL,\n  `c_cdqetd` double DEFAULT NULL,\n  `c_ioru4c` double NOT NULL,\n  PRIMARY KEY (`c_ioru4c`) /*T![clustered_index] NONCLUSTERED */,\n  KEY `t_c1q7y` (`c_ymgvrd`,`c_ee5vqb`,`c_xsjoqb`,`c_mp6ko`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/06/18 11:59:13.099 +00:00] [INFO] [ddl_worker.go:322] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:77, Type:create table, State:none, SchemaState:queueing, SchemaID:74, TableID:76, RowCount:0, ArgLen:1, start time: 2024-06-18 11:59:13.098 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 11:59:13.099 +00:00] [INFO] [ddl.go:571] ["[ddl] start DDL job"] [job="ID:77, Type:create table, State:none, SchemaState:queueing, SchemaID:74, TableID:76, RowCount:0, ArgLen:1, start time: 2024-06-18 11:59:13.098 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_berydd` (\n  `c_ymgvrd` int(11) DEFAULT NULL,\n  `c_ee5vqb` int(11) DEFAULT NULL,\n  `c_xsjoqb` int(11) DEFAULT NULL,\n  `c_xqizm` text DEFAULT NULL,\n  `c__3lu4b` int(11) DEFAULT NULL,\n  `c_mp6ko` double DEFAULT NULL,\n  `c_ndnhmc` double DEFAULT NULL,\n  `c_cdqetd` double DEFAULT NULL,\n  `c_ioru4c` double NOT NULL,\n  PRIMARY KEY (`c_ioru4c`) /*T![clustered_index] NONCLUSTERED */,\n  KEY `t_c1q7y` (`c_ymgvrd`,`c_ee5vqb`,`c_xsjoqb`,`c_mp6ko`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/18 11:59:13.100 +00:00] [INFO] [ddl_worker.go:729] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:create table, State:none, SchemaState:queueing, SchemaID:74, TableID:76, RowCount:0, ArgLen:0, start time: 2024-06-18 11:59:13.098 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:59:13.102 +00:00] [INFO] [domain.go:138] ["diff load InfoSchema success"] [currentSchemaVersion=45] [neededSchemaVersion=46] ["start time"=743.957µs] [phyTblIDs="[76]"] [actionTypes="[8]"]
   > [2024/06/18 11:59:13.103 +00:00] [INFO] [ddl_worker.go:932] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=46] ["take time"=2.159934ms] [job="ID:77, Type:create table, State:done, SchemaState:public, SchemaID:74, TableID:76, RowCount:0, ArgLen:1, start time: 2024-06-18 11:59:13.098 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:59:13.105 +00:00] [INFO] [ddl_worker.go:428] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:create table, State:synced, SchemaState:public, SchemaID:74, TableID:76, RowCount:0, ArgLen:0, start time: 2024-06-18 11:59:13.098 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:59:13.106 +00:00] [INFO] [ddl.go:634] ["[ddl] DDL job is finished"] [jobID=77]
   > [2024/06/18 11:59:13.106 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 11:59:13.106 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=64] ["first split key"=74800000000000004c]
   > [2024/06/18 11:59:13.107 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=64] ["first at"=74800000000000004c] ["first new region left"="{Id:64 StartKey:7480000000000000ff4600000000000000f8 EndKey:7480000000000000ff4c00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:65 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/18 11:59:13.107 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[64]"]
   > [2024/06/18 11:59:13.107 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=46] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_berydd` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/18 11:59:13.108 +00:00] [WARN] [2pc.go:1651] ["schemaLeaseChecker is not set for this transaction"] [sessionID=11] [startTS=450550026235543553] [commitTS=450550026235543554]
   > [2024/06/18 11:59:13.112 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=46] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_berydd` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/18 11:59:13.113 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=46] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_kqoy4`\n--\n\nDROP TABLE IF EXISTS `t_kqoy4`;"] [user=root@%]
   > [2024/06/18 11:59:13.113 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=46] [cur_db=testdb] [sql="CREATE TABLE `t_kqoy4` (\n  `c_embscb` int(11) DEFAULT NULL,\n  `c_gi3pxb` text DEFAULT NULL,\n  `c_fif_7c` text DEFAULT NULL,\n  `c_scsjqb` double DEFAULT NULL,\n  `c_cxqb1` text DEFAULT NULL,\n  `c_w1ibr` int(11) DEFAULT NULL,\n  `c_0lknib` double DEFAULT NULL,\n  `c_qfdzbd` double NOT NULL,\n  `c_7kdcs` double DEFAULT NULL,\n  PRIMARY KEY (`c_qfdzbd`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/06/18 11:59:13.115 +00:00] [INFO] [ddl_worker.go:322] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:79, Type:create table, State:none, SchemaState:queueing, SchemaID:74, TableID:78, RowCount:0, ArgLen:1, start time: 2024-06-18 11:59:13.114 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 11:59:13.115 +00:00] [INFO] [ddl.go:571] ["[ddl] start DDL job"] [job="ID:79, Type:create table, State:none, SchemaState:queueing, SchemaID:74, TableID:78, RowCount:0, ArgLen:1, start time: 2024-06-18 11:59:13.114 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_kqoy4` (\n  `c_embscb` int(11) DEFAULT NULL,\n  `c_gi3pxb` text DEFAULT NULL,\n  `c_fif_7c` text DEFAULT NULL,\n  `c_scsjqb` double DEFAULT NULL,\n  `c_cxqb1` text DEFAULT NULL,\n  `c_w1ibr` int(11) DEFAULT NULL,\n  `c_0lknib` double DEFAULT NULL,\n  `c_qfdzbd` double NOT NULL,\n  `c_7kdcs` double DEFAULT NULL,\n  PRIMARY KEY (`c_qfdzbd`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/18 11:59:13.116 +00:00] [INFO] [ddl_worker.go:729] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:79, Type:create table, State:none, SchemaState:queueing, SchemaID:74, TableID:78, RowCount:0, ArgLen:0, start time: 2024-06-18 11:59:13.114 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:59:13.119 +00:00] [INFO] [domain.go:138] ["diff load InfoSchema success"] [currentSchemaVersion=46] [neededSchemaVersion=47] ["start time"=588.419µs] [phyTblIDs="[78]"] [actionTypes="[8]"]
   > [2024/06/18 11:59:13.121 +00:00] [INFO] [ddl_worker.go:932] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=47] ["take time"=2.501461ms] [job="ID:79, Type:create table, State:done, SchemaState:public, SchemaID:74, TableID:78, RowCount:0, ArgLen:1, start time: 2024-06-18 11:59:13.114 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:59:13.122 +00:00] [INFO] [ddl_worker.go:428] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:79, Type:create table, State:synced, SchemaState:public, SchemaID:74, TableID:78, RowCount:0, ArgLen:0, start time: 2024-06-18 11:59:13.114 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:59:13.123 +00:00] [INFO] [ddl.go:634] ["[ddl] DDL job is finished"] [jobID=79]
   > [2024/06/18 11:59:13.123 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 11:59:13.123 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=66] ["first split key"=74800000000000004e]
   > [2024/06/18 11:59:13.124 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=66] ["first at"=74800000000000004e] ["first new region left"="{Id:66 StartKey:7480000000000000ff4c00000000000000f8 EndKey:7480000000000000ff4e00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:67 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/18 11:59:13.124 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[66]"]
   > [2024/06/18 11:59:13.124 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=47] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_kqoy4` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/18 11:59:13.125 +00:00] [WARN] [2pc.go:1651] ["schemaLeaseChecker is not set for this transaction"] [sessionID=11] [startTS=450550026240000001] [commitTS=450550026240000002]
   > [2024/06/18 11:59:13.128 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=47] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_kqoy4` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/18 11:59:14.173 +00:00] [INFO] [set.go:139] ["set global var"] [conn=13] [name=tx_isolation] [val=REPEATABLE-READ]
