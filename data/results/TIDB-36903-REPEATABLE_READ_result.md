# Bug ID TIDB-36903-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/36903
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              The two tests give a different result.


## Details
 * Database: tidb-v6.1.0
 * Number of scenarios: 2
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
 * Instruction #1:
     - Instruction:  insert into t_vwvgdc (wkey, pkey, c_rdsfbc) values (155, 228000, 99.50);
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
 * Instruction #2:
     - Instruction:  select ref_4.pkey as c0 from t_vwvgdc as ref_4 where 0 <> 0 union select ref_5....
     - Transaction: conn_0
     - Output: [(17000,), (15000,), (66000,), (74000,), (19000,), (20000,), (27000,), (73000,), (40000,), (41000,), (72000,), (69000,), (64000,), (39000,), (21000,), (63000,), (25000,), (67000,), (62000,), (37000,), (16000,), (65000,), (228000,), (18000,), (68000,), (70000,), (26000,), (38000,), (42000,), (71000,)]
     - Executed order: 2

 * Container logs:
   > [2024/07/01 15:16:21.154 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/07/01 15:16:21.157 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=43] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/01 15:16:21.158 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:77, Type:drop schema, State:none, SchemaState:queueing, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:21.157 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:16:21.158 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:77, Type:drop schema, State:none, SchemaState:queueing, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:21.157 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/01 15:16:21.159 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:none, SchemaState:queueing, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:21.157 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:21.160 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=43] [neededSchemaVersion=44] ["start time"=69.074µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:16:21.162 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=44] ["take time"=2.212941ms] [job="ID:77, Type:drop schema, State:running, SchemaState:write only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:21.157 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:21.162 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:running, SchemaState:write only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:21.157 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:21.163 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=44] [neededSchemaVersion=45] ["start time"=167.97µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:16:21.165 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=45] ["take time"=2.238293ms] [job="ID:77, Type:drop schema, State:running, SchemaState:delete only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:21.157 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:21.165 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:running, SchemaState:delete only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:21.157 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:21.166 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=45] [neededSchemaVersion=46] ["start time"=66.909µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:16:21.168 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=46] ["take time"=2.037568ms] [job="ID:77, Type:drop schema, State:done, SchemaState:queueing, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:21.157 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:21.168 +00:00] [INFO] [delete_range.go:103] ["[ddl] add job into delete-range table"] [jobID=77] [jobType="drop schema"]
   > [2024/07/01 15:16:21.168 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:21.157 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:21.170 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=77]
   > [2024/07/01 15:16:21.170 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:16:21.171 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=46] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/01 15:16:21.172 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:79, Type:create schema, State:none, SchemaState:queueing, SchemaID:78, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:16:21.172 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:16:21.173 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:79, Type:create schema, State:none, SchemaState:queueing, SchemaID:78, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:16:21.172 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/01 15:16:21.173 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:79, Type:create schema, State:none, SchemaState:queueing, SchemaID:78, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:21.172 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:21.174 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=46] [neededSchemaVersion=47] ["start time"=189.69µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:16:21.176 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=47] ["take time"=2.195481ms] [job="ID:79, Type:create schema, State:done, SchemaState:public, SchemaID:78, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:16:21.172 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:21.177 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:79, Type:create schema, State:synced, SchemaState:public, SchemaID:78, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:21.172 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:21.177 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=79]
   > [2024/07/01 15:16:21.178 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:16:21.181 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=47] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_5mspyb`\n--\n\nDROP TABLE IF EXISTS `t_5mspyb`;"] [user=root@%]
   > [2024/07/01 15:16:21.182 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=47] [cur_db=testdb] [sql="CREATE TABLE `t_5mspyb` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_dugmmc` int(11) DEFAULT NULL,\n  `c_q0rdv` text DEFAULT NULL,\n  `c_0bhxq` int(11) DEFAULT NULL,\n  `c_qpz_v` text DEFAULT NULL,\n  `c_rgl8pc` double DEFAULT NULL,\n  `c_yisj0d` int(11) DEFAULT NULL,\n  `c_n9hfnb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/07/01 15:16:21.183 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:81, Type:create table, State:none, SchemaState:queueing, SchemaID:78, TableID:80, RowCount:0, ArgLen:1, start time: 2024-07-01 15:16:21.182 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:16:21.183 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:81, Type:create table, State:none, SchemaState:queueing, SchemaID:78, TableID:80, RowCount:0, ArgLen:1, start time: 2024-07-01 15:16:21.182 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_5mspyb` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_dugmmc` int(11) DEFAULT NULL,\n  `c_q0rdv` text DEFAULT NULL,\n  `c_0bhxq` int(11) DEFAULT NULL,\n  `c_qpz_v` text DEFAULT NULL,\n  `c_rgl8pc` double DEFAULT NULL,\n  `c_yisj0d` int(11) DEFAULT NULL,\n  `c_n9hfnb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/01 15:16:21.184 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:81, Type:create table, State:none, SchemaState:queueing, SchemaID:78, TableID:80, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:21.182 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:21.185 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=47] [neededSchemaVersion=48] ["start time"=364.296µs] [phyTblIDs="[80]"] [actionTypes="[8]"]
   > [2024/07/01 15:16:21.187 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=48] ["take time"=2.102102ms] [job="ID:81, Type:create table, State:done, SchemaState:public, SchemaID:78, TableID:80, RowCount:0, ArgLen:1, start time: 2024-07-01 15:16:21.182 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:21.188 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:81, Type:create table, State:synced, SchemaState:public, SchemaID:78, TableID:80, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:21.182 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:21.189 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=81]
   > [2024/07/01 15:16:21.189 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:16:21.189 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=68] ["first split key"=748000000000000050]
   > [2024/07/01 15:16:21.190 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=68] ["first at"=748000000000000050] ["first new region left"="{Id:68 StartKey:7480000000000000ff4a00000000000000f8 EndKey:7480000000000000ff5000000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:69 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/01 15:16:21.190 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[68]"]
   > [2024/07/01 15:16:21.190 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=48] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_5mspyb` DISABLE KEYS */;"] [user=root@%]
   > [2024/07/01 15:16:21.193 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=48] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_5mspyb` ENABLE KEYS */;"] [user=root@%]
   > [2024/07/01 15:16:21.194 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=48] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_vwvgdc`\n--\n\nDROP TABLE IF EXISTS `t_vwvgdc`;"] [user=root@%]
   > [2024/07/01 15:16:21.195 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=48] [cur_db=testdb] [sql="CREATE TABLE `t_vwvgdc` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_rdsfbc` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_8dsy1c` (`wkey`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/07/01 15:16:21.196 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:83, Type:create table, State:none, SchemaState:queueing, SchemaID:78, TableID:82, RowCount:0, ArgLen:1, start time: 2024-07-01 15:16:21.195 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:16:21.196 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:83, Type:create table, State:none, SchemaState:queueing, SchemaID:78, TableID:82, RowCount:0, ArgLen:1, start time: 2024-07-01 15:16:21.195 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_vwvgdc` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_rdsfbc` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_8dsy1c` (`wkey`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/01 15:16:21.197 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:83, Type:create table, State:none, SchemaState:queueing, SchemaID:78, TableID:82, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:21.195 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:21.198 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=48] [neededSchemaVersion=49] ["start time"=210.434µs] [phyTblIDs="[82]"] [actionTypes="[8]"]
   > [2024/07/01 15:16:21.200 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=49] ["take time"=2.14261ms] [job="ID:83, Type:create table, State:done, SchemaState:public, SchemaID:78, TableID:82, RowCount:0, ArgLen:1, start time: 2024-07-01 15:16:21.195 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:21.201 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:83, Type:create table, State:synced, SchemaState:public, SchemaID:78, TableID:82, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:21.195 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:21.202 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=83]
   > [2024/07/01 15:16:21.202 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:16:21.202 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=70] ["first split key"=748000000000000052]
   > [2024/07/01 15:16:21.203 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=70] ["first at"=748000000000000052] ["first new region left"="{Id:70 StartKey:7480000000000000ff5000000000000000f8 EndKey:7480000000000000ff5200000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:71 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/01 15:16:21.203 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[70]"]
   > [2024/07/01 15:16:21.203 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=49] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_vwvgdc` DISABLE KEYS */;"] [user=root@%]
   > [2024/07/01 15:16:21.205 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=49] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_vwvgdc` ENABLE KEYS */;"] [user=root@%]
   > [2024/07/01 15:16:22.235 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/07/01 15:16:22.247 +00:00] [INFO] [set.go:147] ["set global var"] [conn=413] [name=tx_isolation] [val=REPEATABLE-READ]

### Scenario 1
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
 * Instruction #1:
     - Instruction:  BEGIN OPTIMISTIC;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
 * Instruction #2:
     - Instruction:  insert into t_vwvgdc (wkey, pkey, c_rdsfbc) values (155, 228000, 99.50);
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
 * Instruction #3:
     - Instruction:  select ref_4.pkey as c0 from t_vwvgdc as ref_4 where 0 <> 0 union select ref_5....
     - Transaction: conn_0
     - Output: []
     - Executed order: 3
 * Instruction #4:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4

 * Container logs:
   > [2024/07/01 15:16:24.587 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/07/01 15:16:24.589 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=417] [schemaVersion=57] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/01 15:16:24.590 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:90, Type:drop schema, State:none, SchemaState:queueing, SchemaID:85, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:24.59 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:16:24.590 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:90, Type:drop schema, State:none, SchemaState:queueing, SchemaID:85, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:24.59 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/01 15:16:24.591 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:90, Type:drop schema, State:none, SchemaState:queueing, SchemaID:85, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:24.59 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:24.592 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=57] [neededSchemaVersion=58] ["start time"=79.061µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:16:24.594 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=58] ["take time"=2.196179ms] [job="ID:90, Type:drop schema, State:running, SchemaState:write only, SchemaID:85, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:24.59 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:24.594 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:90, Type:drop schema, State:running, SchemaState:write only, SchemaID:85, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:24.59 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:24.594 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=58] [neededSchemaVersion=59] ["start time"=51.055µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:16:24.597 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=59] ["take time"=2.537217ms] [job="ID:90, Type:drop schema, State:running, SchemaState:delete only, SchemaID:85, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:24.59 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:24.597 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:90, Type:drop schema, State:running, SchemaState:delete only, SchemaID:85, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:24.59 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:24.598 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=59] [neededSchemaVersion=60] ["start time"=54.267µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:16:24.600 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=60] ["take time"=2.052235ms] [job="ID:90, Type:drop schema, State:done, SchemaState:queueing, SchemaID:85, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:24.59 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:24.601 +00:00] [INFO] [delete_range.go:103] ["[ddl] add job into delete-range table"] [jobID=90] [jobType="drop schema"]
   > [2024/07/01 15:16:24.601 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:90, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:85, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:24.59 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:24.602 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=90]
   > [2024/07/01 15:16:24.602 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:16:24.603 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=417] [schemaVersion=60] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/01 15:16:24.604 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:92, Type:create schema, State:none, SchemaState:queueing, SchemaID:91, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:16:24.604 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:16:24.604 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:92, Type:create schema, State:none, SchemaState:queueing, SchemaID:91, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:16:24.604 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/01 15:16:24.605 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:92, Type:create schema, State:none, SchemaState:queueing, SchemaID:91, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:24.604 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:24.606 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=60] [neededSchemaVersion=61] ["start time"=144.363µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:16:24.608 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=61] ["take time"=2.265532ms] [job="ID:92, Type:create schema, State:done, SchemaState:public, SchemaID:91, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:16:24.604 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:24.608 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:92, Type:create schema, State:synced, SchemaState:public, SchemaID:91, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:24.604 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:24.609 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=92]
   > [2024/07/01 15:16:24.609 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:16:24.615 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=417] [schemaVersion=61] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_5mspyb`\n--\n\nDROP TABLE IF EXISTS `t_5mspyb`;"] [user=root@%]
   > [2024/07/01 15:16:24.615 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=417] [schemaVersion=61] [cur_db=testdb] [sql="CREATE TABLE `t_5mspyb` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_dugmmc` int(11) DEFAULT NULL,\n  `c_q0rdv` text DEFAULT NULL,\n  `c_0bhxq` int(11) DEFAULT NULL,\n  `c_qpz_v` text DEFAULT NULL,\n  `c_rgl8pc` double DEFAULT NULL,\n  `c_yisj0d` int(11) DEFAULT NULL,\n  `c_n9hfnb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/07/01 15:16:24.617 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:94, Type:create table, State:none, SchemaState:queueing, SchemaID:91, TableID:93, RowCount:0, ArgLen:1, start time: 2024-07-01 15:16:24.616 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:16:24.617 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:94, Type:create table, State:none, SchemaState:queueing, SchemaID:91, TableID:93, RowCount:0, ArgLen:1, start time: 2024-07-01 15:16:24.616 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_5mspyb` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_dugmmc` int(11) DEFAULT NULL,\n  `c_q0rdv` text DEFAULT NULL,\n  `c_0bhxq` int(11) DEFAULT NULL,\n  `c_qpz_v` text DEFAULT NULL,\n  `c_rgl8pc` double DEFAULT NULL,\n  `c_yisj0d` int(11) DEFAULT NULL,\n  `c_n9hfnb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/01 15:16:24.618 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:94, Type:create table, State:none, SchemaState:queueing, SchemaID:91, TableID:93, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:24.616 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:24.620 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=61] [neededSchemaVersion=62] ["start time"=586.393µs] [phyTblIDs="[93]"] [actionTypes="[8]"]
   > [2024/07/01 15:16:24.622 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=62] ["take time"=2.15602ms] [job="ID:94, Type:create table, State:done, SchemaState:public, SchemaID:91, TableID:93, RowCount:0, ArgLen:1, start time: 2024-07-01 15:16:24.616 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:24.623 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:94, Type:create table, State:synced, SchemaState:public, SchemaID:91, TableID:93, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:24.616 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:24.624 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=94]
   > [2024/07/01 15:16:24.624 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:16:24.624 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=74] ["first split key"=74800000000000005d]
   > [2024/07/01 15:16:24.625 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=74] ["first at"=74800000000000005d] ["first new region left"="{Id:74 StartKey:7480000000000000ff5700000000000000f8 EndKey:7480000000000000ff5d00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:75 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/01 15:16:24.625 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[74]"]
   > [2024/07/01 15:16:24.625 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=417] [schemaVersion=62] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_5mspyb` DISABLE KEYS */;"] [user=root@%]
   > [2024/07/01 15:16:24.628 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=417] [schemaVersion=62] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_5mspyb` ENABLE KEYS */;"] [user=root@%]
   > [2024/07/01 15:16:24.629 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=417] [schemaVersion=62] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_vwvgdc`\n--\n\nDROP TABLE IF EXISTS `t_vwvgdc`;"] [user=root@%]
   > [2024/07/01 15:16:24.629 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=417] [schemaVersion=62] [cur_db=testdb] [sql="CREATE TABLE `t_vwvgdc` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_rdsfbc` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_8dsy1c` (`wkey`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/07/01 15:16:24.631 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:96, Type:create table, State:none, SchemaState:queueing, SchemaID:91, TableID:95, RowCount:0, ArgLen:1, start time: 2024-07-01 15:16:24.63 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:16:24.631 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:96, Type:create table, State:none, SchemaState:queueing, SchemaID:91, TableID:95, RowCount:0, ArgLen:1, start time: 2024-07-01 15:16:24.63 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_vwvgdc` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_rdsfbc` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_8dsy1c` (`wkey`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/01 15:16:24.631 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:96, Type:create table, State:none, SchemaState:queueing, SchemaID:91, TableID:95, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:24.63 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:24.633 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=62] [neededSchemaVersion=63] ["start time"=230.898µs] [phyTblIDs="[95]"] [actionTypes="[8]"]
   > [2024/07/01 15:16:24.635 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=63] ["take time"=2.267906ms] [job="ID:96, Type:create table, State:done, SchemaState:public, SchemaID:91, TableID:95, RowCount:0, ArgLen:1, start time: 2024-07-01 15:16:24.63 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:24.635 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:96, Type:create table, State:synced, SchemaState:public, SchemaID:91, TableID:95, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:24.63 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:24.636 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=96]
   > [2024/07/01 15:16:24.636 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:16:24.636 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=76] ["first split key"=74800000000000005f]
   > [2024/07/01 15:16:24.636 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=76] ["first at"=74800000000000005f] ["first new region left"="{Id:76 StartKey:7480000000000000ff5d00000000000000f8 EndKey:7480000000000000ff5f00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:77 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/01 15:16:24.636 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[76]"]
   > [2024/07/01 15:16:24.636 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=417] [schemaVersion=63] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_vwvgdc` DISABLE KEYS */;"] [user=root@%]
   > [2024/07/01 15:16:24.638 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=417] [schemaVersion=63] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_vwvgdc` ENABLE KEYS */;"] [user=root@%]
   > [2024/07/01 15:16:25.671 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/07/01 15:16:25.680 +00:00] [INFO] [set.go:147] ["set global var"] [conn=419] [name=tx_isolation] [val=REPEATABLE-READ]
