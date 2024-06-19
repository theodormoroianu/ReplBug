# Bug ID TIDB-34110-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/34110
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ


## Details
 * Database: tidb-v6.1.0
 * Number of scenarios: 2
 * Initial setup script: /home/theodor/Projects/MasterThesis/data/sql/TIDB-34110_mysql_bk.sql

## Results
### Scenario 0
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - TID: 1
     - Output: None
 * Instruction #2:
     - SQL:  BEGIN OPTIMISTIC;
     - TID: 1
     - Output: None
 * Instruction #3:
     - SQL:  BEGIN OPTIMISTIC;
     - TID: 0
     - Output: None
 * Instruction #4:
     - SQL:  insert into t_zcfqb (wkey, pkey, c_dl_pmd, c_avevqc, c_sqqbbd, c_2wz8nc, c_qyxu...
     - TID: 1
     - Output: None
 * Instruction #5:
     - SQL:  insert into t_zcfqb (wkey, c_rvm_p, c_avevqc, c_ywxlqb, c_sqqbbd, c_2wz8nc, c_q...
     - TID: 0
     - Output: None
 * Instruction #6:
     - SQL:  select pkey from t_zcfqb where wkey = 121;
     - TID: 0
     - Output: [(264001,), (264002,), (264003,), (264004,), (264005,), (264006,), (264007,), (264008,), (264009,), (264010,), (264011,), (264012,), (264013,), (264014,), (264015,), (264016,), (264017,), (264018,), (264019,), (264020,), (264021,), (264022,), (264023,), (264024,), (264025,), (264026,), (264027,), (264028,), (264029,), (264030,), (264031,), (264032,), (264033,), (264034,), (264035,), (264036,), (264037,), (264038,), (264039,), (264040,), (264041,), (264042,), (264043,), (264044,), (264045,), (264046,), (264047,), (264048,), (264049,)]
 * Instruction #7:
     - SQL:  ROLLBACK;
     - TID: 1
     - Output: None
 * Instruction #8:
     - SQL:  COMMIT;
     - TID: 0
     - Output: None

 * Container logs:
   > [2024/06/19 08:45:54.202 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/06/19 08:45:54.206 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=32] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/06/19 08:45:54.207 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=32] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/06/19 08:45:54.209 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:66, Type:create schema, State:none, SchemaState:queueing, SchemaID:65, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 08:45:54.208 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/19 08:45:54.209 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:66, Type:create schema, State:none, SchemaState:queueing, SchemaID:65, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 08:45:54.208 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/19 08:45:54.209 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:create schema, State:none, SchemaState:queueing, SchemaID:65, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:45:54.208 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:45:54.210 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=32] [neededSchemaVersion=33] ["start time"=100.153µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 08:45:54.212 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=33] ["take time"=2.399902ms] [job="ID:66, Type:create schema, State:done, SchemaState:public, SchemaID:65, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 08:45:54.208 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:45:54.212 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:create schema, State:synced, SchemaState:public, SchemaID:65, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:45:54.208 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:45:54.213 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=66]
   > [2024/06/19 08:45:54.213 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/19 08:45:54.227 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=33] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_nvues`\n--\n\nDROP TABLE IF EXISTS `t_nvues`;"] [user=root@%]
   > [2024/06/19 08:45:54.228 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=33] [cur_db=testdb] [sql="CREATE TABLE `t_nvues` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL AUTO_INCREMENT,\n  `c_709vdd` double DEFAULT NULL,\n  `c_gsbzrd` text DEFAULT NULL,\n  `c_bsydab` int(11) DEFAULT NULL,\n  `c_vm9_pb` int(11) DEFAULT NULL,\n  `c_hdnifc` double DEFAULT NULL,\n  `c_dzs4sc` double DEFAULT NULL,\n  `c_h1m_zb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=110001;"] [user=root@%]
   > [2024/06/19 08:45:54.229 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:68, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:67, RowCount:0, ArgLen:1, start time: 2024-06-19 08:45:54.229 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/19 08:45:54.229 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:68, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:67, RowCount:0, ArgLen:1, start time: 2024-06-19 08:45:54.229 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_nvues` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL AUTO_INCREMENT,\n  `c_709vdd` double DEFAULT NULL,\n  `c_gsbzrd` text DEFAULT NULL,\n  `c_bsydab` int(11) DEFAULT NULL,\n  `c_vm9_pb` int(11) DEFAULT NULL,\n  `c_hdnifc` double DEFAULT NULL,\n  `c_dzs4sc` double DEFAULT NULL,\n  `c_h1m_zb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=110001;"]
   > [2024/06/19 08:45:54.230 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:68, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:67, RowCount:0, ArgLen:0, start time: 2024-06-19 08:45:54.229 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:45:54.232 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=33] [neededSchemaVersion=34] ["start time"=369.114µs] [phyTblIDs="[67]"] [actionTypes="[8]"]
   > [2024/06/19 08:45:54.234 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=34] ["take time"=2.25058ms] [job="ID:68, Type:create table, State:done, SchemaState:public, SchemaID:65, TableID:67, RowCount:0, ArgLen:1, start time: 2024-06-19 08:45:54.229 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:45:54.235 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:68, Type:create table, State:synced, SchemaState:public, SchemaID:65, TableID:67, RowCount:0, ArgLen:0, start time: 2024-06-19 08:45:54.229 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:45:54.236 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=68]
   > [2024/06/19 08:45:54.236 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=60] ["first split key"=748000000000000043]
   > [2024/06/19 08:45:54.237 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/19 08:45:54.238 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=34] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_nvues` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/19 08:45:54.239 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=62] ["first at"=748000000000000043] ["first new region left"="{Id:62 StartKey:7480000000000000ff3f00000000000000f8 EndKey:7480000000000000ff4300000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:63 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/19 08:45:54.239 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[62]"]
   > [2024/06/19 08:45:54.240 +00:00] [WARN] [2pc.go:1800] ["schemaLeaseChecker is not set for this transaction"] [sessionID=405] [startTS=450569634903228416] [checkTS=450569634903490560]
   > [2024/06/19 08:45:54.242 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=34] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_nvues` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/19 08:45:54.243 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=34] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_zcfqb`\n--\n\nDROP TABLE IF EXISTS `t_zcfqb`;"] [user=root@%]
   > [2024/06/19 08:45:54.243 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=34] [cur_db=testdb] [sql="CREATE TABLE `t_zcfqb` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL AUTO_INCREMENT,\n  `c_rvm_p` text DEFAULT NULL,\n  `c_dl_pmd` int(11) DEFAULT NULL,\n  `c_avevqc` text DEFAULT NULL,\n  `c_ywxlqb` double DEFAULT NULL,\n  `c_sqqbbd` int(11) DEFAULT NULL,\n  `c_2wz8nc` text DEFAULT NULL,\n  `c_qyxu0` double DEFAULT NULL,\n  `c_slu2bd` int(11) DEFAULT NULL,\n  `c_ph8nh` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=77001;"] [user=root@%]
   > [2024/06/19 08:45:54.245 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:70, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:69, RowCount:0, ArgLen:1, start time: 2024-06-19 08:45:54.244 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/19 08:45:54.245 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:70, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:69, RowCount:0, ArgLen:1, start time: 2024-06-19 08:45:54.244 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_zcfqb` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL AUTO_INCREMENT,\n  `c_rvm_p` text DEFAULT NULL,\n  `c_dl_pmd` int(11) DEFAULT NULL,\n  `c_avevqc` text DEFAULT NULL,\n  `c_ywxlqb` double DEFAULT NULL,\n  `c_sqqbbd` int(11) DEFAULT NULL,\n  `c_2wz8nc` text DEFAULT NULL,\n  `c_qyxu0` double DEFAULT NULL,\n  `c_slu2bd` int(11) DEFAULT NULL,\n  `c_ph8nh` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=77001;"]
   > [2024/06/19 08:45:54.246 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:70, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:69, RowCount:0, ArgLen:0, start time: 2024-06-19 08:45:54.244 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:45:54.248 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=34] [neededSchemaVersion=35] ["start time"=487.146µs] [phyTblIDs="[69]"] [actionTypes="[8]"]
   > [2024/06/19 08:45:54.250 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=35] ["take time"=2.234167ms] [job="ID:70, Type:create table, State:done, SchemaState:public, SchemaID:65, TableID:69, RowCount:0, ArgLen:1, start time: 2024-06-19 08:45:54.244 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:45:54.251 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:70, Type:create table, State:synced, SchemaState:public, SchemaID:65, TableID:69, RowCount:0, ArgLen:0, start time: 2024-06-19 08:45:54.244 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:45:54.252 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=70]
   > [2024/06/19 08:45:54.253 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=64] ["first split key"=748000000000000045]
   > [2024/06/19 08:45:54.253 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=64] ["first at"=748000000000000045] ["first new region left"="{Id:64 StartKey:7480000000000000ff4300000000000000f8 EndKey:7480000000000000ff4500000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:65 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/19 08:45:54.253 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/19 08:45:54.253 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[64]"]
   > [2024/06/19 08:45:54.254 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=35] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_zcfqb` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/19 08:45:54.255 +00:00] [WARN] [2pc.go:1800] ["schemaLeaseChecker is not set for this transaction"] [sessionID=405] [startTS=450569634907422720] [checkTS=450569634907422721]
   > [2024/06/19 08:45:54.257 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=35] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_zcfqb` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/19 08:45:55.292 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/06/19 08:45:55.303 +00:00] [INFO] [set.go:147] ["set global var"] [conn=407] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/06/19 08:45:55.599 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/06/19 08:45:55.610 +00:00] [INFO] [set.go:147] ["set global var"] [conn=409] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/06/19 08:45:56.500 +00:00] [WARN] [2pc.go:1800] ["schemaLeaseChecker is not set for this transaction"] [sessionID=409] [startTS=450569635495673856] [checkTS=450569635495936000]

