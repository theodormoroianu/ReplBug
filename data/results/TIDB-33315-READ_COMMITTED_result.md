# Bug ID TIDB-33315-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/33315
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              conn 1 should get an empty set


## Details
 * Database: tidb-v5.4.0
 * Number of scenarios: 1
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows: 0
 * Instruction #1:
     - Instruction:  BEGIN PESSIMISTIC;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows: 0
 * Instruction #2:
     - Instruction:  UPDATE t SET c1=2, c2=2;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows: 1
 * Instruction #3:
     - Instruction:  BEGIN PESSIMISTIC;
     - Transaction: conn_1
     - Output: None
     - Executed order: 3
     - Affected rows: 0
 * Instruction #4:
     - Instruction:  DELETE FROM t;
     - Transaction: conn_1
     - Output: None
     - Executed order: 5
     - Affected rows: 1
 * Instruction #5:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows: 0
 * Instruction #6:
     - Instruction:  SELECT * FROM t;
     - Transaction: conn_1
     - Output: []
     - Executed order: 6
     - Affected rows: 0
 * Instruction #7:
     - Instruction:  COMMIT;
     - Transaction: conn_1
     - Output: None
     - Executed order: 7
     - Affected rows: 0

 * Container logs:
   > [2024/08/14 17:38:42.245 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=13] [user=root] [host=]
   > [2024/08/14 17:38:42.247 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=13] [schemaVersion=38] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/08/14 17:38:42.248 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:67, Type:drop schema, State:none, SchemaState:queueing, SchemaID:62, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-14 17:38:42.247 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/14 17:38:42.248 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:67, Type:drop schema, State:none, SchemaState:queueing, SchemaID:62, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-14 17:38:42.247 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/08/14 17:38:42.248 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:drop schema, State:none, SchemaState:queueing, SchemaID:62, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-14 17:38:42.247 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/14 17:38:42.249 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=38] [neededSchemaVersion=39] ["start time"=98.756µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/14 17:38:42.251 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=39] ["take time"=2.716087ms] [job="ID:67, Type:drop schema, State:running, SchemaState:write only, SchemaID:62, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-14 17:38:42.247 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/14 17:38:42.252 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:drop schema, State:running, SchemaState:write only, SchemaID:62, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-14 17:38:42.247 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/14 17:38:42.253 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=39] [neededSchemaVersion=40] ["start time"=126.484µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/14 17:38:42.255 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=40] ["take time"=2.217834ms] [job="ID:67, Type:drop schema, State:running, SchemaState:delete only, SchemaID:62, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-14 17:38:42.247 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/14 17:38:42.255 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:drop schema, State:running, SchemaState:delete only, SchemaID:62, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-14 17:38:42.247 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/14 17:38:42.256 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=40] [neededSchemaVersion=41] ["start time"=87.512µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/14 17:38:42.258 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=41] ["take time"=2.276152ms] [job="ID:67, Type:drop schema, State:done, SchemaState:queueing, SchemaID:62, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-14 17:38:42.247 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/14 17:38:42.258 +00:00] [INFO] [delete_range.go:107] ["[ddl] add job into delete-range table"] [jobID=67] [jobType="drop schema"]
   > [2024/08/14 17:38:42.259 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:62, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-14 17:38:42.247 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/14 17:38:42.259 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=67]
   > [2024/08/14 17:38:42.259 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/08/14 17:38:42.260 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=13] [schemaVersion=41] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/08/14 17:38:42.261 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:69, Type:create schema, State:none, SchemaState:queueing, SchemaID:68, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-14 17:38:42.261 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/14 17:38:42.261 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:69, Type:create schema, State:none, SchemaState:queueing, SchemaID:68, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-14 17:38:42.261 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/08/14 17:38:42.262 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:69, Type:create schema, State:none, SchemaState:queueing, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-14 17:38:42.261 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/14 17:38:42.263 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=41] [neededSchemaVersion=42] ["start time"=160.567µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/14 17:38:42.265 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=42] ["take time"=2.238437ms] [job="ID:69, Type:create schema, State:done, SchemaState:public, SchemaID:68, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-14 17:38:42.261 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/14 17:38:42.265 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:69, Type:create schema, State:synced, SchemaState:public, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-14 17:38:42.261 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/14 17:38:42.266 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=69]
   > [2024/08/14 17:38:42.266 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/08/14 17:38:42.268 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=13] [schemaVersion=42] [cur_db=testdb] [sql="CREATE TABLE t (c1 INT PRIMARY KEY, c2 INT);"] [user=root@127.0.0.1]
   > [2024/08/14 17:38:42.269 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:71, Type:create table, State:none, SchemaState:queueing, SchemaID:68, TableID:70, RowCount:0, ArgLen:1, start time: 2024-08-14 17:38:42.269 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/14 17:38:42.269 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:71, Type:create table, State:none, SchemaState:queueing, SchemaID:68, TableID:70, RowCount:0, ArgLen:1, start time: 2024-08-14 17:38:42.269 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE t (c1 INT PRIMARY KEY, c2 INT);"]
   > [2024/08/14 17:38:42.270 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:71, Type:create table, State:none, SchemaState:queueing, SchemaID:68, TableID:70, RowCount:0, ArgLen:0, start time: 2024-08-14 17:38:42.269 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/14 17:38:42.271 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=42] [neededSchemaVersion=43] ["start time"=171.183µs] [phyTblIDs="[70]"] [actionTypes="[8]"]
   > [2024/08/14 17:38:42.273 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=43] ["take time"=2.399563ms] [job="ID:71, Type:create table, State:done, SchemaState:public, SchemaID:68, TableID:70, RowCount:0, ArgLen:1, start time: 2024-08-14 17:38:42.269 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/14 17:38:42.273 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:71, Type:create table, State:synced, SchemaState:public, SchemaID:68, TableID:70, RowCount:0, ArgLen:0, start time: 2024-08-14 17:38:42.269 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/14 17:38:42.274 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=71]
   > [2024/08/14 17:38:42.274 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/08/14 17:38:42.275 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=58] ["first split key"=748000000000000046]
   > [2024/08/14 17:38:42.275 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=58] ["first at"=748000000000000046] ["first new region left"="{Id:58 StartKey:7480000000000000ff4000000000000000f8 EndKey:7480000000000000ff4600000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:59 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/08/14 17:38:42.275 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[58]"]
   > [2024/08/14 17:38:43.327 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=15] [user=root] [host=]
   > [2024/08/14 17:38:43.340 +00:00] [INFO] [set.go:139] ["set global var"] [conn=15] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/08/14 17:38:44.238 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=17] [user=root] [host=]
