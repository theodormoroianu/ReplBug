# Bug ID TIDB-38150-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/38150
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              The first select should return the same result as the second select, but it does not.


## Details
 * Database: tidb-v6.3.0
 * Number of scenarios: 2
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  select t_cp0sl.wkey as c0, t_cp0sl.pkey as c1, t_cp0sl.c_1_kgbc as c2, t_cp0sl....
     - Transaction: conn_0
     - Output: []
     - Executed order: 0
 * Instruction #1:
     - Instruction:  update t_cp0sl set wkey = 59 where t_cp0sl.c_1_kgbc not in ( select subq_0.c0 a...
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
 * Instruction #2:
     - Instruction:  select t_cp0sl.wkey as c0, t_cp0sl.pkey as c1, t_cp0sl.c_1_kgbc as c2, t_cp0sl....
     - Transaction: conn_0
     - Output: [(59, 15000, None, 75.37), (59, 16000, None, 100.57), (59, 17000, None, 34.89)]
     - Executed order: 2

 * Container logs:
   > [2024/07/02 13:57:40.957 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/02 13:57:40.959 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255969] [schemaVersion=58] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/02 13:57:40.961 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:93, Type:drop schema, State:queueing, SchemaState:public, SchemaID:88, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:40.959 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/02 13:57:40.961 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:93, Type:drop schema, State:queueing, SchemaState:public, SchemaID:88, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:40.959 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/02 13:57:40.966 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:93, Type:drop schema, State:queueing, SchemaState:public, SchemaID:88, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:40.959 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:40.969 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=58] [neededSchemaVersion=59] ["start time"=57.759µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 13:57:40.971 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=59] ["take time"=2.261904ms] [job="ID:93, Type:drop schema, State:running, SchemaState:write only, SchemaID:88, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:40.959 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:40.974 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:93, Type:drop schema, State:running, SchemaState:write only, SchemaID:88, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:40.959 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:40.977 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=59] [neededSchemaVersion=60] ["start time"=165.875µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 13:57:40.979 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=60] ["take time"=2.263161ms] [job="ID:93, Type:drop schema, State:running, SchemaState:delete only, SchemaID:88, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:40.959 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:40.982 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:93, Type:drop schema, State:running, SchemaState:delete only, SchemaID:88, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:40.959 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:40.985 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=60] [neededSchemaVersion=61] ["start time"=75.569µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 13:57:40.987 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=61] ["take time"=2.5998ms] [job="ID:93, Type:drop schema, State:done, SchemaState:none, SchemaID:88, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:40.959 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:40.991 +00:00] [INFO] [delete_range.go:109] ["[ddl] add job into delete-range table"] [jobID=93] [jobType="drop schema"]
   > [2024/07/02 13:57:40.992 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:93, Type:drop schema, State:synced, SchemaState:none, SchemaID:88, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:40.959 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:40.993 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=93]
   > [2024/07/02 13:57:40.994 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/02 13:57:40.995 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255969] [schemaVersion=61] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/02 13:57:40.997 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:95, Type:create schema, State:queueing, SchemaState:none, SchemaID:94, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 13:57:40.996 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/02 13:57:40.997 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:95, Type:create schema, State:queueing, SchemaState:none, SchemaID:94, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 13:57:40.996 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/02 13:57:41.006 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:95, Type:create schema, State:queueing, SchemaState:none, SchemaID:94, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:40.996 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:41.008 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=61] [neededSchemaVersion=62] ["start time"=73.054µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 13:57:41.010 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=62] ["take time"=2.255339ms] [job="ID:95, Type:create schema, State:done, SchemaState:public, SchemaID:94, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 13:57:40.996 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:41.014 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:95, Type:create schema, State:synced, SchemaState:public, SchemaID:94, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:40.996 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:41.015 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=95]
   > [2024/07/02 13:57:41.015 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/02 13:57:41.020 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255969] [schemaVersion=62] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_cp0sl`\n--\n\nDROP TABLE IF EXISTS `t_cp0sl`;"] [user=root@%]
   > [2024/07/02 13:57:41.021 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255969] [schemaVersion=62] [cur_db=testdb] [sql="CREATE TABLE `t_cp0sl` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_1_kgbc` int(11) DEFAULT NULL,\n  `c_dw8ly` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_py61ed` (`wkey`,`pkey`,`c_1_kgbc`,`c_dw8ly`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/07/02 13:57:41.023 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:97, Type:create table, State:queueing, SchemaState:none, SchemaID:94, TableID:96, RowCount:0, ArgLen:1, start time: 2024-07-02 13:57:41.022 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/02 13:57:41.023 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:97, Type:create table, State:queueing, SchemaState:none, SchemaID:94, TableID:96, RowCount:0, ArgLen:1, start time: 2024-07-02 13:57:41.022 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_cp0sl` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_1_kgbc` int(11) DEFAULT NULL,\n  `c_dw8ly` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_py61ed` (`wkey`,`pkey`,`c_1_kgbc`,`c_dw8ly`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/02 13:57:41.029 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:97, Type:create table, State:queueing, SchemaState:none, SchemaID:94, TableID:96, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:41.022 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:41.032 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=62] [neededSchemaVersion=63] ["start time"=186.199µs] [phyTblIDs="[96]"] [actionTypes="[8]"]
   > [2024/07/02 13:57:41.034 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=63] ["take time"=2.385385ms] [job="ID:97, Type:create table, State:done, SchemaState:public, SchemaID:94, TableID:96, RowCount:0, ArgLen:1, start time: 2024-07-02 13:57:41.022 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:41.038 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:97, Type:create table, State:synced, SchemaState:public, SchemaID:94, TableID:96, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:41.022 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:41.039 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=97]
   > [2024/07/02 13:57:41.039 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/02 13:57:41.040 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=78] ["first split key"=748000000000000060]
   > [2024/07/02 13:57:41.040 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=78] ["first at"=748000000000000060] ["first new region left"="{Id:78 StartKey:7480000000000000ff5a00000000000000f8 EndKey:7480000000000000ff6000000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:79 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/02 13:57:41.040 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[78]"]
   > [2024/07/02 13:57:41.040 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255969] [schemaVersion=63] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_cp0sl` DISABLE KEYS */;"] [user=root@%]
   > [2024/07/02 13:57:41.042 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255969] [schemaVersion=63] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_cp0sl` ENABLE KEYS */;"] [user=root@%]
   > [2024/07/02 13:57:41.042 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255969] [schemaVersion=63] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_d0c_g`\n--\n\nDROP TABLE IF EXISTS `t_d0c_g`;"] [user=root@%]
   > [2024/07/02 13:57:41.043 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255969] [schemaVersion=63] [cur_db=testdb] [sql="CREATE TABLE `t_d0c_g` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_p5i5kc` int(11) DEFAULT NULL,\n  `c_eephud` text DEFAULT NULL,\n  `c_dmlxnb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/07/02 13:57:41.046 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:99, Type:create table, State:queueing, SchemaState:none, SchemaID:94, TableID:98, RowCount:0, ArgLen:1, start time: 2024-07-02 13:57:41.044 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/02 13:57:41.046 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:99, Type:create table, State:queueing, SchemaState:none, SchemaID:94, TableID:98, RowCount:0, ArgLen:1, start time: 2024-07-02 13:57:41.044 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_d0c_g` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_p5i5kc` int(11) DEFAULT NULL,\n  `c_eephud` text DEFAULT NULL,\n  `c_dmlxnb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/02 13:57:41.051 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:99, Type:create table, State:queueing, SchemaState:none, SchemaID:94, TableID:98, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:41.044 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:41.054 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=63] [neededSchemaVersion=64] ["start time"=326.791µs] [phyTblIDs="[98]"] [actionTypes="[8]"]
   > [2024/07/02 13:57:41.055 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=64] ["take time"=2.027375ms] [job="ID:99, Type:create table, State:done, SchemaState:public, SchemaID:94, TableID:98, RowCount:0, ArgLen:1, start time: 2024-07-02 13:57:41.044 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:41.059 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:99, Type:create table, State:synced, SchemaState:public, SchemaID:94, TableID:98, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:41.044 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:41.061 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=99]
   > [2024/07/02 13:57:41.061 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/02 13:57:41.061 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=80] ["first split key"=748000000000000062]
   > [2024/07/02 13:57:41.062 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=80] ["first at"=748000000000000062] ["first new region left"="{Id:80 StartKey:7480000000000000ff6000000000000000f8 EndKey:7480000000000000ff6200000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:81 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/02 13:57:41.062 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[80]"]
   > [2024/07/02 13:57:41.062 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255969] [schemaVersion=64] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_d0c_g` DISABLE KEYS */;"] [user=root@%]
   > [2024/07/02 13:57:41.064 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255969] [schemaVersion=64] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_d0c_g` ENABLE KEYS */;"] [user=root@%]
   > [2024/07/02 13:57:42.077 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]

### Scenario 1
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
 * Instruction #1:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
 * Instruction #2:
     - Instruction:  select t_cp0sl.wkey as c0, t_cp0sl.pkey as c1, t_cp0sl.c_1_kgbc as c2, t_cp0sl....
     - Transaction: conn_0
     - Output: []
     - Executed order: 2
 * Instruction #3:
     - Instruction:  update t_cp0sl set wkey = 59 where t_cp0sl.c_1_kgbc not in ( select subq_0.c0 a...
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
 * Instruction #4:
     - Instruction:  select t_cp0sl.wkey as c0, t_cp0sl.pkey as c1, t_cp0sl.c_1_kgbc as c2, t_cp0sl....
     - Transaction: conn_0
     - Output: [(59, 15000, None, 75.37), (59, 16000, None, 100.57), (59, 17000, None, 34.89)]
     - Executed order: 4
 * Instruction #5:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 5

 * Container logs:
   > [2024/07/02 13:57:43.546 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/02 13:57:43.549 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255975] [schemaVersion=72] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/02 13:57:43.550 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:106, Type:drop schema, State:queueing, SchemaState:public, SchemaID:101, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:43.549 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/02 13:57:43.550 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:106, Type:drop schema, State:queueing, SchemaState:public, SchemaID:101, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:43.549 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/02 13:57:43.555 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:106, Type:drop schema, State:queueing, SchemaState:public, SchemaID:101, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:43.549 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:43.558 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=72] [neededSchemaVersion=73] ["start time"=97.709µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 13:57:43.560 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=73] ["take time"=2.216646ms] [job="ID:106, Type:drop schema, State:running, SchemaState:write only, SchemaID:101, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:43.549 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:43.562 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:106, Type:drop schema, State:running, SchemaState:write only, SchemaID:101, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:43.549 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:43.564 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=73] [neededSchemaVersion=74] ["start time"=70.122µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 13:57:43.567 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=74] ["take time"=2.763858ms] [job="ID:106, Type:drop schema, State:running, SchemaState:delete only, SchemaID:101, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:43.549 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:43.569 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:106, Type:drop schema, State:running, SchemaState:delete only, SchemaID:101, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:43.549 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:43.572 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=74] [neededSchemaVersion=75] ["start time"=64.464µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 13:57:43.574 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=75] ["take time"=2.261346ms] [job="ID:106, Type:drop schema, State:done, SchemaState:none, SchemaID:101, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:43.549 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:43.578 +00:00] [INFO] [delete_range.go:109] ["[ddl] add job into delete-range table"] [jobID=106] [jobType="drop schema"]
   > [2024/07/02 13:57:43.578 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:106, Type:drop schema, State:synced, SchemaState:none, SchemaID:101, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:43.549 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:43.581 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=106]
   > [2024/07/02 13:57:43.581 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/02 13:57:43.582 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255975] [schemaVersion=75] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/02 13:57:43.584 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:108, Type:create schema, State:queueing, SchemaState:none, SchemaID:107, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 13:57:43.583 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/02 13:57:43.585 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:108, Type:create schema, State:queueing, SchemaState:none, SchemaID:107, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 13:57:43.583 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/02 13:57:43.590 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:108, Type:create schema, State:queueing, SchemaState:none, SchemaID:107, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:43.583 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:43.593 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=75] [neededSchemaVersion=76] ["start time"=126.484µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 13:57:43.595 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=76] ["take time"=2.280412ms] [job="ID:108, Type:create schema, State:done, SchemaState:public, SchemaID:107, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 13:57:43.583 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:43.598 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:108, Type:create schema, State:synced, SchemaState:public, SchemaID:107, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:43.583 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:43.600 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=108]
   > [2024/07/02 13:57:43.600 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/02 13:57:43.606 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255975] [schemaVersion=76] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_cp0sl`\n--\n\nDROP TABLE IF EXISTS `t_cp0sl`;"] [user=root@%]
   > [2024/07/02 13:57:43.607 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255975] [schemaVersion=76] [cur_db=testdb] [sql="CREATE TABLE `t_cp0sl` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_1_kgbc` int(11) DEFAULT NULL,\n  `c_dw8ly` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_py61ed` (`wkey`,`pkey`,`c_1_kgbc`,`c_dw8ly`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/07/02 13:57:43.609 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:110, Type:create table, State:queueing, SchemaState:none, SchemaID:107, TableID:109, RowCount:0, ArgLen:1, start time: 2024-07-02 13:57:43.607 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/02 13:57:43.609 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:110, Type:create table, State:queueing, SchemaState:none, SchemaID:107, TableID:109, RowCount:0, ArgLen:1, start time: 2024-07-02 13:57:43.607 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_cp0sl` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_1_kgbc` int(11) DEFAULT NULL,\n  `c_dw8ly` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_py61ed` (`wkey`,`pkey`,`c_1_kgbc`,`c_dw8ly`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/02 13:57:43.615 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:110, Type:create table, State:queueing, SchemaState:none, SchemaID:107, TableID:109, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:43.607 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:43.619 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=76] [neededSchemaVersion=77] ["start time"=199.958µs] [phyTblIDs="[109]"] [actionTypes="[8]"]
   > [2024/07/02 13:57:43.620 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=77] ["take time"=2.056289ms] [job="ID:110, Type:create table, State:done, SchemaState:public, SchemaID:107, TableID:109, RowCount:0, ArgLen:1, start time: 2024-07-02 13:57:43.607 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:43.624 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:110, Type:create table, State:synced, SchemaState:public, SchemaID:107, TableID:109, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:43.607 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:43.627 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=110]
   > [2024/07/02 13:57:43.627 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/02 13:57:43.627 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=84] ["first split key"=74800000000000006d]
   > [2024/07/02 13:57:43.627 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=84] ["first at"=74800000000000006d] ["first new region left"="{Id:84 StartKey:7480000000000000ff6700000000000000f8 EndKey:7480000000000000ff6d00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:85 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/02 13:57:43.627 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[84]"]
   > [2024/07/02 13:57:43.628 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255975] [schemaVersion=77] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_cp0sl` DISABLE KEYS */;"] [user=root@%]
   > [2024/07/02 13:57:43.630 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255975] [schemaVersion=77] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_cp0sl` ENABLE KEYS */;"] [user=root@%]
   > [2024/07/02 13:57:43.630 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255975] [schemaVersion=77] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_d0c_g`\n--\n\nDROP TABLE IF EXISTS `t_d0c_g`;"] [user=root@%]
   > [2024/07/02 13:57:43.631 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255975] [schemaVersion=77] [cur_db=testdb] [sql="CREATE TABLE `t_d0c_g` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_p5i5kc` int(11) DEFAULT NULL,\n  `c_eephud` text DEFAULT NULL,\n  `c_dmlxnb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/07/02 13:57:43.634 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:112, Type:create table, State:queueing, SchemaState:none, SchemaID:107, TableID:111, RowCount:0, ArgLen:1, start time: 2024-07-02 13:57:43.632 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/02 13:57:43.634 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:112, Type:create table, State:queueing, SchemaState:none, SchemaID:107, TableID:111, RowCount:0, ArgLen:1, start time: 2024-07-02 13:57:43.632 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_d0c_g` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_p5i5kc` int(11) DEFAULT NULL,\n  `c_eephud` text DEFAULT NULL,\n  `c_dmlxnb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/02 13:57:43.640 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:112, Type:create table, State:queueing, SchemaState:none, SchemaID:107, TableID:111, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:43.632 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:43.645 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=77] [neededSchemaVersion=78] ["start time"=377.775µs] [phyTblIDs="[111]"] [actionTypes="[8]"]
   > [2024/07/02 13:57:43.646 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=78] ["take time"=2.087928ms] [job="ID:112, Type:create table, State:done, SchemaState:public, SchemaID:107, TableID:111, RowCount:0, ArgLen:1, start time: 2024-07-02 13:57:43.632 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:43.650 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:112, Type:create table, State:synced, SchemaState:public, SchemaID:107, TableID:111, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:43.632 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:43.653 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=112]
   > [2024/07/02 13:57:43.653 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/02 13:57:43.653 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=86] ["first split key"=74800000000000006f]
   > [2024/07/02 13:57:43.653 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=86] ["first at"=74800000000000006f] ["first new region left"="{Id:86 StartKey:7480000000000000ff6d00000000000000f8 EndKey:7480000000000000ff6f00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:87 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/02 13:57:43.653 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[86]"]
   > [2024/07/02 13:57:43.654 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255975] [schemaVersion=78] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_d0c_g` DISABLE KEYS */;"] [user=root@%]
   > [2024/07/02 13:57:43.656 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255975] [schemaVersion=78] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_d0c_g` ENABLE KEYS */;"] [user=root@%]
   > [2024/07/02 13:57:44.671 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/02 13:57:44.682 +00:00] [INFO] [set.go:149] ["set global var"] [conn=2199023255977] [name=tx_isolation] [val=READ-COMMITTED]