### Scenario 1
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  BEGIN OPTIMISTIC;
     - TID: 0
     - Output: None
 * Instruction #2:
     - SQL:  insert into t_zcfqb (wkey, c_rvm_p, c_avevqc, c_ywxlqb, c_sqqbbd, c_2wz8nc, c_q...
     - TID: 0
     - Output: None
 * Instruction #3:
     - SQL:  select pkey from t_zcfqb where wkey = 121;
     - TID: 0
     - Output: [(77001,), (77002,), (77003,), (77004,), (77005,), (77006,), (77007,), (77008,), (77009,), (77010,), (77011,), (77012,), (77013,), (77014,), (77015,), (77016,), (77017,), (77018,), (77019,), (77020,), (77021,), (77022,), (77023,), (77024,), (77025,), (77026,), (77027,), (77028,), (77029,), (77030,), (77031,), (77032,), (77033,), (77034,), (77035,), (77036,), (77037,), (77038,), (77039,), (77040,), (77041,), (77042,), (77043,), (77044,), (77045,), (77046,), (77047,), (77048,), (77049,)]
 * Instruction #4:
     - SQL:  COMMIT;
     - TID: 0
     - Output: None

 * Container logs:
   > [2024/06/19 08:45:59.480 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/06/19 08:45:59.482 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=413] [schemaVersion=43] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/06/19 08:45:59.483 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:77, Type:drop schema, State:none, SchemaState:queueing, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:45:59.483 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/19 08:45:59.484 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:77, Type:drop schema, State:none, SchemaState:queueing, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:45:59.483 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/06/19 08:45:59.484 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:none, SchemaState:queueing, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:45:59.483 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:45:59.485 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=43] [neededSchemaVersion=44] ["start time"=85.487µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 08:45:59.487 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=44] ["take time"=2.236961ms] [job="ID:77, Type:drop schema, State:running, SchemaState:write only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:45:59.483 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:45:59.487 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:running, SchemaState:write only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:45:59.483 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:45:59.488 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=44] [neededSchemaVersion=45] ["start time"=125.017µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 08:45:59.490 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=45] ["take time"=2.248974ms] [job="ID:77, Type:drop schema, State:running, SchemaState:delete only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:45:59.483 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:45:59.491 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:running, SchemaState:delete only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:45:59.483 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:45:59.492 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=45] [neededSchemaVersion=46] ["start time"=73.404µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 08:45:59.494 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=46] ["take time"=2.084426ms] [job="ID:77, Type:drop schema, State:done, SchemaState:queueing, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:45:59.483 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:45:59.494 +00:00] [INFO] [delete_range.go:103] ["[ddl] add job into delete-range table"] [jobID=77] [jobType="drop schema"]
   > [2024/06/19 08:45:59.494 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:45:59.483 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:45:59.495 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=77]
   > [2024/06/19 08:45:59.495 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/19 08:45:59.497 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=413] [schemaVersion=46] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/06/19 08:45:59.498 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:79, Type:create schema, State:none, SchemaState:queueing, SchemaID:78, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 08:45:59.497 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/19 08:45:59.498 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:79, Type:create schema, State:none, SchemaState:queueing, SchemaID:78, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 08:45:59.497 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/19 08:45:59.499 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:79, Type:create schema, State:none, SchemaState:queueing, SchemaID:78, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:45:59.497 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:45:59.501 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=46] [neededSchemaVersion=47] ["start time"=178.096µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 08:45:59.503 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=47] ["take time"=2.270834ms] [job="ID:79, Type:create schema, State:done, SchemaState:public, SchemaID:78, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 08:45:59.497 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:45:59.504 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:79, Type:create schema, State:synced, SchemaState:public, SchemaID:78, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:45:59.497 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:45:59.505 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=79]
   > [2024/06/19 08:45:59.505 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/19 08:45:59.512 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=413] [schemaVersion=47] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_nvues`\n--\n\nDROP TABLE IF EXISTS `t_nvues`;"] [user=root@%]
   > [2024/06/19 08:45:59.513 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=413] [schemaVersion=47] [cur_db=testdb] [sql="CREATE TABLE `t_nvues` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL AUTO_INCREMENT,\n  `c_709vdd` double DEFAULT NULL,\n  `c_gsbzrd` text DEFAULT NULL,\n  `c_bsydab` int(11) DEFAULT NULL,\n  `c_vm9_pb` int(11) DEFAULT NULL,\n  `c_hdnifc` double DEFAULT NULL,\n  `c_dzs4sc` double DEFAULT NULL,\n  `c_h1m_zb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=110001;"] [user=root@%]
   > [2024/06/19 08:45:59.514 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:81, Type:create table, State:none, SchemaState:queueing, SchemaID:78, TableID:80, RowCount:0, ArgLen:1, start time: 2024-06-19 08:45:59.513 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/19 08:45:59.514 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:81, Type:create table, State:none, SchemaState:queueing, SchemaID:78, TableID:80, RowCount:0, ArgLen:1, start time: 2024-06-19 08:45:59.513 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_nvues` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL AUTO_INCREMENT,\n  `c_709vdd` double DEFAULT NULL,\n  `c_gsbzrd` text DEFAULT NULL,\n  `c_bsydab` int(11) DEFAULT NULL,\n  `c_vm9_pb` int(11) DEFAULT NULL,\n  `c_hdnifc` double DEFAULT NULL,\n  `c_dzs4sc` double DEFAULT NULL,\n  `c_h1m_zb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=110001;"]
   > [2024/06/19 08:45:59.515 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:81, Type:create table, State:none, SchemaState:queueing, SchemaID:78, TableID:80, RowCount:0, ArgLen:0, start time: 2024-06-19 08:45:59.513 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:45:59.518 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=47] [neededSchemaVersion=48] ["start time"=707.497µs] [phyTblIDs="[80]"] [actionTypes="[8]"]
   > [2024/06/19 08:45:59.519 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=48] ["take time"=2.257843ms] [job="ID:81, Type:create table, State:done, SchemaState:public, SchemaID:78, TableID:80, RowCount:0, ArgLen:1, start time: 2024-06-19 08:45:59.513 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:45:59.521 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:81, Type:create table, State:synced, SchemaState:public, SchemaID:78, TableID:80, RowCount:0, ArgLen:0, start time: 2024-06-19 08:45:59.513 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:45:59.522 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=81]
   > [2024/06/19 08:45:59.522 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=68] ["first split key"=748000000000000050]
   > [2024/06/19 08:45:59.523 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=68] ["first at"=748000000000000050] ["first new region left"="{Id:68 StartKey:7480000000000000ff4a00000000000000f8 EndKey:7480000000000000ff5000000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:69 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/19 08:45:59.523 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[68]"]
   > [2024/06/19 08:45:59.523 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/19 08:45:59.524 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=413] [schemaVersion=48] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_nvues` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/19 08:45:59.526 +00:00] [WARN] [2pc.go:1800] ["schemaLeaseChecker is not set for this transaction"] [sessionID=413] [startTS=450569636289183744] [checkTS=450569636289183745]
   > [2024/06/19 08:45:59.529 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=413] [schemaVersion=48] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_nvues` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/19 08:45:59.530 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=413] [schemaVersion=48] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_zcfqb`\n--\n\nDROP TABLE IF EXISTS `t_zcfqb`;"] [user=root@%]
   > [2024/06/19 08:45:59.531 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=413] [schemaVersion=48] [cur_db=testdb] [sql="CREATE TABLE `t_zcfqb` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL AUTO_INCREMENT,\n  `c_rvm_p` text DEFAULT NULL,\n  `c_dl_pmd` int(11) DEFAULT NULL,\n  `c_avevqc` text DEFAULT NULL,\n  `c_ywxlqb` double DEFAULT NULL,\n  `c_sqqbbd` int(11) DEFAULT NULL,\n  `c_2wz8nc` text DEFAULT NULL,\n  `c_qyxu0` double DEFAULT NULL,\n  `c_slu2bd` int(11) DEFAULT NULL,\n  `c_ph8nh` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=77001;"] [user=root@%]
   > [2024/06/19 08:45:59.532 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:83, Type:create table, State:none, SchemaState:queueing, SchemaID:78, TableID:82, RowCount:0, ArgLen:1, start time: 2024-06-19 08:45:59.531 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/19 08:45:59.532 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:83, Type:create table, State:none, SchemaState:queueing, SchemaID:78, TableID:82, RowCount:0, ArgLen:1, start time: 2024-06-19 08:45:59.531 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_zcfqb` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL AUTO_INCREMENT,\n  `c_rvm_p` text DEFAULT NULL,\n  `c_dl_pmd` int(11) DEFAULT NULL,\n  `c_avevqc` text DEFAULT NULL,\n  `c_ywxlqb` double DEFAULT NULL,\n  `c_sqqbbd` int(11) DEFAULT NULL,\n  `c_2wz8nc` text DEFAULT NULL,\n  `c_qyxu0` double DEFAULT NULL,\n  `c_slu2bd` int(11) DEFAULT NULL,\n  `c_ph8nh` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=77001;"]
   > [2024/06/19 08:45:59.533 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:83, Type:create table, State:none, SchemaState:queueing, SchemaID:78, TableID:82, RowCount:0, ArgLen:0, start time: 2024-06-19 08:45:59.531 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:45:59.536 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=48] [neededSchemaVersion=49] ["start time"=574.658µs] [phyTblIDs="[82]"] [actionTypes="[8]"]
   > [2024/06/19 08:45:59.538 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=49] ["take time"=2.072274ms] [job="ID:83, Type:create table, State:done, SchemaState:public, SchemaID:78, TableID:82, RowCount:0, ArgLen:1, start time: 2024-06-19 08:45:59.531 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:45:59.539 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:83, Type:create table, State:synced, SchemaState:public, SchemaID:78, TableID:82, RowCount:0, ArgLen:0, start time: 2024-06-19 08:45:59.531 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:45:59.541 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=83]
   > [2024/06/19 08:45:59.541 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=70] ["first split key"=748000000000000052]
   > [2024/06/19 08:45:59.542 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=70] ["first at"=748000000000000052] ["first new region left"="{Id:70 StartKey:7480000000000000ff5000000000000000f8 EndKey:7480000000000000ff5200000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:71 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/19 08:45:59.542 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/19 08:45:59.542 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[70]"]
   > [2024/06/19 08:45:59.543 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=413] [schemaVersion=49] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_zcfqb` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/19 08:45:59.545 +00:00] [WARN] [2pc.go:1800] ["schemaLeaseChecker is not set for this transaction"] [sessionID=413] [startTS=450569636294164480] [checkTS=450569636294164481]
   > [2024/06/19 08:45:59.548 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=413] [schemaVersion=49] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_zcfqb` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/19 08:46:00.568 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/06/19 08:46:00.582 +00:00] [INFO] [set.go:147] ["set global var"] [conn=415] [name=tx_isolation] [val=REPEATABLE-READ]
