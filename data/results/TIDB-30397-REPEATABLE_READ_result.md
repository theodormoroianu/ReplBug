# Bug ID TIDB-30397-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/30397
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ


## Details
 * Database: tidb-5.4.0
 * Number of scenarios: 2
 * Initial setup script: /home/theodor/Projects/MasterThesis/data/sql/TIDB-30397_mysql_bk.sql

## Results
### Scenario 0
 * Instruction #0:
     - SQL:  update t_berydd set c_cdqetd = t_berydd.c_ioru4c;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  select count(c_mp6ko) from t_berydd;
     - TID: 0
     - Output: [(39,)]

 * Container logs:
   > [2024/06/16 15:30:11.535 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=30] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/06/16 15:30:11.535 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=30] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/06/16 15:30:11.537 +00:00] [INFO] [ddl_worker.go:322] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:62, Type:create schema, State:none, SchemaState:queueing, SchemaID:61, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-16 15:30:11.536 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/16 15:30:11.537 +00:00] [INFO] [ddl.go:571] ["[ddl] start DDL job"] [job="ID:62, Type:create schema, State:none, SchemaState:queueing, SchemaID:61, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-16 15:30:11.536 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/16 15:30:11.537 +00:00] [INFO] [ddl_worker.go:729] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:62, Type:create schema, State:none, SchemaState:queueing, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:11.536 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:11.538 +00:00] [INFO] [domain.go:138] ["diff load InfoSchema success"] [currentSchemaVersion=30] [neededSchemaVersion=31] ["start time"=86.325µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/16 15:30:11.540 +00:00] [INFO] [ddl_worker.go:932] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=31] ["take time"=2.204844ms] [job="ID:62, Type:create schema, State:done, SchemaState:public, SchemaID:61, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-16 15:30:11.536 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:11.540 +00:00] [INFO] [ddl_worker.go:428] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:62, Type:create schema, State:synced, SchemaState:public, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:11.536 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:11.540 +00:00] [INFO] [ddl.go:634] ["[ddl] DDL job is finished"] [jobID=62]
   > [2024/06/16 15:30:11.540 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/16 15:30:11.556 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=31] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_berydd`\n--\n\nDROP TABLE IF EXISTS `t_berydd`;"] [user=root@%]
   > [2024/06/16 15:30:11.557 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=31] [cur_db=testdb] [sql="CREATE TABLE `t_berydd` (\n  `c_ymgvrd` int(11) DEFAULT NULL,\n  `c_ee5vqb` int(11) DEFAULT NULL,\n  `c_xsjoqb` int(11) DEFAULT NULL,\n  `c_xqizm` text DEFAULT NULL,\n  `c__3lu4b` int(11) DEFAULT NULL,\n  `c_mp6ko` double DEFAULT NULL,\n  `c_ndnhmc` double DEFAULT NULL,\n  `c_cdqetd` double DEFAULT NULL,\n  `c_ioru4c` double NOT NULL,\n  PRIMARY KEY (`c_ioru4c`) /*T![clustered_index] NONCLUSTERED */,\n  KEY `t_c1q7y` (`c_ymgvrd`,`c_ee5vqb`,`c_xsjoqb`,`c_mp6ko`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/06/16 15:30:11.558 +00:00] [INFO] [ddl_worker.go:322] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:64, Type:create table, State:none, SchemaState:queueing, SchemaID:61, TableID:63, RowCount:0, ArgLen:1, start time: 2024-06-16 15:30:11.558 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/16 15:30:11.558 +00:00] [INFO] [ddl.go:571] ["[ddl] start DDL job"] [job="ID:64, Type:create table, State:none, SchemaState:queueing, SchemaID:61, TableID:63, RowCount:0, ArgLen:1, start time: 2024-06-16 15:30:11.558 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_berydd` (\n  `c_ymgvrd` int(11) DEFAULT NULL,\n  `c_ee5vqb` int(11) DEFAULT NULL,\n  `c_xsjoqb` int(11) DEFAULT NULL,\n  `c_xqizm` text DEFAULT NULL,\n  `c__3lu4b` int(11) DEFAULT NULL,\n  `c_mp6ko` double DEFAULT NULL,\n  `c_ndnhmc` double DEFAULT NULL,\n  `c_cdqetd` double DEFAULT NULL,\n  `c_ioru4c` double NOT NULL,\n  PRIMARY KEY (`c_ioru4c`) /*T![clustered_index] NONCLUSTERED */,\n  KEY `t_c1q7y` (`c_ymgvrd`,`c_ee5vqb`,`c_xsjoqb`,`c_mp6ko`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/16 15:30:11.559 +00:00] [INFO] [ddl_worker.go:729] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:64, Type:create table, State:none, SchemaState:queueing, SchemaID:61, TableID:63, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:11.558 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:11.561 +00:00] [INFO] [domain.go:138] ["diff load InfoSchema success"] [currentSchemaVersion=31] [neededSchemaVersion=32] ["start time"=248.498µs] [phyTblIDs="[63]"] [actionTypes="[8]"]
   > [2024/06/16 15:30:11.563 +00:00] [INFO] [ddl_worker.go:932] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=32] ["take time"=2.026188ms] [job="ID:64, Type:create table, State:done, SchemaState:public, SchemaID:61, TableID:63, RowCount:0, ArgLen:1, start time: 2024-06-16 15:30:11.558 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:11.563 +00:00] [INFO] [ddl_worker.go:428] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:64, Type:create table, State:synced, SchemaState:public, SchemaID:61, TableID:63, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:11.558 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:11.564 +00:00] [INFO] [ddl.go:634] ["[ddl] DDL job is finished"] [jobID=64]
   > [2024/06/16 15:30:11.564 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/16 15:30:11.564 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=56] ["first split key"=74800000000000003f]
   > [2024/06/16 15:30:11.565 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=32] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_berydd` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/16 15:30:11.566 +00:00] [WARN] [2pc.go:1651] ["schemaLeaseChecker is not set for this transaction"] [sessionID=5] [startTS=450508046090895363] [commitTS=450508046091157504]
   > [2024/06/16 15:30:11.567 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=58] ["first at"=74800000000000003f] ["first new region left"="{Id:58 StartKey:7480000000000000ff3b00000000000000f8 EndKey:7480000000000000ff3f00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:59 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/16 15:30:11.567 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[58]"]
   > [2024/06/16 15:30:11.567 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=32] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_berydd` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/16 15:30:11.568 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=32] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_kqoy4`\n--\n\nDROP TABLE IF EXISTS `t_kqoy4`;"] [user=root@%]
   > [2024/06/16 15:30:11.568 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=32] [cur_db=testdb] [sql="CREATE TABLE `t_kqoy4` (\n  `c_embscb` int(11) DEFAULT NULL,\n  `c_gi3pxb` text DEFAULT NULL,\n  `c_fif_7c` text DEFAULT NULL,\n  `c_scsjqb` double DEFAULT NULL,\n  `c_cxqb1` text DEFAULT NULL,\n  `c_w1ibr` int(11) DEFAULT NULL,\n  `c_0lknib` double DEFAULT NULL,\n  `c_qfdzbd` double NOT NULL,\n  `c_7kdcs` double DEFAULT NULL,\n  PRIMARY KEY (`c_qfdzbd`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/06/16 15:30:11.570 +00:00] [INFO] [ddl_worker.go:322] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:66, Type:create table, State:none, SchemaState:queueing, SchemaID:61, TableID:65, RowCount:0, ArgLen:1, start time: 2024-06-16 15:30:11.569 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/16 15:30:11.570 +00:00] [INFO] [ddl.go:571] ["[ddl] start DDL job"] [job="ID:66, Type:create table, State:none, SchemaState:queueing, SchemaID:61, TableID:65, RowCount:0, ArgLen:1, start time: 2024-06-16 15:30:11.569 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_kqoy4` (\n  `c_embscb` int(11) DEFAULT NULL,\n  `c_gi3pxb` text DEFAULT NULL,\n  `c_fif_7c` text DEFAULT NULL,\n  `c_scsjqb` double DEFAULT NULL,\n  `c_cxqb1` text DEFAULT NULL,\n  `c_w1ibr` int(11) DEFAULT NULL,\n  `c_0lknib` double DEFAULT NULL,\n  `c_qfdzbd` double NOT NULL,\n  `c_7kdcs` double DEFAULT NULL,\n  PRIMARY KEY (`c_qfdzbd`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/16 15:30:11.570 +00:00] [INFO] [ddl_worker.go:729] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:create table, State:none, SchemaState:queueing, SchemaID:61, TableID:65, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:11.569 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:11.572 +00:00] [INFO] [domain.go:138] ["diff load InfoSchema success"] [currentSchemaVersion=32] [neededSchemaVersion=33] ["start time"=377.775µs] [phyTblIDs="[65]"] [actionTypes="[8]"]
   > [2024/06/16 15:30:11.574 +00:00] [INFO] [ddl_worker.go:932] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=33] ["take time"=2.133116ms] [job="ID:66, Type:create table, State:done, SchemaState:public, SchemaID:61, TableID:65, RowCount:0, ArgLen:1, start time: 2024-06-16 15:30:11.569 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:11.574 +00:00] [INFO] [ddl_worker.go:428] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:create table, State:synced, SchemaState:public, SchemaID:61, TableID:65, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:11.569 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:11.575 +00:00] [INFO] [ddl.go:634] ["[ddl] DDL job is finished"] [jobID=66]
   > [2024/06/16 15:30:11.575 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/16 15:30:11.575 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=58] ["first split key"=748000000000000041]
   > [2024/06/16 15:30:11.577 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=33] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_kqoy4` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/16 15:30:11.578 +00:00] [WARN] [2pc.go:1651] ["schemaLeaseChecker is not set for this transaction"] [sessionID=5] [startTS=450508046094041090] [commitTS=450508046094303232]
   > [2024/06/16 15:30:11.578 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=60] ["first at"=748000000000000041] ["first new region left"="{Id:60 StartKey:7480000000000000ff3f00000000000000f8 EndKey:7480000000000000ff4100000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:61 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/16 15:30:11.578 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[60]"]
   > [2024/06/16 15:30:11.578 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=33] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_kqoy4` ENABLE KEYS */;"] [user=root@%]

### Scenario 1
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  start transaction;
     - TID: 0
     - Output: None
 * Instruction #2:
     - SQL:  update t_berydd set c_cdqetd = t_berydd.c_ioru4c;
     - TID: 0
     - Output: None
 * Instruction #3:
     - SQL:  select count(c_mp6ko) from t_berydd;
     - TID: 0
     - Output: [(36,)]
 * Instruction #4:
     - SQL:  commit;
     - TID: 0
     - Output: None

 * Container logs:
   > [2024/06/16 15:30:13.237 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=33] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/06/16 15:30:13.238 +00:00] [INFO] [ddl_worker.go:322] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:67, Type:drop schema, State:none, SchemaState:queueing, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:13.237 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/16 15:30:13.238 +00:00] [INFO] [ddl.go:571] ["[ddl] start DDL job"] [job="ID:67, Type:drop schema, State:none, SchemaState:queueing, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:13.237 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/06/16 15:30:13.238 +00:00] [INFO] [ddl_worker.go:729] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:drop schema, State:none, SchemaState:queueing, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:13.237 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:13.240 +00:00] [INFO] [domain.go:138] ["diff load InfoSchema success"] [currentSchemaVersion=33] [neededSchemaVersion=34] ["start time"=105.81µs] [phyTblIDs="[63,65]"] [actionTypes="[4,4]"]
   > [2024/06/16 15:30:13.242 +00:00] [INFO] [ddl_worker.go:932] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=34] ["take time"=2.172088ms] [job="ID:67, Type:drop schema, State:running, SchemaState:write only, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:13.237 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:13.242 +00:00] [INFO] [ddl_worker.go:729] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:drop schema, State:running, SchemaState:write only, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:13.237 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:13.243 +00:00] [INFO] [domain.go:138] ["diff load InfoSchema success"] [currentSchemaVersion=34] [neededSchemaVersion=35] ["start time"=84.369µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/16 15:30:13.246 +00:00] [INFO] [ddl_worker.go:932] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=35] ["take time"=2.948034ms] [job="ID:67, Type:drop schema, State:running, SchemaState:delete only, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:13.237 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:13.246 +00:00] [INFO] [ddl_worker.go:729] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:drop schema, State:running, SchemaState:delete only, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:13.237 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:13.248 +00:00] [INFO] [domain.go:138] ["diff load InfoSchema success"] [currentSchemaVersion=35] [neededSchemaVersion=36] ["start time"=91.004µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/16 15:30:13.250 +00:00] [INFO] [ddl_worker.go:932] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=36] ["take time"=2.190457ms] [job="ID:67, Type:drop schema, State:done, SchemaState:queueing, SchemaID:61, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-16 15:30:13.237 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:13.250 +00:00] [INFO] [delete_range.go:464] ["[ddl] batch insert into delete-range table"] [jobID=67] [elementIDs="[63,65]"]
   > [2024/06/16 15:30:13.251 +00:00] [INFO] [delete_range.go:107] ["[ddl] add job into delete-range table"] [jobID=67] [jobType="drop schema"]
   > [2024/06/16 15:30:13.251 +00:00] [INFO] [ddl_worker.go:428] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:61, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-16 15:30:13.237 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:13.252 +00:00] [INFO] [ddl.go:634] ["[ddl] DDL job is finished"] [jobID=67]
   > [2024/06/16 15:30:13.252 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/16 15:30:13.253 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=36] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/06/16 15:30:13.254 +00:00] [INFO] [ddl_worker.go:322] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:69, Type:create schema, State:none, SchemaState:queueing, SchemaID:68, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-16 15:30:13.253 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/16 15:30:13.254 +00:00] [INFO] [ddl.go:571] ["[ddl] start DDL job"] [job="ID:69, Type:create schema, State:none, SchemaState:queueing, SchemaID:68, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-16 15:30:13.253 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/16 15:30:13.254 +00:00] [INFO] [ddl_worker.go:729] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:69, Type:create schema, State:none, SchemaState:queueing, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:13.253 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:13.255 +00:00] [INFO] [domain.go:138] ["diff load InfoSchema success"] [currentSchemaVersion=36] [neededSchemaVersion=37] ["start time"=154.56µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/16 15:30:13.257 +00:00] [INFO] [ddl_worker.go:932] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=37] ["take time"=2.04281ms] [job="ID:69, Type:create schema, State:done, SchemaState:public, SchemaID:68, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-16 15:30:13.253 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:13.257 +00:00] [INFO] [ddl_worker.go:428] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:69, Type:create schema, State:synced, SchemaState:public, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:13.253 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:13.258 +00:00] [INFO] [ddl.go:634] ["[ddl] DDL job is finished"] [jobID=69]
   > [2024/06/16 15:30:13.258 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/16 15:30:13.259 +00:00] [INFO] [delete_range.go:238] ["[ddl] delRange emulator complete task"] [jobID=67] [elementID=63] [startKey=74800000000000003f] [endKey=748000000000000040]
   > [2024/06/16 15:30:13.263 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=37] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_berydd`\n--\n\nDROP TABLE IF EXISTS `t_berydd`;"] [user=root@%]
   > [2024/06/16 15:30:13.263 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=37] [cur_db=testdb] [sql="CREATE TABLE `t_berydd` (\n  `c_ymgvrd` int(11) DEFAULT NULL,\n  `c_ee5vqb` int(11) DEFAULT NULL,\n  `c_xsjoqb` int(11) DEFAULT NULL,\n  `c_xqizm` text DEFAULT NULL,\n  `c__3lu4b` int(11) DEFAULT NULL,\n  `c_mp6ko` double DEFAULT NULL,\n  `c_ndnhmc` double DEFAULT NULL,\n  `c_cdqetd` double DEFAULT NULL,\n  `c_ioru4c` double NOT NULL,\n  PRIMARY KEY (`c_ioru4c`) /*T![clustered_index] NONCLUSTERED */,\n  KEY `t_c1q7y` (`c_ymgvrd`,`c_ee5vqb`,`c_xsjoqb`,`c_mp6ko`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/06/16 15:30:13.264 +00:00] [INFO] [delete_range.go:238] ["[ddl] delRange emulator complete task"] [jobID=67] [elementID=65] [startKey=748000000000000041] [endKey=748000000000000042]
   > [2024/06/16 15:30:13.264 +00:00] [INFO] [ddl_worker.go:322] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:71, Type:create table, State:none, SchemaState:queueing, SchemaID:68, TableID:70, RowCount:0, ArgLen:1, start time: 2024-06-16 15:30:13.264 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/16 15:30:13.264 +00:00] [INFO] [ddl.go:571] ["[ddl] start DDL job"] [job="ID:71, Type:create table, State:none, SchemaState:queueing, SchemaID:68, TableID:70, RowCount:0, ArgLen:1, start time: 2024-06-16 15:30:13.264 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_berydd` (\n  `c_ymgvrd` int(11) DEFAULT NULL,\n  `c_ee5vqb` int(11) DEFAULT NULL,\n  `c_xsjoqb` int(11) DEFAULT NULL,\n  `c_xqizm` text DEFAULT NULL,\n  `c__3lu4b` int(11) DEFAULT NULL,\n  `c_mp6ko` double DEFAULT NULL,\n  `c_ndnhmc` double DEFAULT NULL,\n  `c_cdqetd` double DEFAULT NULL,\n  `c_ioru4c` double NOT NULL,\n  PRIMARY KEY (`c_ioru4c`) /*T![clustered_index] NONCLUSTERED */,\n  KEY `t_c1q7y` (`c_ymgvrd`,`c_ee5vqb`,`c_xsjoqb`,`c_mp6ko`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/16 15:30:13.265 +00:00] [INFO] [ddl_worker.go:729] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:71, Type:create table, State:none, SchemaState:queueing, SchemaID:68, TableID:70, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:13.264 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:13.266 +00:00] [INFO] [domain.go:138] ["diff load InfoSchema success"] [currentSchemaVersion=37] [neededSchemaVersion=38] ["start time"=463.472µs] [phyTblIDs="[70]"] [actionTypes="[8]"]
   > [2024/06/16 15:30:13.268 +00:00] [INFO] [ddl_worker.go:932] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=38] ["take time"=2.025979ms] [job="ID:71, Type:create table, State:done, SchemaState:public, SchemaID:68, TableID:70, RowCount:0, ArgLen:1, start time: 2024-06-16 15:30:13.264 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:13.269 +00:00] [INFO] [ddl_worker.go:428] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:71, Type:create table, State:synced, SchemaState:public, SchemaID:68, TableID:70, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:13.264 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:13.270 +00:00] [INFO] [ddl.go:634] ["[ddl] DDL job is finished"] [jobID=71]
   > [2024/06/16 15:30:13.270 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/16 15:30:13.270 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=62] ["first split key"=748000000000000046]
   > [2024/06/16 15:30:13.270 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=62] ["first at"=748000000000000046] ["first new region left"="{Id:62 StartKey:7480000000000000ff4100000000000000f8 EndKey:7480000000000000ff4600000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:63 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/16 15:30:13.270 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[62]"]
   > [2024/06/16 15:30:13.270 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=38] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_berydd` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/16 15:30:13.271 +00:00] [WARN] [2pc.go:1651] ["schemaLeaseChecker is not set for this transaction"] [sessionID=11] [startTS=450508046538113025] [commitTS=450508046538113026]
   > [2024/06/16 15:30:13.272 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=38] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_berydd` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/16 15:30:13.273 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=38] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_kqoy4`\n--\n\nDROP TABLE IF EXISTS `t_kqoy4`;"] [user=root@%]
   > [2024/06/16 15:30:13.273 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=38] [cur_db=testdb] [sql="CREATE TABLE `t_kqoy4` (\n  `c_embscb` int(11) DEFAULT NULL,\n  `c_gi3pxb` text DEFAULT NULL,\n  `c_fif_7c` text DEFAULT NULL,\n  `c_scsjqb` double DEFAULT NULL,\n  `c_cxqb1` text DEFAULT NULL,\n  `c_w1ibr` int(11) DEFAULT NULL,\n  `c_0lknib` double DEFAULT NULL,\n  `c_qfdzbd` double NOT NULL,\n  `c_7kdcs` double DEFAULT NULL,\n  PRIMARY KEY (`c_qfdzbd`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/06/16 15:30:13.274 +00:00] [INFO] [ddl_worker.go:322] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:73, Type:create table, State:none, SchemaState:queueing, SchemaID:68, TableID:72, RowCount:0, ArgLen:1, start time: 2024-06-16 15:30:13.273 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/16 15:30:13.274 +00:00] [INFO] [ddl.go:571] ["[ddl] start DDL job"] [job="ID:73, Type:create table, State:none, SchemaState:queueing, SchemaID:68, TableID:72, RowCount:0, ArgLen:1, start time: 2024-06-16 15:30:13.273 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_kqoy4` (\n  `c_embscb` int(11) DEFAULT NULL,\n  `c_gi3pxb` text DEFAULT NULL,\n  `c_fif_7c` text DEFAULT NULL,\n  `c_scsjqb` double DEFAULT NULL,\n  `c_cxqb1` text DEFAULT NULL,\n  `c_w1ibr` int(11) DEFAULT NULL,\n  `c_0lknib` double DEFAULT NULL,\n  `c_qfdzbd` double NOT NULL,\n  `c_7kdcs` double DEFAULT NULL,\n  PRIMARY KEY (`c_qfdzbd`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/16 15:30:13.274 +00:00] [INFO] [ddl_worker.go:729] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:73, Type:create table, State:none, SchemaState:queueing, SchemaID:68, TableID:72, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:13.273 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:13.276 +00:00] [INFO] [domain.go:138] ["diff load InfoSchema success"] [currentSchemaVersion=38] [neededSchemaVersion=39] ["start time"=322.46µs] [phyTblIDs="[72]"] [actionTypes="[8]"]
   > [2024/06/16 15:30:13.277 +00:00] [INFO] [ddl_worker.go:932] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=39] ["take time"=2.259879ms] [job="ID:73, Type:create table, State:done, SchemaState:public, SchemaID:68, TableID:72, RowCount:0, ArgLen:1, start time: 2024-06-16 15:30:13.273 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:13.279 +00:00] [INFO] [ddl_worker.go:428] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:73, Type:create table, State:synced, SchemaState:public, SchemaID:68, TableID:72, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:13.273 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:13.279 +00:00] [INFO] [ddl.go:634] ["[ddl] DDL job is finished"] [jobID=73]
   > [2024/06/16 15:30:13.279 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/16 15:30:13.280 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=64] ["first split key"=748000000000000048]
   > [2024/06/16 15:30:13.280 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=64] ["first at"=748000000000000048] ["first new region left"="{Id:64 StartKey:7480000000000000ff4600000000000000f8 EndKey:7480000000000000ff4800000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:65 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/16 15:30:13.280 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=39] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_kqoy4` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/16 15:30:13.280 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[64]"]
   > [2024/06/16 15:30:13.281 +00:00] [WARN] [2pc.go:1651] ["schemaLeaseChecker is not set for this transaction"] [sessionID=11] [startTS=450508046540472323] [commitTS=450508046540734464]
   > [2024/06/16 15:30:13.281 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=39] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_kqoy4` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/16 15:30:14.524 +00:00] [INFO] [set.go:139] ["set global var"] [conn=13] [name=tx_isolation] [val=REPEATABLE-READ]
