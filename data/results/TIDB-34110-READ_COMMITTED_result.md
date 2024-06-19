# Bug ID TIDB-34110-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/34110
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED


## Details
 * Database: tidb-v6.1.0
 * Number of scenarios: 2
 * Initial setup script: /home/theodor/Projects/MasterThesis/data/sql/TIDB-34110_mysql_bk.sql

## Results
### Scenario 0
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
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
   > [2024/06/19 08:46:02.603 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/06/19 08:46:02.606 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=419] [schemaVersion=57] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/06/19 08:46:02.607 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:90, Type:drop schema, State:none, SchemaState:queueing, SchemaID:85, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:46:02.606 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/19 08:46:02.607 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:90, Type:drop schema, State:none, SchemaState:queueing, SchemaID:85, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:46:02.606 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/06/19 08:46:02.608 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:90, Type:drop schema, State:none, SchemaState:queueing, SchemaID:85, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:46:02.606 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:46:02.609 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=57] [neededSchemaVersion=58] ["start time"=127.811µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 08:46:02.611 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=58] ["take time"=2.240034ms] [job="ID:90, Type:drop schema, State:running, SchemaState:write only, SchemaID:85, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:46:02.606 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:46:02.611 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:90, Type:drop schema, State:running, SchemaState:write only, SchemaID:85, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:46:02.606 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:46:02.612 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=58] [neededSchemaVersion=59] ["start time"=91.353µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 08:46:02.614 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=59] ["take time"=2.242757ms] [job="ID:90, Type:drop schema, State:running, SchemaState:delete only, SchemaID:85, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:46:02.606 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:46:02.614 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:90, Type:drop schema, State:running, SchemaState:delete only, SchemaID:85, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:46:02.606 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:46:02.616 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=59] [neededSchemaVersion=60] ["start time"=103.436µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 08:46:02.618 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=60] ["take time"=3.053829ms] [job="ID:90, Type:drop schema, State:done, SchemaState:queueing, SchemaID:85, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:46:02.606 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:46:02.619 +00:00] [INFO] [delete_range.go:103] ["[ddl] add job into delete-range table"] [jobID=90] [jobType="drop schema"]
   > [2024/06/19 08:46:02.619 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:90, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:85, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:46:02.606 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:46:02.620 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=90]
   > [2024/06/19 08:46:02.620 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/19 08:46:02.621 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=419] [schemaVersion=60] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/06/19 08:46:02.623 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:92, Type:create schema, State:none, SchemaState:queueing, SchemaID:91, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 08:46:02.623 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/19 08:46:02.623 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:92, Type:create schema, State:none, SchemaState:queueing, SchemaID:91, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 08:46:02.623 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/19 08:46:02.624 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:92, Type:create schema, State:none, SchemaState:queueing, SchemaID:91, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:46:02.623 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:46:02.625 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=60] [neededSchemaVersion=61] ["start time"=218.046µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 08:46:02.627 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=61] ["take time"=2.273697ms] [job="ID:92, Type:create schema, State:done, SchemaState:public, SchemaID:91, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 08:46:02.623 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:46:02.628 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:92, Type:create schema, State:synced, SchemaState:public, SchemaID:91, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:46:02.623 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:46:02.629 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=92]
   > [2024/06/19 08:46:02.629 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/19 08:46:02.637 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=419] [schemaVersion=61] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_nvues`\n--\n\nDROP TABLE IF EXISTS `t_nvues`;"] [user=root@%]
   > [2024/06/19 08:46:02.638 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=419] [schemaVersion=61] [cur_db=testdb] [sql="CREATE TABLE `t_nvues` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL AUTO_INCREMENT,\n  `c_709vdd` double DEFAULT NULL,\n  `c_gsbzrd` text DEFAULT NULL,\n  `c_bsydab` int(11) DEFAULT NULL,\n  `c_vm9_pb` int(11) DEFAULT NULL,\n  `c_hdnifc` double DEFAULT NULL,\n  `c_dzs4sc` double DEFAULT NULL,\n  `c_h1m_zb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=110001;"] [user=root@%]
   > [2024/06/19 08:46:02.640 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:94, Type:create table, State:none, SchemaState:queueing, SchemaID:91, TableID:93, RowCount:0, ArgLen:1, start time: 2024-06-19 08:46:02.639 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/19 08:46:02.640 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:94, Type:create table, State:none, SchemaState:queueing, SchemaID:91, TableID:93, RowCount:0, ArgLen:1, start time: 2024-06-19 08:46:02.639 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_nvues` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL AUTO_INCREMENT,\n  `c_709vdd` double DEFAULT NULL,\n  `c_gsbzrd` text DEFAULT NULL,\n  `c_bsydab` int(11) DEFAULT NULL,\n  `c_vm9_pb` int(11) DEFAULT NULL,\n  `c_hdnifc` double DEFAULT NULL,\n  `c_dzs4sc` double DEFAULT NULL,\n  `c_h1m_zb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=110001;"]
   > [2024/06/19 08:46:02.641 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:94, Type:create table, State:none, SchemaState:queueing, SchemaID:91, TableID:93, RowCount:0, ArgLen:0, start time: 2024-06-19 08:46:02.639 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:46:02.643 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=61] [neededSchemaVersion=62] ["start time"=528.701µs] [phyTblIDs="[93]"] [actionTypes="[8]"]
   > [2024/06/19 08:46:02.645 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=62] ["take time"=2.287945ms] [job="ID:94, Type:create table, State:done, SchemaState:public, SchemaID:91, TableID:93, RowCount:0, ArgLen:1, start time: 2024-06-19 08:46:02.639 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:46:02.646 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:94, Type:create table, State:synced, SchemaState:public, SchemaID:91, TableID:93, RowCount:0, ArgLen:0, start time: 2024-06-19 08:46:02.639 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:46:02.648 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=94]
   > [2024/06/19 08:46:02.648 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=74] ["first split key"=74800000000000005d]
   > [2024/06/19 08:46:02.648 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/19 08:46:02.649 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=74] ["first at"=74800000000000005d] ["first new region left"="{Id:74 StartKey:7480000000000000ff5700000000000000f8 EndKey:7480000000000000ff5d00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:75 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/19 08:46:02.649 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[74]"]
   > [2024/06/19 08:46:02.649 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=419] [schemaVersion=62] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_nvues` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/19 08:46:02.652 +00:00] [WARN] [2pc.go:1800] ["schemaLeaseChecker is not set for this transaction"] [sessionID=419] [startTS=450569637108645888] [checkTS=450569637108645889]
   > [2024/06/19 08:46:02.655 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=419] [schemaVersion=62] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_nvues` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/19 08:46:02.656 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=419] [schemaVersion=62] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_zcfqb`\n--\n\nDROP TABLE IF EXISTS `t_zcfqb`;"] [user=root@%]
   > [2024/06/19 08:46:02.656 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=419] [schemaVersion=62] [cur_db=testdb] [sql="CREATE TABLE `t_zcfqb` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL AUTO_INCREMENT,\n  `c_rvm_p` text DEFAULT NULL,\n  `c_dl_pmd` int(11) DEFAULT NULL,\n  `c_avevqc` text DEFAULT NULL,\n  `c_ywxlqb` double DEFAULT NULL,\n  `c_sqqbbd` int(11) DEFAULT NULL,\n  `c_2wz8nc` text DEFAULT NULL,\n  `c_qyxu0` double DEFAULT NULL,\n  `c_slu2bd` int(11) DEFAULT NULL,\n  `c_ph8nh` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=77001;"] [user=root@%]
   > [2024/06/19 08:46:02.658 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:96, Type:create table, State:none, SchemaState:queueing, SchemaID:91, TableID:95, RowCount:0, ArgLen:1, start time: 2024-06-19 08:46:02.657 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/19 08:46:02.658 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:96, Type:create table, State:none, SchemaState:queueing, SchemaID:91, TableID:95, RowCount:0, ArgLen:1, start time: 2024-06-19 08:46:02.657 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_zcfqb` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL AUTO_INCREMENT,\n  `c_rvm_p` text DEFAULT NULL,\n  `c_dl_pmd` int(11) DEFAULT NULL,\n  `c_avevqc` text DEFAULT NULL,\n  `c_ywxlqb` double DEFAULT NULL,\n  `c_sqqbbd` int(11) DEFAULT NULL,\n  `c_2wz8nc` text DEFAULT NULL,\n  `c_qyxu0` double DEFAULT NULL,\n  `c_slu2bd` int(11) DEFAULT NULL,\n  `c_ph8nh` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=77001;"]
   > [2024/06/19 08:46:02.659 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:96, Type:create table, State:none, SchemaState:queueing, SchemaID:91, TableID:95, RowCount:0, ArgLen:0, start time: 2024-06-19 08:46:02.657 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:46:02.662 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=62] [neededSchemaVersion=63] ["start time"=601.686µs] [phyTblIDs="[95]"] [actionTypes="[8]"]
   > [2024/06/19 08:46:02.663 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=63] ["take time"=2.253443ms] [job="ID:96, Type:create table, State:done, SchemaState:public, SchemaID:91, TableID:95, RowCount:0, ArgLen:1, start time: 2024-06-19 08:46:02.657 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:46:02.665 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:96, Type:create table, State:synced, SchemaState:public, SchemaID:91, TableID:95, RowCount:0, ArgLen:0, start time: 2024-06-19 08:46:02.657 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:46:02.667 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=96]
   > [2024/06/19 08:46:02.667 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=76] ["first split key"=74800000000000005f]
   > [2024/06/19 08:46:02.667 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=76] ["first at"=74800000000000005f] ["first new region left"="{Id:76 StartKey:7480000000000000ff5d00000000000000f8 EndKey:7480000000000000ff5f00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:77 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/19 08:46:02.667 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[76]"]
   > [2024/06/19 08:46:02.667 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/19 08:46:02.668 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=419] [schemaVersion=63] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_zcfqb` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/19 08:46:02.670 +00:00] [WARN] [2pc.go:1800] ["schemaLeaseChecker is not set for this transaction"] [sessionID=419] [startTS=450569637113364480] [checkTS=450569637113364481]
   > [2024/06/19 08:46:02.673 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=419] [schemaVersion=63] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_zcfqb` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/19 08:46:03.691 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/06/19 08:46:03.709 +00:00] [INFO] [set.go:147] ["set global var"] [conn=421] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/06/19 08:46:04.000 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/06/19 08:46:04.014 +00:00] [INFO] [set.go:147] ["set global var"] [conn=423] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/06/19 08:46:04.902 +00:00] [WARN] [2pc.go:1800] ["schemaLeaseChecker is not set for this transaction"] [sessionID=423] [startTS=450569637698207744] [checkTS=450569637698469888]

