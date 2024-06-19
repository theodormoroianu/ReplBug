# Bug ID TIDB-38170-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/38170
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ


## Details
 * Database: tidb-v6.3.0
 * Number of scenarios: 5
 * Initial setup script: /home/theodor/Projects/MasterThesis/data/sql/TIDB-38170_mysql_bk.sql

## Results
### Scenario 0
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  START TRANSACTION;
     - TID: 0
     - Output: None
 * Instruction #2:
     - SQL:  WITH cte_0 AS (select distinct ref_0.wkey as c0, ref_0.pkey as c1, ref_0.c_xhsn...
     - TID: 0
     - Output: [(104, 577000, 47.96), (108, 598000, None), (113, 619000, None), (106, 586000, None), (106, 588000, None)]
 * Instruction #3:
     - SQL:  COMMIT;
     - TID: 0
     - Output: None

 * Container logs:
   > [2024/06/19 09:52:47.774 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/06/19 09:52:47.777 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255957] [schemaVersion=33] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/06/19 09:52:47.778 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255957] [schemaVersion=33] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/06/19 09:52:47.781 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:69, Type:create schema, State:queueing, SchemaState:none, SchemaID:68, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 09:52:47.779 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/06/19 09:52:47.781 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:69, Type:create schema, State:queueing, SchemaState:none, SchemaID:68, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 09:52:47.779 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/19 09:52:48.513 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:69, Type:create schema, State:queueing, SchemaState:none, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:52:47.779 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:52:48.516 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=33] [neededSchemaVersion=34] ["start time"=212.04µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 09:52:48.518 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=34] ["take time"=2.382589ms] [job="ID:69, Type:create schema, State:done, SchemaState:public, SchemaID:68, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 09:52:47.779 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:52:48.525 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:69, Type:create schema, State:synced, SchemaState:public, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:52:47.779 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:52:48.528 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=69]
   > [2024/06/19 09:52:48.528 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/06/19 09:52:48.536 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255957] [schemaVersion=34] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_cqmg3b`\n--\n\nDROP TABLE IF EXISTS `t_cqmg3b`;"] [user=root@%]
   > [2024/06/19 09:52:48.537 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255957] [schemaVersion=34] [cur_db=testdb] [sql="CREATE TABLE `t_cqmg3b` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_anpf_c` int(11) DEFAULT NULL,\n  `c_b_fp_c` text DEFAULT NULL,\n  `c_ndccfb` int(11) DEFAULT NULL,\n  `c_8rswc` int(11) DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/06/19 09:52:48.540 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:71, Type:create table, State:queueing, SchemaState:none, SchemaID:68, TableID:70, RowCount:0, ArgLen:1, start time: 2024-06-19 09:52:48.538 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/06/19 09:52:48.540 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:71, Type:create table, State:queueing, SchemaState:none, SchemaID:68, TableID:70, RowCount:0, ArgLen:1, start time: 2024-06-19 09:52:48.538 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_cqmg3b` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_anpf_c` int(11) DEFAULT NULL,\n  `c_b_fp_c` text DEFAULT NULL,\n  `c_ndccfb` int(11) DEFAULT NULL,\n  `c_8rswc` int(11) DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/19 09:52:48.548 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:71, Type:create table, State:queueing, SchemaState:none, SchemaID:68, TableID:70, RowCount:0, ArgLen:0, start time: 2024-06-19 09:52:48.538 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:52:48.552 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=34] [neededSchemaVersion=35] ["start time"=549.098µs] [phyTblIDs="[70]"] [actionTypes="[8]"]
   > [2024/06/19 09:52:48.554 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=35] ["take time"=2.252543ms] [job="ID:71, Type:create table, State:done, SchemaState:public, SchemaID:68, TableID:70, RowCount:0, ArgLen:1, start time: 2024-06-19 09:52:48.538 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:52:48.559 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:71, Type:create table, State:synced, SchemaState:public, SchemaID:68, TableID:70, RowCount:0, ArgLen:0, start time: 2024-06-19 09:52:48.538 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:52:48.562 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=71]
   > [2024/06/19 09:52:48.562 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/06/19 09:52:48.562 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=66] ["first split key"=748000000000000046]
   > [2024/06/19 09:52:48.563 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=66] ["first at"=748000000000000046] ["first new region left"="{Id:66 StartKey:7480000000000000ff4200000000000000f8 EndKey:7480000000000000ff4600000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:67 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/19 09:52:48.563 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[66]"]
   > [2024/06/19 09:52:48.563 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255957] [schemaVersion=35] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_cqmg3b` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:52:48.567 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255957] [schemaVersion=35] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_cqmg3b` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:52:48.568 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255957] [schemaVersion=35] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_dnmxh`\n--\n\nDROP TABLE IF EXISTS `t_dnmxh`;"] [user=root@%]
   > [2024/06/19 09:52:48.569 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255957] [schemaVersion=35] [cur_db=testdb] [sql="CREATE TABLE `t_dnmxh` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_xhsndb` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/06/19 09:52:48.572 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:73, Type:create table, State:queueing, SchemaState:none, SchemaID:68, TableID:72, RowCount:0, ArgLen:1, start time: 2024-06-19 09:52:48.57 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/06/19 09:52:48.572 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:73, Type:create table, State:queueing, SchemaState:none, SchemaID:68, TableID:72, RowCount:0, ArgLen:1, start time: 2024-06-19 09:52:48.57 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_dnmxh` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_xhsndb` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/19 09:52:48.580 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:73, Type:create table, State:queueing, SchemaState:none, SchemaID:68, TableID:72, RowCount:0, ArgLen:0, start time: 2024-06-19 09:52:48.57 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:52:48.584 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=35] [neededSchemaVersion=36] ["start time"=419.401µs] [phyTblIDs="[72]"] [actionTypes="[8]"]
   > [2024/06/19 09:52:48.586 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=36] ["take time"=2.058243ms] [job="ID:73, Type:create table, State:done, SchemaState:public, SchemaID:68, TableID:72, RowCount:0, ArgLen:1, start time: 2024-06-19 09:52:48.57 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:52:48.591 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:73, Type:create table, State:synced, SchemaState:public, SchemaID:68, TableID:72, RowCount:0, ArgLen:0, start time: 2024-06-19 09:52:48.57 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:52:48.594 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=73]
   > [2024/06/19 09:52:48.594 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/06/19 09:52:48.594 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=68] ["first split key"=748000000000000048]
   > [2024/06/19 09:52:48.595 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=68] ["first at"=748000000000000048] ["first new region left"="{Id:68 StartKey:7480000000000000ff4600000000000000f8 EndKey:7480000000000000ff4800000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:69 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/19 09:52:48.595 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[68]"]
   > [2024/06/19 09:52:48.595 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255957] [schemaVersion=36] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_dnmxh` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:52:48.598 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255957] [schemaVersion=36] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_dnmxh` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:52:49.617 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/06/19 09:52:49.634 +00:00] [INFO] [set.go:149] ["set global var"] [conn=2199023255959] [name=tx_isolation] [val=REPEATABLE-READ]

