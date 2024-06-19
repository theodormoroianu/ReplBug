# Bug ID TIDB-38150-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/38150
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ


## Details
 * Database: tidb-v6.3.0
 * Number of scenarios: 1
 * Initial setup script: /home/theodor/Projects/MasterThesis/data/sql/TIDB-38150_mysql_bk.sql

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
     - SQL:  select t_cp0sl.wkey as c0, t_cp0sl.pkey as c1, t_cp0sl.c_1_kgbc as c2, t_cp0sl....
     - TID: 0
     - Output: []
 * Instruction #3:
     - SQL:  update t_cp0sl set wkey = 59 where t_cp0sl.c_1_kgbc not in ( select subq_0.c0 a...
     - TID: 0
     - Output: None
 * Instruction #4:
     - SQL:  select t_cp0sl.wkey as c0, t_cp0sl.pkey as c1, t_cp0sl.c_1_kgbc as c2, t_cp0sl....
     - TID: 0
     - Output: [(59, 15000, None, 75.37), (59, 16000, None, 100.57), (59, 17000, None, 34.89)]
 * Instruction #5:
     - SQL:  COMMIT;
     - TID: 0
     - Output: None

 * Container logs:
   > [2024/06/19 09:46:05.004 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/06/19 09:46:05.007 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255957] [schemaVersion=33] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/06/19 09:46:05.008 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255957] [schemaVersion=33] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/06/19 09:46:05.010 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:69, Type:create schema, State:queueing, SchemaState:none, SchemaID:68, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 09:46:05.009 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/06/19 09:46:05.011 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:69, Type:create schema, State:queueing, SchemaState:none, SchemaID:68, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 09:46:05.009 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/19 09:46:05.683 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:69, Type:create schema, State:queueing, SchemaState:none, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:46:05.009 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:46:05.687 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=33] [neededSchemaVersion=34] ["start time"=157.773µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 09:46:05.689 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=34] ["take time"=2.233546ms] [job="ID:69, Type:create schema, State:done, SchemaState:public, SchemaID:68, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 09:46:05.009 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:46:05.695 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:69, Type:create schema, State:synced, SchemaState:public, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 09:46:05.009 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:46:05.697 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=69]
   > [2024/06/19 09:46:05.697 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/06/19 09:46:05.705 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255957] [schemaVersion=34] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_cp0sl`\n--\n\nDROP TABLE IF EXISTS `t_cp0sl`;"] [user=root@%]
   > [2024/06/19 09:46:05.706 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255957] [schemaVersion=34] [cur_db=testdb] [sql="CREATE TABLE `t_cp0sl` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_1_kgbc` int(11) DEFAULT NULL,\n  `c_dw8ly` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_py61ed` (`wkey`,`pkey`,`c_1_kgbc`,`c_dw8ly`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/06/19 09:46:05.709 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:71, Type:create table, State:queueing, SchemaState:none, SchemaID:68, TableID:70, RowCount:0, ArgLen:1, start time: 2024-06-19 09:46:05.707 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/06/19 09:46:05.709 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:71, Type:create table, State:queueing, SchemaState:none, SchemaID:68, TableID:70, RowCount:0, ArgLen:1, start time: 2024-06-19 09:46:05.707 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_cp0sl` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_1_kgbc` int(11) DEFAULT NULL,\n  `c_dw8ly` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_py61ed` (`wkey`,`pkey`,`c_1_kgbc`,`c_dw8ly`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/19 09:46:05.717 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:71, Type:create table, State:queueing, SchemaState:none, SchemaID:68, TableID:70, RowCount:0, ArgLen:0, start time: 2024-06-19 09:46:05.707 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:46:05.721 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=34] [neededSchemaVersion=35] ["start time"=561.39µs] [phyTblIDs="[70]"] [actionTypes="[8]"]
   > [2024/06/19 09:46:05.723 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=35] ["take time"=2.286346ms] [job="ID:71, Type:create table, State:done, SchemaState:public, SchemaID:68, TableID:70, RowCount:0, ArgLen:1, start time: 2024-06-19 09:46:05.707 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:46:05.728 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:71, Type:create table, State:synced, SchemaState:public, SchemaID:68, TableID:70, RowCount:0, ArgLen:0, start time: 2024-06-19 09:46:05.707 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:46:05.731 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=71]
   > [2024/06/19 09:46:05.731 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/06/19 09:46:05.731 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=66] ["first split key"=748000000000000046]
   > [2024/06/19 09:46:05.731 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=66] ["first at"=748000000000000046] ["first new region left"="{Id:66 StartKey:7480000000000000ff4200000000000000f8 EndKey:7480000000000000ff4600000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:67 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/19 09:46:05.731 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[66]"]
   > [2024/06/19 09:46:05.732 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255957] [schemaVersion=35] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_cp0sl` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:46:05.734 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255957] [schemaVersion=35] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_cp0sl` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:46:05.735 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255957] [schemaVersion=35] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_d0c_g`\n--\n\nDROP TABLE IF EXISTS `t_d0c_g`;"] [user=root@%]
   > [2024/06/19 09:46:05.736 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255957] [schemaVersion=35] [cur_db=testdb] [sql="CREATE TABLE `t_d0c_g` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_p5i5kc` int(11) DEFAULT NULL,\n  `c_eephud` text DEFAULT NULL,\n  `c_dmlxnb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/06/19 09:46:05.739 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:73, Type:create table, State:queueing, SchemaState:none, SchemaID:68, TableID:72, RowCount:0, ArgLen:1, start time: 2024-06-19 09:46:05.737 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/06/19 09:46:05.739 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:73, Type:create table, State:queueing, SchemaState:none, SchemaID:68, TableID:72, RowCount:0, ArgLen:1, start time: 2024-06-19 09:46:05.737 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_d0c_g` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_p5i5kc` int(11) DEFAULT NULL,\n  `c_eephud` text DEFAULT NULL,\n  `c_dmlxnb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/19 09:46:05.747 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:73, Type:create table, State:queueing, SchemaState:none, SchemaID:68, TableID:72, RowCount:0, ArgLen:0, start time: 2024-06-19 09:46:05.737 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:46:05.752 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=35] [neededSchemaVersion=36] ["start time"=488.405µs] [phyTblIDs="[72]"] [actionTypes="[8]"]
   > [2024/06/19 09:46:05.753 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=36] ["take time"=2.09917ms] [job="ID:73, Type:create table, State:done, SchemaState:public, SchemaID:68, TableID:72, RowCount:0, ArgLen:1, start time: 2024-06-19 09:46:05.737 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:46:05.758 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:73, Type:create table, State:synced, SchemaState:public, SchemaID:68, TableID:72, RowCount:0, ArgLen:0, start time: 2024-06-19 09:46:05.737 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 09:46:05.761 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=73]
   > [2024/06/19 09:46:05.761 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/06/19 09:46:05.761 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=68] ["first split key"=748000000000000048]
   > [2024/06/19 09:46:05.761 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=68] ["first at"=748000000000000048] ["first new region left"="{Id:68 StartKey:7480000000000000ff4600000000000000f8 EndKey:7480000000000000ff4800000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:69 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/19 09:46:05.761 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[68]"]
   > [2024/06/19 09:46:05.762 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255957] [schemaVersion=36] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_d0c_g` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:46:05.765 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255957] [schemaVersion=36] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_d0c_g` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/19 09:46:06.785 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/06/19 09:46:06.798 +00:00] [INFO] [set.go:149] ["set global var"] [conn=2199023255959] [name=tx_isolation] [val=REPEATABLE-READ]
