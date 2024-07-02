# Bug ID TIDB-38150-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/38150
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
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
   > [2024/07/02 13:57:33.342 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/02 13:57:33.345 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255957] [schemaVersion=33] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/02 13:57:33.346 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255957] [schemaVersion=33] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/02 13:57:33.347 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:69, Type:create schema, State:queueing, SchemaState:none, SchemaID:68, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 13:57:33.346 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/02 13:57:33.348 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:69, Type:create schema, State:queueing, SchemaState:none, SchemaID:68, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 13:57:33.346 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/02 13:57:34.054 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:69, Type:create schema, State:queueing, SchemaState:none, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:33.346 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:34.057 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=33] [neededSchemaVersion=34] ["start time"=203.73µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 13:57:34.059 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=34] ["take time"=2.443424ms] [job="ID:69, Type:create schema, State:done, SchemaState:public, SchemaID:68, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 13:57:33.346 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:34.065 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:69, Type:create schema, State:synced, SchemaState:public, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:33.346 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:34.067 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=69]
   > [2024/07/02 13:57:34.067 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/02 13:57:34.074 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255957] [schemaVersion=34] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_cp0sl`\n--\n\nDROP TABLE IF EXISTS `t_cp0sl`;"] [user=root@%]
   > [2024/07/02 13:57:34.075 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255957] [schemaVersion=34] [cur_db=testdb] [sql="CREATE TABLE `t_cp0sl` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_1_kgbc` int(11) DEFAULT NULL,\n  `c_dw8ly` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_py61ed` (`wkey`,`pkey`,`c_1_kgbc`,`c_dw8ly`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/07/02 13:57:34.078 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:71, Type:create table, State:queueing, SchemaState:none, SchemaID:68, TableID:70, RowCount:0, ArgLen:1, start time: 2024-07-02 13:57:34.076 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/02 13:57:34.078 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:71, Type:create table, State:queueing, SchemaState:none, SchemaID:68, TableID:70, RowCount:0, ArgLen:1, start time: 2024-07-02 13:57:34.076 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_cp0sl` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_1_kgbc` int(11) DEFAULT NULL,\n  `c_dw8ly` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_py61ed` (`wkey`,`pkey`,`c_1_kgbc`,`c_dw8ly`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/02 13:57:34.085 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:71, Type:create table, State:queueing, SchemaState:none, SchemaID:68, TableID:70, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:34.076 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:34.089 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=34] [neededSchemaVersion=35] ["start time"=431.903µs] [phyTblIDs="[70]"] [actionTypes="[8]"]
   > [2024/07/02 13:57:34.091 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=35] ["take time"=2.198837ms] [job="ID:71, Type:create table, State:done, SchemaState:public, SchemaID:68, TableID:70, RowCount:0, ArgLen:1, start time: 2024-07-02 13:57:34.076 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:34.095 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:71, Type:create table, State:synced, SchemaState:public, SchemaID:68, TableID:70, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:34.076 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:34.098 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=71]
   > [2024/07/02 13:57:34.098 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/02 13:57:34.098 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=66] ["first split key"=748000000000000046]
   > [2024/07/02 13:57:34.098 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=66] ["first at"=748000000000000046] ["first new region left"="{Id:66 StartKey:7480000000000000ff4200000000000000f8 EndKey:7480000000000000ff4600000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:67 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/02 13:57:34.098 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[66]"]
   > [2024/07/02 13:57:34.098 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255957] [schemaVersion=35] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_cp0sl` DISABLE KEYS */;"] [user=root@%]
   > [2024/07/02 13:57:34.099 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255957] [schemaVersion=35] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_cp0sl` ENABLE KEYS */;"] [user=root@%]
   > [2024/07/02 13:57:34.100 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255957] [schemaVersion=35] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_d0c_g`\n--\n\nDROP TABLE IF EXISTS `t_d0c_g`;"] [user=root@%]
   > [2024/07/02 13:57:34.100 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255957] [schemaVersion=35] [cur_db=testdb] [sql="CREATE TABLE `t_d0c_g` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_p5i5kc` int(11) DEFAULT NULL,\n  `c_eephud` text DEFAULT NULL,\n  `c_dmlxnb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/07/02 13:57:34.101 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:73, Type:create table, State:queueing, SchemaState:none, SchemaID:68, TableID:72, RowCount:0, ArgLen:1, start time: 2024-07-02 13:57:34.101 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/02 13:57:34.102 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:73, Type:create table, State:queueing, SchemaState:none, SchemaID:68, TableID:72, RowCount:0, ArgLen:1, start time: 2024-07-02 13:57:34.101 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_d0c_g` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_p5i5kc` int(11) DEFAULT NULL,\n  `c_eephud` text DEFAULT NULL,\n  `c_dmlxnb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/02 13:57:34.108 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:73, Type:create table, State:queueing, SchemaState:none, SchemaID:68, TableID:72, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:34.101 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:34.113 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=35] [neededSchemaVersion=36] ["start time"=507.612µs] [phyTblIDs="[72]"] [actionTypes="[8]"]
   > [2024/07/02 13:57:34.114 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=36] ["take time"=2.229288ms] [job="ID:73, Type:create table, State:done, SchemaState:public, SchemaID:68, TableID:72, RowCount:0, ArgLen:1, start time: 2024-07-02 13:57:34.101 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:34.118 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:73, Type:create table, State:synced, SchemaState:public, SchemaID:68, TableID:72, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:34.101 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:34.121 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=73]
   > [2024/07/02 13:57:34.121 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/02 13:57:34.121 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=68] ["first split key"=748000000000000048]
   > [2024/07/02 13:57:34.122 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=68] ["first at"=748000000000000048] ["first new region left"="{Id:68 StartKey:7480000000000000ff4600000000000000f8 EndKey:7480000000000000ff4800000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:69 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/02 13:57:34.122 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[68]"]
   > [2024/07/02 13:57:34.122 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255957] [schemaVersion=36] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_d0c_g` DISABLE KEYS */;"] [user=root@%]
   > [2024/07/02 13:57:34.125 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255957] [schemaVersion=36] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_d0c_g` ENABLE KEYS */;"] [user=root@%]
   > [2024/07/02 13:57:35.139 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]

### Scenario 1
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
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
   > [2024/07/02 13:57:37.502 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/02 13:57:37.505 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255963] [schemaVersion=44] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/02 13:57:37.507 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:80, Type:drop schema, State:queueing, SchemaState:public, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:37.505 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/02 13:57:37.507 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:80, Type:drop schema, State:queueing, SchemaState:public, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:37.505 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/02 13:57:37.512 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:80, Type:drop schema, State:queueing, SchemaState:public, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:37.505 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:37.514 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=44] [neededSchemaVersion=45] ["start time"=74.731µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 13:57:37.516 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=45] ["take time"=2.222303ms] [job="ID:80, Type:drop schema, State:running, SchemaState:write only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:37.505 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:37.519 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:80, Type:drop schema, State:running, SchemaState:write only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:37.505 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:37.522 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=45] [neededSchemaVersion=46] ["start time"=68.725µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 13:57:37.524 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=46] ["take time"=2.284812ms] [job="ID:80, Type:drop schema, State:running, SchemaState:delete only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:37.505 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:37.527 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:80, Type:drop schema, State:running, SchemaState:delete only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:37.505 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:37.529 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=46] [neededSchemaVersion=47] ["start time"=68.236µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 13:57:37.531 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=47] ["take time"=2.282159ms] [job="ID:80, Type:drop schema, State:done, SchemaState:none, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:37.505 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:37.534 +00:00] [INFO] [delete_range.go:109] ["[ddl] add job into delete-range table"] [jobID=80] [jobType="drop schema"]
   > [2024/07/02 13:57:37.535 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:80, Type:drop schema, State:synced, SchemaState:none, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:37.505 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:37.546 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=80]
   > [2024/07/02 13:57:37.546 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/02 13:57:37.548 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255963] [schemaVersion=47] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/02 13:57:37.550 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:82, Type:create schema, State:queueing, SchemaState:none, SchemaID:81, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 13:57:37.548 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/02 13:57:37.550 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:82, Type:create schema, State:queueing, SchemaState:none, SchemaID:81, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 13:57:37.548 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/02 13:57:37.557 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:82, Type:create schema, State:queueing, SchemaState:none, SchemaID:81, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:37.548 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:37.559 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=47] [neededSchemaVersion=48] ["start time"=92.54µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 13:57:37.561 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=48] ["take time"=2.260926ms] [job="ID:82, Type:create schema, State:done, SchemaState:public, SchemaID:81, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 13:57:37.548 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:37.565 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:82, Type:create schema, State:synced, SchemaState:public, SchemaID:81, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:37.548 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:37.567 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=82]
   > [2024/07/02 13:57:37.567 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/02 13:57:37.572 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255963] [schemaVersion=48] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_cp0sl`\n--\n\nDROP TABLE IF EXISTS `t_cp0sl`;"] [user=root@%]
   > [2024/07/02 13:57:37.573 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255963] [schemaVersion=48] [cur_db=testdb] [sql="CREATE TABLE `t_cp0sl` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_1_kgbc` int(11) DEFAULT NULL,\n  `c_dw8ly` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_py61ed` (`wkey`,`pkey`,`c_1_kgbc`,`c_dw8ly`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/07/02 13:57:37.576 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:84, Type:create table, State:queueing, SchemaState:none, SchemaID:81, TableID:83, RowCount:0, ArgLen:1, start time: 2024-07-02 13:57:37.574 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/02 13:57:37.576 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:84, Type:create table, State:queueing, SchemaState:none, SchemaID:81, TableID:83, RowCount:0, ArgLen:1, start time: 2024-07-02 13:57:37.574 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_cp0sl` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_1_kgbc` int(11) DEFAULT NULL,\n  `c_dw8ly` double DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,\n  KEY `t_py61ed` (`wkey`,`pkey`,`c_1_kgbc`,`c_dw8ly`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/02 13:57:37.582 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:84, Type:create table, State:queueing, SchemaState:none, SchemaID:81, TableID:83, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:37.574 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:37.586 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=48] [neededSchemaVersion=49] ["start time"=406.899µs] [phyTblIDs="[83]"] [actionTypes="[8]"]
   > [2024/07/02 13:57:37.588 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=49] ["take time"=2.111115ms] [job="ID:84, Type:create table, State:done, SchemaState:public, SchemaID:81, TableID:83, RowCount:0, ArgLen:1, start time: 2024-07-02 13:57:37.574 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:37.592 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:84, Type:create table, State:synced, SchemaState:public, SchemaID:81, TableID:83, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:37.574 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:37.594 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=84]
   > [2024/07/02 13:57:37.595 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/02 13:57:37.595 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=72] ["first split key"=748000000000000053]
   > [2024/07/02 13:57:37.595 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=72] ["first at"=748000000000000053] ["first new region left"="{Id:72 StartKey:7480000000000000ff4d00000000000000f8 EndKey:7480000000000000ff5300000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:73 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/02 13:57:37.595 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[72]"]
   > [2024/07/02 13:57:37.596 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255963] [schemaVersion=49] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_cp0sl` DISABLE KEYS */;"] [user=root@%]
   > [2024/07/02 13:57:37.597 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255963] [schemaVersion=49] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_cp0sl` ENABLE KEYS */;"] [user=root@%]
   > [2024/07/02 13:57:37.598 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255963] [schemaVersion=49] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_d0c_g`\n--\n\nDROP TABLE IF EXISTS `t_d0c_g`;"] [user=root@%]
   > [2024/07/02 13:57:37.599 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255963] [schemaVersion=49] [cur_db=testdb] [sql="CREATE TABLE `t_d0c_g` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_p5i5kc` int(11) DEFAULT NULL,\n  `c_eephud` text DEFAULT NULL,\n  `c_dmlxnb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@%]
   > [2024/07/02 13:57:37.602 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:86, Type:create table, State:queueing, SchemaState:none, SchemaID:81, TableID:85, RowCount:0, ArgLen:1, start time: 2024-07-02 13:57:37.6 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/02 13:57:37.602 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:86, Type:create table, State:queueing, SchemaState:none, SchemaID:81, TableID:85, RowCount:0, ArgLen:1, start time: 2024-07-02 13:57:37.6 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_d0c_g` (\n  `wkey` int(11) DEFAULT NULL,\n  `pkey` int(11) NOT NULL,\n  `c_p5i5kc` int(11) DEFAULT NULL,\n  `c_eephud` text DEFAULT NULL,\n  `c_dmlxnb` text DEFAULT NULL,\n  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/02 13:57:37.608 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:86, Type:create table, State:queueing, SchemaState:none, SchemaID:81, TableID:85, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:37.6 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:37.612 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=49] [neededSchemaVersion=50] ["start time"=425.757µs] [phyTblIDs="[85]"] [actionTypes="[8]"]
   > [2024/07/02 13:57:37.613 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=50] ["take time"=2.070677ms] [job="ID:86, Type:create table, State:done, SchemaState:public, SchemaID:81, TableID:85, RowCount:0, ArgLen:1, start time: 2024-07-02 13:57:37.6 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:37.617 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:86, Type:create table, State:synced, SchemaState:public, SchemaID:81, TableID:85, RowCount:0, ArgLen:0, start time: 2024-07-02 13:57:37.6 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 13:57:37.619 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=86]
   > [2024/07/02 13:57:37.619 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/02 13:57:37.619 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=74] ["first split key"=748000000000000055]
   > [2024/07/02 13:57:37.620 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=74] ["first at"=748000000000000055] ["first new region left"="{Id:74 StartKey:7480000000000000ff5300000000000000f8 EndKey:7480000000000000ff5500000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:75 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/02 13:57:37.620 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[74]"]
   > [2024/07/02 13:57:37.620 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255963] [schemaVersion=50] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_d0c_g` DISABLE KEYS */;"] [user=root@%]
   > [2024/07/02 13:57:37.622 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255963] [schemaVersion=50] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_d0c_g` ENABLE KEYS */;"] [user=root@%]
   > [2024/07/02 13:57:38.635 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/02 13:57:38.647 +00:00] [INFO] [set.go:149] ["set global var"] [conn=2199023255965] [name=tx_isolation] [val=REPEATABLE-READ]
