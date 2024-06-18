# Bug ID TIDB-30326-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/30326
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED


## Details
 * Database: tidb-5.2.1
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
   > [2024/06/18 11:58:51.231 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=26] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:51.232 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=26] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:51.234 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:54, Type:create schema, State:none, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:51.233 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 11:58:51.234 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:54, Type:create schema, State:none, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:51.233 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/18 11:58:51.235 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:54, Type:create schema, State:none, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:51.233 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:51.236 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=26] [neededSchemaVersion=27] ["start time"=148.554µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 11:58:51.238 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=27] ["take time"=2.451175ms] [job="ID:54, Type:create schema, State:done, SchemaState:public, SchemaID:53, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:51.233 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:51.239 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:54, Type:create schema, State:synced, SchemaState:public, SchemaID:53, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:51.233 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:51.239 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=54]
   > [2024/06/18 11:58:51.240 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/18 11:58:51.448 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=27] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_037irb`\n--\n\nDROP TABLE IF EXISTS `t_037irb`;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:51.449 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=27] [cur_db=testdb] [sql="CREATE TABLE `t_037irb` (\n  `c_nrh3o` int(11) DEFAULT NULL,\n  `c_nfauxb` text DEFAULT NULL,\n  `c_y5n4c` int(11) DEFAULT NULL,\n  `c_j9alg` double NOT NULL,\n  `c_4vix1d` text DEFAULT NULL,\n  `c_glkxdb` text DEFAULT NULL,\n  `c_2ykt0d` int(11) DEFAULT NULL,\n  `c_5fxv3c` double DEFAULT NULL,\n  PRIMARY KEY (`c_j9alg`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:51.451 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:56, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:55, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:51.45 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 11:58:51.451 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:56, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:55, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:51.45 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_037irb` (\n  `c_nrh3o` int(11) DEFAULT NULL,\n  `c_nfauxb` text DEFAULT NULL,\n  `c_y5n4c` int(11) DEFAULT NULL,\n  `c_j9alg` double NOT NULL,\n  `c_4vix1d` text DEFAULT NULL,\n  `c_glkxdb` text DEFAULT NULL,\n  `c_2ykt0d` int(11) DEFAULT NULL,\n  `c_5fxv3c` double DEFAULT NULL,\n  PRIMARY KEY (`c_j9alg`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/18 11:58:51.452 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:56, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:55, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:51.45 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:51.454 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=27] [neededSchemaVersion=28] ["start time"=478.557µs] [phyTblIDs="[55]"] [actionTypes="[8]"]
   > [2024/06/18 11:58:51.456 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=28] ["take time"=2.025209ms] [job="ID:56, Type:create table, State:done, SchemaState:public, SchemaID:53, TableID:55, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:51.45 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:51.457 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:56, Type:create table, State:synced, SchemaState:public, SchemaID:53, TableID:55, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:51.45 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:51.458 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=56]
   > [2024/06/18 11:58:51.458 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/18 11:58:51.458 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=50] ["first split key"=748000000000000037]
   > [2024/06/18 11:58:51.459 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=50] ["first at"=748000000000000037] ["first new region left"="{Id:50 StartKey:7480000000000000ff3300000000000000f8 EndKey:7480000000000000ff3700000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:51 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/18 11:58:51.459 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[50]"]
   > [2024/06/18 11:58:51.459 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=28] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_037irb` DISABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:51.460 +00:00] [WARN] [2pc.go:1598] ["schemaLeaseChecker is not set for this transaction"] [sessionID=5] [startTS=450550020560650241] [commitTS=450550020560650242]
   > [2024/06/18 11:58:51.462 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=28] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_037irb` ENABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:51.463 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=28] [cur_db=testdb] [sql="\n--\n-- Temporary view structure for view `t_cpsvpb`\n--\n\nDROP TABLE IF EXISTS `t_cpsvpb`;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:51.463 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=28] [cur_db=testdb] [sql="/*!50001 DROP VIEW IF EXISTS `t_cpsvpb`*/;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:51.466 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:58, Type:create view, State:none, SchemaState:queueing, SchemaID:53, TableID:57, RowCount:0, ArgLen:3, start time: 2024-06-18 11:58:51.465 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 11:58:51.466 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:58, Type:create view, State:none, SchemaState:queueing, SchemaID:53, TableID:57, RowCount:0, ArgLen:3, start time: 2024-06-18 11:58:51.465 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="/*!50001 CREATE VIEW `t_cpsvpb` AS SELECT \n 1 AS `c0`,\n 1 AS `c2`,\n 1 AS `c3`,\n 1 AS `c4`,\n 1 AS `c5`,\n 1 AS `c6`,\n 1 AS `c7`,\n 1 AS `c8`,\n 1 AS `c9`,\n 1 AS `c10`,\n 1 AS `c11`,\n 1 AS `c12`,\n 1 AS `c13`,\n 1 AS `c14`*/;"]
   > [2024/06/18 11:58:51.467 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:58, Type:create view, State:none, SchemaState:queueing, SchemaID:53, TableID:57, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:51.465 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:51.470 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=28] [neededSchemaVersion=29] ["start time"=656.376µs] [phyTblIDs="[57]"] [actionTypes="[2097152]"]
   > [2024/06/18 11:58:51.472 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=29] ["take time"=2.244373ms] [job="ID:58, Type:create view, State:done, SchemaState:public, SchemaID:53, TableID:57, RowCount:0, ArgLen:3, start time: 2024-06-18 11:58:51.465 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:51.473 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:58, Type:create view, State:synced, SchemaState:public, SchemaID:53, TableID:57, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:51.465 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:51.475 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=58]
   > [2024/06/18 11:58:51.475 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/18 11:58:51.476 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=29] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_x7zqmd`\n--\n\nDROP TABLE IF EXISTS `t_x7zqmd`;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:51.477 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=29] [cur_db=testdb] [sql="CREATE TABLE `t_x7zqmd` (\n  `c_8weeq` int(11) NOT NULL,\n  `c_13sfid` double DEFAULT NULL,\n  `c_hhjlmc` text DEFAULT NULL,\n  `c_3b1zld` int(11) DEFAULT NULL,\n  `c_6tu8wd` int(11) DEFAULT NULL,\n  `c_jyc_cd` double DEFAULT NULL,\n  PRIMARY KEY (`c_8weeq`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:51.478 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:60, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:59, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:51.477 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 11:58:51.478 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:60, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:59, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:51.477 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_x7zqmd` (\n  `c_8weeq` int(11) NOT NULL,\n  `c_13sfid` double DEFAULT NULL,\n  `c_hhjlmc` text DEFAULT NULL,\n  `c_3b1zld` int(11) DEFAULT NULL,\n  `c_6tu8wd` int(11) DEFAULT NULL,\n  `c_jyc_cd` double DEFAULT NULL,\n  PRIMARY KEY (`c_8weeq`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/18 11:58:51.479 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:60, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:59, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:51.477 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:51.481 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=29] [neededSchemaVersion=30] ["start time"=386.925µs] [phyTblIDs="[59]"] [actionTypes="[8]"]
   > [2024/06/18 11:58:51.483 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=30] ["take time"=2.036243ms] [job="ID:60, Type:create table, State:done, SchemaState:public, SchemaID:53, TableID:59, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:51.477 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:51.484 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:60, Type:create table, State:synced, SchemaState:public, SchemaID:53, TableID:59, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:51.477 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:51.485 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=60]
   > [2024/06/18 11:58:51.485 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/18 11:58:51.485 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=52] ["first split key"=74800000000000003b]
   > [2024/06/18 11:58:51.486 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=52] ["first at"=74800000000000003b] ["first new region left"="{Id:52 StartKey:7480000000000000ff3700000000000000f8 EndKey:7480000000000000ff3b00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:53 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/18 11:58:51.486 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[52]"]
   > [2024/06/18 11:58:51.486 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=30] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_x7zqmd` DISABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:51.490 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=30] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_x7zqmd` ENABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:51.491 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=30] [cur_db=testdb] [sql="\n--\n-- Final view structure for view `t_cpsvpb`\n--\n\n/*!50001 DROP VIEW IF EXISTS `t_cpsvpb`*/;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:51.492 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:61, Type:drop view, State:none, SchemaState:queueing, SchemaID:53, TableID:57, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:51.491 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 11:58:51.492 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:61, Type:drop view, State:none, SchemaState:queueing, SchemaID:53, TableID:57, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:51.491 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="\n--\n-- Final view structure for view `t_cpsvpb`\n--\n\n/*!50001 DROP VIEW IF EXISTS `t_cpsvpb`*/;"]
   > [2024/06/18 11:58:51.493 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:61, Type:drop view, State:none, SchemaState:queueing, SchemaID:53, TableID:57, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:51.491 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:51.495 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=30] [neededSchemaVersion=31] ["start time"=139.474µs] [phyTblIDs="[57]"] [actionTypes="[16777216]"]
   > [2024/06/18 11:58:51.497 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=31] ["take time"=2.271611ms] [job="ID:61, Type:drop view, State:running, SchemaState:write only, SchemaID:53, TableID:57, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:51.491 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:51.497 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:61, Type:drop view, State:running, SchemaState:write only, SchemaID:53, TableID:57, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:51.491 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:51.499 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=31] [neededSchemaVersion=32] ["start time"=112.934µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 11:58:51.501 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=32] ["take time"=2.16175ms] [job="ID:61, Type:drop view, State:running, SchemaState:delete only, SchemaID:53, TableID:57, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:51.491 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:51.502 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:61, Type:drop view, State:running, SchemaState:delete only, SchemaID:53, TableID:57, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:51.491 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:51.504 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=32] [neededSchemaVersion=33] ["start time"=139.893µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 11:58:51.506 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=33] ["take time"=2.186683ms] [job="ID:61, Type:drop view, State:done, SchemaState:queueing, SchemaID:53, TableID:57, RowCount:0, ArgLen:2, start time: 2024-06-18 11:58:51.491 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:51.507 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:61, Type:drop view, State:synced, SchemaState:queueing, SchemaID:53, TableID:57, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:51.491 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:51.509 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=61]
   > [2024/06/18 11:58:51.509 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/18 11:58:51.514 +00:00] [INFO] [session.go:2203] ["Try to create a new txn inside a transaction auto commit"] [conn=5] [schemaVersion=33] [txnStartTS=450550020574019584] [txnScope=global]
   > [2024/06/18 11:58:51.517 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:63, Type:create view, State:none, SchemaState:queueing, SchemaID:53, TableID:62, RowCount:0, ArgLen:3, start time: 2024-06-18 11:58:51.515 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 11:58:51.517 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:63, Type:create view, State:none, SchemaState:queueing, SchemaID:53, TableID:62, RowCount:0, ArgLen:3, start time: 2024-06-18 11:58:51.515 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="/*!50001 CREATE ALGORITHM=UNDEFINED */\n/*!50013 DEFINER=`root`@`127.0.0.1` SQL SECURITY DEFINER */\n/*!50001 VIEW `t_cpsvpb` (`c0`, `c2`, `c3`, `c4`, `c5`, `c6`, `c7`, `c8`, `c9`, `c10`, `c11`, `c12`, `c13`, `c14`) AS SELECT DISTINCT `subq_0`.`c1` AS `c0`,`subq_0`.`c2` AS `c2`,8 AS `c3`,CASE WHEN (`subq_0`.`c3` NOT IN (SELECT `ref_2`.`c_4vix1d` AS `c0` FROM `testdb`.`t_037irb` AS `ref_2` WHERE `ref_2`.`c_2ykt0d`<=`ref_2`.`c_nrh3o`)) AND (`subq_0`.`c3`<=(SELECT (SELECT `c_hhjlmc` AS `c_hhjlmc` FROM `testdb`.`t_x7zqmd` ORDER BY `c_hhjlmc` LIMIT 4,1) AS `c0` FROM `testdb`.`t_037irb` AS `ref_3` WHERE `subq_0`.`c1`!=`ref_3`.`c_2ykt0d`)) THEN `subq_0`.`c3` ELSE `subq_0`.`c3` END AS `c4`,CASE WHEN `subq_0`.`c1`>=(SELECT MAX(`c_8weeq`) AS `max(c_8weeq)` FROM `testdb`.`t_x7zqmd`) THEN `subq_0`.`c2` ELSE `subq_0`.`c2` END AS `c5`,`subq_0`.`c1` AS `c6`,`subq_0`.`c2` AS `c7`,`subq_0`.`c3` AS `c8`,`subq_0`.`c3` AS `c9`,`subq_0`.`c2` AS `c10`,`subq_0`.`c4` AS `c11`,COUNT(CAST(`subq_0`.`c2` AS DOUBLE)) OVER (PARTITION BY `subq_0`.`c4` ORDER BY `subq_0`.`c1`) AS `c12`,`subq_0`.`c3` AS `c13`,CAST(COALESCE(`subq_0`.`c3`, _UTF8MB4'9sx3k') AS CHAR) AS `c14` FROM (SELECT COUNT(CAST(`ref_1`.`c_jyc_cd` AS DOUBLE)) AS `c0`,AVG(CAST(`ref_1`.`c_3b1zld` AS SIGNED)) AS `c1`,MIN(CAST(`ref_1`.`c_jyc_cd` AS DOUBLE)) AS `c2`,`ref_0`.`c_glkxdb` AS `c3`,COUNT(CAST(`ref_1`.`c_13sfid` AS DOUBLE)) AS `c4` FROM `testdb`.`t_037irb` AS `ref_0` JOIN `testdb`.`t_x7zqmd` AS `ref_1` WHERE `ref_0`.`c_nrh3o`>`ref_1`.`c_8weeq` GROUP BY `ref_0`.`c_glkxdb`) AS `subq_0` WHERE (SELECT `c_8weeq` AS `c_8weeq` FROM `testdb`.`t_x7zqmd` ORDER BY `c_8weeq` LIMIT 2,1) IS NOT NULL */;"]
   > [2024/06/18 11:58:51.518 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:63, Type:create view, State:none, SchemaState:queueing, SchemaID:53, TableID:62, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:51.515 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:51.522 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=33] [neededSchemaVersion=34] ["start time"=735.157µs] [phyTblIDs="[62]"] [actionTypes="[2097152]"]
   > [2024/06/18 11:58:51.523 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=34] ["take time"=2.287465ms] [job="ID:63, Type:create view, State:done, SchemaState:public, SchemaID:53, TableID:62, RowCount:0, ArgLen:3, start time: 2024-06-18 11:58:51.515 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:51.525 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:63, Type:create view, State:synced, SchemaState:public, SchemaID:53, TableID:62, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:51.515 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:51.527 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=63]
   > [2024/06/18 11:58:51.527 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/18 11:58:52.562 +00:00] [INFO] [set.go:127] ["set global var"] [conn=7] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/06/18 11:58:52.862 +00:00] [ERROR] [misc.go:94] ["panic in the recoverable goroutine"] [r="\"invalid memory address or nil pointer dereference\""] ["stack trace"="github.com/pingcap/tidb/util.WithRecovery.func1\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:96\nruntime.gopanic\n\t/usr/local/go/src/runtime/panic.go:965\nruntime.panicmem\n\t/usr/local/go/src/runtime/panic.go:212\nruntime.sigpanic\n\t/usr/local/go/src/runtime/signal_unix.go:734\ngithub.com/pingcap/tidb/util/chunk.(*Chunk).NumRows\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/chunk/chunk.go:349\ngithub.com/pingcap/tidb/executor.(*vecGroupChecker).splitIntoGroups\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/aggregate.go:1456\ngithub.com/pingcap/tidb/executor.(*PipelinedWindowExec).getRowsInPartition\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/pipelined_window.go:188\ngithub.com/pingcap/tidb/executor.(*PipelinedWindowExec).Next\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/pipelined_window.go:124\ngithub.com/pingcap/tidb/executor.Next\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/executor.go:285\ngithub.com/pingcap/tidb/executor.(*ProjectionExec).unParallelExecute\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:193\ngithub.com/pingcap/tidb/executor.(*ProjectionExec).Next\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:179\ngithub.com/pingcap/tidb/executor.Next\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/executor.go:285\ngithub.com/pingcap/tidb/executor.(*CTEExec).computeSeedPart\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/cte.go:225\ngithub.com/pingcap/tidb/executor.(*CTEExec).Next\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/cte.go:160\ngithub.com/pingcap/tidb/executor.Next\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/executor.go:285\ngithub.com/pingcap/tidb/executor.(*HashJoinExec).fetchBuildSideRows\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:268\ngithub.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable.func2\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:702\ngithub.com/pingcap/tidb/util.WithRecovery\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99"]
   > [2024/06/18 11:58:54.782 +00:00] [WARN] [coprocessor.go:192] ["buildCopTasks takes too much time"] [elapsed=746.379842ms] ["range len"=1] ["task len"=1]
   > runtime: goroutine stack exceeds 1000000000-byte limit
   > runtime: sp=0xc0321e0398 stack=[0xc0321e0000, 0xc0521e0000]
   > fatal error: stack overflow
   > runtime stack:
   > runtime.throw(0x3b1a561, 0xe)
   > 	/usr/local/go/src/runtime/panic.go:1117 +0x72
   > runtime.newstack()
   > 	/usr/local/go/src/runtime/stack.go:1069 +0x7ed
   > runtime.morestack()
   > 	/usr/local/go/src/runtime/asm_amd64.s:458 +0x8f
   > goroutine 986 [running]:
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc00046e020, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:182 +0x16f fp=0xc0321e03a8 sp=0xc0321e03a0 pc=0x1ee3a8f
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011b5fd50, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e03f0 sp=0xc0321e03a8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011d8e3f0, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e0438 sp=0xc0321e03f0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011d7ed70, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e0480 sp=0xc0321e0438 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011064e40, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e04c8 sp=0xc0321e0480 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011042280, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e0510 sp=0xc0321e04c8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0110647e0, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e0558 sp=0xc0321e0510 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011064780, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e05a0 sp=0xc0321e0558 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011076720, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e05e8 sp=0xc0321e05a0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc00106f2c0, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e0630 sp=0xc0321e05e8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc01165a020, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e0678 sp=0xc0321e0630 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc00046e020, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e06c0 sp=0xc0321e0678 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011b5fd50, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e0708 sp=0xc0321e06c0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011d8e3f0, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e0750 sp=0xc0321e0708 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011d7ed70, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e0798 sp=0xc0321e0750 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011064e40, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e07e0 sp=0xc0321e0798 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011042280, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e0828 sp=0xc0321e07e0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0110647e0, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e0870 sp=0xc0321e0828 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011064780, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e08b8 sp=0xc0321e0870 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011076720, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e0900 sp=0xc0321e08b8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc00106f2c0, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e0948 sp=0xc0321e0900 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc01165a020, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e0990 sp=0xc0321e0948 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc00046e020, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e09d8 sp=0xc0321e0990 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011b5fd50, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e0a20 sp=0xc0321e09d8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011d8e3f0, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e0a68 sp=0xc0321e0a20 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011d7ed70, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e0ab0 sp=0xc0321e0a68 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011064e40, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e0af8 sp=0xc0321e0ab0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011042280, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e0b40 sp=0xc0321e0af8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0110647e0, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e0b88 sp=0xc0321e0b40 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011064780, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e0bd0 sp=0xc0321e0b88 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011076720, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e0c18 sp=0xc0321e0bd0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc00106f2c0, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e0c60 sp=0xc0321e0c18 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc01165a020, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e0ca8 sp=0xc0321e0c60 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc00046e020, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e0cf0 sp=0xc0321e0ca8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011b5fd50, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e0d38 sp=0xc0321e0cf0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011d8e3f0, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e0d80 sp=0xc0321e0d38 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011d7ed70, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e0dc8 sp=0xc0321e0d80 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011064e40, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e0e10 sp=0xc0321e0dc8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011042280, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e0e58 sp=0xc0321e0e10 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0110647e0, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e0ea0 sp=0xc0321e0e58 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011064780, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e0ee8 sp=0xc0321e0ea0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011076720, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e0f30 sp=0xc0321e0ee8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc00106f2c0, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e0f78 sp=0xc0321e0f30 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc01165a020, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e0fc0 sp=0xc0321e0f78 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc00046e020, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1008 sp=0xc0321e0fc0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011b5fd50, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1050 sp=0xc0321e1008 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011d8e3f0, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1098 sp=0xc0321e1050 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011d7ed70, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e10e0 sp=0xc0321e1098 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011064e40, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1128 sp=0xc0321e10e0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011042280, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1170 sp=0xc0321e1128 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0110647e0, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e11b8 sp=0xc0321e1170 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011064780, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1200 sp=0xc0321e11b8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011076720, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1248 sp=0xc0321e1200 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc00106f2c0, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1290 sp=0xc0321e1248 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc01165a020, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e12d8 sp=0xc0321e1290 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc00046e020, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1320 sp=0xc0321e12d8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011b5fd50, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1368 sp=0xc0321e1320 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011d8e3f0, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e13b0 sp=0xc0321e1368 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011d7ed70, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e13f8 sp=0xc0321e13b0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011064e40, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1440 sp=0xc0321e13f8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011042280, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1488 sp=0xc0321e1440 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0110647e0, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e14d0 sp=0xc0321e1488 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011064780, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1518 sp=0xc0321e14d0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011076720, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1560 sp=0xc0321e1518 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc00106f2c0, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e15a8 sp=0xc0321e1560 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc01165a020, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e15f0 sp=0xc0321e15a8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc00046e020, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1638 sp=0xc0321e15f0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011b5fd50, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1680 sp=0xc0321e1638 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011d8e3f0, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e16c8 sp=0xc0321e1680 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011d7ed70, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1710 sp=0xc0321e16c8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011064e40, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1758 sp=0xc0321e1710 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011042280, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e17a0 sp=0xc0321e1758 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0110647e0, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e17e8 sp=0xc0321e17a0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011064780, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1830 sp=0xc0321e17e8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011076720, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1878 sp=0xc0321e1830 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc00106f2c0, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e18c0 sp=0xc0321e1878 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc01165a020, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1908 sp=0xc0321e18c0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc00046e020, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1950 sp=0xc0321e1908 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011b5fd50, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1998 sp=0xc0321e1950 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011d8e3f0, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e19e0 sp=0xc0321e1998 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011d7ed70, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1a28 sp=0xc0321e19e0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011064e40, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1a70 sp=0xc0321e1a28 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011042280, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1ab8 sp=0xc0321e1a70 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0110647e0, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1b00 sp=0xc0321e1ab8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011064780, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1b48 sp=0xc0321e1b00 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011076720, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1b90 sp=0xc0321e1b48 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc00106f2c0, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1bd8 sp=0xc0321e1b90 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc01165a020, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1c20 sp=0xc0321e1bd8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc00046e020, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1c68 sp=0xc0321e1c20 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011b5fd50, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1cb0 sp=0xc0321e1c68 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011d8e3f0, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1cf8 sp=0xc0321e1cb0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011d7ed70, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1d40 sp=0xc0321e1cf8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011064e40, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1d88 sp=0xc0321e1d40 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011042280, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1dd0 sp=0xc0321e1d88 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0110647e0, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1e18 sp=0xc0321e1dd0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011064780, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1e60 sp=0xc0321e1e18 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011076720, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1ea8 sp=0xc0321e1e60 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc00106f2c0, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1ef0 sp=0xc0321e1ea8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc01165a020, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1f38 sp=0xc0321e1ef0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc00046e020, 0x40385b8, 0xc0110647e0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0321e1f80 sp=0xc0321e1f38 pc=0x1ee3a1c
   > ...additional frames elided...
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:699 +0x198
   > goroutine 1 [chan receive]:
   > github.com/pingcap/tidb/server.(*Server).Run(0xc010f232b0, 0xc0114e54a0, 0xc01067fe00)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/server.go:338 +0x1c5
   > main.main()
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/tidb-server/main.go:200 +0x33d
   > goroutine 15 [select]:
   > go.opencensus.io/stats/view.(*worker).start(0xc00015d980)
   > 	/nfs/cache/mod/go.opencensus.io@v0.22.5/stats/view/worker.go:276 +0xcd
   > created by go.opencensus.io/stats/view.init.0
   > 	/nfs/cache/mod/go.opencensus.io@v0.22.5/stats/view/worker.go:34 +0x68
   > goroutine 171 [chan receive]:
   > go.etcd.io/etcd/pkg/logutil.(*MergeLogger).outputLoop(0xc000908588)
   > 	/nfs/cache/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20200824191128-ae9734ed278b/pkg/logutil/merge_logger.go:173 +0x3ac
   > created by go.etcd.io/etcd/pkg/logutil.NewMergeLogger
   > 	/nfs/cache/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20200824191128-ae9734ed278b/pkg/logutil/merge_logger.go:91 +0x85
   > goroutine 240 [chan receive]:
   > go.etcd.io/etcd/pkg/logutil.(*MergeLogger).outputLoop(0xc0009093b0)
   > 	/nfs/cache/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20200824191128-ae9734ed278b/pkg/logutil/merge_logger.go:173 +0x3ac
   > created by go.etcd.io/etcd/pkg/logutil.NewMergeLogger
   > 	/nfs/cache/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20200824191128-ae9734ed278b/pkg/logutil/merge_logger.go:91 +0x85
   > goroutine 197 [chan receive]:
   > go.etcd.io/etcd/pkg/logutil.(*MergeLogger).outputLoop(0xc0005065e8)
   > 	/nfs/cache/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20200824191128-ae9734ed278b/pkg/logutil/merge_logger.go:173 +0x3ac
   > created by go.etcd.io/etcd/pkg/logutil.NewMergeLogger
   > 	/nfs/cache/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20200824191128-ae9734ed278b/pkg/logutil/merge_logger.go:91 +0x85
   > goroutine 491 [chan receive]:
   > github.com/pingcap/tidb/util/profile.HeapProfileForGlobalMemTracker(0xdf8475800)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/profile/trackerRecorder.go:32 +0xbf
   > created by main.setHeapProfileTracker
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/tidb-server/main.go:266 +0x8d
   > goroutine 492 [chan receive]:
   > github.com/pingcap/tidb/util/systimemon.StartMonitor(0x3c23558, 0x3c228d0, 0xc000a0c5f0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/systimemon/systime_mon.go:31 +0x148
   > created by main.setupMetrics
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/tidb-server/main.go:652 +0x105
   > goroutine 493 [select]:
   > github.com/pingcap/badger.(*DB).updateSize(0xc000aa3200, 0xc000c0bab8)
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/db.go:1032 +0x108
   > created by github.com/pingcap/badger.Open
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/db.go:327 +0xe14
   > goroutine 494 [select]:
   > github.com/pingcap/badger/epoch.(*ResourceManager).collectLoop(0xc000a0f1a0, 0xc000c0bad0)
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/epoch/manager.go:101 +0xdc
   > created by github.com/pingcap/badger/epoch.NewResourceManager
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/epoch/manager.go:79 +0xa7
   > goroutine 495 [select]:
   > github.com/pingcap/badger.Open.func4(0xc000692b68)
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/db.go:341 +0x17c
   > created by github.com/pingcap/badger.Open
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/db.go:338 +0x10a8
   > goroutine 99 [select]:
   > github.com/pingcap/badger.(*blobGCHandler).run(0xc00053b940, 0xc0004e68e8)
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/blob.go:468 +0xd4
   > created by github.com/pingcap/badger.(*blobManager).Open
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/blob.go:292 +0x618
   > goroutine 100 [select]:
   > github.com/pingcap/badger.(*levelsController).runWorker(0xc0006f22a0, 0xc0004e6900, 0x0)
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/levels.go:212 +0x185
   > created by github.com/pingcap/badger.(*levelsController).startCompact
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/levels.go:180 +0x93
   > goroutine 101 [select]:
   > github.com/pingcap/badger.(*levelsController).runWorker(0xc0006f22a0, 0xc0004e6900, 0x0)
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/levels.go:212 +0x185
   > created by github.com/pingcap/badger.(*levelsController).startCompact
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/levels.go:180 +0x93
   > goroutine 102 [select]:
   > github.com/pingcap/badger.(*levelsController).runWorker(0xc0006f22a0, 0xc0004e6900, 0x1)
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/levels.go:212 +0x185
   > created by github.com/pingcap/badger.(*levelsController).startCompact
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/levels.go:180 +0x93
   > goroutine 103 [chan receive]:
   > github.com/pingcap/badger.(*DB).runFlushMemTable(0xc000aa3200, 0xc000a0a0a8, 0x0, 0x0)
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/db.go:913 +0x190
   > created by github.com/pingcap/badger.Open
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/db.go:360 +0x17b0
   > goroutine 345 [chan receive]:
   > github.com/pingcap/badger.(*writeWorker).runMergeLSM(0xc0006e44c0, 0xc000506078)
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/writer.go:154 +0xad
   > created by github.com/pingcap/badger.startWriteWorker
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/writer.go:66 +0x1e8
   > goroutine 344 [chan receive, locked to thread]:
   > github.com/pingcap/badger.(*writeWorker).runWriteLSM(0xc0006e44c0, 0xc000506078)
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/writer.go:141 +0x195
   > created by github.com/pingcap/badger.startWriteWorker
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/writer.go:65 +0x1bc
   > goroutine 343 [select]:
   > github.com/pingcap/badger.(*writeWorker).runWriteVLog(0xc0006e44c0, 0xc000506078)
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/writer.go:94 +0x1dc
   > created by github.com/pingcap/badger.startWriteWorker
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/writer.go:64 +0x190
   > goroutine 346 [select]:
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.writeDBWorker.run(0xc00003a360, 0xc000f8a1c0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:95 +0x205
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*dbWriter).Open
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:198 +0x8f
   > goroutine 347 [select]:
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.writeLockWorker.run(0xc00003a3c0, 0xc000f8a1c0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:147 +0x3e5
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*dbWriter).Open
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:205 +0xdc
   > goroutine 348 [select]:
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*MVCCStore).runUpdateSafePointLoop(0xc0006e8080)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:1549 +0x28a
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.NewMVCCStore
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:84 +0x269
   > goroutine 349 [select]:
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*MVCCStore).StartDeadlockDetection.func1(0xc0006e8080)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:1285 +0x8a
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*MVCCStore).StartDeadlockDetection
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:1283 +0x78
   > goroutine 350 [select]:
   > github.com/tikv/client-go/v2/oracle/oracles.(*pdOracle).updateTS(0xc000f89490, 0x4030f20, 0xc000052058, 0x77359400)
   > 	/nfs/cache/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20210820060448-daddf73a0706/oracle/oracles/pd.go:227 +0x131
   > created by github.com/tikv/client-go/v2/oracle/oracles.NewPdOracle
   > 	/nfs/cache/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20210820060448-daddf73a0706/oracle/oracles/pd.go:75 +0xd3
   > goroutine 351 [select]:
   > github.com/tikv/client-go/v2/internal/locate.(*RegionCache).asyncCheckAndResolveLoop(0xc0006e8180, 0xdf8475800)
   > 	/nfs/cache/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20210820060448-daddf73a0706/internal/locate/region_cache.go:395 +0xdc
   > created by github.com/tikv/client-go/v2/internal/locate.NewRegionCache
   > 	/nfs/cache/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20210820060448-daddf73a0706/internal/locate/region_cache.go:366 +0x259
   > goroutine 352 [select]:
   > github.com/tikv/client-go/v2/tikv.(*KVStore).runSafePointChecker(0xc00052e120)
   > 	/nfs/cache/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20210820060448-daddf73a0706/tikv/kv.go:262 +0x136
   > created by github.com/tikv/client-go/v2/tikv.NewKVStore
   > 	/nfs/cache/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20210820060448-daddf73a0706/tikv/kv.go:185 +0x407
   > goroutine 353 [select]:
   > github.com/tikv/client-go/v2/tikv.(*KVStore).safeTSUpdater(0xc00052e120)
   > 	/nfs/cache/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20210820060448-daddf73a0706/tikv/kv.go:540 +0x194
   > created by github.com/tikv/client-go/v2/tikv.NewKVStore
   > 	/nfs/cache/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20210820060448-daddf73a0706/tikv/kv.go:186 +0x429
   > goroutine 498 [select]:
   > github.com/dgraph-io/ristretto.(*defaultPolicy).processItems(0xc000438f90)
   > 	/nfs/cache/mod/github.com/dgraph-io/ristretto@v0.0.1/policy.go:96 +0xa5
   > created by github.com/dgraph-io/ristretto.newDefaultPolicy
   > 	/nfs/cache/mod/github.com/dgraph-io/ristretto@v0.0.1/policy.go:80 +0x129
   > goroutine 499 [select]:
   > github.com/dgraph-io/ristretto.(*Cache).processItems(0xc00003a7e0)
   > 	/nfs/cache/mod/github.com/dgraph-io/ristretto@v0.0.1/cache.go:257 +0x9d
   > created by github.com/dgraph-io/ristretto.NewCache
   > 	/nfs/cache/mod/github.com/dgraph-io/ristretto@v0.0.1/cache.go:155 +0x205
   > goroutine 852 [select]:
   > github.com/pingcap/tidb/domain.(*Domain).autoAnalyzeWorker(0xc010a9e900, 0x404ecf8, 0xc010f7e820)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:1347 +0x165
   > created by github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:1184 +0x245
   > goroutine 756 [select]:
   > github.com/pingcap/tidb/ddl.(*worker).start(0xc010a8ea50, 0xc010a8a9c0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/ddl/ddl_worker.go:177 +0x315
   > created by github.com/pingcap/tidb/ddl.(*ddl).Start
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/ddl/ddl.go:364 +0x6a5
   > goroutine 754 [select]:
   > github.com/pingcap/tidb/ddl.(*ddl).limitDDLJobs(0xc010ae28c0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/ddl/ddl_worker.go:265 +0x2d9
   > created by github.com/pingcap/tidb/ddl.(*ddl).Start
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/ddl/ddl.go:346 +0x2d5
   > goroutine 785 [sleep]:
   > time.Sleep(0x3b9aca00)
   > 	/usr/local/go/src/runtime/time.go:193 +0xd2
   > github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).startCPUProfileWorker(0xc0003d5860)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:114 +0xb4
   > created by github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).Run
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:92 +0xb7
   > goroutine 849 [select]:
   > github.com/pingcap/tidb/domain.(*Domain).TelemetryRotateSubWindowLoop.func1(0xc010a9e900)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:1113 +0xd8
   > created by github.com/pingcap/tidb/domain.(*Domain).TelemetryRotateSubWindowLoop
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:1106 +0x7f
   > goroutine 757 [select]:
   > github.com/pingcap/tidb/ddl.(*worker).start(0xc010a8eb00, 0xc010a8a9c0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/ddl/ddl_worker.go:177 +0x315
   > created by github.com/pingcap/tidb/ddl.(*ddl).Start
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/ddl/ddl.go:364 +0x6a5
   > goroutine 850 [select]:
   > github.com/pingcap/tidb/domain.(*Domain).loadStatsWorker(0xc010a9e900)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:1226 +0x3cc
   > created by github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:1169 +0x2fa
   > goroutine 761 [select]:
   > github.com/pingcap/tidb/domain.(*Domain).topNSlowQueryLoop(0xc010a9e900)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:423 +0x1e5
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:771 +0x61c
   > goroutine 786 [select]:
   > github.com/pingcap/tidb/domain.(*Domain).globalBindHandleWorkerLoop.func1(0xc010a9e900, 0x404ecf8, 0xc000bd2080)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:1014 +0x157
   > created by github.com/pingcap/tidb/domain.(*Domain).globalBindHandleWorkerLoop
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:1001 +0x73
   > goroutine 866 [chan receive]:
   > github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).startAnalyzeProfileWorker(0xc0003d5860)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:141 +0xd4
   > created by github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).Run
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:93 +0xd9
   > goroutine 763 [select]:
   > github.com/pingcap/tidb/domain.(*Domain).topologySyncerKeeper(0xc010a9e900)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:481 +0x193
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:778 +0x6c5
   > goroutine 787 [select]:
   > github.com/pingcap/tidb/domain.(*Domain).handleEvolvePlanTasksLoop.func1(0xc010a9e900, 0x404ecf8, 0xc000bd2080, 0x40773d8, 0xc0110f6600)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:1050 +0xde
   > created by github.com/pingcap/tidb/domain.(*Domain).handleEvolvePlanTasksLoop
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:1043 +0x8f
   > goroutine 868 [IO wait]:
   > internal/poll.runtime_pollWait(0x7f8dea7cdff0, 0x72, 0x0)
   > 	/usr/local/go/src/runtime/netpoll.go:222 +0x55
   > internal/poll.(*pollDesc).wait(0xc0114e8698, 0x72, 0x0, 0x0, 0x3b05d89)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:87 +0x45
   > internal/poll.(*pollDesc).waitRead(...)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:92
   > internal/poll.(*FD).Accept(0xc0114e8680, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
   > 	/usr/local/go/src/internal/poll/fd_unix.go:401 +0x212
   > net.(*netFD).accept(0xc0114e8680, 0x37bb380, 0x1, 0xc011134450)
   > 	/usr/local/go/src/net/fd_unix.go:172 +0x45
   > net.(*TCPListener).accept(0xc0114ee060, 0xc0113efd70, 0xc0113efd78, 0x10)
   > 	/usr/local/go/src/net/tcpsock_posix.go:139 +0x32
   > net.(*TCPListener).Accept(0xc0114ee060, 0x3c1ef90, 0xc010f232b0, 0xc0115c6480, 0x0)
   > 	/usr/local/go/src/net/tcpsock.go:261 +0x65
   > github.com/pingcap/tidb/server.(*Server).startNetworkListener(0xc010f232b0, 0x4022c80, 0xc0114ee060, 0xc01115d300, 0xc010f80ea0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/server.go:347 +0x6a
   > created by github.com/pingcap/tidb/server.(*Server).Run
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/server.go:332 +0x11b
   > goroutine 984 [select]:
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc011c6ee00, 0x4, 0xc011b55ab0, 0x1, 0x1)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:445 +0x33f
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:339 +0xc5
   > github.com/pingcap/tidb/util.WithRecovery(0xc0119cf8c0, 0xc011b5fcf0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99 +0x4f
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:337 +0x1ab
   > goroutine 848 [select]:
   > github.com/pingcap/tidb/domain.(*Domain).TelemetryReportLoop.func1(0xc010a9e900, 0x40773d8, 0xc010f6e600)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:1084 +0x12f
   > created by github.com/pingcap/tidb/domain.(*Domain).TelemetryReportLoop
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:1076 +0x2b8
   > goroutine 762 [select]:
   > github.com/pingcap/tidb/domain.(*Domain).infoSyncerKeeper(0xc010a9e900)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:455 +0x138
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:774 +0x65b
   > goroutine 855 [syscall]:
   > os/signal.signal_recv(0x0)
   > 	/usr/local/go/src/runtime/sigqueue.go:168 +0xa5
   > os/signal.loop()
   > 	/usr/local/go/src/os/signal/signal_unix.go:23 +0x25
   > created by os/signal.Notify.func1.1
   > 	/usr/local/go/src/os/signal/signal.go:151 +0x45
   > goroutine 760 [select]:
   > github.com/pingcap/tidb/domain.(*Domain).loadSchemaInLoop(0xc010a9e900, 0x4030ee8, 0xc010a7b940, 0xa7a358200)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:513 +0x218
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:768 +0x734
   > goroutine 980 [select]:
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc011c6ee00, 0x0, 0xc011b55ab0, 0x1, 0x1)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:445 +0x33f
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:339 +0xc5
   > github.com/pingcap/tidb/util.WithRecovery(0xc0119cf7c0, 0xc011b5fcb0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99 +0x4f
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:337 +0x1ab
   > goroutine 983 [select]:
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc011c6ee00, 0x3, 0xc011b55ab0, 0x1, 0x1)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:445 +0x33f
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:339 +0xc5
   > github.com/pingcap/tidb/util.WithRecovery(0xc0119cf880, 0xc011b5fce0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99 +0x4f
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:337 +0x1ab
   > goroutine 755 [select]:
   > github.com/pingcap/tidb/ddl.(*delRange).startEmulator(0xc010afa050)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/ddl/delete_range.go:143 +0x128
   > created by github.com/pingcap/tidb/ddl.(*delRange).start
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/ddl/delete_range.go:125 +0x6a
   > goroutine 867 [IO wait]:
   > internal/poll.runtime_pollWait(0x7f8dea7cdf08, 0x72, 0x0)
   > 	/usr/local/go/src/runtime/netpoll.go:222 +0x55
   > internal/poll.(*pollDesc).wait(0xc0114e8718, 0x72, 0x0, 0x0, 0x3b05d89)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:87 +0x45
   > internal/poll.(*pollDesc).waitRead(...)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:92
   > internal/poll.(*FD).Accept(0xc0114e8700, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
   > 	/usr/local/go/src/internal/poll/fd_unix.go:401 +0x212
   > net.(*netFD).accept(0xc0114e8700, 0xc, 0x7f8e1129df18, 0x10)
   > 	/usr/local/go/src/net/fd_unix.go:172 +0x45
   > net.(*TCPListener).accept(0xc0114ee078, 0x11ed178, 0xc, 0x37efe60)
   > 	/usr/local/go/src/net/tcpsock_posix.go:139 +0x32
   > net.(*TCPListener).Accept(0xc0114ee078, 0xc011567240, 0x20, 0x7f8e1129df18, 0x20)
   > 	/usr/local/go/src/net/tcpsock.go:261 +0x65
   > github.com/soheilhy/cmux.(*cMux).Serve(0xc01157e140, 0x0, 0x0)
   > 	/nfs/cache/mod/github.com/soheilhy/cmux@v0.1.4/cmux.go:162 +0x96
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer(0xc010f232b0, 0xc01156a2c0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/http_status.go:370 +0x49f
   > github.com/pingcap/tidb/server.(*Server).startHTTPServer(0xc010f232b0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/http_status.go:346 +0x12a7
   > created by github.com/pingcap/tidb/server.(*Server).startStatusHTTP
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/http_status.go:59 +0x3f
   > goroutine 843 [select]:
   > github.com/pingcap/tidb/domain.(*Domain).LoadSysVarCacheLoop.func1(0xc010a9e900, 0xc010f3a490, 0x6fc23ac00, 0x40773d8, 0xc010f6e000)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:932 +0x125
   > created by github.com/pingcap/tidb/domain.(*Domain).LoadSysVarCacheLoop
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:923 +0xf6
   > goroutine 840 [select]:
   > github.com/pingcap/tidb/domain.(*Domain).LoadPrivilegeLoop.func1(0xc010a9e900, 0xc010f3a330, 0x45d964b800, 0x40773d8, 0xc000be2000)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:883 +0x125
   > created by github.com/pingcap/tidb/domain.(*Domain).LoadPrivilegeLoop
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:874 +0x1f0
   > goroutine 853 [select]:
   > github.com/pingcap/tidb/util/expensivequery.(*Handle).Run(0xc010a77f20)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/expensivequery/expensivequery.go:60 +0x337
   > created by main.createServer
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/tidb-server/main.go:631 +0x1c7
   > goroutine 783 [select]:
   > github.com/pingcap/tidb/util/topsql/reporter.(*RemoteTopSQLReporter).collectWorker(0xc01116a7e0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:325 +0x1bb
   > created by github.com/pingcap/tidb/util/topsql/reporter.NewRemoteTopSQLReporter
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:158 +0x1a7
   > goroutine 782 [chan receive]:
   > github.com/pingcap/tidb/util/signal.SetupSignalHandler.func2(0xc0114f8120, 0xc0114e54a0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:52 +0x52
   > created by github.com/pingcap/tidb/util/signal.SetupSignalHandler
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:51 +0x194
   > goroutine 851 [select]:
   > github.com/pingcap/tidb/domain.(*Domain).updateStatsWorker(0xc010a9e900, 0x40773d8, 0xc010f6ec00, 0x404ecf8, 0xc010f7e820)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:1294 +0x288
   > created by github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:1181 +0x1d6
   > goroutine 784 [select]:
   > github.com/pingcap/tidb/util/topsql/reporter.(*RemoteTopSQLReporter).reportWorker(0xc01116a7e0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:497 +0x211
   > created by github.com/pingcap/tidb/util/topsql/reporter.NewRemoteTopSQLReporter
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:159 +0x1c9
   > goroutine 859 [chan receive]:
   > github.com/soheilhy/cmux.muxListener.Accept(...)
   > 	/nfs/cache/mod/github.com/soheilhy/cmux@v0.1.4/cmux.go:229
   > google.golang.org/grpc.(*Server).Serve(0xc010f7c820, 0x4023c40, 0xc0114ee648, 0x0, 0x0)
   > 	/nfs/cache/mod/google.golang.org/grpc@v1.29.1/server.go:621 +0x27f
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer.func1()
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/http_status.go:361 +0x58
   > github.com/pingcap/tidb/util.WithRecovery(0xc011568580, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99 +0x4f
   > created by github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/http_status.go:360 +0x405
   > goroutine 856 [chan receive]:
   > github.com/pingcap/tidb/util/signal.SetupSignalHandler.func1(0xc0114f80c0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:36 +0x72
   > created by github.com/pingcap/tidb/util/signal.SetupSignalHandler
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:33 +0xb9
   > goroutine 860 [chan receive]:
   > github.com/soheilhy/cmux.muxListener.Accept(...)
   > 	/nfs/cache/mod/github.com/soheilhy/cmux@v0.1.4/cmux.go:229
   > net/http.(*Server).Serve(0xc010f35340, 0x4023c40, 0xc0114ee630, 0x0, 0x0)
   > 	/usr/local/go/src/net/http/server.go:2981 +0x285
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer.func2()
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/http_status.go:366 +0x58
   > github.com/pingcap/tidb/util.WithRecovery(0xc0115685a0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99 +0x4f
   > created by github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/http_status.go:365 +0x488
   > goroutine 982 [select]:
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc011c6ee00, 0x2, 0xc011b55ab0, 0x1, 0x1)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:445 +0x33f
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:339 +0xc5
   > github.com/pingcap/tidb/util.WithRecovery(0xc0119cf840, 0xc011b5fcd0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99 +0x4f
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:337 +0x1ab
   > goroutine 985 [semacquire]:
   > sync.runtime_Semacquire(0xc011c6efd4)
   > 	/usr/local/go/src/runtime/sema.go:56 +0x45
   > sync.(*WaitGroup).Wait(0xc011c6efd4)
   > 	/usr/local/go/src/sync/waitgroup.go:130 +0x65
   > github.com/pingcap/tidb/executor.(*HashJoinExec).waitJoinWorkersAndCloseResultChan(0xc011c6ee00)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:399 +0x3d
   > github.com/pingcap/tidb/util.WithRecovery(0xc011b5fd00, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99 +0x4f
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:342 +0x336
   > goroutine 930 [chan receive]:
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Next(0xc011c6fc00, 0x4030f90, 0xc0119d22a0, 0xc011d6f310, 0xc011a72b80, 0x28aeca3)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:668 +0x87
   > github.com/pingcap/tidb/executor.Next(0x4030f90, 0xc0119d22a0, 0x40359f8, 0xc011c6fc00, 0xc011d6f310, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/executor.go:285 +0x2de
   > github.com/pingcap/tidb/executor.(*ProjectionExec).unParallelExecute(0xc011d20100, 0x4030f90, 0xc0119d22a0, 0xc011d6fc20, 0x0, 0x35346118bc00)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:193 +0xb2
   > github.com/pingcap/tidb/executor.(*ProjectionExec).Next(0xc011d20100, 0x4030f90, 0xc0119d22a0, 0xc011d6fc20, 0xc011e17e30, 0x40773d8)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:179 +0x73
   > github.com/pingcap/tidb/executor.Next(0x4030f90, 0xc0119d22a0, 0x4035f78, 0xc011d20100, 0xc011d6fc20, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/executor.go:285 +0x2de
   > github.com/pingcap/tidb/executor.(*recordSet).Next(0xc011d6fb80, 0x4030f90, 0xc0119d22a0, 0xc011d6fc20, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/adapter.go:145 +0xb5
   > github.com/pingcap/tidb/server.(*tidbResultSet).Next(0xc011d6fbd0, 0x4030f90, 0xc0119d22a0, 0xc011d6fc20, 0xc01198d2a8, 0x400)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/driver_tidb.go:305 +0x51
   > github.com/pingcap/tidb/server.(*clientConn).writeChunks(0xc0115c6480, 0x4030f90, 0xc0119d22a0, 0x4049e68, 0xc011d6fbd0, 0x20000, 0x5d958d8, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/conn.go:2016 +0x4de
   > github.com/pingcap/tidb/server.(*clientConn).writeResultset(0xc0115c6480, 0x4030f90, 0xc0119d22a0, 0x4049e68, 0xc011d6fbd0, 0x29e00, 0x0, 0x0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/conn.go:1964 +0x20e
   > github.com/pingcap/tidb/server.(*clientConn).handleStmt(0xc0115c6480, 0x4030ee8, 0xc0119d22a0, 0x404e488, 0xc0119ca4b0, 0x5d958d8, 0x0, 0x0, 0x1, 0x0, ...)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/conn.go:1844 +0x3e5
   > github.com/pingcap/tidb/server.(*clientConn).handleQuery(0xc0115c6480, 0x4030ee8, 0xc0115fe140, 0xc0005e01a1, 0x18c, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/conn.go:1690 +0x492
   > github.com/pingcap/tidb/server.(*clientConn).dispatch(0xc0115c6480, 0x4030ee8, 0xc0115fe140, 0xc0005e01a0, 0x18d, 0x18c, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/conn.go:1215 +0xafd
   > github.com/pingcap/tidb/server.(*clientConn).Run(0xc0115c6480, 0x4030f90, 0xc0119c7cb0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/conn.go:978 +0x296
   > github.com/pingcap/tidb/server.(*Server).onConn(0xc010f232b0, 0xc0115c6480)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/server.go:501 +0xa53
   > created by github.com/pingcap/tidb/server.(*Server).startNetworkListener
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/server.go:404 +0x8fc
   > goroutine 981 [select]:
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc011c6ee00, 0x1, 0xc011b55ab0, 0x1, 0x1)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:445 +0x33f
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:339 +0xc5
   > github.com/pingcap/tidb/util.WithRecovery(0xc0119cf800, 0xc011b5fcc0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99 +0x4f
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:337 +0x1ab
   > goroutine 979 [select]:
   > github.com/pingcap/tidb/executor.(*HashJoinExec).wait4BuildSide(0xc011c6ee00, 0xc0119d22a0, 0x40365b8, 0xc011c19380)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:244 +0x88
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchProbeSideChunks(0xc011c6ee00, 0x4030f90, 0xc0119d22a0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:223 +0x26f
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func1()
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:324 +0xa9
   > github.com/pingcap/tidb/util.WithRecovery(0xc011993580, 0xc011b5fca0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99 +0x4f
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:322 +0xfd
   > goroutine 978 [chan receive]:
   > github.com/pingcap/tidb/executor.(*HashJoinExec).buildHashTableForList(0xc011c6ee00, 0xc011bc6720, 0xc011bc2840, 0xc011b5fd20)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:758 +0x327
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable(0xc011c6ee00, 0x4030f90, 0xc0119d22a0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:713 +0x1b3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Next.func1()
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:658 +0xa9
   > github.com/pingcap/tidb/util.WithRecovery(0xc011993560, 0xc011b5fbf0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99 +0x4f
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).Next
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:656 +0x305
   > goroutine 964 [chan receive]:
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Next(0xc011c6ee00, 0x4030f90, 0xc0119d22a0, 0xc011d6fc70, 0x0, 0x2)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:668 +0x87
   > github.com/pingcap/tidb/executor.Next(0x4030f90, 0xc0119d22a0, 0x40359f8, 0xc011c6ee00, 0xc011d6fc70, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/executor.go:285 +0x2de
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchProbeSideChunks(0xc011c6fc00, 0x4030f90, 0xc0119d22a0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:211 +0x1d4
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func1()
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:324 +0xa9
   > github.com/pingcap/tidb/util.WithRecovery(0xc011e22300, 0xc011d7ebb0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99 +0x4f
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:322 +0xfd
   > goroutine 965 [select]:
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc011c6fc00, 0x0, 0xc011d61b00, 0x1, 0x1)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:445 +0x33f
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:339 +0xc5
   > github.com/pingcap/tidb/util.WithRecovery(0xc011d10c40, 0xc011d7ebc0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99 +0x4f
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:337 +0x1ab
   > goroutine 966 [select]:
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc011c6fc00, 0x1, 0xc011d61b00, 0x1, 0x1)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:445 +0x33f
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:339 +0xc5
   > github.com/pingcap/tidb/util.WithRecovery(0xc011d10c80, 0xc011d7ebd0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99 +0x4f
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:337 +0x1ab
   > goroutine 967 [select]:
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc011c6fc00, 0x2, 0xc011d61b00, 0x1, 0x1)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:445 +0x33f
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:339 +0xc5
   > github.com/pingcap/tidb/util.WithRecovery(0xc011d10cc0, 0xc011d7ebe0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99 +0x4f
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:337 +0x1ab
   > goroutine 968 [select]:
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc011c6fc00, 0x3, 0xc011d61b00, 0x1, 0x1)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:445 +0x33f
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:339 +0xc5
   > github.com/pingcap/tidb/util.WithRecovery(0xc011d10d00, 0xc011d7ebf0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99 +0x4f
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:337 +0x1ab
   > goroutine 969 [select]:
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc011c6fc00, 0x4, 0xc011d61b00, 0x1, 0x1)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:445 +0x33f
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:339 +0xc5
   > github.com/pingcap/tidb/util.WithRecovery(0xc011d10d40, 0xc011d7ec00)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99 +0x4f
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:337 +0x1ab
   > goroutine 970 [semacquire]:
   > sync.runtime_Semacquire(0xc011c6fdd4)
   > 	/usr/local/go/src/runtime/sema.go:56 +0x45
   > sync.(*WaitGroup).Wait(0xc011c6fdd4)
   > 	/usr/local/go/src/sync/waitgroup.go:130 +0x65
   > github.com/pingcap/tidb/executor.(*HashJoinExec).waitJoinWorkersAndCloseResultChan(0xc011c6fc00)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:399 +0x3d
   > github.com/pingcap/tidb/util.WithRecovery(0xc011d7ec10, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99 +0x4f
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:342 +0x336
   > goroutine 94 [select]:
   > github.com/pingcap/tidb/executor.readProjectionInput(0xc00106e5a0, 0xc011f0c000, 0x3b1ee58)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:459 +0x86
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc001078040, 0x4030f90, 0xc0119d22a0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:427 +0x129
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:275 +0x78f
   > goroutine 95 [select]:
   > github.com/pingcap/tidb/executor.readProjectionInput(0xc00106e6c0, 0xc011f0c000, 0x3b1ee58)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:459 +0x86
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc001078080, 0x4030f90, 0xc0119d22a0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:427 +0x129
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:275 +0x78f
   > goroutine 96 [select]:
   > github.com/pingcap/tidb/executor.readProjectionInput(0xc00106e7e0, 0xc011f0c000, 0x3b1ee58)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:459 +0x86
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc0010780c0, 0x4030f90, 0xc0119d22a0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:427 +0x129
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:275 +0x78f
   > goroutine 97 [select]:
   > github.com/pingcap/tidb/executor.readProjectionInput(0xc00106e900, 0xc011f0c000, 0x3b1ee58)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:459 +0x86
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc001078100, 0x4030f90, 0xc0119d22a0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:427 +0x129
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:275 +0x78f
   > goroutine 1042 [select]:
   > github.com/pingcap/tidb/executor.readProjectionInput(0xc00106ea20, 0xc011f0c000, 0x3b1ee58)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:459 +0x86
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc001078140, 0x4030f90, 0xc0119d22a0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:427 +0x129
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:275 +0x78f
   > goroutine 1040 [select]:
   > github.com/pingcap/tidb/executor.readProjectionInput(0xc01167a180, 0xc01167c000, 0xc0105cca00)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:459 +0x86
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc011678040, 0x4030f90, 0xc0119d22a0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:427 +0x129
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:275 +0x78f
   > goroutine 1041 [select]:
   > github.com/pingcap/tidb/executor.readProjectionInput(0xc01167a2a0, 0xc01167c000, 0x3b1ee58)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:459 +0x86
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc011678080, 0x4030f90, 0xc0119d22a0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:427 +0x129
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:275 +0x78f
   > goroutine 1058 [select]:
   > github.com/pingcap/tidb/executor.readProjectionInput(0xc01167a3c0, 0xc01167c000, 0x3b1ee58)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:459 +0x86
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc0116780c0, 0x4030f90, 0xc0119d22a0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:427 +0x129
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:275 +0x78f
   > goroutine 1059 [select]:
   > github.com/pingcap/tidb/executor.readProjectionInput(0xc01167a4e0, 0xc01167c000, 0x3b1ee58)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:459 +0x86
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc011678100, 0x4030f90, 0xc0119d22a0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:427 +0x129
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:275 +0x78f
   > goroutine 1060 [select]:
   > github.com/pingcap/tidb/executor.readProjectionInput(0xc01167a600, 0xc01167c000, 0x3b1ee58)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:459 +0x86
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc011678140, 0x4030f90, 0xc0119d22a0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:427 +0x129
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:275 +0x78f
   > goroutine 1006 [chan receive]:
   > gopkg.in/natefinch/lumberjack%2ev2.(*Logger).millRun(0xc000a0e7e0)
   > 	/nfs/cache/mod/gopkg.in/natefinch/lumberjack.v2@v2.0.0/lumberjack.go:379 +0x5d
   > created by gopkg.in/natefinch/lumberjack%2ev2.(*Logger).mill.func1
   > 	/nfs/cache/mod/gopkg.in/natefinch/lumberjack.v2@v2.0.0/lumberjack.go:390 +0x75
