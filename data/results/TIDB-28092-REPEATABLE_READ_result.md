# Bug ID TIDB-28092-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/28092
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              Should not throw an error.


## Details
 * Database: tidb-v5.2.1
 * Number of scenarios: 2
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  start transaction;
     - TID: 0
     - Output: None
 * Instruction #2:
     - SQL:  update t set b = 'test' where a;
     - TID: 0
     - Output: ERROR: 1292 (22007): Truncated incorrect DOUBLE value: ''
 * Instruction #3:
     - SQL:  rollback;
     - TID: 0
     - Output: Skipped due to previous error.

 * Container logs:
   > [2024/06/25 18:23:53.614 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=26] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/06/25 18:23:53.615 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=26] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/06/25 18:23:53.616 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:54, Type:create schema, State:none, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-25 18:23:53.615 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/25 18:23:53.616 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:54, Type:create schema, State:none, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-25 18:23:53.615 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/25 18:23:53.617 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:54, Type:create schema, State:none, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-25 18:23:53.615 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/25 18:23:53.618 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=26] [neededSchemaVersion=27] ["start time"=153.792µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/25 18:23:53.620 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=27] ["take time"=2.264769ms] [job="ID:54, Type:create schema, State:done, SchemaState:public, SchemaID:53, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-25 18:23:53.615 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/25 18:23:53.620 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:54, Type:create schema, State:synced, SchemaState:public, SchemaID:53, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-25 18:23:53.615 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/25 18:23:53.621 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=54]
   > [2024/06/25 18:23:53.621 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/25 18:23:53.623 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=27] [cur_db=testdb] [sql="create table t(a blob not null, b text);"] [user=root@127.0.0.1]
   > [2024/06/25 18:23:53.624 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:56, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:55, RowCount:0, ArgLen:1, start time: 2024-06-25 18:23:53.624 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/25 18:23:53.624 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:56, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:55, RowCount:0, ArgLen:1, start time: 2024-06-25 18:23:53.624 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t(a blob not null, b text);"]
   > [2024/06/25 18:23:53.625 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:56, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:55, RowCount:0, ArgLen:0, start time: 2024-06-25 18:23:53.624 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/25 18:23:53.626 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=27] [neededSchemaVersion=28] ["start time"=339.014µs] [phyTblIDs="[55]"] [actionTypes="[8]"]
   > [2024/06/25 18:23:53.628 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=28] ["take time"=2.159656ms] [job="ID:56, Type:create table, State:done, SchemaState:public, SchemaID:53, TableID:55, RowCount:0, ArgLen:1, start time: 2024-06-25 18:23:53.624 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/25 18:23:53.629 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:56, Type:create table, State:synced, SchemaState:public, SchemaID:53, TableID:55, RowCount:0, ArgLen:0, start time: 2024-06-25 18:23:53.624 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/25 18:23:53.630 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=56]
   > [2024/06/25 18:23:53.630 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/25 18:23:53.630 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=50] ["first split key"=748000000000000037]
   > [2024/06/25 18:23:53.630 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=50] ["first at"=748000000000000037] ["first new region left"="{Id:50 StartKey:7480000000000000ff3300000000000000f8 EndKey:7480000000000000ff3700000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:51 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/25 18:23:53.630 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[50]"]
   > [2024/06/25 18:23:53.631 +00:00] [WARN] [2pc.go:1598] ["schemaLeaseChecker is not set for this transaction"] [sessionID=5] [startTS=450714621347102722] [commitTS=450714621347364864]
   > [2024/06/25 18:23:54.702 +00:00] [INFO] [set.go:127] ["set global var"] [conn=7] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/06/25 18:23:55.288 +00:00] [WARN] [session.go:1683] ["run statement failed"] [conn=7] [schemaVersion=28] [error="[tikv:1292]Truncated incorrect DOUBLE value: ''"] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 7,\n  \"status\": 3,\n  \"strictMode\": true,\n  \"txn\": \"450714621702569984\",\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"127.0.0.1\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/06/25 18:23:55.288 +00:00] [INFO] [conn.go:995] ["command dispatched failed"] [conn=7] [connInfo="id:7, addr:127.0.0.1:54162 status:11, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:1, autocommit:1"] [sql=" update t set b = 'test' where a;"] [txn_mode=OPTIMISTIC] [err="[tikv:1292]Truncated incorrect DOUBLE value: ''"]

### Scenario 1
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  start transaction;
     - TID: 0
     - Output: None
 * Instruction #2:
     - SQL:  update t set b = 'def';
     - TID: 0
     - Output: None
 * Instruction #3:
     - SQL:  update t set b = 'test' where a;
     - TID: 0
     - Output: ERROR: 1292 (22007): Truncated incorrect DOUBLE value: ''
 * Instruction #4:
     - SQL:  rollback;
     - TID: 0
     - Output: Skipped due to previous error.

 * Container logs:
   > [2024/06/25 18:23:57.224 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=36] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/06/25 18:23:57.224 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:63, Type:drop schema, State:none, SchemaState:queueing, SchemaID:58, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-25 18:23:57.224 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/25 18:23:57.224 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:63, Type:drop schema, State:none, SchemaState:queueing, SchemaID:58, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-25 18:23:57.224 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/06/25 18:23:57.225 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:63, Type:drop schema, State:none, SchemaState:queueing, SchemaID:58, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-25 18:23:57.224 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/25 18:23:57.226 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=36] [neededSchemaVersion=37] ["start time"=81.925µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/25 18:23:57.228 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=37] ["take time"=2.233618ms] [job="ID:63, Type:drop schema, State:running, SchemaState:write only, SchemaID:58, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-25 18:23:57.224 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/25 18:23:57.228 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:63, Type:drop schema, State:running, SchemaState:write only, SchemaID:58, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-25 18:23:57.224 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/25 18:23:57.229 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=37] [neededSchemaVersion=38] ["start time"=72.357µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/25 18:23:57.231 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=38] ["take time"=2.237531ms] [job="ID:63, Type:drop schema, State:running, SchemaState:delete only, SchemaID:58, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-25 18:23:57.224 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/25 18:23:57.231 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:63, Type:drop schema, State:running, SchemaState:delete only, SchemaID:58, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-25 18:23:57.224 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/25 18:23:57.232 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=38] [neededSchemaVersion=39] ["start time"=76.757µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/25 18:23:57.234 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=39] ["take time"=2.303251ms] [job="ID:63, Type:drop schema, State:done, SchemaState:queueing, SchemaID:58, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-25 18:23:57.224 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/25 18:23:57.235 +00:00] [INFO] [delete_range.go:106] ["[ddl] add job into delete-range table"] [jobID=63] [jobType="drop schema"]
   > [2024/06/25 18:23:57.235 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:63, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:58, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-25 18:23:57.224 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/25 18:23:57.236 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=63]
   > [2024/06/25 18:23:57.236 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/25 18:23:57.238 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=39] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/06/25 18:23:57.239 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:65, Type:create schema, State:none, SchemaState:queueing, SchemaID:64, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-25 18:23:57.238 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/25 18:23:57.239 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:65, Type:create schema, State:none, SchemaState:queueing, SchemaID:64, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-25 18:23:57.238 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/25 18:23:57.239 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:create schema, State:none, SchemaState:queueing, SchemaID:64, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-25 18:23:57.238 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/25 18:23:57.240 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=39] [neededSchemaVersion=40] ["start time"=139.126µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/25 18:23:57.242 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=40] ["take time"=2.216019ms] [job="ID:65, Type:create schema, State:done, SchemaState:public, SchemaID:64, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-25 18:23:57.238 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/25 18:23:57.243 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:create schema, State:synced, SchemaState:public, SchemaID:64, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-25 18:23:57.238 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/25 18:23:57.243 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=65]
   > [2024/06/25 18:23:57.243 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/25 18:23:57.246 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=40] [cur_db=testdb] [sql="create table t(a blob not null, b text);"] [user=root@127.0.0.1]
   > [2024/06/25 18:23:57.247 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:67, Type:create table, State:none, SchemaState:queueing, SchemaID:64, TableID:66, RowCount:0, ArgLen:1, start time: 2024-06-25 18:23:57.246 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/25 18:23:57.247 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:67, Type:create table, State:none, SchemaState:queueing, SchemaID:64, TableID:66, RowCount:0, ArgLen:1, start time: 2024-06-25 18:23:57.246 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t(a blob not null, b text);"]
   > [2024/06/25 18:23:57.248 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:create table, State:none, SchemaState:queueing, SchemaID:64, TableID:66, RowCount:0, ArgLen:0, start time: 2024-06-25 18:23:57.246 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/25 18:23:57.249 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=40] [neededSchemaVersion=41] ["start time"=265.051µs] [phyTblIDs="[66]"] [actionTypes="[8]"]
   > [2024/06/25 18:23:57.252 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=41] ["take time"=2.806324ms] [job="ID:67, Type:create table, State:done, SchemaState:public, SchemaID:64, TableID:66, RowCount:0, ArgLen:1, start time: 2024-06-25 18:23:57.246 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/25 18:23:57.252 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:create table, State:synced, SchemaState:public, SchemaID:64, TableID:66, RowCount:0, ArgLen:0, start time: 2024-06-25 18:23:57.246 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/25 18:23:57.254 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=67]
   > [2024/06/25 18:23:57.254 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/25 18:23:57.254 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=54] ["first split key"=748000000000000042]
   > [2024/06/25 18:23:57.254 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=54] ["first at"=748000000000000042] ["first new region left"="{Id:54 StartKey:7480000000000000ff3c00000000000000f8 EndKey:7480000000000000ff4200000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:55 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/25 18:23:57.254 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[54]"]
   > [2024/06/25 18:23:57.255 +00:00] [WARN] [2pc.go:1598] ["schemaLeaseChecker is not set for this transaction"] [sessionID=11] [startTS=450714622297112578] [commitTS=450714622297374720]
   > [2024/06/25 18:23:58.323 +00:00] [INFO] [set.go:127] ["set global var"] [conn=13] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/06/25 18:23:59.205 +00:00] [WARN] [session.go:1683] ["run statement failed"] [conn=13] [schemaVersion=41] [error="[types:1292]Truncated incorrect DOUBLE value: ''"] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 13,\n  \"status\": 3,\n  \"strictMode\": true,\n  \"txn\": \"450714622650744832\",\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"127.0.0.1\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/06/25 18:23:59.205 +00:00] [INFO] [conn.go:995] ["command dispatched failed"] [conn=13] [connInfo="id:13, addr:127.0.0.1:54184 status:11, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:1, autocommit:1"] [sql=" update t set b = 'test' where a;"] [txn_mode=OPTIMISTIC] [err="[types:1292]Truncated incorrect DOUBLE value: ''\ngithub.com/pingcap/errors.AddStack\n\t/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.20210425183316-da1aaba5fb63/errors.go:174\ngithub.com/pingcap/errors.(*Error).GenWithStackByArgs\n\t/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.20210425183316-da1aaba5fb63/normalize.go:159\ngithub.com/pingcap/tidb/types.getValidFloatPrefix\n\t/go/src/github.com/pingcap/tidb/types/convert.go:713\ngithub.com/pingcap/tidb/types.StrToFloat\n\t/go/src/github.com/pingcap/tidb/types/convert.go:527\ngithub.com/pingcap/tidb/types.(*Datum).ToBool\n\t/go/src/github.com/pingcap/tidb/types/datum.go:1597\ngithub.com/pingcap/tidb/expression.EvalBool\n\t/go/src/github.com/pingcap/tidb/expression/expression.go:258\ngithub.com/pingcap/tidb/executor.(*memTableReader).getMemRows.func1\n\t/go/src/github.com/pingcap/tidb/executor/mem_reader.go:209\ngithub.com/pingcap/tidb/executor.iterTxnMemBuffer\n\t/go/src/github.com/pingcap/tidb/executor/mem_reader.go:349\ngithub.com/pingcap/tidb/executor.(*memTableReader).getMemRows\n\t/go/src/github.com/pingcap/tidb/executor/mem_reader.go:202\ngithub.com/pingcap/tidb/executor.(*UnionScanExec).open\n\t/go/src/github.com/pingcap/tidb/executor/union_scan.go:95\ngithub.com/pingcap/tidb/executor.(*UnionScanExec).Open\n\t/go/src/github.com/pingcap/tidb/executor/union_scan.go:65\ngithub.com/pingcap/tidb/executor.(*UpdateExec).Open\n\t/go/src/github.com/pingcap/tidb/executor/update.go:428\ngithub.com/pingcap/tidb/executor.(*ExecStmt).Exec\n\t/go/src/github.com/pingcap/tidb/executor/adapter.go:388\ngithub.com/pingcap/tidb/session.runStmt\n\t/go/src/github.com/pingcap/tidb/session/session.go:1786\ngithub.com/pingcap/tidb/session.(*session).ExecuteStmt\n\t/go/src/github.com/pingcap/tidb/session/session.go:1680\ngithub.com/pingcap/tidb/server.(*TiDBContext).ExecuteStmt\n\t/go/src/github.com/pingcap/tidb/server/driver_tidb.go:218\ngithub.com/pingcap/tidb/server.(*clientConn).handleStmt\n\t/go/src/github.com/pingcap/tidb/server/conn.go:1818\ngithub.com/pingcap/tidb/server.(*clientConn).handleQuery\n\t/go/src/github.com/pingcap/tidb/server/conn.go:1690\ngithub.com/pingcap/tidb/server.(*clientConn).dispatch\n\t/go/src/github.com/pingcap/tidb/server/conn.go:1215\ngithub.com/pingcap/tidb/server.(*clientConn).Run\n\t/go/src/github.com/pingcap/tidb/server/conn.go:978\ngithub.com/pingcap/tidb/server.(*Server).onConn\n\t/go/src/github.com/pingcap/tidb/server/server.go:501\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1594"]