### Scenario 1
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  START TRANSACTION;
     - TID: 0
     - Output: None
 * Instruction #2:
     - SQL:  WITH cte_0 AS (select distinct ref_0.wkey as c0, ref_0.pkey as c1, ref_0.c_xhsn...
     - TID: 0
     - Output: [(104, 577000, 47.96), (106, 586000, None), (108, 598000, None), (113, 619000, None), (106, 588000, None)]
 * Instruction #3:
     - SQL:  COMMIT;
     - TID: 0
     - Output: None

 * Container logs:
   > [2024/06/19 09:52:52.375 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/06/19 09:52:52.377 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255963] [schemaVersion=44] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/06/19 09:52:52.378 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:80, Type:drop schema, State:queueing, SchemaState:public, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:52:52.377 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/06/19 09:52:52.378 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:80, Type:drop schema, State:queueing, SchemaState:public, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:52:52.377 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/06/19 09:52:52.385 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:80, Type:drop schema, State:queueing, SchemaState:public, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:52:52.377 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:52:52.388 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=44] [neededSchemaVersion=45] ["start time"=86.743µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 09:52:52.390 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=45] ["take time"=2.457599ms] [job="ID:80, Type:drop schema, State:running, SchemaState:write only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:52:52.377 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:52:52.395 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:80, Type:drop schema, State:running, SchemaState:write only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:52:52.377 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:52:52.398 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=45] [neededSchemaVersion=46] ["start time"=120.129µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 09:52:52.400 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=46] ["take time"=2.331535ms] [job="ID:80, Type:drop schema, State:running, SchemaState:delete only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:52:52.377 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:52:52.404 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:80, Type:drop schema, State:running, SchemaState:delete only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:52:52.377 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:52:52.408 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=46] [neededSchemaVersion=47] ["start time"=87.302µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 09:52:52.410 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=47] ["take time"=2.239063ms] [job="ID:80, Type:drop schema, State:done, SchemaState:none, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:52:52.377 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:52:52.414 +00:00] [INFO] [delete_range.go:109] ["[ddl] add job into delete-range table"] [jobID=80] [jobType="drop schema"]
   > [2024/06/19 09:52:52.414 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:80, Type:drop schema, State:synced, SchemaState:none, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:52:52.377 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:52:52.416 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=80]
   > [2024/06/19 09:52:52.416 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/06/19 09:52:52.418 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255963] [schemaVersion=47] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/06/19 09:52:52.421 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:82, Type:create schema, State:queueing, SchemaState:none, SchemaID:81, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 09:52:52.419 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/06/19 09:52:52.421 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:82, Type:create schema, State:queueing, SchemaState:none, SchemaID:81, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 09:52:52.419 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/19 09:52:52.429 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:82, Type:create schema, State:queueing, SchemaState:none, SchemaID:81, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:52:52.419 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:52:52.433 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=47] [neededSchemaVersion=48] ["start time"=162.452µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 09:52:52.435 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=48] ["take time"=2.781037ms] [job="ID:82, Type:create schema, State:done, SchemaState:public, SchemaID:81, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 09:52:52.419 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:52:52.439 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:82, Type:create schema, State:synced, SchemaState:public, SchemaID:81, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:52:52.419 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:52:52.441 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=82]
   > [2024/06/19 09:52:52.442 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/06/19 09:52:52.448 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255963] [schemaVersion=48] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_cqmg3b`\n--\n\nDROP TABLE IF EXISTS `t_cqmg3b`;"] [user=root@%]
   > [2024/06/19 09:52:52.449 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255963] [schemaVersion=48] [cur_db=testdb] [sql="CREATE TABLE `t_cqmg3b` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_anpf_c` int(11) DEFAULT NULL,\n  `c_b_fp_c` text DEFAULT NULL,\n  `c_ndccfb` int(11) DEFAULT NULL,\n  `c_8rswc` int(11) DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/06/19 09:52:52.452 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:84, Type:create table, State:queueing, SchemaState:none, SchemaID:81, TableID:83, RowCount:0, ArgLen:1, start time: 2024-06-19 09:52:52.45 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/06/19 09:52:52.452 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:84, Type:create table, State:queueing, SchemaState:none, SchemaID:81, TableID:83, RowCount:0, ArgLen:1, start time: 2024-06-19 09:52:52.45 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_cqmg3b` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_anpf_c` int(11) DEFAULT NULL,\n  `c_b_fp_c` text DEFAULT NULL,\n  `c_ndccfb` int(11) DEFAULT NULL,\n  `c_8rswc` int(11) DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/19 09:52:52.459 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:84, Type:create table, State:queueing, SchemaState:none, SchemaID:81, TableID:83, RowCount:0, ArgLen:0, start time: 2024-06-19 09:52:52.45 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:52:52.464 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=48] [neededSchemaVersion=49] ["start time"=436.931µs] [phyTblIDs="[83]"] [actionTypes="[8]"]
   > [2024/06/19 09:52:52.465 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=49] ["take time"=2.056776ms] [job="ID:84, Type:create table, State:done, SchemaState:public, SchemaID:81, TableID:83, RowCount:0, ArgLen:1, start time: 2024-06-19 09:52:52.45 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:52:52.469 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:84, Type:create table, State:synced, SchemaState:public, SchemaID:81, TableID:83, RowCount:0, ArgLen:0, start time: 2024-06-19 09:52:52.45 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:52:52.472 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=84]
   > [2024/06/19 09:52:52.472 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/06/19 09:52:52.472 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=72] ["first split key"=748000000000000053]
   > [2024/06/19 09:52:52.473 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=72] ["first at"=748000000000000053] ["first new region left"="{Id:72 StartKey:7480000000000000ff4d00000000000000f8 EndKey:7480000000000000ff5300000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:73 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/19 09:52:52.473 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[72]"]
   > [2024/06/19 09:52:52.473 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255963] [schemaVersion=49] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_cqmg3b` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:52:52.476 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255963] [schemaVersion=49] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_cqmg3b` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:52:52.477 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255963] [schemaVersion=49] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_dnmxh`\n--\n\nDROP TABLE IF EXISTS `t_dnmxh`;"] [user=root@%]
   > [2024/06/19 09:52:52.478 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255963] [schemaVersion=49] [cur_db=testdb] [sql="CREATE TABLE `t_dnmxh` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_xhsndb` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/06/19 09:52:52.481 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:86, Type:create table, State:queueing, SchemaState:none, SchemaID:81, TableID:85, RowCount:0, ArgLen:1, start time: 2024-06-19 09:52:52.479 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/06/19 09:52:52.481 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:86, Type:create table, State:queueing, SchemaState:none, SchemaID:81, TableID:85, RowCount:0, ArgLen:1, start time: 2024-06-19 09:52:52.479 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_dnmxh` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_xhsndb` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/19 09:52:52.488 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:86, Type:create table, State:queueing, SchemaState:none, SchemaID:81, TableID:85, RowCount:0, ArgLen:0, start time: 2024-06-19 09:52:52.479 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:52:52.491 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=49] [neededSchemaVersion=50] ["start time"=405.503µs] [phyTblIDs="[85]"] [actionTypes="[8]"]
   > [2024/06/19 09:52:52.493 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=50] ["take time"=2.068091ms] [job="ID:86, Type:create table, State:done, SchemaState:public, SchemaID:81, TableID:85, RowCount:0, ArgLen:1, start time: 2024-06-19 09:52:52.479 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:52:52.497 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:86, Type:create table, State:synced, SchemaState:public, SchemaID:81, TableID:85, RowCount:0, ArgLen:0, start time: 2024-06-19 09:52:52.479 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:52:52.500 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=86]
   > [2024/06/19 09:52:52.500 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/06/19 09:52:52.500 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=74] ["first split key"=748000000000000055]
   > [2024/06/19 09:52:52.500 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=74] ["first at"=748000000000000055] ["first new region left"="{Id:74 StartKey:7480000000000000ff5300000000000000f8 EndKey:7480000000000000ff5500000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:75 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/19 09:52:52.501 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[74]"]
   > [2024/06/19 09:52:52.501 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255963] [schemaVersion=50] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_dnmxh` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:52:52.503 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255963] [schemaVersion=50] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_dnmxh` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:52:53.517 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/06/19 09:52:53.530 +00:00] [INFO] [set.go:149] ["set global var"] [conn=2199023255965] [name=tx_isolation] [val=REPEATABLE-READ]

