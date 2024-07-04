# Bug ID TIDB-34177-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/34177
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              Error on the first scenario


## Details
 * Database: tidb-v6.0.0
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
     - Instruction:  BEGIN;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
 * Instruction #2:
     - Instruction:  DELETE FROM t WHERE (CAST(('123abc') AS DOUBLE)) IS NULL;
     - Transaction: conn_0
     - Output: ERROR: 1292 (22007): Truncated incorrect DOUBLE value: '123abc'
     - Executed order: Not executed
 * Instruction #3:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2

 * Container logs:
   > [2024/07/03 14:52:30.638 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/07/03 14:52:30.641 +00:00] [INFO] [session.go:3208] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=42] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/03 14:52:30.642 +00:00] [INFO] [ddl_worker.go:325] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:75, Type:drop schema, State:none, SchemaState:queueing, SchemaID:70, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 14:52:30.642 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/03 14:52:30.642 +00:00] [INFO] [ddl.go:615] ["[ddl] start DDL job"] [job="ID:75, Type:drop schema, State:none, SchemaState:queueing, SchemaID:70, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 14:52:30.642 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/03 14:52:30.643 +00:00] [INFO] [ddl_worker.go:758] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:75, Type:drop schema, State:none, SchemaState:queueing, SchemaID:70, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 14:52:30.642 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 14:52:30.644 +00:00] [INFO] [domain.go:138] ["diff load InfoSchema success"] [currentSchemaVersion=42] [neededSchemaVersion=43] ["start time"=67.677µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/03 14:52:30.646 +00:00] [INFO] [ddl_worker.go:966] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=43] ["take time"=2.28055ms] [job="ID:75, Type:drop schema, State:running, SchemaState:write only, SchemaID:70, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 14:52:30.642 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 14:52:30.646 +00:00] [INFO] [ddl_worker.go:758] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:75, Type:drop schema, State:running, SchemaState:write only, SchemaID:70, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 14:52:30.642 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 14:52:30.647 +00:00] [INFO] [domain.go:138] ["diff load InfoSchema success"] [currentSchemaVersion=43] [neededSchemaVersion=44] ["start time"=124.528µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/03 14:52:30.649 +00:00] [INFO] [ddl_worker.go:966] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=44] ["take time"=2.111531ms] [job="ID:75, Type:drop schema, State:running, SchemaState:delete only, SchemaID:70, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 14:52:30.642 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 14:52:30.649 +00:00] [INFO] [ddl_worker.go:758] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:75, Type:drop schema, State:running, SchemaState:delete only, SchemaID:70, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 14:52:30.642 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 14:52:30.650 +00:00] [INFO] [domain.go:138] ["diff load InfoSchema success"] [currentSchemaVersion=44] [neededSchemaVersion=45] ["start time"=67.188µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/03 14:52:30.652 +00:00] [INFO] [ddl_worker.go:966] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=45] ["take time"=2.26672ms] [job="ID:75, Type:drop schema, State:done, SchemaState:queueing, SchemaID:70, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 14:52:30.642 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 14:52:30.653 +00:00] [INFO] [delete_range.go:107] ["[ddl] add job into delete-range table"] [jobID=75] [jobType="drop schema"]
   > [2024/07/03 14:52:30.653 +00:00] [INFO] [ddl_worker.go:439] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:75, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:70, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 14:52:30.642 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 14:52:30.654 +00:00] [INFO] [ddl.go:679] ["[ddl] DDL job is finished"] [jobID=75]
   > [2024/07/03 14:52:30.654 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/03 14:52:30.656 +00:00] [INFO] [session.go:3208] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=45] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/03 14:52:30.657 +00:00] [INFO] [ddl_worker.go:325] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:77, Type:create schema, State:none, SchemaState:queueing, SchemaID:76, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-03 14:52:30.656 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/03 14:52:30.657 +00:00] [INFO] [ddl.go:615] ["[ddl] start DDL job"] [job="ID:77, Type:create schema, State:none, SchemaState:queueing, SchemaID:76, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-03 14:52:30.656 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/03 14:52:30.658 +00:00] [INFO] [ddl_worker.go:758] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:create schema, State:none, SchemaState:queueing, SchemaID:76, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 14:52:30.656 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 14:52:30.659 +00:00] [INFO] [domain.go:138] ["diff load InfoSchema success"] [currentSchemaVersion=45] [neededSchemaVersion=46] ["start time"=149.182µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/03 14:52:30.661 +00:00] [INFO] [ddl_worker.go:966] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=46] ["take time"=2.250238ms] [job="ID:77, Type:create schema, State:done, SchemaState:public, SchemaID:76, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-03 14:52:30.656 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 14:52:30.662 +00:00] [INFO] [ddl_worker.go:439] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:create schema, State:synced, SchemaState:public, SchemaID:76, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 14:52:30.656 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 14:52:30.663 +00:00] [INFO] [ddl.go:679] ["[ddl] DDL job is finished"] [jobID=77]
   > [2024/07/03 14:52:30.663 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/03 14:52:30.666 +00:00] [INFO] [session.go:3208] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=46] [cur_db=testdb] [sql="DROP TABLE IF EXISTS t;"] [user=root@%]
   > [2024/07/03 14:52:30.666 +00:00] [INFO] [session.go:3208] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=46] [cur_db=testdb] [sql="CREATE TABLE t (c1 VARCHAR(14));"] [user=root@%]
   > [2024/07/03 14:52:30.668 +00:00] [INFO] [ddl_worker.go:325] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:79, Type:create table, State:none, SchemaState:queueing, SchemaID:76, TableID:78, RowCount:0, ArgLen:1, start time: 2024-07-03 14:52:30.667 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/03 14:52:30.668 +00:00] [INFO] [ddl.go:615] ["[ddl] start DDL job"] [job="ID:79, Type:create table, State:none, SchemaState:queueing, SchemaID:76, TableID:78, RowCount:0, ArgLen:1, start time: 2024-07-03 14:52:30.667 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE t (c1 VARCHAR(14));"]
   > [2024/07/03 14:52:30.669 +00:00] [INFO] [ddl_worker.go:758] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:79, Type:create table, State:none, SchemaState:queueing, SchemaID:76, TableID:78, RowCount:0, ArgLen:0, start time: 2024-07-03 14:52:30.667 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 14:52:30.671 +00:00] [INFO] [domain.go:138] ["diff load InfoSchema success"] [currentSchemaVersion=46] [neededSchemaVersion=47] ["start time"=343.064µs] [phyTblIDs="[78]"] [actionTypes="[8]"]
   > [2024/07/03 14:52:30.673 +00:00] [INFO] [ddl_worker.go:966] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=47] ["take time"=2.320499ms] [job="ID:79, Type:create table, State:done, SchemaState:public, SchemaID:76, TableID:78, RowCount:0, ArgLen:1, start time: 2024-07-03 14:52:30.667 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 14:52:30.674 +00:00] [INFO] [ddl_worker.go:439] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:79, Type:create table, State:synced, SchemaState:public, SchemaID:76, TableID:78, RowCount:0, ArgLen:0, start time: 2024-07-03 14:52:30.667 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 14:52:30.675 +00:00] [INFO] [ddl.go:679] ["[ddl] DDL job is finished"] [jobID=79]
   > [2024/07/03 14:52:30.675 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/03 14:52:30.675 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=66] ["first split key"=74800000000000004e]
   > [2024/07/03 14:52:30.676 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=66] ["first at"=74800000000000004e] ["first new region left"="{Id:66 StartKey:7480000000000000ff4800000000000000f8 EndKey:7480000000000000ff4e00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:67 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/03 14:52:30.676 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[66]"]
   > [2024/07/03 14:52:30.676 +00:00] [WARN] [2pc.go:1800] ["schemaLeaseChecker is not set for this transaction"] [sessionID=11] [startTS=450892490519609345] [checkTS=450892490519609346]
   > [2024/07/03 14:52:31.719 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/07/03 14:52:31.732 +00:00] [INFO] [set.go:139] ["set global var"] [conn=13] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/07/03 14:52:32.320 +00:00] [WARN] [session.go:1866] ["run statement failed"] [conn=13] [schemaVersion=47] [error="[tikv:1292]Truncated incorrect DOUBLE value: '123abc'"] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 13,\n  \"status\": 3,\n  \"strictMode\": true,\n  \"txn\": \"450892490871406592\",\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"127.0.0.1\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/07/03 14:52:32.321 +00:00] [INFO] [conn.go:1123] ["command dispatched failed"] [conn=13] [connInfo="id:13, addr:127.0.0.1:37022 status:11, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:1, autocommit:1"] [sql=" DELETE FROM t WHERE (CAST(('123abc') AS DOUBLE)) IS NULL;"] [txn_mode=OPTIMISTIC] [timestamp=450892490871406592] [err="[tikv:1292]Truncated incorrect DOUBLE value: '123abc'"]
