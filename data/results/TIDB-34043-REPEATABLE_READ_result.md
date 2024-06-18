# Bug ID TIDB-34043-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/34043
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ


## Details
 * Database: tidb-v6.1.0
 * Number of scenarios: 1
 * Initial setup script: /home/theodor/Projects/MasterThesis/data/sql/TIDB-34043_mysql_bk.sql

## Results
### Scenario 0
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  start transaction;
     - TID: 0
     - Output: None
 * Instruction #2:
     - SQL:  select ref_0.c_lmpznc as c5 from t_zb_m5 as ref_0 where (ref_0.c_mu4_e in ( sel...
     - TID: 0
     - Output: ERROR: Timeout for this transaction.
 * Instruction #3:
     - SQL:  commit;
     - TID: 0
     - Output: ERROR: Timeout for this transaction.

 * Container logs:
   > [2024/06/18 16:22:14.471 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/06/18 16:22:14.474 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=32] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/06/18 16:22:14.475 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=32] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/06/18 16:22:14.476 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:66, Type:create schema, State:none, SchemaState:queueing, SchemaID:65, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 16:22:14.475 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 16:22:14.476 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:66, Type:create schema, State:none, SchemaState:queueing, SchemaID:65, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 16:22:14.475 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/18 16:22:14.476 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:create schema, State:none, SchemaState:queueing, SchemaID:65, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:22:14.475 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:22:14.476 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=32] [neededSchemaVersion=33] ["start time"=78.921µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 16:22:14.479 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=33] ["take time"=2.238926ms] [job="ID:66, Type:create schema, State:done, SchemaState:public, SchemaID:65, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 16:22:14.475 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:22:14.479 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:create schema, State:synced, SchemaState:public, SchemaID:65, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:22:14.475 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:22:14.480 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=66]
   > [2024/06/18 16:22:14.480 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 16:22:14.483 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=33] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_wzgyvd`\n--\n\nDROP TABLE IF EXISTS `t_wzgyvd`;"] [user=root@%]
   > [2024/06/18 16:22:14.484 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=33] [cur_db=testdb] [sql="CREATE TABLE `t_wzgyvd` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_oswlic` text DEFAULT NULL,\n  `c_c23g6c` int(11) DEFAULT NULL,\n  `c__gkztd` double DEFAULT NULL,\n  `c_pqvmnd` text DEFAULT NULL,\n  `c_dm4wqb` text DEFAULT NULL,\n  `c_hysvi` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  UNIQUE KEY `pkey_2` (`pkey`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/06/18 16:22:14.485 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:68, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:67, RowCount:0, ArgLen:1, start time: 2024-06-18 16:22:14.484 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 16:22:14.485 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:68, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:67, RowCount:0, ArgLen:1, start time: 2024-06-18 16:22:14.484 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_wzgyvd` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_oswlic` text DEFAULT NULL,\n  `c_c23g6c` int(11) DEFAULT NULL,\n  `c__gkztd` double DEFAULT NULL,\n  `c_pqvmnd` text DEFAULT NULL,\n  `c_dm4wqb` text DEFAULT NULL,\n  `c_hysvi` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  UNIQUE KEY `pkey_2` (`pkey`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/18 16:22:14.485 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:68, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:67, RowCount:0, ArgLen:0, start time: 2024-06-18 16:22:14.484 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:22:14.487 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=33] [neededSchemaVersion=34] ["start time"=375.122µs] [phyTblIDs="[67]"] [actionTypes="[8]"]
   > [2024/06/18 16:22:14.488 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=34] ["take time"=2.018155ms] [job="ID:68, Type:create table, State:done, SchemaState:public, SchemaID:65, TableID:67, RowCount:0, ArgLen:1, start time: 2024-06-18 16:22:14.484 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:22:14.489 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:68, Type:create table, State:synced, SchemaState:public, SchemaID:65, TableID:67, RowCount:0, ArgLen:0, start time: 2024-06-18 16:22:14.484 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:22:14.490 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=68]
   > [2024/06/18 16:22:14.490 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 16:22:14.490 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=60] ["first split key"=748000000000000043]
   > [2024/06/18 16:22:14.491 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=34] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_wzgyvd` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/18 16:22:14.492 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=34] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_wzgyvd` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/18 16:22:14.493 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=34] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_zb_m5`\n--\n\nDROP TABLE IF EXISTS `t_zb_m5`;"] [user=root@%]
   > [2024/06/18 16:22:14.493 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=62] ["first at"=748000000000000043] ["first new region left"="{Id:62 StartKey:7480000000000000ff3f00000000000000f8 EndKey:7480000000000000ff4300000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:63 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/18 16:22:14.493 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[62]"]
   > [2024/06/18 16:22:14.493 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=34] [cur_db=testdb] [sql="CREATE TABLE `t_zb_m5` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_4iptac` double DEFAULT NULL,\n  `c_kbcikb` double DEFAULT NULL,\n  `c_mu4_e` double DEFAULT NULL,\n  `c_lmpznc` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  UNIQUE KEY `pkey_2` (`pkey`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/06/18 16:22:14.494 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:70, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:69, RowCount:0, ArgLen:1, start time: 2024-06-18 16:22:14.494 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 16:22:14.494 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:70, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:69, RowCount:0, ArgLen:1, start time: 2024-06-18 16:22:14.494 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_zb_m5` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_4iptac` double DEFAULT NULL,\n  `c_kbcikb` double DEFAULT NULL,\n  `c_mu4_e` double DEFAULT NULL,\n  `c_lmpznc` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  UNIQUE KEY `pkey_2` (`pkey`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/18 16:22:14.495 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:70, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:69, RowCount:0, ArgLen:0, start time: 2024-06-18 16:22:14.494 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:22:14.496 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=34] [neededSchemaVersion=35] ["start time"=197.234µs] [phyTblIDs="[69]"] [actionTypes="[8]"]
   > [2024/06/18 16:22:14.498 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=35] ["take time"=2.179421ms] [job="ID:70, Type:create table, State:done, SchemaState:public, SchemaID:65, TableID:69, RowCount:0, ArgLen:1, start time: 2024-06-18 16:22:14.494 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:22:14.498 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:70, Type:create table, State:synced, SchemaState:public, SchemaID:65, TableID:69, RowCount:0, ArgLen:0, start time: 2024-06-18 16:22:14.494 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:22:14.499 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=70]
   > [2024/06/18 16:22:14.499 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 16:22:14.499 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=62] ["first split key"=748000000000000045]
   > [2024/06/18 16:22:14.499 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=35] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_zb_m5` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/18 16:22:14.501 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=35] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_zb_m5` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/18 16:22:14.502 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=64] ["first at"=748000000000000045] ["first new region left"="{Id:64 StartKey:7480000000000000ff4300000000000000f8 EndKey:7480000000000000ff4500000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:65 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/18 16:22:14.502 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[64]"]
   > [2024/06/18 16:22:15.543 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/06/18 16:22:15.552 +00:00] [INFO] [set.go:147] ["set global var"] [conn=407] [name=tx_isolation] [val=REPEATABLE-READ]
