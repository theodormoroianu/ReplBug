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
     - Output: Error: 2013 (HY000): Lost connection to MySQL server during query

 * Container logs:
   > [2024/06/06 10:01:07.115 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=26] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/06/06 10:01:07.116 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=26] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/06/06 10:01:07.117 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:54, Type:create schema, State:none, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-06 10:01:07.116 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/06 10:01:07.117 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:54, Type:create schema, State:none, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-06 10:01:07.116 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/06 10:01:07.117 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:54, Type:create schema, State:none, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-06 10:01:07.116 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/06 10:01:07.118 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=26] [neededSchemaVersion=27] ["start time"=98.966µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/06 10:01:07.120 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=27] ["take time"=2.237459ms] [job="ID:54, Type:create schema, State:done, SchemaState:public, SchemaID:53, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-06 10:01:07.116 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/06 10:01:07.120 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:54, Type:create schema, State:synced, SchemaState:public, SchemaID:53, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-06 10:01:07.116 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/06 10:01:07.121 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=54]
   > [2024/06/06 10:01:07.121 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/06 10:01:07.127 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=27] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_037irb`\n--\n\nDROP TABLE IF EXISTS `t_037irb`;"] [user=root@127.0.0.1]
   > [2024/06/06 10:01:07.128 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=27] [cur_db=testdb] [sql="CREATE TABLE `t_037irb` (\n  `c_nrh3o` int(11) DEFAULT NULL,\n  `c_nfauxb` text DEFAULT NULL,\n  `c_y5n4c` int(11) DEFAULT NULL,\n  `c_j9alg` double NOT NULL,\n  `c_4vix1d` text DEFAULT NULL,\n  `c_glkxdb` text DEFAULT NULL,\n  `c_2ykt0d` int(11) DEFAULT NULL,\n  `c_5fxv3c` double DEFAULT NULL,\n  PRIMARY KEY (`c_j9alg`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/06/06 10:01:07.130 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:56, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:55, RowCount:0, ArgLen:1, start time: 2024-06-06 10:01:07.129 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/06 10:01:07.130 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:56, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:55, RowCount:0, ArgLen:1, start time: 2024-06-06 10:01:07.129 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_037irb` (\n  `c_nrh3o` int(11) DEFAULT NULL,\n  `c_nfauxb` text DEFAULT NULL,\n  `c_y5n4c` int(11) DEFAULT NULL,\n  `c_j9alg` double NOT NULL,\n  `c_4vix1d` text DEFAULT NULL,\n  `c_glkxdb` text DEFAULT NULL,\n  `c_2ykt0d` int(11) DEFAULT NULL,\n  `c_5fxv3c` double DEFAULT NULL,\n  PRIMARY KEY (`c_j9alg`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/06 10:01:07.130 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:56, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:55, RowCount:0, ArgLen:0, start time: 2024-06-06 10:01:07.129 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/06 10:01:07.132 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=27] [neededSchemaVersion=28] ["start time"=292.429µs] [phyTblIDs="[55]"] [actionTypes="[8]"]
   > [2024/06/06 10:01:07.134 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=28] ["take time"=2.089743ms] [job="ID:56, Type:create table, State:done, SchemaState:public, SchemaID:53, TableID:55, RowCount:0, ArgLen:1, start time: 2024-06-06 10:01:07.129 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/06 10:01:07.134 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:56, Type:create table, State:synced, SchemaState:public, SchemaID:53, TableID:55, RowCount:0, ArgLen:0, start time: 2024-06-06 10:01:07.129 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/06 10:01:07.135 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=56]
   > [2024/06/06 10:01:07.135 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/06 10:01:07.135 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=50] ["first split key"=748000000000000037]
   > [2024/06/06 10:01:07.136 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=28] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_037irb` DISABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/06/06 10:01:07.136 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=50] ["first at"=748000000000000037] ["first new region left"="{Id:50 StartKey:7480000000000000ff3300000000000000f8 EndKey:7480000000000000ff3700000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:51 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/06 10:01:07.136 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[50]"]
   > [2024/06/06 10:01:07.136 +00:00] [WARN] [2pc.go:1598] ["schemaLeaseChecker is not set for this transaction"] [sessionID=5] [startTS=450276377791299586] [commitTS=450276377791299588]
   > [2024/06/06 10:01:07.138 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=28] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_037irb` ENABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/06/06 10:01:07.138 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=28] [cur_db=testdb] [sql="\n--\n-- Temporary view structure for view `t_cpsvpb`\n--\n\nDROP TABLE IF EXISTS `t_cpsvpb`;"] [user=root@127.0.0.1]
   > [2024/06/06 10:01:07.138 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=28] [cur_db=testdb] [sql="/*!50001 DROP VIEW IF EXISTS `t_cpsvpb`*/;"] [user=root@127.0.0.1]
   > [2024/06/06 10:01:07.140 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:58, Type:create view, State:none, SchemaState:queueing, SchemaID:53, TableID:57, RowCount:0, ArgLen:3, start time: 2024-06-06 10:01:07.139 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/06 10:01:07.140 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:58, Type:create view, State:none, SchemaState:queueing, SchemaID:53, TableID:57, RowCount:0, ArgLen:3, start time: 2024-06-06 10:01:07.139 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="/*!50001 CREATE VIEW `t_cpsvpb` AS SELECT \n 1 AS `c0`,\n 1 AS `c2`,\n 1 AS `c3`,\n 1 AS `c4`,\n 1 AS `c5`,\n 1 AS `c6`,\n 1 AS `c7`,\n 1 AS `c8`,\n 1 AS `c9`,\n 1 AS `c10`,\n 1 AS `c11`,\n 1 AS `c12`,\n 1 AS `c13`,\n 1 AS `c14`*/;"]
   > [2024/06/06 10:01:07.140 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:58, Type:create view, State:none, SchemaState:queueing, SchemaID:53, TableID:57, RowCount:0, ArgLen:0, start time: 2024-06-06 10:01:07.139 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/06 10:01:07.142 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=28] [neededSchemaVersion=29] ["start time"=368.626µs] [phyTblIDs="[57]"] [actionTypes="[2097152]"]
   > [2024/06/06 10:01:07.144 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=29] ["take time"=2.26295ms] [job="ID:58, Type:create view, State:done, SchemaState:public, SchemaID:53, TableID:57, RowCount:0, ArgLen:3, start time: 2024-06-06 10:01:07.139 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/06 10:01:07.146 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:58, Type:create view, State:synced, SchemaState:public, SchemaID:53, TableID:57, RowCount:0, ArgLen:0, start time: 2024-06-06 10:01:07.139 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/06 10:01:07.147 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=58]
   > [2024/06/06 10:01:07.147 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/06 10:01:07.147 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=29] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_x7zqmd`\n--\n\nDROP TABLE IF EXISTS `t_x7zqmd`;"] [user=root@127.0.0.1]
   > [2024/06/06 10:01:07.148 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=29] [cur_db=testdb] [sql="CREATE TABLE `t_x7zqmd` (\n  `c_8weeq` int(11) NOT NULL,\n  `c_13sfid` double DEFAULT NULL,\n  `c_hhjlmc` text DEFAULT NULL,\n  `c_3b1zld` int(11) DEFAULT NULL,\n  `c_6tu8wd` int(11) DEFAULT NULL,\n  `c_jyc_cd` double DEFAULT NULL,\n  PRIMARY KEY (`c_8weeq`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/06/06 10:01:07.149 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:60, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:59, RowCount:0, ArgLen:1, start time: 2024-06-06 10:01:07.148 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/06 10:01:07.149 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:60, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:59, RowCount:0, ArgLen:1, start time: 2024-06-06 10:01:07.148 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_x7zqmd` (\n  `c_8weeq` int(11) NOT NULL,\n  `c_13sfid` double DEFAULT NULL,\n  `c_hhjlmc` text DEFAULT NULL,\n  `c_3b1zld` int(11) DEFAULT NULL,\n  `c_6tu8wd` int(11) DEFAULT NULL,\n  `c_jyc_cd` double DEFAULT NULL,\n  PRIMARY KEY (`c_8weeq`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/06 10:01:07.149 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:60, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:59, RowCount:0, ArgLen:0, start time: 2024-06-06 10:01:07.148 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/06 10:01:07.151 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=29] [neededSchemaVersion=30] ["start time"=335.731µs] [phyTblIDs="[59]"] [actionTypes="[8]"]
   > [2024/06/06 10:01:07.152 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=30] ["take time"=2.053983ms] [job="ID:60, Type:create table, State:done, SchemaState:public, SchemaID:53, TableID:59, RowCount:0, ArgLen:1, start time: 2024-06-06 10:01:07.148 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/06 10:01:07.154 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:60, Type:create table, State:synced, SchemaState:public, SchemaID:53, TableID:59, RowCount:0, ArgLen:0, start time: 2024-06-06 10:01:07.148 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/06 10:01:07.155 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=60]
   > [2024/06/06 10:01:07.155 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/06 10:01:07.155 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=52] ["first split key"=74800000000000003b]
   > [2024/06/06 10:01:07.156 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=52] ["first at"=74800000000000003b] ["first new region left"="{Id:52 StartKey:7480000000000000ff3700000000000000f8 EndKey:7480000000000000ff3b00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:53 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/06 10:01:07.156 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[52]"]
   > [2024/06/06 10:01:07.156 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=30] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_x7zqmd` DISABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/06/06 10:01:07.159 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=30] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_x7zqmd` ENABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/06/06 10:01:07.159 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=30] [cur_db=testdb] [sql="\n--\n-- Final view structure for view `t_cpsvpb`\n--\n\n/*!50001 DROP VIEW IF EXISTS `t_cpsvpb`*/;"] [user=root@127.0.0.1]
   > [2024/06/06 10:01:07.160 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:61, Type:drop view, State:none, SchemaState:queueing, SchemaID:53, TableID:57, RowCount:0, ArgLen:0, start time: 2024-06-06 10:01:07.16 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/06 10:01:07.160 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:61, Type:drop view, State:none, SchemaState:queueing, SchemaID:53, TableID:57, RowCount:0, ArgLen:0, start time: 2024-06-06 10:01:07.16 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="\n--\n-- Final view structure for view `t_cpsvpb`\n--\n\n/*!50001 DROP VIEW IF EXISTS `t_cpsvpb`*/;"]
   > [2024/06/06 10:01:07.161 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:61, Type:drop view, State:none, SchemaState:queueing, SchemaID:53, TableID:57, RowCount:0, ArgLen:0, start time: 2024-06-06 10:01:07.16 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/06 10:01:07.163 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=30] [neededSchemaVersion=31] ["start time"=202.402µs] [phyTblIDs="[57]"] [actionTypes="[16777216]"]
   > [2024/06/06 10:01:07.165 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=31] ["take time"=2.287256ms] [job="ID:61, Type:drop view, State:running, SchemaState:write only, SchemaID:53, TableID:57, RowCount:0, ArgLen:0, start time: 2024-06-06 10:01:07.16 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/06 10:01:07.165 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:61, Type:drop view, State:running, SchemaState:write only, SchemaID:53, TableID:57, RowCount:0, ArgLen:0, start time: 2024-06-06 10:01:07.16 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/06 10:01:07.166 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=31] [neededSchemaVersion=32] ["start time"=113.493µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/06 10:01:07.169 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=32] ["take time"=2.722232ms] [job="ID:61, Type:drop view, State:running, SchemaState:delete only, SchemaID:53, TableID:57, RowCount:0, ArgLen:0, start time: 2024-06-06 10:01:07.16 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/06 10:01:07.170 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:61, Type:drop view, State:running, SchemaState:delete only, SchemaID:53, TableID:57, RowCount:0, ArgLen:0, start time: 2024-06-06 10:01:07.16 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/06 10:01:07.172 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=32] [neededSchemaVersion=33] ["start time"=123.621µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/06 10:01:07.174 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=33] ["take time"=2.245351ms] [job="ID:61, Type:drop view, State:done, SchemaState:queueing, SchemaID:53, TableID:57, RowCount:0, ArgLen:2, start time: 2024-06-06 10:01:07.16 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/06 10:01:07.175 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:61, Type:drop view, State:synced, SchemaState:queueing, SchemaID:53, TableID:57, RowCount:0, ArgLen:0, start time: 2024-06-06 10:01:07.16 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/06 10:01:07.176 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=61]
   > [2024/06/06 10:01:07.176 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/06 10:01:07.182 +00:00] [INFO] [session.go:2203] ["Try to create a new txn inside a transaction auto commit"] [conn=5] [schemaVersion=33] [txnStartTS=450276377802309632] [txnScope=global]
   > [2024/06/06 10:01:07.184 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:63, Type:create view, State:none, SchemaState:queueing, SchemaID:53, TableID:62, RowCount:0, ArgLen:3, start time: 2024-06-06 10:01:07.183 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/06 10:01:07.184 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:63, Type:create view, State:none, SchemaState:queueing, SchemaID:53, TableID:62, RowCount:0, ArgLen:3, start time: 2024-06-06 10:01:07.183 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="/*!50001 CREATE ALGORITHM=UNDEFINED */\n/*!50013 DEFINER=`root`@`127.0.0.1` SQL SECURITY DEFINER */\n/*!50001 VIEW `t_cpsvpb` (`c0`, `c2`, `c3`, `c4`, `c5`, `c6`, `c7`, `c8`, `c9`, `c10`, `c11`, `c12`, `c13`, `c14`) AS SELECT DISTINCT `subq_0`.`c1` AS `c0`,`subq_0`.`c2` AS `c2`,8 AS `c3`,CASE WHEN (`subq_0`.`c3` NOT IN (SELECT `ref_2`.`c_4vix1d` AS `c0` FROM `testdb`.`t_037irb` AS `ref_2` WHERE `ref_2`.`c_2ykt0d`<=`ref_2`.`c_nrh3o`)) AND (`subq_0`.`c3`<=(SELECT (SELECT `c_hhjlmc` AS `c_hhjlmc` FROM `testdb`.`t_x7zqmd` ORDER BY `c_hhjlmc` LIMIT 4,1) AS `c0` FROM `testdb`.`t_037irb` AS `ref_3` WHERE `subq_0`.`c1`!=`ref_3`.`c_2ykt0d`)) THEN `subq_0`.`c3` ELSE `subq_0`.`c3` END AS `c4`,CASE WHEN `subq_0`.`c1`>=(SELECT MAX(`c_8weeq`) AS `max(c_8weeq)` FROM `testdb`.`t_x7zqmd`) THEN `subq_0`.`c2` ELSE `subq_0`.`c2` END AS `c5`,`subq_0`.`c1` AS `c6`,`subq_0`.`c2` AS `c7`,`subq_0`.`c3` AS `c8`,`subq_0`.`c3` AS `c9`,`subq_0`.`c2` AS `c10`,`subq_0`.`c4` AS `c11`,COUNT(CAST(`subq_0`.`c2` AS DOUBLE)) OVER (PARTITION BY `subq_0`.`c4` ORDER BY `subq_0`.`c1`) AS `c12`,`subq_0`.`c3` AS `c13`,CAST(COALESCE(`subq_0`.`c3`, _UTF8MB4'9sx3k') AS CHAR) AS `c14` FROM (SELECT COUNT(CAST(`ref_1`.`c_jyc_cd` AS DOUBLE)) AS `c0`,AVG(CAST(`ref_1`.`c_3b1zld` AS SIGNED)) AS `c1`,MIN(CAST(`ref_1`.`c_jyc_cd` AS DOUBLE)) AS `c2`,`ref_0`.`c_glkxdb` AS `c3`,COUNT(CAST(`ref_1`.`c_13sfid` AS DOUBLE)) AS `c4` FROM `testdb`.`t_037irb` AS `ref_0` JOIN `testdb`.`t_x7zqmd` AS `ref_1` WHERE `ref_0`.`c_nrh3o`>`ref_1`.`c_8weeq` GROUP BY `ref_0`.`c_glkxdb`) AS `subq_0` WHERE (SELECT `c_8weeq` AS `c_8weeq` FROM `testdb`.`t_x7zqmd` ORDER BY `c_8weeq` LIMIT 2,1) IS NOT NULL */;"]
   > [2024/06/06 10:01:07.185 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:63, Type:create view, State:none, SchemaState:queueing, SchemaID:53, TableID:62, RowCount:0, ArgLen:0, start time: 2024-06-06 10:01:07.183 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/06 10:01:07.188 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=33] [neededSchemaVersion=34] ["start time"=621.384µs] [phyTblIDs="[62]"] [actionTypes="[2097152]"]
   > [2024/06/06 10:01:07.190 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=34] ["take time"=2.279503ms] [job="ID:63, Type:create view, State:done, SchemaState:public, SchemaID:53, TableID:62, RowCount:0, ArgLen:3, start time: 2024-06-06 10:01:07.183 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/06 10:01:07.192 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:63, Type:create view, State:synced, SchemaState:public, SchemaID:53, TableID:62, RowCount:0, ArgLen:0, start time: 2024-06-06 10:01:07.183 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/06 10:01:07.193 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=63]
   > [2024/06/06 10:01:07.193 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/06 10:01:08.424 +00:00] [INFO] [set.go:127] ["set global var"] [conn=7] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/06/06 10:01:08.632 +00:00] [ERROR] [misc.go:94] ["panic in the recoverable goroutine"] [r="\"invalid memory address or nil pointer dereference\""] ["stack trace"="github.com/pingcap/tidb/util.WithRecovery.func1\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:96\nruntime.gopanic\n\t/usr/local/go/src/runtime/panic.go:965\nruntime.panicmem\n\t/usr/local/go/src/runtime/panic.go:212\nruntime.sigpanic\n\t/usr/local/go/src/runtime/signal_unix.go:734\ngithub.com/pingcap/tidb/util/chunk.(*Chunk).NumRows\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/chunk/chunk.go:349\ngithub.com/pingcap/tidb/executor.(*vecGroupChecker).splitIntoGroups\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/aggregate.go:1456\ngithub.com/pingcap/tidb/executor.(*PipelinedWindowExec).getRowsInPartition\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/pipelined_window.go:188\ngithub.com/pingcap/tidb/executor.(*PipelinedWindowExec).Next\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/pipelined_window.go:124\ngithub.com/pingcap/tidb/executor.Next\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/executor.go:285\ngithub.com/pingcap/tidb/executor.(*ProjectionExec).unParallelExecute\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:193\ngithub.com/pingcap/tidb/executor.(*ProjectionExec).Next\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:179\ngithub.com/pingcap/tidb/executor.Next\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/executor.go:285\ngithub.com/pingcap/tidb/executor.(*CTEExec).computeSeedPart\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/cte.go:225\ngithub.com/pingcap/tidb/executor.(*CTEExec).Next\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/cte.go:160\ngithub.com/pingcap/tidb/executor.Next\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/executor.go:285\ngithub.com/pingcap/tidb/executor.(*SelectionExec).Next\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/executor.go:1301\ngithub.com/pingcap/tidb/executor.Next\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/executor.go:285\ngithub.com/pingcap/tidb/executor.(*HashJoinExec).fetchBuildSideRows\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:268\ngithub.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable.func2\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:702\ngithub.com/pingcap/tidb/util.WithRecovery\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99"]
   > runtime: goroutine stack exceeds 1000000000-byte limit
   > runtime: sp=0xc032070398 stack=[0xc032070000, 0xc052070000]
   > fatal error: stack overflow
   > runtime stack:
   > runtime.throw(0x3b1a561, 0xe)
   > 	/usr/local/go/src/runtime/panic.go:1117 +0x72
   > runtime.newstack()
   > 	/usr/local/go/src/runtime/stack.go:1069 +0x7ed
   > runtime.morestack()
   > 	/usr/local/go/src/runtime/asm_amd64.s:458 +0x8f
   > goroutine 995 [running]:
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0119f4ba0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:182 +0x16f fp=0xc0320703a8 sp=0xc0320703a0 pc=0x1ee3a8f
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0119f4b40, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0320703f0 sp=0xc0320703a8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011d43da0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032070438 sp=0xc0320703f0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011d43c80, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032070480 sp=0xc032070438 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc000426010, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0320704c8 sp=0xc032070480 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011c7fcd0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032070510 sp=0xc0320704c8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc0109ec210, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032070558 sp=0xc032070510 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc0115cb2a0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0320705a0 sp=0xc032070558 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc01193a3b0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0320705e8 sp=0xc0320705a0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0119f5200, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032070630 sp=0xc0320705e8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011d43620, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032070678 sp=0xc032070630 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc0119e23c0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0320706c0 sp=0xc032070678 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0119f4ba0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032070708 sp=0xc0320706c0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0119f4b40, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032070750 sp=0xc032070708 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011d43da0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032070798 sp=0xc032070750 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011d43c80, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0320707e0 sp=0xc032070798 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc000426010, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032070828 sp=0xc0320707e0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011c7fcd0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032070870 sp=0xc032070828 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc0109ec210, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0320708b8 sp=0xc032070870 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc0115cb2a0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032070900 sp=0xc0320708b8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc01193a3b0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032070948 sp=0xc032070900 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0119f5200, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032070990 sp=0xc032070948 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011d43620, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0320709d8 sp=0xc032070990 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc0119e23c0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032070a20 sp=0xc0320709d8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0119f4ba0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032070a68 sp=0xc032070a20 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0119f4b40, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032070ab0 sp=0xc032070a68 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011d43da0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032070af8 sp=0xc032070ab0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011d43c80, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032070b40 sp=0xc032070af8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc000426010, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032070b88 sp=0xc032070b40 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011c7fcd0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032070bd0 sp=0xc032070b88 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc0109ec210, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032070c18 sp=0xc032070bd0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc0115cb2a0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032070c60 sp=0xc032070c18 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc01193a3b0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032070ca8 sp=0xc032070c60 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0119f5200, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032070cf0 sp=0xc032070ca8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011d43620, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032070d38 sp=0xc032070cf0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc0119e23c0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032070d80 sp=0xc032070d38 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0119f4ba0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032070dc8 sp=0xc032070d80 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0119f4b40, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032070e10 sp=0xc032070dc8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011d43da0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032070e58 sp=0xc032070e10 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011d43c80, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032070ea0 sp=0xc032070e58 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc000426010, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032070ee8 sp=0xc032070ea0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011c7fcd0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032070f30 sp=0xc032070ee8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc0109ec210, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032070f78 sp=0xc032070f30 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc0115cb2a0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032070fc0 sp=0xc032070f78 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc01193a3b0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071008 sp=0xc032070fc0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0119f5200, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071050 sp=0xc032071008 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011d43620, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071098 sp=0xc032071050 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc0119e23c0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0320710e0 sp=0xc032071098 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0119f4ba0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071128 sp=0xc0320710e0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0119f4b40, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071170 sp=0xc032071128 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011d43da0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0320711b8 sp=0xc032071170 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011d43c80, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071200 sp=0xc0320711b8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc000426010, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071248 sp=0xc032071200 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011c7fcd0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071290 sp=0xc032071248 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc0109ec210, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0320712d8 sp=0xc032071290 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc0115cb2a0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071320 sp=0xc0320712d8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc01193a3b0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071368 sp=0xc032071320 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0119f5200, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0320713b0 sp=0xc032071368 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011d43620, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0320713f8 sp=0xc0320713b0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc0119e23c0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071440 sp=0xc0320713f8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0119f4ba0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071488 sp=0xc032071440 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0119f4b40, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0320714d0 sp=0xc032071488 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011d43da0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071518 sp=0xc0320714d0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011d43c80, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071560 sp=0xc032071518 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc000426010, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0320715a8 sp=0xc032071560 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011c7fcd0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0320715f0 sp=0xc0320715a8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc0109ec210, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071638 sp=0xc0320715f0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc0115cb2a0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071680 sp=0xc032071638 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc01193a3b0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0320716c8 sp=0xc032071680 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0119f5200, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071710 sp=0xc0320716c8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011d43620, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071758 sp=0xc032071710 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc0119e23c0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0320717a0 sp=0xc032071758 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0119f4ba0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0320717e8 sp=0xc0320717a0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0119f4b40, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071830 sp=0xc0320717e8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011d43da0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071878 sp=0xc032071830 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011d43c80, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0320718c0 sp=0xc032071878 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc000426010, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071908 sp=0xc0320718c0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011c7fcd0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071950 sp=0xc032071908 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc0109ec210, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071998 sp=0xc032071950 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc0115cb2a0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc0320719e0 sp=0xc032071998 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc01193a3b0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071a28 sp=0xc0320719e0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0119f5200, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071a70 sp=0xc032071a28 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011d43620, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071ab8 sp=0xc032071a70 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc0119e23c0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071b00 sp=0xc032071ab8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0119f4ba0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071b48 sp=0xc032071b00 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0119f4b40, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071b90 sp=0xc032071b48 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011d43da0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071bd8 sp=0xc032071b90 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011d43c80, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071c20 sp=0xc032071bd8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc000426010, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071c68 sp=0xc032071c20 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc011c7fcd0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071cb0 sp=0xc032071c68 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc0109ec210, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071cf8 sp=0xc032071cb0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc0115cb2a0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071d40 sp=0xc032071cf8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc01193a3b0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071d88 sp=0xc032071d40 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0119f5200, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071dd0 sp=0xc032071d88 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011d43620, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071e18 sp=0xc032071dd0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x4038578, 0xc0119e23c0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071e60 sp=0xc032071e18 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0119f4ba0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071ea8 sp=0xc032071e60 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc0119f4b40, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071ef0 sp=0xc032071ea8 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011d43da0, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071f38 sp=0xc032071ef0 pc=0x1ee3a1c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback(0x40385b8, 0xc011d43c80, 0x40385b8, 0xc0119f4ba0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/memory/tracker.go:193 +0xfc fp=0xc032071f80 sp=0xc032071f38 pc=0x1ee3a1c
   > ...additional frames elided...
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:699 +0x198
   > goroutine 1 [chan receive]:
   > github.com/pingcap/tidb/server.(*Server).Run(0xc01097d930, 0xc011226b70, 0xc0101e9f20)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/server.go:338 +0x1c5
   > main.main()
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/tidb-server/main.go:200 +0x33d
   > goroutine 9 [select]:
   > go.opencensus.io/stats/view.(*worker).start(0xc000143980)
   > 	/nfs/cache/mod/go.opencensus.io@v0.22.5/stats/view/worker.go:276 +0xcd
   > created by go.opencensus.io/stats/view.init.0
   > 	/nfs/cache/mod/go.opencensus.io@v0.22.5/stats/view/worker.go:34 +0x68
   > goroutine 166 [chan receive]:
   > go.etcd.io/etcd/pkg/logutil.(*MergeLogger).outputLoop(0xc00099a210)
   > 	/nfs/cache/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20200824191128-ae9734ed278b/pkg/logutil/merge_logger.go:173 +0x3ac
   > created by go.etcd.io/etcd/pkg/logutil.NewMergeLogger
   > 	/nfs/cache/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20200824191128-ae9734ed278b/pkg/logutil/merge_logger.go:91 +0x85
   > goroutine 78 [chan receive]:
   > go.etcd.io/etcd/pkg/logutil.(*MergeLogger).outputLoop(0xc000b5e4b0)
   > 	/nfs/cache/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20200824191128-ae9734ed278b/pkg/logutil/merge_logger.go:173 +0x3ac
   > created by go.etcd.io/etcd/pkg/logutil.NewMergeLogger
   > 	/nfs/cache/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20200824191128-ae9734ed278b/pkg/logutil/merge_logger.go:91 +0x85
   > goroutine 193 [chan receive]:
   > go.etcd.io/etcd/pkg/logutil.(*MergeLogger).outputLoop(0xc00058ed38)
   > 	/nfs/cache/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20200824191128-ae9734ed278b/pkg/logutil/merge_logger.go:173 +0x3ac
   > created by go.etcd.io/etcd/pkg/logutil.NewMergeLogger
   > 	/nfs/cache/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20200824191128-ae9734ed278b/pkg/logutil/merge_logger.go:91 +0x85
   > goroutine 458 [chan receive]:
   > github.com/pingcap/tidb/util/systimemon.StartMonitor(0x3c23558, 0x3c228d0, 0xc0009a4a30)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/systimemon/systime_mon.go:31 +0x148
   > created by main.setupMetrics
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/tidb-server/main.go:652 +0x105
   > goroutine 717 [select]:
   > github.com/pingcap/tidb/executor.readProjectionInput(0xc011d84900, 0xc0117fa0c0, 0x3b1ee58)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:459 +0x86
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc0117f8280, 0x4030f90, 0xc011aaeff0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:427 +0x129
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:275 +0x78f
   > goroutine 457 [chan receive]:
   > github.com/pingcap/tidb/util/profile.HeapProfileForGlobalMemTracker(0xdf8475800)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/profile/trackerRecorder.go:32 +0xbf
   > created by main.setHeapProfileTracker
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/tidb-server/main.go:266 +0x8d
   > goroutine 459 [select]:
   > github.com/pingcap/badger.(*DB).updateSize(0xc000cc4900, 0xc00099b380)
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/db.go:1032 +0x108
   > created by github.com/pingcap/badger.Open
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/db.go:327 +0xe14
   > goroutine 460 [select]:
   > github.com/pingcap/badger/epoch.(*ResourceManager).collectLoop(0xc000cf8060, 0xc00099b398)
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/epoch/manager.go:101 +0xdc
   > created by github.com/pingcap/badger/epoch.NewResourceManager
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/epoch/manager.go:79 +0xa7
   > goroutine 461 [select]:
   > github.com/pingcap/badger.Open.func4(0xc00068e340)
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/db.go:341 +0x17c
   > created by github.com/pingcap/badger.Open
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/db.go:338 +0x10a8
   > goroutine 462 [select]:
   > github.com/pingcap/badger.(*blobGCHandler).run(0xc000850ac0, 0xc00099b950)
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/blob.go:468 +0xd4
   > created by github.com/pingcap/badger.(*blobManager).Open
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/blob.go:292 +0x618
   > goroutine 463 [select]:
   > github.com/pingcap/badger.(*levelsController).runWorker(0xc00024da40, 0xc00099b968, 0x100)
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/levels.go:212 +0x185
   > created by github.com/pingcap/badger.(*levelsController).startCompact
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/levels.go:180 +0x93
   > goroutine 464 [select]:
   > github.com/pingcap/badger.(*levelsController).runWorker(0xc00024da40, 0xc00099b968, 0x100)
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/levels.go:212 +0x185
   > created by github.com/pingcap/badger.(*levelsController).startCompact
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/levels.go:180 +0x93
   > goroutine 465 [select]:
   > github.com/pingcap/badger.(*levelsController).runWorker(0xc00024da40, 0xc00099b968, 0x101)
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/levels.go:212 +0x185
   > created by github.com/pingcap/badger.(*levelsController).startCompact
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/levels.go:180 +0x93
   > goroutine 466 [chan receive]:
   > github.com/pingcap/badger.(*DB).runFlushMemTable(0xc000cc4900, 0xc00099b908, 0x0, 0x0)
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/db.go:913 +0x190
   > created by github.com/pingcap/badger.Open
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/db.go:360 +0x17b0
   > goroutine 835 [select]:
   > github.com/pingcap/tidb/domain.(*Domain).updateStatsWorker(0xc0105b7f00, 0x40773d8, 0xc010479a00, 0x404ecf8, 0xc010c4eee0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:1294 +0x288
   > created by github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:1181 +0x1d6
   > goroutine 482 [select]:
   > github.com/pingcap/badger.(*writeWorker).runWriteVLog(0xc0000dcd40, 0xc00026c108)
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/writer.go:94 +0x1dc
   > created by github.com/pingcap/badger.startWriteWorker
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/writer.go:64 +0x190
   > goroutine 483 [chan receive, locked to thread]:
   > github.com/pingcap/badger.(*writeWorker).runWriteLSM(0xc0000dcd40, 0xc00026c108)
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/writer.go:141 +0x195
   > created by github.com/pingcap/badger.startWriteWorker
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/writer.go:65 +0x1bc
   > goroutine 484 [chan receive]:
   > github.com/pingcap/badger.(*writeWorker).runMergeLSM(0xc0000dcd40, 0xc00026c108)
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/writer.go:154 +0xad
   > created by github.com/pingcap/badger.startWriteWorker
   > 	/nfs/cache/mod/github.com/pingcap/badger@v1.5.1-0.20200908111422-2e78ee155d19/writer.go:66 +0x1e8
   > goroutine 485 [select]:
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.writeDBWorker.run(0xc000c361e0, 0xc000b1a800)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:95 +0x205
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*dbWriter).Open
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:198 +0x8f
   > goroutine 486 [select]:
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.writeLockWorker.run(0xc000c36240, 0xc000b1a800)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:147 +0x3e5
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*dbWriter).Open
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:205 +0xdc
   > goroutine 487 [select]:
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*MVCCStore).runUpdateSafePointLoop(0xc000b38080)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:1549 +0x28a
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.NewMVCCStore
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:84 +0x269
   > goroutine 488 [select]:
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*MVCCStore).StartDeadlockDetection.func1(0xc000b38080)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:1285 +0x8a
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*MVCCStore).StartDeadlockDetection
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:1283 +0x78
   > goroutine 489 [select]:
   > github.com/tikv/client-go/v2/oracle/oracles.(*pdOracle).updateTS(0xc0002b4620, 0x4030f20, 0xc000052058, 0x77359400)
   > 	/nfs/cache/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20210820060448-daddf73a0706/oracle/oracles/pd.go:227 +0x131
   > created by github.com/tikv/client-go/v2/oracle/oracles.NewPdOracle
   > 	/nfs/cache/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20210820060448-daddf73a0706/oracle/oracles/pd.go:75 +0xd3
   > goroutine 490 [select]:
   > github.com/tikv/client-go/v2/internal/locate.(*RegionCache).asyncCheckAndResolveLoop(0xc000b38180, 0xdf8475800)
   > 	/nfs/cache/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20210820060448-daddf73a0706/internal/locate/region_cache.go:395 +0xdc
   > created by github.com/tikv/client-go/v2/internal/locate.NewRegionCache
   > 	/nfs/cache/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20210820060448-daddf73a0706/internal/locate/region_cache.go:366 +0x259
   > goroutine 491 [select]:
   > github.com/tikv/client-go/v2/tikv.(*KVStore).runSafePointChecker(0xc000b86240)
   > 	/nfs/cache/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20210820060448-daddf73a0706/tikv/kv.go:262 +0x136
   > created by github.com/tikv/client-go/v2/tikv.NewKVStore
   > 	/nfs/cache/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20210820060448-daddf73a0706/tikv/kv.go:185 +0x407
   > goroutine 492 [select]:
   > github.com/tikv/client-go/v2/tikv.(*KVStore).safeTSUpdater(0xc000b86240)
   > 	/nfs/cache/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20210820060448-daddf73a0706/tikv/kv.go:540 +0x194
   > created by github.com/tikv/client-go/v2/tikv.NewKVStore
   > 	/nfs/cache/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20210820060448-daddf73a0706/tikv/kv.go:186 +0x429
   > goroutine 493 [select]:
   > github.com/dgraph-io/ristretto.(*defaultPolicy).processItems(0xc0009632c0)
   > 	/nfs/cache/mod/github.com/dgraph-io/ristretto@v0.0.1/policy.go:96 +0xa5
   > created by github.com/dgraph-io/ristretto.newDefaultPolicy
   > 	/nfs/cache/mod/github.com/dgraph-io/ristretto@v0.0.1/policy.go:80 +0x129
   > goroutine 494 [select]:
   > github.com/dgraph-io/ristretto.(*Cache).processItems(0xc000c36600)
   > 	/nfs/cache/mod/github.com/dgraph-io/ristretto@v0.0.1/cache.go:257 +0x9d
   > created by github.com/dgraph-io/ristretto.NewCache
   > 	/nfs/cache/mod/github.com/dgraph-io/ristretto@v0.0.1/cache.go:155 +0x205
   > goroutine 705 [select]:
   > github.com/pingcap/tidb/executor.readProjectionInput(0xc011e16ea0, 0xc0109fe060, 0x3b1ee58)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:459 +0x86
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc0109fc300, 0x4030f90, 0xc011aaeff0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:427 +0x129
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:275 +0x78f
   > goroutine 382 [select]:
   > github.com/pingcap/tidb/ddl.(*ddl).limitDDLJobs(0xc010c94d90)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/ddl/ddl_worker.go:265 +0x2d9
   > created by github.com/pingcap/tidb/ddl.(*ddl).Start
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/ddl/ddl.go:346 +0x2d5
   > goroutine 704 [select]:
   > github.com/pingcap/tidb/executor.readProjectionInput(0xc011e16d80, 0xc0109fe060, 0x3b1ee58)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:459 +0x86
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc0109fc2c0, 0x4030f90, 0xc011aaeff0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:427 +0x129
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:275 +0x78f
   > goroutine 715 [select]:
   > github.com/pingcap/tidb/executor.readProjectionInput(0xc011d846c0, 0xc0117fa0c0, 0x3b1ee58)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:459 +0x86
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc0117f8200, 0x4030f90, 0xc011aaeff0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:427 +0x129
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:275 +0x78f
   > goroutine 714 [select]:
   > github.com/pingcap/tidb/executor.readProjectionInput(0xc011d845a0, 0xc0117fa0c0, 0x3b1ee58)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:459 +0x86
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc0117f81c0, 0x4030f90, 0xc011aaeff0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:427 +0x129
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:275 +0x78f
   > goroutine 716 [select]:
   > github.com/pingcap/tidb/executor.readProjectionInput(0xc011d847e0, 0xc0117fa0c0, 0x3b1ee58)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:459 +0x86
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc0117f8240, 0x4030f90, 0xc011aaeff0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:427 +0x129
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:275 +0x78f
   > goroutine 793 [sleep]:
   > time.Sleep(0x3b9aca00)
   > 	/usr/local/go/src/runtime/time.go:193 +0xd2
   > github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).startCPUProfileWorker(0xc0009315f0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:114 +0xb4
   > created by github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).Run
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:92 +0xb7
   > goroutine 1058 [select]:
   > github.com/pingcap/tidb/executor.readProjectionInput(0xc011e16fc0, 0xc0109fe060, 0x3b1ee58)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:459 +0x86
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc0109fc340, 0x4030f90, 0xc011aaeff0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:427 +0x129
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:275 +0x78f
   > goroutine 791 [select]:
   > github.com/pingcap/tidb/util/topsql/reporter.(*RemoteTopSQLReporter).collectWorker(0xc01135a0e0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:325 +0x1bb
   > created by github.com/pingcap/tidb/util/topsql/reporter.NewRemoteTopSQLReporter
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:158 +0x1a7
   > goroutine 790 [chan receive]:
   > github.com/pingcap/tidb/util/signal.SetupSignalHandler.func2(0xc0113bf6e0, 0xc011226b70)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:52 +0x52
   > created by github.com/pingcap/tidb/util/signal.SetupSignalHandler
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:51 +0x194
   > goroutine 792 [select]:
   > github.com/pingcap/tidb/util/topsql/reporter.(*RemoteTopSQLReporter).reportWorker(0xc01135a0e0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:497 +0x211
   > created by github.com/pingcap/tidb/util/topsql/reporter.NewRemoteTopSQLReporter
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:159 +0x1c9
   > goroutine 384 [select]:
   > github.com/pingcap/tidb/ddl.(*worker).start(0xc0105f2370, 0xc010c992c0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/ddl/ddl_worker.go:177 +0x315
   > created by github.com/pingcap/tidb/ddl.(*ddl).Start
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/ddl/ddl.go:364 +0x6a5
   > goroutine 834 [select]:
   > github.com/pingcap/tidb/domain.(*Domain).loadStatsWorker(0xc0105b7f00)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:1226 +0x3cc
   > created by github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:1169 +0x2fa
   > goroutine 820 [chan receive]:
   > github.com/pingcap/tidb/util/signal.SetupSignalHandler.func1(0xc0111c9920)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:36 +0x72
   > created by github.com/pingcap/tidb/util/signal.SetupSignalHandler
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:33 +0xb9
   > goroutine 703 [select]:
   > github.com/pingcap/tidb/executor.readProjectionInput(0xc011e16c60, 0xc0109fe060, 0x3b1ee58)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:459 +0x86
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc0109fc280, 0x4030f90, 0xc011aaeff0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:427 +0x129
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:275 +0x78f
   > goroutine 383 [select]:
   > github.com/pingcap/tidb/ddl.(*delRange).startEmulator(0xc010afd680)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/ddl/delete_range.go:143 +0x128
   > created by github.com/pingcap/tidb/ddl.(*delRange).start
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/ddl/delete_range.go:125 +0x6a
   > goroutine 385 [select]:
   > github.com/pingcap/tidb/ddl.(*worker).start(0xc0105f2420, 0xc010c992c0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/ddl/ddl_worker.go:177 +0x315
   > created by github.com/pingcap/tidb/ddl.(*ddl).Start
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/ddl/ddl.go:364 +0x6a5
   > goroutine 724 [select]:
   > github.com/pingcap/tidb/domain.(*Domain).loadSchemaInLoop(0xc0105b7f00, 0x4030ee8, 0xc0105d4c80, 0xa7a358200)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:513 +0x218
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:768 +0x734
   > goroutine 725 [select]:
   > github.com/pingcap/tidb/domain.(*Domain).topNSlowQueryLoop(0xc0105b7f00)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:423 +0x1e5
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:771 +0x61c
   > goroutine 726 [select]:
   > github.com/pingcap/tidb/domain.(*Domain).infoSyncerKeeper(0xc0105b7f00)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:455 +0x138
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:774 +0x65b
   > goroutine 727 [select]:
   > github.com/pingcap/tidb/domain.(*Domain).topologySyncerKeeper(0xc0105b7f00)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:481 +0x193
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:778 +0x6c5
   > goroutine 753 [select]:
   > github.com/pingcap/tidb/domain.(*Domain).TelemetryRotateSubWindowLoop.func1(0xc0105b7f00)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:1113 +0xd8
   > created by github.com/pingcap/tidb/domain.(*Domain).TelemetryRotateSubWindowLoop
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:1106 +0x7f
   > goroutine 813 [select]:
   > github.com/pingcap/tidb/domain.(*Domain).LoadPrivilegeLoop.func1(0xc0105b7f00, 0xc010d94658, 0x45d964b800, 0x40773d8, 0xc010478800)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:883 +0x125
   > created by github.com/pingcap/tidb/domain.(*Domain).LoadPrivilegeLoop
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:874 +0x1f0
   > goroutine 739 [select]:
   > github.com/pingcap/tidb/domain.(*Domain).handleEvolvePlanTasksLoop.func1(0xc0105b7f00, 0x404ecf8, 0xc010c4e1c0, 0x40773d8, 0xc0105eec00)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:1050 +0xde
   > created by github.com/pingcap/tidb/domain.(*Domain).handleEvolvePlanTasksLoop
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:1043 +0x8f
   > goroutine 738 [select]:
   > github.com/pingcap/tidb/domain.(*Domain).globalBindHandleWorkerLoop.func1(0xc0105b7f00, 0x404ecf8, 0xc010c4e1c0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:1014 +0x157
   > created by github.com/pingcap/tidb/domain.(*Domain).globalBindHandleWorkerLoop
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:1001 +0x73
   > goroutine 816 [select]:
   > github.com/pingcap/tidb/domain.(*Domain).LoadSysVarCacheLoop.func1(0xc0105b7f00, 0xc010d947b8, 0x6fc23ac00, 0x40773d8, 0xc010dd0c00)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:932 +0x125
   > created by github.com/pingcap/tidb/domain.(*Domain).LoadSysVarCacheLoop
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:923 +0xf6
   > goroutine 752 [select]:
   > github.com/pingcap/tidb/domain.(*Domain).TelemetryReportLoop.func1(0xc0105b7f00, 0x40773d8, 0xc010dd1200)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:1084 +0x12f
   > created by github.com/pingcap/tidb/domain.(*Domain).TelemetryReportLoop
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:1076 +0x2b8
   > goroutine 819 [syscall]:
   > os/signal.signal_recv(0x1252646)
   > 	/usr/local/go/src/runtime/sigqueue.go:168 +0xa5
   > os/signal.loop()
   > 	/usr/local/go/src/os/signal/signal_unix.go:23 +0x25
   > created by os/signal.Notify.func1.1
   > 	/usr/local/go/src/os/signal/signal.go:151 +0x45
   > goroutine 801 [chan receive]:
   > github.com/soheilhy/cmux.muxListener.Accept(...)
   > 	/nfs/cache/mod/github.com/soheilhy/cmux@v0.1.4/cmux.go:229
   > net/http.(*Server).Serve(0xc010d74460, 0x4023c40, 0xc0006d4ed0, 0x0, 0x0)
   > 	/usr/local/go/src/net/http/server.go:2981 +0x285
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer.func2()
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/http_status.go:366 +0x58
   > github.com/pingcap/tidb/util.WithRecovery(0xc0115188c0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99 +0x4f
   > created by github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/http_status.go:365 +0x488
   > goroutine 800 [chan receive]:
   > github.com/soheilhy/cmux.muxListener.Accept(...)
   > 	/nfs/cache/mod/github.com/soheilhy/cmux@v0.1.4/cmux.go:229
   > google.golang.org/grpc.(*Server).Serve(0xc010d169c0, 0x4023c40, 0xc0006d4ee8, 0x0, 0x0)
   > 	/nfs/cache/mod/google.golang.org/grpc@v1.29.1/server.go:621 +0x27f
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer.func1()
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/http_status.go:361 +0x58
   > github.com/pingcap/tidb/util.WithRecovery(0xc0115188a0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99 +0x4f
   > created by github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/http_status.go:360 +0x405
   > goroutine 795 [IO wait]:
   > internal/poll.runtime_pollWait(0x7fe37b426f08, 0x72, 0x0)
   > 	/usr/local/go/src/runtime/netpoll.go:222 +0x55
   > internal/poll.(*pollDesc).wait(0xc0111a7198, 0x72, 0x0, 0x0, 0x3b05d89)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:87 +0x45
   > internal/poll.(*pollDesc).waitRead(...)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:92
   > internal/poll.(*FD).Accept(0xc0111a7180, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
   > 	/usr/local/go/src/internal/poll/fd_unix.go:401 +0x212
   > net.(*netFD).accept(0xc0111a7180, 0xc, 0x7fe37b6da878, 0x10)
   > 	/usr/local/go/src/net/fd_unix.go:172 +0x45
   > net.(*TCPListener).accept(0xc01097f2a8, 0x11ed178, 0xc, 0x37efe60)
   > 	/usr/local/go/src/net/tcpsock_posix.go:139 +0x32
   > net.(*TCPListener).Accept(0xc01097f2a8, 0xc01152c900, 0x20, 0x7fe37b6da878, 0x20)
   > 	/usr/local/go/src/net/tcpsock.go:261 +0x65
   > github.com/soheilhy/cmux.(*cMux).Serve(0xc01152a320, 0x0, 0x0)
   > 	/nfs/cache/mod/github.com/soheilhy/cmux@v0.1.4/cmux.go:162 +0x96
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer(0xc01097d930, 0xc01151e380)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/http_status.go:370 +0x49f
   > github.com/pingcap/tidb/server.(*Server).startHTTPServer(0xc01097d930)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/http_status.go:346 +0x12a7
   > created by github.com/pingcap/tidb/server.(*Server).startStatusHTTP
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/http_status.go:59 +0x3f
   > goroutine 794 [chan receive]:
   > github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).startAnalyzeProfileWorker(0xc0009315f0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:141 +0xd4
   > created by github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).Run
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:93 +0xd9
   > goroutine 796 [IO wait]:
   > internal/poll.runtime_pollWait(0x7fe37b426ff0, 0x72, 0x0)
   > 	/usr/local/go/src/runtime/netpoll.go:222 +0x55
   > internal/poll.(*pollDesc).wait(0xc0111a7118, 0x72, 0x0, 0x0, 0x3b05d89)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:87 +0x45
   > internal/poll.(*pollDesc).waitRead(...)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:92
   > internal/poll.(*FD).Accept(0xc0111a7100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
   > 	/usr/local/go/src/internal/poll/fd_unix.go:401 +0x212
   > net.(*netFD).accept(0xc0111a7100, 0x37bb380, 0x1, 0xc000656838)
   > 	/usr/local/go/src/net/fd_unix.go:172 +0x45
   > net.(*TCPListener).accept(0xc01097f290, 0xc00fa04d70, 0xc00fa04d78, 0x10)
   > 	/usr/local/go/src/net/tcpsock_posix.go:139 +0x32
   > net.(*TCPListener).Accept(0xc01097f290, 0x3c1ef90, 0xc01097d930, 0xc0112f4d80, 0x0)
   > 	/usr/local/go/src/net/tcpsock.go:261 +0x65
   > github.com/pingcap/tidb/server.(*Server).startNetworkListener(0xc01097d930, 0x4022c80, 0xc01097f290, 0xc01133ca00, 0xc0006ce8a0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/server.go:347 +0x6a
   > created by github.com/pingcap/tidb/server.(*Server).Run
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/server.go:332 +0x11b
   > goroutine 836 [select]:
   > github.com/pingcap/tidb/domain.(*Domain).autoAnalyzeWorker(0xc0105b7f00, 0x404ecf8, 0xc010c4eee0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:1347 +0x165
   > created by github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/domain/domain.go:1184 +0x245
   > goroutine 837 [select]:
   > github.com/pingcap/tidb/util/expensivequery.(*Handle).Run(0xc010506e10)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/expensivequery/expensivequery.go:60 +0x337
   > created by main.createServer
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/tidb-server/main.go:631 +0x1c7
   > goroutine 861 [chan receive]:
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Close(0xc00f99d600, 0x0, 0xc011c7b5c0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:121 +0xd0
   > github.com/pingcap/tidb/executor.(*baseExecutor).Close(0xc011cd8200, 0xff, 0x4031a48)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/executor.go:180 +0x7e
   > github.com/pingcap/tidb/executor.(*ProjectionExec).Close(0xc011cd8200, 0x3fe17c0, 0xc0109e8fc0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:328 +0x138
   > github.com/pingcap/tidb/executor.(*recordSet).Close(0xc011d68e60, 0x4030f90, 0xc011aaeff0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/adapter.go:169 +0x38
   > github.com/pingcap/tidb/session.(*execStmtResult).Close(0xc011d4cb10, 0xc011d4cb10, 0x4030f90)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/session/session.go:1833 +0x42
   > github.com/pingcap/tidb/server.(*tidbResultSet).Close(0xc011d68eb0, 0xc0109e8fc0, 0xc011bcafc8)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/driver_tidb.go:323 +0x4a
   > github.com/pingcap/parser/terror.Call(0xc011bcb108)
   > 	/nfs/cache/mod/github.com/pingcap/parser@v0.0.0-20210831085004-b5390aa83f65/terror/terror.go:282 +0x3f
   > github.com/pingcap/tidb/server.(*clientConn).handleStmt(0xc0112f4d80, 0x4030ee8, 0xc011aaeff0, 0x404e488, 0xc010d694a0, 0x5d958d8, 0x0, 0x0, 0x1, 0x1, ...)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/conn.go:1846 +0x445
   > github.com/pingcap/tidb/server.(*clientConn).handleQuery(0xc0112f4d80, 0x4030ee8, 0xc011b28000, 0xc00ff721a1, 0x18c, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/conn.go:1690 +0x492
   > github.com/pingcap/tidb/server.(*clientConn).dispatch(0xc0112f4d80, 0x4030ee8, 0xc011b28000, 0xc00ff721a0, 0x18d, 0x18c, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/conn.go:1215 +0xafd
   > github.com/pingcap/tidb/server.(*clientConn).Run(0xc0112f4d80, 0x4030f90, 0xc011a08450)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/conn.go:978 +0x296
   > github.com/pingcap/tidb/server.(*Server).onConn(0xc01097d930, 0xc0112f4d80)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/server.go:501 +0xa53
   > created by github.com/pingcap/tidb/server.(*Server).startNetworkListener
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/server.go:404 +0x8fc
   > goroutine 713 [select]:
   > github.com/pingcap/tidb/executor.readProjectionInput(0xc011d84480, 0xc0117fa0c0, 0xc011268800)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:459 +0x86
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc0117f8180, 0x4030f90, 0xc011aaeff0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:427 +0x129
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:275 +0x78f
   > goroutine 702 [select]:
   > github.com/pingcap/tidb/executor.readProjectionInput(0xc011e16b40, 0xc0109fe060, 0xc011268800)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:459 +0x86
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc0109fc240, 0x4030f90, 0xc011aaeff0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:427 +0x129
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:275 +0x78f
   > goroutine 962 [chan receive]:
   > github.com/pingcap/tidb/executor.(*HashJoinExec).buildHashTableForList(0xc00f99d600, 0xc011d42f60, 0xc011d4cc00, 0xc011c7fbb0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:758 +0x327
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable(0xc00f99d600, 0x4030f90, 0xc011aaeff0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:713 +0x1b3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Next.func1()
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:658 +0xa9
   > github.com/pingcap/tidb/util.WithRecovery(0xc011c31b20, 0xc011c7fad0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99 +0x4f
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).Next
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:656 +0x305
   > goroutine 970 [chan receive]:
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Next(0xc00f99d400, 0x4030f90, 0xc011aaeff0, 0xc011d685a0, 0x7fe3333fffff, 0x7fe35333ada8)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:668 +0x87
   > github.com/pingcap/tidb/executor.Next(0x4030f90, 0xc011aaeff0, 0x40359f8, 0xc00f99d400, 0xc011d685a0, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/executor.go:285 +0x2de
   > github.com/pingcap/tidb/executor.(*ProjectionExec).unParallelExecute(0xc011c87c00, 0x4030f90, 0xc011aaeff0, 0xc011d69270, 0x0, 0x85f83aeddf00)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:193 +0xb2
   > github.com/pingcap/tidb/executor.(*ProjectionExec).Next(0xc011c87c00, 0x4030f90, 0xc011aaeff0, 0xc011d69270, 0x38eb320, 0xc011d63d50)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/projection.go:179 +0x73
   > github.com/pingcap/tidb/executor.Next(0x4030f90, 0xc011aaeff0, 0x4035f78, 0xc011c87c00, 0xc011d69270, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/executor.go:285 +0x2de
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchBuildSideRows(0xc00f99d600, 0x4030f90, 0xc011aaeff0, 0xc011d42f60, 0xc0118a1800)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:268 +0x194
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable.func2()
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:702 +0xcf
   > github.com/pingcap/tidb/util.WithRecovery(0xc011d4cc00, 0xc011c7fbb0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99 +0x4f
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:699 +0x198
   > goroutine 971 [chan receive]:
   > github.com/pingcap/tidb/executor.(*HashJoinExec).buildHashTableForList(0xc00f99d400, 0xc011d43560, 0xc011d72a20, 0xc011c7fcb0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:758 +0x327
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable(0xc00f99d400, 0x4030f90, 0xc011aaeff0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:713 +0x1b3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Next.func1()
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:658 +0xa9
   > github.com/pingcap/tidb/util.WithRecovery(0xc011d74380, 0xc011c7fbd0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99 +0x4f
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).Next
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:656 +0x305
   > goroutine 972 [select]:
   > github.com/pingcap/tidb/executor.(*HashJoinExec).wait4BuildSide(0xc00f99d400, 0xc011aaeff0, 0x4035bb8, 0xc011918540)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:244 +0x88
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchProbeSideChunks(0xc00f99d400, 0x4030f90, 0xc011aaeff0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:223 +0x26f
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func1()
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:324 +0xa9
   > github.com/pingcap/tidb/util.WithRecovery(0xc011d743a0, 0xc011c7fc30)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99 +0x4f
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:322 +0xfd
   > goroutine 973 [select]:
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc00f99d400, 0x0, 0x5d958d8, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:445 +0x33f
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:339 +0xc5
   > github.com/pingcap/tidb/util.WithRecovery(0xc011c811c0, 0xc011c7fc40)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99 +0x4f
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:337 +0x1ab
   > goroutine 974 [select]:
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc00f99d400, 0x1, 0x5d958d8, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:445 +0x33f
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:339 +0xc5
   > github.com/pingcap/tidb/util.WithRecovery(0xc011c81200, 0xc011c7fc50)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99 +0x4f
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:337 +0x1ab
   > goroutine 975 [select]:
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc00f99d400, 0x2, 0x5d958d8, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:445 +0x33f
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:339 +0xc5
   > github.com/pingcap/tidb/util.WithRecovery(0xc011c81240, 0xc011c7fc60)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99 +0x4f
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:337 +0x1ab
   > goroutine 976 [select]:
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc00f99d400, 0x3, 0x5d958d8, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:445 +0x33f
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:339 +0xc5
   > github.com/pingcap/tidb/util.WithRecovery(0xc011c81280, 0xc011c7fc70)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99 +0x4f
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:337 +0x1ab
   > goroutine 977 [select]:
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc00f99d400, 0x4, 0x5d958d8, 0x0, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:445 +0x33f
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:339 +0xc5
   > github.com/pingcap/tidb/util.WithRecovery(0xc011c812c0, 0xc011c7fc80)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99 +0x4f
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:337 +0x1ab
   > goroutine 994 [semacquire]:
   > sync.runtime_Semacquire(0xc00f99d5d4)
   > 	/usr/local/go/src/runtime/sema.go:56 +0x45
   > sync.(*WaitGroup).Wait(0xc00f99d5d4)
   > 	/usr/local/go/src/sync/waitgroup.go:130 +0x65
   > github.com/pingcap/tidb/executor.(*HashJoinExec).waitJoinWorkersAndCloseResultChan(0xc00f99d400)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:399 +0x3d
   > github.com/pingcap/tidb/util.WithRecovery(0xc011c7fc90, 0x0)
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/util/misc.go:99 +0x4f
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/join.go:342 +0x336
