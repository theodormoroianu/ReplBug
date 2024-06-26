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
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  BEGIN PESSIMISTIC;
     - TID: 0
     - Output: None
 * Instruction #2:
     - SQL:  UPDATE t SET c1=2, c2=2;
     - TID: 0
     - Output: None
 * Instruction #3:
     - SQL:  BEGIN PESSIMISTIC;
     - TID: 1
     - Output: None
 * Instruction #4:
     - SQL:  DELETE FROM t;
     - TID: 1
     - Output: None
 * Instruction #5:
     - SQL:  COMMIT;
     - TID: 0
     - Output: None
 * Instruction #6:
     - SQL:  SELECT * FROM t;
     - TID: 1
     - Output: [(1, 1)]
 * Instruction #7:
     - SQL:  COMMIT;
     - TID: 1
     - Output: None

 * Container logs:
   > [2024/06/26 12:18:45.394 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=5] [user=root] [host=]
   > [2024/06/26 12:18:45.398 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=28] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/06/26 12:18:45.399 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=28] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/06/26 12:18:45.401 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:58, Type:create schema, State:none, SchemaState:queueing, SchemaID:57, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-26 12:18:45.4 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/26 12:18:45.401 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:58, Type:create schema, State:none, SchemaState:queueing, SchemaID:57, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-26 12:18:45.4 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/26 12:18:45.401 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:58, Type:create schema, State:none, SchemaState:queueing, SchemaID:57, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-26 12:18:45.4 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/26 12:18:45.402 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=28] [neededSchemaVersion=29] ["start time"=149.252µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/26 12:18:45.404 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=29] ["take time"=2.266583ms] [job="ID:58, Type:create schema, State:done, SchemaState:public, SchemaID:57, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-26 12:18:45.4 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/26 12:18:45.405 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:58, Type:create schema, State:synced, SchemaState:public, SchemaID:57, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-26 12:18:45.4 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/26 12:18:45.405 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=58]
   > [2024/06/26 12:18:45.406 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/26 12:18:45.409 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=29] [cur_db=testdb] [sql="CREATE TABLE t (c1 INT PRIMARY KEY, c2 INT);"] [user=root@127.0.0.1]
   > [2024/06/26 12:18:45.410 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:60, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:59, RowCount:0, ArgLen:1, start time: 2024-06-26 12:18:45.409 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/26 12:18:45.410 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:60, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:59, RowCount:0, ArgLen:1, start time: 2024-06-26 12:18:45.409 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE t (c1 INT PRIMARY KEY, c2 INT);"]
   > [2024/06/26 12:18:45.411 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:60, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:59, RowCount:0, ArgLen:0, start time: 2024-06-26 12:18:45.409 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/26 12:18:45.412 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=29] [neededSchemaVersion=30] ["start time"=269.73µs] [phyTblIDs="[59]"] [actionTypes="[8]"]
   > [2024/06/26 12:18:45.414 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=30] ["take time"=2.026886ms] [job="ID:60, Type:create table, State:done, SchemaState:public, SchemaID:57, TableID:59, RowCount:0, ArgLen:1, start time: 2024-06-26 12:18:45.409 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/26 12:18:45.414 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:60, Type:create table, State:synced, SchemaState:public, SchemaID:57, TableID:59, RowCount:0, ArgLen:0, start time: 2024-06-26 12:18:45.409 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/26 12:18:45.415 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=60]
   > [2024/06/26 12:18:45.415 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/26 12:18:45.416 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=52] ["first split key"=74800000000000003b]
   > [2024/06/26 12:18:45.418 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=54] ["first at"=74800000000000003b] ["first new region left"="{Id:54 StartKey:7480000000000000ff3700000000000000f8 EndKey:7480000000000000ff3b00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:55 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/26 12:18:45.418 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[54]"]
   > [2024/06/26 12:18:46.492 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=7] [user=root] [host=]
   > [2024/06/26 12:18:46.502 +00:00] [INFO] [set.go:139] ["set global var"] [conn=7] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/06/26 12:18:47.454 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=9] [user=root] [host=]
