# Bug ID TIDB-30326-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/30326
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              The two cases should give the same result


## Details
 * Database: tidb-v5.4.0
 * Number of scenarios: 1
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
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
   > [2024/07/02 12:29:31.130 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=5] [user=root] [host=]
   > [2024/07/02 12:29:31.133 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=28] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/07/02 12:29:31.135 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=28] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/07/02 12:29:31.136 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:58, Type:create schema, State:none, SchemaState:queueing, SchemaID:57, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 12:29:31.135 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 12:29:31.136 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:58, Type:create schema, State:none, SchemaState:queueing, SchemaID:57, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 12:29:31.135 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/02 12:29:31.136 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:58, Type:create schema, State:none, SchemaState:queueing, SchemaID:57, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:29:31.135 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:31.137 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=28] [neededSchemaVersion=29] ["start time"=121.596µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 12:29:31.139 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=29] ["take time"=2.527445ms] [job="ID:58, Type:create schema, State:done, SchemaState:public, SchemaID:57, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 12:29:31.135 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:31.140 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:58, Type:create schema, State:synced, SchemaState:public, SchemaID:57, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:29:31.135 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:31.141 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=58]
   > [2024/07/02 12:29:31.141 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 12:29:31.148 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=29] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_037irb`\n--\n\nDROP TABLE IF EXISTS `t_037irb`;"] [user=root@127.0.0.1]
   > [2024/07/02 12:29:31.149 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=29] [cur_db=testdb] [sql="CREATE TABLE `t_037irb` (\n  `c_nrh3o` int(11) DEFAULT NULL,\n  `c_nfauxb` text DEFAULT NULL,\n  `c_y5n4c` int(11) DEFAULT NULL,\n  `c_j9alg` double NOT NULL,\n  `c_4vix1d` text DEFAULT NULL,\n  `c_glkxdb` text DEFAULT NULL,\n  `c_2ykt0d` int(11) DEFAULT NULL,\n  `c_5fxv3c` double DEFAULT NULL,\n  PRIMARY KEY (`c_j9alg`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/07/02 12:29:31.150 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:60, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:59, RowCount:0, ArgLen:1, start time: 2024-07-02 12:29:31.15 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 12:29:31.150 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:60, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:59, RowCount:0, ArgLen:1, start time: 2024-07-02 12:29:31.15 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_037irb` (\n  `c_nrh3o` int(11) DEFAULT NULL,\n  `c_nfauxb` text DEFAULT NULL,\n  `c_y5n4c` int(11) DEFAULT NULL,\n  `c_j9alg` double NOT NULL,\n  `c_4vix1d` text DEFAULT NULL,\n  `c_glkxdb` text DEFAULT NULL,\n  `c_2ykt0d` int(11) DEFAULT NULL,\n  `c_5fxv3c` double DEFAULT NULL,\n  PRIMARY KEY (`c_j9alg`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/02 12:29:31.151 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:60, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:59, RowCount:0, ArgLen:0, start time: 2024-07-02 12:29:31.15 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:31.153 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=29] [neededSchemaVersion=30] ["start time"=452.228µs] [phyTblIDs="[59]"] [actionTypes="[8]"]
   > [2024/07/02 12:29:31.155 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=30] ["take time"=2.247587ms] [job="ID:60, Type:create table, State:done, SchemaState:public, SchemaID:57, TableID:59, RowCount:0, ArgLen:1, start time: 2024-07-02 12:29:31.15 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:31.156 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:60, Type:create table, State:synced, SchemaState:public, SchemaID:57, TableID:59, RowCount:0, ArgLen:0, start time: 2024-07-02 12:29:31.15 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:31.157 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=60]
   > [2024/07/02 12:29:31.157 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 12:29:31.157 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=52] ["first split key"=74800000000000003b]
   > [2024/07/02 12:29:31.158 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=30] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_037irb` DISABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/07/02 12:29:31.159 +00:00] [WARN] [2pc.go:1596] ["schemaLeaseChecker is not set for this transaction"] [sessionID=5] [startTS=450867592209104896] [commitTS=450867592209104897]
   > [2024/07/02 12:29:31.160 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=54] ["first at"=74800000000000003b] ["first new region left"="{Id:54 StartKey:7480000000000000ff3700000000000000f8 EndKey:7480000000000000ff3b00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:55 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/02 12:29:31.160 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[54]"]
   > [2024/07/02 12:29:31.161 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=30] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_037irb` ENABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/07/02 12:29:31.161 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=30] [cur_db=testdb] [sql="\n--\n-- Temporary view structure for view `t_cpsvpb`\n--\n\nDROP TABLE IF EXISTS `t_cpsvpb`;"] [user=root@127.0.0.1]
   > [2024/07/02 12:29:31.162 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=30] [cur_db=testdb] [sql="/*!50001 DROP VIEW IF EXISTS `t_cpsvpb`*/;"] [user=root@127.0.0.1]
   > [2024/07/02 12:29:31.165 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:62, Type:create view, State:none, SchemaState:queueing, SchemaID:57, TableID:61, RowCount:0, ArgLen:3, start time: 2024-07-02 12:29:31.164 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 12:29:31.165 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:62, Type:create view, State:none, SchemaState:queueing, SchemaID:57, TableID:61, RowCount:0, ArgLen:3, start time: 2024-07-02 12:29:31.164 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="/*!50001 CREATE VIEW `t_cpsvpb` AS SELECT \n 1 AS `c0`,\n 1 AS `c2`,\n 1 AS `c3`,\n 1 AS `c4`,\n 1 AS `c5`,\n 1 AS `c6`,\n 1 AS `c7`,\n 1 AS `c8`,\n 1 AS `c9`,\n 1 AS `c10`,\n 1 AS `c11`,\n 1 AS `c12`,\n 1 AS `c13`,\n 1 AS `c14`*/;"]
   > [2024/07/02 12:29:31.165 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:62, Type:create view, State:none, SchemaState:queueing, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-07-02 12:29:31.164 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:31.168 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=30] [neededSchemaVersion=31] ["start time"=554.546µs] [phyTblIDs="[61]"] [actionTypes="[2097152]"]
   > [2024/07/02 12:29:31.170 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=31] ["take time"=2.247448ms] [job="ID:62, Type:create view, State:done, SchemaState:public, SchemaID:57, TableID:61, RowCount:0, ArgLen:3, start time: 2024-07-02 12:29:31.164 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:31.171 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:62, Type:create view, State:synced, SchemaState:public, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-07-02 12:29:31.164 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:31.173 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=62]
   > [2024/07/02 12:29:31.173 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 12:29:31.173 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=31] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_x7zqmd`\n--\n\nDROP TABLE IF EXISTS `t_x7zqmd`;"] [user=root@127.0.0.1]
   > [2024/07/02 12:29:31.174 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=31] [cur_db=testdb] [sql="CREATE TABLE `t_x7zqmd` (\n  `c_8weeq` int(11) NOT NULL,\n  `c_13sfid` double DEFAULT NULL,\n  `c_hhjlmc` text DEFAULT NULL,\n  `c_3b1zld` int(11) DEFAULT NULL,\n  `c_6tu8wd` int(11) DEFAULT NULL,\n  `c_jyc_cd` double DEFAULT NULL,\n  PRIMARY KEY (`c_8weeq`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/07/02 12:29:31.176 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:64, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:63, RowCount:0, ArgLen:1, start time: 2024-07-02 12:29:31.175 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 12:29:31.176 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:64, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:63, RowCount:0, ArgLen:1, start time: 2024-07-02 12:29:31.175 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_x7zqmd` (\n  `c_8weeq` int(11) NOT NULL,\n  `c_13sfid` double DEFAULT NULL,\n  `c_hhjlmc` text DEFAULT NULL,\n  `c_3b1zld` int(11) DEFAULT NULL,\n  `c_6tu8wd` int(11) DEFAULT NULL,\n  `c_jyc_cd` double DEFAULT NULL,\n  PRIMARY KEY (`c_8weeq`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/02 12:29:31.176 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:64, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:63, RowCount:0, ArgLen:0, start time: 2024-07-02 12:29:31.175 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:31.178 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=31] [neededSchemaVersion=32] ["start time"=384.481µs] [phyTblIDs="[63]"] [actionTypes="[8]"]
   > [2024/07/02 12:29:31.179 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=32] ["take time"=2.068862ms] [job="ID:64, Type:create table, State:done, SchemaState:public, SchemaID:57, TableID:63, RowCount:0, ArgLen:1, start time: 2024-07-02 12:29:31.175 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:31.180 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:64, Type:create table, State:synced, SchemaState:public, SchemaID:57, TableID:63, RowCount:0, ArgLen:0, start time: 2024-07-02 12:29:31.175 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:31.181 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=64]
   > [2024/07/02 12:29:31.181 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 12:29:31.182 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=56] ["first split key"=74800000000000003f]
   > [2024/07/02 12:29:31.182 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=32] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_x7zqmd` DISABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/07/02 12:29:31.182 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=56] ["first at"=74800000000000003f] ["first new region left"="{Id:56 StartKey:7480000000000000ff3b00000000000000f8 EndKey:7480000000000000ff3f00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:57 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/02 12:29:31.182 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[56]"]
   > [2024/07/02 12:29:31.184 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=32] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_x7zqmd` ENABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/07/02 12:29:31.185 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=32] [cur_db=testdb] [sql="\n--\n-- Final view structure for view `t_cpsvpb`\n--\n\n/*!50001 DROP VIEW IF EXISTS `t_cpsvpb`*/;"] [user=root@127.0.0.1]
   > [2024/07/02 12:29:31.186 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:65, Type:drop view, State:none, SchemaState:queueing, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-07-02 12:29:31.185 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 12:29:31.186 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:65, Type:drop view, State:none, SchemaState:queueing, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-07-02 12:29:31.185 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="\n--\n-- Final view structure for view `t_cpsvpb`\n--\n\n/*!50001 DROP VIEW IF EXISTS `t_cpsvpb`*/;"]
   > [2024/07/02 12:29:31.186 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:drop view, State:none, SchemaState:queueing, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-07-02 12:29:31.185 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:31.188 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=32] [neededSchemaVersion=33] ["start time"=119.081µs] [phyTblIDs="[61]"] [actionTypes="[16777216]"]
   > [2024/07/02 12:29:31.190 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=33] ["take time"=2.219371ms] [job="ID:65, Type:drop view, State:running, SchemaState:write only, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-07-02 12:29:31.185 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:31.190 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:drop view, State:running, SchemaState:write only, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-07-02 12:29:31.185 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:31.191 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=33] [neededSchemaVersion=34] ["start time"=78.642µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 12:29:31.194 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=34] ["take time"=2.801575ms] [job="ID:65, Type:drop view, State:running, SchemaState:delete only, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-07-02 12:29:31.185 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:31.194 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:drop view, State:running, SchemaState:delete only, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-07-02 12:29:31.185 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:31.196 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=34] [neededSchemaVersion=35] ["start time"=79.131µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 12:29:31.198 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=35] ["take time"=2.591071ms] [job="ID:65, Type:drop view, State:done, SchemaState:queueing, SchemaID:57, TableID:61, RowCount:0, ArgLen:3, start time: 2024-07-02 12:29:31.185 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:31.199 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:drop view, State:synced, SchemaState:queueing, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-07-02 12:29:31.185 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:31.201 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=65]
   > [2024/07/02 12:29:31.201 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 12:29:31.206 +00:00] [INFO] [session.go:2108] ["Try to create a new txn inside a transaction auto commit"] [conn=5] [schemaVersion=35] [txnStartTS=450867592220639232] [txnScope=global]
   > [2024/07/02 12:29:31.208 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:67, Type:create view, State:none, SchemaState:queueing, SchemaID:57, TableID:66, RowCount:0, ArgLen:3, start time: 2024-07-02 12:29:31.207 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 12:29:31.208 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:67, Type:create view, State:none, SchemaState:queueing, SchemaID:57, TableID:66, RowCount:0, ArgLen:3, start time: 2024-07-02 12:29:31.207 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="/*!50001 CREATE ALGORITHM=UNDEFINED */\n/*!50013 DEFINER=`root`@`127.0.0.1` SQL SECURITY DEFINER */\n/*!50001 VIEW `t_cpsvpb` (`c0`, `c2`, `c3`, `c4`, `c5`, `c6`, `c7`, `c8`, `c9`, `c10`, `c11`, `c12`, `c13`, `c14`) AS SELECT DISTINCT `subq_0`.`c1` AS `c0`,`subq_0`.`c2` AS `c2`,8 AS `c3`,CASE WHEN (`subq_0`.`c3` NOT IN (SELECT `ref_2`.`c_4vix1d` AS `c0` FROM `testdb`.`t_037irb` AS `ref_2` WHERE `ref_2`.`c_2ykt0d`<=`ref_2`.`c_nrh3o`)) AND (`subq_0`.`c3`<=(SELECT (SELECT `c_hhjlmc` AS `c_hhjlmc` FROM `testdb`.`t_x7zqmd` ORDER BY `c_hhjlmc` LIMIT 4,1) AS `c0` FROM `testdb`.`t_037irb` AS `ref_3` WHERE `subq_0`.`c1`!=`ref_3`.`c_2ykt0d`)) THEN `subq_0`.`c3` ELSE `subq_0`.`c3` END AS `c4`,CASE WHEN `subq_0`.`c1`>=(SELECT MAX(`c_8weeq`) AS `max(c_8weeq)` FROM `testdb`.`t_x7zqmd`) THEN `subq_0`.`c2` ELSE `subq_0`.`c2` END AS `c5`,`subq_0`.`c1` AS `c6`,`subq_0`.`c2` AS `c7`,`subq_0`.`c3` AS `c8`,`subq_0`.`c3` AS `c9`,`subq_0`.`c2` AS `c10`,`subq_0`.`c4` AS `c11`,COUNT(CAST(`subq_0`.`c2` AS DOUBLE)) OVER (PARTITION BY `subq_0`.`c4` ORDER BY `subq_0`.`c1`) AS `c12`,`subq_0`.`c3` AS `c13`,CAST(COALESCE(`subq_0`.`c3`, _UTF8MB4'9sx3k') AS CHAR) AS `c14` FROM (SELECT COUNT(CAST(`ref_1`.`c_jyc_cd` AS DOUBLE)) AS `c0`,AVG(CAST(`ref_1`.`c_3b1zld` AS SIGNED)) AS `c1`,MIN(CAST(`ref_1`.`c_jyc_cd` AS DOUBLE)) AS `c2`,`ref_0`.`c_glkxdb` AS `c3`,COUNT(CAST(`ref_1`.`c_13sfid` AS DOUBLE)) AS `c4` FROM `testdb`.`t_037irb` AS `ref_0` JOIN `testdb`.`t_x7zqmd` AS `ref_1` WHERE `ref_0`.`c_nrh3o`>`ref_1`.`c_8weeq` GROUP BY `ref_0`.`c_glkxdb`) AS `subq_0` WHERE (SELECT `c_8weeq` AS `c_8weeq` FROM `testdb`.`t_x7zqmd` ORDER BY `c_8weeq` LIMIT 2,1) IS NOT NULL */;"]
   > [2024/07/02 12:29:31.209 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:create view, State:none, SchemaState:queueing, SchemaID:57, TableID:66, RowCount:0, ArgLen:0, start time: 2024-07-02 12:29:31.207 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:31.212 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=35] [neededSchemaVersion=36] ["start time"=624.318µs] [phyTblIDs="[66]"] [actionTypes="[2097152]"]
   > [2024/07/02 12:29:31.213 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=36] ["take time"=2.244514ms] [job="ID:67, Type:create view, State:done, SchemaState:public, SchemaID:57, TableID:66, RowCount:0, ArgLen:3, start time: 2024-07-02 12:29:31.207 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:31.215 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:create view, State:synced, SchemaState:public, SchemaID:57, TableID:66, RowCount:0, ArgLen:0, start time: 2024-07-02 12:29:31.207 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:29:31.216 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=67]
   > [2024/07/02 12:29:31.216 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 12:29:32.309 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=7] [user=root] [host=]
   > [2024/07/02 12:29:32.330 +00:00] [INFO] [set.go:139] ["set global var"] [conn=7] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/07/02 12:29:32.858 +00:00] [ERROR] [misc.go:95] ["panic in the recoverable goroutine"] [r="\"invalid memory address or nil pointer dereference\""] ["stack trace"="github.com/pingcap/tidb/util.WithRecovery.func1\n\t/go/src/github.com/pingcap/tidb/util/misc.go:97\nruntime.gopanic\n\t/usr/local/go/src/runtime/panic.go:884\nruntime.panicmem\n\t/usr/local/go/src/runtime/panic.go:260\nruntime.sigpanic\n\t/usr/local/go/src/runtime/signal_unix.go:839\ngithub.com/pingcap/tidb/executor.(*vecGroupChecker).splitIntoGroups\n\t/go/src/github.com/pingcap/tidb/executor/aggregate.go:1457\ngithub.com/pingcap/tidb/executor.(*PipelinedWindowExec).getRowsInPartition\n\t/go/src/github.com/pingcap/tidb/executor/pipelined_window.go:189\ngithub.com/pingcap/tidb/executor.(*PipelinedWindowExec).Next\n\t/go/src/github.com/pingcap/tidb/executor/pipelined_window.go:125\ngithub.com/pingcap/tidb/executor.Next\n\t/go/src/github.com/pingcap/tidb/executor/executor.go:286\ngithub.com/pingcap/tidb/executor.(*ProjectionExec).unParallelExecute\n\t/go/src/github.com/pingcap/tidb/executor/projection.go:194\ngithub.com/pingcap/tidb/executor.(*ProjectionExec).Next\n\t/go/src/github.com/pingcap/tidb/executor/projection.go:180\ngithub.com/pingcap/tidb/executor.Next\n\t/go/src/github.com/pingcap/tidb/executor/executor.go:286\ngithub.com/pingcap/tidb/executor.(*CTEExec).computeSeedPart\n\t/go/src/github.com/pingcap/tidb/executor/cte.go:226\ngithub.com/pingcap/tidb/executor.(*CTEExec).Next\n\t/go/src/github.com/pingcap/tidb/executor/cte.go:161\ngithub.com/pingcap/tidb/executor.Next\n\t/go/src/github.com/pingcap/tidb/executor/executor.go:286\ngithub.com/pingcap/tidb/executor.(*SelectionExec).Next\n\t/go/src/github.com/pingcap/tidb/executor/executor.go:1317\ngithub.com/pingcap/tidb/executor.Next\n\t/go/src/github.com/pingcap/tidb/executor/executor.go:286\ngithub.com/pingcap/tidb/executor.(*HashJoinExec).fetchBuildSideRows\n\t/go/src/github.com/pingcap/tidb/executor/join.go:266\ngithub.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable.func2\n\t/go/src/github.com/pingcap/tidb/executor/join.go:715\ngithub.com/pingcap/tidb/util.WithRecovery\n\t/go/src/github.com/pingcap/tidb/util/misc.go:100"]
   > runtime: goroutine stack exceeds 1000000000-byte limit
   > runtime: sp=0xc032960390 stack=[0xc032960000, 0xc052960000]
   > fatal error: stack overflow
   > runtime stack:
   > runtime.throw({0x3aa773d?, 0x590b5c0?})
   > 	/usr/local/go/src/runtime/panic.go:1047 +0x5d fp=0x7f44944a9888 sp=0x7f44944a9858 pc=0x13b859d
   > runtime.newstack()
   > 	/usr/local/go/src/runtime/stack.go:1103 +0x5cc fp=0x7f44944a9a40 sp=0x7f44944a9888 pc=0x13d35ec
   > runtime.morestack()
   > 	/usr/local/go/src/runtime/asm_amd64.s:570 +0x8b fp=0x7f44944a9a48 sp=0x7f44944a9a40 pc=0x13ec60b
   > goroutine 1307 [running]:
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60?, 0xc011aae7e0?}, {0x4012e60?, 0xc011aae7e0?})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:183 +0x12c fp=0xc0329603a0 sp=0xc032960398 pc=0x1f5780c
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011aae780}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329603d8 sp=0xc0329603a0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01251f200}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960410 sp=0xc0329603d8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01076f8c0}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960448 sp=0xc032960410 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01262c190}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960480 sp=0xc032960448 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc012514470}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329604b8 sp=0xc032960480 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc012499c80}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329604f0 sp=0xc0329604b8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011aa4430}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960528 sp=0xc0329604f0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc012534260}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960560 sp=0xc032960528 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011aaee40}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960598 sp=0xc032960560 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011aa4260}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329605d0 sp=0xc032960598 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011aae7e0}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960608 sp=0xc0329605d0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011aae780}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960640 sp=0xc032960608 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01251f200}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960678 sp=0xc032960640 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01076f8c0}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329606b0 sp=0xc032960678 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01262c190}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329606e8 sp=0xc0329606b0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc012514470}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960720 sp=0xc0329606e8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc012499c80}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960758 sp=0xc032960720 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011aa4430}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960790 sp=0xc032960758 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc012534260}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329607c8 sp=0xc032960790 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011aaee40}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960800 sp=0xc0329607c8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011aa4260}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960838 sp=0xc032960800 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011aae7e0}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960870 sp=0xc032960838 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011aae780}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329608a8 sp=0xc032960870 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01251f200}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329608e0 sp=0xc0329608a8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01076f8c0}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960918 sp=0xc0329608e0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01262c190}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960950 sp=0xc032960918 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc012514470}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960988 sp=0xc032960950 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc012499c80}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329609c0 sp=0xc032960988 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011aa4430}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329609f8 sp=0xc0329609c0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc012534260}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960a30 sp=0xc0329609f8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011aaee40}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960a68 sp=0xc032960a30 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011aa4260}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960aa0 sp=0xc032960a68 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011aae7e0}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960ad8 sp=0xc032960aa0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011aae780}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960b10 sp=0xc032960ad8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01251f200}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960b48 sp=0xc032960b10 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01076f8c0}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960b80 sp=0xc032960b48 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01262c190}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960bb8 sp=0xc032960b80 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc012514470}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960bf0 sp=0xc032960bb8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc012499c80}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960c28 sp=0xc032960bf0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011aa4430}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960c60 sp=0xc032960c28 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc012534260}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960c98 sp=0xc032960c60 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011aaee40}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960cd0 sp=0xc032960c98 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011aa4260}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960d08 sp=0xc032960cd0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011aae7e0}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960d40 sp=0xc032960d08 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011aae780}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960d78 sp=0xc032960d40 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01251f200}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960db0 sp=0xc032960d78 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01076f8c0}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960de8 sp=0xc032960db0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01262c190}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960e20 sp=0xc032960de8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc012514470}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960e58 sp=0xc032960e20 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc012499c80}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960e90 sp=0xc032960e58 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011aa4430}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960ec8 sp=0xc032960e90 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc012534260}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960f00 sp=0xc032960ec8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011aaee40}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960f38 sp=0xc032960f00 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011aa4260}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960f70 sp=0xc032960f38 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011aae7e0}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960fa8 sp=0xc032960f70 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011aae780}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032960fe0 sp=0xc032960fa8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01251f200}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032961018 sp=0xc032960fe0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01076f8c0}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032961050 sp=0xc032961018 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01262c190}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032961088 sp=0xc032961050 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc012514470}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329610c0 sp=0xc032961088 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc012499c80}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329610f8 sp=0xc0329610c0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011aa4430}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032961130 sp=0xc0329610f8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc012534260}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032961168 sp=0xc032961130 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011aaee40}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329611a0 sp=0xc032961168 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011aa4260}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329611d8 sp=0xc0329611a0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011aae7e0}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032961210 sp=0xc0329611d8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011aae780}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032961248 sp=0xc032961210 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01251f200}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032961280 sp=0xc032961248 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01076f8c0}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329612b8 sp=0xc032961280 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01262c190}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329612f0 sp=0xc0329612b8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc012514470}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032961328 sp=0xc0329612f0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc012499c80}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032961360 sp=0xc032961328 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011aa4430}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032961398 sp=0xc032961360 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc012534260}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329613d0 sp=0xc032961398 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011aaee40}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032961408 sp=0xc0329613d0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011aa4260}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032961440 sp=0xc032961408 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011aae7e0}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032961478 sp=0xc032961440 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011aae780}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329614b0 sp=0xc032961478 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01251f200}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329614e8 sp=0xc0329614b0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01076f8c0}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032961520 sp=0xc0329614e8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01262c190}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032961558 sp=0xc032961520 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc012514470}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032961590 sp=0xc032961558 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc012499c80}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329615c8 sp=0xc032961590 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011aa4430}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032961600 sp=0xc0329615c8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc012534260}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032961638 sp=0xc032961600 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011aaee40}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032961670 sp=0xc032961638 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011aa4260}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329616a8 sp=0xc032961670 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011aae7e0}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329616e0 sp=0xc0329616a8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011aae780}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032961718 sp=0xc0329616e0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01251f200}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032961750 sp=0xc032961718 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc01076f8c0}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032961788 sp=0xc032961750 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc01262c190}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329617c0 sp=0xc032961788 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc012514470}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329617f8 sp=0xc0329617c0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc012499c80}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032961830 sp=0xc0329617f8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011aa4430}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032961868 sp=0xc032961830 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc012534260}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329618a0 sp=0xc032961868 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011aaee40}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc0329618d8 sp=0xc0329618a0 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e20, 0xc011aa4260}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032961910 sp=0xc0329618d8 pc=0x1f577a5
   > github.com/pingcap/tidb/util/memory.reArrangeFallback({0x4012e60, 0xc011aae7e0}, {0x4012e60, 0xc011aae7e0})
   > 	/go/src/github.com/pingcap/tidb/util/memory/tracker.go:194 +0xc5 fp=0xc032961948 sp=0xc032961910 pc=0x1f577a5
   > ...additional frames elided...
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:712 +0x22d
   > goroutine 1 [chan receive]:
   > runtime.gopark(0xc01151af60?, 0xc010df5dc0?, 0xbf?, 0xc1?, 0x37fc5c0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010df5d40 sp=0xc010df5d20 pc=0x13bb516
   > runtime.chanrecv(0xc010bb66c0, 0xc010df5e30, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc010df5dd0 sp=0xc010df5d40 pc=0x13854bb
   > runtime.chanrecv1(0xc01056e5b0?, 0x0?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc010df5df8 sp=0xc010df5dd0 pc=0x1384fb8
   > github.com/pingcap/tidb/server.(*Server).Run(0xc01056e5b0)
   > 	/go/src/github.com/pingcap/tidb/server/server.go:370 +0x1f0 fp=0xc010df5e50 sp=0xc010df5df8 pc=0x31e23d0
   > main.main()
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:213 +0x539 fp=0xc010df5f80 sp=0xc010df5e50 pc=0x33af4b9
   > runtime.main()
   > 	/usr/local/go/src/runtime/proc.go:250 +0x212 fp=0xc010df5fe0 sp=0xc010df5f80 pc=0x13bb152
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010df5fe8 sp=0xc010df5fe0 pc=0x13ee6e1
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
   > goroutine 18 [GC worker (idle)]:
   > runtime.gopark(0x21e4c83e2a4d?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008a750 sp=0xc00008a730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008a7e0 sp=0xc00008a750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008a7e8 sp=0xc00008a7e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 19 [GC worker (idle)]:
   > runtime.gopark(0x21e4c83d0e05?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008af50 sp=0xc00008af30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008afe0 sp=0xc00008af50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008afe8 sp=0xc00008afe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 20 [GC worker (idle)]:
   > runtime.gopark(0x5f8be00?, 0x1?, 0xea?, 0x35?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008b750 sp=0xc00008b730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008b7e0 sp=0xc00008b750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008b7e8 sp=0xc00008b7e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 21 [GC worker (idle)]:
   > runtime.gopark(0x21e4c82d20fd?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008bf50 sp=0xc00008bf30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008bfe0 sp=0xc00008bf50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008bfe8 sp=0xc00008bfe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 22 [GC worker (idle)]:
   > runtime.gopark(0x21e4c84874ee?, 0x3?, 0x30?, 0xe4?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008c750 sp=0xc00008c730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008c7e0 sp=0xc00008c750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008c7e8 sp=0xc00008c7e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 23 [GC worker (idle)]:
   > runtime.gopark(0x21e4c83d174c?, 0x3?, 0x9b?, 0xf?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008cf50 sp=0xc00008cf30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008cfe0 sp=0xc00008cf50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008cfe8 sp=0xc00008cfe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 24 [GC worker (idle)]:
   > runtime.gopark(0x21e4c83d2236?, 0x3?, 0xb4?, 0x22?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008d750 sp=0xc00008d730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008d7e0 sp=0xc00008d750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008d7e8 sp=0xc00008d7e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 34 [GC worker (idle)]:
   > runtime.gopark(0x21e4c83d174c?, 0x3?, 0xe8?, 0x5f?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000114750 sp=0xc000114730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0001147e0 sp=0xc000114750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0001147e8 sp=0xc0001147e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 35 [GC worker (idle)]:
   > runtime.gopark(0x21e4c84c5bff?, 0x1?, 0xf3?, 0x73?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000691f50 sp=0xc000691f30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc000691fe0 sp=0xc000691f50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000691fe8 sp=0xc000691fe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 25 [GC worker (idle)]:
   > runtime.gopark(0x21e4c83d04bf?, 0x3?, 0x50?, 0x75?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00008df50 sp=0xc00008df30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc00008dfe0 sp=0xc00008df50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00008dfe8 sp=0xc00008dfe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 7 [GC worker (idle)]:
   > runtime.gopark(0x21e4c83d04bf?, 0x1?, 0xdf?, 0x67?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000090f50 sp=0xc000090f30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc000090fe0 sp=0xc000090f50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000090fe8 sp=0xc000090fe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 36 [GC worker (idle)]:
   > runtime.gopark(0x21e4c83def5f?, 0x3?, 0xf4?, 0x44?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000115750 sp=0xc000115730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0001157e0 sp=0xc000115750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0001157e8 sp=0xc0001157e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 8 [GC worker (idle)]:
   > runtime.gopark(0x21e4c840b540?, 0x1?, 0x4a?, 0x52?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000091750 sp=0xc000091730 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc0000917e0 sp=0xc000091750 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000917e8 sp=0xc0000917e0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 37 [GC worker (idle)]:
   > runtime.gopark(0x21e4c83d0e05?, 0x3?, 0xea?, 0x6d?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000115f50 sp=0xc000115f30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc000115fe0 sp=0xc000115f50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000115fe8 sp=0xc000115fe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 9 [GC worker (idle)]:
   > runtime.gopark(0x21e4c83d04bf?, 0x3?, 0x87?, 0xa6?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000091f50 sp=0xc000091f30 pc=0x13bb516
   > runtime.gcBgMarkWorker()
   > 	/usr/local/go/src/runtime/mgc.go:1235 +0xf1 fp=0xc000091fe0 sp=0xc000091f50 pc=0x139af51
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000091fe8 sp=0xc000091fe0 pc=0x13ee6e1
   > created by runtime.gcBgMarkStartWorkers
   > 	/usr/local/go/src/runtime/mgc.go:1159 +0x25
   > goroutine 267 [select]:
   > runtime.gopark(0xc000112708?, 0x2?, 0x0?, 0x0?, 0xc0001126e4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000112568 sp=0xc000112548 pc=0x13bb516
   > runtime.selectgo(0xc000112708, 0xc0001126e0, 0xc0000061a0?, 0x0, 0xc0000061a0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0001126a8 sp=0xc000112568 pc=0x13cbbdc
   > github.com/pingcap/badger.(*blobGCHandler).run(0xc000c521c0, 0xc000dea048)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/blob.go:468 +0xd6 fp=0xc0001127c0 sp=0xc0001126a8 pc=0x3288896
   > github.com/pingcap/badger.(*blobManager).Open.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/blob.go:292 +0x2a fp=0xc0001127e0 sp=0xc0001127c0 pc=0x328754a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0001127e8 sp=0xc0001127e0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.(*blobManager).Open
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/blob.go:292 +0x5bd
   > goroutine 11 [select]:
   > runtime.gopark(0xc000111f88?, 0x3?, 0x78?, 0xc5?, 0xc000111f72?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000111df8 sp=0xc000111dd8 pc=0x13bb516
   > runtime.selectgo(0xc000111f88, 0xc000111f6c, 0xc0008e5680?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000111f38 sp=0xc000111df8 pc=0x13cbbdc
   > go.opencensus.io/stats/view.(*worker).start(0xc0008e5680)
   > 	/go/pkg/mod/go.opencensus.io@v0.23.0/stats/view/worker.go:276 +0xad fp=0xc000111fc8 sp=0xc000111f38 pc=0x29900cd
   > go.opencensus.io/stats/view.init.0.func1()
   > 	/go/pkg/mod/go.opencensus.io@v0.23.0/stats/view/worker.go:34 +0x26 fp=0xc000111fe0 sp=0xc000111fc8 pc=0x298f346
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000111fe8 sp=0xc000111fe0 pc=0x13ee6e1
   > created by go.opencensus.io/stats/view.init.0
   > 	/go/pkg/mod/go.opencensus.io@v0.23.0/stats/view/worker.go:34 +0x8d
   > goroutine 134 [chan receive]:
   > runtime.gopark(0xc0000bc480?, 0x13c1374?, 0x10?, 0xfe?, 0x13d8de5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00009fdb8 sp=0xc00009fd98 pc=0x13bb516
   > runtime.chanrecv(0xc00068c1e0, 0xc00009ff28, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc00009fe48 sp=0xc00009fdb8 pc=0x13854bb
   > runtime.chanrecv2(0x3b9aca00?, 0x13bb600?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc00009fe70 sp=0xc00009fe48 pc=0x1384ff8
   > go.etcd.io/etcd/pkg/logutil.(*MergeLogger).outputLoop(0xc000536e40)
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:173 +0x8c fp=0xc00009ffc8 sp=0xc00009fe70 pc=0x1a12c4c
   > go.etcd.io/etcd/pkg/logutil.NewMergeLogger.func1()
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:91 +0x26 fp=0xc00009ffe0 sp=0xc00009ffc8 pc=0x1a124c6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00009ffe8 sp=0xc00009ffe0 pc=0x13ee6e1
   > created by go.etcd.io/etcd/pkg/logutil.NewMergeLogger
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:91 +0xb6
   > goroutine 443 [chan receive]:
   > runtime.gopark(0xc000906148?, 0x2?, 0x78?, 0x9e?, 0x13d8de5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000695e20 sp=0xc000695e00 pc=0x13bb516
   > runtime.chanrecv(0xc00068db60, 0x0, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000695eb0 sp=0xc000695e20 pc=0x13854bb
   > runtime.chanrecv1(0xdf8475800?, 0x1b?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc000695ed8 sp=0xc000695eb0 pc=0x1384fb8
   > github.com/pingcap/tidb/util/profile.HeapProfileForGlobalMemTracker(0xc000d9afc0?)
   > 	/go/src/github.com/pingcap/tidb/util/profile/trackerRecorder.go:33 +0xa7 fp=0xc000695fc8 sp=0xc000695ed8 pc=0x267adc7
   > main.setHeapProfileTracker.func1()
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:279 +0x26 fp=0xc000695fe0 sp=0xc000695fc8 pc=0x33afc46
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000695fe8 sp=0xc000695fe0 pc=0x13ee6e1
   > created by main.setHeapProfileTracker
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:279 +0xa5
   > goroutine 178 [chan receive]:
   > runtime.gopark(0xc00068c540?, 0x1?, 0x10?, 0x96?, 0x13d8de5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000a095b8 sp=0xc000a09598 pc=0x13bb516
   > runtime.chanrecv(0xc00068c4e0, 0xc000a09728, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000a09648 sp=0xc000a095b8 pc=0x13854bb
   > runtime.chanrecv2(0x3b9aca00?, 0x13bb600?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc000a09670 sp=0xc000a09648 pc=0x1384ff8
   > go.etcd.io/etcd/pkg/logutil.(*MergeLogger).outputLoop(0xc00061f2c0)
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:173 +0x8c fp=0xc000a097c8 sp=0xc000a09670 pc=0x1a12c4c
   > go.etcd.io/etcd/pkg/logutil.NewMergeLogger.func1()
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:91 +0x26 fp=0xc000a097e0 sp=0xc000a097c8 pc=0x1a124c6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000a097e8 sp=0xc000a097e0 pc=0x13ee6e1
   > created by go.etcd.io/etcd/pkg/logutil.NewMergeLogger
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:91 +0xb6
   > goroutine 181 [chan receive]:
   > runtime.gopark(0xc0000bc5a0?, 0x1?, 0x10?, 0x9e?, 0x13d8de5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000a09db8 sp=0xc000a09d98 pc=0x13bb516
   > runtime.chanrecv(0xc0000bc360, 0xc000a09f28, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000a09e48 sp=0xc000a09db8 pc=0x13854bb
   > runtime.chanrecv2(0x3b9aca00?, 0x13bb600?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc000a09e70 sp=0xc000a09e48 pc=0x1384ff8
   > go.etcd.io/etcd/pkg/logutil.(*MergeLogger).outputLoop(0xc00061f3f8)
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:173 +0x8c fp=0xc000a09fc8 sp=0xc000a09e70 pc=0x1a12c4c
   > go.etcd.io/etcd/pkg/logutil.NewMergeLogger.func1()
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:91 +0x26 fp=0xc000a09fe0 sp=0xc000a09fc8 pc=0x1a124c6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000a09fe8 sp=0xc000a09fe0 pc=0x13ee6e1
   > created by go.etcd.io/etcd/pkg/logutil.NewMergeLogger
   > 	/go/pkg/mod/go.etcd.io/etcd@v0.5.0-alpha.5.0.20210512015243-d19fbe541bf9/pkg/logutil/merge_logger.go:91 +0xb6
   > goroutine 444 [chan receive]:
   > runtime.gopark(0xc000bd22a0?, 0x13c1374?, 0x38?, 0xfe?, 0x13d8de5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000cbfde0 sp=0xc000cbfdc0 pc=0x13bb516
   > runtime.chanrecv(0xc0008f9f20, 0x0, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000cbfe70 sp=0xc000cbfde0 pc=0x13854bb
   > runtime.chanrecv1(0x5f5e100?, 0x3ace4e4?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc000cbfe98 sp=0xc000cbfe70 pc=0x1384fb8
   > github.com/pingcap/tidb/util/systimemon.StartMonitor(0x3bccd98, 0x3bcc3f0, 0xc000d96da0)
   > 	/go/src/github.com/pingcap/tidb/util/systimemon/systime_mon.go:32 +0x185 fp=0xc000cbffb8 sp=0xc000cbfe98 pc=0x33ac665
   > main.setupMetrics.func3()
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:696 +0x31 fp=0xc000cbffe0 sp=0xc000cbffb8 pc=0x33b2df1
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000cbffe8 sp=0xc000cbffe0 pc=0x13ee6e1
   > created by main.setupMetrics
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:696 +0x115
   > goroutine 445 [select]:
   > runtime.gopark(0xc000a0b780?, 0x2?, 0x0?, 0x30?, 0xc000a0b74c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00009cdd0 sp=0xc00009cdb0 pc=0x13bb516
   > runtime.selectgo(0xc00009cf80, 0xc000a0b748, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00009cf10 sp=0xc00009cdd0 pc=0x13cbbdc
   > github.com/pingcap/badger.(*DB).updateSize(0x0?, 0xc000dea108)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:1039 +0x105 fp=0xc00009cfc0 sp=0xc00009cf10 pc=0x329a445
   > github.com/pingcap/badger.Open.func5()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:328 +0x2a fp=0xc00009cfe0 sp=0xc00009cfc0 pc=0x329450a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00009cfe8 sp=0xc00009cfe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.Open
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:328 +0xf5c
   > goroutine 446 [select]:
   > runtime.gopark(0xc000a0bf88?, 0x2?, 0x20?, 0x0?, 0xc000a0bf64?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000a0bde8 sp=0xc000a0bdc8 pc=0x13bb516
   > runtime.selectgo(0xc000a0bf88, 0xc000a0bf60, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000a0bf28 sp=0xc000a0bde8 pc=0x13cbbdc
   > github.com/pingcap/badger/epoch.(*ResourceManager).collectLoop(0x0?, 0xc000dea138)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/epoch/manager.go:101 +0xd3 fp=0xc000a0bfc0 sp=0xc000a0bf28 pc=0x3257a13
   > github.com/pingcap/badger/epoch.NewResourceManager.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/epoch/manager.go:79 +0x2a fp=0xc000a0bfe0 sp=0xc000a0bfc0 pc=0x32577aa
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000a0bfe8 sp=0xc000a0bfe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger/epoch.NewResourceManager
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/epoch/manager.go:79 +0xdd
   > goroutine 447 [select]:
   > runtime.gopark(0xc000cbbe68?, 0x2?, 0xd8?, 0x41?, 0xc000cbbe3c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000cbbcc0 sp=0xc000cbbca0 pc=0x13bb516
   > runtime.selectgo(0xc000cbbe68, 0xc000cbbe38, 0x0?, 0x1, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000cbbe00 sp=0xc000cbbcc0 pc=0x13cbbdc
   > github.com/pingcap/badger.Open.func4()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:342 +0x155 fp=0xc000cbbfe0 sp=0xc000cbbe00 pc=0x3294495
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000cbbfe8 sp=0xc000cbbfe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.Open
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:339 +0x11f8
   > goroutine 268 [select]:
   > runtime.gopark(0xc000116760?, 0x2?, 0x4?, 0x30?, 0xc00011672c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000116598 sp=0xc000116578 pc=0x13bb516
   > runtime.selectgo(0xc000116760, 0xc000116728, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0001166d8 sp=0xc000116598 pc=0x13cbbdc
   > github.com/pingcap/badger.(*levelsController).runWorker(0xc0001662a0, 0xc000dea078, 0x0)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:212 +0x1fb fp=0xc0001167b8 sp=0xc0001166d8 pc=0x32a297b
   > github.com/pingcap/badger.(*levelsController).startCompact.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:180 +0x2e fp=0xc0001167e0 sp=0xc0001167b8 pc=0x32a274e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0001167e8 sp=0xc0001167e0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.(*levelsController).startCompact
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:180 +0x65
   > goroutine 269 [select]:
   > runtime.gopark(0xc000116f60?, 0x2?, 0x4?, 0x30?, 0xc000116f2c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000116d98 sp=0xc000116d78 pc=0x13bb516
   > runtime.selectgo(0xc000116f60, 0xc000116f28, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000116ed8 sp=0xc000116d98 pc=0x13cbbdc
   > github.com/pingcap/badger.(*levelsController).runWorker(0xc0001662a0, 0xc000dea078, 0x0)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:212 +0x1fb fp=0xc000116fb8 sp=0xc000116ed8 pc=0x32a297b
   > github.com/pingcap/badger.(*levelsController).startCompact.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:180 +0x2e fp=0xc000116fe0 sp=0xc000116fb8 pc=0x32a274e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000116fe8 sp=0xc000116fe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.(*levelsController).startCompact
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:180 +0x65
   > goroutine 270 [select]:
   > runtime.gopark(0xc000117760?, 0x2?, 0x4?, 0x30?, 0xc00011772c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000117598 sp=0xc000117578 pc=0x13bb516
   > runtime.selectgo(0xc000117760, 0xc000117728, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0001176d8 sp=0xc000117598 pc=0x13cbbdc
   > github.com/pingcap/badger.(*levelsController).runWorker(0xc0001662a0, 0xc000dea078, 0x1)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:212 +0x1fb fp=0xc0001177b8 sp=0xc0001176d8 pc=0x32a297b
   > github.com/pingcap/badger.(*levelsController).startCompact.func1()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:180 +0x2e fp=0xc0001177e0 sp=0xc0001177b8 pc=0x32a274e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0001177e8 sp=0xc0001177e0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.(*levelsController).startCompact
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/levels.go:180 +0x65
   > goroutine 271 [chan receive]:
   > runtime.gopark(0x0?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00009eac0 sp=0xc00009eaa0 pc=0x13bb516
   > runtime.chanrecv(0xc000d9bce0, 0xc00009ec60, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc00009eb50 sp=0xc00009eac0 pc=0x13854bb
   > runtime.chanrecv2(0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc00009eb78 sp=0xc00009eb50 pc=0x1384ff8
   > github.com/pingcap/badger.(*DB).runFlushMemTable(0xc000dd0d80, 0x0?)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:920 +0xdd fp=0xc00009efc0 sp=0xc00009eb78 pc=0x3298efd
   > github.com/pingcap/badger.Open.func6()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:361 +0x2a fp=0xc00009efe0 sp=0xc00009efc0 pc=0x329430a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00009efe8 sp=0xc00009efe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.Open
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/db.go:361 +0x158d
   > goroutine 448 [select]:
   > runtime.gopark(0xc000cbef78?, 0x3?, 0x25?, 0x48?, 0xc000cbef32?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000cbed98 sp=0xc000cbed78 pc=0x13bb516
   > runtime.selectgo(0xc000cbef78, 0xc000cbef2c, 0x1?, 0x0, 0xc000241860?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000cbeed8 sp=0xc000cbed98 pc=0x13cbbdc
   > github.com/pingcap/badger.(*writeWorker).runWriteVLog(0xc000c180e0, 0xc000dea0d8)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:94 +0x137 fp=0xc000cbefc0 sp=0xc000cbeed8 pc=0x32b28b7
   > github.com/pingcap/badger.startWriteWorker.func2()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:64 +0x2a fp=0xc000cbefe0 sp=0xc000cbefc0 pc=0x32b238a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000cbefe8 sp=0xc000cbefe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.startWriteWorker
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:64 +0x1f9
   > goroutine 449 [chan receive, locked to thread]:
   > runtime.gopark(0xc000cb8e98?, 0x1456628?, 0xf?, 0x0?, 0x1?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000cb8e68 sp=0xc000cb8e48 pc=0x13bb516
   > runtime.chanrecv(0xc00068c240, 0xc000cb8f88, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc000cb8ef8 sp=0xc000cb8e68 pc=0x13854bb
   > runtime.chanrecv2(0xc000d91e60?, 0x3ef52a19eb1ed899?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc000cb8f20 sp=0xc000cb8ef8 pc=0x1384ff8
   > github.com/pingcap/badger.(*writeWorker).runWriteLSM(0xc000c180e0, 0xc000dea108?)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:141 +0x15e fp=0xc000cb8fc0 sp=0xc000cb8f20 pc=0x32b2efe
   > github.com/pingcap/badger.startWriteWorker.func3()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:65 +0x2a fp=0xc000cb8fe0 sp=0xc000cb8fc0 pc=0x32b232a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000cb8fe8 sp=0xc000cb8fe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.startWriteWorker
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:65 +0x24d
   > goroutine 466 [chan receive]:
   > runtime.gopark(0x0?, 0x0?, 0x0?, 0x0?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0000a1ea8 sp=0xc0000a1e88 pc=0x13bb516
   > runtime.chanrecv(0xc00068c2a0, 0xc0000a1f88, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc0000a1f38 sp=0xc0000a1ea8 pc=0x13854bb
   > runtime.chanrecv2(0xc000c18040?, 0x0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc0000a1f60 sp=0xc0000a1f38 pc=0x1384ff8
   > github.com/pingcap/badger.(*writeWorker).runMergeLSM(0x3bcc3f0?, 0xc000d96da0?)
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:154 +0x9b fp=0xc0000a1fc0 sp=0xc0000a1f60 pc=0x32b307b
   > github.com/pingcap/badger.startWriteWorker.func4()
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:66 +0x2a fp=0xc0000a1fe0 sp=0xc0000a1fc0 pc=0x32b22ca
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000a1fe8 sp=0xc0000a1fe0 pc=0x13ee6e1
   > created by github.com/pingcap/badger.startWriteWorker
   > 	/go/pkg/mod/github.com/pingcap/badger@v1.5.1-0.20210831093107-2f6cb8008145/writer.go:66 +0x2a5
   > goroutine 467 [select]:
   > runtime.gopark(0xc000cb9f88?, 0x2?, 0x0?, 0x0?, 0xc000cb9f4c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000cb9da0 sp=0xc000cb9d80 pc=0x13bb516
   > runtime.selectgo(0xc000cb9f88, 0xc000cb9f48, 0xc000908cd8?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000cb9ee0 sp=0xc000cb9da0 pc=0x13cbbdc
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.writeDBWorker.run({0xc00068c360?, 0xc000dae040?})
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:96 +0x145 fp=0xc000cb9fc0 sp=0xc000cb9ee0 pc=0x3308de5
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*dbWriter).Open.func1()
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:202 +0x2a fp=0xc000cb9fe0 sp=0xc000cb9fc0 pc=0x330996a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000cb9fe8 sp=0xc000cb9fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*dbWriter).Open
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:199 +0xc5
   > goroutine 468 [select]:
   > runtime.gopark(0xc00009de70?, 0x2?, 0x90?, 0xde?, 0xc00009de1c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00009dc58 sp=0xc00009dc38 pc=0x13bb516
   > runtime.selectgo(0xc00009de70, 0xc00009de18, 0x23?, 0x0, 0xc010aa2d20?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00009dd98 sp=0xc00009dc58 pc=0x13cbbdc
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.writeLockWorker.run({0xc00068c3c0?, 0xc000dae040?})
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:148 +0x15f fp=0xc00009dfc0 sp=0xc00009dd98 pc=0x33093bf
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*dbWriter).Open.func2()
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:209 +0x2a fp=0xc00009dfe0 sp=0xc00009dfc0 pc=0x330990a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00009dfe8 sp=0xc00009dfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*dbWriter).Open
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/write.go:206 +0x159
   > goroutine 469 [select]:
   > runtime.gopark(0xc000a0e718?, 0x2?, 0x0?, 0x0?, 0xc000a0e704?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000a0e588 sp=0xc000a0e568 pc=0x13bb516
   > runtime.selectgo(0xc000a0e718, 0xc000a0e700, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000a0e6c8 sp=0xc000a0e588 pc=0x13cbbdc
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*MVCCStore).runUpdateSafePointLoop(0xc000c15400)
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:1550 +0x217 fp=0xc000a0e7c8 sp=0xc000a0e6c8 pc=0x32facd7
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.NewMVCCStore.func1()
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:85 +0x26 fp=0xc000a0e7e0 sp=0xc000a0e7c8 pc=0x32ed406
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000a0e7e8 sp=0xc000a0e7e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.NewMVCCStore
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:85 +0x337
   > goroutine 470 [select]:
   > runtime.gopark(0xc000a0efb0?, 0x2?, 0x0?, 0x0?, 0xc000a0ef9c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000a0ee28 sp=0xc000a0ee08 pc=0x13bb516
   > runtime.selectgo(0xc000a0efb0, 0xc000a0ef98, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000a0ef68 sp=0xc000a0ee28 pc=0x13cbbdc
   > github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*MVCCStore).StartDeadlockDetection.func1()
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:1286 +0x7b fp=0xc000a0efe0 sp=0xc000a0ef68 pc=0x32f895b
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000a0efe8 sp=0xc000a0efe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/store/mockstore/unistore/tikv.(*MVCCStore).StartDeadlockDetection
   > 	/go/src/github.com/pingcap/tidb/store/mockstore/unistore/tikv/mvcc.go:1284 +0xb6
   > goroutine 471 [select]:
   > runtime.gopark(0xc0000a2f78?, 0x2?, 0x0?, 0x30?, 0xc0000a2f3c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0000a2dc0 sp=0xc0000a2da0 pc=0x13bb516
   > runtime.selectgo(0xc0000a2f78, 0xc0000a2f38, 0xc000a0b7b0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0000a2f00 sp=0xc0000a2dc0 pc=0x13cbbdc
   > github.com/tikv/client-go/v2/oracle/oracles.(*pdOracle).updateTS(0xc0008e22a0, {0x400d640, 0xc00005c058}, 0xc000dea108?)
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/oracle/oracles/pd.go:229 +0x128 fp=0xc0000a2fb0 sp=0xc0000a2f00 pc=0x1e9b548
   > github.com/tikv/client-go/v2/oracle/oracles.NewPdOracle.func1()
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/oracle/oracles/pd.go:77 +0x32 fp=0xc0000a2fe0 sp=0xc0000a2fb0 pc=0x1e9a772
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000a2fe8 sp=0xc0000a2fe0 pc=0x13ee6e1
   > created by github.com/tikv/client-go/v2/oracle/oracles.NewPdOracle
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/oracle/oracles/pd.go:77 +0x119
   > goroutine 472 [select]:
   > runtime.gopark(0xc000113f78?, 0x3?, 0x0?, 0xbe?, 0xc000113f5a?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000113de0 sp=0xc000113dc0 pc=0x13bb516
   > runtime.selectgo(0xc000113f78, 0xc000113f54, 0x1000200000000?, 0x0, 0xc0009ca2d8?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000113f20 sp=0xc000113de0 pc=0x13cbbdc
   > github.com/tikv/client-go/v2/internal/locate.(*RegionCache).asyncCheckAndResolveLoop(0xc000c15d00, 0xc000dea0d8?)
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/internal/locate/region_cache.go:399 +0xd1 fp=0xc000113fc0 sp=0xc000113f20 pc=0x1e6bff1
   > github.com/tikv/client-go/v2/internal/locate.NewRegionCache.func1()
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/internal/locate/region_cache.go:370 +0x2a fp=0xc000113fe0 sp=0xc000113fc0 pc=0x1e6bc6a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000113fe8 sp=0xc000113fe0 pc=0x13ee6e1
   > created by github.com/tikv/client-go/v2/internal/locate.NewRegionCache
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/internal/locate/region_cache.go:370 +0x2e6
   > goroutine 473 [select]:
   > runtime.gopark(0xc000a0f710?, 0x2?, 0x11?, 0x30?, 0xc000a0f6ac?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000693d10 sp=0xc000693cf0 pc=0x13bb516
   > runtime.selectgo(0xc000693f10, 0xc000a0f6a8, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000693e50 sp=0xc000693d10 pc=0x13cbbdc
   > github.com/tikv/client-go/v2/tikv.(*KVStore).runSafePointChecker(0xc000ca4120)
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/tikv/kv.go:264 +0x12b fp=0xc000693fc8 sp=0xc000693e50 pc=0x1ed6f0b
   > github.com/tikv/client-go/v2/tikv.NewKVStore.func1()
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/tikv/kv.go:187 +0x26 fp=0xc000693fe0 sp=0xc000693fc8 pc=0x1ed6d06
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000693fe8 sp=0xc000693fe0 pc=0x13ee6e1
   > created by github.com/tikv/client-go/v2/tikv.NewKVStore
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/tikv/kv.go:187 +0x3d6
   > goroutine 474 [select]:
   > runtime.gopark(0xc011e36f80?, 0x2?, 0x0?, 0xbe?, 0xc011e36f44?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc011e36dc8 sp=0xc011e36da8 pc=0x13bb516
   > runtime.selectgo(0xc011e36f80, 0xc011e36f40, 0xc000c520c0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc011e36f08 sp=0xc011e36dc8 pc=0x13cbbdc
   > github.com/tikv/client-go/v2/tikv.(*KVStore).safeTSUpdater(0xc000ca4120)
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/tikv/kv.go:544 +0x165 fp=0xc011e36fc8 sp=0xc011e36f08 pc=0x1ed8e65
   > github.com/tikv/client-go/v2/tikv.NewKVStore.func2()
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/tikv/kv.go:188 +0x26 fp=0xc011e36fe0 sp=0xc011e36fc8 pc=0x1ed6ca6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc011e36fe8 sp=0xc011e36fe0 pc=0x13ee6e1
   > created by github.com/tikv/client-go/v2/tikv.NewKVStore
   > 	/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.0-alpha.0.20211102120533-b8cc5a319d96/tikv/kv.go:188 +0x416
   > goroutine 475 [select]:
   > runtime.gopark(0xc0008d4798?, 0x2?, 0x0?, 0x0?, 0xc0008d476c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0008d45e8 sp=0xc0008d45c8 pc=0x13bb516
   > runtime.selectgo(0xc0008d4798, 0xc0008d4768, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0008d4728 sp=0xc0008d45e8 pc=0x13cbbdc
   > github.com/dgraph-io/ristretto.(*defaultPolicy).processItems(0xc000983590)
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.0.1/policy.go:96 +0x91 fp=0xc0008d47c8 sp=0xc0008d4728 pc=0x23cf0d1
   > github.com/dgraph-io/ristretto.newDefaultPolicy.func1()
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.0.1/policy.go:80 +0x26 fp=0xc0008d47e0 sp=0xc0008d47c8 pc=0x23cef86
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0008d47e8 sp=0xc0008d47e0 pc=0x13ee6e1
   > created by github.com/dgraph-io/ristretto.newDefaultPolicy
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.0.1/policy.go:80 +0x156
   > goroutine 476 [select]:
   > runtime.gopark(0xc0008d4f98?, 0x2?, 0x0?, 0x0?, 0xc0008d4f74?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0008d4df0 sp=0xc0008d4dd0 pc=0x13bb516
   > runtime.selectgo(0xc0008d4f98, 0xc0008d4f70, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0008d4f30 sp=0xc0008d4df0 pc=0x13cbbdc
   > github.com/dgraph-io/ristretto.(*Cache).processItems(0xc00068c840)
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.0.1/cache.go:257 +0x85 fp=0xc0008d4fc8 sp=0xc0008d4f30 pc=0x23ce025
   > github.com/dgraph-io/ristretto.NewCache.func2()
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.0.1/cache.go:155 +0x26 fp=0xc0008d4fe0 sp=0xc0008d4fc8 pc=0x23cd846
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0008d4fe8 sp=0xc0008d4fe0 pc=0x13ee6e1
   > created by github.com/dgraph-io/ristretto.NewCache
   > 	/go/pkg/mod/github.com/dgraph-io/ristretto@v0.0.1/cache.go:155 +0x485
   > goroutine 714 [select]:
   > runtime.gopark(0xc010eb5f58?, 0x4?, 0xab?, 0x62?, 0xc010eb5da8?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010eb5bf8 sp=0xc010eb5bd8 pc=0x13bb516
   > runtime.selectgo(0xc010eb5f58, 0xc010eb5da0, 0xc00068ee38?, 0x0, 0x1?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010eb5d38 sp=0xc010eb5bf8 pc=0x13cbbdc
   > github.com/pingcap/tidb/ddl.(*worker).start(0xc010a998c0, 0xc010d6ae40)
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl_worker.go:178 +0x318 fp=0xc010eb5fc0 sp=0xc010eb5d38 pc=0x2622e98
   > github.com/pingcap/tidb/ddl.(*ddl).Start.func2()
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:369 +0x2a fp=0xc010eb5fe0 sp=0xc010eb5fc0 pc=0x25e9a6a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010eb5fe8 sp=0xc010eb5fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/ddl.(*ddl).Start
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:369 +0x5c5
   > goroutine 635 [select]:
   > runtime.gopark(0xc00fce8fa8?, 0x2?, 0x0?, 0x30?, 0xc00fce8f84?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fce8e08 sp=0xc00fce8de8 pc=0x13bb516
   > runtime.selectgo(0xc00fce8fa8, 0xc00fce8f80, 0xc0106311d0?, 0x0, 0xc00068d0e0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fce8f48 sp=0xc00fce8e08 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).TelemetryRotateSubWindowLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1169 +0xcc fp=0xc00fce8fe0 sp=0xc00fce8f48 pc=0x26a5c4c
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fce8fe8 sp=0xc00fce8fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).TelemetryRotateSubWindowLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1162 +0x8f
   > goroutine 717 [select]:
   > runtime.gopark(0xc00ff7bf78?, 0x3?, 0x10?, 0x0?, 0xc00ff7bf12?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00ff7bd60 sp=0xc00ff7bd40 pc=0x13bb516
   > runtime.selectgo(0xc00ff7bf78, 0xc00ff7bf0c, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00ff7bea0 sp=0xc00ff7bd60 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).topNSlowQueryLoop(0xc010abbc20)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:455 +0x194 fp=0xc00ff7bfc8 sp=0xc00ff7bea0 pc=0x269e914
   > github.com/pingcap/tidb/domain.(*Domain).Init.func11()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:828 +0x26 fp=0xc00ff7bfe0 sp=0xc00ff7bfc8 pc=0x26a2ac6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00ff7bfe8 sp=0xc00ff7bfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:828 +0xe52
   > goroutine 634 [select]:
   > runtime.gopark(0xc00fce9f28?, 0x2?, 0x0?, 0x30?, 0xc00fce9ed4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fce9d48 sp=0xc00fce9d28 pc=0x13bb516
   > runtime.selectgo(0xc00fce9f28, 0xc00fce9ed0, 0x9?, 0x0, 0x15?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fce9e88 sp=0xc00fce9d48 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).TelemetryReportLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1140 +0x11c fp=0xc00fce9fe0 sp=0xc00fce9e88 pc=0x26a573c
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fce9fe8 sp=0xc00fce9fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).TelemetryReportLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1132 +0x285
   > goroutine 713 [select]:
   > runtime.gopark(0xc0005d7f58?, 0x4?, 0xab?, 0x62?, 0xc0005d7da8?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0005d7bf8 sp=0xc0005d7bd8 pc=0x13bb516
   > runtime.selectgo(0xc0005d7f58, 0xc0005d7da0, 0xc010bcae38?, 0x0, 0x1?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0005d7d38 sp=0xc0005d7bf8 pc=0x13cbbdc
   > github.com/pingcap/tidb/ddl.(*worker).start(0xc010a99970, 0xc010d6ae40)
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl_worker.go:178 +0x318 fp=0xc0005d7fc0 sp=0xc0005d7d38 pc=0x2622e98
   > github.com/pingcap/tidb/ddl.(*ddl).Start.func2()
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:369 +0x2a fp=0xc0005d7fe0 sp=0xc0005d7fc0 pc=0x25e9a6a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0005d7fe8 sp=0xc0005d7fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/ddl.(*ddl).Start
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:369 +0x5c5
   > goroutine 711 [select]:
   > runtime.gopark(0xc0107aff38?, 0x2?, 0x0?, 0x0?, 0xc0107afefc?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0107afd50 sp=0xc0107afd30 pc=0x13bb516
   > runtime.selectgo(0xc0107aff38, 0xc0107afef8, 0x1?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0107afe90 sp=0xc0107afd50 pc=0x13cbbdc
   > github.com/pingcap/tidb/ddl.(*ddl).limitDDLJobs(0xc010d6caf0)
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl_worker.go:263 +0x173 fp=0xc0107affc8 sp=0xc0107afe90 pc=0x2623fd3
   > github.com/pingcap/tidb/ddl.(*ddl).Start.func1()
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:351 +0x26 fp=0xc0107affe0 sp=0xc0107affc8 pc=0x25e9ac6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0107affe8 sp=0xc0107affe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/ddl.(*ddl).Start
   > 	/go/src/github.com/pingcap/tidb/ddl/ddl.go:351 +0x2ea
   > goroutine 712 [select]:
   > runtime.gopark(0xc000cbcf90?, 0x2?, 0x0?, 0x0?, 0xc000cbcf6c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000cbcdf0 sp=0xc000cbcdd0 pc=0x13bb516
   > runtime.selectgo(0xc000cbcf90, 0xc000cbcf68, 0xc00ff78758?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000cbcf30 sp=0xc000cbcdf0 pc=0x13cbbdc
   > github.com/pingcap/tidb/ddl.(*delRange).startEmulator(0xc0107491a0)
   > 	/go/src/github.com/pingcap/tidb/ddl/delete_range.go:144 +0x125 fp=0xc000cbcfc8 sp=0xc000cbcf30 pc=0x262b9e5
   > github.com/pingcap/tidb/ddl.(*delRange).start.func1()
   > 	/go/src/github.com/pingcap/tidb/ddl/delete_range.go:126 +0x26 fp=0xc000cbcfe0 sp=0xc000cbcfc8 pc=0x262b7a6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000cbcfe8 sp=0xc000cbcfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/ddl.(*delRange).start
   > 	/go/src/github.com/pingcap/tidb/ddl/delete_range.go:126 +0x6d
   > goroutine 1281 [chan receive]:
   > runtime.gopark(0xc01237fc20?, 0xc01251ea80?, 0x3?, 0x0?, 0xc01092dcf8?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01092dca8 sp=0xc01092dc88 pc=0x13bb516
   > runtime.chanrecv(0xc01251e9c0, 0xc01092de08, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc01092dd38 sp=0xc01092dca8 pc=0x13854bb
   > runtime.chanrecv2(0xc010ae5d40?, 0x4012e60?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc01092dd60 sp=0xc01092dd38 pc=0x1384ff8
   > github.com/pingcap/tidb/executor.(*HashJoinExec).buildHashTableForList(0xc0124a0900, 0x1?)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:762 +0x2d6 fp=0xc01092de78 sp=0xc01092dd60 pc=0x3065af6
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable(0xc0124a0900, {0x400d6b0?, 0xc011e2fc80})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:726 +0x23f fp=0xc01092df28 sp=0xc01092de78 pc=0x30653ff
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Next.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:671 +0x8f fp=0xc01092df90 sp=0xc01092df28 pc=0x306504f
   > github.com/pingcap/tidb/util.WithRecovery(0x0?, 0x0?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc01092dfc0 sp=0xc01092df90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Next.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:669 +0x2a fp=0xc01092dfe0 sp=0xc01092dfc0 pc=0x3064f8a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01092dfe8 sp=0xc01092dfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).Next
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:669 +0x5b2
   > goroutine 835 [select]:
   > runtime.gopark(0xc00fceaf18?, 0x3?, 0x0?, 0x30?, 0xc00fceae8a?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fceacc8 sp=0xc00fceaca8 pc=0x13bb516
   > runtime.selectgo(0xc00fceaf18, 0xc00fceae84, 0xc000093400?, 0x0, 0x13bb516?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fceae08 sp=0xc00fceacc8 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).LoadSysVarCacheLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:989 +0x145 fp=0xc00fceafe0 sp=0xc00fceae08 pc=0x26a3dc5
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fceafe8 sp=0xc00fceafe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).LoadSysVarCacheLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:980 +0x172
   > goroutine 641 [select]:
   > runtime.gopark(0xc010eb1eb0?, 0x2?, 0x18?, 0x0?, 0xc010eb1e5c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010eb1cc8 sp=0xc010eb1ca8 pc=0x13bb516
   > runtime.selectgo(0xc010eb1eb0, 0xc010eb1e58, 0xc01056e5b0?, 0x0, 0x10000000000?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010eb1e08 sp=0xc010eb1cc8 pc=0x13cbbdc
   > github.com/pingcap/tidb/util/expensivequery.(*Handle).Run(0xc0106dff50)
   > 	/go/src/github.com/pingcap/tidb/util/expensivequery/expensivequery.go:61 +0x198 fp=0xc010eb1fc8 sp=0xc010eb1e08 pc=0x2695d58
   > main.createServer.func1()
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:675 +0x26 fp=0xc010eb1fe0 sp=0xc010eb1fc8 pc=0x33b2be6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010eb1fe8 sp=0xc010eb1fe0 pc=0x13ee6e1
   > created by main.createServer
   > 	/go/src/github.com/pingcap/tidb/tidb-server/main.go:675 +0x439
   > goroutine 1302 [select]:
   > runtime.gopark(0xc000a0a610?, 0x2?, 0x90?, 0x6a?, 0xc000a0a58c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000a0a3e0 sp=0xc000a0a3c0 pc=0x13bb516
   > runtime.selectgo(0xc000a0a610, 0xc000a0a588, 0xc0105269d0?, 0x0, 0x13cc174?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000a0a520 sp=0xc000a0a3e0 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc0124a06c0, 0x1, {0x5f8a1a8, 0x0, 0x0})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:441 +0x4f4 fp=0xc000a0a710 sp=0xc000a0a520 pc=0x30626b4
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:335 +0xb3 fp=0xc000a0a790 sp=0xc000a0a710 pc=0x30613d3
   > github.com/pingcap/tidb/util.WithRecovery(0x400d6b0?, 0xc012583470?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc000a0a7c0 sp=0xc000a0a790 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x2a fp=0xc000a0a7e0 sp=0xc000a0a7c0 pc=0x30612ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000a0a7e8 sp=0xc000a0a7e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x1c9
   > goroutine 640 [chan receive]:
   > runtime.gopark(0x44bbca5eb8?, 0xc00040c820?, 0x48?, 0xb6?, 0x13d8de5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00ff7b5f0 sp=0xc00ff7b5d0 pc=0x13bb516
   > runtime.chanrecv(0xc0057cd9e0, 0xc00ff7b738, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc00ff7b680 sp=0xc00ff7b5f0 pc=0x13854bb
   > runtime.chanrecv2(0x9356907420000?, 0x0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc00ff7b6a8 sp=0xc00ff7b680 pc=0x1384ff8
   > github.com/pingcap/tidb/server.NewServer.func1()
   > 	/go/src/github.com/pingcap/tidb/server/server.go:209 +0x98 fp=0xc00ff7b7e0 sp=0xc00ff7b6a8 pc=0x31e1638
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00ff7b7e8 sp=0xc00ff7b7e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/server.NewServer
   > 	/go/src/github.com/pingcap/tidb/server/server.go:208 +0x32a
   > goroutine 791 [chan receive]:
   > runtime.gopark(0x50?, 0xc000db2480?, 0x8?, 0x3d?, 0x138c1bf?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0000a3c80 sp=0xc0000a3c60 pc=0x13bb516
   > runtime.chanrecv(0xc01092ba40, 0xc0000a3d48, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc0000a3d10 sp=0xc0000a3c80 pc=0x13854bb
   > runtime.chanrecv2(0x141e886?, 0xc0005c24f0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc0000a3d38 sp=0xc0000a3d10 pc=0x1384ff8
   > github.com/soheilhy/cmux.muxListener.Accept(...)
   > 	/go/pkg/mod/github.com/soheilhy/cmux@v0.1.4/cmux.go:229
   > github.com/soheilhy/cmux.(*muxListener).Accept(0x5828400?)
   > 	<autogenerated>:1 +0x45 fp=0xc0000a3d68 sp=0xc0000a3d38 pc=0x2dc7625
   > net/http.(*onceCloseListener).Accept(0x400d640?)
   > 	<autogenerated>:1 +0x2a fp=0xc0000a3d80 sp=0xc0000a3d68 pc=0x16e0c6a
   > net/http.(*Server).Serve(0xc010f4a2d0, {0x400cb50, 0xc0108665a0})
   > 	/usr/local/go/src/net/http/server.go:3070 +0x385 fp=0xc0000a3eb0 sp=0xc0000a3d80 pc=0x16b6f45
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer.func2()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:462 +0x3e fp=0xc0000a3f90 sp=0xc0000a3eb0 pc=0x31dadbe
   > github.com/pingcap/tidb/util.WithRecovery(0x5f539a0?, 0xc00fceefb8?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc0000a3fc0 sp=0xc0000a3f90 pc=0x1ffabd3
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer.func6()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:461 +0x28 fp=0xc0000a3fe0 sp=0xc0000a3fc0 pc=0x31dad48
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0000a3fe8 sp=0xc0000a3fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:461 +0x4ea
   > goroutine 882 [select, locked to thread]:
   > runtime.gopark(0xc00ff7a7a8?, 0x2?, 0x0?, 0x0?, 0xc00ff7a7a4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00ff7a618 sp=0xc00ff7a5f8 pc=0x13bb516
   > runtime.selectgo(0xc00ff7a7a8, 0xc00ff7a7a0, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00ff7a758 sp=0xc00ff7a618 pc=0x13cbbdc
   > runtime.ensureSigM.func1()
   > 	/usr/local/go/src/runtime/signal_unix.go:995 +0x1b0 fp=0xc00ff7a7e0 sp=0xc00ff7a758 pc=0x13d0070
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00ff7a7e8 sp=0xc00ff7a7e0 pc=0x13ee6e1
   > created by runtime.ensureSigM
   > 	/usr/local/go/src/runtime/signal_unix.go:978 +0xbd
   > goroutine 790 [chan receive]:
   > runtime.gopark(0x3a8bf40?, 0xc0005b6cf8?, 0xfc?, 0xb?, 0xa?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0005b6cb0 sp=0xc0005b6c90 pc=0x13bb516
   > runtime.chanrecv(0xc01092baa0, 0xc0005b6d78, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc0005b6d40 sp=0xc0005b6cb0 pc=0x13854bb
   > runtime.chanrecv2(0xc0112d3228?, 0x2?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc0005b6d68 sp=0xc0005b6d40 pc=0x1384ff8
   > github.com/soheilhy/cmux.muxListener.Accept(...)
   > 	/go/pkg/mod/github.com/soheilhy/cmux@v0.1.4/cmux.go:229
   > github.com/soheilhy/cmux.(*muxListener).Accept(0x3ff0f40?)
   > 	<autogenerated>:1 +0x45 fp=0xc0005b6d98 sp=0xc0005b6d68 pc=0x2dc7625
   > google.golang.org/grpc.(*Server).Serve(0xc0003549c0, {0x400cb50, 0xc0108665b8})
   > 	/go/pkg/mod/google.golang.org/grpc@v1.29.1/server.go:621 +0x362 fp=0xc0005b6eb0 sp=0xc0005b6d98 pc=0x19749a2
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer.func1()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:457 +0x3e fp=0xc0005b6f90 sp=0xc0005b6eb0 pc=0x31db01e
   > github.com/pingcap/tidb/util.WithRecovery(0x31d65c6?, 0xc01092b860?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc0005b6fc0 sp=0xc0005b6f90 pc=0x1ffabd3
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer.func5()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:456 +0x28 fp=0xc0005b6fe0 sp=0xc0005b6fc0 pc=0x31dafa8
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0005b6fe8 sp=0xc0005b6fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:456 +0x42c
   > goroutine 1250 [chan receive]:
   > runtime.gopark(0xfb69ec46?, 0x0?, 0x80?, 0x8e?, 0x138c1bf?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc012378df8 sp=0xc012378dd8 pc=0x13bb516
   > runtime.chanrecv(0xc0125ee7e0, 0xc012378f38, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc012378e88 sp=0xc012378df8 pc=0x13854bb
   > runtime.chanrecv2(0xc0124a0b00?, 0x35182e0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc012378eb0 sp=0xc012378e88 pc=0x1384ff8
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Close(0xc0124a0900)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:123 +0x385 fp=0xc012378f58 sp=0xc012378eb0 pc=0x305fcc5
   > github.com/pingcap/tidb/executor.(*baseExecutor).Close(0xc000536678?)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:181 +0x7c fp=0xc012378f98 sp=0xc012378f58 pc=0x2feeadc
   > github.com/pingcap/tidb/executor.(*ProjectionExec).Close(0xc0124f4b40)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:329 +0x1cf fp=0xc012379000 sp=0xc012378f98 pc=0x30997af
   > github.com/pingcap/tidb/executor.(*recordSet).Close(0xc0125c3e00)
   > 	/go/src/github.com/pingcap/tidb/executor/adapter.go:176 +0x2a fp=0xc012379040 sp=0xc012379000 pc=0x2f612ca
   > github.com/pingcap/tidb/session.(*execStmtResult).Close(0xc0125e0ba0)
   > 	/go/src/github.com/pingcap/tidb/session/session.go:1734 +0x36 fp=0xc012379090 sp=0xc012379040 pc=0x314b676
   > github.com/pingcap/tidb/server.(*tidbResultSet).Close(0x1fdcc853a?)
   > 	/go/src/github.com/pingcap/tidb/server/driver_tidb.go:324 +0x3c fp=0xc0123790b0 sp=0xc012379090 pc=0x31c611c
   > github.com/pingcap/tidb/server.ResultSet.Close-fm()
   > 	<autogenerated>:1 +0x2b fp=0xc0123790c8 sp=0xc0123790b0 pc=0x31f7acb
   > github.com/pingcap/tidb/parser/terror.Call(0xc0123791d8?)
   > 	/go/src/github.com/pingcap/tidb/parser/terror/terror.go:298 +0x31 fp=0xc012379208 sp=0xc0123790c8 pc=0x1b74a51
   > github.com/pingcap/tidb/server.(*clientConn).handleStmt.func1()
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:1911 +0x26 fp=0xc012379220 sp=0xc012379208 pc=0x31bbd26
   > github.com/pingcap/tidb/server.(*clientConn).handleStmt(0xc011f03680, {0x400d608, 0xc0057ce500}, {0x401fff0, 0xc0118c10e0}, {0x5f8a1a8, 0x0, 0x0}, 0x1)
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:1934 +0x413 fp=0xc0123792f0 sp=0xc012379220 pc=0x31bbaf3
   > github.com/pingcap/tidb/server.(*clientConn).handleQuery(0xc011f03680, {0x400d608, 0xc0057ce500}, {0xc010f509c1, 0x18c})
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:1775 +0x774 fp=0xc012379468 sp=0xc0123792f0 pc=0x31ba494
   > github.com/pingcap/tidb/server.(*clientConn).dispatch(0xc011f03680, {0x400d6b0, 0xc011f78300?}, {0xc010f509c0, 0x18d, 0x18d})
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:1279 +0x1025 fp=0xc012379858 sp=0xc012379468 pc=0x31b6045
   > github.com/pingcap/tidb/server.(*clientConn).Run(0xc011f03680, {0x400d6b0, 0xc011f78300})
   > 	/go/src/github.com/pingcap/tidb/server/conn.go:1034 +0x253 fp=0xc012379e18 sp=0xc012379858 pc=0x31b2b33
   > github.com/pingcap/tidb/server.(*Server).onConn(0xc01056e5b0, 0xc011f03680)
   > 	/go/src/github.com/pingcap/tidb/server/server.go:550 +0x6c5 fp=0xc012379fc0 sp=0xc012379e18 pc=0x31e4165
   > github.com/pingcap/tidb/server.(*Server).startNetworkListener.func2()
   > 	/go/src/github.com/pingcap/tidb/server/server.go:453 +0x2a fp=0xc012379fe0 sp=0xc012379fc0 pc=0x31e300a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc012379fe8 sp=0xc012379fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/server.(*Server).startNetworkListener
   > 	/go/src/github.com/pingcap/tidb/server/server.go:453 +0x5ca
   > goroutine 718 [select]:
   > runtime.gopark(0xc010ff86f8?, 0x3?, 0x8?, 0x0?, 0xc010ff8682?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0005bcd08 sp=0xc0005bcce8 pc=0x13bb516
   > runtime.selectgo(0xc0005bcef8, 0xc010ff867c, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0005bce48 sp=0xc0005bcd08 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).infoSyncerKeeper(0xc010abbc20)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:487 +0x165 fp=0xc0005bcfc8 sp=0xc0005bce48 pc=0x269ee45
   > github.com/pingcap/tidb/domain.(*Domain).Init.func12()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:829 +0x26 fp=0xc0005bcfe0 sp=0xc0005bcfc8 pc=0x26a2a66
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0005bcfe8 sp=0xc0005bcfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:829 +0xe95
   > goroutine 716 [select]:
   > runtime.gopark(0xc0107abf50?, 0x4?, 0x0?, 0x0?, 0xc0107abd00?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0107abb78 sp=0xc0107abb58 pc=0x13bb516
   > runtime.selectgo(0xc0107abf50, 0xc0107abcf8, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0107abcb8 sp=0xc0107abb78 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).loadSchemaInLoop(0xc010abbc20, {0x400d608, 0xc010aa54c0}, 0x0?)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:565 +0x1aa fp=0xc0107abfb0 sp=0xc0107abcb8 pc=0x26a00aa
   > github.com/pingcap/tidb/domain.(*Domain).Init.func10()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:825 +0x32 fp=0xc0107abfe0 sp=0xc0107abfb0 pc=0x26a2b32
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0107abfe8 sp=0xc0107abfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:825 +0xdeb
   > goroutine 639 [select]:
   > runtime.gopark(0xc00ff79fa8?, 0x2?, 0x40?, 0x0?, 0xc00ff79f7c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00ff79e00 sp=0xc00ff79de0 pc=0x13bb516
   > runtime.selectgo(0xc00ff79fa8, 0xc00ff79f78, 0x100010000?, 0x0, 0xc010ac3040?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00ff79f40 sp=0xc00ff79e00 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).PlanReplayerLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1191 +0xf6 fp=0xc00ff79fe0 sp=0xc00ff79f40 pc=0x26a5f36
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00ff79fe8 sp=0xc00ff79fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).PlanReplayerLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1182 +0x6c
   > goroutine 720 [select]:
   > runtime.gopark(0xc01092ce78?, 0x3?, 0x0?, 0x0?, 0xc01092cdf2?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01092cc78 sp=0xc01092cc58 pc=0x13bb516
   > runtime.selectgo(0xc01092ce78, 0xc01092cdec, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01092cdb8 sp=0xc01092cc78 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).topologySyncerKeeper(0xc010abbc20)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:533 +0x165 fp=0xc01092cfc8 sp=0xc01092cdb8 pc=0x269f8c5
   > github.com/pingcap/tidb/domain.(*Domain).Init.func14()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:834 +0x26 fp=0xc01092cfe0 sp=0xc01092cfc8 pc=0x26a29a6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01092cfe8 sp=0xc01092cfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:834 +0xf3d
   > goroutine 719 [select]:
   > runtime.gopark(0xc00ff79ef0?, 0x2?, 0x0?, 0x0?, 0xc00ff79ebc?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0005bdd38 sp=0xc0005bdd18 pc=0x13bb516
   > runtime.selectgo(0xc0005bdef0, 0xc00ff79eb8, 0xb1?, 0x0, 0xc000dedaa0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0005bde78 sp=0xc0005bdd38 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).globalConfigSyncerKeeper(0xc010abbc20)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:510 +0xe5 fp=0xc0005bdfc8 sp=0xc0005bde78 pc=0x269f405
   > github.com/pingcap/tidb/domain.(*Domain).Init.func13()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:830 +0x26 fp=0xc0005bdfe0 sp=0xc0005bdfc8 pc=0x26a2a06
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0005bdfe8 sp=0xc0005bdfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).Init
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:830 +0xedc
   > goroutine 745 [select]:
   > runtime.gopark(0xc0107e1e90?, 0x3?, 0x90?, 0xbe?, 0xc0107e1e02?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0107e1c70 sp=0xc0107e1c50 pc=0x13bb516
   > runtime.selectgo(0xc0107e1e90, 0xc0107e1dfc, 0x3a8be78?, 0x0, 0xc0111a98c0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0107e1db0 sp=0xc0107e1c70 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).globalBindHandleWorkerLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1071 +0x16f fp=0xc0107e1fe0 sp=0xc0107e1db0 pc=0x26a476f
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0107e1fe8 sp=0xc0107e1fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).globalBindHandleWorkerLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1058 +0xad
   > goroutine 1300 [select]:
   > runtime.gopark(0xc012603e30?, 0x2?, 0x80?, 0x57?, 0xc012603e1c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc012603ca8 sp=0xc012603c88 pc=0x13bb516
   > runtime.selectgo(0xc012603e30, 0xc012603e18, 0xc01251ed20?, 0x0, 0x2fef900?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc012603de8 sp=0xc012603ca8 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).wait4BuildSide(0xc0124a06c0)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:242 +0x6f fp=0xc012603e60 sp=0xc012603de8 pc=0x30605ef
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchProbeSideChunks(0xc0124a06c0, {0x400d6b0, 0xc011e2fc80})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:221 +0x233 fp=0xc012603f28 sp=0xc012603e60 pc=0x3060333
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:322 +0x8f fp=0xc012603f90 sp=0xc012603f28 pc=0x306156f
   > github.com/pingcap/tidb/util.WithRecovery(0x23de786?, 0xc000bbd600?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc012603fc0 sp=0xc012603f90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func3()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:320 +0x2a fp=0xc012603fe0 sp=0xc012603fc0 pc=0x30614aa
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc012603fe8 sp=0xc012603fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:320 +0x14f
   > goroutine 746 [select]:
   > runtime.gopark(0xc0005baf28?, 0x2?, 0x4?, 0x30?, 0xc0005baed4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0005bad48 sp=0xc0005bad28 pc=0x13bb516
   > runtime.selectgo(0xc0005baf28, 0xc0005baed0, 0xc00fe5f000?, 0x0, 0xc010ff46d8?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0005bae88 sp=0xc0005bad48 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).handleEvolvePlanTasksLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1106 +0x107 fp=0xc0005bafe0 sp=0xc0005bae88 pc=0x26a4fe7
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0005bafe8 sp=0xc0005bafe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).handleEvolvePlanTasksLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1099 +0xe5
   > goroutine 636 [select]:
   > runtime.gopark(0xc0118afd48?, 0x2?, 0x8?, 0x21?, 0xc0118afc94?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0118afb08 sp=0xc0118afae8 pc=0x13bb516
   > runtime.selectgo(0xc0118afd48, 0xc0118afc90, 0xc010f817a0?, 0x0, 0x1?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0118afc48 sp=0xc0118afb08 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).loadStatsWorker(0xc010abbc20)
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1304 +0x485 fp=0xc0118affc8 sp=0xc0118afc48 pc=0x26a6ea5
   > github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1247 +0x26 fp=0xc0118affe0 sp=0xc0118affc8 pc=0x26a6666
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0118affe8 sp=0xc0118affe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1247 +0x105
   > goroutine 637 [select]:
   > runtime.gopark(0xc010899f28?, 0x6?, 0x50?, 0xc0?, 0xc010899bb4?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010899a20 sp=0xc010899a00 pc=0x13bb516
   > runtime.selectgo(0xc010899f28, 0xc010899ba8, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010899b60 sp=0xc010899a20 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).updateStatsWorker(0xc010abbc20, {0x309938e?, 0xc01063a0c0?}, {0x401ea10, 0xc011510b00})
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1372 +0x234 fp=0xc010899fa8 sp=0xc010899b60 pc=0x26a7e54
   > github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop.func3()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1259 +0x36 fp=0xc010899fe0 sp=0xc010899fa8 pc=0x26a65b6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010899fe8 sp=0xc010899fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1259 +0x29a
   > goroutine 736 [select]:
   > runtime.gopark(0xc01092ff18?, 0x3?, 0x0?, 0x30?, 0xc01092fe9a?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01092fcd8 sp=0xc01092fcb8 pc=0x13bb516
   > runtime.selectgo(0xc01092ff18, 0xc01092fe94, 0xc0057ccae0?, 0x0, 0xc00053ae40?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01092fe18 sp=0xc01092fcd8 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).LoadPrivilegeLoop.func1()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:939 +0x145 fp=0xc01092ffe0 sp=0xc01092fe18 pc=0x26a3585
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01092ffe8 sp=0xc01092ffe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).LoadPrivilegeLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:930 +0x205
   > goroutine 638 [select]:
   > runtime.gopark(0xc0107ddf78?, 0x2?, 0x0?, 0x30?, 0xc0107ddf4c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0107dddd0 sp=0xc0107dddb0 pc=0x13bb516
   > runtime.selectgo(0xc0107ddf78, 0xc0107ddf48, 0xc010f817a0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0107ddf10 sp=0xc0107dddd0 pc=0x13cbbdc
   > github.com/pingcap/tidb/domain.(*Domain).autoAnalyzeWorker(0xc010abbc20, {0x401ea10, 0xc011510b00})
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1425 +0x105 fp=0xc0107ddfb8 sp=0xc0107ddf10 pc=0x26a8bc5
   > github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop.func4()
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1262 +0x2e fp=0xc0107ddfe0 sp=0xc0107ddfb8 pc=0x26a654e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0107ddfe8 sp=0xc0107ddfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/domain.(*Domain).UpdateTableStatsLoop
   > 	/go/src/github.com/pingcap/tidb/domain/domain.go:1262 +0x31a
   > goroutine 883 [syscall]:
   > runtime.notetsleepg(0x40424f0?, 0xc000d89c00?)
   > 	/usr/local/go/src/runtime/lock_futex.go:236 +0x34 fp=0xc00fcea7a0 sp=0xc00fcea768 pc=0x138acd4
   > os/signal.signal_recv()
   > 	/usr/local/go/src/runtime/sigqueue.go:152 +0x2f fp=0xc00fcea7c0 sp=0xc00fcea7a0 pc=0x13ea6cf
   > os/signal.loop()
   > 	/usr/local/go/src/os/signal/signal_unix.go:23 +0x19 fp=0xc00fcea7e0 sp=0xc00fcea7c0 pc=0x2cac7f9
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fcea7e8 sp=0xc00fcea7e0 pc=0x13ee6e1
   > created by os/signal.Notify.func1.1
   > 	/usr/local/go/src/os/signal/signal.go:151 +0x2a
   > goroutine 884 [chan receive]:
   > runtime.gopark(0x5f8be00?, 0xc00fceb720?, 0x28?, 0xc3?, 0x0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fceb6a0 sp=0xc00fceb680 pc=0x13bb516
   > runtime.chanrecv(0xc00068dda0, 0xc00fceb7a0, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc00fceb730 sp=0xc00fceb6a0 pc=0x13854bb
   > runtime.chanrecv1(0x0?, 0x10000c00fce4900?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc00fceb758 sp=0xc00fceb730 pc=0x1384fb8
   > github.com/pingcap/tidb/util/signal.SetupSignalHandler.func1()
   > 	/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:37 +0x4f fp=0xc00fceb7e0 sp=0xc00fceb758 pc=0x33ac32f
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fceb7e8 sp=0xc00fceb7e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/util/signal.SetupSignalHandler
   > 	/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:34 +0xb6
   > goroutine 885 [chan receive]:
   > runtime.gopark(0x0?, 0x141d011?, 0x98?, 0xe6?, 0x1ecccb7?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fcee660 sp=0xc00fcee640 pc=0x13bb516
   > runtime.chanrecv(0xc00068de00, 0xc00fcee780, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc00fcee6f0 sp=0xc00fcee660 pc=0x13854bb
   > runtime.chanrecv1(0xc00fc2a680?, 0x1?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc00fcee718 sp=0xc00fcee6f0 pc=0x1384fb8
   > github.com/pingcap/tidb/util/signal.SetupSignalHandler.func2()
   > 	/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:53 +0x45 fp=0xc00fcee7e0 sp=0xc00fcee718 pc=0x33ac105
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fcee7e8 sp=0xc00fcee7e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/util/signal.SetupSignalHandler
   > 	/go/src/github.com/pingcap/tidb/util/signal/signal_posix.go:52 +0x19f
   > goroutine 886 [select]:
   > runtime.gopark(0xc00fcedf80?, 0x3?, 0x0?, 0x30?, 0xc00fcedf3a?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00fcedda8 sp=0xc00fcedd88 pc=0x13bb516
   > runtime.selectgo(0xc00fcedf80, 0xc00fcedf34, 0x10?, 0x0, 0x2?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc00fcedee8 sp=0xc00fcedda8 pc=0x13cbbdc
   > github.com/pingcap/tidb/util/topsql/reporter.(*RemoteTopSQLReporter).collectWorker(0xc00097fb90)
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:327 +0x13a fp=0xc00fcedfc8 sp=0xc00fcedee8 pc=0x2547eda
   > github.com/pingcap/tidb/util/topsql/reporter.NewRemoteTopSQLReporter.func1()
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:160 +0x26 fp=0xc00fcedfe0 sp=0xc00fcedfc8 pc=0x2546c26
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00fcedfe8 sp=0xc00fcedfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/util/topsql/reporter.NewRemoteTopSQLReporter
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:160 +0x1b6
   > goroutine 887 [select]:
   > runtime.gopark(0xc000a0cf40?, 0x2?, 0x0?, 0x0?, 0xc000a0cf04?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000a0cd88 sp=0xc000a0cd68 pc=0x13bb516
   > runtime.selectgo(0xc000a0cf40, 0xc000a0cf00, 0x0?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000a0cec8 sp=0xc000a0cd88 pc=0x13cbbdc
   > github.com/pingcap/tidb/util/topsql/reporter.(*RemoteTopSQLReporter).reportWorker(0xc00097fb90)
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:499 +0x1ae fp=0xc000a0cfc8 sp=0xc000a0cec8 pc=0x254924e
   > github.com/pingcap/tidb/util/topsql/reporter.NewRemoteTopSQLReporter.func2()
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:161 +0x26 fp=0xc000a0cfe0 sp=0xc000a0cfc8 pc=0x2546bc6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000a0cfe8 sp=0xc000a0cfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/util/topsql/reporter.NewRemoteTopSQLReporter
   > 	/go/src/github.com/pingcap/tidb/util/topsql/reporter/reporter.go:161 +0x1f6
   > goroutine 888 [sleep]:
   > runtime.gopark(0x21e61b7e1b71?, 0x0?, 0x88?, 0xdf?, 0x25412d5?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000a0df58 sp=0xc000a0df38 pc=0x13bb516
   > time.Sleep(0x3b9aca00)
   > 	/usr/local/go/src/runtime/time.go:195 +0x135 fp=0xc000a0df98 sp=0xc000a0df58 pc=0x13eaf15
   > github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).startCPUProfileWorker(0xc000dae040?)
   > 	/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:115 +0x65 fp=0xc000a0dfc8 sp=0xc000a0df98 pc=0x2540065
   > github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).Run.func1()
   > 	/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:93 +0x26 fp=0xc000a0dfe0 sp=0xc000a0dfc8 pc=0x253fea6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000a0dfe8 sp=0xc000a0dfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).Run
   > 	/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:93 +0xca
   > goroutine 889 [chan receive]:
   > runtime.gopark(0xc00ff7d5f8?, 0x400d6b0?, 0x80?, 0xd6?, 0xc00ff7d638?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc00ff7d5e0 sp=0xc00ff7d5c0 pc=0x13bb516
   > runtime.chanrecv(0xc0002f6c60, 0xc00ff7d708, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc00ff7d670 sp=0xc00ff7d5e0 pc=0x13854bb
   > runtime.chanrecv1(0xc0106e7a70?, 0x5f60988?)
   > 	/usr/local/go/src/runtime/chan.go:442 +0x18 fp=0xc00ff7d698 sp=0xc00ff7d670 pc=0x1384fb8
   > github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).startAnalyzeProfileWorker(0xc0004bfb90)
   > 	/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:142 +0x7c fp=0xc00ff7d7c8 sp=0xc00ff7d698 pc=0x25402bc
   > github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).Run.func2()
   > 	/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:94 +0x26 fp=0xc00ff7d7e0 sp=0xc00ff7d7c8 pc=0x253fe46
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc00ff7d7e8 sp=0xc00ff7d7e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/util/topsql/tracecpu.(*sqlCPUProfiler).Run
   > 	/go/src/github.com/pingcap/tidb/util/topsql/tracecpu/profile.go:94 +0x10a
   > goroutine 890 [IO wait]:
   > runtime.gopark(0xf?, 0xc0106c0c30?, 0x3?, 0x0?, 0xc0005d18d0?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0005d1860 sp=0xc0005d1840 pc=0x13bb516
   > runtime.netpollblock(0x203004?, 0x106c0c30?, 0xc0?)
   > 	/usr/local/go/src/runtime/netpoll.go:526 +0xf7 fp=0xc0005d1898 sp=0xc0005d1860 pc=0x13b38f7
   > internal/poll.runtime_pollWait(0x7f449486a618, 0x72)
   > 	/usr/local/go/src/runtime/netpoll.go:305 +0x89 fp=0xc0005d18b8 sp=0xc0005d1898 pc=0x13e7d09
   > internal/poll.(*pollDesc).wait(0xc010b9d500?, 0xc0057ae660?, 0x0)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:84 +0x32 fp=0xc0005d18e0 sp=0xc0005d18b8 pc=0x1465192
   > internal/poll.(*pollDesc).waitRead(...)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:89
   > internal/poll.(*FD).Accept(0xc010b9d500)
   > 	/usr/local/go/src/internal/poll/fd_unix.go:614 +0x234 fp=0xc0005d1978 sp=0xc0005d18e0 pc=0x146a594
   > net.(*netFD).accept(0xc010b9d500)
   > 	/usr/local/go/src/net/fd_unix.go:172 +0x35 fp=0xc0005d1a30 sp=0xc0005d1978 pc=0x1589055
   > net.(*TCPListener).accept(0xc011521200)
   > 	/usr/local/go/src/net/tcpsock_posix.go:142 +0x28 fp=0xc0005d1a60 sp=0xc0005d1a30 pc=0x15a5088
   > net.(*TCPListener).Accept(0xc011521200)
   > 	/usr/local/go/src/net/tcpsock.go:288 +0x3d fp=0xc0005d1a90 sp=0xc0005d1a60 pc=0x15a40fd
   > github.com/soheilhy/cmux.(*cMux).Serve(0xc0057ba370)
   > 	/go/pkg/mod/github.com/soheilhy/cmux@v0.1.4/cmux.go:162 +0xa9 fp=0xc0005d1b20 sp=0xc0005d1a90 pc=0x2dc5da9
   > github.com/pingcap/tidb/server.(*Server).startStatusServerAndRPCServer(0xc01056e5b0, 0xc0008431c0)
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:466 +0x4f7 fp=0xc0005d1c90 sp=0xc0005d1b20 pc=0x31dab17
   > github.com/pingcap/tidb/server.(*Server).startHTTPServer(0xc01056e5b0)
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:442 +0x15d0 fp=0xc0005d1fc8 sp=0xc0005d1c90 pc=0x31d9f10
   > github.com/pingcap/tidb/server.(*Server).startStatusHTTP.func1()
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:62 +0x26 fp=0xc0005d1fe0 sp=0xc0005d1fc8 pc=0x31d65c6
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0005d1fe8 sp=0xc0005d1fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/server.(*Server).startStatusHTTP
   > 	/go/src/github.com/pingcap/tidb/server/http_status.go:62 +0x56
   > goroutine 891 [IO wait]:
   > runtime.gopark(0x18?, 0xc000600000?, 0x50?, 0xf6?, 0xc000cbab70?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000cbab00 sp=0xc000cbaae0 pc=0x13bb516
   > runtime.netpollblock(0x14?, 0x2432d05?, 0x0?)
   > 	/usr/local/go/src/runtime/netpoll.go:526 +0xf7 fp=0xc000cbab38 sp=0xc000cbab00 pc=0x13b38f7
   > internal/poll.runtime_pollWait(0x7f449486a7f8, 0x72)
   > 	/usr/local/go/src/runtime/netpoll.go:305 +0x89 fp=0xc000cbab58 sp=0xc000cbab38 pc=0x13e7d09
   > internal/poll.(*pollDesc).wait(0xc010b9d180?, 0xc000cbad20?, 0x0)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:84 +0x32 fp=0xc000cbab80 sp=0xc000cbab58 pc=0x1465192
   > internal/poll.(*pollDesc).waitRead(...)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:89
   > internal/poll.(*FD).Accept(0xc010b9d180)
   > 	/usr/local/go/src/internal/poll/fd_unix.go:614 +0x234 fp=0xc000cbac18 sp=0xc000cbab80 pc=0x146a594
   > net.(*netFD).accept(0xc010b9d180)
   > 	/usr/local/go/src/net/fd_unix.go:172 +0x35 fp=0xc000cbacd0 sp=0xc000cbac18 pc=0x1589055
   > net.(*TCPListener).accept(0xc0115211e8)
   > 	/usr/local/go/src/net/tcpsock_posix.go:142 +0x28 fp=0xc000cbad00 sp=0xc000cbacd0 pc=0x15a5088
   > net.(*TCPListener).Accept(0xc0115211e8)
   > 	/usr/local/go/src/net/tcpsock.go:288 +0x3d fp=0xc000cbad30 sp=0xc000cbad00 pc=0x15a40fd
   > github.com/pingcap/tidb/server.(*Server).startNetworkListener(0xc01056e5b0, {0x400b9b0, 0xc0115211e8}, 0x0, 0xc00ff78fb8?)
   > 	/go/src/github.com/pingcap/tidb/server/server.go:383 +0xa6 fp=0xc000cbafa8 sp=0xc000cbad30 pc=0x31e25a6
   > github.com/pingcap/tidb/server.(*Server).Run.func1()
   > 	/go/src/github.com/pingcap/tidb/server/server.go:368 +0x34 fp=0xc000cbafe0 sp=0xc000cbafa8 pc=0x31e24d4
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000cbafe8 sp=0xc000cbafe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/server.(*Server).Run
   > 	/go/src/github.com/pingcap/tidb/server/server.go:368 +0x145
   > goroutine 892 [IO wait]:
   > runtime.gopark(0x1456628?, 0x0?, 0x1?, 0x0?, 0xc010933b78?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010933b08 sp=0xc010933ae8 pc=0x13bb516
   > runtime.netpollblock(0x1?, 0x67?, 0x0?)
   > 	/usr/local/go/src/runtime/netpoll.go:526 +0xf7 fp=0xc010933b40 sp=0xc010933b08 pc=0x13b38f7
   > internal/poll.runtime_pollWait(0x7f449486a708, 0x72)
   > 	/usr/local/go/src/runtime/netpoll.go:305 +0x89 fp=0xc010933b60 sp=0xc010933b40 pc=0x13e7d09
   > internal/poll.(*pollDesc).wait(0xc010b9d200?, 0x1395201?, 0x0)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:84 +0x32 fp=0xc010933b88 sp=0xc010933b60 pc=0x1465192
   > internal/poll.(*pollDesc).waitRead(...)
   > 	/usr/local/go/src/internal/poll/fd_poll_runtime.go:89
   > internal/poll.(*FD).Accept(0xc010b9d200)
   > 	/usr/local/go/src/internal/poll/fd_unix.go:614 +0x234 fp=0xc010933c20 sp=0xc010933b88 pc=0x146a594
   > net.(*netFD).accept(0xc010b9d200)
   > 	/usr/local/go/src/net/fd_unix.go:172 +0x35 fp=0xc010933cd8 sp=0xc010933c20 pc=0x1589055
   > net.(*UnixListener).accept(0xc00ff7c558?)
   > 	/usr/local/go/src/net/unixsock_posix.go:166 +0x1c fp=0xc010933d00 sp=0xc010933cd8 pc=0x15aba1c
   > net.(*UnixListener).Accept(0xc000bcec90)
   > 	/usr/local/go/src/net/unixsock.go:260 +0x3d fp=0xc010933d30 sp=0xc010933d00 pc=0x15aa0bd
   > github.com/pingcap/tidb/server.(*Server).startNetworkListener(0xc01056e5b0, {0x400b9e0, 0xc000bcec90}, 0x1, 0xc00ff7c538?)
   > 	/go/src/github.com/pingcap/tidb/server/server.go:383 +0xa6 fp=0xc010933fa8 sp=0xc010933d30 pc=0x31e25a6
   > github.com/pingcap/tidb/server.(*Server).Run.func2()
   > 	/go/src/github.com/pingcap/tidb/server/server.go:369 +0x37 fp=0xc010933fe0 sp=0xc010933fa8 pc=0x31e2477
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010933fe8 sp=0xc010933fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/server.(*Server).Run
   > 	/go/src/github.com/pingcap/tidb/server/server.go:369 +0x1db
   > goroutine 1305 [select]:
   > runtime.gopark(0xc0117a8e10?, 0x2?, 0xc0?, 0x6a?, 0xc0117a8d8c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010f6dbe0 sp=0xc010f6dbc0 pc=0x13bb516
   > runtime.selectgo(0xc010f6de10, 0xc0117a8d88, 0x13cb293?, 0x0, 0x13cc174?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010f6dd20 sp=0xc010f6dbe0 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc0124a06c0, 0x4, {0x5f8a1a8, 0x0, 0x0})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:441 +0x4f4 fp=0xc010f6df10 sp=0xc010f6dd20 pc=0x30626b4
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:335 +0xb3 fp=0xc010f6df90 sp=0xc010f6df10 pc=0x30613d3
   > github.com/pingcap/tidb/util.WithRecovery(0x400d6b0?, 0xc012493920?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc010f6dfc0 sp=0xc010f6df90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x2a fp=0xc010f6dfe0 sp=0xc010f6dfc0 pc=0x30612ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010f6dfe8 sp=0xc010f6dfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x1c9
   > goroutine 142 [select]:
   > runtime.gopark(0xc012606f78?, 0x2?, 0xa0?, 0x6d?, 0xc012606eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc012606d58 sp=0xc012606d38 pc=0x13bb516
   > runtime.selectgo(0xc012606f78, 0xc012606ee8, 0xc000dbae00?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc012606e98 sp=0xc012606d58 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc000671b00, {0x400d6b0?, 0xc011e2fc80?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc012606fb8 sp=0xc012606e98 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc012606fe0 sp=0xc012606fb8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc012606fe8 sp=0xc012606fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 1298 [chan receive]:
   > runtime.gopark(0x13c37d1?, 0xc0109309d0?, 0x0?, 0x38?, 0xc012514430?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0109309c0 sp=0xc0109309a0 pc=0x13bb516
   > runtime.chanrecv(0xc01251ef60, 0xc010930b10, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc010930a50 sp=0xc0109309c0 pc=0x13854bb
   > runtime.chanrecv2(0xc0124a06c0?, 0x400d6b0?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc010930a78 sp=0xc010930a50 pc=0x1384ff8
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Next(0xc0124a06c0, {0x400d6b0?, 0xc011e2fc80?}, 0xc0125c3540)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:681 +0x652 fp=0xc010930b38 sp=0xc010930a78 pc=0x3064d52
   > github.com/pingcap/tidb/executor.Next({0x400d6b0, 0xc011e2fc80}, {0x40101a0, 0xc0124a06c0}, 0xc0125c3540)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:286 +0x4a8 fp=0xc010930c78 sp=0xc010930b38 pc=0x2fef688
   > github.com/pingcap/tidb/executor.(*ProjectionExec).unParallelExecute(0xc0124f4a20, {0x400d6b0?, 0xc011e2fc80?}, 0xc012504730)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:194 +0xb8 fp=0xc010930cc8 sp=0xc010930c78 pc=0x3098758
   > github.com/pingcap/tidb/executor.(*ProjectionExec).Next(0xc0124f4a20, {0x400d6b0, 0xc011e2fc80}, 0xc0125127e0?)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:180 +0x5a fp=0xc010930d00 sp=0xc010930cc8 pc=0x309861a
   > github.com/pingcap/tidb/executor.Next({0x400d6b0, 0xc011e2fc80}, {0x4010760, 0xc0124f4a20}, 0xc012504730)
   > 	/go/src/github.com/pingcap/tidb/executor/executor.go:286 +0x4a8 fp=0xc010930e40 sp=0xc010930d00 pc=0x2fef688
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchBuildSideRows(0xc0124a0900, {0x400d6b0, 0xc011e2fc80}, 0xc01251e9c0, 0xc012516120)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:266 +0x1a5 fp=0xc010930f10 sp=0xc010930e40 pc=0x3060845
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:715 +0xab fp=0xc010930f90 sp=0xc010930f10 pc=0x306572b
   > github.com/pingcap/tidb/util.WithRecovery(0x23de786?, 0xc000bbd900?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc010930fc0 sp=0xc010930f90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:712 +0x2a fp=0xc010930fe0 sp=0xc010930fc0 pc=0x306558a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010930fe8 sp=0xc010930fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:712 +0x22d
   > goroutine 1299 [chan receive]:
   > runtime.gopark(0xc01237fc20?, 0xc01251f080?, 0x3?, 0x0?, 0xc010931cf8?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010931ca8 sp=0xc010931c88 pc=0x13bb516
   > runtime.chanrecv(0xc01251efc0, 0xc010931e08, 0x1)
   > 	/usr/local/go/src/runtime/chan.go:583 +0x49b fp=0xc010931d38 sp=0xc010931ca8 pc=0x13854bb
   > runtime.chanrecv2(0xc010ae5d40?, 0x4012e60?)
   > 	/usr/local/go/src/runtime/chan.go:447 +0x18 fp=0xc010931d60 sp=0xc010931d38 pc=0x1384ff8
   > github.com/pingcap/tidb/executor.(*HashJoinExec).buildHashTableForList(0xc0124a06c0, 0x1?)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:762 +0x2d6 fp=0xc010931e78 sp=0xc010931d60 pc=0x3065af6
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndBuildHashTable(0xc0124a06c0, {0x400d6b0?, 0xc011e2fc80})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:726 +0x23f fp=0xc010931f28 sp=0xc010931e78 pc=0x30653ff
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Next.func1()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:671 +0x8f fp=0xc010931f90 sp=0xc010931f28 pc=0x306504f
   > github.com/pingcap/tidb/util.WithRecovery(0x23de786?, 0xc000bbd900?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc010931fc0 sp=0xc010931f90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).Next.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:669 +0x2a fp=0xc010931fe0 sp=0xc010931fc0 pc=0x3064f8a
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010931fe8 sp=0xc010931fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).Next
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:669 +0x5b2
   > goroutine 1301 [select]:
   > runtime.gopark(0xc010ff3e10?, 0x2?, 0x80?, 0x6a?, 0xc010ff3d8c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc011e33be0 sp=0xc011e33bc0 pc=0x13bb516
   > runtime.selectgo(0xc011e33e10, 0xc010ff3d88, 0x8?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc011e33d20 sp=0xc011e33be0 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc0124a06c0, 0x0, {0x5f8a1a8, 0x0, 0x0})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:441 +0x4f4 fp=0xc011e33f10 sp=0xc011e33d20 pc=0x30626b4
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:335 +0xb3 fp=0xc011e33f90 sp=0xc011e33f10 pc=0x30613d3
   > github.com/pingcap/tidb/util.WithRecovery(0x0?, 0x0?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc011e33fc0 sp=0xc011e33f90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x2a fp=0xc011e33fe0 sp=0xc011e33fc0 pc=0x30612ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc011e33fe8 sp=0xc011e33fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x1c9
   > goroutine 1303 [select]:
   > runtime.gopark(0xc0117ad610?, 0x2?, 0xa0?, 0x6a?, 0xc0117ad58c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc010f6cbe0 sp=0xc010f6cbc0 pc=0x13bb516
   > runtime.selectgo(0xc010f6ce10, 0xc0117ad588, 0x0?, 0x0, 0x13cc174?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc010f6cd20 sp=0xc010f6cbe0 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc0124a06c0, 0x2, {0x5f8a1a8, 0x0, 0x0})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:441 +0x4f4 fp=0xc010f6cf10 sp=0xc010f6cd20 pc=0x30626b4
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:335 +0xb3 fp=0xc010f6cf90 sp=0xc010f6cf10 pc=0x30613d3
   > github.com/pingcap/tidb/util.WithRecovery(0x5f539a0?, 0xc0117ad7b8?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc010f6cfc0 sp=0xc010f6cf90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x2a fp=0xc010f6cfe0 sp=0xc010f6cfc0 pc=0x30612ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc010f6cfe8 sp=0xc010f6cfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x1c9
   > goroutine 1306 [semacquire]:
   > runtime.gopark(0x0?, 0x2780?, 0xe0?, 0xb0?, 0x5f61680?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0117ade78 sp=0xc0117ade58 pc=0x13bb516
   > runtime.goparkunlock(...)
   > 	/usr/local/go/src/runtime/proc.go:369
   > runtime.semacquire1(0xc0124a08b8, 0x54?, 0x1, 0x0)
   > 	/usr/local/go/src/runtime/sema.go:150 +0x1fe fp=0xc0117adee0 sp=0xc0117ade78 pc=0x13cce5e
   > sync.runtime_Semacquire(0xc011f63260?)
   > 	/usr/local/go/src/runtime/sema.go:62 +0x25 fp=0xc0117adf10 sp=0xc0117adee0 pc=0x13e9f65
   > sync.(*WaitGroup).Wait(0xc01039fc01?)
   > 	/usr/local/go/src/sync/waitgroup.go:139 +0x52 fp=0xc0117adf38 sp=0xc0117adf10 pc=0x13fd1f2
   > github.com/pingcap/tidb/executor.(*HashJoinExec).waitJoinWorkersAndCloseResultChan(0xc0124a06c0)
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:395 +0x33 fp=0xc0117adf78 sp=0xc0117adf38 pc=0x3061fb3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).waitJoinWorkersAndCloseResultChan-fm()
   > 	<autogenerated>:1 +0x26 fp=0xc0117adf90 sp=0xc0117adf78 pc=0x31277c6
   > github.com/pingcap/tidb/util.WithRecovery(0x23de786?, 0xc010a0fd00?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc0117adfc0 sp=0xc0117adf90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func5()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:338 +0x28 fp=0xc0117adfe0 sp=0xc0117adfc0 pc=0x3061288
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0117adfe8 sp=0xc0117adfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:338 +0x3b8
   > goroutine 1304 [select]:
   > runtime.gopark(0xc01133e610?, 0x2?, 0xb0?, 0x6a?, 0xc01133e58c?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc011e32be0 sp=0xc011e32bc0 pc=0x13bb516
   > runtime.selectgo(0xc011e32e10, 0xc01133e588, 0x0?, 0x0, 0x13cc174?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc011e32d20 sp=0xc011e32be0 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.(*HashJoinExec).runJoinWorker(0xc0124a06c0, 0x3, {0x5f8a1a8, 0x0, 0x0})
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:441 +0x4f4 fp=0xc011e32f10 sp=0xc011e32d20 pc=0x30626b4
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:335 +0xb3 fp=0xc011e32f90 sp=0xc011e32f10 pc=0x30613d3
   > github.com/pingcap/tidb/util.WithRecovery(0x5f539a0?, 0xc01133e7b8?)
   > 	/go/src/github.com/pingcap/tidb/util/misc.go:100 +0x53 fp=0xc011e32fc0 sp=0xc011e32f90 pc=0x1ffabd3
   > github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable.func4()
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x2a fp=0xc011e32fe0 sp=0xc011e32fc0 pc=0x30612ea
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc011e32fe8 sp=0xc011e32fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*HashJoinExec).fetchAndProbeHashTable
   > 	/go/src/github.com/pingcap/tidb/executor/join.go:333 +0x1c9
   > goroutine 801 [select]:
   > runtime.gopark(0xc012719f78?, 0x2?, 0xa0?, 0x9d?, 0xc012719eec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc012719d58 sp=0xc012719d38 pc=0x13bb516
   > runtime.selectgo(0xc012719f78, 0xc012719ee8, 0xc000dbae00?, 0x0, 0xfae2637f?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc012719e98 sp=0xc012719d58 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc00ff2c700, {0x400d6b0?, 0xc011e2fc80?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc012719fb8 sp=0xc012719e98 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc012719fe0 sp=0xc012719fb8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc012719fe8 sp=0xc012719fe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 1346 [select]:
   > runtime.gopark(0xc0117acf78?, 0x2?, 0xb0?, 0x30?, 0xc0117aceec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc0117acd58 sp=0xc0117acd38 pc=0x13bb516
   > runtime.selectgo(0xc0117acf78, 0xc0117acee8, 0x3aac226?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc0117ace98 sp=0xc0117acd58 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc00ff2c740, {0x400d6b0?, 0xc011e2fc80?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc0117acfb8 sp=0xc0117ace98 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc0117acfe0 sp=0xc0117acfb8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0117acfe8 sp=0xc0117acfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 1347 [select]:
   > runtime.gopark(0xc01254c778?, 0x2?, 0x0?, 0x0?, 0xc01254c6ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01254c558 sp=0xc01254c538 pc=0x13bb516
   > runtime.selectgo(0xc01254c778, 0xc01254c6e8, 0x3aac226?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01254c698 sp=0xc01254c558 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc00ff2c780, {0x400d6b0?, 0xc011e2fc80?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc01254c7b8 sp=0xc01254c698 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc01254c7e0 sp=0xc01254c7b8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01254c7e8 sp=0xc01254c7e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 1348 [select]:
   > runtime.gopark(0xc01254cf78?, 0x2?, 0x0?, 0x0?, 0xc01254ceec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01254cd58 sp=0xc01254cd38 pc=0x13bb516
   > runtime.selectgo(0xc01254cf78, 0xc01254cee8, 0x3aac226?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01254ce98 sp=0xc01254cd58 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc00ff2c7c0, {0x400d6b0?, 0xc011e2fc80?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc01254cfb8 sp=0xc01254ce98 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc01254cfe0 sp=0xc01254cfb8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01254cfe8 sp=0xc01254cfe0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 1349 [select]:
   > runtime.gopark(0xc01254d778?, 0x2?, 0x0?, 0x0?, 0xc01254d6ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc01254d558 sp=0xc01254d538 pc=0x13bb516
   > runtime.selectgo(0xc01254d778, 0xc01254d6e8, 0x3aac226?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc01254d698 sp=0xc01254d558 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc00ff2c800, {0x400d6b0?, 0xc011e2fc80?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc01254d7b8 sp=0xc01254d698 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc01254d7e0 sp=0xc01254d7b8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc01254d7e8 sp=0xc01254d7e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 143 [select]:
   > runtime.gopark(0xc012646778?, 0x2?, 0x0?, 0x0?, 0xc0126466ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc012646558 sp=0xc012646538 pc=0x13bb516
   > runtime.selectgo(0xc012646778, 0xc0126466e8, 0x3aac226?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc012646698 sp=0xc012646558 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc000671b40, {0x400d6b0?, 0xc011e2fc80?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc0126467b8 sp=0xc012646698 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc0126467e0 sp=0xc0126467b8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0126467e8 sp=0xc0126467e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 144 [select]:
   > runtime.gopark(0xc011345778?, 0x2?, 0x1?, 0x0?, 0xc0113456ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc011345558 sp=0xc011345538 pc=0x13bb516
   > runtime.selectgo(0xc011345778, 0xc0113456e8, 0x3aac226?, 0x0, 0xc012514370?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc011345698 sp=0xc011345558 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc000671b80, {0x400d6b0?, 0xc011e2fc80?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc0113457b8 sp=0xc011345698 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc0113457e0 sp=0xc0113457b8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc0113457e8 sp=0xc0113457e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 145 [select]:
   > runtime.gopark(0xc000a0c778?, 0x2?, 0x1?, 0xb5?, 0xc000a0c6ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000a0c558 sp=0xc000a0c538 pc=0x13bb516
   > runtime.selectgo(0xc000a0c778, 0xc000a0c6e8, 0x3aac226?, 0x0, 0x0?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000a0c698 sp=0xc000a0c558 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc000671bc0, {0x400d6b0?, 0xc011e2fc80?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc000a0c7b8 sp=0xc000a0c698 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc000a0c7e0 sp=0xc000a0c7b8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000a0c7e8 sp=0xc000a0c7e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
   > goroutine 1378 [select]:
   > runtime.gopark(0xc000a75778?, 0x2?, 0x45?, 0x10?, 0xc000a756ec?)
   > 	/usr/local/go/src/runtime/proc.go:363 +0xd6 fp=0xc000a75558 sp=0xc000a75538 pc=0x13bb516
   > runtime.selectgo(0xc000a75778, 0xc000a756e8, 0x3aac226?, 0x0, 0x537000006c5?, 0x1)
   > 	/usr/local/go/src/runtime/select.go:328 +0x7bc fp=0xc000a75698 sp=0xc000a75558 pc=0x13cbbdc
   > github.com/pingcap/tidb/executor.readProjectionInput(...)
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:460
   > github.com/pingcap/tidb/executor.(*projectionWorker).run(0xc000671c00, {0x400d6b0?, 0xc011e2fc80?})
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:428 +0x194 fp=0xc000a757b8 sp=0xc000a75698 pc=0x309a0f4
   > github.com/pingcap/tidb/executor.(*ProjectionExec).prepare.func2()
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x2e fp=0xc000a757e0 sp=0xc000a757b8 pc=0x309938e
   > runtime.goexit()
   > 	/usr/local/go/src/runtime/asm_amd64.s:1594 +0x1 fp=0xc000a757e8 sp=0xc000a757e0 pc=0x13ee6e1
   > created by github.com/pingcap/tidb/executor.(*ProjectionExec).prepare
   > 	/go/src/github.com/pingcap/tidb/executor/projection.go:276 +0x69b
