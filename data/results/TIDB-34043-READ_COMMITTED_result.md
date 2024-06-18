# Bug ID TIDB-34043-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/34043
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED


## Details
 * Database: tidb-v6.1.0
 * Number of scenarios: 1
 * Initial setup script: /home/theodor/Projects/MasterThesis/data/sql/TIDB-34043_mysql_bk.sql

## Results
### Scenario 0
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
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
   > [2024/06/18 16:22:27.126 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/06/18 16:22:27.129 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=43] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/06/18 16:22:27.130 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:77, Type:drop schema, State:none, SchemaState:queueing, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:22:27.129 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 16:22:27.130 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:77, Type:drop schema, State:none, SchemaState:queueing, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:22:27.129 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/06/18 16:22:27.130 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:none, SchemaState:queueing, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:22:27.129 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:22:27.132 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=43] [neededSchemaVersion=44] ["start time"=110.49µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 16:22:27.134 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=44] ["take time"=2.235504ms] [job="ID:77, Type:drop schema, State:running, SchemaState:write only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:22:27.129 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:22:27.134 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:running, SchemaState:write only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:22:27.129 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:22:27.135 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=44] [neededSchemaVersion=45] ["start time"=83.531µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 16:22:27.137 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=45] ["take time"=2.065928ms] [job="ID:77, Type:drop schema, State:running, SchemaState:delete only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:22:27.129 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:22:27.137 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:running, SchemaState:delete only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:22:27.129 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:22:27.138 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=45] [neededSchemaVersion=46] ["start time"=64.883µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 16:22:27.140 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=46] ["take time"=2.335518ms] [job="ID:77, Type:drop schema, State:done, SchemaState:queueing, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:22:27.129 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:22:27.141 +00:00] [INFO] [delete_range.go:103] ["[ddl] add job into delete-range table"] [jobID=77] [jobType="drop schema"]
   > [2024/06/18 16:22:27.141 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:22:27.129 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:22:27.143 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=77]
   > [2024/06/18 16:22:27.143 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 16:22:27.144 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=46] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/06/18 16:22:27.146 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:79, Type:create schema, State:none, SchemaState:queueing, SchemaID:78, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 16:22:27.145 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 16:22:27.146 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:79, Type:create schema, State:none, SchemaState:queueing, SchemaID:78, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 16:22:27.145 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/18 16:22:27.147 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:79, Type:create schema, State:none, SchemaState:queueing, SchemaID:78, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:22:27.145 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:22:27.148 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=46] [neededSchemaVersion=47] ["start time"=165.805µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 16:22:27.151 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=47] ["take time"=2.925264ms] [job="ID:79, Type:create schema, State:done, SchemaState:public, SchemaID:78, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 16:22:27.145 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:22:27.151 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:79, Type:create schema, State:synced, SchemaState:public, SchemaID:78, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:22:27.145 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:22:27.152 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=79]
   > [2024/06/18 16:22:27.152 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 16:22:27.160 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=47] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_wzgyvd`\n--\n\nDROP TABLE IF EXISTS `t_wzgyvd`;"] [user=root@%]
   > [2024/06/18 16:22:27.160 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=47] [cur_db=testdb] [sql="CREATE TABLE `t_wzgyvd` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_oswlic` text DEFAULT NULL,\n  `c_c23g6c` int(11) DEFAULT NULL,\n  `c__gkztd` double DEFAULT NULL,\n  `c_pqvmnd` text DEFAULT NULL,\n  `c_dm4wqb` text DEFAULT NULL,\n  `c_hysvi` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  UNIQUE KEY `pkey_2` (`pkey`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/06/18 16:22:27.162 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:81, Type:create table, State:none, SchemaState:queueing, SchemaID:78, TableID:80, RowCount:0, ArgLen:1, start time: 2024-06-18 16:22:27.161 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 16:22:27.162 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:81, Type:create table, State:none, SchemaState:queueing, SchemaID:78, TableID:80, RowCount:0, ArgLen:1, start time: 2024-06-18 16:22:27.161 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_wzgyvd` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_oswlic` text DEFAULT NULL,\n  `c_c23g6c` int(11) DEFAULT NULL,\n  `c__gkztd` double DEFAULT NULL,\n  `c_pqvmnd` text DEFAULT NULL,\n  `c_dm4wqb` text DEFAULT NULL,\n  `c_hysvi` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  UNIQUE KEY `pkey_2` (`pkey`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/18 16:22:27.163 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:81, Type:create table, State:none, SchemaState:queueing, SchemaID:78, TableID:80, RowCount:0, ArgLen:0, start time: 2024-06-18 16:22:27.161 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:22:27.166 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=47] [neededSchemaVersion=48] ["start time"=320.575µs] [phyTblIDs="[80]"] [actionTypes="[8]"]
   > [2024/06/18 16:22:27.167 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=48] ["take time"=2.067813ms] [job="ID:81, Type:create table, State:done, SchemaState:public, SchemaID:78, TableID:80, RowCount:0, ArgLen:1, start time: 2024-06-18 16:22:27.161 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:22:27.168 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:81, Type:create table, State:synced, SchemaState:public, SchemaID:78, TableID:80, RowCount:0, ArgLen:0, start time: 2024-06-18 16:22:27.161 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:22:27.169 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=81]
   > [2024/06/18 16:22:27.169 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 16:22:27.170 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=48] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_wzgyvd` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/18 16:22:27.171 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=68] ["first split key"=748000000000000050]
   > [2024/06/18 16:22:27.172 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=68] ["first at"=748000000000000050] ["first new region left"="{Id:68 StartKey:7480000000000000ff4a00000000000000f8 EndKey:7480000000000000ff5000000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:69 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/18 16:22:27.172 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[68]"]
   > [2024/06/18 16:22:27.172 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=48] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_wzgyvd` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/18 16:22:27.172 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=48] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_zb_m5`\n--\n\nDROP TABLE IF EXISTS `t_zb_m5`;"] [user=root@%]
   > [2024/06/18 16:22:27.173 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=48] [cur_db=testdb] [sql="CREATE TABLE `t_zb_m5` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_4iptac` double DEFAULT NULL,\n  `c_kbcikb` double DEFAULT NULL,\n  `c_mu4_e` double DEFAULT NULL,\n  `c_lmpznc` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  UNIQUE KEY `pkey_2` (`pkey`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/06/18 16:22:27.174 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:83, Type:create table, State:none, SchemaState:queueing, SchemaID:78, TableID:82, RowCount:0, ArgLen:1, start time: 2024-06-18 16:22:27.174 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 16:22:27.174 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:83, Type:create table, State:none, SchemaState:queueing, SchemaID:78, TableID:82, RowCount:0, ArgLen:1, start time: 2024-06-18 16:22:27.174 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_zb_m5` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_4iptac` double DEFAULT NULL,\n  `c_kbcikb` double DEFAULT NULL,\n  `c_mu4_e` double DEFAULT NULL,\n  `c_lmpznc` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  UNIQUE KEY `pkey_2` (`pkey`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/18 16:22:27.175 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:83, Type:create table, State:none, SchemaState:queueing, SchemaID:78, TableID:82, RowCount:0, ArgLen:0, start time: 2024-06-18 16:22:27.174 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:22:27.176 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=48] [neededSchemaVersion=49] ["start time"=260.441µs] [phyTblIDs="[82]"] [actionTypes="[8]"]
   > [2024/06/18 16:22:27.178 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=49] ["take time"=2.089184ms] [job="ID:83, Type:create table, State:done, SchemaState:public, SchemaID:78, TableID:82, RowCount:0, ArgLen:1, start time: 2024-06-18 16:22:27.174 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:22:27.179 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:83, Type:create table, State:synced, SchemaState:public, SchemaID:78, TableID:82, RowCount:0, ArgLen:0, start time: 2024-06-18 16:22:27.174 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:22:27.180 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=83]
   > [2024/06/18 16:22:27.180 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 16:22:27.180 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=68] ["first split key"=748000000000000052]
   > [2024/06/18 16:22:27.180 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=49] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_zb_m5` DISABLE KEYS */;"] [user=root@%]
   > [2024/06/18 16:22:27.182 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=49] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_zb_m5` ENABLE KEYS */;"] [user=root@%]
   > [2024/06/18 16:22:27.183 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=70] ["first at"=748000000000000052] ["first new region left"="{Id:70 StartKey:7480000000000000ff5000000000000000f8 EndKey:7480000000000000ff5200000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:71 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/18 16:22:27.183 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[70]"]
   > [2024/06/18 16:22:28.212 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/06/18 16:22:28.221 +00:00] [INFO] [set.go:147] ["set global var"] [conn=413] [name=tx_isolation] [val=READ-COMMITTED]
