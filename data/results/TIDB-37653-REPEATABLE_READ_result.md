# Bug ID TIDB-37653-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/37653
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              TiDB locks the record which is filtered by the non-index condition


## Details
 * Database: tidb-v6.2.0
 * Number of scenarios: 1
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 0 / 0
 * Instruction #1:
     - Instruction:  begin pessimistic;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  select * from t1 where id1 = 1 and id2 = 2 for update;
     - Transaction: conn_0
     - Output: []
     - Executed order: 2
     - Affected rows / Warnings: 0 / 0
 * Instruction #3:
     - Instruction:  begin pessimistic;
     - Transaction: conn_1
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 0 / 0
 * Instruction #4:
     - Instruction:  select * from t1 where id1 = 1 for update;
     - Transaction: conn_1
     - Output: [(1, 1, 1)]
     - Executed order: 5
     - Affected rows / Warnings: 1 / 0
 * Instruction #5:
     - Instruction:  commit;
     - Transaction: conn_1
     - Output: None
     - Executed order: 6
     - Affected rows / Warnings: 0 / 0
 * Instruction #6:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows / Warnings: 0 / 0

 * Container logs:
   > [2024/07/23 16:08:56.347 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/07/23 16:08:56.349 +00:00] [INFO] [session.go:3224] ["CRUCIAL OPERATION"] [conn=2199023255957] [schemaVersion=33] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/23 16:08:56.349 +00:00] [INFO] [session.go:3224] ["CRUCIAL OPERATION"] [conn=2199023255957] [schemaVersion=33] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/23 16:08:56.351 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:69, Type:create schema, State:queueing, SchemaState:none, SchemaID:68, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 16:08:56.35 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/23 16:08:56.351 +00:00] [INFO] [ddl.go:928] ["[ddl] start DDL job"] [job="ID:69, Type:create schema, State:queueing, SchemaState:none, SchemaID:68, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 16:08:56.35 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/23 16:08:56.357 +00:00] [INFO] [ddl_worker.go:1084] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:69, Type:create schema, State:queueing, SchemaState:none, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 16:08:56.35 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 16:08:56.360 +00:00] [INFO] [domain.go:154] ["diff load InfoSchema success"] [currentSchemaVersion=33] [neededSchemaVersion=34] ["start time"=90.236µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 16:08:56.362 +00:00] [INFO] [ddl_worker.go:1293] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=34] ["take time"=2.216088ms] [job="ID:69, Type:create schema, State:done, SchemaState:public, SchemaID:68, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 16:08:56.35 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 16:08:56.364 +00:00] [INFO] [ddl_worker.go:564] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:69, Type:create schema, State:synced, SchemaState:public, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 16:08:56.35 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 16:08:56.365 +00:00] [INFO] [ddl.go:1021] ["[ddl] DDL job is finished"] [jobID=69]
   > [2024/07/23 16:08:56.366 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/23 16:08:56.367 +00:00] [INFO] [session.go:3224] ["CRUCIAL OPERATION"] [conn=2199023255957] [schemaVersion=34] [cur_db=testdb] [sql="create table t1(id1 int, id2 int, id3 int, PRIMARY KEY(id1), UNIQUE KEY udx_id2 (id2));"] [user=root@%]
   > [2024/07/23 16:08:56.370 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:71, Type:create table, State:queueing, SchemaState:none, SchemaID:68, TableID:70, RowCount:0, ArgLen:1, start time: 2024-07-23 16:08:56.368 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/23 16:08:56.370 +00:00] [INFO] [ddl.go:928] ["[ddl] start DDL job"] [job="ID:71, Type:create table, State:queueing, SchemaState:none, SchemaID:68, TableID:70, RowCount:0, ArgLen:1, start time: 2024-07-23 16:08:56.368 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t1(id1 int, id2 int, id3 int, PRIMARY KEY(id1), UNIQUE KEY udx_id2 (id2));"]
   > [2024/07/23 16:08:56.375 +00:00] [INFO] [ddl_worker.go:1084] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:71, Type:create table, State:queueing, SchemaState:none, SchemaID:68, TableID:70, RowCount:0, ArgLen:0, start time: 2024-07-23 16:08:56.368 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 16:08:56.378 +00:00] [INFO] [domain.go:154] ["diff load InfoSchema success"] [currentSchemaVersion=34] [neededSchemaVersion=35] ["start time"=438.887µs] [phyTblIDs="[70]"] [actionTypes="[8]"]
   > [2024/07/23 16:08:56.380 +00:00] [INFO] [ddl_worker.go:1293] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=35] ["take time"=2.127109ms] [job="ID:71, Type:create table, State:done, SchemaState:public, SchemaID:68, TableID:70, RowCount:0, ArgLen:1, start time: 2024-07-23 16:08:56.368 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 16:08:56.383 +00:00] [INFO] [ddl_worker.go:564] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:71, Type:create table, State:synced, SchemaState:public, SchemaID:68, TableID:70, RowCount:0, ArgLen:0, start time: 2024-07-23 16:08:56.368 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 16:08:56.385 +00:00] [INFO] [ddl.go:1021] ["[ddl] DDL job is finished"] [jobID=71]
   > [2024/07/23 16:08:56.385 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/23 16:08:56.386 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=66] ["first split key"=748000000000000046]
   > [2024/07/23 16:08:56.386 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=66] ["first at"=748000000000000046] ["first new region left"="{Id:66 StartKey:7480000000000000ff4200000000000000f8 EndKey:7480000000000000ff4600000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:67 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/23 16:08:56.386 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[66]"]
   > [2024/07/23 16:08:57.405 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/07/23 16:08:57.415 +00:00] [INFO] [set.go:152] ["set global var"] [conn=2199023255959] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/07/23 16:08:58.316 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
