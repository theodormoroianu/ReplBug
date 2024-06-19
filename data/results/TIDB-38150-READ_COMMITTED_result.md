# Bug ID TIDB-38150-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/38150
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED


## Details
 * Database: tidb-v6.3.0
 * Number of scenarios: 1
 * Initial setup script: /home/theodor/Projects/MasterThesis/data/sql/TIDB-38150_mysql_bk.sql

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
     - SQL:  select t_cp0sl.wkey as c0, t_cp0sl.pkey as c1, t_cp0sl.c_1_kgbc as c2, t_cp0sl....
     - TID: 0
     - Output: []
 * Instruction #3:
     - SQL:  update t_cp0sl set wkey = 59 where t_cp0sl.c_1_kgbc not in ( select subq_0.c0 a...
     - TID: 0
     - Output: None
 * Instruction #4:
     - SQL:  select t_cp0sl.wkey as c0, t_cp0sl.pkey as c1, t_cp0sl.c_1_kgbc as c2, t_cp0sl....
     - TID: 0
     - Output: [(59, 15000, None, 75.37), (59, 16000, None, 100.57), (59, 17000, None, 34.89)]
 * Instruction #5:
     - SQL:  COMMIT;
     - TID: 0
     - Output: None

 * Container logs:
   > [2024/06/19 09:46:10.171 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/06/19 09:46:10.174 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255963] [schemaVersion=44] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/06/19 09:46:10.176 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:80, Type:drop schema, State:queueing, SchemaState:public, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:46:10.174 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/06/19 09:46:10.177 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:80, Type:drop schema, State:queueing, SchemaState:public, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:46:10.174 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/06/19 09:46:10.183 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:80, Type:drop schema, State:queueing, SchemaState:public, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:46:10.174 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:46:10.186 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=44] [neededSchemaVersion=45] ["start time"=100.573µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 09:46:10.188 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=45] ["take time"=2.258479ms] [job="ID:80, Type:drop schema, State:running, SchemaState:write only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:46:10.174 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:46:10.191 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:80, Type:drop schema, State:running, SchemaState:write only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:46:10.174 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:46:10.195 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=45] [neededSchemaVersion=46] ["start time"=93.519µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 09:46:10.197 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=46] ["take time"=2.287254ms] [job="ID:80, Type:drop schema, State:running, SchemaState:delete only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:46:10.174 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:46:10.201 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:80, Type:drop schema, State:running, SchemaState:delete only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:46:10.174 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:46:10.204 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=46] [neededSchemaVersion=47] ["start time"=97.29µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 09:46:10.206 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=47] ["take time"=2.313445ms] [job="ID:80, Type:drop schema, State:done, SchemaState:none, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:46:10.174 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:46:10.212 +00:00] [INFO] [delete_range.go:109] ["[ddl] add job into delete-range table"] [jobID=80] [jobType="drop schema"]
   > [2024/06/19 09:46:10.213 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:80, Type:drop schema, State:synced, SchemaState:none, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:46:10.174 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:46:10.216 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=80]
   > [2024/06/19 09:46:10.216 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/06/19 09:46:10.217 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255963] [schemaVersion=47] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/06/19 09:46:10.219 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:82, Type:create schema, State:queueing, SchemaState:none, SchemaID:81, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 09:46:10.218 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/06/19 09:46:10.219 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:82, Type:create schema, State:queueing, SchemaState:none, SchemaID:81, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 09:46:10.218 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/19 09:46:10.229 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:82, Type:create schema, State:queueing, SchemaState:none, SchemaID:81, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:46:10.218 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:46:10.232 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=47] [neededSchemaVersion=48] ["start time"=159.798µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 09:46:10.234 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=48] ["take time"=2.267978ms] [job="ID:82, Type:create schema, State:done, SchemaState:public, SchemaID:81, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 09:46:10.218 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:46:10.238 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:82, Type:create schema, State:synced, SchemaState:public, SchemaID:81, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:46:10.218 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:46:10.240 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=82]
   > [2024/06/19 09:46:10.240 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/06/19 09:46:10.246 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255963] [schemaVersion=48] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_cp0sl`\n--\n\nDROP TABLE IF EXISTS `t_cp0sl`;"] [user=root@%]
   > [2024/06/19 09:46:10.247 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255963] [schemaVersion=48] [cur_db=testdb] [sql="CREATE TABLE `t_cp0sl` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_1_kgbc` int(11) DEFAULT NULL,\n  `c_dw8ly` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_py61ed` (`wkey`,`pkey`,`c_1_kgbc`,`c_dw8ly`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/06/19 09:46:10.249 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:84, Type:create table, State:queueing, SchemaState:none, SchemaID:81, TableID:83, RowCount:0, ArgLen:1, start time: 2024-06-19 09:46:10.248 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/06/19 09:46:10.249 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:84, Type:create table, State:queueing, SchemaState:none, SchemaID:81, TableID:83, RowCount:0, ArgLen:1, start time: 2024-06-19 09:46:10.248 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_cp0sl` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_1_kgbc` int(11) DEFAULT NULL,\n  `c_dw8ly` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_py61ed` (`wkey`,`pkey`,`c_1_kgbc`,`c_dw8ly`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/19 09:46:10.256 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:84, Type:create table, State:queueing, SchemaState:none, SchemaID:81, TableID:83, RowCount:0, ArgLen:0, start time: 2024-06-19 09:46:10.248 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:46:10.260 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=48] [neededSchemaVersion=49] ["start time"=444.265µs] [phyTblIDs="[83]"] [actionTypes="[8]"]
   > [2024/06/19 09:46:10.261 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=49] ["take time"=2.029049ms] [job="ID:84, Type:create table, State:done, SchemaState:public, SchemaID:81, TableID:83, RowCount:0, ArgLen:1, start time: 2024-06-19 09:46:10.248 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:46:10.266 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:84, Type:create table, State:synced, SchemaState:public, SchemaID:81, TableID:83, RowCount:0, ArgLen:0, start time: 2024-06-19 09:46:10.248 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:46:10.269 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=84]
   > [2024/06/19 09:46:10.269 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/06/19 09:46:10.269 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=72] ["first split key"=748000000000000053]
   > [2024/06/19 09:46:10.270 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=72] ["first at"=748000000000000053] ["first new region left"="{Id:72 StartKey:7480000000000000ff4d00000000000000f8 EndKey:7480000000000000ff5300000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:73 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/19 09:46:10.270 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[72]"]
   > [2024/06/19 09:46:10.270 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255963] [schemaVersion=49] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_cp0sl` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:46:10.272 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255963] [schemaVersion=49] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_cp0sl` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:46:10.273 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255963] [schemaVersion=49] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_d0c_g`\n--\n\nDROP TABLE IF EXISTS `t_d0c_g`;"] [user=root@%]
   > [2024/06/19 09:46:10.274 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255963] [schemaVersion=49] [cur_db=testdb] [sql="CREATE TABLE `t_d0c_g` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_p5i5kc` int(11) DEFAULT NULL,\n  `c_eephud` text DEFAULT NULL,\n  `c_dmlxnb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/06/19 09:46:10.277 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:86, Type:create table, State:queueing, SchemaState:none, SchemaID:81, TableID:85, RowCount:0, ArgLen:1, start time: 2024-06-19 09:46:10.275 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/06/19 09:46:10.278 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:86, Type:create table, State:queueing, SchemaState:none, SchemaID:81, TableID:85, RowCount:0, ArgLen:1, start time: 2024-06-19 09:46:10.275 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_d0c_g` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_p5i5kc` int(11) DEFAULT NULL,\n  `c_eephud` text DEFAULT NULL,\n  `c_dmlxnb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/19 09:46:10.284 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:86, Type:create table, State:queueing, SchemaState:none, SchemaID:81, TableID:85, RowCount:0, ArgLen:0, start time: 2024-06-19 09:46:10.275 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:46:10.289 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=49] [neededSchemaVersion=50] ["start time"=459.49µs] [phyTblIDs="[85]"] [actionTypes="[8]"]
   > [2024/06/19 09:46:10.290 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=50] ["take time"=2.086808ms] [job="ID:86, Type:create table, State:done, SchemaState:public, SchemaID:81, TableID:85, RowCount:0, ArgLen:1, start time: 2024-06-19 09:46:10.275 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:46:10.294 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:86, Type:create table, State:synced, SchemaState:public, SchemaID:81, TableID:85, RowCount:0, ArgLen:0, start time: 2024-06-19 09:46:10.275 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:46:10.298 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=86]
   > [2024/06/19 09:46:10.298 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/06/19 09:46:10.298 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=74] ["first split key"=748000000000000055]
   > [2024/06/19 09:46:10.298 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=74] ["first at"=748000000000000055] ["first new region left"="{Id:74 StartKey:7480000000000000ff5300000000000000f8 EndKey:7480000000000000ff5500000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:75 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/19 09:46:10.298 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[74]"]
   > [2024/06/19 09:46:10.299 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255963] [schemaVersion=50] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_d0c_g` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:46:10.302 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255963] [schemaVersion=50] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_d0c_g` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:46:11.316 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/06/19 09:46:11.331 +00:00] [INFO] [set.go:149] ["set global var"] [conn=2199023255965] [name=tx_isolation] [val=READ-COMMITTED]
