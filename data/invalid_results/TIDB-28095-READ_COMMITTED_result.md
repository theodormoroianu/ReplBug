# Bug ID TIDB-28095-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/28095
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              Should not throw an error on the third scenario.


## Details
 * Database: tidb-v5.2.1
 * Number of scenarios: 3
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
 * Instruction #1:
     - Instruction:  update t set a = 'test' where cast(a as decimal);
     - Transaction: conn_0
     - Output: ERROR: 1105 (HY000): Bad Number
     - Executed order: Not executed

 * Container logs:
   > [2024/07/03 13:29:51.211 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=23] [schemaVersion=62] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/07/03 13:29:51.212 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:85, Type:drop schema, State:none, SchemaState:queueing, SchemaID:80, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:51.211 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/03 13:29:51.212 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:85, Type:drop schema, State:none, SchemaState:queueing, SchemaID:80, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:51.211 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/03 13:29:51.213 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:85, Type:drop schema, State:none, SchemaState:queueing, SchemaID:80, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:51.211 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:51.214 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=62] [neededSchemaVersion=63] ["start time"=118.801µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/03 13:29:51.216 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=63] ["take time"=2.296548ms] [job="ID:85, Type:drop schema, State:running, SchemaState:write only, SchemaID:80, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:51.211 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:51.217 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:85, Type:drop schema, State:running, SchemaState:write only, SchemaID:80, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:51.211 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:51.218 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=63] [neededSchemaVersion=64] ["start time"=99.804µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/03 13:29:51.220 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=64] ["take time"=2.267075ms] [job="ID:85, Type:drop schema, State:running, SchemaState:delete only, SchemaID:80, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:51.211 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:51.220 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:85, Type:drop schema, State:running, SchemaState:delete only, SchemaID:80, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:51.211 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:51.222 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=64] [neededSchemaVersion=65] ["start time"=90.725µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/03 13:29:51.224 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=65] ["take time"=2.76456ms] [job="ID:85, Type:drop schema, State:done, SchemaState:queueing, SchemaID:80, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:51.211 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:51.225 +00:00] [INFO] [delete_range.go:106] ["[ddl] add job into delete-range table"] [jobID=85] [jobType="drop schema"]
   > [2024/07/03 13:29:51.225 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:85, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:80, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:51.211 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:51.226 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=85]
   > [2024/07/03 13:29:51.226 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/07/03 13:29:51.228 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=23] [schemaVersion=65] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/07/03 13:29:51.229 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:87, Type:create schema, State:none, SchemaState:queueing, SchemaID:86, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-03 13:29:51.228 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/03 13:29:51.229 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:87, Type:create schema, State:none, SchemaState:queueing, SchemaID:86, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-03 13:29:51.228 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/03 13:29:51.230 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:87, Type:create schema, State:none, SchemaState:queueing, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:51.228 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:51.232 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=65] [neededSchemaVersion=66] ["start time"=168.39µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/03 13:29:51.234 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=66] ["take time"=2.305279ms] [job="ID:87, Type:create schema, State:done, SchemaState:public, SchemaID:86, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-03 13:29:51.228 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:51.234 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:87, Type:create schema, State:synced, SchemaState:public, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:51.228 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:51.235 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=87]
   > [2024/07/03 13:29:51.236 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/07/03 13:29:51.239 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=23] [schemaVersion=66] [cur_db=testdb] [sql="drop table if exists t;"] [user=root@127.0.0.1]
   > [2024/07/03 13:29:51.239 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=23] [schemaVersion=66] [cur_db=testdb] [sql="create table t(a varchar(20));"] [user=root@127.0.0.1]
   > [2024/07/03 13:29:51.241 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:89, Type:create table, State:none, SchemaState:queueing, SchemaID:86, TableID:88, RowCount:0, ArgLen:1, start time: 2024-07-03 13:29:51.24 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/03 13:29:51.241 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:89, Type:create table, State:none, SchemaState:queueing, SchemaID:86, TableID:88, RowCount:0, ArgLen:1, start time: 2024-07-03 13:29:51.24 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t(a varchar(20));"]
   > [2024/07/03 13:29:51.242 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:89, Type:create table, State:none, SchemaState:queueing, SchemaID:86, TableID:88, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:51.24 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:51.244 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=66] [neededSchemaVersion=67] ["start time"=462.494µs] [phyTblIDs="[88]"] [actionTypes="[8]"]
   > [2024/07/03 13:29:51.246 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=67] ["take time"=2.252966ms] [job="ID:89, Type:create table, State:done, SchemaState:public, SchemaID:86, TableID:88, RowCount:0, ArgLen:1, start time: 2024-07-03 13:29:51.24 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:51.247 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:89, Type:create table, State:synced, SchemaState:public, SchemaID:86, TableID:88, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:51.24 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:51.248 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=89]
   > [2024/07/03 13:29:51.248 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/07/03 13:29:51.248 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=62] ["first split key"=748000000000000058]
   > [2024/07/03 13:29:51.249 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=62] ["first at"=748000000000000058] ["first new region left"="{Id:62 StartKey:7480000000000000ff5200000000000000f8 EndKey:7480000000000000ff5800000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:63 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/03 13:29:51.249 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[62]"]
   > [2024/07/03 13:29:51.249 +00:00] [WARN] [2pc.go:1598] ["schemaLeaseChecker is not set for this transaction"] [sessionID=23] [startTS=450891190435577857] [commitTS=450891190435577858]
   > [2024/07/03 13:29:52.316 +00:00] [INFO] [set.go:127] ["set global var"] [conn=25] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/07/03 13:29:52.593 +00:00] [INFO] [tidb.go:242] ["rollbackTxn called due to ddl/autocommit failure"]
   > [2024/07/03 13:29:52.594 +00:00] [WARN] [session.go:1683] ["run statement failed"] [conn=25] [schemaVersion=67] [error="[tikv:8029]Bad Number"] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 25,\n  \"status\": 2,\n  \"strictMode\": true,\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"127.0.0.1\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/07/03 13:29:52.594 +00:00] [INFO] [conn.go:995] ["command dispatched failed"] [conn=25] [connInfo="id:25, addr:127.0.0.1:51972 status:10, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:0, autocommit:1"] [sql=" update t set a = 'test' where cast(a as decimal);"] [txn_mode=OPTIMISTIC] [err="[tikv:8029]Bad Number"]

### Scenario 1
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
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
   > [2024/07/03 13:29:54.504 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=29] [schemaVersion=75] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/07/03 13:29:54.505 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:96, Type:drop schema, State:none, SchemaState:queueing, SchemaID:91, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:54.504 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/03 13:29:54.505 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:96, Type:drop schema, State:none, SchemaState:queueing, SchemaID:91, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:54.504 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/03 13:29:54.505 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:96, Type:drop schema, State:none, SchemaState:queueing, SchemaID:91, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:54.504 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:54.507 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=75] [neededSchemaVersion=76] ["start time"=99.175µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/03 13:29:54.509 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=76] ["take time"=2.256948ms] [job="ID:96, Type:drop schema, State:running, SchemaState:write only, SchemaID:91, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:54.504 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:54.509 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:96, Type:drop schema, State:running, SchemaState:write only, SchemaID:91, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:54.504 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:54.510 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=76] [neededSchemaVersion=77] ["start time"=138.916µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/03 13:29:54.513 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=77] ["take time"=3.001115ms] [job="ID:96, Type:drop schema, State:running, SchemaState:delete only, SchemaID:91, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:54.504 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:54.513 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:96, Type:drop schema, State:running, SchemaState:delete only, SchemaID:91, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:54.504 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:54.514 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=77] [neededSchemaVersion=78] ["start time"=127.95µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/03 13:29:54.516 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=78] ["take time"=2.027097ms] [job="ID:96, Type:drop schema, State:done, SchemaState:queueing, SchemaID:91, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:54.504 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:54.517 +00:00] [INFO] [delete_range.go:106] ["[ddl] add job into delete-range table"] [jobID=96] [jobType="drop schema"]
   > [2024/07/03 13:29:54.517 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:96, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:91, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:54.504 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:54.518 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=96]
   > [2024/07/03 13:29:54.518 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/07/03 13:29:54.520 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=29] [schemaVersion=78] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/07/03 13:29:54.521 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:98, Type:create schema, State:none, SchemaState:queueing, SchemaID:97, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-03 13:29:54.52 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/03 13:29:54.521 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:98, Type:create schema, State:none, SchemaState:queueing, SchemaID:97, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-03 13:29:54.52 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/03 13:29:54.522 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:98, Type:create schema, State:none, SchemaState:queueing, SchemaID:97, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:54.52 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:54.523 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=78] [neededSchemaVersion=79] ["start time"=181.45µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/03 13:29:54.525 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=79] ["take time"=2.272452ms] [job="ID:98, Type:create schema, State:done, SchemaState:public, SchemaID:97, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-03 13:29:54.52 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:54.526 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:98, Type:create schema, State:synced, SchemaState:public, SchemaID:97, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:54.52 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:54.526 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=98]
   > [2024/07/03 13:29:54.526 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/07/03 13:29:54.530 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=29] [schemaVersion=79] [cur_db=testdb] [sql="drop table if exists t;"] [user=root@127.0.0.1]
   > [2024/07/03 13:29:54.530 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=29] [schemaVersion=79] [cur_db=testdb] [sql="create table t(a varchar(20));"] [user=root@127.0.0.1]
   > [2024/07/03 13:29:54.532 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:100, Type:create table, State:none, SchemaState:queueing, SchemaID:97, TableID:99, RowCount:0, ArgLen:1, start time: 2024-07-03 13:29:54.531 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/03 13:29:54.532 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:100, Type:create table, State:none, SchemaState:queueing, SchemaID:97, TableID:99, RowCount:0, ArgLen:1, start time: 2024-07-03 13:29:54.531 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t(a varchar(20));"]
   > [2024/07/03 13:29:54.532 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:100, Type:create table, State:none, SchemaState:queueing, SchemaID:97, TableID:99, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:54.531 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:54.534 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=79] [neededSchemaVersion=80] ["start time"=307.794µs] [phyTblIDs="[99]"] [actionTypes="[8]"]
   > [2024/07/03 13:29:54.536 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=80] ["take time"=2.369184ms] [job="ID:100, Type:create table, State:done, SchemaState:public, SchemaID:97, TableID:99, RowCount:0, ArgLen:1, start time: 2024-07-03 13:29:54.531 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:54.537 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:100, Type:create table, State:synced, SchemaState:public, SchemaID:97, TableID:99, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:54.531 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:54.538 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=100]
   > [2024/07/03 13:29:54.538 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/07/03 13:29:54.538 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=66] ["first split key"=748000000000000063]
   > [2024/07/03 13:29:54.538 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=66] ["first at"=748000000000000063] ["first new region left"="{Id:66 StartKey:7480000000000000ff5d00000000000000f8 EndKey:7480000000000000ff6300000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:67 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/03 13:29:54.538 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[66]"]
   > [2024/07/03 13:29:54.539 +00:00] [WARN] [2pc.go:1598] ["schemaLeaseChecker is not set for this transaction"] [sessionID=29] [startTS=450891191297769474] [commitTS=450891191298031616]
   > [2024/07/03 13:29:55.607 +00:00] [INFO] [set.go:127] ["set global var"] [conn=31] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/07/03 13:29:56.186 +00:00] [WARN] [session.go:1683] ["run statement failed"] [conn=31] [schemaVersion=80] [error="[tikv:8029]Bad Number"] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 31,\n  \"status\": 3,\n  \"strictMode\": true,\n  \"txn\": \"450891191650615296\",\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"127.0.0.1\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/07/03 13:29:56.186 +00:00] [INFO] [conn.go:995] ["command dispatched failed"] [conn=31] [connInfo="id:31, addr:127.0.0.1:48096 status:11, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:1, autocommit:1"] [sql=" update t set a = 'test' where cast(a as decimal);"] [txn_mode=OPTIMISTIC] [err="[tikv:8029]Bad Number"]

### Scenario 2
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
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
   > [2024/07/03 13:29:58.431 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=35] [schemaVersion=88] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/07/03 13:29:58.432 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:107, Type:drop schema, State:none, SchemaState:queueing, SchemaID:102, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:58.431 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/03 13:29:58.432 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:107, Type:drop schema, State:none, SchemaState:queueing, SchemaID:102, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:58.431 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/03 13:29:58.433 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:107, Type:drop schema, State:none, SchemaState:queueing, SchemaID:102, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:58.431 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:58.434 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=88] [neededSchemaVersion=89] ["start time"=110.7µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/03 13:29:58.436 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=89] ["take time"=2.209525ms] [job="ID:107, Type:drop schema, State:running, SchemaState:write only, SchemaID:102, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:58.431 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:58.437 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:107, Type:drop schema, State:running, SchemaState:write only, SchemaID:102, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:58.431 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:58.437 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=89] [neededSchemaVersion=90] ["start time"=99.805µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/03 13:29:58.440 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=90] ["take time"=2.394886ms] [job="ID:107, Type:drop schema, State:running, SchemaState:delete only, SchemaID:102, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:58.431 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:58.440 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:107, Type:drop schema, State:running, SchemaState:delete only, SchemaID:102, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:58.431 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:58.441 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=90] [neededSchemaVersion=91] ["start time"=119.639µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/03 13:29:58.443 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=91] ["take time"=2.185849ms] [job="ID:107, Type:drop schema, State:done, SchemaState:queueing, SchemaID:102, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:58.431 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:58.443 +00:00] [INFO] [delete_range.go:106] ["[ddl] add job into delete-range table"] [jobID=107] [jobType="drop schema"]
   > [2024/07/03 13:29:58.443 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:107, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:102, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:58.431 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:58.444 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=107]
   > [2024/07/03 13:29:58.444 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/07/03 13:29:58.445 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=35] [schemaVersion=91] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/07/03 13:29:58.446 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:109, Type:create schema, State:none, SchemaState:queueing, SchemaID:108, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-03 13:29:58.446 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/03 13:29:58.446 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:109, Type:create schema, State:none, SchemaState:queueing, SchemaID:108, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-03 13:29:58.446 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/03 13:29:58.447 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:109, Type:create schema, State:none, SchemaState:queueing, SchemaID:108, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:58.446 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:58.448 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=91] [neededSchemaVersion=92] ["start time"=142.339µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/03 13:29:58.449 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=92] ["take time"=2.152674ms] [job="ID:109, Type:create schema, State:done, SchemaState:public, SchemaID:108, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-03 13:29:58.446 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:58.450 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:109, Type:create schema, State:synced, SchemaState:public, SchemaID:108, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:58.446 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:58.451 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=109]
   > [2024/07/03 13:29:58.451 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/07/03 13:29:58.453 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=35] [schemaVersion=92] [cur_db=testdb] [sql="drop table if exists t;"] [user=root@127.0.0.1]
   > [2024/07/03 13:29:58.454 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=35] [schemaVersion=92] [cur_db=testdb] [sql="create table t(a varchar(20));"] [user=root@127.0.0.1]
   > [2024/07/03 13:29:58.455 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:111, Type:create table, State:none, SchemaState:queueing, SchemaID:108, TableID:110, RowCount:0, ArgLen:1, start time: 2024-07-03 13:29:58.454 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/03 13:29:58.455 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:111, Type:create table, State:none, SchemaState:queueing, SchemaID:108, TableID:110, RowCount:0, ArgLen:1, start time: 2024-07-03 13:29:58.454 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t(a varchar(20));"]
   > [2024/07/03 13:29:58.456 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:111, Type:create table, State:none, SchemaState:queueing, SchemaID:108, TableID:110, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:58.454 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:58.457 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=92] [neededSchemaVersion=93] ["start time"=281.883µs] [phyTblIDs="[110]"] [actionTypes="[8]"]
   > [2024/07/03 13:29:58.459 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=93] ["take time"=2.199746ms] [job="ID:111, Type:create table, State:done, SchemaState:public, SchemaID:108, TableID:110, RowCount:0, ArgLen:1, start time: 2024-07-03 13:29:58.454 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:58.459 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:111, Type:create table, State:synced, SchemaState:public, SchemaID:108, TableID:110, RowCount:0, ArgLen:0, start time: 2024-07-03 13:29:58.454 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/03 13:29:58.460 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=111]
   > [2024/07/03 13:29:58.460 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/07/03 13:29:58.460 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=70] ["first split key"=74800000000000006e]
   > [2024/07/03 13:29:58.461 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=70] ["first at"=74800000000000006e] ["first new region left"="{Id:70 StartKey:7480000000000000ff6800000000000000f8 EndKey:7480000000000000ff6e00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:71 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/03 13:29:58.461 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[70]"]
   > [2024/07/03 13:29:58.461 +00:00] [WARN] [2pc.go:1598] ["schemaLeaseChecker is not set for this transaction"] [sessionID=35] [startTS=450891192326160384] [commitTS=450891192326160385]
   > [2024/07/03 13:29:59.527 +00:00] [INFO] [set.go:127] ["set global var"] [conn=37] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/07/03 13:30:00.406 +00:00] [WARN] [session.go:1683] ["run statement failed"] [conn=37] [schemaVersion=93] [error="[types:8029]Bad Number"] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 37,\n  \"status\": 3,\n  \"strictMode\": true,\n  \"txn\": \"450891192678219776\",\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"127.0.0.1\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/07/03 13:30:00.406 +00:00] [INFO] [conn.go:995] ["command dispatched failed"] [conn=37] [connInfo="id:37, addr:127.0.0.1:48128 status:11, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:1, autocommit:1"] [sql=" update t set a = 'test' where cast(a as decimal);"] [txn_mode=OPTIMISTIC] [err="[types:8029]Bad Number"]