### Scenario 2
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  START TRANSACTION;
     - TID: 0
     - Output: None
 * Instruction #2:
     - SQL:  WITH cte_0 AS (select distinct ref_0.wkey as c0, ref_0.pkey as c1, ref_0.c_xhsn...
     - TID: 0
     - Output: [(106, 589000, None), (108, 597000, 47.51), (113, 617000, None), (113, 623000, 63.81), (104, 576000, 92.4), (113, 618000, 92.6), (113, 620000, 91.65), (113, 622000, 31.3)]
 * Instruction #3:
     - SQL:  COMMIT;
     - TID: 0
     - Output: None

 * Container logs:
   > [2024/06/19 09:52:56.330 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/06/19 09:52:56.333 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255969] [schemaVersion=58] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/06/19 09:52:56.335 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:93, Type:drop schema, State:queueing, SchemaState:public, SchemaID:88, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:52:56.333 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/06/19 09:52:56.336 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:93, Type:drop schema, State:queueing, SchemaState:public, SchemaID:88, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:52:56.333 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/06/19 09:52:56.342 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:93, Type:drop schema, State:queueing, SchemaState:public, SchemaID:88, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:52:56.333 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:52:56.345 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=58] [neededSchemaVersion=59] ["start time"=63.487µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 09:52:56.347 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=59] ["take time"=2.274194ms] [job="ID:93, Type:drop schema, State:running, SchemaState:write only, SchemaID:88, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:52:56.333 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:52:56.351 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:93, Type:drop schema, State:running, SchemaState:write only, SchemaID:88, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:52:56.333 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:52:56.354 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=59] [neededSchemaVersion=60] ["start time"=59.156µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 09:52:56.356 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=60] ["take time"=2.299268ms] [job="ID:93, Type:drop schema, State:running, SchemaState:delete only, SchemaID:88, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:52:56.333 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:52:56.360 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:93, Type:drop schema, State:running, SchemaState:delete only, SchemaID:88, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:52:56.333 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:52:56.363 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=60] [neededSchemaVersion=61] ["start time"=94.496µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 09:52:56.365 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=61] ["take time"=2.31589ms] [job="ID:93, Type:drop schema, State:done, SchemaState:none, SchemaID:88, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:52:56.333 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:52:56.370 +00:00] [INFO] [delete_range.go:109] ["[ddl] add job into delete-range table"] [jobID=93] [jobType="drop schema"]
   > [2024/06/19 09:52:56.370 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:93, Type:drop schema, State:synced, SchemaState:none, SchemaID:88, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:52:56.333 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:52:56.372 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=93]
   > [2024/06/19 09:52:56.372 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/06/19 09:52:56.374 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255969] [schemaVersion=61] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/06/19 09:52:56.377 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:95, Type:create schema, State:queueing, SchemaState:none, SchemaID:94, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 09:52:56.375 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/06/19 09:52:56.377 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:95, Type:create schema, State:queueing, SchemaState:none, SchemaID:94, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 09:52:56.375 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/19 09:52:56.385 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:95, Type:create schema, State:queueing, SchemaState:none, SchemaID:94, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:52:56.375 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:52:56.388 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=61] [neededSchemaVersion=62] ["start time"=158.331µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 09:52:56.390 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=62] ["take time"=2.345712ms] [job="ID:95, Type:create schema, State:done, SchemaState:public, SchemaID:94, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 09:52:56.375 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:52:56.393 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:95, Type:create schema, State:synced, SchemaState:public, SchemaID:94, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:52:56.375 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:52:56.395 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=95]
   > [2024/06/19 09:52:56.395 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/06/19 09:52:56.402 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255969] [schemaVersion=62] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_cqmg3b`\n--\n\nDROP TABLE IF EXISTS `t_cqmg3b`;"] [user=root@%]
   > [2024/06/19 09:52:56.403 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255969] [schemaVersion=62] [cur_db=testdb] [sql="CREATE TABLE `t_cqmg3b` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_anpf_c` int(11) DEFAULT NULL,\n  `c_b_fp_c` text DEFAULT NULL,\n  `c_ndccfb` int(11) DEFAULT NULL,\n  `c_8rswc` int(11) DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/06/19 09:52:56.406 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:97, Type:create table, State:queueing, SchemaState:none, SchemaID:94, TableID:96, RowCount:0, ArgLen:1, start time: 2024-06-19 09:52:56.404 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/06/19 09:52:56.406 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:97, Type:create table, State:queueing, SchemaState:none, SchemaID:94, TableID:96, RowCount:0, ArgLen:1, start time: 2024-06-19 09:52:56.404 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_cqmg3b` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_anpf_c` int(11) DEFAULT NULL,\n  `c_b_fp_c` text DEFAULT NULL,\n  `c_ndccfb` int(11) DEFAULT NULL,\n  `c_8rswc` int(11) DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/19 09:52:56.413 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:97, Type:create table, State:queueing, SchemaState:none, SchemaID:94, TableID:96, RowCount:0, ArgLen:0, start time: 2024-06-19 09:52:56.404 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:52:56.418 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=62] [neededSchemaVersion=63] ["start time"=430.995µs] [phyTblIDs="[96]"] [actionTypes="[8]"]
   > [2024/06/19 09:52:56.419 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=63] ["take time"=2.06851ms] [job="ID:97, Type:create table, State:done, SchemaState:public, SchemaID:94, TableID:96, RowCount:0, ArgLen:1, start time: 2024-06-19 09:52:56.404 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:52:56.424 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:97, Type:create table, State:synced, SchemaState:public, SchemaID:94, TableID:96, RowCount:0, ArgLen:0, start time: 2024-06-19 09:52:56.404 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:52:56.427 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=97]
   > [2024/06/19 09:52:56.427 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/06/19 09:52:56.427 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=78] ["first split key"=748000000000000060]
   > [2024/06/19 09:52:56.428 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=78] ["first at"=748000000000000060] ["first new region left"="{Id:78 StartKey:7480000000000000ff5a00000000000000f8 EndKey:7480000000000000ff6000000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:79 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/19 09:52:56.428 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[78]"]
   > [2024/06/19 09:52:56.428 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255969] [schemaVersion=63] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_cqmg3b` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:52:56.432 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255969] [schemaVersion=63] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_cqmg3b` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:52:56.433 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255969] [schemaVersion=63] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_dnmxh`\n--\n\nDROP TABLE IF EXISTS `t_dnmxh`;"] [user=root@%]
   > [2024/06/19 09:52:56.433 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255969] [schemaVersion=63] [cur_db=testdb] [sql="CREATE TABLE `t_dnmxh` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_xhsndb` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/06/19 09:52:56.436 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:99, Type:create table, State:queueing, SchemaState:none, SchemaID:94, TableID:98, RowCount:0, ArgLen:1, start time: 2024-06-19 09:52:56.434 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/06/19 09:52:56.437 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:99, Type:create table, State:queueing, SchemaState:none, SchemaID:94, TableID:98, RowCount:0, ArgLen:1, start time: 2024-06-19 09:52:56.434 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_dnmxh` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_xhsndb` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/19 09:52:56.443 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:99, Type:create table, State:queueing, SchemaState:none, SchemaID:94, TableID:98, RowCount:0, ArgLen:0, start time: 2024-06-19 09:52:56.434 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:52:56.447 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=63] [neededSchemaVersion=64] ["start time"=440.423µs] [phyTblIDs="[98]"] [actionTypes="[8]"]
   > [2024/06/19 09:52:56.448 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=64] ["take time"=2.021855ms] [job="ID:99, Type:create table, State:done, SchemaState:public, SchemaID:94, TableID:98, RowCount:0, ArgLen:1, start time: 2024-06-19 09:52:56.434 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:52:56.453 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:99, Type:create table, State:synced, SchemaState:public, SchemaID:94, TableID:98, RowCount:0, ArgLen:0, start time: 2024-06-19 09:52:56.434 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:52:56.455 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=99]
   > [2024/06/19 09:52:56.455 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/06/19 09:52:56.455 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=80] ["first split key"=748000000000000062]
   > [2024/06/19 09:52:56.456 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=80] ["first at"=748000000000000062] ["first new region left"="{Id:80 StartKey:7480000000000000ff6000000000000000f8 EndKey:7480000000000000ff6200000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:81 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/19 09:52:56.456 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[80]"]
   > [2024/06/19 09:52:56.457 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255969] [schemaVersion=64] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_dnmxh` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:52:56.459 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255969] [schemaVersion=64] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_dnmxh` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:52:57.473 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/06/19 09:52:57.488 +00:00] [INFO] [set.go:149] ["set global var"] [conn=2199023255971] [name=tx_isolation] [val=REPEATABLE-READ]

