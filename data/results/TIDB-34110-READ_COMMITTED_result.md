# Bug ID TIDB-34110-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/34110
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              Looses connection to the server.


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
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
     - Transaction: conn_1
     - Output: None
     - Executed order: 1
 * Instruction #2:
     - Instruction:  BEGIN OPTIMISTIC;
     - Transaction: conn_1
     - Output: None
     - Executed order: 2
 * Instruction #3:
     - Instruction:  BEGIN OPTIMISTIC;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
 * Instruction #4:
     - Instruction:  insert into t_zcfqb (wkey, pkey, c_dl_pmd, c_avevqc, c_sqqbbd, c_2wz8nc, c_qyxu...
     - Transaction: conn_1
     - Output: None
     - Executed order: 4
 * Instruction #5:
     - Instruction:  insert into t_zcfqb (wkey, c_rvm_p, c_avevqc, c_ywxlqb, c_sqqbbd, c_2wz8nc, c_q...
     - Transaction: conn_0
     - Output: None
     - Executed order: 5
 * Instruction #6:
     - Instruction:  select pkey from t_zcfqb where wkey = 121;
     - Transaction: conn_0
     - Output: [(264001,), (264002,), (264003,), (264004,), (264005,), (264006,), (264007,), (264008,), (264009,), (264010,), (264011,), (264012,), (264013,), (264014,), (264015,), (264016,), (264017,), (264018,), (264019,), (264020,), (264021,), (264022,), (264023,), (264024,), (264025,), (264026,), (264027,), (264028,), (264029,), (264030,), (264031,), (264032,), (264033,), (264034,), (264035,), (264036,), (264037,), (264038,), (264039,), (264040,), (264041,), (264042,), (264043,), (264044,), (264045,), (264046,), (264047,), (264048,), (264049,)]
     - Executed order: 6
 * Instruction #7:
     - Instruction:  ROLLBACK;
     - Transaction: conn_1
     - Output: None
     - Executed order: 7
 * Instruction #8:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 8

 * Container logs:
   > [2024/07/01 15:15:25.513 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/07/01 15:15:25.515 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=455] [schemaVersion=145] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/01 15:15:25.516 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:176, Type:drop schema, State:none, SchemaState:queueing, SchemaID:171, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:25.515 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:15:25.516 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:176, Type:drop schema, State:none, SchemaState:queueing, SchemaID:171, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:25.515 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/01 15:15:25.516 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:176, Type:drop schema, State:none, SchemaState:queueing, SchemaID:171, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:25.515 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:25.517 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=145] [neededSchemaVersion=146] ["start time"=47.283µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:15:25.519 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=146] ["take time"=2.064806ms] [job="ID:176, Type:drop schema, State:running, SchemaState:write only, SchemaID:171, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:25.515 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:25.519 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:176, Type:drop schema, State:running, SchemaState:write only, SchemaID:171, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:25.515 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:25.520 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=146] [neededSchemaVersion=147] ["start time"=48.051µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:15:25.522 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=147] ["take time"=2.651618ms] [job="ID:176, Type:drop schema, State:running, SchemaState:delete only, SchemaID:171, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:25.515 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:25.523 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:176, Type:drop schema, State:running, SchemaState:delete only, SchemaID:171, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:25.515 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:25.523 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=147] [neededSchemaVersion=148] ["start time"=68.096µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:15:25.526 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=148] ["take time"=2.414085ms] [job="ID:176, Type:drop schema, State:done, SchemaState:queueing, SchemaID:171, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:25.515 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:25.526 +00:00] [INFO] [delete_range.go:103] ["[ddl] add job into delete-range table"] [jobID=176] [jobType="drop schema"]
   > [2024/07/01 15:15:25.526 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:176, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:171, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:25.515 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:25.527 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=176]
   > [2024/07/01 15:15:25.527 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:15:25.528 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=455] [schemaVersion=148] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/01 15:15:25.529 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:178, Type:create schema, State:none, SchemaState:queueing, SchemaID:177, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:15:25.529 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:15:25.529 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:178, Type:create schema, State:none, SchemaState:queueing, SchemaID:177, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:15:25.529 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/01 15:15:25.529 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:178, Type:create schema, State:none, SchemaState:queueing, SchemaID:177, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:25.529 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:25.530 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=148] [neededSchemaVersion=149] ["start time"=102.878µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:15:25.532 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=149] ["take time"=2.236478ms] [job="ID:178, Type:create schema, State:done, SchemaState:public, SchemaID:177, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:15:25.529 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:25.533 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:178, Type:create schema, State:synced, SchemaState:public, SchemaID:177, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:25.529 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:25.533 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=178]
   > [2024/07/01 15:15:25.533 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:15:25.742 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=455] [schemaVersion=149] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_nvues`\n--\n\nDROP TABLE IF EXISTS `t_nvues`;"] [user=root@%]
   > [2024/07/01 15:15:25.742 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=455] [schemaVersion=149] [cur_db=testdb] [sql="CREATE TABLE `t_nvues` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL AUTO_INCREMENT,\n  `c_709vdd` double DEFAULT NULL,\n  `c_gsbzrd` text DEFAULT NULL,\n  `c_bsydab` int(11) DEFAULT NULL,\n  `c_vm9_pb` int(11) DEFAULT NULL,\n  `c_hdnifc` double DEFAULT NULL,\n  `c_dzs4sc` double DEFAULT NULL,\n  `c_h1m_zb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=110001;"] [user=root@%]
   > [2024/07/01 15:15:25.744 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:180, Type:create table, State:none, SchemaState:queueing, SchemaID:177, TableID:179, RowCount:0, ArgLen:1, start time: 2024-07-01 15:15:25.743 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:15:25.744 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:180, Type:create table, State:none, SchemaState:queueing, SchemaID:177, TableID:179, RowCount:0, ArgLen:1, start time: 2024-07-01 15:15:25.743 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_nvues` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL AUTO_INCREMENT,\n  `c_709vdd` double DEFAULT NULL,\n  `c_gsbzrd` text DEFAULT NULL,\n  `c_bsydab` int(11) DEFAULT NULL,\n  `c_vm9_pb` int(11) DEFAULT NULL,\n  `c_hdnifc` double DEFAULT NULL,\n  `c_dzs4sc` double DEFAULT NULL,\n  `c_h1m_zb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=110001;"]
   > [2024/07/01 15:15:25.744 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:180, Type:create table, State:none, SchemaState:queueing, SchemaID:177, TableID:179, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:25.743 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:25.747 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=149] [neededSchemaVersion=150] ["start time"=505.306µs] [phyTblIDs="[179]"] [actionTypes="[8]"]
   > [2024/07/01 15:15:25.748 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=150] ["take time"=2.086318ms] [job="ID:180, Type:create table, State:done, SchemaState:public, SchemaID:177, TableID:179, RowCount:0, ArgLen:1, start time: 2024-07-01 15:15:25.743 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:25.749 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:180, Type:create table, State:synced, SchemaState:public, SchemaID:177, TableID:179, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:25.743 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:25.751 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=180]
   > [2024/07/01 15:15:25.751 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=118] ["first split key"=7480000000000000b3]
   > [2024/07/01 15:15:25.751 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=118] ["first at"=7480000000000000b3] ["first new region left"="{Id:118 StartKey:7480000000000000ffad00000000000000f8 EndKey:7480000000000000ffb300000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:119 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/01 15:15:25.751 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[118]"]
   > [2024/07/01 15:15:25.751 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:15:25.752 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=455] [schemaVersion=150] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_nvues` DISABLE KEYS */;"] [user=root@%]
   > [2024/07/01 15:15:25.754 +00:00] [WARN] [2pc.go:1800] ["schemaLeaseChecker is not set for this transaction"] [sessionID=455] [startTS=450847552504856576] [checkTS=450847552504856577]
   > [2024/07/01 15:15:25.764 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=455] [schemaVersion=150] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_nvues` ENABLE KEYS */;"] [user=root@%]
   > [2024/07/01 15:15:25.764 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=455] [schemaVersion=150] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_zcfqb`\n--\n\nDROP TABLE IF EXISTS `t_zcfqb`;"] [user=root@%]
   > [2024/07/01 15:15:25.765 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=455] [schemaVersion=150] [cur_db=testdb] [sql="CREATE TABLE `t_zcfqb` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL AUTO_INCREMENT,\n  `c_rvm_p` text DEFAULT NULL,\n  `c_dl_pmd` int(11) DEFAULT NULL,\n  `c_avevqc` text DEFAULT NULL,\n  `c_ywxlqb` double DEFAULT NULL,\n  `c_sqqbbd` int(11) DEFAULT NULL,\n  `c_2wz8nc` text DEFAULT NULL,\n  `c_qyxu0` double DEFAULT NULL,\n  `c_slu2bd` int(11) DEFAULT NULL,\n  `c_ph8nh` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=77001;"] [user=root@%]
   > [2024/07/01 15:15:25.766 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:182, Type:create table, State:none, SchemaState:queueing, SchemaID:177, TableID:181, RowCount:0, ArgLen:1, start time: 2024-07-01 15:15:25.765 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:15:25.766 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:182, Type:create table, State:none, SchemaState:queueing, SchemaID:177, TableID:181, RowCount:0, ArgLen:1, start time: 2024-07-01 15:15:25.765 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_zcfqb` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL AUTO_INCREMENT,\n  `c_rvm_p` text DEFAULT NULL,\n  `c_dl_pmd` int(11) DEFAULT NULL,\n  `c_avevqc` text DEFAULT NULL,\n  `c_ywxlqb` double DEFAULT NULL,\n  `c_sqqbbd` int(11) DEFAULT NULL,\n  `c_2wz8nc` text DEFAULT NULL,\n  `c_qyxu0` double DEFAULT NULL,\n  `c_slu2bd` int(11) DEFAULT NULL,\n  `c_ph8nh` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=77001;"]
   > [2024/07/01 15:15:25.766 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:182, Type:create table, State:none, SchemaState:queueing, SchemaID:177, TableID:181, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:25.765 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:25.768 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=150] [neededSchemaVersion=151] ["start time"=726.426µs] [phyTblIDs="[181]"] [actionTypes="[8]"]
   > [2024/07/01 15:15:25.770 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=151] ["take time"=2.620398ms] [job="ID:182, Type:create table, State:done, SchemaState:public, SchemaID:177, TableID:181, RowCount:0, ArgLen:1, start time: 2024-07-01 15:15:25.765 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:25.772 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:182, Type:create table, State:synced, SchemaState:public, SchemaID:177, TableID:181, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:25.765 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:25.772 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=182]
   > [2024/07/01 15:15:25.773 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=120] ["first split key"=7480000000000000b5]
   > [2024/07/01 15:15:25.773 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:15:25.773 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=120] ["first at"=7480000000000000b5] ["first new region left"="{Id:120 StartKey:7480000000000000ffb300000000000000f8 EndKey:7480000000000000ffb500000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:121 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/01 15:15:25.773 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[120]"]
   > [2024/07/01 15:15:25.773 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=455] [schemaVersion=151] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_zcfqb` DISABLE KEYS */;"] [user=root@%]
   > [2024/07/01 15:15:25.774 +00:00] [WARN] [2pc.go:1800] ["schemaLeaseChecker is not set for this transaction"] [sessionID=455] [startTS=450847552510099456] [checkTS=450847552510099458]
   > [2024/07/01 15:15:25.775 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=455] [schemaVersion=151] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_zcfqb` ENABLE KEYS */;"] [user=root@%]
   > [2024/07/01 15:15:26.797 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/07/01 15:15:26.807 +00:00] [INFO] [set.go:147] ["set global var"] [conn=457] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/07/01 15:15:27.101 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/07/01 15:15:27.109 +00:00] [INFO] [set.go:147] ["set global var"] [conn=459] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/07/01 15:15:28.002 +00:00] [WARN] [2pc.go:1800] ["schemaLeaseChecker is not set for this transaction"] [sessionID=459] [startTS=450847553093894144] [checkTS=450847553094156288]

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
     - Instruction:  insert into t_zcfqb (wkey, c_rvm_p, c_avevqc, c_ywxlqb, c_sqqbbd, c_2wz8nc, c_q...
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
 * Instruction #3:
     - Instruction:  select pkey from t_zcfqb where wkey = 121;
     - Transaction: conn_0
     - Output: [(77001,), (77002,), (77003,), (77004,), (77005,), (77006,), (77007,), (77008,), (77009,), (77010,), (77011,), (77012,), (77013,), (77014,), (77015,), (77016,), (77017,), (77018,), (77019,), (77020,), (77021,), (77022,), (77023,), (77024,), (77025,), (77026,), (77027,), (77028,), (77029,), (77030,), (77031,), (77032,), (77033,), (77034,), (77035,), (77036,), (77037,), (77038,), (77039,), (77040,), (77041,), (77042,), (77043,), (77044,), (77045,), (77046,), (77047,), (77048,), (77049,)]
     - Executed order: 3
 * Instruction #4:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4

 * Container logs:
   > [2024/07/01 15:15:31.304 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/07/01 15:15:31.307 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=463] [schemaVersion=159] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/01 15:15:31.308 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:189, Type:drop schema, State:none, SchemaState:queueing, SchemaID:184, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:31.307 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:15:31.308 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:189, Type:drop schema, State:none, SchemaState:queueing, SchemaID:184, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:31.307 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/01 15:15:31.308 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:189, Type:drop schema, State:none, SchemaState:queueing, SchemaID:184, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:31.307 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:31.309 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=159] [neededSchemaVersion=160] ["start time"=69.074µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:15:31.311 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=160] ["take time"=2.024018ms] [job="ID:189, Type:drop schema, State:running, SchemaState:write only, SchemaID:184, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:31.307 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:31.311 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:189, Type:drop schema, State:running, SchemaState:write only, SchemaID:184, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:31.307 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:31.312 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=160] [neededSchemaVersion=161] ["start time"=88.21µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:15:31.314 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=161] ["take time"=2.051886ms] [job="ID:189, Type:drop schema, State:running, SchemaState:delete only, SchemaID:184, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:31.307 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:31.314 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:189, Type:drop schema, State:running, SchemaState:delete only, SchemaID:184, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:31.307 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:31.315 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=161] [neededSchemaVersion=162] ["start time"=70.401µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:15:31.318 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=162] ["take time"=2.611459ms] [job="ID:189, Type:drop schema, State:done, SchemaState:queueing, SchemaID:184, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:31.307 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:31.318 +00:00] [INFO] [delete_range.go:103] ["[ddl] add job into delete-range table"] [jobID=189] [jobType="drop schema"]
   > [2024/07/01 15:15:31.318 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:189, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:184, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:31.307 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:31.320 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=189]
   > [2024/07/01 15:15:31.320 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:15:31.321 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=463] [schemaVersion=162] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/01 15:15:31.322 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:191, Type:create schema, State:none, SchemaState:queueing, SchemaID:190, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:15:31.322 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:15:31.322 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:191, Type:create schema, State:none, SchemaState:queueing, SchemaID:190, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:15:31.322 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/01 15:15:31.323 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:191, Type:create schema, State:none, SchemaState:queueing, SchemaID:190, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:31.322 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:31.324 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=162] [neededSchemaVersion=163] ["start time"=137.588µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:15:31.326 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=163] ["take time"=2.254496ms] [job="ID:191, Type:create schema, State:done, SchemaState:public, SchemaID:190, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:15:31.322 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:31.326 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:191, Type:create schema, State:synced, SchemaState:public, SchemaID:190, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:31.322 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:31.327 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=191]
   > [2024/07/01 15:15:31.327 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:15:31.543 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=463] [schemaVersion=163] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_nvues`\n--\n\nDROP TABLE IF EXISTS `t_nvues`;"] [user=root@%]
   > [2024/07/01 15:15:31.544 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=463] [schemaVersion=163] [cur_db=testdb] [sql="CREATE TABLE `t_nvues` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL AUTO_INCREMENT,\n  `c_709vdd` double DEFAULT NULL,\n  `c_gsbzrd` text DEFAULT NULL,\n  `c_bsydab` int(11) DEFAULT NULL,\n  `c_vm9_pb` int(11) DEFAULT NULL,\n  `c_hdnifc` double DEFAULT NULL,\n  `c_dzs4sc` double DEFAULT NULL,\n  `c_h1m_zb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=110001;"] [user=root@%]
   > [2024/07/01 15:15:31.545 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:193, Type:create table, State:none, SchemaState:queueing, SchemaID:190, TableID:192, RowCount:0, ArgLen:1, start time: 2024-07-01 15:15:31.544 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:15:31.545 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:193, Type:create table, State:none, SchemaState:queueing, SchemaID:190, TableID:192, RowCount:0, ArgLen:1, start time: 2024-07-01 15:15:31.544 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_nvues` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL AUTO_INCREMENT,\n  `c_709vdd` double DEFAULT NULL,\n  `c_gsbzrd` text DEFAULT NULL,\n  `c_bsydab` int(11) DEFAULT NULL,\n  `c_vm9_pb` int(11) DEFAULT NULL,\n  `c_hdnifc` double DEFAULT NULL,\n  `c_dzs4sc` double DEFAULT NULL,\n  `c_h1m_zb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=110001;"]
   > [2024/07/01 15:15:31.545 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:193, Type:create table, State:none, SchemaState:queueing, SchemaID:190, TableID:192, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:31.544 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:31.547 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=163] [neededSchemaVersion=164] ["start time"=357.87µs] [phyTblIDs="[192]"] [actionTypes="[8]"]
   > [2024/07/01 15:15:31.548 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=164] ["take time"=2.054749ms] [job="ID:193, Type:create table, State:done, SchemaState:public, SchemaID:190, TableID:192, RowCount:0, ArgLen:1, start time: 2024-07-01 15:15:31.544 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:31.549 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:193, Type:create table, State:synced, SchemaState:public, SchemaID:190, TableID:192, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:31.544 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:31.550 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=193]
   > [2024/07/01 15:15:31.550 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=124] ["first split key"=7480000000000000c0]
   > [2024/07/01 15:15:31.563 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=124] ["first at"=7480000000000000c0] ["first new region left"="{Id:124 StartKey:7480000000000000ffba00000000000000f8 EndKey:7480000000000000ffc000000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:125 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/01 15:15:31.563 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[124]"]
   > [2024/07/01 15:15:31.563 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:15:31.564 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=463] [schemaVersion=164] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_nvues` DISABLE KEYS */;"] [user=root@%]
   > [2024/07/01 15:15:31.565 +00:00] [WARN] [2pc.go:1800] ["schemaLeaseChecker is not set for this transaction"] [sessionID=463] [startTS=450847554028175360] [checkTS=450847554028175361]
   > [2024/07/01 15:15:31.566 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=463] [schemaVersion=164] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_nvues` ENABLE KEYS */;"] [user=root@%]
   > [2024/07/01 15:15:31.567 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=463] [schemaVersion=164] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_zcfqb`\n--\n\nDROP TABLE IF EXISTS `t_zcfqb`;"] [user=root@%]
   > [2024/07/01 15:15:31.567 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=463] [schemaVersion=164] [cur_db=testdb] [sql="CREATE TABLE `t_zcfqb` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL AUTO_INCREMENT,\n  `c_rvm_p` text DEFAULT NULL,\n  `c_dl_pmd` int(11) DEFAULT NULL,\n  `c_avevqc` text DEFAULT NULL,\n  `c_ywxlqb` double DEFAULT NULL,\n  `c_sqqbbd` int(11) DEFAULT NULL,\n  `c_2wz8nc` text DEFAULT NULL,\n  `c_qyxu0` double DEFAULT NULL,\n  `c_slu2bd` int(11) DEFAULT NULL,\n  `c_ph8nh` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=77001;"] [user=root@%]
   > [2024/07/01 15:15:31.568 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:195, Type:create table, State:none, SchemaState:queueing, SchemaID:190, TableID:194, RowCount:0, ArgLen:1, start time: 2024-07-01 15:15:31.567 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:15:31.568 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:195, Type:create table, State:none, SchemaState:queueing, SchemaID:190, TableID:194, RowCount:0, ArgLen:1, start time: 2024-07-01 15:15:31.567 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_zcfqb` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL AUTO_INCREMENT,\n  `c_rvm_p` text DEFAULT NULL,\n  `c_dl_pmd` int(11) DEFAULT NULL,\n  `c_avevqc` text DEFAULT NULL,\n  `c_ywxlqb` double DEFAULT NULL,\n  `c_sqqbbd` int(11) DEFAULT NULL,\n  `c_2wz8nc` text DEFAULT NULL,\n  `c_qyxu0` double DEFAULT NULL,\n  `c_slu2bd` int(11) DEFAULT NULL,\n  `c_ph8nh` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=77001;"]
   > [2024/07/01 15:15:31.568 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:195, Type:create table, State:none, SchemaState:queueing, SchemaID:190, TableID:194, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:31.567 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:31.569 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=164] [neededSchemaVersion=165] ["start time"=255.272µs] [phyTblIDs="[194]"] [actionTypes="[8]"]
   > [2024/07/01 15:15:31.571 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=165] ["take time"=2.105384ms] [job="ID:195, Type:create table, State:done, SchemaState:public, SchemaID:190, TableID:194, RowCount:0, ArgLen:1, start time: 2024-07-01 15:15:31.567 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:31.572 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:195, Type:create table, State:synced, SchemaState:public, SchemaID:190, TableID:194, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:31.567 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:31.573 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=195]
   > [2024/07/01 15:15:31.573 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=126] ["first split key"=7480000000000000c2]
   > [2024/07/01 15:15:31.573 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=126] ["first at"=7480000000000000c2] ["first new region left"="{Id:126 StartKey:7480000000000000ffc000000000000000f8 EndKey:7480000000000000ffc200000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:127 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/01 15:15:31.573 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[126]"]
   > [2024/07/01 15:15:31.574 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:15:31.574 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=463] [schemaVersion=165] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_zcfqb` DISABLE KEYS */;"] [user=root@%]
   > [2024/07/01 15:15:31.575 +00:00] [WARN] [2pc.go:1800] ["schemaLeaseChecker is not set for this transaction"] [sessionID=463] [startTS=450847554030796800] [checkTS=450847554030796801]
   > [2024/07/01 15:15:31.576 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=463] [schemaVersion=165] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_zcfqb` ENABLE KEYS */;"] [user=root@%]
   > [2024/07/01 15:15:32.595 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/07/01 15:15:32.602 +00:00] [INFO] [set.go:147] ["set global var"] [conn=465] [name=tx_isolation] [val=READ-COMMITTED]
