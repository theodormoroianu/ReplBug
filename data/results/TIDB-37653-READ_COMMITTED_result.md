# Bug ID TIDB-37653-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/37653
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              TiDB locks the record which is filtered by the non-index condition


## Details
 * Database: tidb-v6.2.0
 * Number of scenarios: 1
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
   > [2024/07/23 16:09:00.194 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/07/23 16:09:00.198 +00:00] [INFO] [session.go:3224] ["CRUCIAL OPERATION"] [conn=2199023255965] [schemaVersion=43] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/23 16:09:00.201 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:78, Type:drop schema, State:queueing, SchemaState:public, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 16:09:00.199 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/23 16:09:00.201 +00:00] [INFO] [ddl.go:928] ["[ddl] start DDL job"] [job="ID:78, Type:drop schema, State:queueing, SchemaState:public, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 16:09:00.199 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/23 16:09:00.205 +00:00] [INFO] [ddl_worker.go:1084] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:78, Type:drop schema, State:queueing, SchemaState:public, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 16:09:00.199 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 16:09:00.208 +00:00] [INFO] [domain.go:154] ["diff load InfoSchema success"] [currentSchemaVersion=43] [neededSchemaVersion=44] ["start time"=90.865µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 16:09:00.210 +00:00] [INFO] [ddl_worker.go:1293] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=44] ["take time"=2.68808ms] [job="ID:78, Type:drop schema, State:running, SchemaState:write only, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 16:09:00.199 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 16:09:00.214 +00:00] [INFO] [ddl_worker.go:1084] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:78, Type:drop schema, State:running, SchemaState:write only, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 16:09:00.199 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 16:09:00.217 +00:00] [INFO] [domain.go:154] ["diff load InfoSchema success"] [currentSchemaVersion=44] [neededSchemaVersion=45] ["start time"=80.318µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 16:09:00.219 +00:00] [INFO] [ddl_worker.go:1293] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=45] ["take time"=2.588905ms] [job="ID:78, Type:drop schema, State:running, SchemaState:delete only, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 16:09:00.199 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 16:09:00.223 +00:00] [INFO] [ddl_worker.go:1084] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:78, Type:drop schema, State:running, SchemaState:delete only, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 16:09:00.199 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 16:09:00.226 +00:00] [INFO] [domain.go:154] ["diff load InfoSchema success"] [currentSchemaVersion=45] [neededSchemaVersion=46] ["start time"=83.042µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 16:09:00.228 +00:00] [INFO] [ddl_worker.go:1293] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=46] ["take time"=2.29892ms] [job="ID:78, Type:drop schema, State:done, SchemaState:none, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 16:09:00.199 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 16:09:00.232 +00:00] [INFO] [delete_range.go:109] ["[ddl] add job into delete-range table"] [jobID=78] [jobType="drop schema"]
   > [2024/07/23 16:09:00.232 +00:00] [INFO] [ddl_worker.go:564] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:78, Type:drop schema, State:synced, SchemaState:none, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 16:09:00.199 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 16:09:00.234 +00:00] [INFO] [ddl.go:1021] ["[ddl] DDL job is finished"] [jobID=78]
   > [2024/07/23 16:09:00.234 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/23 16:09:00.236 +00:00] [INFO] [session.go:3224] ["CRUCIAL OPERATION"] [conn=2199023255965] [schemaVersion=46] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/23 16:09:00.238 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:80, Type:create schema, State:queueing, SchemaState:none, SchemaID:79, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 16:09:00.236 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/23 16:09:00.238 +00:00] [INFO] [ddl.go:928] ["[ddl] start DDL job"] [job="ID:80, Type:create schema, State:queueing, SchemaState:none, SchemaID:79, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 16:09:00.236 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/23 16:09:00.246 +00:00] [INFO] [ddl_worker.go:1084] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:80, Type:create schema, State:queueing, SchemaState:none, SchemaID:79, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 16:09:00.236 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 16:09:00.249 +00:00] [INFO] [domain.go:154] ["diff load InfoSchema success"] [currentSchemaVersion=46] [neededSchemaVersion=47] ["start time"=193.602µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 16:09:00.251 +00:00] [INFO] [ddl_worker.go:1293] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=47] ["take time"=2.274266ms] [job="ID:80, Type:create schema, State:done, SchemaState:public, SchemaID:79, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 16:09:00.236 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 16:09:00.254 +00:00] [INFO] [ddl_worker.go:564] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:80, Type:create schema, State:synced, SchemaState:public, SchemaID:79, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 16:09:00.236 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 16:09:00.256 +00:00] [INFO] [ddl.go:1021] ["[ddl] DDL job is finished"] [jobID=80]
   > [2024/07/23 16:09:00.256 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/23 16:09:00.260 +00:00] [INFO] [session.go:3224] ["CRUCIAL OPERATION"] [conn=2199023255965] [schemaVersion=47] [cur_db=testdb] [sql="create table t1(id1 int, id2 int, id3 int, PRIMARY KEY(id1), UNIQUE KEY udx_id2 (id2));"] [user=root@%]
   > [2024/07/23 16:09:00.262 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:82, Type:create table, State:queueing, SchemaState:none, SchemaID:79, TableID:81, RowCount:0, ArgLen:1, start time: 2024-07-23 16:09:00.26 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/23 16:09:00.262 +00:00] [INFO] [ddl.go:928] ["[ddl] start DDL job"] [job="ID:82, Type:create table, State:queueing, SchemaState:none, SchemaID:79, TableID:81, RowCount:0, ArgLen:1, start time: 2024-07-23 16:09:00.26 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t1(id1 int, id2 int, id3 int, PRIMARY KEY(id1), UNIQUE KEY udx_id2 (id2));"]
   > [2024/07/23 16:09:00.269 +00:00] [INFO] [ddl_worker.go:1084] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:82, Type:create table, State:queueing, SchemaState:none, SchemaID:79, TableID:81, RowCount:0, ArgLen:0, start time: 2024-07-23 16:09:00.26 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 16:09:00.273 +00:00] [INFO] [domain.go:154] ["diff load InfoSchema success"] [currentSchemaVersion=47] [neededSchemaVersion=48] ["start time"=416.049µs] [phyTblIDs="[81]"] [actionTypes="[8]"]
   > [2024/07/23 16:09:00.274 +00:00] [INFO] [ddl_worker.go:1293] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=48] ["take time"=2.235923ms] [job="ID:82, Type:create table, State:done, SchemaState:public, SchemaID:79, TableID:81, RowCount:0, ArgLen:1, start time: 2024-07-23 16:09:00.26 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 16:09:00.279 +00:00] [INFO] [ddl_worker.go:564] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:82, Type:create table, State:synced, SchemaState:public, SchemaID:79, TableID:81, RowCount:0, ArgLen:0, start time: 2024-07-23 16:09:00.26 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 16:09:00.281 +00:00] [INFO] [ddl.go:1021] ["[ddl] DDL job is finished"] [jobID=82]
   > [2024/07/23 16:09:00.281 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/23 16:09:00.281 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=70] ["first split key"=748000000000000051]
   > [2024/07/23 16:09:00.281 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=70] ["first at"=748000000000000051] ["first new region left"="{Id:70 StartKey:7480000000000000ff4b00000000000000f8 EndKey:7480000000000000ff5100000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:71 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/23 16:09:00.282 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[70]"]
   > [2024/07/23 16:09:01.295 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/07/23 16:09:01.305 +00:00] [INFO] [set.go:152] ["set global var"] [conn=2199023255967] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/07/23 16:09:02.205 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
