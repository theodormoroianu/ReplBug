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
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
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
     - Output: []
 * Instruction #7:
     - SQL:  COMMIT;
     - TID: 1
     - Output: None

 * Container logs:
   > [2024/06/26 12:18:50.377 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=13] [user=root] [host=]
   > [2024/06/26 12:18:50.379 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=13] [schemaVersion=38] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/06/26 12:18:50.380 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:67, Type:drop schema, State:none, SchemaState:queueing, SchemaID:62, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-26 12:18:50.38 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/26 12:18:50.380 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:67, Type:drop schema, State:none, SchemaState:queueing, SchemaID:62, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-26 12:18:50.38 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/06/26 12:18:50.381 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:drop schema, State:none, SchemaState:queueing, SchemaID:62, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-26 12:18:50.38 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/26 12:18:50.381 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=38] [neededSchemaVersion=39] ["start time"=152.116µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/26 12:18:50.384 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=39] ["take time"=2.704423ms] [job="ID:67, Type:drop schema, State:running, SchemaState:write only, SchemaID:62, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-26 12:18:50.38 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/26 12:18:50.384 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:drop schema, State:running, SchemaState:write only, SchemaID:62, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-26 12:18:50.38 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/26 12:18:50.385 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=39] [neededSchemaVersion=40] ["start time"=57.271µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/26 12:18:50.387 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=40] ["take time"=2.782717ms] [job="ID:67, Type:drop schema, State:running, SchemaState:delete only, SchemaID:62, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-26 12:18:50.38 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/26 12:18:50.388 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:drop schema, State:running, SchemaState:delete only, SchemaID:62, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-26 12:18:50.38 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/26 12:18:50.389 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=40] [neededSchemaVersion=41] ["start time"=80.458µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/26 12:18:50.391 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=41] ["take time"=2.20212ms] [job="ID:67, Type:drop schema, State:done, SchemaState:queueing, SchemaID:62, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-26 12:18:50.38 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/26 12:18:50.391 +00:00] [INFO] [delete_range.go:107] ["[ddl] add job into delete-range table"] [jobID=67] [jobType="drop schema"]
   > [2024/06/26 12:18:50.391 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:62, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-26 12:18:50.38 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/26 12:18:50.391 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=67]
   > [2024/06/26 12:18:50.391 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/26 12:18:50.392 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=13] [schemaVersion=41] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/06/26 12:18:50.393 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:69, Type:create schema, State:none, SchemaState:queueing, SchemaID:68, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-26 12:18:50.393 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/26 12:18:50.393 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:69, Type:create schema, State:none, SchemaState:queueing, SchemaID:68, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-26 12:18:50.393 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/26 12:18:50.394 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:69, Type:create schema, State:none, SchemaState:queueing, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-26 12:18:50.393 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/26 12:18:50.394 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=41] [neededSchemaVersion=42] ["start time"=74.801µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/26 12:18:50.396 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=42] ["take time"=2.21958ms] [job="ID:69, Type:create schema, State:done, SchemaState:public, SchemaID:68, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-26 12:18:50.393 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/26 12:18:50.397 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:69, Type:create schema, State:synced, SchemaState:public, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-26 12:18:50.393 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/26 12:18:50.397 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=69]
   > [2024/06/26 12:18:50.397 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/26 12:18:50.400 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=13] [schemaVersion=42] [cur_db=testdb] [sql="CREATE TABLE t (c1 INT PRIMARY KEY, c2 INT);"] [user=root@127.0.0.1]
   > [2024/06/26 12:18:50.401 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:71, Type:create table, State:none, SchemaState:queueing, SchemaID:68, TableID:70, RowCount:0, ArgLen:1, start time: 2024-06-26 12:18:50.4 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/26 12:18:50.401 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:71, Type:create table, State:none, SchemaState:queueing, SchemaID:68, TableID:70, RowCount:0, ArgLen:1, start time: 2024-06-26 12:18:50.4 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE t (c1 INT PRIMARY KEY, c2 INT);"]
   > [2024/06/26 12:18:50.401 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:71, Type:create table, State:none, SchemaState:queueing, SchemaID:68, TableID:70, RowCount:0, ArgLen:0, start time: 2024-06-26 12:18:50.4 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/26 12:18:50.402 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=42] [neededSchemaVersion=43] ["start time"=251.501µs] [phyTblIDs="[70]"] [actionTypes="[8]"]
   > [2024/06/26 12:18:50.404 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=43] ["take time"=2.314286ms] [job="ID:71, Type:create table, State:done, SchemaState:public, SchemaID:68, TableID:70, RowCount:0, ArgLen:1, start time: 2024-06-26 12:18:50.4 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/26 12:18:50.405 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:71, Type:create table, State:synced, SchemaState:public, SchemaID:68, TableID:70, RowCount:0, ArgLen:0, start time: 2024-06-26 12:18:50.4 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/26 12:18:50.406 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=71]
   > [2024/06/26 12:18:50.406 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/26 12:18:50.406 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=58] ["first split key"=748000000000000046]
   > [2024/06/26 12:18:50.407 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=58] ["first at"=748000000000000046] ["first new region left"="{Id:58 StartKey:7480000000000000ff4000000000000000f8 EndKey:7480000000000000ff4600000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:59 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/26 12:18:50.407 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[58]"]
   > [2024/06/26 12:18:51.499 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=15] [user=root] [host=]
   > [2024/06/26 12:18:51.522 +00:00] [INFO] [set.go:139] ["set global var"] [conn=15] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/06/26 12:18:52.438 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=17] [user=root] [host=]
