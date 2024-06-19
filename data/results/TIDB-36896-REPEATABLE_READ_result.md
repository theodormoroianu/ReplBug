# Bug ID TIDB-36896-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/36896
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ


## Details
 * Database: tidb-v6.1.0
 * Number of scenarios: 1
 * Initial setup script: /home/theodor/Projects/MasterThesis/data/sql/TIDB-36896_mysql_bk.sql

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
     - SQL:  WITH cte_0 AS (select ref_0.wkey as c0, ref_0.pkey as c1, ref_0.c_rrbxh as c2, ...
     - TID: 0
     - Output: ERROR: Timeout for this transaction.
 * Instruction #3:
     - SQL:  commit;
     - TID: 0
     - Output: ERROR: Timeout for this transaction.

 * Container logs:
   > [2024/06/19 08:57:13.783 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/06/19 08:57:13.787 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=32] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/06/19 08:57:13.788 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=32] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/06/19 08:57:13.790 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:66, Type:create schema, State:none, SchemaState:queueing, SchemaID:65, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 08:57:13.789 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/19 08:57:13.790 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:66, Type:create schema, State:none, SchemaState:queueing, SchemaID:65, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 08:57:13.789 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/19 08:57:13.790 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:create schema, State:none, SchemaState:queueing, SchemaID:65, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:57:13.789 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:57:13.791 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=32] [neededSchemaVersion=33] ["start time"=161.056µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/19 08:57:13.793 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=33] ["take time"=2.208401ms] [job="ID:66, Type:create schema, State:done, SchemaState:public, SchemaID:65, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-19 08:57:13.789 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:57:13.794 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:create schema, State:synced, SchemaState:public, SchemaID:65, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-19 08:57:13.789 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:57:13.795 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=66]
   > [2024/06/19 08:57:13.795 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/19 08:57:13.801 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=33] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_2el7jd`\n--\n\nDROP TABLE IF EXISTS `t_2el7jd`;"] [user=root@%]
   > [2024/06/19 08:57:13.802 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=33] [cur_db=testdb] [sql="CREATE TABLE `t_2el7jd` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_hzkgf` text DEFAULT NULL,\n  `c_si87c` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_alxrj` (`wkey`,`pkey`,`c_si87c`),\n  KEY `t_za4dpb` (`pkey`,`c_si87c`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/06/19 08:57:13.804 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:68, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:67, RowCount:0, ArgLen:1, start time: 2024-06-19 08:57:13.803 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/19 08:57:13.804 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:68, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:67, RowCount:0, ArgLen:1, start time: 2024-06-19 08:57:13.803 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_2el7jd` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_hzkgf` text DEFAULT NULL,\n  `c_si87c` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_alxrj` (`wkey`,`pkey`,`c_si87c`),\n  KEY `t_za4dpb` (`pkey`,`c_si87c`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/19 08:57:13.804 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:68, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:67, RowCount:0, ArgLen:0, start time: 2024-06-19 08:57:13.803 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:57:13.806 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=33] [neededSchemaVersion=34] ["start time"=440.772µs] [phyTblIDs="[67]"] [actionTypes="[8]"]
   > [2024/06/19 08:57:13.808 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=34] ["take time"=2.091556ms] [job="ID:68, Type:create table, State:done, SchemaState:public, SchemaID:65, TableID:67, RowCount:0, ArgLen:1, start time: 2024-06-19 08:57:13.803 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:57:13.809 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:68, Type:create table, State:synced, SchemaState:public, SchemaID:65, TableID:67, RowCount:0, ArgLen:0, start time: 2024-06-19 08:57:13.803 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:57:13.810 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=68]
   > [2024/06/19 08:57:13.810 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/19 08:57:13.810 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=60] ["first split key"=748000000000000043]
   > [2024/06/19 08:57:13.811 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=34] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_2el7jd` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/19 08:57:13.814 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=62] ["first at"=748000000000000043] ["first new region left"="{Id:62 StartKey:7480000000000000ff3f00000000000000f8 EndKey:7480000000000000ff4300000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:63 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/19 08:57:13.814 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[62]"]
   > [2024/06/19 08:57:13.815 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=34] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_2el7jd` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/19 08:57:13.816 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=34] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_p7c1bd`\n--\n\nDROP TABLE IF EXISTS `t_p7c1bd`;"] [user=root@%]
   > [2024/06/19 08:57:13.816 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=34] [cur_db=testdb] [sql="CREATE TABLE `t_p7c1bd` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_rrbxh` text DEFAULT NULL,\n  `c_c5cvkb` int(11) DEFAULT NULL,\n  `c_ag5ccc` int(11) DEFAULT NULL,\n  `c_qo4qvc` text DEFAULT NULL,\n  `c_lhs3h` int(11) DEFAULT NULL,\n  `c_8dah2b` int(11) DEFAULT NULL,\n  `c_eg6xsc` int(11) DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_s0z7f` (`c_ag5ccc`,`c_8dah2b`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/06/19 08:57:13.818 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:70, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:69, RowCount:0, ArgLen:1, start time: 2024-06-19 08:57:13.817 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/19 08:57:13.818 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:70, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:69, RowCount:0, ArgLen:1, start time: 2024-06-19 08:57:13.817 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_p7c1bd` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_rrbxh` text DEFAULT NULL,\n  `c_c5cvkb` int(11) DEFAULT NULL,\n  `c_ag5ccc` int(11) DEFAULT NULL,\n  `c_qo4qvc` text DEFAULT NULL,\n  `c_lhs3h` int(11) DEFAULT NULL,\n  `c_8dah2b` int(11) DEFAULT NULL,\n  `c_eg6xsc` int(11) DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_s0z7f` (`c_ag5ccc`,`c_8dah2b`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/19 08:57:13.819 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:70, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:69, RowCount:0, ArgLen:0, start time: 2024-06-19 08:57:13.817 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:57:13.821 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=34] [neededSchemaVersion=35] ["start time"=452.576µs] [phyTblIDs="[69]"] [actionTypes="[8]"]
   > [2024/06/19 08:57:13.823 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=35] ["take time"=2.256872ms] [job="ID:70, Type:create table, State:done, SchemaState:public, SchemaID:65, TableID:69, RowCount:0, ArgLen:1, start time: 2024-06-19 08:57:13.817 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:57:13.824 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:70, Type:create table, State:synced, SchemaState:public, SchemaID:65, TableID:69, RowCount:0, ArgLen:0, start time: 2024-06-19 08:57:13.817 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/19 08:57:13.825 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=70]
   > [2024/06/19 08:57:13.825 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/19 08:57:13.825 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=64] ["first split key"=748000000000000045]
   > [2024/06/19 08:57:13.826 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=64] ["first at"=748000000000000045] ["first new region left"="{Id:64 StartKey:7480000000000000ff4300000000000000f8 EndKey:7480000000000000ff4500000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:65 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/19 08:57:13.826 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[64]"]
   > [2024/06/19 08:57:13.826 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=35] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_p7c1bd` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/19 08:57:13.831 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=405] [schemaVersion=35] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_p7c1bd` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/19 08:57:14.859 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/06/19 08:57:14.872 +00:00] [INFO] [set.go:147] ["set global var"] [conn=407] [name=tx_isolation] [val=REPEATABLE-READ]
