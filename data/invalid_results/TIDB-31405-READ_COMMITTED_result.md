# Bug ID TIDB-31405-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/31405
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              Error on the first scenario


## Details
 * Database: tidb-v5.3.0
 * Number of scenarios: 1
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  INSERT INTO t0 VALUES(1.0);
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 1 / 0
 * Instruction #1:
     - Instruction:  UPDATE t0 SET c0 = c0 + 1 WHERE c0 > 'a';
     - Transaction: conn_0
     - Output: ERROR: 1105 (HY000): Bad Number
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0

 * Container logs:
   > [2024/07/04 10:55:20.263 +00:00] [INFO] [session.go:2834] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=37] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/07/04 10:55:20.264 +00:00] [INFO] [ddl_worker.go:319] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:65, Type:drop schema, State:none, SchemaState:queueing, SchemaID:60, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-04 10:55:20.263 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/04 10:55:20.264 +00:00] [INFO] [ddl.go:549] ["[ddl] start DDL job"] [job="ID:65, Type:drop schema, State:none, SchemaState:queueing, SchemaID:60, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-04 10:55:20.263 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/04 10:55:20.264 +00:00] [INFO] [ddl_worker.go:728] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:drop schema, State:none, SchemaState:queueing, SchemaID:60, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-04 10:55:20.263 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 10:55:20.265 +00:00] [INFO] [domain.go:130] ["diff load InfoSchema success"] [currentSchemaVersion=37] [neededSchemaVersion=38] ["start time"=97.709µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/04 10:55:20.267 +00:00] [INFO] [ddl_worker.go:919] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=38] ["take time"=2.278666ms] [job="ID:65, Type:drop schema, State:running, SchemaState:write only, SchemaID:60, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-04 10:55:20.263 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 10:55:20.268 +00:00] [INFO] [ddl_worker.go:728] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:drop schema, State:running, SchemaState:write only, SchemaID:60, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-04 10:55:20.263 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 10:55:20.269 +00:00] [INFO] [domain.go:130] ["diff load InfoSchema success"] [currentSchemaVersion=38] [neededSchemaVersion=39] ["start time"=105.321µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/04 10:55:20.271 +00:00] [INFO] [ddl_worker.go:919] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=39] ["take time"=2.142963ms] [job="ID:65, Type:drop schema, State:running, SchemaState:delete only, SchemaID:60, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-04 10:55:20.263 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 10:55:20.271 +00:00] [INFO] [ddl_worker.go:728] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:drop schema, State:running, SchemaState:delete only, SchemaID:60, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-04 10:55:20.263 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 10:55:20.273 +00:00] [INFO] [domain.go:130] ["diff load InfoSchema success"] [currentSchemaVersion=39] [neededSchemaVersion=40] ["start time"=102.598µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/04 10:55:20.275 +00:00] [INFO] [ddl_worker.go:919] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=40] ["take time"=2.237739ms] [job="ID:65, Type:drop schema, State:done, SchemaState:queueing, SchemaID:60, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-04 10:55:20.263 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 10:55:20.275 +00:00] [INFO] [delete_range.go:107] ["[ddl] add job into delete-range table"] [jobID=65] [jobType="drop schema"]
   > [2024/07/04 10:55:20.275 +00:00] [INFO] [ddl_worker.go:424] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:60, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-04 10:55:20.263 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 10:55:20.276 +00:00] [INFO] [ddl.go:604] ["[ddl] DDL job is finished"] [jobID=65]
   > [2024/07/04 10:55:20.276 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/04 10:55:20.277 +00:00] [INFO] [session.go:2834] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=40] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/07/04 10:55:20.279 +00:00] [INFO] [ddl_worker.go:319] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:67, Type:create schema, State:none, SchemaState:queueing, SchemaID:66, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-04 10:55:20.278 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/04 10:55:20.279 +00:00] [INFO] [ddl.go:549] ["[ddl] start DDL job"] [job="ID:67, Type:create schema, State:none, SchemaState:queueing, SchemaID:66, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-04 10:55:20.278 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/04 10:55:20.279 +00:00] [INFO] [ddl_worker.go:728] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:create schema, State:none, SchemaState:queueing, SchemaID:66, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-04 10:55:20.278 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 10:55:20.280 +00:00] [INFO] [domain.go:130] ["diff load InfoSchema success"] [currentSchemaVersion=40] [neededSchemaVersion=41] ["start time"=184.733µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/04 10:55:20.282 +00:00] [INFO] [ddl_worker.go:919] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=41] ["take time"=2.409201ms] [job="ID:67, Type:create schema, State:done, SchemaState:public, SchemaID:66, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-04 10:55:20.278 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 10:55:20.283 +00:00] [INFO] [ddl_worker.go:424] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:create schema, State:synced, SchemaState:public, SchemaID:66, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-04 10:55:20.278 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 10:55:20.284 +00:00] [INFO] [ddl.go:604] ["[ddl] DDL job is finished"] [jobID=67]
   > [2024/07/04 10:55:20.284 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/04 10:55:20.286 +00:00] [INFO] [session.go:2834] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=41] [cur_db=testdb] [sql="DROP TABLE IF EXISTS t0;"] [user=root@127.0.0.1]
   > [2024/07/04 10:55:20.287 +00:00] [INFO] [session.go:2834] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=41] [cur_db=testdb] [sql="CREATE TABLE t0(c0 DECIMAL);"] [user=root@127.0.0.1]
   > [2024/07/04 10:55:20.288 +00:00] [INFO] [ddl_worker.go:319] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:69, Type:create table, State:none, SchemaState:queueing, SchemaID:66, TableID:68, RowCount:0, ArgLen:1, start time: 2024-07-04 10:55:20.287 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/04 10:55:20.288 +00:00] [INFO] [ddl.go:549] ["[ddl] start DDL job"] [job="ID:69, Type:create table, State:none, SchemaState:queueing, SchemaID:66, TableID:68, RowCount:0, ArgLen:1, start time: 2024-07-04 10:55:20.287 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE t0(c0 DECIMAL);"]
   > [2024/07/04 10:55:20.288 +00:00] [INFO] [ddl_worker.go:728] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:69, Type:create table, State:none, SchemaState:queueing, SchemaID:66, TableID:68, RowCount:0, ArgLen:0, start time: 2024-07-04 10:55:20.287 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 10:55:20.290 +00:00] [INFO] [domain.go:130] ["diff load InfoSchema success"] [currentSchemaVersion=41] [neededSchemaVersion=42] ["start time"=277.203µs] [phyTblIDs="[68]"] [actionTypes="[8]"]
   > [2024/07/04 10:55:20.292 +00:00] [INFO] [ddl_worker.go:919] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=42] ["take time"=2.247378ms] [job="ID:69, Type:create table, State:done, SchemaState:public, SchemaID:66, TableID:68, RowCount:0, ArgLen:1, start time: 2024-07-04 10:55:20.287 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 10:55:20.292 +00:00] [INFO] [ddl_worker.go:424] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:69, Type:create table, State:synced, SchemaState:public, SchemaID:66, TableID:68, RowCount:0, ArgLen:0, start time: 2024-07-04 10:55:20.287 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 10:55:20.293 +00:00] [INFO] [ddl.go:604] ["[ddl] DDL job is finished"] [jobID=69]
   > [2024/07/04 10:55:20.293 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/04 10:55:20.293 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=56] ["first split key"=748000000000000044]
   > [2024/07/04 10:55:20.294 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=56] ["first at"=748000000000000044] ["first new region left"="{Id:56 StartKey:7480000000000000ff3e00000000000000f8 EndKey:7480000000000000ff4400000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:57 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/04 10:55:20.294 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[56]"]
   > [2024/07/04 10:55:21.416 +00:00] [WARN] [2pc.go:1601] ["schemaLeaseChecker is not set for this transaction"] [sessionID=13] [startTS=450911409645813761] [commitTS=450911409646075904]
   > [2024/07/04 10:55:21.641 +00:00] [INFO] [tidb.go:243] ["rollbackTxn called due to ddl/autocommit failure"]
   > [2024/07/04 10:55:21.641 +00:00] [WARN] [session.go:1571] ["run statement failed"] [conn=13] [schemaVersion=42] [error="[tikv:8029]Bad Number"] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 13,\n  \"status\": 2,\n  \"strictMode\": true,\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"127.0.0.1\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/07/04 10:55:21.642 +00:00] [INFO] [conn.go:997] ["command dispatched failed"] [conn=13] [connInfo="id:13, addr:127.0.0.1:60476 status:10, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:0, autocommit:1"] [sql=" UPDATE t0 SET c0 = c0 + 1 WHERE c0 > 'a';"] [txn_mode=OPTIMISTIC] [err="[tikv:8029]Bad Number"]
