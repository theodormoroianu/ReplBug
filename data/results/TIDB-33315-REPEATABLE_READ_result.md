# Bug ID TIDB-33315-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/33315
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              conn 1 should get an empty set


## Details
 * Database: tidb-v5.4.0
 * Number of scenarios: 1
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
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
     - Output: [(1, 1)]
     - Executed order: 6
     - Affected rows: 1
 * Instruction #7:
     - Instruction:  COMMIT;
     - Transaction: conn_1
     - Output: None
     - Executed order: 7
     - Affected rows: 0

 * Container logs:
   > [2024/08/14 17:38:38.258 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=5] [user=root] [host=]
   > [2024/08/14 17:38:38.260 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=28] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/08/14 17:38:38.261 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=28] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/08/14 17:38:38.262 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:58, Type:create schema, State:none, SchemaState:queueing, SchemaID:57, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-14 17:38:38.262 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/14 17:38:38.262 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:58, Type:create schema, State:none, SchemaState:queueing, SchemaID:57, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-14 17:38:38.262 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/08/14 17:38:38.262 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:58, Type:create schema, State:none, SchemaState:queueing, SchemaID:57, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-14 17:38:38.262 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/14 17:38:38.263 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=28] [neededSchemaVersion=29] ["start time"=76.756µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/14 17:38:38.265 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=29] ["take time"=2.186753ms] [job="ID:58, Type:create schema, State:done, SchemaState:public, SchemaID:57, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-14 17:38:38.262 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/14 17:38:38.265 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:58, Type:create schema, State:synced, SchemaState:public, SchemaID:57, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-14 17:38:38.262 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/14 17:38:38.266 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=58]
   > [2024/08/14 17:38:38.266 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/08/14 17:38:38.267 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=29] [cur_db=testdb] [sql="CREATE TABLE t (c1 INT PRIMARY KEY, c2 INT);"] [user=root@127.0.0.1]
   > [2024/08/14 17:38:38.269 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:60, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:59, RowCount:0, ArgLen:1, start time: 2024-08-14 17:38:38.268 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/14 17:38:38.269 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:60, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:59, RowCount:0, ArgLen:1, start time: 2024-08-14 17:38:38.268 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE t (c1 INT PRIMARY KEY, c2 INT);"]
   > [2024/08/14 17:38:38.270 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:60, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:59, RowCount:0, ArgLen:0, start time: 2024-08-14 17:38:38.268 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/14 17:38:38.271 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=29] [neededSchemaVersion=30] ["start time"=215.253µs] [phyTblIDs="[59]"] [actionTypes="[8]"]
   > [2024/08/14 17:38:38.273 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=30] ["take time"=2.122916ms] [job="ID:60, Type:create table, State:done, SchemaState:public, SchemaID:57, TableID:59, RowCount:0, ArgLen:1, start time: 2024-08-14 17:38:38.268 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/14 17:38:38.273 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:60, Type:create table, State:synced, SchemaState:public, SchemaID:57, TableID:59, RowCount:0, ArgLen:0, start time: 2024-08-14 17:38:38.268 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/14 17:38:38.274 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=60]
   > [2024/08/14 17:38:38.274 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/08/14 17:38:38.275 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=52] ["first split key"=74800000000000003b]
   > [2024/08/14 17:38:38.277 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=54] ["first at"=74800000000000003b] ["first new region left"="{Id:54 StartKey:7480000000000000ff3700000000000000f8 EndKey:7480000000000000ff3b00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:55 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/08/14 17:38:38.277 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[54]"]
   > [2024/08/14 17:38:39.334 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=7] [user=root] [host=]
   > [2024/08/14 17:38:39.346 +00:00] [INFO] [set.go:139] ["set global var"] [conn=7] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/08/14 17:38:40.244 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=9] [user=root] [host=]