### Scenario 1
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
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
   > [2024/06/19 08:46:06.996 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/06/19 08:46:06.998 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=427] [schemaVersion=71] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/06/19 08:46:06.999 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:103, Type:drop schema, State:none, SchemaState:queueing, SchemaID:98, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:46:06.998 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/19 08:46:06.999 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:103, Type:drop schema, State:none, SchemaState:queueing, SchemaID:98, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:46:06.998 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/06/19 08:46:06.999 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:103, Type:drop schema, State:none, SchemaState:queueing, SchemaID:98, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:46:06.998 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:46:07.000 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=71] [neededSchemaVersion=72] ["start time"=66.21µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 08:46:07.002 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=72] ["take time"=2.847447ms] [job="ID:103, Type:drop schema, State:running, SchemaState:write only, SchemaID:98, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:46:06.998 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:46:07.003 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:103, Type:drop schema, State:running, SchemaState:write only, SchemaID:98, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:46:06.998 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:46:07.003 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=72] [neededSchemaVersion=73] ["start time"=96.032µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 08:46:07.006 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=73] ["take time"=2.36065ms] [job="ID:103, Type:drop schema, State:running, SchemaState:delete only, SchemaID:98, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:46:06.998 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:46:07.006 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:103, Type:drop schema, State:running, SchemaState:delete only, SchemaID:98, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:46:06.998 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:46:07.007 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=73] [neededSchemaVersion=74] ["start time"=63.207µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 08:46:07.009 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=74] ["take time"=2.401158ms] [job="ID:103, Type:drop schema, State:done, SchemaState:queueing, SchemaID:98, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:46:06.998 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:46:07.009 +00:00] [INFO] [delete_range.go:103] ["[ddl] add job into delete-range table"] [jobID=103] [jobType="drop schema"]
   > [2024/06/19 08:46:07.009 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:103, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:98, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:46:06.998 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:46:07.010 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=103]
   > [2024/06/19 08:46:07.010 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/19 08:46:07.011 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=427] [schemaVersion=74] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/06/19 08:46:07.013 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:105, Type:create schema, State:none, SchemaState:queueing, SchemaID:104, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 08:46:07.012 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/19 08:46:07.013 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:105, Type:create schema, State:none, SchemaState:queueing, SchemaID:104, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 08:46:07.012 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/19 08:46:07.013 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:105, Type:create schema, State:none, SchemaState:queueing, SchemaID:104, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:46:07.012 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:46:07.014 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=74] [neededSchemaVersion=75] ["start time"=152.954µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 08:46:07.016 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=75] ["take time"=2.163557ms] [job="ID:105, Type:create schema, State:done, SchemaState:public, SchemaID:104, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 08:46:07.012 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:46:07.017 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:105, Type:create schema, State:synced, SchemaState:public, SchemaID:104, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:46:07.012 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:46:07.017 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=105]
   > [2024/06/19 08:46:07.017 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/19 08:46:07.022 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=427] [schemaVersion=75] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_nvues`\n--\n\nDROP TABLE IF EXISTS `t_nvues`;"] [user=root@%]
   > [2024/06/19 08:46:07.022 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=427] [schemaVersion=75] [cur_db=testdb] [sql="CREATE TABLE `t_nvues` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL AUTO_INCREMENT,\n  `c_709vdd` double DEFAULT NULL,\n  `c_gsbzrd` text DEFAULT NULL,\n  `c_bsydab` int(11) DEFAULT NULL,\n  `c_vm9_pb` int(11) DEFAULT NULL,\n  `c_hdnifc` double DEFAULT NULL,\n  `c_dzs4sc` double DEFAULT NULL,\n  `c_h1m_zb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=110001;"] [user=root@%]
   > [2024/06/19 08:46:07.023 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:107, Type:create table, State:none, SchemaState:queueing, SchemaID:104, TableID:106, RowCount:0, ArgLen:1, start time: 2024-06-19 08:46:07.023 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/19 08:46:07.023 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:107, Type:create table, State:none, SchemaState:queueing, SchemaID:104, TableID:106, RowCount:0, ArgLen:1, start time: 2024-06-19 08:46:07.023 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_nvues` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL AUTO_INCREMENT,\n  `c_709vdd` double DEFAULT NULL,\n  `c_gsbzrd` text DEFAULT NULL,\n  `c_bsydab` int(11) DEFAULT NULL,\n  `c_vm9_pb` int(11) DEFAULT NULL,\n  `c_hdnifc` double DEFAULT NULL,\n  `c_dzs4sc` double DEFAULT NULL,\n  `c_h1m_zb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=110001;"]
   > [2024/06/19 08:46:07.024 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:107, Type:create table, State:none, SchemaState:queueing, SchemaID:104, TableID:106, RowCount:0, ArgLen:0, start time: 2024-06-19 08:46:07.023 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:46:07.025 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=75] [neededSchemaVersion=76] ["start time"=287.887µs] [phyTblIDs="[106]"] [actionTypes="[8]"]
   > [2024/06/19 08:46:07.027 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=76] ["take time"=2.218033ms] [job="ID:107, Type:create table, State:done, SchemaState:public, SchemaID:104, TableID:106, RowCount:0, ArgLen:1, start time: 2024-06-19 08:46:07.023 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:46:07.028 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:107, Type:create table, State:synced, SchemaState:public, SchemaID:104, TableID:106, RowCount:0, ArgLen:0, start time: 2024-06-19 08:46:07.023 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:46:07.030 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=107]
   > [2024/06/19 08:46:07.030 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=80] ["first split key"=74800000000000006a]
   > [2024/06/19 08:46:07.030 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/19 08:46:07.030 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=80] ["first at"=74800000000000006a] ["first new region left"="{Id:80 StartKey:7480000000000000ff6400000000000000f8 EndKey:7480000000000000ff6a00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:81 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/19 08:46:07.030 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[80]"]
   > [2024/06/19 08:46:07.031 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=427] [schemaVersion=76] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_nvues` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/19 08:46:07.032 +00:00] [WARN] [2pc.go:1800] ["schemaLeaseChecker is not set for this transaction"] [sessionID=427] [startTS=450569638256836608] [checkTS=450569638256836609]
   > [2024/06/19 08:46:07.034 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=427] [schemaVersion=76] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_nvues` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/19 08:46:07.034 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=427] [schemaVersion=76] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_zcfqb`\n--\n\nDROP TABLE IF EXISTS `t_zcfqb`;"] [user=root@%]
   > [2024/06/19 08:46:07.035 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=427] [schemaVersion=76] [cur_db=testdb] [sql="CREATE TABLE `t_zcfqb` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL AUTO_INCREMENT,\n  `c_rvm_p` text DEFAULT NULL,\n  `c_dl_pmd` int(11) DEFAULT NULL,\n  `c_avevqc` text DEFAULT NULL,\n  `c_ywxlqb` double DEFAULT NULL,\n  `c_sqqbbd` int(11) DEFAULT NULL,\n  `c_2wz8nc` text DEFAULT NULL,\n  `c_qyxu0` double DEFAULT NULL,\n  `c_slu2bd` int(11) DEFAULT NULL,\n  `c_ph8nh` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=77001;"] [user=root@%]
   > [2024/06/19 08:46:07.036 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:109, Type:create table, State:none, SchemaState:queueing, SchemaID:104, TableID:108, RowCount:0, ArgLen:1, start time: 2024-06-19 08:46:07.035 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/19 08:46:07.036 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:109, Type:create table, State:none, SchemaState:queueing, SchemaID:104, TableID:108, RowCount:0, ArgLen:1, start time: 2024-06-19 08:46:07.035 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_zcfqb` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL AUTO_INCREMENT,\n  `c_rvm_p` text DEFAULT NULL,\n  `c_dl_pmd` int(11) DEFAULT NULL,\n  `c_avevqc` text DEFAULT NULL,\n  `c_ywxlqb` double DEFAULT NULL,\n  `c_sqqbbd` int(11) DEFAULT NULL,\n  `c_2wz8nc` text DEFAULT NULL,\n  `c_qyxu0` double DEFAULT NULL,\n  `c_slu2bd` int(11) DEFAULT NULL,\n  `c_ph8nh` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=77001;"]
   > [2024/06/19 08:46:07.036 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:109, Type:create table, State:none, SchemaState:queueing, SchemaID:104, TableID:108, RowCount:0, ArgLen:0, start time: 2024-06-19 08:46:07.035 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:46:07.039 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=76] [neededSchemaVersion=77] ["start time"=618.658µs] [phyTblIDs="[108]"] [actionTypes="[8]"]
   > [2024/06/19 08:46:07.040 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=77] ["take time"=2.181297ms] [job="ID:109, Type:create table, State:done, SchemaState:public, SchemaID:104, TableID:108, RowCount:0, ArgLen:1, start time: 2024-06-19 08:46:07.035 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:46:07.041 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:109, Type:create table, State:synced, SchemaState:public, SchemaID:104, TableID:108, RowCount:0, ArgLen:0, start time: 2024-06-19 08:46:07.035 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:46:07.042 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=109]
   > [2024/06/19 08:46:07.042 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=82] ["first split key"=74800000000000006c]
   > [2024/06/19 08:46:07.042 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/19 08:46:07.042 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=82] ["first at"=74800000000000006c] ["first new region left"="{Id:82 StartKey:7480000000000000ff6a00000000000000f8 EndKey:7480000000000000ff6c00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:83 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/19 08:46:07.042 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[82]"]
   > [2024/06/19 08:46:07.043 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=427] [schemaVersion=77] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_zcfqb` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/19 08:46:07.045 +00:00] [WARN] [2pc.go:1800] ["schemaLeaseChecker is not set for this transaction"] [sessionID=427] [startTS=450569638260244480] [checkTS=450569638260244481]
   > [2024/06/19 08:46:07.048 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=427] [schemaVersion=77] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_zcfqb` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/19 08:46:08.077 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/06/19 08:46:08.089 +00:00] [INFO] [set.go:147] ["set global var"] [conn=429] [name=tx_isolation] [val=READ-COMMITTED]
