# Bug ID TIDB-30397-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/30397
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED


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
   > [2024/06/16 15:30:15.630 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=39] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/06/16 15:30:15.631 +00:00] [INFO] [ddl_worker.go:322] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:74, Type:drop schema, State:none, SchemaState:queueing, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:15.631 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/16 15:30:15.631 +00:00] [INFO] [ddl.go:571] ["[ddl] start DDL job"] [job="ID:74, Type:drop schema, State:none, SchemaState:queueing, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:15.631 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/06/16 15:30:15.632 +00:00] [INFO] [ddl_worker.go:729] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:74, Type:drop schema, State:none, SchemaState:queueing, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:15.631 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:15.633 +00:00] [INFO] [domain.go:138] ["diff load InfoSchema success"] [currentSchemaVersion=39] [neededSchemaVersion=40] ["start time"=82.693µs] [phyTblIDs="[70,72]"] [actionTypes="[4,4]"]
   > [2024/06/16 15:30:15.635 +00:00] [INFO] [ddl_worker.go:932] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=40] ["take time"=2.224539ms] [job="ID:74, Type:drop schema, State:running, SchemaState:write only, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:15.631 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:15.635 +00:00] [INFO] [ddl_worker.go:729] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:74, Type:drop schema, State:running, SchemaState:write only, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:15.631 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:15.636 +00:00] [INFO] [domain.go:138] ["diff load InfoSchema success"] [currentSchemaVersion=40] [neededSchemaVersion=41] ["start time"=84.928µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/16 15:30:15.638 +00:00] [INFO] [ddl_worker.go:932] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=41] ["take time"=2.336077ms] [job="ID:74, Type:drop schema, State:running, SchemaState:delete only, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:15.631 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:15.638 +00:00] [INFO] [ddl_worker.go:729] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:74, Type:drop schema, State:running, SchemaState:delete only, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:15.631 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:15.641 +00:00] [INFO] [domain.go:138] ["diff load InfoSchema success"] [currentSchemaVersion=41] [neededSchemaVersion=42] ["start time"=152.605µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/16 15:30:15.643 +00:00] [INFO] [ddl_worker.go:932] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=42] ["take time"=2.36988ms] [job="ID:74, Type:drop schema, State:done, SchemaState:queueing, SchemaID:68, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-16 15:30:15.631 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:15.643 +00:00] [INFO] [delete_range.go:464] ["[ddl] batch insert into delete-range table"] [jobID=74] [elementIDs="[70,72]"]
   > [2024/06/16 15:30:15.645 +00:00] [INFO] [delete_range.go:107] ["[ddl] add job into delete-range table"] [jobID=74] [jobType="drop schema"]
   > [2024/06/16 15:30:15.645 +00:00] [INFO] [ddl_worker.go:428] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:74, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:68, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-16 15:30:15.631 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:15.646 +00:00] [INFO] [ddl.go:634] ["[ddl] DDL job is finished"] [jobID=74]
   > [2024/06/16 15:30:15.646 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/16 15:30:15.647 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=42] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/06/16 15:30:15.648 +00:00] [INFO] [ddl_worker.go:322] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:76, Type:create schema, State:none, SchemaState:queueing, SchemaID:75, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-16 15:30:15.647 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/16 15:30:15.648 +00:00] [INFO] [ddl.go:571] ["[ddl] start DDL job"] [job="ID:76, Type:create schema, State:none, SchemaState:queueing, SchemaID:75, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-16 15:30:15.647 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/16 15:30:15.648 +00:00] [INFO] [ddl_worker.go:729] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:76, Type:create schema, State:none, SchemaState:queueing, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:15.647 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:15.649 +00:00] [INFO] [domain.go:138] ["diff load InfoSchema success"] [currentSchemaVersion=42] [neededSchemaVersion=43] ["start time"=224.682µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/16 15:30:15.650 +00:00] [INFO] [delete_range.go:238] ["[ddl] delRange emulator complete task"] [jobID=74] [elementID=70] [startKey=748000000000000046] [endKey=748000000000000047]
   > [2024/06/16 15:30:15.651 +00:00] [INFO] [ddl_worker.go:932] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=43] ["take time"=2.039039ms] [job="ID:76, Type:create schema, State:done, SchemaState:public, SchemaID:75, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-16 15:30:15.647 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:15.652 +00:00] [INFO] [ddl_worker.go:428] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:76, Type:create schema, State:synced, SchemaState:public, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:15.647 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:15.652 +00:00] [INFO] [ddl.go:634] ["[ddl] DDL job is finished"] [jobID=76]
   > [2024/06/16 15:30:15.652 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/16 15:30:15.654 +00:00] [INFO] [delete_range.go:238] ["[ddl] delRange emulator complete task"] [jobID=74] [elementID=72] [startKey=748000000000000048] [endKey=748000000000000049]
   > [2024/06/16 15:30:15.656 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=43] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_berydd`\n--\n\nDROP TABLE IF EXISTS `t_berydd`;"] [user=root@%]
   > [2024/06/16 15:30:15.656 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=43] [cur_db=testdb] [sql="CREATE TABLE `t_berydd` (\n  `c_ymgvrd` int(11) DEFAULT NULL,\n  `c_ee5vqb` int(11) DEFAULT NULL,\n  `c_xsjoqb` int(11) DEFAULT NULL,\n  `c_xqizm` text DEFAULT NULL,\n  `c__3lu4b` int(11) DEFAULT NULL,\n  `c_mp6ko` double DEFAULT NULL,\n  `c_ndnhmc` double DEFAULT NULL,\n  `c_cdqetd` double DEFAULT NULL,\n  `c_ioru4c` double NOT NULL,\n  PRIMARY KEY (`c_ioru4c`) /*T![clustered_index] NONCLUSTERED */,\n  KEY `t_c1q7y` (`c_ymgvrd`,`c_ee5vqb`,`c_xsjoqb`,`c_mp6ko`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/06/16 15:30:15.657 +00:00] [INFO] [ddl_worker.go:322] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:78, Type:create table, State:none, SchemaState:queueing, SchemaID:75, TableID:77, RowCount:0, ArgLen:1, start time: 2024-06-16 15:30:15.657 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/16 15:30:15.657 +00:00] [INFO] [ddl.go:571] ["[ddl] start DDL job"] [job="ID:78, Type:create table, State:none, SchemaState:queueing, SchemaID:75, TableID:77, RowCount:0, ArgLen:1, start time: 2024-06-16 15:30:15.657 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_berydd` (\n  `c_ymgvrd` int(11) DEFAULT NULL,\n  `c_ee5vqb` int(11) DEFAULT NULL,\n  `c_xsjoqb` int(11) DEFAULT NULL,\n  `c_xqizm` text DEFAULT NULL,\n  `c__3lu4b` int(11) DEFAULT NULL,\n  `c_mp6ko` double DEFAULT NULL,\n  `c_ndnhmc` double DEFAULT NULL,\n  `c_cdqetd` double DEFAULT NULL,\n  `c_ioru4c` double NOT NULL,\n  PRIMARY KEY (`c_ioru4c`) /*T![clustered_index] NONCLUSTERED */,\n  KEY `t_c1q7y` (`c_ymgvrd`,`c_ee5vqb`,`c_xsjoqb`,`c_mp6ko`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/16 15:30:15.658 +00:00] [INFO] [ddl_worker.go:729] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:78, Type:create table, State:none, SchemaState:queueing, SchemaID:75, TableID:77, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:15.657 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:15.661 +00:00] [INFO] [domain.go:138] ["diff load InfoSchema success"] [currentSchemaVersion=43] [neededSchemaVersion=44] ["start time"=355.776µs] [phyTblIDs="[77]"] [actionTypes="[8]"]
   > [2024/06/16 15:30:15.663 +00:00] [INFO] [ddl_worker.go:932] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=44] ["take time"=2.233618ms] [job="ID:78, Type:create table, State:done, SchemaState:public, SchemaID:75, TableID:77, RowCount:0, ArgLen:1, start time: 2024-06-16 15:30:15.657 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:15.664 +00:00] [INFO] [ddl_worker.go:428] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:78, Type:create table, State:synced, SchemaState:public, SchemaID:75, TableID:77, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:15.657 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:15.665 +00:00] [INFO] [ddl.go:634] ["[ddl] DDL job is finished"] [jobID=78]
   > [2024/06/16 15:30:15.665 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/16 15:30:15.665 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=66] ["first split key"=74800000000000004d]
   > [2024/06/16 15:30:15.665 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=66] ["first at"=74800000000000004d] ["first new region left"="{Id:66 StartKey:7480000000000000ff4800000000000000f8 EndKey:7480000000000000ff4d00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:67 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/16 15:30:15.665 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[66]"]
   > [2024/06/16 15:30:15.666 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=44] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_berydd` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/16 15:30:15.667 +00:00] [WARN] [2pc.go:1651] ["schemaLeaseChecker is not set for this transaction"] [sessionID=17] [startTS=450508047166210049] [commitTS=450508047166210050]
   > [2024/06/16 15:30:15.670 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=44] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_berydd` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/16 15:30:15.670 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=44] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_kqoy4`\n--\n\nDROP TABLE IF EXISTS `t_kqoy4`;"] [user=root@%]
   > [2024/06/16 15:30:15.671 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=44] [cur_db=testdb] [sql="CREATE TABLE `t_kqoy4` (\n  `c_embscb` int(11) DEFAULT NULL,\n  `c_gi3pxb` text DEFAULT NULL,\n  `c_fif_7c` text DEFAULT NULL,\n  `c_scsjqb` double DEFAULT NULL,\n  `c_cxqb1` text DEFAULT NULL,\n  `c_w1ibr` int(11) DEFAULT NULL,\n  `c_0lknib` double DEFAULT NULL,\n  `c_qfdzbd` double NOT NULL,\n  `c_7kdcs` double DEFAULT NULL,\n  PRIMARY KEY (`c_qfdzbd`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/06/16 15:30:15.672 +00:00] [INFO] [ddl_worker.go:322] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:80, Type:create table, State:none, SchemaState:queueing, SchemaID:75, TableID:79, RowCount:0, ArgLen:1, start time: 2024-06-16 15:30:15.671 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/16 15:30:15.672 +00:00] [INFO] [ddl.go:571] ["[ddl] start DDL job"] [job="ID:80, Type:create table, State:none, SchemaState:queueing, SchemaID:75, TableID:79, RowCount:0, ArgLen:1, start time: 2024-06-16 15:30:15.671 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_kqoy4` (\n  `c_embscb` int(11) DEFAULT NULL,\n  `c_gi3pxb` text DEFAULT NULL,\n  `c_fif_7c` text DEFAULT NULL,\n  `c_scsjqb` double DEFAULT NULL,\n  `c_cxqb1` text DEFAULT NULL,\n  `c_w1ibr` int(11) DEFAULT NULL,\n  `c_0lknib` double DEFAULT NULL,\n  `c_qfdzbd` double NOT NULL,\n  `c_7kdcs` double DEFAULT NULL,\n  PRIMARY KEY (`c_qfdzbd`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/16 15:30:15.673 +00:00] [INFO] [ddl_worker.go:729] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:80, Type:create table, State:none, SchemaState:queueing, SchemaID:75, TableID:79, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:15.671 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:15.675 +00:00] [INFO] [domain.go:138] ["diff load InfoSchema success"] [currentSchemaVersion=44] [neededSchemaVersion=45] ["start time"=426.804µs] [phyTblIDs="[79]"] [actionTypes="[8]"]
   > [2024/06/16 15:30:15.677 +00:00] [INFO] [ddl_worker.go:932] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=45] ["take time"=2.248565ms] [job="ID:80, Type:create table, State:done, SchemaState:public, SchemaID:75, TableID:79, RowCount:0, ArgLen:1, start time: 2024-06-16 15:30:15.671 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:15.678 +00:00] [INFO] [ddl_worker.go:428] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:80, Type:create table, State:synced, SchemaState:public, SchemaID:75, TableID:79, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:15.671 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:15.679 +00:00] [INFO] [ddl.go:634] ["[ddl] DDL job is finished"] [jobID=80]
   > [2024/06/16 15:30:15.679 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/16 15:30:15.680 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=68] ["first split key"=74800000000000004f]
   > [2024/06/16 15:30:15.680 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=68] ["first at"=74800000000000004f] ["first new region left"="{Id:68 StartKey:7480000000000000ff4d00000000000000f8 EndKey:7480000000000000ff4f00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:69 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/16 15:30:15.680 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[68]"]
   > [2024/06/16 15:30:15.680 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=45] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_kqoy4` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/16 15:30:15.681 +00:00] [WARN] [2pc.go:1651] ["schemaLeaseChecker is not set for this transaction"] [sessionID=17] [startTS=450508047169880065] [commitTS=450508047169880066]
   > [2024/06/16 15:30:15.683 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=45] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_kqoy4` ENABLE KEYS */;"] [user=root@%]

### Scenario 1
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
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
   > [2024/06/16 15:30:17.386 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=23] [schemaVersion=45] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/06/16 15:30:17.387 +00:00] [INFO] [ddl_worker.go:322] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:81, Type:drop schema, State:none, SchemaState:queueing, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:17.386 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/16 15:30:17.387 +00:00] [INFO] [ddl.go:571] ["[ddl] start DDL job"] [job="ID:81, Type:drop schema, State:none, SchemaState:queueing, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:17.386 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/06/16 15:30:17.387 +00:00] [INFO] [ddl_worker.go:729] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:81, Type:drop schema, State:none, SchemaState:queueing, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:17.386 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:17.389 +00:00] [INFO] [domain.go:138] ["diff load InfoSchema success"] [currentSchemaVersion=45] [neededSchemaVersion=46] ["start time"=73.683µs] [phyTblIDs="[77,79]"] [actionTypes="[4,4]"]
   > [2024/06/16 15:30:17.391 +00:00] [INFO] [ddl_worker.go:932] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=46] ["take time"=2.120614ms] [job="ID:81, Type:drop schema, State:running, SchemaState:write only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:17.386 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:17.391 +00:00] [INFO] [ddl_worker.go:729] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:81, Type:drop schema, State:running, SchemaState:write only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:17.386 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:17.392 +00:00] [INFO] [domain.go:138] ["diff load InfoSchema success"] [currentSchemaVersion=46] [neededSchemaVersion=47] ["start time"=46.166µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/16 15:30:17.394 +00:00] [INFO] [ddl_worker.go:932] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=47] ["take time"=2.575496ms] [job="ID:81, Type:drop schema, State:running, SchemaState:delete only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:17.386 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:17.394 +00:00] [INFO] [ddl_worker.go:729] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:81, Type:drop schema, State:running, SchemaState:delete only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:17.386 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:17.396 +00:00] [INFO] [domain.go:138] ["diff load InfoSchema success"] [currentSchemaVersion=47] [neededSchemaVersion=48] ["start time"=59.366µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/16 15:30:17.398 +00:00] [INFO] [ddl_worker.go:932] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=48] ["take time"=2.892439ms] [job="ID:81, Type:drop schema, State:done, SchemaState:queueing, SchemaID:75, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-16 15:30:17.386 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:17.399 +00:00] [INFO] [delete_range.go:464] ["[ddl] batch insert into delete-range table"] [jobID=81] [elementIDs="[77,79]"]
   > [2024/06/16 15:30:17.400 +00:00] [INFO] [delete_range.go:107] ["[ddl] add job into delete-range table"] [jobID=81] [jobType="drop schema"]
   > [2024/06/16 15:30:17.400 +00:00] [INFO] [ddl_worker.go:428] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:81, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:75, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-16 15:30:17.386 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:17.401 +00:00] [INFO] [ddl.go:634] ["[ddl] DDL job is finished"] [jobID=81]
   > [2024/06/16 15:30:17.401 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/16 15:30:17.402 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=23] [schemaVersion=48] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/06/16 15:30:17.403 +00:00] [INFO] [ddl_worker.go:322] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:83, Type:create schema, State:none, SchemaState:queueing, SchemaID:82, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-16 15:30:17.402 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/16 15:30:17.403 +00:00] [INFO] [ddl.go:571] ["[ddl] start DDL job"] [job="ID:83, Type:create schema, State:none, SchemaState:queueing, SchemaID:82, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-16 15:30:17.402 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/16 15:30:17.403 +00:00] [INFO] [ddl_worker.go:729] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:83, Type:create schema, State:none, SchemaState:queueing, SchemaID:82, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:17.402 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:17.404 +00:00] [INFO] [domain.go:138] ["diff load InfoSchema success"] [currentSchemaVersion=48] [neededSchemaVersion=49] ["start time"=106.928µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/16 15:30:17.405 +00:00] [INFO] [delete_range.go:238] ["[ddl] delRange emulator complete task"] [jobID=81] [elementID=77] [startKey=74800000000000004d] [endKey=74800000000000004e]
   > [2024/06/16 15:30:17.405 +00:00] [INFO] [ddl_worker.go:932] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=49] ["take time"=2.019693ms] [job="ID:83, Type:create schema, State:done, SchemaState:public, SchemaID:82, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-16 15:30:17.402 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:17.406 +00:00] [INFO] [ddl_worker.go:428] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:83, Type:create schema, State:synced, SchemaState:public, SchemaID:82, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:17.402 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:17.406 +00:00] [INFO] [ddl.go:634] ["[ddl] DDL job is finished"] [jobID=83]
   > [2024/06/16 15:30:17.406 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/16 15:30:17.408 +00:00] [INFO] [delete_range.go:238] ["[ddl] delRange emulator complete task"] [jobID=81] [elementID=79] [startKey=74800000000000004f] [endKey=748000000000000050]
   > [2024/06/16 15:30:17.409 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=23] [schemaVersion=49] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_berydd`\n--\n\nDROP TABLE IF EXISTS `t_berydd`;"] [user=root@%]
   > [2024/06/16 15:30:17.410 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=23] [schemaVersion=49] [cur_db=testdb] [sql="CREATE TABLE `t_berydd` (\n  `c_ymgvrd` int(11) DEFAULT NULL,\n  `c_ee5vqb` int(11) DEFAULT NULL,\n  `c_xsjoqb` int(11) DEFAULT NULL,\n  `c_xqizm` text DEFAULT NULL,\n  `c__3lu4b` int(11) DEFAULT NULL,\n  `c_mp6ko` double DEFAULT NULL,\n  `c_ndnhmc` double DEFAULT NULL,\n  `c_cdqetd` double DEFAULT NULL,\n  `c_ioru4c` double NOT NULL,\n  PRIMARY KEY (`c_ioru4c`) /*T![clustered_index] NONCLUSTERED */,\n  KEY `t_c1q7y` (`c_ymgvrd`,`c_ee5vqb`,`c_xsjoqb`,`c_mp6ko`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/06/16 15:30:17.411 +00:00] [INFO] [ddl_worker.go:322] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:85, Type:create table, State:none, SchemaState:queueing, SchemaID:82, TableID:84, RowCount:0, ArgLen:1, start time: 2024-06-16 15:30:17.41 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/16 15:30:17.411 +00:00] [INFO] [ddl.go:571] ["[ddl] start DDL job"] [job="ID:85, Type:create table, State:none, SchemaState:queueing, SchemaID:82, TableID:84, RowCount:0, ArgLen:1, start time: 2024-06-16 15:30:17.41 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_berydd` (\n  `c_ymgvrd` int(11) DEFAULT NULL,\n  `c_ee5vqb` int(11) DEFAULT NULL,\n  `c_xsjoqb` int(11) DEFAULT NULL,\n  `c_xqizm` text DEFAULT NULL,\n  `c__3lu4b` int(11) DEFAULT NULL,\n  `c_mp6ko` double DEFAULT NULL,\n  `c_ndnhmc` double DEFAULT NULL,\n  `c_cdqetd` double DEFAULT NULL,\n  `c_ioru4c` double NOT NULL,\n  PRIMARY KEY (`c_ioru4c`) /*T![clustered_index] NONCLUSTERED */,\n  KEY `t_c1q7y` (`c_ymgvrd`,`c_ee5vqb`,`c_xsjoqb`,`c_mp6ko`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/16 15:30:17.411 +00:00] [INFO] [ddl_worker.go:729] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:85, Type:create table, State:none, SchemaState:queueing, SchemaID:82, TableID:84, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:17.41 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:17.413 +00:00] [INFO] [domain.go:138] ["diff load InfoSchema success"] [currentSchemaVersion=49] [neededSchemaVersion=50] ["start time"=340.829µs] [phyTblIDs="[84]"] [actionTypes="[8]"]
   > [2024/06/16 15:30:17.415 +00:00] [INFO] [ddl_worker.go:932] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=50] ["take time"=2.136329ms] [job="ID:85, Type:create table, State:done, SchemaState:public, SchemaID:82, TableID:84, RowCount:0, ArgLen:1, start time: 2024-06-16 15:30:17.41 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:17.415 +00:00] [INFO] [ddl_worker.go:428] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:85, Type:create table, State:synced, SchemaState:public, SchemaID:82, TableID:84, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:17.41 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:17.416 +00:00] [INFO] [ddl.go:634] ["[ddl] DDL job is finished"] [jobID=85]
   > [2024/06/16 15:30:17.416 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/16 15:30:17.416 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=70] ["first split key"=748000000000000054]
   > [2024/06/16 15:30:17.416 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=70] ["first at"=748000000000000054] ["first new region left"="{Id:70 StartKey:7480000000000000ff4f00000000000000f8 EndKey:7480000000000000ff5400000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:71 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/16 15:30:17.416 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[70]"]
   > [2024/06/16 15:30:17.416 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=23] [schemaVersion=50] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_berydd` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/16 15:30:17.417 +00:00] [WARN] [2pc.go:1651] ["schemaLeaseChecker is not set for this transaction"] [sessionID=23] [startTS=450508047624962049] [commitTS=450508047624962050]
   > [2024/06/16 15:30:17.419 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=23] [schemaVersion=50] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_berydd` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/16 15:30:17.419 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=23] [schemaVersion=50] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_kqoy4`\n--\n\nDROP TABLE IF EXISTS `t_kqoy4`;"] [user=root@%]
   > [2024/06/16 15:30:17.419 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=23] [schemaVersion=50] [cur_db=testdb] [sql="CREATE TABLE `t_kqoy4` (\n  `c_embscb` int(11) DEFAULT NULL,\n  `c_gi3pxb` text DEFAULT NULL,\n  `c_fif_7c` text DEFAULT NULL,\n  `c_scsjqb` double DEFAULT NULL,\n  `c_cxqb1` text DEFAULT NULL,\n  `c_w1ibr` int(11) DEFAULT NULL,\n  `c_0lknib` double DEFAULT NULL,\n  `c_qfdzbd` double NOT NULL,\n  `c_7kdcs` double DEFAULT NULL,\n  PRIMARY KEY (`c_qfdzbd`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/06/16 15:30:17.420 +00:00] [INFO] [ddl_worker.go:322] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:87, Type:create table, State:none, SchemaState:queueing, SchemaID:82, TableID:86, RowCount:0, ArgLen:1, start time: 2024-06-16 15:30:17.42 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/16 15:30:17.420 +00:00] [INFO] [ddl.go:571] ["[ddl] start DDL job"] [job="ID:87, Type:create table, State:none, SchemaState:queueing, SchemaID:82, TableID:86, RowCount:0, ArgLen:1, start time: 2024-06-16 15:30:17.42 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_kqoy4` (\n  `c_embscb` int(11) DEFAULT NULL,\n  `c_gi3pxb` text DEFAULT NULL,\n  `c_fif_7c` text DEFAULT NULL,\n  `c_scsjqb` double DEFAULT NULL,\n  `c_cxqb1` text DEFAULT NULL,\n  `c_w1ibr` int(11) DEFAULT NULL,\n  `c_0lknib` double DEFAULT NULL,\n  `c_qfdzbd` double NOT NULL,\n  `c_7kdcs` double DEFAULT NULL,\n  PRIMARY KEY (`c_qfdzbd`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/16 15:30:17.420 +00:00] [INFO] [ddl_worker.go:729] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:87, Type:create table, State:none, SchemaState:queueing, SchemaID:82, TableID:86, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:17.42 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:17.421 +00:00] [INFO] [domain.go:138] ["diff load InfoSchema success"] [currentSchemaVersion=50] [neededSchemaVersion=51] ["start time"=262.396µs] [phyTblIDs="[86]"] [actionTypes="[8]"]
   > [2024/06/16 15:30:17.424 +00:00] [INFO] [ddl_worker.go:932] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=51] ["take time"=2.901728ms] [job="ID:87, Type:create table, State:done, SchemaState:public, SchemaID:82, TableID:86, RowCount:0, ArgLen:1, start time: 2024-06-16 15:30:17.42 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:17.425 +00:00] [INFO] [ddl_worker.go:428] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:87, Type:create table, State:synced, SchemaState:public, SchemaID:82, TableID:86, RowCount:0, ArgLen:0, start time: 2024-06-16 15:30:17.42 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/16 15:30:17.427 +00:00] [INFO] [ddl.go:634] ["[ddl] DDL job is finished"] [jobID=87]
   > [2024/06/16 15:30:17.427 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/16 15:30:17.427 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=72] ["first split key"=748000000000000056]
   > [2024/06/16 15:30:17.427 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=72] ["first at"=748000000000000056] ["first new region left"="{Id:72 StartKey:7480000000000000ff5400000000000000f8 EndKey:7480000000000000ff5600000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:73 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/16 15:30:17.427 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[72]"]
   > [2024/06/16 15:30:17.427 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=23] [schemaVersion=51] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_kqoy4` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/16 15:30:17.429 +00:00] [WARN] [2pc.go:1651] ["schemaLeaseChecker is not set for this transaction"] [sessionID=23] [startTS=450508047627845634] [commitTS=450508047628107776]
   > [2024/06/16 15:30:17.430 +00:00] [INFO] [session.go:3047] ["CRUCIAL OPERATION"] [conn=23] [schemaVersion=51] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_kqoy4` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/16 15:30:18.671 +00:00] [INFO] [set.go:139] ["set global var"] [conn=25] [name=tx_isolation] [val=READ-COMMITTED]
