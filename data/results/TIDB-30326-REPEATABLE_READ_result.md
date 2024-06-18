# Bug ID TIDB-30326-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/30326
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ


## Details
 * Database: tidb-v5.4.0-local
 * Number of scenarios: 1
 * Initial setup script: /home/theodor/Projects/MasterThesis/data/sql/TIDB-30326_mysql_bk.sql

## Results
### Scenario 0
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  WITH cte_0 AS (select 1 as c1, (FIRST_VALUE(1) over (partition by subq_0.c0) < ...
     - TID: 0
     - Output: ERROR: 2013 (HY000): Lost connection to MySQL server during query

 * Container logs:
   > [2024/06/18 13:42:16.370 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=53] [user=root] [host=]
   > [2024/06/18 13:42:16.373 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=53] [schemaVersion=197] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/06/18 13:42:16.374 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:220, Type:drop schema, State:none, SchemaState:queueing, SchemaID:215, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:16.373 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 13:42:16.374 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:220, Type:drop schema, State:none, SchemaState:queueing, SchemaID:215, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:16.373 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/06/18 13:42:16.374 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:220, Type:drop schema, State:none, SchemaState:queueing, SchemaID:215, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:16.373 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:16.375 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=197] [neededSchemaVersion=198] ["start time"=92.331µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 13:42:16.377 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=198] ["take time"=2.128158ms] [job="ID:220, Type:drop schema, State:running, SchemaState:write only, SchemaID:215, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:16.373 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:16.378 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:220, Type:drop schema, State:running, SchemaState:write only, SchemaID:215, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:16.373 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:16.379 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=198] [neededSchemaVersion=199] ["start time"=76.966µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 13:42:16.381 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=199] ["take time"=2.267213ms] [job="ID:220, Type:drop schema, State:running, SchemaState:delete only, SchemaID:215, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:16.373 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:16.381 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:220, Type:drop schema, State:running, SchemaState:delete only, SchemaID:215, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:16.373 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:16.382 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=199] [neededSchemaVersion=200] ["start time"=82.903µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 13:42:16.384 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=200] ["take time"=2.266026ms] [job="ID:220, Type:drop schema, State:done, SchemaState:queueing, SchemaID:215, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:16.373 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:16.385 +00:00] [INFO] [delete_range.go:107] ["[ddl] add job into delete-range table"] [jobID=220] [jobType="drop schema"]
   > [2024/06/18 13:42:16.385 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:220, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:215, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:16.373 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:16.385 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=220]
   > [2024/06/18 13:42:16.385 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 13:42:16.387 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=53] [schemaVersion=200] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/06/18 13:42:16.388 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:222, Type:create schema, State:none, SchemaState:queueing, SchemaID:221, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 13:42:16.388 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 13:42:16.388 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:222, Type:create schema, State:none, SchemaState:queueing, SchemaID:221, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 13:42:16.388 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/18 13:42:16.389 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:222, Type:create schema, State:none, SchemaState:queueing, SchemaID:221, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:16.388 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:16.390 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=200] [neededSchemaVersion=201] ["start time"=157.913µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 13:42:16.392 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=201] ["take time"=2.247936ms] [job="ID:222, Type:create schema, State:done, SchemaState:public, SchemaID:221, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 13:42:16.388 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:16.392 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:222, Type:create schema, State:synced, SchemaState:public, SchemaID:221, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:16.388 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:16.393 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=222]
   > [2024/06/18 13:42:16.393 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 13:42:16.400 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=53] [schemaVersion=201] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_037irb`\n--\n\nDROP TABLE IF EXISTS `t_037irb`;"] [user=root@127.0.0.1]
   > [2024/06/18 13:42:16.400 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=53] [schemaVersion=201] [cur_db=testdb] [sql="CREATE TABLE `t_037irb` (\n  `c_nrh3o` int(11) DEFAULT NULL,\n  `c_nfauxb` text DEFAULT NULL,\n  `c_y5n4c` int(11) DEFAULT NULL,\n  `c_j9alg` double NOT NULL,\n  `c_4vix1d` text DEFAULT NULL,\n  `c_glkxdb` text DEFAULT NULL,\n  `c_2ykt0d` int(11) DEFAULT NULL,\n  `c_5fxv3c` double DEFAULT NULL,\n  PRIMARY KEY (`c_j9alg`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/06/18 13:42:16.402 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:224, Type:create table, State:none, SchemaState:queueing, SchemaID:221, TableID:223, RowCount:0, ArgLen:1, start time: 2024-06-18 13:42:16.401 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 13:42:16.402 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:224, Type:create table, State:none, SchemaState:queueing, SchemaID:221, TableID:223, RowCount:0, ArgLen:1, start time: 2024-06-18 13:42:16.401 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_037irb` (\n  `c_nrh3o` int(11) DEFAULT NULL,\n  `c_nfauxb` text DEFAULT NULL,\n  `c_y5n4c` int(11) DEFAULT NULL,\n  `c_j9alg` double NOT NULL,\n  `c_4vix1d` text DEFAULT NULL,\n  `c_glkxdb` text DEFAULT NULL,\n  `c_2ykt0d` int(11) DEFAULT NULL,\n  `c_5fxv3c` double DEFAULT NULL,\n  PRIMARY KEY (`c_j9alg`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/18 13:42:16.403 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:224, Type:create table, State:none, SchemaState:queueing, SchemaID:221, TableID:223, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:16.401 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:16.405 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=201] [neededSchemaVersion=202] ["start time"=444.126µs] [phyTblIDs="[223]"] [actionTypes="[8]"]
   > [2024/06/18 13:42:16.407 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=202] ["take time"=2.06502ms] [job="ID:224, Type:create table, State:done, SchemaState:public, SchemaID:221, TableID:223, RowCount:0, ArgLen:1, start time: 2024-06-18 13:42:16.401 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:16.408 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:224, Type:create table, State:synced, SchemaState:public, SchemaID:221, TableID:223, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:16.401 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:16.409 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=224]
   > [2024/06/18 13:42:16.409 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 13:42:16.409 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=102] ["first split key"=7480000000000000df]
   > [2024/06/18 13:42:16.410 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=102] ["first at"=7480000000000000df] ["first new region left"="{Id:102 StartKey:7480000000000000ffd900000000000000f8 EndKey:7480000000000000ffdf00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:103 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/18 13:42:16.410 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[102]"]
   > [2024/06/18 13:42:16.410 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=53] [schemaVersion=202] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_037irb` DISABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/06/18 13:42:16.411 +00:00] [WARN] [2pc.go:1596] ["schemaLeaseChecker is not set for this transaction"] [sessionID=53] [startTS=450551647151063043] [commitTS=450551647151325184]
   > [2024/06/18 13:42:16.412 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=53] [schemaVersion=202] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_037irb` ENABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/06/18 13:42:16.413 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=53] [schemaVersion=202] [cur_db=testdb] [sql="\n--\n-- Temporary view structure for view `t_cpsvpb`\n--\n\nDROP TABLE IF EXISTS `t_cpsvpb`;"] [user=root@127.0.0.1]
   > [2024/06/18 13:42:16.413 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=53] [schemaVersion=202] [cur_db=testdb] [sql="/*!50001 DROP VIEW IF EXISTS `t_cpsvpb`*/;"] [user=root@127.0.0.1]
   > [2024/06/18 13:42:16.415 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:226, Type:create view, State:none, SchemaState:queueing, SchemaID:221, TableID:225, RowCount:0, ArgLen:3, start time: 2024-06-18 13:42:16.414 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 13:42:16.415 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:226, Type:create view, State:none, SchemaState:queueing, SchemaID:221, TableID:225, RowCount:0, ArgLen:3, start time: 2024-06-18 13:42:16.414 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="/*!50001 CREATE VIEW `t_cpsvpb` AS SELECT \n 1 AS `c0`,\n 1 AS `c2`,\n 1 AS `c3`,\n 1 AS `c4`,\n 1 AS `c5`,\n 1 AS `c6`,\n 1 AS `c7`,\n 1 AS `c8`,\n 1 AS `c9`,\n 1 AS `c10`,\n 1 AS `c11`,\n 1 AS `c12`,\n 1 AS `c13`,\n 1 AS `c14`*/;"]
   > [2024/06/18 13:42:16.416 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:226, Type:create view, State:none, SchemaState:queueing, SchemaID:221, TableID:225, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:16.414 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:16.419 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=202] [neededSchemaVersion=203] ["start time"=608.464µs] [phyTblIDs="[225]"] [actionTypes="[2097152]"]
   > [2024/06/18 13:42:16.421 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=203] ["take time"=2.235575ms] [job="ID:226, Type:create view, State:done, SchemaState:public, SchemaID:221, TableID:225, RowCount:0, ArgLen:3, start time: 2024-06-18 13:42:16.414 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:16.422 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:226, Type:create view, State:synced, SchemaState:public, SchemaID:221, TableID:225, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:16.414 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:16.423 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=226]
   > [2024/06/18 13:42:16.423 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 13:42:16.424 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=53] [schemaVersion=203] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_x7zqmd`\n--\n\nDROP TABLE IF EXISTS `t_x7zqmd`;"] [user=root@127.0.0.1]
   > [2024/06/18 13:42:16.425 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=53] [schemaVersion=203] [cur_db=testdb] [sql="CREATE TABLE `t_x7zqmd` (\n  `c_8weeq` int(11) NOT NULL,\n  `c_13sfid` double DEFAULT NULL,\n  `c_hhjlmc` text DEFAULT NULL,\n  `c_3b1zld` int(11) DEFAULT NULL,\n  `c_6tu8wd` int(11) DEFAULT NULL,\n  `c_jyc_cd` double DEFAULT NULL,\n  PRIMARY KEY (`c_8weeq`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/06/18 13:42:16.426 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:228, Type:create table, State:none, SchemaState:queueing, SchemaID:221, TableID:227, RowCount:0, ArgLen:1, start time: 2024-06-18 13:42:16.425 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 13:42:16.426 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:228, Type:create table, State:none, SchemaState:queueing, SchemaID:221, TableID:227, RowCount:0, ArgLen:1, start time: 2024-06-18 13:42:16.425 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_x7zqmd` (\n  `c_8weeq` int(11) NOT NULL,\n  `c_13sfid` double DEFAULT NULL,\n  `c_hhjlmc` text DEFAULT NULL,\n  `c_3b1zld` int(11) DEFAULT NULL,\n  `c_6tu8wd` int(11) DEFAULT NULL,\n  `c_jyc_cd` double DEFAULT NULL,\n  PRIMARY KEY (`c_8weeq`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/18 13:42:16.427 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:228, Type:create table, State:none, SchemaState:queueing, SchemaID:221, TableID:227, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:16.425 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:16.429 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=203] [neededSchemaVersion=204] ["start time"=369.744µs] [phyTblIDs="[227]"] [actionTypes="[8]"]
   > [2024/06/18 13:42:16.430 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=204] ["take time"=2.048049ms] [job="ID:228, Type:create table, State:done, SchemaState:public, SchemaID:221, TableID:227, RowCount:0, ArgLen:1, start time: 2024-06-18 13:42:16.425 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:16.431 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:228, Type:create table, State:synced, SchemaState:public, SchemaID:221, TableID:227, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:16.425 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:16.432 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=228]
   > [2024/06/18 13:42:16.432 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 13:42:16.433 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=104] ["first split key"=7480000000000000e3]
   > [2024/06/18 13:42:16.433 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=104] ["first at"=7480000000000000e3] ["first new region left"="{Id:104 StartKey:7480000000000000ffdf00000000000000f8 EndKey:7480000000000000ffe300000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:105 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/18 13:42:16.433 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[104]"]
   > [2024/06/18 13:42:16.433 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=53] [schemaVersion=204] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_x7zqmd` DISABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/06/18 13:42:16.436 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=53] [schemaVersion=204] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_x7zqmd` ENABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/06/18 13:42:16.436 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=53] [schemaVersion=204] [cur_db=testdb] [sql="\n--\n-- Final view structure for view `t_cpsvpb`\n--\n\n/*!50001 DROP VIEW IF EXISTS `t_cpsvpb`*/;"] [user=root@127.0.0.1]
   > [2024/06/18 13:42:16.437 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:229, Type:drop view, State:none, SchemaState:queueing, SchemaID:221, TableID:225, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:16.436 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 13:42:16.437 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:229, Type:drop view, State:none, SchemaState:queueing, SchemaID:221, TableID:225, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:16.436 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="\n--\n-- Final view structure for view `t_cpsvpb`\n--\n\n/*!50001 DROP VIEW IF EXISTS `t_cpsvpb`*/;"]
   > [2024/06/18 13:42:16.437 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:229, Type:drop view, State:none, SchemaState:queueing, SchemaID:221, TableID:225, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:16.436 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:16.439 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=204] [neededSchemaVersion=205] ["start time"=90.167µs] [phyTblIDs="[225]"] [actionTypes="[16777216]"]
   > [2024/06/18 13:42:16.441 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=205] ["take time"=2.289353ms] [job="ID:229, Type:drop view, State:running, SchemaState:write only, SchemaID:221, TableID:225, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:16.436 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:16.441 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:229, Type:drop view, State:running, SchemaState:write only, SchemaID:221, TableID:225, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:16.436 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:16.443 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=205] [neededSchemaVersion=206] ["start time"=96.871µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 13:42:16.445 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=206] ["take time"=2.677255ms] [job="ID:229, Type:drop view, State:running, SchemaState:delete only, SchemaID:221, TableID:225, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:16.436 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:16.446 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:229, Type:drop view, State:running, SchemaState:delete only, SchemaID:221, TableID:225, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:16.436 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:16.448 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=206] [neededSchemaVersion=207] ["start time"=81.436µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 13:42:16.450 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=207] ["take time"=2.627249ms] [job="ID:229, Type:drop view, State:done, SchemaState:queueing, SchemaID:221, TableID:225, RowCount:0, ArgLen:3, start time: 2024-06-18 13:42:16.436 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:16.451 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:229, Type:drop view, State:synced, SchemaState:queueing, SchemaID:221, TableID:225, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:16.436 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:16.452 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=229]
   > [2024/06/18 13:42:16.452 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 13:42:16.457 +00:00] [INFO] [session.go:2108] ["Try to create a new txn inside a transaction auto commit"] [conn=53] [schemaVersion=207] [txnStartTS=450551647162597376] [txnScope=global]
   > [2024/06/18 13:42:16.459 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:231, Type:create view, State:none, SchemaState:queueing, SchemaID:221, TableID:230, RowCount:0, ArgLen:3, start time: 2024-06-18 13:42:16.458 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 13:42:16.459 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:231, Type:create view, State:none, SchemaState:queueing, SchemaID:221, TableID:230, RowCount:0, ArgLen:3, start time: 2024-06-18 13:42:16.458 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="/*!50001 CREATE ALGORITHM=UNDEFINED */\n/*!50013 DEFINER=`root`@`127.0.0.1` SQL SECURITY DEFINER */\n/*!50001 VIEW `t_cpsvpb` (`c0`, `c2`, `c3`, `c4`, `c5`, `c6`, `c7`, `c8`, `c9`, `c10`, `c11`, `c12`, `c13`, `c14`) AS SELECT DISTINCT `subq_0`.`c1` AS `c0`,`subq_0`.`c2` AS `c2`,8 AS `c3`,CASE WHEN (`subq_0`.`c3` NOT IN (SELECT `ref_2`.`c_4vix1d` AS `c0` FROM `testdb`.`t_037irb` AS `ref_2` WHERE `ref_2`.`c_2ykt0d`<=`ref_2`.`c_nrh3o`)) AND (`subq_0`.`c3`<=(SELECT (SELECT `c_hhjlmc` AS `c_hhjlmc` FROM `testdb`.`t_x7zqmd` ORDER BY `c_hhjlmc` LIMIT 4,1) AS `c0` FROM `testdb`.`t_037irb` AS `ref_3` WHERE `subq_0`.`c1`!=`ref_3`.`c_2ykt0d`)) THEN `subq_0`.`c3` ELSE `subq_0`.`c3` END AS `c4`,CASE WHEN `subq_0`.`c1`>=(SELECT MAX(`c_8weeq`) AS `max(c_8weeq)` FROM `testdb`.`t_x7zqmd`) THEN `subq_0`.`c2` ELSE `subq_0`.`c2` END AS `c5`,`subq_0`.`c1` AS `c6`,`subq_0`.`c2` AS `c7`,`subq_0`.`c3` AS `c8`,`subq_0`.`c3` AS `c9`,`subq_0`.`c2` AS `c10`,`subq_0`.`c4` AS `c11`,COUNT(CAST(`subq_0`.`c2` AS DOUBLE)) OVER (PARTITION BY `subq_0`.`c4` ORDER BY `subq_0`.`c1`) AS `c12`,`subq_0`.`c3` AS `c13`,CAST(COALESCE(`subq_0`.`c3`, _UTF8MB4'9sx3k') AS CHAR) AS `c14` FROM (SELECT COUNT(CAST(`ref_1`.`c_jyc_cd` AS DOUBLE)) AS `c0`,AVG(CAST(`ref_1`.`c_3b1zld` AS SIGNED)) AS `c1`,MIN(CAST(`ref_1`.`c_jyc_cd` AS DOUBLE)) AS `c2`,`ref_0`.`c_glkxdb` AS `c3`,COUNT(CAST(`ref_1`.`c_13sfid` AS DOUBLE)) AS `c4` FROM `testdb`.`t_037irb` AS `ref_0` JOIN `testdb`.`t_x7zqmd` AS `ref_1` WHERE `ref_0`.`c_nrh3o`>`ref_1`.`c_8weeq` GROUP BY `ref_0`.`c_glkxdb`) AS `subq_0` WHERE (SELECT `c_8weeq` AS `c_8weeq` FROM `testdb`.`t_x7zqmd` ORDER BY `c_8weeq` LIMIT 2,1) IS NOT NULL */;"]
   > [2024/06/18 13:42:16.460 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:231, Type:create view, State:none, SchemaState:queueing, SchemaID:221, TableID:230, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:16.458 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:16.463 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=207] [neededSchemaVersion=208] ["start time"=551.263µs] [phyTblIDs="[230]"] [actionTypes="[2097152]"]
   > [2024/06/18 13:42:16.465 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=208] ["take time"=2.393697ms] [job="ID:231, Type:create view, State:done, SchemaState:public, SchemaID:221, TableID:230, RowCount:0, ArgLen:3, start time: 2024-06-18 13:42:16.458 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:16.466 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:231, Type:create view, State:synced, SchemaState:public, SchemaID:221, TableID:230, RowCount:0, ArgLen:0, start time: 2024-06-18 13:42:16.458 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:42:16.468 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=231]
   > [2024/06/18 13:42:16.468 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 13:42:17.556 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=55] [user=root] [host=]
   > [2024/06/18 13:42:17.572 +00:00] [INFO] [set.go:139] ["set global var"] [conn=55] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/06/18 13:42:17.797 +00:00] [ERROR] [misc.go:95] ["panic in the recoverable goroutine"] [r="\"invalid memory address or nil pointer dereference\""] ["stack trace"="github.com/pingcap/tidb/util.WithRecovery.func1\n\t/go/src/github.com/pingcap/tidb/util/misc.go:97\nruntime.gopanic\n\t/usr/local/go/src/runtime/panic.go:884\nruntime.panicmem\n\t/usr/local/go/src/runtime/panic.go:260\nruntime.sigpanic\n\t/usr/local/go/src/runtime/signal_unix.go:839\ngithub.com/pingcap/tidb/executor.(*vecGroupChecker).splitIntoGroups\n\t/go/src/github.com/pingcap/tidb/executor/aggregate.go:1457\ngithub.com/pingcap/tidb/executor.(*PipelinedWindowExec).getRowsInPartition\n\t/go/src/github.com/pingcap/tidb/executor/pipelined_window.go:189\ngithub.com/pingcap/tidb/executor.(*PipelinedWindowExec).Next\n\t/go/src/github.com/pingcap/tidb/executor/pipelined_window.go:125\ngithub.com/pingcap/tidb/executor.Next\n\t/go/src/github.com/pingcap/tidb/executor/executor.go:286\ngithub.com/pingcap/tidb/executor.(*ProjectionExec).unParallelExecute\n\t/go/src/github.com/pingcap/tidb/executor/projection.go:194\ngithub.com/pingcap/tidb/executor.(*ProjectionExec).Next\n\t/go/src/github.com/pingcap/tidb/executor/projection.go:180\ngithub.com/pingcap/tidb/executor.Next\n\t/go/src/github.com/pingcap/tidb/executor/executor.go:286\ngithub.com/pingcap/tidb/executor.(*CTEExec).computeSeedPart\n\t/go/src/github.com/pingcap/tidb/executor/cte.go:226\ngithub.com/pingcap/tidb/executor.(*CTEExec).Next\n\t/go/src/github.com/pingcap/tidb/executor/cte.go:161\ngithub.com/pingcap/tidb/executor.Next\n\t/go/src/github.com/pingcap/tidb/executor/executor.go:286\ngithub.com/pingcap/tidb/executor.(*SelectionExec).Next\n\t/go/src/github.com/pingcap/tidb/executor/executor.go:1317\ngithub.com/pingcap/tidb/executor.Next\n\t/go/src/github.com/pingcap/tidb/executor/executor.go:286\ngithub.com/pingcap/tidb/executor.(*HashJoinExec).fetchBuildSideRows\n\t/go/src/github.com/pingcap/tidb/executor/join.go:266\ngithub.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable.func2\n\t/go/src/github.com/pingcap/tidb/executor/join.go:715\ngithub.com/pingcap/tidb/util.WithRecovery\n\t/go/src/github.com/pingcap/tidb/util/misc.go:100"]
   > runtime: goroutine stack exceeds 1000000000-byte limit
   > runtime: sp=0xc03c080390 stack=[0xc03c080000, 0xc05c080000]
   > fatal error: stack overflow
   > runtime stack:
   > runtime.throw({0x3aa773d?, 0x590b5c0?})
   > 	/usr/local/go/src/runtime/panic.go:1047 +0x5d fp=0x7fc5dc951888 sp=0x7fc5dc951858 pc=0x13b859d
   > runtime.newstack()
   > 	/usr/local/go/src/runtime/stack.go:1103 +0x5cc fp=0x7fc5dc951a40 sp=0x7fc5dc951888 pc=0x13d35ec
   > runtime.morestack()
   > 	/usr/local/go/src/runtime/asm_amd64.s:570 +0x8b fp=0x7fc5dc951a48 sp=0x7fc5dc951a40 pc=0x13ec60b
   > goroutine 5113 [running]:
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60?, 0xc01222bbc0?}, {0x4012e60?, 0xc01222bc20?})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:183 +0x12c fp=0xc03c0803a0 sp=0xc03c080398 pc=0x1f5780c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01ba509c0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c0803d8 sp=0xc03c0803a0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01accae40}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080410 sp=0xc03c0803d8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01c73f230}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080448 sp=0xc03c080410 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01c37a2c0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080480 sp=0xc03c080448 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01c6ec2f0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c0804b8 sp=0xc03c080480 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01c2e14c0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c0804f0 sp=0xc03c0804b8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01be3ad60}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080528 sp=0xc03c0804f0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01b63baa0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080560 sp=0xc03c080528 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0003bfeb0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080598 sp=0xc03c080560 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01ae84f60}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c0805d0 sp=0xc03c080598 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01222bc20}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080608 sp=0xc03c0805d0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01222bbc0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080640 sp=0xc03c080608 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01ba509c0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080678 sp=0xc03c080640 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01accae40}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c0806b0 sp=0xc03c080678 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01c73f230}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c0806e8 sp=0xc03c0806b0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01c37a2c0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080720 sp=0xc03c0806e8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01c6ec2f0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080758 sp=0xc03c080720 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01c2e14c0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080790 sp=0xc03c080758 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01be3ad60}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c0807c8 sp=0xc03c080790 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01b63baa0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080800 sp=0xc03c0807c8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0003bfeb0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080838 sp=0xc03c080800 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01ae84f60}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080870 sp=0xc03c080838 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01222bc20}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c0808a8 sp=0xc03c080870 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01222bbc0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c0808e0 sp=0xc03c0808a8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01ba509c0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080918 sp=0xc03c0808e0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01accae40}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080950 sp=0xc03c080918 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01c73f230}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080988 sp=0xc03c080950 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01c37a2c0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c0809c0 sp=0xc03c080988 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01c6ec2f0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c0809f8 sp=0xc03c0809c0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01c2e14c0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080a30 sp=0xc03c0809f8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01be3ad60}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080a68 sp=0xc03c080a30 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01b63baa0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080aa0 sp=0xc03c080a68 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0003bfeb0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080ad8 sp=0xc03c080aa0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01ae84f60}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080b10 sp=0xc03c080ad8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01222bc20}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080b48 sp=0xc03c080b10 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01222bbc0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080b80 sp=0xc03c080b48 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01ba509c0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080bb8 sp=0xc03c080b80 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01accae40}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080bf0 sp=0xc03c080bb8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01c73f230}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080c28 sp=0xc03c080bf0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01c37a2c0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080c60 sp=0xc03c080c28 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01c6ec2f0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080c98 sp=0xc03c080c60 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01c2e14c0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080cd0 sp=0xc03c080c98 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01be3ad60}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080d08 sp=0xc03c080cd0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01b63baa0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080d40 sp=0xc03c080d08 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0003bfeb0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080d78 sp=0xc03c080d40 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01ae84f60}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080db0 sp=0xc03c080d78 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01222bc20}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080de8 sp=0xc03c080db0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01222bbc0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080e20 sp=0xc03c080de8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01ba509c0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080e58 sp=0xc03c080e20 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01accae40}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080e90 sp=0xc03c080e58 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01c73f230}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080ec8 sp=0xc03c080e90 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01c37a2c0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080f00 sp=0xc03c080ec8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01c6ec2f0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080f38 sp=0xc03c080f00 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01c2e14c0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080f70 sp=0xc03c080f38 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01be3ad60}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080fa8 sp=0xc03c080f70 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01b63baa0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c080fe0 sp=0xc03c080fa8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0003bfeb0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c081018 sp=0xc03c080fe0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01ae84f60}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c081050 sp=0xc03c081018 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01222bc20}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c081088 sp=0xc03c081050 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01222bbc0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c0810c0 sp=0xc03c081088 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01ba509c0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c0810f8 sp=0xc03c0810c0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01accae40}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c081130 sp=0xc03c0810f8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01c73f230}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c081168 sp=0xc03c081130 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01c37a2c0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c0811a0 sp=0xc03c081168 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01c6ec2f0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c0811d8 sp=0xc03c0811a0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01c2e14c0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c081210 sp=0xc03c0811d8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01be3ad60}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c081248 sp=0xc03c081210 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01b63baa0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c081280 sp=0xc03c081248 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0003bfeb0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c0812b8 sp=0xc03c081280 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01ae84f60}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c0812f0 sp=0xc03c0812b8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01222bc20}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c081328 sp=0xc03c0812f0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01222bbc0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c081360 sp=0xc03c081328 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01ba509c0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c081398 sp=0xc03c081360 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01accae40}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c0813d0 sp=0xc03c081398 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01c73f230}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c081408 sp=0xc03c0813d0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01c37a2c0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c081440 sp=0xc03c081408 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01c6ec2f0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c081478 sp=0xc03c081440 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01c2e14c0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c0814b0 sp=0xc03c081478 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01be3ad60}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c0814e8 sp=0xc03c0814b0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01b63baa0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c081520 sp=0xc03c0814e8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0003bfeb0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c081558 sp=0xc03c081520 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01ae84f60}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c081590 sp=0xc03c081558 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01222bc20}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c0815c8 sp=0xc03c081590 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01222bbc0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c081600 sp=0xc03c0815c8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01ba509c0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c081638 sp=0xc03c081600 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01accae40}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c081670 sp=0xc03c081638 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01c73f230}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c0816a8 sp=0xc03c081670 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01c37a2c0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c0816e0 sp=0xc03c0816a8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01c6ec2f0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c081718 sp=0xc03c0816e0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01c2e14c0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c081750 sp=0xc03c081718 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01be3ad60}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c081788 sp=0xc03c081750 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01b63baa0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c0817c0 sp=0xc03c081788 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc0003bfeb0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c0817f8 sp=0xc03c0817c0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01ae84f60}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c081830 sp=0xc03c0817f8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01222bc20}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c081868 sp=0xc03c081830 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01222bbc0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c0818a0 sp=0xc03c081868 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01ba509c0}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c0818d8 sp=0xc03c0818a0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01accae40}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c081910 sp=0xc03c0818d8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01c73f230}, {0x4012e60, 0xc01222bc20})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03c081948 sp=0xc03c081910 pc=0x1f577a5
   > ...additional frames elided...
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:712 +0x22d
   > goroutine 1 [chan receive]:
   > runtime.gopark(0xc0112d75b0?, 0xc000e7fdc0?, 0xbf?, 0xc1?, 0x37fc5c0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fe89d40 sp=0xc00fe89d20 pc=0x13bb516
   > runtime.chanrecv(0xc010e15560, 0xc000e7fe30, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc00fe89dd0 sp=0xc00fe89d40 pc=0x13854bb
   > runtime.chanrecv1(0xc0113456c0?, 0x0?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc00fe89df8 sp=0xc00fe89dd0 pc=0x1384fb8
   > github.com/pingcap/tidb/server.(*Server).Run(0xc0113456c0)
   > 	/go/src/github.com/pingcap/tidb/server/server.go:370 +0x1f0 fp=0xc00fe89e50 sp=0xc00fe89df8 pc=0x31e23d0
   > main.main()
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:213 +0x539 fp=0xc00fe89f80 sp=0xc00fe89e50 pc=0x33af4b9
   > runtime.main()
   > 	/usr/local/go/src/runtime/proc.go:250 +0x212 fp=0xc00fe89fe0 sp=0xc00fe89f80 pc=0x13bb152
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fe89fe8 sp=0xc00fe89fe0 pc=0x13ee6e1
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
   > runtime.gopark(0xc0000c0000?, 0x3fe2f28?, 0x0?, 0x0?, 0x0?)
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
   > goroutine 18 [GC worker (idle)]:
   > runtime.gopark(0x3ad7042cba48?, 0x3?, 0x5e?, 0xd?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008a750 sp=0xc00008a730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008a7e0 sp=0xc00008a750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008a7e8 sp=0xc00008a7e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 19 [GC worker (idle)]:
   > runtime.gopark(0x3ad7042c5628?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008af50 sp=0xc00008af30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008afe0 sp=0xc00008af50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008afe8 sp=0xc00008afe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 34 [GC worker (idle)]:
   > runtime.gopark(0x3ad7042cba48?, 0x1?, 0x7f?, 0x80?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000508750 sp=0xc000508730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0005087e0 sp=0xc000508750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0005087e8 sp=0xc0005087e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 35 [GC worker (idle)]:
   > runtime.gopark(0x5f8be00?, 0x1?, 0xd3?, 0xc?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000508f50 sp=0xc000508f30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc000508fe0 sp=0xc000508f50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000508fe8 sp=0xc000508fe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 7 [GC worker (idle)]:
   > runtime.gopark(0x3ad704321691?, 0x1?, 0x62?, 0x44?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000090f50 sp=0xc000090f30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc000090fe0 sp=0xc000090f50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000090fe8 sp=0xc000090fe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 20 [GC worker (idle)]:
   > runtime.gopark(0x3ad7042c5628?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008b750 sp=0xc00008b730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008b7e0 sp=0xc00008b750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008b7e8 sp=0xc00008b7e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 36 [GC worker (idle)]:
   > runtime.gopark(0x5f8be00?, 0x1?, 0xd3?, 0x39?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000509750 sp=0xc000509730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0005097e0 sp=0xc000509750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0005097e8 sp=0xc0005097e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 21 [GC worker (idle)]:
   > runtime.gopark(0x3ad7042c68fb?, 0x3?, 0x5e?, 0x7?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008bf50 sp=0xc00008bf30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008bfe0 sp=0xc00008bf50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008bfe8 sp=0xc00008bfe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 37 [GC worker (idle)]:
   > runtime.gopark(0x3ad7043b34d2?, 0x1?, 0xaf?, 0x67?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000509f50 sp=0xc000509f30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc000509fe0 sp=0xc000509f50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000509fe8 sp=0xc000509fe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 8 [GC worker (idle)]:
   > runtime.gopark(0x3ad7042c9eba?, 0x1?, 0xc1?, 0x4a?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000091750 sp=0xc000091730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0000917e0 sp=0xc000091750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000917e8 sp=0xc0000917e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 22 [GC worker (idle)]:
   > runtime.gopark(0x3ad7042c68fb?, 0x3?, 0x47?, 0x9?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008c750 sp=0xc00008c730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008c7e0 sp=0xc00008c750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008c7e8 sp=0xc00008c7e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 38 [GC worker (idle)]:
   > runtime.gopark(0x3ad70432217b?, 0x3?, 0xad?, 0x9f?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00050a750 sp=0xc00050a730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00050a7e0 sp=0xc00050a750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00050a7e8 sp=0xc00050a7e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 9 [GC worker (idle)]:
   > runtime.gopark(0x3ad7043b75c0?, 0x1?, 0xe4?, 0xd2?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000091f50 sp=0xc000091f30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc000091fe0 sp=0xc000091f50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000091fe8 sp=0xc000091fe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 39 [GC worker (idle)]:
   > runtime.gopark(0x3ad7042c5628?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00050af50 sp=0xc00050af30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00050afe0 sp=0xc00050af50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00050afe8 sp=0xc00050afe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 10 [GC worker (idle)]:
   > runtime.gopark(0x3ad70432111c?, 0x1?, 0xb8?, 0x4f?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000504750 sp=0xc000504730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0005047e0 sp=0xc000504750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0005047e8 sp=0xc0005047e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 14 [select]:
   > runtime.gopark(0xc00009ff88?, 0x3?, 0x0?, 0x0?, 0xc00009ff72?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00009fdf8 sp=0xc00009fdd8 pc=0x13bb516
   > runtime.selectgo(0xc00009ff88, 0xc00009ff6c, 0xc000a5d680?, 0x0, 0xc00050bf88?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00009ff38 sp=0xc00009fdf8 pc=0x13cbbdc
   > go.opencensus.io/stats/view.(*worker).start(0xc000a5d680)
   > 	/go/pkg/mod/go.opencensus.io@v0.23.0/stats/view/worker.go:276 +0xad fp=0xc00009ffc8 sp=0xc00009ff38 pc=0x29900cd
   > go.opencensus.io/stats/view.init.0.func1()
   > 	/go/pkg/mod/go.opencensus.io@v0.23.0/stats/view/worker.go:34 +0x26 fp=0xc00009ffe0 sp=0xc00009ffc8 pc=0x298f346
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00009ffe8 sp=0xc00009ffe0 pc=0x13ee6e1
   > created by go.opencensus.io/stats/view.init.0
   > 	/go/pkg/mod/go.opencensus.io@v0.23.0/stats/view/worker.go:34 +0x8d
   > goroutine 148 [chan receive]:
   > runtime.gopark(0xc00060e8a0?, 0x13c1374?, 0x10?, 0x4e?, 0x13d8de5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000504db8 sp=0xc000504d98 pc=0x13bb516
   > runtime.chanrecv(0xc00060e480, 0xc000504f28, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000504e48 sp=0xc000504db8 pc=0x13854bb
   > runtime.chanrecv2(0x3b9aca00?, 0x13bb600?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc000504e70 sp=0xc000504e48 pc=0x1384ff8
   > go.etcd.io/etcd/pkg/logutil.(*MergeLogger).outputLoop(0xc000013b00)
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:173 +0x8c fp=0xc000504fc8 sp=0xc000504e70 pc=0x1a12c4c
   > go.etcd.io/etcd/pkg/logutil.NewMergeLogger.func1()
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:91 +0x26 fp=0xc000504fe0 sp=0xc000504fc8 pc=0x1a124c6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000504fe8 sp=0xc000504fe0 pc=0x13ee6e1
   > created by go.etcd.io/etcd/pkg/logutil.NewMergeLogger
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:91 +0xb6
   > goroutine 159 [chan receive]:
   > runtime.gopark(0xc0002f7140?, 0x1?, 0x10?, 0xa6?, 0x13d8de5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000b4a5b8 sp=0xc000b4a598 pc=0x13bb516
   > runtime.chanrecv(0xc0002f70e0, 0xc000b4a728, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000b4a648 sp=0xc000b4a5b8 pc=0x13854bb
   > runtime.chanrecv2(0x3649c80?, 0xc000b426f0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc000b4a670 sp=0xc000b4a648 pc=0x1384ff8
   > go.etcd.io/etcd/pkg/logutil.(*MergeLogger).outputLoop(0xc000013da0)
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:173 +0x8c fp=0xc000b4a7c8 sp=0xc000b4a670 pc=0x1a12c4c
   > go.etcd.io/etcd/pkg/logutil.NewMergeLogger.func1()
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:91 +0x26 fp=0xc000b4a7e0 sp=0xc000b4a7c8 pc=0x1a124c6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000b4a7e8 sp=0xc000b4a7e0 pc=0x13ee6e1
   > created by go.etcd.io/etcd/pkg/logutil.NewMergeLogger
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:91 +0xb6
   > goroutine 194 [chan receive]:
   > runtime.gopark(0xc00060e840?, 0x1?, 0x10?, 0xae?, 0x13d8de5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000b4adb8 sp=0xc000b4ad98 pc=0x13bb516
   > runtime.chanrecv(0xc00060f140, 0xc000b4af28, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000b4ae48 sp=0xc000b4adb8 pc=0x13854bb
   > runtime.chanrecv2(0x3b9aca00?, 0x13bb600?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc000b4ae70 sp=0xc000b4ae48 pc=0x1384ff8
   > go.etcd.io/etcd/pkg/logutil.(*MergeLogger).outputLoop(0xc000013ed8)
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:173 +0x8c fp=0xc000b4afc8 sp=0xc000b4ae70 pc=0x1a12c4c
   > go.etcd.io/etcd/pkg/logutil.NewMergeLogger.func1()
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:91 +0x26 fp=0xc000b4afe0 sp=0xc000b4afc8 pc=0x1a124c6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000b4afe8 sp=0xc000b4afe0 pc=0x13ee6e1
   > created by go.etcd.io/etcd/pkg/logutil.NewMergeLogger
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:91 +0xb6
   > goroutine 466 [select]:
   > runtime.gopark(0xc000b4b708?, 0x2?, 0x0?, 0xb6?, 0xc000b4b6e4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000b4b568 sp=0xc000b4b548 pc=0x13bb516
   > runtime.selectgo(0xc000b4b708, 0xc000b4b6e0, 0xc000b4b6e8?, 0x0, 0xc00055a5a0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000b4b6a8 sp=0xc000b4b568 pc=0x13cbbdc
   > github.com/pingcap/badger.(*blobGCHandler).run(0xc000a3e500, 0xc000edc048)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/blob.go:468 +0xd6 fp=0xc000b4b7c0 sp=0xc000b4b6a8 pc=0x3288896
   > github.com/pingcap/badger.(*blobManager).Open.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/blob.go:292 +0x2a fp=0xc000b4b7e0 sp=0xc000b4b7c0 pc=0x328754a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000b4b7e8 sp=0xc000b4b7e0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.(*blobManager).Open
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/blob.go:292 +0x5bd
   > goroutine 439 [chan receive]:
   > runtime.gopark(0xc60449f5b8?, 0xc00026b1e0?, 0x78?, 0xbe?, 0x13d8de5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc001034e20 sp=0xc001034e00 pc=0x13bb516
   > runtime.chanrecv(0xc000b71d40, 0x0, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc001034eb0 sp=0xc001034e20 pc=0x13854bb
   > runtime.chanrecv1(0xdf8475800?, 0x1b?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc001034ed8 sp=0xc001034eb0 pc=0x1384fb8
   > github.com/pingcap/tidb/util/profile.HeapProfileForGlobalMemTracker(0xc000edb440?)
   > 	/go/src/github.com/pingcap/tidb/util/profile/trackerRecorder.go:33 +0xa7 fp=0xc001034fc8 sp=0xc001034ed8 pc=0x267adc7
   > main.setHeapProfileTracker.func1()
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:279 +0x26 fp=0xc001034fe0 sp=0xc001034fc8 pc=0x33afc46
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc001034fe8 sp=0xc001034fe0 pc=0x13ee6e1
   > created by main.setHeapProfileTracker
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:279 +0xa5
   > goroutine 450 [chan receive]:
   > runtime.gopark(0xc00069e060?, 0xc00069e058?, 0xe?, 0x17?, 0x2?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc001030de0 sp=0xc001030dc0 pc=0x13bb516
   > runtime.chanrecv(0xc00069e000, 0x0, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc001030e70 sp=0xc001030de0 pc=0x13854bb
   > runtime.chanrecv1(0x5f5e100?, 0x3ace4e4?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc001030e98 sp=0xc001030e70 pc=0x1384fb8
   > github.com/pingcap/tidb/util/systimemon.StartMonitor(0x3bccd98, 0x3bcc3f0, 0xc000da2010)
   > 	/go/src/github.com/pingcap/tidb/util/systimemon/systime_mon.go:32 +0x185 fp=0xc001030fb8 sp=0xc001030e98 pc=0x33ac665
   > main.setupMetrics.func3()
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:696 +0x31 fp=0xc001030fe0 sp=0xc001030fb8 pc=0x33b2df1
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc001030fe8 sp=0xc001030fe0 pc=0x13ee6e1
   > created by main.setupMetrics
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:696 +0x115
   > goroutine 298 [select]:
   > runtime.gopark(0xc000b49f80?, 0x2?, 0x0?, 0x0?, 0xc000b49f4c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000b49dd0 sp=0xc000b49db0 pc=0x13bb516
   > runtime.selectgo(0xc000b49f80, 0xc000b49f48, 0x27e?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000b49f10 sp=0xc000b49dd0 pc=0x13cbbdc
   > github.com/pingcap/badger.(*DB).updateSize(0x0?, 0xc000fb22a0)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:1039 +0x105 fp=0xc000b49fc0 sp=0xc000b49f10 pc=0x329a445
   > github.com/pingcap/badger.Open.func5()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:328 +0x2a fp=0xc000b49fe0 sp=0xc000b49fc0 pc=0x329450a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000b49fe8 sp=0xc000b49fe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.Open
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:328 +0xf5c
   > goroutine 299 [select]:
   > runtime.gopark(0xc000b44788?, 0x2?, 0x2?, 0x0?, 0xc000b44764?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000b445e8 sp=0xc000b445c8 pc=0x13bb516
   > runtime.selectgo(0xc000b44788, 0xc000b44760, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000b44728 sp=0xc000b445e8 pc=0x13cbbdc
   > github.com/pingcap/badger/epoch.(*ResourceManager).collectLoop(0x0?, 0xc000fb22d0)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/epoch/manager.go:101 +0xd3 fp=0xc000b447c0 sp=0xc000b44728 pc=0x3257a13
   > github.com/pingcap/badger/epoch.NewResourceManager.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/epoch/manager.go:79 +0x2a fp=0xc000b447e0 sp=0xc000b447c0 pc=0x32577aa
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000b447e8 sp=0xc000b447e0 pc=0x13ee6e1
   > created by github.com/pingcap/badger/epoch.NewResourceManager
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/epoch/manager.go:79 +0xdd
   > goroutine 300 [select]:
   > runtime.gopark(0xc0000a2e68?, 0x2?, 0x8?, 0xf1?, 0xc0000a2e3c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0000a2cc0 sp=0xc0000a2ca0 pc=0x13bb516
   > runtime.selectgo(0xc0000a2e68, 0xc0000a2e38, 0x0?, 0x1, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0000a2e00 sp=0xc0000a2cc0 pc=0x13cbbdc
   > github.com/pingcap/badger.Open.func4()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:342 +0x155 fp=0xc0000a2fe0 sp=0xc0000a2e00 pc=0x3294495
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000a2fe8 sp=0xc0000a2fe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.Open
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:339 +0x11f8
   > goroutine 467 [select]:
   > runtime.gopark(0xc000b48f60?, 0x2?, 0x4?, 0x30?, 0xc000b48f2c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000b48d98 sp=0xc000b48d78 pc=0x13bb516
   > runtime.selectgo(0xc000b48f60, 0xc000b48f28, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000b48ed8 sp=0xc000b48d98 pc=0x13cbbdc
   > github.com/pingcap/badger.(*levelsController).runWorker(0xc0001c7ce0, 0xc000edc078, 0x0)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:212 +0x1fb fp=0xc000b48fb8 sp=0xc000b48ed8 pc=0x32a297b
   > github.com/pingcap/badger.(*levelsController).startCompact.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:180 +0x2e fp=0xc000b48fe0 sp=0xc000b48fb8 pc=0x32a274e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000b48fe8 sp=0xc000b48fe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.(*levelsController).startCompact
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:180 +0x65
   > goroutine 468 [select]:
   > runtime.gopark(0xc000b49760?, 0x2?, 0x4?, 0x30?, 0xc000b4972c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000b49598 sp=0xc000b49578 pc=0x13bb516
   > runtime.selectgo(0xc000b49760, 0xc000b49728, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000b496d8 sp=0xc000b49598 pc=0x13cbbdc
   > github.com/pingcap/badger.(*levelsController).runWorker(0xc0001c7ce0, 0xc000edc078, 0x0)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:212 +0x1fb fp=0xc000b497b8 sp=0xc000b496d8 pc=0x32a297b
   > github.com/pingcap/badger.(*levelsController).startCompact.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:180 +0x2e fp=0xc000b497e0 sp=0xc000b497b8 pc=0x32a274e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000b497e8 sp=0xc000b497e0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.(*levelsController).startCompact
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:180 +0x65
   > goroutine 469 [select]:
   > runtime.gopark(0xc000b44f60?, 0x2?, 0x4?, 0x30?, 0xc000b44f2c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000b44d98 sp=0xc000b44d78 pc=0x13bb516
   > runtime.selectgo(0xc000b44f60, 0xc000b44f28, 0x0?, 0x0, 0xf4240?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000b44ed8 sp=0xc000b44d98 pc=0x13cbbdc
   > github.com/pingcap/badger.(*levelsController).runWorker(0xc0001c7ce0, 0xc000edc078, 0x1)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:212 +0x1fb fp=0xc000b44fb8 sp=0xc000b44ed8 pc=0x32a297b
   > github.com/pingcap/badger.(*levelsController).startCompact.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:180 +0x2e fp=0xc000b44fe0 sp=0xc000b44fb8 pc=0x32a274e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000b44fe8 sp=0xc000b44fe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.(*levelsController).startCompact
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:180 +0x65
   > goroutine 470 [chan receive]:
   > runtime.gopark(0x3bcc8a0?, 0xc000b71438?, 0xe?, 0x17?, 0x2?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0000a1ac0 sp=0xc0000a1aa0 pc=0x13bb516
   > runtime.chanrecv(0xc000b713e0, 0xc0000a1c60, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc0000a1b50 sp=0xc0000a1ac0 pc=0x13854bb
   > runtime.chanrecv2(0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc0000a1b78 sp=0xc0000a1b50 pc=0x1384ff8
   > github.com/pingcap/badger.(*DB).runFlushMemTable(0xc0000fcd80, 0x0?)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:920 +0xdd fp=0xc0000a1fc0 sp=0xc0000a1b78 pc=0x3298efd
   > github.com/pingcap/badger.Open.func6()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:361 +0x2a fp=0xc0000a1fe0 sp=0xc0000a1fc0 pc=0x329430a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000a1fe8 sp=0xc0000a1fe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.Open
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:361 +0x158d
   > goroutine 171 [chan receive]:
   > runtime.gopark(0xc0012486e8?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc001032ea8 sp=0xc001032e88 pc=0x13bb516
   > runtime.chanrecv(0xc00060e900, 0xc001032f88, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc001032f38 sp=0xc001032ea8 pc=0x13854bb
   > runtime.chanrecv2(0xc000f76060?, 0xc000905800?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc001032f60 sp=0xc001032f38 pc=0x1384ff8
   > github.com/pingcap/badger.(*writeWorker).runMergeLSM(0x0?, 0xd4?)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:154 +0x9b fp=0xc001032fc0 sp=0xc001032f60 pc=0x32b307b
   > github.com/pingcap/badger.startWriteWorker.func4()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:66 +0x2a fp=0xc001032fe0 sp=0xc001032fc0 pc=0x32b22ca
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc001032fe8 sp=0xc001032fe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.startWriteWorker
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:66 +0x2a5
   > goroutine 170 [chan receive, locked to thread]:
   > runtime.gopark(0xc00009ee98?, 0x1456628?, 0xf?, 0x0?, 0x1?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00009ee68 sp=0xc00009ee48 pc=0x13bb516
   > runtime.chanrecv(0xc00060e420, 0xc00009ef88, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc00009eef8 sp=0xc00009ee68 pc=0x13854bb
   > runtime.chanrecv2(0xc000f7ec60?, 0x3ef1f177af97905e?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc00009ef20 sp=0xc00009eef8 pc=0x1384ff8
   > github.com/pingcap/badger.(*writeWorker).runWriteLSM(0xc000a222a0, 0xc000ac2460?)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:141 +0x15e fp=0xc00009efc0 sp=0xc00009ef20 pc=0x32b2efe
   > github.com/pingcap/badger.startWriteWorker.func3()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:65 +0x2a fp=0xc00009efe0 sp=0xc00009efc0 pc=0x32b232a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00009efe8 sp=0xc00009efe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.startWriteWorker
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:65 +0x24d
   > goroutine 169 [select]:
   > runtime.gopark(0xc001035f78?, 0x3?, 0x25?, 0x48?, 0xc001035f32?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc001035d98 sp=0xc001035d78 pc=0x13bb516
   > runtime.selectgo(0xc001035f78, 0xc001035f2c, 0x1?, 0x0, 0xc000d01a00?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc001035ed8 sp=0xc001035d98 pc=0x13cbbdc
   > github.com/pingcap/badger.(*writeWorker).runWriteVLog(0xc000a222a0, 0xc000edc150)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:94 +0x137 fp=0xc001035fc0 sp=0xc001035ed8 pc=0x32b28b7
   > github.com/pingcap/badger.startWriteWorker.func2()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:64 +0x2a fp=0xc001035fe0 sp=0xc001035fc0 pc=0x32b238a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc001035fe8 sp=0xc001035fe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.startWriteWorker
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:64 +0x1f9
   > goroutine 172 [select]:
   > runtime.gopark(0xc0003b8f88?, 0x2?, 0x0?, 0x0?, 0xc0003b8f4c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0003b8da0 sp=0xc0003b8d80 pc=0x13bb516
   > runtime.selectgo(0xc0003b8f88, 0xc0003b8f48, 0xc0005aa150?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0003b8ee0 sp=0xc0003b8da0 pc=0x13cbbdc
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.writeDBWorker.run({0xc00060ed20?, 0xc000dc20c0?})
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:96 +0x145 fp=0xc0003b8fc0 sp=0xc0003b8ee0 pc=0x3308de5
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*dbWriter).Open.func1()
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:202 +0x2a fp=0xc0003b8fe0 sp=0xc0003b8fc0 pc=0x330996a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0003b8fe8 sp=0xc0003b8fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*dbWriter).Open
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:199 +0xc5
   > goroutine 173 [select]:
   > runtime.gopark(0xc001031e70?, 0x2?, 0x90?, 0x1e?, 0xc001031e1c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc001031c58 sp=0xc001031c38 pc=0x13bb516
   > runtime.selectgo(0xc001031e70, 0xc001031e18, 0x13?, 0x0, 0xc01b9cae80?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc001031d98 sp=0xc001031c58 pc=0x13cbbdc
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.writeLockWorker.run({0xc00060ed80?, 0xc000dc20c0?})
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:148 +0x15f fp=0xc001031fc0 sp=0xc001031d98 pc=0x33093bf
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*dbWriter).Open.func2()
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:209 +0x2a fp=0xc001031fe0 sp=0xc001031fc0 pc=0x330990a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc001031fe8 sp=0xc001031fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*dbWriter).Open
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:206 +0x159
   > goroutine 174 [select]:
   > runtime.gopark(0xc00008d718?, 0x2?, 0x0?, 0x0?, 0xc00008d704?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008d588 sp=0xc00008d568 pc=0x13bb516
   > runtime.selectgo(0xc00008d718, 0xc00008d700, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00008d6c8 sp=0xc00008d588 pc=0x13cbbdc
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*MVCCStore).runUpdateSafePointLoop(0xc000b74780)
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:1550 +0x217 fp=0xc00008d7c8 sp=0xc00008d6c8 pc=0x32facd7
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.NewMVCCStore.func1()
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:85 +0x26 fp=0xc00008d7e0 sp=0xc00008d7c8 pc=0x32ed406
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008d7e8 sp=0xc00008d7e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.NewMVCCStore
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:85 +0x337
   > goroutine 175 [select]:
   > runtime.gopark(0xc00008dfb0?, 0x2?, 0x0?, 0x0?, 0xc00008df9c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008de28 sp=0xc00008de08 pc=0x13bb516
   > runtime.selectgo(0xc00008dfb0, 0xc00008df98, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00008df68 sp=0xc00008de28 pc=0x13cbbdc
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*MVCCStore).StartDeadlockDetection.func1()
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:1286 +0x7b fp=0xc00008dfe0 sp=0xc00008df68 pc=0x32f895b
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008dfe8 sp=0xc00008dfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*MVCCStore).StartDeadlockDetection
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:1284 +0xb6
   > goroutine 176 [select]:
   > runtime.gopark(0xc0003bbf78?, 0x2?, 0x2?, 0x0?, 0xc0003bbf3c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0003bbdc0 sp=0xc0003bbda0 pc=0x13bb516
   > runtime.selectgo(0xc0003bbf78, 0xc0003bbf38, 0xc000b47fb0?, 0x0, 0xc00060e1e0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0003bbf00 sp=0xc0003bbdc0 pc=0x13cbbdc
   > github.com/tikv/client-go/v2/oracle/oracles.(*pdOracle).updateTS(0xc000f87030, {0x400d640, 0xc000056058}, 0xc000ac2460?)
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/oracle/oracles/pd.go:229 +0x128 fp=0xc0003bbfb0 sp=0xc0003bbf00 pc=0x1e9b548
   > github.com/tikv/client-go/v2/oracle/oracles.NewPdOracle.func1()
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/oracle/oracles/pd.go:77 +0x32 fp=0xc0003bbfe0 sp=0xc0003bbfb0 pc=0x1e9a772
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0003bbfe8 sp=0xc0003bbfe0 pc=0x13ee6e1
   > created by github.com/tikv/client-go/v2/oracle/oracles.NewPdOracle
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/oracle/oracles/pd.go:77 +0x119
   > goroutine 177 [select]:
   > runtime.gopark(0xc000506f78?, 0x3?, 0x8?, 0x0?, 0xc000506f5a?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000506de0 sp=0xc000506dc0 pc=0x13bb516
   > runtime.selectgo(0xc000506f78, 0xc000506f54, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000506f20 sp=0xc000506de0 pc=0x13cbbdc
   > github.com/tikv/client-go/v2/internal/locate.(*RegionCache).asyncCheckAndResolveLoop(0xc000b75080, 0x0?)
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/internal/locate/region_cache.go:399 +0xd1 fp=0xc000506fc0 sp=0xc000506f20 pc=0x1e6bff1
   > github.com/tikv/client-go/v2/internal/locate.NewRegionCache.func1()
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/internal/locate/region_cache.go:370 +0x2a fp=0xc000506fe0 sp=0xc000506fc0 pc=0x1e6bc6a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000506fe8 sp=0xc000506fe0 pc=0x13ee6e1
   > created by github.com/tikv/client-go/v2/internal/locate.NewRegionCache
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/internal/locate/region_cache.go:370 +0x2e6
   > goroutine 482 [select]:
   > runtime.gopark(0xc001033f10?, 0x2?, 0x3?, 0x30?, 0xc001033eac?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc001033d10 sp=0xc001033cf0 pc=0x13bb516
   > runtime.selectgo(0xc001033f10, 0xc001033ea8, 0x0?, 0x0, 0x5f55780?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc001033e50 sp=0xc001033d10 pc=0x13cbbdc
   > github.com/tikv/client-go/v2/tikv.(*KVStore).runSafePointChecker(0xc000b7b680)
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/tikv/kv.go:264 +0x12b fp=0xc001033fc8 sp=0xc001033e50 pc=0x1ed6f0b
   > github.com/tikv/client-go/v2/tikv.NewKVStore.func1()
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/tikv/kv.go:187 +0x26 fp=0xc001033fe0 sp=0xc001033fc8 pc=0x1ed6d06
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc001033fe8 sp=0xc001033fe0 pc=0x13ee6e1
   > created by github.com/tikv/client-go/v2/tikv.NewKVStore
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/tikv/kv.go:187 +0x3d6
   > goroutine 483 [select]:
   > runtime.gopark(0xc0003baf80?, 0x2?, 0x0?, 0xbe?, 0xc0003baf44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0003badc8 sp=0xc0003bada8 pc=0x13bb516
   > runtime.selectgo(0xc0003baf80, 0xc0003baf40, 0xc000a3e700?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0003baf08 sp=0xc0003badc8 pc=0x13cbbdc
   > github.com/tikv/client-go/v2/tikv.(*KVStore).safeTSUpdater(0xc000b7b680)
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/tikv/kv.go:544 +0x165 fp=0xc0003bafc8 sp=0xc0003baf08 pc=0x1ed8e65
   > github.com/tikv/client-go/v2/tikv.NewKVStore.func2()
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/tikv/kv.go:188 +0x26 fp=0xc0003bafe0 sp=0xc0003bafc8 pc=0x1ed6ca6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0003bafe8 sp=0xc0003bafe0 pc=0x13ee6e1
   > created by github.com/tikv/client-go/v2/tikv.NewKVStore
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/tikv/kv.go:188 +0x416
   > goroutine 484 [select]:
   > runtime.gopark(0xc00050bf98?, 0x2?, 0x90?, 0xbe?, 0xc00050bf6c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00050bde8 sp=0xc00050bdc8 pc=0x13bb516
   > runtime.selectgo(0xc00050bf98, 0xc00050bf68, 0x13848e0?, 0x0, 0x13848e0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00050bf28 sp=0xc00050bde8 pc=0x13cbbdc
   > github.com/dgraph-io/ristretto.(*defaultPolicy).processItems(0xc000c8d230)
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.0.1/policy.go:96 +0x91 fp=0xc00050bfc8 sp=0xc00050bf28 pc=0x23cf0d1
   > github.com/dgraph-io/ristretto.newDefaultPolicy.func1()
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.0.1/policy.go:80 +0x26 fp=0xc00050bfe0 sp=0xc00050bfc8 pc=0x23cef86
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00050bfe8 sp=0xc00050bfe0 pc=0x13ee6e1
   > created by github.com/dgraph-io/ristretto.newDefaultPolicy
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.0.1/policy.go:80 +0x156
   > goroutine 485 [select]:
   > runtime.gopark(0xc00050b798?, 0x2?, 0x0?, 0x0?, 0xc00050b774?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00050b5f0 sp=0xc00050b5d0 pc=0x13bb516
   > runtime.selectgo(0xc00050b798, 0xc00050b770, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00050b730 sp=0xc00050b5f0 pc=0x13cbbdc
   > github.com/dgraph-io/ristretto.(*Cache).processItems(0xc00060f1a0)
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.0.1/cache.go:257 +0x85 fp=0xc00050b7c8 sp=0xc00050b730 pc=0x23ce025
   > github.com/dgraph-io/ristretto.NewCache.func2()
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.0.1/cache.go:155 +0x26 fp=0xc00050b7e0 sp=0xc00050b7c8 pc=0x23cd846
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00050b7e8 sp=0xc00050b7e0 pc=0x13ee6e1
   > created by github.com/dgraph-io/ristretto.NewCache
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.0.1/cache.go:155 +0x485
   > goroutine 753 [chan receive]:
   > runtime.gopark(0x0?, 0x0?, 0xa8?, 0x6c?, 0xc010ccbed4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010ccbde0 sp=0xc010ccbdc0 pc=0x13bb516
   > runtime.chanrecv(0xc0002fb980, 0xc010ccbf08, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc010ccbe70 sp=0xc010ccbde0 pc=0x13854bb
   > runtime.chanrecv1(0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc010ccbe98 sp=0xc010ccbe70 pc=0x1384fb8
   > github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).startAnalyzeProfileWorker(0xc000610120)
   > 	/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:142 +0x7c fp=0xc010ccbfc8 sp=0xc010ccbe98 pc=0x25402bc
   > github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).Run.func2()
   > 	/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:94 +0x26 fp=0xc010ccbfe0 sp=0xc010ccbfc8 pc=0x253fe46
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010ccbfe8 sp=0xc010ccbfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).Run
   > 	/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:94 +0x10a
   > goroutine 303 [select]:
   > runtime.gopark(0xc00099df38?, 0x2?, 0x0?, 0x0?, 0xc00099defc?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00099dd50 sp=0xc00099dd30 pc=0x13bb516
   > runtime.selectgo(0xc00099df38, 0xc00099def8, 0x1?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00099de90 sp=0xc00099dd50 pc=0x13cbbdc
   > github.com/pingcap/tidb/ddl.(*ddl).limitDDLJobs(0xc010e08230)
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl_worker.go:263 +0x173 fp=0xc00099dfc8 sp=0xc00099de90 pc=0x2623fd3
   > github.com/pingcap/tidb/ddl.(*ddl).Start.func1()
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:351 +0x26 fp=0xc00099dfe0 sp=0xc00099dfc8 pc=0x25e9ac6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00099dfe8 sp=0xc00099dfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/ddl.(*ddl).Start
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:351 +0x2ea
   > goroutine 304 [select]:
   > runtime.gopark(0xc000b35f90?, 0x2?, 0x6?, 0x0?, 0xc000b35f6c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000b35df0 sp=0xc000b35dd0 pc=0x13bb516
   > runtime.selectgo(0xc000b35f90, 0xc000b35f68, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000b35f30 sp=0xc000b35df0 pc=0x13cbbdc
   > github.com/pingcap/tidb/ddl.(*delRange).startEmulator(0xc010e48cc0)
   > 	/go/src/github.com/pingcap/tidb/ddl/delete_range.go:144 +0x125 fp=0xc000b35fc8 sp=0xc000b35f30 pc=0x262b9e5
   > github.com/pingcap/tidb/ddl.(*delRange).start.func1()
   > 	/go/src/github.com/pingcap/tidb/ddl/delete_range.go:126 +0x26 fp=0xc000b35fe0 sp=0xc000b35fc8 pc=0x262b7a6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000b35fe8 sp=0xc000b35fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/ddl.(*delRange).start
   > 	/go/src/github.com/pingcap/tidb/ddl/delete_range.go:126 +0x6d
   > goroutine 751 [select]:
   > runtime.gopark(0xc010cccf40?, 0x2?, 0x2e?, 0xab?, 0xc010cccf04?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010cccd88 sp=0xc010cccd68 pc=0x13bb516
   > runtime.selectgo(0xc010cccf40, 0xc010cccf00, 0x3647520?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010cccec8 sp=0xc010cccd88 pc=0x13cbbdc
   > github.com/pingcap/tidb/util/topsql/reporter.(*RemoteTopSQLReporter).reportWorker(0xc0116581c0)
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:499 +0x1ae fp=0xc010cccfc8 sp=0xc010cccec8 pc=0x254924e
   > github.com/pingcap/tidb/util/topsql/reporter.NewRemoteTopSQLReporter.func2()
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:161 +0x26 fp=0xc010cccfe0 sp=0xc010cccfc8 pc=0x2546bc6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010cccfe8 sp=0xc010cccfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/util/topsql/reporter.NewRemoteTopSQLReporter
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:161 +0x1f6
   > goroutine 866 [IO wait]:
   > runtime.gopark(0xf?, 0xc011ab6c30?, 0x6?, 0x0?, 0xc000bb78d0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000bb7860 sp=0xc000bb7840 pc=0x13bb516
   > runtime.netpollblock(0x203004?, 0x11ab6c30?, 0xc0?)
   > 	/usr/local/go/src/runtime/netpoll.go:526 +0xf7 fp=0xc000bb7898 sp=0xc000bb7860 pc=0x13b38f7
   > internal/poll.runtime_pollWait(0x7fc5dd06a618, 0x72)
   > 	/usr/local/go/src/runtime/netpoll.go:305 +0x89 fp=0xc000bb78b8 sp=0xc000bb7898 pc=0x13e7d09
   > internal/poll.(*pollDesc).wait(0xc0113eea00?, 0xc011b25470?, 0x0)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:84 +0x32 fp=0xc000bb78e0 sp=0xc000bb78b8 pc=0x1465192
   > internal/poll.(*pollDesc).waitRead(...)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:89
   > internal/poll.(*FD).Accept(0xc0113eea00)
   > 	/usr/local/go/src/internal/poll/fd_unix.go:614 +0x234 fp=0xc000bb7978 sp=0xc000bb78e0 pc=0x146a594
   > net.(*netFD).accept(0xc0113eea00)
   > 	/usr/local/go/src/net/fd_unix.go:172 +0x35 fp=0xc000bb7a30 sp=0xc000bb7978 pc=0x1589055
   > net.(*TCPListener).accept(0xc010571e18)
   > 	/usr/local/go/src/net/tcpsock_posix.go:142 +0x28 fp=0xc000bb7a60 sp=0xc000bb7a30 pc=0x15a5088
   > net.(*TCPListener).Accept(0xc010571e18)
   > 	/usr/local/go/src/net/tcpsock.go:288 +0x3d fp=0xc000bb7a90 sp=0xc000bb7a60 pc=0x15a40fd
   > github.com/soheilhy/cmux.(*cMux).Serve(0xc011aef2c0)
   > 	/go/pkg/mod/github.com/soheilhy/cmux@v0.1.4/cmux.go:162 +0xa9 fp=0xc000bb7b20 sp=0xc000bb7a90 pc=0x2dc5da9
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer(0xc0113456c0, 0xc0113e5780)
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:466 +0x4f7 fp=0xc000bb7c90 sp=0xc000bb7b20 pc=0x31dab17
   > github.com/pingcap/tidb/server.(*Server).startHTTPServer(0xc0113456c0)
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:442 +0x15d0 fp=0xc000bb7fc8 sp=0xc000bb7c90 pc=0x31d9f10
   > github.com/pingcap/tidb/server.(*Server).startStatusHTTP.func1()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:62 +0x26 fp=0xc000bb7fe0 sp=0xc000bb7fc8 pc=0x31d65c6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000bb7fe8 sp=0xc000bb7fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/server.(*Server).startStatusHTTP
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:62 +0x56
   > goroutine 5108 [select]:
   > runtime.gopark(0xc0141dae10?, 0x2?, 0xc8?, 0xcc?, 0xc0141dad8c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0141dabe0 sp=0xc0141dabc0 pc=0x13bb516
   > runtime.selectgo(0xc0141dae10, 0xc0141dad88, 0xc000d205e8?, 0x0, 0xc000b7b790?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0141dad20 sp=0xc0141dabe0 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc010df4000, 0x1, {0x5f8a1a8, 0x0, 0x0})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:441 +0x4f4 fp=0xc0141daf10 sp=0xc0141dad20 pc=0x30626b4
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:335 +0xb3 fp=0xc0141daf90 sp=0xc0141daf10 pc=0x30613d3
   > github.com/pingcap/tidb/util.WithRecovery(0x400d6b0?, 0xc0141dad38?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc0141dafc0 sp=0xc0141daf90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x2a fp=0xc0141dafe0 sp=0xc0141dafc0 pc=0x30612ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0141dafe8 sp=0xc0141dafe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x1c9
   > goroutine 817 [chan receive]:
   > runtime.gopark(0xc0000c6418?, 0xc00040d6c0?, 0x48?, 0x6e?, 0x13d8de5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000b46df0 sp=0xc000b46dd0 pc=0x13bb516
   > runtime.chanrecv(0xc010cb6ea0, 0xc000b46f38, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000b46e80 sp=0xc000b46df0 pc=0x13854bb
   > runtime.chanrecv2(0x9356907420000?, 0x0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc000b46ea8 sp=0xc000b46e80 pc=0x1384ff8
   > github.com/pingcap/tidb/server.NewServer.func1()
   > 	/go/src/github.com/pingcap/tidb/server/server.go:209 +0x98 fp=0xc000b46fe0 sp=0xc000b46ea8 pc=0x31e1638
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000b46fe8 sp=0xc000b46fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/server.NewServer
   > 	/go/src/github.com/pingcap/tidb/server/server.go:208 +0x32a
   > goroutine 752 [sleep]:
   > runtime.gopark(0x3ad985dad9bd?, 0x2fe82d7?, 0x88?, 0x57?, 0x25412d5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000b45758 sp=0xc000b45738 pc=0x13bb516
   > time.Sleep(0x3b9aca00)
   > 	/usr/local/go/src/runtime/time.go:195 +0x135 fp=0xc000b45798 sp=0xc000b45758 pc=0x13eaf15
   > github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).startCPUProfileWorker(0xc000b457b8?)
   > 	/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:115 +0x65 fp=0xc000b457c8 sp=0xc000b45798 pc=0x2540065
   > github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).Run.func1()
   > 	/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:93 +0x26 fp=0xc000b457e0 sp=0xc000b457c8 pc=0x253fea6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000b457e8 sp=0xc000b457e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).Run
   > 	/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:93 +0xca
   > goroutine 750 [select]:
   > runtime.gopark(0xc010b1e780?, 0x3?, 0x4?, 0x30?, 0xc010b1e73a?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010b1e5a8 sp=0xc010b1e588 pc=0x13bb516
   > runtime.selectgo(0xc010b1e780, 0xc010b1e734, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010b1e6e8 sp=0xc010b1e5a8 pc=0x13cbbdc
   > github.com/pingcap/tidb/util/topsql/reporter.(*RemoteTopSQLReporter).collectWorker(0xc0116581c0)
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:327 +0x13a fp=0xc010b1e7c8 sp=0xc010b1e6e8 pc=0x2547eda
   > github.com/pingcap/tidb/util/topsql/reporter.NewRemoteTopSQLReporter.func1()
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:160 +0x26 fp=0xc010b1e7e0 sp=0xc010b1e7c8 pc=0x2546c26
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010b1e7e8 sp=0xc010b1e7e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/util/topsql/reporter.NewRemoteTopSQLReporter
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:160 +0x1b6
   > goroutine 815 [select]:
   > runtime.gopark(0xc01c793f78?, 0x2?, 0x4?, 0x30?, 0xc01c793f4c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01c793dd0 sp=0xc01c793db0 pc=0x13bb516
   > runtime.selectgo(0xc01c793f78, 0xc01c793f48, 0xc01c635490?, 0x0, 0xc010b21e58?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01c793f10 sp=0xc01c793dd0 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).autoAnalyzeWorker(0xc000ffe360, {0x401ea10, 0xc01057fd00})
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1425 +0x105 fp=0xc01c793fb8 sp=0xc01c793f10 pc=0x26a8bc5
   > github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop.func4()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1262 +0x2e fp=0xc01c793fe0 sp=0xc01c793fb8 pc=0x26a654e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01c793fe8 sp=0xc01c793fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1262 +0x31a
   > goroutine 867 [IO wait]:
   > runtime.gopark(0x18?, 0xc000534c00?, 0x60?, 0x20?, 0xc00104cb70?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00104cb00 sp=0xc00104cae0 pc=0x13bb516
   > runtime.netpollblock(0x14?, 0x2432d05?, 0x0?)
   > 	/usr/local/go/src/runtime/netpoll.go:526 +0xf7 fp=0xc00104cb38 sp=0xc00104cb00 pc=0x13b38f7
   > internal/poll.runtime_pollWait(0x7fc5dd06a7f8, 0x72)
   > 	/usr/local/go/src/runtime/netpoll.go:305 +0x89 fp=0xc00104cb58 sp=0xc00104cb38 pc=0x13e7d09
   > internal/poll.(*pollDesc).wait(0xc0113ee800?, 0xc00104cd20?, 0x0)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:84 +0x32 fp=0xc00104cb80 sp=0xc00104cb58 pc=0x1465192
   > internal/poll.(*pollDesc).waitRead(...)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:89
   > internal/poll.(*FD).Accept(0xc0113ee800)
   > 	/usr/local/go/src/internal/poll/fd_unix.go:614 +0x234 fp=0xc00104cc18 sp=0xc00104cb80 pc=0x146a594
   > net.(*netFD).accept(0xc0113ee800)
   > 	/usr/local/go/src/net/fd_unix.go:172 +0x35 fp=0xc00104ccd0 sp=0xc00104cc18 pc=0x1589055
   > net.(*TCPListener).accept(0xc010571e00)
   > 	/usr/local/go/src/net/tcpsock_posix.go:142 +0x28 fp=0xc00104cd00 sp=0xc00104ccd0 pc=0x15a5088
   > net.(*TCPListener).Accept(0xc010571e00)
   > 	/usr/local/go/src/net/tcpsock.go:288 +0x3d fp=0xc00104cd30 sp=0xc00104cd00 pc=0x15a40fd
   > github.com/pingcap/tidb/server.(*Server).startNetworkListener(0xc0113456c0, {0x400b9b0, 0xc010571e00}, 0x0, 0xc000056058?)
   > 	/go/src/github.com/pingcap/tidb/server/server.go:383 +0xa6 fp=0xc00104cfa8 sp=0xc00104cd30 pc=0x31e25a6
   > github.com/pingcap/tidb/server.(*Server).Run.func1()
   > 	/go/src/github.com/pingcap/tidb/server/server.go:368 +0x34 fp=0xc00104cfe0 sp=0xc00104cfa8 pc=0x31e24d4
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00104cfe8 sp=0xc00104cfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/server.(*Server).Run
   > 	/go/src/github.com/pingcap/tidb/server/server.go:368 +0x145
   > goroutine 868 [IO wait]:
   > runtime.gopark(0x1396deb?, 0x7fc5db8b2d00?, 0xe0?, 0x79?, 0xc001049b78?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc001049b08 sp=0xc001049ae8 pc=0x13bb516
   > runtime.netpollblock(0x1?, 0x1049ba0?, 0xc0?)
   > 	/usr/local/go/src/runtime/netpoll.go:526 +0xf7 fp=0xc001049b40 sp=0xc001049b08 pc=0x13b38f7
   > internal/poll.runtime_pollWait(0x7fc5dd06a708, 0x72)
   > 	/usr/local/go/src/runtime/netpoll.go:305 +0x89 fp=0xc001049b60 sp=0xc001049b40 pc=0x13e7d09
   > internal/poll.(*pollDesc).wait(0xc0113ee880?, 0x1?, 0x0)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:84 +0x32 fp=0xc001049b88 sp=0xc001049b60 pc=0x1465192
   > internal/poll.(*pollDesc).waitRead(...)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:89
   > internal/poll.(*FD).Accept(0xc0113ee880)
   > 	/usr/local/go/src/internal/poll/fd_unix.go:614 +0x234 fp=0xc001049c20 sp=0xc001049b88 pc=0x146a594
   > net.(*netFD).accept(0xc0113ee880)
   > 	/usr/local/go/src/net/fd_unix.go:172 +0x35 fp=0xc001049cd8 sp=0xc001049c20 pc=0x1589055
   > net.(*UnixListener).accept(0xc000b86d48?)
   > 	/usr/local/go/src/net/unixsock_posix.go:166 +0x1c fp=0xc001049d00 sp=0xc001049cd8 pc=0x15aba1c
   > net.(*UnixListener).Accept(0xc011a9c750)
   > 	/usr/local/go/src/net/unixsock.go:260 +0x3d fp=0xc001049d30 sp=0xc001049d00 pc=0x15aa0bd
   > github.com/pingcap/tidb/server.(*Server).startNetworkListener(0xc0113456c0, {0x400b9e0, 0xc011a9c750}, 0x1, 0xc000056058?)
   > 	/go/src/github.com/pingcap/tidb/server/server.go:383 +0xa6 fp=0xc001049fa8 sp=0xc001049d30 pc=0x31e25a6
   > github.com/pingcap/tidb/server.(*Server).Run.func2()
   > 	/go/src/github.com/pingcap/tidb/server/server.go:369 +0x37 fp=0xc001049fe0 sp=0xc001049fa8 pc=0x31e2477
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc001049fe8 sp=0xc001049fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/server.(*Server).Run
   > 	/go/src/github.com/pingcap/tidb/server/server.go:369 +0x1db
   > goroutine 749 [chan receive]:
   > runtime.gopark(0x0?, 0x0?, 0x88?, 0x6?, 0x309a506?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010b20660 sp=0xc010b20640 pc=0x13bb516
   > runtime.chanrecv(0xc0113e3740, 0xc010b20780, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc010b206f0 sp=0xc010b20660 pc=0x13854bb
   > runtime.chanrecv1(0x0?, 0x309a4e0?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc010b20718 sp=0xc010b206f0 pc=0x1384fb8
   > github.com/pingcap/tidb/util/signal.SetupSignalHandler.func2()
   > 	/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:53 +0x45 fp=0xc010b207e0 sp=0xc010b20718 pc=0x33ac105
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010b207e8 sp=0xc010b207e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/util/signal.SetupSignalHandler
   > 	/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:52 +0x19f
   > goroutine 305 [select]:
   > runtime.gopark(0xc010393f58?, 0x4?, 0xab?, 0x62?, 0xc010393da8?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010393bf8 sp=0xc010393bd8 pc=0x13bb516
   > runtime.selectgo(0xc010393f58, 0xc010393da0, 0x24?, 0x0, 0x1?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010393d38 sp=0xc010393bf8 pc=0x13cbbdc
   > github.com/pingcap/tidb/ddl.(*worker).start(0xc010e2e8f0, 0xc000fee0c0)
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl_worker.go:178 +0x318 fp=0xc010393fc0 sp=0xc010393d38 pc=0x2622e98
   > github.com/pingcap/tidb/ddl.(*ddl).Start.func2()
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:369 +0x2a fp=0xc010393fe0 sp=0xc010393fc0 pc=0x25e9a6a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010393fe8 sp=0xc010393fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/ddl.(*ddl).Start
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:369 +0x5c5
   > goroutine 722 [select]:
   > runtime.gopark(0xc0005f1f58?, 0x4?, 0xab?, 0x62?, 0xc0005f1da8?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0005f1bf8 sp=0xc0005f1bd8 pc=0x13bb516
   > runtime.selectgo(0xc0005f1f58, 0xc0005f1da0, 0xc000fe2e38?, 0x0, 0x1?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0005f1d38 sp=0xc0005f1bf8 pc=0x13cbbdc
   > github.com/pingcap/tidb/ddl.(*worker).start(0xc010e2e840, 0xc000fee0c0)
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl_worker.go:178 +0x318 fp=0xc0005f1fc0 sp=0xc0005f1d38 pc=0x2622e98
   > github.com/pingcap/tidb/ddl.(*ddl).Start.func2()
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:369 +0x2a fp=0xc0005f1fe0 sp=0xc0005f1fc0 pc=0x25e9a6a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0005f1fe8 sp=0xc0005f1fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/ddl.(*ddl).Start
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:369 +0x5c5
   > goroutine 724 [select]:
   > runtime.gopark(0xc000999f50?, 0x4?, 0x4?, 0x30?, 0xc000999d00?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000999b78 sp=0xc000999b58 pc=0x13bb516
   > runtime.selectgo(0xc000999f50, 0xc000999cf8, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000999cb8 sp=0xc000999b78 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).loadSchemaInLoop(0xc000ffe360, {0x400d608, 0xc000fe83c0}, 0x0?)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:565 +0x1aa fp=0xc000999fb0 sp=0xc000999cb8 pc=0x26a00aa
   > github.com/pingcap/tidb/domain.(*Domain).Init.func10()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:825 +0x32 fp=0xc000999fe0 sp=0xc000999fb0 pc=0x26a2b32
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000999fe8 sp=0xc000999fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:825 +0xdeb
   > goroutine 725 [select]:
   > runtime.gopark(0xc010b20f78?, 0x3?, 0x4?, 0x30?, 0xc010b20f12?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010b20d60 sp=0xc010b20d40 pc=0x13bb516
   > runtime.selectgo(0xc010b20f78, 0xc010b20f0c, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010b20ea0 sp=0xc010b20d60 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).topNSlowQueryLoop(0xc000ffe360)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:455 +0x194 fp=0xc010b20fc8 sp=0xc010b20ea0 pc=0x269e914
   > github.com/pingcap/tidb/domain.(*Domain).Init.func11()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:828 +0x26 fp=0xc010b20fe0 sp=0xc010b20fc8 pc=0x26a2ac6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010b20fe8 sp=0xc010b20fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:828 +0xe52
   > goroutine 726 [select]:
   > runtime.gopark(0xc0003b7ef8?, 0x3?, 0x4?, 0x30?, 0xc0003b7e82?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0003b7d08 sp=0xc0003b7ce8 pc=0x13bb516
   > runtime.selectgo(0xc0003b7ef8, 0xc0003b7e7c, 0xc000dc2500?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0003b7e48 sp=0xc0003b7d08 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).infoSyncerKeeper(0xc000ffe360)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:487 +0x165 fp=0xc0003b7fc8 sp=0xc0003b7e48 pc=0x269ee45
   > github.com/pingcap/tidb/domain.(*Domain).Init.func12()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:829 +0x26 fp=0xc0003b7fe0 sp=0xc0003b7fc8 pc=0x26a2a66
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0003b7fe8 sp=0xc0003b7fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:829 +0xe95
   > goroutine 727 [select]:
   > runtime.gopark(0xc0110dfef0?, 0x2?, 0x0?, 0x0?, 0xc0110dfebc?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0003bdd38 sp=0xc0003bdd18 pc=0x13bb516
   > runtime.selectgo(0xc0003bdef0, 0xc0110dfeb8, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0003bde78 sp=0xc0003bdd38 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).globalConfigSyncerKeeper(0xc000ffe360)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:510 +0xe5 fp=0xc0003bdfc8 sp=0xc0003bde78 pc=0x269f405
   > github.com/pingcap/tidb/domain.(*Domain).Init.func13()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:830 +0x26 fp=0xc0003bdfe0 sp=0xc0003bdfc8 pc=0x26a2a06
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0003bdfe8 sp=0xc0003bdfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:830 +0xedc
   > goroutine 728 [select]:
   > runtime.gopark(0xc0110e0678?, 0x3?, 0x4?, 0x30?, 0xc0110e05f2?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0110e0478 sp=0xc0110e0458 pc=0x13bb516
   > runtime.selectgo(0xc0110e0678, 0xc0110e05ec, 0xc000056050?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0110e05b8 sp=0xc0110e0478 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).topologySyncerKeeper(0xc000ffe360)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:533 +0x165 fp=0xc0110e07c8 sp=0xc0110e05b8 pc=0x269f8c5
   > github.com/pingcap/tidb/domain.(*Domain).Init.func14()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:834 +0x26 fp=0xc0110e07e0 sp=0xc0110e07c8 pc=0x26a29a6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0110e07e8 sp=0xc0110e07e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:834 +0xf3d
   > goroutine 738 [select]:
   > runtime.gopark(0xc00102ef28?, 0x2?, 0x0?, 0x30?, 0xc00102eed4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00102ed48 sp=0xc00102ed28 pc=0x13bb516
   > runtime.selectgo(0xc00102ef28, 0xc00102eed0, 0xc0110e2e00?, 0x0, 0x24?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00102ee88 sp=0xc00102ed48 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).handleEvolvePlanTasksLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1106 +0x107 fp=0xc00102efe0 sp=0xc00102ee88 pc=0x26a4fe7
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00102efe8 sp=0xc00102efe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).handleEvolvePlanTasksLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1099 +0xe5
   > goroutine 5005 [select]:
   > runtime.gopark(0xc000677f78?, 0x2?, 0xc7?, 0xb5?, 0xc000677eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000677d58 sp=0xc000677d38 pc=0x13bb516
   > runtime.selectgo(0xc000677f78, 0xc000677ee8, 0x3aac226?, 0x0, 0xc0101c8078?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000677e98 sp=0xc000677d58 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc011b50bc0, {0x400d6b0?, 0xc01bbde2d0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc000677fb8 sp=0xc000677e98 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc000677fe0 sp=0xc000677fb8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000677fe8 sp=0xc000677fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 850 [select]:
   > runtime.gopark(0xc00fe85eb0?, 0x2?, 0x1c?, 0x0?, 0xc00fe85e5c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fe85cc8 sp=0xc00fe85ca8 pc=0x13bb516
   > runtime.selectgo(0xc00fe85eb0, 0xc00fe85e58, 0xc0113456c0?, 0x0, 0x13bb516?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fe85e08 sp=0xc00fe85cc8 pc=0x13cbbdc
   > github.com/pingcap/tidb/util/expensivequery.(*Handle).Run(0xc000fda120)
   > 	/go/src/github.com/pingcap/tidb/util/expensivequery/expensivequery.go:61 +0x198 fp=0xc00fe85fc8 sp=0xc00fe85e08 pc=0x2695d58
   > main.createServer.func1()
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:675 +0x26 fp=0xc00fe85fe0 sp=0xc00fe85fc8 pc=0x33b2be6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fe85fe8 sp=0xc00fe85fe0 pc=0x13ee6e1
   > created by main.createServer
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:675 +0x439
   > goroutine 737 [select]:
   > runtime.gopark(0xc010397e90?, 0x3?, 0x50?, 0x61?, 0xc010397e02?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010397c70 sp=0xc010397c50 pc=0x13bb516
   > runtime.selectgo(0xc010397e90, 0xc010397dfc, 0x3a8be78?, 0x0, 0x141f32a?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010397db0 sp=0xc010397c70 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).globalBindHandleWorkerLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1071 +0x16f fp=0xc010397fe0 sp=0xc010397db0 pc=0x26a476f
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010397fe8 sp=0xc010397fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).globalBindHandleWorkerLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1058 +0xad
   > goroutine 851 [select, locked to thread]:
   > runtime.gopark(0xc010557fa8?, 0x2?, 0x0?, 0x0?, 0xc010557fa4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010557e18 sp=0xc010557df8 pc=0x13bb516
   > runtime.selectgo(0xc010557fa8, 0xc010557fa0, 0x0?, 0x0, 0x400d678?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010557f58 sp=0xc010557e18 pc=0x13cbbdc
   > runtime.ensureSigM.func1()
   > 	/usr/local/go/src/runtime/signal_unix.go:995 +0x1b0 fp=0xc010557fe0 sp=0xc010557f58 pc=0x13d0070
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010557fe8 sp=0xc010557fe0 pc=0x13ee6e1
   > created by runtime.ensureSigM
   > 	/usr/local/go/src/runtime/signal_unix.go:978 +0xbd
   > goroutine 813 [select]:
   > runtime.gopark(0xc00fe07d48?, 0x2?, 0xe0?, 0xee?, 0xc00fe07c94?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fe07b08 sp=0xc00fe07ae8 pc=0x13bb516
   > runtime.selectgo(0xc00fe07d48, 0xc00fe07c90, 0xc01c635490?, 0x0, 0x1?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fe07c48 sp=0xc00fe07b08 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).loadStatsWorker(0xc000ffe360)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1304 +0x485 fp=0xc00fe07fc8 sp=0xc00fe07c48 pc=0x26a6ea5
   > github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1247 +0x26 fp=0xc00fe07fe0 sp=0xc00fe07fc8 pc=0x26a6666
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fe07fe8 sp=0xc00fe07fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1247 +0x105
   > goroutine 741 [select]:
   > runtime.gopark(0xc000b48718?, 0x3?, 0x4?, 0x30?, 0xc000b4869a?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000b484d8 sp=0xc000b484b8 pc=0x13bb516
   > runtime.selectgo(0xc000b48718, 0xc000b48694, 0xc0106ef6e0?, 0x0, 0xc011394c00?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000b48618 sp=0xc000b484d8 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).LoadPrivilegeLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:939 +0x145 fp=0xc000b487e0 sp=0xc000b48618 pc=0x26a3585
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000b487e8 sp=0xc000b487e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).LoadPrivilegeLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:930 +0x205
   > goroutine 814 [select]:
   > runtime.gopark(0xc01be65f28?, 0x6?, 0x50?, 0x60?, 0xc01be65bb4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01be65a20 sp=0xc01be65a00 pc=0x13bb516
   > runtime.selectgo(0xc01be65f28, 0xc01be65ba8, 0xc0187988c0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01be65b60 sp=0xc01be65a20 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).updateStatsWorker(0xc000ffe360, {0x309938e?, 0xc0113e4140?}, {0x401ea10, 0xc01057fd00})
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1372 +0x234 fp=0xc01be65fa8 sp=0xc01be65b60 pc=0x26a7e54
   > github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop.func3()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1259 +0x36 fp=0xc01be65fe0 sp=0xc01be65fa8 pc=0x26a65b6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01be65fe8 sp=0xc01be65fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1259 +0x29a
   > goroutine 816 [select]:
   > runtime.gopark(0xc000b89fa8?, 0x2?, 0x40?, 0x0?, 0xc000b89f7c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000b89e00 sp=0xc000b89de0 pc=0x13bb516
   > runtime.selectgo(0xc000b89fa8, 0xc000b89f78, 0xc0113e4180?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000b89f40 sp=0xc000b89e00 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).PlanReplayerLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1191 +0xf6 fp=0xc000b89fe0 sp=0xc000b89f40 pc=0x26a5f36
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000b89fe8 sp=0xc000b89fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).PlanReplayerLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1182 +0x6c
   > goroutine 811 [select]:
   > runtime.gopark(0xc00ff15728?, 0x2?, 0x4?, 0x30?, 0xc00ff156d4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00ff15548 sp=0xc00ff15528 pc=0x13bb516
   > runtime.selectgo(0xc00ff15728, 0xc00ff156d0, 0x9?, 0x0, 0x15?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00ff15688 sp=0xc00ff15548 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).TelemetryReportLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1140 +0x11c fp=0xc00ff157e0 sp=0xc00ff15688 pc=0x26a573c
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00ff157e8 sp=0xc00ff157e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).TelemetryReportLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1132 +0x285
   > goroutine 744 [select]:
   > runtime.gopark(0xc01c78ff18?, 0x3?, 0x4?, 0x30?, 0xc01c78fe8a?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01c78fcc8 sp=0xc01c78fca8 pc=0x13bb516
   > runtime.selectgo(0xc01c78ff18, 0xc01c78fe84, 0xc0110e3c00?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01c78fe08 sp=0xc01c78fcc8 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).LoadSysVarCacheLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:989 +0x145 fp=0xc01c78ffe0 sp=0xc01c78fe08 pc=0x26a3dc5
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01c78ffe8 sp=0xc01c78ffe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).LoadSysVarCacheLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:980 +0x172
   > goroutine 812 [select]:
   > runtime.gopark(0xc0110dd7a8?, 0x2?, 0x4?, 0x30?, 0xc0110dd784?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0110dd608 sp=0xc0110dd5e8 pc=0x13bb516
   > runtime.selectgo(0xc0110dd7a8, 0xc0110dd780, 0xc01148e120?, 0x0, 0xc0114299e0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0110dd748 sp=0xc0110dd608 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).TelemetryRotateSubWindowLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1169 +0xcc fp=0xc0110dd7e0 sp=0xc0110dd748 pc=0x26a5c4c
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0110dd7e8 sp=0xc0110dd7e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).TelemetryRotateSubWindowLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1162 +0x8f
   > goroutine 852 [syscall]:
   > runtime.notetsleepg(0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/lock_futex.go:236 +0x34 fp=0xc0105597a0 sp=0xc010559768 pc=0x138acd4
   > os/signal.signal_recv()
   > 	/usr/local/go/src/runtime/sigqueue.go:152 +0x2f fp=0xc0105597c0 sp=0xc0105597a0 pc=0x13ea6cf
   > os/signal.loop()
   > 	/usr/local/go/src/os/signal/signal_unix.go:23 +0x19 fp=0xc0105597e0 sp=0xc0105597c0 pc=0x2cac7f9
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0105597e8 sp=0xc0105597e0 pc=0x13ee6e1
   > created by os/signal.Notify.func1.1
   > 	/usr/local/go/src/os/signal/signal.go:151 +0x2a
   > goroutine 853 [chan receive]:
   > runtime.gopark(0x5f8be00?, 0xc010559f20?, 0x28?, 0xc3?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010559ea0 sp=0xc010559e80 pc=0x13bb516
   > runtime.chanrecv(0xc0113e36e0, 0xc010559fa0, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc010559f30 sp=0xc010559ea0 pc=0x13854bb
   > runtime.chanrecv1(0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc010559f58 sp=0xc010559f30 pc=0x1384fb8
   > github.com/pingcap/tidb/util/signal.SetupSignalHandler.func1()
   > 	/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:37 +0x4f fp=0xc010559fe0 sp=0xc010559f58 pc=0x33ac32f
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010559fe8 sp=0xc010559fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/util/signal.SetupSignalHandler
   > 	/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:34 +0xb6
   > goroutine 856 [chan receive]:
   > runtime.gopark(0x3a8bf40?, 0xc0003b9cf8?, 0xfc?, 0xb?, 0xa?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0003b9cb0 sp=0xc0003b9c90 pc=0x13bb516
   > runtime.chanrecv(0xc0113e3bc0, 0xc0003b9d78, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc0003b9d40 sp=0xc0003b9cb0 pc=0x13854bb
   > runtime.chanrecv2(0xc010c972f8?, 0x2?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc0003b9d68 sp=0xc0003b9d40 pc=0x1384ff8
   > github.com/soheilhy/cmux.muxListener.Accept(...)
   > 	/go/pkg/mod/github.com/soheilhy/cmux@v0.1.4/cmux.go:229
   > github.com/soheilhy/cmux.(*muxListener).Accept(0x3ff0f40?)
   > 	<autogenerated>:1 +0x45 fp=0xc0003b9d98 sp=0xc0003b9d68 pc=0x2dc7625
   > google.golang.org/grpc.(*Server).Serve(0xc000870680, {0x400cb50, 0xc011b002e8})
   > 	/go/pkg/mod/google.golang.org/grpc@v1.29.1/server.go:621 +0x362 fp=0xc0003b9eb0 sp=0xc0003b9d98 pc=0x19749a2
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer.func1()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:457 +0x3e fp=0xc0003b9f90 sp=0xc0003b9eb0 pc=0x31db01e
   > github.com/pingcap/tidb/util.WithRecovery(0x31d65c6?, 0xc0113e3980?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc0003b9fc0 sp=0xc0003b9f90 pc=0x1ffabd3
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer.func5()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:456 +0x28 fp=0xc0003b9fe0 sp=0xc0003b9fc0 pc=0x31dafa8
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0003b9fe8 sp=0xc0003b9fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:456 +0x42c
   > goroutine 857 [chan receive]:
   > runtime.gopark(0x50?, 0xc011b0d800?, 0x8?, 0x3d?, 0x138c1bf?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0000a3c80 sp=0xc0000a3c60 pc=0x13bb516
   > runtime.chanrecv(0xc0113e3b60, 0xc0000a3d48, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc0000a3d10 sp=0xc0000a3c80 pc=0x13854bb
   > runtime.chanrecv2(0x141e886?, 0xc011b03190?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc0000a3d38 sp=0xc0000a3d10 pc=0x1384ff8
   > github.com/soheilhy/cmux.muxListener.Accept(...)
   > 	/go/pkg/mod/github.com/soheilhy/cmux@v0.1.4/cmux.go:229
   > github.com/soheilhy/cmux.(*muxListener).Accept(0x5828400?)
   > 	<autogenerated>:1 +0x45 fp=0xc0000a3d68 sp=0xc0000a3d38 pc=0x2dc7625
   > net/http.(*onceCloseListener).Accept(0x400d640?)
   > 	<autogenerated>:1 +0x2a fp=0xc0000a3d80 sp=0xc0000a3d68 pc=0x16e0c6a
   > net/http.(*Server).Serve(0xc000ebfc20, {0x400cb50, 0xc011b002d0})
   > 	/usr/local/go/src/net/http/server.go:3070 +0x385 fp=0xc0000a3eb0 sp=0xc0000a3d80 pc=0x16b6f45
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer.func2()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:462 +0x3e fp=0xc0000a3f90 sp=0xc0000a3eb0 pc=0x31dadbe
   > github.com/pingcap/tidb/util.WithRecovery(0x0?, 0x0?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc0000a3fc0 sp=0xc0000a3f90 pc=0x1ffabd3
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer.func6()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:461 +0x28 fp=0xc0000a3fe0 sp=0xc0000a3fc0 pc=0x31dad48
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000a3fe8 sp=0xc0000a3fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:461 +0x4ea
   > goroutine 5056 [chan receive]:
   > runtime.gopark(0x13c37d1?, 0xc0010469d0?, 0x0?, 0x38?, 0xc01c27e290?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0010469c0 sp=0xc0010469a0 pc=0x13bb516
   > runtime.chanrecv(0xc01ae84e40, 0xc001046b10, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc001046a50 sp=0xc0010469c0 pc=0x13854bb
   > runtime.chanrecv2(0xc010df4000?, 0x400d6b0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc001046a78 sp=0xc001046a50 pc=0x1384ff8
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Next(0xc010df4000, {0x400d6b0?, 0xc01bbde2d0?}, 0xc010e57810)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:681 +0x652 fp=0xc001046b38 sp=0xc001046a78 pc=0x3064d52
   > github.com/pingcap/tidb/executor.Next({0x400d6b0, 0xc01bbde2d0}, {0x40101a0, 0xc010df4000}, 0xc010e57810)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:286 +0x4a8 fp=0xc001046c78 sp=0xc001046b38 pc=0x2fef688
   > github.com/pingcap/tidb/executor.(*ProjectionExec).unParallelExecute(0xc010df2240, {0x400d6b0?, 0xc01bbde2d0?}, 0xc010a7e2d0)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:194 +0xb8 fp=0xc001046cc8 sp=0xc001046c78 pc=0x3098758
   > github.com/pingcap/tidb/executor.(*ProjectionExec).Next(0xc010df2240, {0x400d6b0, 0xc01bbde2d0}, 0xc018c73730?)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:180 +0x5a fp=0xc001046d00 sp=0xc001046cc8 pc=0x309861a
   > github.com/pingcap/tidb/executor.Next({0x400d6b0, 0xc01bbde2d0}, {0x4010760, 0xc010df2240}, 0xc010a7e2d0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:286 +0x4a8 fp=0xc001046e40 sp=0xc001046d00 pc=0x2fef688
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchBuildSideRows(0xc010df4240, {0x400d6b0, 0xc01bbde2d0}, 0xc01c5cfe60, 0xc012ffcd20)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:266 +0x1a5 fp=0xc001046f10 sp=0xc001046e40 pc=0x3060845
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:715 +0xab fp=0xc001046f90 sp=0xc001046f10 pc=0x306572b
   > github.com/pingcap/tidb/util.WithRecovery(0x23de786?, 0xc0106b3940?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc001046fc0 sp=0xc001046f90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:712 +0x2a fp=0xc001046fe0 sp=0xc001046fc0 pc=0x306558a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc001046fe8 sp=0xc001046fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:712 +0x22d
   > goroutine 5083 [chan receive]:
   > runtime.gopark(0xc010ad6000?, 0xc01c5cff20?, 0x3?, 0x0?, 0xc010e87cf8?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010e87ca8 sp=0xc010e87c88 pc=0x13bb516
   > runtime.chanrecv(0xc01c5cfe60, 0xc010e87e08, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc010e87d38 sp=0xc010e87ca8 pc=0x13854bb
   > runtime.chanrecv2(0xc0108f6eb0?, 0x4012e60?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc010e87d60 sp=0xc010e87d38 pc=0x1384ff8
   > github.com/pingcap/tidb/executor.(*HashJoinExec).buildHashTableForList(0xc010df4240, 0x1?)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:762 +0x2d6 fp=0xc010e87e78 sp=0xc010e87d60 pc=0x3065af6
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable(0xc010df4240, {0x400d6b0?, 0xc01bbde2d0})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:726 +0x23f fp=0xc010e87f28 sp=0xc010e87e78 pc=0x30653ff
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Next.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:671 +0x8f fp=0xc010e87f90 sp=0xc010e87f28 pc=0x306504f
   > github.com/pingcap/tidb/util.WithRecovery(0xc0113456c0?, 0xc01a361d38?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc010e87fc0 sp=0xc010e87f90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Next.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:669 +0x2a fp=0xc010e87fe0 sp=0xc010e87fc0 pc=0x3064f8a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010e87fe8 sp=0xc010e87fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).Next
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:669 +0x5b2
   > goroutine 5111 [select]:
   > runtime.gopark(0xc0110dce10?, 0x2?, 0x8?, 0xcd?, 0xc0110dcd8c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0110dcbe0 sp=0xc0110dcbc0 pc=0x13bb516
   > runtime.selectgo(0xc0110dce10, 0xc0110dcd88, 0xc012fab090?, 0x0, 0xc000b7b790?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0110dcd20 sp=0xc0110dcbe0 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc010df4000, 0x4, {0x5f8a1a8, 0x0, 0x0})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:441 +0x4f4 fp=0xc0110dcf10 sp=0xc0110dcd20 pc=0x30626b4
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:335 +0xb3 fp=0xc0110dcf90 sp=0xc0110dcf10 pc=0x30613d3
   > github.com/pingcap/tidb/util.WithRecovery(0x23de786?, 0xc0110dcd38?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc0110dcfc0 sp=0xc0110dcf90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x2a fp=0xc0110dcfe0 sp=0xc0110dcfc0 pc=0x30612ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0110dcfe8 sp=0xc0110dcfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x1c9
   > goroutine 5022 [chan receive]:
   > runtime.gopark(0x7c0122db1?, 0x0?, 0x80?, 0xee?, 0x138c1bf?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010c8edf8 sp=0xc010c8edd8 pc=0x13bb516
   > runtime.chanrecv(0xc0105139e0, 0xc010c8ef38, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc010c8ee88 sp=0xc010c8edf8 pc=0x13854bb
   > runtime.chanrecv2(0xc010df4440?, 0x35182e0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc010c8eeb0 sp=0xc010c8ee88 pc=0x1384ff8
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Close(0xc010df4240)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:123 +0x385 fp=0xc010c8ef58 sp=0xc010c8eeb0 pc=0x305fcc5
   > github.com/pingcap/tidb/executor.(*baseExecutor).Close(0xc01a6dffe0?)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:181 +0x7c fp=0xc010c8ef98 sp=0xc010c8ef58 pc=0x2feeadc
   > github.com/pingcap/tidb/executor.(*ProjectionExec).Close(0xc010df2360)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:329 +0x1cf fp=0xc010c8f000 sp=0xc010c8ef98 pc=0x30997af
   > github.com/pingcap/tidb/executor.(*recordSet).Close(0xc0110140f0)
   > 	/go/src/github.com/pingcap/tidb/executor/adapter.go:176 +0x2a fp=0xc010c8f040 sp=0xc010c8f000 pc=0x2f612ca
   > github.com/pingcap/tidb/session.(*execStmtResult).Close(0xc01c01df50)
   > 	/go/src/github.com/pingcap/tidb/session/session.go:1734 +0x36 fp=0xc010c8f090 sp=0xc010c8f040 pc=0x314b676
   > github.com/pingcap/tidb/server.(*tidbResultSet).Close(0xbf4aa58d?)
   > 	/go/src/github.com/pingcap/tidb/server/driver_tidb.go:324 +0x3c fp=0xc010c8f0b0 sp=0xc010c8f090 pc=0x31c611c
   > github.com/pingcap/tidb/server.ResultSet.Close-fm()
   > 	<autogenerated>:1 +0x2b fp=0xc010c8f0c8 sp=0xc010c8f0b0 pc=0x31f7acb
   > github.com/pingcap/tidb/parser/terror.Call(0xc010c8f1d8?)
   > 	/go/src/github.com/pingcap/tidb/parser/terror/terror.go:298 +0x31 fp=0xc010c8f208 sp=0xc010c8f0c8 pc=0x1b74a51
   > github.com/pingcap/tidb/server.(*clientConn).handleStmt.func1()
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:1911 +0x26 fp=0xc010c8f220 sp=0xc010c8f208 pc=0x31bbd26
   > github.com/pingcap/tidb/server.(*clientConn).handleStmt(0xc0108c7a40, {0x400d608, 0xc00fed6080}, {0x401fff0, 0xc0104fb4a0}, {0x5f8a1a8, 0x0, 0x0}, 0x1)
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:1934 +0x413 fp=0xc010c8f2f0 sp=0xc010c8f220 pc=0x31bbaf3
   > github.com/pingcap/tidb/server.(*clientConn).handleQuery(0xc0108c7a40, {0x400d608, 0xc00fed6080}, {0xc0180cc4e1, 0x18c})
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:1775 +0x774 fp=0xc010c8f468 sp=0xc010c8f2f0 pc=0x31ba494
   > github.com/pingcap/tidb/server.(*clientConn).dispatch(0xc0108c7a40, {0x400d6b0, 0xc01b801470?}, {0xc0180cc4e0, 0x18d, 0x18d})
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:1279 +0x1025 fp=0xc010c8f858 sp=0xc010c8f468 pc=0x31b6045
   > github.com/pingcap/tidb/server.(*clientConn).Run(0xc0108c7a40, {0x400d6b0, 0xc01b801470})
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:1034 +0x253 fp=0xc010c8fe18 sp=0xc010c8f858 pc=0x31b2b33
   > github.com/pingcap/tidb/server.(*Server).onConn(0xc0113456c0, 0xc0108c7a40)
   > 	/go/src/github.com/pingcap/tidb/server/server.go:550 +0x6c5 fp=0xc010c8ffc0 sp=0xc010c8fe18 pc=0x31e4165
   > github.com/pingcap/tidb/server.(*Server).startNetworkListener.func2()
   > 	/go/src/github.com/pingcap/tidb/server/server.go:453 +0x2a fp=0xc010c8ffe0 sp=0xc010c8ffc0 pc=0x31e300a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010c8ffe8 sp=0xc010c8ffe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/server.(*Server).startNetworkListener
   > 	/go/src/github.com/pingcap/tidb/server/server.go:453 +0x5ca
   > goroutine 5001 [select]:
   > runtime.gopark(0xc010e81f78?, 0x2?, 0xa0?, 0x1d?, 0xc010e81eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010e81d58 sp=0xc010e81d38 pc=0x13bb516
   > runtime.selectgo(0xc010e81f78, 0xc010e81ee8, 0xc000c5f800?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010e81e98 sp=0xc010e81d58 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc011b50ac0, {0x400d6b0?, 0xc01bbde2d0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc010e81fb8 sp=0xc010e81e98 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc010e81fe0 sp=0xc010e81fb8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010e81fe8 sp=0xc010e81fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 5112 [semacquire]:
   > runtime.gopark(0x0?, 0x1980?, 0xa0?, 0xf1?, 0x5f60880?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01b9ea678 sp=0xc01b9ea658 pc=0x13bb516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc010df41f8, 0x54?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc01b9ea6e0 sp=0xc01b9ea678 pc=0x13cce5e
   > sync.runtime_Semacquire(0xc019825ec0?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc01b9ea710 sp=0xc01b9ea6e0 pc=0x13e9f65
   > sync.(*WaitGroup).Wait(0xc016e80c01?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc01b9ea738 sp=0xc01b9ea710 pc=0x13fd1f2
   > github.com/pingcap/tidb/executor.(*HashJoinExec).waitJoinWorkersAndCloseResultChan(0xc010df4000)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:395 +0x33 fp=0xc01b9ea778 sp=0xc01b9ea738 pc=0x3061fb3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).waitJoinWorkersAndCloseResultChan-fm()
   > 	<autogenerated>:1 +0x26 fp=0xc01b9ea790 sp=0xc01b9ea778 pc=0x31277c6
   > github.com/pingcap/tidb/util.WithRecovery(0x23de786?, 0xc016e819c0?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc01b9ea7c0 sp=0xc01b9ea790 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:338 +0x28 fp=0xc01b9ea7e0 sp=0xc01b9ea7c0 pc=0x3061288
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01b9ea7e8 sp=0xc01b9ea7e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:338 +0x3b8
   > goroutine 5110 [select]:
   > runtime.gopark(0xc0110e1e10?, 0x2?, 0xf8?, 0xcc?, 0xc0110e1d8c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0110e1be0 sp=0xc0110e1bc0 pc=0x13bb516
   > runtime.selectgo(0xc0110e1e10, 0xc0110e1d88, 0x172d28d?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0110e1d20 sp=0xc0110e1be0 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc010df4000, 0x3, {0x5f8a1a8, 0x0, 0x0})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:441 +0x4f4 fp=0xc0110e1f10 sp=0xc0110e1d20 pc=0x30626b4
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:335 +0xb3 fp=0xc0110e1f90 sp=0xc0110e1f10 pc=0x30613d3
   > github.com/pingcap/tidb/util.WithRecovery(0xc01b289ba0?, 0xc0110e1fa0?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc0110e1fc0 sp=0xc0110e1f90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x2a fp=0xc0110e1fe0 sp=0xc0110e1fc0 pc=0x30612ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0110e1fe8 sp=0xc0110e1fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x1c9
   > goroutine 5057 [chan receive]:
   > runtime.gopark(0xc010ad6000?, 0xc01ae84f60?, 0x3?, 0x0?, 0xc00104dcf8?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00104dca8 sp=0xc00104dc88 pc=0x13bb516
   > runtime.chanrecv(0xc01ae84ea0, 0xc00104de08, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc00104dd38 sp=0xc00104dca8 pc=0x13854bb
   > runtime.chanrecv2(0xc0108f6eb0?, 0x4012e60?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc00104dd60 sp=0xc00104dd38 pc=0x1384ff8
   > github.com/pingcap/tidb/executor.(*HashJoinExec).buildHashTableForList(0xc010df4000, 0x1?)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:762 +0x2d6 fp=0xc00104de78 sp=0xc00104dd60 pc=0x3065af6
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable(0xc010df4000, {0x400d6b0?, 0xc01bbde2d0})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:726 +0x23f fp=0xc00104df28 sp=0xc00104de78 pc=0x30653ff
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Next.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:671 +0x8f fp=0xc00104df90 sp=0xc00104df28 pc=0x306504f
   > github.com/pingcap/tidb/util.WithRecovery(0x23de786?, 0xc0106b3940?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc00104dfc0 sp=0xc00104df90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Next.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:669 +0x2a fp=0xc00104dfe0 sp=0xc00104dfc0 pc=0x3064f8a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00104dfe8 sp=0xc00104dfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).Next
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:669 +0x5b2
   > goroutine 5004 [select]:
   > runtime.gopark(0xc01a365778?, 0x2?, 0x1?, 0x55?, 0xc01a3656ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01a365558 sp=0xc01a365538 pc=0x13bb516
   > runtime.selectgo(0xc01a365778, 0xc01a3656e8, 0x3aac226?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01a365698 sp=0xc01a365558 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc011b50b80, {0x400d6b0?, 0xc01bbde2d0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc01a3657b8 sp=0xc01a365698 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc01a3657e0 sp=0xc01a3657b8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01a3657e8 sp=0xc01a3657e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 5106 [select]:
   > runtime.gopark(0xc00102fe30?, 0x2?, 0x80?, 0x57?, 0xc00102fe1c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00102fca8 sp=0xc00102fc88 pc=0x13bb516
   > runtime.selectgo(0xc00102fe30, 0xc00102fe18, 0xc01336be60?, 0x0, 0x2fef900?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00102fde8 sp=0xc00102fca8 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).wait4BuildSide(0xc010df4000)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:242 +0x6f fp=0xc00102fe60 sp=0xc00102fde8 pc=0x30605ef
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchProbeSideChunks(0xc010df4000, {0x400d6b0, 0xc01bbde2d0})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:221 +0x233 fp=0xc00102ff28 sp=0xc00102fe60 pc=0x3060333
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:322 +0x8f fp=0xc00102ff90 sp=0xc00102ff28 pc=0x306156f
   > github.com/pingcap/tidb/util.WithRecovery(0xc0113456c0?, 0xc01a361d38?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc00102ffc0 sp=0xc00102ff90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func3()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:320 +0x2a fp=0xc00102ffe0 sp=0xc00102ffc0 pc=0x30614aa
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00102ffe8 sp=0xc00102ffe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:320 +0x14f
   > goroutine 5002 [select]:
   > runtime.gopark(0xc0110dff78?, 0x2?, 0x2?, 0x0?, 0xc0110dfeec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0110dfd58 sp=0xc0110dfd38 pc=0x13bb516
   > runtime.selectgo(0xc0110dff78, 0xc0110dfee8, 0x3aac226?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0110dfe98 sp=0xc0110dfd58 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc011b50b00, {0x400d6b0?, 0xc01bbde2d0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc0110dffb8 sp=0xc0110dfe98 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc0110dffe0 sp=0xc0110dffb8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0110dffe8 sp=0xc0110dffe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 5109 [select]:
   > runtime.gopark(0xc015ab9e10?, 0x2?, 0xe0?, 0xcc?, 0xc015ab9d8c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc015ab9be0 sp=0xc015ab9bc0 pc=0x13bb516
   > runtime.selectgo(0xc015ab9e10, 0xc015ab9d88, 0xc015ab9da8?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc015ab9d20 sp=0xc015ab9be0 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc010df4000, 0x2, {0x5f8a1a8, 0x0, 0x0})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:441 +0x4f4 fp=0xc015ab9f10 sp=0xc015ab9d20 pc=0x30626b4
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:335 +0xb3 fp=0xc015ab9f90 sp=0xc015ab9f10 pc=0x30613d3
   > github.com/pingcap/tidb/util.WithRecovery(0x2?, 0xc015ab9d38?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc015ab9fc0 sp=0xc015ab9f90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x2a fp=0xc015ab9fe0 sp=0xc015ab9fc0 pc=0x30612ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc015ab9fe8 sp=0xc015ab9fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x1c9
   > goroutine 5003 [select]:
   > runtime.gopark(0xc0110da778?, 0x2?, 0x2?, 0x0?, 0xc0110da6ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0110da558 sp=0xc0110da538 pc=0x13bb516
   > runtime.selectgo(0xc0110da778, 0xc0110da6e8, 0x3aac226?, 0x0, 0x7bfa5ef94?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0110da698 sp=0xc0110da558 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc011b50b40, {0x400d6b0?, 0xc01bbde2d0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc0110da7b8 sp=0xc0110da698 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc0110da7e0 sp=0xc0110da7b8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0110da7e8 sp=0xc0110da7e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 5107 [select]:
   > runtime.gopark(0xc015ab7610?, 0x2?, 0xb0?, 0xcc?, 0xc015ab758c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc015ab73e0 sp=0xc015ab73c0 pc=0x13bb516
   > runtime.selectgo(0xc015ab7610, 0xc015ab7588, 0x0?, 0x0, 0xc000b7b790?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc015ab7520 sp=0xc015ab73e0 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc010df4000, 0x0, {0x5f8a1a8, 0x0, 0x0})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:441 +0x4f4 fp=0xc015ab7710 sp=0xc015ab7520 pc=0x30626b4
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:335 +0xb3 fp=0xc015ab7790 sp=0xc015ab7710 pc=0x30613d3
   > github.com/pingcap/tidb/util.WithRecovery(0x400d6b0?, 0xc01c256bd0?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc015ab77c0 sp=0xc015ab7790 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x2a fp=0xc015ab77e0 sp=0xc015ab77c0 pc=0x30612ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc015ab77e8 sp=0xc015ab77e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x1c9
   > goroutine 5138 [select]:
   > runtime.gopark(0xc010647f78?, 0x2?, 0xa0?, 0x7d?, 0xc010647eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010647d58 sp=0xc010647d38 pc=0x13bb516
   > runtime.selectgo(0xc010647f78, 0xc010647ee8, 0xc000c5f800?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010647e98 sp=0xc010647d58 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc010bb9640, {0x400d6b0?, 0xc01bbde2d0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc010647fb8 sp=0xc010647e98 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc010647fe0 sp=0xc010647fb8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010647fe8 sp=0xc010647fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 5139 [select]:
   > runtime.gopark(0xc010ccdf78?, 0x2?, 0x2?, 0x0?, 0xc010ccdeec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010ccdd58 sp=0xc010ccdd38 pc=0x13bb516
   > runtime.selectgo(0xc010ccdf78, 0xc010ccdee8, 0x3aac226?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010ccde98 sp=0xc010ccdd58 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc010bb9680, {0x400d6b0?, 0xc01bbde2d0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc010ccdfb8 sp=0xc010ccde98 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc010ccdfe0 sp=0xc010ccdfb8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010ccdfe8 sp=0xc010ccdfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 5140 [select]:
   > runtime.gopark(0xc010cc9778?, 0x2?, 0x2?, 0x0?, 0xc010cc96ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010cc9558 sp=0xc010cc9538 pc=0x13bb516
   > runtime.selectgo(0xc010cc9778, 0xc010cc96e8, 0x3aac226?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010cc9698 sp=0xc010cc9558 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc010bb96c0, {0x400d6b0?, 0xc01bbde2d0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc010cc97b8 sp=0xc010cc9698 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc010cc97e0 sp=0xc010cc97b8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010cc97e8 sp=0xc010cc97e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 5141 [select]:
   > runtime.gopark(0xc00ff14778?, 0x2?, 0x2?, 0x0?, 0xc00ff146ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00ff14558 sp=0xc00ff14538 pc=0x13bb516
   > runtime.selectgo(0xc00ff14778, 0xc00ff146e8, 0x3aac226?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00ff14698 sp=0xc00ff14558 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc010bb9700, {0x400d6b0?, 0xc01bbde2d0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc00ff147b8 sp=0xc00ff14698 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc00ff147e0 sp=0xc00ff147b8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00ff147e8 sp=0xc00ff147e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 5142 [select]:
   > runtime.gopark(0xc010558f78?, 0x2?, 0x1?, 0x0?, 0xc010558eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010558d58 sp=0xc010558d38 pc=0x13bb516
   > runtime.selectgo(0xc010558f78, 0xc010558ee8, 0x3aac226?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010558e98 sp=0xc010558d58 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc010bb9740, {0x400d6b0?, 0xc01bbde2d0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc010558fb8 sp=0xc010558e98 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc010558fe0 sp=0xc010558fb8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010558fe8 sp=0xc010558fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
