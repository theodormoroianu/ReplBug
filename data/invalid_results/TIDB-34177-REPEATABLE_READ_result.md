# Bug ID TIDB-34177-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/34177
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              Error on the first scenario


## Details
 * Database: tidb-v6.0.0
 * Number of scenarios: 1
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
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
   > [2024/07/03 14:52:27.899 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/07/03 14:52:27.902 +00:00] [INFO] [session.go:3208] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=32] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/03 14:52:27.903 +00:00] [INFO] [session.go:3208] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=32] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/03 14:52:27.904 +00:00] [INFO] [ddl_worker.go:325] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:66, Type:create schema, State:none, SchemaState:queueing, SchemaID:65, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-03 14:52:27.903 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/03 14:52:27.904 +00:00] [INFO] [ddl.go:615] ["[ddl] start DDL job"] [job="ID:66, Type:create schema, State:none, SchemaState:queueing, SchemaID:65, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-03 14:52:27.903 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/03 14:52:27.904 +00:00] [INFO] [ddl_worker.go:758] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:create schema, State:none, SchemaState:queueing, SchemaID:65, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 14:52:27.903 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 14:52:27.905 +00:00] [INFO] [domain.go:138] ["diff load InfoSchema success"] [currentSchemaVersion=32] [neededSchemaVersion=33] ["start time"=96.801µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/03 14:52:27.907 +00:00] [INFO] [ddl_worker.go:966] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=33] ["take time"=2.24493ms] [job="ID:66, Type:create schema, State:done, SchemaState:public, SchemaID:65, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-03 14:52:27.903 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 14:52:27.907 +00:00] [INFO] [ddl_worker.go:439] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:create schema, State:synced, SchemaState:public, SchemaID:65, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 14:52:27.903 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 14:52:27.908 +00:00] [INFO] [ddl.go:679] ["[ddl] DDL job is finished"] [jobID=66]
   > [2024/07/03 14:52:27.908 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/03 14:52:27.910 +00:00] [INFO] [session.go:3208] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=33] [cur_db=testdb] [sql="DROP TABLE IF EXISTS t;"] [user=root@%]
   > [2024/07/03 14:52:27.911 +00:00] [INFO] [session.go:3208] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=33] [cur_db=testdb] [sql="CREATE TABLE t (c1 VARCHAR(14));"] [user=root@%]
   > [2024/07/03 14:52:27.912 +00:00] [INFO] [ddl_worker.go:325] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:68, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:67, RowCount:0, ArgLen:1, start time: 2024-07-03 14:52:27.912 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/03 14:52:27.912 +00:00] [INFO] [ddl.go:615] ["[ddl] start DDL job"] [job="ID:68, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:67, RowCount:0, ArgLen:1, start time: 2024-07-03 14:52:27.912 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE t (c1 VARCHAR(14));"]
   > [2024/07/03 14:52:27.912 +00:00] [INFO] [ddl_worker.go:758] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:68, Type:create table, State:none, SchemaState:queueing, SchemaID:65, TableID:67, RowCount:0, ArgLen:0, start time: 2024-07-03 14:52:27.912 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 14:52:27.914 +00:00] [INFO] [domain.go:138] ["diff load InfoSchema success"] [currentSchemaVersion=33] [neededSchemaVersion=34] ["start time"=387.343µs] [phyTblIDs="[67]"] [actionTypes="[8]"]
   > [2024/07/03 14:52:27.915 +00:00] [INFO] [ddl_worker.go:966] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=34] ["take time"=2.024788ms] [job="ID:68, Type:create table, State:done, SchemaState:public, SchemaID:65, TableID:67, RowCount:0, ArgLen:1, start time: 2024-07-03 14:52:27.912 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 14:52:27.916 +00:00] [INFO] [ddl_worker.go:439] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:68, Type:create table, State:synced, SchemaState:public, SchemaID:65, TableID:67, RowCount:0, ArgLen:0, start time: 2024-07-03 14:52:27.912 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 14:52:27.916 +00:00] [INFO] [ddl.go:679] ["[ddl] DDL job is finished"] [jobID=68]
   > [2024/07/03 14:52:27.916 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/03 14:52:27.916 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=60] ["first split key"=748000000000000043]
   > [2024/07/03 14:52:27.917 +00:00] [WARN] [2pc.go:1800] ["schemaLeaseChecker is not set for this transaction"] [sessionID=5] [startTS=450892489796354049] [checkTS=450892489796354050]
   > [2024/07/03 14:52:27.919 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=62] ["first at"=748000000000000043] ["first new region left"="{Id:62 StartKey:7480000000000000ff3f00000000000000f8 EndKey:7480000000000000ff4300000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:63 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/03 14:52:27.919 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[62]"]
   > [2024/07/03 14:52:28.980 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/07/03 14:52:28.992 +00:00] [INFO] [set.go:139] ["set global var"] [conn=7] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/07/03 14:52:29.584 +00:00] [WARN] [session.go:1866] ["run statement failed"] [conn=7] [schemaVersion=34] [error="[tikv:1292]Truncated incorrect DOUBLE value: '123abc'"] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 7,\n  \"status\": 3,\n  \"strictMode\": true,\n  \"txn\": \"450892490153394176\",\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"127.0.0.1\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/07/03 14:52:29.584 +00:00] [INFO] [conn.go:1123] ["command dispatched failed"] [conn=7] [connInfo="id:7, addr:127.0.0.1:37004 status:11, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:1, autocommit:1"] [sql=" DELETE FROM t WHERE (CAST(('123abc') AS DOUBLE)) IS NULL;"] [txn_mode=OPTIMISTIC] [timestamp=450892490153394176] [err="[tikv:1292]Truncated incorrect DOUBLE value: '123abc'"]
