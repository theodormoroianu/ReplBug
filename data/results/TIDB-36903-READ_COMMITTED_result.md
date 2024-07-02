# Bug ID TIDB-36903-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/36903
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              The two tests give a different result.


## Details
 * Database: tidb-v6.1.0
 * Number of scenarios: 2
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
 * Instruction #1:
     - Instruction:  insert into t_vwvgdc (wkey, pkey, c_rdsfbc) values (155, 228000, 99.50);
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
 * Instruction #2:
     - Instruction:  select ref_4.pkey as c0 from t_vwvgdc as ref_4 where 0 <> 0 union select ref_5....
     - Transaction: conn_0
     - Output: [(67000,), (16000,), (39000,), (21000,), (65000,), (62000,), (25000,), (37000,), (63000,), (26000,), (38000,), (68000,), (70000,), (228000,), (18000,), (71000,), (42000,), (17000,), (66000,), (15000,), (74000,), (19000,), (20000,), (73000,), (41000,), (69000,), (27000,), (40000,), (64000,), (72000,)]
     - Executed order: 2

 * Container logs:
   > [2024/07/01 15:16:28.611 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/07/01 15:16:28.613 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=423] [schemaVersion=71] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/01 15:16:28.614 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:103, Type:drop schema, State:none, SchemaState:queueing, SchemaID:98, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:28.613 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:16:28.614 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:103, Type:drop schema, State:none, SchemaState:queueing, SchemaID:98, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:28.613 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/01 15:16:28.614 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:103, Type:drop schema, State:none, SchemaState:queueing, SchemaID:98, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:28.613 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:28.615 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=71] [neededSchemaVersion=72] ["start time"=52.103µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:16:28.617 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=72] ["take time"=2.243043ms] [job="ID:103, Type:drop schema, State:running, SchemaState:write only, SchemaID:98, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:28.613 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:28.618 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:103, Type:drop schema, State:running, SchemaState:write only, SchemaID:98, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:28.613 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:28.618 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=72] [neededSchemaVersion=73] ["start time"=67.816µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:16:28.621 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=73] ["take time"=2.227049ms] [job="ID:103, Type:drop schema, State:running, SchemaState:delete only, SchemaID:98, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:28.613 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:28.621 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:103, Type:drop schema, State:running, SchemaState:delete only, SchemaID:98, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:28.613 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:28.622 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=73] [neededSchemaVersion=74] ["start time"=65.162µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:16:28.624 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=74] ["take time"=2.051885ms] [job="ID:103, Type:drop schema, State:done, SchemaState:queueing, SchemaID:98, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:28.613 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:28.624 +00:00] [INFO] [delete_range.go:103] ["[ddl] add job into delete-range table"] [jobID=103] [jobType="drop schema"]
   > [2024/07/01 15:16:28.624 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:103, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:98, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:28.613 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:28.625 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=103]
   > [2024/07/01 15:16:28.625 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:16:28.625 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=423] [schemaVersion=74] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/01 15:16:28.626 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:105, Type:create schema, State:none, SchemaState:queueing, SchemaID:104, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:16:28.626 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:16:28.626 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:105, Type:create schema, State:none, SchemaState:queueing, SchemaID:104, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:16:28.626 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/01 15:16:28.626 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:105, Type:create schema, State:none, SchemaState:queueing, SchemaID:104, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:28.626 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:28.627 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=74] [neededSchemaVersion=75] ["start time"=72.356µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:16:28.629 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=75] ["take time"=2.189893ms] [job="ID:105, Type:create schema, State:done, SchemaState:public, SchemaID:104, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:16:28.626 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:28.629 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:105, Type:create schema, State:synced, SchemaState:public, SchemaID:104, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:28.626 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:28.630 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=105]
   > [2024/07/01 15:16:28.630 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:16:28.633 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=423] [schemaVersion=75] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_5mspyb`\n--\n\nDROP TABLE IF EXISTS `t_5mspyb`;"] [user=root@%]
   > [2024/07/01 15:16:28.633 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=423] [schemaVersion=75] [cur_db=testdb] [sql="CREATE TABLE `t_5mspyb` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_dugmmc` int(11) DEFAULT NULL,\n  `c_q0rdv` text DEFAULT NULL,\n  `c_0bhxq` int(11) DEFAULT NULL,\n  `c_qpz_v` text DEFAULT NULL,\n  `c_rgl8pc` double DEFAULT NULL,\n  `c_yisj0d` int(11) DEFAULT NULL,\n  `c_n9hfnb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/07/01 15:16:28.634 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:107, Type:create table, State:none, SchemaState:queueing, SchemaID:104, TableID:106, RowCount:0, ArgLen:1, start time: 2024-07-01 15:16:28.634 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:16:28.634 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:107, Type:create table, State:none, SchemaState:queueing, SchemaID:104, TableID:106, RowCount:0, ArgLen:1, start time: 2024-07-01 15:16:28.634 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_5mspyb` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_dugmmc` int(11) DEFAULT NULL,\n  `c_q0rdv` text DEFAULT NULL,\n  `c_0bhxq` int(11) DEFAULT NULL,\n  `c_qpz_v` text DEFAULT NULL,\n  `c_rgl8pc` double DEFAULT NULL,\n  `c_yisj0d` int(11) DEFAULT NULL,\n  `c_n9hfnb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/01 15:16:28.635 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:107, Type:create table, State:none, SchemaState:queueing, SchemaID:104, TableID:106, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:28.634 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:28.637 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=75] [neededSchemaVersion=76] ["start time"=471.922µs] [phyTblIDs="[106]"] [actionTypes="[8]"]
   > [2024/07/01 15:16:28.639 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=76] ["take time"=2.02381ms] [job="ID:107, Type:create table, State:done, SchemaState:public, SchemaID:104, TableID:106, RowCount:0, ArgLen:1, start time: 2024-07-01 15:16:28.634 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:28.639 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:107, Type:create table, State:synced, SchemaState:public, SchemaID:104, TableID:106, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:28.634 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:28.640 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=107]
   > [2024/07/01 15:16:28.640 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:16:28.640 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=80] ["first split key"=74800000000000006a]
   > [2024/07/01 15:16:28.640 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=80] ["first at"=74800000000000006a] ["first new region left"="{Id:80 StartKey:7480000000000000ff6400000000000000f8 EndKey:7480000000000000ff6a00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:81 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/01 15:16:28.640 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[80]"]
   > [2024/07/01 15:16:28.641 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=423] [schemaVersion=76] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_5mspyb` DISABLE KEYS */;"] [user=root@%]
   > [2024/07/01 15:16:28.642 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=423] [schemaVersion=76] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_5mspyb` ENABLE KEYS */;"] [user=root@%]
   > [2024/07/01 15:16:28.643 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=423] [schemaVersion=76] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_vwvgdc`\n--\n\nDROP TABLE IF EXISTS `t_vwvgdc`;"] [user=root@%]
   > [2024/07/01 15:16:28.643 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=423] [schemaVersion=76] [cur_db=testdb] [sql="CREATE TABLE `t_vwvgdc` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_rdsfbc` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_8dsy1c` (`wkey`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/07/01 15:16:28.644 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:109, Type:create table, State:none, SchemaState:queueing, SchemaID:104, TableID:108, RowCount:0, ArgLen:1, start time: 2024-07-01 15:16:28.643 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:16:28.644 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:109, Type:create table, State:none, SchemaState:queueing, SchemaID:104, TableID:108, RowCount:0, ArgLen:1, start time: 2024-07-01 15:16:28.643 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_vwvgdc` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_rdsfbc` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_8dsy1c` (`wkey`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/01 15:16:28.644 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:109, Type:create table, State:none, SchemaState:queueing, SchemaID:104, TableID:108, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:28.643 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:28.645 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=76] [neededSchemaVersion=77] ["start time"=190.808µs] [phyTblIDs="[108]"] [actionTypes="[8]"]
   > [2024/07/01 15:16:28.647 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=77] ["take time"=2.178928ms] [job="ID:109, Type:create table, State:done, SchemaState:public, SchemaID:104, TableID:108, RowCount:0, ArgLen:1, start time: 2024-07-01 15:16:28.643 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:28.647 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:109, Type:create table, State:synced, SchemaState:public, SchemaID:104, TableID:108, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:28.643 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:28.648 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=109]
   > [2024/07/01 15:16:28.648 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:16:28.648 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=82] ["first split key"=74800000000000006c]
   > [2024/07/01 15:16:28.648 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=82] ["first at"=74800000000000006c] ["first new region left"="{Id:82 StartKey:7480000000000000ff6a00000000000000f8 EndKey:7480000000000000ff6c00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:83 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/01 15:16:28.648 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[82]"]
   > [2024/07/01 15:16:28.648 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=423] [schemaVersion=77] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_vwvgdc` DISABLE KEYS */;"] [user=root@%]
   > [2024/07/01 15:16:28.650 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=423] [schemaVersion=77] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_vwvgdc` ENABLE KEYS */;"] [user=root@%]
   > [2024/07/01 15:16:29.688 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/07/01 15:16:29.706 +00:00] [INFO] [set.go:147] ["set global var"] [conn=425] [name=tx_isolation] [val=READ-COMMITTED]

### Scenario 1
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
 * Instruction #1:
     - Instruction:  BEGIN OPTIMISTIC;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
 * Instruction #2:
     - Instruction:  insert into t_vwvgdc (wkey, pkey, c_rdsfbc) values (155, 228000, 99.50);
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
 * Instruction #3:
     - Instruction:  select ref_4.pkey as c0 from t_vwvgdc as ref_4 where 0 <> 0 union select ref_5....
     - Transaction: conn_0
     - Output: []
     - Executed order: 3
 * Instruction #4:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4

 * Container logs:
   > [2024/07/01 15:16:32.103 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/07/01 15:16:32.104 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=429] [schemaVersion=85] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/01 15:16:32.105 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:116, Type:drop schema, State:none, SchemaState:queueing, SchemaID:111, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:32.105 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:16:32.105 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:116, Type:drop schema, State:none, SchemaState:queueing, SchemaID:111, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:32.105 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/01 15:16:32.105 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:116, Type:drop schema, State:none, SchemaState:queueing, SchemaID:111, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:32.105 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:32.106 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=85] [neededSchemaVersion=86] ["start time"=45.816µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:16:32.108 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=86] ["take time"=2.2223ms] [job="ID:116, Type:drop schema, State:running, SchemaState:write only, SchemaID:111, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:32.105 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:32.108 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:116, Type:drop schema, State:running, SchemaState:write only, SchemaID:111, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:32.105 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:32.109 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=86] [neededSchemaVersion=87] ["start time"=95.125µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:16:32.111 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=87] ["take time"=2.195411ms] [job="ID:116, Type:drop schema, State:running, SchemaState:delete only, SchemaID:111, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:32.105 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:32.111 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:116, Type:drop schema, State:running, SchemaState:delete only, SchemaID:111, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:32.105 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:32.112 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=87] [neededSchemaVersion=88] ["start time"=56.083µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:16:32.114 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=88] ["take time"=2.190103ms] [job="ID:116, Type:drop schema, State:done, SchemaState:queueing, SchemaID:111, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:32.105 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:32.115 +00:00] [INFO] [delete_range.go:103] ["[ddl] add job into delete-range table"] [jobID=116] [jobType="drop schema"]
   > [2024/07/01 15:16:32.115 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:116, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:111, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:32.105 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:32.116 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=116]
   > [2024/07/01 15:16:32.116 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:16:32.117 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=429] [schemaVersion=88] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/01 15:16:32.117 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:118, Type:create schema, State:none, SchemaState:queueing, SchemaID:117, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:16:32.117 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:16:32.118 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:118, Type:create schema, State:none, SchemaState:queueing, SchemaID:117, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:16:32.117 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/01 15:16:32.118 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:118, Type:create schema, State:none, SchemaState:queueing, SchemaID:117, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:32.117 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:32.118 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=88] [neededSchemaVersion=89] ["start time"=81.646µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:16:32.120 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=89] ["take time"=2.209309ms] [job="ID:118, Type:create schema, State:done, SchemaState:public, SchemaID:117, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:16:32.117 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:32.121 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:118, Type:create schema, State:synced, SchemaState:public, SchemaID:117, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:32.117 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:32.122 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=118]
   > [2024/07/01 15:16:32.122 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:16:32.125 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=429] [schemaVersion=89] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_5mspyb`\n--\n\nDROP TABLE IF EXISTS `t_5mspyb`;"] [user=root@%]
   > [2024/07/01 15:16:32.125 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=429] [schemaVersion=89] [cur_db=testdb] [sql="CREATE TABLE `t_5mspyb` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_dugmmc` int(11) DEFAULT NULL,\n  `c_q0rdv` text DEFAULT NULL,\n  `c_0bhxq` int(11) DEFAULT NULL,\n  `c_qpz_v` text DEFAULT NULL,\n  `c_rgl8pc` double DEFAULT NULL,\n  `c_yisj0d` int(11) DEFAULT NULL,\n  `c_n9hfnb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/07/01 15:16:32.126 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:120, Type:create table, State:none, SchemaState:queueing, SchemaID:117, TableID:119, RowCount:0, ArgLen:1, start time: 2024-07-01 15:16:32.126 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:16:32.126 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:120, Type:create table, State:none, SchemaState:queueing, SchemaID:117, TableID:119, RowCount:0, ArgLen:1, start time: 2024-07-01 15:16:32.126 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_5mspyb` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_dugmmc` int(11) DEFAULT NULL,\n  `c_q0rdv` text DEFAULT NULL,\n  `c_0bhxq` int(11) DEFAULT NULL,\n  `c_qpz_v` text DEFAULT NULL,\n  `c_rgl8pc` double DEFAULT NULL,\n  `c_yisj0d` int(11) DEFAULT NULL,\n  `c_n9hfnb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/01 15:16:32.126 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:120, Type:create table, State:none, SchemaState:queueing, SchemaID:117, TableID:119, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:32.126 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:32.127 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=89] [neededSchemaVersion=90] ["start time"=225.66µs] [phyTblIDs="[119]"] [actionTypes="[8]"]
   > [2024/07/01 15:16:32.129 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=90] ["take time"=2.030095ms] [job="ID:120, Type:create table, State:done, SchemaState:public, SchemaID:117, TableID:119, RowCount:0, ArgLen:1, start time: 2024-07-01 15:16:32.126 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:32.130 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:120, Type:create table, State:synced, SchemaState:public, SchemaID:117, TableID:119, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:32.126 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:32.132 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=120]
   > [2024/07/01 15:16:32.132 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:16:32.132 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=86] ["first split key"=748000000000000077]
   > [2024/07/01 15:16:32.132 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=86] ["first at"=748000000000000077] ["first new region left"="{Id:86 StartKey:7480000000000000ff7100000000000000f8 EndKey:7480000000000000ff7700000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:87 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/01 15:16:32.132 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[86]"]
   > [2024/07/01 15:16:32.132 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=429] [schemaVersion=90] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_5mspyb` DISABLE KEYS */;"] [user=root@%]
   > [2024/07/01 15:16:32.136 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=429] [schemaVersion=90] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_5mspyb` ENABLE KEYS */;"] [user=root@%]
   > [2024/07/01 15:16:32.136 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=429] [schemaVersion=90] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_vwvgdc`\n--\n\nDROP TABLE IF EXISTS `t_vwvgdc`;"] [user=root@%]
   > [2024/07/01 15:16:32.136 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=429] [schemaVersion=90] [cur_db=testdb] [sql="CREATE TABLE `t_vwvgdc` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_rdsfbc` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_8dsy1c` (`wkey`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/07/01 15:16:32.137 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:122, Type:create table, State:none, SchemaState:queueing, SchemaID:117, TableID:121, RowCount:0, ArgLen:1, start time: 2024-07-01 15:16:32.137 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:16:32.137 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:122, Type:create table, State:none, SchemaState:queueing, SchemaID:117, TableID:121, RowCount:0, ArgLen:1, start time: 2024-07-01 15:16:32.137 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_vwvgdc` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_rdsfbc` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_8dsy1c` (`wkey`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/01 15:16:32.138 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:122, Type:create table, State:none, SchemaState:queueing, SchemaID:117, TableID:121, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:32.137 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:32.139 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=90] [neededSchemaVersion=91] ["start time"=255.692µs] [phyTblIDs="[121]"] [actionTypes="[8]"]
   > [2024/07/01 15:16:32.141 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=91] ["take time"=2.1959ms] [job="ID:122, Type:create table, State:done, SchemaState:public, SchemaID:117, TableID:121, RowCount:0, ArgLen:1, start time: 2024-07-01 15:16:32.137 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:32.142 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:122, Type:create table, State:synced, SchemaState:public, SchemaID:117, TableID:121, RowCount:0, ArgLen:0, start time: 2024-07-01 15:16:32.137 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:16:32.142 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=122]
   > [2024/07/01 15:16:32.142 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:16:32.143 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=88] ["first split key"=748000000000000079]
   > [2024/07/01 15:16:32.143 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=88] ["first at"=748000000000000079] ["first new region left"="{Id:88 StartKey:7480000000000000ff7700000000000000f8 EndKey:7480000000000000ff7900000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:89 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/01 15:16:32.143 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[88]"]
   > [2024/07/01 15:16:32.143 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=429] [schemaVersion=91] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_vwvgdc` DISABLE KEYS */;"] [user=root@%]
   > [2024/07/01 15:16:32.146 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=429] [schemaVersion=91] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_vwvgdc` ENABLE KEYS */;"] [user=root@%]
   > [2024/07/01 15:16:33.181 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/07/01 15:16:33.189 +00:00] [INFO] [set.go:147] ["set global var"] [conn=431] [name=tx_isolation] [val=READ-COMMITTED]
