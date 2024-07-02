# Bug ID TIDB-34110-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/34110
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              Looses connection to the server.


## Details
 * Database: tidb-v6.1.0
 * Number of scenarios: 2
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
 * Instruction #1:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
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
   > [2024/07/01 15:15:15.217 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/07/01 15:15:15.219 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=441] [schemaVersion=117] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/01 15:15:15.220 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:150, Type:drop schema, State:none, SchemaState:queueing, SchemaID:145, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:15.219 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:15:15.220 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:150, Type:drop schema, State:none, SchemaState:queueing, SchemaID:145, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:15.219 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/01 15:15:15.221 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:150, Type:drop schema, State:none, SchemaState:queueing, SchemaID:145, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:15.219 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:15.222 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=117] [neededSchemaVersion=118] ["start time"=93.099µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:15:15.224 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=118] ["take time"=2.083943ms] [job="ID:150, Type:drop schema, State:running, SchemaState:write only, SchemaID:145, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:15.219 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:15.224 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:150, Type:drop schema, State:running, SchemaState:write only, SchemaID:145, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:15.219 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:15.225 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=118] [neededSchemaVersion=119] ["start time"=50.845µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:15:15.227 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=119] ["take time"=2.201626ms] [job="ID:150, Type:drop schema, State:running, SchemaState:delete only, SchemaID:145, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:15.219 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:15.227 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:150, Type:drop schema, State:running, SchemaState:delete only, SchemaID:145, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:15.219 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:15.228 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=119] [neededSchemaVersion=120] ["start time"=71.448µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:15:15.230 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=120] ["take time"=2.12962ms] [job="ID:150, Type:drop schema, State:done, SchemaState:queueing, SchemaID:145, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:15.219 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:15.230 +00:00] [INFO] [delete_range.go:103] ["[ddl] add job into delete-range table"] [jobID=150] [jobType="drop schema"]
   > [2024/07/01 15:15:15.231 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:150, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:145, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:15.219 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:15.231 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=150]
   > [2024/07/01 15:15:15.231 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:15:15.232 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=441] [schemaVersion=120] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/01 15:15:15.233 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:152, Type:create schema, State:none, SchemaState:queueing, SchemaID:151, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:15:15.233 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:15:15.233 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:152, Type:create schema, State:none, SchemaState:queueing, SchemaID:151, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:15:15.233 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/01 15:15:15.233 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:152, Type:create schema, State:none, SchemaState:queueing, SchemaID:151, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:15.233 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:15.234 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=120] [neededSchemaVersion=121] ["start time"=87.233µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:15:15.236 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=121] ["take time"=2.223836ms] [job="ID:152, Type:create schema, State:done, SchemaState:public, SchemaID:151, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:15:15.233 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:15.236 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:152, Type:create schema, State:synced, SchemaState:public, SchemaID:151, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:15.233 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:15.237 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=152]
   > [2024/07/01 15:15:15.237 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:15:15.446 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=441] [schemaVersion=121] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_nvues`\n--\n\nDROP TABLE IF EXISTS `t_nvues`;"] [user=root@%]
   > [2024/07/01 15:15:15.446 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=441] [schemaVersion=121] [cur_db=testdb] [sql="CREATE TABLE `t_nvues` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL AUTO_INCREMENT,\n  `c_709vdd` double DEFAULT NULL,\n  `c_gsbzrd` text DEFAULT NULL,\n  `c_bsydab` int(11) DEFAULT NULL,\n  `c_vm9_pb` int(11) DEFAULT NULL,\n  `c_hdnifc` double DEFAULT NULL,\n  `c_dzs4sc` double DEFAULT NULL,\n  `c_h1m_zb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=110001;"] [user=root@%]
   > [2024/07/01 15:15:15.447 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:154, Type:create table, State:none, SchemaState:queueing, SchemaID:151, TableID:153, RowCount:0, ArgLen:1, start time: 2024-07-01 15:15:15.447 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:15:15.447 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:154, Type:create table, State:none, SchemaState:queueing, SchemaID:151, TableID:153, RowCount:0, ArgLen:1, start time: 2024-07-01 15:15:15.447 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_nvues` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL AUTO_INCREMENT,\n  `c_709vdd` double DEFAULT NULL,\n  `c_gsbzrd` text DEFAULT NULL,\n  `c_bsydab` int(11) DEFAULT NULL,\n  `c_vm9_pb` int(11) DEFAULT NULL,\n  `c_hdnifc` double DEFAULT NULL,\n  `c_dzs4sc` double DEFAULT NULL,\n  `c_h1m_zb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=110001;"]
   > [2024/07/01 15:15:15.448 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:154, Type:create table, State:none, SchemaState:queueing, SchemaID:151, TableID:153, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:15.447 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:15.449 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=121] [neededSchemaVersion=122] ["start time"=347.812µs] [phyTblIDs="[153]"] [actionTypes="[8]"]
   > [2024/07/01 15:15:15.451 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=122] ["take time"=2.047136ms] [job="ID:154, Type:create table, State:done, SchemaState:public, SchemaID:151, TableID:153, RowCount:0, ArgLen:1, start time: 2024-07-01 15:15:15.447 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:15.452 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:154, Type:create table, State:synced, SchemaState:public, SchemaID:151, TableID:153, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:15.447 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:15.453 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=154]
   > [2024/07/01 15:15:15.453 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=106] ["first split key"=748000000000000099]
   > [2024/07/01 15:15:15.454 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:15:15.454 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=106] ["first at"=748000000000000099] ["first new region left"="{Id:106 StartKey:7480000000000000ff9300000000000000f8 EndKey:7480000000000000ff9900000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:107 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/01 15:15:15.454 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[106]"]
   > [2024/07/01 15:15:15.454 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=441] [schemaVersion=122] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_nvues` DISABLE KEYS */;"] [user=root@%]
   > [2024/07/01 15:15:15.455 +00:00] [WARN] [2pc.go:1800] ["schemaLeaseChecker is not set for this transaction"] [sessionID=441] [startTS=450847549805035520] [checkTS=450847549805035521]
   > [2024/07/01 15:15:15.457 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=441] [schemaVersion=122] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_nvues` ENABLE KEYS */;"] [user=root@%]
   > [2024/07/01 15:15:15.457 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=441] [schemaVersion=122] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_zcfqb`\n--\n\nDROP TABLE IF EXISTS `t_zcfqb`;"] [user=root@%]
   > [2024/07/01 15:15:15.458 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=441] [schemaVersion=122] [cur_db=testdb] [sql="CREATE TABLE `t_zcfqb` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL AUTO_INCREMENT,\n  `c_rvm_p` text DEFAULT NULL,\n  `c_dl_pmd` int(11) DEFAULT NULL,\n  `c_avevqc` text DEFAULT NULL,\n  `c_ywxlqb` double DEFAULT NULL,\n  `c_sqqbbd` int(11) DEFAULT NULL,\n  `c_2wz8nc` text DEFAULT NULL,\n  `c_qyxu0` double DEFAULT NULL,\n  `c_slu2bd` int(11) DEFAULT NULL,\n  `c_ph8nh` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=77001;"] [user=root@%]
   > [2024/07/01 15:15:15.459 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:156, Type:create table, State:none, SchemaState:queueing, SchemaID:151, TableID:155, RowCount:0, ArgLen:1, start time: 2024-07-01 15:15:15.458 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:15:15.459 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:156, Type:create table, State:none, SchemaState:queueing, SchemaID:151, TableID:155, RowCount:0, ArgLen:1, start time: 2024-07-01 15:15:15.458 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_zcfqb` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL AUTO_INCREMENT,\n  `c_rvm_p` text DEFAULT NULL,\n  `c_dl_pmd` int(11) DEFAULT NULL,\n  `c_avevqc` text DEFAULT NULL,\n  `c_ywxlqb` double DEFAULT NULL,\n  `c_sqqbbd` int(11) DEFAULT NULL,\n  `c_2wz8nc` text DEFAULT NULL,\n  `c_qyxu0` double DEFAULT NULL,\n  `c_slu2bd` int(11) DEFAULT NULL,\n  `c_ph8nh` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=77001;"]
   > [2024/07/01 15:15:15.459 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:156, Type:create table, State:none, SchemaState:queueing, SchemaID:151, TableID:155, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:15.458 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:15.460 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=122] [neededSchemaVersion=123] ["start time"=253.387µs] [phyTblIDs="[155]"] [actionTypes="[8]"]
   > [2024/07/01 15:15:15.463 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=123] ["take time"=2.500201ms] [job="ID:156, Type:create table, State:done, SchemaState:public, SchemaID:151, TableID:155, RowCount:0, ArgLen:1, start time: 2024-07-01 15:15:15.458 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:15.463 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:156, Type:create table, State:synced, SchemaState:public, SchemaID:151, TableID:155, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:15.458 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:15.464 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=156]
   > [2024/07/01 15:15:15.464 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=108] ["first split key"=74800000000000009b]
   > [2024/07/01 15:15:15.464 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:15:15.464 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=108] ["first at"=74800000000000009b] ["first new region left"="{Id:108 StartKey:7480000000000000ff9900000000000000f8 EndKey:7480000000000000ff9b00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:109 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/01 15:15:15.464 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[108]"]
   > [2024/07/01 15:15:15.465 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=441] [schemaVersion=123] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_zcfqb` DISABLE KEYS */;"] [user=root@%]
   > [2024/07/01 15:15:15.466 +00:00] [WARN] [2pc.go:1800] ["schemaLeaseChecker is not set for this transaction"] [sessionID=441] [startTS=450847549807656962] [checkTS=450847549807919104]
   > [2024/07/01 15:15:15.467 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=441] [schemaVersion=123] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_zcfqb` ENABLE KEYS */;"] [user=root@%]
   > [2024/07/01 15:15:16.498 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/07/01 15:15:16.507 +00:00] [INFO] [set.go:147] ["set global var"] [conn=443] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/07/01 15:15:16.857 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/07/01 15:15:16.867 +00:00] [INFO] [set.go:147] ["set global var"] [conn=445] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/07/01 15:15:17.714 +00:00] [WARN] [2pc.go:1800] ["schemaLeaseChecker is not set for this transaction"] [sessionID=445] [startTS=450847550397218816] [checkTS=450847550397218817]

### Scenario 1
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
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
   > [2024/07/01 15:15:20.937 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/07/01 15:15:20.939 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=449] [schemaVersion=131] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/01 15:15:20.939 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:163, Type:drop schema, State:none, SchemaState:queueing, SchemaID:158, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:20.939 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:15:20.940 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:163, Type:drop schema, State:none, SchemaState:queueing, SchemaID:158, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:20.939 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/01 15:15:20.940 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:163, Type:drop schema, State:none, SchemaState:queueing, SchemaID:158, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:20.939 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:20.940 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=131] [neededSchemaVersion=132] ["start time"=51.963µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:15:20.942 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=132] ["take time"=2.017104ms] [job="ID:163, Type:drop schema, State:running, SchemaState:write only, SchemaID:158, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:20.939 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:20.942 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:163, Type:drop schema, State:running, SchemaState:write only, SchemaID:158, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:20.939 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:20.943 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=132] [neededSchemaVersion=133] ["start time"=44.28µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:15:20.946 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=133] ["take time"=2.870852ms] [job="ID:163, Type:drop schema, State:running, SchemaState:delete only, SchemaID:158, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:20.939 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:20.946 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:163, Type:drop schema, State:running, SchemaState:delete only, SchemaID:158, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:20.939 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:20.946 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=133] [neededSchemaVersion=134] ["start time"=79.549µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:15:20.949 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=134] ["take time"=2.592672ms] [job="ID:163, Type:drop schema, State:done, SchemaState:queueing, SchemaID:158, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:20.939 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:20.949 +00:00] [INFO] [delete_range.go:103] ["[ddl] add job into delete-range table"] [jobID=163] [jobType="drop schema"]
   > [2024/07/01 15:15:20.949 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:163, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:158, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:20.939 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:20.950 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=163]
   > [2024/07/01 15:15:20.950 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:15:20.951 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=449] [schemaVersion=134] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/01 15:15:20.952 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:165, Type:create schema, State:none, SchemaState:queueing, SchemaID:164, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:15:20.952 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:15:20.952 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:165, Type:create schema, State:none, SchemaState:queueing, SchemaID:164, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:15:20.952 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/01 15:15:20.953 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:165, Type:create schema, State:none, SchemaState:queueing, SchemaID:164, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:20.952 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:20.954 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=134] [neededSchemaVersion=135] ["start time"=85.975µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:15:20.956 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=135] ["take time"=2.08541ms] [job="ID:165, Type:create schema, State:done, SchemaState:public, SchemaID:164, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:15:20.952 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:20.956 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:165, Type:create schema, State:synced, SchemaState:public, SchemaID:164, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:20.952 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:20.956 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=165]
   > [2024/07/01 15:15:20.957 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:15:21.165 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=449] [schemaVersion=135] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_nvues`\n--\n\nDROP TABLE IF EXISTS `t_nvues`;"] [user=root@%]
   > [2024/07/01 15:15:21.165 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=449] [schemaVersion=135] [cur_db=testdb] [sql="CREATE TABLE `t_nvues` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL AUTO_INCREMENT,\n  `c_709vdd` double DEFAULT NULL,\n  `c_gsbzrd` text DEFAULT NULL,\n  `c_bsydab` int(11) DEFAULT NULL,\n  `c_vm9_pb` int(11) DEFAULT NULL,\n  `c_hdnifc` double DEFAULT NULL,\n  `c_dzs4sc` double DEFAULT NULL,\n  `c_h1m_zb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=110001;"] [user=root@%]
   > [2024/07/01 15:15:21.167 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:167, Type:create table, State:none, SchemaState:queueing, SchemaID:164, TableID:166, RowCount:0, ArgLen:1, start time: 2024-07-01 15:15:21.166 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:15:21.167 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:167, Type:create table, State:none, SchemaState:queueing, SchemaID:164, TableID:166, RowCount:0, ArgLen:1, start time: 2024-07-01 15:15:21.166 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_nvues` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL AUTO_INCREMENT,\n  `c_709vdd` double DEFAULT NULL,\n  `c_gsbzrd` text DEFAULT NULL,\n  `c_bsydab` int(11) DEFAULT NULL,\n  `c_vm9_pb` int(11) DEFAULT NULL,\n  `c_hdnifc` double DEFAULT NULL,\n  `c_dzs4sc` double DEFAULT NULL,\n  `c_h1m_zb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=110001;"]
   > [2024/07/01 15:15:21.167 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:167, Type:create table, State:none, SchemaState:queueing, SchemaID:164, TableID:166, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:21.166 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:21.169 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=135] [neededSchemaVersion=136] ["start time"=290.054µs] [phyTblIDs="[166]"] [actionTypes="[8]"]
   > [2024/07/01 15:15:21.170 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=136] ["take time"=2.190662ms] [job="ID:167, Type:create table, State:done, SchemaState:public, SchemaID:164, TableID:166, RowCount:0, ArgLen:1, start time: 2024-07-01 15:15:21.166 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:21.171 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:167, Type:create table, State:synced, SchemaState:public, SchemaID:164, TableID:166, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:21.166 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:21.172 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=167]
   > [2024/07/01 15:15:21.172 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=112] ["first split key"=7480000000000000a6]
   > [2024/07/01 15:15:21.172 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=112] ["first at"=7480000000000000a6] ["first new region left"="{Id:112 StartKey:7480000000000000ffa000000000000000f8 EndKey:7480000000000000ffa600000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:113 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/01 15:15:21.172 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[112]"]
   > [2024/07/01 15:15:21.172 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:15:21.173 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=449] [schemaVersion=136] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_nvues` DISABLE KEYS */;"] [user=root@%]
   > [2024/07/01 15:15:21.174 +00:00] [WARN] [2pc.go:1800] ["schemaLeaseChecker is not set for this transaction"] [sessionID=449] [startTS=450847551304237056] [checkTS=450847551304237057]
   > [2024/07/01 15:15:21.176 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=449] [schemaVersion=136] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_nvues` ENABLE KEYS */;"] [user=root@%]
   > [2024/07/01 15:15:21.176 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=449] [schemaVersion=136] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_zcfqb`\n--\n\nDROP TABLE IF EXISTS `t_zcfqb`;"] [user=root@%]
   > [2024/07/01 15:15:21.176 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=449] [schemaVersion=136] [cur_db=testdb] [sql="CREATE TABLE `t_zcfqb` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL AUTO_INCREMENT,\n  `c_rvm_p` text DEFAULT NULL,\n  `c_dl_pmd` int(11) DEFAULT NULL,\n  `c_avevqc` text DEFAULT NULL,\n  `c_ywxlqb` double DEFAULT NULL,\n  `c_sqqbbd` int(11) DEFAULT NULL,\n  `c_2wz8nc` text DEFAULT NULL,\n  `c_qyxu0` double DEFAULT NULL,\n  `c_slu2bd` int(11) DEFAULT NULL,\n  `c_ph8nh` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=77001;"] [user=root@%]
   > [2024/07/01 15:15:21.177 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:169, Type:create table, State:none, SchemaState:queueing, SchemaID:164, TableID:168, RowCount:0, ArgLen:1, start time: 2024-07-01 15:15:21.177 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:15:21.177 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:169, Type:create table, State:none, SchemaState:queueing, SchemaID:164, TableID:168, RowCount:0, ArgLen:1, start time: 2024-07-01 15:15:21.177 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_zcfqb` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL AUTO_INCREMENT,\n  `c_rvm_p` text DEFAULT NULL,\n  `c_dl_pmd` int(11) DEFAULT NULL,\n  `c_avevqc` text DEFAULT NULL,\n  `c_ywxlqb` double DEFAULT NULL,\n  `c_sqqbbd` int(11) DEFAULT NULL,\n  `c_2wz8nc` text DEFAULT NULL,\n  `c_qyxu0` double DEFAULT NULL,\n  `c_slu2bd` int(11) DEFAULT NULL,\n  `c_ph8nh` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=77001;"]
   > [2024/07/01 15:15:21.178 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:169, Type:create table, State:none, SchemaState:queueing, SchemaID:164, TableID:168, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:21.177 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:21.179 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=136] [neededSchemaVersion=137] ["start time"=314.148µs] [phyTblIDs="[168]"] [actionTypes="[8]"]
   > [2024/07/01 15:15:21.181 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=137] ["take time"=2.209589ms] [job="ID:169, Type:create table, State:done, SchemaState:public, SchemaID:164, TableID:168, RowCount:0, ArgLen:1, start time: 2024-07-01 15:15:21.177 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:21.182 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:169, Type:create table, State:synced, SchemaState:public, SchemaID:164, TableID:168, RowCount:0, ArgLen:0, start time: 2024-07-01 15:15:21.177 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:15:21.183 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=169]
   > [2024/07/01 15:15:21.183 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=114] ["first split key"=7480000000000000a8]
   > [2024/07/01 15:15:21.183 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=114] ["first at"=7480000000000000a8] ["first new region left"="{Id:114 StartKey:7480000000000000ffa600000000000000f8 EndKey:7480000000000000ffa800000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:115 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/01 15:15:21.183 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:15:21.183 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[114]"]
   > [2024/07/01 15:15:21.184 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=449] [schemaVersion=137] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_zcfqb` DISABLE KEYS */;"] [user=root@%]
   > [2024/07/01 15:15:21.185 +00:00] [WARN] [2pc.go:1800] ["schemaLeaseChecker is not set for this transaction"] [sessionID=449] [startTS=450847551306858498] [checkTS=450847551307120640]
   > [2024/07/01 15:15:21.186 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=449] [schemaVersion=137] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_zcfqb` ENABLE KEYS */;"] [user=root@%]
   > [2024/07/01 15:15:22.219 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/07/01 15:15:22.229 +00:00] [INFO] [set.go:147] ["set global var"] [conn=451] [name=tx_isolation] [val=REPEATABLE-READ]
