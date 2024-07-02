# Bug ID TIDB-30326-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/30326
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              The two cases should give the same result


## Details
 * Database: tidb-v5.4.0
 * Number of scenarios: 1
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
 * Instruction #1:
     - Instruction:  begin;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
 * Instruction #2:
     - Instruction:  WITH cte_0 AS (select 1 as c1, (FIRST_VALUE(1) over (partition by subq_0.c0) < ...
     - Transaction: conn_0
     - Output: ERROR: 2013 (HY000): Lost connection to MySQL server during query
     - Executed order: Not executed

 * Container logs:
   > [2024/07/02 12:29:38.230 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=5] [user=root] [host=]
   > [2024/07/02 12:29:38.233 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=28] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/07/02 12:29:38.234 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=28] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/07/02 12:29:38.236 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:58, Type:create schema, State:none, SchemaState:queueing, SchemaID:57, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 12:29:38.235 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 12:29:38.236 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:58, Type:create schema, State:none, SchemaState:queueing, SchemaID:57, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 12:29:38.235 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/02 12:29:38.236 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:58, Type:create schema, State:none, SchemaState:queueing, SchemaID:57, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:29:38.235 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:38.238 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=28] [neededSchemaVersion=29] ["start time"=173.557µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 12:29:38.240 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=29] ["take time"=2.230825ms] [job="ID:58, Type:create schema, State:done, SchemaState:public, SchemaID:57, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 12:29:38.235 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:38.240 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:58, Type:create schema, State:synced, SchemaState:public, SchemaID:57, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:29:38.235 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:38.241 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=58]
   > [2024/07/02 12:29:38.241 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 12:29:38.255 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=29] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_037irb`\n--\n\nDROP TABLE IF EXISTS `t_037irb`;"] [user=root@127.0.0.1]
   > [2024/07/02 12:29:38.256 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=29] [cur_db=testdb] [sql="CREATE TABLE `t_037irb` (\n  `c_nrh3o` int(11) DEFAULT NULL,\n  `c_nfauxb` text DEFAULT NULL,\n  `c_y5n4c` int(11) DEFAULT NULL,\n  `c_j9alg` double NOT NULL,\n  `c_4vix1d` text DEFAULT NULL,\n  `c_glkxdb` text DEFAULT NULL,\n  `c_2ykt0d` int(11) DEFAULT NULL,\n  `c_5fxv3c` double DEFAULT NULL,\n  PRIMARY KEY (`c_j9alg`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/07/02 12:29:38.258 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:60, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:59, RowCount:0, ArgLen:1, start time: 2024-07-02 12:29:38.257 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 12:29:38.258 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:60, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:59, RowCount:0, ArgLen:1, start time: 2024-07-02 12:29:38.257 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_037irb` (\n  `c_nrh3o` int(11) DEFAULT NULL,\n  `c_nfauxb` text DEFAULT NULL,\n  `c_y5n4c` int(11) DEFAULT NULL,\n  `c_j9alg` double NOT NULL,\n  `c_4vix1d` text DEFAULT NULL,\n  `c_glkxdb` text DEFAULT NULL,\n  `c_2ykt0d` int(11) DEFAULT NULL,\n  `c_5fxv3c` double DEFAULT NULL,\n  PRIMARY KEY (`c_j9alg`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/02 12:29:38.259 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:60, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:59, RowCount:0, ArgLen:0, start time: 2024-07-02 12:29:38.257 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:38.261 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=29] [neededSchemaVersion=30] ["start time"=465.847µs] [phyTblIDs="[59]"] [actionTypes="[8]"]
   > [2024/07/02 12:29:38.263 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=30] ["take time"=2.248286ms] [job="ID:60, Type:create table, State:done, SchemaState:public, SchemaID:57, TableID:59, RowCount:0, ArgLen:1, start time: 2024-07-02 12:29:38.257 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:38.264 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:60, Type:create table, State:synced, SchemaState:public, SchemaID:57, TableID:59, RowCount:0, ArgLen:0, start time: 2024-07-02 12:29:38.257 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:38.265 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=60]
   > [2024/07/02 12:29:38.265 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 12:29:38.265 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=52] ["first split key"=74800000000000003b]
   > [2024/07/02 12:29:38.266 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=30] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_037irb` DISABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/07/02 12:29:38.267 +00:00] [WARN] [2pc.go:1596] ["schemaLeaseChecker is not set for this transaction"] [sessionID=5] [startTS=450867594072162306] [commitTS=450867594072424448]
   > [2024/07/02 12:29:38.268 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=54] ["first at"=74800000000000003b] ["first new region left"="{Id:54 StartKey:7480000000000000ff3700000000000000f8 EndKey:7480000000000000ff3b00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:55 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/02 12:29:38.268 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[54]"]
   > [2024/07/02 12:29:38.268 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=30] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_037irb` ENABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/07/02 12:29:38.269 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=30] [cur_db=testdb] [sql="\n--\n-- Temporary view structure for view `t_cpsvpb`\n--\n\nDROP TABLE IF EXISTS `t_cpsvpb`;"] [user=root@127.0.0.1]
   > [2024/07/02 12:29:38.269 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=30] [cur_db=testdb] [sql="/*!50001 DROP VIEW IF EXISTS `t_cpsvpb`*/;"] [user=root@127.0.0.1]
   > [2024/07/02 12:29:38.272 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:62, Type:create view, State:none, SchemaState:queueing, SchemaID:57, TableID:61, RowCount:0, ArgLen:3, start time: 2024-07-02 12:29:38.271 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 12:29:38.272 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:62, Type:create view, State:none, SchemaState:queueing, SchemaID:57, TableID:61, RowCount:0, ArgLen:3, start time: 2024-07-02 12:29:38.271 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="/*!50001 CREATE VIEW `t_cpsvpb` AS SELECT \n 1 AS `c0`,\n 1 AS `c2`,\n 1 AS `c3`,\n 1 AS `c4`,\n 1 AS `c5`,\n 1 AS `c6`,\n 1 AS `c7`,\n 1 AS `c8`,\n 1 AS `c9`,\n 1 AS `c10`,\n 1 AS `c11`,\n 1 AS `c12`,\n 1 AS `c13`,\n 1 AS `c14`*/;"]
   > [2024/07/02 12:29:38.273 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:62, Type:create view, State:none, SchemaState:queueing, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-07-02 12:29:38.271 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:38.276 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=30] [neededSchemaVersion=31] ["start time"=563.067µs] [phyTblIDs="[61]"] [actionTypes="[2097152]"]
   > [2024/07/02 12:29:38.278 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=31] ["take time"=2.267981ms] [job="ID:62, Type:create view, State:done, SchemaState:public, SchemaID:57, TableID:61, RowCount:0, ArgLen:3, start time: 2024-07-02 12:29:38.271 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:38.279 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:62, Type:create view, State:synced, SchemaState:public, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-07-02 12:29:38.271 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:38.280 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=62]
   > [2024/07/02 12:29:38.280 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 12:29:38.281 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=31] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_x7zqmd`\n--\n\nDROP TABLE IF EXISTS `t_x7zqmd`;"] [user=root@127.0.0.1]
   > [2024/07/02 12:29:38.282 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=31] [cur_db=testdb] [sql="CREATE TABLE `t_x7zqmd` (\n  `c_8weeq` int(11) NOT NULL,\n  `c_13sfid` double DEFAULT NULL,\n  `c_hhjlmc` text DEFAULT NULL,\n  `c_3b1zld` int(11) DEFAULT NULL,\n  `c_6tu8wd` int(11) DEFAULT NULL,\n  `c_jyc_cd` double DEFAULT NULL,\n  PRIMARY KEY (`c_8weeq`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/07/02 12:29:38.283 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:64, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:63, RowCount:0, ArgLen:1, start time: 2024-07-02 12:29:38.282 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 12:29:38.283 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:64, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:63, RowCount:0, ArgLen:1, start time: 2024-07-02 12:29:38.282 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_x7zqmd` (\n  `c_8weeq` int(11) NOT NULL,\n  `c_13sfid` double DEFAULT NULL,\n  `c_hhjlmc` text DEFAULT NULL,\n  `c_3b1zld` int(11) DEFAULT NULL,\n  `c_6tu8wd` int(11) DEFAULT NULL,\n  `c_jyc_cd` double DEFAULT NULL,\n  PRIMARY KEY (`c_8weeq`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/02 12:29:38.284 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:64, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:63, RowCount:0, ArgLen:0, start time: 2024-07-02 12:29:38.282 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:38.286 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=31] [neededSchemaVersion=32] ["start time"=689.83µs] [phyTblIDs="[63]"] [actionTypes="[8]"]
   > [2024/07/02 12:29:38.287 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=32] ["take time"=2.028004ms] [job="ID:64, Type:create table, State:done, SchemaState:public, SchemaID:57, TableID:63, RowCount:0, ArgLen:1, start time: 2024-07-02 12:29:38.282 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:38.288 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:64, Type:create table, State:synced, SchemaState:public, SchemaID:57, TableID:63, RowCount:0, ArgLen:0, start time: 2024-07-02 12:29:38.282 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:38.289 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=64]
   > [2024/07/02 12:29:38.290 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 12:29:38.290 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=56] ["first split key"=74800000000000003f]
   > [2024/07/02 12:29:38.290 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=56] ["first at"=74800000000000003f] ["first new region left"="{Id:56 StartKey:7480000000000000ff3b00000000000000f8 EndKey:7480000000000000ff3f00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:57 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/02 12:29:38.290 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[56]"]
   > [2024/07/02 12:29:38.290 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=32] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_x7zqmd` DISABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/07/02 12:29:38.293 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=32] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_x7zqmd` ENABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/07/02 12:29:38.294 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=32] [cur_db=testdb] [sql="\n--\n-- Final view structure for view `t_cpsvpb`\n--\n\n/*!50001 DROP VIEW IF EXISTS `t_cpsvpb`*/;"] [user=root@127.0.0.1]
   > [2024/07/02 12:29:38.295 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:65, Type:drop view, State:none, SchemaState:queueing, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-07-02 12:29:38.294 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 12:29:38.295 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:65, Type:drop view, State:none, SchemaState:queueing, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-07-02 12:29:38.294 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="\n--\n-- Final view structure for view `t_cpsvpb`\n--\n\n/*!50001 DROP VIEW IF EXISTS `t_cpsvpb`*/;"]
   > [2024/07/02 12:29:38.295 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:drop view, State:none, SchemaState:queueing, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-07-02 12:29:38.294 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:38.297 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=32] [neededSchemaVersion=33] ["start time"=89.189µs] [phyTblIDs="[61]"] [actionTypes="[16777216]"]
   > [2024/07/02 12:29:38.299 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=33] ["take time"=2.272521ms] [job="ID:65, Type:drop view, State:running, SchemaState:write only, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-07-02 12:29:38.294 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:38.299 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:drop view, State:running, SchemaState:write only, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-07-02 12:29:38.294 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:38.301 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=33] [neededSchemaVersion=34] ["start time"=84.439µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 12:29:38.303 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=34] ["take time"=2.765118ms] [job="ID:65, Type:drop view, State:running, SchemaState:delete only, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-07-02 12:29:38.294 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:38.304 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:drop view, State:running, SchemaState:delete only, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-07-02 12:29:38.294 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:38.305 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=34] [neededSchemaVersion=35] ["start time"=92.192µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 12:29:38.308 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=35] ["take time"=2.491267ms] [job="ID:65, Type:drop view, State:done, SchemaState:queueing, SchemaID:57, TableID:61, RowCount:0, ArgLen:3, start time: 2024-07-02 12:29:38.294 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:38.309 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:drop view, State:synced, SchemaState:queueing, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-07-02 12:29:38.294 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:38.310 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=65]
   > [2024/07/02 12:29:38.310 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 12:29:38.315 +00:00] [INFO] [session.go:2108] ["Try to create a new txn inside a transaction auto commit"] [conn=5] [schemaVersion=35] [txnStartTS=450867594084220928] [txnScope=global]
   > [2024/07/02 12:29:38.317 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:67, Type:create view, State:none, SchemaState:queueing, SchemaID:57, TableID:66, RowCount:0, ArgLen:3, start time: 2024-07-02 12:29:38.316 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 12:29:38.317 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:67, Type:create view, State:none, SchemaState:queueing, SchemaID:57, TableID:66, RowCount:0, ArgLen:3, start time: 2024-07-02 12:29:38.316 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="/*!50001 CREATE ALGORITHM=UNDEFINED */\n/*!50013 DEFINER=`root`@`127.0.0.1` SQL SECURITY DEFINER */\n/*!50001 VIEW `t_cpsvpb` (`c0`, `c2`, `c3`, `c4`, `c5`, `c6`, `c7`, `c8`, `c9`, `c10`, `c11`, `c12`, `c13`, `c14`) AS SELECT DISTINCT `subq_0`.`c1` AS `c0`,`subq_0`.`c2` AS `c2`,8 AS `c3`,CASE WHEN (`subq_0`.`c3` NOT IN (SELECT `ref_2`.`c_4vix1d` AS `c0` FROM `testdb`.`t_037irb` AS `ref_2` WHERE `ref_2`.`c_2ykt0d`<=`ref_2`.`c_nrh3o`)) AND (`subq_0`.`c3`<=(SELECT (SELECT `c_hhjlmc` AS `c_hhjlmc` FROM `testdb`.`t_x7zqmd` ORDER BY `c_hhjlmc` LIMIT 4,1) AS `c0` FROM `testdb`.`t_037irb` AS `ref_3` WHERE `subq_0`.`c1`!=`ref_3`.`c_2ykt0d`)) THEN `subq_0`.`c3` ELSE `subq_0`.`c3` END AS `c4`,CASE WHEN `subq_0`.`c1`>=(SELECT MAX(`c_8weeq`) AS `max(c_8weeq)` FROM `testdb`.`t_x7zqmd`) THEN `subq_0`.`c2` ELSE `subq_0`.`c2` END AS `c5`,`subq_0`.`c1` AS `c6`,`subq_0`.`c2` AS `c7`,`subq_0`.`c3` AS `c8`,`subq_0`.`c3` AS `c9`,`subq_0`.`c2` AS `c10`,`subq_0`.`c4` AS `c11`,COUNT(CAST(`subq_0`.`c2` AS DOUBLE)) OVER (PARTITION BY `subq_0`.`c4` ORDER BY `subq_0`.`c1`) AS `c12`,`subq_0`.`c3` AS `c13`,CAST(COALESCE(`subq_0`.`c3`, _UTF8MB4'9sx3k') AS CHAR) AS `c14` FROM (SELECT COUNT(CAST(`ref_1`.`c_jyc_cd` AS DOUBLE)) AS `c0`,AVG(CAST(`ref_1`.`c_3b1zld` AS SIGNED)) AS `c1`,MIN(CAST(`ref_1`.`c_jyc_cd` AS DOUBLE)) AS `c2`,`ref_0`.`c_glkxdb` AS `c3`,COUNT(CAST(`ref_1`.`c_13sfid` AS DOUBLE)) AS `c4` FROM `testdb`.`t_037irb` AS `ref_0` JOIN `testdb`.`t_x7zqmd` AS `ref_1` WHERE `ref_0`.`c_nrh3o`>`ref_1`.`c_8weeq` GROUP BY `ref_0`.`c_glkxdb`) AS `subq_0` WHERE (SELECT `c_8weeq` AS `c_8weeq` FROM `testdb`.`t_x7zqmd` ORDER BY `c_8weeq` LIMIT 2,1) IS NOT NULL */;"]
   > [2024/07/02 12:29:38.318 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:create view, State:none, SchemaState:queueing, SchemaID:57, TableID:66, RowCount:0, ArgLen:0, start time: 2024-07-02 12:29:38.316 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:38.321 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=35] [neededSchemaVersion=36] ["start time"=559.156µs] [phyTblIDs="[66]"] [actionTypes="[2097152]"]
   > [2024/07/02 12:29:38.323 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=36] ["take time"=2.263232ms] [job="ID:67, Type:create view, State:done, SchemaState:public, SchemaID:57, TableID:66, RowCount:0, ArgLen:3, start time: 2024-07-02 12:29:38.316 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:38.324 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:create view, State:synced, SchemaState:public, SchemaID:57, TableID:66, RowCount:0, ArgLen:0, start time: 2024-07-02 12:29:38.316 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:38.326 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=67]
   > [2024/07/02 12:29:38.326 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 12:29:39.380 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=7] [user=root] [host=]
   > [2024/07/02 12:29:39.392 +00:00] [INFO] [set.go:139] ["set global var"] [conn=7] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/07/02 12:29:39.962 +00:00] [ERROR] [misc.go:95] ["panic in the recoverable goroutine"] [r="\"invalid memory address or nil pointer dereference\""] ["stack trace"="github.com/pingcap/tidb/util.WithRecovery.func1\n\t/go/src/github.com/pingcap/tidb/util/misc.go:97\nruntime.gopanic\n\t/usr/local/go/src/runtime/panic.go:884\nruntime.panicmem\n\t/usr/local/go/src/runtime/panic.go:260\nruntime.sigpanic\n\t/usr/local/go/src/runtime/signal_unix.go:839\ngithub.com/pingcap/tidb/executor.(*vecGroupChecker).splitIntoGroups\n\t/go/src/github.com/pingcap/tidb/executor/aggregate.go:1457\ngithub.com/pingcap/tidb/executor.(*PipelinedWindowExec).getRowsInPartition\n\t/go/src/github.com/pingcap/tidb/executor/pipelined_window.go:189\ngithub.com/pingcap/tidb/executor.(*PipelinedWindowExec).Next\n\t/go/src/github.com/pingcap/tidb/executor/pipelined_window.go:125\ngithub.com/pingcap/tidb/executor.Next\n\t/go/src/github.com/pingcap/tidb/executor/executor.go:286\ngithub.com/pingcap/tidb/executor.(*ProjectionExec).unParallelExecute\n\t/go/src/github.com/pingcap/tidb/executor/projection.go:194\ngithub.com/pingcap/tidb/executor.(*ProjectionExec).Next\n\t/go/src/github.com/pingcap/tidb/executor/projection.go:180\ngithub.com/pingcap/tidb/executor.Next\n\t/go/src/github.com/pingcap/tidb/executor/executor.go:286\ngithub.com/pingcap/tidb/executor.(*CTEExec).computeSeedPart\n\t/go/src/github.com/pingcap/tidb/executor/cte.go:226\ngithub.com/pingcap/tidb/executor.(*CTEExec).Next\n\t/go/src/github.com/pingcap/tidb/executor/cte.go:161\ngithub.com/pingcap/tidb/executor.Next\n\t/go/src/github.com/pingcap/tidb/executor/executor.go:286\ngithub.com/pingcap/tidb/executor.(*HashJoinExec).fetchBuildSideRows\n\t/go/src/github.com/pingcap/tidb/executor/join.go:266\ngithub.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable.func2\n\t/go/src/github.com/pingcap/tidb/executor/join.go:715\ngithub.com/pingcap/tidb/util.WithRecovery\n\t/go/src/github.com/pingcap/tidb/util/misc.go:100"]
   > runtime: goroutine stack exceeds 1000000000-byte limit
   > runtime: sp=0xc0312f8380 stack=[0xc0312f8000, 0xc0512f8000]
   > fatal error: stack overflow
   > runtime stack:
   > runtime.throw({0x3aa773d?, 0x590b5c0?})
   > 	/usr/local/go/src/runtime/panic.go:1047 +0x5d fp=0x7fa158cdc888 sp=0x7fa158cdc858 pc=0x13b859d
   > runtime.newstack()
   > 	/usr/local/go/src/runtime/stack.go:1103 +0x5cc fp=0x7fa158cdca40 sp=0x7fa158cdc888 pc=0x13d35ec
   > runtime.morestack()
   > 	/usr/local/go/src/runtime/asm_amd64.s:570 +0x8b fp=0x7fa158cdca48 sp=0x7fa158cdca40 pc=0x13ec60b
   > goroutine 994 [running]:
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60?, 0xc010540de0?}, {0x4012e60?, 0xc010540de0?})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:183 +0x12c fp=0xc0312f8390 sp=0xc0312f8388 pc=0x1f5780c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc010540d80}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f83c8 sp=0xc0312f8390 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011093080}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8400 sp=0xc0312f83c8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0103cb0e0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8438 sp=0xc0312f8400 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc010aa4d80}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8470 sp=0xc0312f8438 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0100faff0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f84a8 sp=0xc0312f8470 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0105e0ab0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f84e0 sp=0xc0312f84a8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc000705fb0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8518 sp=0xc0312f84e0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0100fafd0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8550 sp=0xc0312f8518 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011092d20}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8588 sp=0xc0312f8550 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc010317240}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f85c0 sp=0xc0312f8588 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc010540de0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f85f8 sp=0xc0312f85c0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc010540d80}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8630 sp=0xc0312f85f8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011093080}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8668 sp=0xc0312f8630 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0103cb0e0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f86a0 sp=0xc0312f8668 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc010aa4d80}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f86d8 sp=0xc0312f86a0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0100faff0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8710 sp=0xc0312f86d8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0105e0ab0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8748 sp=0xc0312f8710 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc000705fb0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8780 sp=0xc0312f8748 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0100fafd0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f87b8 sp=0xc0312f8780 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011092d20}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f87f0 sp=0xc0312f87b8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc010317240}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8828 sp=0xc0312f87f0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc010540de0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8860 sp=0xc0312f8828 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc010540d80}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8898 sp=0xc0312f8860 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011093080}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f88d0 sp=0xc0312f8898 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0103cb0e0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8908 sp=0xc0312f88d0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc010aa4d80}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8940 sp=0xc0312f8908 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0100faff0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8978 sp=0xc0312f8940 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0105e0ab0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f89b0 sp=0xc0312f8978 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc000705fb0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f89e8 sp=0xc0312f89b0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0100fafd0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8a20 sp=0xc0312f89e8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011092d20}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8a58 sp=0xc0312f8a20 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc010317240}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8a90 sp=0xc0312f8a58 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc010540de0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8ac8 sp=0xc0312f8a90 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc010540d80}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8b00 sp=0xc0312f8ac8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011093080}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8b38 sp=0xc0312f8b00 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0103cb0e0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8b70 sp=0xc0312f8b38 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc010aa4d80}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8ba8 sp=0xc0312f8b70 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0100faff0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8be0 sp=0xc0312f8ba8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0105e0ab0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8c18 sp=0xc0312f8be0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc000705fb0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8c50 sp=0xc0312f8c18 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0100fafd0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8c88 sp=0xc0312f8c50 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011092d20}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8cc0 sp=0xc0312f8c88 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc010317240}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8cf8 sp=0xc0312f8cc0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc010540de0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8d30 sp=0xc0312f8cf8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc010540d80}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8d68 sp=0xc0312f8d30 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011093080}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8da0 sp=0xc0312f8d68 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0103cb0e0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8dd8 sp=0xc0312f8da0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc010aa4d80}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8e10 sp=0xc0312f8dd8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0100faff0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8e48 sp=0xc0312f8e10 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0105e0ab0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8e80 sp=0xc0312f8e48 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc000705fb0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8eb8 sp=0xc0312f8e80 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0100fafd0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8ef0 sp=0xc0312f8eb8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011092d20}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8f28 sp=0xc0312f8ef0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc010317240}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8f60 sp=0xc0312f8f28 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc010540de0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8f98 sp=0xc0312f8f60 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc010540d80}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f8fd0 sp=0xc0312f8f98 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011093080}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f9008 sp=0xc0312f8fd0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0103cb0e0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f9040 sp=0xc0312f9008 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc010aa4d80}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f9078 sp=0xc0312f9040 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0100faff0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f90b0 sp=0xc0312f9078 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0105e0ab0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f90e8 sp=0xc0312f90b0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc000705fb0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f9120 sp=0xc0312f90e8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0100fafd0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f9158 sp=0xc0312f9120 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011092d20}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f9190 sp=0xc0312f9158 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc010317240}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f91c8 sp=0xc0312f9190 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc010540de0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f9200 sp=0xc0312f91c8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc010540d80}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f9238 sp=0xc0312f9200 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011093080}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f9270 sp=0xc0312f9238 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0103cb0e0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f92a8 sp=0xc0312f9270 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc010aa4d80}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f92e0 sp=0xc0312f92a8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0100faff0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f9318 sp=0xc0312f92e0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0105e0ab0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f9350 sp=0xc0312f9318 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc000705fb0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f9388 sp=0xc0312f9350 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0100fafd0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f93c0 sp=0xc0312f9388 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011092d20}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f93f8 sp=0xc0312f93c0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc010317240}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f9430 sp=0xc0312f93f8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc010540de0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f9468 sp=0xc0312f9430 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc010540d80}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f94a0 sp=0xc0312f9468 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011093080}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f94d8 sp=0xc0312f94a0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0103cb0e0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f9510 sp=0xc0312f94d8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc010aa4d80}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f9548 sp=0xc0312f9510 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0100faff0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f9580 sp=0xc0312f9548 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0105e0ab0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f95b8 sp=0xc0312f9580 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc000705fb0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f95f0 sp=0xc0312f95b8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0100fafd0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f9628 sp=0xc0312f95f0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011092d20}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f9660 sp=0xc0312f9628 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc010317240}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f9698 sp=0xc0312f9660 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc010540de0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f96d0 sp=0xc0312f9698 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc010540d80}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f9708 sp=0xc0312f96d0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011093080}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f9740 sp=0xc0312f9708 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0103cb0e0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f9778 sp=0xc0312f9740 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc010aa4d80}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f97b0 sp=0xc0312f9778 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0100faff0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f97e8 sp=0xc0312f97b0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0105e0ab0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f9820 sp=0xc0312f97e8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc000705fb0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f9858 sp=0xc0312f9820 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0100fafd0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f9890 sp=0xc0312f9858 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011092d20}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f98c8 sp=0xc0312f9890 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc010317240}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f9900 sp=0xc0312f98c8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc010540de0}, {0x4012e60, 0xc010540de0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0312f9938 sp=0xc0312f9900 pc=0x1f577a5
   > ...additional frames elided...
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:712 +0x22d
   > goroutine 1 [chan receive]:
   > runtime.gopark(0xc01053bf70?, 0xc010cfddc0?, 0xbf?, 0xc1?, 0x37fc5c0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010cfdd40 sp=0xc010cfdd20 pc=0x13bb516
   > runtime.chanrecv(0xc000560540, 0xc010cfde30, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc010cfddd0 sp=0xc010cfdd40 pc=0x13854bb
   > runtime.chanrecv1(0xc000cced00?, 0x0?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc010cfddf8 sp=0xc010cfddd0 pc=0x1384fb8
   > github.com/pingcap/tidb/server.(*Server).Run(0xc000cced00)
   > 	/go/src/github.com/pingcap/tidb/server/server.go:370 +0x1f0 fp=0xc010cfde50 sp=0xc010cfddf8 pc=0x31e23d0
   > main.main()
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:213 +0x539 fp=0xc010cfdf80 sp=0xc010cfde50 pc=0x33af4b9
   > runtime.main()
   > 	/usr/local/go/src/runtime/proc.go:250 +0x212 fp=0xc010cfdfe0 sp=0xc010cfdf80 pc=0x13bb152
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010cfdfe8 sp=0xc010cfdfe0 pc=0x13ee6e1
   > goroutine 2 [force gc (idle)]:
   > runtime.gopark(0x0?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008efb0 sp=0xc00008ef90 pc=0x13bb516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.forcegchelper()
   > 	/usr/local/go/src/runtime/proc.go:302 +0xad fp=0xc00008efe0 sp=0xc00008efb0 pc=0x13bb3ad
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008efe8 sp=0xc00008efe0 pc=0x13ee6e1
   > created by runtime.init.6
   > 	/usr/local/go/src/runtime/proc.go:290 +0x25
   > goroutine 3 [GC sweep wait]:
   > runtime.gopark(0x1?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008f790 sp=0xc00008f770 pc=0x13bb516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.bgsweep(0x0?)
   > 	/usr/local/go/src/runtime/mgcsweep.go:297 +0xd7 fp=0xc00008f7c8 sp=0xc00008f790 pc=0x13a4337
   > runtime.gcenable.func1()
   > 	/usr/local/go/src/runtime/mgc.go:178 +0x26 fp=0xc00008f7e0 sp=0xc00008f7c8 pc=0x1398e06
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008f7e8 sp=0xc00008f7e0 pc=0x13ee6e1
   > created by runtime.gcenable
   > 	/usr/local/go/src/runtime/mgc.go:178 +0x6b
   > goroutine 4 [GC scavenge wait]:
   > runtime.gopark(0xc0000b8000?, 0x3fe2f28?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008ff70 sp=0xc00008ff50 pc=0x13bb516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.(*scavengerState).park(0x5f57220)
   > 	/usr/local/go/src/runtime/mgcscavenge.go:389 +0x53 fp=0xc00008ffa0 sp=0xc00008ff70 pc=0x13a2313
   > runtime.bgscavenge(0x0?)
   > 	/usr/local/go/src/runtime/mgcscavenge.go:622 +0x65 fp=0xc00008ffc8 sp=0xc00008ffa0 pc=0x13a2925
   > runtime.gcenable.func2()
   > 	/usr/local/go/src/runtime/mgc.go:179 +0x26 fp=0xc00008ffe0 sp=0xc00008ffc8 pc=0x1398da6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008ffe8 sp=0xc00008ffe0 pc=0x13ee6e1
   > created by runtime.gcenable
   > 	/usr/local/go/src/runtime/mgc.go:179 +0xaa
   > goroutine 5 [finalizer wait]:
   > runtime.gopark(0x5f58620?, 0xc000007860?, 0x0?, 0x0?, 0xc00008e770?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008e628 sp=0xc00008e608 pc=0x13bb516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.runfinq()
   > 	/usr/local/go/src/runtime/mfinal.go:180 +0x10f fp=0xc00008e7e0 sp=0xc00008e628 pc=0x1397f0f
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008e7e8 sp=0xc00008e7e0 pc=0x13ee6e1
   > created by runtime.createfing
   > 	/usr/local/go/src/runtime/mfinal.go:157 +0x45
   > goroutine 6 [GC worker (idle)]:
   > runtime.gopark(0x0?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000090750 sp=0xc000090730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0000907e0 sp=0xc000090750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000907e8 sp=0xc0000907e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 7 [GC worker (idle)]:
   > runtime.gopark(0x21e6a9148a26?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000090f50 sp=0xc000090f30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc000090fe0 sp=0xc000090f50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000090fe8 sp=0xc000090fe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 18 [GC worker (idle)]:
   > runtime.gopark(0x21e6a91473c7?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008a750 sp=0xc00008a730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008a7e0 sp=0xc00008a750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008a7e8 sp=0xc00008a7e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 8 [GC worker (idle)]:
   > runtime.gopark(0x21e6bc9ff507?, 0x1?, 0xa7?, 0x57?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000091750 sp=0xc000091730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0000917e0 sp=0xc000091750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000917e8 sp=0xc0000917e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 19 [GC worker (idle)]:
   > runtime.gopark(0x21e6bca0520f?, 0x1?, 0x93?, 0x42?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008af50 sp=0xc00008af30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008afe0 sp=0xc00008af50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008afe8 sp=0xc00008afe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 9 [GC worker (idle)]:
   > runtime.gopark(0x21e6bca0cb31?, 0x3?, 0xa8?, 0x37?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000091f50 sp=0xc000091f30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc000091fe0 sp=0xc000091f50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000091fe8 sp=0xc000091fe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 20 [GC worker (idle)]:
   > runtime.gopark(0x21e6bca09f44?, 0xc00010e060?, 0x18?, 0x14?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008b750 sp=0xc00008b730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008b7e0 sp=0xc00008b750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008b7e8 sp=0xc00008b7e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 10 [GC worker (idle)]:
   > runtime.gopark(0x21e6bc9ff507?, 0x1?, 0x52?, 0x84?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00049e750 sp=0xc00049e730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00049e7e0 sp=0xc00049e750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00049e7e8 sp=0xc00049e7e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 11 [GC worker (idle)]:
   > runtime.gopark(0x21e6a91473c7?, 0x3?, 0x5d?, 0x4e?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00049ef50 sp=0xc00049ef30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00049efe0 sp=0xc00049ef50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00049efe8 sp=0xc00049efe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 34 [GC worker (idle)]:
   > runtime.gopark(0x21e6bc9705b3?, 0x1?, 0x47?, 0xf?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00049a750 sp=0xc00049a730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00049a7e0 sp=0xc00049a750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00049a7e8 sp=0xc00049a7e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 21 [GC worker (idle)]:
   > runtime.gopark(0x21e6bca0cb31?, 0x1?, 0x7d?, 0x5f?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008bf50 sp=0xc00008bf30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008bfe0 sp=0xc00008bf50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008bfe8 sp=0xc00008bfe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 12 [GC worker (idle)]:
   > runtime.gopark(0x21e6bc96fff8?, 0x1?, 0x7c?, 0xcb?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00049f750 sp=0xc00049f730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00049f7e0 sp=0xc00049f750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00049f7e8 sp=0xc00049f7e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 22 [GC worker (idle)]:
   > runtime.gopark(0x21e6bca0d477?, 0x3?, 0x5d?, 0x7?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00009cf50 sp=0xc00009cf30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00009cfe0 sp=0xc00009cf50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00009cfe8 sp=0xc00009cfe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 35 [GC worker (idle)]:
   > runtime.gopark(0x21e6bca0520f?, 0x3?, 0xab?, 0x55?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00049af50 sp=0xc00049af30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00049afe0 sp=0xc00049af50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00049afe8 sp=0xc00049afe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 23 [GC worker (idle)]:
   > runtime.gopark(0x21e6a9146c24?, 0x1?, 0xfe?, 0x27?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008cf50 sp=0xc00008cf30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008cfe0 sp=0xc00008cf50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008cfe8 sp=0xc00008cfe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 36 [GC worker (idle)]:
   > runtime.gopark(0x21e6bca0d477?, 0x1?, 0xef?, 0x50?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00049b750 sp=0xc00049b730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00049b7e0 sp=0xc00049b750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00049b7e8 sp=0xc00049b7e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 68 [select]:
   > runtime.gopark(0xc00049cf88?, 0x3?, 0xa8?, 0x4c?, 0xc00049cf72?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00049cdf8 sp=0xc00049cdd8 pc=0x13bb516
   > runtime.selectgo(0xc00049cf88, 0xc00049cf6c, 0xc000111e80?, 0x0, 0xc00049cf88?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00049cf38 sp=0xc00049cdf8 pc=0x13cbbdc
   > go.opencensus.io/stats/view.(*worker).start(0xc000111e80)
   > 	/go/pkg/mod/go.opencensus.io@v0.23.0/stats/view/worker.go:276 +0xad fp=0xc00049cfc8 sp=0xc00049cf38 pc=0x29900cd
   > go.opencensus.io/stats/view.init.0.func1()
   > 	/go/pkg/mod/go.opencensus.io@v0.23.0/stats/view/worker.go:34 +0x26 fp=0xc00049cfe0 sp=0xc00049cfc8 pc=0x298f346
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00049cfe8 sp=0xc00049cfe0 pc=0x13ee6e1
   > created by go.opencensus.io/stats/view.init.0
   > 	/go/pkg/mod/go.opencensus.io@v0.23.0/stats/view/worker.go:34 +0x8d
   > goroutine 137 [chan receive]:
   > runtime.gopark(0xc0002fc840?, 0x13c1374?, 0x10?, 0xc6?, 0x13d8de5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00049c5b8 sp=0xc00049c598 pc=0x13bb516
   > runtime.chanrecv(0xc0002fc7e0, 0xc00049c728, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc00049c648 sp=0xc00049c5b8 pc=0x13854bb
   > runtime.chanrecv2(0x3b9aca00?, 0x13bb600?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc00049c670 sp=0xc00049c648 pc=0x1384ff8
   > go.etcd.io/etcd/pkg/logutil.(*MergeLogger).outputLoop(0xc000868750)
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:173 +0x8c fp=0xc00049c7c8 sp=0xc00049c670 pc=0x1a12c4c
   > go.etcd.io/etcd/pkg/logutil.NewMergeLogger.func1()
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:91 +0x26 fp=0xc00049c7e0 sp=0xc00049c7c8 pc=0x1a124c6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00049c7e8 sp=0xc00049c7e0 pc=0x13ee6e1
   > created by go.etcd.io/etcd/pkg/logutil.NewMergeLogger
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:91 +0xb6
   > goroutine 107 [chan receive]:
   > runtime.gopark(0xc0002fc960?, 0x1?, 0x10?, 0xa6?, 0x13d8de5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000f1a5b8 sp=0xc000f1a598 pc=0x13bb516
   > runtime.chanrecv(0xc0002fc900, 0xc000f1a728, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000f1a648 sp=0xc000f1a5b8 pc=0x13854bb
   > runtime.chanrecv2(0x3b9aca00?, 0x13bb600?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc000f1a670 sp=0xc000f1a648 pc=0x1384ff8
   > go.etcd.io/etcd/pkg/logutil.(*MergeLogger).outputLoop(0xc000152af8)
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:173 +0x8c fp=0xc000f1a7c8 sp=0xc000f1a670 pc=0x1a12c4c
   > go.etcd.io/etcd/pkg/logutil.NewMergeLogger.func1()
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:91 +0x26 fp=0xc000f1a7e0 sp=0xc000f1a7c8 pc=0x1a124c6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000f1a7e8 sp=0xc000f1a7e0 pc=0x13ee6e1
   > created by go.etcd.io/etcd/pkg/logutil.NewMergeLogger
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:91 +0xb6
   > goroutine 121 [chan receive]:
   > runtime.gopark(0xc000149d40?, 0x0?, 0x10?, 0x66?, 0x13d8de5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000f165b8 sp=0xc000f16598 pc=0x13bb516
   > runtime.chanrecv(0xc000149ce0, 0xc000f16728, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000f16648 sp=0xc000f165b8 pc=0x13854bb
   > runtime.chanrecv2(0x3b9aca00?, 0x13bb600?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc000f16670 sp=0xc000f16648 pc=0x1384ff8
   > go.etcd.io/etcd/pkg/logutil.(*MergeLogger).outputLoop(0xc00052c648)
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:173 +0x8c fp=0xc000f167c8 sp=0xc000f16670 pc=0x1a12c4c
   > go.etcd.io/etcd/pkg/logutil.NewMergeLogger.func1()
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:91 +0x26 fp=0xc000f167e0 sp=0xc000f167c8 pc=0x1a124c6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000f167e8 sp=0xc000f167e0 pc=0x13ee6e1
   > created by go.etcd.io/etcd/pkg/logutil.NewMergeLogger
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:91 +0xb6
   > goroutine 434 [chan receive]:
   > runtime.gopark(0xa17ffbff18?, 0x0?, 0x78?, 0x9e?, 0x13d8de5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000622e20 sp=0xc000622e00 pc=0x13bb516
   > runtime.chanrecv(0xc0002fc4e0, 0x0, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000622eb0 sp=0xc000622e20 pc=0x13854bb
   > runtime.chanrecv1(0xdf8475800?, 0x1b?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc000622ed8 sp=0xc000622eb0 pc=0x1384fb8
   > github.com/pingcap/tidb/util/profile.HeapProfileForGlobalMemTracker(0xc000701d40?)
   > 	/go/src/github.com/pingcap/tidb/util/profile/trackerRecorder.go:33 +0xa7 fp=0xc000622fc8 sp=0xc000622ed8 pc=0x267adc7
   > main.setHeapProfileTracker.func1()
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:279 +0x26 fp=0xc000622fe0 sp=0xc000622fc8 pc=0x33afc46
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000622fe8 sp=0xc000622fe0 pc=0x13ee6e1
   > created by main.setHeapProfileTracker
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:279 +0xa5
   > goroutine 435 [chan receive]:
   > runtime.gopark(0xc0002fc6c0?, 0x13c1374?, 0x38?, 0xfe?, 0x13d8de5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00009fde0 sp=0xc00009fdc0 pc=0x13bb516
   > runtime.chanrecv(0xc0002fc660, 0x0, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc00009fe70 sp=0xc00009fde0 pc=0x13854bb
   > runtime.chanrecv1(0x5f5e100?, 0x3ace4e4?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc00009fe98 sp=0xc00009fe70 pc=0x1384fb8
   > github.com/pingcap/tidb/util/systimemon.StartMonitor(0x3bccd98, 0x3bcc3f0, 0xc000ac3730)
   > 	/go/src/github.com/pingcap/tidb/util/systimemon/systime_mon.go:32 +0x185 fp=0xc00009ffb8 sp=0xc00009fe98 pc=0x33ac665
   > main.setupMetrics.func3()
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:696 +0x31 fp=0xc00009ffe0 sp=0xc00009ffb8 pc=0x33b2df1
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00009ffe8 sp=0xc00009ffe0 pc=0x13ee6e1
   > created by main.setupMetrics
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:696 +0x115
   > goroutine 436 [select]:
   > runtime.gopark(0xc000f18f80?, 0x2?, 0x10?, 0x0?, 0xc000f18f4c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000f18dd0 sp=0xc000f18db0 pc=0x13bb516
   > runtime.selectgo(0xc000f18f80, 0xc000f18f48, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000f18f10 sp=0xc000f18dd0 pc=0x13cbbdc
   > github.com/pingcap/badger.(*DB).updateSize(0x0?, 0xc0006859c8)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:1039 +0x105 fp=0xc000f18fc0 sp=0xc000f18f10 pc=0x329a445
   > github.com/pingcap/badger.Open.func5()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:328 +0x2a fp=0xc000f18fe0 sp=0xc000f18fc0 pc=0x329450a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000f18fe8 sp=0xc000f18fe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.Open
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:328 +0xf5c
   > goroutine 437 [select]:
   > runtime.gopark(0xc000f19788?, 0x2?, 0x8?, 0x0?, 0xc000f19764?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000f195e8 sp=0xc000f195c8 pc=0x13bb516
   > runtime.selectgo(0xc000f19788, 0xc000f19760, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000f19728 sp=0xc000f195e8 pc=0x13cbbdc
   > github.com/pingcap/badger/epoch.(*ResourceManager).collectLoop(0x0?, 0xc0006859f8)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/epoch/manager.go:101 +0xd3 fp=0xc000f197c0 sp=0xc000f19728 pc=0x3257a13
   > github.com/pingcap/badger/epoch.NewResourceManager.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/epoch/manager.go:79 +0x2a fp=0xc000f197e0 sp=0xc000f197c0 pc=0x32577aa
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000f197e8 sp=0xc000f197e0 pc=0x13ee6e1
   > created by github.com/pingcap/badger/epoch.NewResourceManager
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/epoch/manager.go:79 +0xdd
   > goroutine 438 [select]:
   > runtime.gopark(0xc000626e68?, 0x2?, 0xc8?, 0x3?, 0xc000626e3c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000626cc0 sp=0xc000626ca0 pc=0x13bb516
   > runtime.selectgo(0xc000626e68, 0xc000626e38, 0x0?, 0x1, 0x1?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000626e00 sp=0xc000626cc0 pc=0x13cbbdc
   > github.com/pingcap/badger.Open.func4()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:342 +0x155 fp=0xc000626fe0 sp=0xc000626e00 pc=0x3294495
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000626fe8 sp=0xc000626fe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.Open
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:339 +0x11f8
   > goroutine 439 [select]:
   > runtime.gopark(0xc000f16f08?, 0x2?, 0x0?, 0x0?, 0xc000f16ee4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00009ed68 sp=0xc00009ed48 pc=0x13bb516
   > runtime.selectgo(0xc00009ef08, 0xc000f16ee0, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00009eea8 sp=0xc00009ed68 pc=0x13cbbdc
   > github.com/pingcap/badger.(*blobGCHandler).run(0xc000120240, 0xc0000122e8)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/blob.go:468 +0xd6 fp=0xc00009efc0 sp=0xc00009eea8 pc=0x3288896
   > github.com/pingcap/badger.(*blobManager).Open.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/blob.go:292 +0x2a fp=0xc00009efe0 sp=0xc00009efc0 pc=0x328754a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00009efe8 sp=0xc00009efe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.(*blobManager).Open
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/blob.go:292 +0x5bd
   > goroutine 440 [select]:
   > runtime.gopark(0xc000f17760?, 0x2?, 0x4?, 0x30?, 0xc000f1772c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000f17598 sp=0xc000f17578 pc=0x13bb516
   > runtime.selectgo(0xc000f17760, 0xc000f17728, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000f176d8 sp=0xc000f17598 pc=0x13cbbdc
   > github.com/pingcap/badger.(*levelsController).runWorker(0xc0001c7dc0, 0xc000012570, 0x0)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:212 +0x1fb fp=0xc000f177b8 sp=0xc000f176d8 pc=0x32a297b
   > github.com/pingcap/badger.(*levelsController).startCompact.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:180 +0x2e fp=0xc000f177e0 sp=0xc000f177b8 pc=0x32a274e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000f177e8 sp=0xc000f177e0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.(*levelsController).startCompact
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:180 +0x65
   > goroutine 441 [select]:
   > runtime.gopark(0xc000f19f60?, 0x2?, 0x4?, 0x30?, 0xc000f19f2c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000f19d98 sp=0xc000f19d78 pc=0x13bb516
   > runtime.selectgo(0xc000f19f60, 0xc000f19f28, 0x0?, 0x0, 0xf4240?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000f19ed8 sp=0xc000f19d98 pc=0x13cbbdc
   > github.com/pingcap/badger.(*levelsController).runWorker(0xc0001c7dc0, 0xc000012570, 0x0)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:212 +0x1fb fp=0xc000f19fb8 sp=0xc000f19ed8 pc=0x32a297b
   > github.com/pingcap/badger.(*levelsController).startCompact.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:180 +0x2e fp=0xc000f19fe0 sp=0xc000f19fb8 pc=0x32a274e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000f19fe8 sp=0xc000f19fe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.(*levelsController).startCompact
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:180 +0x65
   > goroutine 442 [select]:
   > runtime.gopark(0xc000f18760?, 0x2?, 0x4?, 0x30?, 0xc000f1872c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000f18598 sp=0xc000f18578 pc=0x13bb516
   > runtime.selectgo(0xc000f18760, 0xc000f18728, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000f186d8 sp=0xc000f18598 pc=0x13cbbdc
   > github.com/pingcap/badger.(*levelsController).runWorker(0xc0001c7dc0, 0xc000012570, 0x1)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:212 +0x1fb fp=0xc000f187b8 sp=0xc000f186d8 pc=0x32a297b
   > github.com/pingcap/badger.(*levelsController).startCompact.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:180 +0x2e fp=0xc000f187e0 sp=0xc000f187b8 pc=0x32a274e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000f187e8 sp=0xc000f187e0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.(*levelsController).startCompact
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:180 +0x65
   > goroutine 443 [chan receive]:
   > runtime.gopark(0x1?, 0x1?, 0xc0?, 0x16?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000623ac0 sp=0xc000623aa0 pc=0x13bb516
   > runtime.chanrecv(0xc000f524e0, 0xc000623c60, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000623b50 sp=0xc000623ac0 pc=0x13854bb
   > runtime.chanrecv2(0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc000623b78 sp=0xc000623b50 pc=0x1384ff8
   > github.com/pingcap/badger.(*DB).runFlushMemTable(0xc000f70900, 0xc000701d40?)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:920 +0xdd fp=0xc000623fc0 sp=0xc000623b78 pc=0x3298efd
   > github.com/pingcap/badger.Open.func6()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:361 +0x2a fp=0xc000623fe0 sp=0xc000623fc0 pc=0x329430a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000623fe8 sp=0xc000623fe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.Open
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:361 +0x158d
   > goroutine 450 [select]:
   > runtime.gopark(0xc00009df78?, 0x3?, 0x25?, 0x48?, 0xc00009df32?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00009dd98 sp=0xc00009dd78 pc=0x13bb516
   > runtime.selectgo(0xc00009df78, 0xc00009df2c, 0x1?, 0x0, 0xc00059da00?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00009ded8 sp=0xc00009dd98 pc=0x13cbbdc
   > github.com/pingcap/badger.(*writeWorker).runWriteVLog(0xc0004c0160, 0xc000684228)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:94 +0x137 fp=0xc00009dfc0 sp=0xc00009ded8 pc=0x32b28b7
   > github.com/pingcap/badger.startWriteWorker.func2()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:64 +0x2a fp=0xc00009dfe0 sp=0xc00009dfc0 pc=0x32b238a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00009dfe8 sp=0xc00009dfe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.startWriteWorker
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:64 +0x1f9
   > goroutine 451 [chan receive, locked to thread]:
   > runtime.gopark(0xc000653e98?, 0x1456628?, 0xf?, 0x0?, 0x1?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000653e68 sp=0xc000653e48 pc=0x13bb516
   > runtime.chanrecv(0xc000fc6540, 0xc000653f88, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000653ef8 sp=0xc000653e68 pc=0x13854bb
   > runtime.chanrecv2(0xc000f6eab0?, 0x3ef16def246e2703?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc000653f20 sp=0xc000653ef8 pc=0x1384ff8
   > github.com/pingcap/badger.(*writeWorker).runWriteLSM(0xc0004c0160, 0x0?)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:141 +0x15e fp=0xc000653fc0 sp=0xc000653f20 pc=0x32b2efe
   > github.com/pingcap/badger.startWriteWorker.func3()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:65 +0x2a fp=0xc000653fe0 sp=0xc000653fc0 pc=0x32b232a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000653fe8 sp=0xc000653fe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.startWriteWorker
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:65 +0x24d
   > goroutine 452 [chan receive]:
   > runtime.gopark(0xc0011928b0?, 0xc0011928b0?, 0xb0?, 0x28?, 0xc0011928b0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0000a1ea8 sp=0xc0000a1e88 pc=0x13bb516
   > runtime.chanrecv(0xc000fc65a0, 0xc0000a1f88, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc0000a1f38 sp=0xc0000a1ea8 pc=0x13854bb
   > runtime.chanrecv2(0xc0004c0040?, 0x0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc0000a1f60 sp=0xc0000a1f38 pc=0x1384ff8
   > github.com/pingcap/badger.(*writeWorker).runMergeLSM(0x0?, 0x0?)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:154 +0x9b fp=0xc0000a1fc0 sp=0xc0000a1f60 pc=0x32b307b
   > github.com/pingcap/badger.startWriteWorker.func4()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:66 +0x2a fp=0xc0000a1fe0 sp=0xc0000a1fc0 pc=0x32b22ca
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000a1fe8 sp=0xc0000a1fe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.startWriteWorker
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:66 +0x2a5
   > goroutine 453 [select]:
   > runtime.gopark(0xc000654f88?, 0x2?, 0x0?, 0x0?, 0xc000654f4c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000654da0 sp=0xc000654d80 pc=0x13bb516
   > runtime.selectgo(0xc000654f88, 0xc000654f48, 0xc01069f730?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000654ee0 sp=0xc000654da0 pc=0x13cbbdc
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.writeDBWorker.run({0xc000fc6660?, 0xc000fbcf80?})
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:96 +0x145 fp=0xc000654fc0 sp=0xc000654ee0 pc=0x3308de5
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*dbWriter).Open.func1()
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:202 +0x2a fp=0xc000654fe0 sp=0xc000654fc0 pc=0x330996a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000654fe8 sp=0xc000654fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*dbWriter).Open
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:199 +0xc5
   > goroutine 454 [select]:
   > runtime.gopark(0xc000621e70?, 0x2?, 0x90?, 0x1e?, 0xc000621e1c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000621c58 sp=0xc000621c38 pc=0x13bb516
   > runtime.selectgo(0xc000621e70, 0xc000621e18, 0x13?, 0x0, 0xc00fcc4680?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000621d98 sp=0xc000621c58 pc=0x13cbbdc
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.writeLockWorker.run({0xc000fc66c0?, 0xc000fbcf80?})
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:148 +0x15f fp=0xc000621fc0 sp=0xc000621d98 pc=0x33093bf
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*dbWriter).Open.func2()
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:209 +0x2a fp=0xc000621fe0 sp=0xc000621fc0 pc=0x330990a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000621fe8 sp=0xc000621fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*dbWriter).Open
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:206 +0x159
   > goroutine 455 [select]:
   > runtime.gopark(0xc000f14718?, 0x2?, 0x10?, 0x0?, 0xc000f14704?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000f14588 sp=0xc000f14568 pc=0x13bb516
   > runtime.selectgo(0xc000f14718, 0xc000f14700, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000f146c8 sp=0xc000f14588 pc=0x13cbbdc
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*MVCCStore).runUpdateSafePointLoop(0xc000e5e780)
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:1550 +0x217 fp=0xc000f147c8 sp=0xc000f146c8 pc=0x32facd7
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.NewMVCCStore.func1()
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:85 +0x26 fp=0xc000f147e0 sp=0xc000f147c8 pc=0x32ed406
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000f147e8 sp=0xc000f147e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.NewMVCCStore
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:85 +0x337
   > goroutine 456 [select]:
   > runtime.gopark(0xc000f14fb0?, 0x2?, 0x0?, 0x0?, 0xc000f14f9c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000f14e28 sp=0xc000f14e08 pc=0x13bb516
   > runtime.selectgo(0xc000f14fb0, 0xc000f14f98, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000f14f68 sp=0xc000f14e28 pc=0x13cbbdc
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*MVCCStore).StartDeadlockDetection.func1()
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:1286 +0x7b fp=0xc000f14fe0 sp=0xc000f14f68 pc=0x32f895b
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000f14fe8 sp=0xc000f14fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*MVCCStore).StartDeadlockDetection
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:1284 +0xb6
   > goroutine 457 [select]:
   > runtime.gopark(0xc000d06f78?, 0x2?, 0x8?, 0x0?, 0xc000d06f3c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000d06dc0 sp=0xc000d06da0 pc=0x13bb516
   > runtime.selectgo(0xc000d06f78, 0xc000d06f38, 0xc0004a0fb0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000d06f00 sp=0xc000d06dc0 pc=0x13cbbdc
   > github.com/tikv/client-go/v2/oracle/oracles.(*pdOracle).updateTS(0xc000841570, {0x400d640, 0xc000056058}, 0x0?)
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/oracle/oracles/pd.go:229 +0x128 fp=0xc000d06fb0 sp=0xc000d06f00 pc=0x1e9b548
   > github.com/tikv/client-go/v2/oracle/oracles.NewPdOracle.func1()
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/oracle/oracles/pd.go:77 +0x32 fp=0xc000d06fe0 sp=0xc000d06fb0 pc=0x1e9a772
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000d06fe8 sp=0xc000d06fe0 pc=0x13ee6e1
   > created by github.com/tikv/client-go/v2/oracle/oracles.NewPdOracle
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/oracle/oracles/pd.go:77 +0x119
   > goroutine 458 [select]:
   > runtime.gopark(0xc000f15778?, 0x3?, 0x0?, 0x0?, 0xc000f1575a?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000f155e0 sp=0xc000f155c0 pc=0x13bb516
   > runtime.selectgo(0xc000f15778, 0xc000f15754, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000f15720 sp=0xc000f155e0 pc=0x13cbbdc
   > github.com/tikv/client-go/v2/internal/locate.(*RegionCache).asyncCheckAndResolveLoop(0xc000e5e880, 0x0?)
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/internal/locate/region_cache.go:399 +0xd1 fp=0xc000f157c0 sp=0xc000f15720 pc=0x1e6bff1
   > github.com/tikv/client-go/v2/internal/locate.NewRegionCache.func1()
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/internal/locate/region_cache.go:370 +0x2a fp=0xc000f157e0 sp=0xc000f157c0 pc=0x1e6bc6a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000f157e8 sp=0xc000f157e0 pc=0x13ee6e1
   > created by github.com/tikv/client-go/v2/internal/locate.NewRegionCache
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/internal/locate/region_cache.go:370 +0x2e6
   > goroutine 459 [select]:
   > runtime.gopark(0xc0000a2f10?, 0x2?, 0x11?, 0x30?, 0xc0000a2eac?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0000a2d10 sp=0xc0000a2cf0 pc=0x13bb516
   > runtime.selectgo(0xc0000a2f10, 0xc0000a2ea8, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0000a2e50 sp=0xc0000a2d10 pc=0x13cbbdc
   > github.com/tikv/client-go/v2/tikv.(*KVStore).runSafePointChecker(0xc00028ed80)
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/tikv/kv.go:264 +0x12b fp=0xc0000a2fc8 sp=0xc0000a2e50 pc=0x1ed6f0b
   > github.com/tikv/client-go/v2/tikv.NewKVStore.func1()
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/tikv/kv.go:187 +0x26 fp=0xc0000a2fe0 sp=0xc0000a2fc8 pc=0x1ed6d06
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000a2fe8 sp=0xc0000a2fe0 pc=0x13ee6e1
   > created by github.com/tikv/client-go/v2/tikv.NewKVStore
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/tikv/kv.go:187 +0x3d6
   > goroutine 460 [select]:
   > runtime.gopark(0xc000d02f80?, 0x2?, 0x0?, 0xbe?, 0xc000d02f44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000d02dc8 sp=0xc000d02da8 pc=0x13bb516
   > runtime.selectgo(0xc000d02f80, 0xc000d02f40, 0xc000632140?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000d02f08 sp=0xc000d02dc8 pc=0x13cbbdc
   > github.com/tikv/client-go/v2/tikv.(*KVStore).safeTSUpdater(0xc00028ed80)
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/tikv/kv.go:544 +0x165 fp=0xc000d02fc8 sp=0xc000d02f08 pc=0x1ed8e65
   > github.com/tikv/client-go/v2/tikv.NewKVStore.func2()
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/tikv/kv.go:188 +0x26 fp=0xc000d02fe0 sp=0xc000d02fc8 pc=0x1ed6ca6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000d02fe8 sp=0xc000d02fe0 pc=0x13ee6e1
   > created by github.com/tikv/client-go/v2/tikv.NewKVStore
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/tikv/kv.go:188 +0x416
   > goroutine 461 [select]:
   > runtime.gopark(0xc000551f98?, 0x2?, 0x0?, 0x0?, 0xc000551f6c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000551de8 sp=0xc000551dc8 pc=0x13bb516
   > runtime.selectgo(0xc000551f98, 0xc000551f68, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000551f28 sp=0xc000551de8 pc=0x13cbbdc
   > github.com/dgraph-io/ristretto.(*defaultPolicy).processItems(0xc0001faf90)
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.0.1/policy.go:96 +0x91 fp=0xc000551fc8 sp=0xc000551f28 pc=0x23cf0d1
   > github.com/dgraph-io/ristretto.newDefaultPolicy.func1()
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.0.1/policy.go:80 +0x26 fp=0xc000551fe0 sp=0xc000551fc8 pc=0x23cef86
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000551fe8 sp=0xc000551fe0 pc=0x13ee6e1
   > created by github.com/dgraph-io/ristretto.newDefaultPolicy
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.0.1/policy.go:80 +0x156
   > goroutine 462 [select]:
   > runtime.gopark(0xc000553798?, 0x2?, 0x0?, 0x0?, 0xc000553774?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0005535f0 sp=0xc0005535d0 pc=0x13bb516
   > runtime.selectgo(0xc000553798, 0xc000553770, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000553730 sp=0xc0005535f0 pc=0x13cbbdc
   > github.com/dgraph-io/ristretto.(*Cache).processItems(0xc000fc7500)
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.0.1/cache.go:257 +0x85 fp=0xc0005537c8 sp=0xc000553730 pc=0x23ce025
   > github.com/dgraph-io/ristretto.NewCache.func2()
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.0.1/cache.go:155 +0x26 fp=0xc0005537e0 sp=0xc0005537c8 pc=0x23cd846
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0005537e8 sp=0xc0005537e0 pc=0x13ee6e1
   > created by github.com/dgraph-io/ristretto.NewCache
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.0.1/cache.go:155 +0x485
   > goroutine 717 [select]:
   > runtime.gopark(0xc0005d9f58?, 0x4?, 0xab?, 0x62?, 0xc0005d9da8?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0005d9bf8 sp=0xc0005d9bd8 pc=0x13bb516
   > runtime.selectgo(0xc0005d9f58, 0xc0005d9da0, 0xc000d07e38?, 0x0, 0x1?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0005d9d38 sp=0xc0005d9bf8 pc=0x13cbbdc
   > github.com/pingcap/tidb/ddl.(*worker).start(0xc0106a8f20, 0xc000770180)
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl_worker.go:178 +0x318 fp=0xc0005d9fc0 sp=0xc0005d9d38 pc=0x2622e98
   > github.com/pingcap/tidb/ddl.(*ddl).Start.func2()
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:369 +0x2a fp=0xc0005d9fe0 sp=0xc0005d9fc0 pc=0x25e9a6a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0005d9fe8 sp=0xc0005d9fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/ddl.(*ddl).Start
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:369 +0x5c5
   > goroutine 719 [select]:
   > runtime.gopark(0xc000d3ff50?, 0x4?, 0x4?, 0x30?, 0xc000d3fd00?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000d3fb78 sp=0xc000d3fb58 pc=0x13bb516
   > runtime.selectgo(0xc000d3ff50, 0xc000d3fcf8, 0x400ccd0?, 0x0, 0x203004?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000d3fcb8 sp=0xc000d3fb78 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).loadSchemaInLoop(0xc0105b4120, {0x400d608, 0xc010a9e440}, 0xc0006ecd38?)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:565 +0x1aa fp=0xc000d3ffb0 sp=0xc000d3fcb8 pc=0x26a00aa
   > github.com/pingcap/tidb/domain.(*Domain).Init.func10()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:825 +0x32 fp=0xc000d3ffe0 sp=0xc000d3ffb0 pc=0x26a2b32
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000d3ffe8 sp=0xc000d3ffe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:825 +0xdeb
   > goroutine 716 [select]:
   > runtime.gopark(0xc0005ddf58?, 0x4?, 0xab?, 0x62?, 0xc0005ddda8?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0005ddbf8 sp=0xc0005ddbd8 pc=0x13bb516
   > runtime.selectgo(0xc0005ddf58, 0xc0005ddda0, 0xc000d04e38?, 0x0, 0x1?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0005ddd38 sp=0xc0005ddbf8 pc=0x13cbbdc
   > github.com/pingcap/tidb/ddl.(*worker).start(0xc0106a8e70, 0xc000770180)
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl_worker.go:178 +0x318 fp=0xc0005ddfc0 sp=0xc0005ddd38 pc=0x2622e98
   > github.com/pingcap/tidb/ddl.(*ddl).Start.func2()
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:369 +0x2a fp=0xc0005ddfe0 sp=0xc0005ddfc0 pc=0x25e9a6a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0005ddfe8 sp=0xc0005ddfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/ddl.(*ddl).Start
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:369 +0x5c5
   > goroutine 714 [select]:
   > runtime.gopark(0xc00fb95f38?, 0x2?, 0x0?, 0x0?, 0xc00fb95efc?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fb95d50 sp=0xc00fb95d30 pc=0x13bb516
   > runtime.selectgo(0xc00fb95f38, 0xc00fb95ef8, 0x1?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fb95e90 sp=0xc00fb95d50 pc=0x13cbbdc
   > github.com/pingcap/tidb/ddl.(*ddl).limitDDLJobs(0xc010c4ad90)
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl_worker.go:263 +0x173 fp=0xc00fb95fc8 sp=0xc00fb95e90 pc=0x2623fd3
   > github.com/pingcap/tidb/ddl.(*ddl).Start.func1()
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:351 +0x26 fp=0xc00fb95fe0 sp=0xc00fb95fc8 pc=0x25e9ac6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fb95fe8 sp=0xc00fb95fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/ddl.(*ddl).Start
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:351 +0x2ea
   > goroutine 715 [select]:
   > runtime.gopark(0xc0000a3f90?, 0x2?, 0x0?, 0x0?, 0xc0000a3f6c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0000a3df0 sp=0xc0000a3dd0 pc=0x13bb516
   > runtime.selectgo(0xc0000a3f90, 0xc0000a3f68, 0x15?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0000a3f30 sp=0xc0000a3df0 pc=0x13cbbdc
   > github.com/pingcap/tidb/ddl.(*delRange).startEmulator(0xc0104baae0)
   > 	/go/src/github.com/pingcap/tidb/ddl/delete_range.go:144 +0x125 fp=0xc0000a3fc8 sp=0xc0000a3f30 pc=0x262b9e5
   > github.com/pingcap/tidb/ddl.(*delRange).start.func1()
   > 	/go/src/github.com/pingcap/tidb/ddl/delete_range.go:126 +0x26 fp=0xc0000a3fe0 sp=0xc0000a3fc8 pc=0x262b7a6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000a3fe8 sp=0xc0000a3fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/ddl.(*delRange).start
   > 	/go/src/github.com/pingcap/tidb/ddl/delete_range.go:126 +0x6d
   > goroutine 853 [syscall]:
   > runtime.notetsleepg(0x65746174735f6567?, 0x6e3a226f666e695f?)
   > 	/usr/local/go/src/runtime/lock_futex.go:236 +0x34 fp=0xc00fb44fa0 sp=0xc00fb44f68 pc=0x138acd4
   > os/signal.signal_recv()
   > 	/usr/local/go/src/runtime/sigqueue.go:152 +0x2f fp=0xc00fb44fc0 sp=0xc00fb44fa0 pc=0x13ea6cf
   > os/signal.loop()
   > 	/usr/local/go/src/os/signal/signal_unix.go:23 +0x19 fp=0xc00fb44fe0 sp=0xc00fb44fc0 pc=0x2cac7f9
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fb44fe8 sp=0xc00fb44fe0 pc=0x13ee6e1
   > created by os/signal.Notify.func1.1
   > 	/usr/local/go/src/os/signal/signal.go:151 +0x2a
   > goroutine 657 [semacquire]:
   > runtime.gopark(0x2c6c6c756e3a2274?, 0x746c756166656422?, 0x20?, 0xcd?, 0x625f746c75616665?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fb40678 sp=0xc00fb40658 pc=0x13bb516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc010aeed38, 0x61?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc00fb406e0 sp=0xc00fb40678 pc=0x13cce5e
   > sync.runtime_Semacquire(0x3a2267616c46222c?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc00fb40710 sp=0xc00fb406e0 pc=0x13e9f65
   > sync.(*WaitGroup).Wait(0x626d38667475223a?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc00fb40738 sp=0xc00fb40710 pc=0x13fd1f2
   > github.com/pingcap/tidb/executor.(*HashJoinExec).waitJoinWorkersAndCloseResultChan(0xc010aeeb40)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:395 +0x33 fp=0xc00fb40778 sp=0xc00fb40738 pc=0x3061fb3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).waitJoinWorkersAndCloseResultChan-fm()
   > 	<autogenerated>:1 +0x26 fp=0xc00fb40790 sp=0xc00fb40778 pc=0x31277c6
   > github.com/pingcap/tidb/util.WithRecovery(0x656d616e222c3432?, 0x223a224f227b3a22?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc00fb407c0 sp=0xc00fb40790 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:338 +0x28 fp=0xc00fb407e0 sp=0xc00fb407c0 pc=0x3061288
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fb407e8 sp=0xc00fb407e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:338 +0x3b8
   > goroutine 854 [chan receive]:
   > runtime.gopark(0x5f8be00?, 0xc00fb45720?, 0x28?, 0xc3?, 0x7665223a224c222c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fb456a0 sp=0xc00fb45680 pc=0x13bb516
   > runtime.chanrecv(0xc000cdba40, 0xc00fb457a0, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc00fb45730 sp=0xc00fb456a0 pc=0x13854bb
   > runtime.chanrecv1(0x656e6567222c2222?, 0x74735f6465746172?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc00fb45758 sp=0xc00fb45730 pc=0x1384fb8
   > github.com/pingcap/tidb/util/signal.SetupSignalHandler.func1()
   > 	/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:37 +0x4f fp=0xc00fb457e0 sp=0xc00fb45758 pc=0x33ac32f
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fb457e8 sp=0xc00fb457e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/util/signal.SetupSignalHandler
   > 	/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:34 +0xb6
   > goroutine 873 [select]:
   > runtime.gopark(0xc011152778?, 0x2?, 0x0?, 0x0?, 0xc0111526ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc011152558 sp=0xc011152538 pc=0x13bb516
   > runtime.selectgo(0xc011152778, 0xc0111526e8, 0x3aac226?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc011152698 sp=0xc011152558 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc00069d380, {0x400d6b0?, 0xc01080b3e0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc0111527b8 sp=0xc011152698 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc0111527e0 sp=0xc0111527b8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0111527e8 sp=0xc0111527e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 851 [select]:
   > runtime.gopark(0xc01030feb0?, 0x2?, 0x16?, 0x0?, 0xc01030fe5c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01030fcc8 sp=0xc01030fca8 pc=0x13bb516
   > runtime.selectgo(0xc01030feb0, 0xc01030fe58, 0xc000cced00?, 0x0, 0x616c46222c373432?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01030fe08 sp=0xc01030fcc8 pc=0x13cbbdc
   > github.com/pingcap/tidb/util/expensivequery.(*Handle).Run(0xc010aa6078)
   > 	/go/src/github.com/pingcap/tidb/util/expensivequery/expensivequery.go:61 +0x198 fp=0xc01030ffc8 sp=0xc01030fe08 pc=0x2695d58
   > main.createServer.func1()
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:675 +0x26 fp=0xc01030ffe0 sp=0xc01030ffc8 pc=0x33b2be6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01030ffe8 sp=0xc01030ffe0 pc=0x13ee6e1
   > created by main.createServer
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:675 +0x439
   > goroutine 852 [select, locked to thread]:
   > runtime.gopark(0xc00fb447a8?, 0x2?, 0x65?, 0x78?, 0xc00fb447a4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fb44618 sp=0xc00fb445f8 pc=0x13bb516
   > runtime.selectgo(0xc00fb447a8, 0xc00fb447a0, 0x0?, 0x0, 0x222c7d2276697270?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fb44758 sp=0xc00fb44618 pc=0x13cbbdc
   > runtime.ensureSigM.func1()
   > 	/usr/local/go/src/runtime/signal_unix.go:995 +0x1b0 fp=0xc00fb447e0 sp=0xc00fb44758 pc=0x13d0070
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fb447e8 sp=0xc00fb447e0 pc=0x13ee6e1
   > created by runtime.ensureSigM
   > 	/usr/local/go/src/runtime/signal_unix.go:978 +0xbd
   > goroutine 769 [select]:
   > runtime.gopark(0xc00fb437a8?, 0x2?, 0x4?, 0x30?, 0xc00fb4377c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fb43600 sp=0xc00fb435e0 pc=0x13bb516
   > runtime.selectgo(0xc00fb437a8, 0xc00fb43778, 0x226465726f74735f?, 0x0, 0x6e65646e65706564?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fb43740 sp=0xc00fb43600 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).PlanReplayerLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1191 +0xf6 fp=0xc00fb437e0 sp=0xc00fb43740 pc=0x26a5f36
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fb437e8 sp=0xc00fb437e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).PlanReplayerLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1182 +0x6c
   > goroutine 653 [select]:
   > runtime.gopark(0xc00fb43e10?, 0x2?, 0x8?, 0xb2?, 0xc00fb43d8c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fb43be0 sp=0xc00fb43bc0 pc=0x13bb516
   > runtime.selectgo(0xc00fb43e10, 0xc00fb43d88, 0x3656160?, 0x0, 0x31e5697?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fb43d20 sp=0xc00fb43be0 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc010aeeb40, 0x1, {0xc000d082d8, 0x1, 0x1})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:441 +0x4f4 fp=0xc00fb43f10 sp=0xc00fb43d20 pc=0x30626b4
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:335 +0xb3 fp=0xc00fb43f90 sp=0xc00fb43f10 pc=0x30613d3
   > github.com/pingcap/tidb/util.WithRecovery(0x33b2be6?, 0xc010aa6078?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc00fb43fc0 sp=0xc00fb43f90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x2a fp=0xc00fb43fe0 sp=0xc00fb43fc0 pc=0x30612ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fb43fe8 sp=0xc00fb43fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x1c9
   > goroutine 655 [select]:
   > runtime.gopark(0xc01065b610?, 0x2?, 0x28?, 0xb2?, 0xc01065b58c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01065b3e0 sp=0xc01065b3c0 pc=0x13bb516
   > runtime.selectgo(0xc01065b610, 0xc01065b588, 0x0?, 0x0, 0x13cc174?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01065b520 sp=0xc01065b3e0 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc010aeeb40, 0x3, {0xc000d082d8, 0x1, 0x1})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:441 +0x4f4 fp=0xc01065b710 sp=0xc01065b520 pc=0x30626b4
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:335 +0xb3 fp=0xc01065b790 sp=0xc01065b710 pc=0x30613d3
   > github.com/pingcap/tidb/util.WithRecovery(0x5f539a0?, 0xc01065b7b8?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc01065b7c0 sp=0xc01065b790 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x2a fp=0xc01065b7e0 sp=0xc01065b7c0 pc=0x30612ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01065b7e8 sp=0xc01065b7e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x1c9
   > goroutine 652 [select]:
   > runtime.gopark(0xc00008c610?, 0x2?, 0xf8?, 0xb1?, 0xc00008c58c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008c3e0 sp=0xc00008c3c0 pc=0x13bb516
   > runtime.selectgo(0xc00008c610, 0xc00008c588, 0xc000e2b180?, 0x0, 0xc000700000?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00008c520 sp=0xc00008c3e0 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc010aeeb40, 0x0, {0xc000d082d8, 0x1, 0x1})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:441 +0x4f4 fp=0xc00008c710 sp=0xc00008c520 pc=0x30626b4
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:335 +0xb3 fp=0xc00008c790 sp=0xc00008c710 pc=0x30613d3
   > github.com/pingcap/tidb/util.WithRecovery(0x400d6b0?, 0xc010f32d50?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc00008c7c0 sp=0xc00008c790 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x2a fp=0xc00008c7e0 sp=0xc00008c7c0 pc=0x30612ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008c7e8 sp=0xc00008c7e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x1c9
   > goroutine 766 [select]:
   > runtime.gopark(0xc011a99d48?, 0x2?, 0x8?, 0xf1?, 0xc011a99c94?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc011a99b08 sp=0xc011a99ae8 pc=0x13bb516
   > runtime.selectgo(0xc011a99d48, 0xc011a99c90, 0xc0102d9260?, 0x0, 0x1?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc011a99c48 sp=0xc011a99b08 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).loadStatsWorker(0xc0105b4120)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1304 +0x485 fp=0xc011a99fc8 sp=0xc011a99c48 pc=0x26a6ea5
   > github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1247 +0x26 fp=0xc011a99fe0 sp=0xc011a99fc8 pc=0x26a6666
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc011a99fe8 sp=0xc011a99fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1247 +0x105
   > goroutine 768 [select]:
   > runtime.gopark(0xc000d3bf78?, 0x2?, 0x4?, 0x30?, 0xc000d3bf4c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000d3bdd0 sp=0xc000d3bdb0 pc=0x13bb516
   > runtime.selectgo(0xc000d3bf78, 0xc000d3bf48, 0xc0102d9260?, 0x0, 0xc000f1b658?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000d3bf10 sp=0xc000d3bdd0 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).autoAnalyzeWorker(0xc0105b4120, {0x401ea10, 0xc000fc3020})
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1425 +0x105 fp=0xc000d3bfb8 sp=0xc000d3bf10 pc=0x26a8bc5
   > github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop.func4()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1262 +0x2e fp=0xc000d3bfe0 sp=0xc000d3bfb8 pc=0x26a654e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000d3bfe8 sp=0xc000d3bfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1262 +0x31a
   > goroutine 656 [select]:
   > runtime.gopark(0xc01065d610?, 0x2?, 0x38?, 0xb2?, 0xc01065d58c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01065d3e0 sp=0xc01065d3c0 pc=0x13bb516
   > runtime.selectgo(0xc01065d610, 0xc01065d588, 0x0?, 0x0, 0x13cc174?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01065d520 sp=0xc01065d3e0 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc010aeeb40, 0x4, {0xc000d082d8, 0x1, 0x1})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:441 +0x4f4 fp=0xc01065d710 sp=0xc01065d520 pc=0x30626b4
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:335 +0xb3 fp=0xc01065d790 sp=0xc01065d710 pc=0x30613d3
   > github.com/pingcap/tidb/util.WithRecovery(0x5f539a0?, 0xc01065d7b8?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc01065d7c0 sp=0xc01065d790 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x2a fp=0xc01065d7e0 sp=0xc01065d7c0 pc=0x30612ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01065d7e8 sp=0xc01065d7e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x1c9
   > goroutine 797 [select]:
   > runtime.gopark(0xc0006eb740?, 0x2?, 0x2e?, 0xab?, 0xc0006eb704?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0006eb588 sp=0xc0006eb568 pc=0x13bb516
   > runtime.selectgo(0xc0006eb740, 0xc0006eb700, 0x3647520?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0006eb6c8 sp=0xc0006eb588 pc=0x13cbbdc
   > github.com/pingcap/tidb/util/topsql/reporter.(*RemoteTopSQLReporter).reportWorker(0xc00fbaa540)
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:499 +0x1ae fp=0xc0006eb7c8 sp=0xc0006eb6c8 pc=0x254924e
   > github.com/pingcap/tidb/util/topsql/reporter.NewRemoteTopSQLReporter.func2()
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:161 +0x26 fp=0xc0006eb7e0 sp=0xc0006eb7c8 pc=0x2546bc6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0006eb7e8 sp=0xc0006eb7e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/util/topsql/reporter.NewRemoteTopSQLReporter
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:161 +0x1f6
   > goroutine 654 [select]:
   > runtime.gopark(0xc01065e610?, 0x2?, 0x18?, 0xb2?, 0xc01065e58c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01065e3e0 sp=0xc01065e3c0 pc=0x13bb516
   > runtime.selectgo(0xc01065e610, 0xc01065e588, 0x0?, 0x0, 0x13cc174?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01065e520 sp=0xc01065e3e0 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc010aeeb40, 0x2, {0xc000d082d8, 0x1, 0x1})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:441 +0x4f4 fp=0xc01065e710 sp=0xc01065e520 pc=0x30626b4
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:335 +0xb3 fp=0xc01065e790 sp=0xc01065e710 pc=0x30613d3
   > github.com/pingcap/tidb/util.WithRecovery(0x5f539a0?, 0xc01065e7b8?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc01065e7c0 sp=0xc01065e790 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x2a fp=0xc01065e7e0 sp=0xc01065e7c0 pc=0x30612ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01065e7e8 sp=0xc01065e7e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x1c9
   > goroutine 850 [chan receive]:
   > runtime.gopark(0xc0005305a8?, 0xc0009c0820?, 0x48?, 0xee?, 0x13d8de5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01065edf0 sp=0xc01065edd0 pc=0x13bb516
   > runtime.chanrecv(0xc000c51500, 0xc01065ef38, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc01065ee80 sp=0xc01065edf0 pc=0x13854bb
   > runtime.chanrecv2(0x9356907420000?, 0x2?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc01065eea8 sp=0xc01065ee80 pc=0x1384ff8
   > github.com/pingcap/tidb/server.NewServer.func1()
   > 	/go/src/github.com/pingcap/tidb/server/server.go:209 +0x98 fp=0xc01065efe0 sp=0xc01065eea8 pc=0x31e1638
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01065efe8 sp=0xc01065efe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/server.NewServer
   > 	/go/src/github.com/pingcap/tidb/server/server.go:208 +0x32a
   > goroutine 720 [select]:
   > runtime.gopark(0xc0006ed778?, 0x3?, 0x4?, 0x30?, 0xc0006ed712?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0006ed560 sp=0xc0006ed540 pc=0x13bb516
   > runtime.selectgo(0xc0006ed778, 0xc0006ed70c, 0x2?, 0x0, 0xc0104d41a0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0006ed6a0 sp=0xc0006ed560 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).topNSlowQueryLoop(0xc0105b4120)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:455 +0x194 fp=0xc0006ed7c8 sp=0xc0006ed6a0 pc=0x269e914
   > github.com/pingcap/tidb/domain.(*Domain).Init.func11()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:828 +0x26 fp=0xc0006ed7e0 sp=0xc0006ed7c8 pc=0x26a2ac6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0006ed7e8 sp=0xc0006ed7e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:828 +0xe52
   > goroutine 721 [select]:
   > runtime.gopark(0xc0006a3ef8?, 0x3?, 0x0?, 0x0?, 0xc0006a3e82?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0006a3d08 sp=0xc0006a3ce8 pc=0x13bb516
   > runtime.selectgo(0xc0006a3ef8, 0xc0006a3e7c, 0xc00fec8960?, 0x0, 0x400d678?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0006a3e48 sp=0xc0006a3d08 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).infoSyncerKeeper(0xc0105b4120)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:487 +0x165 fp=0xc0006a3fc8 sp=0xc0006a3e48 pc=0x269ee45
   > github.com/pingcap/tidb/domain.(*Domain).Init.func12()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:829 +0x26 fp=0xc0006a3fe0 sp=0xc0006a3fc8 pc=0x26a2a66
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0006a3fe8 sp=0xc0006a3fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:829 +0xe95
   > goroutine 722 [select]:
   > runtime.gopark(0xc0006e7ef0?, 0x2?, 0x0?, 0x0?, 0xc0006e7ebc?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000d2fd38 sp=0xc000d2fd18 pc=0x13bb516
   > runtime.selectgo(0xc000d2fef0, 0xc0006e7eb8, 0x4020f40?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000d2fe78 sp=0xc000d2fd38 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).globalConfigSyncerKeeper(0xc0105b4120)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:510 +0xe5 fp=0xc000d2ffc8 sp=0xc000d2fe78 pc=0x269f405
   > github.com/pingcap/tidb/domain.(*Domain).Init.func13()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:830 +0x26 fp=0xc000d2ffe0 sp=0xc000d2ffc8 pc=0x26a2a06
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000d2ffe8 sp=0xc000d2ffe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:830 +0xedc
   > goroutine 723 [select]:
   > runtime.gopark(0xc000d30e78?, 0x3?, 0x8?, 0x0?, 0xc000d30df2?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000d30c78 sp=0xc000d30c58 pc=0x13bb516
   > runtime.selectgo(0xc000d30e78, 0xc000d30dec, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000d30db8 sp=0xc000d30c78 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).topologySyncerKeeper(0xc0105b4120)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:533 +0x165 fp=0xc000d30fc8 sp=0xc000d30db8 pc=0x269f8c5
   > github.com/pingcap/tidb/domain.(*Domain).Init.func14()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:834 +0x26 fp=0xc000d30fe0 sp=0xc000d30fc8 pc=0x26a29a6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000d30fe8 sp=0xc000d30fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:834 +0xf3d
   > goroutine 765 [select]:
   > runtime.gopark(0xc00049dfa8?, 0x2?, 0x4?, 0x30?, 0xc00049df84?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00049de08 sp=0xc00049dde8 pc=0x13bb516
   > runtime.selectgo(0xc00049dfa8, 0xc00049df80, 0xc0107429c0?, 0x0, 0xc000cdaf60?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00049df48 sp=0xc00049de08 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).TelemetryRotateSubWindowLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1169 +0xcc fp=0xc00049dfe0 sp=0xc00049df48 pc=0x26a5c4c
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00049dfe8 sp=0xc00049dfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).TelemetryRotateSubWindowLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1162 +0x8f
   > goroutine 733 [select]:
   > runtime.gopark(0xc01105ef28?, 0x2?, 0x4?, 0x30?, 0xc01105eed4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01105ed48 sp=0xc01105ed28 pc=0x13bb516
   > runtime.selectgo(0xc01105ef28, 0xc01105eed0, 0xc0006d3000?, 0x0, 0xc00067db80?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01105ee88 sp=0xc01105ed48 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).handleEvolvePlanTasksLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1106 +0x107 fp=0xc01105efe0 sp=0xc01105ee88 pc=0x26a4fe7
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01105efe8 sp=0xc01105efe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).handleEvolvePlanTasksLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1099 +0xe5
   > goroutine 732 [select]:
   > runtime.gopark(0xc01030be90?, 0x3?, 0xe0?, 0x4a?, 0xc01030be02?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01030bc70 sp=0xc01030bc50 pc=0x13bb516
   > runtime.selectgo(0xc01030be90, 0xc01030bdfc, 0x3a8be78?, 0x0, 0x141f32a?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01030bdb0 sp=0xc01030bc70 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).globalBindHandleWorkerLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1071 +0x16f fp=0xc01030bfe0 sp=0xc01030bdb0 pc=0x26a476f
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01030bfe8 sp=0xc01030bfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).globalBindHandleWorkerLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1058 +0xad
   > goroutine 788 [select]:
   > runtime.gopark(0xc000d04f18?, 0x3?, 0x4?, 0x30?, 0xc000d04e8a?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000d04cc8 sp=0xc000d04ca8 pc=0x13bb516
   > runtime.selectgo(0xc000d04f18, 0xc000d04e84, 0xc0006eb788?, 0x0, 0x13bb516?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000d04e08 sp=0xc000d04cc8 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).LoadSysVarCacheLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:989 +0x145 fp=0xc000d04fe0 sp=0xc000d04e08 pc=0x26a3dc5
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000d04fe8 sp=0xc000d04fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).LoadSysVarCacheLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:980 +0x172
   > goroutine 870 [select]:
   > runtime.gopark(0xc011148778?, 0x2?, 0x0?, 0x0?, 0xc0111486ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc011148558 sp=0xc011148538 pc=0x13bb516
   > runtime.selectgo(0xc011148778, 0xc0111486e8, 0x3aac226?, 0x0, 0xabcfc939?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc011148698 sp=0xc011148558 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc00069d2c0, {0x400d6b0?, 0xc01080b3e0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc0111487b8 sp=0xc011148698 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc0111487e0 sp=0xc0111487b8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0111487e8 sp=0xc0111487e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 625 [select]:
   > runtime.gopark(0xc000553f18?, 0x3?, 0x4?, 0x30?, 0xc000553e9a?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000650cd8 sp=0xc000650cb8 pc=0x13bb516
   > runtime.selectgo(0xc000650f18, 0xc000553e94, 0xc000d14240?, 0x0, 0xc000cda660?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000650e18 sp=0xc000650cd8 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).LoadPrivilegeLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:939 +0x145 fp=0xc000650fe0 sp=0xc000650e18 pc=0x26a3585
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000650fe8 sp=0xc000650fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).LoadPrivilegeLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:930 +0x205
   > goroutine 807 [chan receive]:
   > runtime.gopark(0x50?, 0xc00fc44f00?, 0x8?, 0x4d?, 0x138c1bf?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000624c80 sp=0xc000624c60 pc=0x13bb516
   > runtime.chanrecv(0xc000c518c0, 0xc000624d48, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000624d10 sp=0xc000624c80 pc=0x13854bb
   > runtime.chanrecv2(0x141e886?, 0xc0006aeb10?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc000624d38 sp=0xc000624d10 pc=0x1384ff8
   > github.com/soheilhy/cmux.muxListener.Accept(...)
   > 	/go/pkg/mod/github.com/soheilhy/cmux@v0.1.4/cmux.go:229
   > github.com/soheilhy/cmux.(*muxListener).Accept(0x5828400?)
   > 	<autogenerated>:1 +0x45 fp=0xc000624d68 sp=0xc000624d38 pc=0x2dc7625
   > net/http.(*onceCloseListener).Accept(0x400d640?)
   > 	<autogenerated>:1 +0x2a fp=0xc000624d80 sp=0xc000624d68 pc=0x16e0c6a
   > net/http.(*Server).Serve(0xc000f10ff0, {0x400cb50, 0xc000ca4be8})
   > 	/usr/local/go/src/net/http/server.go:3070 +0x385 fp=0xc000624eb0 sp=0xc000624d80 pc=0x16b6f45
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer.func2()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:462 +0x3e fp=0xc000624f90 sp=0xc000624eb0 pc=0x31dadbe
   > github.com/pingcap/tidb/util.WithRecovery(0x400d640?, 0xc000056058?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc000624fc0 sp=0xc000624f90 pc=0x1ffabd3
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer.func6()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:461 +0x28 fp=0xc000624fe0 sp=0xc000624fc0 pc=0x31dad48
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000624fe8 sp=0xc000624fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:461 +0x4ea
   > goroutine 866 [IO wait]:
   > runtime.gopark(0xc000627b90?, 0x13847dd?, 0x20?, 0x8e?, 0xc000627b78?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000627b08 sp=0xc000627ae8 pc=0x13bb516
   > runtime.netpollblock(0x7fa158314f58?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/netpoll.go:526 +0xf7 fp=0xc000627b40 sp=0xc000627b08 pc=0x13b38f7
   > internal/poll.runtime_pollWait(0x7fa17fe267c8, 0x72)
   > 	/usr/local/go/src/runtime/netpoll.go:305 +0x89 fp=0xc000627b60 sp=0xc000627b40 pc=0x13e7d09
   > internal/poll.(*pollDesc).wait(0xc001090f80?, 0x1395201?, 0x0)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:84 +0x32 fp=0xc000627b88 sp=0xc000627b60 pc=0x1465192
   > internal/poll.(*pollDesc).waitRead(...)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:89
   > internal/poll.(*FD).Accept(0xc001090f80)
   > 	/usr/local/go/src/internal/poll/fd_unix.go:614 +0x234 fp=0xc000627c20 sp=0xc000627b88 pc=0x146a594
   > net.(*netFD).accept(0xc001090f80)
   > 	/usr/local/go/src/net/fd_unix.go:172 +0x35 fp=0xc000627cd8 sp=0xc000627c20 pc=0x1589055
   > net.(*UnixListener).accept(0xc010662b40?)
   > 	/usr/local/go/src/net/unixsock_posix.go:166 +0x1c fp=0xc000627d00 sp=0xc000627cd8 pc=0x15aba1c
   > net.(*UnixListener).Accept(0xc010688480)
   > 	/usr/local/go/src/net/unixsock.go:260 +0x3d fp=0xc000627d30 sp=0xc000627d00 pc=0x15aa0bd
   > github.com/pingcap/tidb/server.(*Server).startNetworkListener(0xc000cced00, {0x400b9e0, 0xc010688480}, 0x1, 0xc0103fe570?)
   > 	/go/src/github.com/pingcap/tidb/server/server.go:383 +0xa6 fp=0xc000627fa8 sp=0xc000627d30 pc=0x31e25a6
   > github.com/pingcap/tidb/server.(*Server).Run.func2()
   > 	/go/src/github.com/pingcap/tidb/server/server.go:369 +0x37 fp=0xc000627fe0 sp=0xc000627fa8 pc=0x31e2477
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000627fe8 sp=0xc000627fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/server.(*Server).Run
   > 	/go/src/github.com/pingcap/tidb/server/server.go:369 +0x1db
   > goroutine 890 [chan receive]:
   > runtime.gopark(0x13c37d1?, 0xc0109c4b50?, 0x0?, 0x38?, 0xc000705e40?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0109c4b40 sp=0xc0109c4b20 pc=0x13bb516
   > runtime.chanrecv(0xc0111362a0, 0xc0109c4c90, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc0109c4bd0 sp=0xc0109c4b40 pc=0x13854bb
   > runtime.chanrecv2(0xc010aef680?, 0x400d6b0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc0109c4bf8 sp=0xc0109c4bd0 pc=0x1384ff8
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Next(0xc010aef680, {0x400d6b0?, 0xc01080b3e0?}, 0xc010f694a0)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:681 +0x652 fp=0xc0109c4cb8 sp=0xc0109c4bf8 pc=0x3064d52
   > github.com/pingcap/tidb/executor.Next({0x400d6b0, 0xc01080b3e0}, {0x40101a0, 0xc010aef680}, 0xc010f694a0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:286 +0x4a8 fp=0xc0109c4df8 sp=0xc0109c4cb8 pc=0x2fef688
   > github.com/pingcap/tidb/executor.(*ProjectionExec).unParallelExecute(0xc010f20d80, {0x400d6b0?, 0xc01080b3e0?}, 0xc010f69db0)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:194 +0xb8 fp=0xc0109c4e48 sp=0xc0109c4df8 pc=0x3098758
   > github.com/pingcap/tidb/executor.(*ProjectionExec).Next(0xc010f20d80, {0x400d6b0, 0xc01080b3e0}, 0xc010531930?)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:180 +0x5a fp=0xc0109c4e80 sp=0xc0109c4e48 pc=0x309861a
   > github.com/pingcap/tidb/executor.Next({0x400d6b0, 0xc01080b3e0}, {0x4010760, 0xc010f20d80}, 0xc010f69db0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:286 +0x4a8 fp=0xc0109c4fc0 sp=0xc0109c4e80 pc=0x2fef688
   > github.com/pingcap/tidb/executor.(*recordSet).Next(0xc010f69d10, {0x400d6b0?, 0xc01080b3e0?}, 0xc010f69db0)
   > 	/go/src/github.com/pingcap/tidb/executor/adapter.go:147 +0xbf fp=0xc0109c5050 sp=0xc0109c4fc0 pc=0x2f60d1f
   > github.com/pingcap/tidb/session.(*execStmtResult).Next(0xc01080b3b0?, {0x400d6b0?, 0xc01080b3e0?}, 0xc0102c2000?)
   > 	<autogenerated>:1 +0x34 fp=0xc0109c5080 sp=0xc0109c5050 pc=0x315d9d4
   > github.com/pingcap/tidb/server.(*tidbResultSet).Next(0xba023c3d?, {0x400d6b0?, 0xc01080b3e0?}, 0xc010665380?)
   > 	/go/src/github.com/pingcap/tidb/server/driver_tidb.go:306 +0x2b fp=0xc0109c50b0 sp=0xc0109c5080 pc=0x31c5f6b
   > github.com/pingcap/tidb/server.(*clientConn).writeChunks(0xc010445cc0, {0x400d6b0, 0xc01080b3e0}, {0x401c468, 0xc010f69d60}, 0x0, 0x109c?)
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:2103 +0x15e fp=0xc0109c5170 sp=0xc0109c50b0 pc=0x31bd47e
   > github.com/pingcap/tidb/server.(*clientConn).writeResultset(0xc010445cc0, {0x400d6b0, 0xc01080b3e0}, {0x401c468, 0xc010f69d60}, 0x80?, 0x3, 0x23b?)
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:2052 +0x174 fp=0xc0109c5220 sp=0xc0109c5170 pc=0x31bcc74
   > github.com/pingcap/tidb/server.(*clientConn).handleStmt(0xc010445cc0, {0x400d608, 0xc01035c040}, {0x401fff0, 0xc00fc890e0}, {0x5f8a1a8, 0x0, 0x0}, 0x1)
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:1932 +0x3d6 fp=0xc0109c52f0 sp=0xc0109c5220 pc=0x31bbab6
   > github.com/pingcap/tidb/server.(*clientConn).handleQuery(0xc010445cc0, {0x400d608, 0xc01035c040}, {0xc000cbcea1, 0x18c})
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:1775 +0x774 fp=0xc0109c5468 sp=0xc0109c52f0 pc=0x31ba494
   > github.com/pingcap/tidb/server.(*clientConn).dispatch(0xc010445cc0, {0x400d6b0, 0xc00fcb3a10?}, {0xc000cbcea0, 0x18d, 0x18d})
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:1279 +0x1025 fp=0xc0109c5858 sp=0xc0109c5468 pc=0x31b6045
   > github.com/pingcap/tidb/server.(*clientConn).Run(0xc010445cc0, {0x400d6b0, 0xc00fcb3a10})
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:1034 +0x253 fp=0xc0109c5e18 sp=0xc0109c5858 pc=0x31b2b33
   > github.com/pingcap/tidb/server.(*Server).onConn(0xc000cced00, 0xc010445cc0)
   > 	/go/src/github.com/pingcap/tidb/server/server.go:550 +0x6c5 fp=0xc0109c5fc0 sp=0xc0109c5e18 pc=0x31e4165
   > github.com/pingcap/tidb/server.(*Server).startNetworkListener.func2()
   > 	/go/src/github.com/pingcap/tidb/server/server.go:453 +0x2a fp=0xc0109c5fe0 sp=0xc0109c5fc0 pc=0x31e300a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0109c5fe8 sp=0xc0109c5fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/server.(*Server).startNetworkListener
   > 	/go/src/github.com/pingcap/tidb/server/server.go:453 +0x5ca
   > goroutine 767 [select]:
   > runtime.gopark(0xc01010df28?, 0x6?, 0x50?, 0x60?, 0xc01010dbb4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01010da20 sp=0xc01010da00 pc=0x13bb516
   > runtime.selectgo(0xc01010df28, 0xc01010dba8, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01010db60 sp=0xc01010da20 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).updateStatsWorker(0xc0105b4120, {0x309938e?, 0xc0105bad80?}, {0x401ea10, 0xc000fc3020})
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1372 +0x234 fp=0xc01010dfa8 sp=0xc01010db60 pc=0x26a7e54
   > github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop.func3()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1259 +0x36 fp=0xc01010dfe0 sp=0xc01010dfa8 pc=0x26a65b6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01010dfe8 sp=0xc01010dfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1259 +0x29a
   > goroutine 801 [IO wait]:
   > runtime.gopark(0x18?, 0xc000100800?, 0xd8?, 0x4c?, 0xc000651b70?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000651b00 sp=0xc000651ae0 pc=0x13bb516
   > runtime.netpollblock(0x14?, 0x2432d05?, 0x0?)
   > 	/usr/local/go/src/runtime/netpoll.go:526 +0xf7 fp=0xc000651b38 sp=0xc000651b00 pc=0x13b38f7
   > internal/poll.runtime_pollWait(0x7fa17fe268b8, 0x72)
   > 	/usr/local/go/src/runtime/netpoll.go:305 +0x89 fp=0xc000651b58 sp=0xc000651b38 pc=0x13e7d09
   > internal/poll.(*pollDesc).wait(0xc001090f00?, 0xc000651d20?, 0x0)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:84 +0x32 fp=0xc000651b80 sp=0xc000651b58 pc=0x1465192
   > internal/poll.(*pollDesc).waitRead(...)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:89
   > internal/poll.(*FD).Accept(0xc001090f00)
   > 	/usr/local/go/src/internal/poll/fd_unix.go:614 +0x234 fp=0xc000651c18 sp=0xc000651b80 pc=0x146a594
   > net.(*netFD).accept(0xc001090f00)
   > 	/usr/local/go/src/net/fd_unix.go:172 +0x35 fp=0xc000651cd0 sp=0xc000651c18 pc=0x1589055
   > net.(*TCPListener).accept(0xc00fb66138)
   > 	/usr/local/go/src/net/tcpsock_posix.go:142 +0x28 fp=0xc000651d00 sp=0xc000651cd0 pc=0x15a5088
   > net.(*TCPListener).Accept(0xc00fb66138)
   > 	/usr/local/go/src/net/tcpsock.go:288 +0x3d fp=0xc000651d30 sp=0xc000651d00 pc=0x15a40fd
   > github.com/pingcap/tidb/server.(*Server).startNetworkListener(0xc000cced00, {0x400b9b0, 0xc00fb66138}, 0x0, 0xc01056bb60?)
   > 	/go/src/github.com/pingcap/tidb/server/server.go:383 +0xa6 fp=0xc000651fa8 sp=0xc000651d30 pc=0x31e25a6
   > github.com/pingcap/tidb/server.(*Server).Run.func1()
   > 	/go/src/github.com/pingcap/tidb/server/server.go:368 +0x34 fp=0xc000651fe0 sp=0xc000651fa8 pc=0x31e24d4
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000651fe8 sp=0xc000651fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/server.(*Server).Run
   > 	/go/src/github.com/pingcap/tidb/server/server.go:368 +0x145
   > goroutine 800 [IO wait]:
   > runtime.gopark(0xf?, 0xc00fc68410?, 0x3?, 0x0?, 0xc0005bf8d0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0005bf860 sp=0xc0005bf840 pc=0x13bb516
   > runtime.netpollblock(0x203003?, 0xfc68410?, 0xc0?)
   > 	/usr/local/go/src/runtime/netpoll.go:526 +0xf7 fp=0xc0005bf898 sp=0xc0005bf860 pc=0x13b38f7
   > internal/poll.runtime_pollWait(0x7fa17fe266d8, 0x72)
   > 	/usr/local/go/src/runtime/netpoll.go:305 +0x89 fp=0xc0005bf8b8 sp=0xc0005bf898 pc=0x13e7d09
   > internal/poll.(*pollDesc).wait(0xc001091180?, 0xc00fc5e630?, 0x0)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:84 +0x32 fp=0xc0005bf8e0 sp=0xc0005bf8b8 pc=0x1465192
   > internal/poll.(*pollDesc).waitRead(...)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:89
   > internal/poll.(*FD).Accept(0xc001091180)
   > 	/usr/local/go/src/internal/poll/fd_unix.go:614 +0x234 fp=0xc0005bf978 sp=0xc0005bf8e0 pc=0x146a594
   > net.(*netFD).accept(0xc001091180)
   > 	/usr/local/go/src/net/fd_unix.go:172 +0x35 fp=0xc0005bfa30 sp=0xc0005bf978 pc=0x1589055
   > net.(*TCPListener).accept(0xc00fb66150)
   > 	/usr/local/go/src/net/tcpsock_posix.go:142 +0x28 fp=0xc0005bfa60 sp=0xc0005bfa30 pc=0x15a5088
   > net.(*TCPListener).Accept(0xc00fb66150)
   > 	/usr/local/go/src/net/tcpsock.go:288 +0x3d fp=0xc0005bfa90 sp=0xc0005bfa60 pc=0x15a40fd
   > github.com/soheilhy/cmux.(*cMux).Serve(0xc010a35ea0)
   > 	/go/pkg/mod/github.com/soheilhy/cmux@v0.1.4/cmux.go:162 +0xa9 fp=0xc0005bfb20 sp=0xc0005bfa90 pc=0x2dc5da9
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer(0xc000cced00, 0xc00056be00)
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:466 +0x4f7 fp=0xc0005bfc90 sp=0xc0005bfb20 pc=0x31dab17
   > github.com/pingcap/tidb/server.(*Server).startHTTPServer(0xc000cced00)
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:442 +0x15d0 fp=0xc0005bffc8 sp=0xc0005bfc90 pc=0x31d9f10
   > github.com/pingcap/tidb/server.(*Server).startStatusHTTP.func1()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:62 +0x26 fp=0xc0005bffe0 sp=0xc0005bffc8 pc=0x31d65c6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0005bffe8 sp=0xc0005bffe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/server.(*Server).startStatusHTTP
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:62 +0x56
   > goroutine 806 [chan receive]:
   > runtime.gopark(0x3a8bf40?, 0xc000d31cf8?, 0xfc?, 0xb?, 0xa?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000d31cb0 sp=0xc000d31c90 pc=0x13bb516
   > runtime.chanrecv(0xc000c51920, 0xc000d31d78, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000d31d40 sp=0xc000d31cb0 pc=0x13854bb
   > runtime.chanrecv2(0xc010d01680?, 0x2?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc000d31d68 sp=0xc000d31d40 pc=0x1384ff8
   > github.com/soheilhy/cmux.muxListener.Accept(...)
   > 	/go/pkg/mod/github.com/soheilhy/cmux@v0.1.4/cmux.go:229
   > github.com/soheilhy/cmux.(*muxListener).Accept(0x3ff0f40?)
   > 	<autogenerated>:1 +0x45 fp=0xc000d31d98 sp=0xc000d31d68 pc=0x2dc7625
   > google.golang.org/grpc.(*Server).Serve(0xc0009a6000, {0x400cb50, 0xc000ca4c00})
   > 	/go/pkg/mod/google.golang.org/grpc@v1.29.1/server.go:621 +0x362 fp=0xc000d31eb0 sp=0xc000d31d98 pc=0x19749a2
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer.func1()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:457 +0x3e fp=0xc000d31f90 sp=0xc000d31eb0 pc=0x31db01e
   > github.com/pingcap/tidb/util.WithRecovery(0x400d640?, 0xc000c516e0?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc000d31fc0 sp=0xc000d31f90 pc=0x1ffabd3
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer.func5()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:456 +0x28 fp=0xc000d31fe0 sp=0xc000d31fc0 pc=0x31dafa8
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000d31fe8 sp=0xc000d31fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:456 +0x42c
   > goroutine 871 [select]:
   > runtime.gopark(0xc00008d778?, 0x2?, 0x1?, 0x0?, 0xc00008d6ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008d558 sp=0xc00008d538 pc=0x13bb516
   > runtime.selectgo(0xc00008d778, 0xc00008d6e8, 0x3aac226?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00008d698 sp=0xc00008d558 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc00069d300, {0x400d6b0?, 0xc01080b3e0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc00008d7b8 sp=0xc00008d698 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc00008d7e0 sp=0xc00008d7b8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008d7e8 sp=0xc00008d7e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 764 [select]:
   > runtime.gopark(0xc00054d728?, 0x2?, 0x4?, 0x30?, 0xc00054d6d4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00054d548 sp=0xc00054d528 pc=0x13bb516
   > runtime.selectgo(0xc00054d728, 0xc00054d6d0, 0x9?, 0x0, 0x15?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00054d688 sp=0xc00054d548 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).TelemetryReportLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1140 +0x11c fp=0xc00054d7e0 sp=0xc00054d688 pc=0x26a573c
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00054d7e8 sp=0xc00054d7e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).TelemetryReportLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1132 +0x285
   > goroutine 798 [sleep]:
   > runtime.gopark(0x21e7c52c5051?, 0x2fe82d7?, 0x88?, 0xbf?, 0x25412d5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01065bf58 sp=0xc01065bf38 pc=0x13bb516
   > time.Sleep(0x3b9aca00)
   > 	/usr/local/go/src/runtime/time.go:195 +0x135 fp=0xc01065bf98 sp=0xc01065bf58 pc=0x13eaf15
   > github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).startCPUProfileWorker(0xc01065bfb8?)
   > 	/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:115 +0x65 fp=0xc01065bfc8 sp=0xc01065bf98 pc=0x2540065
   > github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).Run.func1()
   > 	/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:93 +0x26 fp=0xc01065bfe0 sp=0xc01065bfc8 pc=0x253fea6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01065bfe8 sp=0xc01065bfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).Run
   > 	/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:93 +0xca
   > goroutine 796 [select]:
   > runtime.gopark(0xc0006e7f80?, 0x3?, 0x4?, 0x30?, 0xc0006e7f3a?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0006e7da8 sp=0xc0006e7d88 pc=0x13bb516
   > runtime.selectgo(0xc0006e7f80, 0xc0006e7f34, 0x0?, 0x0, 0xc0006e7f10?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0006e7ee8 sp=0xc0006e7da8 pc=0x13cbbdc
   > github.com/pingcap/tidb/util/topsql/reporter.(*RemoteTopSQLReporter).collectWorker(0xc00fbaa540)
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:327 +0x13a fp=0xc0006e7fc8 sp=0xc0006e7ee8 pc=0x2547eda
   > github.com/pingcap/tidb/util/topsql/reporter.NewRemoteTopSQLReporter.func1()
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:160 +0x26 fp=0xc0006e7fe0 sp=0xc0006e7fc8 pc=0x2546c26
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0006e7fe8 sp=0xc0006e7fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/util/topsql/reporter.NewRemoteTopSQLReporter
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:160 +0x1b6
   > goroutine 795 [chan receive]:
   > runtime.gopark(0xc00fedc2d0?, 0x400d678?, 0x88?, 0x86?, 0x309a506?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0006e8660 sp=0xc0006e8640 pc=0x13bb516
   > runtime.chanrecv(0xc000cdbaa0, 0xc0006e8780, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc0006e86f0 sp=0xc0006e8660 pc=0x13854bb
   > runtime.chanrecv1(0x0?, 0x309a4e0?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc0006e8718 sp=0xc0006e86f0 pc=0x1384fb8
   > github.com/pingcap/tidb/util/signal.SetupSignalHandler.func2()
   > 	/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:53 +0x45 fp=0xc0006e87e0 sp=0xc0006e8718 pc=0x33ac105
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0006e87e8 sp=0xc0006e87e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/util/signal.SetupSignalHandler
   > 	/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:52 +0x19f
   > goroutine 799 [chan receive]:
   > runtime.gopark(0x1?, 0x2?, 0x0?, 0x0?, 0x4e223a22746c7561?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fb3fde0 sp=0xc00fb3fdc0 pc=0x13bb516
   > runtime.chanrecv(0xc0007009c0, 0xc00fb3ff08, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc00fb3fe70 sp=0xc00fb3fde0 pc=0x13854bb
   > runtime.chanrecv1(0xc00fb3ff78?, 0xc00fb3fee8?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc00fb3fe98 sp=0xc00fb3fe70 pc=0x1384fb8
   > github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).startAnalyzeProfileWorker(0xc000a8c210)
   > 	/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:142 +0x7c fp=0xc00fb3ffc8 sp=0xc00fb3fe98 pc=0x25402bc
   > github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).Run.func2()
   > 	/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:94 +0x26 fp=0xc00fb3ffe0 sp=0xc00fb3ffc8 pc=0x253fe46
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fb3ffe8 sp=0xc00fb3ffe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).Run
   > 	/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:94 +0x10a
   > goroutine 872 [select]:
   > runtime.gopark(0xc011151f78?, 0x2?, 0x0?, 0x0?, 0xc011151eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc011151d58 sp=0xc011151d38 pc=0x13bb516
   > runtime.selectgo(0xc011151f78, 0xc011151ee8, 0x3aac226?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc011151e98 sp=0xc011151d58 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc00069d340, {0x400d6b0?, 0xc01080b3e0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc011151fb8 sp=0xc011151e98 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc011151fe0 sp=0xc011151fb8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc011151fe8 sp=0xc011151fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 869 [select]:
   > runtime.gopark(0xc01105ff78?, 0x2?, 0xa0?, 0xfd?, 0xc01105feec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01105fd58 sp=0xc01105fd38 pc=0x13bb516
   > runtime.selectgo(0xc01105ff78, 0xc01105fee8, 0xc000cb7200?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01105fe98 sp=0xc01105fd58 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc00069d280, {0x400d6b0?, 0xc01080b3e0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc01105ffb8 sp=0xc01105fe98 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc01105ffe0 sp=0xc01105ffb8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01105ffe8 sp=0xc01105ffe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 651 [select]:
   > runtime.gopark(0xc0006a1e30?, 0x2?, 0x80?, 0x57?, 0xc0006a1e1c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0006a1ca8 sp=0xc0006a1c88 pc=0x13bb516
   > runtime.selectgo(0xc0006a1e30, 0xc0006a1e18, 0xc0110928a0?, 0x0, 0x2fef900?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0006a1de8 sp=0xc0006a1ca8 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).wait4BuildSide(0xc010aeeb40)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:242 +0x6f fp=0xc0006a1e60 sp=0xc0006a1de8 pc=0x30605ef
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchProbeSideChunks(0xc010aeeb40, {0x400d6b0, 0xc01080b3e0})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:221 +0x233 fp=0xc0006a1f28 sp=0xc0006a1e60 pc=0x3060333
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:322 +0x8f fp=0xc0006a1f90 sp=0xc0006a1f28 pc=0x306156f
   > github.com/pingcap/tidb/util.WithRecovery(0xc010a9e440?, 0xc0006ecd38?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc0006a1fc0 sp=0xc0006a1f90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func3()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:320 +0x2a fp=0xc0006a1fe0 sp=0xc0006a1fc0 pc=0x30614aa
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0006a1fe8 sp=0xc0006a1fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:320 +0x14f
   > goroutine 650 [chan receive]:
   > runtime.gopark(0xc0109a3c20?, 0xc011092c00?, 0x3?, 0x0?, 0xc0107f9cf8?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0107f9ca8 sp=0xc0107f9c88 pc=0x13bb516
   > runtime.chanrecv(0xc011092b40, 0xc0107f9e08, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc0107f9d38 sp=0xc0107f9ca8 pc=0x13854bb
   > runtime.chanrecv2(0xc0102f9040?, 0x4012e60?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc0107f9d60 sp=0xc0107f9d38 pc=0x1384ff8
   > github.com/pingcap/tidb/executor.(*HashJoinExec).buildHashTableForList(0xc010aeeb40, 0x1?)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:762 +0x2d6 fp=0xc0107f9e78 sp=0xc0107f9d60 pc=0x3065af6
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable(0xc010aeeb40, {0x400d6b0?, 0xc01080b3e0})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:726 +0x23f fp=0xc0107f9f28 sp=0xc0107f9e78 pc=0x30653ff
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Next.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:671 +0x8f fp=0xc0107f9f90 sp=0xc0107f9f28 pc=0x306504f
   > github.com/pingcap/tidb/util.WithRecovery(0x23de786?, 0xc0106651c0?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc0107f9fc0 sp=0xc0107f9f90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Next.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:669 +0x2a fp=0xc0107f9fe0 sp=0xc0107f9fc0 pc=0x3064f8a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0107f9fe8 sp=0xc0107f9fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).Next
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:669 +0x5b2
   > goroutine 975 [chan receive]:
   > runtime.gopark(0x13c37d1?, 0xc0107f8bb8?, 0x0?, 0x38?, 0xc011088370?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0107f8ba8 sp=0xc0107f8b88 pc=0x13bb516
   > runtime.chanrecv(0xc011092ae0, 0xc0107f8cf8, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc0107f8c38 sp=0xc0107f8ba8 pc=0x13854bb
   > runtime.chanrecv2(0xc010aeeb40?, 0x400d6b0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc0107f8c60 sp=0xc0107f8c38 pc=0x1384ff8
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Next(0xc010aeeb40, {0x400d6b0?, 0xc01080b3e0?}, 0xc010f69f90)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:681 +0x652 fp=0xc0107f8d20 sp=0xc0107f8c60 pc=0x3064d52
   > github.com/pingcap/tidb/executor.Next({0x400d6b0, 0xc01080b3e0}, {0x40101a0, 0xc010aeeb40}, 0xc010f69f90)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:286 +0x4a8 fp=0xc0107f8e60 sp=0xc0107f8d20 pc=0x2fef688
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchProbeSideChunks(0xc010aef680, {0x400d6b0, 0xc01080b3e0})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:209 +0x1d6 fp=0xc0107f8f28 sp=0xc0107f8e60 pc=0x30602d6
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:322 +0x8f fp=0xc0107f8f90 sp=0xc0107f8f28 pc=0x306156f
   > github.com/pingcap/tidb/util.WithRecovery(0xc010a9e440?, 0xc0006ecd38?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc0107f8fc0 sp=0xc0107f8f90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func3()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:320 +0x2a fp=0xc0107f8fe0 sp=0xc0107f8fc0 pc=0x30614aa
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0107f8fe8 sp=0xc0107f8fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:320 +0x14f
   > goroutine 976 [select]:
   > runtime.gopark(0xc0006e9e10?, 0x2?, 0x70?, 0x2d?, 0xc0006e9d8c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0006e9be0 sp=0xc0006e9bc0 pc=0x13bb516
   > runtime.selectgo(0xc0006e9e10, 0xc0006e9d88, 0x13cb293?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0006e9d20 sp=0xc0006e9be0 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc010aef680, 0x0, {0xc010015b08, 0x1, 0x1})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:441 +0x4f4 fp=0xc0006e9f10 sp=0xc0006e9d20 pc=0x30626b4
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:335 +0xb3 fp=0xc0006e9f90 sp=0xc0006e9f10 pc=0x30613d3
   > github.com/pingcap/tidb/util.WithRecovery(0x0?, 0xc0006e9fa0?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc0006e9fc0 sp=0xc0006e9f90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x2a fp=0xc0006e9fe0 sp=0xc0006e9fc0 pc=0x30612ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0006e9fe8 sp=0xc0006e9fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x1c9
   > goroutine 977 [select]:
   > runtime.gopark(0xc0006e7610?, 0x2?, 0x78?, 0x2d?, 0xc0006e758c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0006e73e0 sp=0xc0006e73c0 pc=0x13bb516
   > runtime.selectgo(0xc0006e7610, 0xc0006e7588, 0x0?, 0x0, 0xc00028ee90?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0006e7520 sp=0xc0006e73e0 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc010aef680, 0x1, {0xc010015b08, 0x1, 0x1})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:441 +0x4f4 fp=0xc0006e7710 sp=0xc0006e7520 pc=0x30626b4
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:335 +0xb3 fp=0xc0006e7790 sp=0xc0006e7710 pc=0x30613d3
   > github.com/pingcap/tidb/util.WithRecovery(0xc00feb4ea0?, 0xc0006e7538?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc0006e77c0 sp=0xc0006e7790 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x2a fp=0xc0006e77e0 sp=0xc0006e77c0 pc=0x30612ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0006e77e8 sp=0xc0006e77e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x1c9
   > goroutine 978 [select]:
   > runtime.gopark(0xc0006e8e10?, 0x2?, 0x80?, 0x2d?, 0xc0006e8d8c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0006a5be0 sp=0xc0006a5bc0 pc=0x13bb516
   > runtime.selectgo(0xc0006a5e10, 0xc0006e8d88, 0x0?, 0x0, 0xc00028ee90?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0006a5d20 sp=0xc0006a5be0 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc010aef680, 0x2, {0xc010015b08, 0x1, 0x1})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:441 +0x4f4 fp=0xc0006a5f10 sp=0xc0006a5d20 pc=0x30626b4
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:335 +0xb3 fp=0xc0006a5f90 sp=0xc0006a5f10 pc=0x30613d3
   > github.com/pingcap/tidb/util.WithRecovery(0xc00feb50a0?, 0xc0006e8d38?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc0006a5fc0 sp=0xc0006a5f90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x2a fp=0xc0006a5fe0 sp=0xc0006a5fc0 pc=0x30612ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0006a5fe8 sp=0xc0006a5fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x1c9
   > goroutine 979 [select]:
   > runtime.gopark(0xc0006ea610?, 0x2?, 0x88?, 0x2d?, 0xc0006ea58c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0006a4be0 sp=0xc0006a4bc0 pc=0x13bb516
   > runtime.selectgo(0xc0006a4e10, 0xc0006ea588, 0x0?, 0x0, 0x13e673a?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0006a4d20 sp=0xc0006a4be0 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc010aef680, 0x3, {0xc010015b08, 0x1, 0x1})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:441 +0x4f4 fp=0xc0006a4f10 sp=0xc0006a4d20 pc=0x30626b4
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:335 +0xb3 fp=0xc0006a4f90 sp=0xc0006a4f10 pc=0x30613d3
   > github.com/pingcap/tidb/util.WithRecovery(0xc0103f1080?, 0xc0006ea7a0?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc0006a4fc0 sp=0xc0006a4f90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x2a fp=0xc0006a4fe0 sp=0xc0006a4fc0 pc=0x30612ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0006a4fe8 sp=0xc0006a4fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x1c9
   > goroutine 980 [select]:
   > runtime.gopark(0xc0006eae10?, 0x2?, 0x90?, 0x2d?, 0xc0006ead8c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000d03be0 sp=0xc000d03bc0 pc=0x13bb516
   > runtime.selectgo(0xc000d03e10, 0xc0006ead88, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000d03d20 sp=0xc000d03be0 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc010aef680, 0x4, {0xc010015b08, 0x1, 0x1})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:441 +0x4f4 fp=0xc000d03f10 sp=0xc000d03d20 pc=0x30626b4
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:335 +0xb3 fp=0xc000d03f90 sp=0xc000d03f10 pc=0x30613d3
   > github.com/pingcap/tidb/util.WithRecovery(0x0?, 0x0?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc000d03fc0 sp=0xc000d03f90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x2a fp=0xc000d03fe0 sp=0xc000d03fc0 pc=0x30612ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000d03fe8 sp=0xc000d03fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x1c9
   > goroutine 981 [semacquire]:
   > runtime.gopark(0x1ecccb7?, 0x1ed29e5?, 0xe0?, 0xe1?, 0xc0104cb380?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0006e6e78 sp=0xc0006e6e58 pc=0x13bb516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc010aef878, 0x54?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc0006e6ee0 sp=0xc0006e6e78 pc=0x13cce5e
   > sync.runtime_Semacquire(0x4020f40?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc0006e6f10 sp=0xc0006e6ee0 pc=0x13e9f65
   > sync.(*WaitGroup).Wait(0xc010a9f901?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc0006e6f38 sp=0xc0006e6f10 pc=0x13fd1f2
   > github.com/pingcap/tidb/executor.(*HashJoinExec).waitJoinWorkersAndCloseResultChan(0xc010aef680)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:395 +0x33 fp=0xc0006e6f78 sp=0xc0006e6f38 pc=0x3061fb3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).waitJoinWorkersAndCloseResultChan-fm()
   > 	<autogenerated>:1 +0x26 fp=0xc0006e6f90 sp=0xc0006e6f78 pc=0x31277c6
   > github.com/pingcap/tidb/util.WithRecovery(0xc01053bad0?, 0xc0006e6fa0?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc0006e6fc0 sp=0xc0006e6f90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:338 +0x28 fp=0xc0006e6fe0 sp=0xc0006e6fc0 pc=0x3061288
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0006e6fe8 sp=0xc0006e6fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:338 +0x3b8
   > goroutine 1023 [select]:
   > runtime.gopark(0xc00fb45f78?, 0x2?, 0x78?, 0x5d?, 0xc00fb45eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fb45d58 sp=0xc00fb45d38 pc=0x13bb516
   > runtime.selectgo(0xc00fb45f78, 0xc00fb45ee8, 0x3aac226?, 0x0, 0x7473222c7d5d2259?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fb45e98 sp=0xc00fb45d58 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc010730640, {0x400d6b0?, 0xc01080b3e0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc00fb45fb8 sp=0xc00fb45e98 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc00fb45fe0 sp=0xc00fb45fb8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fb45fe8 sp=0xc00fb45fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 1024 [select]:
   > runtime.gopark(0xc01103ff78?, 0x2?, 0x0?, 0x0?, 0xc01103feec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01103fd58 sp=0xc01103fd38 pc=0x13bb516
   > runtime.selectgo(0xc01103ff78, 0xc01103fee8, 0x3aac226?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01103fe98 sp=0xc01103fd58 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc010730680, {0x400d6b0?, 0xc01080b3e0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc01103ffb8 sp=0xc01103fe98 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc01103ffe0 sp=0xc01103ffb8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01103ffe8 sp=0xc01103ffe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 1025 [select]:
   > runtime.gopark(0xc011040778?, 0x2?, 0x0?, 0x0?, 0xc0110406ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc011040558 sp=0xc011040538 pc=0x13bb516
   > runtime.selectgo(0xc011040778, 0xc0110406e8, 0x3aac226?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc011040698 sp=0xc011040558 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc0107306c0, {0x400d6b0?, 0xc01080b3e0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc0110407b8 sp=0xc011040698 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc0110407e0 sp=0xc0110407b8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0110407e8 sp=0xc0110407e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 1042 [select]:
   > runtime.gopark(0xc011040f78?, 0x2?, 0x0?, 0x0?, 0xc011040eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc011040d58 sp=0xc011040d38 pc=0x13bb516
   > runtime.selectgo(0xc011040f78, 0xc011040ee8, 0x3aac226?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc011040e98 sp=0xc011040d58 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc010730700, {0x400d6b0?, 0xc01080b3e0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc011040fb8 sp=0xc011040e98 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc011040fe0 sp=0xc011040fb8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc011040fe8 sp=0xc011040fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 1043 [select]:
   > runtime.gopark(0xc011041778?, 0x2?, 0x0?, 0x0?, 0xc0110416ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc011041558 sp=0xc011041538 pc=0x13bb516
   > runtime.selectgo(0xc011041778, 0xc0110416e8, 0x3aac226?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc011041698 sp=0xc011041558 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc010730740, {0x400d6b0?, 0xc01080b3e0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc0110417b8 sp=0xc011041698 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc0110417e0 sp=0xc0110417b8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0110417e8 sp=0xc0110417e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
