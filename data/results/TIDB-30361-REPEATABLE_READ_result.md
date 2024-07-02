# Bug ID TIDB-30361-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/30361
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              The two resulting tables are different.


## Details
 * Database: tidb-v5.4.0
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
     - Instruction:  start transaction;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
 * Instruction #2:
     - Instruction:  start transaction;
     - Transaction: conn_1
     - Output: None
     - Executed order: 2
 * Instruction #3:
     - Instruction:  select ref_14.c_qpjzzd as c1 from t_q_zw9c as ref_14 order by c1 desc;
     - Transaction: conn_0
     - Output: [(0,)]
     - Executed order: 3
 * Instruction #4:
     - Instruction:  delete from t_q_zw9c;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
 * Instruction #5:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: None
     - Executed order: 5
 * Instruction #6:
     - Instruction:  select ref_14.c_qpjzzd as c1 from t_q_zw9c as ref_14 order by c1 desc;
     - Transaction: conn_1
     - Output: []
     - Executed order: 6
 * Instruction #7:
     - Instruction:  commit;
     - Transaction: conn_1
     - Output: None
     - Executed order: 7

 * Container logs:
   > [2024/07/02 12:41:31.460 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=5] [user=root] [host=]
   > [2024/07/02 12:41:31.462 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=28] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/07/02 12:41:31.462 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=28] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/07/02 12:41:31.463 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:58, Type:create schema, State:none, SchemaState:queueing, SchemaID:57, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 12:41:31.463 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 12:41:31.463 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:58, Type:create schema, State:none, SchemaState:queueing, SchemaID:57, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 12:41:31.463 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/02 12:41:31.464 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:58, Type:create schema, State:none, SchemaState:queueing, SchemaID:57, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:31.463 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:31.464 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=28] [neededSchemaVersion=29] ["start time"=72.426µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 12:41:31.466 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=29] ["take time"=2.256458ms] [job="ID:58, Type:create schema, State:done, SchemaState:public, SchemaID:57, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 12:41:31.463 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:31.467 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:58, Type:create schema, State:synced, SchemaState:public, SchemaID:57, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:31.463 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:31.468 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=58]
   > [2024/07/02 12:41:31.468 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 12:41:31.480 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=29] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_q_zw9c`\n--\n\nDROP TABLE IF EXISTS `t_q_zw9c`;"] [user=root@127.0.0.1]
   > [2024/07/02 12:41:31.481 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=29] [cur_db=testdb] [sql="CREATE TABLE `t_q_zw9c` (\n  `c_qpjzzd` int(11) NOT NULL,\n  `c_1mp0eb` int(11) DEFAULT NULL,\n  `c_3dcuc` double DEFAULT NULL,\n  PRIMARY KEY (`c_qpjzzd`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/07/02 12:41:31.483 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:60, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:59, RowCount:0, ArgLen:1, start time: 2024-07-02 12:41:31.482 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 12:41:31.483 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:60, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:59, RowCount:0, ArgLen:1, start time: 2024-07-02 12:41:31.482 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_q_zw9c` (\n  `c_qpjzzd` int(11) NOT NULL,\n  `c_1mp0eb` int(11) DEFAULT NULL,\n  `c_3dcuc` double DEFAULT NULL,\n  PRIMARY KEY (`c_qpjzzd`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/02 12:41:31.484 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:60, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:59, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:31.482 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:31.486 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=29] [neededSchemaVersion=30] ["start time"=341.807µs] [phyTblIDs="[59]"] [actionTypes="[8]"]
   > [2024/07/02 12:41:31.487 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=30] ["take time"=2.084437ms] [job="ID:60, Type:create table, State:done, SchemaState:public, SchemaID:57, TableID:59, RowCount:0, ArgLen:1, start time: 2024-07-02 12:41:31.482 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:31.488 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:60, Type:create table, State:synced, SchemaState:public, SchemaID:57, TableID:59, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:31.482 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:31.489 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=60]
   > [2024/07/02 12:41:31.489 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 12:41:31.489 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=52] ["first split key"=74800000000000003b]
   > [2024/07/02 12:41:31.490 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=30] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_q_zw9c` DISABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/07/02 12:41:31.491 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=30] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_q_zw9c` ENABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/07/02 12:41:31.492 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=54] ["first at"=74800000000000003b] ["first new region left"="{Id:54 StartKey:7480000000000000ff3700000000000000f8 EndKey:7480000000000000ff3b00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:55 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/02 12:41:31.492 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[54]"]
   > [2024/07/02 12:41:32.585 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=7] [user=root] [host=]
   > [2024/07/02 12:41:32.602 +00:00] [INFO] [set.go:139] ["set global var"] [conn=7] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/07/02 12:41:33.192 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=9] [user=root] [host=]

### Scenario 1
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
 * Instruction #1:
     - Instruction:  start transaction;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
 * Instruction #2:
     - Instruction:  start transaction;
     - Transaction: conn_1
     - Output: None
     - Executed order: 2
 * Instruction #3:
     - Instruction:  select ref_14.c_qpjzzd as c1 from t_q_zw9c as ref_14;
     - Transaction: conn_0
     - Output: [(0,)]
     - Executed order: 3
 * Instruction #4:
     - Instruction:  delete from t_q_zw9c;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
 * Instruction #5:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: None
     - Executed order: 5
 * Instruction #6:
     - Instruction:  select ref_14.c_qpjzzd as c1 from t_q_zw9c as ref_14;
     - Transaction: conn_1
     - Output: [(0,)]
     - Executed order: 6
 * Instruction #7:
     - Instruction:  commit;
     - Transaction: conn_1
     - Output: None
     - Executed order: 7

 * Container logs:
   > [2024/07/02 12:41:36.347 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=13] [user=root] [host=]
   > [2024/07/02 12:41:36.349 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=13] [schemaVersion=38] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/07/02 12:41:36.350 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:67, Type:drop schema, State:none, SchemaState:queueing, SchemaID:62, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:36.349 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 12:41:36.350 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:67, Type:drop schema, State:none, SchemaState:queueing, SchemaID:62, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:36.349 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/02 12:41:36.350 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:drop schema, State:none, SchemaState:queueing, SchemaID:62, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:36.349 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:36.351 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=38] [neededSchemaVersion=39] ["start time"=50.356µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 12:41:36.353 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=39] ["take time"=2.227264ms] [job="ID:67, Type:drop schema, State:running, SchemaState:write only, SchemaID:62, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:36.349 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:36.353 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:drop schema, State:running, SchemaState:write only, SchemaID:62, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:36.349 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:36.354 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=39] [neededSchemaVersion=40] ["start time"=52.521µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 12:41:36.356 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=40] ["take time"=2.393907ms] [job="ID:67, Type:drop schema, State:running, SchemaState:delete only, SchemaID:62, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:36.349 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:36.357 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:drop schema, State:running, SchemaState:delete only, SchemaID:62, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:36.349 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:36.357 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=40] [neededSchemaVersion=41] ["start time"=66.28µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 12:41:36.360 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=41] ["take time"=2.447825ms] [job="ID:67, Type:drop schema, State:done, SchemaState:queueing, SchemaID:62, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:36.349 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:36.360 +00:00] [INFO] [delete_range.go:107] ["[ddl] add job into delete-range table"] [jobID=67] [jobType="drop schema"]
   > [2024/07/02 12:41:36.360 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:62, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:36.349 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:36.361 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=67]
   > [2024/07/02 12:41:36.361 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 12:41:36.362 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=13] [schemaVersion=41] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/07/02 12:41:36.363 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:69, Type:create schema, State:none, SchemaState:queueing, SchemaID:68, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 12:41:36.363 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 12:41:36.363 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:69, Type:create schema, State:none, SchemaState:queueing, SchemaID:68, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 12:41:36.363 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/02 12:41:36.363 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:69, Type:create schema, State:none, SchemaState:queueing, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:36.363 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:36.364 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=41] [neededSchemaVersion=42] ["start time"=125.437µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 12:41:36.366 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=42] ["take time"=2.195975ms] [job="ID:69, Type:create schema, State:done, SchemaState:public, SchemaID:68, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 12:41:36.363 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:36.367 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:69, Type:create schema, State:synced, SchemaState:public, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:36.363 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:36.367 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=69]
   > [2024/07/02 12:41:36.367 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 12:41:36.370 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=13] [schemaVersion=42] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_q_zw9c`\n--\n\nDROP TABLE IF EXISTS `t_q_zw9c`;"] [user=root@127.0.0.1]
   > [2024/07/02 12:41:36.370 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=13] [schemaVersion=42] [cur_db=testdb] [sql="CREATE TABLE `t_q_zw9c` (\n  `c_qpjzzd` int(11) NOT NULL,\n  `c_1mp0eb` int(11) DEFAULT NULL,\n  `c_3dcuc` double DEFAULT NULL,\n  PRIMARY KEY (`c_qpjzzd`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/07/02 12:41:36.372 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:71, Type:create table, State:none, SchemaState:queueing, SchemaID:68, TableID:70, RowCount:0, ArgLen:1, start time: 2024-07-02 12:41:36.371 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 12:41:36.372 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:71, Type:create table, State:none, SchemaState:queueing, SchemaID:68, TableID:70, RowCount:0, ArgLen:1, start time: 2024-07-02 12:41:36.371 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_q_zw9c` (\n  `c_qpjzzd` int(11) NOT NULL,\n  `c_1mp0eb` int(11) DEFAULT NULL,\n  `c_3dcuc` double DEFAULT NULL,\n  PRIMARY KEY (`c_qpjzzd`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/02 12:41:36.373 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:71, Type:create table, State:none, SchemaState:queueing, SchemaID:68, TableID:70, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:36.371 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:36.375 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=42] [neededSchemaVersion=43] ["start time"=399.846µs] [phyTblIDs="[70]"] [actionTypes="[8]"]
   > [2024/07/02 12:41:36.376 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=43] ["take time"=2.243957ms] [job="ID:71, Type:create table, State:done, SchemaState:public, SchemaID:68, TableID:70, RowCount:0, ArgLen:1, start time: 2024-07-02 12:41:36.371 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:36.377 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:71, Type:create table, State:synced, SchemaState:public, SchemaID:68, TableID:70, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:36.371 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:36.378 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=71]
   > [2024/07/02 12:41:36.378 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 12:41:36.378 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=58] ["first split key"=748000000000000046]
   > [2024/07/02 12:41:36.379 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=13] [schemaVersion=43] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_q_zw9c` DISABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/07/02 12:41:36.379 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=58] ["first at"=748000000000000046] ["first new region left"="{Id:58 StartKey:7480000000000000ff4000000000000000f8 EndKey:7480000000000000ff4600000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:59 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/02 12:41:36.379 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[58]"]
   > [2024/07/02 12:41:36.379 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=13] [schemaVersion=43] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_q_zw9c` ENABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/07/02 12:41:37.487 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=15] [user=root] [host=]
   > [2024/07/02 12:41:37.508 +00:00] [INFO] [set.go:139] ["set global var"] [conn=15] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/07/02 12:41:38.103 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=17] [user=root] [host=]
