# Bug ID TIDB-28095-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/28095
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              Should not throw an error on the third scenario.


## Details
 * Database: tidb-v5.2.1
 * Number of scenarios: 3
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
 * Instruction #1:
     - Instruction:  update t set a = 'test' where cast(a as decimal);
     - Transaction: conn_0
     - Output: ERROR: 1105 (HY000): Bad Number
     - Executed order: Not executed

 * Container logs:
   > [2024/07/03 13:29:42.408 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=26] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/07/03 13:29:42.409 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=26] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/07/03 13:29:42.411 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:54, Type:create schema, State:none, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-03 13:29:42.41 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/03 13:29:42.411 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:54, Type:create schema, State:none, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-03 13:29:42.41 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/03 13:29:42.411 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:54, Type:create schema, State:none, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:42.41 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:42.412 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=26] [neededSchemaVersion=27] ["start time"=122.573µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/03 13:29:42.414 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=27] ["take time"=2.274758ms] [job="ID:54, Type:create schema, State:done, SchemaState:public, SchemaID:53, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-03 13:29:42.41 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:42.415 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:54, Type:create schema, State:synced, SchemaState:public, SchemaID:53, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:42.41 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:42.416 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=54]
   > [2024/07/03 13:29:42.416 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/07/03 13:29:42.419 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=27] [cur_db=testdb] [sql="drop table if exists t;"] [user=root@127.0.0.1]
   > [2024/07/03 13:29:42.419 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=27] [cur_db=testdb] [sql="create table t(a varchar(20));"] [user=root@127.0.0.1]
   > [2024/07/03 13:29:42.421 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:56, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:55, RowCount:0, ArgLen:1, start time: 2024-07-03 13:29:42.42 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/03 13:29:42.421 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:56, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:55, RowCount:0, ArgLen:1, start time: 2024-07-03 13:29:42.42 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t(a varchar(20));"]
   > [2024/07/03 13:29:42.421 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:56, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:55, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:42.42 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:42.422 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=27] [neededSchemaVersion=28] ["start time"=233.552µs] [phyTblIDs="[55]"] [actionTypes="[8]"]
   > [2024/07/03 13:29:42.424 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=28] ["take time"=2.090164ms] [job="ID:56, Type:create table, State:done, SchemaState:public, SchemaID:53, TableID:55, RowCount:0, ArgLen:1, start time: 2024-07-03 13:29:42.42 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:42.425 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:56, Type:create table, State:synced, SchemaState:public, SchemaID:53, TableID:55, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:42.42 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:42.426 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=56]
   > [2024/07/03 13:29:42.426 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/07/03 13:29:42.426 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=50] ["first split key"=748000000000000037]
   > [2024/07/03 13:29:42.426 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=50] ["first at"=748000000000000037] ["first new region left"="{Id:50 StartKey:7480000000000000ff3300000000000000f8 EndKey:7480000000000000ff3700000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:51 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/03 13:29:42.426 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[50]"]
   > [2024/07/03 13:29:42.427 +00:00] [WARN] [2pc.go:1598] ["schemaLeaseChecker is not set for this transaction"] [sessionID=5] [startTS=450891188122681346] [commitTS=450891188122943488]
   > [2024/07/03 13:29:43.496 +00:00] [INFO] [set.go:127] ["set global var"] [conn=7] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/07/03 13:29:43.778 +00:00] [INFO] [tidb.go:242] ["rollbackTxn called due to ddl/autocommit failure"]
   > [2024/07/03 13:29:43.778 +00:00] [WARN] [session.go:1683] ["run statement failed"] [conn=7] [schemaVersion=28] [error="[tikv:8029]Bad Number"] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 7,\n  \"status\": 2,\n  \"strictMode\": true,\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"127.0.0.1\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/07/03 13:29:43.779 +00:00] [INFO] [conn.go:995] ["command dispatched failed"] [conn=7] [connInfo="id:7, addr:127.0.0.1:43446 status:10, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:0, autocommit:1"] [sql=" update t set a = 'test' where cast(a as decimal);"] [txn_mode=OPTIMISTIC] [err="[tikv:8029]Bad Number"]

### Scenario 1
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
 * Instruction #1:
     - Instruction:  start transaction;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
 * Instruction #2:
     - Instruction:  update t set a = 'test' where cast(a as decimal);
     - Transaction: conn_0
     - Output: ERROR: 1105 (HY000): Bad Number
     - Executed order: Not executed
 * Instruction #3:
     - Instruction:  rollback;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2

 * Container logs:
   > [2024/07/03 13:29:45.439 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=36] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/07/03 13:29:45.439 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:63, Type:drop schema, State:none, SchemaState:queueing, SchemaID:58, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:45.439 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/03 13:29:45.439 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:63, Type:drop schema, State:none, SchemaState:queueing, SchemaID:58, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:45.439 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/03 13:29:45.440 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:63, Type:drop schema, State:none, SchemaState:queueing, SchemaID:58, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:45.439 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:45.441 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=36] [neededSchemaVersion=37] ["start time"=71.937µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/03 13:29:45.443 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=37] ["take time"=2.235017ms] [job="ID:63, Type:drop schema, State:running, SchemaState:write only, SchemaID:58, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:45.439 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:45.444 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:63, Type:drop schema, State:running, SchemaState:write only, SchemaID:58, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:45.439 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:45.445 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=37] [neededSchemaVersion=38] ["start time"=77.106µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/03 13:29:45.447 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=38] ["take time"=2.298992ms] [job="ID:63, Type:drop schema, State:running, SchemaState:delete only, SchemaID:58, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:45.439 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:45.447 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:63, Type:drop schema, State:running, SchemaState:delete only, SchemaID:58, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:45.439 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:45.449 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=38] [neededSchemaVersion=39] ["start time"=101.271µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/03 13:29:45.451 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=39] ["take time"=2.71155ms] [job="ID:63, Type:drop schema, State:done, SchemaState:queueing, SchemaID:58, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:45.439 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:45.451 +00:00] [INFO] [delete_range.go:106] ["[ddl] add job into delete-range table"] [jobID=63] [jobType="drop schema"]
   > [2024/07/03 13:29:45.451 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:63, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:58, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:45.439 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:45.452 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=63]
   > [2024/07/03 13:29:45.452 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/07/03 13:29:45.453 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=39] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/07/03 13:29:45.455 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:65, Type:create schema, State:none, SchemaState:queueing, SchemaID:64, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-03 13:29:45.454 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/03 13:29:45.455 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:65, Type:create schema, State:none, SchemaState:queueing, SchemaID:64, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-03 13:29:45.454 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/03 13:29:45.455 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:create schema, State:none, SchemaState:queueing, SchemaID:64, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:45.454 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:45.456 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=39] [neededSchemaVersion=40] ["start time"=125.855µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/03 13:29:45.458 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=40] ["take time"=2.139193ms] [job="ID:65, Type:create schema, State:done, SchemaState:public, SchemaID:64, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-03 13:29:45.454 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:45.458 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:create schema, State:synced, SchemaState:public, SchemaID:64, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:45.454 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:45.459 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=65]
   > [2024/07/03 13:29:45.459 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/07/03 13:29:45.461 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=40] [cur_db=testdb] [sql="drop table if exists t;"] [user=root@127.0.0.1]
   > [2024/07/03 13:29:45.461 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=40] [cur_db=testdb] [sql="create table t(a varchar(20));"] [user=root@127.0.0.1]
   > [2024/07/03 13:29:45.462 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:67, Type:create table, State:none, SchemaState:queueing, SchemaID:64, TableID:66, RowCount:0, ArgLen:1, start time: 2024-07-03 13:29:45.462 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/03 13:29:45.462 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:67, Type:create table, State:none, SchemaState:queueing, SchemaID:64, TableID:66, RowCount:0, ArgLen:1, start time: 2024-07-03 13:29:45.462 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t(a varchar(20));"]
   > [2024/07/03 13:29:45.463 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:create table, State:none, SchemaState:queueing, SchemaID:64, TableID:66, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:45.462 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:45.464 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=40] [neededSchemaVersion=41] ["start time"=200.098µs] [phyTblIDs="[66]"] [actionTypes="[8]"]
   > [2024/07/03 13:29:45.466 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=41] ["take time"=2.218046ms] [job="ID:67, Type:create table, State:done, SchemaState:public, SchemaID:64, TableID:66, RowCount:0, ArgLen:1, start time: 2024-07-03 13:29:45.462 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:45.466 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:create table, State:synced, SchemaState:public, SchemaID:64, TableID:66, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:45.462 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:45.467 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=67]
   > [2024/07/03 13:29:45.467 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/07/03 13:29:45.467 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=54] ["first split key"=748000000000000042]
   > [2024/07/03 13:29:45.468 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=54] ["first at"=748000000000000042] ["first new region left"="{Id:54 StartKey:7480000000000000ff3c00000000000000f8 EndKey:7480000000000000ff4200000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:55 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/03 13:29:45.468 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[54]"]
   > [2024/07/03 13:29:45.468 +00:00] [WARN] [2pc.go:1598] ["schemaLeaseChecker is not set for this transaction"] [sessionID=11] [startTS=450891188920123393] [commitTS=450891188920123394]
   > [2024/07/03 13:29:46.534 +00:00] [INFO] [set.go:127] ["set global var"] [conn=13] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/07/03 13:29:47.115 +00:00] [WARN] [session.go:1683] ["run statement failed"] [conn=13] [schemaVersion=41] [error="[tikv:8029]Bad Number"] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 13,\n  \"status\": 3,\n  \"strictMode\": true,\n  \"txn\": \"450891189272707072\",\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"127.0.0.1\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/07/03 13:29:47.115 +00:00] [INFO] [conn.go:995] ["command dispatched failed"] [conn=13] [connInfo="id:13, addr:127.0.0.1:51938 status:11, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:1, autocommit:1"] [sql=" update t set a = 'test' where cast(a as decimal);"] [txn_mode=OPTIMISTIC] [err="[tikv:8029]Bad Number"]

### Scenario 2
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
 * Instruction #1:
     - Instruction:  start transaction;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
 * Instruction #2:
     - Instruction:  update t set a = 'xyz';
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
 * Instruction #3:
     - Instruction:  update t set a = 'test' where cast(a as decimal);
     - Transaction: conn_0
     - Output: ERROR: 8029 (HY000): Bad Number
     - Executed order: Not executed
 * Instruction #4:
     - Instruction:  rollback;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3

 * Container logs:
   > [2024/07/03 13:29:48.122 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=49] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/07/03 13:29:48.123 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:74, Type:drop schema, State:none, SchemaState:queueing, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:48.122 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/03 13:29:48.123 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:74, Type:drop schema, State:none, SchemaState:queueing, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:48.122 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/03 13:29:48.124 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:74, Type:drop schema, State:none, SchemaState:queueing, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:48.122 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:48.125 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=49] [neededSchemaVersion=50] ["start time"=113.493µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/03 13:29:48.127 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=50] ["take time"=2.194439ms] [job="ID:74, Type:drop schema, State:running, SchemaState:write only, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:48.122 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:48.127 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:74, Type:drop schema, State:running, SchemaState:write only, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:48.122 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:48.129 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=50] [neededSchemaVersion=51] ["start time"=86.744µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/03 13:29:48.131 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=51] ["take time"=2.23788ms] [job="ID:74, Type:drop schema, State:running, SchemaState:delete only, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:48.122 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:48.131 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:74, Type:drop schema, State:running, SchemaState:delete only, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:48.122 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:48.132 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=51] [neededSchemaVersion=52] ["start time"=90.166µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/03 13:29:48.135 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=52] ["take time"=2.931134ms] [job="ID:74, Type:drop schema, State:done, SchemaState:queueing, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:48.122 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:48.135 +00:00] [INFO] [delete_range.go:106] ["[ddl] add job into delete-range table"] [jobID=74] [jobType="drop schema"]
   > [2024/07/03 13:29:48.136 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:74, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:48.122 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:48.136 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=74]
   > [2024/07/03 13:29:48.136 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/07/03 13:29:48.138 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=52] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/07/03 13:29:48.139 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:76, Type:create schema, State:none, SchemaState:queueing, SchemaID:75, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-03 13:29:48.138 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/03 13:29:48.139 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:76, Type:create schema, State:none, SchemaState:queueing, SchemaID:75, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-03 13:29:48.138 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/03 13:29:48.139 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:76, Type:create schema, State:none, SchemaState:queueing, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:48.138 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:48.140 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=52] [neededSchemaVersion=53] ["start time"=104.204µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/03 13:29:48.142 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=53] ["take time"=2.293056ms] [job="ID:76, Type:create schema, State:done, SchemaState:public, SchemaID:75, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-03 13:29:48.138 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:48.143 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:76, Type:create schema, State:synced, SchemaState:public, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:48.138 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:48.143 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=76]
   > [2024/07/03 13:29:48.143 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/07/03 13:29:48.146 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=53] [cur_db=testdb] [sql="drop table if exists t;"] [user=root@127.0.0.1]
   > [2024/07/03 13:29:48.146 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=53] [cur_db=testdb] [sql="create table t(a varchar(20));"] [user=root@127.0.0.1]
   > [2024/07/03 13:29:48.147 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:78, Type:create table, State:none, SchemaState:queueing, SchemaID:75, TableID:77, RowCount:0, ArgLen:1, start time: 2024-07-03 13:29:48.147 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/03 13:29:48.147 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:78, Type:create table, State:none, SchemaState:queueing, SchemaID:75, TableID:77, RowCount:0, ArgLen:1, start time: 2024-07-03 13:29:48.147 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t(a varchar(20));"]
   > [2024/07/03 13:29:48.148 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:78, Type:create table, State:none, SchemaState:queueing, SchemaID:75, TableID:77, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:48.147 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:48.149 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=53] [neededSchemaVersion=54] ["start time"=268.404µs] [phyTblIDs="[77]"] [actionTypes="[8]"]
   > [2024/07/03 13:29:48.151 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=54] ["take time"=2.187734ms] [job="ID:78, Type:create table, State:done, SchemaState:public, SchemaID:75, TableID:77, RowCount:0, ArgLen:1, start time: 2024-07-03 13:29:48.147 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:48.152 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:78, Type:create table, State:synced, SchemaState:public, SchemaID:75, TableID:77, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:48.147 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:48.153 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=78]
   > [2024/07/03 13:29:48.153 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/07/03 13:29:48.153 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=58] ["first split key"=74800000000000004d]
   > [2024/07/03 13:29:48.153 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=58] ["first at"=74800000000000004d] ["first new region left"="{Id:58 StartKey:7480000000000000ff4700000000000000f8 EndKey:7480000000000000ff4d00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:59 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/03 13:29:48.153 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[58]"]
   > [2024/07/03 13:29:48.154 +00:00] [WARN] [2pc.go:1598] ["schemaLeaseChecker is not set for this transaction"] [sessionID=17] [startTS=450891189624242177] [commitTS=450891189624242178]
   > [2024/07/03 13:29:49.220 +00:00] [INFO] [set.go:127] ["set global var"] [conn=19] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/07/03 13:29:50.101 +00:00] [WARN] [session.go:1683] ["run statement failed"] [conn=19] [schemaVersion=54] [error="[types:8029]Bad Number"] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 19,\n  \"status\": 3,\n  \"strictMode\": true,\n  \"txn\": \"450891189976563712\",\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"127.0.0.1\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/07/03 13:29:50.101 +00:00] [INFO] [conn.go:995] ["command dispatched failed"] [conn=19] [connInfo="id:19, addr:127.0.0.1:51948 status:11, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:1, autocommit:1"] [sql=" update t set a = 'test' where cast(a as decimal);"] [txn_mode=OPTIMISTIC] [err="[types:8029]Bad Number"]
