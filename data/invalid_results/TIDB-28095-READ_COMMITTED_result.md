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
     - Affected rows / Warnings: 0 / 0
 * Instruction #1:
     - Instruction:  update t set a = 'test' where cast(a as decimal);
     - Transaction: conn_0
     - Output: ERROR: 1105 (HY000): Bad Number
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0

 * Container logs:
   > [2024/07/05 12:58:59.105 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=23] [schemaVersion=62] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/07/05 12:58:59.106 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:85, Type:drop schema, State:none, SchemaState:queueing, SchemaID:80, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-05 12:58:59.105 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/05 12:58:59.106 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:85, Type:drop schema, State:none, SchemaState:queueing, SchemaID:80, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-05 12:58:59.105 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/05 12:58:59.107 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:85, Type:drop schema, State:none, SchemaState:queueing, SchemaID:80, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-05 12:58:59.105 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/05 12:58:59.108 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=62] [neededSchemaVersion=63] ["start time"=101.201µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/05 12:58:59.110 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=63] ["take time"=2.225027ms] [job="ID:85, Type:drop schema, State:running, SchemaState:write only, SchemaID:80, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-05 12:58:59.105 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/05 12:58:59.110 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:85, Type:drop schema, State:running, SchemaState:write only, SchemaID:80, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-05 12:58:59.105 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/05 12:58:59.111 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=63] [neededSchemaVersion=64] ["start time"=136.332µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/05 12:58:59.113 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=64] ["take time"=2.231522ms] [job="ID:85, Type:drop schema, State:running, SchemaState:delete only, SchemaID:80, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-05 12:58:59.105 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/05 12:58:59.114 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:85, Type:drop schema, State:running, SchemaState:delete only, SchemaID:80, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-05 12:58:59.105 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/05 12:58:59.115 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=64] [neededSchemaVersion=65] ["start time"=106.649µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/05 12:58:59.118 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=65] ["take time"=3.106573ms] [job="ID:85, Type:drop schema, State:done, SchemaState:queueing, SchemaID:80, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-05 12:58:59.105 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/05 12:58:59.118 +00:00] [INFO] [delete_range.go:106] ["[ddl] add job into delete-range table"] [jobID=85] [jobType="drop schema"]
   > [2024/07/05 12:58:59.118 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:85, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:80, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-05 12:58:59.105 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/05 12:58:59.120 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=85]
   > [2024/07/05 12:58:59.120 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/07/05 12:58:59.121 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=23] [schemaVersion=65] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/07/05 12:58:59.123 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:87, Type:create schema, State:none, SchemaState:queueing, SchemaID:86, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-05 12:58:59.122 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/05 12:58:59.123 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:87, Type:create schema, State:none, SchemaState:queueing, SchemaID:86, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-05 12:58:59.122 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/05 12:58:59.123 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:87, Type:create schema, State:none, SchemaState:queueing, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-05 12:58:59.122 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/05 12:58:59.125 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=65] [neededSchemaVersion=66] ["start time"=166.573µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/05 12:58:59.126 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=66] ["take time"=2.217833ms] [job="ID:87, Type:create schema, State:done, SchemaState:public, SchemaID:86, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-05 12:58:59.122 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/05 12:58:59.127 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:87, Type:create schema, State:synced, SchemaState:public, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-05 12:58:59.122 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/05 12:58:59.128 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=87]
   > [2024/07/05 12:58:59.128 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/07/05 12:58:59.131 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=23] [schemaVersion=66] [cur_db=testdb] [sql="drop table if exists t;"] [user=root@127.0.0.1]
   > [2024/07/05 12:58:59.131 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=23] [schemaVersion=66] [cur_db=testdb] [sql="create table t(a varchar(20));"] [user=root@127.0.0.1]
   > [2024/07/05 12:58:59.133 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:89, Type:create table, State:none, SchemaState:queueing, SchemaID:86, TableID:88, RowCount:0, ArgLen:1, start time: 2024-07-05 12:58:59.132 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/05 12:58:59.133 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:89, Type:create table, State:none, SchemaState:queueing, SchemaID:86, TableID:88, RowCount:0, ArgLen:1, start time: 2024-07-05 12:58:59.132 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t(a varchar(20));"]
   > [2024/07/05 12:58:59.134 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:89, Type:create table, State:none, SchemaState:queueing, SchemaID:86, TableID:88, RowCount:0, ArgLen:0, start time: 2024-07-05 12:58:59.132 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/05 12:58:59.136 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=66] [neededSchemaVersion=67] ["start time"=289.355µs] [phyTblIDs="[88]"] [actionTypes="[8]"]
   > [2024/07/05 12:58:59.137 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=67] ["take time"=2.265116ms] [job="ID:89, Type:create table, State:done, SchemaState:public, SchemaID:86, TableID:88, RowCount:0, ArgLen:1, start time: 2024-07-05 12:58:59.132 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/05 12:58:59.138 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:89, Type:create table, State:synced, SchemaState:public, SchemaID:86, TableID:88, RowCount:0, ArgLen:0, start time: 2024-07-05 12:58:59.132 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/05 12:58:59.139 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=89]
   > [2024/07/05 12:58:59.139 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/07/05 12:58:59.140 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=62] ["first split key"=748000000000000058]
   > [2024/07/05 12:58:59.140 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=62] ["first at"=748000000000000058] ["first new region left"="{Id:62 StartKey:7480000000000000ff5200000000000000f8 EndKey:7480000000000000ff5800000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:63 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/05 12:58:59.140 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[62]"]
   > [2024/07/05 12:58:59.141 +00:00] [WARN] [2pc.go:1598] ["schemaLeaseChecker is not set for this transaction"] [sessionID=23] [startTS=450936003399516161] [commitTS=450936003399778304]
   > [2024/07/05 12:59:00.211 +00:00] [INFO] [set.go:127] ["set global var"] [conn=25] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/07/05 12:59:00.487 +00:00] [INFO] [tidb.go:242] ["rollbackTxn called due to ddl/autocommit failure"]
   > [2024/07/05 12:59:00.487 +00:00] [WARN] [session.go:1683] ["run statement failed"] [conn=25] [schemaVersion=67] [error="[tikv:8029]Bad Number"] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 25,\n  \"status\": 2,\n  \"strictMode\": true,\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"127.0.0.1\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/07/05 12:59:00.487 +00:00] [INFO] [conn.go:995] ["command dispatched failed"] [conn=25] [connInfo="id:25, addr:127.0.0.1:33892 status:10, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:0, autocommit:1"] [sql=" update t set a = 'test' where cast(a as decimal);"] [txn_mode=OPTIMISTIC] [err="[tikv:8029]Bad Number"]

### Scenario 1
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
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
   > [2024/07/05 12:59:01.368 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=29] [schemaVersion=75] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/07/05 12:59:01.369 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:96, Type:drop schema, State:none, SchemaState:queueing, SchemaID:91, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-05 12:59:01.368 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/05 12:59:01.369 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:96, Type:drop schema, State:none, SchemaState:queueing, SchemaID:91, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-05 12:59:01.368 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/05 12:59:01.369 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:96, Type:drop schema, State:none, SchemaState:queueing, SchemaID:91, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-05 12:59:01.368 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/05 12:59:01.370 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=75] [neededSchemaVersion=76] ["start time"=101.97µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/05 12:59:01.372 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=76] ["take time"=2.205471ms] [job="ID:96, Type:drop schema, State:running, SchemaState:write only, SchemaID:91, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-05 12:59:01.368 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/05 12:59:01.372 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:96, Type:drop schema, State:running, SchemaState:write only, SchemaID:91, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-05 12:59:01.368 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/05 12:59:01.373 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=76] [neededSchemaVersion=77] ["start time"=70.191µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/05 12:59:01.375 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=77] ["take time"=2.48484ms] [job="ID:96, Type:drop schema, State:running, SchemaState:delete only, SchemaID:91, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-05 12:59:01.368 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/05 12:59:01.376 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:96, Type:drop schema, State:running, SchemaState:delete only, SchemaID:91, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-05 12:59:01.368 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/05 12:59:01.377 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=77] [neededSchemaVersion=78] ["start time"=70.052µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/05 12:59:01.379 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=78] ["take time"=2.32071ms] [job="ID:96, Type:drop schema, State:done, SchemaState:queueing, SchemaID:91, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-05 12:59:01.368 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/05 12:59:01.379 +00:00] [INFO] [delete_range.go:106] ["[ddl] add job into delete-range table"] [jobID=96] [jobType="drop schema"]
   > [2024/07/05 12:59:01.379 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:96, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:91, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-05 12:59:01.368 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/05 12:59:01.380 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=96]
   > [2024/07/05 12:59:01.380 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/07/05 12:59:01.381 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=29] [schemaVersion=78] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/07/05 12:59:01.383 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:98, Type:create schema, State:none, SchemaState:queueing, SchemaID:97, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-05 12:59:01.382 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/05 12:59:01.383 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:98, Type:create schema, State:none, SchemaState:queueing, SchemaID:97, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-05 12:59:01.382 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/05 12:59:01.383 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:98, Type:create schema, State:none, SchemaState:queueing, SchemaID:97, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-05 12:59:01.382 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/05 12:59:01.384 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=78] [neededSchemaVersion=79] ["start time"=125.087µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/05 12:59:01.386 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=79] ["take time"=2.199255ms] [job="ID:98, Type:create schema, State:done, SchemaState:public, SchemaID:97, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-05 12:59:01.382 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/05 12:59:01.386 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:98, Type:create schema, State:synced, SchemaState:public, SchemaID:97, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-05 12:59:01.382 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/05 12:59:01.387 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=98]
   > [2024/07/05 12:59:01.387 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/07/05 12:59:01.389 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=29] [schemaVersion=79] [cur_db=testdb] [sql="drop table if exists t;"] [user=root@127.0.0.1]
   > [2024/07/05 12:59:01.389 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=29] [schemaVersion=79] [cur_db=testdb] [sql="create table t(a varchar(20));"] [user=root@127.0.0.1]
   > [2024/07/05 12:59:01.390 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:100, Type:create table, State:none, SchemaState:queueing, SchemaID:97, TableID:99, RowCount:0, ArgLen:1, start time: 2024-07-05 12:59:01.39 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/05 12:59:01.391 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:100, Type:create table, State:none, SchemaState:queueing, SchemaID:97, TableID:99, RowCount:0, ArgLen:1, start time: 2024-07-05 12:59:01.39 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t(a varchar(20));"]
   > [2024/07/05 12:59:01.391 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:100, Type:create table, State:none, SchemaState:queueing, SchemaID:97, TableID:99, RowCount:0, ArgLen:0, start time: 2024-07-05 12:59:01.39 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/05 12:59:01.392 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=79] [neededSchemaVersion=80] ["start time"=242.492µs] [phyTblIDs="[99]"] [actionTypes="[8]"]
   > [2024/07/05 12:59:01.394 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=80] ["take time"=2.21944ms] [job="ID:100, Type:create table, State:done, SchemaState:public, SchemaID:97, TableID:99, RowCount:0, ArgLen:1, start time: 2024-07-05 12:59:01.39 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/05 12:59:01.395 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:100, Type:create table, State:synced, SchemaState:public, SchemaID:97, TableID:99, RowCount:0, ArgLen:0, start time: 2024-07-05 12:59:01.39 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/05 12:59:01.395 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=100]
   > [2024/07/05 12:59:01.395 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/07/05 12:59:01.395 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=66] ["first split key"=748000000000000063]
   > [2024/07/05 12:59:01.396 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=66] ["first at"=748000000000000063] ["first new region left"="{Id:66 StartKey:7480000000000000ff5d00000000000000f8 EndKey:7480000000000000ff6300000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:67 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/05 12:59:01.396 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[66]"]
   > [2024/07/05 12:59:01.396 +00:00] [WARN] [2pc.go:1598] ["schemaLeaseChecker is not set for this transaction"] [sessionID=29] [startTS=450936003990913025] [commitTS=450936003990913026]
   > [2024/07/05 12:59:02.462 +00:00] [INFO] [set.go:127] ["set global var"] [conn=31] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/07/05 12:59:03.045 +00:00] [WARN] [session.go:1683] ["run statement failed"] [conn=31] [schemaVersion=80] [error="[tikv:8029]Bad Number"] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 31,\n  \"status\": 3,\n  \"strictMode\": true,\n  \"txn\": \"450936004344020992\",\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"127.0.0.1\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/07/05 12:59:03.045 +00:00] [INFO] [conn.go:995] ["command dispatched failed"] [conn=31] [connInfo="id:31, addr:127.0.0.1:50032 status:11, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:1, autocommit:1"] [sql=" update t set a = 'test' where cast(a as decimal);"] [txn_mode=OPTIMISTIC] [err="[tikv:8029]Bad Number"]

### Scenario 2
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
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
   > [2024/07/05 12:59:05.298 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=35] [schemaVersion=88] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/07/05 12:59:05.299 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:107, Type:drop schema, State:none, SchemaState:queueing, SchemaID:102, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-05 12:59:05.298 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/05 12:59:05.299 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:107, Type:drop schema, State:none, SchemaState:queueing, SchemaID:102, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-05 12:59:05.298 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/05 12:59:05.300 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:107, Type:drop schema, State:none, SchemaState:queueing, SchemaID:102, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-05 12:59:05.298 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/05 12:59:05.301 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=88] [neededSchemaVersion=89] ["start time"=126.274µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/05 12:59:05.303 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=89] ["take time"=2.246608ms] [job="ID:107, Type:drop schema, State:running, SchemaState:write only, SchemaID:102, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-05 12:59:05.298 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/05 12:59:05.303 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:107, Type:drop schema, State:running, SchemaState:write only, SchemaID:102, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-05 12:59:05.298 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/05 12:59:05.304 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=89] [neededSchemaVersion=90] ["start time"=124.249µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/05 12:59:05.306 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=90] ["take time"=2.196042ms] [job="ID:107, Type:drop schema, State:running, SchemaState:delete only, SchemaID:102, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-05 12:59:05.298 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/05 12:59:05.307 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:107, Type:drop schema, State:running, SchemaState:delete only, SchemaID:102, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-05 12:59:05.298 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/05 12:59:05.308 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=90] [neededSchemaVersion=91] ["start time"=122.782µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/05 12:59:05.310 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=91] ["take time"=2.236551ms] [job="ID:107, Type:drop schema, State:done, SchemaState:queueing, SchemaID:102, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-05 12:59:05.298 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/05 12:59:05.310 +00:00] [INFO] [delete_range.go:106] ["[ddl] add job into delete-range table"] [jobID=107] [jobType="drop schema"]
   > [2024/07/05 12:59:05.310 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:107, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:102, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-05 12:59:05.298 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/05 12:59:05.312 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=107]
   > [2024/07/05 12:59:05.312 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/07/05 12:59:05.313 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=35] [schemaVersion=91] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/07/05 12:59:05.315 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:109, Type:create schema, State:none, SchemaState:queueing, SchemaID:108, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-05 12:59:05.314 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/05 12:59:05.315 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:109, Type:create schema, State:none, SchemaState:queueing, SchemaID:108, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-05 12:59:05.314 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/05 12:59:05.316 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:109, Type:create schema, State:none, SchemaState:queueing, SchemaID:108, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-05 12:59:05.314 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/05 12:59:05.317 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=91] [neededSchemaVersion=92] ["start time"=178.306µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/05 12:59:05.319 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=92] ["take time"=2.280761ms] [job="ID:109, Type:create schema, State:done, SchemaState:public, SchemaID:108, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-05 12:59:05.314 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/05 12:59:05.319 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:109, Type:create schema, State:synced, SchemaState:public, SchemaID:108, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-05 12:59:05.314 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/05 12:59:05.320 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=109]
   > [2024/07/05 12:59:05.320 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/07/05 12:59:05.324 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=35] [schemaVersion=92] [cur_db=testdb] [sql="drop table if exists t;"] [user=root@127.0.0.1]
   > [2024/07/05 12:59:05.324 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=35] [schemaVersion=92] [cur_db=testdb] [sql="create table t(a varchar(20));"] [user=root@127.0.0.1]
   > [2024/07/05 12:59:05.326 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:111, Type:create table, State:none, SchemaState:queueing, SchemaID:108, TableID:110, RowCount:0, ArgLen:1, start time: 2024-07-05 12:59:05.325 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/05 12:59:05.326 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:111, Type:create table, State:none, SchemaState:queueing, SchemaID:108, TableID:110, RowCount:0, ArgLen:1, start time: 2024-07-05 12:59:05.325 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t(a varchar(20));"]
   > [2024/07/05 12:59:05.326 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:111, Type:create table, State:none, SchemaState:queueing, SchemaID:108, TableID:110, RowCount:0, ArgLen:0, start time: 2024-07-05 12:59:05.325 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/05 12:59:05.328 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=92] [neededSchemaVersion=93] ["start time"=280.765µs] [phyTblIDs="[110]"] [actionTypes="[8]"]
   > [2024/07/05 12:59:05.330 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=93] ["take time"=2.284742ms] [job="ID:111, Type:create table, State:done, SchemaState:public, SchemaID:108, TableID:110, RowCount:0, ArgLen:1, start time: 2024-07-05 12:59:05.325 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/05 12:59:05.331 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:111, Type:create table, State:synced, SchemaState:public, SchemaID:108, TableID:110, RowCount:0, ArgLen:0, start time: 2024-07-05 12:59:05.325 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/05 12:59:05.332 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=111]
   > [2024/07/05 12:59:05.332 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/07/05 12:59:05.332 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=70] ["first split key"=74800000000000006e]
   > [2024/07/05 12:59:05.332 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=70] ["first at"=74800000000000006e] ["first new region left"="{Id:70 StartKey:7480000000000000ff6800000000000000f8 EndKey:7480000000000000ff6e00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:71 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/05 12:59:05.333 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[70]"]
   > [2024/07/05 12:59:05.333 +00:00] [WARN] [2pc.go:1598] ["schemaLeaseChecker is not set for this transaction"] [sessionID=35] [startTS=450936005022711810] [commitTS=450936005022973952]
   > [2024/07/05 12:59:06.400 +00:00] [INFO] [set.go:127] ["set global var"] [conn=37] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/07/05 12:59:07.280 +00:00] [WARN] [session.go:1683] ["run statement failed"] [conn=37] [schemaVersion=93] [error="[types:8029]Bad Number"] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 37,\n  \"status\": 3,\n  \"strictMode\": true,\n  \"txn\": \"450936005375295488\",\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"127.0.0.1\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/07/05 12:59:07.280 +00:00] [INFO] [conn.go:995] ["command dispatched failed"] [conn=37] [connInfo="id:37, addr:127.0.0.1:50076 status:11, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:1, autocommit:1"] [sql=" update t set a = 'test' where cast(a as decimal);"] [txn_mode=OPTIMISTIC] [err="[types:8029]Bad Number"]
