# Bug ID TIDB-36903-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/36903
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ


## Details
 * Database: tidb-v6.1.0
 * Number of scenarios: 2
 * Initial setup script: /home/theodor/Projects/MasterThesis/data/sql/TIDB-36903_mysql_bk.sql

## Results
### Scenario 0
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  insert into t_vwvgdc (wkey, pkey, c_rdsfbc) values (155, 228000, 99.50);
     - TID: 0
     - Output: None
 * Instruction #2:
     - SQL:  select ref_4.pkey as c0 from t_vwvgdc as ref_4 where 0 <> 0 union select ref_5....
     - TID: 0
     - Output: [(26000,), (38000,), (71000,), (68000,), (70000,), (228000,), (18000,), (42000,), (19000,), (74000,), (20000,), (66000,), (15000,), (17000,), (21000,), (16000,), (62000,), (37000,), (67000,), (63000,), (39000,), (65000,), (25000,), (27000,), (69000,), (73000,), (41000,), (64000,), (40000,), (72000,)]

 * Container logs:
   > [2024/06/19 09:30:37.729 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/06/19 09:30:37.733 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=32] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/06/19 09:30:37.734 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=32] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/06/19 09:30:37.736 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:66, Type:create schema, State:none, SchemaState:queueing, SchemaID:65, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 09:30:37.735 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/19 09:30:37.736 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:66, Type:create schema, State:none, SchemaState:queueing, SchemaID:65, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 09:30:37.735 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/19 09:30:37.736 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:create schema, State:none, SchemaState:queueing, SchemaID:65, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:37.735 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:37.737 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=32] [neededSchemaVersion=33] ["start time"=144.014µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 09:30:37.739 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=33] ["take time"=2.224119ms] [job="ID:66, Type:create schema, State:done, SchemaState:public, SchemaID:65, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 09:30:37.735 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:37.740 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:create schema, State:synced, SchemaState:public, SchemaID:65, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:37.735 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:37.740 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=66]
   > [2024/06/19 09:30:37.740 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/19 09:30:37.746 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=33] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_5mspyb`\n--\n\nDROP TABLE IF EXISTS `t_5mspyb`;"] [user=root@%]
   > [2024/06/19 09:30:37.747 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=33] [cur_db=testdb] [sql="CREATE TABLE `t_5mspyb` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_dugmmc` int(11) DEFAULT NULL,\n  `c_q0rdv` text DEFAULT NULL,\n  `c_0bhxq` int(11) DEFAULT NULL,\n  `c_qpz_v` text DEFAULT NULL,\n  `c_rgl8pc` double DEFAULT NULL,\n  `c_yisj0d` int(11) DEFAULT NULL,\n  `c_n9hfnb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/06/19 09:30:37.749 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:68, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:67, RowCount:0, ArgLen:1, start time: 2024-06-19 09:30:37.748 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/19 09:30:37.749 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:68, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:67, RowCount:0, ArgLen:1, start time: 2024-06-19 09:30:37.748 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_5mspyb` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_dugmmc` int(11) DEFAULT NULL,\n  `c_q0rdv` text DEFAULT NULL,\n  `c_0bhxq` int(11) DEFAULT NULL,\n  `c_qpz_v` text DEFAULT NULL,\n  `c_rgl8pc` double DEFAULT NULL,\n  `c_yisj0d` int(11) DEFAULT NULL,\n  `c_n9hfnb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/19 09:30:37.749 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:68, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:67, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:37.748 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:37.752 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=33] [neededSchemaVersion=34] ["start time"=514.806µs] [phyTblIDs="[67]"] [actionTypes="[8]"]
   > [2024/06/19 09:30:37.753 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=34] ["take time"=2.115794ms] [job="ID:68, Type:create table, State:done, SchemaState:public, SchemaID:65, TableID:67, RowCount:0, ArgLen:1, start time: 2024-06-19 09:30:37.748 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:37.754 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:68, Type:create table, State:synced, SchemaState:public, SchemaID:65, TableID:67, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:37.748 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:37.755 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=68]
   > [2024/06/19 09:30:37.755 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/19 09:30:37.756 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=60] ["first split key"=748000000000000043]
   > [2024/06/19 09:30:37.756 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=34] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_5mspyb` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:30:37.758 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=34] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_5mspyb` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:30:37.758 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=62] ["first at"=748000000000000043] ["first new region left"="{Id:62 StartKey:7480000000000000ff3f00000000000000f8 EndKey:7480000000000000ff4300000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:63 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/19 09:30:37.759 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[62]"]
   > [2024/06/19 09:30:37.759 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=34] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_vwvgdc`\n--\n\nDROP TABLE IF EXISTS `t_vwvgdc`;"] [user=root@%]
   > [2024/06/19 09:30:37.759 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=34] [cur_db=testdb] [sql="CREATE TABLE `t_vwvgdc` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_rdsfbc` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_8dsy1c` (`wkey`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/06/19 09:30:37.761 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:70, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:69, RowCount:0, ArgLen:1, start time: 2024-06-19 09:30:37.76 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/19 09:30:37.761 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:70, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:69, RowCount:0, ArgLen:1, start time: 2024-06-19 09:30:37.76 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_vwvgdc` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_rdsfbc` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_8dsy1c` (`wkey`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/19 09:30:37.761 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:70, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:69, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:37.76 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:37.763 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=34] [neededSchemaVersion=35] ["start time"=338.105µs] [phyTblIDs="[69]"] [actionTypes="[8]"]
   > [2024/06/19 09:30:37.765 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=35] ["take time"=2.048186ms] [job="ID:70, Type:create table, State:done, SchemaState:public, SchemaID:65, TableID:69, RowCount:0, ArgLen:1, start time: 2024-06-19 09:30:37.76 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:37.765 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:70, Type:create table, State:synced, SchemaState:public, SchemaID:65, TableID:69, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:37.76 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:37.766 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=70]
   > [2024/06/19 09:30:37.767 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/19 09:30:37.767 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=62] ["first split key"=748000000000000045]
   > [2024/06/19 09:30:37.767 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=35] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_vwvgdc` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:30:37.769 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=64] ["first at"=748000000000000045] ["first new region left"="{Id:64 StartKey:7480000000000000ff4300000000000000f8 EndKey:7480000000000000ff4500000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:65 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/19 09:30:37.770 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[64]"]
   > [2024/06/19 09:30:37.770 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=35] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_vwvgdc` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:30:38.802 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/06/19 09:30:38.814 +00:00] [INFO] [set.go:147] ["set global var"] [conn=407] [name=tx_isolation] [val=REPEATABLE-READ]

