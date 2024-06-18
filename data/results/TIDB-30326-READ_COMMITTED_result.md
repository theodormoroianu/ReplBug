# Bug ID TIDB-30326-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/30326
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED


## Details
 * Database: tidb-v5.4.0
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
   > [2024/06/18 16:12:09.663 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=5] [user=root] [host=]
   > [2024/06/18 16:12:09.667 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=28] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/06/18 16:12:09.668 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=28] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/06/18 16:12:09.669 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:58, Type:create schema, State:none, SchemaState:queueing, SchemaID:57, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 16:12:09.669 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 16:12:09.669 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:58, Type:create schema, State:none, SchemaState:queueing, SchemaID:57, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 16:12:09.669 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/18 16:12:09.670 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:58, Type:create schema, State:none, SchemaState:queueing, SchemaID:57, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:09.669 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:09.671 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=28] [neededSchemaVersion=29] ["start time"=177.329µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 16:12:09.673 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=29] ["take time"=2.246122ms] [job="ID:58, Type:create schema, State:done, SchemaState:public, SchemaID:57, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 16:12:09.669 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:09.674 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:58, Type:create schema, State:synced, SchemaState:public, SchemaID:57, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:09.669 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:09.675 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=58]
   > [2024/06/18 16:12:09.675 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 16:12:09.688 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=29] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_037irb`\n--\n\nDROP TABLE IF EXISTS `t_037irb`;"] [user=root@127.0.0.1]
   > [2024/06/18 16:12:09.689 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=29] [cur_db=testdb] [sql="CREATE TABLE `t_037irb` (\n  `c_nrh3o` int(11) DEFAULT NULL,\n  `c_nfauxb` text DEFAULT NULL,\n  `c_y5n4c` int(11) DEFAULT NULL,\n  `c_j9alg` double NOT NULL,\n  `c_4vix1d` text DEFAULT NULL,\n  `c_glkxdb` text DEFAULT NULL,\n  `c_2ykt0d` int(11) DEFAULT NULL,\n  `c_5fxv3c` double DEFAULT NULL,\n  PRIMARY KEY (`c_j9alg`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/06/18 16:12:09.691 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:60, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:59, RowCount:0, ArgLen:1, start time: 2024-06-18 16:12:09.69 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 16:12:09.691 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:60, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:59, RowCount:0, ArgLen:1, start time: 2024-06-18 16:12:09.69 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_037irb` (\n  `c_nrh3o` int(11) DEFAULT NULL,\n  `c_nfauxb` text DEFAULT NULL,\n  `c_y5n4c` int(11) DEFAULT NULL,\n  `c_j9alg` double NOT NULL,\n  `c_4vix1d` text DEFAULT NULL,\n  `c_glkxdb` text DEFAULT NULL,\n  `c_2ykt0d` int(11) DEFAULT NULL,\n  `c_5fxv3c` double DEFAULT NULL,\n  PRIMARY KEY (`c_j9alg`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/18 16:12:09.691 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:60, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:59, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:09.69 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:09.694 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=29] [neededSchemaVersion=30] ["start time"=746.682µs] [phyTblIDs="[59]"] [actionTypes="[8]"]
   > [2024/06/18 16:12:09.695 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=30] ["take time"=2.258065ms] [job="ID:60, Type:create table, State:done, SchemaState:public, SchemaID:57, TableID:59, RowCount:0, ArgLen:1, start time: 2024-06-18 16:12:09.69 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:09.696 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:60, Type:create table, State:synced, SchemaState:public, SchemaID:57, TableID:59, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:09.69 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:09.698 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=60]
   > [2024/06/18 16:12:09.698 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 16:12:09.698 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=52] ["first split key"=74800000000000003b]
   > [2024/06/18 16:12:09.698 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=30] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_037irb` DISABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/06/18 16:12:09.699 +00:00] [WARN] [2pc.go:1596] ["schemaLeaseChecker is not set for this transaction"] [sessionID=5] [startTS=450554004687814657] [commitTS=450554004687814658]
   > [2024/06/18 16:12:09.701 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=54] ["first at"=74800000000000003b] ["first new region left"="{Id:54 StartKey:7480000000000000ff3700000000000000f8 EndKey:7480000000000000ff3b00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:55 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/18 16:12:09.701 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[54]"]
   > [2024/06/18 16:12:09.701 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=30] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_037irb` ENABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/06/18 16:12:09.702 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=30] [cur_db=testdb] [sql="\n--\n-- Temporary view structure for view `t_cpsvpb`\n--\n\nDROP TABLE IF EXISTS `t_cpsvpb`;"] [user=root@127.0.0.1]
   > [2024/06/18 16:12:09.702 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=30] [cur_db=testdb] [sql="/*!50001 DROP VIEW IF EXISTS `t_cpsvpb`*/;"] [user=root@127.0.0.1]
   > [2024/06/18 16:12:09.703 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:62, Type:create view, State:none, SchemaState:queueing, SchemaID:57, TableID:61, RowCount:0, ArgLen:3, start time: 2024-06-18 16:12:09.703 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 16:12:09.703 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:62, Type:create view, State:none, SchemaState:queueing, SchemaID:57, TableID:61, RowCount:0, ArgLen:3, start time: 2024-06-18 16:12:09.703 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="/*!50001 CREATE VIEW `t_cpsvpb` AS SELECT \n 1 AS `c0`,\n 1 AS `c2`,\n 1 AS `c3`,\n 1 AS `c4`,\n 1 AS `c5`,\n 1 AS `c6`,\n 1 AS `c7`,\n 1 AS `c8`,\n 1 AS `c9`,\n 1 AS `c10`,\n 1 AS `c11`,\n 1 AS `c12`,\n 1 AS `c13`,\n 1 AS `c14`*/;"]
   > [2024/06/18 16:12:09.704 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:62, Type:create view, State:none, SchemaState:queueing, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:09.703 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:09.705 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=30] [neededSchemaVersion=31] ["start time"=214.135µs] [phyTblIDs="[61]"] [actionTypes="[2097152]"]
   > [2024/06/18 16:12:09.707 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=31] ["take time"=2.232572ms] [job="ID:62, Type:create view, State:done, SchemaState:public, SchemaID:57, TableID:61, RowCount:0, ArgLen:3, start time: 2024-06-18 16:12:09.703 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:09.708 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:62, Type:create view, State:synced, SchemaState:public, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:09.703 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:09.709 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=62]
   > [2024/06/18 16:12:09.709 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 16:12:09.710 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=31] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_x7zqmd`\n--\n\nDROP TABLE IF EXISTS `t_x7zqmd`;"] [user=root@127.0.0.1]
   > [2024/06/18 16:12:09.710 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=31] [cur_db=testdb] [sql="CREATE TABLE `t_x7zqmd` (\n  `c_8weeq` int(11) NOT NULL,\n  `c_13sfid` double DEFAULT NULL,\n  `c_hhjlmc` text DEFAULT NULL,\n  `c_3b1zld` int(11) DEFAULT NULL,\n  `c_6tu8wd` int(11) DEFAULT NULL,\n  `c_jyc_cd` double DEFAULT NULL,\n  PRIMARY KEY (`c_8weeq`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/06/18 16:12:09.711 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:64, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:63, RowCount:0, ArgLen:1, start time: 2024-06-18 16:12:09.711 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 16:12:09.711 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:64, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:63, RowCount:0, ArgLen:1, start time: 2024-06-18 16:12:09.711 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_x7zqmd` (\n  `c_8weeq` int(11) NOT NULL,\n  `c_13sfid` double DEFAULT NULL,\n  `c_hhjlmc` text DEFAULT NULL,\n  `c_3b1zld` int(11) DEFAULT NULL,\n  `c_6tu8wd` int(11) DEFAULT NULL,\n  `c_jyc_cd` double DEFAULT NULL,\n  PRIMARY KEY (`c_8weeq`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/18 16:12:09.712 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:64, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:63, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:09.711 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:09.713 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=31] [neededSchemaVersion=32] ["start time"=262.955µs] [phyTblIDs="[63]"] [actionTypes="[8]"]
   > [2024/06/18 16:12:09.715 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=32] ["take time"=2.02144ms] [job="ID:64, Type:create table, State:done, SchemaState:public, SchemaID:57, TableID:63, RowCount:0, ArgLen:1, start time: 2024-06-18 16:12:09.711 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:09.715 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:64, Type:create table, State:synced, SchemaState:public, SchemaID:57, TableID:63, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:09.711 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:09.716 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=64]
   > [2024/06/18 16:12:09.716 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 16:12:09.716 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=54] ["first split key"=74800000000000003f]
   > [2024/06/18 16:12:09.717 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=32] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_x7zqmd` DISABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/06/18 16:12:09.719 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=32] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_x7zqmd` ENABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/06/18 16:12:09.719 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=56] ["first at"=74800000000000003f] ["first new region left"="{Id:56 StartKey:7480000000000000ff3b00000000000000f8 EndKey:7480000000000000ff3f00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:57 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/18 16:12:09.719 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[56]"]
   > [2024/06/18 16:12:09.719 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=32] [cur_db=testdb] [sql="\n--\n-- Final view structure for view `t_cpsvpb`\n--\n\n/*!50001 DROP VIEW IF EXISTS `t_cpsvpb`*/;"] [user=root@127.0.0.1]
   > [2024/06/18 16:12:09.720 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:65, Type:drop view, State:none, SchemaState:queueing, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:09.719 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 16:12:09.720 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:65, Type:drop view, State:none, SchemaState:queueing, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:09.719 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="\n--\n-- Final view structure for view `t_cpsvpb`\n--\n\n/*!50001 DROP VIEW IF EXISTS `t_cpsvpb`*/;"]
   > [2024/06/18 16:12:09.720 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:drop view, State:none, SchemaState:queueing, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:09.719 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:09.722 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=32] [neededSchemaVersion=33] ["start time"=66.909µs] [phyTblIDs="[61]"] [actionTypes="[16777216]"]
   > [2024/06/18 16:12:09.724 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=33] ["take time"=2.658261ms] [job="ID:65, Type:drop view, State:running, SchemaState:write only, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:09.719 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:09.725 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:drop view, State:running, SchemaState:write only, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:09.719 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:09.726 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=33] [neededSchemaVersion=34] ["start time"=64.883µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 16:12:09.728 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=34] ["take time"=2.201143ms] [job="ID:65, Type:drop view, State:running, SchemaState:delete only, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:09.719 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:09.728 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:drop view, State:running, SchemaState:delete only, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:09.719 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:09.730 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=34] [neededSchemaVersion=35] ["start time"=119.919µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 16:12:09.732 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=35] ["take time"=2.684242ms] [job="ID:65, Type:drop view, State:done, SchemaState:queueing, SchemaID:57, TableID:61, RowCount:0, ArgLen:3, start time: 2024-06-18 16:12:09.719 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:09.733 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:drop view, State:synced, SchemaState:queueing, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:09.719 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:09.734 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=65]
   > [2024/06/18 16:12:09.734 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 16:12:09.740 +00:00] [INFO] [session.go:2108] ["Try to create a new txn inside a transaction auto commit"] [conn=5] [schemaVersion=35] [txnStartTS=450554004697251840] [txnScope=global]
   > [2024/06/18 16:12:09.741 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:67, Type:create view, State:none, SchemaState:queueing, SchemaID:57, TableID:66, RowCount:0, ArgLen:3, start time: 2024-06-18 16:12:09.74 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 16:12:09.741 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:67, Type:create view, State:none, SchemaState:queueing, SchemaID:57, TableID:66, RowCount:0, ArgLen:3, start time: 2024-06-18 16:12:09.74 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="/*!50001 CREATE ALGORITHM=UNDEFINED */\n/*!50013 DEFINER=`root`@`127.0.0.1` SQL SECURITY DEFINER */\n/*!50001 VIEW `t_cpsvpb` (`c0`, `c2`, `c3`, `c4`, `c5`, `c6`, `c7`, `c8`, `c9`, `c10`, `c11`, `c12`, `c13`, `c14`) AS SELECT DISTINCT `subq_0`.`c1` AS `c0`,`subq_0`.`c2` AS `c2`,8 AS `c3`,CASE WHEN (`subq_0`.`c3` NOT IN (SELECT `ref_2`.`c_4vix1d` AS `c0` FROM `testdb`.`t_037irb` AS `ref_2` WHERE `ref_2`.`c_2ykt0d`<=`ref_2`.`c_nrh3o`)) AND (`subq_0`.`c3`<=(SELECT (SELECT `c_hhjlmc` AS `c_hhjlmc` FROM `testdb`.`t_x7zqmd` ORDER BY `c_hhjlmc` LIMIT 4,1) AS `c0` FROM `testdb`.`t_037irb` AS `ref_3` WHERE `subq_0`.`c1`!=`ref_3`.`c_2ykt0d`)) THEN `subq_0`.`c3` ELSE `subq_0`.`c3` END AS `c4`,CASE WHEN `subq_0`.`c1`>=(SELECT MAX(`c_8weeq`) AS `max(c_8weeq)` FROM `testdb`.`t_x7zqmd`) THEN `subq_0`.`c2` ELSE `subq_0`.`c2` END AS `c5`,`subq_0`.`c1` AS `c6`,`subq_0`.`c2` AS `c7`,`subq_0`.`c3` AS `c8`,`subq_0`.`c3` AS `c9`,`subq_0`.`c2` AS `c10`,`subq_0`.`c4` AS `c11`,COUNT(CAST(`subq_0`.`c2` AS DOUBLE)) OVER (PARTITION BY `subq_0`.`c4` ORDER BY `subq_0`.`c1`) AS `c12`,`subq_0`.`c3` AS `c13`,CAST(COALESCE(`subq_0`.`c3`, _UTF8MB4'9sx3k') AS CHAR) AS `c14` FROM (SELECT COUNT(CAST(`ref_1`.`c_jyc_cd` AS DOUBLE)) AS `c0`,AVG(CAST(`ref_1`.`c_3b1zld` AS SIGNED)) AS `c1`,MIN(CAST(`ref_1`.`c_jyc_cd` AS DOUBLE)) AS `c2`,`ref_0`.`c_glkxdb` AS `c3`,COUNT(CAST(`ref_1`.`c_13sfid` AS DOUBLE)) AS `c4` FROM `testdb`.`t_037irb` AS `ref_0` JOIN `testdb`.`t_x7zqmd` AS `ref_1` WHERE `ref_0`.`c_nrh3o`>`ref_1`.`c_8weeq` GROUP BY `ref_0`.`c_glkxdb`) AS `subq_0` WHERE (SELECT `c_8weeq` AS `c_8weeq` FROM `testdb`.`t_x7zqmd` ORDER BY `c_8weeq` LIMIT 2,1) IS NOT NULL */;"]
   > [2024/06/18 16:12:09.742 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:create view, State:none, SchemaState:queueing, SchemaID:57, TableID:66, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:09.74 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:09.744 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=35] [neededSchemaVersion=36] ["start time"=557.34µs] [phyTblIDs="[66]"] [actionTypes="[2097152]"]
   > [2024/06/18 16:12:09.746 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=36] ["take time"=2.266237ms] [job="ID:67, Type:create view, State:done, SchemaState:public, SchemaID:57, TableID:66, RowCount:0, ArgLen:3, start time: 2024-06-18 16:12:09.74 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:09.748 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:create view, State:synced, SchemaState:public, SchemaID:57, TableID:66, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:09.74 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:09.749 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=67]
   > [2024/06/18 16:12:09.749 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 16:12:10.829 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=7] [user=root] [host=]
   > [2024/06/18 16:12:10.848 +00:00] [INFO] [set.go:139] ["set global var"] [conn=7] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/06/18 16:12:11.078 +00:00] [ERROR] [misc.go:95] ["panic in the recoverable goroutine"] [r="\"invalid memory address or nil pointer dereference\""] ["stack trace"="github.com/pingcap/tidb/util.WithRecovery.func1\n\t/go/src/github.com/pingcap/tidb/util/misc.go:97\nruntime.gopanic\n\t/usr/local/go/src/runtime/panic.go:884\nruntime.panicmem\n\t/usr/local/go/src/runtime/panic.go:260\nruntime.sigpanic\n\t/usr/local/go/src/runtime/signal_unix.go:839\ngithub.com/pingcap/tidb/executor.(*vecGroupChecker).splitIntoGroups\n\t/go/src/github.com/pingcap/tidb/executor/aggregate.go:1457\ngithub.com/pingcap/tidb/executor.(*PipelinedWindowExec).getRowsInPartition\n\t/go/src/github.com/pingcap/tidb/executor/pipelined_window.go:189\ngithub.com/pingcap/tidb/executor.(*PipelinedWindowExec).Next\n\t/go/src/github.com/pingcap/tidb/executor/pipelined_window.go:125\ngithub.com/pingcap/tidb/executor.Next\n\t/go/src/github.com/pingcap/tidb/executor/executor.go:286\ngithub.com/pingcap/tidb/executor.(*ProjectionExec).unParallelExecute\n\t/go/src/github.com/pingcap/tidb/executor/projection.go:194\ngithub.com/pingcap/tidb/executor.(*ProjectionExec).Next\n\t/go/src/github.com/pingcap/tidb/executor/projection.go:180\ngithub.com/pingcap/tidb/executor.Next\n\t/go/src/github.com/pingcap/tidb/executor/executor.go:286\ngithub.com/pingcap/tidb/executor.(*CTEExec).computeSeedPart\n\t/go/src/github.com/pingcap/tidb/executor/cte.go:226\ngithub.com/pingcap/tidb/executor.(*CTEExec).Next\n\t/go/src/github.com/pingcap/tidb/executor/cte.go:161\ngithub.com/pingcap/tidb/executor.Next\n\t/go/src/github.com/pingcap/tidb/executor/executor.go:286\ngithub.com/pingcap/tidb/executor.(*HashJoinExec).fetchBuildSideRows\n\t/go/src/github.com/pingcap/tidb/executor/join.go:266\ngithub.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable.func2\n\t/go/src/github.com/pingcap/tidb/executor/join.go:715\ngithub.com/pingcap/tidb/util.WithRecovery\n\t/go/src/github.com/pingcap/tidb/util/misc.go:100"]
   > runtime: goroutine stack exceeds 1000000000-byte limit
   > runtime: sp=0xc0325ee380 stack=[0xc0325ee000, 0xc0525ee000]
   > fatal error: stack overflow
   > runtime stack:
   > runtime.throw({0x3aa773d?, 0x590b5c0?})
   > 	/usr/local/go/src/runtime/panic.go:1047 +0x5d fp=0x7f3774854888 sp=0x7f3774854858 pc=0x13b859d
   > runtime.newstack()
   > 	/usr/local/go/src/runtime/stack.go:1103 +0x5cc fp=0x7f3774854a40 sp=0x7f3774854888 pc=0x13d35ec
   > runtime.morestack()
   > 	/usr/local/go/src/runtime/asm_amd64.s:570 +0x8b fp=0x7f3774854a48 sp=0x7f3774854a40 pc=0x13ec60b
   > goroutine 936 [running]:
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60?, 0xc011fa2de0?}, {0x4012e60?, 0xc011fa2e40?})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:183 +0x12c fp=0xc0325ee390 sp=0xc0325ee388 pc=0x1f5780c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc000bf2de0}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ee3c8 sp=0xc0325ee390 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0123fe060}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ee400 sp=0xc0325ee3c8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0121c0800}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ee438 sp=0xc0325ee400 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01250c230}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ee470 sp=0xc0325ee438 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0120681e0}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ee4a8 sp=0xc0325ee470 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0124ac9f0}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ee4e0 sp=0xc0325ee4a8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01240e160}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ee518 sp=0xc0325ee4e0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc000bf2720}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ee550 sp=0xc0325ee518 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0120727e0}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ee588 sp=0xc0325ee550 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011f91120}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ee5c0 sp=0xc0325ee588 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011fa2e40}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ee5f8 sp=0xc0325ee5c0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011fa2de0}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ee630 sp=0xc0325ee5f8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc000bf2de0}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ee668 sp=0xc0325ee630 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0123fe060}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ee6a0 sp=0xc0325ee668 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0121c0800}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ee6d8 sp=0xc0325ee6a0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01250c230}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ee710 sp=0xc0325ee6d8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0120681e0}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ee748 sp=0xc0325ee710 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0124ac9f0}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ee780 sp=0xc0325ee748 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01240e160}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ee7b8 sp=0xc0325ee780 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc000bf2720}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ee7f0 sp=0xc0325ee7b8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0120727e0}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ee828 sp=0xc0325ee7f0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011f91120}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ee860 sp=0xc0325ee828 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011fa2e40}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ee898 sp=0xc0325ee860 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011fa2de0}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ee8d0 sp=0xc0325ee898 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc000bf2de0}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ee908 sp=0xc0325ee8d0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0123fe060}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ee940 sp=0xc0325ee908 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0121c0800}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ee978 sp=0xc0325ee940 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01250c230}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ee9b0 sp=0xc0325ee978 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0120681e0}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ee9e8 sp=0xc0325ee9b0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0124ac9f0}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325eea20 sp=0xc0325ee9e8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01240e160}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325eea58 sp=0xc0325eea20 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc000bf2720}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325eea90 sp=0xc0325eea58 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0120727e0}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325eeac8 sp=0xc0325eea90 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011f91120}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325eeb00 sp=0xc0325eeac8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011fa2e40}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325eeb38 sp=0xc0325eeb00 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011fa2de0}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325eeb70 sp=0xc0325eeb38 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc000bf2de0}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325eeba8 sp=0xc0325eeb70 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0123fe060}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325eebe0 sp=0xc0325eeba8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0121c0800}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325eec18 sp=0xc0325eebe0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01250c230}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325eec50 sp=0xc0325eec18 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0120681e0}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325eec88 sp=0xc0325eec50 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0124ac9f0}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325eecc0 sp=0xc0325eec88 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01240e160}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325eecf8 sp=0xc0325eecc0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc000bf2720}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325eed30 sp=0xc0325eecf8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0120727e0}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325eed68 sp=0xc0325eed30 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011f91120}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325eeda0 sp=0xc0325eed68 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011fa2e40}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325eedd8 sp=0xc0325eeda0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011fa2de0}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325eee10 sp=0xc0325eedd8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc000bf2de0}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325eee48 sp=0xc0325eee10 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0123fe060}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325eee80 sp=0xc0325eee48 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0121c0800}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325eeeb8 sp=0xc0325eee80 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01250c230}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325eeef0 sp=0xc0325eeeb8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0120681e0}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325eef28 sp=0xc0325eeef0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0124ac9f0}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325eef60 sp=0xc0325eef28 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01240e160}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325eef98 sp=0xc0325eef60 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc000bf2720}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325eefd0 sp=0xc0325eef98 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0120727e0}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef008 sp=0xc0325eefd0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011f91120}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef040 sp=0xc0325ef008 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011fa2e40}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef078 sp=0xc0325ef040 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011fa2de0}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef0b0 sp=0xc0325ef078 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc000bf2de0}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef0e8 sp=0xc0325ef0b0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0123fe060}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef120 sp=0xc0325ef0e8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0121c0800}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef158 sp=0xc0325ef120 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01250c230}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef190 sp=0xc0325ef158 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0120681e0}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef1c8 sp=0xc0325ef190 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0124ac9f0}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef200 sp=0xc0325ef1c8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01240e160}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef238 sp=0xc0325ef200 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc000bf2720}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef270 sp=0xc0325ef238 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0120727e0}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef2a8 sp=0xc0325ef270 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011f91120}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef2e0 sp=0xc0325ef2a8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011fa2e40}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef318 sp=0xc0325ef2e0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011fa2de0}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef350 sp=0xc0325ef318 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc000bf2de0}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef388 sp=0xc0325ef350 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0123fe060}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef3c0 sp=0xc0325ef388 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0121c0800}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef3f8 sp=0xc0325ef3c0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01250c230}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef430 sp=0xc0325ef3f8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0120681e0}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef468 sp=0xc0325ef430 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0124ac9f0}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef4a0 sp=0xc0325ef468 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01240e160}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef4d8 sp=0xc0325ef4a0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc000bf2720}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef510 sp=0xc0325ef4d8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0120727e0}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef548 sp=0xc0325ef510 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011f91120}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef580 sp=0xc0325ef548 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011fa2e40}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef5b8 sp=0xc0325ef580 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011fa2de0}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef5f0 sp=0xc0325ef5b8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc000bf2de0}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef628 sp=0xc0325ef5f0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0123fe060}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef660 sp=0xc0325ef628 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0121c0800}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef698 sp=0xc0325ef660 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01250c230}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef6d0 sp=0xc0325ef698 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0120681e0}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef708 sp=0xc0325ef6d0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0124ac9f0}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef740 sp=0xc0325ef708 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01240e160}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef778 sp=0xc0325ef740 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc000bf2720}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef7b0 sp=0xc0325ef778 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0120727e0}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef7e8 sp=0xc0325ef7b0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011f91120}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef820 sp=0xc0325ef7e8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011fa2e40}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef858 sp=0xc0325ef820 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011fa2de0}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef890 sp=0xc0325ef858 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc000bf2de0}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef8c8 sp=0xc0325ef890 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0123fe060}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef900 sp=0xc0325ef8c8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0121c0800}, {0x4012e60, 0xc011fa2e40})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0325ef938 sp=0xc0325ef900 pc=0x1f577a5
   > ...additional frames elided...
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:712 +0x22d
   > goroutine 1 [chan receive]:
   > runtime.gopark(0xc0106a9180?, 0xc0111f1dc0?, 0xbf?, 0xc1?, 0x37fc5c0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0111f1d40 sp=0xc0111f1d20 pc=0x13bb516
   > runtime.chanrecv(0xc01120a480, 0xc0111f1e30, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc0111f1dd0 sp=0xc0111f1d40 pc=0x13854bb
   > runtime.chanrecv1(0xc010515ba0?, 0x0?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc0111f1df8 sp=0xc0111f1dd0 pc=0x1384fb8
   > github.com/pingcap/tidb/server.(*Server).Run(0xc010515ba0)
   > 	/go/src/github.com/pingcap/tidb/server/server.go:370 +0x1f0 fp=0xc0111f1e50 sp=0xc0111f1df8 pc=0x31e23d0
   > main.main()
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:213 +0x539 fp=0xc0111f1f80 sp=0xc0111f1e50 pc=0x33af4b9
   > runtime.main()
   > 	/usr/local/go/src/runtime/proc.go:250 +0x212 fp=0xc0111f1fe0 sp=0xc0111f1f80 pc=0x13bb152
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0111f1fe8 sp=0xc0111f1fe0 pc=0x13ee6e1
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
   > goroutine 18 [GC sweep wait]:
   > runtime.gopark(0x1?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008a790 sp=0xc00008a770 pc=0x13bb516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.bgsweep(0x0?)
   > 	/usr/local/go/src/runtime/mgcsweep.go:297 +0xd7 fp=0xc00008a7c8 sp=0xc00008a790 pc=0x13a4337
   > runtime.gcenable.func1()
   > 	/usr/local/go/src/runtime/mgc.go:178 +0x26 fp=0xc00008a7e0 sp=0xc00008a7c8 pc=0x1398e06
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008a7e8 sp=0xc00008a7e0 pc=0x13ee6e1
   > created by runtime.gcenable
   > 	/usr/local/go/src/runtime/mgc.go:178 +0x6b
   > goroutine 19 [GC scavenge wait]:
   > runtime.gopark(0xc00010e000?, 0x3fe2f28?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008af70 sp=0xc00008af50 pc=0x13bb516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.(*scavengerState).park(0x5f57220)
   > 	/usr/local/go/src/runtime/mgcscavenge.go:389 +0x53 fp=0xc00008afa0 sp=0xc00008af70 pc=0x13a2313
   > runtime.bgscavenge(0x0?)
   > 	/usr/local/go/src/runtime/mgcscavenge.go:622 +0x65 fp=0xc00008afc8 sp=0xc00008afa0 pc=0x13a2925
   > runtime.gcenable.func2()
   > 	/usr/local/go/src/runtime/mgc.go:179 +0x26 fp=0xc00008afe0 sp=0xc00008afc8 pc=0x1398da6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008afe8 sp=0xc00008afe0 pc=0x13ee6e1
   > created by runtime.gcenable
   > 	/usr/local/go/src/runtime/mgc.go:179 +0xaa
   > goroutine 3 [finalizer wait]:
   > runtime.gopark(0x5f58620?, 0xc000007520?, 0x0?, 0x0?, 0xc00008e770?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008e628 sp=0xc00008e608 pc=0x13bb516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.runfinq()
   > 	/usr/local/go/src/runtime/mfinal.go:180 +0x10f fp=0xc00008e7e0 sp=0xc00008e628 pc=0x1397f0f
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008e7e8 sp=0xc00008e7e0 pc=0x13ee6e1
   > created by runtime.createfing
   > 	/usr/local/go/src/runtime/mfinal.go:157 +0x45
   > goroutine 4 [GC worker (idle)]:
   > runtime.gopark(0x0?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008f750 sp=0xc00008f730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008f7e0 sp=0xc00008f750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008f7e8 sp=0xc00008f7e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 20 [GC worker (idle)]:
   > runtime.gopark(0x0?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008b750 sp=0xc00008b730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008b7e0 sp=0xc00008b750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008b7e8 sp=0xc00008b7e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 34 [GC worker (idle)]:
   > runtime.gopark(0x3fbeca0dee7e?, 0x1?, 0xaf?, 0x72?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000506750 sp=0xc000506730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0005067e0 sp=0xc000506750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0005067e8 sp=0xc0005067e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 21 [GC worker (idle)]:
   > runtime.gopark(0x3fbeca0da403?, 0x3?, 0xce?, 0xf4?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008bf50 sp=0xc00008bf30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008bfe0 sp=0xc00008bf50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008bfe8 sp=0xc00008bfe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 35 [GC worker (idle)]:
   > runtime.gopark(0x3fbeca19075f?, 0x3?, 0x5f?, 0xd?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000506f50 sp=0xc000506f30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc000506fe0 sp=0xc000506f50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000506fe8 sp=0xc000506fe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 5 [GC worker (idle)]:
   > runtime.gopark(0x3fbeca1bd870?, 0x1?, 0x28?, 0xef?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008ff50 sp=0xc00008ff30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008ffe0 sp=0xc00008ff50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008ffe8 sp=0xc00008ffe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 6 [GC worker (idle)]:
   > runtime.gopark(0x3fbeca0d9e8e?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000090750 sp=0xc000090730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0000907e0 sp=0xc000090750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000907e8 sp=0xc0000907e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 22 [GC worker (idle)]:
   > runtime.gopark(0x3fbeca0dee7e?, 0x3?, 0xc8?, 0x52?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008c750 sp=0xc00008c730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008c7e0 sp=0xc00008c750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008c7e8 sp=0xc00008c7e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 36 [GC worker (idle)]:
   > runtime.gopark(0x3fbeca0dee7e?, 0x3?, 0x9c?, 0xe9?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000507750 sp=0xc000507730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0005077e0 sp=0xc000507750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0005077e8 sp=0xc0005077e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 37 [GC worker (idle)]:
   > runtime.gopark(0x3fbeca0de8c3?, 0x3?, 0xd3?, 0x5e?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000507f50 sp=0xc000507f30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc000507fe0 sp=0xc000507f50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000507fe8 sp=0xc000507fe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 7 [GC worker (idle)]:
   > runtime.gopark(0x5f8be00?, 0x3?, 0xf6?, 0x94?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000090f50 sp=0xc000090f30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc000090fe0 sp=0xc000090f50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000090fe8 sp=0xc000090fe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 23 [GC worker (idle)]:
   > runtime.gopark(0x3fbeca2097da?, 0x1?, 0x20?, 0x67?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008cf50 sp=0xc00008cf30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008cfe0 sp=0xc00008cf50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008cfe8 sp=0xc00008cfe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 24 [GC worker (idle)]:
   > runtime.gopark(0x5f8be00?, 0x1?, 0x28?, 0xfa?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008d750 sp=0xc00008d730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008d7e0 sp=0xc00008d750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008d7e8 sp=0xc00008d7e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 38 [GC worker (idle)]:
   > runtime.gopark(0x3fbeca0de8c3?, 0x3?, 0x4e?, 0xad?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000508750 sp=0xc000508730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0005087e0 sp=0xc000508750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0005087e8 sp=0xc0005087e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 39 [GC worker (idle)]:
   > runtime.gopark(0x3fbeca0dd44d?, 0x3?, 0x39?, 0xd8?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000508f50 sp=0xc000508f30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc000508fe0 sp=0xc000508f50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000508fe8 sp=0xc000508fe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 25 [GC worker (idle)]:
   > runtime.gopark(0x3fbeb83e1c9e?, 0x3?, 0x10?, 0xbb?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008df50 sp=0xc00008df30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008dfe0 sp=0xc00008df50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008dfe8 sp=0xc00008dfe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 16 [select]:
   > runtime.gopark(0xc000504788?, 0x3?, 0x48?, 0xab?, 0xc000504772?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0005045f8 sp=0xc0005045d8 pc=0x13bb516
   > runtime.selectgo(0xc000504788, 0xc00050476c, 0xc00077b680?, 0x0, 0xc000504788?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000504738 sp=0xc0005045f8 pc=0x13cbbdc
   > go.opencensus.io/stats/view.(*worker).start(0xc00077b680)
   > 	/go/pkg/mod/go.opencensus.io@v0.23.0/stats/view/worker.go:276 +0xad fp=0xc0005047c8 sp=0xc000504738 pc=0x29900cd
   > go.opencensus.io/stats/view.init.0.func1()
   > 	/go/pkg/mod/go.opencensus.io@v0.23.0/stats/view/worker.go:34 +0x26 fp=0xc0005047e0 sp=0xc0005047c8 pc=0x298f346
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0005047e8 sp=0xc0005047e0 pc=0x13ee6e1
   > created by go.opencensus.io/stats/view.init.0
   > 	/go/pkg/mod/go.opencensus.io@v0.23.0/stats/view/worker.go:34 +0x8d
   > goroutine 126 [chan receive]:
   > runtime.gopark(0xc0005660c0?, 0x13c1374?, 0x10?, 0x3e?, 0x13d8de5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000503db8 sp=0xc000503d98 pc=0x13bb516
   > runtime.chanrecv(0xc000566060, 0xc000503f28, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000503e48 sp=0xc000503db8 pc=0x13854bb
   > runtime.chanrecv2(0x3b9aca00?, 0x13bb600?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc000503e70 sp=0xc000503e48 pc=0x1384ff8
   > go.etcd.io/etcd/pkg/logutil.(*MergeLogger).outputLoop(0xc0000133e0)
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:173 +0x8c fp=0xc000503fc8 sp=0xc000503e70 pc=0x1a12c4c
   > go.etcd.io/etcd/pkg/logutil.NewMergeLogger.func1()
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:91 +0x26 fp=0xc000503fe0 sp=0xc000503fc8 pc=0x1a124c6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000503fe8 sp=0xc000503fe0 pc=0x13ee6e1
   > created by go.etcd.io/etcd/pkg/logutil.NewMergeLogger
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:91 +0xb6
   > goroutine 167 [chan receive]:
   > runtime.gopark(0xc0005664e0?, 0x1?, 0x10?, 0x4e?, 0x13d8de5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000504db8 sp=0xc000504d98 pc=0x13bb516
   > runtime.chanrecv(0xc000566480, 0xc000504f28, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000504e48 sp=0xc000504db8 pc=0x13854bb
   > runtime.chanrecv2(0x3b9aca00?, 0x13bb600?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc000504e70 sp=0xc000504e48 pc=0x1384ff8
   > go.etcd.io/etcd/pkg/logutil.(*MergeLogger).outputLoop(0xc000013908)
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:173 +0x8c fp=0xc000504fc8 sp=0xc000504e70 pc=0x1a12c4c
   > go.etcd.io/etcd/pkg/logutil.NewMergeLogger.func1()
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:91 +0x26 fp=0xc000504fe0 sp=0xc000504fc8 pc=0x1a124c6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000504fe8 sp=0xc000504fe0 pc=0x13ee6e1
   > created by go.etcd.io/etcd/pkg/logutil.NewMergeLogger
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:91 +0xb6
   > goroutine 170 [chan receive]:
   > runtime.gopark(0xc000114180?, 0x0?, 0x10?, 0x56?, 0x13d8de5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0005055b8 sp=0xc000505598 pc=0x13bb516
   > runtime.chanrecv(0xc000950360, 0xc000505728, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000505648 sp=0xc0005055b8 pc=0x13854bb
   > runtime.chanrecv2(0x3b9aca00?, 0x13bb600?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc000505670 sp=0xc000505648 pc=0x1384ff8
   > go.etcd.io/etcd/pkg/logutil.(*MergeLogger).outputLoop(0xc000013a40)
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:173 +0x8c fp=0xc0005057c8 sp=0xc000505670 pc=0x1a12c4c
   > go.etcd.io/etcd/pkg/logutil.NewMergeLogger.func1()
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:91 +0x26 fp=0xc0005057e0 sp=0xc0005057c8 pc=0x1a124c6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0005057e8 sp=0xc0005057e0 pc=0x13ee6e1
   > created by go.etcd.io/etcd/pkg/logutil.NewMergeLogger
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:91 +0xb6
   > goroutine 439 [chan receive]:
   > runtime.gopark(0x379c3fc5b8?, 0xc0009fcea0?, 0x78?, 0xfe?, 0x13d8de5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00009fe20 sp=0xc00009fe00 pc=0x13bb516
   > runtime.chanrecv(0xc000e3b080, 0x0, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc00009feb0 sp=0xc00009fe20 pc=0x13854bb
   > runtime.chanrecv1(0xdf8475800?, 0x1b?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc00009fed8 sp=0xc00009feb0 pc=0x1384fb8
   > github.com/pingcap/tidb/util/profile.HeapProfileForGlobalMemTracker(0xc000d59860?)
   > 	/go/src/github.com/pingcap/tidb/util/profile/trackerRecorder.go:33 +0xa7 fp=0xc00009ffc8 sp=0xc00009fed8 pc=0x267adc7
   > main.setHeapProfileTracker.func1()
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:279 +0x26 fp=0xc00009ffe0 sp=0xc00009ffc8 pc=0x33afc46
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00009ffe8 sp=0xc00009ffe0 pc=0x13ee6e1
   > created by main.setHeapProfileTracker
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:279 +0xa5
   > goroutine 441 [select]:
   > runtime.gopark(0xc000d35f80?, 0x2?, 0x10?, 0x0?, 0xc000d35f4c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000d35dd0 sp=0xc000d35db0 pc=0x13bb516
   > runtime.selectgo(0xc000d35f80, 0xc000d35f48, 0xc000d2e3b8?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000d35f10 sp=0xc000d35dd0 pc=0x13cbbdc
   > github.com/pingcap/badger.(*DB).updateSize(0x0?, 0xc000d4dd40)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:1039 +0x105 fp=0xc000d35fc0 sp=0xc000d35f10 pc=0x329a445
   > github.com/pingcap/badger.Open.func5()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:328 +0x2a fp=0xc000d35fe0 sp=0xc000d35fc0 pc=0x329450a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000d35fe8 sp=0xc000d35fe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.Open
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:328 +0xf5c
   > goroutine 440 [chan receive]:
   > runtime.gopark(0xc000e3b140?, 0x13c1374?, 0x38?, 0x1e?, 0x13d8de5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0000a1de0 sp=0xc0000a1dc0 pc=0x13bb516
   > runtime.chanrecv(0xc000e3b0e0, 0x0, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc0000a1e70 sp=0xc0000a1de0 pc=0x13854bb
   > runtime.chanrecv1(0x5f5e100?, 0x3ace4e4?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc0000a1e98 sp=0xc0000a1e70 pc=0x1384fb8
   > github.com/pingcap/tidb/util/systimemon.StartMonitor(0x3bccd98, 0x3bcc3f0, 0xc000d5eaa0)
   > 	/go/src/github.com/pingcap/tidb/util/systimemon/systime_mon.go:32 +0x185 fp=0xc0000a1fb8 sp=0xc0000a1e98 pc=0x33ac665
   > main.setupMetrics.func3()
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:696 +0x31 fp=0xc0000a1fe0 sp=0xc0000a1fb8 pc=0x33b2df1
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000a1fe8 sp=0xc0000a1fe0 pc=0x13ee6e1
   > created by main.setupMetrics
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:696 +0x115
   > goroutine 442 [select]:
   > runtime.gopark(0xc000d36788?, 0x2?, 0x8?, 0x0?, 0xc000d36764?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000d365e8 sp=0xc000d365c8 pc=0x13bb516
   > runtime.selectgo(0xc000d36788, 0xc000d36760, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000d36728 sp=0xc000d365e8 pc=0x13cbbdc
   > github.com/pingcap/badger/epoch.(*ResourceManager).collectLoop(0x0?, 0xc000d4dd70)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/epoch/manager.go:101 +0xd3 fp=0xc000d367c0 sp=0xc000d36728 pc=0x3257a13
   > github.com/pingcap/badger/epoch.NewResourceManager.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/epoch/manager.go:79 +0x2a fp=0xc000d367e0 sp=0xc000d367c0 pc=0x32577aa
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000d367e8 sp=0xc000d367e0 pc=0x13ee6e1
   > created by github.com/pingcap/badger/epoch.NewResourceManager
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/epoch/manager.go:79 +0xdd
   > goroutine 443 [select]:
   > runtime.gopark(0xc000f3fe68?, 0x2?, 0x8?, 0xc1?, 0xc000f3fe3c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000f3fcc0 sp=0xc000f3fca0 pc=0x13bb516
   > runtime.selectgo(0xc000f3fe68, 0xc000f3fe38, 0x0?, 0x1, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000f3fe00 sp=0xc000f3fcc0 pc=0x13cbbdc
   > github.com/pingcap/badger.Open.func4()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:342 +0x155 fp=0xc000f3ffe0 sp=0xc000f3fe00 pc=0x3294495
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000f3ffe8 sp=0xc000f3ffe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.Open
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:339 +0x11f8
   > goroutine 358 [select]:
   > runtime.gopark(0xc000509708?, 0x2?, 0x0?, 0x0?, 0xc0005096e4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0000a3d68 sp=0xc0000a3d48 pc=0x13bb516
   > runtime.selectgo(0xc0000a3f08, 0xc0005096e0, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0000a3ea8 sp=0xc0000a3d68 pc=0x13cbbdc
   > github.com/pingcap/badger.(*blobGCHandler).run(0xc000527900, 0xc000012168)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/blob.go:468 +0xd6 fp=0xc0000a3fc0 sp=0xc0000a3ea8 pc=0x3288896
   > github.com/pingcap/badger.(*blobManager).Open.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/blob.go:292 +0x2a fp=0xc0000a3fe0 sp=0xc0000a3fc0 pc=0x328754a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000a3fe8 sp=0xc0000a3fe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.(*blobManager).Open
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/blob.go:292 +0x5bd
   > goroutine 359 [select]:
   > runtime.gopark(0xc000509f60?, 0x2?, 0x3?, 0x30?, 0xc000509f2c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000509d98 sp=0xc000509d78 pc=0x13bb516
   > runtime.selectgo(0xc000509f60, 0xc000509f28, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000509ed8 sp=0xc000509d98 pc=0x13cbbdc
   > github.com/pingcap/badger.(*levelsController).runWorker(0xc0001c3ea0, 0xc0000121b0, 0x0)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:212 +0x1fb fp=0xc000509fb8 sp=0xc000509ed8 pc=0x32a297b
   > github.com/pingcap/badger.(*levelsController).startCompact.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:180 +0x2e fp=0xc000509fe0 sp=0xc000509fb8 pc=0x32a274e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000509fe8 sp=0xc000509fe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.(*levelsController).startCompact
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:180 +0x65
   > goroutine 360 [select]:
   > runtime.gopark(0xc000505f60?, 0x2?, 0x3?, 0x30?, 0xc000505f2c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000505d98 sp=0xc000505d78 pc=0x13bb516
   > runtime.selectgo(0xc000505f60, 0xc000505f28, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000505ed8 sp=0xc000505d98 pc=0x13cbbdc
   > github.com/pingcap/badger.(*levelsController).runWorker(0xc0001c3ea0, 0xc0000121b0, 0x0)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:212 +0x1fb fp=0xc000505fb8 sp=0xc000505ed8 pc=0x32a297b
   > github.com/pingcap/badger.(*levelsController).startCompact.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:180 +0x2e fp=0xc000505fe0 sp=0xc000505fb8 pc=0x32a274e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000505fe8 sp=0xc000505fe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.(*levelsController).startCompact
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:180 +0x65
   > goroutine 361 [select]:
   > runtime.gopark(0xc000502760?, 0x2?, 0x4?, 0x30?, 0xc00050272c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000502598 sp=0xc000502578 pc=0x13bb516
   > runtime.selectgo(0xc000502760, 0xc000502728, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0005026d8 sp=0xc000502598 pc=0x13cbbdc
   > github.com/pingcap/badger.(*levelsController).runWorker(0xc0001c3ea0, 0xc0000121b0, 0x1)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:212 +0x1fb fp=0xc0005027b8 sp=0xc0005026d8 pc=0x32a297b
   > github.com/pingcap/badger.(*levelsController).startCompact.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:180 +0x2e fp=0xc0005027e0 sp=0xc0005027b8 pc=0x32a274e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0005027e8 sp=0xc0005027e0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.(*levelsController).startCompact
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:180 +0x65
   > goroutine 362 [chan receive]:
   > runtime.gopark(0x0?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000f3cac0 sp=0xc000f3caa0 pc=0x13bb516
   > runtime.chanrecv(0xc000d7a5a0, 0xc000f3cc60, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000f3cb50 sp=0xc000f3cac0 pc=0x13854bb
   > runtime.chanrecv2(0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc000f3cb78 sp=0xc000f3cb50 pc=0x1384ff8
   > github.com/pingcap/badger.(*DB).runFlushMemTable(0xc000f13200, 0x0?)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:920 +0xdd fp=0xc000f3cfc0 sp=0xc000f3cb78 pc=0x3298efd
   > github.com/pingcap/badger.Open.func6()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:361 +0x2a fp=0xc000f3cfe0 sp=0xc000f3cfc0 pc=0x329430a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000f3cfe8 sp=0xc000f3cfe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.Open
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:361 +0x158d
   > goroutine 363 [select]:
   > runtime.gopark(0xc000f3af78?, 0x3?, 0x25?, 0x48?, 0xc000f3af32?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000f3ad98 sp=0xc000f3ad78 pc=0x13bb516
   > runtime.selectgo(0xc000f3af78, 0xc000f3af2c, 0x1?, 0x0, 0xc0009fc340?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000f3aed8 sp=0xc000f3ad98 pc=0x13cbbdc
   > github.com/pingcap/badger.(*writeWorker).runWriteVLog(0xc000d76060, 0xc000f34018)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:94 +0x137 fp=0xc000f3afc0 sp=0xc000f3aed8 pc=0x32b28b7
   > github.com/pingcap/badger.startWriteWorker.func2()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:64 +0x2a fp=0xc000f3afe0 sp=0xc000f3afc0 pc=0x32b238a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000f3afe8 sp=0xc000f3afe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.startWriteWorker
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:64 +0x1f9
   > goroutine 364 [chan receive, locked to thread]:
   > runtime.gopark(0xc00009ce98?, 0x1456628?, 0xf?, 0x0?, 0x1?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00009ce68 sp=0xc00009ce48 pc=0x13bb516
   > runtime.chanrecv(0xc000e3a8a0, 0xc00009cf88, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc00009cef8 sp=0xc00009ce68 pc=0x13854bb
   > runtime.chanrecv2(0xc000f16360?, 0x3ef01c82c2928c34?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc00009cf20 sp=0xc00009cef8 pc=0x1384ff8
   > github.com/pingcap/badger.(*writeWorker).runWriteLSM(0xc000d76060, 0xc0000124c8?)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:141 +0x15e fp=0xc00009cfc0 sp=0xc00009cf20 pc=0x32b2efe
   > github.com/pingcap/badger.startWriteWorker.func3()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:65 +0x2a fp=0xc00009cfe0 sp=0xc00009cfc0 pc=0x32b232a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00009cfe8 sp=0xc00009cfe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.startWriteWorker
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:65 +0x24d
   > goroutine 365 [chan receive]:
   > runtime.gopark(0x0?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000f4aea8 sp=0xc000f4ae88 pc=0x13bb516
   > runtime.chanrecv(0xc000e3a900, 0xc000f4af88, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000f4af38 sp=0xc000f4aea8 pc=0x13854bb
   > runtime.chanrecv2(0xc00085cca0?, 0xc000d31fa8?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc000f4af60 sp=0xc000f4af38 pc=0x1384ff8
   > github.com/pingcap/badger.(*writeWorker).runMergeLSM(0x3bcc3f0?, 0xc000d5eaa0?)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:154 +0x9b fp=0xc000f4afc0 sp=0xc000f4af60 pc=0x32b307b
   > github.com/pingcap/badger.startWriteWorker.func4()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:66 +0x2a fp=0xc000f4afe0 sp=0xc000f4afc0 pc=0x32b22ca
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000f4afe8 sp=0xc000f4afe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.startWriteWorker
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:66 +0x2a5
   > goroutine 366 [select]:
   > runtime.gopark(0xc00009df88?, 0x2?, 0x0?, 0x0?, 0xc00009df4c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00009dda0 sp=0xc00009dd80 pc=0x13bb516
   > runtime.selectgo(0xc00009df88, 0xc00009df48, 0xc0005bf0d0?, 0x0, 0x3?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00009dee0 sp=0xc00009dda0 pc=0x13cbbdc
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.writeDBWorker.run({0xc000e3a9c0?, 0xc000527f40?})
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:96 +0x145 fp=0xc00009dfc0 sp=0xc00009dee0 pc=0x3308de5
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*dbWriter).Open.func1()
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:202 +0x2a fp=0xc00009dfe0 sp=0xc00009dfc0 pc=0x330996a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00009dfe8 sp=0xc00009dfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*dbWriter).Open
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:199 +0xc5
   > goroutine 367 [select]:
   > runtime.gopark(0xc000f4ee70?, 0x2?, 0x90?, 0xee?, 0xc000f4ee1c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000f4ec58 sp=0xc000f4ec38 pc=0x13bb516
   > runtime.selectgo(0xc000f4ee70, 0xc000f4ee18, 0x13?, 0x0, 0xc000d87900?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000f4ed98 sp=0xc000f4ec58 pc=0x13cbbdc
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.writeLockWorker.run({0xc000e3aa20?, 0xc000527f40?})
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:148 +0x15f fp=0xc000f4efc0 sp=0xc000f4ed98 pc=0x33093bf
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*dbWriter).Open.func2()
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:209 +0x2a fp=0xc000f4efe0 sp=0xc000f4efc0 pc=0x330990a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000f4efe8 sp=0xc000f4efe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*dbWriter).Open
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:206 +0x159
   > goroutine 368 [select]:
   > runtime.gopark(0xc000d37f18?, 0x2?, 0x0?, 0x0?, 0xc000d37f04?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000d37d88 sp=0xc000d37d68 pc=0x13bb516
   > runtime.selectgo(0xc000d37f18, 0xc000d37f00, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000d37ec8 sp=0xc000d37d88 pc=0x13cbbdc
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*MVCCStore).runUpdateSafePointLoop(0xc00016c000)
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:1550 +0x217 fp=0xc000d37fc8 sp=0xc000d37ec8 pc=0x32facd7
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.NewMVCCStore.func1()
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:85 +0x26 fp=0xc000d37fe0 sp=0xc000d37fc8 pc=0x32ed406
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000d37fe8 sp=0xc000d37fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.NewMVCCStore
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:85 +0x337
   > goroutine 369 [select]:
   > runtime.gopark(0xc000d327b0?, 0x2?, 0x0?, 0x0?, 0xc000d3279c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000d32628 sp=0xc000d32608 pc=0x13bb516
   > runtime.selectgo(0xc000d327b0, 0xc000d32798, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000d32768 sp=0xc000d32628 pc=0x13cbbdc
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*MVCCStore).StartDeadlockDetection.func1()
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:1286 +0x7b fp=0xc000d327e0 sp=0xc000d32768 pc=0x32f895b
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000d327e8 sp=0xc000d327e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*MVCCStore).StartDeadlockDetection
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:1284 +0xb6
   > goroutine 466 [select]:
   > runtime.gopark(0xc000c80f78?, 0x2?, 0x0?, 0x0?, 0xc000c80f3c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000c80dc0 sp=0xc000c80da0 pc=0x13bb516
   > runtime.selectgo(0xc000c80f78, 0xc000c80f38, 0xc000d347b0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000c80f00 sp=0xc000c80dc0 pc=0x13cbbdc
   > github.com/tikv/client-go/v2/oracle/oracles.(*pdOracle).updateTS(0xc000776620, {0x400d640, 0xc000058058}, 0xc0000124c8?)
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/oracle/oracles/pd.go:229 +0x128 fp=0xc000c80fb0 sp=0xc000c80f00 pc=0x1e9b548
   > github.com/tikv/client-go/v2/oracle/oracles.NewPdOracle.func1()
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/oracle/oracles/pd.go:77 +0x32 fp=0xc000c80fe0 sp=0xc000c80fb0 pc=0x1e9a772
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000c80fe8 sp=0xc000c80fe0 pc=0x13ee6e1
   > created by github.com/tikv/client-go/v2/oracle/oracles.NewPdOracle
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/oracle/oracles/pd.go:77 +0x119
   > goroutine 467 [select]:
   > runtime.gopark(0xc000d32f78?, 0x3?, 0x8?, 0x0?, 0xc000d32f5a?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000d32de0 sp=0xc000d32dc0 pc=0x13bb516
   > runtime.selectgo(0xc000d32f78, 0xc000d32f54, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000d32f20 sp=0xc000d32de0 pc=0x13cbbdc
   > github.com/tikv/client-go/v2/internal/locate.(*RegionCache).asyncCheckAndResolveLoop(0xc00016de00, 0x0?)
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/internal/locate/region_cache.go:399 +0xd1 fp=0xc000d32fc0 sp=0xc000d32f20 pc=0x1e6bff1
   > github.com/tikv/client-go/v2/internal/locate.NewRegionCache.func1()
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/internal/locate/region_cache.go:370 +0x2a fp=0xc000d32fe0 sp=0xc000d32fc0 pc=0x1e6bc6a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000d32fe8 sp=0xc000d32fe0 pc=0x13ee6e1
   > created by github.com/tikv/client-go/v2/internal/locate.NewRegionCache
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/internal/locate/region_cache.go:370 +0x2e6
   > goroutine 468 [select]:
   > runtime.gopark(0xc000d33710?, 0x2?, 0x11?, 0x30?, 0xc000d336ac?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000f4bd10 sp=0xc000f4bcf0 pc=0x13bb516
   > runtime.selectgo(0xc000f4bf10, 0xc000d336a8, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000f4be50 sp=0xc000f4bd10 pc=0x13cbbdc
   > github.com/tikv/client-go/v2/tikv.(*KVStore).runSafePointChecker(0xc000e3c000)
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/tikv/kv.go:264 +0x12b fp=0xc000f4bfc8 sp=0xc000f4be50 pc=0x1ed6f0b
   > github.com/tikv/client-go/v2/tikv.NewKVStore.func1()
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/tikv/kv.go:187 +0x26 fp=0xc000f4bfe0 sp=0xc000f4bfc8 pc=0x1ed6d06
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000f4bfe8 sp=0xc000f4bfe0 pc=0x13ee6e1
   > created by github.com/tikv/client-go/v2/tikv.NewKVStore
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/tikv/kv.go:187 +0x3d6
   > goroutine 469 [select]:
   > runtime.gopark(0xc000f3ef80?, 0x2?, 0x0?, 0xbe?, 0xc000f3ef44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000f3edc8 sp=0xc000f3eda8 pc=0x13bb516
   > runtime.selectgo(0xc000f3ef80, 0xc000f3ef40, 0xc0000fa700?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000f3ef08 sp=0xc000f3edc8 pc=0x13cbbdc
   > github.com/tikv/client-go/v2/tikv.(*KVStore).safeTSUpdater(0xc000e3c000)
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/tikv/kv.go:544 +0x165 fp=0xc000f3efc8 sp=0xc000f3ef08 pc=0x1ed8e65
   > github.com/tikv/client-go/v2/tikv.NewKVStore.func2()
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/tikv/kv.go:188 +0x26 fp=0xc000f3efe0 sp=0xc000f3efc8 pc=0x1ed6ca6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000f3efe8 sp=0xc000f3efe0 pc=0x13ee6e1
   > created by github.com/tikv/client-go/v2/tikv.NewKVStore
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/tikv/kv.go:188 +0x416
   > goroutine 470 [select]:
   > runtime.gopark(0xc000e73f98?, 0x2?, 0x0?, 0x0?, 0xc000e73f6c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000e73de8 sp=0xc000e73dc8 pc=0x13bb516
   > runtime.selectgo(0xc000e73f98, 0xc000e73f68, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000e73f28 sp=0xc000e73de8 pc=0x13cbbdc
   > github.com/dgraph-io/ristretto.(*defaultPolicy).processItems(0xc000544630)
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.0.1/policy.go:96 +0x91 fp=0xc000e73fc8 sp=0xc000e73f28 pc=0x23cf0d1
   > github.com/dgraph-io/ristretto.newDefaultPolicy.func1()
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.0.1/policy.go:80 +0x26 fp=0xc000e73fe0 sp=0xc000e73fc8 pc=0x23cef86
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000e73fe8 sp=0xc000e73fe0 pc=0x13ee6e1
   > created by github.com/dgraph-io/ristretto.newDefaultPolicy
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.0.1/policy.go:80 +0x156
   > goroutine 471 [select]:
   > runtime.gopark(0xc000e74798?, 0x2?, 0x0?, 0x0?, 0xc000e74774?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000e745f0 sp=0xc000e745d0 pc=0x13bb516
   > runtime.selectgo(0xc000e74798, 0xc000e74770, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000e74730 sp=0xc000e745f0 pc=0x13cbbdc
   > github.com/dgraph-io/ristretto.(*Cache).processItems(0xc000e3ade0)
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.0.1/cache.go:257 +0x85 fp=0xc000e747c8 sp=0xc000e74730 pc=0x23ce025
   > github.com/dgraph-io/ristretto.NewCache.func2()
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.0.1/cache.go:155 +0x26 fp=0xc000e747e0 sp=0xc000e747c8 pc=0x23cd846
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000e747e8 sp=0xc000e747e0 pc=0x13ee6e1
   > created by github.com/dgraph-io/ristretto.NewCache
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.0.1/cache.go:155 +0x485
   > goroutine 817 [select]:
   > runtime.gopark(0xc00fc13740?, 0x2?, 0x2?, 0x0?, 0xc00fc13704?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fc13588 sp=0xc00fc13568 pc=0x13bb516
   > runtime.selectgo(0xc00fc13740, 0xc00fc13700, 0x1ec360b?, 0x0, 0x1000000000001?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fc136c8 sp=0xc00fc13588 pc=0x13cbbdc
   > github.com/pingcap/tidb/util/topsql/reporter.(*RemoteTopSQLReporter).reportWorker(0xc00022d650)
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:499 +0x1ae fp=0xc00fc137c8 sp=0xc00fc136c8 pc=0x254924e
   > github.com/pingcap/tidb/util/topsql/reporter.NewRemoteTopSQLReporter.func2()
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:161 +0x26 fp=0xc00fc137e0 sp=0xc00fc137c8 pc=0x2546bc6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fc137e8 sp=0xc00fc137e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/util/topsql/reporter.NewRemoteTopSQLReporter
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:161 +0x1f6
   > goroutine 728 [select]:
   > runtime.gopark(0xc010f49f58?, 0x4?, 0xab?, 0x62?, 0xc010f49da8?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010f49bf8 sp=0xc010f49bd8 pc=0x13bb516
   > runtime.selectgo(0xc010f49f58, 0xc010f49da0, 0xc000c86e38?, 0x0, 0x1?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010f49d38 sp=0xc010f49bf8 pc=0x13cbbdc
   > github.com/pingcap/tidb/ddl.(*worker).start(0xc010d328f0, 0xc010c7d740)
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl_worker.go:178 +0x318 fp=0xc010f49fc0 sp=0xc010f49d38 pc=0x2622e98
   > github.com/pingcap/tidb/ddl.(*ddl).Start.func2()
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:369 +0x2a fp=0xc010f49fe0 sp=0xc010f49fc0 pc=0x25e9a6a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010f49fe8 sp=0xc010f49fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/ddl.(*ddl).Start
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:369 +0x5c5
   > goroutine 732 [select]:
   > runtime.gopark(0xc0103c7ef8?, 0x3?, 0x4?, 0x30?, 0xc0103c7e82?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0103c7d08 sp=0xc0103c7ce8 pc=0x13bb516
   > runtime.selectgo(0xc0103c7ef8, 0xc0103c7e7c, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0103c7e48 sp=0xc0103c7d08 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).infoSyncerKeeper(0xc0005dcb40)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:487 +0x165 fp=0xc0103c7fc8 sp=0xc0103c7e48 pc=0x269ee45
   > github.com/pingcap/tidb/domain.(*Domain).Init.func12()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:829 +0x26 fp=0xc0103c7fe0 sp=0xc0103c7fc8 pc=0x26a2a66
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0103c7fe8 sp=0xc0103c7fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:829 +0xe95
   > goroutine 730 [select]:
   > runtime.gopark(0xc010575f50?, 0x4?, 0x4?, 0x30?, 0xc010575d00?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010575b78 sp=0xc010575b58 pc=0x13bb516
   > runtime.selectgo(0xc010575f50, 0xc010575cf8, 0x400ccd0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010575cb8 sp=0xc010575b78 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).loadSchemaInLoop(0xc0005dcb40, {0x400d608, 0xc0005c2740}, 0xc00fc0e538?)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:565 +0x1aa fp=0xc010575fb0 sp=0xc010575cb8 pc=0x26a00aa
   > github.com/pingcap/tidb/domain.(*Domain).Init.func10()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:825 +0x32 fp=0xc010575fe0 sp=0xc010575fb0 pc=0x26a2b32
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010575fe8 sp=0xc010575fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:825 +0xdeb
   > goroutine 731 [select]:
   > runtime.gopark(0xc00fc0ff78?, 0x3?, 0x4?, 0x30?, 0xc00fc0ff12?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fc0fd60 sp=0xc00fc0fd40 pc=0x13bb516
   > runtime.selectgo(0xc00fc0ff78, 0xc00fc0ff0c, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fc0fea0 sp=0xc00fc0fd60 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).topNSlowQueryLoop(0xc0005dcb40)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:455 +0x194 fp=0xc00fc0ffc8 sp=0xc00fc0fea0 pc=0x269e914
   > github.com/pingcap/tidb/domain.(*Domain).Init.func11()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:828 +0x26 fp=0xc00fc0ffe0 sp=0xc00fc0ffc8 pc=0x26a2ac6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fc0ffe8 sp=0xc00fc0ffe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:828 +0xe52
   > goroutine 726 [select]:
   > runtime.gopark(0xc010b1ef90?, 0x2?, 0x0?, 0x0?, 0xc010b1ef6c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010b1edf0 sp=0xc010b1edd0 pc=0x13bb516
   > runtime.selectgo(0xc010b1ef90, 0xc010b1ef68, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010b1ef30 sp=0xc010b1edf0 pc=0x13cbbdc
   > github.com/pingcap/tidb/ddl.(*delRange).startEmulator(0xc010d0dda0)
   > 	/go/src/github.com/pingcap/tidb/ddl/delete_range.go:144 +0x125 fp=0xc010b1efc8 sp=0xc010b1ef30 pc=0x262b9e5
   > github.com/pingcap/tidb/ddl.(*delRange).start.func1()
   > 	/go/src/github.com/pingcap/tidb/ddl/delete_range.go:126 +0x26 fp=0xc010b1efe0 sp=0xc010b1efc8 pc=0x262b7a6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010b1efe8 sp=0xc010b1efe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/ddl.(*delRange).start
   > 	/go/src/github.com/pingcap/tidb/ddl/delete_range.go:126 +0x6d
   > goroutine 727 [select]:
   > runtime.gopark(0xc010089f58?, 0x4?, 0xab?, 0x62?, 0xc010089da8?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010089bf8 sp=0xc010089bd8 pc=0x13bb516
   > runtime.selectgo(0xc010089f58, 0xc010089da0, 0xc00009ee38?, 0x0, 0x1?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010089d38 sp=0xc010089bf8 pc=0x13cbbdc
   > github.com/pingcap/tidb/ddl.(*worker).start(0xc010d32840, 0xc010c7d740)
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl_worker.go:178 +0x318 fp=0xc010089fc0 sp=0xc010089d38 pc=0x2622e98
   > github.com/pingcap/tidb/ddl.(*ddl).Start.func2()
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:369 +0x2a fp=0xc010089fe0 sp=0xc010089fc0 pc=0x25e9a6a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010089fe8 sp=0xc010089fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/ddl.(*ddl).Start
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:369 +0x5c5
   > goroutine 725 [select]:
   > runtime.gopark(0xc010579f38?, 0x2?, 0x0?, 0x0?, 0xc010579efc?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010579d50 sp=0xc010579d30 pc=0x13bb516
   > runtime.selectgo(0xc010579f38, 0xc010579ef8, 0x1?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010579e90 sp=0xc010579d50 pc=0x13cbbdc
   > github.com/pingcap/tidb/ddl.(*ddl).limitDDLJobs(0xc010d08770)
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl_worker.go:263 +0x173 fp=0xc010579fc8 sp=0xc010579e90 pc=0x2623fd3
   > github.com/pingcap/tidb/ddl.(*ddl).Start.func1()
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:351 +0x26 fp=0xc010579fe0 sp=0xc010579fc8 pc=0x25e9ac6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010579fe8 sp=0xc010579fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/ddl.(*ddl).Start
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:351 +0x2ea
   > goroutine 845 [select]:
   > runtime.gopark(0xc0005037a8?, 0x2?, 0x4?, 0x30?, 0xc00050377c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000503600 sp=0xc0005035e0 pc=0x13bb516
   > runtime.selectgo(0xc0005037a8, 0xc000503778, 0x0?, 0x0, 0xc00fa4d9e0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000503740 sp=0xc000503600 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).PlanReplayerLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1191 +0xf6 fp=0xc0005037e0 sp=0xc000503740 pc=0x26a5f36
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0005037e8 sp=0xc0005037e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).PlanReplayerLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1182 +0x6c
   > goroutine 843 [select]:
   > runtime.gopark(0xc010651f28?, 0x6?, 0x50?, 0x80?, 0xc010651bb4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010651a20 sp=0xc010651a00 pc=0x13bb516
   > runtime.selectgo(0xc010651f28, 0xc010651ba8, 0x0?, 0x0, 0x138c3fb?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010651b60 sp=0xc010651a20 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).updateStatsWorker(0xc0005dcb40, {0x23de7ee?, 0xc000e3a5a0?}, {0x401ea10, 0xc010a2ae00})
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1372 +0x234 fp=0xc010651fa8 sp=0xc010651b60 pc=0x26a7e54
   > github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop.func3()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1259 +0x36 fp=0xc010651fe0 sp=0xc010651fa8 pc=0x26a65b6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010651fe8 sp=0xc010651fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1259 +0x29a
   > goroutine 882 [sleep]:
   > runtime.gopark(0x3fbff388067b?, 0xc0106d8480?, 0x88?, 0x6f?, 0x25412d5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000d36f58 sp=0xc000d36f38 pc=0x13bb516
   > time.Sleep(0x3b9aca00)
   > 	/usr/local/go/src/runtime/time.go:195 +0x135 fp=0xc000d36f98 sp=0xc000d36f58 pc=0x13eaf15
   > github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).startCPUProfileWorker(0xc000058058?)
   > 	/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:115 +0x65 fp=0xc000d36fc8 sp=0xc000d36f98 pc=0x2540065
   > github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).Run.func1()
   > 	/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:93 +0x26 fp=0xc000d36fe0 sp=0xc000d36fc8 pc=0x253fea6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000d36fe8 sp=0xc000d36fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).Run
   > 	/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:93 +0xca
   > goroutine 835 [select]:
   > runtime.gopark(0xc0103caf18?, 0x3?, 0x4?, 0x30?, 0xc0103cae8a?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0103cacc8 sp=0xc0103caca8 pc=0x13bb516
   > runtime.selectgo(0xc0103caf18, 0xc0103cae84, 0xc0103caf88?, 0x0, 0x13bb516?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0103cae08 sp=0xc0103cacc8 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).LoadSysVarCacheLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:989 +0x145 fp=0xc0103cafe0 sp=0xc0103cae08 pc=0x26a3dc5
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0103cafe8 sp=0xc0103cafe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).LoadSysVarCacheLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:980 +0x172
   > goroutine 846 [chan receive]:
   > runtime.gopark(0xc00001ebe8?, 0xc0008a8d00?, 0x48?, 0xb6?, 0x13d8de5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0103cb5f0 sp=0xc0103cb5d0 pc=0x13bb516
   > runtime.chanrecv(0xc011401860, 0xc0103cb738, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc0103cb680 sp=0xc0103cb5f0 pc=0x13854bb
   > runtime.chanrecv2(0x9356907420000?, 0x0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc0103cb6a8 sp=0xc0103cb680 pc=0x1384ff8
   > github.com/pingcap/tidb/server.NewServer.func1()
   > 	/go/src/github.com/pingcap/tidb/server/server.go:209 +0x98 fp=0xc0103cb7e0 sp=0xc0103cb6a8 pc=0x31e1638
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0103cb7e8 sp=0xc0103cb7e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/server.NewServer
   > 	/go/src/github.com/pingcap/tidb/server/server.go:208 +0x32a
   > goroutine 1152 [select]:
   > runtime.gopark(0xc000c85e30?, 0x2?, 0x80?, 0x57?, 0xc000c85e1c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000c85ca8 sp=0xc000c85c88 pc=0x13bb516
   > runtime.selectgo(0xc000c85e30, 0xc000c85e18, 0xc0121c8ba0?, 0x0, 0x2fef900?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000c85de8 sp=0xc000c85ca8 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).wait4BuildSide(0xc01221ad80)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:242 +0x6f fp=0xc000c85e60 sp=0xc000c85de8 pc=0x30605ef
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchProbeSideChunks(0xc01221ad80, {0x400d6b0, 0xc0120b97d0})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:221 +0x233 fp=0xc000c85f28 sp=0xc000c85e60 pc=0x3060333
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:322 +0x8f fp=0xc000c85f90 sp=0xc000c85f28 pc=0x306156f
   > github.com/pingcap/tidb/util.WithRecovery(0x5f539a0?, 0xc00fc10fb8?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc000c85fc0 sp=0xc000c85f90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func3()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:320 +0x2a fp=0xc000c85fe0 sp=0xc000c85fc0 pc=0x30614aa
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000c85fe8 sp=0xc000c85fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:320 +0x14f
   > goroutine 847 [select]:
   > runtime.gopark(0xc010085eb0?, 0x2?, 0x19?, 0x0?, 0xc010085e5c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010085cc8 sp=0xc010085ca8 pc=0x13bb516
   > runtime.selectgo(0xc010085eb0, 0xc010085e58, 0xc010515ba0?, 0x0, 0xc010d88cc0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010085e08 sp=0xc010085cc8 pc=0x13cbbdc
   > github.com/pingcap/tidb/util/expensivequery.(*Handle).Run(0xc000598fd8)
   > 	/go/src/github.com/pingcap/tidb/util/expensivequery/expensivequery.go:61 +0x198 fp=0xc010085fc8 sp=0xc010085e08 pc=0x2695d58
   > main.createServer.func1()
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:675 +0x26 fp=0xc010085fe0 sp=0xc010085fc8 pc=0x33b2be6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010085fe8 sp=0xc010085fe0 pc=0x13ee6e1
   > created by main.createServer
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:675 +0x439
   > goroutine 900 [chan receive]:
   > runtime.gopark(0x50?, 0xc000663680?, 0x8?, 0x2d?, 0x138c1bf?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000c82c80 sp=0xc000c82c60 pc=0x13bb516
   > runtime.chanrecv(0xc00fb76420, 0xc000c82d48, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000c82d10 sp=0xc000c82c80 pc=0x13854bb
   > runtime.chanrecv2(0x141e886?, 0xc0059539c0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc000c82d38 sp=0xc000c82d10 pc=0x1384ff8
   > github.com/soheilhy/cmux.muxListener.Accept(...)
   > 	/go/pkg/mod/github.com/soheilhy/cmux@v0.1.4/cmux.go:229
   > github.com/soheilhy/cmux.(*muxListener).Accept(0x5828400?)
   > 	<autogenerated>:1 +0x45 fp=0xc000c82d68 sp=0xc000c82d38 pc=0x2dc7625
   > net/http.(*onceCloseListener).Accept(0x400d640?)
   > 	<autogenerated>:1 +0x2a fp=0xc000c82d80 sp=0xc000c82d68 pc=0x16e0c6a
   > net/http.(*Server).Serve(0xc00fce3770, {0x400cb50, 0xc0105ce5e8})
   > 	/usr/local/go/src/net/http/server.go:3070 +0x385 fp=0xc000c82eb0 sp=0xc000c82d80 pc=0x16b6f45
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer.func2()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:462 +0x3e fp=0xc000c82f90 sp=0xc000c82eb0 pc=0x31dadbe
   > github.com/pingcap/tidb/util.WithRecovery(0x31d65c6?, 0xc010515ba0?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc000c82fc0 sp=0xc000c82f90 pc=0x1ffabd3
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer.func6()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:461 +0x28 fp=0xc000c82fe0 sp=0xc000c82fc0 pc=0x31dad48
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000c82fe8 sp=0xc000c82fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:461 +0x4ea
   > goroutine 899 [chan receive]:
   > runtime.gopark(0x3a8bf40?, 0xc000f4ccf8?, 0xfc?, 0xb?, 0xa?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000f4ccb0 sp=0xc000f4cc90 pc=0x13bb516
   > runtime.chanrecv(0xc00fb76480, 0xc000f4cd78, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000f4cd40 sp=0xc000f4ccb0 pc=0x13854bb
   > runtime.chanrecv2(0xc000f0ed90?, 0x2?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc000f4cd68 sp=0xc000f4cd40 pc=0x1384ff8
   > github.com/soheilhy/cmux.muxListener.Accept(...)
   > 	/go/pkg/mod/github.com/soheilhy/cmux@v0.1.4/cmux.go:229
   > github.com/soheilhy/cmux.(*muxListener).Accept(0x3ff0f40?)
   > 	<autogenerated>:1 +0x45 fp=0xc000f4cd98 sp=0xc000f4cd68 pc=0x2dc7625
   > google.golang.org/grpc.(*Server).Serve(0xc0008c0340, {0x400cb50, 0xc0105ce600})
   > 	/go/pkg/mod/google.golang.org/grpc@v1.29.1/server.go:621 +0x362 fp=0xc000f4ceb0 sp=0xc000f4cd98 pc=0x19749a2
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer.func1()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:457 +0x3e fp=0xc000f4cf90 sp=0xc000f4ceb0 pc=0x31db01e
   > github.com/pingcap/tidb/util.WithRecovery(0x400d640?, 0xc00fb76240?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc000f4cfc0 sp=0xc000f4cf90 pc=0x1ffabd3
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer.func5()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:456 +0x28 fp=0xc000f4cfe0 sp=0xc000f4cfc0 pc=0x31dafa8
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000f4cfe8 sp=0xc000f4cfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:456 +0x42c
   > goroutine 840 [select]:
   > runtime.gopark(0xc00fc14f28?, 0x2?, 0x4?, 0x30?, 0xc00fc14ed4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fc14d48 sp=0xc00fc14d28 pc=0x13bb516
   > runtime.selectgo(0xc00fc14f28, 0xc00fc14ed0, 0x9?, 0x0, 0x15?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fc14e88 sp=0xc00fc14d48 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).TelemetryReportLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1140 +0x11c fp=0xc00fc14fe0 sp=0xc00fc14e88 pc=0x26a573c
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fc14fe8 sp=0xc00fc14fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).TelemetryReportLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1132 +0x285
   > goroutine 1315 [select]:
   > runtime.gopark(0xc000e6ee10?, 0x2?, 0x70?, 0x92?, 0xc000e6ed8c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000e6ebe0 sp=0xc000e6ebc0 pc=0x13bb516
   > runtime.selectgo(0xc000e6ee10, 0xc000e6ed88, 0x13cb293?, 0x0, 0x13cc174?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000e6ed20 sp=0xc000e6ebe0 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc01221ad80, 0x2, {0xc00fabbca0, 0x1, 0x1})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:441 +0x4f4 fp=0xc000e6ef10 sp=0xc000e6ed20 pc=0x30626b4
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:335 +0xb3 fp=0xc000e6ef90 sp=0xc000e6ef10 pc=0x30613d3
   > github.com/pingcap/tidb/util.WithRecovery(0x23de786?, 0xc01053ca00?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc000e6efc0 sp=0xc000e6ef90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x2a fp=0xc000e6efe0 sp=0xc000e6efc0 pc=0x30612ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000e6efe8 sp=0xc000e6efe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x1c9
   > goroutine 801 [chan receive]:
   > runtime.gopark(0x13c37d1?, 0xc012170b50?, 0x0?, 0x38?, 0xc0124ac820?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc012170b40 sp=0xc012170b20 pc=0x13bb516
   > runtime.chanrecv(0xc012367800, 0xc012170c90, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc012170bd0 sp=0xc012170b40 pc=0x13854bb
   > runtime.chanrecv2(0xc01221b8c0?, 0x400d6b0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc012170bf8 sp=0xc012170bd0 pc=0x1384ff8
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Next(0xc01221b8c0, {0x400d6b0?, 0xc0120b97d0?}, 0xc0124a6500)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:681 +0x652 fp=0xc012170cb8 sp=0xc012170bf8 pc=0x3064d52
   > github.com/pingcap/tidb/executor.Next({0x400d6b0, 0xc0120b97d0}, {0x40101a0, 0xc01221b8c0}, 0xc0124a6500)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:286 +0x4a8 fp=0xc012170df8 sp=0xc012170cb8 pc=0x2fef688
   > github.com/pingcap/tidb/executor.(*ProjectionExec).unParallelExecute(0xc01231e6c0, {0x400d6b0?, 0xc0120b97d0?}, 0xc0124a6e10)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:194 +0xb8 fp=0xc012170e48 sp=0xc012170df8 pc=0x3098758
   > github.com/pingcap/tidb/executor.(*ProjectionExec).Next(0xc01231e6c0, {0x400d6b0, 0xc0120b97d0}, 0xc0122721a0?)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:180 +0x5a fp=0xc012170e80 sp=0xc012170e48 pc=0x309861a
   > github.com/pingcap/tidb/executor.Next({0x400d6b0, 0xc0120b97d0}, {0x4010760, 0xc01231e6c0}, 0xc0124a6e10)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:286 +0x4a8 fp=0xc012170fc0 sp=0xc012170e80 pc=0x2fef688
   > github.com/pingcap/tidb/executor.(*recordSet).Next(0xc0124a6d70, {0x400d6b0?, 0xc0120b97d0?}, 0xc0124a6e10)
   > 	/go/src/github.com/pingcap/tidb/executor/adapter.go:147 +0xbf fp=0xc012171050 sp=0xc012170fc0 pc=0x2f60d1f
   > github.com/pingcap/tidb/session.(*execStmtResult).Next(0xc0120b97a0?, {0x400d6b0?, 0xc0120b97d0?}, 0xc00fd94000?)
   > 	<autogenerated>:1 +0x34 fp=0xc012171080 sp=0xc012171050 pc=0x315d9d4
   > github.com/pingcap/tidb/server.(*tidbResultSet).Next(0x3f3269fa6f9d46cd?, {0x400d6b0?, 0xc0120b97d0?}, 0xc00fa49ec0?)
   > 	/go/src/github.com/pingcap/tidb/server/driver_tidb.go:306 +0x2b fp=0xc0121710b0 sp=0xc012171080 pc=0x31c5f6b
   > github.com/pingcap/tidb/server.(*clientConn).writeChunks(0xc000e0aa00, {0x400d6b0, 0xc0120b97d0}, {0x401c468, 0xc0124a6dc0}, 0x0, 0x1217?)
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:2103 +0x15e fp=0xc012171170 sp=0xc0121710b0 pc=0x31bd47e
   > github.com/pingcap/tidb/server.(*clientConn).writeResultset(0xc000e0aa00, {0x400d6b0, 0xc0120b97d0}, {0x401c468, 0xc0124a6dc0}, 0x60?, 0x2, 0x23b?)
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:2052 +0x174 fp=0xc012171220 sp=0xc012171170 pc=0x31bcc74
   > github.com/pingcap/tidb/server.(*clientConn).handleStmt(0xc000e0aa00, {0x400d608, 0xc000138200}, {0x401fff0, 0xc0118bed20}, {0x5f8a1a8, 0x0, 0x0}, 0x1)
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:1932 +0x3d6 fp=0xc0121712f0 sp=0xc012171220 pc=0x31bbab6
   > github.com/pingcap/tidb/server.(*clientConn).handleQuery(0xc000e0aa00, {0x400d608, 0xc000138200}, {0xc010bee821, 0x18c})
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:1775 +0x774 fp=0xc012171468 sp=0xc0121712f0 pc=0x31ba494
   > github.com/pingcap/tidb/server.(*clientConn).dispatch(0xc000e0aa00, {0x400d6b0, 0xc010fe00c0?}, {0xc010bee820, 0x18d, 0x18d})
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:1279 +0x1025 fp=0xc012171858 sp=0xc012171468 pc=0x31b6045
   > github.com/pingcap/tidb/server.(*clientConn).Run(0xc000e0aa00, {0x400d6b0, 0xc010fe00c0})
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:1034 +0x253 fp=0xc012171e18 sp=0xc012171858 pc=0x31b2b33
   > github.com/pingcap/tidb/server.(*Server).onConn(0xc010515ba0, 0xc000e0aa00)
   > 	/go/src/github.com/pingcap/tidb/server/server.go:550 +0x6c5 fp=0xc012171fc0 sp=0xc012171e18 pc=0x31e4165
   > github.com/pingcap/tidb/server.(*Server).startNetworkListener.func2()
   > 	/go/src/github.com/pingcap/tidb/server/server.go:453 +0x2a fp=0xc012171fe0 sp=0xc012171fc0 pc=0x31e300a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc012171fe8 sp=0xc012171fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/server.(*Server).startNetworkListener
   > 	/go/src/github.com/pingcap/tidb/server/server.go:453 +0x5ca
   > goroutine 1318 [semacquire]:
   > runtime.gopark(0x0?, 0x0?, 0x60?, 0x49?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01138c678 sp=0xc01138c658 pc=0x13bb516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc01221af78, 0x0?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc01138c6e0 sp=0xc01138c678 pc=0x13cce5e
   > sync.runtime_Semacquire(0x0?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc01138c710 sp=0xc01138c6e0 pc=0x13e9f65
   > sync.(*WaitGroup).Wait(0x0?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc01138c738 sp=0xc01138c710 pc=0x13fd1f2
   > github.com/pingcap/tidb/executor.(*HashJoinExec).waitJoinWorkersAndCloseResultChan(0xc01221ad80)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:395 +0x33 fp=0xc01138c778 sp=0xc01138c738 pc=0x3061fb3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).waitJoinWorkersAndCloseResultChan-fm()
   > 	<autogenerated>:1 +0x26 fp=0xc01138c790 sp=0xc01138c778 pc=0x31277c6
   > github.com/pingcap/tidb/util.WithRecovery(0x0?, 0x0?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc01138c7c0 sp=0xc01138c790 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:338 +0x28 fp=0xc01138c7e0 sp=0xc01138c7c0 pc=0x3061288
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01138c7e8 sp=0xc01138c7e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:338 +0x3b8
   > goroutine 886 [IO wait]:
   > runtime.gopark(0xc000c87b30?, 0x25ca355?, 0xf0?, 0xa3?, 0xc000c87b78?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000c87b08 sp=0xc000c87ae8 pc=0x13bb516
   > runtime.netpollblock(0xc010a6d560?, 0xe419d6a7?, 0xd0?)
   > 	/usr/local/go/src/runtime/netpoll.go:526 +0xf7 fp=0xc000c87b40 sp=0xc000c87b08 pc=0x13b38f7
   > internal/poll.runtime_pollWait(0x7f379c261fb8, 0x72)
   > 	/usr/local/go/src/runtime/netpoll.go:305 +0x89 fp=0xc000c87b60 sp=0xc000c87b40 pc=0x13e7d09
   > internal/poll.(*pollDesc).wait(0xc011183300?, 0x1?, 0x0)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:84 +0x32 fp=0xc000c87b88 sp=0xc000c87b60 pc=0x1465192
   > internal/poll.(*pollDesc).waitRead(...)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:89
   > internal/poll.(*FD).Accept(0xc011183300)
   > 	/usr/local/go/src/internal/poll/fd_unix.go:614 +0x234 fp=0xc000c87c20 sp=0xc000c87b88 pc=0x146a594
   > net.(*netFD).accept(0xc011183300)
   > 	/usr/local/go/src/net/fd_unix.go:172 +0x35 fp=0xc000c87cd8 sp=0xc000c87c20 pc=0x1589055
   > net.(*UnixListener).accept(0xc0114015c0?)
   > 	/usr/local/go/src/net/unixsock_posix.go:166 +0x1c fp=0xc000c87d00 sp=0xc000c87cd8 pc=0x15aba1c
   > net.(*UnixListener).Accept(0xc010427d70)
   > 	/usr/local/go/src/net/unixsock.go:260 +0x3d fp=0xc000c87d30 sp=0xc000c87d00 pc=0x15aa0bd
   > github.com/pingcap/tidb/server.(*Server).startNetworkListener(0xc010515ba0, {0x400b9e0, 0xc010427d70}, 0x1, 0xc0105fb7c0?)
   > 	/go/src/github.com/pingcap/tidb/server/server.go:383 +0xa6 fp=0xc000c87fa8 sp=0xc000c87d30 pc=0x31e25a6
   > github.com/pingcap/tidb/server.(*Server).Run.func2()
   > 	/go/src/github.com/pingcap/tidb/server/server.go:369 +0x37 fp=0xc000c87fe0 sp=0xc000c87fa8 pc=0x31e2477
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000c87fe8 sp=0xc000c87fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/server.(*Server).Run
   > 	/go/src/github.com/pingcap/tidb/server/server.go:369 +0x1db
   > goroutine 1151 [chan receive]:
   > runtime.gopark(0xc012182280?, 0xc0120727e0?, 0x3?, 0x0?, 0xc000f3dcf8?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000f3dca8 sp=0xc000f3dc88 pc=0x13bb516
   > runtime.chanrecv(0xc012072720, 0xc000f3de08, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000f3dd38 sp=0xc000f3dca8 pc=0x13854bb
   > runtime.chanrecv2(0xc0109a6eb0?, 0x4012e60?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc000f3dd60 sp=0xc000f3dd38 pc=0x1384ff8
   > github.com/pingcap/tidb/executor.(*HashJoinExec).buildHashTableForList(0xc01221ad80, 0x1?)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:762 +0x2d6 fp=0xc000f3de78 sp=0xc000f3dd60 pc=0x3065af6
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable(0xc01221ad80, {0x400d6b0?, 0xc0120b97d0})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:726 +0x23f fp=0xc000f3df28 sp=0xc000f3de78 pc=0x30653ff
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Next.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:671 +0x8f fp=0xc000f3df90 sp=0xc000f3df28 pc=0x306504f
   > github.com/pingcap/tidb/util.WithRecovery(0x23de786?, 0xc00fa49b00?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc000f3dfc0 sp=0xc000f3df90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Next.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:669 +0x2a fp=0xc000f3dfe0 sp=0xc000f3dfc0 pc=0x3064f8a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000f3dfe8 sp=0xc000f3dfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).Next
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:669 +0x5b2
   > goroutine 848 [select, locked to thread]:
   > runtime.gopark(0xc0103cbfa8?, 0x2?, 0x80?, 0x93?, 0xc0103cbfa4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0103cbe18 sp=0xc0103cbdf8 pc=0x13bb516
   > runtime.selectgo(0xc0103cbfa8, 0xc0103cbfa0, 0x0?, 0x0, 0xc0106cf200?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0103cbf58 sp=0xc0103cbe18 pc=0x13cbbdc
   > runtime.ensureSigM.func1()
   > 	/usr/local/go/src/runtime/signal_unix.go:995 +0x1b0 fp=0xc0103cbfe0 sp=0xc0103cbf58 pc=0x13d0070
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0103cbfe8 sp=0xc0103cbfe0 pc=0x13ee6e1
   > created by runtime.ensureSigM
   > 	/usr/local/go/src/runtime/signal_unix.go:978 +0xbd
   > goroutine 885 [IO wait]:
   > runtime.gopark(0x18?, 0xc000100c00?, 0x0?, 0xc0?, 0xc0000a2b70?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0000a2b00 sp=0xc0000a2ae0 pc=0x13bb516
   > runtime.netpollblock(0x14?, 0x2432d05?, 0x0?)
   > 	/usr/local/go/src/runtime/netpoll.go:526 +0xf7 fp=0xc0000a2b38 sp=0xc0000a2b00 pc=0x13b38f7
   > internal/poll.runtime_pollWait(0x7f379c2620a8, 0x72)
   > 	/usr/local/go/src/runtime/netpoll.go:305 +0x89 fp=0xc0000a2b58 sp=0xc0000a2b38 pc=0x13e7d09
   > internal/poll.(*pollDesc).wait(0xc011183280?, 0xc0000a2d20?, 0x0)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:84 +0x32 fp=0xc0000a2b80 sp=0xc0000a2b58 pc=0x1465192
   > internal/poll.(*pollDesc).waitRead(...)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:89
   > internal/poll.(*FD).Accept(0xc011183280)
   > 	/usr/local/go/src/internal/poll/fd_unix.go:614 +0x234 fp=0xc0000a2c18 sp=0xc0000a2b80 pc=0x146a594
   > net.(*netFD).accept(0xc011183280)
   > 	/usr/local/go/src/net/fd_unix.go:172 +0x35 fp=0xc0000a2cd0 sp=0xc0000a2c18 pc=0x1589055
   > net.(*TCPListener).accept(0xc0105ce120)
   > 	/usr/local/go/src/net/tcpsock_posix.go:142 +0x28 fp=0xc0000a2d00 sp=0xc0000a2cd0 pc=0x15a5088
   > net.(*TCPListener).Accept(0xc0105ce120)
   > 	/usr/local/go/src/net/tcpsock.go:288 +0x3d fp=0xc0000a2d30 sp=0xc0000a2d00 pc=0x15a40fd
   > github.com/pingcap/tidb/server.(*Server).startNetworkListener(0xc010515ba0, {0x400b9b0, 0xc0105ce120}, 0x0, 0xc0005443c0?)
   > 	/go/src/github.com/pingcap/tidb/server/server.go:383 +0xa6 fp=0xc0000a2fa8 sp=0xc0000a2d30 pc=0x31e25a6
   > github.com/pingcap/tidb/server.(*Server).Run.func1()
   > 	/go/src/github.com/pingcap/tidb/server/server.go:368 +0x34 fp=0xc0000a2fe0 sp=0xc0000a2fa8 pc=0x31e24d4
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000a2fe8 sp=0xc0000a2fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/server.(*Server).Run
   > 	/go/src/github.com/pingcap/tidb/server/server.go:368 +0x145
   > goroutine 844 [select]:
   > runtime.gopark(0xc010b8df78?, 0x2?, 0x0?, 0xbe?, 0xc010b8df4c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010b8ddd0 sp=0xc010b8ddb0 pc=0x13bb516
   > runtime.selectgo(0xc010b8df78, 0xc010b8df48, 0xc010934310?, 0x0, 0xc00fc12658?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010b8df10 sp=0xc010b8ddd0 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).autoAnalyzeWorker(0xc0005dcb40, {0x401ea10, 0xc010a2ae00})
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1425 +0x105 fp=0xc010b8dfb8 sp=0xc010b8df10 pc=0x26a8bc5
   > github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop.func4()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1262 +0x2e fp=0xc010b8dfe0 sp=0xc010b8dfb8 pc=0x26a654e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010b8dfe8 sp=0xc010b8dfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1262 +0x31a
   > goroutine 884 [IO wait]:
   > runtime.gopark(0xf?, 0xc010a17110?, 0x2?, 0x0?, 0xc0005d18d0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0005d1860 sp=0xc0005d1840 pc=0x13bb516
   > runtime.netpollblock(0x203004?, 0x10a17110?, 0xc0?)
   > 	/usr/local/go/src/runtime/netpoll.go:526 +0xf7 fp=0xc0005d1898 sp=0xc0005d1860 pc=0x13b38f7
   > internal/poll.runtime_pollWait(0x7f379c261ec8, 0x72)
   > 	/usr/local/go/src/runtime/netpoll.go:305 +0x89 fp=0xc0005d18b8 sp=0xc0005d1898 pc=0x13e7d09
   > internal/poll.(*pollDesc).wait(0xc011183480?, 0xc000bb4480?, 0x0)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:84 +0x32 fp=0xc0005d18e0 sp=0xc0005d18b8 pc=0x1465192
   > internal/poll.(*pollDesc).waitRead(...)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:89
   > internal/poll.(*FD).Accept(0xc011183480)
   > 	/usr/local/go/src/internal/poll/fd_unix.go:614 +0x234 fp=0xc0005d1978 sp=0xc0005d18e0 pc=0x146a594
   > net.(*netFD).accept(0xc011183480)
   > 	/usr/local/go/src/net/fd_unix.go:172 +0x35 fp=0xc0005d1a30 sp=0xc0005d1978 pc=0x1589055
   > net.(*TCPListener).accept(0xc0105ce138)
   > 	/usr/local/go/src/net/tcpsock_posix.go:142 +0x28 fp=0xc0005d1a60 sp=0xc0005d1a30 pc=0x15a5088
   > net.(*TCPListener).Accept(0xc0105ce138)
   > 	/usr/local/go/src/net/tcpsock.go:288 +0x3d fp=0xc0005d1a90 sp=0xc0005d1a60 pc=0x15a40fd
   > github.com/soheilhy/cmux.(*cMux).Serve(0xc000bdd270)
   > 	/go/pkg/mod/github.com/soheilhy/cmux@v0.1.4/cmux.go:162 +0xa9 fp=0xc0005d1b20 sp=0xc0005d1a90 pc=0x2dc5da9
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer(0xc010515ba0, 0xc000911840)
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:466 +0x4f7 fp=0xc0005d1c90 sp=0xc0005d1b20 pc=0x31dab17
   > github.com/pingcap/tidb/server.(*Server).startHTTPServer(0xc010515ba0)
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:442 +0x15d0 fp=0xc0005d1fc8 sp=0xc0005d1c90 pc=0x31d9f10
   > github.com/pingcap/tidb/server.(*Server).startStatusHTTP.func1()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:62 +0x26 fp=0xc0005d1fe0 sp=0xc0005d1fc8 pc=0x31d65c6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0005d1fe8 sp=0xc0005d1fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/server.(*Server).startStatusHTTP
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:62 +0x56
   > goroutine 816 [select]:
   > runtime.gopark(0xc000d31f80?, 0x3?, 0x1?, 0x30?, 0xc000d31f3a?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000d31da8 sp=0xc000d31d88 pc=0x13bb516
   > runtime.selectgo(0xc000d31f80, 0xc000d31f34, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000d31ee8 sp=0xc000d31da8 pc=0x13cbbdc
   > github.com/pingcap/tidb/util/topsql/reporter.(*RemoteTopSQLReporter).collectWorker(0xc00022d650)
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:327 +0x13a fp=0xc000d31fc8 sp=0xc000d31ee8 pc=0x2547eda
   > github.com/pingcap/tidb/util/topsql/reporter.NewRemoteTopSQLReporter.func1()
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:160 +0x26 fp=0xc000d31fe0 sp=0xc000d31fc8 pc=0x2546c26
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000d31fe8 sp=0xc000d31fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/util/topsql/reporter.NewRemoteTopSQLReporter
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:160 +0x1b6
   > goroutine 842 [select]:
   > runtime.gopark(0xc010dedd48?, 0x2?, 0x0?, 0x72?, 0xc010dedc94?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010dedb08 sp=0xc010dedae8 pc=0x13bb516
   > runtime.selectgo(0xc010dedd48, 0xc010dedc90, 0xc010934310?, 0x0, 0x1?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010dedc48 sp=0xc010dedb08 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).loadStatsWorker(0xc0005dcb40)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1304 +0x485 fp=0xc010dedfc8 sp=0xc010dedc48 pc=0x26a6ea5
   > github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1247 +0x26 fp=0xc010dedfe0 sp=0xc010dedfc8 pc=0x26a6666
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010dedfe8 sp=0xc010dedfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1247 +0x105
   > goroutine 832 [select]:
   > runtime.gopark(0xc00fc15718?, 0x3?, 0x4?, 0x30?, 0xc00fc1569a?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fc154d8 sp=0xc00fc154b8 pc=0x13bb516
   > runtime.selectgo(0xc00fc15718, 0xc00fc15694, 0xc000e3acc0?, 0x0, 0xc0059443c0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fc15618 sp=0xc00fc154d8 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).LoadPrivilegeLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:939 +0x145 fp=0xc00fc157e0 sp=0xc00fc15618 pc=0x26a3585
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fc157e8 sp=0xc00fc157e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).LoadPrivilegeLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:930 +0x205
   > goroutine 841 [select]:
   > runtime.gopark(0xc00fc11fa8?, 0x2?, 0x4?, 0x30?, 0xc00fc11f84?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fc11e08 sp=0xc00fc11de8 pc=0x13bb516
   > runtime.selectgo(0xc00fc11fa8, 0xc00fc11f80, 0xc0104263c0?, 0x0, 0xc0005677a0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fc11f48 sp=0xc00fc11e08 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).TelemetryRotateSubWindowLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1169 +0xcc fp=0xc00fc11fe0 sp=0xc00fc11f48 pc=0x26a5c4c
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fc11fe8 sp=0xc00fc11fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).TelemetryRotateSubWindowLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1162 +0x8f
   > goroutine 883 [chan receive]:
   > runtime.gopark(0x1?, 0x2?, 0x0?, 0x0?, 0xc010749e38?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010749de0 sp=0xc010749dc0 pc=0x13bb516
   > runtime.chanrecv(0xc0000d2600, 0xc010749f08, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc010749e70 sp=0xc010749de0 pc=0x13854bb
   > runtime.chanrecv1(0xc010749f78?, 0xc010749ee8?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc010749e98 sp=0xc010749e70 pc=0x1384fb8
   > github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).startAnalyzeProfileWorker(0xc0009889c0)
   > 	/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:142 +0x7c fp=0xc010749fc8 sp=0xc010749e98 pc=0x25402bc
   > github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).Run.func2()
   > 	/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:94 +0x26 fp=0xc010749fe0 sp=0xc010749fc8 pc=0x253fe46
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010749fe8 sp=0xc010749fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).Run
   > 	/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:94 +0x10a
   > goroutine 1299 [select]:
   > runtime.gopark(0xc0103c9e10?, 0x2?, 0xb0?, 0x1d?, 0xc0103c9d8c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0111f4be0 sp=0xc0111f4bc0 pc=0x13bb516
   > runtime.selectgo(0xc0111f4e10, 0xc0103c9d88, 0x0?, 0x0, 0x13cc174?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0111f4d20 sp=0xc0111f4be0 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc01221b8c0, 0x0, {0xc012359cc8, 0x1, 0x1})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:441 +0x4f4 fp=0xc0111f4f10 sp=0xc0111f4d20 pc=0x30626b4
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:335 +0xb3 fp=0xc0111f4f90 sp=0xc0111f4f10 pc=0x30613d3
   > github.com/pingcap/tidb/util.WithRecovery(0x0?, 0xc0103c9ec8?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc0111f4fc0 sp=0xc0111f4f90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x2a fp=0xc0111f4fe0 sp=0xc0111f4fc0 pc=0x30612ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0111f4fe8 sp=0xc0111f4fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x1c9
   > goroutine 733 [select]:
   > runtime.gopark(0xc0103ccef0?, 0x2?, 0x0?, 0x0?, 0xc0103ccebc?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0103ccd38 sp=0xc0103ccd18 pc=0x13bb516
   > runtime.selectgo(0xc0103ccef0, 0xc0103cceb8, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0103cce78 sp=0xc0103ccd38 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).globalConfigSyncerKeeper(0xc0005dcb40)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:510 +0xe5 fp=0xc0103ccfc8 sp=0xc0103cce78 pc=0x269f405
   > github.com/pingcap/tidb/domain.(*Domain).Init.func13()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:830 +0x26 fp=0xc0103ccfe0 sp=0xc0103ccfc8 pc=0x26a2a06
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0103ccfe8 sp=0xc0103ccfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:830 +0xedc
   > goroutine 734 [select]:
   > runtime.gopark(0xc000e72678?, 0x3?, 0x4?, 0x30?, 0xc000e725f2?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000e72478 sp=0xc000e72458 pc=0x13bb516
   > runtime.selectgo(0xc000e72678, 0xc000e725ec, 0x138c501?, 0x0, 0x2664b26?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000e725b8 sp=0xc000e72478 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).topologySyncerKeeper(0xc0005dcb40)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:533 +0x165 fp=0xc000e727c8 sp=0xc000e725b8 pc=0x269f8c5
   > github.com/pingcap/tidb/domain.(*Domain).Init.func14()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:834 +0x26 fp=0xc000e727e0 sp=0xc000e727c8 pc=0x26a29a6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000e727e8 sp=0xc000e727e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:834 +0xf3d
   > goroutine 743 [select]:
   > runtime.gopark(0xc010b91e90?, 0x3?, 0x60?, 0x15?, 0xc010b91e02?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010b91c70 sp=0xc010b91c50 pc=0x13bb516
   > runtime.selectgo(0xc010b91e90, 0xc010b91dfc, 0x3a8be78?, 0x0, 0xc0112185a0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010b91db0 sp=0xc010b91c70 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).globalBindHandleWorkerLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1071 +0x16f fp=0xc010b91fe0 sp=0xc010b91db0 pc=0x26a476f
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010b91fe8 sp=0xc010b91fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).globalBindHandleWorkerLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1058 +0xad
   > goroutine 744 [select]:
   > runtime.gopark(0xc000c81f28?, 0x2?, 0x4?, 0x30?, 0xc000c81ed4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000c81d48 sp=0xc000c81d28 pc=0x13bb516
   > runtime.selectgo(0xc000c81f28, 0xc000c81ed0, 0xc010c07000?, 0x0, 0xc010745ed8?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000c81e88 sp=0xc000c81d48 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).handleEvolvePlanTasksLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1106 +0x107 fp=0xc000c81fe0 sp=0xc000c81e88 pc=0x26a4fe7
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000c81fe8 sp=0xc000c81fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).handleEvolvePlanTasksLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1099 +0xe5
   > goroutine 777 [select]:
   > runtime.gopark(0xc00fc15f78?, 0x2?, 0x1?, 0x0?, 0xc00fc15eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fc15d58 sp=0xc00fc15d38 pc=0x13bb516
   > runtime.selectgo(0xc00fc15f78, 0xc00fc15ee8, 0x3aac226?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fc15e98 sp=0xc00fc15d58 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc00fa643c0, {0x400d6b0?, 0xc0120b97d0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc00fc15fb8 sp=0xc00fc15e98 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc00fc15fe0 sp=0xc00fc15fb8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fc15fe8 sp=0xc00fc15fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 775 [select]:
   > runtime.gopark(0xc00fc14778?, 0x2?, 0xc7?, 0xb5?, 0xc00fc146ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fc14558 sp=0xc00fc14538 pc=0x13bb516
   > runtime.selectgo(0xc00fc14778, 0xc00fc146e8, 0x3aac226?, 0x0, 0xd0b7887a?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fc14698 sp=0xc00fc14558 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc00fa64340, {0x400d6b0?, 0xc0120b97d0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc00fc147b8 sp=0xc00fc14698 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc00fc147e0 sp=0xc00fc147b8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fc147e8 sp=0xc00fc147e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 1316 [select]:
   > runtime.gopark(0xc0121f1e10?, 0x2?, 0x80?, 0x92?, 0xc0121f1d8c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0121f1be0 sp=0xc0121f1bc0 pc=0x13bb516
   > runtime.selectgo(0xc0121f1e10, 0xc0121f1d88, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0121f1d20 sp=0xc0121f1be0 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc01221ad80, 0x3, {0xc00fabbca0, 0x1, 0x1})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:441 +0x4f4 fp=0xc0121f1f10 sp=0xc0121f1d20 pc=0x30626b4
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:335 +0xb3 fp=0xc0121f1f90 sp=0xc0121f1f10 pc=0x30613d3
   > github.com/pingcap/tidb/util.WithRecovery(0x0?, 0x0?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc0121f1fc0 sp=0xc0121f1f90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x2a fp=0xc0121f1fe0 sp=0xc0121f1fc0 pc=0x30612ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0121f1fe8 sp=0xc0121f1fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x1c9
   > goroutine 774 [select]:
   > runtime.gopark(0xc011393778?, 0x2?, 0x0?, 0x0?, 0xc0113936ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc011393558 sp=0xc011393538 pc=0x13bb516
   > runtime.selectgo(0xc011393778, 0xc0113936e8, 0x3aac226?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc011393698 sp=0xc011393558 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc00fa64300, {0x400d6b0?, 0xc0120b97d0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc0113937b8 sp=0xc011393698 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc0113937e0 sp=0xc0113937b8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0113937e8 sp=0xc0113937e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 776 [select]:
   > runtime.gopark(0xc011393f78?, 0x2?, 0x0?, 0x0?, 0xc011393eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc011393d58 sp=0xc011393d38 pc=0x13bb516
   > runtime.selectgo(0xc011393f78, 0xc011393ee8, 0x3aac226?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc011393e98 sp=0xc011393d58 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc00fa64380, {0x400d6b0?, 0xc0120b97d0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc011393fb8 sp=0xc011393e98 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc011393fe0 sp=0xc011393fb8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc011393fe8 sp=0xc011393fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 814 [chan receive]:
   > runtime.gopark(0x5f8be00?, 0xc000d34f20?, 0x28?, 0xc3?, 0x4020f40?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000d34ea0 sp=0xc000d34e80 pc=0x13bb516
   > runtime.chanrecv(0xc00fb76000, 0xc000d34fa0, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000d34f30 sp=0xc000d34ea0 pc=0x13854bb
   > runtime.chanrecv1(0x0?, 0xc00fa4dcb0?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc000d34f58 sp=0xc000d34f30 pc=0x1384fb8
   > github.com/pingcap/tidb/util/signal.SetupSignalHandler.func1()
   > 	/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:37 +0x4f fp=0xc000d34fe0 sp=0xc000d34f58 pc=0x33ac32f
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000d34fe8 sp=0xc000d34fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/util/signal.SetupSignalHandler
   > 	/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:34 +0xb6
   > goroutine 813 [syscall]:
   > runtime.notetsleepg(0x13c2505?, 0xc0005097d0?)
   > 	/usr/local/go/src/runtime/lock_futex.go:236 +0x34 fp=0xc0005097a0 sp=0xc000509768 pc=0x138acd4
   > os/signal.signal_recv()
   > 	/usr/local/go/src/runtime/sigqueue.go:152 +0x2f fp=0xc0005097c0 sp=0xc0005097a0 pc=0x13ea6cf
   > os/signal.loop()
   > 	/usr/local/go/src/os/signal/signal_unix.go:23 +0x19 fp=0xc0005097e0 sp=0xc0005097c0 pc=0x2cac7f9
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0005097e8 sp=0xc0005097e0 pc=0x13ee6e1
   > created by os/signal.Notify.func1.1
   > 	/usr/local/go/src/os/signal/signal.go:151 +0x2a
   > goroutine 1298 [chan receive]:
   > runtime.gopark(0x13c37d1?, 0xc00009ebb8?, 0x0?, 0x38?, 0xc0121c0770?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00009eba8 sp=0xc00009eb88 pc=0x13bb516
   > runtime.chanrecv(0xc0121c8de0, 0xc00009ecf8, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc00009ec38 sp=0xc00009eba8 pc=0x13854bb
   > runtime.chanrecv2(0xc01221ad80?, 0x400d6b0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc00009ec60 sp=0xc00009ec38 pc=0x1384ff8
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Next(0xc01221ad80, {0x400d6b0?, 0xc0120b97d0?}, 0xc0124a6ff0)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:681 +0x652 fp=0xc00009ed20 sp=0xc00009ec60 pc=0x3064d52
   > github.com/pingcap/tidb/executor.Next({0x400d6b0, 0xc0120b97d0}, {0x40101a0, 0xc01221ad80}, 0xc0124a6ff0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:286 +0x4a8 fp=0xc00009ee60 sp=0xc00009ed20 pc=0x2fef688
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchProbeSideChunks(0xc01221b8c0, {0x400d6b0, 0xc0120b97d0})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:209 +0x1d6 fp=0xc00009ef28 sp=0xc00009ee60 pc=0x30602d6
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:322 +0x8f fp=0xc00009ef90 sp=0xc00009ef28 pc=0x306156f
   > github.com/pingcap/tidb/util.WithRecovery(0x5f539a0?, 0xc00fc10fb8?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc00009efc0 sp=0xc00009ef90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func3()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:320 +0x2a fp=0xc00009efe0 sp=0xc00009efc0 pc=0x30614aa
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00009efe8 sp=0xc00009efe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:320 +0x14f
   > goroutine 815 [chan receive]:
   > runtime.gopark(0xc0103bc7b0?, 0x400d678?, 0x88?, 0xe6?, 0x309a506?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000e6e660 sp=0xc000e6e640 pc=0x13bb516
   > runtime.chanrecv(0xc0002fd1a0, 0xc000e6e780, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000e6e6f0 sp=0xc000e6e660 pc=0x13854bb
   > runtime.chanrecv1(0x0?, 0x309a4e0?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc000e6e718 sp=0xc000e6e6f0 pc=0x1384fb8
   > github.com/pingcap/tidb/util/signal.SetupSignalHandler.func2()
   > 	/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:53 +0x45 fp=0xc000e6e7e0 sp=0xc000e6e718 pc=0x33ac105
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000e6e7e8 sp=0xc000e6e7e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/util/signal.SetupSignalHandler
   > 	/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:52 +0x19f
   > goroutine 1300 [select]:
   > runtime.gopark(0xc0103c6610?, 0x2?, 0xb8?, 0x1d?, 0xc0103c658c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0103c63e0 sp=0xc0103c63c0 pc=0x13bb516
   > runtime.selectgo(0xc0103c6610, 0xc0103c6588, 0x13cb293?, 0x0, 0x13cc174?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0103c6520 sp=0xc0103c63e0 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc01221b8c0, 0x1, {0xc012359cc8, 0x1, 0x1})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:441 +0x4f4 fp=0xc0103c6710 sp=0xc0103c6520 pc=0x30626b4
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:335 +0xb3 fp=0xc0103c6790 sp=0xc0103c6710 pc=0x30613d3
   > github.com/pingcap/tidb/util.WithRecovery(0x23de786?, 0xc0102709c0?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc0103c67c0 sp=0xc0103c6790 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x2a fp=0xc0103c67e0 sp=0xc0103c67c0 pc=0x30612ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0103c67e8 sp=0xc0103c67e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x1c9
   > goroutine 1301 [select]:
   > runtime.gopark(0xc0103c9610?, 0x2?, 0xc0?, 0x1d?, 0xc0103c958c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0111f6be0 sp=0xc0111f6bc0 pc=0x13bb516
   > runtime.selectgo(0xc0111f6e10, 0xc0103c9588, 0xc011413418?, 0x0, 0x13cc174?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0111f6d20 sp=0xc0111f6be0 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc01221b8c0, 0x2, {0xc012359cc8, 0x1, 0x1})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:441 +0x4f4 fp=0xc0111f6f10 sp=0xc0111f6d20 pc=0x30626b4
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:335 +0xb3 fp=0xc0111f6f90 sp=0xc0111f6f10 pc=0x30613d3
   > github.com/pingcap/tidb/util.WithRecovery(0x400d6b0?, 0xc0118bb3e0?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc0111f6fc0 sp=0xc0111f6f90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x2a fp=0xc0111f6fe0 sp=0xc0111f6fc0 pc=0x30612ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0111f6fe8 sp=0xc0111f6fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x1c9
   > goroutine 1314 [select]:
   > runtime.gopark(0xc000091610?, 0x2?, 0x60?, 0x92?, 0xc00009158c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0000913e0 sp=0xc0000913c0 pc=0x13bb516
   > runtime.selectgo(0xc000091610, 0xc000091588, 0xc0114891e8?, 0x0, 0x13cc174?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000091520 sp=0xc0000913e0 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc01221ad80, 0x1, {0xc00fabbca0, 0x1, 0x1})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:441 +0x4f4 fp=0xc000091710 sp=0xc000091520 pc=0x30626b4
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:335 +0xb3 fp=0xc000091790 sp=0xc000091710 pc=0x30613d3
   > github.com/pingcap/tidb/util.WithRecovery(0x400d6b0?, 0xc0122cb590?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc0000917c0 sp=0xc000091790 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x2a fp=0xc0000917e0 sp=0xc0000917c0 pc=0x30612ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000917e8 sp=0xc0000917e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x1c9
   > goroutine 1153 [select]:
   > runtime.gopark(0xc00fc10610?, 0x2?, 0x50?, 0x92?, 0xc00fc1058c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fc103e0 sp=0xc00fc103c0 pc=0x13bb516
   > runtime.selectgo(0xc00fc10610, 0xc00fc10588, 0x0?, 0x0, 0x13cc174?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fc10520 sp=0xc00fc103e0 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc01221ad80, 0x0, {0xc00fabbca0, 0x1, 0x1})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:441 +0x4f4 fp=0xc00fc10710 sp=0xc00fc10520 pc=0x30626b4
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:335 +0xb3 fp=0xc00fc10790 sp=0xc00fc10710 pc=0x30613d3
   > github.com/pingcap/tidb/util.WithRecovery(0x5f539a0?, 0xc00fc107b8?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc00fc107c0 sp=0xc00fc10790 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x2a fp=0xc00fc107e0 sp=0xc00fc107c0 pc=0x30612ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fc107e8 sp=0xc00fc107e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x1c9
   > goroutine 773 [select]:
   > runtime.gopark(0xc0111f8f78?, 0x2?, 0xa0?, 0x8d?, 0xc0111f8eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0111f8d58 sp=0xc0111f8d38 pc=0x13bb516
   > runtime.selectgo(0xc0111f8f78, 0xc0111f8ee8, 0xc011196e00?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0111f8e98 sp=0xc0111f8d58 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc00fa642c0, {0x400d6b0?, 0xc0120b97d0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc0111f8fb8 sp=0xc0111f8e98 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc0111f8fe0 sp=0xc0111f8fb8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0111f8fe8 sp=0xc0111f8fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 1317 [select]:
   > runtime.gopark(0xc010742e10?, 0x2?, 0x90?, 0x92?, 0xc010742d8c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010742be0 sp=0xc010742bc0 pc=0x13bb516
   > runtime.selectgo(0xc010742e10, 0xc010742d88, 0x13cb293?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010742d20 sp=0xc010742be0 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc01221ad80, 0x4, {0xc00fabbca0, 0x1, 0x1})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:441 +0x4f4 fp=0xc010742f10 sp=0xc010742d20 pc=0x30626b4
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:335 +0xb3 fp=0xc010742f90 sp=0xc010742f10 pc=0x30613d3
   > github.com/pingcap/tidb/util.WithRecovery(0x23de786?, 0xc0104e3540?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc010742fc0 sp=0xc010742f90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x2a fp=0xc010742fe0 sp=0xc010742fc0 pc=0x30612ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010742fe8 sp=0xc010742fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x1c9
   > goroutine 1349 [select]:
   > runtime.gopark(0xc000d37778?, 0x2?, 0x6b?, 0xca?, 0xc000d376ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000d37558 sp=0xc000d37538 pc=0x13bb516
   > runtime.selectgo(0xc000d37778, 0xc000d376e8, 0x3aac226?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000d37698 sp=0xc000d37558 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc0106cff00, {0x400d6b0?, 0xc0120b97d0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc000d377b8 sp=0xc000d37698 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc000d377e0 sp=0xc000d377b8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000d377e8 sp=0xc000d377e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 1302 [select]:
   > runtime.gopark(0xc010747610?, 0x2?, 0xc8?, 0x1d?, 0xc01074758c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0111f5be0 sp=0xc0111f5bc0 pc=0x13bb516
   > runtime.selectgo(0xc0111f5e10, 0xc010747588, 0x0?, 0x0, 0x13cc174?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0111f5d20 sp=0xc0111f5be0 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc01221b8c0, 0x3, {0xc012359cc8, 0x1, 0x1})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:441 +0x4f4 fp=0xc0111f5f10 sp=0xc0111f5d20 pc=0x30626b4
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:335 +0xb3 fp=0xc0111f5f90 sp=0xc0111f5f10 pc=0x30613d3
   > github.com/pingcap/tidb/util.WithRecovery(0x0?, 0xc0107476c8?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc0111f5fc0 sp=0xc0111f5f90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x2a fp=0xc0111f5fe0 sp=0xc0111f5fc0 pc=0x30612ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0111f5fe8 sp=0xc0111f5fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x1c9
   > goroutine 1303 [select]:
   > runtime.gopark(0xc010748610?, 0x2?, 0xd0?, 0x1d?, 0xc01074858c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0111f7be0 sp=0xc0111f7bc0 pc=0x13bb516
   > runtime.selectgo(0xc0111f7e10, 0xc010748588, 0xc011412aa0?, 0x0, 0x13cc174?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0111f7d20 sp=0xc0111f7be0 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc01221b8c0, 0x4, {0xc012359cc8, 0x1, 0x1})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:441 +0x4f4 fp=0xc0111f7f10 sp=0xc0111f7d20 pc=0x30626b4
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:335 +0xb3 fp=0xc0111f7f90 sp=0xc0111f7f10 pc=0x30613d3
   > github.com/pingcap/tidb/util.WithRecovery(0x400d6b0?, 0xc0005c7590?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc0111f7fc0 sp=0xc0111f7f90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x2a fp=0xc0111f7fe0 sp=0xc0111f7fc0 pc=0x30612ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0111f7fe8 sp=0xc0111f7fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x1c9
   > goroutine 1304 [semacquire]:
   > runtime.gopark(0x916f4b4700000000?, 0xc010748ea0?, 0x80?, 0x90?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010748e78 sp=0xc010748e58 pc=0x13bb516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc01221bab8, 0xb8?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc010748ee0 sp=0xc010748e78 pc=0x13cce5e
   > sync.runtime_Semacquire(0x0?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc010748f10 sp=0xc010748ee0 pc=0x13e9f65
   > sync.(*WaitGroup).Wait(0xc010748fa8?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc010748f38 sp=0xc010748f10 pc=0x13fd1f2
   > github.com/pingcap/tidb/executor.(*HashJoinExec).waitJoinWorkersAndCloseResultChan(0xc01221b8c0)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:395 +0x33 fp=0xc010748f78 sp=0xc010748f38 pc=0x3061fb3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).waitJoinWorkersAndCloseResultChan-fm()
   > 	<autogenerated>:1 +0x26 fp=0xc010748f90 sp=0xc010748f78 pc=0x31277c6
   > github.com/pingcap/tidb/util.WithRecovery(0x400d6b0?, 0xc011b1f080?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc010748fc0 sp=0xc010748f90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:338 +0x28 fp=0xc010748fe0 sp=0xc010748fc0 pc=0x3061288
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010748fe8 sp=0xc010748fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:338 +0x3b8
   > goroutine 1350 [select]:
   > runtime.gopark(0xc0121ea778?, 0x2?, 0x0?, 0x0?, 0xc0121ea6ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0121ea558 sp=0xc0121ea538 pc=0x13bb516
   > runtime.selectgo(0xc0121ea778, 0xc0121ea6e8, 0x3aac226?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0121ea698 sp=0xc0121ea558 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc0106cff40, {0x400d6b0?, 0xc0120b97d0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc0121ea7b8 sp=0xc0121ea698 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc0121ea7e0 sp=0xc0121ea7b8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0121ea7e8 sp=0xc0121ea7e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 1351 [select]:
   > runtime.gopark(0xc0121eaf78?, 0x2?, 0x0?, 0x0?, 0xc0121eaeec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0121ead58 sp=0xc0121ead38 pc=0x13bb516
   > runtime.selectgo(0xc0121eaf78, 0xc0121eaee8, 0x3aac226?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0121eae98 sp=0xc0121ead58 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc0106cff80, {0x400d6b0?, 0xc0120b97d0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc0121eafb8 sp=0xc0121eae98 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc0121eafe0 sp=0xc0121eafb8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0121eafe8 sp=0xc0121eafe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 1352 [select]:
   > runtime.gopark(0xc0121eb778?, 0x2?, 0x0?, 0x0?, 0xc0121eb6ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0121eb558 sp=0xc0121eb538 pc=0x13bb516
   > runtime.selectgo(0xc0121eb778, 0xc0121eb6e8, 0x3aac226?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0121eb698 sp=0xc0121eb558 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc0106cffc0, {0x400d6b0?, 0xc0120b97d0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc0121eb7b8 sp=0xc0121eb698 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc0121eb7e0 sp=0xc0121eb7b8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0121eb7e8 sp=0xc0121eb7e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 1353 [select]:
   > runtime.gopark(0xc0121ebf78?, 0x2?, 0x0?, 0x0?, 0xc0121ebeec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0121ebd58 sp=0xc0121ebd38 pc=0x13bb516
   > runtime.selectgo(0xc0121ebf78, 0xc0121ebee8, 0x3aac226?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0121ebe98 sp=0xc0121ebd58 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc00fd94140, {0x400d6b0?, 0xc0120b97d0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc0121ebfb8 sp=0xc0121ebe98 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc0121ebfe0 sp=0xc0121ebfb8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0121ebfe8 sp=0xc0121ebfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