### Scenario 3
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  START TRANSACTION;
     - TID: 0
     - Output: None
 * Instruction #2:
     - SQL:  WITH cte_0 AS (select distinct ref_0.wkey as c0, ref_0.pkey as c1, ref_0.c_xhsn...
     - TID: 0
     - Output: [(106, 586000, None), (104, 577000, 47.96), (113, 619000, None), (108, 598000, None), (106, 588000, None)]
 * Instruction #3:
     - SQL:  COMMIT;
     - TID: 0
     - Output: None

 * Container logs:
   > [2024/06/19 09:53:00.356 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/06/19 09:53:00.358 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255975] [schemaVersion=72] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/06/19 09:53:00.361 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:106, Type:drop schema, State:queueing, SchemaState:public, SchemaID:101, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:53:00.359 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/06/19 09:53:00.361 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:106, Type:drop schema, State:queueing, SchemaState:public, SchemaID:101, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:53:00.359 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/06/19 09:53:00.367 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:106, Type:drop schema, State:queueing, SchemaState:public, SchemaID:101, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:53:00.359 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:53:00.371 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=72] [neededSchemaVersion=73] ["start time"=78.851µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 09:53:00.373 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=73] ["take time"=2.261692ms] [job="ID:106, Type:drop schema, State:running, SchemaState:write only, SchemaID:101, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:53:00.359 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:53:00.377 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:106, Type:drop schema, State:running, SchemaState:write only, SchemaID:101, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:53:00.359 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:53:00.380 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=73] [neededSchemaVersion=74] ["start time"=82.903µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 09:53:00.382 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=74] ["take time"=2.323502ms] [job="ID:106, Type:drop schema, State:running, SchemaState:delete only, SchemaID:101, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:53:00.359 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:53:00.386 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:106, Type:drop schema, State:running, SchemaState:delete only, SchemaID:101, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:53:00.359 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:53:00.389 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=74] [neededSchemaVersion=75] ["start time"=84.09µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 09:53:00.391 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=75] ["take time"=2.268328ms] [job="ID:106, Type:drop schema, State:done, SchemaState:none, SchemaID:101, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:53:00.359 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:53:00.395 +00:00] [INFO] [delete_range.go:109] ["[ddl] add job into delete-range table"] [jobID=106] [jobType="drop schema"]
   > [2024/06/19 09:53:00.395 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:106, Type:drop schema, State:synced, SchemaState:none, SchemaID:101, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:53:00.359 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:53:00.397 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=106]
   > [2024/06/19 09:53:00.397 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/06/19 09:53:00.399 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255975] [schemaVersion=75] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/06/19 09:53:00.402 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:108, Type:create schema, State:queueing, SchemaState:none, SchemaID:107, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 09:53:00.4 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/06/19 09:53:00.402 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:108, Type:create schema, State:queueing, SchemaState:none, SchemaID:107, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 09:53:00.4 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/19 09:53:00.410 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:108, Type:create schema, State:queueing, SchemaState:none, SchemaID:107, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:53:00.4 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:53:00.413 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=75] [neededSchemaVersion=76] ["start time"=139.055µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 09:53:00.415 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=76] ["take time"=2.285159ms] [job="ID:108, Type:create schema, State:done, SchemaState:public, SchemaID:107, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 09:53:00.4 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:53:00.419 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:108, Type:create schema, State:synced, SchemaState:public, SchemaID:107, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:53:00.4 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:53:00.421 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=108]
   > [2024/06/19 09:53:00.421 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/06/19 09:53:00.429 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255975] [schemaVersion=76] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_cqmg3b`\n--\n\nDROP TABLE IF EXISTS `t_cqmg3b`;"] [user=root@%]
   > [2024/06/19 09:53:00.430 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255975] [schemaVersion=76] [cur_db=testdb] [sql="CREATE TABLE `t_cqmg3b` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_anpf_c` int(11) DEFAULT NULL,\n  `c_b_fp_c` text DEFAULT NULL,\n  `c_ndccfb` int(11) DEFAULT NULL,\n  `c_8rswc` int(11) DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/06/19 09:53:00.433 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:110, Type:create table, State:queueing, SchemaState:none, SchemaID:107, TableID:109, RowCount:0, ArgLen:1, start time: 2024-06-19 09:53:00.431 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/06/19 09:53:00.433 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:110, Type:create table, State:queueing, SchemaState:none, SchemaID:107, TableID:109, RowCount:0, ArgLen:1, start time: 2024-06-19 09:53:00.431 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_cqmg3b` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_anpf_c` int(11) DEFAULT NULL,\n  `c_b_fp_c` text DEFAULT NULL,\n  `c_ndccfb` int(11) DEFAULT NULL,\n  `c_8rswc` int(11) DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/19 09:53:00.440 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:110, Type:create table, State:queueing, SchemaState:none, SchemaID:107, TableID:109, RowCount:0, ArgLen:0, start time: 2024-06-19 09:53:00.431 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:53:00.444 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=76] [neededSchemaVersion=77] ["start time"=452.227µs] [phyTblIDs="[109]"] [actionTypes="[8]"]
   > [2024/06/19 09:53:00.446 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=77] ["take time"=2.064389ms] [job="ID:110, Type:create table, State:done, SchemaState:public, SchemaID:107, TableID:109, RowCount:0, ArgLen:1, start time: 2024-06-19 09:53:00.431 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:53:00.450 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:110, Type:create table, State:synced, SchemaState:public, SchemaID:107, TableID:109, RowCount:0, ArgLen:0, start time: 2024-06-19 09:53:00.431 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:53:00.453 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=110]
   > [2024/06/19 09:53:00.453 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/06/19 09:53:00.453 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=84] ["first split key"=74800000000000006d]
   > [2024/06/19 09:53:00.453 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=84] ["first at"=74800000000000006d] ["first new region left"="{Id:84 StartKey:7480000000000000ff6700000000000000f8 EndKey:7480000000000000ff6d00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:85 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/19 09:53:00.454 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[84]"]
   > [2024/06/19 09:53:00.454 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255975] [schemaVersion=77] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_cqmg3b` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:53:00.457 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255975] [schemaVersion=77] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_cqmg3b` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:53:00.458 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255975] [schemaVersion=77] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_dnmxh`\n--\n\nDROP TABLE IF EXISTS `t_dnmxh`;"] [user=root@%]
   > [2024/06/19 09:53:00.459 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255975] [schemaVersion=77] [cur_db=testdb] [sql="CREATE TABLE `t_dnmxh` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_xhsndb` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/06/19 09:53:00.462 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:112, Type:create table, State:queueing, SchemaState:none, SchemaID:107, TableID:111, RowCount:0, ArgLen:1, start time: 2024-06-19 09:53:00.46 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/06/19 09:53:00.462 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:112, Type:create table, State:queueing, SchemaState:none, SchemaID:107, TableID:111, RowCount:0, ArgLen:1, start time: 2024-06-19 09:53:00.46 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_dnmxh` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_xhsndb` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/19 09:53:00.469 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:112, Type:create table, State:queueing, SchemaState:none, SchemaID:107, TableID:111, RowCount:0, ArgLen:0, start time: 2024-06-19 09:53:00.46 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:53:00.473 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=77] [neededSchemaVersion=78] ["start time"=395.026µs] [phyTblIDs="[111]"] [actionTypes="[8]"]
   > [2024/06/19 09:53:00.475 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=78] ["take time"=2.474152ms] [job="ID:112, Type:create table, State:done, SchemaState:public, SchemaID:107, TableID:111, RowCount:0, ArgLen:1, start time: 2024-06-19 09:53:00.46 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:53:00.479 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:112, Type:create table, State:synced, SchemaState:public, SchemaID:107, TableID:111, RowCount:0, ArgLen:0, start time: 2024-06-19 09:53:00.46 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:53:00.482 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=112]
   > [2024/06/19 09:53:00.482 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/06/19 09:53:00.482 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=86] ["first split key"=74800000000000006f]
   > [2024/06/19 09:53:00.483 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=86] ["first at"=74800000000000006f] ["first new region left"="{Id:86 StartKey:7480000000000000ff6d00000000000000f8 EndKey:7480000000000000ff6f00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:87 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/19 09:53:00.483 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[86]"]
   > [2024/06/19 09:53:00.483 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255975] [schemaVersion=78] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_dnmxh` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:53:00.485 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255975] [schemaVersion=78] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_dnmxh` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:53:01.500 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/06/19 09:53:01.512 +00:00] [INFO] [set.go:149] ["set global var"] [conn=2199023255977] [name=tx_isolation] [val=REPEATABLE-READ]

