# Bug ID TIDB-30326-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/30326
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED


## Details
 * Database: tidb-v5.4.0-local
 * Number of scenarios: 1
 * Initial setup script: /home/theodor/Projects/MasterThesis/data/sql/TIDB-30326_mysql_bk.sql

## Results
### Scenario 0
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  WITH cte_0 AS (select 1 as c1, (FIRST_VALUE(1) over (partition by subq_0.c0) < ...
     - TID: 0
     - Output: ERROR: 2013 (HY000): Lost connection to MySQL server during query

 * Container logs:
   > [2024/06/18 13:42:24.408 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=5] [user=root] [host=]
   > [2024/06/18 13:42:24.411 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=28] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/06/18 13:42:24.412 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=28] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/06/18 13:42:24.414 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:58, Type:create schema, State:none, SchemaState:queueing, SchemaID:57, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 13:42:24.413 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 13:42:24.414 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:58, Type:create schema, State:none, SchemaState:queueing, SchemaID:57, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 13:42:24.413 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/18 13:42:24.414 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:58, Type:create schema, State:none, SchemaState:queueing, SchemaID:57, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:24.413 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:24.415 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=28] [neededSchemaVersion=29] ["start time"=78.781µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 13:42:24.417 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=29] ["take time"=2.198349ms] [job="ID:58, Type:create schema, State:done, SchemaState:public, SchemaID:57, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 13:42:24.413 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:24.417 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:58, Type:create schema, State:synced, SchemaState:public, SchemaID:57, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:24.413 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:24.418 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=58]
   > [2024/06/18 13:42:24.418 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 13:42:24.423 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=29] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_037irb`\n--\n\nDROP TABLE IF EXISTS `t_037irb`;"] [user=root@127.0.0.1]
   > [2024/06/18 13:42:24.423 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=29] [cur_db=testdb] [sql="CREATE TABLE `t_037irb` (\n  `c_nrh3o` int(11) DEFAULT NULL,\n  `c_nfauxb` text DEFAULT NULL,\n  `c_y5n4c` int(11) DEFAULT NULL,\n  `c_j9alg` double NOT NULL,\n  `c_4vix1d` text DEFAULT NULL,\n  `c_glkxdb` text DEFAULT NULL,\n  `c_2ykt0d` int(11) DEFAULT NULL,\n  `c_5fxv3c` double DEFAULT NULL,\n  PRIMARY KEY (`c_j9alg`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/06/18 13:42:24.424 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:60, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:59, RowCount:0, ArgLen:1, start time: 2024-06-18 13:42:24.423 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 13:42:24.424 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:60, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:59, RowCount:0, ArgLen:1, start time: 2024-06-18 13:42:24.423 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_037irb` (\n  `c_nrh3o` int(11) DEFAULT NULL,\n  `c_nfauxb` text DEFAULT NULL,\n  `c_y5n4c` int(11) DEFAULT NULL,\n  `c_j9alg` double NOT NULL,\n  `c_4vix1d` text DEFAULT NULL,\n  `c_glkxdb` text DEFAULT NULL,\n  `c_2ykt0d` int(11) DEFAULT NULL,\n  `c_5fxv3c` double DEFAULT NULL,\n  PRIMARY KEY (`c_j9alg`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/18 13:42:24.424 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:60, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:59, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:24.423 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:24.425 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=29] [neededSchemaVersion=30] ["start time"=207.361µs] [phyTblIDs="[59]"] [actionTypes="[8]"]
   > [2024/06/18 13:42:24.427 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=30] ["take time"=2.249613ms] [job="ID:60, Type:create table, State:done, SchemaState:public, SchemaID:57, TableID:59, RowCount:0, ArgLen:1, start time: 2024-06-18 13:42:24.423 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:24.428 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:60, Type:create table, State:synced, SchemaState:public, SchemaID:57, TableID:59, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:24.423 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:24.429 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=60]
   > [2024/06/18 13:42:24.429 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 13:42:24.430 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=52] ["first split key"=74800000000000003b]
   > [2024/06/18 13:42:24.430 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=30] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_037irb` DISABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/06/18 13:42:24.431 +00:00] [WARN] [2pc.go:1596] ["schemaLeaseChecker is not set for this transaction"] [sessionID=5] [startTS=450551649253720065] [commitTS=450551649253720066]
   > [2024/06/18 13:42:24.432 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=54] ["first at"=74800000000000003b] ["first new region left"="{Id:54 StartKey:7480000000000000ff3700000000000000f8 EndKey:7480000000000000ff3b00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:55 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/18 13:42:24.432 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[54]"]
   > [2024/06/18 13:42:24.433 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=30] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_037irb` ENABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/06/18 13:42:24.433 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=30] [cur_db=testdb] [sql="\n--\n-- Temporary view structure for view `t_cpsvpb`\n--\n\nDROP TABLE IF EXISTS `t_cpsvpb`;"] [user=root@127.0.0.1]
   > [2024/06/18 13:42:24.433 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=30] [cur_db=testdb] [sql="/*!50001 DROP VIEW IF EXISTS `t_cpsvpb`*/;"] [user=root@127.0.0.1]
   > [2024/06/18 13:42:24.435 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:62, Type:create view, State:none, SchemaState:queueing, SchemaID:57, TableID:61, RowCount:0, ArgLen:3, start time: 2024-06-18 13:42:24.434 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 13:42:24.435 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:62, Type:create view, State:none, SchemaState:queueing, SchemaID:57, TableID:61, RowCount:0, ArgLen:3, start time: 2024-06-18 13:42:24.434 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="/*!50001 CREATE VIEW `t_cpsvpb` AS SELECT \n 1 AS `c0`,\n 1 AS `c2`,\n 1 AS `c3`,\n 1 AS `c4`,\n 1 AS `c5`,\n 1 AS `c6`,\n 1 AS `c7`,\n 1 AS `c8`,\n 1 AS `c9`,\n 1 AS `c10`,\n 1 AS `c11`,\n 1 AS `c12`,\n 1 AS `c13`,\n 1 AS `c14`*/;"]
   > [2024/06/18 13:42:24.435 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:62, Type:create view, State:none, SchemaState:queueing, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:24.434 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:24.437 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=30] [neededSchemaVersion=31] ["start time"=524.444µs] [phyTblIDs="[61]"] [actionTypes="[2097152]"]
   > [2024/06/18 13:42:24.440 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=31] ["take time"=2.854725ms] [job="ID:62, Type:create view, State:done, SchemaState:public, SchemaID:57, TableID:61, RowCount:0, ArgLen:3, start time: 2024-06-18 13:42:24.434 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:24.441 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:62, Type:create view, State:synced, SchemaState:public, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:24.434 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:24.442 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=62]
   > [2024/06/18 13:42:24.442 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 13:42:24.443 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=31] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_x7zqmd`\n--\n\nDROP TABLE IF EXISTS `t_x7zqmd`;"] [user=root@127.0.0.1]
   > [2024/06/18 13:42:24.443 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=31] [cur_db=testdb] [sql="CREATE TABLE `t_x7zqmd` (\n  `c_8weeq` int(11) NOT NULL,\n  `c_13sfid` double DEFAULT NULL,\n  `c_hhjlmc` text DEFAULT NULL,\n  `c_3b1zld` int(11) DEFAULT NULL,\n  `c_6tu8wd` int(11) DEFAULT NULL,\n  `c_jyc_cd` double DEFAULT NULL,\n  PRIMARY KEY (`c_8weeq`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/06/18 13:42:24.445 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:64, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:63, RowCount:0, ArgLen:1, start time: 2024-06-18 13:42:24.444 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 13:42:24.445 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:64, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:63, RowCount:0, ArgLen:1, start time: 2024-06-18 13:42:24.444 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_x7zqmd` (\n  `c_8weeq` int(11) NOT NULL,\n  `c_13sfid` double DEFAULT NULL,\n  `c_hhjlmc` text DEFAULT NULL,\n  `c_3b1zld` int(11) DEFAULT NULL,\n  `c_6tu8wd` int(11) DEFAULT NULL,\n  `c_jyc_cd` double DEFAULT NULL,\n  PRIMARY KEY (`c_8weeq`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/18 13:42:24.446 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:64, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:63, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:24.444 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:24.447 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=31] [neededSchemaVersion=32] ["start time"=359.267µs] [phyTblIDs="[63]"] [actionTypes="[8]"]
   > [2024/06/18 13:42:24.449 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=32] ["take time"=2.335728ms] [job="ID:64, Type:create table, State:done, SchemaState:public, SchemaID:57, TableID:63, RowCount:0, ArgLen:1, start time: 2024-06-18 13:42:24.444 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:24.450 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:64, Type:create table, State:synced, SchemaState:public, SchemaID:57, TableID:63, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:24.444 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:24.451 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=64]
   > [2024/06/18 13:42:24.451 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 13:42:24.451 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=56] ["first split key"=74800000000000003f]
   > [2024/06/18 13:42:24.452 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=56] ["first at"=74800000000000003f] ["first new region left"="{Id:56 StartKey:7480000000000000ff3b00000000000000f8 EndKey:7480000000000000ff3f00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:57 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/18 13:42:24.452 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[56]"]
   > [2024/06/18 13:42:24.452 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=32] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_x7zqmd` DISABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/06/18 13:42:24.455 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=32] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_x7zqmd` ENABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/06/18 13:42:24.455 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=32] [cur_db=testdb] [sql="\n--\n-- Final view structure for view `t_cpsvpb`\n--\n\n/*!50001 DROP VIEW IF EXISTS `t_cpsvpb`*/;"] [user=root@127.0.0.1]
   > [2024/06/18 13:42:24.456 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:65, Type:drop view, State:none, SchemaState:queueing, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:24.455 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 13:42:24.456 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:65, Type:drop view, State:none, SchemaState:queueing, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:24.455 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="\n--\n-- Final view structure for view `t_cpsvpb`\n--\n\n/*!50001 DROP VIEW IF EXISTS `t_cpsvpb`*/;"]
   > [2024/06/18 13:42:24.456 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:drop view, State:none, SchemaState:queueing, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:24.455 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:24.458 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=32] [neededSchemaVersion=33] ["start time"=92.541µs] [phyTblIDs="[61]"] [actionTypes="[16777216]"]
   > [2024/06/18 13:42:24.460 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=33] ["take time"=2.300737ms] [job="ID:65, Type:drop view, State:running, SchemaState:write only, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:24.455 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:24.460 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:drop view, State:running, SchemaState:write only, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:24.455 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:24.462 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=33] [neededSchemaVersion=34] ["start time"=118.312µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 13:42:24.464 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=34] ["take time"=2.753943ms] [job="ID:65, Type:drop view, State:running, SchemaState:delete only, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:24.455 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:24.465 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:drop view, State:running, SchemaState:delete only, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:24.455 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:24.466 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=34] [neededSchemaVersion=35] ["start time"=105.671µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 13:42:24.469 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=35] ["take time"=2.574378ms] [job="ID:65, Type:drop view, State:done, SchemaState:queueing, SchemaID:57, TableID:61, RowCount:0, ArgLen:3, start time: 2024-06-18 13:42:24.455 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:24.470 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:drop view, State:synced, SchemaState:queueing, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:24.455 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:24.471 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=65]
   > [2024/06/18 13:42:24.471 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 13:42:24.477 +00:00] [INFO] [session.go:2108] ["Try to create a new txn inside a transaction auto commit"] [conn=5] [schemaVersion=35] [txnStartTS=450551649264992256] [txnScope=global]
   > [2024/06/18 13:42:24.479 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:67, Type:create view, State:none, SchemaState:queueing, SchemaID:57, TableID:66, RowCount:0, ArgLen:3, start time: 2024-06-18 13:42:24.478 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 13:42:24.479 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:67, Type:create view, State:none, SchemaState:queueing, SchemaID:57, TableID:66, RowCount:0, ArgLen:3, start time: 2024-06-18 13:42:24.478 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="/*!50001 CREATE ALGORITHM=UNDEFINED */\n/*!50013 DEFINER=`root`@`127.0.0.1` SQL SECURITY DEFINER */\n/*!50001 VIEW `t_cpsvpb` (`c0`, `c2`, `c3`, `c4`, `c5`, `c6`, `c7`, `c8`, `c9`, `c10`, `c11`, `c12`, `c13`, `c14`) AS SELECT DISTINCT `subq_0`.`c1` AS `c0`,`subq_0`.`c2` AS `c2`,8 AS `c3`,CASE WHEN (`subq_0`.`c3` NOT IN (SELECT `ref_2`.`c_4vix1d` AS `c0` FROM `testdb`.`t_037irb` AS `ref_2` WHERE `ref_2`.`c_2ykt0d`<=`ref_2`.`c_nrh3o`)) AND (`subq_0`.`c3`<=(SELECT (SELECT `c_hhjlmc` AS `c_hhjlmc` FROM `testdb`.`t_x7zqmd` ORDER BY `c_hhjlmc` LIMIT 4,1) AS `c0` FROM `testdb`.`t_037irb` AS `ref_3` WHERE `subq_0`.`c1`!=`ref_3`.`c_2ykt0d`)) THEN `subq_0`.`c3` ELSE `subq_0`.`c3` END AS `c4`,CASE WHEN `subq_0`.`c1`>=(SELECT MAX(`c_8weeq`) AS `max(c_8weeq)` FROM `testdb`.`t_x7zqmd`) THEN `subq_0`.`c2` ELSE `subq_0`.`c2` END AS `c5`,`subq_0`.`c1` AS `c6`,`subq_0`.`c2` AS `c7`,`subq_0`.`c3` AS `c8`,`subq_0`.`c3` AS `c9`,`subq_0`.`c2` AS `c10`,`subq_0`.`c4` AS `c11`,COUNT(CAST(`subq_0`.`c2` AS DOUBLE)) OVER (PARTITION BY `subq_0`.`c4` ORDER BY `subq_0`.`c1`) AS `c12`,`subq_0`.`c3` AS `c13`,CAST(COALESCE(`subq_0`.`c3`, _UTF8MB4'9sx3k') AS CHAR) AS `c14` FROM (SELECT COUNT(CAST(`ref_1`.`c_jyc_cd` AS DOUBLE)) AS `c0`,AVG(CAST(`ref_1`.`c_3b1zld` AS SIGNED)) AS `c1`,MIN(CAST(`ref_1`.`c_jyc_cd` AS DOUBLE)) AS `c2`,`ref_0`.`c_glkxdb` AS `c3`,COUNT(CAST(`ref_1`.`c_13sfid` AS DOUBLE)) AS `c4` FROM `testdb`.`t_037irb` AS `ref_0` JOIN `testdb`.`t_x7zqmd` AS `ref_1` WHERE `ref_0`.`c_nrh3o`>`ref_1`.`c_8weeq` GROUP BY `ref_0`.`c_glkxdb`) AS `subq_0` WHERE (SELECT `c_8weeq` AS `c_8weeq` FROM `testdb`.`t_x7zqmd` ORDER BY `c_8weeq` LIMIT 2,1) IS NOT NULL */;"]
   > [2024/06/18 13:42:24.480 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:create view, State:none, SchemaState:queueing, SchemaID:57, TableID:66, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:24.478 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:24.483 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=35] [neededSchemaVersion=36] ["start time"=577.944µs] [phyTblIDs="[66]"] [actionTypes="[2097152]"]
   > [2024/06/18 13:42:24.486 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=36] ["take time"=2.719929ms] [job="ID:67, Type:create view, State:done, SchemaState:public, SchemaID:57, TableID:66, RowCount:0, ArgLen:3, start time: 2024-06-18 13:42:24.478 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:24.487 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:create view, State:synced, SchemaState:public, SchemaID:57, TableID:66, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:24.478 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:24.488 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=67]
   > [2024/06/18 13:42:24.489 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 13:42:25.530 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=7] [user=root] [host=]
   > [2024/06/18 13:42:25.554 +00:00] [INFO] [set.go:139] ["set global var"] [conn=7] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/06/18 13:42:25.825 +00:00] [ERROR] [misc.go:95] ["panic in the recoverable goroutine"] [r="\"invalid memory address or nil pointer dereference\""] ["stack trace"="github.com/pingcap/tidb/util.WithRecovery.func1\n\t/go/src/github.com/pingcap/tidb/util/misc.go:97\nruntime.gopanic\n\t/usr/local/go/src/runtime/panic.go:884\nruntime.panicmem\n\t/usr/local/go/src/runtime/panic.go:260\nruntime.sigpanic\n\t/usr/local/go/src/runtime/signal_unix.go:839\ngithub.com/pingcap/tidb/executor.(*vecGroupChecker).splitIntoGroups\n\t/go/src/github.com/pingcap/tidb/executor/aggregate.go:1457\ngithub.com/pingcap/tidb/executor.(*PipelinedWindowExec).getRowsInPartition\n\t/go/src/github.com/pingcap/tidb/executor/pipelined_window.go:189\ngithub.com/pingcap/tidb/executor.(*PipelinedWindowExec).Next\n\t/go/src/github.com/pingcap/tidb/executor/pipelined_window.go:125\ngithub.com/pingcap/tidb/executor.Next\n\t/go/src/github.com/pingcap/tidb/executor/executor.go:286\ngithub.com/pingcap/tidb/executor.(*ProjectionExec).unParallelExecute\n\t/go/src/github.com/pingcap/tidb/executor/projection.go:194\ngithub.com/pingcap/tidb/executor.(*ProjectionExec).Next\n\t/go/src/github.com/pingcap/tidb/executor/projection.go:180\ngithub.com/pingcap/tidb/executor.Next\n\t/go/src/github.com/pingcap/tidb/executor/executor.go:286\ngithub.com/pingcap/tidb/executor.(*CTEExec).computeSeedPart\n\t/go/src/github.com/pingcap/tidb/executor/cte.go:226\ngithub.com/pingcap/tidb/executor.(*CTEExec).Next\n\t/go/src/github.com/pingcap/tidb/executor/cte.go:161\ngithub.com/pingcap/tidb/executor.Next\n\t/go/src/github.com/pingcap/tidb/executor/executor.go:286\ngithub.com/pingcap/tidb/executor.(*SelectionExec).Next\n\t/go/src/github.com/pingcap/tidb/executor/executor.go:1317\ngithub.com/pingcap/tidb/executor.Next\n\t/go/src/github.com/pingcap/tidb/executor/executor.go:286\ngithub.com/pingcap/tidb/executor.(*HashJoinExec).fetchBuildSideRows\n\t/go/src/github.com/pingcap/tidb/executor/join.go:266\ngithub.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable.func2\n\t/go/src/github.com/pingcap/tidb/executor/join.go:715\ngithub.com/pingcap/tidb/util.WithRecovery\n\t/go/src/github.com/pingcap/tidb/util/misc.go:100"]
   > runtime: goroutine stack exceeds 1000000000-byte limit
   > runtime: sp=0xc032980390 stack=[0xc032980000, 0xc052980000]
   > fatal error: stack overflow
   > runtime stack:
   > runtime.throw({0x3aa773d?, 0x590b5c0?})
   > 	/usr/local/go/src/runtime/panic.go:1047 +0x5d fp=0x7f2072add888 sp=0x7f2072add858 pc=0x13b859d
   > runtime.newstack()
   > 	/usr/local/go/src/runtime/stack.go:1103 +0x5cc fp=0x7f2072adda40 sp=0x7f2072add888 pc=0x13d35ec
   > runtime.morestack()
   > 	/usr/local/go/src/runtime/asm_amd64.s:570 +0x8b fp=0x7f2072adda48 sp=0x7f2072adda40 pc=0x13ec60b
   > goroutine 1151 [running]:
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60?, 0xc0121a8300?}, {0x4012e60?, 0xc0121a8300?})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:183 +0x12c fp=0xc0329803a0 sp=0xc032980398 pc=0x1f5780c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0121a82a0}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329803d8 sp=0xc0329803a0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc000810660}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980410 sp=0xc0329803d8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0004a50e0}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980448 sp=0xc032980410 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011a46f20}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980480 sp=0xc032980448 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011f618e0}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329804b8 sp=0xc032980480 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011eb2180}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329804f0 sp=0xc0329804b8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011eb2160}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980528 sp=0xc0329804f0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011f618c0}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980560 sp=0xc032980528 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc012088600}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980598 sp=0xc032980560 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011f61710}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329805d0 sp=0xc032980598 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0121a8300}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980608 sp=0xc0329805d0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0121a82a0}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980640 sp=0xc032980608 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc000810660}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980678 sp=0xc032980640 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0004a50e0}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329806b0 sp=0xc032980678 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011a46f20}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329806e8 sp=0xc0329806b0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011f618e0}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980720 sp=0xc0329806e8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011eb2180}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980758 sp=0xc032980720 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011eb2160}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980790 sp=0xc032980758 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011f618c0}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329807c8 sp=0xc032980790 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc012088600}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980800 sp=0xc0329807c8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011f61710}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980838 sp=0xc032980800 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0121a8300}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980870 sp=0xc032980838 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0121a82a0}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329808a8 sp=0xc032980870 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc000810660}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329808e0 sp=0xc0329808a8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0004a50e0}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980918 sp=0xc0329808e0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011a46f20}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980950 sp=0xc032980918 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011f618e0}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980988 sp=0xc032980950 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011eb2180}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329809c0 sp=0xc032980988 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011eb2160}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329809f8 sp=0xc0329809c0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011f618c0}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980a30 sp=0xc0329809f8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc012088600}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980a68 sp=0xc032980a30 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011f61710}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980aa0 sp=0xc032980a68 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0121a8300}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980ad8 sp=0xc032980aa0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0121a82a0}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980b10 sp=0xc032980ad8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc000810660}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980b48 sp=0xc032980b10 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0004a50e0}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980b80 sp=0xc032980b48 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011a46f20}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980bb8 sp=0xc032980b80 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011f618e0}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980bf0 sp=0xc032980bb8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011eb2180}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980c28 sp=0xc032980bf0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011eb2160}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980c60 sp=0xc032980c28 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011f618c0}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980c98 sp=0xc032980c60 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc012088600}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980cd0 sp=0xc032980c98 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011f61710}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980d08 sp=0xc032980cd0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0121a8300}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980d40 sp=0xc032980d08 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0121a82a0}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980d78 sp=0xc032980d40 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc000810660}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980db0 sp=0xc032980d78 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0004a50e0}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980de8 sp=0xc032980db0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011a46f20}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980e20 sp=0xc032980de8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011f618e0}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980e58 sp=0xc032980e20 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011eb2180}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980e90 sp=0xc032980e58 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011eb2160}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980ec8 sp=0xc032980e90 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011f618c0}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980f00 sp=0xc032980ec8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc012088600}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980f38 sp=0xc032980f00 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011f61710}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980f70 sp=0xc032980f38 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0121a8300}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980fa8 sp=0xc032980f70 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0121a82a0}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032980fe0 sp=0xc032980fa8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc000810660}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032981018 sp=0xc032980fe0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0004a50e0}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032981050 sp=0xc032981018 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011a46f20}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032981088 sp=0xc032981050 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011f618e0}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329810c0 sp=0xc032981088 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011eb2180}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329810f8 sp=0xc0329810c0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011eb2160}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032981130 sp=0xc0329810f8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011f618c0}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032981168 sp=0xc032981130 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc012088600}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329811a0 sp=0xc032981168 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011f61710}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329811d8 sp=0xc0329811a0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0121a8300}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032981210 sp=0xc0329811d8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0121a82a0}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032981248 sp=0xc032981210 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc000810660}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032981280 sp=0xc032981248 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0004a50e0}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329812b8 sp=0xc032981280 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011a46f20}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329812f0 sp=0xc0329812b8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011f618e0}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032981328 sp=0xc0329812f0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011eb2180}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032981360 sp=0xc032981328 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011eb2160}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032981398 sp=0xc032981360 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011f618c0}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329813d0 sp=0xc032981398 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc012088600}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032981408 sp=0xc0329813d0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011f61710}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032981440 sp=0xc032981408 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0121a8300}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032981478 sp=0xc032981440 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0121a82a0}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329814b0 sp=0xc032981478 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc000810660}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329814e8 sp=0xc0329814b0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0004a50e0}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032981520 sp=0xc0329814e8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011a46f20}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032981558 sp=0xc032981520 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011f618e0}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032981590 sp=0xc032981558 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011eb2180}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329815c8 sp=0xc032981590 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011eb2160}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032981600 sp=0xc0329815c8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011f618c0}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032981638 sp=0xc032981600 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc012088600}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032981670 sp=0xc032981638 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011f61710}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329816a8 sp=0xc032981670 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0121a8300}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329816e0 sp=0xc0329816a8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0121a82a0}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032981718 sp=0xc0329816e0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc000810660}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032981750 sp=0xc032981718 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0004a50e0}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032981788 sp=0xc032981750 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011a46f20}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329817c0 sp=0xc032981788 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011f618e0}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329817f8 sp=0xc0329817c0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011eb2180}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032981830 sp=0xc0329817f8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011eb2160}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032981868 sp=0xc032981830 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011f618c0}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329818a0 sp=0xc032981868 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc012088600}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329818d8 sp=0xc0329818a0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011f61710}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032981910 sp=0xc0329818d8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0121a8300}, {0x4012e60, 0xc0121a8300})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032981948 sp=0xc032981910 pc=0x1f577a5
   > ...additional frames elided...
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:712 +0x22d
   > goroutine 1 [chan receive]:
   > runtime.gopark(0xc0105514a0?, 0xc0107b7dc0?, 0xbf?, 0xc1?, 0x37fc5c0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0107b7d40 sp=0xc0107b7d20 pc=0x13bb516
   > runtime.chanrecv(0xc0003a4c60, 0xc0107b7e30, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc0107b7dd0 sp=0xc0107b7d40 pc=0x13854bb
   > runtime.chanrecv1(0xc0059ae9c0?, 0x0?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc0107b7df8 sp=0xc0107b7dd0 pc=0x1384fb8
   > github.com/pingcap/tidb/server.(*Server).Run(0xc0059ae9c0)
   > 	/go/src/github.com/pingcap/tidb/server/server.go:370 +0x1f0 fp=0xc0107b7e50 sp=0xc0107b7df8 pc=0x31e23d0
   > main.main()
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:213 +0x539 fp=0xc0107b7f80 sp=0xc0107b7e50 pc=0x33af4b9
   > runtime.main()
   > 	/usr/local/go/src/runtime/proc.go:250 +0x212 fp=0xc0107b7fe0 sp=0xc0107b7f80 pc=0x13bb152
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0107b7fe8 sp=0xc0107b7fe0 pc=0x13ee6e1
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
   > runtime.gopark(0x0?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000090f50 sp=0xc000090f30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc000090fe0 sp=0xc000090f50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000090fe8 sp=0xc000090fe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 18 [GC worker (idle)]:
   > runtime.gopark(0x3ada26e6be69?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008a750 sp=0xc00008a730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008a7e0 sp=0xc00008a750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008a7e8 sp=0xc00008a7e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 8 [GC worker (idle)]:
   > runtime.gopark(0x3ada3ab1845f?, 0xc00005b1e0?, 0x18?, 0x14?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000091750 sp=0xc000091730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0000917e0 sp=0xc000091750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000917e8 sp=0xc0000917e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 19 [GC worker (idle)]:
   > runtime.gopark(0x3ada3ab3479e?, 0x3?, 0xfc?, 0xd9?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008af50 sp=0xc00008af30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008afe0 sp=0xc00008af50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008afe8 sp=0xc00008afe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 9 [GC worker (idle)]:
   > runtime.gopark(0x5f8be00?, 0x1?, 0x39?, 0x95?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000091f50 sp=0xc000091f30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc000091fe0 sp=0xc000091f50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000091fe8 sp=0xc000091fe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 20 [GC worker (idle)]:
   > runtime.gopark(0x3ada3ab17218?, 0x3?, 0x77?, 0x23?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008b750 sp=0xc00008b730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008b7e0 sp=0xc00008b750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008b7e8 sp=0xc00008b7e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 10 [GC worker (idle)]:
   > runtime.gopark(0x3ada3ab3479e?, 0x3?, 0x75?, 0x5?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00049e750 sp=0xc00049e730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00049e7e0 sp=0xc00049e750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00049e7e8 sp=0xc00049e7e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 11 [GC worker (idle)]:
   > runtime.gopark(0x3ada3ab1778d?, 0x3?, 0x8d?, 0x19?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00049ef50 sp=0xc00049ef30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00049efe0 sp=0xc00049ef50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00049efe8 sp=0xc00049efe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 12 [GC worker (idle)]:
   > runtime.gopark(0x5f8be00?, 0x1?, 0x55?, 0xe1?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00049f750 sp=0xc00049f730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00049f7e0 sp=0xc00049f750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00049f7e8 sp=0xc00049f7e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 13 [GC worker (idle)]:
   > runtime.gopark(0x3ada3aaf4172?, 0x3?, 0x1?, 0x13?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00049ff50 sp=0xc00049ff30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00049ffe0 sp=0xc00049ff50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00049ffe8 sp=0xc00049ffe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 14 [GC worker (idle)]:
   > runtime.gopark(0x3ada3ab3479e?, 0x1?, 0xc8?, 0xa8?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004a0750 sp=0xc0004a0730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0004a07e0 sp=0xc0004a0750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004a07e8 sp=0xc0004a07e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 15 [GC worker (idle)]:
   > runtime.gopark(0x3ada3ab17218?, 0x1?, 0x40?, 0xaf?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004a0f50 sp=0xc0004a0f30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0004a0fe0 sp=0xc0004a0f50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004a0fe8 sp=0xc0004a0fe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 34 [GC worker (idle)]:
   > runtime.gopark(0x5f8be00?, 0x3?, 0x4d?, 0x51?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00049a750 sp=0xc00049a730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00049a7e0 sp=0xc00049a750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00049a7e8 sp=0xc00049a7e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 16 [GC worker (idle)]:
   > runtime.gopark(0x3ada3ab3479e?, 0x1?, 0xa?, 0x76?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004a1750 sp=0xc0004a1730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0004a17e0 sp=0xc0004a1750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004a17e8 sp=0xc0004a17e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 50 [GC worker (idle)]:
   > runtime.gopark(0x3ada3aaf7d78?, 0x1?, 0x82?, 0x98?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004a1f50 sp=0xc0004a1f30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0004a1fe0 sp=0xc0004a1f50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004a1fe8 sp=0xc0004a1fe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 163 [chan receive]:
   > runtime.gopark(0xc0004a2000?, 0x1?, 0x10?, 0xde?, 0x13d8de5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008ddb8 sp=0xc00008dd98 pc=0x13bb516
   > runtime.chanrecv(0xc000bf69c0, 0xc00008df28, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc00008de48 sp=0xc00008ddb8 pc=0x13854bb
   > runtime.chanrecv2(0x3b9aca00?, 0x13bb600?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc00008de70 sp=0xc00008de48 pc=0x1384ff8
   > go.etcd.io/etcd/pkg/logutil.(*MergeLogger).outputLoop(0xc000575ad0)
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:173 +0x8c fp=0xc00008dfc8 sp=0xc00008de70 pc=0x1a12c4c
   > go.etcd.io/etcd/pkg/logutil.NewMergeLogger.func1()
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:91 +0x26 fp=0xc00008dfe0 sp=0xc00008dfc8 pc=0x1a124c6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008dfe8 sp=0xc00008dfe0 pc=0x13ee6e1
   > created by go.etcd.io/etcd/pkg/logutil.NewMergeLogger
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:91 +0xb6
   > goroutine 22 [select]:
   > runtime.gopark(0xc00008d788?, 0x3?, 0x58?, 0xde?, 0xc00008d772?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008d5f8 sp=0xc00008d5d8 pc=0x13bb516
   > runtime.selectgo(0xc00008d788, 0xc00008d76c, 0xc000a2f680?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00008d738 sp=0xc00008d5f8 pc=0x13cbbdc
   > go.opencensus.io/stats/view.(*worker).start(0xc000a2f680)
   > 	/go/pkg/mod/go.opencensus.io@v0.23.0/stats/view/worker.go:276 +0xad fp=0xc00008d7c8 sp=0xc00008d738 pc=0x29900cd
   > go.opencensus.io/stats/view.init.0.func1()
   > 	/go/pkg/mod/go.opencensus.io@v0.23.0/stats/view/worker.go:34 +0x26 fp=0xc00008d7e0 sp=0xc00008d7c8 pc=0x298f346
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008d7e8 sp=0xc00008d7e0 pc=0x13ee6e1
   > created by go.opencensus.io/stats/view.init.0
   > 	/go/pkg/mod/go.opencensus.io@v0.23.0/stats/view/worker.go:34 +0x8d
   > goroutine 48 [chan receive]:
   > runtime.gopark(0xc0002fa060?, 0x13c1374?, 0x10?, 0xce?, 0x13d8de5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008cdb8 sp=0xc00008cd98 pc=0x13bb516
   > runtime.chanrecv(0xc0002fb740, 0xc00008cf28, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc00008ce48 sp=0xc00008cdb8 pc=0x13854bb
   > runtime.chanrecv2(0x3b9aca00?, 0x13bb600?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc00008ce70 sp=0xc00008ce48 pc=0x1384ff8
   > go.etcd.io/etcd/pkg/logutil.(*MergeLogger).outputLoop(0xc0006208b8)
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:173 +0x8c fp=0xc00008cfc8 sp=0xc00008ce70 pc=0x1a12c4c
   > go.etcd.io/etcd/pkg/logutil.NewMergeLogger.func1()
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:91 +0x26 fp=0xc00008cfe0 sp=0xc00008cfc8 pc=0x1a124c6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008cfe8 sp=0xc00008cfe0 pc=0x13ee6e1
   > created by go.etcd.io/etcd/pkg/logutil.NewMergeLogger
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:91 +0xb6
   > goroutine 180 [chan receive]:
   > runtime.gopark(0xc000bf6a80?, 0x2?, 0x10?, 0xd6?, 0x13d8de5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000b1d5b8 sp=0xc000b1d598 pc=0x13bb516
   > runtime.chanrecv(0xc000bf6a20, 0xc000b1d728, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000b1d648 sp=0xc000b1d5b8 pc=0x13854bb
   > runtime.chanrecv2(0x3b9aca00?, 0x13bb600?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc000b1d670 sp=0xc000b1d648 pc=0x1384ff8
   > go.etcd.io/etcd/pkg/logutil.(*MergeLogger).outputLoop(0xc0004b7a70)
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:173 +0x8c fp=0xc000b1d7c8 sp=0xc000b1d670 pc=0x1a12c4c
   > go.etcd.io/etcd/pkg/logutil.NewMergeLogger.func1()
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:91 +0x26 fp=0xc000b1d7e0 sp=0xc000b1d7c8 pc=0x1a124c6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000b1d7e8 sp=0xc000b1d7e0 pc=0x13ee6e1
   > created by go.etcd.io/etcd/pkg/logutil.NewMergeLogger
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:91 +0xb6
   > goroutine 1268 [select]:
   > runtime.gopark(0xc00fd3a778?, 0x2?, 0x2?, 0x0?, 0xc00fd3a6ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fd3a558 sp=0xc00fd3a538 pc=0x13bb516
   > runtime.selectgo(0xc00fd3a778, 0xc00fd3a6e8, 0x3aac226?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fd3a698 sp=0xc00fd3a558 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc0105af5c0, {0x400d6b0?, 0xc01127c9f0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc00fd3a7b8 sp=0xc00fd3a698 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc00fd3a7e0 sp=0xc00fd3a7b8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fd3a7e8 sp=0xc00fd3a7e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 294 [select]:
   > runtime.gopark(0xc000b19708?, 0x2?, 0x0?, 0x0?, 0xc000b196e4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000b19568 sp=0xc000b19548 pc=0x13bb516
   > runtime.selectgo(0xc000b19708, 0xc000b196e0, 0xc0000061a0?, 0x0, 0xc0000061a0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000b196a8 sp=0xc000b19568 pc=0x13cbbdc
   > github.com/pingcap/badger.(*blobGCHandler).run(0xc000c44380, 0xc000da4090)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/blob.go:468 +0xd6 fp=0xc000b197c0 sp=0xc000b196a8 pc=0x3288896
   > github.com/pingcap/badger.(*blobManager).Open.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/blob.go:292 +0x2a fp=0xc000b197e0 sp=0xc000b197c0 pc=0x328754a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000b197e8 sp=0xc000b197e0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.(*blobManager).Open
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/blob.go:292 +0x5bd
   > goroutine 431 [chan receive]:
   > runtime.gopark(0x209a4ff3c8?, 0x0?, 0x78?, 0xfe?, 0x13d8de5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00009fe20 sp=0xc00009fe00 pc=0x13bb516
   > runtime.chanrecv(0xc000b3e300, 0x0, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc00009feb0 sp=0xc00009fe20 pc=0x13854bb
   > runtime.chanrecv1(0xdf8475800?, 0x1b?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc00009fed8 sp=0xc00009feb0 pc=0x1384fb8
   > github.com/pingcap/tidb/util/profile.HeapProfileForGlobalMemTracker(0xc000af8ba0?)
   > 	/go/src/github.com/pingcap/tidb/util/profile/trackerRecorder.go:33 +0xa7 fp=0xc00009ffc8 sp=0xc00009fed8 pc=0x267adc7
   > main.setHeapProfileTracker.func1()
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:279 +0x26 fp=0xc00009ffe0 sp=0xc00009ffc8 pc=0x33afc46
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00009ffe8 sp=0xc00009ffe0 pc=0x13ee6e1
   > created by main.setHeapProfileTracker
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:279 +0xa5
   > goroutine 432 [chan receive]:
   > runtime.gopark(0xc000da1440?, 0x13c1374?, 0x38?, 0xde?, 0x13d8de5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000dadde0 sp=0xc000daddc0 pc=0x13bb516
   > runtime.chanrecv(0xc000da13e0, 0x0, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000dade70 sp=0xc000dadde0 pc=0x13854bb
   > runtime.chanrecv1(0x5f5e100?, 0x3ace4e4?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc000dade98 sp=0xc000dade70 pc=0x1384fb8
   > github.com/pingcap/tidb/util/systimemon.StartMonitor(0x3bccd98, 0x3bcc3f0, 0xc000af4f50)
   > 	/go/src/github.com/pingcap/tidb/util/systimemon/systime_mon.go:32 +0x185 fp=0xc000dadfb8 sp=0xc000dade98 pc=0x33ac665
   > main.setupMetrics.func3()
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:696 +0x31 fp=0xc000dadfe0 sp=0xc000dadfb8 pc=0x33b2df1
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000dadfe8 sp=0xc000dadfe0 pc=0x13ee6e1
   > created by main.setupMetrics
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:696 +0x115
   > goroutine 433 [select]:
   > runtime.gopark(0xc000ee1f80?, 0x2?, 0x10?, 0x0?, 0xc000ee1f4c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000ee1dd0 sp=0xc000ee1db0 pc=0x13bb516
   > runtime.selectgo(0xc000ee1f80, 0xc000ee1f48, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000ee1f10 sp=0xc000ee1dd0 pc=0x13cbbdc
   > github.com/pingcap/badger.(*DB).updateSize(0x0?, 0xc000aef7b8)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:1039 +0x105 fp=0xc000ee1fc0 sp=0xc000ee1f10 pc=0x329a445
   > github.com/pingcap/badger.Open.func5()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:328 +0x2a fp=0xc000ee1fe0 sp=0xc000ee1fc0 pc=0x329450a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000ee1fe8 sp=0xc000ee1fe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.Open
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:328 +0xf5c
   > goroutine 434 [select]:
   > runtime.gopark(0xc000ee2788?, 0x2?, 0x0?, 0x30?, 0xc000ee2764?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000ee25e8 sp=0xc000ee25c8 pc=0x13bb516
   > runtime.selectgo(0xc000ee2788, 0xc000ee2760, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000ee2728 sp=0xc000ee25e8 pc=0x13cbbdc
   > github.com/pingcap/badger/epoch.(*ResourceManager).collectLoop(0x0?, 0xc000aef7e8)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/epoch/manager.go:101 +0xd3 fp=0xc000ee27c0 sp=0xc000ee2728 pc=0x3257a13
   > github.com/pingcap/badger/epoch.NewResourceManager.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/epoch/manager.go:79 +0x2a fp=0xc000ee27e0 sp=0xc000ee27c0 pc=0x32577aa
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000ee27e8 sp=0xc000ee27e0 pc=0x13ee6e1
   > created by github.com/pingcap/badger/epoch.NewResourceManager
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/epoch/manager.go:79 +0xdd
   > goroutine 435 [select]:
   > runtime.gopark(0xc000da9e68?, 0x2?, 0x8?, 0xe1?, 0xc000da9e3c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000da9cc0 sp=0xc000da9ca0 pc=0x13bb516
   > runtime.selectgo(0xc000da9e68, 0xc000da9e38, 0x0?, 0x1, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000da9e00 sp=0xc000da9cc0 pc=0x13cbbdc
   > github.com/pingcap/badger.Open.func4()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:342 +0x155 fp=0xc000da9fe0 sp=0xc000da9e00 pc=0x3294495
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000da9fe8 sp=0xc000da9fe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.Open
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:339 +0x11f8
   > goroutine 295 [select]:
   > runtime.gopark(0xc00049bf60?, 0x2?, 0x4?, 0x30?, 0xc00049bf2c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00049bd98 sp=0xc00049bd78 pc=0x13bb516
   > runtime.selectgo(0xc00049bf60, 0xc00049bf28, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00049bed8 sp=0xc00049bd98 pc=0x13cbbdc
   > github.com/pingcap/badger.(*levelsController).runWorker(0xc000ae81c0, 0xc000da40c0, 0x0)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:212 +0x1fb fp=0xc00049bfb8 sp=0xc00049bed8 pc=0x32a297b
   > github.com/pingcap/badger.(*levelsController).startCompact.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:180 +0x2e fp=0xc00049bfe0 sp=0xc00049bfb8 pc=0x32a274e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00049bfe8 sp=0xc00049bfe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.(*levelsController).startCompact
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:180 +0x65
   > goroutine 296 [select]:
   > runtime.gopark(0xc00049c760?, 0x2?, 0x4?, 0x30?, 0xc00049c72c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00049c598 sp=0xc00049c578 pc=0x13bb516
   > runtime.selectgo(0xc00049c760, 0xc00049c728, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00049c6d8 sp=0xc00049c598 pc=0x13cbbdc
   > github.com/pingcap/badger.(*levelsController).runWorker(0xc000ae81c0, 0xc000da40c0, 0x0)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:212 +0x1fb fp=0xc00049c7b8 sp=0xc00049c6d8 pc=0x32a297b
   > github.com/pingcap/badger.(*levelsController).startCompact.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:180 +0x2e fp=0xc00049c7e0 sp=0xc00049c7b8 pc=0x32a274e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00049c7e8 sp=0xc00049c7e0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.(*levelsController).startCompact
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:180 +0x65
   > goroutine 297 [select]:
   > runtime.gopark(0xc00049cf60?, 0x2?, 0x4?, 0x30?, 0xc00049cf2c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00049cd98 sp=0xc00049cd78 pc=0x13bb516
   > runtime.selectgo(0xc00049cf60, 0xc00049cf28, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00049ced8 sp=0xc00049cd98 pc=0x13cbbdc
   > github.com/pingcap/badger.(*levelsController).runWorker(0xc000ae81c0, 0xc000da40c0, 0x1)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:212 +0x1fb fp=0xc00049cfb8 sp=0xc00049ced8 pc=0x32a297b
   > github.com/pingcap/badger.(*levelsController).startCompact.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:180 +0x2e fp=0xc00049cfe0 sp=0xc00049cfb8 pc=0x32a274e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00049cfe8 sp=0xc00049cfe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.(*levelsController).startCompact
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:180 +0x65
   > goroutine 298 [chan receive]:
   > runtime.gopark(0x0?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00009eac0 sp=0xc00009eaa0 pc=0x13bb516
   > runtime.chanrecv(0xc000af98c0, 0xc00009ec60, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc00009eb50 sp=0xc00009eac0 pc=0x13854bb
   > runtime.chanrecv2(0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc00009eb78 sp=0xc00009eb50 pc=0x1384ff8
   > github.com/pingcap/badger.(*DB).runFlushMemTable(0xc000ebad80, 0x0?)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:920 +0xdd fp=0xc00009efc0 sp=0xc00009eb78 pc=0x3298efd
   > github.com/pingcap/badger.Open.func6()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:361 +0x2a fp=0xc00009efe0 sp=0xc00009efc0 pc=0x329430a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00009efe8 sp=0xc00009efe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.Open
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:361 +0x158d
   > goroutine 884 [chan receive]:
   > runtime.gopark(0xcf947df5?, 0x0?, 0x80?, 0xe?, 0x138c1bf?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0115f0df8 sp=0xc0115f0dd8 pc=0x13bb516
   > runtime.chanrecv(0xc01203b7a0, 0xc0115f0f38, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc0115f0e88 sp=0xc0115f0df8 pc=0x13854bb
   > runtime.chanrecv2(0xc011c3bd00?, 0x35182e0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc0115f0eb0 sp=0xc0115f0e88 pc=0x1384ff8
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Close(0xc011c3bb00)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:123 +0x385 fp=0xc0115f0f58 sp=0xc0115f0eb0 pc=0x305fcc5
   > github.com/pingcap/tidb/executor.(*baseExecutor).Close(0xc010b022a0?)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:181 +0x7c fp=0xc0115f0f98 sp=0xc0115f0f58 pc=0x2feeadc
   > github.com/pingcap/tidb/executor.(*ProjectionExec).Close(0xc011f099e0)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:329 +0x1cf fp=0xc0115f1000 sp=0xc0115f0f98 pc=0x30997af
   > github.com/pingcap/tidb/executor.(*recordSet).Close(0xc012047950)
   > 	/go/src/github.com/pingcap/tidb/executor/adapter.go:176 +0x2a fp=0xc0115f1040 sp=0xc0115f1000 pc=0x2f612ca
   > github.com/pingcap/tidb/session.(*execStmtResult).Close(0xc0120728a0)
   > 	/go/src/github.com/pingcap/tidb/session/session.go:1734 +0x36 fp=0xc0115f1090 sp=0xc0115f1040 pc=0x314b676
   > github.com/pingcap/tidb/server.(*tidbResultSet).Close(0x3f35b9291ac54203?)
   > 	/go/src/github.com/pingcap/tidb/server/driver_tidb.go:324 +0x3c fp=0xc0115f10b0 sp=0xc0115f1090 pc=0x31c611c
   > github.com/pingcap/tidb/server.ResultSet.Close-fm()
   > 	<autogenerated>:1 +0x2b fp=0xc0115f10c8 sp=0xc0115f10b0 pc=0x31f7acb
   > github.com/pingcap/tidb/parser/terror.Call(0xc0115f11d8?)
   > 	/go/src/github.com/pingcap/tidb/parser/terror/terror.go:298 +0x31 fp=0xc0115f1208 sp=0xc0115f10c8 pc=0x1b74a51
   > github.com/pingcap/tidb/server.(*clientConn).handleStmt.func1()
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:1911 +0x26 fp=0xc0115f1220 sp=0xc0115f1208 pc=0x31bbd26
   > github.com/pingcap/tidb/server.(*clientConn).handleStmt(0xc0110ec500, {0x400d608, 0xc010664740}, {0x401fff0, 0xc0114831d0}, {0x5f8a1a8, 0x0, 0x0}, 0x1)
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:1934 +0x413 fp=0xc0115f12f0 sp=0xc0115f1220 pc=0x31bbaf3
   > github.com/pingcap/tidb/server.(*clientConn).handleQuery(0xc0110ec500, {0x400d608, 0xc010664740}, {0xc000a68821, 0x18c})
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:1775 +0x774 fp=0xc0115f1468 sp=0xc0115f12f0 pc=0x31ba494
   > github.com/pingcap/tidb/server.(*clientConn).dispatch(0xc0110ec500, {0x400d6b0, 0xc0110f06f0?}, {0xc000a68820, 0x18d, 0x18d})
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:1279 +0x1025 fp=0xc0115f1858 sp=0xc0115f1468 pc=0x31b6045
   > github.com/pingcap/tidb/server.(*clientConn).Run(0xc0110ec500, {0x400d6b0, 0xc0110f06f0})
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:1034 +0x253 fp=0xc0115f1e18 sp=0xc0115f1858 pc=0x31b2b33
   > github.com/pingcap/tidb/server.(*Server).onConn(0xc0059ae9c0, 0xc0110ec500)
   > 	/go/src/github.com/pingcap/tidb/server/server.go:550 +0x6c5 fp=0xc0115f1fc0 sp=0xc0115f1e18 pc=0x31e4165
   > github.com/pingcap/tidb/server.(*Server).startNetworkListener.func2()
   > 	/go/src/github.com/pingcap/tidb/server/server.go:453 +0x2a fp=0xc0115f1fe0 sp=0xc0115f1fc0 pc=0x31e300a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0115f1fe8 sp=0xc0115f1fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/server.(*Server).startNetworkListener
   > 	/go/src/github.com/pingcap/tidb/server/server.go:453 +0x5ca
   > goroutine 765 [select]:
   > runtime.gopark(0xc010025eb0?, 0x2?, 0x16?, 0x0?, 0xc010025e5c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010025cc8 sp=0xc010025ca8 pc=0x13bb516
   > runtime.selectgo(0xc010025eb0, 0xc010025e58, 0xc0059ae9c0?, 0x0, 0x2?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010025e08 sp=0xc010025cc8 pc=0x13cbbdc
   > github.com/pingcap/tidb/util/expensivequery.(*Handle).Run(0xc0003a2078)
   > 	/go/src/github.com/pingcap/tidb/util/expensivequery/expensivequery.go:61 +0x198 fp=0xc010025fc8 sp=0xc010025e08 pc=0x2695d58
   > main.createServer.func1()
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:675 +0x26 fp=0xc010025fe0 sp=0xc010025fc8 pc=0x33b2be6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010025fe8 sp=0xc010025fe0 pc=0x13ee6e1
   > created by main.createServer
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:675 +0x439
   > goroutine 436 [select]:
   > runtime.gopark(0xc000daaf78?, 0x3?, 0x25?, 0x48?, 0xc000daaf32?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000daad98 sp=0xc000daad78 pc=0x13bb516
   > runtime.selectgo(0xc000daaf78, 0xc000daaf2c, 0x1?, 0x0, 0xc000161a00?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000daaed8 sp=0xc000daad98 pc=0x13cbbdc
   > github.com/pingcap/badger.(*writeWorker).runWriteVLog(0xc000726100, 0xc000b20018)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:94 +0x137 fp=0xc000daafc0 sp=0xc000daaed8 pc=0x32b28b7
   > github.com/pingcap/badger.startWriteWorker.func2()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:64 +0x2a fp=0xc000daafe0 sp=0xc000daafc0 pc=0x32b238a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000daafe8 sp=0xc000daafe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.startWriteWorker
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:64 +0x1f9
   > goroutine 437 [chan receive, locked to thread]:
   > runtime.gopark(0xc000dabe98?, 0x1456628?, 0xf?, 0x0?, 0x1?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000dabe68 sp=0xc000dabe48 pc=0x13bb516
   > runtime.chanrecv(0xc000ee7320, 0xc000dabf88, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000dabef8 sp=0xc000dabe68 pc=0x13854bb
   > runtime.chanrecv2(0xc000e978c0?, 0x3f047820e7c5e643?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc000dabf20 sp=0xc000dabef8 pc=0x1384ff8
   > github.com/pingcap/badger.(*writeWorker).runWriteLSM(0xc000726100, 0x0?)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:141 +0x15e fp=0xc000dabfc0 sp=0xc000dabf20 pc=0x32b2efe
   > github.com/pingcap/badger.startWriteWorker.func3()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:65 +0x2a fp=0xc000dabfe0 sp=0xc000dabfc0 pc=0x32b232a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000dabfe8 sp=0xc000dabfe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.startWriteWorker
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:65 +0x24d
   > goroutine 438 [chan receive]:
   > runtime.gopark(0xc000f00078?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000dbfea8 sp=0xc000dbfe88 pc=0x13bb516
   > runtime.chanrecv(0xc000ee7380, 0xc000dbff88, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000dbff38 sp=0xc000dbfea8 pc=0x13854bb
   > runtime.chanrecv2(0xc000c62020?, 0x0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc000dbff60 sp=0xc000dbff38 pc=0x1384ff8
   > github.com/pingcap/badger.(*writeWorker).runMergeLSM(0xc000b1c238?, 0x174b991?)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:154 +0x9b fp=0xc000dbffc0 sp=0xc000dbff60 pc=0x32b307b
   > github.com/pingcap/badger.startWriteWorker.func4()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:66 +0x2a fp=0xc000dbffe0 sp=0xc000dbffc0 pc=0x32b22ca
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000dbffe8 sp=0xc000dbffe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.startWriteWorker
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:66 +0x2a5
   > goroutine 439 [select]:
   > runtime.gopark(0xc000dacf88?, 0x2?, 0x0?, 0x0?, 0xc000dacf4c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000dacda0 sp=0xc000dacd80 pc=0x13bb516
   > runtime.selectgo(0xc000dacf88, 0xc000dacf48, 0xc010b72060?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000dacee0 sp=0xc000dacda0 pc=0x13cbbdc
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.writeDBWorker.run({0xc000ee7440?, 0xc000ceac40?})
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:96 +0x145 fp=0xc000dacfc0 sp=0xc000dacee0 pc=0x3308de5
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*dbWriter).Open.func1()
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:202 +0x2a fp=0xc000dacfe0 sp=0xc000dacfc0 pc=0x330996a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000dacfe8 sp=0xc000dacfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*dbWriter).Open
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:199 +0xc5
   > goroutine 440 [select]:
   > runtime.gopark(0xc00009de70?, 0x2?, 0x90?, 0xde?, 0xc00009de1c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00009dc58 sp=0xc00009dc38 pc=0x13bb516
   > runtime.selectgo(0xc00009de70, 0xc00009de18, 0x13?, 0x0, 0xc0108f8600?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00009dd98 sp=0xc00009dc58 pc=0x13cbbdc
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.writeLockWorker.run({0xc000ee74a0?, 0xc000ceac40?})
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:148 +0x15f fp=0xc00009dfc0 sp=0xc00009dd98 pc=0x33093bf
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*dbWriter).Open.func2()
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:209 +0x2a fp=0xc00009dfe0 sp=0xc00009dfc0 pc=0x330990a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00009dfe8 sp=0xc00009dfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*dbWriter).Open
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:206 +0x159
   > goroutine 441 [select]:
   > runtime.gopark(0xc000b18718?, 0x2?, 0x0?, 0xbe?, 0xc000b18704?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000b18588 sp=0xc000b18568 pc=0x13bb516
   > runtime.selectgo(0xc000b18718, 0xc000b18700, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000b186c8 sp=0xc000b18588 pc=0x13cbbdc
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*MVCCStore).runUpdateSafePointLoop(0xc00075ba80)
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:1550 +0x217 fp=0xc000b187c8 sp=0xc000b186c8 pc=0x32facd7
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.NewMVCCStore.func1()
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:85 +0x26 fp=0xc000b187e0 sp=0xc000b187c8 pc=0x32ed406
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000b187e8 sp=0xc000b187e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.NewMVCCStore
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:85 +0x337
   > goroutine 442 [select]:
   > runtime.gopark(0xc000b18fb0?, 0x2?, 0x0?, 0x0?, 0xc000b18f9c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000b18e28 sp=0xc000b18e08 pc=0x13bb516
   > runtime.selectgo(0xc000b18fb0, 0xc000b18f98, 0xc000b191f0?, 0x0, 0xc000b5f598?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000b18f68 sp=0xc000b18e28 pc=0x13cbbdc
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*MVCCStore).StartDeadlockDetection.func1()
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:1286 +0x7b fp=0xc000b18fe0 sp=0xc000b18f68 pc=0x32f895b
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000b18fe8 sp=0xc000b18fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*MVCCStore).StartDeadlockDetection
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:1284 +0xb6
   > goroutine 443 [select]:
   > runtime.gopark(0xc0000a2f78?, 0x2?, 0x0?, 0x30?, 0xc0000a2f3c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0000a2dc0 sp=0xc0000a2da0 pc=0x13bb516
   > runtime.selectgo(0xc0000a2f78, 0xc0000a2f38, 0xc000b1b7b0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0000a2f00 sp=0xc0000a2dc0 pc=0x13cbbdc
   > github.com/tikv/client-go/v2/oracle/oracles.(*pdOracle).updateTS(0xc000a2c850, {0x400d640, 0xc000056058}, 0x0?)
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/oracle/oracles/pd.go:229 +0x128 fp=0xc0000a2fb0 sp=0xc0000a2f00 pc=0x1e9b548
   > github.com/tikv/client-go/v2/oracle/oracles.NewPdOracle.func1()
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/oracle/oracles/pd.go:77 +0x32 fp=0xc0000a2fe0 sp=0xc0000a2fb0 pc=0x1e9a772
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000a2fe8 sp=0xc0000a2fe0 pc=0x13ee6e1
   > created by github.com/tikv/client-go/v2/oracle/oracles.NewPdOracle
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/oracle/oracles/pd.go:77 +0x119
   > goroutine 444 [select]:
   > runtime.gopark(0xc000b1ff78?, 0x3?, 0x20?, 0x0?, 0xc000b1ff5a?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000b1fde0 sp=0xc000b1fdc0 pc=0x13bb516
   > runtime.selectgo(0xc000b1ff78, 0xc000b1ff54, 0x1000200000002?, 0x0, 0xc000630260?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000b1ff20 sp=0xc000b1fde0 pc=0x13cbbdc
   > github.com/tikv/client-go/v2/internal/locate.(*RegionCache).asyncCheckAndResolveLoop(0xc00075bb80, 0xc000b20018?)
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/internal/locate/region_cache.go:399 +0xd1 fp=0xc000b1ffc0 sp=0xc000b1ff20 pc=0x1e6bff1
   > github.com/tikv/client-go/v2/internal/locate.NewRegionCache.func1()
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/internal/locate/region_cache.go:370 +0x2a fp=0xc000b1ffe0 sp=0xc000b1ffc0 pc=0x1e6bc6a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000b1ffe8 sp=0xc000b1ffe0 pc=0x13ee6e1
   > created by github.com/tikv/client-go/v2/internal/locate.NewRegionCache
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/internal/locate/region_cache.go:370 +0x2e6
   > goroutine 445 [select]:
   > runtime.gopark(0xc000b1df10?, 0x2?, 0x0?, 0x30?, 0xc000b1deac?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000dbbd10 sp=0xc000dbbcf0 pc=0x13bb516
   > runtime.selectgo(0xc000dbbf10, 0xc000b1dea8, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000dbbe50 sp=0xc000dbbd10 pc=0x13cbbdc
   > github.com/tikv/client-go/v2/tikv.(*KVStore).runSafePointChecker(0xc000c48360)
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/tikv/kv.go:264 +0x12b fp=0xc000dbbfc8 sp=0xc000dbbe50 pc=0x1ed6f0b
   > github.com/tikv/client-go/v2/tikv.NewKVStore.func1()
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/tikv/kv.go:187 +0x26 fp=0xc000dbbfe0 sp=0xc000dbbfc8 pc=0x1ed6d06
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000dbbfe8 sp=0xc000dbbfe0 pc=0x13ee6e1
   > created by github.com/tikv/client-go/v2/tikv.NewKVStore
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/tikv/kv.go:187 +0x3d6
   > goroutine 446 [select]:
   > runtime.gopark(0xc010becf80?, 0x2?, 0x0?, 0xbe?, 0xc010becf44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010becdc8 sp=0xc010becda8 pc=0x13bb516
   > runtime.selectgo(0xc010becf80, 0xc010becf40, 0xc000c44500?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010becf08 sp=0xc010becdc8 pc=0x13cbbdc
   > github.com/tikv/client-go/v2/tikv.(*KVStore).safeTSUpdater(0xc000c48360)
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/tikv/kv.go:544 +0x165 fp=0xc010becfc8 sp=0xc010becf08 pc=0x1ed8e65
   > github.com/tikv/client-go/v2/tikv.NewKVStore.func2()
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/tikv/kv.go:188 +0x26 fp=0xc010becfe0 sp=0xc010becfc8 pc=0x1ed6ca6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010becfe8 sp=0xc010becfe0 pc=0x13ee6e1
   > created by github.com/tikv/client-go/v2/tikv.NewKVStore
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/tikv/kv.go:188 +0x416
   > goroutine 447 [select]:
   > runtime.gopark(0xc000ee0f98?, 0x2?, 0x0?, 0x0?, 0xc000ee0f6c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000ee0de8 sp=0xc000ee0dc8 pc=0x13bb516
   > runtime.selectgo(0xc000ee0f98, 0xc000ee0f68, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000ee0f28 sp=0xc000ee0de8 pc=0x13cbbdc
   > github.com/dgraph-io/ristretto.(*defaultPolicy).processItems(0xc000508d80)
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.0.1/policy.go:96 +0x91 fp=0xc000ee0fc8 sp=0xc000ee0f28 pc=0x23cf0d1
   > github.com/dgraph-io/ristretto.newDefaultPolicy.func1()
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.0.1/policy.go:80 +0x26 fp=0xc000ee0fe0 sp=0xc000ee0fc8 pc=0x23cef86
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000ee0fe8 sp=0xc000ee0fe0 pc=0x13ee6e1
   > created by github.com/dgraph-io/ristretto.newDefaultPolicy
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.0.1/policy.go:80 +0x156
   > goroutine 448 [select]:
   > runtime.gopark(0xc000ee2f98?, 0x2?, 0x60?, 0x99?, 0xc000ee2f74?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000ee2df0 sp=0xc000ee2dd0 pc=0x13bb516
   > runtime.selectgo(0xc000ee2f98, 0xc000ee2f70, 0xffffffffffffffff?, 0x0, 0xa?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000ee2f30 sp=0xc000ee2df0 pc=0x13cbbdc
   > github.com/dgraph-io/ristretto.(*Cache).processItems(0xc000ee7860)
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.0.1/cache.go:257 +0x85 fp=0xc000ee2fc8 sp=0xc000ee2f30 pc=0x23ce025
   > github.com/dgraph-io/ristretto.NewCache.func2()
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.0.1/cache.go:155 +0x26 fp=0xc000ee2fe0 sp=0xc000ee2fc8 pc=0x23cd846
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000ee2fe8 sp=0xc000ee2fe0 pc=0x13ee6e1
   > created by github.com/dgraph-io/ristretto.NewCache
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.0.1/cache.go:155 +0x485
   > goroutine 604 [select]:
   > runtime.gopark(0xc0107dff58?, 0x4?, 0xab?, 0x62?, 0xc0107dfda8?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0107dfbf8 sp=0xc0107dfbd8 pc=0x13bb516
   > runtime.selectgo(0xc0107dff58, 0xc0107dfda0, 0xc00009ce38?, 0x0, 0x1?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0107dfd38 sp=0xc0107dfbf8 pc=0x13cbbdc
   > github.com/pingcap/tidb/ddl.(*worker).start(0xc010b10f20, 0xc00fda8180)
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl_worker.go:178 +0x318 fp=0xc0107dffc0 sp=0xc0107dfd38 pc=0x2622e98
   > github.com/pingcap/tidb/ddl.(*ddl).Start.func2()
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:369 +0x2a fp=0xc0107dffe0 sp=0xc0107dffc0 pc=0x25e9a6a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0107dffe8 sp=0xc0107dffe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/ddl.(*ddl).Start
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:369 +0x5c5
   > goroutine 602 [select]:
   > runtime.gopark(0xc00fb3bf38?, 0x2?, 0x0?, 0x0?, 0xc00fb3befc?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fb3bd50 sp=0xc00fb3bd30 pc=0x13bb516
   > runtime.selectgo(0xc00fb3bf38, 0xc00fb3bef8, 0x1?, 0x0, 0x2?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fb3be90 sp=0xc00fb3bd50 pc=0x13cbbdc
   > github.com/pingcap/tidb/ddl.(*ddl).limitDDLJobs(0xc0009c4ee0)
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl_worker.go:263 +0x173 fp=0xc00fb3bfc8 sp=0xc00fb3be90 pc=0x2623fd3
   > github.com/pingcap/tidb/ddl.(*ddl).Start.func1()
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:351 +0x26 fp=0xc00fb3bfe0 sp=0xc00fb3bfc8 pc=0x25e9ac6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fb3bfe8 sp=0xc00fb3bfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/ddl.(*ddl).Start
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:351 +0x2ea
   > goroutine 1267 [select]:
   > runtime.gopark(0xc00049b778?, 0x2?, 0x2?, 0x0?, 0xc00049b6ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00049b558 sp=0xc00049b538 pc=0x13bb516
   > runtime.selectgo(0xc00049b778, 0xc00049b6e8, 0x3aac226?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00049b698 sp=0xc00049b558 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc0105af580, {0x400d6b0?, 0xc01127c9f0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc00049b7b8 sp=0xc00049b698 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc00049b7e0 sp=0xc00049b7b8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00049b7e8 sp=0xc00049b7e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 759 [select]:
   > runtime.gopark(0xc0107fbfa8?, 0x2?, 0x3?, 0x30?, 0xc0107fbf84?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0107fbe08 sp=0xc0107fbde8 pc=0x13bb516
   > runtime.selectgo(0xc0107fbfa8, 0xc0107fbf80, 0xc010adf500?, 0x0, 0xc0105a6fc0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0107fbf48 sp=0xc0107fbe08 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).TelemetryRotateSubWindowLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1169 +0xcc fp=0xc0107fbfe0 sp=0xc0107fbf48 pc=0x26a5c4c
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0107fbfe8 sp=0xc0107fbfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).TelemetryRotateSubWindowLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1162 +0x8f
   > goroutine 762 [select]:
   > runtime.gopark(0xc0112eff78?, 0x2?, 0x3?, 0x30?, 0xc0112eff4c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0112efdd0 sp=0xc0112efdb0 pc=0x13bb516
   > runtime.selectgo(0xc0112eff78, 0xc0112eff48, 0xc0106d8af0?, 0x0, 0xc00049d658?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0112eff10 sp=0xc0112efdd0 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).autoAnalyzeWorker(0xc0008c8a20, {0x401ea10, 0xc010685340})
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1425 +0x105 fp=0xc0112effb8 sp=0xc0112eff10 pc=0x26a8bc5
   > github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop.func4()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1262 +0x2e fp=0xc0112effe0 sp=0xc0112effb8 pc=0x26a654e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0112effe8 sp=0xc0112effe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1262 +0x31a
   > goroutine 851 [select]:
   > runtime.gopark(0xc000b1bf40?, 0x2?, 0x4?, 0x0?, 0xc000b1bf04?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000b1bd88 sp=0xc000b1bd68 pc=0x13bb516
   > runtime.selectgo(0xc000b1bf40, 0xc000b1bf00, 0x100000001?, 0x0, 0xc0005a7220?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000b1bec8 sp=0xc000b1bd88 pc=0x13cbbdc
   > github.com/pingcap/tidb/util/topsql/reporter.(*RemoteTopSQLReporter).reportWorker(0xc0059b2d20)
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:499 +0x1ae fp=0xc000b1bfc8 sp=0xc000b1bec8 pc=0x254924e
   > github.com/pingcap/tidb/util/topsql/reporter.NewRemoteTopSQLReporter.func2()
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:161 +0x26 fp=0xc000b1bfe0 sp=0xc000b1bfc8 pc=0x2546bc6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000b1bfe8 sp=0xc000b1bfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/util/topsql/reporter.NewRemoteTopSQLReporter
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:161 +0x1f6
   > goroutine 722 [select]:
   > runtime.gopark(0xc00fd3f6f0?, 0x2?, 0x0?, 0x0?, 0xc00fd3f6bc?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fd3f538 sp=0xc00fd3f518 pc=0x13bb516
   > runtime.selectgo(0xc00fd3f6f0, 0xc00fd3f6b8, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fd3f678 sp=0xc00fd3f538 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).globalConfigSyncerKeeper(0xc0008c8a20)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:510 +0xe5 fp=0xc00fd3f7c8 sp=0xc00fd3f678 pc=0x269f405
   > github.com/pingcap/tidb/domain.(*Domain).Init.func13()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:830 +0x26 fp=0xc00fd3f7e0 sp=0xc00fd3f7c8 pc=0x26a2a06
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fd3f7e8 sp=0xc00fd3f7e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:830 +0xedc
   > goroutine 764 [chan receive]:
   > runtime.gopark(0xc010cd9b38?, 0xc0000e3ba0?, 0x48?, 0x8e?, 0x13d8de5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fd38df0 sp=0xc00fd38dd0 pc=0x13bb516
   > runtime.chanrecv(0xc00fb70900, 0xc00fd38f38, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc00fd38e80 sp=0xc00fd38df0 pc=0x13854bb
   > runtime.chanrecv2(0x9356907420000?, 0xc0003589c0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc00fd38ea8 sp=0xc00fd38e80 pc=0x1384ff8
   > github.com/pingcap/tidb/server.NewServer.func1()
   > 	/go/src/github.com/pingcap/tidb/server/server.go:209 +0x98 fp=0xc00fd38fe0 sp=0xc00fd38ea8 pc=0x31e1638
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fd38fe8 sp=0xc00fd38fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/server.NewServer
   > 	/go/src/github.com/pingcap/tidb/server/server.go:208 +0x32a
   > goroutine 758 [select]:
   > runtime.gopark(0xc0107faf28?, 0x2?, 0x0?, 0x30?, 0xc0107faed4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0107fad48 sp=0xc0107fad28 pc=0x13bb516
   > runtime.selectgo(0xc0107faf28, 0xc0107faed0, 0x9?, 0x0, 0x15?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0107fae88 sp=0xc0107fad48 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).TelemetryReportLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1140 +0x11c fp=0xc0107fafe0 sp=0xc0107fae88 pc=0x26a573c
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0107fafe8 sp=0xc0107fafe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).TelemetryReportLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1132 +0x285
   > goroutine 761 [select]:
   > runtime.gopark(0xc0108f1f28?, 0x6?, 0x50?, 0x60?, 0xc0108f1bb4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0108f1a20 sp=0xc0108f1a00 pc=0x13bb516
   > runtime.selectgo(0xc0108f1f28, 0xc0108f1ba8, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0108f1b60 sp=0xc0108f1a20 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).updateStatsWorker(0xc0008c8a20, {0x309938e?, 0xc000afb300?}, {0x401ea10, 0xc010685340})
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1372 +0x234 fp=0xc0108f1fa8 sp=0xc0108f1b60 pc=0x26a7e54
   > github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop.func3()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1259 +0x36 fp=0xc0108f1fe0 sp=0xc0108f1fa8 pc=0x26a65b6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0108f1fe8 sp=0xc0108f1fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1259 +0x29a
   > goroutine 1089 [select]:
   > runtime.gopark(0xc000ee3f78?, 0x2?, 0x2?, 0x0?, 0xc000ee3eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000ee3d58 sp=0xc000ee3d38 pc=0x13bb516
   > runtime.selectgo(0xc000ee3f78, 0xc000ee3ee8, 0x3aac226?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000ee3e98 sp=0xc000ee3d58 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc0105af500, {0x400d6b0?, 0xc01127c9f0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc000ee3fb8 sp=0xc000ee3e98 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc000ee3fe0 sp=0xc000ee3fb8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000ee3fe8 sp=0xc000ee3fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 1147 [select]:
   > runtime.gopark(0xc010e6ae10?, 0x2?, 0x78?, 0xb2?, 0xc010e6ad8c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010e6abe0 sp=0xc010e6abc0 pc=0x13bb516
   > runtime.selectgo(0xc010e6ae10, 0xc010e6ad88, 0xc00feeb190?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010e6ad20 sp=0xc010e6abe0 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc011c3b8c0, 0x2, {0x5f8a1a8, 0x0, 0x0})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:441 +0x4f4 fp=0xc010e6af10 sp=0xc010e6ad20 pc=0x30626b4
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:335 +0xb3 fp=0xc010e6af90 sp=0xc010e6af10 pc=0x30613d3
   > github.com/pingcap/tidb/util.WithRecovery(0x400d6b0?, 0xc012003a10?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc010e6afc0 sp=0xc010e6af90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x2a fp=0xc010e6afe0 sp=0xc010e6afc0 pc=0x30612ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010e6afe8 sp=0xc010e6afe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x1c9
   > goroutine 797 [select]:
   > runtime.gopark(0xc0107fb718?, 0x3?, 0x0?, 0x30?, 0xc0107fb68a?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0107becc8 sp=0xc0107beca8 pc=0x13bb516
   > runtime.selectgo(0xc0107bef18, 0xc0107fb684, 0x0?, 0x0, 0x13bb516?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0107bee08 sp=0xc0107becc8 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).LoadSysVarCacheLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:989 +0x145 fp=0xc0107befe0 sp=0xc0107bee08 pc=0x26a3dc5
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0107befe8 sp=0xc0107befe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).LoadSysVarCacheLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:980 +0x172
   > goroutine 767 [syscall]:
   > runtime.notetsleepg(0x13c2505?, 0xc0005dcc80?)
   > 	/usr/local/go/src/runtime/lock_futex.go:236 +0x34 fp=0xc0107f9fa0 sp=0xc0107f9f68 pc=0x138acd4
   > os/signal.signal_recv()
   > 	/usr/local/go/src/runtime/sigqueue.go:152 +0x2f fp=0xc0107f9fc0 sp=0xc0107f9fa0 pc=0x13ea6cf
   > os/signal.loop()
   > 	/usr/local/go/src/os/signal/signal_unix.go:23 +0x19 fp=0xc0107f9fe0 sp=0xc0107f9fc0 pc=0x2cac7f9
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0107f9fe8 sp=0xc0107f9fe0 pc=0x13ee6e1
   > created by os/signal.Notify.func1.1
   > 	/usr/local/go/src/os/signal/signal.go:151 +0x2a
   > goroutine 768 [chan receive]:
   > runtime.gopark(0x5f8be00?, 0xc0107f9720?, 0x28?, 0xc3?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0107f96a0 sp=0xc0107f9680 pc=0x13bb516
   > runtime.chanrecv(0xc0105a7c80, 0xc0107f97a0, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc0107f9730 sp=0xc0107f96a0 pc=0x13854bb
   > runtime.chanrecv1(0xc0107f97d0?, 0x2fe82d7?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc0107f9758 sp=0xc0107f9730 pc=0x1384fb8
   > github.com/pingcap/tidb/util/signal.SetupSignalHandler.func1()
   > 	/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:37 +0x4f fp=0xc0107f97e0 sp=0xc0107f9758 pc=0x33ac32f
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0107f97e8 sp=0xc0107f97e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/util/signal.SetupSignalHandler
   > 	/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:34 +0xb6
   > goroutine 769 [chan receive]:
   > runtime.gopark(0x13f4d05?, 0x0?, 0x0?, 0x0?, 0xc010b25f58?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010b25e60 sp=0xc010b25e40 pc=0x13bb516
   > runtime.chanrecv(0xc0105a7ce0, 0xc010b25f80, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc010b25ef0 sp=0xc010b25e60 pc=0x13854bb
   > runtime.chanrecv1(0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc010b25f18 sp=0xc010b25ef0 pc=0x1384fb8
   > github.com/pingcap/tidb/util/signal.SetupSignalHandler.func2()
   > 	/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:53 +0x45 fp=0xc010b25fe0 sp=0xc010b25f18 pc=0x33ac105
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010b25fe8 sp=0xc010b25fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/util/signal.SetupSignalHandler
   > 	/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:52 +0x19f
   > goroutine 852 [sleep]:
   > runtime.gopark(0x3adb52d7b390?, 0x0?, 0x88?, 0x1f?, 0x25412d5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010b21f58 sp=0xc010b21f38 pc=0x13bb516
   > time.Sleep(0x3b9aca00)
   > 	/usr/local/go/src/runtime/time.go:195 +0x135 fp=0xc010b21f98 sp=0xc010b21f58 pc=0x13eaf15
   > github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).startCPUProfileWorker(0xc000056058?)
   > 	/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:115 +0x65 fp=0xc010b21fc8 sp=0xc010b21f98 pc=0x2540065
   > github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).Run.func1()
   > 	/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:93 +0x26 fp=0xc010b21fe0 sp=0xc010b21fc8 pc=0x253fea6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010b21fe8 sp=0xc010b21fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).Run
   > 	/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:93 +0xca
   > goroutine 850 [select]:
   > runtime.gopark(0xc010b21780?, 0x3?, 0x4?, 0x30?, 0xc010b2173a?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010b215a8 sp=0xc010b21588 pc=0x13bb516
   > runtime.selectgo(0xc010b21780, 0xc010b21734, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010b216e8 sp=0xc010b215a8 pc=0x13cbbdc
   > github.com/pingcap/tidb/util/topsql/reporter.(*RemoteTopSQLReporter).collectWorker(0xc0059b2d20)
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:327 +0x13a fp=0xc010b217c8 sp=0xc010b216e8 pc=0x2547eda
   > github.com/pingcap/tidb/util/topsql/reporter.NewRemoteTopSQLReporter.func1()
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:160 +0x26 fp=0xc010b217e0 sp=0xc010b217c8 pc=0x2546c26
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010b217e8 sp=0xc010b217e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/util/topsql/reporter.NewRemoteTopSQLReporter
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:160 +0x1b6
   > goroutine 605 [select]:
   > runtime.gopark(0xc0107e3f58?, 0x4?, 0xab?, 0x62?, 0xc0107e3da8?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0107e3bf8 sp=0xc0107e3bd8 pc=0x13bb516
   > runtime.selectgo(0xc0107e3f58, 0xc0107e3da0, 0xc000e2ee38?, 0x0, 0x1?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0107e3d38 sp=0xc0107e3bf8 pc=0x13cbbdc
   > github.com/pingcap/tidb/ddl.(*worker).start(0xc010b10fd0, 0xc00fda8180)
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl_worker.go:178 +0x318 fp=0xc0107e3fc0 sp=0xc0107e3d38 pc=0x2622e98
   > github.com/pingcap/tidb/ddl.(*ddl).Start.func2()
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:369 +0x2a fp=0xc0107e3fe0 sp=0xc0107e3fc0 pc=0x25e9a6a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0107e3fe8 sp=0xc0107e3fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/ddl.(*ddl).Start
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:369 +0x5c5
   > goroutine 766 [select, locked to thread]:
   > runtime.gopark(0xc000b1cfa8?, 0x2?, 0x6?, 0x0?, 0xc000b1cfa4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000b1ce18 sp=0xc000b1cdf8 pc=0x13bb516
   > runtime.selectgo(0xc000b1cfa8, 0xc000b1cfa0, 0x0?, 0x0, 0xc010aea120?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000b1cf58 sp=0xc000b1ce18 pc=0x13cbbdc
   > runtime.ensureSigM.func1()
   > 	/usr/local/go/src/runtime/signal_unix.go:995 +0x1b0 fp=0xc000b1cfe0 sp=0xc000b1cf58 pc=0x13d0070
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000b1cfe8 sp=0xc000b1cfe0 pc=0x13ee6e1
   > created by runtime.ensureSigM
   > 	/usr/local/go/src/runtime/signal_unix.go:978 +0xbd
   > goroutine 854 [IO wait]:
   > runtime.gopark(0x3?, 0xc0106384e0?, 0x6?, 0x0?, 0xc000d4b8d0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000d4b860 sp=0xc000d4b840 pc=0x13bb516
   > runtime.netpollblock(0x203004?, 0x106384e0?, 0xc0?)
   > 	/usr/local/go/src/runtime/netpoll.go:526 +0xf7 fp=0xc000d4b898 sp=0xc000d4b860 pc=0x13b38f7
   > internal/poll.runtime_pollWait(0x7f209a265618, 0x72)
   > 	/usr/local/go/src/runtime/netpoll.go:305 +0x89 fp=0xc000d4b8b8 sp=0xc000d4b898 pc=0x13e7d09
   > internal/poll.(*pollDesc).wait(0xc000e7dd80?, 0xc01061f0e0?, 0x0)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:84 +0x32 fp=0xc000d4b8e0 sp=0xc000d4b8b8 pc=0x1465192
   > internal/poll.(*pollDesc).waitRead(...)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:89
   > internal/poll.(*FD).Accept(0xc000e7dd80)
   > 	/usr/local/go/src/internal/poll/fd_unix.go:614 +0x234 fp=0xc000d4b978 sp=0xc000d4b8e0 pc=0x146a594
   > net.(*netFD).accept(0xc000e7dd80)
   > 	/usr/local/go/src/net/fd_unix.go:172 +0x35 fp=0xc000d4ba30 sp=0xc000d4b978 pc=0x1589055
   > net.(*TCPListener).accept(0xc0104d3668)
   > 	/usr/local/go/src/net/tcpsock_posix.go:142 +0x28 fp=0xc000d4ba60 sp=0xc000d4ba30 pc=0x15a5088
   > net.(*TCPListener).Accept(0xc0104d3668)
   > 	/usr/local/go/src/net/tcpsock.go:288 +0x3d fp=0xc000d4ba90 sp=0xc000d4ba60 pc=0x15a40fd
   > github.com/soheilhy/cmux.(*cMux).Serve(0xc010a2a000)
   > 	/go/pkg/mod/github.com/soheilhy/cmux@v0.1.4/cmux.go:162 +0xa9 fp=0xc000d4bb20 sp=0xc000d4ba90 pc=0x2dc5da9
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer(0xc0059ae9c0, 0xc010565100)
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:466 +0x4f7 fp=0xc000d4bc90 sp=0xc000d4bb20 pc=0x31dab17
   > github.com/pingcap/tidb/server.(*Server).startHTTPServer(0xc0059ae9c0)
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:442 +0x15d0 fp=0xc000d4bfc8 sp=0xc000d4bc90 pc=0x31d9f10
   > github.com/pingcap/tidb/server.(*Server).startStatusHTTP.func1()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:62 +0x26 fp=0xc000d4bfe0 sp=0xc000d4bfc8 pc=0x31d65c6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000d4bfe8 sp=0xc000d4bfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/server.(*Server).startStatusHTTP
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:62 +0x56
   > goroutine 855 [IO wait]:
   > runtime.gopark(0x18?, 0xc00590e000?, 0x40?, 0x28?, 0xc0107bfb70?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0107bfb00 sp=0xc0107bfae0 pc=0x13bb516
   > runtime.netpollblock(0x14?, 0x2432d05?, 0x0?)
   > 	/usr/local/go/src/runtime/netpoll.go:526 +0xf7 fp=0xc0107bfb38 sp=0xc0107bfb00 pc=0x13b38f7
   > internal/poll.runtime_pollWait(0x7f209a2657f8, 0x72)
   > 	/usr/local/go/src/runtime/netpoll.go:305 +0x89 fp=0xc0107bfb58 sp=0xc0107bfb38 pc=0x13e7d09
   > internal/poll.(*pollDesc).wait(0xc000e7db80?, 0xc0107bfd20?, 0x0)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:84 +0x32 fp=0xc0107bfb80 sp=0xc0107bfb58 pc=0x1465192
   > internal/poll.(*pollDesc).waitRead(...)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:89
   > internal/poll.(*FD).Accept(0xc000e7db80)
   > 	/usr/local/go/src/internal/poll/fd_unix.go:614 +0x234 fp=0xc0107bfc18 sp=0xc0107bfb80 pc=0x146a594
   > net.(*netFD).accept(0xc000e7db80)
   > 	/usr/local/go/src/net/fd_unix.go:172 +0x35 fp=0xc0107bfcd0 sp=0xc0107bfc18 pc=0x1589055
   > net.(*TCPListener).accept(0xc0104d3650)
   > 	/usr/local/go/src/net/tcpsock_posix.go:142 +0x28 fp=0xc0107bfd00 sp=0xc0107bfcd0 pc=0x15a5088
   > net.(*TCPListener).Accept(0xc0104d3650)
   > 	/usr/local/go/src/net/tcpsock.go:288 +0x3d fp=0xc0107bfd30 sp=0xc0107bfd00 pc=0x15a40fd
   > github.com/pingcap/tidb/server.(*Server).startNetworkListener(0xc0059ae9c0, {0x400b9b0, 0xc0104d3650}, 0x0, 0xc000b1c668?)
   > 	/go/src/github.com/pingcap/tidb/server/server.go:383 +0xa6 fp=0xc0107bffa8 sp=0xc0107bfd30 pc=0x31e25a6
   > github.com/pingcap/tidb/server.(*Server).Run.func1()
   > 	/go/src/github.com/pingcap/tidb/server/server.go:368 +0x34 fp=0xc0107bffe0 sp=0xc0107bffa8 pc=0x31e24d4
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0107bffe8 sp=0xc0107bffe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/server.(*Server).Run
   > 	/go/src/github.com/pingcap/tidb/server/server.go:368 +0x145
   > goroutine 853 [chan receive]:
   > runtime.gopark(0xc000e925a0?, 0xc010a6baa0?, 0x20?, 0xbc?, 0x100000000000058?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000b1ede0 sp=0xc000b1edc0 pc=0x13bb516
   > runtime.chanrecv(0xc0002fa840, 0xc000b1ef08, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000b1ee70 sp=0xc000b1ede0 pc=0x13854bb
   > runtime.chanrecv1(0x0?, 0xe?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc000b1ee98 sp=0xc000b1ee70 pc=0x1384fb8
   > github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).startAnalyzeProfileWorker(0xc0004d1b90)
   > 	/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:142 +0x7c fp=0xc000b1efc8 sp=0xc000b1ee98 pc=0x25402bc
   > github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).Run.func2()
   > 	/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:94 +0x26 fp=0xc000b1efe0 sp=0xc000b1efc8 pc=0x253fe46
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000b1efe8 sp=0xc000b1efe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).Run
   > 	/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:94 +0x10a
   > goroutine 733 [select]:
   > runtime.gopark(0xc000da7f28?, 0x2?, 0x4?, 0x30?, 0xc000da7ed4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000da7d48 sp=0xc000da7d28 pc=0x13bb516
   > runtime.selectgo(0xc000da7f28, 0xc000da7ed0, 0xc00052b800?, 0x0, 0xc0009868c0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000da7e88 sp=0xc000da7d48 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).handleEvolvePlanTasksLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1106 +0x107 fp=0xc000da7fe0 sp=0xc000da7e88 pc=0x26a4fe7
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000da7fe8 sp=0xc000da7fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).handleEvolvePlanTasksLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1099 +0xe5
   > goroutine 856 [IO wait]:
   > runtime.gopark(0x7f2071a3ff00?, 0xc000e2eb58?, 0xeb?, 0x6d?, 0xc000e2eb78?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000e2eb08 sp=0xc000e2eae8 pc=0x13bb516
   > runtime.netpollblock(0x7f2073097308?, 0x67?, 0x0?)
   > 	/usr/local/go/src/runtime/netpoll.go:526 +0xf7 fp=0xc000e2eb40 sp=0xc000e2eb08 pc=0x13b38f7
   > internal/poll.runtime_pollWait(0x7f209a265708, 0x72)
   > 	/usr/local/go/src/runtime/netpoll.go:305 +0x89 fp=0xc000e2eb60 sp=0xc000e2eb40 pc=0x13e7d09
   > internal/poll.(*pollDesc).wait(0xc000e7dc00?, 0x1?, 0x0)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:84 +0x32 fp=0xc000e2eb88 sp=0xc000e2eb60 pc=0x1465192
   > internal/poll.(*pollDesc).waitRead(...)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:89
   > internal/poll.(*FD).Accept(0xc000e7dc00)
   > 	/usr/local/go/src/internal/poll/fd_unix.go:614 +0x234 fp=0xc000e2ec20 sp=0xc000e2eb88 pc=0x146a594
   > net.(*netFD).accept(0xc000e7dc00)
   > 	/usr/local/go/src/net/fd_unix.go:172 +0x35 fp=0xc000e2ecd8 sp=0xc000e2ec20 pc=0x1589055
   > net.(*UnixListener).accept(0x7f2073072078?)
   > 	/usr/local/go/src/net/unixsock_posix.go:166 +0x1c fp=0xc000e2ed00 sp=0xc000e2ecd8 pc=0x15aba1c
   > net.(*UnixListener).Accept(0xc010579b00)
   > 	/usr/local/go/src/net/unixsock.go:260 +0x3d fp=0xc000e2ed30 sp=0xc000e2ed00 pc=0x15aa0bd
   > github.com/pingcap/tidb/server.(*Server).startNetworkListener(0xc0059ae9c0, {0x400b9e0, 0xc010579b00}, 0x1, 0xc010b237b8?)
   > 	/go/src/github.com/pingcap/tidb/server/server.go:383 +0xa6 fp=0xc000e2efa8 sp=0xc000e2ed30 pc=0x31e25a6
   > github.com/pingcap/tidb/server.(*Server).Run.func2()
   > 	/go/src/github.com/pingcap/tidb/server/server.go:369 +0x37 fp=0xc000e2efe0 sp=0xc000e2efa8 pc=0x31e2477
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000e2efe8 sp=0xc000e2efe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/server.(*Server).Run
   > 	/go/src/github.com/pingcap/tidb/server/server.go:369 +0x1db
   > goroutine 732 [select]:
   > runtime.gopark(0xc0112f3e90?, 0x3?, 0x20?, 0xf9?, 0xc0112f3e02?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0112f3c70 sp=0xc0112f3c50 pc=0x13bb516
   > runtime.selectgo(0xc0112f3e90, 0xc0112f3dfc, 0x3a8be78?, 0x0, 0x141f32a?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0112f3db0 sp=0xc0112f3c70 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).globalBindHandleWorkerLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1071 +0x16f fp=0xc0112f3fe0 sp=0xc0112f3db0 pc=0x26a476f
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0112f3fe8 sp=0xc0112f3fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).globalBindHandleWorkerLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1058 +0xad
   > goroutine 723 [select]:
   > runtime.gopark(0xc00008be78?, 0x3?, 0x4?, 0x30?, 0xc00008bdf2?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008bc78 sp=0xc00008bc58 pc=0x13bb516
   > runtime.selectgo(0xc00008be78, 0xc00008bdec, 0x1?, 0x0, 0x2?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00008bdb8 sp=0xc00008bc78 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).topologySyncerKeeper(0xc0008c8a20)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:533 +0x165 fp=0xc00008bfc8 sp=0xc00008bdb8 pc=0x269f8c5
   > github.com/pingcap/tidb/domain.(*Domain).Init.func14()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:834 +0x26 fp=0xc00008bfe0 sp=0xc00008bfc8 pc=0x26a29a6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008bfe8 sp=0xc00008bfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:834 +0xf3d
   > goroutine 609 [select]:
   > runtime.gopark(0xc000ee16f8?, 0x3?, 0x4?, 0x30?, 0xc000ee1682?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000ee1508 sp=0xc000ee14e8 pc=0x13bb516
   > runtime.selectgo(0xc000ee16f8, 0xc000ee167c, 0x0?, 0x0, 0xc010ac49c0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000ee1648 sp=0xc000ee1508 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).infoSyncerKeeper(0xc0008c8a20)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:487 +0x165 fp=0xc000ee17c8 sp=0xc000ee1648 pc=0x269ee45
   > github.com/pingcap/tidb/domain.(*Domain).Init.func12()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:829 +0x26 fp=0xc000ee17e0 sp=0xc000ee17c8 pc=0x26a2a66
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000ee17e8 sp=0xc000ee17e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:829 +0xe95
   > goroutine 608 [select]:
   > runtime.gopark(0xc00fd3ef78?, 0x3?, 0x4?, 0x30?, 0xc00fd3ef12?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fd3ed60 sp=0xc00fd3ed40 pc=0x13bb516
   > runtime.selectgo(0xc00fd3ef78, 0xc00fd3ef0c, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fd3eea0 sp=0xc00fd3ed60 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).topNSlowQueryLoop(0xc0008c8a20)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:455 +0x194 fp=0xc00fd3efc8 sp=0xc00fd3eea0 pc=0x269e914
   > github.com/pingcap/tidb/domain.(*Domain).Init.func11()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:828 +0x26 fp=0xc00fd3efe0 sp=0xc00fd3efc8 pc=0x26a2ac6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fd3efe8 sp=0xc00fd3efe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:828 +0xe52
   > goroutine 607 [select]:
   > runtime.gopark(0xc010021f50?, 0x4?, 0x4?, 0x30?, 0xc010021d00?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010021b78 sp=0xc010021b58 pc=0x13bb516
   > runtime.selectgo(0xc010021f50, 0xc010021cf8, 0x400ccd0?, 0x0, 0x1e?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010021cb8 sp=0xc010021b78 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).loadSchemaInLoop(0xc0008c8a20, {0x400d608, 0xc000e32240}, 0xc00049b7b8?)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:565 +0x1aa fp=0xc010021fb0 sp=0xc010021cb8 pc=0x26a00aa
   > github.com/pingcap/tidb/domain.(*Domain).Init.func10()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:825 +0x32 fp=0xc010021fe0 sp=0xc010021fb0 pc=0x26a2b32
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010021fe8 sp=0xc010021fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:825 +0xdeb
   > goroutine 794 [select]:
   > runtime.gopark(0xc000b1af18?, 0x3?, 0x0?, 0x30?, 0xc000b1ae9a?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0107bdcd8 sp=0xc0107bdcb8 pc=0x13bb516
   > runtime.selectgo(0xc0107bdf18, 0xc000b1ae94, 0xc0005e2ae0?, 0x0, 0xc010577ec0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0107bde18 sp=0xc0107bdcd8 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).LoadPrivilegeLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:939 +0x145 fp=0xc0107bdfe0 sp=0xc0107bde18 pc=0x26a3585
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0107bdfe8 sp=0xc0107bdfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).LoadPrivilegeLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:930 +0x205
   > goroutine 603 [select]:
   > runtime.gopark(0xc000dbef90?, 0x2?, 0x0?, 0x0?, 0xc000dbef6c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000dbedf0 sp=0xc000dbedd0 pc=0x13bb516
   > runtime.selectgo(0xc000dbef90, 0xc000dbef68, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000dbef30 sp=0xc000dbedf0 pc=0x13cbbdc
   > github.com/pingcap/tidb/ddl.(*delRange).startEmulator(0xc01062c420)
   > 	/go/src/github.com/pingcap/tidb/ddl/delete_range.go:144 +0x125 fp=0xc000dbefc8 sp=0xc000dbef30 pc=0x262b9e5
   > github.com/pingcap/tidb/ddl.(*delRange).start.func1()
   > 	/go/src/github.com/pingcap/tidb/ddl/delete_range.go:126 +0x26 fp=0xc000dbefe0 sp=0xc000dbefc8 pc=0x262b7a6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000dbefe8 sp=0xc000dbefe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/ddl.(*delRange).start
   > 	/go/src/github.com/pingcap/tidb/ddl/delete_range.go:126 +0x6d
   > goroutine 1145 [select]:
   > runtime.gopark(0xc010e6ee10?, 0x2?, 0x58?, 0xb2?, 0xc010e6ed8c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010e6ebe0 sp=0xc010e6ebc0 pc=0x13bb516
   > runtime.selectgo(0xc010e6ee10, 0xc010e6ed88, 0x8?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010e6ed20 sp=0xc010e6ebe0 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc011c3b8c0, 0x0, {0x5f8a1a8, 0x0, 0x0})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:441 +0x4f4 fp=0xc010e6ef10 sp=0xc010e6ed20 pc=0x30626b4
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:335 +0xb3 fp=0xc010e6ef90 sp=0xc010e6ef10 pc=0x30613d3
   > github.com/pingcap/tidb/util.WithRecovery(0x0?, 0x0?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc010e6efc0 sp=0xc010e6ef90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x2a fp=0xc010e6efe0 sp=0xc010e6efc0 pc=0x30612ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010e6efe8 sp=0xc010e6efe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x1c9
   > goroutine 760 [select]:
   > runtime.gopark(0xc011b4dd48?, 0x2?, 0x18?, 0xef?, 0xc011b4dc94?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc011b4db08 sp=0xc011b4dae8 pc=0x13bb516
   > runtime.selectgo(0xc011b4dd48, 0xc011b4dc90, 0xc0106d8af0?, 0x0, 0x1?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc011b4dc48 sp=0xc011b4db08 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).loadStatsWorker(0xc0008c8a20)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1304 +0x485 fp=0xc011b4dfc8 sp=0xc011b4dc48 pc=0x26a6ea5
   > github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1247 +0x26 fp=0xc011b4dfe0 sp=0xc011b4dfc8 pc=0x26a6666
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc011b4dfe8 sp=0xc011b4dfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1247 +0x105
   > goroutine 763 [select]:
   > runtime.gopark(0xc010b1e7a8?, 0x2?, 0x3?, 0x30?, 0xc010b1e77c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000da8e00 sp=0xc000da8de0 pc=0x13bb516
   > runtime.selectgo(0xc000da8fa8, 0xc010b1e778, 0xc000afb3c0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000da8f40 sp=0xc000da8e00 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).PlanReplayerLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1191 +0xf6 fp=0xc000da8fe0 sp=0xc000da8f40 pc=0x26a5f36
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000da8fe8 sp=0xc000da8fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).PlanReplayerLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1182 +0x6c
   > goroutine 868 [chan receive]:
   > runtime.gopark(0x50?, 0xc010502180?, 0x8?, 0x9d?, 0x138c1bf?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000db9c80 sp=0xc000db9c60 pc=0x13bb516
   > runtime.chanrecv(0xc0101b8fc0, 0xc000db9d48, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000db9d10 sp=0xc000db9c80 pc=0x13854bb
   > runtime.chanrecv2(0x141e886?, 0xc0058b6dd0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc000db9d38 sp=0xc000db9d10 pc=0x1384ff8
   > github.com/soheilhy/cmux.muxListener.Accept(...)
   > 	/go/pkg/mod/github.com/soheilhy/cmux@v0.1.4/cmux.go:229
   > github.com/soheilhy/cmux.(*muxListener).Accept(0x5828400?)
   > 	<autogenerated>:1 +0x45 fp=0xc000db9d68 sp=0xc000db9d38 pc=0x2dc7625
   > net/http.(*onceCloseListener).Accept(0x400d640?)
   > 	<autogenerated>:1 +0x2a fp=0xc000db9d80 sp=0xc000db9d68 pc=0x16e0c6a
   > net/http.(*Server).Serve(0xc01063c000, {0x400cb50, 0xc010690768})
   > 	/usr/local/go/src/net/http/server.go:3070 +0x385 fp=0xc000db9eb0 sp=0xc000db9d80 pc=0x16b6f45
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer.func2()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:462 +0x3e fp=0xc000db9f90 sp=0xc000db9eb0 pc=0x31dadbe
   > github.com/pingcap/tidb/util.WithRecovery(0x400d640?, 0xc000056058?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc000db9fc0 sp=0xc000db9f90 pc=0x1ffabd3
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer.func6()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:461 +0x28 fp=0xc000db9fe0 sp=0xc000db9fc0 pc=0x31dad48
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000db9fe8 sp=0xc000db9fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:461 +0x4ea
   > goroutine 867 [chan receive]:
   > runtime.gopark(0x3a8bf40?, 0xc0107b9cf8?, 0xfc?, 0xb?, 0xa?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0107b9cb0 sp=0xc0107b9c90 pc=0x13bb516
   > runtime.chanrecv(0xc0101b9020, 0xc0107b9d78, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc0107b9d40 sp=0xc0107b9cb0 pc=0x13854bb
   > runtime.chanrecv2(0xc00fd758e8?, 0x2?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc0107b9d68 sp=0xc0107b9d40 pc=0x1384ff8
   > github.com/soheilhy/cmux.muxListener.Accept(...)
   > 	/go/pkg/mod/github.com/soheilhy/cmux@v0.1.4/cmux.go:229
   > github.com/soheilhy/cmux.(*muxListener).Accept(0x3ff0f40?)
   > 	<autogenerated>:1 +0x45 fp=0xc0107b9d98 sp=0xc0107b9d68 pc=0x2dc7625
   > google.golang.org/grpc.(*Server).Serve(0xc00045b1e0, {0x400cb50, 0xc010690780})
   > 	/go/pkg/mod/google.golang.org/grpc@v1.29.1/server.go:621 +0x362 fp=0xc0107b9eb0 sp=0xc0107b9d98 pc=0x19749a2
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer.func1()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:457 +0x3e fp=0xc0107b9f90 sp=0xc0107b9eb0 pc=0x31db01e
   > github.com/pingcap/tidb/util.WithRecovery(0x400d640?, 0xc0101b8de0?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc0107b9fc0 sp=0xc0107b9f90 pc=0x1ffabd3
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer.func5()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:456 +0x28 fp=0xc0107b9fe0 sp=0xc0107b9fc0 pc=0x31dafa8
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0107b9fe8 sp=0xc0107b9fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:456 +0x42c
   > goroutine 1146 [select]:
   > runtime.gopark(0xc0107f7e10?, 0x2?, 0x68?, 0xb2?, 0xc0107f7d8c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0107f7be0 sp=0xc0107f7bc0 pc=0x13bb516
   > runtime.selectgo(0xc0107f7e10, 0xc0107f7d88, 0x13cb293?, 0x0, 0x13cc174?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0107f7d20 sp=0xc0107f7be0 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc011c3b8c0, 0x1, {0x5f8a1a8, 0x0, 0x0})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:441 +0x4f4 fp=0xc0107f7f10 sp=0xc0107f7d20 pc=0x30626b4
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:335 +0xb3 fp=0xc0107f7f90 sp=0xc0107f7f10 pc=0x30613d3
   > github.com/pingcap/tidb/util.WithRecovery(0x23de786?, 0xc000bb3d40?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc0107f7fc0 sp=0xc0107f7f90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x2a fp=0xc0107f7fe0 sp=0xc0107f7fc0 pc=0x30612ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0107f7fe8 sp=0xc0107f7fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x1c9
   > goroutine 1266 [select]:
   > runtime.gopark(0xc000ee3778?, 0x2?, 0x2?, 0x0?, 0xc000ee36ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000ee3558 sp=0xc000ee3538 pc=0x13bb516
   > runtime.selectgo(0xc000ee3778, 0xc000ee36e8, 0x3aac226?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000ee3698 sp=0xc000ee3558 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc0105af540, {0x400d6b0?, 0xc01127c9f0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc000ee37b8 sp=0xc000ee3698 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc000ee37e0 sp=0xc000ee37b8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000ee37e8 sp=0xc000ee37e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 1144 [select]:
   > runtime.gopark(0xc010befe30?, 0x2?, 0x80?, 0x57?, 0xc010befe1c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010befca8 sp=0xc010befc88 pc=0x13bb516
   > runtime.selectgo(0xc010befe30, 0xc010befe18, 0xc011480e40?, 0x0, 0x2fef900?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010befde8 sp=0xc010befca8 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).wait4BuildSide(0xc011c3b8c0)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:242 +0x6f fp=0xc010befe60 sp=0xc010befde8 pc=0x30605ef
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchProbeSideChunks(0xc011c3b8c0, {0x400d6b0, 0xc01127c9f0})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:221 +0x233 fp=0xc010beff28 sp=0xc010befe60 pc=0x3060333
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:322 +0x8f fp=0xc010beff90 sp=0xc010beff28 pc=0x306156f
   > github.com/pingcap/tidb/util.WithRecovery(0x23de786?, 0xc000bb3e40?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc010beffc0 sp=0xc010beff90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func3()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:320 +0x2a fp=0xc010beffe0 sp=0xc010beffc0 pc=0x30614aa
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010beffe8 sp=0xc010beffe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:320 +0x14f
   > goroutine 1088 [select]:
   > runtime.gopark(0xc0121e9f78?, 0x2?, 0xa0?, 0x9d?, 0xc0121e9eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0121e9d58 sp=0xc0121e9d38 pc=0x13bb516
   > runtime.selectgo(0xc0121e9f78, 0xc0121e9ee8, 0xc000df1400?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0121e9e98 sp=0xc0121e9d58 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc0105af4c0, {0x400d6b0?, 0xc01127c9f0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc0121e9fb8 sp=0xc0121e9e98 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc0121e9fe0 sp=0xc0121e9fb8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0121e9fe8 sp=0xc0121e9fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 1143 [chan receive]:
   > runtime.gopark(0xc011a29630?, 0xc011e95f80?, 0x3?, 0x0?, 0xc000e2fcf8?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000e2fca8 sp=0xc000e2fc88 pc=0x13bb516
   > runtime.chanrecv(0xc011e95ec0, 0xc000e2fe08, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000e2fd38 sp=0xc000e2fca8 pc=0x13854bb
   > runtime.chanrecv2(0xc00fb967b0?, 0x4012e60?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc000e2fd60 sp=0xc000e2fd38 pc=0x1384ff8
   > github.com/pingcap/tidb/executor.(*HashJoinExec).buildHashTableForList(0xc011c3b8c0, 0x1?)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:762 +0x2d6 fp=0xc000e2fe78 sp=0xc000e2fd60 pc=0x3065af6
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable(0xc011c3b8c0, {0x400d6b0?, 0xc01127c9f0})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:726 +0x23f fp=0xc000e2ff28 sp=0xc000e2fe78 pc=0x30653ff
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Next.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:671 +0x8f fp=0xc000e2ff90 sp=0xc000e2ff28 pc=0x306504f
   > github.com/pingcap/tidb/util.WithRecovery(0x23de786?, 0xc000ef0f00?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc000e2ffc0 sp=0xc000e2ff90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Next.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:669 +0x2a fp=0xc000e2ffe0 sp=0xc000e2ffc0 pc=0x3064f8a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000e2ffe8 sp=0xc000e2ffe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).Next
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:669 +0x5b2
   > goroutine 1142 [chan receive]:
   > runtime.gopark(0x13c37d1?, 0xc000e2d9d0?, 0x0?, 0x38?, 0xc011b5be10?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000e2d9c0 sp=0xc000e2d9a0 pc=0x13bb516
   > runtime.chanrecv(0xc011e95e60, 0xc000e2db10, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000e2da50 sp=0xc000e2d9c0 pc=0x13854bb
   > runtime.chanrecv2(0xc011c3b8c0?, 0x400d6b0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc000e2da78 sp=0xc000e2da50 pc=0x1384ff8
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Next(0xc011c3b8c0, {0x400d6b0?, 0xc01127c9f0?}, 0xc012047090)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:681 +0x652 fp=0xc000e2db38 sp=0xc000e2da78 pc=0x3064d52
   > github.com/pingcap/tidb/executor.Next({0x400d6b0, 0xc01127c9f0}, {0x40101a0, 0xc011c3b8c0}, 0xc012047090)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:286 +0x4a8 fp=0xc000e2dc78 sp=0xc000e2db38 pc=0x2fef688
   > github.com/pingcap/tidb/executor.(*ProjectionExec).unParallelExecute(0xc011f098c0, {0x400d6b0?, 0xc01127c9f0?}, 0xc011e979a0)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:194 +0xb8 fp=0xc000e2dcc8 sp=0xc000e2dc78 pc=0x3098758
   > github.com/pingcap/tidb/executor.(*ProjectionExec).Next(0xc011f098c0, {0x400d6b0, 0xc01127c9f0}, 0xc011e989a0?)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:180 +0x5a fp=0xc000e2dd00 sp=0xc000e2dcc8 pc=0x309861a
   > github.com/pingcap/tidb/executor.Next({0x400d6b0, 0xc01127c9f0}, {0x4010760, 0xc011f098c0}, 0xc011e979a0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:286 +0x4a8 fp=0xc000e2de40 sp=0xc000e2dd00 pc=0x2fef688
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchBuildSideRows(0xc011c3bb00, {0x400d6b0, 0xc01127c9f0}, 0xc011e958c0, 0xc01106ff80)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:266 +0x1a5 fp=0xc000e2df10 sp=0xc000e2de40 pc=0x3060845
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:715 +0xab fp=0xc000e2df90 sp=0xc000e2df10 pc=0x306572b
   > github.com/pingcap/tidb/util.WithRecovery(0x23de786?, 0xc000ef0f00?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc000e2dfc0 sp=0xc000e2df90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:712 +0x2a fp=0xc000e2dfe0 sp=0xc000e2dfc0 pc=0x306558a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000e2dfe8 sp=0xc000e2dfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:712 +0x22d
   > goroutine 1158 [chan receive]:
   > runtime.gopark(0xc011a29630?, 0xc011e95980?, 0x3?, 0x0?, 0xc0107bccf8?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0107bcca8 sp=0xc0107bcc88 pc=0x13bb516
   > runtime.chanrecv(0xc011e958c0, 0xc0107bce08, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc0107bcd38 sp=0xc0107bcca8 pc=0x13854bb
   > runtime.chanrecv2(0xc00fb967b0?, 0x4012e60?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc0107bcd60 sp=0xc0107bcd38 pc=0x1384ff8
   > github.com/pingcap/tidb/executor.(*HashJoinExec).buildHashTableForList(0xc011c3bb00, 0x1?)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:762 +0x2d6 fp=0xc0107bce78 sp=0xc0107bcd60 pc=0x3065af6
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable(0xc011c3bb00, {0x400d6b0?, 0xc01127c9f0})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:726 +0x23f fp=0xc0107bcf28 sp=0xc0107bce78 pc=0x30653ff
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Next.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:671 +0x8f fp=0xc0107bcf90 sp=0xc0107bcf28 pc=0x306504f
   > github.com/pingcap/tidb/util.WithRecovery(0x0?, 0x0?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc0107bcfc0 sp=0xc0107bcf90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Next.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:669 +0x2a fp=0xc0107bcfe0 sp=0xc0107bcfc0 pc=0x3064f8a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0107bcfe8 sp=0xc0107bcfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).Next
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:669 +0x5b2
   > goroutine 1148 [select]:
   > runtime.gopark(0xc0107fb610?, 0x2?, 0x88?, 0xb2?, 0xc0107fb58c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0107fb3e0 sp=0xc0107fb3c0 pc=0x13bb516
   > runtime.selectgo(0xc0107fb610, 0xc0107fb588, 0xc00feeb148?, 0x0, 0x20?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0107fb520 sp=0xc0107fb3e0 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc011c3b8c0, 0x3, {0x5f8a1a8, 0x0, 0x0})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:441 +0x4f4 fp=0xc0107fb710 sp=0xc0107fb520 pc=0x30626b4
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:335 +0xb3 fp=0xc0107fb790 sp=0xc0107fb710 pc=0x30613d3
   > github.com/pingcap/tidb/util.WithRecovery(0x400d6b0?, 0xc0120020c0?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc0107fb7c0 sp=0xc0107fb790 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x2a fp=0xc0107fb7e0 sp=0xc0107fb7c0 pc=0x30612ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0107fb7e8 sp=0xc0107fb7e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x1c9
   > goroutine 1149 [select]:
   > runtime.gopark(0xc000ede610?, 0x2?, 0x98?, 0xb2?, 0xc000ede58c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000ede3e0 sp=0xc000ede3c0 pc=0x13bb516
   > runtime.selectgo(0xc000ede610, 0xc000ede588, 0xc00feeb100?, 0x0, 0x13cc174?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000ede520 sp=0xc000ede3e0 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc011c3b8c0, 0x4, {0x5f8a1a8, 0x0, 0x0})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:441 +0x4f4 fp=0xc000ede710 sp=0xc000ede520 pc=0x30626b4
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:335 +0xb3 fp=0xc000ede790 sp=0xc000ede710 pc=0x30613d3
   > github.com/pingcap/tidb/util.WithRecovery(0x400d6b0?, 0xc011f075f0?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc000ede7c0 sp=0xc000ede790 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x2a fp=0xc000ede7e0 sp=0xc000ede7c0 pc=0x30612ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000ede7e8 sp=0xc000ede7e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x1c9
   > goroutine 1150 [semacquire]:
   > runtime.gopark(0xc00fd3cfd0?, 0x26a5025?, 0x20?, 0x1?, 0x40424f0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fd3ce78 sp=0xc00fd3ce58 pc=0x13bb516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc011c3bab8, 0x0?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc00fd3cee0 sp=0xc00fd3ce78 pc=0x13cce5e
   > sync.runtime_Semacquire(0x0?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc00fd3cf10 sp=0xc00fd3cee0 pc=0x13e9f65
   > sync.(*WaitGroup).Wait(0xc0107140c0?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc00fd3cf38 sp=0xc00fd3cf10 pc=0x13fd1f2
   > github.com/pingcap/tidb/executor.(*HashJoinExec).waitJoinWorkersAndCloseResultChan(0xc011c3b8c0)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:395 +0x33 fp=0xc00fd3cf78 sp=0xc00fd3cf38 pc=0x3061fb3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).waitJoinWorkersAndCloseResultChan-fm()
   > 	<autogenerated>:1 +0x26 fp=0xc00fd3cf90 sp=0xc00fd3cf78 pc=0x31277c6
   > github.com/pingcap/tidb/util.WithRecovery(0x5f539a0?, 0xc00fd3cf18?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc00fd3cfc0 sp=0xc00fd3cf90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:338 +0x28 fp=0xc00fd3cfe0 sp=0xc00fd3cfc0 pc=0x3061288
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fd3cfe8 sp=0xc00fd3cfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:338 +0x3b8
   > goroutine 1219 [select]:
   > runtime.gopark(0xc010bf2f78?, 0x2?, 0xa0?, 0x2d?, 0xc010bf2eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010bf2d58 sp=0xc010bf2d38 pc=0x13bb516
   > runtime.selectgo(0xc010bf2f78, 0xc010bf2ee8, 0xc000df1400?, 0x0, 0x4020f40?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010bf2e98 sp=0xc010bf2d58 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc00fc76040, {0x400d6b0?, 0xc01127c9f0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc010bf2fb8 sp=0xc010bf2e98 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc010bf2fe0 sp=0xc010bf2fb8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010bf2fe8 sp=0xc010bf2fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 1220 [select]:
   > runtime.gopark(0xc000b1df78?, 0x2?, 0x78?, 0xdd?, 0xc000b1deec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000b1dd58 sp=0xc000b1dd38 pc=0x13bb516
   > runtime.selectgo(0xc000b1df78, 0xc000b1dee8, 0x3aac226?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000b1de98 sp=0xc000b1dd58 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc00fc76080, {0x400d6b0?, 0xc01127c9f0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc000b1dfb8 sp=0xc000b1de98 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc000b1dfe0 sp=0xc000b1dfb8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000b1dfe8 sp=0xc000b1dfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 1221 [select]:
   > runtime.gopark(0xc0122a9f78?, 0x2?, 0x0?, 0x0?, 0xc0122a9eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0122a9d58 sp=0xc0122a9d38 pc=0x13bb516
   > runtime.selectgo(0xc0122a9f78, 0xc0122a9ee8, 0x3aac226?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0122a9e98 sp=0xc0122a9d58 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc00fc760c0, {0x400d6b0?, 0xc01127c9f0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc0122a9fb8 sp=0xc0122a9e98 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc0122a9fe0 sp=0xc0122a9fb8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0122a9fe8 sp=0xc0122a9fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 1222 [select]:
   > runtime.gopark(0xc0122aa778?, 0x2?, 0x0?, 0x0?, 0xc0122aa6ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0122aa558 sp=0xc0122aa538 pc=0x13bb516
   > runtime.selectgo(0xc0122aa778, 0xc0122aa6e8, 0x3aac226?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0122aa698 sp=0xc0122aa558 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc00fc76100, {0x400d6b0?, 0xc01127c9f0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc0122aa7b8 sp=0xc0122aa698 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc0122aa7e0 sp=0xc0122aa7b8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0122aa7e8 sp=0xc0122aa7e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 1223 [select]:
   > runtime.gopark(0xc0122aaf78?, 0x2?, 0x0?, 0x0?, 0xc0122aaeec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0122aad58 sp=0xc0122aad38 pc=0x13bb516
   > runtime.selectgo(0xc0122aaf78, 0xc0122aaee8, 0x3aac226?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0122aae98 sp=0xc0122aad58 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc00fc76140, {0x400d6b0?, 0xc01127c9f0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc0122aafb8 sp=0xc0122aae98 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc0122aafe0 sp=0xc0122aafb8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0122aafe8 sp=0xc0122aafe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
