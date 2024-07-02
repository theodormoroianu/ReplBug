# Bug ID TIDB-30361-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/30361
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              The two resulting tables are different.


## Details
 * Database: tidb-v5.4.0
 * Number of scenarios: 2
 * Initial setup script: Yes

## Results
### Scenario 0
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
   > [2024/07/02 12:41:41.335 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=21] [user=root] [host=]
   > [2024/07/02 12:41:41.339 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=21] [schemaVersion=51] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/07/02 12:41:41.339 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:78, Type:drop schema, State:none, SchemaState:queueing, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:41.339 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 12:41:41.339 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:78, Type:drop schema, State:none, SchemaState:queueing, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:41.339 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/02 12:41:41.340 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:78, Type:drop schema, State:none, SchemaState:queueing, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:41.339 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:41.341 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=51] [neededSchemaVersion=52] ["start time"=135.004µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 12:41:41.343 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=52] ["take time"=2.221257ms] [job="ID:78, Type:drop schema, State:running, SchemaState:write only, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:41.339 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:41.343 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:78, Type:drop schema, State:running, SchemaState:write only, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:41.339 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:41.344 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=52] [neededSchemaVersion=53] ["start time"=94.008µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 12:41:41.346 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=53] ["take time"=2.234876ms] [job="ID:78, Type:drop schema, State:running, SchemaState:delete only, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:41.339 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:41.346 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:78, Type:drop schema, State:running, SchemaState:delete only, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:41.339 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:41.347 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=53] [neededSchemaVersion=54] ["start time"=97.709µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 12:41:41.349 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=54] ["take time"=2.096939ms] [job="ID:78, Type:drop schema, State:done, SchemaState:queueing, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:41.339 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:41.350 +00:00] [INFO] [delete_range.go:107] ["[ddl] add job into delete-range table"] [jobID=78] [jobType="drop schema"]
   > [2024/07/02 12:41:41.350 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:78, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:41.339 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:41.351 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=78]
   > [2024/07/02 12:41:41.351 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 12:41:41.352 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=21] [schemaVersion=54] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/07/02 12:41:41.353 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:80, Type:create schema, State:none, SchemaState:queueing, SchemaID:79, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 12:41:41.352 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 12:41:41.353 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:80, Type:create schema, State:none, SchemaState:queueing, SchemaID:79, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 12:41:41.352 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/02 12:41:41.353 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:80, Type:create schema, State:none, SchemaState:queueing, SchemaID:79, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:41.352 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:41.355 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=54] [neededSchemaVersion=55] ["start time"=360.524µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 12:41:41.357 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=55] ["take time"=2.249055ms] [job="ID:80, Type:create schema, State:done, SchemaState:public, SchemaID:79, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 12:41:41.352 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:41.357 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:80, Type:create schema, State:synced, SchemaState:public, SchemaID:79, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:41.352 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:41.357 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=80]
   > [2024/07/02 12:41:41.357 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 12:41:41.361 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=21] [schemaVersion=55] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_q_zw9c`\n--\n\nDROP TABLE IF EXISTS `t_q_zw9c`;"] [user=root@127.0.0.1]
   > [2024/07/02 12:41:41.362 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=21] [schemaVersion=55] [cur_db=testdb] [sql="CREATE TABLE `t_q_zw9c` (\n  `c_qpjzzd` int(11) NOT NULL,\n  `c_1mp0eb` int(11) DEFAULT NULL,\n  `c_3dcuc` double DEFAULT NULL,\n  PRIMARY KEY (`c_qpjzzd`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/07/02 12:41:41.363 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:82, Type:create table, State:none, SchemaState:queueing, SchemaID:79, TableID:81, RowCount:0, ArgLen:1, start time: 2024-07-02 12:41:41.362 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 12:41:41.363 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:82, Type:create table, State:none, SchemaState:queueing, SchemaID:79, TableID:81, RowCount:0, ArgLen:1, start time: 2024-07-02 12:41:41.362 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_q_zw9c` (\n  `c_qpjzzd` int(11) NOT NULL,\n  `c_1mp0eb` int(11) DEFAULT NULL,\n  `c_3dcuc` double DEFAULT NULL,\n  PRIMARY KEY (`c_qpjzzd`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/02 12:41:41.364 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:82, Type:create table, State:none, SchemaState:queueing, SchemaID:79, TableID:81, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:41.362 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:41.366 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=55] [neededSchemaVersion=56] ["start time"=381.198µs] [phyTblIDs="[81]"] [actionTypes="[8]"]
   > [2024/07/02 12:41:41.367 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=56] ["take time"=2.26896ms] [job="ID:82, Type:create table, State:done, SchemaState:public, SchemaID:79, TableID:81, RowCount:0, ArgLen:1, start time: 2024-07-02 12:41:41.362 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:41.368 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:82, Type:create table, State:synced, SchemaState:public, SchemaID:79, TableID:81, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:41.362 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:41.369 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=82]
   > [2024/07/02 12:41:41.369 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 12:41:41.369 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=62] ["first split key"=748000000000000051]
   > [2024/07/02 12:41:41.370 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=62] ["first at"=748000000000000051] ["first new region left"="{Id:62 StartKey:7480000000000000ff4b00000000000000f8 EndKey:7480000000000000ff5100000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:63 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/02 12:41:41.370 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[62]"]
   > [2024/07/02 12:41:41.370 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=21] [schemaVersion=56] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_q_zw9c` DISABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/07/02 12:41:41.371 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=21] [schemaVersion=56] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_q_zw9c` ENABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/07/02 12:41:42.481 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=23] [user=root] [host=]
   > [2024/07/02 12:41:42.500 +00:00] [INFO] [set.go:139] ["set global var"] [conn=23] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/07/02 12:41:43.081 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=25] [user=root] [host=]

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
   > [2024/07/02 12:41:46.364 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=29] [user=root] [host=]
   > [2024/07/02 12:41:46.367 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=29] [schemaVersion=64] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/07/02 12:41:46.368 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:89, Type:drop schema, State:none, SchemaState:queueing, SchemaID:84, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:46.367 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 12:41:46.368 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:89, Type:drop schema, State:none, SchemaState:queueing, SchemaID:84, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:46.367 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/02 12:41:46.369 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:89, Type:drop schema, State:none, SchemaState:queueing, SchemaID:84, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:46.367 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:46.370 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=64] [neededSchemaVersion=65] ["start time"=161.335µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 12:41:46.372 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=65] ["take time"=2.283627ms] [job="ID:89, Type:drop schema, State:running, SchemaState:write only, SchemaID:84, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:46.367 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:46.372 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:89, Type:drop schema, State:running, SchemaState:write only, SchemaID:84, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:46.367 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:46.373 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=65] [neededSchemaVersion=66] ["start time"=60.483µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 12:41:46.375 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=66] ["take time"=2.380637ms] [job="ID:89, Type:drop schema, State:running, SchemaState:delete only, SchemaID:84, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:46.367 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:46.375 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:89, Type:drop schema, State:running, SchemaState:delete only, SchemaID:84, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:46.367 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:46.376 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=66] [neededSchemaVersion=67] ["start time"=77.594µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 12:41:46.378 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=67] ["take time"=2.346345ms] [job="ID:89, Type:drop schema, State:done, SchemaState:queueing, SchemaID:84, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:46.367 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:46.378 +00:00] [INFO] [delete_range.go:107] ["[ddl] add job into delete-range table"] [jobID=89] [jobType="drop schema"]
   > [2024/07/02 12:41:46.379 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:89, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:84, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:46.367 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:46.379 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=89]
   > [2024/07/02 12:41:46.379 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 12:41:46.380 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=29] [schemaVersion=67] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/07/02 12:41:46.381 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:91, Type:create schema, State:none, SchemaState:queueing, SchemaID:90, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 12:41:46.381 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 12:41:46.381 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:91, Type:create schema, State:none, SchemaState:queueing, SchemaID:90, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 12:41:46.381 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/02 12:41:46.382 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:91, Type:create schema, State:none, SchemaState:queueing, SchemaID:90, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:46.381 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:46.383 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=67] [neededSchemaVersion=68] ["start time"=88.978µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 12:41:46.385 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=68] ["take time"=2.235575ms] [job="ID:91, Type:create schema, State:done, SchemaState:public, SchemaID:90, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 12:41:46.381 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:46.385 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:91, Type:create schema, State:synced, SchemaState:public, SchemaID:90, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:46.381 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:46.386 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=91]
   > [2024/07/02 12:41:46.386 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 12:41:46.390 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=29] [schemaVersion=68] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_q_zw9c`\n--\n\nDROP TABLE IF EXISTS `t_q_zw9c`;"] [user=root@127.0.0.1]
   > [2024/07/02 12:41:46.391 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=29] [schemaVersion=68] [cur_db=testdb] [sql="CREATE TABLE `t_q_zw9c` (\n  `c_qpjzzd` int(11) NOT NULL,\n  `c_1mp0eb` int(11) DEFAULT NULL,\n  `c_3dcuc` double DEFAULT NULL,\n  PRIMARY KEY (`c_qpjzzd`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/07/02 12:41:46.392 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:93, Type:create table, State:none, SchemaState:queueing, SchemaID:90, TableID:92, RowCount:0, ArgLen:1, start time: 2024-07-02 12:41:46.391 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 12:41:46.392 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:93, Type:create table, State:none, SchemaState:queueing, SchemaID:90, TableID:92, RowCount:0, ArgLen:1, start time: 2024-07-02 12:41:46.391 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_q_zw9c` (\n  `c_qpjzzd` int(11) NOT NULL,\n  `c_1mp0eb` int(11) DEFAULT NULL,\n  `c_3dcuc` double DEFAULT NULL,\n  PRIMARY KEY (`c_qpjzzd`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/02 12:41:46.392 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:93, Type:create table, State:none, SchemaState:queueing, SchemaID:90, TableID:92, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:46.391 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:46.394 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=68] [neededSchemaVersion=69] ["start time"=259.603µs] [phyTblIDs="[92]"] [actionTypes="[8]"]
   > [2024/07/02 12:41:46.396 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=69] ["take time"=2.245912ms] [job="ID:93, Type:create table, State:done, SchemaState:public, SchemaID:90, TableID:92, RowCount:0, ArgLen:1, start time: 2024-07-02 12:41:46.391 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:46.396 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:93, Type:create table, State:synced, SchemaState:public, SchemaID:90, TableID:92, RowCount:0, ArgLen:0, start time: 2024-07-02 12:41:46.391 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:41:46.397 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=93]
   > [2024/07/02 12:41:46.397 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/02 12:41:46.397 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=66] ["first split key"=74800000000000005c]
   > [2024/07/02 12:41:46.398 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=66] ["first at"=74800000000000005c] ["first new region left"="{Id:66 StartKey:7480000000000000ff5600000000000000f8 EndKey:7480000000000000ff5c00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:67 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/02 12:41:46.398 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[66]"]
   > [2024/07/02 12:41:46.398 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=29] [schemaVersion=69] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_q_zw9c` DISABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/07/02 12:41:46.399 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=29] [schemaVersion=69] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_q_zw9c` ENABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/07/02 12:41:47.504 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=31] [user=root] [host=]
   > [2024/07/02 12:41:47.523 +00:00] [INFO] [set.go:139] ["set global var"] [conn=31] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/07/02 12:41:48.120 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=33] [user=root] [host=]
