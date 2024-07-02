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
 * Instruction #1:
     - Instruction:  BEGIN PESSIMISTIC;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
 * Instruction #2:
     - Instruction:  UPDATE t SET c1=2, c2=2;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
 * Instruction #3:
     - Instruction:  BEGIN PESSIMISTIC;
     - Transaction: conn_1
     - Output: None
     - Executed order: 3
 * Instruction #4:
     - Instruction:  DELETE FROM t;
     - Transaction: conn_1
     - Output: None
     - Executed order: 5
 * Instruction #5:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
 * Instruction #6:
     - Instruction:  SELECT * FROM t;
     - Transaction: conn_1
     - Output: []
     - Executed order: 6
 * Instruction #7:
     - Instruction:  COMMIT;
     - Transaction: conn_1
     - Output: None
     - Executed order: 7

 * Container logs:
   > [2024/07/01 15:14:28.415 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=125] [user=root] [host=]
   > [2024/07/01 15:14:28.417 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=125] [schemaVersion=398] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/07/01 15:14:28.418 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:407, Type:drop schema, State:none, SchemaState:queueing, SchemaID:402, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:14:28.417 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:14:28.418 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:407, Type:drop schema, State:none, SchemaState:queueing, SchemaID:402, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:14:28.417 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/01 15:14:28.419 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:407, Type:drop schema, State:none, SchemaState:queueing, SchemaID:402, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:14:28.417 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:14:28.420 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=398] [neededSchemaVersion=399] ["start time"=69.283µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:14:28.422 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=399] ["take time"=2.048114ms] [job="ID:407, Type:drop schema, State:running, SchemaState:write only, SchemaID:402, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:14:28.417 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:14:28.422 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:407, Type:drop schema, State:running, SchemaState:write only, SchemaID:402, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:14:28.417 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:14:28.423 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=399] [neededSchemaVersion=400] ["start time"=121.874µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:14:28.425 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=400] ["take time"=2.031771ms] [job="ID:407, Type:drop schema, State:running, SchemaState:delete only, SchemaID:402, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:14:28.417 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:14:28.425 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:407, Type:drop schema, State:running, SchemaState:delete only, SchemaID:402, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:14:28.417 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:14:28.428 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=400] [neededSchemaVersion=401] ["start time"=110.001µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:14:28.430 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=401] ["take time"=2.150712ms] [job="ID:407, Type:drop schema, State:done, SchemaState:queueing, SchemaID:402, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:14:28.417 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:14:28.431 +00:00] [INFO] [delete_range.go:107] ["[ddl] add job into delete-range table"] [jobID=407] [jobType="drop schema"]
   > [2024/07/01 15:14:28.431 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:407, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:402, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:14:28.417 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:14:28.436 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=407]
   > [2024/07/01 15:14:28.436 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:14:28.440 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=125] [schemaVersion=401] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/07/01 15:14:28.441 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:409, Type:create schema, State:none, SchemaState:queueing, SchemaID:408, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:14:28.441 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:14:28.441 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:409, Type:create schema, State:none, SchemaState:queueing, SchemaID:408, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:14:28.441 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/01 15:14:28.442 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:409, Type:create schema, State:none, SchemaState:queueing, SchemaID:408, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:14:28.441 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:14:28.443 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=401] [neededSchemaVersion=402] ["start time"=152.186µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:14:28.445 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=402] ["take time"=2.070673ms] [job="ID:409, Type:create schema, State:done, SchemaState:public, SchemaID:408, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:14:28.441 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:14:28.445 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:409, Type:create schema, State:synced, SchemaState:public, SchemaID:408, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:14:28.441 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:14:28.446 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=409]
   > [2024/07/01 15:14:28.446 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:14:28.447 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=125] [schemaVersion=402] [cur_db=testdb] [sql="CREATE TABLE t (c1 INT PRIMARY KEY, c2 INT);"] [user=root@127.0.0.1]
   > [2024/07/01 15:14:28.448 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:411, Type:create table, State:none, SchemaState:queueing, SchemaID:408, TableID:410, RowCount:0, ArgLen:1, start time: 2024-07-01 15:14:28.448 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:14:28.448 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:411, Type:create table, State:none, SchemaState:queueing, SchemaID:408, TableID:410, RowCount:0, ArgLen:1, start time: 2024-07-01 15:14:28.448 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE t (c1 INT PRIMARY KEY, c2 INT);"]
   > [2024/07/01 15:14:28.448 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:411, Type:create table, State:none, SchemaState:queueing, SchemaID:408, TableID:410, RowCount:0, ArgLen:0, start time: 2024-07-01 15:14:28.448 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:14:28.449 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=402] [neededSchemaVersion=403] ["start time"=176.211µs] [phyTblIDs="[410]"] [actionTypes="[8]"]
   > [2024/07/01 15:14:28.451 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=403] ["take time"=2.058101ms] [job="ID:411, Type:create table, State:done, SchemaState:public, SchemaID:408, TableID:410, RowCount:0, ArgLen:1, start time: 2024-07-01 15:14:28.448 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:14:28.452 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:411, Type:create table, State:synced, SchemaState:public, SchemaID:408, TableID:410, RowCount:0, ArgLen:0, start time: 2024-07-01 15:14:28.448 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:14:28.452 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=411]
   > [2024/07/01 15:14:28.452 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:14:28.452 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=162] ["first split key"=74800000000000019a]
   > [2024/07/01 15:14:28.453 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=162] ["first at"=74800000000000019a] ["first new region left"="{Id:162 StartKey:7480000000000001ff9400000000000000f8 EndKey:7480000000000001ff9a00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:163 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/01 15:14:28.453 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[162]"]
   > [2024/07/01 15:14:29.573 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=127] [user=root] [host=]
   > [2024/07/01 15:14:29.605 +00:00] [INFO] [set.go:139] ["set global var"] [conn=127] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/07/01 15:14:30.483 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=129] [user=root] [host=]
