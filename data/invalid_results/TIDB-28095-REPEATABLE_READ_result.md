# Bug ID TIDB-28095-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/28095
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              Should not throw an error on the third scenario.


## Details
 * Database: tidb-v5.2.1.remote
 * Number of scenarios: 3
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 0 / 0
 * Instruction #1:
     - Instruction:  update t set a = 'test' where cast(a as decimal);
     - Transaction: conn_0
     - Output: ERROR: 1105 (HY000): Bad Number
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0

 * Container logs:
   > [2024/07/04 11:07:48.504 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=26] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/07/04 11:07:48.505 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=26] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/07/04 11:07:48.507 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:54, Type:create schema, State:none, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-04 11:07:48.506 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/04 11:07:48.507 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:54, Type:create schema, State:none, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-04 11:07:48.506 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/04 11:07:48.507 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:54, Type:create schema, State:none, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-04 11:07:48.506 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 11:07:48.508 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=26] [neededSchemaVersion=27] ["start time"=160.986µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/04 11:07:48.511 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=27] ["take time"=2.699185ms] [job="ID:54, Type:create schema, State:done, SchemaState:public, SchemaID:53, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-04 11:07:48.506 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 11:07:48.512 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:54, Type:create schema, State:synced, SchemaState:public, SchemaID:53, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-04 11:07:48.506 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 11:07:48.512 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=54]
   > [2024/07/04 11:07:48.512 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/07/04 11:07:48.514 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=27] [cur_db=testdb] [sql="drop table if exists t;"] [user=root@127.0.0.1]
   > [2024/07/04 11:07:48.515 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=27] [cur_db=testdb] [sql="create table t(a varchar(20));"] [user=root@127.0.0.1]
   > [2024/07/04 11:07:48.516 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:56, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:55, RowCount:0, ArgLen:1, start time: 2024-07-04 11:07:48.515 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/04 11:07:48.516 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:56, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:55, RowCount:0, ArgLen:1, start time: 2024-07-04 11:07:48.515 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t(a varchar(20));"]
   > [2024/07/04 11:07:48.516 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:56, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:55, RowCount:0, ArgLen:0, start time: 2024-07-04 11:07:48.515 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 11:07:48.518 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=27] [neededSchemaVersion=28] ["start time"=285.025µs] [phyTblIDs="[55]"] [actionTypes="[8]"]
   > [2024/07/04 11:07:48.520 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=28] ["take time"=2.070398ms] [job="ID:56, Type:create table, State:done, SchemaState:public, SchemaID:53, TableID:55, RowCount:0, ArgLen:1, start time: 2024-07-04 11:07:48.515 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 11:07:48.520 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:56, Type:create table, State:synced, SchemaState:public, SchemaID:53, TableID:55, RowCount:0, ArgLen:0, start time: 2024-07-04 11:07:48.515 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 11:07:48.520 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=56]
   > [2024/07/04 11:07:48.520 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/07/04 11:07:48.521 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=50] ["first split key"=748000000000000037]
   > [2024/07/04 11:07:48.521 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=50] ["first at"=748000000000000037] ["first new region left"="{Id:50 StartKey:7480000000000000ff3300000000000000f8 EndKey:7480000000000000ff3700000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:51 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/04 11:07:48.521 +00:00] [WARN] [2pc.go:1598] ["schemaLeaseChecker is not set for this transaction"] [sessionID=5] [startTS=450911605495169025] [commitTS=450911605495169026]
   > [2024/07/04 11:07:48.521 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[50]"]
   > [2024/07/04 11:07:49.579 +00:00] [INFO] [set.go:127] ["set global var"] [conn=7] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/07/04 11:07:49.868 +00:00] [INFO] [tidb.go:242] ["rollbackTxn called due to ddl/autocommit failure"]
   > [2024/07/04 11:07:49.869 +00:00] [WARN] [session.go:1683] ["run statement failed"] [conn=7] [schemaVersion=28] [error="[tikv:8029]Bad Number"] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 7,\n  \"status\": 2,\n  \"strictMode\": true,\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"127.0.0.1\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/07/04 11:07:49.869 +00:00] [INFO] [conn.go:995] ["command dispatched failed"] [conn=7] [connInfo="id:7, addr:127.0.0.1:43350 status:10, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:0, autocommit:1"] [sql=" update t set a = 'test' where cast(a as decimal);"] [txn_mode=OPTIMISTIC] [err="[tikv:8029]Bad Number"]

### Scenario 1
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 0 / 0
 * Instruction #1:
     - Instruction:  start transaction;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  update t set a = 'test' where cast(a as decimal);
     - Transaction: conn_0
     - Output: ERROR: 1105 (HY000): Bad Number
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #3:
     - Instruction:  rollback;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 0 / 0

 * Container logs:
   > [2024/07/04 11:07:51.447 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=36] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/07/04 11:07:51.448 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:63, Type:drop schema, State:none, SchemaState:queueing, SchemaID:58, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-04 11:07:51.447 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/04 11:07:51.448 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:63, Type:drop schema, State:none, SchemaState:queueing, SchemaID:58, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-04 11:07:51.447 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/04 11:07:51.448 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:63, Type:drop schema, State:none, SchemaState:queueing, SchemaID:58, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-04 11:07:51.447 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 11:07:51.449 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=36] [neededSchemaVersion=37] ["start time"=119.291µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/04 11:07:51.451 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=37] ["take time"=2.255409ms] [job="ID:63, Type:drop schema, State:running, SchemaState:write only, SchemaID:58, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-04 11:07:51.447 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 11:07:51.452 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:63, Type:drop schema, State:running, SchemaState:write only, SchemaID:58, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-04 11:07:51.447 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 11:07:51.453 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=37] [neededSchemaVersion=38] ["start time"=74.87µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/04 11:07:51.455 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=38] ["take time"=2.239346ms] [job="ID:63, Type:drop schema, State:running, SchemaState:delete only, SchemaID:58, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-04 11:07:51.447 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 11:07:51.455 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:63, Type:drop schema, State:running, SchemaState:delete only, SchemaID:58, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-04 11:07:51.447 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 11:07:51.456 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=38] [neededSchemaVersion=39] ["start time"=113.913µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/04 11:07:51.458 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=39] ["take time"=2.209942ms] [job="ID:63, Type:drop schema, State:done, SchemaState:queueing, SchemaID:58, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-04 11:07:51.447 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 11:07:51.458 +00:00] [INFO] [delete_range.go:106] ["[ddl] add job into delete-range table"] [jobID=63] [jobType="drop schema"]
   > [2024/07/04 11:07:51.459 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:63, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:58, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-04 11:07:51.447 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 11:07:51.460 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=63]
   > [2024/07/04 11:07:51.460 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/07/04 11:07:51.461 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=39] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/07/04 11:07:51.462 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:65, Type:create schema, State:none, SchemaState:queueing, SchemaID:64, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-04 11:07:51.462 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/04 11:07:51.462 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:65, Type:create schema, State:none, SchemaState:queueing, SchemaID:64, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-04 11:07:51.462 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/04 11:07:51.463 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:create schema, State:none, SchemaState:queueing, SchemaID:64, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-04 11:07:51.462 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 11:07:51.464 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=39] [neededSchemaVersion=40] ["start time"=177.539µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/04 11:07:51.466 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=40] ["take time"=2.242139ms] [job="ID:65, Type:create schema, State:done, SchemaState:public, SchemaID:64, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-04 11:07:51.462 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 11:07:51.466 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:create schema, State:synced, SchemaState:public, SchemaID:64, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-04 11:07:51.462 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 11:07:51.467 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=65]
   > [2024/07/04 11:07:51.467 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/07/04 11:07:51.469 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=40] [cur_db=testdb] [sql="drop table if exists t;"] [user=root@127.0.0.1]
   > [2024/07/04 11:07:51.470 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=40] [cur_db=testdb] [sql="create table t(a varchar(20));"] [user=root@127.0.0.1]
   > [2024/07/04 11:07:51.471 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:67, Type:create table, State:none, SchemaState:queueing, SchemaID:64, TableID:66, RowCount:0, ArgLen:1, start time: 2024-07-04 11:07:51.47 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/04 11:07:51.471 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:67, Type:create table, State:none, SchemaState:queueing, SchemaID:64, TableID:66, RowCount:0, ArgLen:1, start time: 2024-07-04 11:07:51.47 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t(a varchar(20));"]
   > [2024/07/04 11:07:51.472 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:create table, State:none, SchemaState:queueing, SchemaID:64, TableID:66, RowCount:0, ArgLen:0, start time: 2024-07-04 11:07:51.47 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 11:07:51.473 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=40] [neededSchemaVersion=41] ["start time"=331.679µs] [phyTblIDs="[66]"] [actionTypes="[8]"]
   > [2024/07/04 11:07:51.475 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=41] ["take time"=2.232221ms] [job="ID:67, Type:create table, State:done, SchemaState:public, SchemaID:64, TableID:66, RowCount:0, ArgLen:1, start time: 2024-07-04 11:07:51.47 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 11:07:51.476 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:create table, State:synced, SchemaState:public, SchemaID:64, TableID:66, RowCount:0, ArgLen:0, start time: 2024-07-04 11:07:51.47 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 11:07:51.477 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=67]
   > [2024/07/04 11:07:51.477 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/07/04 11:07:51.477 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=54] ["first split key"=748000000000000042]
   > [2024/07/04 11:07:51.477 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=54] ["first at"=748000000000000042] ["first new region left"="{Id:54 StartKey:7480000000000000ff3c00000000000000f8 EndKey:7480000000000000ff4200000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:55 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/04 11:07:51.477 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[54]"]
   > [2024/07/04 11:07:51.478 +00:00] [WARN] [2pc.go:1598] ["schemaLeaseChecker is not set for this transaction"] [sessionID=11] [startTS=450911606270066690] [commitTS=450911606270328832]
   > [2024/07/04 11:07:52.538 +00:00] [INFO] [set.go:127] ["set global var"] [conn=13] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/07/04 11:07:53.121 +00:00] [WARN] [session.go:1683] ["run statement failed"] [conn=13] [schemaVersion=41] [error="[tikv:8029]Bad Number"] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 13,\n  \"status\": 3,\n  \"strictMode\": true,\n  \"txn\": \"450911606621863936\",\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"127.0.0.1\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/07/04 11:07:53.121 +00:00] [INFO] [conn.go:995] ["command dispatched failed"] [conn=13] [connInfo="id:13, addr:127.0.0.1:43374 status:11, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:1, autocommit:1"] [sql=" update t set a = 'test' where cast(a as decimal);"] [txn_mode=OPTIMISTIC] [err="[tikv:8029]Bad Number"]

### Scenario 2
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 0 / 0
 * Instruction #1:
     - Instruction:  start transaction;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  update t set a = 'xyz';
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 2 / 0
 * Instruction #3:
     - Instruction:  update t set a = 'test' where cast(a as decimal);
     - Transaction: conn_0
     - Output: ERROR: 8029 (HY000): Bad Number
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #4:
     - Instruction:  rollback;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 0 / 0

 * Container logs:
   > [2024/07/04 11:07:54.091 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=49] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/07/04 11:07:54.091 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:74, Type:drop schema, State:none, SchemaState:queueing, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-04 11:07:54.091 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/04 11:07:54.091 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:74, Type:drop schema, State:none, SchemaState:queueing, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-04 11:07:54.091 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/04 11:07:54.092 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:74, Type:drop schema, State:none, SchemaState:queueing, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-04 11:07:54.091 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 11:07:54.092 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=49] [neededSchemaVersion=50] ["start time"=91.563µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/04 11:07:54.095 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=50] ["take time"=2.202329ms] [job="ID:74, Type:drop schema, State:running, SchemaState:write only, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-04 11:07:54.091 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 11:07:54.095 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:74, Type:drop schema, State:running, SchemaState:write only, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-04 11:07:54.091 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 11:07:54.095 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=50] [neededSchemaVersion=51] ["start time"=75.918µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/04 11:07:54.098 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=51] ["take time"=2.507748ms] [job="ID:74, Type:drop schema, State:running, SchemaState:delete only, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-04 11:07:54.091 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 11:07:54.098 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:74, Type:drop schema, State:running, SchemaState:delete only, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-04 11:07:54.091 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 11:07:54.099 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=51] [neededSchemaVersion=52] ["start time"=61.95µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/04 11:07:54.101 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=52] ["take time"=2.266375ms] [job="ID:74, Type:drop schema, State:done, SchemaState:queueing, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-04 11:07:54.091 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 11:07:54.101 +00:00] [INFO] [delete_range.go:106] ["[ddl] add job into delete-range table"] [jobID=74] [jobType="drop schema"]
   > [2024/07/04 11:07:54.101 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:74, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-04 11:07:54.091 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 11:07:54.102 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=74]
   > [2024/07/04 11:07:54.102 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/07/04 11:07:54.103 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=52] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/07/04 11:07:54.104 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:76, Type:create schema, State:none, SchemaState:queueing, SchemaID:75, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-04 11:07:54.104 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/04 11:07:54.104 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:76, Type:create schema, State:none, SchemaState:queueing, SchemaID:75, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-04 11:07:54.104 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/04 11:07:54.105 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:76, Type:create schema, State:none, SchemaState:queueing, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-04 11:07:54.104 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 11:07:54.106 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=52] [neededSchemaVersion=53] ["start time"=184.173µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/04 11:07:54.108 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=53] ["take time"=2.227821ms] [job="ID:76, Type:create schema, State:done, SchemaState:public, SchemaID:75, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-04 11:07:54.104 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 11:07:54.108 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:76, Type:create schema, State:synced, SchemaState:public, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-04 11:07:54.104 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 11:07:54.109 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=76]
   > [2024/07/04 11:07:54.109 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/07/04 11:07:54.110 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=53] [cur_db=testdb] [sql="drop table if exists t;"] [user=root@127.0.0.1]
   > [2024/07/04 11:07:54.111 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=53] [cur_db=testdb] [sql="create table t(a varchar(20));"] [user=root@127.0.0.1]
   > [2024/07/04 11:07:54.111 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:78, Type:create table, State:none, SchemaState:queueing, SchemaID:75, TableID:77, RowCount:0, ArgLen:1, start time: 2024-07-04 11:07:54.111 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/04 11:07:54.112 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:78, Type:create table, State:none, SchemaState:queueing, SchemaID:75, TableID:77, RowCount:0, ArgLen:1, start time: 2024-07-04 11:07:54.111 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t(a varchar(20));"]
   > [2024/07/04 11:07:54.112 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:78, Type:create table, State:none, SchemaState:queueing, SchemaID:75, TableID:77, RowCount:0, ArgLen:0, start time: 2024-07-04 11:07:54.111 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 11:07:54.112 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=53] [neededSchemaVersion=54] ["start time"=177.329µs] [phyTblIDs="[77]"] [actionTypes="[8]"]
   > [2024/07/04 11:07:54.114 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=54] ["take time"=2.183052ms] [job="ID:78, Type:create table, State:done, SchemaState:public, SchemaID:75, TableID:77, RowCount:0, ArgLen:1, start time: 2024-07-04 11:07:54.111 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 11:07:54.115 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:78, Type:create table, State:synced, SchemaState:public, SchemaID:75, TableID:77, RowCount:0, ArgLen:0, start time: 2024-07-04 11:07:54.111 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 11:07:54.115 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=78]
   > [2024/07/04 11:07:54.115 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/07/04 11:07:54.115 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=58] ["first split key"=74800000000000004d]
   > [2024/07/04 11:07:54.116 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=58] ["first at"=74800000000000004d] ["first new region left"="{Id:58 StartKey:7480000000000000ff4700000000000000f8 EndKey:7480000000000000ff4d00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:59 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/04 11:07:54.116 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[58]"]
   > [2024/07/04 11:07:54.116 +00:00] [WARN] [2pc.go:1598] ["schemaLeaseChecker is not set for this transaction"] [sessionID=17] [startTS=450911606961864704] [commitTS=450911606961864705]
   > [2024/07/04 11:07:55.182 +00:00] [INFO] [set.go:127] ["set global var"] [conn=19] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/07/04 11:07:56.065 +00:00] [WARN] [session.go:1683] ["run statement failed"] [conn=19] [schemaVersion=54] [error="[types:8029]Bad Number"] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 19,\n  \"status\": 3,\n  \"strictMode\": true,\n  \"txn\": \"450911607314710528\",\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"127.0.0.1\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/07/04 11:07:56.065 +00:00] [INFO] [conn.go:995] ["command dispatched failed"] [conn=19] [connInfo="id:19, addr:127.0.0.1:43402 status:11, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:1, autocommit:1"] [sql=" update t set a = 'test' where cast(a as decimal);"] [txn_mode=OPTIMISTIC] [err="[types:8029]Bad Number"]