### Scenario 4
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  START TRANSACTION;
     - TID: 0
     - Output: None
 * Instruction #2:
     - SQL:  WITH cte_0 AS (select distinct ref_0.wkey as c0, ref_0.pkey as c1, ref_0.c_xhsn...
     - TID: 0
     - Output: [(104, 575000, 9.53), (104, 572000, 44.37), (106, 585000, None)]
 * Instruction #3:
     - SQL:  COMMIT;
     - TID: 0
     - Output: None

 * Container logs:
   > [2024/06/19 09:53:04.488 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/06/19 09:53:04.492 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255981] [schemaVersion=86] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/06/19 09:53:04.494 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:119, Type:drop schema, State:queueing, SchemaState:public, SchemaID:114, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:53:04.492 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/06/19 09:53:04.494 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:119, Type:drop schema, State:queueing, SchemaState:public, SchemaID:114, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:53:04.492 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/06/19 09:53:04.501 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:119, Type:drop schema, State:queueing, SchemaState:public, SchemaID:114, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:53:04.492 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:53:04.504 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=86] [neededSchemaVersion=87] ["start time"=76.407µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 09:53:04.507 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=87] ["take time"=2.883705ms] [job="ID:119, Type:drop schema, State:running, SchemaState:write only, SchemaID:114, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:53:04.492 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:53:04.513 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:119, Type:drop schema, State:running, SchemaState:write only, SchemaID:114, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:53:04.492 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:53:04.516 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=87] [neededSchemaVersion=88] ["start time"=95.893µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 09:53:04.518 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=88] ["take time"=2.644286ms] [job="ID:119, Type:drop schema, State:running, SchemaState:delete only, SchemaID:114, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:53:04.492 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:53:04.521 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:119, Type:drop schema, State:running, SchemaState:delete only, SchemaID:114, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:53:04.492 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:53:04.525 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=88] [neededSchemaVersion=89] ["start time"=88.908µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 09:53:04.527 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=89] ["take time"=2.806599ms] [job="ID:119, Type:drop schema, State:done, SchemaState:none, SchemaID:114, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:53:04.492 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:53:04.531 +00:00] [INFO] [delete_range.go:109] ["[ddl] add job into delete-range table"] [jobID=119] [jobType="drop schema"]
   > [2024/06/19 09:53:04.532 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:119, Type:drop schema, State:synced, SchemaState:none, SchemaID:114, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:53:04.492 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:53:04.534 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=119]
   > [2024/06/19 09:53:04.534 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/06/19 09:53:04.536 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255981] [schemaVersion=89] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/06/19 09:53:04.538 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:121, Type:create schema, State:queueing, SchemaState:none, SchemaID:120, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 09:53:04.537 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/06/19 09:53:04.539 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:121, Type:create schema, State:queueing, SchemaState:none, SchemaID:120, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 09:53:04.537 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/19 09:53:04.546 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:121, Type:create schema, State:queueing, SchemaState:none, SchemaID:120, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:53:04.537 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:53:04.549 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=89] [neededSchemaVersion=90] ["start time"=153.303µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 09:53:04.551 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=90] ["take time"=2.281737ms] [job="ID:121, Type:create schema, State:done, SchemaState:public, SchemaID:120, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 09:53:04.537 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:53:04.555 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:121, Type:create schema, State:synced, SchemaState:public, SchemaID:120, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:53:04.537 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:53:04.557 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=121]
   > [2024/06/19 09:53:04.557 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/06/19 09:53:04.563 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255981] [schemaVersion=90] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_cqmg3b`\n--\n\nDROP TABLE IF EXISTS `t_cqmg3b`;"] [user=root@%]
   > [2024/06/19 09:53:04.564 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255981] [schemaVersion=90] [cur_db=testdb] [sql="CREATE TABLE `t_cqmg3b` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_anpf_c` int(11) DEFAULT NULL,\n  `c_b_fp_c` text DEFAULT NULL,\n  `c_ndccfb` int(11) DEFAULT NULL,\n  `c_8rswc` int(11) DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/06/19 09:53:04.567 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:123, Type:create table, State:queueing, SchemaState:none, SchemaID:120, TableID:122, RowCount:0, ArgLen:1, start time: 2024-06-19 09:53:04.565 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/06/19 09:53:04.567 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:123, Type:create table, State:queueing, SchemaState:none, SchemaID:120, TableID:122, RowCount:0, ArgLen:1, start time: 2024-06-19 09:53:04.565 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_cqmg3b` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_anpf_c` int(11) DEFAULT NULL,\n  `c_b_fp_c` text DEFAULT NULL,\n  `c_ndccfb` int(11) DEFAULT NULL,\n  `c_8rswc` int(11) DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/19 09:53:04.574 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:123, Type:create table, State:queueing, SchemaState:none, SchemaID:120, TableID:122, RowCount:0, ArgLen:0, start time: 2024-06-19 09:53:04.565 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:53:04.578 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=90] [neededSchemaVersion=91] ["start time"=468.849µs] [phyTblIDs="[122]"] [actionTypes="[8]"]
   > [2024/06/19 09:53:04.580 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=91] ["take time"=2.143939ms] [job="ID:123, Type:create table, State:done, SchemaState:public, SchemaID:120, TableID:122, RowCount:0, ArgLen:1, start time: 2024-06-19 09:53:04.565 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:53:04.584 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:123, Type:create table, State:synced, SchemaState:public, SchemaID:120, TableID:122, RowCount:0, ArgLen:0, start time: 2024-06-19 09:53:04.565 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:53:04.587 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=123]
   > [2024/06/19 09:53:04.587 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/06/19 09:53:04.587 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=90] ["first split key"=74800000000000007a]
   > [2024/06/19 09:53:04.588 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=90] ["first at"=74800000000000007a] ["first new region left"="{Id:90 StartKey:7480000000000000ff7400000000000000f8 EndKey:7480000000000000ff7a00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:91 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/19 09:53:04.588 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[90]"]
   > [2024/06/19 09:53:04.588 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255981] [schemaVersion=91] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_cqmg3b` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:53:04.592 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255981] [schemaVersion=91] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_cqmg3b` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:53:04.593 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255981] [schemaVersion=91] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_dnmxh`\n--\n\nDROP TABLE IF EXISTS `t_dnmxh`;"] [user=root@%]
   > [2024/06/19 09:53:04.594 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255981] [schemaVersion=91] [cur_db=testdb] [sql="CREATE TABLE `t_dnmxh` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_xhsndb` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/06/19 09:53:04.597 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:125, Type:create table, State:queueing, SchemaState:none, SchemaID:120, TableID:124, RowCount:0, ArgLen:1, start time: 2024-06-19 09:53:04.595 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/06/19 09:53:04.597 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:125, Type:create table, State:queueing, SchemaState:none, SchemaID:120, TableID:124, RowCount:0, ArgLen:1, start time: 2024-06-19 09:53:04.595 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_dnmxh` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_xhsndb` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/19 09:53:04.604 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:125, Type:create table, State:queueing, SchemaState:none, SchemaID:120, TableID:124, RowCount:0, ArgLen:0, start time: 2024-06-19 09:53:04.595 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:53:04.609 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=91] [neededSchemaVersion=92] ["start time"=590.583µs] [phyTblIDs="[124]"] [actionTypes="[8]"]
   > [2024/06/19 09:53:04.610 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=92] ["take time"=2.058243ms] [job="ID:125, Type:create table, State:done, SchemaState:public, SchemaID:120, TableID:124, RowCount:0, ArgLen:1, start time: 2024-06-19 09:53:04.595 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:53:04.615 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:125, Type:create table, State:synced, SchemaState:public, SchemaID:120, TableID:124, RowCount:0, ArgLen:0, start time: 2024-06-19 09:53:04.595 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:53:04.618 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=125]
   > [2024/06/19 09:53:04.618 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/06/19 09:53:04.618 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=92] ["first split key"=74800000000000007c]
   > [2024/06/19 09:53:04.619 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=92] ["first at"=74800000000000007c] ["first new region left"="{Id:92 StartKey:7480000000000000ff7a00000000000000f8 EndKey:7480000000000000ff7c00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:93 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/19 09:53:04.619 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[92]"]
   > [2024/06/19 09:53:04.619 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255981] [schemaVersion=92] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_dnmxh` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:53:04.621 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255981] [schemaVersion=92] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_dnmxh` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:53:05.635 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/06/19 09:53:05.652 +00:00] [INFO] [set.go:149] ["set global var"] [conn=2199023255983] [name=tx_isolation] [val=REPEATABLE-READ]
