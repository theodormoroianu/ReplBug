# Bug ID TIDB-39977-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/39977
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              Gets warnings when running in a transaction.


## Details
 * Database: tidb-v6.4.0
 * Number of scenarios: 2
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 0 / 0
 * Instruction #1:
     - Instruction:  BEGIN;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  DELETE FROM t;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 2 / 0
 * Instruction #3:
     - Instruction:  SELECT /*+ STREAM_AGG()*/c0 FROM t WHERE c1 FOR UPDATE; -- Warning
     - Transaction: conn_0
     - Output: []
     - Executed order: 3
     - Affected rows / Warnings: 0 / 2
 * Instruction #4:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows / Warnings: 0 / 0

 * Container logs:
   > [2024/07/10 13:46:12.264 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/10 13:46:12.267 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=2199023255969] [schemaVersion=57] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/10 13:46:12.271 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:91, Type:drop schema, State:queueing, SchemaState:public, SchemaID:86, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-10 13:46:12.269 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/10 13:46:12.272 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:91, Type:drop schema, State:queueing, SchemaState:public, SchemaID:86, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-10 13:46:12.269 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/10 13:46:12.279 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:91, Type:drop schema, State:queueing, SchemaState:public, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-10 13:46:12.269 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:12.282 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=57] [neededSchemaVersion=58] ["start time"=133.119µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/10 13:46:12.284 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=58] ["take time"=2.018785ms] [job="ID:91, Type:drop schema, State:running, SchemaState:write only, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-10 13:46:12.269 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:12.288 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:91, Type:drop schema, State:running, SchemaState:write only, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-10 13:46:12.269 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:12.290 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=58] [neededSchemaVersion=59] ["start time"=85.068µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/10 13:46:12.293 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=59] ["take time"=2.493851ms] [job="ID:91, Type:drop schema, State:running, SchemaState:delete only, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-10 13:46:12.269 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:12.297 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:91, Type:drop schema, State:running, SchemaState:delete only, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-10 13:46:12.269 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:12.300 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=59] [neededSchemaVersion=60] ["start time"=85.486µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/10 13:46:12.302 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=60] ["take time"=2.079198ms] [job="ID:91, Type:drop schema, State:done, SchemaState:none, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-10 13:46:12.269 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:12.308 +00:00] [INFO] [delete_range.go:109] ["[ddl] add job into delete-range table"] [jobID=91] [jobType="drop schema"]
   > [2024/07/10 13:46:12.308 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:91, Type:drop schema, State:synced, SchemaState:none, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-10 13:46:12.269 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:12.311 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=91]
   > [2024/07/10 13:46:12.311 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/10 13:46:12.312 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=2199023255969] [schemaVersion=60] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/10 13:46:12.316 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:93, Type:create schema, State:queueing, SchemaState:none, SchemaID:92, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-10 13:46:12.314 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/10 13:46:12.316 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:93, Type:create schema, State:queueing, SchemaState:none, SchemaID:92, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-10 13:46:12.314 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/10 13:46:12.325 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:93, Type:create schema, State:queueing, SchemaState:none, SchemaID:92, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-10 13:46:12.314 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:12.328 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=60] [neededSchemaVersion=61] ["start time"=195.697µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/10 13:46:12.330 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=61] ["take time"=2.030518ms] [job="ID:93, Type:create schema, State:done, SchemaState:public, SchemaID:92, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-10 13:46:12.314 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:12.335 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:93, Type:create schema, State:synced, SchemaState:public, SchemaID:92, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-10 13:46:12.314 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:12.337 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=93]
   > [2024/07/10 13:46:12.337 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/10 13:46:12.340 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=2199023255969] [schemaVersion=61] [cur_db=testdb] [sql="CREATE TABLE t(c0 DECIMAL, c1 BLOB(79));"] [user=root@%]
   > [2024/07/10 13:46:12.340 +00:00] [INFO] [ddl_api.go:1033] ["Automatically convert BLOB(79) to TINYBLOB"]
   > [2024/07/10 13:46:12.345 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:95, Type:create table, State:queueing, SchemaState:none, SchemaID:92, TableID:94, RowCount:0, ArgLen:2, start time: 2024-07-10 13:46:12.343 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/10 13:46:12.345 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:95, Type:create table, State:queueing, SchemaState:none, SchemaID:92, TableID:94, RowCount:0, ArgLen:2, start time: 2024-07-10 13:46:12.343 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE t(c0 DECIMAL, c1 BLOB(79));"]
   > [2024/07/10 13:46:12.352 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:95, Type:create table, State:queueing, SchemaState:none, SchemaID:92, TableID:94, RowCount:0, ArgLen:0, start time: 2024-07-10 13:46:12.343 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:12.356 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=61] [neededSchemaVersion=62] ["start time"=324.975µs] [phyTblIDs="[94]"] [actionTypes="[8]"]
   > [2024/07/10 13:46:12.357 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=62] ["take time"=2.026189ms] [job="ID:95, Type:create table, State:done, SchemaState:public, SchemaID:92, TableID:94, RowCount:0, ArgLen:2, start time: 2024-07-10 13:46:12.343 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:12.362 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:95, Type:create table, State:synced, SchemaState:public, SchemaID:92, TableID:94, RowCount:0, ArgLen:0, start time: 2024-07-10 13:46:12.343 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:12.364 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=95]
   > [2024/07/10 13:46:12.364 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/10 13:46:12.364 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=84] ["first split key"=74800000000000005e]
   > [2024/07/10 13:46:12.365 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=84] ["first at"=74800000000000005e] ["first new region left"="{Id:84 StartKey:7480000000000000ff5800000000000000f8 EndKey:7480000000000000ff5e00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:85 store_id:1 ] EncryptionMeta:<nil> IsInFlashback:false}"] ["new region count"=1]
   > [2024/07/10 13:46:12.365 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[84]"]
   > [2024/07/10 13:46:12.366 +00:00] [WARN] [2pc.go:1873] ["schemaLeaseChecker is not set for this transaction"] [sessionID=2199023255969] [startTS=451049992320450561] [checkTS=451049992320712705]
   > [2024/07/10 13:46:13.381 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/10 13:46:13.397 +00:00] [INFO] [set.go:141] ["set global var"] [conn=2199023255971] [name=tx_isolation] [val=READ-COMMITTED]

### Scenario 1
 * Instruction #0:
     - Instruction:  DELETE FROM t;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 2 / 0
 * Instruction #1:
     - Instruction:  SELECT /*+ STREAM_AGG()*/c0 FROM t WHERE c1 FOR UPDATE; -- Warning
     - Transaction: conn_0
     - Output: []
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0

 * Container logs:
   > [2024/07/10 13:46:15.517 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/10 13:46:15.520 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=2199023255975] [schemaVersion=70] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/10 13:46:15.523 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:102, Type:drop schema, State:queueing, SchemaState:public, SchemaID:97, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-10 13:46:15.522 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/10 13:46:15.523 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:102, Type:drop schema, State:queueing, SchemaState:public, SchemaID:97, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-10 13:46:15.522 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/10 13:46:15.529 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:102, Type:drop schema, State:queueing, SchemaState:public, SchemaID:97, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-10 13:46:15.522 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:15.532 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=70] [neededSchemaVersion=71] ["start time"=96.731µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/10 13:46:15.534 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=71] ["take time"=2.325531ms] [job="ID:102, Type:drop schema, State:running, SchemaState:write only, SchemaID:97, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-10 13:46:15.522 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:15.537 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:102, Type:drop schema, State:running, SchemaState:write only, SchemaID:97, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-10 13:46:15.522 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:15.539 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=71] [neededSchemaVersion=72] ["start time"=69.493µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/10 13:46:15.542 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=72] ["take time"=2.615865ms] [job="ID:102, Type:drop schema, State:running, SchemaState:delete only, SchemaID:97, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-10 13:46:15.522 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:15.546 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:102, Type:drop schema, State:running, SchemaState:delete only, SchemaID:97, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-10 13:46:15.522 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:15.549 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=72] [neededSchemaVersion=73] ["start time"=94.217µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/10 13:46:15.551 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=73] ["take time"=2.071656ms] [job="ID:102, Type:drop schema, State:done, SchemaState:none, SchemaID:97, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-10 13:46:15.522 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:15.554 +00:00] [INFO] [delete_range.go:109] ["[ddl] add job into delete-range table"] [jobID=102] [jobType="drop schema"]
   > [2024/07/10 13:46:15.554 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:102, Type:drop schema, State:synced, SchemaState:none, SchemaID:97, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-10 13:46:15.522 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:15.557 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=102]
   > [2024/07/10 13:46:15.557 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/10 13:46:15.558 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=2199023255975] [schemaVersion=73] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/10 13:46:15.562 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:104, Type:create schema, State:queueing, SchemaState:none, SchemaID:103, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-10 13:46:15.56 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/10 13:46:15.562 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:104, Type:create schema, State:queueing, SchemaState:none, SchemaID:103, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-10 13:46:15.56 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/10 13:46:15.569 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:104, Type:create schema, State:queueing, SchemaState:none, SchemaID:103, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-10 13:46:15.56 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:15.572 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=73] [neededSchemaVersion=74] ["start time"=133.119µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/10 13:46:15.574 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=74] ["take time"=2.486169ms] [job="ID:104, Type:create schema, State:done, SchemaState:public, SchemaID:103, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-10 13:46:15.56 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:15.577 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:104, Type:create schema, State:synced, SchemaState:public, SchemaID:103, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-10 13:46:15.56 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:15.579 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=104]
   > [2024/07/10 13:46:15.579 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/10 13:46:15.582 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=2199023255975] [schemaVersion=74] [cur_db=testdb] [sql="CREATE TABLE t(c0 DECIMAL, c1 BLOB(79));"] [user=root@%]
   > [2024/07/10 13:46:15.582 +00:00] [INFO] [ddl_api.go:1033] ["Automatically convert BLOB(79) to TINYBLOB"]
   > [2024/07/10 13:46:15.585 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:106, Type:create table, State:queueing, SchemaState:none, SchemaID:103, TableID:105, RowCount:0, ArgLen:2, start time: 2024-07-10 13:46:15.583 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/10 13:46:15.585 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:106, Type:create table, State:queueing, SchemaState:none, SchemaID:103, TableID:105, RowCount:0, ArgLen:2, start time: 2024-07-10 13:46:15.583 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE t(c0 DECIMAL, c1 BLOB(79));"]
   > [2024/07/10 13:46:15.593 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:106, Type:create table, State:queueing, SchemaState:none, SchemaID:103, TableID:105, RowCount:0, ArgLen:0, start time: 2024-07-10 13:46:15.583 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:15.596 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=74] [neededSchemaVersion=75] ["start time"=374.144µs] [phyTblIDs="[105]"] [actionTypes="[8]"]
   > [2024/07/10 13:46:15.598 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=75] ["take time"=2.226426ms] [job="ID:106, Type:create table, State:done, SchemaState:public, SchemaID:103, TableID:105, RowCount:0, ArgLen:2, start time: 2024-07-10 13:46:15.583 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:15.602 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:106, Type:create table, State:synced, SchemaState:public, SchemaID:103, TableID:105, RowCount:0, ArgLen:0, start time: 2024-07-10 13:46:15.583 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:15.605 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=106]
   > [2024/07/10 13:46:15.605 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/10 13:46:15.605 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=88] ["first split key"=748000000000000069]
   > [2024/07/10 13:46:15.605 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=88] ["first at"=748000000000000069] ["first new region left"="{Id:88 StartKey:7480000000000000ff6300000000000000f8 EndKey:7480000000000000ff6900000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:89 store_id:1 ] EncryptionMeta:<nil> IsInFlashback:false}"] ["new region count"=1]
   > [2024/07/10 13:46:15.605 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[88]"]
   > [2024/07/10 13:46:15.606 +00:00] [WARN] [2pc.go:1873] ["schemaLeaseChecker is not set for this transaction"] [sessionID=2199023255975] [startTS=451049993170059265] [checkTS=451049993170059266]
   > [2024/07/10 13:46:16.622 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
