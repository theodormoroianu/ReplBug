# Bug ID TIDB-30326-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/30326
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ


## Details
 * Database: tidb-5.2.1
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
   > [2024/06/18 11:58:41.293 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=53] [schemaVersion=195] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:41.294 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:216, Type:drop schema, State:none, SchemaState:queueing, SchemaID:211, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:41.294 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 11:58:41.294 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:216, Type:drop schema, State:none, SchemaState:queueing, SchemaID:211, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:41.294 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/06/18 11:58:41.295 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:216, Type:drop schema, State:none, SchemaState:queueing, SchemaID:211, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:41.294 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:41.296 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=195] [neededSchemaVersion=196] ["start time"=102.668µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 11:58:41.298 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=196] ["take time"=2.266931ms] [job="ID:216, Type:drop schema, State:running, SchemaState:write only, SchemaID:211, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:41.294 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:41.298 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:216, Type:drop schema, State:running, SchemaState:write only, SchemaID:211, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:41.294 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:41.299 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=196] [neededSchemaVersion=197] ["start time"=72.077µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 11:58:41.301 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=197] ["take time"=2.336285ms] [job="ID:216, Type:drop schema, State:running, SchemaState:delete only, SchemaID:211, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:41.294 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:41.301 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:216, Type:drop schema, State:running, SchemaState:delete only, SchemaID:211, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:41.294 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:41.302 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=197] [neededSchemaVersion=198] ["start time"=77.873µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 11:58:41.304 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=198] ["take time"=2.245071ms] [job="ID:216, Type:drop schema, State:done, SchemaState:queueing, SchemaID:211, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:41.294 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:41.305 +00:00] [INFO] [delete_range.go:106] ["[ddl] add job into delete-range table"] [jobID=216] [jobType="drop schema"]
   > [2024/06/18 11:58:41.305 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:216, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:211, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:41.294 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:41.306 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=216]
   > [2024/06/18 11:58:41.306 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/18 11:58:41.308 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=53] [schemaVersion=198] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:41.309 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:218, Type:create schema, State:none, SchemaState:queueing, SchemaID:217, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:41.308 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 11:58:41.309 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:218, Type:create schema, State:none, SchemaState:queueing, SchemaID:217, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:41.308 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/18 11:58:41.310 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:218, Type:create schema, State:none, SchemaState:queueing, SchemaID:217, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:41.308 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:41.311 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=198] [neededSchemaVersion=199] ["start time"=139.335µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 11:58:41.313 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=199] ["take time"=2.240811ms] [job="ID:218, Type:create schema, State:done, SchemaState:public, SchemaID:217, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:41.308 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:41.314 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:218, Type:create schema, State:synced, SchemaState:public, SchemaID:217, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:41.308 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:41.314 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=218]
   > [2024/06/18 11:58:41.314 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/18 11:58:41.528 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=53] [schemaVersion=199] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_037irb`\n--\n\nDROP TABLE IF EXISTS `t_037irb`;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:41.529 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=53] [schemaVersion=199] [cur_db=testdb] [sql="CREATE TABLE `t_037irb` (\n  `c_nrh3o` int(11) DEFAULT NULL,\n  `c_nfauxb` text DEFAULT NULL,\n  `c_y5n4c` int(11) DEFAULT NULL,\n  `c_j9alg` double NOT NULL,\n  `c_4vix1d` text DEFAULT NULL,\n  `c_glkxdb` text DEFAULT NULL,\n  `c_2ykt0d` int(11) DEFAULT NULL,\n  `c_5fxv3c` double DEFAULT NULL,\n  PRIMARY KEY (`c_j9alg`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:41.531 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:220, Type:create table, State:none, SchemaState:queueing, SchemaID:217, TableID:219, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:41.53 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 11:58:41.531 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:220, Type:create table, State:none, SchemaState:queueing, SchemaID:217, TableID:219, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:41.53 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_037irb` (\n  `c_nrh3o` int(11) DEFAULT NULL,\n  `c_nfauxb` text DEFAULT NULL,\n  `c_y5n4c` int(11) DEFAULT NULL,\n  `c_j9alg` double NOT NULL,\n  `c_4vix1d` text DEFAULT NULL,\n  `c_glkxdb` text DEFAULT NULL,\n  `c_2ykt0d` int(11) DEFAULT NULL,\n  `c_5fxv3c` double DEFAULT NULL,\n  PRIMARY KEY (`c_j9alg`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/18 11:58:41.532 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:220, Type:create table, State:none, SchemaState:queueing, SchemaID:217, TableID:219, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:41.53 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:41.534 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=199] [neededSchemaVersion=200] ["start time"=455.161µs] [phyTblIDs="[219]"] [actionTypes="[8]"]
   > [2024/06/18 11:58:41.536 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=200] ["take time"=2.049514ms] [job="ID:220, Type:create table, State:done, SchemaState:public, SchemaID:217, TableID:219, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:41.53 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:41.537 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:220, Type:create table, State:synced, SchemaState:public, SchemaID:217, TableID:219, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:41.53 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:41.538 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=220]
   > [2024/06/18 11:58:41.538 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/18 11:58:41.538 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=98] ["first split key"=7480000000000000db]
   > [2024/06/18 11:58:41.539 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=98] ["first at"=7480000000000000db] ["first new region left"="{Id:98 StartKey:7480000000000000ffd500000000000000f8 EndKey:7480000000000000ffdb00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:99 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/18 11:58:41.539 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[98]"]
   > [2024/06/18 11:58:41.539 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=53] [schemaVersion=200] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_037irb` DISABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:41.540 +00:00] [WARN] [2pc.go:1598] ["schemaLeaseChecker is not set for this transaction"] [sessionID=53] [startTS=450550017960181761] [commitTS=450550017960181762]
   > [2024/06/18 11:58:41.542 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=53] [schemaVersion=200] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_037irb` ENABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:41.542 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=53] [schemaVersion=200] [cur_db=testdb] [sql="\n--\n-- Temporary view structure for view `t_cpsvpb`\n--\n\nDROP TABLE IF EXISTS `t_cpsvpb`;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:41.542 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=53] [schemaVersion=200] [cur_db=testdb] [sql="/*!50001 DROP VIEW IF EXISTS `t_cpsvpb`*/;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:41.545 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:222, Type:create view, State:none, SchemaState:queueing, SchemaID:217, TableID:221, RowCount:0, ArgLen:3, start time: 2024-06-18 11:58:41.544 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 11:58:41.545 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:222, Type:create view, State:none, SchemaState:queueing, SchemaID:217, TableID:221, RowCount:0, ArgLen:3, start time: 2024-06-18 11:58:41.544 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="/*!50001 CREATE VIEW `t_cpsvpb` AS SELECT \n 1 AS `c0`,\n 1 AS `c2`,\n 1 AS `c3`,\n 1 AS `c4`,\n 1 AS `c5`,\n 1 AS `c6`,\n 1 AS `c7`,\n 1 AS `c8`,\n 1 AS `c9`,\n 1 AS `c10`,\n 1 AS `c11`,\n 1 AS `c12`,\n 1 AS `c13`,\n 1 AS `c14`*/;"]
   > [2024/06/18 11:58:41.546 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:222, Type:create view, State:none, SchemaState:queueing, SchemaID:217, TableID:221, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:41.544 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:41.549 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=200] [neededSchemaVersion=201] ["start time"=650.159µs] [phyTblIDs="[221]"] [actionTypes="[2097152]"]
   > [2024/06/18 11:58:41.550 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=201] ["take time"=2.239902ms] [job="ID:222, Type:create view, State:done, SchemaState:public, SchemaID:217, TableID:221, RowCount:0, ArgLen:3, start time: 2024-06-18 11:58:41.544 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:41.552 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:222, Type:create view, State:synced, SchemaState:public, SchemaID:217, TableID:221, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:41.544 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:41.553 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=222]
   > [2024/06/18 11:58:41.553 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/18 11:58:41.554 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=53] [schemaVersion=201] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_x7zqmd`\n--\n\nDROP TABLE IF EXISTS `t_x7zqmd`;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:41.555 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=53] [schemaVersion=201] [cur_db=testdb] [sql="CREATE TABLE `t_x7zqmd` (\n  `c_8weeq` int(11) NOT NULL,\n  `c_13sfid` double DEFAULT NULL,\n  `c_hhjlmc` text DEFAULT NULL,\n  `c_3b1zld` int(11) DEFAULT NULL,\n  `c_6tu8wd` int(11) DEFAULT NULL,\n  `c_jyc_cd` double DEFAULT NULL,\n  PRIMARY KEY (`c_8weeq`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:41.556 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:224, Type:create table, State:none, SchemaState:queueing, SchemaID:217, TableID:223, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:41.555 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 11:58:41.556 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:224, Type:create table, State:none, SchemaState:queueing, SchemaID:217, TableID:223, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:41.555 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_x7zqmd` (\n  `c_8weeq` int(11) NOT NULL,\n  `c_13sfid` double DEFAULT NULL,\n  `c_hhjlmc` text DEFAULT NULL,\n  `c_3b1zld` int(11) DEFAULT NULL,\n  `c_6tu8wd` int(11) DEFAULT NULL,\n  `c_jyc_cd` double DEFAULT NULL,\n  PRIMARY KEY (`c_8weeq`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/18 11:58:41.557 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:224, Type:create table, State:none, SchemaState:queueing, SchemaID:217, TableID:223, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:41.555 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:41.559 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=201] [neededSchemaVersion=202] ["start time"=438.747µs] [phyTblIDs="[223]"] [actionTypes="[8]"]
   > [2024/06/18 11:58:41.560 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=202] ["take time"=2.055311ms] [job="ID:224, Type:create table, State:done, SchemaState:public, SchemaID:217, TableID:223, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:41.555 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:41.561 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:224, Type:create table, State:synced, SchemaState:public, SchemaID:217, TableID:223, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:41.555 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:41.562 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=224]
   > [2024/06/18 11:58:41.562 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/18 11:58:41.562 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=100] ["first split key"=7480000000000000df]
   > [2024/06/18 11:58:41.563 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=100] ["first at"=7480000000000000df] ["first new region left"="{Id:100 StartKey:7480000000000000ffdb00000000000000f8 EndKey:7480000000000000ffdf00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:101 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/18 11:58:41.563 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[100]"]
   > [2024/06/18 11:58:41.563 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=53] [schemaVersion=202] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_x7zqmd` DISABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:41.566 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=53] [schemaVersion=202] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_x7zqmd` ENABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:41.566 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=53] [schemaVersion=202] [cur_db=testdb] [sql="\n--\n-- Final view structure for view `t_cpsvpb`\n--\n\n/*!50001 DROP VIEW IF EXISTS `t_cpsvpb`*/;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:41.567 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:225, Type:drop view, State:none, SchemaState:queueing, SchemaID:217, TableID:221, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:41.567 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 11:58:41.567 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:225, Type:drop view, State:none, SchemaState:queueing, SchemaID:217, TableID:221, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:41.567 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="\n--\n-- Final view structure for view `t_cpsvpb`\n--\n\n/*!50001 DROP VIEW IF EXISTS `t_cpsvpb`*/;"]
   > [2024/06/18 11:58:41.568 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:225, Type:drop view, State:none, SchemaState:queueing, SchemaID:217, TableID:221, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:41.567 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:41.569 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=202] [neededSchemaVersion=203] ["start time"=83.322µs] [phyTblIDs="[221]"] [actionTypes="[16777216]"]
   > [2024/06/18 11:58:41.571 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=203] ["take time"=2.053425ms] [job="ID:225, Type:drop view, State:running, SchemaState:write only, SchemaID:217, TableID:221, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:41.567 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:41.571 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:225, Type:drop view, State:running, SchemaState:write only, SchemaID:217, TableID:221, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:41.567 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:41.573 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=203] [neededSchemaVersion=204] ["start time"=105.042µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 11:58:41.575 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=204] ["take time"=2.754987ms] [job="ID:225, Type:drop view, State:running, SchemaState:delete only, SchemaID:217, TableID:221, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:41.567 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:41.576 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:225, Type:drop view, State:running, SchemaState:delete only, SchemaID:217, TableID:221, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:41.567 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:41.577 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=204] [neededSchemaVersion=205] ["start time"=85.277µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 11:58:41.580 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=205] ["take time"=2.546859ms] [job="ID:225, Type:drop view, State:done, SchemaState:queueing, SchemaID:217, TableID:221, RowCount:0, ArgLen:2, start time: 2024-06-18 11:58:41.567 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:41.581 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:225, Type:drop view, State:synced, SchemaState:queueing, SchemaID:217, TableID:221, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:41.567 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:41.583 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=225]
   > [2024/06/18 11:58:41.583 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/18 11:58:41.588 +00:00] [INFO] [session.go:2203] ["Try to create a new txn inside a transaction auto commit"] [conn=53] [schemaVersion=205] [txnStartTS=450550017971978240] [txnScope=global]
   > [2024/06/18 11:58:41.590 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:227, Type:create view, State:none, SchemaState:queueing, SchemaID:217, TableID:226, RowCount:0, ArgLen:3, start time: 2024-06-18 11:58:41.589 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 11:58:41.590 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:227, Type:create view, State:none, SchemaState:queueing, SchemaID:217, TableID:226, RowCount:0, ArgLen:3, start time: 2024-06-18 11:58:41.589 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="/*!50001 CREATE ALGORITHM=UNDEFINED */\n/*!50013 DEFINER=`root`@`127.0.0.1` SQL SECURITY DEFINER */\n/*!50001 VIEW `t_cpsvpb` (`c0`, `c2`, `c3`, `c4`, `c5`, `c6`, `c7`, `c8`, `c9`, `c10`, `c11`, `c12`, `c13`, `c14`) AS SELECT DISTINCT `subq_0`.`c1` AS `c0`,`subq_0`.`c2` AS `c2`,8 AS `c3`,CASE WHEN (`subq_0`.`c3` NOT IN (SELECT `ref_2`.`c_4vix1d` AS `c0` FROM `testdb`.`t_037irb` AS `ref_2` WHERE `ref_2`.`c_2ykt0d`<=`ref_2`.`c_nrh3o`)) AND (`subq_0`.`c3`<=(SELECT (SELECT `c_hhjlmc` AS `c_hhjlmc` FROM `testdb`.`t_x7zqmd` ORDER BY `c_hhjlmc` LIMIT 4,1) AS `c0` FROM `testdb`.`t_037irb` AS `ref_3` WHERE `subq_0`.`c1`!=`ref_3`.`c_2ykt0d`)) THEN `subq_0`.`c3` ELSE `subq_0`.`c3` END AS `c4`,CASE WHEN `subq_0`.`c1`>=(SELECT MAX(`c_8weeq`) AS `max(c_8weeq)` FROM `testdb`.`t_x7zqmd`) THEN `subq_0`.`c2` ELSE `subq_0`.`c2` END AS `c5`,`subq_0`.`c1` AS `c6`,`subq_0`.`c2` AS `c7`,`subq_0`.`c3` AS `c8`,`subq_0`.`c3` AS `c9`,`subq_0`.`c2` AS `c10`,`subq_0`.`c4` AS `c11`,COUNT(CAST(`subq_0`.`c2` AS DOUBLE)) OVER (PARTITION BY `subq_0`.`c4` ORDER BY `subq_0`.`c1`) AS `c12`,`subq_0`.`c3` AS `c13`,CAST(COALESCE(`subq_0`.`c3`, _UTF8MB4'9sx3k') AS CHAR) AS `c14` FROM (SELECT COUNT(CAST(`ref_1`.`c_jyc_cd` AS DOUBLE)) AS `c0`,AVG(CAST(`ref_1`.`c_3b1zld` AS SIGNED)) AS `c1`,MIN(CAST(`ref_1`.`c_jyc_cd` AS DOUBLE)) AS `c2`,`ref_0`.`c_glkxdb` AS `c3`,COUNT(CAST(`ref_1`.`c_13sfid` AS DOUBLE)) AS `c4` FROM `testdb`.`t_037irb` AS `ref_0` JOIN `testdb`.`t_x7zqmd` AS `ref_1` WHERE `ref_0`.`c_nrh3o`>`ref_1`.`c_8weeq` GROUP BY `ref_0`.`c_glkxdb`) AS `subq_0` WHERE (SELECT `c_8weeq` AS `c_8weeq` FROM `testdb`.`t_x7zqmd` ORDER BY `c_8weeq` LIMIT 2,1) IS NOT NULL */;"]
   > [2024/06/18 11:58:41.591 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:227, Type:create view, State:none, SchemaState:queueing, SchemaID:217, TableID:226, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:41.589 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:41.595 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=205] [neededSchemaVersion=206] ["start time"=664.407µs] [phyTblIDs="[226]"] [actionTypes="[2097152]"]
   > [2024/06/18 11:58:41.596 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=206] ["take time"=2.277338ms] [job="ID:227, Type:create view, State:done, SchemaState:public, SchemaID:217, TableID:226, RowCount:0, ArgLen:3, start time: 2024-06-18 11:58:41.589 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:41.598 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:227, Type:create view, State:synced, SchemaState:public, SchemaID:217, TableID:226, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:41.589 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:41.599 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=227]
   > [2024/06/18 11:58:41.599 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/18 11:58:42.635 +00:00] [INFO] [set.go:127] ["set global var"] [conn=55] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/06/18 11:58:42.932 +00:00] [ERROR] [misc.go:94] ["panic in the recoverable goroutine"] [r="\"invalid memory address or nil pointer dereference\""] ["stack trace"="github.com/pingcap/tidb/util.WithRecovery.func1\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:96\nruntime.gopanic\n\t/usr/local/go/src/runtime/panic.go:965\nruntime.panicmem\n\t/usr/local/go/src/runtime/panic.go:212\nruntime.sigpanic\n\t/usr/local/go/src/runtime/signal_unix.go:734\ngithub.com/pingcap/tidb/util/chunk.(*Chunk).NumRows\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/chunk/chunk.go:349\ngithub.com/pingcap/tidb/executor.(*vecGroupChecker).splitIntoGroups\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/aggregate.go:1456\ngithub.com/pingcap/tidb/executor.(*PipelinedWindowExec).getRowsInPartition\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/pipelined_window.go:188\ngithub.com/pingcap/tidb/executor.(*PipelinedWindowExec).Next\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/pipelined_window.go:124\ngithub.com/pingcap/tidb/executor.Next\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/executor.go:285\ngithub.com/pingcap/tidb/executor.(*ProjectionExec).unParallelExecute\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:193\ngithub.com/pingcap/tidb/executor.(*ProjectionExec).Next\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:179\ngithub.com/pingcap/tidb/executor.Next\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/executor.go:285\ngithub.com/pingcap/tidb/executor.(*CTEExec).computeSeedPart\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/cte.go:225\ngithub.com/pingcap/tidb/executor.(*CTEExec).Next\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/cte.go:160\ngithub.com/pingcap/tidb/executor.Next\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/executor.go:285\ngithub.com/pingcap/tidb/executor.(*SelectionExec).Next\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/executor.go:1301\ngithub.com/pingcap/tidb/executor.Next\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/executor.go:285\ngithub.com/pingcap/tidb/executor.(*HashJoinExec).fetchBuildSideRows\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:268\ngithub.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable.func2\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:702\ngithub.com/pingcap/tidb/util.WithRecovery\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99"]
   > runtime: goroutine stack exceeds 1000000000-byte limit
   > runtime: sp=0xc037b00398 stack=[0xc037b00000, 0xc057b00000]
   > fatal error: stack overflow
   > runtime stack:
   > runtime.throw(0x3b1a561, 0xe)
   > 	/usr/local/go/src/runtime/panic.go:1117 +0x72
   > runtime.newstack()
   > 	/usr/local/go/src/runtime/stack.go:1069 +0x7ed
   > runtime.morestack()
   > 	/usr/local/go/src/runtime/asm_amd64.s:458 +0x8f
   > goroutine 5088 [running]:
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016bcde00, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:182 +0x16f fp=0xc037b003a8 sp=0xc037b003a0 pc=0x1ee3a8f
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016bcdda0, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b003f0 sp=0xc037b003a8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016ea0900, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b00438 sp=0xc037b003f0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016d0cd80, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b00480 sp=0xc037b00438 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc016e84110, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b004c8 sp=0xc037b00480 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc0168d2b40, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b00510 sp=0xc037b004c8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc0165c82e0, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b00558 sp=0xc037b00510 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc015fce260, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b005a0 sp=0xc037b00558 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc016c125a0, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b005e8 sp=0xc037b005a0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016d86ae0, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b00630 sp=0xc037b005e8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc016c12430, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b00678 sp=0xc037b00630 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0168ecf60, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b006c0 sp=0xc037b00678 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016bcde00, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b00708 sp=0xc037b006c0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016bcdda0, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b00750 sp=0xc037b00708 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016ea0900, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b00798 sp=0xc037b00750 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016d0cd80, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b007e0 sp=0xc037b00798 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc016e84110, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b00828 sp=0xc037b007e0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc0168d2b40, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b00870 sp=0xc037b00828 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc0165c82e0, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b008b8 sp=0xc037b00870 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc015fce260, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b00900 sp=0xc037b008b8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc016c125a0, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b00948 sp=0xc037b00900 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016d86ae0, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b00990 sp=0xc037b00948 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc016c12430, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b009d8 sp=0xc037b00990 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0168ecf60, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b00a20 sp=0xc037b009d8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016bcde00, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b00a68 sp=0xc037b00a20 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016bcdda0, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b00ab0 sp=0xc037b00a68 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016ea0900, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b00af8 sp=0xc037b00ab0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016d0cd80, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b00b40 sp=0xc037b00af8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc016e84110, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b00b88 sp=0xc037b00b40 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc0168d2b40, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b00bd0 sp=0xc037b00b88 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc0165c82e0, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b00c18 sp=0xc037b00bd0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc015fce260, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b00c60 sp=0xc037b00c18 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc016c125a0, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b00ca8 sp=0xc037b00c60 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016d86ae0, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b00cf0 sp=0xc037b00ca8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc016c12430, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b00d38 sp=0xc037b00cf0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0168ecf60, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b00d80 sp=0xc037b00d38 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016bcde00, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b00dc8 sp=0xc037b00d80 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016bcdda0, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b00e10 sp=0xc037b00dc8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016ea0900, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b00e58 sp=0xc037b00e10 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016d0cd80, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b00ea0 sp=0xc037b00e58 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc016e84110, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b00ee8 sp=0xc037b00ea0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc0168d2b40, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b00f30 sp=0xc037b00ee8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc0165c82e0, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b00f78 sp=0xc037b00f30 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc015fce260, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b00fc0 sp=0xc037b00f78 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc016c125a0, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01008 sp=0xc037b00fc0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016d86ae0, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01050 sp=0xc037b01008 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc016c12430, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01098 sp=0xc037b01050 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0168ecf60, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b010e0 sp=0xc037b01098 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016bcde00, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01128 sp=0xc037b010e0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016bcdda0, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01170 sp=0xc037b01128 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016ea0900, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b011b8 sp=0xc037b01170 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016d0cd80, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01200 sp=0xc037b011b8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc016e84110, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01248 sp=0xc037b01200 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc0168d2b40, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01290 sp=0xc037b01248 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc0165c82e0, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b012d8 sp=0xc037b01290 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc015fce260, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01320 sp=0xc037b012d8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc016c125a0, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01368 sp=0xc037b01320 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016d86ae0, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b013b0 sp=0xc037b01368 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc016c12430, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b013f8 sp=0xc037b013b0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0168ecf60, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01440 sp=0xc037b013f8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016bcde00, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01488 sp=0xc037b01440 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016bcdda0, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b014d0 sp=0xc037b01488 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016ea0900, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01518 sp=0xc037b014d0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016d0cd80, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01560 sp=0xc037b01518 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc016e84110, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b015a8 sp=0xc037b01560 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc0168d2b40, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b015f0 sp=0xc037b015a8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc0165c82e0, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01638 sp=0xc037b015f0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc015fce260, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01680 sp=0xc037b01638 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc016c125a0, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b016c8 sp=0xc037b01680 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016d86ae0, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01710 sp=0xc037b016c8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc016c12430, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01758 sp=0xc037b01710 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0168ecf60, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b017a0 sp=0xc037b01758 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016bcde00, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b017e8 sp=0xc037b017a0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016bcdda0, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01830 sp=0xc037b017e8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016ea0900, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01878 sp=0xc037b01830 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016d0cd80, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b018c0 sp=0xc037b01878 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc016e84110, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01908 sp=0xc037b018c0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc0168d2b40, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01950 sp=0xc037b01908 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc0165c82e0, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01998 sp=0xc037b01950 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc015fce260, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b019e0 sp=0xc037b01998 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc016c125a0, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01a28 sp=0xc037b019e0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016d86ae0, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01a70 sp=0xc037b01a28 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc016c12430, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01ab8 sp=0xc037b01a70 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0168ecf60, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01b00 sp=0xc037b01ab8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016bcde00, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01b48 sp=0xc037b01b00 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016bcdda0, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01b90 sp=0xc037b01b48 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016ea0900, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01bd8 sp=0xc037b01b90 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016d0cd80, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01c20 sp=0xc037b01bd8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc016e84110, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01c68 sp=0xc037b01c20 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc0168d2b40, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01cb0 sp=0xc037b01c68 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc0165c82e0, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01cf8 sp=0xc037b01cb0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc015fce260, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01d40 sp=0xc037b01cf8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc016c125a0, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01d88 sp=0xc037b01d40 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016d86ae0, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01dd0 sp=0xc037b01d88 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc016c12430, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01e18 sp=0xc037b01dd0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0168ecf60, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01e60 sp=0xc037b01e18 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016bcde00, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01ea8 sp=0xc037b01e60 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016bcdda0, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01ef0 sp=0xc037b01ea8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016ea0900, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01f38 sp=0xc037b01ef0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc016d0cd80, 0x40385b8, 0xc016bcde00, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc037b01f80 sp=0xc037b01f38 pc=0x1ee3a1c
   > ...additional frames elided...
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:699 +0x198
   > goroutine 1 [chan receive]:
   > github.com/pingcap/tidb/server.(*Server).Run(0xc01134cc30, 0xc01136d7d0, 0xc0111027e0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/server.go:338 +0x1c5
   > main.main()
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/tidb-server/main.go:200 +0x33d
   > goroutine 40 [select]:
   > go.opencensus.io/stats/view.(*worker).start(0xc0002e5980)
   > 	/nfs/cache/mod/go.opencensus.io@v0.22.5/stats/view/worker.go:276 +0xcd
   > created by go.opencensus.io/stats/view.init.0
   > 	/nfs/cache/mod/go.opencensus.io@v0.22.5/stats/view/worker.go:34 +0x68
   > goroutine 133 [chan receive]:
   > go.etcd.io/etcd/pkg/logutil.(*MergeLogger).outputLoop(0xc000d2c5a0)
   > 	/nfs/cache/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20200824191128-ae9734ed278b/pkg/logutil/merge_logger.go:173 +0x3ac
   > created by go.etcd.io/etcd/pkg/logutil.NewMergeLogger
   > 	/nfs/cache/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20200824191128-ae9734ed278b/pkg/logutil/merge_logger.go:91 +0x85
   > goroutine 145 [chan receive]:
   > go.etcd.io/etcd/pkg/logutil.(*MergeLogger).outputLoop(0xc000d2c858)
   > 	/nfs/cache/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20200824191128-ae9734ed278b/pkg/logutil/merge_logger.go:173 +0x3ac
   > created by go.etcd.io/etcd/pkg/logutil.NewMergeLogger
   > 	/nfs/cache/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20200824191128-ae9734ed278b/pkg/logutil/merge_logger.go:91 +0x85
   > goroutine 212 [chan receive]:
   > go.etcd.io/etcd/pkg/logutil.(*MergeLogger).outputLoop(0xc000d2c990)
   > 	/nfs/cache/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20200824191128-ae9734ed278b/pkg/logutil/merge_logger.go:173 +0x3ac
   > created by go.etcd.io/etcd/pkg/logutil.NewMergeLogger
   > 	/nfs/cache/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20200824191128-ae9734ed278b/pkg/logutil/merge_logger.go:91 +0x85
   > goroutine 660 [chan receive]:
   > github.com/pingcap/tidb/util/signal.SetupSignalHandler.func1(0xc011378780)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:36 +0x72
   > created by github.com/pingcap/tidb/util/signal.SetupSignalHandler
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:33 +0xb9
   > goroutine 479 [chan receive]:
   > github.com/pingcap/tidb/util/profile.HeapProfileForGlobalMemTracker(0xdf8475800)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/profile/trackerRecorder.go:32 +0xbf
   > created by main.setHeapProfileTracker
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/tidb-server/main.go:266 +0x8d
   > goroutine 480 [chan receive]:
   > github.com/pingcap/tidb/util/systimemon.StartMonitor(0x3c23558, 0x3c228d0, 0xc00004edc0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/systimemon/systime_mon.go:31 +0x148
   > created by main.setupMetrics
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/tidb-server/main.go:652 +0x105
   > goroutine 481 [select]:
   > github.com/pingcap/badger.(*DB).updateSize(0xc000b80900, 0xc000b3b6e0)
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/db.go:1032 +0x108
   > created by github.com/pingcap/badger.Open
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/db.go:327 +0xe14
   > goroutine 482 [select]:
   > github.com/pingcap/badger/epoch.(*ResourceManager).collectLoop(0xc000b3f9e0, 0xc000b3b6f8)
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/epoch/manager.go:101 +0xdc
   > created by github.com/pingcap/badger/epoch.NewResourceManager
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/epoch/manager.go:79 +0xa7
   > goroutine 483 [select]:
   > github.com/pingcap/badger.Open.func4(0xc000b7c1d0)
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/db.go:341 +0x17c
   > created by github.com/pingcap/badger.Open
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/db.go:338 +0x10a8
   > goroutine 53 [select]:
   > github.com/pingcap/badger.(*blobGCHandler).run(0xc0006bc040, 0xc0006be018)
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/blob.go:468 +0xd4
   > created by github.com/pingcap/badger.(*blobManager).Open
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/blob.go:292 +0x618
   > goroutine 54 [select]:
   > github.com/pingcap/badger.(*levelsController).runWorker(0xc0005f22a0, 0xc0006be030, 0x0)
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/levels.go:212 +0x185
   > created by github.com/pingcap/badger.(*levelsController).startCompact
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/levels.go:180 +0x93
   > goroutine 55 [select]:
   > github.com/pingcap/badger.(*levelsController).runWorker(0xc0005f22a0, 0xc0006be030, 0x0)
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/levels.go:212 +0x185
   > created by github.com/pingcap/badger.(*levelsController).startCompact
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/levels.go:180 +0x93
   > goroutine 56 [select]:
   > github.com/pingcap/badger.(*levelsController).runWorker(0xc0005f22a0, 0xc0006be030, 0x1)
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/levels.go:212 +0x185
   > created by github.com/pingcap/badger.(*levelsController).startCompact
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/levels.go:180 +0x93
   > goroutine 57 [chan receive]:
   > github.com/pingcap/badger.(*DB).runFlushMemTable(0xc000b80900, 0xc000b3bc68, 0x0, 0x0)
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/db.go:913 +0x190
   > created by github.com/pingcap/badger.Open
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/db.go:360 +0x17b0
   > goroutine 312 [select]:
   > github.com/pingcap/badger.(*writeWorker).runWriteVLog(0xc000124160, 0xc0005a0030)
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/writer.go:94 +0x1dc
   > created by github.com/pingcap/badger.startWriteWorker
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/writer.go:64 +0x190
   > goroutine 313 [chan receive, locked to thread]:
   > github.com/pingcap/badger.(*writeWorker).runWriteLSM(0xc000124160, 0xc0005a0030)
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/writer.go:141 +0x195
   > created by github.com/pingcap/badger.startWriteWorker
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/writer.go:65 +0x1bc
   > goroutine 314 [chan receive]:
   > github.com/pingcap/badger.(*writeWorker).runMergeLSM(0xc000124160, 0xc0005a0030)
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/writer.go:154 +0xad
   > created by github.com/pingcap/badger.startWriteWorker
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/writer.go:66 +0x1e8
   > goroutine 315 [select]:
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.writeDBWorker.run(0xc0006b4120, 0xc0002ea580)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:95 +0x205
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*dbWriter).Open
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:198 +0x8f
   > goroutine 316 [select]:
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.writeLockWorker.run(0xc0006b4300, 0xc0002ea580)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:147 +0x3e5
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*dbWriter).Open
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:205 +0xdc
   > goroutine 317 [select]:
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*MVCCStore).runUpdateSafePointLoop(0xc0003b8680)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:1549 +0x28a
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.NewMVCCStore
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:84 +0x269
   > goroutine 318 [select]:
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*MVCCStore).StartDeadlockDetection.func1(0xc0003b8680)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:1285 +0x8a
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*MVCCStore).StartDeadlockDetection
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:1283 +0x78
   > goroutine 319 [select]:
   > github.com/tikv/client-go/v2/oracle/oracles.(*pdOracle).updateTS(0xc0005bb3b0, 0x4030f20, 0xc000056058, 0x77359400)
   > 	/nfs/cache/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20210820060448-daddf73a0706/oracle/oracles/pd.go:227 +0x131
   > created by github.com/tikv/client-go/v2/oracle/oracles.NewPdOracle
   > 	/nfs/cache/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20210820060448-daddf73a0706/oracle/oracles/pd.go:75 +0xd3
   > goroutine 320 [select]:
   > github.com/tikv/client-go/v2/internal/locate.(*RegionCache).asyncCheckAndResolveLoop(0xc0003b8780, 0xdf8475800)
   > 	/nfs/cache/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20210820060448-daddf73a0706/internal/locate/region_cache.go:395 +0xdc
   > created by github.com/tikv/client-go/v2/internal/locate.NewRegionCache
   > 	/nfs/cache/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20210820060448-daddf73a0706/internal/locate/region_cache.go:366 +0x259
   > goroutine 321 [select]:
   > github.com/tikv/client-go/v2/tikv.(*KVStore).runSafePointChecker(0xc000abeb40)
   > 	/nfs/cache/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20210820060448-daddf73a0706/tikv/kv.go:262 +0x136
   > created by github.com/tikv/client-go/v2/tikv.NewKVStore
   > 	/nfs/cache/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20210820060448-daddf73a0706/tikv/kv.go:185 +0x407
   > goroutine 498 [select]:
   > github.com/tikv/client-go/v2/tikv.(*KVStore).safeTSUpdater(0xc000abeb40)
   > 	/nfs/cache/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20210820060448-daddf73a0706/tikv/kv.go:540 +0x194
   > created by github.com/tikv/client-go/v2/tikv.NewKVStore
   > 	/nfs/cache/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20210820060448-daddf73a0706/tikv/kv.go:186 +0x429
   > goroutine 499 [select]:
   > github.com/dgraph-io/ristretto.(*defaultPolicy).processItems(0xc0006b1980)
   > 	/nfs/cache/mod/github.com/dgraph-io/ristretto@v0.0.1/policy.go:96 +0xa5
   > created by github.com/dgraph-io/ristretto.newDefaultPolicy
   > 	/nfs/cache/mod/github.com/dgraph-io/ristretto@v0.0.1/policy.go:80 +0x129
   > goroutine 500 [select]:
   > github.com/dgraph-io/ristretto.(*Cache).processItems(0xc0006b46c0)
   > 	/nfs/cache/mod/github.com/dgraph-io/ristretto@v0.0.1/cache.go:257 +0x9d
   > created by github.com/dgraph-io/ristretto.NewCache
   > 	/nfs/cache/mod/github.com/dgraph-io/ristretto@v0.0.1/cache.go:155 +0x205
   > goroutine 665 [chan receive]:
   > github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).startAnalyzeProfileWorker(0xc0009876e0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:141 +0xd4
   > created by github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).Run
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:93 +0xd9
   > goroutine 620 [select]:
   > github.com/pingcap/tidb/ddl.(*ddl).limitDDLJobs(0xc010268690)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/ddl/ddl_worker.go:265 +0x2d9
   > created by github.com/pingcap/tidb/ddl.(*ddl).Start
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/ddl/ddl.go:346 +0x2d5
   > goroutine 754 [select]:
   > github.com/pingcap/tidb/domain.(*Domain).loadSchemaInLoop(0xc010227600, 0x4030ee8, 0xc01020bc00, 0xa7a358200)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:513 +0x218
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:768 +0x734
   > goroutine 666 [IO wait]:
   > internal/poll.runtime_pollWait(0x7f5d49d7df08, 0x72, 0x0)
   > 	/usr/local/go/src/runtime/netpoll.go:222 +0x55
   > internal/poll.(*pollDesc).wait(0xc011143298, 0x72, 0x0, 0x0, 0x3b05d89)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:87 +0x45
   > internal/poll.(*pollDesc).waitRead(...)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:92
   > internal/poll.(*FD).Accept(0xc011143280, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
   > 	/usr/local/go/src/internal/poll/fd_unix.go:401 +0x212
   > net.(*netFD).accept(0xc011143280, 0xc, 0x7f5d708395b8, 0x10)
   > 	/usr/local/go/src/net/fd_unix.go:172 +0x45
   > net.(*TCPListener).accept(0xc010551a10, 0x11ed178, 0xc, 0x37efe60)
   > 	/usr/local/go/src/net/tcpsock_posix.go:139 +0x32
   > net.(*TCPListener).Accept(0xc010551a10, 0xc011466ef0, 0x20, 0x7f5d708395b8, 0x20)
   > 	/usr/local/go/src/net/tcpsock.go:261 +0x65
   > github.com/soheilhy/cmux.(*cMux).Serve(0xc011436fa0, 0x0, 0x0)
   > 	/nfs/cache/mod/github.com/soheilhy/cmux@v0.1.4/cmux.go:162 +0x96
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer(0xc01134cc30, 0xc0105cfcc0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/http_status.go:370 +0x49f
   > github.com/pingcap/tidb/server.(*Server).startHTTPServer(0xc01134cc30)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/http_status.go:346 +0x12a7
   > created by github.com/pingcap/tidb/server.(*Server).startStatusHTTP
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/http_status.go:59 +0x3f
   > goroutine 661 [chan receive]:
   > github.com/pingcap/tidb/util/signal.SetupSignalHandler.func2(0xc010b73440, 0xc01136d7d0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:52 +0x52
   > created by github.com/pingcap/tidb/util/signal.SetupSignalHandler
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:51 +0x194
   > goroutine 756 [select]:
   > github.com/pingcap/tidb/domain.(*Domain).infoSyncerKeeper(0xc010227600)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:455 +0x138
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:774 +0x65b
   > goroutine 755 [select]:
   > github.com/pingcap/tidb/domain.(*Domain).topNSlowQueryLoop(0xc010227600)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:423 +0x1e5
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:771 +0x61c
   > goroutine 672 [chan receive]:
   > github.com/soheilhy/cmux.muxListener.Accept(...)
   > 	/nfs/cache/mod/github.com/soheilhy/cmux@v0.1.4/cmux.go:229
   > net/http.(*Server).Serve(0xc00f9c7b20, 0x4023c40, 0xc0105ded08, 0x0, 0x0)
   > 	/usr/local/go/src/net/http/server.go:2981 +0x285
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer.func2()
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/http_status.go:366 +0x58
   > github.com/pingcap/tidb/util.WithRecovery(0xc011458620, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99 +0x4f
   > created by github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/http_status.go:365 +0x488
   > goroutine 667 [IO wait]:
   > internal/poll.runtime_pollWait(0x7f5d49d7dff0, 0x72, 0x0)
   > 	/usr/local/go/src/runtime/netpoll.go:222 +0x55
   > internal/poll.(*pollDesc).wait(0xc011143218, 0x72, 0x0, 0x0, 0x3b05d89)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:87 +0x45
   > internal/poll.(*pollDesc).waitRead(...)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:92
   > internal/poll.(*FD).Accept(0xc011143200, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
   > 	/usr/local/go/src/internal/poll/fd_unix.go:401 +0x212
   > net.(*netFD).accept(0xc011143200, 0x37bb380, 0x1, 0xc0142e0c78)
   > 	/usr/local/go/src/net/fd_unix.go:172 +0x45
   > net.(*TCPListener).accept(0xc0105519f8, 0xc010a9dd70, 0xc010a9dd78, 0x10)
   > 	/usr/local/go/src/net/tcpsock_posix.go:139 +0x32
   > net.(*TCPListener).Accept(0xc0105519f8, 0x3c1ef90, 0xc01134cc30, 0xc015aeb8c0, 0x0)
   > 	/usr/local/go/src/net/tcpsock.go:261 +0x65
   > github.com/pingcap/tidb/server.(*Server).startNetworkListener(0xc01134cc30, 0x4022c80, 0xc0105519f8, 0xc010b73500, 0xc010b53e00)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/server.go:347 +0x6a
   > created by github.com/pingcap/tidb/server.(*Server).Run
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/server.go:332 +0x11b
   > goroutine 622 [select]:
   > github.com/pingcap/tidb/ddl.(*worker).start(0xc01021c6e0, 0xc01026a540)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/ddl/ddl_worker.go:177 +0x315
   > created by github.com/pingcap/tidb/ddl.(*ddl).Start
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/ddl/ddl.go:364 +0x6a5
   > goroutine 623 [select]:
   > github.com/pingcap/tidb/ddl.(*worker).start(0xc01021c790, 0xc01026a540)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/ddl/ddl_worker.go:177 +0x315
   > created by github.com/pingcap/tidb/ddl.(*ddl).Start
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/ddl/ddl.go:364 +0x6a5
   > goroutine 671 [chan receive]:
   > github.com/soheilhy/cmux.muxListener.Accept(...)
   > 	/nfs/cache/mod/github.com/soheilhy/cmux@v0.1.4/cmux.go:229
   > google.golang.org/grpc.(*Server).Serve(0xc0104f6ea0, 0x4023c40, 0xc0105ded20, 0x0, 0x0)
   > 	/nfs/cache/mod/google.golang.org/grpc@v1.29.1/server.go:621 +0x27f
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer.func1()
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/http_status.go:361 +0x58
   > github.com/pingcap/tidb/util.WithRecovery(0xc011458600, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99 +0x4f
   > created by github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/http_status.go:360 +0x405
   > goroutine 664 [sleep]:
   > time.Sleep(0x3b9aca00)
   > 	/usr/local/go/src/runtime/time.go:193 +0xd2
   > github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).startCPUProfileWorker(0xc0009876e0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:114 +0xb4
   > created by github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).Run
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:92 +0xb7
   > goroutine 659 [syscall]:
   > os/signal.signal_recv(0x1252646)
   > 	/usr/local/go/src/runtime/sigqueue.go:168 +0xa5
   > os/signal.loop()
   > 	/usr/local/go/src/os/signal/signal_unix.go:23 +0x25
   > created by os/signal.Notify.func1.1
   > 	/usr/local/go/src/os/signal/signal.go:151 +0x45
   > goroutine 621 [select]:
   > github.com/pingcap/tidb/ddl.(*delRange).startEmulator(0xc01026e320)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/ddl/delete_range.go:143 +0x128
   > created by github.com/pingcap/tidb/ddl.(*delRange).start
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/ddl/delete_range.go:125 +0x6a
   > goroutine 757 [select]:
   > github.com/pingcap/tidb/domain.(*Domain).topologySyncerKeeper(0xc010227600)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:481 +0x193
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:778 +0x6c5
   > goroutine 783 [select]:
   > github.com/pingcap/tidb/domain.(*Domain).TelemetryReportLoop.func1(0xc010227600, 0x40773d8, 0xc01052fe00)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:1084 +0x12f
   > created by github.com/pingcap/tidb/domain.(*Domain).TelemetryReportLoop
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:1076 +0x2b8
   > goroutine 712 [select]:
   > github.com/pingcap/tidb/domain.(*Domain).globalBindHandleWorkerLoop.func1(0xc010227600, 0x404ecf8, 0xc01050bfa0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:1014 +0x157
   > created by github.com/pingcap/tidb/domain.(*Domain).globalBindHandleWorkerLoop
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:1001 +0x73
   > goroutine 713 [select]:
   > github.com/pingcap/tidb/domain.(*Domain).handleEvolvePlanTasksLoop.func1(0xc010227600, 0x404ecf8, 0xc01050bfa0, 0x40773d8, 0xc0005d9400)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:1050 +0xde
   > created by github.com/pingcap/tidb/domain.(*Domain).handleEvolvePlanTasksLoop
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:1043 +0x8f
   > goroutine 820 [select]:
   > github.com/pingcap/tidb/domain.(*Domain).LoadPrivilegeLoop.func1(0xc010227600, 0xc0007260c0, 0x45d964b800, 0x40773d8, 0xc01052ec00)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:883 +0x125
   > created by github.com/pingcap/tidb/domain.(*Domain).LoadPrivilegeLoop
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:874 +0x1f0
   > goroutine 778 [select]:
   > github.com/pingcap/tidb/domain.(*Domain).LoadSysVarCacheLoop.func1(0xc010227600, 0xc0006af8d0, 0x6fc23ac00, 0x40773d8, 0xc011282000)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:932 +0x125
   > created by github.com/pingcap/tidb/domain.(*Domain).LoadSysVarCacheLoop
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:923 +0xf6
   > goroutine 662 [select]:
   > github.com/pingcap/tidb/util/topsql/reporter.(*RemoteTopSQLReporter).collectWorker(0xc010b70d90)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:325 +0x1bb
   > created by github.com/pingcap/tidb/util/topsql/reporter.NewRemoteTopSQLReporter
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:158 +0x1a7
   > goroutine 663 [select]:
   > github.com/pingcap/tidb/util/topsql/reporter.(*RemoteTopSQLReporter).reportWorker(0xc010b70d90)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:497 +0x211
   > created by github.com/pingcap/tidb/util/topsql/reporter.NewRemoteTopSQLReporter
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:159 +0x1c9
   > goroutine 784 [select]:
   > github.com/pingcap/tidb/domain.(*Domain).TelemetryRotateSubWindowLoop.func1(0xc010227600)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:1113 +0xd8
   > created by github.com/pingcap/tidb/domain.(*Domain).TelemetryRotateSubWindowLoop
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:1106 +0x7f
   > goroutine 785 [select]:
   > github.com/pingcap/tidb/domain.(*Domain).loadStatsWorker(0xc010227600)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:1226 +0x3cc
   > created by github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:1169 +0x2fa
   > goroutine 834 [select]:
   > github.com/pingcap/tidb/domain.(*Domain).updateStatsWorker(0xc010227600, 0x40773d8, 0xc011366400, 0x404ecf8, 0xc0109e90a0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:1294 +0x288
   > created by github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:1181 +0x1d6
   > goroutine 835 [select]:
   > github.com/pingcap/tidb/domain.(*Domain).autoAnalyzeWorker(0xc010227600, 0x404ecf8, 0xc0109e90a0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:1347 +0x165
   > created by github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:1184 +0x245
   > goroutine 836 [select]:
   > github.com/pingcap/tidb/util/expensivequery.(*Handle).Run(0xc00ff2d350)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/expensivequery/expensivequery.go:60 +0x337
   > created by main.createServer
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/tidb-server/main.go:631 +0x1c7
   > goroutine 5086 [select]:
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc016af2c00, 0x4, 0x5d958d8, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:445 +0x33f
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:339 +0xc5
   > github.com/pingcap/tidb/util.WithRecovery(0xc016b52840, 0xc016a65fa0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99 +0x4f
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:337 +0x1ab
   > goroutine 5087 [semacquire]:
   > sync.runtime_Semacquire(0xc016af2dd4)
   > 	/usr/local/go/src/runtime/sema.go:56 +0x45
   > sync.(*WaitGroup).Wait(0xc016af2dd4)
   > 	/usr/local/go/src/sync/waitgroup.go:130 +0x65
   > github.com/pingcap/tidb/executor.(*HashJoinExec).waitJoinWorkersAndCloseResultChan(0xc016af2c00)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:399 +0x3d
   > github.com/pingcap/tidb/util.WithRecovery(0xc016a65fb0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99 +0x4f
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:342 +0x336
   > goroutine 5081 [select]:
   > github.com/pingcap/tidb/executor.(*HashJoinExec).wait4BuildSide(0xc016af2c00, 0xc016554690, 0x4035bb8, 0xc016ae8380)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:244 +0x88
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchProbeSideChunks(0xc016af2c00, 0x4030f90, 0xc016554690)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:223 +0x26f
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func1()
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:324 +0xa9
   > github.com/pingcap/tidb/util.WithRecovery(0xc0161f5d80, 0xc016a65f50)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99 +0x4f
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:322 +0xfd
   > goroutine 5208 [select]:
   > github.com/pingcap/tidb/executor.readProjectionInput(0xc016d87140, 0xc0165e2120, 0x3b1ee58)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:459 +0x86
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc0168e0940, 0x4030f90, 0xc016554690)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:427 +0x129
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:275 +0x78f
   > goroutine 5119 [chan receive]:
   > github.com/pingcap/tidb/executor.(*HashJoinExec).buildHashTableForList(0xc016af2e00, 0xc0168ec8a0, 0xc0161e8b40, 0xc016a65ed0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:758 +0x327
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable(0xc016af2e00, 0x4030f90, 0xc016554690)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:713 +0x1b3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Next.func1()
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:658 +0xa9
   > github.com/pingcap/tidb/util.WithRecovery(0xc0168dc720, 0xc0168d29d0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99 +0x4f
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).Next
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:656 +0x305
   > goroutine 4975 [chan receive]:
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Close(0xc016af2e00, 0x0, 0xc016aeec30)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:121 +0xd0
   > github.com/pingcap/tidb/executor.(*baseExecutor).Close(0xc016b2db00, 0xff, 0x4031a48)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/executor.go:180 +0x7e
   > github.com/pingcap/tidb/executor.(*ProjectionExec).Close(0xc016b2db00, 0x3fe17c0, 0xc0165aec18)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:328 +0x138
   > github.com/pingcap/tidb/executor.(*recordSet).Close(0xc0168c2aa0, 0x4030f90, 0xc016554690)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/adapter.go:169 +0x38
   > github.com/pingcap/tidb/session.(*execStmtResult).Close(0xc016c06930, 0xc016c06930, 0x4030f90)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/session/session.go:1833 +0x42
   > github.com/pingcap/tidb/server.(*tidbResultSet).Close(0xc0168c2af0, 0xc0165aec18, 0xc016a20fc8)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/driver_tidb.go:323 +0x4a
   > github.com/pingcap/parser/terror.Call(0xc016a21108)
   > 	/nfs/cache/mod/github.com/pingcap/parser@v0.0.0-20210831085004-b5390aa83f65/terror/terror.go:282 +0x3f
   > github.com/pingcap/tidb/server.(*clientConn).handleStmt(0xc015aeb8c0, 0x4030ee8, 0xc016554690, 0x404e488, 0xc016133860, 0x5d958d8, 0x0, 0x0, 0x1, 0x1, ...)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/conn.go:1846 +0x445
   > github.com/pingcap/tidb/server.(*clientConn).handleQuery(0xc015aeb8c0, 0x4030ee8, 0xc016512b00, 0xc015e409c1, 0x18c, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/conn.go:1690 +0x492
   > github.com/pingcap/tidb/server.(*clientConn).dispatch(0xc015aeb8c0, 0x4030ee8, 0xc016512b00, 0xc015e409c0, 0x18d, 0x18c, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/conn.go:1215 +0xafd
   > github.com/pingcap/tidb/server.(*clientConn).Run(0xc015aeb8c0, 0x4030f90, 0xc016522f30)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/conn.go:978 +0x296
   > github.com/pingcap/tidb/server.(*Server).onConn(0xc01134cc30, 0xc015aeb8c0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/server.go:501 +0xa53
   > created by github.com/pingcap/tidb/server.(*Server).startNetworkListener
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/server.go:404 +0x8fc
   > goroutine 5205 [select]:
   > github.com/pingcap/tidb/executor.readProjectionInput(0xc016d86de0, 0xc0165e2120, 0x3b1ee58)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:459 +0x86
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc0168e0880, 0x4030f90, 0xc016554690)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:427 +0x129
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:275 +0x78f
   > goroutine 5082 [select]:
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc016af2c00, 0x0, 0x5d958d8, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:445 +0x33f
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:339 +0xc5
   > github.com/pingcap/tidb/util.WithRecovery(0xc016b52740, 0xc016a65f60)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99 +0x4f
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:337 +0x1ab
   > goroutine 5206 [select]:
   > github.com/pingcap/tidb/executor.readProjectionInput(0xc016d86f00, 0xc0165e2120, 0x3b1ee58)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:459 +0x86
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc0168e08c0, 0x4030f90, 0xc016554690)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:427 +0x129
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:275 +0x78f
   > goroutine 5079 [chan receive]:
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Next(0xc016af2c00, 0x4030f90, 0xc016554690, 0xc016e380a0, 0x7f5d293fffff, 0x7f5d49c48758)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:668 +0x87
   > github.com/pingcap/tidb/executor.Next(0x4030f90, 0xc016554690, 0x40359f8, 0xc016af2c00, 0xc016e380a0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/executor.go:285 +0x2de
   > github.com/pingcap/tidb/executor.(*ProjectionExec).unParallelExecute(0xc016b2d500, 0x4030f90, 0xc016554690, 0xc016e38500, 0x0, 0x3532110acd00)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:193 +0xb2
   > github.com/pingcap/tidb/executor.(*ProjectionExec).Next(0xc016b2d500, 0x4030f90, 0xc016554690, 0xc016e38500, 0x38eb320, 0xc016e36bd0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:179 +0x73
   > github.com/pingcap/tidb/executor.Next(0x4030f90, 0xc016554690, 0x4035f78, 0xc016b2d500, 0xc016e38500, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/executor.go:285 +0x2de
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchBuildSideRows(0xc016af2e00, 0x4030f90, 0xc016554690, 0xc0168ec8a0, 0xc015d32d80)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:268 +0x194
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable.func2()
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:702 +0xcf
   > github.com/pingcap/tidb/util.WithRecovery(0xc0161e8b40, 0xc016a65ed0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99 +0x4f
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:699 +0x198
   > goroutine 5080 [chan receive]:
   > github.com/pingcap/tidb/executor.(*HashJoinExec).buildHashTableForList(0xc016af2c00, 0xc0168ecea0, 0xc010ffd5f0, 0xc016a65fd0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:758 +0x327
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable(0xc016af2c00, 0x4030f90, 0xc016554690)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:713 +0x1b3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Next.func1()
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:658 +0xa9
   > github.com/pingcap/tidb/util.WithRecovery(0xc0161f5d60, 0xc016a65ef0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99 +0x4f
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).Next
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:656 +0x305
   > goroutine 5204 [select]:
   > github.com/pingcap/tidb/executor.readProjectionInput(0xc016d86cc0, 0xc0165e2120, 0xc01638a400)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:459 +0x86
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc0168e0840, 0x4030f90, 0xc016554690)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:427 +0x129
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:275 +0x78f
   > goroutine 5207 [select]:
   > github.com/pingcap/tidb/executor.readProjectionInput(0xc016d87020, 0xc0165e2120, 0x3b1ee58)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:459 +0x86
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc0168e0900, 0x4030f90, 0xc016554690)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:427 +0x129
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:275 +0x78f
   > goroutine 5084 [select]:
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc016af2c00, 0x2, 0x5d958d8, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:445 +0x33f
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:339 +0xc5
   > github.com/pingcap/tidb/util.WithRecovery(0xc016b527c0, 0xc016a65f80)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99 +0x4f
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:337 +0x1ab
   > goroutine 5083 [select]:
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc016af2c00, 0x1, 0x5d958d8, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:445 +0x33f
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:339 +0xc5
   > github.com/pingcap/tidb/util.WithRecovery(0xc016b52780, 0xc016a65f70)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99 +0x4f
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:337 +0x1ab
   > goroutine 5085 [select]:
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc016af2c00, 0x3, 0x5d958d8, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:445 +0x33f
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:339 +0xc5
   > github.com/pingcap/tidb/util.WithRecovery(0xc016b52800, 0xc016a65f90)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99 +0x4f
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:337 +0x1ab
   > goroutine 5175 [select]:
   > github.com/pingcap/tidb/executor.readProjectionInput(0xc0168ed0e0, 0xc015d32e40, 0xc01638a400)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:459 +0x86
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc016b52900, 0x4030f90, 0xc016554690)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:427 +0x129
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:275 +0x78f
   > goroutine 5176 [select]:
   > github.com/pingcap/tidb/executor.readProjectionInput(0xc0168ed200, 0xc015d32e40, 0x3b1ee58)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:459 +0x86
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc016b52940, 0x4030f90, 0xc016554690)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:427 +0x129
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:275 +0x78f
   > goroutine 5177 [select]:
   > github.com/pingcap/tidb/executor.readProjectionInput(0xc0168ed320, 0xc015d32e40, 0x3b1ee58)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:459 +0x86
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc016b52980, 0x4030f90, 0xc016554690)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:427 +0x129
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:275 +0x78f
   > goroutine 5178 [select]:
   > github.com/pingcap/tidb/executor.readProjectionInput(0xc0168ed440, 0xc015d32e40, 0x3b1ee58)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:459 +0x86
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc016b529c0, 0x4030f90, 0xc016554690)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:427 +0x129
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:275 +0x78f
   > goroutine 5179 [select]:
   > github.com/pingcap/tidb/executor.readProjectionInput(0xc0168ed560, 0xc015d32e40, 0x3b1ee58)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:459 +0x86
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc016b52a00, 0x4030f90, 0xc016554690)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:427 +0x129
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:275 +0x78f
