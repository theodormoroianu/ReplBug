# Bug ID TIDB-30326-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/30326
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ


## Details
 * Database: tidb-v5.4.0
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
   > [2024/06/18 16:12:01.634 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=53] [user=root] [host=]
   > [2024/06/18 16:12:01.637 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=53] [schemaVersion=197] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/06/18 16:12:01.638 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:220, Type:drop schema, State:none, SchemaState:queueing, SchemaID:215, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:01.638 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 16:12:01.638 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:220, Type:drop schema, State:none, SchemaState:queueing, SchemaID:215, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:01.638 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/06/18 16:12:01.639 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:220, Type:drop schema, State:none, SchemaState:queueing, SchemaID:215, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:01.638 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:01.640 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=197] [neededSchemaVersion=198] ["start time"=85.766µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 16:12:01.642 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=198] ["take time"=2.247797ms] [job="ID:220, Type:drop schema, State:running, SchemaState:write only, SchemaID:215, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:01.638 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:01.642 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:220, Type:drop schema, State:running, SchemaState:write only, SchemaID:215, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:01.638 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:01.643 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=198] [neededSchemaVersion=199] ["start time"=81.156µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 16:12:01.645 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=199] ["take time"=2.322947ms] [job="ID:220, Type:drop schema, State:running, SchemaState:delete only, SchemaID:215, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:01.638 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:01.646 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:220, Type:drop schema, State:running, SchemaState:delete only, SchemaID:215, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:01.638 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:01.647 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=199] [neededSchemaVersion=200] ["start time"=106.02µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 16:12:01.649 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=200] ["take time"=2.285302ms] [job="ID:220, Type:drop schema, State:done, SchemaState:queueing, SchemaID:215, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:01.638 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:01.649 +00:00] [INFO] [delete_range.go:107] ["[ddl] add job into delete-range table"] [jobID=220] [jobType="drop schema"]
   > [2024/06/18 16:12:01.649 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:220, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:215, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:01.638 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:01.650 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=220]
   > [2024/06/18 16:12:01.650 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 16:12:01.651 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=53] [schemaVersion=200] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/06/18 16:12:01.652 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:222, Type:create schema, State:none, SchemaState:queueing, SchemaID:221, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 16:12:01.651 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 16:12:01.652 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:222, Type:create schema, State:none, SchemaState:queueing, SchemaID:221, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 16:12:01.651 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/18 16:12:01.652 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:222, Type:create schema, State:none, SchemaState:queueing, SchemaID:221, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:01.651 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:01.653 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=200] [neededSchemaVersion=201] ["start time"=101.55µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 16:12:01.655 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=201] ["take time"=2.186057ms] [job="ID:222, Type:create schema, State:done, SchemaState:public, SchemaID:221, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 16:12:01.651 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:01.655 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:222, Type:create schema, State:synced, SchemaState:public, SchemaID:221, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:01.651 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:01.656 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=222]
   > [2024/06/18 16:12:01.656 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 16:12:01.660 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=53] [schemaVersion=201] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_037irb`\n--\n\nDROP TABLE IF EXISTS `t_037irb`;"] [user=root@127.0.0.1]
   > [2024/06/18 16:12:01.661 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=53] [schemaVersion=201] [cur_db=testdb] [sql="CREATE TABLE `t_037irb` (\n  `c_nrh3o` int(11) DEFAULT NULL,\n  `c_nfauxb` text DEFAULT NULL,\n  `c_y5n4c` int(11) DEFAULT NULL,\n  `c_j9alg` double NOT NULL,\n  `c_4vix1d` text DEFAULT NULL,\n  `c_glkxdb` text DEFAULT NULL,\n  `c_2ykt0d` int(11) DEFAULT NULL,\n  `c_5fxv3c` double DEFAULT NULL,\n  PRIMARY KEY (`c_j9alg`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/06/18 16:12:01.662 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:224, Type:create table, State:none, SchemaState:queueing, SchemaID:221, TableID:223, RowCount:0, ArgLen:1, start time: 2024-06-18 16:12:01.662 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 16:12:01.662 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:224, Type:create table, State:none, SchemaState:queueing, SchemaID:221, TableID:223, RowCount:0, ArgLen:1, start time: 2024-06-18 16:12:01.662 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_037irb` (\n  `c_nrh3o` int(11) DEFAULT NULL,\n  `c_nfauxb` text DEFAULT NULL,\n  `c_y5n4c` int(11) DEFAULT NULL,\n  `c_j9alg` double NOT NULL,\n  `c_4vix1d` text DEFAULT NULL,\n  `c_glkxdb` text DEFAULT NULL,\n  `c_2ykt0d` int(11) DEFAULT NULL,\n  `c_5fxv3c` double DEFAULT NULL,\n  PRIMARY KEY (`c_j9alg`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/18 16:12:01.663 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:224, Type:create table, State:none, SchemaState:queueing, SchemaID:221, TableID:223, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:01.662 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:01.665 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=201] [neededSchemaVersion=202] ["start time"=473.809µs] [phyTblIDs="[223]"] [actionTypes="[8]"]
   > [2024/06/18 16:12:01.666 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=202] ["take time"=2.023116ms] [job="ID:224, Type:create table, State:done, SchemaState:public, SchemaID:221, TableID:223, RowCount:0, ArgLen:1, start time: 2024-06-18 16:12:01.662 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:01.667 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:224, Type:create table, State:synced, SchemaState:public, SchemaID:221, TableID:223, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:01.662 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:01.668 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=224]
   > [2024/06/18 16:12:01.668 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 16:12:01.668 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=102] ["first split key"=7480000000000000df]
   > [2024/06/18 16:12:01.668 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=102] ["first at"=7480000000000000df] ["first new region left"="{Id:102 StartKey:7480000000000000ffd900000000000000f8 EndKey:7480000000000000ffdf00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:103 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/18 16:12:01.668 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[102]"]
   > [2024/06/18 16:12:01.669 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=53] [schemaVersion=202] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_037irb` DISABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/06/18 16:12:01.669 +00:00] [WARN] [2pc.go:1596] ["schemaLeaseChecker is not set for this transaction"] [sessionID=53] [startTS=450554002582798338] [commitTS=450554002582798339]
   > [2024/06/18 16:12:01.671 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=53] [schemaVersion=202] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_037irb` ENABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/06/18 16:12:01.671 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=53] [schemaVersion=202] [cur_db=testdb] [sql="\n--\n-- Temporary view structure for view `t_cpsvpb`\n--\n\nDROP TABLE IF EXISTS `t_cpsvpb`;"] [user=root@127.0.0.1]
   > [2024/06/18 16:12:01.671 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=53] [schemaVersion=202] [cur_db=testdb] [sql="/*!50001 DROP VIEW IF EXISTS `t_cpsvpb`*/;"] [user=root@127.0.0.1]
   > [2024/06/18 16:12:01.673 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:226, Type:create view, State:none, SchemaState:queueing, SchemaID:221, TableID:225, RowCount:0, ArgLen:3, start time: 2024-06-18 16:12:01.673 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 16:12:01.673 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:226, Type:create view, State:none, SchemaState:queueing, SchemaID:221, TableID:225, RowCount:0, ArgLen:3, start time: 2024-06-18 16:12:01.673 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="/*!50001 CREATE VIEW `t_cpsvpb` AS SELECT \n 1 AS `c0`,\n 1 AS `c2`,\n 1 AS `c3`,\n 1 AS `c4`,\n 1 AS `c5`,\n 1 AS `c6`,\n 1 AS `c7`,\n 1 AS `c8`,\n 1 AS `c9`,\n 1 AS `c10`,\n 1 AS `c11`,\n 1 AS `c12`,\n 1 AS `c13`,\n 1 AS `c14`*/;"]
   > [2024/06/18 16:12:01.674 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:226, Type:create view, State:none, SchemaState:queueing, SchemaID:221, TableID:225, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:01.673 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:01.677 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=202] [neededSchemaVersion=203] ["start time"=541.905µs] [phyTblIDs="[225]"] [actionTypes="[2097152]"]
   > [2024/06/18 16:12:01.679 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=203] ["take time"=2.254432ms] [job="ID:226, Type:create view, State:done, SchemaState:public, SchemaID:221, TableID:225, RowCount:0, ArgLen:3, start time: 2024-06-18 16:12:01.673 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:01.680 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:226, Type:create view, State:synced, SchemaState:public, SchemaID:221, TableID:225, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:01.673 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:01.682 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=226]
   > [2024/06/18 16:12:01.682 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 16:12:01.682 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=53] [schemaVersion=203] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_x7zqmd`\n--\n\nDROP TABLE IF EXISTS `t_x7zqmd`;"] [user=root@127.0.0.1]
   > [2024/06/18 16:12:01.683 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=53] [schemaVersion=203] [cur_db=testdb] [sql="CREATE TABLE `t_x7zqmd` (\n  `c_8weeq` int(11) NOT NULL,\n  `c_13sfid` double DEFAULT NULL,\n  `c_hhjlmc` text DEFAULT NULL,\n  `c_3b1zld` int(11) DEFAULT NULL,\n  `c_6tu8wd` int(11) DEFAULT NULL,\n  `c_jyc_cd` double DEFAULT NULL,\n  PRIMARY KEY (`c_8weeq`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/06/18 16:12:01.684 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:228, Type:create table, State:none, SchemaState:queueing, SchemaID:221, TableID:227, RowCount:0, ArgLen:1, start time: 2024-06-18 16:12:01.684 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 16:12:01.685 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:228, Type:create table, State:none, SchemaState:queueing, SchemaID:221, TableID:227, RowCount:0, ArgLen:1, start time: 2024-06-18 16:12:01.684 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_x7zqmd` (\n  `c_8weeq` int(11) NOT NULL,\n  `c_13sfid` double DEFAULT NULL,\n  `c_hhjlmc` text DEFAULT NULL,\n  `c_3b1zld` int(11) DEFAULT NULL,\n  `c_6tu8wd` int(11) DEFAULT NULL,\n  `c_jyc_cd` double DEFAULT NULL,\n  PRIMARY KEY (`c_8weeq`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/18 16:12:01.685 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:228, Type:create table, State:none, SchemaState:queueing, SchemaID:221, TableID:227, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:01.684 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:01.687 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=203] [neededSchemaVersion=204] ["start time"=368.137µs] [phyTblIDs="[227]"] [actionTypes="[8]"]
   > [2024/06/18 16:12:01.688 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=204] ["take time"=2.023255ms] [job="ID:228, Type:create table, State:done, SchemaState:public, SchemaID:221, TableID:227, RowCount:0, ArgLen:1, start time: 2024-06-18 16:12:01.684 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:01.689 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:228, Type:create table, State:synced, SchemaState:public, SchemaID:221, TableID:227, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:01.684 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:01.690 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=228]
   > [2024/06/18 16:12:01.690 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 16:12:01.690 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=104] ["first split key"=7480000000000000e3]
   > [2024/06/18 16:12:01.691 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=104] ["first at"=7480000000000000e3] ["first new region left"="{Id:104 StartKey:7480000000000000ffdf00000000000000f8 EndKey:7480000000000000ffe300000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:105 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/18 16:12:01.691 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[104]"]
   > [2024/06/18 16:12:01.691 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=53] [schemaVersion=204] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_x7zqmd` DISABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/06/18 16:12:01.693 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=53] [schemaVersion=204] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_x7zqmd` ENABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/06/18 16:12:01.694 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=53] [schemaVersion=204] [cur_db=testdb] [sql="\n--\n-- Final view structure for view `t_cpsvpb`\n--\n\n/*!50001 DROP VIEW IF EXISTS `t_cpsvpb`*/;"] [user=root@127.0.0.1]
   > [2024/06/18 16:12:01.695 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:229, Type:drop view, State:none, SchemaState:queueing, SchemaID:221, TableID:225, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:01.694 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 16:12:01.695 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:229, Type:drop view, State:none, SchemaState:queueing, SchemaID:221, TableID:225, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:01.694 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="\n--\n-- Final view structure for view `t_cpsvpb`\n--\n\n/*!50001 DROP VIEW IF EXISTS `t_cpsvpb`*/;"]
   > [2024/06/18 16:12:01.695 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:229, Type:drop view, State:none, SchemaState:queueing, SchemaID:221, TableID:225, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:01.694 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:01.697 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=204] [neededSchemaVersion=205] ["start time"=98.268µs] [phyTblIDs="[225]"] [actionTypes="[16777216]"]
   > [2024/06/18 16:12:01.699 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=205] ["take time"=2.242768ms] [job="ID:229, Type:drop view, State:running, SchemaState:write only, SchemaID:221, TableID:225, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:01.694 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:01.699 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:229, Type:drop view, State:running, SchemaState:write only, SchemaID:221, TableID:225, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:01.694 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:01.700 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=205] [neededSchemaVersion=206] ["start time"=93.868µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 16:12:01.703 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=206] ["take time"=3.017248ms] [job="ID:229, Type:drop view, State:running, SchemaState:delete only, SchemaID:221, TableID:225, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:01.694 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:01.704 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:229, Type:drop view, State:running, SchemaState:delete only, SchemaID:221, TableID:225, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:01.694 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:01.705 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=206] [neededSchemaVersion=207] ["start time"=89.119µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 16:12:01.708 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=207] ["take time"=2.235505ms] [job="ID:229, Type:drop view, State:done, SchemaState:queueing, SchemaID:221, TableID:225, RowCount:0, ArgLen:3, start time: 2024-06-18 16:12:01.694 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:01.709 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:229, Type:drop view, State:synced, SchemaState:queueing, SchemaID:221, TableID:225, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:01.694 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:01.710 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=229]
   > [2024/06/18 16:12:01.710 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 16:12:01.715 +00:00] [INFO] [session.go:2108] ["Try to create a new txn inside a transaction auto commit"] [conn=53] [schemaVersion=207] [txnStartTS=450554002594070528] [txnScope=global]
   > [2024/06/18 16:12:01.717 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:231, Type:create view, State:none, SchemaState:queueing, SchemaID:221, TableID:230, RowCount:0, ArgLen:3, start time: 2024-06-18 16:12:01.716 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 16:12:01.717 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:231, Type:create view, State:none, SchemaState:queueing, SchemaID:221, TableID:230, RowCount:0, ArgLen:3, start time: 2024-06-18 16:12:01.716 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="/*!50001 CREATE ALGORITHM=UNDEFINED */\n/*!50013 DEFINER=`root`@`127.0.0.1` SQL SECURITY DEFINER */\n/*!50001 VIEW `t_cpsvpb` (`c0`, `c2`, `c3`, `c4`, `c5`, `c6`, `c7`, `c8`, `c9`, `c10`, `c11`, `c12`, `c13`, `c14`) AS SELECT DISTINCT `subq_0`.`c1` AS `c0`,`subq_0`.`c2` AS `c2`,8 AS `c3`,CASE WHEN (`subq_0`.`c3` NOT IN (SELECT `ref_2`.`c_4vix1d` AS `c0` FROM `testdb`.`t_037irb` AS `ref_2` WHERE `ref_2`.`c_2ykt0d`<=`ref_2`.`c_nrh3o`)) AND (`subq_0`.`c3`<=(SELECT (SELECT `c_hhjlmc` AS `c_hhjlmc` FROM `testdb`.`t_x7zqmd` ORDER BY `c_hhjlmc` LIMIT 4,1) AS `c0` FROM `testdb`.`t_037irb` AS `ref_3` WHERE `subq_0`.`c1`!=`ref_3`.`c_2ykt0d`)) THEN `subq_0`.`c3` ELSE `subq_0`.`c3` END AS `c4`,CASE WHEN `subq_0`.`c1`>=(SELECT MAX(`c_8weeq`) AS `max(c_8weeq)` FROM `testdb`.`t_x7zqmd`) THEN `subq_0`.`c2` ELSE `subq_0`.`c2` END AS `c5`,`subq_0`.`c1` AS `c6`,`subq_0`.`c2` AS `c7`,`subq_0`.`c3` AS `c8`,`subq_0`.`c3` AS `c9`,`subq_0`.`c2` AS `c10`,`subq_0`.`c4` AS `c11`,COUNT(CAST(`subq_0`.`c2` AS DOUBLE)) OVER (PARTITION BY `subq_0`.`c4` ORDER BY `subq_0`.`c1`) AS `c12`,`subq_0`.`c3` AS `c13`,CAST(COALESCE(`subq_0`.`c3`, _UTF8MB4'9sx3k') AS CHAR) AS `c14` FROM (SELECT COUNT(CAST(`ref_1`.`c_jyc_cd` AS DOUBLE)) AS `c0`,AVG(CAST(`ref_1`.`c_3b1zld` AS SIGNED)) AS `c1`,MIN(CAST(`ref_1`.`c_jyc_cd` AS DOUBLE)) AS `c2`,`ref_0`.`c_glkxdb` AS `c3`,COUNT(CAST(`ref_1`.`c_13sfid` AS DOUBLE)) AS `c4` FROM `testdb`.`t_037irb` AS `ref_0` JOIN `testdb`.`t_x7zqmd` AS `ref_1` WHERE `ref_0`.`c_nrh3o`>`ref_1`.`c_8weeq` GROUP BY `ref_0`.`c_glkxdb`) AS `subq_0` WHERE (SELECT `c_8weeq` AS `c_8weeq` FROM `testdb`.`t_x7zqmd` ORDER BY `c_8weeq` LIMIT 2,1) IS NOT NULL */;"]
   > [2024/06/18 16:12:01.718 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:231, Type:create view, State:none, SchemaState:queueing, SchemaID:221, TableID:230, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:01.716 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:01.721 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=207] [neededSchemaVersion=208] ["start time"=604.762µs] [phyTblIDs="[230]"] [actionTypes="[2097152]"]
   > [2024/06/18 16:12:01.722 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=208] ["take time"=2.24668ms] [job="ID:231, Type:create view, State:done, SchemaState:public, SchemaID:221, TableID:230, RowCount:0, ArgLen:3, start time: 2024-06-18 16:12:01.716 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:01.724 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:231, Type:create view, State:synced, SchemaState:public, SchemaID:221, TableID:230, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:01.716 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:01.725 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=231]
   > [2024/06/18 16:12:01.725 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 16:12:02.810 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=55] [user=root] [host=]
   > [2024/06/18 16:12:02.829 +00:00] [INFO] [set.go:139] ["set global var"] [conn=55] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/06/18 16:12:03.058 +00:00] [ERROR] [misc.go:95] ["panic in the recoverable goroutine"] [r="\"invalid memory address or nil pointer dereference\""] ["stack trace"="github.com/pingcap/tidb/util.WithRecovery.func1\n\t/go/src/github.com/pingcap/tidb/util/misc.go:97\nruntime.gopanic\n\t/usr/local/go/src/runtime/panic.go:884\nruntime.panicmem\n\t/usr/local/go/src/runtime/panic.go:260\nruntime.sigpanic\n\t/usr/local/go/src/runtime/signal_unix.go:839\ngithub.com/pingcap/tidb/executor.(*vecGroupChecker).splitIntoGroups\n\t/go/src/github.com/pingcap/tidb/executor/aggregate.go:1457\ngithub.com/pingcap/tidb/executor.(*PipelinedWindowExec).getRowsInPartition\n\t/go/src/github.com/pingcap/tidb/executor/pipelined_window.go:189\ngithub.com/pingcap/tidb/executor.(*PipelinedWindowExec).Next\n\t/go/src/github.com/pingcap/tidb/executor/pipelined_window.go:125\ngithub.com/pingcap/tidb/executor.Next\n\t/go/src/github.com/pingcap/tidb/executor/executor.go:286\ngithub.com/pingcap/tidb/executor.(*ProjectionExec).unParallelExecute\n\t/go/src/github.com/pingcap/tidb/executor/projection.go:194\ngithub.com/pingcap/tidb/executor.(*ProjectionExec).Next\n\t/go/src/github.com/pingcap/tidb/executor/projection.go:180\ngithub.com/pingcap/tidb/executor.Next\n\t/go/src/github.com/pingcap/tidb/executor/executor.go:286\ngithub.com/pingcap/tidb/executor.(*CTEExec).computeSeedPart\n\t/go/src/github.com/pingcap/tidb/executor/cte.go:226\ngithub.com/pingcap/tidb/executor.(*CTEExec).Next\n\t/go/src/github.com/pingcap/tidb/executor/cte.go:161\ngithub.com/pingcap/tidb/executor.Next\n\t/go/src/github.com/pingcap/tidb/executor/executor.go:286\ngithub.com/pingcap/tidb/executor.(*SelectionExec).Next\n\t/go/src/github.com/pingcap/tidb/executor/executor.go:1317\ngithub.com/pingcap/tidb/executor.Next\n\t/go/src/github.com/pingcap/tidb/executor/executor.go:286\ngithub.com/pingcap/tidb/executor.(*HashJoinExec).fetchBuildSideRows\n\t/go/src/github.com/pingcap/tidb/executor/join.go:266\ngithub.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable.func2\n\t/go/src/github.com/pingcap/tidb/executor/join.go:715\ngithub.com/pingcap/tidb/util.WithRecovery\n\t/go/src/github.com/pingcap/tidb/util/misc.go:100"]
   > [2024/06/18 16:12:04.906 +00:00] [WARN] [coprocessor.go:197] ["buildCopTasks takes too much time"] [elapsed=556.044559ms] ["range len"=1] ["task len"=1]
   > runtime: goroutine stack exceeds 1000000000-byte limit
   > runtime: sp=0xc03a280390 stack=[0xc03a280000, 0xc05a280000]
   > fatal error: stack overflow
   > runtime stack:
   > runtime.throw({0x3aa773d?, 0x590b5c0?})
   > 	/usr/local/go/src/runtime/panic.go:1047 +0x5d fp=0x7f71a692f888 sp=0x7f71a692f858 pc=0x13b859d
   > runtime.newstack()
   > 	/usr/local/go/src/runtime/stack.go:1103 +0x5cc fp=0x7f71a692fa40 sp=0x7f71a692f888 pc=0x13d35ec
   > runtime.morestack()
   > 	/usr/local/go/src/runtime/asm_amd64.s:570 +0x8b fp=0x7f71a692fa48 sp=0x7f71a692fa40 pc=0x13ec60b
   > goroutine 5083 [running]:
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60?, 0xc0104cc660?}, {0x4012e60?, 0xc0104cc6c0?})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:183 +0x12c fp=0xc03a2803a0 sp=0xc03a280398 pc=0x1f5780c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01117cc60}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a2803d8 sp=0xc03a2803a0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0111f5980}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280410 sp=0xc03a2803d8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01a7342d0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280448 sp=0xc03a280410 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01a702f00}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280480 sp=0xc03a280448 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01a7b6ed0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a2804b8 sp=0xc03a280480 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc000bbf8d0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a2804f0 sp=0xc03a2804b8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01a7342b0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280528 sp=0xc03a2804f0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0104ccd20}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280560 sp=0xc03a280528 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01a6bff40}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280598 sp=0xc03a280560 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc010dbdce0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a2805d0 sp=0xc03a280598 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0104cc6c0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280608 sp=0xc03a2805d0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0104cc660}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280640 sp=0xc03a280608 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01117cc60}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280678 sp=0xc03a280640 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0111f5980}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a2806b0 sp=0xc03a280678 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01a7342d0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a2806e8 sp=0xc03a2806b0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01a702f00}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280720 sp=0xc03a2806e8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01a7b6ed0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280758 sp=0xc03a280720 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc000bbf8d0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280790 sp=0xc03a280758 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01a7342b0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a2807c8 sp=0xc03a280790 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0104ccd20}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280800 sp=0xc03a2807c8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01a6bff40}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280838 sp=0xc03a280800 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc010dbdce0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280870 sp=0xc03a280838 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0104cc6c0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a2808a8 sp=0xc03a280870 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0104cc660}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a2808e0 sp=0xc03a2808a8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01117cc60}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280918 sp=0xc03a2808e0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0111f5980}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280950 sp=0xc03a280918 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01a7342d0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280988 sp=0xc03a280950 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01a702f00}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a2809c0 sp=0xc03a280988 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01a7b6ed0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a2809f8 sp=0xc03a2809c0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc000bbf8d0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280a30 sp=0xc03a2809f8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01a7342b0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280a68 sp=0xc03a280a30 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0104ccd20}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280aa0 sp=0xc03a280a68 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01a6bff40}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280ad8 sp=0xc03a280aa0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc010dbdce0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280b10 sp=0xc03a280ad8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0104cc6c0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280b48 sp=0xc03a280b10 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0104cc660}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280b80 sp=0xc03a280b48 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01117cc60}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280bb8 sp=0xc03a280b80 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0111f5980}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280bf0 sp=0xc03a280bb8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01a7342d0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280c28 sp=0xc03a280bf0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01a702f00}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280c60 sp=0xc03a280c28 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01a7b6ed0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280c98 sp=0xc03a280c60 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc000bbf8d0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280cd0 sp=0xc03a280c98 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01a7342b0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280d08 sp=0xc03a280cd0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0104ccd20}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280d40 sp=0xc03a280d08 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01a6bff40}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280d78 sp=0xc03a280d40 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc010dbdce0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280db0 sp=0xc03a280d78 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0104cc6c0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280de8 sp=0xc03a280db0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0104cc660}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280e20 sp=0xc03a280de8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01117cc60}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280e58 sp=0xc03a280e20 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0111f5980}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280e90 sp=0xc03a280e58 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01a7342d0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280ec8 sp=0xc03a280e90 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01a702f00}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280f00 sp=0xc03a280ec8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01a7b6ed0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280f38 sp=0xc03a280f00 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc000bbf8d0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280f70 sp=0xc03a280f38 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01a7342b0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280fa8 sp=0xc03a280f70 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0104ccd20}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a280fe0 sp=0xc03a280fa8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01a6bff40}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a281018 sp=0xc03a280fe0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc010dbdce0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a281050 sp=0xc03a281018 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0104cc6c0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a281088 sp=0xc03a281050 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0104cc660}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a2810c0 sp=0xc03a281088 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01117cc60}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a2810f8 sp=0xc03a2810c0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0111f5980}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a281130 sp=0xc03a2810f8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01a7342d0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a281168 sp=0xc03a281130 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01a702f00}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a2811a0 sp=0xc03a281168 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01a7b6ed0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a2811d8 sp=0xc03a2811a0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc000bbf8d0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a281210 sp=0xc03a2811d8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01a7342b0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a281248 sp=0xc03a281210 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0104ccd20}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a281280 sp=0xc03a281248 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01a6bff40}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a2812b8 sp=0xc03a281280 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc010dbdce0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a2812f0 sp=0xc03a2812b8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0104cc6c0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a281328 sp=0xc03a2812f0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0104cc660}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a281360 sp=0xc03a281328 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01117cc60}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a281398 sp=0xc03a281360 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0111f5980}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a2813d0 sp=0xc03a281398 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01a7342d0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a281408 sp=0xc03a2813d0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01a702f00}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a281440 sp=0xc03a281408 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01a7b6ed0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a281478 sp=0xc03a281440 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc000bbf8d0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a2814b0 sp=0xc03a281478 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01a7342b0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a2814e8 sp=0xc03a2814b0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0104ccd20}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a281520 sp=0xc03a2814e8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01a6bff40}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a281558 sp=0xc03a281520 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc010dbdce0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a281590 sp=0xc03a281558 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0104cc6c0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a2815c8 sp=0xc03a281590 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0104cc660}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a281600 sp=0xc03a2815c8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01117cc60}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a281638 sp=0xc03a281600 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0111f5980}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a281670 sp=0xc03a281638 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01a7342d0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a2816a8 sp=0xc03a281670 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01a702f00}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a2816e0 sp=0xc03a2816a8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01a7b6ed0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a281718 sp=0xc03a2816e0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc000bbf8d0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a281750 sp=0xc03a281718 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01a7342b0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a281788 sp=0xc03a281750 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0104ccd20}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a2817c0 sp=0xc03a281788 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01a6bff40}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a2817f8 sp=0xc03a2817c0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc010dbdce0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a281830 sp=0xc03a2817f8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0104cc6c0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a281868 sp=0xc03a281830 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0104cc660}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a2818a0 sp=0xc03a281868 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01117cc60}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a2818d8 sp=0xc03a2818a0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc0111f5980}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a281910 sp=0xc03a2818d8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01a7342d0}, {0x4012e60, 0xc0104cc6c0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc03a281948 sp=0xc03a281910 pc=0x1f577a5
   > ...additional frames elided...
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:712 +0x22d
   > goroutine 1 [chan receive]:
   > runtime.gopark(0xc010c90da0?, 0xc0112cfdc0?, 0xbf?, 0xc1?, 0x37fc5c0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0006fbd40 sp=0xc0006fbd20 pc=0x13bb516
   > runtime.chanrecv(0xc010a10480, 0xc0112cfe30, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc0006fbdd0 sp=0xc0006fbd40 pc=0x13854bb
   > runtime.chanrecv1(0xc0104c6680?, 0x0?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc0006fbdf8 sp=0xc0006fbdd0 pc=0x1384fb8
   > github.com/pingcap/tidb/server.(*Server).Run(0xc0104c6680)
   > 	/go/src/github.com/pingcap/tidb/server/server.go:370 +0x1f0 fp=0xc0006fbe50 sp=0xc0006fbdf8 pc=0x31e23d0
   > main.main()
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:213 +0x539 fp=0xc0006fbf80 sp=0xc0006fbe50 pc=0x33af4b9
   > runtime.main()
   > 	/usr/local/go/src/runtime/proc.go:250 +0x212 fp=0xc0006fbfe0 sp=0xc0006fbf80 pc=0x13bb152
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0006fbfe8 sp=0xc0006fbfe0 pc=0x13ee6e1
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
   > runtime.gopark(0x5f57220?, 0x3fe2f28?, 0x0?, 0x0?, 0x0?)
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
   > goroutine 18 [finalizer wait]:
   > runtime.gopark(0x5f58620?, 0xc0001024e0?, 0x0?, 0x0?, 0xc00008e770?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008e628 sp=0xc00008e608 pc=0x13bb516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.runfinq()
   > 	/usr/local/go/src/runtime/mfinal.go:180 +0x10f fp=0xc00008e7e0 sp=0xc00008e628 pc=0x1397f0f
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008e7e8 sp=0xc00008e7e0 pc=0x13ee6e1
   > created by runtime.createfing
   > 	/usr/local/go/src/runtime/mfinal.go:157 +0x45
   > goroutine 19 [GC worker (idle)]:
   > runtime.gopark(0x0?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008a750 sp=0xc00008a730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008a7e0 sp=0xc00008a750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008a7e8 sp=0xc00008a7e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 20 [GC worker (idle)]:
   > runtime.gopark(0x3fbbadcc1e5e?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008af50 sp=0xc00008af30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008afe0 sp=0xc00008af50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008afe8 sp=0xc00008afe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 5 [GC worker (idle)]:
   > runtime.gopark(0x3fbbadcc1701?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000090750 sp=0xc000090730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0000907e0 sp=0xc000090750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000907e8 sp=0xc0000907e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 6 [GC worker (idle)]:
   > runtime.gopark(0x3fbbadcc8f97?, 0x1?, 0xf4?, 0x83?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000090f50 sp=0xc000090f30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc000090fe0 sp=0xc000090f50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000090fe8 sp=0xc000090fe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 34 [GC worker (idle)]:
   > runtime.gopark(0x3fbbadcc07ff?, 0x1?, 0xcb?, 0x3?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004aa750 sp=0xc0004aa730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0004aa7e0 sp=0xc0004aa750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004aa7e8 sp=0xc0004aa7e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 21 [GC worker (idle)]:
   > runtime.gopark(0x3fbbadd15ceb?, 0x1?, 0x5f?, 0x81?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008b750 sp=0xc00008b730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008b7e0 sp=0xc00008b750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008b7e8 sp=0xc00008b7e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 22 [GC worker (idle)]:
   > runtime.gopark(0x3fbbadcc1701?, 0x1?, 0x9a?, 0xd?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008bf50 sp=0xc00008bf30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008bfe0 sp=0xc00008bf50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008bfe8 sp=0xc00008bfe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 23 [GC worker (idle)]:
   > runtime.gopark(0x3fbbadcc601e?, 0x1?, 0xe8?, 0x77?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008c750 sp=0xc00008c730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008c7e0 sp=0xc00008c750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008c7e8 sp=0xc00008c7e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 7 [GC worker (idle)]:
   > runtime.gopark(0x3fbbadd0837b?, 0x3?, 0x9c?, 0x1d?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000091750 sp=0xc000091730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0000917e0 sp=0xc000091750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000917e8 sp=0xc0000917e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 35 [GC worker (idle)]:
   > runtime.gopark(0x5f8be00?, 0x1?, 0xb5?, 0xd3?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004aaf50 sp=0xc0004aaf30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0004aafe0 sp=0xc0004aaf50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004aafe8 sp=0xc0004aafe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 36 [GC worker (idle)]:
   > runtime.gopark(0x5f8be00?, 0x1?, 0xa8?, 0x48?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004ab750 sp=0xc0004ab730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0004ab7e0 sp=0xc0004ab750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004ab7e8 sp=0xc0004ab7e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 37 [GC worker (idle)]:
   > runtime.gopark(0x3fbbadcc601e?, 0x1?, 0x21?, 0x80?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004abf50 sp=0xc0004abf30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0004abfe0 sp=0xc0004abf50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004abfe8 sp=0xc0004abfe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 50 [GC worker (idle)]:
   > runtime.gopark(0x3fbbadd07c1d?, 0x1?, 0x9a?, 0xa6?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004a6750 sp=0xc0004a6730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0004a67e0 sp=0xc0004a6750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004a67e8 sp=0xc0004a67e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 51 [GC worker (idle)]:
   > runtime.gopark(0x3fbbadcc8f97?, 0x1?, 0x2d?, 0x4?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000686f50 sp=0xc000686f30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc000686fe0 sp=0xc000686f50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000686fe8 sp=0xc000686fe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 38 [GC worker (idle)]:
   > runtime.gopark(0x3fbbadcc07ff?, 0x1?, 0xbf?, 0x45?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004ac750 sp=0xc0004ac730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0004ac7e0 sp=0xc0004ac750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004ac7e8 sp=0xc0004ac7e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 39 [GC worker (idle)]:
   > runtime.gopark(0x3fbbadd4bc1f?, 0x1?, 0xdb?, 0x86?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004acf50 sp=0xc0004acf30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0004acfe0 sp=0xc0004acf50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004acfe8 sp=0xc0004acfe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 10 [select]:
   > runtime.gopark(0xc00009cf88?, 0x3?, 0xa8?, 0xb8?, 0xc00009cf72?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00009cdf8 sp=0xc00009cdd8 pc=0x13bb516
   > runtime.selectgo(0xc00009cf88, 0xc00009cf6c, 0xc000912280?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00009cf38 sp=0xc00009cdf8 pc=0x13cbbdc
   > go.opencensus.io/stats/view.(*worker).start(0xc000912280)
   > 	/go/pkg/mod/go.opencensus.io@v0.23.0/stats/view/worker.go:276 +0xad fp=0xc00009cfc8 sp=0xc00009cf38 pc=0x29900cd
   > go.opencensus.io/stats/view.init.0.func1()
   > 	/go/pkg/mod/go.opencensus.io@v0.23.0/stats/view/worker.go:34 +0x26 fp=0xc00009cfe0 sp=0xc00009cfc8 pc=0x298f346
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00009cfe8 sp=0xc00009cfe0 pc=0x13ee6e1
   > created by go.opencensus.io/stats/view.init.0
   > 	/go/pkg/mod/go.opencensus.io@v0.23.0/stats/view/worker.go:34 +0x8d
   > goroutine 47 [chan receive]:
   > runtime.gopark(0xc0002f5c20?, 0x13c1374?, 0x10?, 0x9e?, 0x13d8de5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000689db8 sp=0xc000689d98 pc=0x13bb516
   > runtime.chanrecv(0xc0002f5bc0, 0xc000689f28, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000689e48 sp=0xc000689db8 pc=0x13854bb
   > runtime.chanrecv2(0x3b9aca00?, 0x13bb600?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc000689e70 sp=0xc000689e48 pc=0x1384ff8
   > go.etcd.io/etcd/pkg/logutil.(*MergeLogger).outputLoop(0xc000012840)
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:173 +0x8c fp=0xc000689fc8 sp=0xc000689e70 pc=0x1a12c4c
   > go.etcd.io/etcd/pkg/logutil.NewMergeLogger.func1()
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:91 +0x26 fp=0xc000689fe0 sp=0xc000689fc8 pc=0x1a124c6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000689fe8 sp=0xc000689fe0 pc=0x13ee6e1
   > created by go.etcd.io/etcd/pkg/logutil.NewMergeLogger
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:91 +0xb6
   > goroutine 210 [chan receive]:
   > runtime.gopark(0xc000680540?, 0x0?, 0x10?, 0x1e?, 0x13d8de5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0000a1db8 sp=0xc0000a1d98 pc=0x13bb516
   > runtime.chanrecv(0xc0006804e0, 0xc0000a1f28, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc0000a1e48 sp=0xc0000a1db8 pc=0x13854bb
   > runtime.chanrecv2(0x3b9aca00?, 0x13bb600?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc0000a1e70 sp=0xc0000a1e48 pc=0x1384ff8
   > go.etcd.io/etcd/pkg/logutil.(*MergeLogger).outputLoop(0xc000129c50)
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:173 +0x8c fp=0xc0000a1fc8 sp=0xc0000a1e70 pc=0x1a12c4c
   > go.etcd.io/etcd/pkg/logutil.NewMergeLogger.func1()
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:91 +0x26 fp=0xc0000a1fe0 sp=0xc0000a1fc8 pc=0x1a124c6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000a1fe8 sp=0xc0000a1fe0 pc=0x13ee6e1
   > created by go.etcd.io/etcd/pkg/logutil.NewMergeLogger
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:91 +0xb6
   > goroutine 196 [chan receive]:
   > runtime.gopark(0xc000680600?, 0x1?, 0x10?, 0x4e?, 0x13d8de5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000684db8 sp=0xc000684d98 pc=0x13bb516
   > runtime.chanrecv(0xc0006805a0, 0xc000684f28, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000684e48 sp=0xc000684db8 pc=0x13854bb
   > runtime.chanrecv2(0x3b9aca00?, 0x13bb600?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc000684e70 sp=0xc000684e48 pc=0x1384ff8
   > go.etcd.io/etcd/pkg/logutil.(*MergeLogger).outputLoop(0xc00002fd28)
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:173 +0x8c fp=0xc000684fc8 sp=0xc000684e70 pc=0x1a12c4c
   > go.etcd.io/etcd/pkg/logutil.NewMergeLogger.func1()
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:91 +0x26 fp=0xc000684fe0 sp=0xc000684fc8 pc=0x1a124c6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000684fe8 sp=0xc000684fe0 pc=0x13ee6e1
   > created by go.etcd.io/etcd/pkg/logutil.NewMergeLogger
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:91 +0xb6
   > goroutine 439 [chan receive]:
   > runtime.gopark(0x171cee90a68?, 0x0?, 0x78?, 0x8e?, 0x13d8de5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000688e20 sp=0xc000688e00 pc=0x13bb516
   > runtime.chanrecv(0xc0000bc1e0, 0x0, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000688eb0 sp=0xc000688e20 pc=0x13854bb
   > runtime.chanrecv1(0xdf8475800?, 0x1b?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc000688ed8 sp=0xc000688eb0 pc=0x1384fb8
   > github.com/pingcap/tidb/util/profile.HeapProfileForGlobalMemTracker(0xc00055d800?)
   > 	/go/src/github.com/pingcap/tidb/util/profile/trackerRecorder.go:33 +0xa7 fp=0xc000688fc8 sp=0xc000688ed8 pc=0x267adc7
   > main.setHeapProfileTracker.func1()
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:279 +0x26 fp=0xc000688fe0 sp=0xc000688fc8 pc=0x33afc46
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000688fe8 sp=0xc000688fe0 pc=0x13ee6e1
   > created by main.setHeapProfileTracker
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:279 +0xa5
   > goroutine 440 [chan receive]:
   > runtime.gopark(0xc011e13320?, 0xc0000bc298?, 0xe?, 0x17?, 0x2?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00009fde0 sp=0xc00009fdc0 pc=0x13bb516
   > runtime.chanrecv(0xc0000bc240, 0x0, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc00009fe70 sp=0xc00009fde0 pc=0x13854bb
   > runtime.chanrecv1(0x5f5e100?, 0x3ace4e4?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc00009fe98 sp=0xc00009fe70 pc=0x1384fb8
   > github.com/pingcap/tidb/util/systimemon.StartMonitor(0x3bccd98, 0x3bcc3f0, 0xc000a11050)
   > 	/go/src/github.com/pingcap/tidb/util/systimemon/systime_mon.go:32 +0x185 fp=0xc00009ffb8 sp=0xc00009fe98 pc=0x33ac665
   > main.setupMetrics.func3()
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:696 +0x31 fp=0xc00009ffe0 sp=0xc00009ffb8 pc=0x33b2df1
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00009ffe8 sp=0xc00009ffe0 pc=0x13ee6e1
   > created by main.setupMetrics
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:696 +0x115
   > goroutine 441 [select]:
   > runtime.gopark(0xc0004a7f80?, 0x2?, 0x10?, 0x0?, 0xc0004a7f4c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004a7dd0 sp=0xc0004a7db0 pc=0x13bb516
   > runtime.selectgo(0xc0004a7f80, 0xc0004a7f48, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0004a7f10 sp=0xc0004a7dd0 pc=0x13cbbdc
   > github.com/pingcap/badger.(*DB).updateSize(0x0?, 0xc000ee6c90)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:1039 +0x105 fp=0xc0004a7fc0 sp=0xc0004a7f10 pc=0x329a445
   > github.com/pingcap/badger.Open.func5()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:328 +0x2a fp=0xc0004a7fe0 sp=0xc0004a7fc0 pc=0x329450a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004a7fe8 sp=0xc0004a7fe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.Open
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:328 +0xf5c
   > goroutine 442 [select]:
   > runtime.gopark(0xc0004a8788?, 0x2?, 0x9?, 0x18?, 0xc0004a8764?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004a85e8 sp=0xc0004a85c8 pc=0x13bb516
   > runtime.selectgo(0xc0004a8788, 0xc0004a8760, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0004a8728 sp=0xc0004a85e8 pc=0x13cbbdc
   > github.com/pingcap/badger/epoch.(*ResourceManager).collectLoop(0x0?, 0xc000ee6cc0)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/epoch/manager.go:101 +0xd3 fp=0xc0004a87c0 sp=0xc0004a8728 pc=0x3257a13
   > github.com/pingcap/badger/epoch.NewResourceManager.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/epoch/manager.go:79 +0x2a fp=0xc0004a87e0 sp=0xc0004a87c0 pc=0x32577aa
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004a87e8 sp=0xc0004a87e0 pc=0x13ee6e1
   > created by github.com/pingcap/badger/epoch.NewResourceManager
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/epoch/manager.go:79 +0xdd
   > goroutine 443 [select]:
   > runtime.gopark(0xc00009de68?, 0x2?, 0x8?, 0x1?, 0xc00009de3c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00009dcc0 sp=0xc00009dca0 pc=0x13bb516
   > runtime.selectgo(0xc00009de68, 0xc00009de38, 0x0?, 0x1, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00009de00 sp=0xc00009dcc0 pc=0x13cbbdc
   > github.com/pingcap/badger.Open.func4()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:342 +0x155 fp=0xc00009dfe0 sp=0xc00009de00 pc=0x3294495
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00009dfe8 sp=0xc00009dfe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.Open
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:339 +0x11f8
   > goroutine 444 [select]:
   > runtime.gopark(0xc00008df08?, 0x2?, 0x0?, 0x0?, 0xc00008dee4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000d20d68 sp=0xc000d20d48 pc=0x13bb516
   > runtime.selectgo(0xc000d20f08, 0xc00008dee0, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000d20ea8 sp=0xc000d20d68 pc=0x13cbbdc
   > github.com/pingcap/badger.(*blobGCHandler).run(0xc000cd0200, 0xc000faa048)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/blob.go:468 +0xd6 fp=0xc000d20fc0 sp=0xc000d20ea8 pc=0x3288896
   > github.com/pingcap/badger.(*blobManager).Open.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/blob.go:292 +0x2a fp=0xc000d20fe0 sp=0xc000d20fc0 pc=0x328754a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000d20fe8 sp=0xc000d20fe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.(*blobManager).Open
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/blob.go:292 +0x5bd
   > goroutine 445 [select]:
   > runtime.gopark(0xc000682f60?, 0x2?, 0x4?, 0x30?, 0xc000682f2c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000682d98 sp=0xc000682d78 pc=0x13bb516
   > runtime.selectgo(0xc000682f60, 0xc000682f28, 0x0?, 0x0, 0xc0004adf48?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000682ed8 sp=0xc000682d98 pc=0x13cbbdc
   > github.com/pingcap/badger.(*levelsController).runWorker(0xc0000e2460, 0xc000faa078, 0x0)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:212 +0x1fb fp=0xc000682fb8 sp=0xc000682ed8 pc=0x32a297b
   > github.com/pingcap/badger.(*levelsController).startCompact.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:180 +0x2e fp=0xc000682fe0 sp=0xc000682fb8 pc=0x32a274e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000682fe8 sp=0xc000682fe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.(*levelsController).startCompact
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:180 +0x65
   > goroutine 446 [select]:
   > runtime.gopark(0xc000d21f60?, 0x2?, 0x4?, 0x30?, 0xc000d21f2c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000d21d98 sp=0xc000d21d78 pc=0x13bb516
   > runtime.selectgo(0xc000d21f60, 0xc000d21f28, 0x0?, 0x0, 0xf4240?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000d21ed8 sp=0xc000d21d98 pc=0x13cbbdc
   > github.com/pingcap/badger.(*levelsController).runWorker(0xc0000e2460, 0xc000faa078, 0x0)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:212 +0x1fb fp=0xc000d21fb8 sp=0xc000d21ed8 pc=0x32a297b
   > github.com/pingcap/badger.(*levelsController).startCompact.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:180 +0x2e fp=0xc000d21fe0 sp=0xc000d21fb8 pc=0x32a274e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000d21fe8 sp=0xc000d21fe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.(*levelsController).startCompact
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:180 +0x65
   > goroutine 447 [select]:
   > runtime.gopark(0xc000687f60?, 0x2?, 0x3?, 0x30?, 0xc000687f2c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000687d98 sp=0xc000687d78 pc=0x13bb516
   > runtime.selectgo(0xc000687f60, 0xc000687f28, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000687ed8 sp=0xc000687d98 pc=0x13cbbdc
   > github.com/pingcap/badger.(*levelsController).runWorker(0xc0000e2460, 0xc000faa078, 0x1)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:212 +0x1fb fp=0xc000687fb8 sp=0xc000687ed8 pc=0x32a297b
   > github.com/pingcap/badger.(*levelsController).startCompact.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:180 +0x2e fp=0xc000687fe0 sp=0xc000687fb8 pc=0x32a274e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000687fe8 sp=0xc000687fe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.(*levelsController).startCompact
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:180 +0x65
   > goroutine 448 [chan receive]:
   > runtime.gopark(0x0?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000685ac0 sp=0xc000685aa0 pc=0x13bb516
   > runtime.chanrecv(0xc000ed0de0, 0xc000685c60, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000685b50 sp=0xc000685ac0 pc=0x13854bb
   > runtime.chanrecv2(0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc000685b78 sp=0xc000685b50 pc=0x1384ff8
   > github.com/pingcap/badger.(*DB).runFlushMemTable(0xc000de0480, 0x0?)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:920 +0xdd fp=0xc000685fc0 sp=0xc000685b78 pc=0x3298efd
   > github.com/pingcap/badger.Open.func6()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:361 +0x2a fp=0xc000685fe0 sp=0xc000685fc0 pc=0x329430a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000685fe8 sp=0xc000685fe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.Open
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:361 +0x158d
   > goroutine 3366 [chan receive]:
   > runtime.gopark(0xc0108e14a0?, 0xc010dbdce0?, 0x3?, 0x0?, 0xc01122dcf8?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01122dca8 sp=0xc01122dc88 pc=0x13bb516
   > runtime.chanrecv(0xc010dbdc20, 0xc01122de08, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc01122dd38 sp=0xc01122dca8 pc=0x13854bb
   > runtime.chanrecv2(0xc010afe7b0?, 0x4012e60?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc01122dd60 sp=0xc01122dd38 pc=0x1384ff8
   > github.com/pingcap/tidb/executor.(*HashJoinExec).buildHashTableForList(0xc010e858c0, 0x1?)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:762 +0x2d6 fp=0xc01122de78 sp=0xc01122dd60 pc=0x3065af6
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable(0xc010e858c0, {0x400d6b0?, 0xc017de12c0})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:726 +0x23f fp=0xc01122df28 sp=0xc01122de78 pc=0x30653ff
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Next.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:671 +0x8f fp=0xc01122df90 sp=0xc01122df28 pc=0x306504f
   > github.com/pingcap/tidb/util.WithRecovery(0x5f539a0?, 0xc011a797b8?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc01122dfc0 sp=0xc01122df90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Next.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:669 +0x2a fp=0xc01122dfe0 sp=0xc01122dfc0 pc=0x3064f8a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01122dfe8 sp=0xc01122dfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).Next
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:669 +0x5b2
   > goroutine 482 [select]:
   > runtime.gopark(0xc000d1bf78?, 0x3?, 0x25?, 0x48?, 0xc000d1bf32?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000d1bd98 sp=0xc000d1bd78 pc=0x13bb516
   > runtime.selectgo(0xc000d1bf78, 0xc000d1bf2c, 0x1?, 0x0, 0xc0009f4ea0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000d1bed8 sp=0xc000d1bd98 pc=0x13cbbdc
   > github.com/pingcap/badger.(*writeWorker).runWriteVLog(0xc000b9c080, 0xc000012180)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:94 +0x137 fp=0xc000d1bfc0 sp=0xc000d1bed8 pc=0x32b28b7
   > github.com/pingcap/badger.startWriteWorker.func2()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:64 +0x2a fp=0xc000d1bfe0 sp=0xc000d1bfc0 pc=0x32b238a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000d1bfe8 sp=0xc000d1bfe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.startWriteWorker
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:64 +0x1f9
   > goroutine 483 [chan receive, locked to thread]:
   > runtime.gopark(0xc000d1ce98?, 0x1456628?, 0xf?, 0x0?, 0x1?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000d1ce68 sp=0xc000d1ce48 pc=0x13bb516
   > runtime.chanrecv(0xc000fa02a0, 0xc000d1cf88, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000d1cef8 sp=0xc000d1ce68 pc=0x13854bb
   > runtime.chanrecv2(0xc0004c47e0?, 0x3ef44926ff371c10?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc000d1cf20 sp=0xc000d1cef8 pc=0x1384ff8
   > github.com/pingcap/badger.(*writeWorker).runWriteLSM(0xc000b9c080, 0x0?)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:141 +0x15e fp=0xc000d1cfc0 sp=0xc000d1cf20 pc=0x32b2efe
   > github.com/pingcap/badger.startWriteWorker.func3()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:65 +0x2a fp=0xc000d1cfe0 sp=0xc000d1cfc0 pc=0x32b232a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000d1cfe8 sp=0xc000d1cfe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.startWriteWorker
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:65 +0x24d
   > goroutine 484 [chan receive]:
   > runtime.gopark(0xc0011699d0?, 0xc0011f9ae0?, 0x70?, 0xc2?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000ef5ea8 sp=0xc000ef5e88 pc=0x13bb516
   > runtime.chanrecv(0xc000fa0300, 0xc000ef5f88, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000ef5f38 sp=0xc000ef5ea8 pc=0x13854bb
   > runtime.chanrecv2(0xc000ed4020?, 0x0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc000ef5f60 sp=0xc000ef5f38 pc=0x1384ff8
   > github.com/pingcap/badger.(*writeWorker).runMergeLSM(0x0?, 0x0?)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:154 +0x9b fp=0xc000ef5fc0 sp=0xc000ef5f60 pc=0x32b307b
   > github.com/pingcap/badger.startWriteWorker.func4()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:66 +0x2a fp=0xc000ef5fe0 sp=0xc000ef5fc0 pc=0x32b22ca
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000ef5fe8 sp=0xc000ef5fe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.startWriteWorker
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:66 +0x2a5
   > goroutine 485 [select]:
   > runtime.gopark(0xc0000a2f88?, 0x2?, 0x0?, 0x0?, 0xc0000a2f4c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0000a2da0 sp=0xc0000a2d80 pc=0x13bb516
   > runtime.selectgo(0xc0000a2f88, 0xc0000a2f48, 0xc010c903d0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0000a2ee0 sp=0xc0000a2da0 pc=0x13cbbdc
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.writeDBWorker.run({0xc000fa03c0?, 0xc000cd0a40?})
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:96 +0x145 fp=0xc0000a2fc0 sp=0xc0000a2ee0 pc=0x3308de5
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*dbWriter).Open.func1()
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:202 +0x2a fp=0xc0000a2fe0 sp=0xc0000a2fc0 pc=0x330996a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000a2fe8 sp=0xc0000a2fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*dbWriter).Open
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:199 +0xc5
   > goroutine 486 [select]:
   > runtime.gopark(0xc000683e70?, 0x2?, 0x90?, 0x3e?, 0xc000683e1c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000683c58 sp=0xc000683c38 pc=0x13bb516
   > runtime.selectgo(0xc000683e70, 0xc000683e18, 0x13?, 0x0, 0xc01a8cf200?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000683d98 sp=0xc000683c58 pc=0x13cbbdc
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.writeLockWorker.run({0xc000fa0420?, 0xc000cd0a40?})
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:148 +0x15f fp=0xc000683fc0 sp=0xc000683d98 pc=0x33093bf
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*dbWriter).Open.func2()
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:209 +0x2a fp=0xc000683fe0 sp=0xc000683fc0 pc=0x330990a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000683fe8 sp=0xc000683fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*dbWriter).Open
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:206 +0x159
   > goroutine 487 [select]:
   > runtime.gopark(0xc0005aff18?, 0x2?, 0x20?, 0x0?, 0xc0005aff04?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0005afd88 sp=0xc0005afd68 pc=0x13bb516
   > runtime.selectgo(0xc0005aff18, 0xc0005aff00, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0005afec8 sp=0xc0005afd88 pc=0x13cbbdc
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*MVCCStore).runUpdateSafePointLoop(0xc000912000)
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:1550 +0x217 fp=0xc0005affc8 sp=0xc0005afec8 pc=0x32facd7
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.NewMVCCStore.func1()
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:85 +0x26 fp=0xc0005affe0 sp=0xc0005affc8 pc=0x32ed406
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0005affe8 sp=0xc0005affe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.NewMVCCStore
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:85 +0x337
   > goroutine 488 [select]:
   > runtime.gopark(0xc000091fb0?, 0x2?, 0x0?, 0x0?, 0xc000091f9c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000091e28 sp=0xc000091e08 pc=0x13bb516
   > runtime.selectgo(0xc000091fb0, 0xc000091f98, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000091f68 sp=0xc000091e28 pc=0x13cbbdc
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*MVCCStore).StartDeadlockDetection.func1()
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:1286 +0x7b fp=0xc000091fe0 sp=0xc000091f68 pc=0x32f895b
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000091fe8 sp=0xc000091fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*MVCCStore).StartDeadlockDetection
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:1284 +0xb6
   > goroutine 148 [select]:
   > runtime.gopark(0xc000628f78?, 0x2?, 0x0?, 0x30?, 0xc000628f3c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000628dc0 sp=0xc000628da0 pc=0x13bb516
   > runtime.selectgo(0xc000628f78, 0xc000628f38, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000628f00 sp=0xc000628dc0 pc=0x13cbbdc
   > github.com/tikv/client-go/v2/oracle/oracles.(*pdOracle).updateTS(0xc0004fe000, {0x400d640, 0xc000120008}, 0xc000cd0a40?)
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/oracle/oracles/pd.go:229 +0x128 fp=0xc000628fb0 sp=0xc000628f00 pc=0x1e9b548
   > github.com/tikv/client-go/v2/oracle/oracles.NewPdOracle.func1()
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/oracle/oracles/pd.go:77 +0x32 fp=0xc000628fe0 sp=0xc000628fb0 pc=0x1e9a772
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000628fe8 sp=0xc000628fe0 pc=0x13ee6e1
   > created by github.com/tikv/client-go/v2/oracle/oracles.NewPdOracle
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/oracle/oracles/pd.go:77 +0x119
   > goroutine 149 [select]:
   > runtime.gopark(0xc00008df78?, 0x3?, 0x10?, 0x0?, 0xc00008df5a?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008dde0 sp=0xc00008ddc0 pc=0x13bb516
   > runtime.selectgo(0xc00008df78, 0xc00008df54, 0x1000200000000?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00008df20 sp=0xc00008dde0 pc=0x13cbbdc
   > github.com/tikv/client-go/v2/internal/locate.(*RegionCache).asyncCheckAndResolveLoop(0xc000a36400, 0xc000ee6018?)
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/internal/locate/region_cache.go:399 +0xd1 fp=0xc00008dfc0 sp=0xc00008df20 pc=0x1e6bff1
   > github.com/tikv/client-go/v2/internal/locate.NewRegionCache.func1()
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/internal/locate/region_cache.go:370 +0x2a fp=0xc00008dfe0 sp=0xc00008dfc0 pc=0x1e6bc6a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008dfe8 sp=0xc00008dfe0 pc=0x13ee6e1
   > created by github.com/tikv/client-go/v2/internal/locate.NewRegionCache
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/internal/locate/region_cache.go:370 +0x2e6
   > goroutine 150 [select]:
   > runtime.gopark(0xc000ef1f10?, 0x2?, 0x5?, 0x30?, 0xc000ef1eac?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000ef1d10 sp=0xc000ef1cf0 pc=0x13bb516
   > runtime.selectgo(0xc000ef1f10, 0xc000ef1ea8, 0x0?, 0x0, 0x5f55780?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000ef1e50 sp=0xc000ef1d10 pc=0x13cbbdc
   > github.com/tikv/client-go/v2/tikv.(*KVStore).runSafePointChecker(0xc000950d80)
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/tikv/kv.go:264 +0x12b fp=0xc000ef1fc8 sp=0xc000ef1e50 pc=0x1ed6f0b
   > github.com/tikv/client-go/v2/tikv.NewKVStore.func1()
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/tikv/kv.go:187 +0x26 fp=0xc000ef1fe0 sp=0xc000ef1fc8 pc=0x1ed6d06
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000ef1fe8 sp=0xc000ef1fe0 pc=0x13ee6e1
   > created by github.com/tikv/client-go/v2/tikv.NewKVStore
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/tikv/kv.go:187 +0x3d6
   > goroutine 151 [select]:
   > runtime.gopark(0xc000ef7f80?, 0x2?, 0x0?, 0xbe?, 0xc000ef7f44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000ef7dc8 sp=0xc000ef7da8 pc=0x13bb516
   > runtime.selectgo(0xc000ef7f80, 0xc000ef7f40, 0xc000513a40?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000ef7f08 sp=0xc000ef7dc8 pc=0x13cbbdc
   > github.com/tikv/client-go/v2/tikv.(*KVStore).safeTSUpdater(0xc000950d80)
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/tikv/kv.go:544 +0x165 fp=0xc000ef7fc8 sp=0xc000ef7f08 pc=0x1ed8e65
   > github.com/tikv/client-go/v2/tikv.NewKVStore.func2()
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/tikv/kv.go:188 +0x26 fp=0xc000ef7fe0 sp=0xc000ef7fc8 pc=0x1ed6ca6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000ef7fe8 sp=0xc000ef7fe0 pc=0x13ee6e1
   > created by github.com/tikv/client-go/v2/tikv.NewKVStore
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/tikv/kv.go:188 +0x416
   > goroutine 152 [select]:
   > runtime.gopark(0xc0005aaf98?, 0x2?, 0x90?, 0xae?, 0xc0005aaf6c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0005aade8 sp=0xc0005aadc8 pc=0x13bb516
   > runtime.selectgo(0xc0005aaf98, 0xc0005aaf68, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0005aaf28 sp=0xc0005aade8 pc=0x13cbbdc
   > github.com/dgraph-io/ristretto.(*defaultPolicy).processItems(0xc0001eedb0)
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.0.1/policy.go:96 +0x91 fp=0xc0005aafc8 sp=0xc0005aaf28 pc=0x23cf0d1
   > github.com/dgraph-io/ristretto.newDefaultPolicy.func1()
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.0.1/policy.go:80 +0x26 fp=0xc0005aafe0 sp=0xc0005aafc8 pc=0x23cef86
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0005aafe8 sp=0xc0005aafe0 pc=0x13ee6e1
   > created by github.com/dgraph-io/ristretto.newDefaultPolicy
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.0.1/policy.go:80 +0x156
   > goroutine 153 [select]:
   > runtime.gopark(0xc0005ab798?, 0x2?, 0x0?, 0x0?, 0xc0005ab774?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0005ab5f0 sp=0xc0005ab5d0 pc=0x13bb516
   > runtime.selectgo(0xc0005ab798, 0xc0005ab770, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0005ab730 sp=0xc0005ab5f0 pc=0x13cbbdc
   > github.com/dgraph-io/ristretto.(*Cache).processItems(0xc000ed0c00)
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.0.1/cache.go:257 +0x85 fp=0xc0005ab7c8 sp=0xc0005ab730 pc=0x23ce025
   > github.com/dgraph-io/ristretto.NewCache.func2()
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.0.1/cache.go:155 +0x26 fp=0xc0005ab7e0 sp=0xc0005ab7c8 pc=0x23cd846
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0005ab7e8 sp=0xc0005ab7e0 pc=0x13ee6e1
   > created by github.com/dgraph-io/ristretto.NewCache
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.0.1/cache.go:155 +0x485
   > goroutine 55 [select]:
   > runtime.gopark(0xc000909f18?, 0x3?, 0x6?, 0x30?, 0xc000909e8a?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000909cc8 sp=0xc000909ca8 pc=0x13bb516
   > runtime.selectgo(0xc000909f18, 0xc000909e84, 0xc011250000?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000909e08 sp=0xc000909cc8 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).LoadSysVarCacheLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:989 +0x145 fp=0xc000909fe0 sp=0xc000909e08 pc=0x26a3dc5
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000909fe8 sp=0xc000909fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).LoadSysVarCacheLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:980 +0x172
   > goroutine 727 [select]:
   > runtime.gopark(0xc01a877f38?, 0x2?, 0x0?, 0x0?, 0xc01a877efc?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01a877d50 sp=0xc01a877d30 pc=0x13bb516
   > runtime.selectgo(0xc01a877f38, 0xc01a877ef8, 0x1?, 0x0, 0x2?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01a877e90 sp=0xc01a877d50 pc=0x13cbbdc
   > github.com/pingcap/tidb/ddl.(*ddl).limitDDLJobs(0xc010ba62a0)
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl_worker.go:263 +0x173 fp=0xc01a877fc8 sp=0xc01a877e90 pc=0x2623fd3
   > github.com/pingcap/tidb/ddl.(*ddl).Start.func1()
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:351 +0x26 fp=0xc01a877fe0 sp=0xc01a877fc8 pc=0x25e9ac6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01a877fe8 sp=0xc01a877fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/ddl.(*ddl).Start
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:351 +0x2ea
   > goroutine 728 [select]:
   > runtime.gopark(0xc01a96bf90?, 0x2?, 0xbf?, 0xc1?, 0xc01a96bf6c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01a96bdf0 sp=0xc01a96bdd0 pc=0x13bb516
   > runtime.selectgo(0xc01a96bf90, 0xc01a96bf68, 0x25?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01a96bf30 sp=0xc01a96bdf0 pc=0x13cbbdc
   > github.com/pingcap/tidb/ddl.(*delRange).startEmulator(0xc010be0900)
   > 	/go/src/github.com/pingcap/tidb/ddl/delete_range.go:144 +0x125 fp=0xc01a96bfc8 sp=0xc01a96bf30 pc=0x262b9e5
   > github.com/pingcap/tidb/ddl.(*delRange).start.func1()
   > 	/go/src/github.com/pingcap/tidb/ddl/delete_range.go:126 +0x26 fp=0xc01a96bfe0 sp=0xc01a96bfc8 pc=0x262b7a6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01a96bfe8 sp=0xc01a96bfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/ddl.(*delRange).start
   > 	/go/src/github.com/pingcap/tidb/ddl/delete_range.go:126 +0x6d
   > goroutine 79 [select]:
   > runtime.gopark(0xc018042778?, 0x2?, 0xc0?, 0x9?, 0xc0180426ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc018042558 sp=0xc018042538 pc=0x13bb516
   > runtime.selectgo(0xc018042778, 0xc0180426e8, 0x3aac226?, 0x0, 0xc01a459c60?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc018042698 sp=0xc018042558 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc0186bff40, {0x400d6b0?, 0xc017de12c0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc0180427b8 sp=0xc018042698 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc0180427e0 sp=0xc0180427b8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0180427e8 sp=0xc0180427e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 60 [select]:
   > runtime.gopark(0xc00fb28728?, 0x2?, 0x0?, 0x30?, 0xc00fb286d4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fb28548 sp=0xc00fb28528 pc=0x13bb516
   > runtime.selectgo(0xc00fb28728, 0xc00fb286d0, 0x9?, 0x0, 0x15?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fb28688 sp=0xc00fb28548 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).TelemetryReportLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1140 +0x11c fp=0xc00fb287e0 sp=0xc00fb28688 pc=0x26a573c
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fb287e8 sp=0xc00fb287e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).TelemetryReportLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1132 +0x285
   > goroutine 730 [select]:
   > runtime.gopark(0xc01a6edf58?, 0x4?, 0xab?, 0x62?, 0xc01a6edda8?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01a6edbf8 sp=0xc01a6edbd8 pc=0x13bb516
   > runtime.selectgo(0xc01a6edf58, 0xc01a6edda0, 0xc000ef1e38?, 0x0, 0x1?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01a6edd38 sp=0xc01a6edbf8 pc=0x13cbbdc
   > github.com/pingcap/tidb/ddl.(*worker).start(0xc010e24420, 0xc010ba43c0)
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl_worker.go:178 +0x318 fp=0xc01a6edfc0 sp=0xc01a6edd38 pc=0x2622e98
   > github.com/pingcap/tidb/ddl.(*ddl).Start.func2()
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:369 +0x2a fp=0xc01a6edfe0 sp=0xc01a6edfc0 pc=0x25e9a6a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01a6edfe8 sp=0xc01a6edfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/ddl.(*ddl).Start
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:369 +0x5c5
   > goroutine 52 [select]:
   > runtime.gopark(0xc000a72f18?, 0x3?, 0x0?, 0x30?, 0xc000a72e9a?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000a72cd8 sp=0xc000a72cb8 pc=0x13bb516
   > runtime.selectgo(0xc000a72f18, 0xc000a72e94, 0xc010a10420?, 0x0, 0xc010db7d40?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000a72e18 sp=0xc000a72cd8 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).LoadPrivilegeLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:939 +0x145 fp=0xc000a72fe0 sp=0xc000a72e18 pc=0x26a3585
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000a72fe8 sp=0xc000a72fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).LoadPrivilegeLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:930 +0x205
   > goroutine 729 [select]:
   > runtime.gopark(0xc000963f58?, 0x4?, 0xab?, 0x62?, 0xc000963da8?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000963bf8 sp=0xc000963bd8 pc=0x13bb516
   > runtime.selectgo(0xc000963f58, 0xc000963da0, 0xc000627e38?, 0x0, 0x1?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000963d38 sp=0xc000963bf8 pc=0x13cbbdc
   > github.com/pingcap/tidb/ddl.(*worker).start(0xc010e24370, 0xc010ba43c0)
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl_worker.go:178 +0x318 fp=0xc000963fc0 sp=0xc000963d38 pc=0x2622e98
   > github.com/pingcap/tidb/ddl.(*ddl).Start.func2()
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:369 +0x2a fp=0xc000963fe0 sp=0xc000963fc0 pc=0x25e9a6a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000963fe8 sp=0xc000963fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/ddl.(*ddl).Start
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:369 +0x5c5
   > goroutine 5184 [select]:
   > runtime.gopark(0xc000ef3f78?, 0x2?, 0xa0?, 0x3d?, 0xc000ef3eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000ef3d58 sp=0xc000ef3d38 pc=0x13bb516
   > runtime.selectgo(0xc000ef3f78, 0xc000ef3ee8, 0xc011e4aa00?, 0x0, 0x4020f40?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000ef3e98 sp=0xc000ef3d58 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc018dc65c0, {0x400d6b0?, 0xc017de12c0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc000ef3fb8 sp=0xc000ef3e98 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc000ef3fe0 sp=0xc000ef3fb8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000ef3fe8 sp=0xc000ef3fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 732 [select]:
   > runtime.gopark(0xc00090df50?, 0x4?, 0x4?, 0x30?, 0xc00090dd00?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00090db78 sp=0xc00090db58 pc=0x13bb516
   > runtime.selectgo(0xc00090df50, 0xc00090dcf8, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00090dcb8 sp=0xc00090db78 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).loadSchemaInLoop(0xc0106ea240, {0x400d608, 0xc0106c6e80}, 0x0?)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:565 +0x1aa fp=0xc00090dfb0 sp=0xc00090dcb8 pc=0x26a00aa
   > github.com/pingcap/tidb/domain.(*Domain).Init.func10()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:825 +0x32 fp=0xc00090dfe0 sp=0xc00090dfb0 pc=0x26a2b32
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00090dfe8 sp=0xc00090dfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:825 +0xdeb
   > goroutine 733 [select]:
   > runtime.gopark(0xc01037af78?, 0x3?, 0x4?, 0x30?, 0xc01037af12?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01037ad60 sp=0xc01037ad40 pc=0x13bb516
   > runtime.selectgo(0xc01037af78, 0xc01037af0c, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01037aea0 sp=0xc01037ad60 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).topNSlowQueryLoop(0xc0106ea240)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:455 +0x194 fp=0xc01037afc8 sp=0xc01037aea0 pc=0x269e914
   > github.com/pingcap/tidb/domain.(*Domain).Init.func11()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:828 +0x26 fp=0xc01037afe0 sp=0xc01037afc8 pc=0x26a2ac6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01037afe8 sp=0xc01037afe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:828 +0xe52
   > goroutine 734 [select]:
   > runtime.gopark(0xc000623ef8?, 0x3?, 0x4?, 0x30?, 0xc000623e82?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000623d08 sp=0xc000623ce8 pc=0x13bb516
   > runtime.selectgo(0xc000623ef8, 0xc000623e7c, 0xc00095a440?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000623e48 sp=0xc000623d08 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).infoSyncerKeeper(0xc0106ea240)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:487 +0x165 fp=0xc000623fc8 sp=0xc000623e48 pc=0x269ee45
   > github.com/pingcap/tidb/domain.(*Domain).Init.func12()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:829 +0x26 fp=0xc000623fe0 sp=0xc000623fc8 pc=0x26a2a66
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000623fe8 sp=0xc000623fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:829 +0xe95
   > goroutine 735 [select]:
   > runtime.gopark(0xc01037bef0?, 0x2?, 0x0?, 0x0?, 0xc01037bebc?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01037bd38 sp=0xc01037bd18 pc=0x13bb516
   > runtime.selectgo(0xc01037bef0, 0xc01037beb8, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01037be78 sp=0xc01037bd38 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).globalConfigSyncerKeeper(0xc0106ea240)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:510 +0xe5 fp=0xc01037bfc8 sp=0xc01037be78 pc=0x269f405
   > github.com/pingcap/tidb/domain.(*Domain).Init.func13()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:830 +0x26 fp=0xc01037bfe0 sp=0xc01037bfc8 pc=0x26a2a06
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01037bfe8 sp=0xc01037bfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:830 +0xedc
   > goroutine 736 [select]:
   > runtime.gopark(0xc000624e78?, 0x3?, 0x4?, 0x30?, 0xc000624df2?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000624c78 sp=0xc000624c58 pc=0x13bb516
   > runtime.selectgo(0xc000624e78, 0xc000624dec, 0xc000120000?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000624db8 sp=0xc000624c78 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).topologySyncerKeeper(0xc0106ea240)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:533 +0x165 fp=0xc000624fc8 sp=0xc000624db8 pc=0x269f8c5
   > github.com/pingcap/tidb/domain.(*Domain).Init.func14()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:834 +0x26 fp=0xc000624fe0 sp=0xc000624fc8 pc=0x26a29a6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000624fe8 sp=0xc000624fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:834 +0xf3d
   > goroutine 745 [select]:
   > runtime.gopark(0xc01a6e9e90?, 0x3?, 0x90?, 0xe0?, 0xc01a6e9e02?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01a6e9c70 sp=0xc01a6e9c50 pc=0x13bb516
   > runtime.selectgo(0xc01a6e9e90, 0xc01a6e9dfc, 0x3a8be78?, 0x0, 0x141f32a?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01a6e9db0 sp=0xc01a6e9c70 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).globalBindHandleWorkerLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1071 +0x16f fp=0xc01a6e9fe0 sp=0xc01a6e9db0 pc=0x26a476f
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01a6e9fe8 sp=0xc01a6e9fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).globalBindHandleWorkerLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1058 +0xad
   > goroutine 746 [select]:
   > runtime.gopark(0xc000ef4f28?, 0x2?, 0x4?, 0x30?, 0xc000ef4ed4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000ef4d48 sp=0xc000ef4d28 pc=0x13bb516
   > runtime.selectgo(0xc000ef4f28, 0xc000ef4ed0, 0xc0101b1000?, 0x0, 0xc010f58100?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000ef4e88 sp=0xc000ef4d48 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).handleEvolvePlanTasksLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1106 +0x107 fp=0xc000ef4fe0 sp=0xc000ef4e88 pc=0x26a4fe7
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000ef4fe8 sp=0xc000ef4fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).handleEvolvePlanTasksLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1099 +0xe5
   > goroutine 3369 [select]:
   > runtime.gopark(0xc0005abe10?, 0x2?, 0x90?, 0x80?, 0xc0005abd8c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0005abbe0 sp=0xc0005abbc0 pc=0x13bb516
   > runtime.selectgo(0xc0005abe10, 0xc0005abd88, 0x13bb516?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0005abd20 sp=0xc0005abbe0 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc010e858c0, 0x1, {0x5f8a1a8, 0x0, 0x0})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:441 +0x4f4 fp=0xc0005abf10 sp=0xc0005abd20 pc=0x30626b4
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:335 +0xb3 fp=0xc0005abf90 sp=0xc0005abf10 pc=0x30613d3
   > github.com/pingcap/tidb/util.WithRecovery(0xc013b40420?, 0x5?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc0005abfc0 sp=0xc0005abf90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x2a fp=0xc0005abfe0 sp=0xc0005abfc0 pc=0x30612ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0005abfe8 sp=0xc0005abfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x1c9
   > goroutine 827 [chan receive]:
   > runtime.gopark(0x3a8bf40?, 0xc000ef2cf8?, 0xfc?, 0xb?, 0xa?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000ef2cb0 sp=0xc000ef2c90 pc=0x13bb516
   > runtime.chanrecv(0xc00012ccc0, 0xc000ef2d78, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000ef2d40 sp=0xc000ef2cb0 pc=0x13854bb
   > runtime.chanrecv2(0xc000640a9c?, 0x2?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc000ef2d68 sp=0xc000ef2d40 pc=0x1384ff8
   > github.com/soheilhy/cmux.muxListener.Accept(...)
   > 	/go/pkg/mod/github.com/soheilhy/cmux@v0.1.4/cmux.go:229
   > github.com/soheilhy/cmux.(*muxListener).Accept(0x3ff0f40?)
   > 	<autogenerated>:1 +0x45 fp=0xc000ef2d98 sp=0xc000ef2d68 pc=0x2dc7625
   > google.golang.org/grpc.(*Server).Serve(0xc000981380, {0x400cb50, 0xc010f11158})
   > 	/go/pkg/mod/google.golang.org/grpc@v1.29.1/server.go:621 +0x362 fp=0xc000ef2eb0 sp=0xc000ef2d98 pc=0x19749a2
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer.func1()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:457 +0x3e fp=0xc000ef2f90 sp=0xc000ef2eb0 pc=0x31db01e
   > github.com/pingcap/tidb/util.WithRecovery(0x400d640?, 0xc00012c7e0?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc000ef2fc0 sp=0xc000ef2f90 pc=0x1ffabd3
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer.func5()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:456 +0x28 fp=0xc000ef2fe0 sp=0xc000ef2fc0 pc=0x31dafa8
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000ef2fe8 sp=0xc000ef2fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:456 +0x42c
   > goroutine 828 [chan receive]:
   > runtime.gopark(0x50?, 0xc00fb31080?, 0x8?, 0xd?, 0x138c1bf?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000ef0c80 sp=0xc000ef0c60 pc=0x13bb516
   > runtime.chanrecv(0xc00012cc00, 0xc000ef0d48, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000ef0d10 sp=0xc000ef0c80 pc=0x13854bb
   > runtime.chanrecv2(0x141e886?, 0xc00040fa40?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc000ef0d38 sp=0xc000ef0d10 pc=0x1384ff8
   > github.com/soheilhy/cmux.muxListener.Accept(...)
   > 	/go/pkg/mod/github.com/soheilhy/cmux@v0.1.4/cmux.go:229
   > github.com/soheilhy/cmux.(*muxListener).Accept(0x5828400?)
   > 	<autogenerated>:1 +0x45 fp=0xc000ef0d68 sp=0xc000ef0d38 pc=0x2dc7625
   > net/http.(*onceCloseListener).Accept(0x400d640?)
   > 	<autogenerated>:1 +0x2a fp=0xc000ef0d80 sp=0xc000ef0d68 pc=0x16e0c6a
   > net/http.(*Server).Serve(0xc010f432c0, {0x400cb50, 0xc010f11140})
   > 	/usr/local/go/src/net/http/server.go:3070 +0x385 fp=0xc000ef0eb0 sp=0xc000ef0d80 pc=0x16b6f45
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer.func2()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:462 +0x3e fp=0xc000ef0f90 sp=0xc000ef0eb0 pc=0x31dadbe
   > github.com/pingcap/tidb/util.WithRecovery(0x400d640?, 0xc000120008?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc000ef0fc0 sp=0xc000ef0f90 pc=0x1ffabd3
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer.func6()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:461 +0x28 fp=0xc000ef0fe0 sp=0xc000ef0fc0 pc=0x31dad48
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000ef0fe8 sp=0xc000ef0fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:461 +0x4ea
   > goroutine 61 [select]:
   > runtime.gopark(0xc01037c7a8?, 0x2?, 0x4?, 0x30?, 0xc01037c784?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01037c608 sp=0xc01037c5e8 pc=0x13bb516
   > runtime.selectgo(0xc01037c7a8, 0xc01037c780, 0xc00062ac60?, 0x0, 0xc01132ecc0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01037c748 sp=0xc01037c608 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).TelemetryRotateSubWindowLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1169 +0xcc fp=0xc01037c7e0 sp=0xc01037c748 pc=0x26a5c4c
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01037c7e8 sp=0xc01037c7e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).TelemetryRotateSubWindowLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1162 +0x8f
   > goroutine 62 [select]:
   > runtime.gopark(0xc01163bd48?, 0x2?, 0xe0?, 0xee?, 0xc01163bc94?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01163bb08 sp=0xc01163bae8 pc=0x13bb516
   > runtime.selectgo(0xc01163bd48, 0xc01163bc90, 0xc01a69fe30?, 0x0, 0x1?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01163bc48 sp=0xc01163bb08 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).loadStatsWorker(0xc0106ea240)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1304 +0x485 fp=0xc01163bfc8 sp=0xc01163bc48 pc=0x26a6ea5
   > github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1247 +0x26 fp=0xc01163bfe0 sp=0xc01163bfc8 pc=0x26a6666
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01163bfe8 sp=0xc01163bfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1247 +0x105
   > goroutine 63 [select]:
   > runtime.gopark(0xc000b99f28?, 0x6?, 0x0?, 0x0?, 0xc000b99bb4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000b99a20 sp=0xc000b99a00 pc=0x13bb516
   > runtime.selectgo(0xc000b99f28, 0xc000b99ba8, 0xc015a201c0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000b99b60 sp=0xc000b99a20 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).updateStatsWorker(0xc0106ea240, {0xc0106ea240?, 0x400d608?}, {0x401ea10, 0xc010592d20})
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1372 +0x234 fp=0xc000b99fa8 sp=0xc000b99b60 pc=0x26a7e54
   > github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop.func3()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1259 +0x36 fp=0xc000b99fe0 sp=0xc000b99fa8 pc=0x26a65b6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000b99fe8 sp=0xc000b99fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1259 +0x29a
   > goroutine 64 [select]:
   > runtime.gopark(0xc01a87bf78?, 0x2?, 0x4?, 0x30?, 0xc01a87bf4c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01a87bdd0 sp=0xc01a87bdb0 pc=0x13bb516
   > runtime.selectgo(0xc01a87bf78, 0xc01a87bf48, 0xc01a69fe30?, 0x0, 0x141d0d0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01a87bf10 sp=0xc01a87bdd0 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).autoAnalyzeWorker(0xc0106ea240, {0x401ea10, 0xc010592d20})
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1425 +0x105 fp=0xc01a87bfb8 sp=0xc01a87bf10 pc=0x26a8bc5
   > github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop.func4()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1262 +0x2e fp=0xc01a87bfe0 sp=0xc01a87bfb8 pc=0x26a654e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01a87bfe8 sp=0xc01a87bfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1262 +0x31a
   > goroutine 65 [select]:
   > runtime.gopark(0xc01037ffa8?, 0x2?, 0x4?, 0x30?, 0xc01037ff7c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01037fe00 sp=0xc01037fde0 pc=0x13bb516
   > runtime.selectgo(0xc01037ffa8, 0xc01037ff78, 0x0?, 0x0, 0x100000000000000?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01037ff40 sp=0xc01037fe00 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).PlanReplayerLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1191 +0xf6 fp=0xc01037ffe0 sp=0xc01037ff40 pc=0x26a5f36
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01037ffe8 sp=0xc01037ffe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).PlanReplayerLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1182 +0x6c
   > goroutine 850 [chan receive]:
   > runtime.gopark(0xc000ecc418?, 0xc0008bfa00?, 0x48?, 0xde?, 0x13d8de5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0005addf0 sp=0xc0005addd0 pc=0x13bb516
   > runtime.chanrecv(0xc00012c360, 0xc0005adf38, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc0005ade80 sp=0xc0005addf0 pc=0x13854bb
   > runtime.chanrecv2(0x9356907420000?, 0x0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc0005adea8 sp=0xc0005ade80 pc=0x1384ff8
   > github.com/pingcap/tidb/server.NewServer.func1()
   > 	/go/src/github.com/pingcap/tidb/server/server.go:209 +0x98 fp=0xc0005adfe0 sp=0xc0005adea8 pc=0x31e1638
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0005adfe8 sp=0xc0005adfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/server.NewServer
   > 	/go/src/github.com/pingcap/tidb/server/server.go:208 +0x32a
   > goroutine 851 [select]:
   > runtime.gopark(0xc010255eb0?, 0x2?, 0x1e?, 0x0?, 0xc010255e5c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010255cc8 sp=0xc010255ca8 pc=0x13bb516
   > runtime.selectgo(0xc010255eb0, 0xc010255e58, 0xc0104c6680?, 0x0, 0x2?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010255e08 sp=0xc010255cc8 pc=0x13cbbdc
   > github.com/pingcap/tidb/util/expensivequery.(*Handle).Run(0xc0104d14a0)
   > 	/go/src/github.com/pingcap/tidb/util/expensivequery/expensivequery.go:61 +0x198 fp=0xc010255fc8 sp=0xc010255e08 pc=0x2695d58
   > main.createServer.func1()
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:675 +0x26 fp=0xc010255fe0 sp=0xc010255fc8 pc=0x33b2be6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010255fe8 sp=0xc010255fe0 pc=0x13ee6e1
   > created by main.createServer
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:675 +0x439
   > goroutine 852 [select, locked to thread]:
   > runtime.gopark(0xc010f5f7a8?, 0x2?, 0x0?, 0x0?, 0xc010f5f7a4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010f5f618 sp=0xc010f5f5f8 pc=0x13bb516
   > runtime.selectgo(0xc010f5f7a8, 0xc010f5f7a0, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010f5f758 sp=0xc010f5f618 pc=0x13cbbdc
   > runtime.ensureSigM.func1()
   > 	/usr/local/go/src/runtime/signal_unix.go:995 +0x1b0 fp=0xc010f5f7e0 sp=0xc010f5f758 pc=0x13d0070
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010f5f7e8 sp=0xc010f5f7e0 pc=0x13ee6e1
   > created by runtime.ensureSigM
   > 	/usr/local/go/src/runtime/signal_unix.go:978 +0xbd
   > goroutine 853 [syscall]:
   > runtime.notetsleepg(0xc010f5c720?, 0xc010f5c7d0?)
   > 	/usr/local/go/src/runtime/lock_futex.go:236 +0x34 fp=0xc010f5c7a0 sp=0xc010f5c768 pc=0x138acd4
   > os/signal.signal_recv()
   > 	/usr/local/go/src/runtime/sigqueue.go:152 +0x2f fp=0xc010f5c7c0 sp=0xc010f5c7a0 pc=0x13ea6cf
   > os/signal.loop()
   > 	/usr/local/go/src/os/signal/signal_unix.go:23 +0x19 fp=0xc010f5c7e0 sp=0xc010f5c7c0 pc=0x2cac7f9
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010f5c7e8 sp=0xc010f5c7e0 pc=0x13ee6e1
   > created by os/signal.Notify.func1.1
   > 	/usr/local/go/src/os/signal/signal.go:151 +0x2a
   > goroutine 854 [chan receive]:
   > runtime.gopark(0x5f8be00?, 0xc010f5cf20?, 0x28?, 0xc3?, 0xc011329310?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010f5cea0 sp=0xc010f5ce80 pc=0x13bb516
   > runtime.chanrecv(0xc000680960, 0xc010f5cfa0, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc010f5cf30 sp=0xc010f5cea0 pc=0x13854bb
   > runtime.chanrecv1(0xc01132f0e0?, 0xc010f5cf10?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc010f5cf58 sp=0xc010f5cf30 pc=0x1384fb8
   > github.com/pingcap/tidb/util/signal.SetupSignalHandler.func1()
   > 	/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:37 +0x4f fp=0xc010f5cfe0 sp=0xc010f5cf58 pc=0x33ac32f
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010f5cfe8 sp=0xc010f5cfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/util/signal.SetupSignalHandler
   > 	/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:34 +0xb6
   > goroutine 806 [chan receive]:
   > runtime.gopark(0xc010c7a870?, 0xc0104c6680?, 0x0?, 0x0?, 0x4020720?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0005ace60 sp=0xc0005ace40 pc=0x13bb516
   > runtime.chanrecv(0xc0006809c0, 0xc0005acf80, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc0005acef0 sp=0xc0005ace60 pc=0x13854bb
   > runtime.chanrecv1(0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc0005acf18 sp=0xc0005acef0 pc=0x1384fb8
   > github.com/pingcap/tidb/util/signal.SetupSignalHandler.func2()
   > 	/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:53 +0x45 fp=0xc0005acfe0 sp=0xc0005acf18 pc=0x33ac105
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0005acfe8 sp=0xc0005acfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/util/signal.SetupSignalHandler
   > 	/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:52 +0x19f
   > goroutine 807 [select]:
   > runtime.gopark(0xc0005aef80?, 0x3?, 0x0?, 0x30?, 0xc0005aef3a?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0005aeda8 sp=0xc0005aed88 pc=0x13bb516
   > runtime.selectgo(0xc0005aef80, 0xc0005aef34, 0xc010c90b80?, 0x0, 0x2?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0005aeee8 sp=0xc0005aeda8 pc=0x13cbbdc
   > github.com/pingcap/tidb/util/topsql/reporter.(*RemoteTopSQLReporter).collectWorker(0xc000dabb90)
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:327 +0x13a fp=0xc0005aefc8 sp=0xc0005aeee8 pc=0x2547eda
   > github.com/pingcap/tidb/util/topsql/reporter.NewRemoteTopSQLReporter.func1()
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:160 +0x26 fp=0xc0005aefe0 sp=0xc0005aefc8 pc=0x2546c26
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0005aefe8 sp=0xc0005aefe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/util/topsql/reporter.NewRemoteTopSQLReporter
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:160 +0x1b6
   > goroutine 808 [select]:
   > runtime.gopark(0xc0004a6f40?, 0x2?, 0x60?, 0x53?, 0xc0004a6f04?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004a6d88 sp=0xc0004a6d68 pc=0x13bb516
   > runtime.selectgo(0xc0004a6f40, 0xc0004a6f00, 0x1ec360b?, 0x0, 0xc0004a6f10?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0004a6ec8 sp=0xc0004a6d88 pc=0x13cbbdc
   > github.com/pingcap/tidb/util/topsql/reporter.(*RemoteTopSQLReporter).reportWorker(0xc000dabb90)
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:499 +0x1ae fp=0xc0004a6fc8 sp=0xc0004a6ec8 pc=0x254924e
   > github.com/pingcap/tidb/util/topsql/reporter.NewRemoteTopSQLReporter.func2()
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:161 +0x26 fp=0xc0004a6fe0 sp=0xc0004a6fc8 pc=0x2546bc6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004a6fe8 sp=0xc0004a6fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/util/topsql/reporter.NewRemoteTopSQLReporter
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:161 +0x1f6
   > goroutine 809 [sleep]:
   > runtime.gopark(0x3fbe160bbc5b?, 0xc00062f040?, 0x88?, 0xd7?, 0x25412d5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004ad758 sp=0xc0004ad738 pc=0x13bb516
   > time.Sleep(0x3b9aca00)
   > 	/usr/local/go/src/runtime/time.go:195 +0x135 fp=0xc0004ad798 sp=0xc0004ad758 pc=0x13eaf15
   > github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).startCPUProfileWorker(0xc00055d800?)
   > 	/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:115 +0x65 fp=0xc0004ad7c8 sp=0xc0004ad798 pc=0x2540065
   > github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).Run.func1()
   > 	/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:93 +0x26 fp=0xc0004ad7e0 sp=0xc0004ad7c8 pc=0x253fea6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004ad7e8 sp=0xc0004ad7e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).Run
   > 	/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:93 +0xca
   > goroutine 810 [chan receive]:
   > runtime.gopark(0xc000adb520?, 0x58?, 0x68?, 0xa?, 0x60?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0004adde0 sp=0xc0004addc0 pc=0x13bb516
   > runtime.chanrecv(0xc0002f47e0, 0xc0004adf08, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc0004ade70 sp=0xc0004adde0 pc=0x13854bb
   > runtime.chanrecv1(0x0?, 0x1?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc0004ade98 sp=0xc0004ade70 pc=0x1384fb8
   > github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).startAnalyzeProfileWorker(0xc0009e61b0)
   > 	/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:142 +0x7c fp=0xc0004adfc8 sp=0xc0004ade98 pc=0x25402bc
   > github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).Run.func2()
   > 	/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:94 +0x26 fp=0xc0004adfe0 sp=0xc0004adfc8 pc=0x253fe46
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0004adfe8 sp=0xc0004adfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).Run
   > 	/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:94 +0x10a
   > goroutine 811 [IO wait]:
   > runtime.gopark(0xf?, 0xc011241930?, 0x2?, 0x0?, 0xc0006398d0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000639860 sp=0xc000639840 pc=0x13bb516
   > runtime.netpollblock(0x203004?, 0x11241930?, 0xc0?)
   > 	/usr/local/go/src/runtime/netpoll.go:526 +0xf7 fp=0xc000639898 sp=0xc000639860 pc=0x13b38f7
   > internal/poll.runtime_pollWait(0x7f71a7a28d90, 0x72)
   > 	/usr/local/go/src/runtime/netpoll.go:305 +0x89 fp=0xc0006398b8 sp=0xc000639898 pc=0x13e7d09
   > internal/poll.(*pollDesc).wait(0xc01130fc80?, 0xc000d946f0?, 0x0)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:84 +0x32 fp=0xc0006398e0 sp=0xc0006398b8 pc=0x1465192
   > internal/poll.(*pollDesc).waitRead(...)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:89
   > internal/poll.(*FD).Accept(0xc01130fc80)
   > 	/usr/local/go/src/internal/poll/fd_unix.go:614 +0x234 fp=0xc000639978 sp=0xc0006398e0 pc=0x146a594
   > net.(*netFD).accept(0xc01130fc80)
   > 	/usr/local/go/src/net/fd_unix.go:172 +0x35 fp=0xc000639a30 sp=0xc000639978 pc=0x1589055
   > net.(*TCPListener).accept(0xc010251560)
   > 	/usr/local/go/src/net/tcpsock_posix.go:142 +0x28 fp=0xc000639a60 sp=0xc000639a30 pc=0x15a5088
   > net.(*TCPListener).Accept(0xc010251560)
   > 	/usr/local/go/src/net/tcpsock.go:288 +0x3d fp=0xc000639a90 sp=0xc000639a60 pc=0x15a40fd
   > github.com/soheilhy/cmux.(*cMux).Serve(0xc0004f5680)
   > 	/go/pkg/mod/github.com/soheilhy/cmux@v0.1.4/cmux.go:162 +0xa9 fp=0xc000639b20 sp=0xc000639a90 pc=0x2dc5da9
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer(0xc0104c6680, 0xc010ecfd40)
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:466 +0x4f7 fp=0xc000639c90 sp=0xc000639b20 pc=0x31dab17
   > github.com/pingcap/tidb/server.(*Server).startHTTPServer(0xc0104c6680)
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:442 +0x15d0 fp=0xc000639fc8 sp=0xc000639c90 pc=0x31d9f10
   > github.com/pingcap/tidb/server.(*Server).startStatusHTTP.func1()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:62 +0x26 fp=0xc000639fe0 sp=0xc000639fc8 pc=0x31d65c6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000639fe8 sp=0xc000639fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/server.(*Server).startStatusHTTP
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:62 +0x56
   > goroutine 812 [IO wait]:
   > runtime.gopark(0x18?, 0xc00051c800?, 0x90?, 0x40?, 0xc000625b70?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000625b00 sp=0xc000625ae0 pc=0x13bb516
   > runtime.netpollblock(0x14?, 0x2432d05?, 0x0?)
   > 	/usr/local/go/src/runtime/netpoll.go:526 +0xf7 fp=0xc000625b38 sp=0xc000625b00 pc=0x13b38f7
   > internal/poll.runtime_pollWait(0x7f71a7a28f70, 0x72)
   > 	/usr/local/go/src/runtime/netpoll.go:305 +0x89 fp=0xc000625b58 sp=0xc000625b38 pc=0x13e7d09
   > internal/poll.(*pollDesc).wait(0xc01130fa80?, 0xc000625d20?, 0x0)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:84 +0x32 fp=0xc000625b80 sp=0xc000625b58 pc=0x1465192
   > internal/poll.(*pollDesc).waitRead(...)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:89
   > internal/poll.(*FD).Accept(0xc01130fa80)
   > 	/usr/local/go/src/internal/poll/fd_unix.go:614 +0x234 fp=0xc000625c18 sp=0xc000625b80 pc=0x146a594
   > net.(*netFD).accept(0xc01130fa80)
   > 	/usr/local/go/src/net/fd_unix.go:172 +0x35 fp=0xc000625cd0 sp=0xc000625c18 pc=0x1589055
   > net.(*TCPListener).accept(0xc010251548)
   > 	/usr/local/go/src/net/tcpsock_posix.go:142 +0x28 fp=0xc000625d00 sp=0xc000625cd0 pc=0x15a5088
   > net.(*TCPListener).Accept(0xc010251548)
   > 	/usr/local/go/src/net/tcpsock.go:288 +0x3d fp=0xc000625d30 sp=0xc000625d00 pc=0x15a40fd
   > github.com/pingcap/tidb/server.(*Server).startNetworkListener(0xc0104c6680, {0x400b9b0, 0xc010251548}, 0x0, 0x0?)
   > 	/go/src/github.com/pingcap/tidb/server/server.go:383 +0xa6 fp=0xc000625fa8 sp=0xc000625d30 pc=0x31e25a6
   > github.com/pingcap/tidb/server.(*Server).Run.func1()
   > 	/go/src/github.com/pingcap/tidb/server/server.go:368 +0x34 fp=0xc000625fe0 sp=0xc000625fa8 pc=0x31e24d4
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000625fe8 sp=0xc000625fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/server.(*Server).Run
   > 	/go/src/github.com/pingcap/tidb/server/server.go:368 +0x145
   > goroutine 813 [IO wait]:
   > runtime.gopark(0x0?, 0x0?, 0x0?, 0x0?, 0xc000626b78?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000626b08 sp=0xc000626ae8 pc=0x13bb516
   > runtime.netpollblock(0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/netpoll.go:526 +0xf7 fp=0xc000626b40 sp=0xc000626b08 pc=0x13b38f7
   > internal/poll.runtime_pollWait(0x7f71a7a28e80, 0x72)
   > 	/usr/local/go/src/runtime/netpoll.go:305 +0x89 fp=0xc000626b60 sp=0xc000626b40 pc=0x13e7d09
   > internal/poll.(*pollDesc).wait(0xc01130fb00?, 0x1?, 0x0)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:84 +0x32 fp=0xc000626b88 sp=0xc000626b60 pc=0x1465192
   > internal/poll.(*pollDesc).waitRead(...)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:89
   > internal/poll.(*FD).Accept(0xc01130fb00)
   > 	/usr/local/go/src/internal/poll/fd_unix.go:614 +0x234 fp=0xc000626c20 sp=0xc000626b88 pc=0x146a594
   > net.(*netFD).accept(0xc01130fb00)
   > 	/usr/local/go/src/net/fd_unix.go:172 +0x35 fp=0xc000626cd8 sp=0xc000626c20 pc=0x1589055
   > net.(*UnixListener).accept(0x0?)
   > 	/usr/local/go/src/net/unixsock_posix.go:166 +0x1c fp=0xc000626d00 sp=0xc000626cd8 pc=0x15aba1c
   > net.(*UnixListener).Accept(0xc000d833b0)
   > 	/usr/local/go/src/net/unixsock.go:260 +0x3d fp=0xc000626d30 sp=0xc000626d00 pc=0x15aa0bd
   > github.com/pingcap/tidb/server.(*Server).startNetworkListener(0xc0104c6680, {0x400b9e0, 0xc000d833b0}, 0x1, 0x0?)
   > 	/go/src/github.com/pingcap/tidb/server/server.go:383 +0xa6 fp=0xc000626fa8 sp=0xc000626d30 pc=0x31e25a6
   > github.com/pingcap/tidb/server.(*Server).Run.func2()
   > 	/go/src/github.com/pingcap/tidb/server/server.go:369 +0x37 fp=0xc000626fe0 sp=0xc000626fa8 pc=0x31e2477
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000626fe8 sp=0xc000626fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/server.(*Server).Run
   > 	/go/src/github.com/pingcap/tidb/server/server.go:369 +0x1db
   > goroutine 80 [select]:
   > runtime.gopark(0xc017222f78?, 0x2?, 0x1?, 0x11?, 0xc017222eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc017222d58 sp=0xc017222d38 pc=0x13bb516
   > runtime.selectgo(0xc017222f78, 0xc017222ee8, 0x3aac226?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc017222e98 sp=0xc017222d58 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc0186bff80, {0x400d6b0?, 0xc017de12c0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc017222fb8 sp=0xc017222e98 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc017222fe0 sp=0xc017222fb8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc017222fe8 sp=0xc017222fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 78 [select]:
   > runtime.gopark(0xc018045778?, 0x2?, 0x2?, 0x0?, 0xc0180456ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc018045558 sp=0xc018045538 pc=0x13bb516
   > runtime.selectgo(0xc018045778, 0xc0180456e8, 0x3aac226?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc018045698 sp=0xc018045558 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc0186bff00, {0x400d6b0?, 0xc017de12c0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc0180457b8 sp=0xc018045698 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc0180457e0 sp=0xc0180457b8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0180457e8 sp=0xc0180457e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 77 [select]:
   > runtime.gopark(0xc018043778?, 0x2?, 0x2?, 0x0?, 0xc0180436ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc018043558 sp=0xc018043538 pc=0x13bb516
   > runtime.selectgo(0xc018043778, 0xc0180436e8, 0x3aac226?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc018043698 sp=0xc018043558 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc0186bfec0, {0x400d6b0?, 0xc017de12c0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc0180437b8 sp=0xc018043698 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc0180437e0 sp=0xc0180437b8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0180437e8 sp=0xc0180437e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 3367 [select]:
   > runtime.gopark(0xc000d1ae30?, 0x2?, 0x80?, 0x57?, 0xc000d1ae1c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000d1aca8 sp=0xc000d1ac88 pc=0x13bb516
   > runtime.selectgo(0xc000d1ae30, 0xc000d1ae18, 0xc00fe38960?, 0x0, 0x2fef900?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000d1ade8 sp=0xc000d1aca8 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).wait4BuildSide(0xc010e858c0)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:242 +0x6f fp=0xc000d1ae60 sp=0xc000d1ade8 pc=0x30605ef
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchProbeSideChunks(0xc010e858c0, {0x400d6b0, 0xc017de12c0})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:221 +0x233 fp=0xc000d1af28 sp=0xc000d1ae60 pc=0x3060333
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:322 +0x8f fp=0xc000d1af90 sp=0xc000d1af28 pc=0x306156f
   > github.com/pingcap/tidb/util.WithRecovery(0x400d6b0?, 0xc0175e6ff0?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc000d1afc0 sp=0xc000d1af90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func3()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:320 +0x2a fp=0xc000d1afe0 sp=0xc000d1afc0 pc=0x30614aa
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000d1afe8 sp=0xc000d1afe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:320 +0x14f
   > goroutine 3373 [semacquire]:
   > runtime.gopark(0xc0135b9d70?, 0x2?, 0x0?, 0xd2?, 0xc00ff7d5a0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0135b9e78 sp=0xc0135b9e58 pc=0x13bb516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc010e85ab8, 0x0?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc0135b9ee0 sp=0xc0135b9e78 pc=0x13cce5e
   > sync.runtime_Semacquire(0xc010e85b00?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc0135b9f10 sp=0xc0135b9ee0 pc=0x13e9f65
   > sync.(*WaitGroup).Wait(0x10000c01803a201?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc0135b9f38 sp=0xc0135b9f10 pc=0x13fd1f2
   > github.com/pingcap/tidb/executor.(*HashJoinExec).waitJoinWorkersAndCloseResultChan(0xc010e858c0)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:395 +0x33 fp=0xc0135b9f78 sp=0xc0135b9f38 pc=0x3061fb3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).waitJoinWorkersAndCloseResultChan-fm()
   > 	<autogenerated>:1 +0x26 fp=0xc0135b9f90 sp=0xc0135b9f78 pc=0x31277c6
   > github.com/pingcap/tidb/util.WithRecovery(0x2?, 0xc0135b9d38?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc0135b9fc0 sp=0xc0135b9f90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:338 +0x28 fp=0xc0135b9fe0 sp=0xc0135b9fc0 pc=0x3061288
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0135b9fe8 sp=0xc0135b9fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:338 +0x3b8
   > goroutine 5204 [select]:
   > runtime.gopark(0xc018043f78?, 0x2?, 0x2?, 0x0?, 0xc018043eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc018043d58 sp=0xc018043d38 pc=0x13bb516
   > runtime.selectgo(0xc018043f78, 0xc018043ee8, 0x3aac226?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc018043e98 sp=0xc018043d58 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc018dc66c0, {0x400d6b0?, 0xc017de12c0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc018043fb8 sp=0xc018043e98 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc018043fe0 sp=0xc018043fb8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc018043fe8 sp=0xc018043fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 3372 [select]:
   > runtime.gopark(0xc011f1b610?, 0x2?, 0xc0?, 0x80?, 0xc011f1b58c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc011f1b3e0 sp=0xc011f1b3c0 pc=0x13bb516
   > runtime.selectgo(0xc011f1b610, 0xc011f1b588, 0x13bb516?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc011f1b520 sp=0xc011f1b3e0 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc010e858c0, 0x4, {0x5f8a1a8, 0x0, 0x0})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:441 +0x4f4 fp=0xc011f1b710 sp=0xc011f1b520 pc=0x30626b4
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:335 +0xb3 fp=0xc011f1b790 sp=0xc011f1b710 pc=0x30613d3
   > github.com/pingcap/tidb/util.WithRecovery(0xc013b40420?, 0x5?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc011f1b7c0 sp=0xc011f1b790 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x2a fp=0xc011f1b7e0 sp=0xc011f1b7c0 pc=0x30612ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc011f1b7e8 sp=0xc011f1b7e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x1c9
   > goroutine 3371 [select]:
   > runtime.gopark(0xc011f14610?, 0x2?, 0xb0?, 0x80?, 0xc011f1458c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc011f143e0 sp=0xc011f143c0 pc=0x13bb516
   > runtime.selectgo(0xc011f14610, 0xc011f14588, 0x13bb516?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc011f14520 sp=0xc011f143e0 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc010e858c0, 0x3, {0x5f8a1a8, 0x0, 0x0})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:441 +0x4f4 fp=0xc011f14710 sp=0xc011f14520 pc=0x30626b4
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:335 +0xb3 fp=0xc011f14790 sp=0xc011f14710 pc=0x30613d3
   > github.com/pingcap/tidb/util.WithRecovery(0xc013b40420?, 0x5?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc011f147c0 sp=0xc011f14790 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x2a fp=0xc011f147e0 sp=0xc011f147c0 pc=0x30612ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc011f147e8 sp=0xc011f147e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x1c9
   > goroutine 76 [select]:
   > runtime.gopark(0xc00fe55f78?, 0x2?, 0xa0?, 0x5d?, 0xc00fe55eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fe55d58 sp=0xc00fe55d38 pc=0x13bb516
   > runtime.selectgo(0xc00fe55f78, 0xc00fe55ee8, 0xc011e4aa00?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fe55e98 sp=0xc00fe55d58 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc0186bfe80, {0x400d6b0?, 0xc017de12c0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc00fe55fb8 sp=0xc00fe55e98 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc00fe55fe0 sp=0xc00fe55fb8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fe55fe8 sp=0xc00fe55fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 5202 [select]:
   > runtime.gopark(0xc01721f778?, 0x2?, 0xc7?, 0xb5?, 0xc01721f6ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01721f558 sp=0xc01721f538 pc=0x13bb516
   > runtime.selectgo(0xc01721f778, 0xc01721f6e8, 0x3aac226?, 0x0, 0xc011572078?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01721f698 sp=0xc01721f558 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc018dc6640, {0x400d6b0?, 0xc017de12c0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc01721f7b8 sp=0xc01721f698 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc01721f7e0 sp=0xc01721f7b8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01721f7e8 sp=0xc01721f7e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 3368 [select]:
   > runtime.gopark(0xc018044610?, 0x2?, 0x80?, 0x80?, 0xc01804458c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0180443e0 sp=0xc0180443c0 pc=0x13bb516
   > runtime.selectgo(0xc018044610, 0xc018044588, 0xc010a72000?, 0x0, 0xc000950e90?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc018044520 sp=0xc0180443e0 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc010e858c0, 0x0, {0x5f8a1a8, 0x0, 0x0})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:441 +0x4f4 fp=0xc018044710 sp=0xc018044520 pc=0x30626b4
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:335 +0xb3 fp=0xc018044790 sp=0xc018044710 pc=0x30613d3
   > github.com/pingcap/tidb/util.WithRecovery(0xc01011ec00?, 0x5f55780?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc0180447c0 sp=0xc018044790 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x2a fp=0xc0180447e0 sp=0xc0180447c0 pc=0x30612ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0180447e8 sp=0xc0180447e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x1c9
   > goroutine 3370 [select]:
   > runtime.gopark(0xc01803ee10?, 0x2?, 0xa0?, 0x80?, 0xc01803ed8c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01803ebe0 sp=0xc01803ebc0 pc=0x13bb516
   > runtime.selectgo(0xc01803ee10, 0xc01803ed88, 0x13bb516?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01803ed20 sp=0xc01803ebe0 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc010e858c0, 0x2, {0x5f8a1a8, 0x0, 0x0})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:441 +0x4f4 fp=0xc01803ef10 sp=0xc01803ed20 pc=0x30626b4
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:335 +0xb3 fp=0xc01803ef90 sp=0xc01803ef10 pc=0x30613d3
   > github.com/pingcap/tidb/util.WithRecovery(0xc013b40420?, 0x5?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc01803efc0 sp=0xc01803ef90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x2a fp=0xc01803efe0 sp=0xc01803efc0 pc=0x30612ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01803efe8 sp=0xc01803efe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x1c9
   > goroutine 5185 [select]:
   > runtime.gopark(0xc013cba778?, 0x2?, 0x0?, 0xc8?, 0xc013cba6ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc013cba558 sp=0xc013cba538 pc=0x13bb516
   > runtime.selectgo(0xc013cba778, 0xc013cba6e8, 0x3aac226?, 0x0, 0x4020f40?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc013cba698 sp=0xc013cba558 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc018dc6600, {0x400d6b0?, 0xc017de12c0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc013cba7b8 sp=0xc013cba698 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc013cba7e0 sp=0xc013cba7b8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc013cba7e8 sp=0xc013cba7e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 5203 [select]:
   > runtime.gopark(0xc013cbb778?, 0x2?, 0x8?, 0x0?, 0xc013cbb6ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc013cbb558 sp=0xc013cbb538 pc=0x13bb516
   > runtime.selectgo(0xc013cbb778, 0xc013cbb6e8, 0x3aac226?, 0x0, 0xc01068f4a0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc013cbb698 sp=0xc013cbb558 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc018dc6680, {0x400d6b0?, 0xc017de12c0?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc013cbb7b8 sp=0xc013cbb698 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc013cbb7e0 sp=0xc013cbb7b8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc013cbb7e8 sp=0xc013cbb7e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 3365 [chan receive]:
   > runtime.gopark(0x13c37d1?, 0xc000d1e9d0?, 0x0?, 0x38?, 0xc01a7b6e80?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000d1e9c0 sp=0xc000d1e9a0 pc=0x13bb516
   > runtime.chanrecv(0xc00fe38ba0, 0xc000d1eb10, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000d1ea50 sp=0xc000d1e9c0 pc=0x13854bb
   > runtime.chanrecv2(0xc010e858c0?, 0x400d6b0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc000d1ea78 sp=0xc000d1ea50 pc=0x1384ff8
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Next(0xc010e858c0, {0x400d6b0?, 0xc017de12c0?}, 0xc01120a3c0)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:681 +0x652 fp=0xc000d1eb38 sp=0xc000d1ea78 pc=0x3064d52
   > github.com/pingcap/tidb/executor.Next({0x400d6b0, 0xc017de12c0}, {0x40101a0, 0xc010e858c0}, 0xc01120a3c0)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:286 +0x4a8 fp=0xc000d1ec78 sp=0xc000d1eb38 pc=0x2fef688
   > github.com/pingcap/tidb/executor.(*ProjectionExec).unParallelExecute(0xc01112d680, {0x400d6b0?, 0xc017de12c0?}, 0xc00fe2c370)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:194 +0xb8 fp=0xc000d1ecc8 sp=0xc000d1ec78 pc=0x3098758
   > github.com/pingcap/tidb/executor.(*ProjectionExec).Next(0xc01112d680, {0x400d6b0, 0xc017de12c0}, 0xc018f83110?)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:180 +0x5a fp=0xc000d1ed00 sp=0xc000d1ecc8 pc=0x309861a
   > github.com/pingcap/tidb/executor.Next({0x400d6b0, 0xc017de12c0}, {0x4010760, 0xc01112d680}, 0xc00fe2c370)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:286 +0x4a8 fp=0xc000d1ee40 sp=0xc000d1ed00 pc=0x2fef688
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchBuildSideRows(0xc010e85b00, {0x400d6b0, 0xc017de12c0}, 0xc00fe38600, 0xc0178614a0)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:266 +0x1a5 fp=0xc000d1ef10 sp=0xc000d1ee40 pc=0x3060845
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:715 +0xab fp=0xc000d1ef90 sp=0xc000d1ef10 pc=0x306572b
   > github.com/pingcap/tidb/util.WithRecovery(0x5f539a0?, 0xc011a797b8?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc000d1efc0 sp=0xc000d1ef90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:712 +0x2a fp=0xc000d1efe0 sp=0xc000d1efc0 pc=0x306558a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000d1efe8 sp=0xc000d1efe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:712 +0x22d
   > goroutine 5322 [chan receive]:
   > runtime.gopark(0x35182e0?, 0xc01871f7af?, 0x50?, 0x19?, 0xc01871f720?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01871f6e0 sp=0xc01871f6c0 pc=0x13bb516
   > runtime.chanrecv(0xc000d018f0, 0xc01871f7af, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc01871f770 sp=0xc01871f6e0 pc=0x13854bb
   > runtime.chanrecv2(0xc0115c7e00?, 0x13c2505?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc01871f798 sp=0xc01871f770 pc=0x1384ff8
   > gopkg.in/natefinch/lumberjack%2ev2.(*Logger).millRun(0xc000ed07e0)
   > 	/go/pkg/mod/gopkg.in/natefinch/lumberjack.v2@v2.0.0/lumberjack.go:379 +0x45 fp=0xc01871f7c8 sp=0xc01871f798 pc=0x17361e5
   > gopkg.in/natefinch/lumberjack%2ev2.(*Logger).mill.func1.1()
   > 	/go/pkg/mod/gopkg.in/natefinch/lumberjack.v2@v2.0.0/lumberjack.go:390 +0x26 fp=0xc01871f7e0 sp=0xc01871f7c8 pc=0x17363a6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01871f7e8 sp=0xc01871f7e0 pc=0x13ee6e1
   > created by gopkg.in/natefinch/lumberjack%2ev2.(*Logger).mill.func1
   > 	/go/pkg/mod/gopkg.in/natefinch/lumberjack.v2@v2.0.0/lumberjack.go:390 +0x96
   > goroutine 5140 [chan receive]:
   > runtime.gopark(0xc0108e14a0?, 0xc00fe386c0?, 0x3?, 0x0?, 0xc000d1dcf8?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000d1dca8 sp=0xc000d1dc88 pc=0x13bb516
   > runtime.chanrecv(0xc00fe38600, 0xc000d1de08, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000d1dd38 sp=0xc000d1dca8 pc=0x13854bb
   > runtime.chanrecv2(0xc010afe7b0?, 0x4012e60?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc000d1dd60 sp=0xc000d1dd38 pc=0x1384ff8
   > github.com/pingcap/tidb/executor.(*HashJoinExec).buildHashTableForList(0xc010e85b00, 0x1?)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:762 +0x2d6 fp=0xc000d1de78 sp=0xc000d1dd60 pc=0x3065af6
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable(0xc010e85b00, {0x400d6b0?, 0xc017de12c0})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:726 +0x23f fp=0xc000d1df28 sp=0xc000d1de78 pc=0x30653ff
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Next.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:671 +0x8f fp=0xc000d1df90 sp=0xc000d1df28 pc=0x306504f
   > github.com/pingcap/tidb/util.WithRecovery(0x400d6b0?, 0xc0175e6ff0?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc000d1dfc0 sp=0xc000d1df90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Next.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:669 +0x2a fp=0xc000d1dfe0 sp=0xc000d1dfc0 pc=0x3064f8a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000d1dfe8 sp=0xc000d1dfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).Next
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:669 +0x5b2
   > goroutine 5105 [chan receive]:
   > runtime.gopark(0x82d86c405?, 0x0?, 0x80?, 0xee?, 0x138c1bf?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010d8edf8 sp=0xc010d8edd8 pc=0x13bb516
   > runtime.chanrecv(0xc0112145a0, 0xc010d8ef38, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc010d8ee88 sp=0xc010d8edf8 pc=0x13854bb
   > runtime.chanrecv2(0xc010e85d00?, 0x35182e0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc010d8eeb0 sp=0xc010d8ee88 pc=0x1384ff8
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Close(0xc010e85b00)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:123 +0x385 fp=0xc010d8ef58 sp=0xc010d8eeb0 pc=0x305fcc5
   > github.com/pingcap/tidb/executor.(*baseExecutor).Close(0xc0199b1368?)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:181 +0x7c fp=0xc010d8ef98 sp=0xc010d8ef58 pc=0x2feeadc
   > github.com/pingcap/tidb/executor.(*ProjectionExec).Close(0xc01112d7a0)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:329 +0x1cf fp=0xc010d8f000 sp=0xc010d8ef98 pc=0x30997af
   > github.com/pingcap/tidb/executor.(*recordSet).Close(0xc01120ac80)
   > 	/go/src/github.com/pingcap/tidb/executor/adapter.go:176 +0x2a fp=0xc010d8f040 sp=0xc010d8f000 pc=0x2f612ca
   > github.com/pingcap/tidb/session.(*execStmtResult).Close(0xc0199cc480)
   > 	/go/src/github.com/pingcap/tidb/session/session.go:1734 +0x36 fp=0xc010d8f090 sp=0xc010d8f040 pc=0x314b676
   > github.com/pingcap/tidb/server.(*tidbResultSet).Close(0x1c42fc540?)
   > 	/go/src/github.com/pingcap/tidb/server/driver_tidb.go:324 +0x3c fp=0xc010d8f0b0 sp=0xc010d8f090 pc=0x31c611c
   > github.com/pingcap/tidb/server.ResultSet.Close-fm()
   > 	<autogenerated>:1 +0x2b fp=0xc010d8f0c8 sp=0xc010d8f0b0 pc=0x31f7acb
   > github.com/pingcap/tidb/parser/terror.Call(0xc010d8f1d8?)
   > 	/go/src/github.com/pingcap/tidb/parser/terror/terror.go:298 +0x31 fp=0xc010d8f208 sp=0xc010d8f0c8 pc=0x1b74a51
   > github.com/pingcap/tidb/server.(*clientConn).handleStmt.func1()
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:1911 +0x26 fp=0xc010d8f220 sp=0xc010d8f208 pc=0x31bbd26
   > github.com/pingcap/tidb/server.(*clientConn).handleStmt(0xc010b34b40, {0x400d608, 0xc0168d6140}, {0x401fff0, 0xc019ca54a0}, {0x5f8a1a8, 0x0, 0x0}, 0x1)
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:1934 +0x413 fp=0xc010d8f2f0 sp=0xc010d8f220 pc=0x31bbaf3
   > github.com/pingcap/tidb/server.(*clientConn).handleQuery(0xc010b34b40, {0x400d608, 0xc0168d6140}, {0xc01012e821, 0x18c})
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:1775 +0x774 fp=0xc010d8f468 sp=0xc010d8f2f0 pc=0x31ba494
   > github.com/pingcap/tidb/server.(*clientConn).dispatch(0xc010b34b40, {0x400d6b0, 0xc0176240f0?}, {0xc01012e820, 0x18d, 0x18d})
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:1279 +0x1025 fp=0xc010d8f858 sp=0xc010d8f468 pc=0x31b6045
   > github.com/pingcap/tidb/server.(*clientConn).Run(0xc010b34b40, {0x400d6b0, 0xc0176240f0})
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:1034 +0x253 fp=0xc010d8fe18 sp=0xc010d8f858 pc=0x31b2b33
   > github.com/pingcap/tidb/server.(*Server).onConn(0xc0104c6680, 0xc010b34b40)
   > 	/go/src/github.com/pingcap/tidb/server/server.go:550 +0x6c5 fp=0xc010d8ffc0 sp=0xc010d8fe18 pc=0x31e4165
   > github.com/pingcap/tidb/server.(*Server).startNetworkListener.func2()
   > 	/go/src/github.com/pingcap/tidb/server/server.go:453 +0x2a fp=0xc010d8ffe0 sp=0xc010d8ffc0 pc=0x31e300a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010d8ffe8 sp=0xc010d8ffe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/server.(*Server).startNetworkListener
   > 	/go/src/github.com/pingcap/tidb/server/server.go:453 +0x5ca
