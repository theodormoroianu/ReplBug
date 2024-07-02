# Bug ID TIDB-34043-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/34043
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
     - Instruction:  select ref_0.c_lmpznc as c5 from t_zb_m5 as ref_0 where (ref_0.c_mu4_e in ( sel...
     - Transaction: conn_0
     - Output: ERROR: Timeout for this transaction.
     - Executed order: Not executed

 * Container logs:
   > [2024/07/02 13:22:22.138 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/07/02 13:22:22.140 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=417] [schemaVersion=57] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/02 13:22:22.140 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:90, Type:drop schema, State:none, SchemaState:queueing, SchemaID:85, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:22:22.14 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 13:22:22.140 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:90, Type:drop schema, State:none, SchemaState:queueing, SchemaID:85, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:22:22.14 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/02 13:22:22.141 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:90, Type:drop schema, State:none, SchemaState:queueing, SchemaID:85, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:22:22.14 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:22:22.141 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=57] [neededSchemaVersion=58] ["start time"=78.642µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 13:22:22.143 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=58] ["take time"=2.108602ms] [job="ID:90, Type:drop schema, State:running, SchemaState:write only, SchemaID:85, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:22:22.14 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:22:22.144 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:90, Type:drop schema, State:running, SchemaState:write only, SchemaID:85, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:22:22.14 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:22:22.144 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=58] [neededSchemaVersion=59] ["start time"=47.143µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 13:22:22.147 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=59] ["take time"=2.657071ms] [job="ID:90, Type:drop schema, State:running, SchemaState:delete only, SchemaID:85, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:22:22.14 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:22:22.147 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:90, Type:drop schema, State:running, SchemaState:delete only, SchemaID:85, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:22:22.14 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:22:22.148 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=59] [neededSchemaVersion=60] ["start time"=65.792µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 13:22:22.150 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=60] ["take time"=2.033383ms] [job="ID:90, Type:drop schema, State:done, SchemaState:queueing, SchemaID:85, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:22:22.14 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:22:22.150 +00:00] [INFO] [delete_range.go:103] ["[ddl] add job into delete-range table"] [jobID=90] [jobType="drop schema"]
   > [2024/07/02 13:22:22.150 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:90, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:85, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:22:22.14 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:22:22.151 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=90]
   > [2024/07/02 13:22:22.151 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 13:22:22.152 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=417] [schemaVersion=60] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/02 13:22:22.153 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:92, Type:create schema, State:none, SchemaState:queueing, SchemaID:91, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 13:22:22.153 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 13:22:22.153 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:92, Type:create schema, State:none, SchemaState:queueing, SchemaID:91, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 13:22:22.153 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/02 13:22:22.153 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:92, Type:create schema, State:none, SchemaState:queueing, SchemaID:91, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:22:22.153 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:22:22.154 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=60] [neededSchemaVersion=61] ["start time"=76.337µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 13:22:22.156 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=61] ["take time"=2.139263ms] [job="ID:92, Type:create schema, State:done, SchemaState:public, SchemaID:91, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 13:22:22.153 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:22:22.156 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:92, Type:create schema, State:synced, SchemaState:public, SchemaID:91, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:22:22.153 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:22:22.157 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=92]
   > [2024/07/02 13:22:22.157 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 13:22:22.161 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=417] [schemaVersion=61] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_wzgyvd`\n--\n\nDROP TABLE IF EXISTS `t_wzgyvd`;"] [user=root@%]
   > [2024/07/02 13:22:22.162 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=417] [schemaVersion=61] [cur_db=testdb] [sql="CREATE TABLE `t_wzgyvd` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_oswlic` text DEFAULT NULL,\n  `c_c23g6c` int(11) DEFAULT NULL,\n  `c__gkztd` double DEFAULT NULL,\n  `c_pqvmnd` text DEFAULT NULL,\n  `c_dm4wqb` text DEFAULT NULL,\n  `c_hysvi` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  UNIQUE KEY `pkey_2` (`pkey`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/07/02 13:22:22.163 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:94, Type:create table, State:none, SchemaState:queueing, SchemaID:91, TableID:93, RowCount:0, ArgLen:1, start time: 2024-07-02 13:22:22.163 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 13:22:22.163 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:94, Type:create table, State:none, SchemaState:queueing, SchemaID:91, TableID:93, RowCount:0, ArgLen:1, start time: 2024-07-02 13:22:22.163 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_wzgyvd` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_oswlic` text DEFAULT NULL,\n  `c_c23g6c` int(11) DEFAULT NULL,\n  `c__gkztd` double DEFAULT NULL,\n  `c_pqvmnd` text DEFAULT NULL,\n  `c_dm4wqb` text DEFAULT NULL,\n  `c_hysvi` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  UNIQUE KEY `pkey_2` (`pkey`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/02 13:22:22.164 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:94, Type:create table, State:none, SchemaState:queueing, SchemaID:91, TableID:93, RowCount:0, ArgLen:0, start time: 2024-07-02 13:22:22.163 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:22:22.166 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=61] [neededSchemaVersion=62] ["start time"=359.128µs] [phyTblIDs="[93]"] [actionTypes="[8]"]
   > [2024/07/02 13:22:22.167 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=62] ["take time"=2.028493ms] [job="ID:94, Type:create table, State:done, SchemaState:public, SchemaID:91, TableID:93, RowCount:0, ArgLen:1, start time: 2024-07-02 13:22:22.163 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:22:22.168 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:94, Type:create table, State:synced, SchemaState:public, SchemaID:91, TableID:93, RowCount:0, ArgLen:0, start time: 2024-07-02 13:22:22.163 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:22:22.169 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=94]
   > [2024/07/02 13:22:22.169 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 13:22:22.169 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=74] ["first split key"=74800000000000005d]
   > [2024/07/02 13:22:22.169 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=74] ["first at"=74800000000000005d] ["first new region left"="{Id:74 StartKey:7480000000000000ff5700000000000000f8 EndKey:7480000000000000ff5d00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:75 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/02 13:22:22.169 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[74]"]
   > [2024/07/02 13:22:22.170 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=417] [schemaVersion=62] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_wzgyvd` DISABLE KEYS */;"] [user=root@%]
   > [2024/07/02 13:22:22.172 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=417] [schemaVersion=62] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_wzgyvd` ENABLE KEYS */;"] [user=root@%]
   > [2024/07/02 13:22:22.172 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=417] [schemaVersion=62] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_zb_m5`\n--\n\nDROP TABLE IF EXISTS `t_zb_m5`;"] [user=root@%]
   > [2024/07/02 13:22:22.173 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=417] [schemaVersion=62] [cur_db=testdb] [sql="CREATE TABLE `t_zb_m5` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_4iptac` double DEFAULT NULL,\n  `c_kbcikb` double DEFAULT NULL,\n  `c_mu4_e` double DEFAULT NULL,\n  `c_lmpznc` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  UNIQUE KEY `pkey_2` (`pkey`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/07/02 13:22:22.174 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:96, Type:create table, State:none, SchemaState:queueing, SchemaID:91, TableID:95, RowCount:0, ArgLen:1, start time: 2024-07-02 13:22:22.174 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 13:22:22.174 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:96, Type:create table, State:none, SchemaState:queueing, SchemaID:91, TableID:95, RowCount:0, ArgLen:1, start time: 2024-07-02 13:22:22.174 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_zb_m5` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_4iptac` double DEFAULT NULL,\n  `c_kbcikb` double DEFAULT NULL,\n  `c_mu4_e` double DEFAULT NULL,\n  `c_lmpznc` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  UNIQUE KEY `pkey_2` (`pkey`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/02 13:22:22.174 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:96, Type:create table, State:none, SchemaState:queueing, SchemaID:91, TableID:95, RowCount:0, ArgLen:0, start time: 2024-07-02 13:22:22.174 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:22:22.176 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=62] [neededSchemaVersion=63] ["start time"=415.84µs] [phyTblIDs="[95]"] [actionTypes="[8]"]
   > [2024/07/02 13:22:22.178 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=63] ["take time"=2.356541ms] [job="ID:96, Type:create table, State:done, SchemaState:public, SchemaID:91, TableID:95, RowCount:0, ArgLen:1, start time: 2024-07-02 13:22:22.174 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:22:22.178 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:96, Type:create table, State:synced, SchemaState:public, SchemaID:91, TableID:95, RowCount:0, ArgLen:0, start time: 2024-07-02 13:22:22.174 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:22:22.179 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=96]
   > [2024/07/02 13:22:22.179 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 13:22:22.179 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=76] ["first split key"=74800000000000005f]
   > [2024/07/02 13:22:22.179 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=417] [schemaVersion=63] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_zb_m5` DISABLE KEYS */;"] [user=root@%]
   > [2024/07/02 13:22:22.179 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=76] ["first at"=74800000000000005f] ["first new region left"="{Id:76 StartKey:7480000000000000ff5d00000000000000f8 EndKey:7480000000000000ff5f00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:77 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/02 13:22:22.179 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[76]"]
   > [2024/07/02 13:22:22.180 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=417] [schemaVersion=63] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_zb_m5` ENABLE KEYS */;"] [user=root@%]
   > [2024/07/02 13:22:23.209 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]

### Scenario 1
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
 * Instruction #1:
     - Instruction:  start transaction;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
 * Instruction #2:
     - Instruction:  select ref_0.c_lmpznc as c5 from t_zb_m5 as ref_0 where (ref_0.c_mu4_e in ( sel...
     - Transaction: conn_0
     - Output: ERROR: Timeout for this transaction.
     - Executed order: Not executed
 * Instruction #3:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: ERROR: Timeout for this transaction.
     - Executed order: Not executed

 * Container logs:
   > [2024/07/02 13:22:33.960 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/07/02 13:22:33.962 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=423] [schemaVersion=71] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/02 13:22:33.963 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:103, Type:drop schema, State:none, SchemaState:queueing, SchemaID:98, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:22:33.962 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 13:22:33.963 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:103, Type:drop schema, State:none, SchemaState:queueing, SchemaID:98, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:22:33.962 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/02 13:22:33.963 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:103, Type:drop schema, State:none, SchemaState:queueing, SchemaID:98, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:22:33.962 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:22:33.964 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=71] [neededSchemaVersion=72] ["start time"=49.239µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 13:22:33.966 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=72] ["take time"=2.013337ms] [job="ID:103, Type:drop schema, State:running, SchemaState:write only, SchemaID:98, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:22:33.962 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:22:33.966 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:103, Type:drop schema, State:running, SchemaState:write only, SchemaID:98, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:22:33.962 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:22:33.966 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=72] [neededSchemaVersion=73] ["start time"=54.686µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 13:22:33.968 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=73] ["take time"=2.017877ms] [job="ID:103, Type:drop schema, State:running, SchemaState:delete only, SchemaID:98, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:22:33.962 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:22:33.968 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:103, Type:drop schema, State:running, SchemaState:delete only, SchemaID:98, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:22:33.962 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:22:33.969 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=73] [neededSchemaVersion=74] ["start time"=55.664µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 13:22:33.971 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=74] ["take time"=2.291798ms] [job="ID:103, Type:drop schema, State:done, SchemaState:queueing, SchemaID:98, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:22:33.962 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:22:33.972 +00:00] [INFO] [delete_range.go:103] ["[ddl] add job into delete-range table"] [jobID=103] [jobType="drop schema"]
   > [2024/07/02 13:22:33.972 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:103, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:98, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:22:33.962 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:22:33.972 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=103]
   > [2024/07/02 13:22:33.972 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 13:22:33.973 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=423] [schemaVersion=74] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/02 13:22:33.974 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:105, Type:create schema, State:none, SchemaState:queueing, SchemaID:104, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 13:22:33.974 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 13:22:33.974 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:105, Type:create schema, State:none, SchemaState:queueing, SchemaID:104, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 13:22:33.974 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/02 13:22:33.974 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:105, Type:create schema, State:none, SchemaState:queueing, SchemaID:104, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:22:33.974 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:22:33.975 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=74] [neededSchemaVersion=75] ["start time"=73.893µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 13:22:33.977 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=75] ["take time"=2.200794ms] [job="ID:105, Type:create schema, State:done, SchemaState:public, SchemaID:104, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 13:22:33.974 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:22:33.977 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:105, Type:create schema, State:synced, SchemaState:public, SchemaID:104, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:22:33.974 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:22:33.978 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=105]
   > [2024/07/02 13:22:33.978 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 13:22:33.982 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=423] [schemaVersion=75] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_wzgyvd`\n--\n\nDROP TABLE IF EXISTS `t_wzgyvd`;"] [user=root@%]
   > [2024/07/02 13:22:33.982 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=423] [schemaVersion=75] [cur_db=testdb] [sql="CREATE TABLE `t_wzgyvd` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_oswlic` text DEFAULT NULL,\n  `c_c23g6c` int(11) DEFAULT NULL,\n  `c__gkztd` double DEFAULT NULL,\n  `c_pqvmnd` text DEFAULT NULL,\n  `c_dm4wqb` text DEFAULT NULL,\n  `c_hysvi` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  UNIQUE KEY `pkey_2` (`pkey`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/07/02 13:22:33.984 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:107, Type:create table, State:none, SchemaState:queueing, SchemaID:104, TableID:106, RowCount:0, ArgLen:1, start time: 2024-07-02 13:22:33.983 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 13:22:33.984 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:107, Type:create table, State:none, SchemaState:queueing, SchemaID:104, TableID:106, RowCount:0, ArgLen:1, start time: 2024-07-02 13:22:33.983 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_wzgyvd` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_oswlic` text DEFAULT NULL,\n  `c_c23g6c` int(11) DEFAULT NULL,\n  `c__gkztd` double DEFAULT NULL,\n  `c_pqvmnd` text DEFAULT NULL,\n  `c_dm4wqb` text DEFAULT NULL,\n  `c_hysvi` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  UNIQUE KEY `pkey_2` (`pkey`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/02 13:22:33.984 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:107, Type:create table, State:none, SchemaState:queueing, SchemaID:104, TableID:106, RowCount:0, ArgLen:0, start time: 2024-07-02 13:22:33.983 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:22:33.985 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=75] [neededSchemaVersion=76] ["start time"=195.627µs] [phyTblIDs="[106]"] [actionTypes="[8]"]
   > [2024/07/02 13:22:33.987 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=76] ["take time"=2.027655ms] [job="ID:107, Type:create table, State:done, SchemaState:public, SchemaID:104, TableID:106, RowCount:0, ArgLen:1, start time: 2024-07-02 13:22:33.983 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:22:33.987 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:107, Type:create table, State:synced, SchemaState:public, SchemaID:104, TableID:106, RowCount:0, ArgLen:0, start time: 2024-07-02 13:22:33.983 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:22:33.988 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=107]
   > [2024/07/02 13:22:33.988 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 13:22:33.988 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=80] ["first split key"=74800000000000006a]
   > [2024/07/02 13:22:33.988 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=80] ["first at"=74800000000000006a] ["first new region left"="{Id:80 StartKey:7480000000000000ff6400000000000000f8 EndKey:7480000000000000ff6a00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:81 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/02 13:22:33.988 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[80]"]
   > [2024/07/02 13:22:33.988 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=423] [schemaVersion=76] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_wzgyvd` DISABLE KEYS */;"] [user=root@%]
   > [2024/07/02 13:22:33.990 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=423] [schemaVersion=76] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_wzgyvd` ENABLE KEYS */;"] [user=root@%]
   > [2024/07/02 13:22:33.990 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=423] [schemaVersion=76] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_zb_m5`\n--\n\nDROP TABLE IF EXISTS `t_zb_m5`;"] [user=root@%]
   > [2024/07/02 13:22:33.990 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=423] [schemaVersion=76] [cur_db=testdb] [sql="CREATE TABLE `t_zb_m5` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_4iptac` double DEFAULT NULL,\n  `c_kbcikb` double DEFAULT NULL,\n  `c_mu4_e` double DEFAULT NULL,\n  `c_lmpznc` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  UNIQUE KEY `pkey_2` (`pkey`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/07/02 13:22:33.991 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:109, Type:create table, State:none, SchemaState:queueing, SchemaID:104, TableID:108, RowCount:0, ArgLen:1, start time: 2024-07-02 13:22:33.991 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 13:22:33.991 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:109, Type:create table, State:none, SchemaState:queueing, SchemaID:104, TableID:108, RowCount:0, ArgLen:1, start time: 2024-07-02 13:22:33.991 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_zb_m5` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_4iptac` double DEFAULT NULL,\n  `c_kbcikb` double DEFAULT NULL,\n  `c_mu4_e` double DEFAULT NULL,\n  `c_lmpznc` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  UNIQUE KEY `pkey_2` (`pkey`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/02 13:22:33.991 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:109, Type:create table, State:none, SchemaState:queueing, SchemaID:104, TableID:108, RowCount:0, ArgLen:0, start time: 2024-07-02 13:22:33.991 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:22:33.992 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=76] [neededSchemaVersion=77] ["start time"=164.897µs] [phyTblIDs="[108]"] [actionTypes="[8]"]
   > [2024/07/02 13:22:33.994 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=77] ["take time"=2.023814ms] [job="ID:109, Type:create table, State:done, SchemaState:public, SchemaID:104, TableID:108, RowCount:0, ArgLen:1, start time: 2024-07-02 13:22:33.991 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:22:33.995 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:109, Type:create table, State:synced, SchemaState:public, SchemaID:104, TableID:108, RowCount:0, ArgLen:0, start time: 2024-07-02 13:22:33.991 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:22:33.996 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=109]
   > [2024/07/02 13:22:33.996 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 13:22:33.996 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=82] ["first split key"=74800000000000006c]
   > [2024/07/02 13:22:33.997 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=82] ["first at"=74800000000000006c] ["first new region left"="{Id:82 StartKey:7480000000000000ff6a00000000000000f8 EndKey:7480000000000000ff6c00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:83 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/02 13:22:33.997 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[82]"]
   > [2024/07/02 13:22:33.997 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=423] [schemaVersion=77] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_zb_m5` DISABLE KEYS */;"] [user=root@%]
   > [2024/07/02 13:22:33.999 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=423] [schemaVersion=77] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_zb_m5` ENABLE KEYS */;"] [user=root@%]
   > [2024/07/02 13:22:35.033 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/07/02 13:22:35.046 +00:00] [INFO] [set.go:147] ["set global var"] [conn=425] [name=tx_isolation] [val=READ-COMMITTED]