### Scenario 1
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
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
   > [2024/06/19 09:30:41.145 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/06/19 09:30:41.148 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=43] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/06/19 09:30:41.148 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:77, Type:drop schema, State:none, SchemaState:queueing, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:41.148 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/19 09:30:41.149 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:77, Type:drop schema, State:none, SchemaState:queueing, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:41.148 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/06/19 09:30:41.149 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:none, SchemaState:queueing, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:41.148 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:41.150 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=43] [neededSchemaVersion=44] ["start time"=63.626µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 09:30:41.152 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=44] ["take time"=2.241859ms] [job="ID:77, Type:drop schema, State:running, SchemaState:write only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:41.148 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:41.152 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:running, SchemaState:write only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:41.148 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:41.153 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=44] [neededSchemaVersion=45] ["start time"=102.459µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 09:30:41.155 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=45] ["take time"=2.290957ms] [job="ID:77, Type:drop schema, State:running, SchemaState:delete only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:41.148 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:41.155 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:running, SchemaState:delete only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:41.148 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:41.156 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=45] [neededSchemaVersion=46] ["start time"=81.436µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 09:30:41.158 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=46] ["take time"=2.369111ms] [job="ID:77, Type:drop schema, State:done, SchemaState:queueing, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:41.148 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:41.159 +00:00] [INFO] [delete_range.go:103] ["[ddl] add job into delete-range table"] [jobID=77] [jobType="drop schema"]
   > [2024/06/19 09:30:41.159 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:41.148 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:41.160 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=77]
   > [2024/06/19 09:30:41.160 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/19 09:30:41.162 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=46] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/06/19 09:30:41.163 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:79, Type:create schema, State:none, SchemaState:queueing, SchemaID:78, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 09:30:41.162 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/19 09:30:41.163 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:79, Type:create schema, State:none, SchemaState:queueing, SchemaID:78, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 09:30:41.162 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/19 09:30:41.164 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:79, Type:create schema, State:none, SchemaState:queueing, SchemaID:78, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:41.162 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:41.165 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=46] [neededSchemaVersion=47] ["start time"=144.294µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 09:30:41.167 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=47] ["take time"=2.269167ms] [job="ID:79, Type:create schema, State:done, SchemaState:public, SchemaID:78, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 09:30:41.162 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:41.167 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:79, Type:create schema, State:synced, SchemaState:public, SchemaID:78, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:41.162 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:41.168 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=79]
   > [2024/06/19 09:30:41.168 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/19 09:30:41.175 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=47] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_5mspyb`\n--\n\nDROP TABLE IF EXISTS `t_5mspyb`;"] [user=root@%]
   > [2024/06/19 09:30:41.176 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=47] [cur_db=testdb] [sql="CREATE TABLE `t_5mspyb` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_dugmmc` int(11) DEFAULT NULL,\n  `c_q0rdv` text DEFAULT NULL,\n  `c_0bhxq` int(11) DEFAULT NULL,\n  `c_qpz_v` text DEFAULT NULL,\n  `c_rgl8pc` double DEFAULT NULL,\n  `c_yisj0d` int(11) DEFAULT NULL,\n  `c_n9hfnb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/06/19 09:30:41.178 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:81, Type:create table, State:none, SchemaState:queueing, SchemaID:78, TableID:80, RowCount:0, ArgLen:1, start time: 2024-06-19 09:30:41.177 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/19 09:30:41.178 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:81, Type:create table, State:none, SchemaState:queueing, SchemaID:78, TableID:80, RowCount:0, ArgLen:1, start time: 2024-06-19 09:30:41.177 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_5mspyb` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_dugmmc` int(11) DEFAULT NULL,\n  `c_q0rdv` text DEFAULT NULL,\n  `c_0bhxq` int(11) DEFAULT NULL,\n  `c_qpz_v` text DEFAULT NULL,\n  `c_rgl8pc` double DEFAULT NULL,\n  `c_yisj0d` int(11) DEFAULT NULL,\n  `c_n9hfnb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/19 09:30:41.178 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:81, Type:create table, State:none, SchemaState:queueing, SchemaID:78, TableID:80, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:41.177 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:41.181 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=47] [neededSchemaVersion=48] ["start time"=701.423µs] [phyTblIDs="[80]"] [actionTypes="[8]"]
   > [2024/06/19 09:30:41.183 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=48] ["take time"=2.304786ms] [job="ID:81, Type:create table, State:done, SchemaState:public, SchemaID:78, TableID:80, RowCount:0, ArgLen:1, start time: 2024-06-19 09:30:41.177 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:41.184 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:81, Type:create table, State:synced, SchemaState:public, SchemaID:78, TableID:80, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:41.177 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:41.185 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=81]
   > [2024/06/19 09:30:41.185 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/19 09:30:41.186 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=68] ["first split key"=748000000000000050]
   > [2024/06/19 09:30:41.186 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=68] ["first at"=748000000000000050] ["first new region left"="{Id:68 StartKey:7480000000000000ff4a00000000000000f8 EndKey:7480000000000000ff5000000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:69 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/19 09:30:41.186 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[68]"]
   > [2024/06/19 09:30:41.187 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=48] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_5mspyb` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:30:41.191 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=48] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_5mspyb` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:30:41.192 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=48] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_vwvgdc`\n--\n\nDROP TABLE IF EXISTS `t_vwvgdc`;"] [user=root@%]
   > [2024/06/19 09:30:41.193 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=48] [cur_db=testdb] [sql="CREATE TABLE `t_vwvgdc` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_rdsfbc` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_8dsy1c` (`wkey`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/06/19 09:30:41.194 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:83, Type:create table, State:none, SchemaState:queueing, SchemaID:78, TableID:82, RowCount:0, ArgLen:1, start time: 2024-06-19 09:30:41.193 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/19 09:30:41.194 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:83, Type:create table, State:none, SchemaState:queueing, SchemaID:78, TableID:82, RowCount:0, ArgLen:1, start time: 2024-06-19 09:30:41.193 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_vwvgdc` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_rdsfbc` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_8dsy1c` (`wkey`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/19 09:30:41.195 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:83, Type:create table, State:none, SchemaState:queueing, SchemaID:78, TableID:82, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:41.193 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:41.197 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=48] [neededSchemaVersion=49] ["start time"=416.747µs] [phyTblIDs="[82]"] [actionTypes="[8]"]
   > [2024/06/19 09:30:41.199 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=49] ["take time"=2.12641ms] [job="ID:83, Type:create table, State:done, SchemaState:public, SchemaID:78, TableID:82, RowCount:0, ArgLen:1, start time: 2024-06-19 09:30:41.193 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:41.200 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:83, Type:create table, State:synced, SchemaState:public, SchemaID:78, TableID:82, RowCount:0, ArgLen:0, start time: 2024-06-19 09:30:41.193 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:30:41.201 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=83]
   > [2024/06/19 09:30:41.201 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/19 09:30:41.201 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=70] ["first split key"=748000000000000052]
   > [2024/06/19 09:30:41.202 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=49] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_vwvgdc` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:30:41.202 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=70] ["first at"=748000000000000052] ["first new region left"="{Id:70 StartKey:7480000000000000ff5000000000000000f8 EndKey:7480000000000000ff5200000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:71 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/19 09:30:41.202 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[70]"]
   > [2024/06/19 09:30:41.205 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=49] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_vwvgdc` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:30:42.230 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/06/19 09:30:42.245 +00:00] [INFO] [set.go:147] ["set global var"] [conn=413] [name=tx_isolation] [val=REPEATABLE-READ]
