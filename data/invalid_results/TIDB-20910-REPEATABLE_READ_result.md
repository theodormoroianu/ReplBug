# Bug ID TIDB-20910-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/20910
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              admin check table t should work


## Details
 * Database: tidb-45571c5e
 * Number of scenarios: 2
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  begin;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 0 / 0
 * Instruction #1:
     - Instruction:  alter table t add unique index uk(c);
     - Transaction: conn_1
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  update t set c = 2 where id = 3;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 1 / 0
 * Instruction #3:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: ERROR: 9007 (HY000): Write conflict, txnStartTS=451345874843860992, conflictStartTS=451345874929057793, conflictCommitTS=451345874929319936, key={tableID=47, handle=3} primary=[]byte(nil) [try again later]
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #4:
     - Instruction:  admin check table t;
     - Transaction: conn_1
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 0 / 0

 * Container logs:
   > [2024/07/23 15:17:53.576 +00:00] [INFO] [session.go:2166] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=22] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.15]
   > [2024/07/23 15:17:53.577 +00:00] [INFO] [session.go:2166] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=22] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.15]
   > [2024/07/23 15:17:53.577 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 15:17:53.577 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/23 15:17:53.577 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 15:17:53.577 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/23 15:17:53.577 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:17:53.577 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:53.578 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=22] [neededSchemaVersion=23] ["start time"=62.509µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 15:17:53.580 +00:00] [INFO] [ddl_worker.go:782] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=23] ["take time"=2.20631ms] [job="ID:46, Type:create schema, State:done, SchemaState:public, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 15:17:53.577 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:53.581 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:46, Type:create schema, State:synced, SchemaState:public, SchemaID:45, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:17:53.577 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:53.581 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=46]
   > [2024/07/23 15:17:53.581 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/07/23 15:17:53.583 +00:00] [INFO] [session.go:2166] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=23] [cur_db=testdb] [sql="create table t (id int auto_increment primary key, c int);"] [user=root@10.88.0.15]
   > [2024/07/23 15:17:53.585 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-07-23 15:17:53.584 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/23 15:17:53.585 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-07-23 15:17:53.584 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t (id int auto_increment primary key, c int);"]
   > [2024/07/23 15:17:53.585 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-23 15:17:53.584 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:53.587 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=23] [neededSchemaVersion=24] ["start time"=388.392µs] [phyTblIDs="[47]"] [actionTypes="[8]"]
   > [2024/07/23 15:17:53.589 +00:00] [INFO] [ddl_worker.go:782] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=24] ["take time"=2.220767ms] [job="ID:48, Type:create table, State:done, SchemaState:public, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-07-23 15:17:53.584 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:53.589 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:48, Type:create table, State:synced, SchemaState:public, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-23 15:17:53.584 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:53.591 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=48]
   > [2024/07/23 15:17:53.591 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/07/23 15:17:53.591 +00:00] [INFO] [split_region.go:60] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=42] ["first split key"=74800000000000002f]
   > [2024/07/23 15:17:53.591 +00:00] [INFO] [split_region.go:157] ["batch split regions complete"] ["batch region ID"=42] ["first at"=74800000000000002f] ["first new region left"="{Id:42 StartKey:7480000000000000ff2b00000000000000f8 EndKey: RegionEpoch:{ConfVer:0 Version:1} Peers:[id:43 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/23 15:17:53.591 +00:00] [INFO] [split_region.go:209] ["split regions complete"] ["region count"=1] ["region IDs"="[42]"]
   > [2024/07/23 15:17:54.928 +00:00] [INFO] [session.go:2166] ["CRUCIAL OPERATION"] [conn=4] [schemaVersion=24] [cur_db=testdb] [sql=" alter table t add unique index uk(c);"] [user=root@10.88.0.15]
   > [2024/07/23 15:17:54.929 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:49, Type:add index, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:5, start time: 2024-07-23 15:17:54.928 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/23 15:17:54.929 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:49, Type:add index, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:5, start time: 2024-07-23 15:17:54.928 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query=" alter table t add unique index uk(c);"]
   > [2024/07/23 15:17:54.929 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 4, tp add index"] [job="ID:49, Type:add index, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-23 15:17:54.928 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:54.929 +00:00] [INFO] [index.go:462] ["[ddl] run add index job"] [job="ID:49, Type:add index, State:running, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:5, start time: 2024-07-23 15:17:54.928 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [indexInfo="{\"id\":1,\"idx_name\":{\"O\":\"uk\",\"L\":\"uk\"},\"tbl_name\":{\"O\":\"\",\"L\":\"\"},\"idx_cols\":[{\"name\":{\"O\":\"c\",\"L\":\"c\"},\"offset\":1,\"length\":-1}],\"state\":0,\"comment\":\"\",\"index_type\":1,\"is_unique\":true,\"is_primary\":false,\"is_invisible\":false}"]
   > [2024/07/23 15:17:54.931 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=24] [neededSchemaVersion=25] ["start time"=271.476µs] [phyTblIDs="[47]"] [actionTypes="[128]"]
   > [2024/07/23 15:17:54.933 +00:00] [INFO] [ddl_worker.go:782] ["[ddl] wait latest schema version changed"] [worker="worker 4, tp add index"] [ver=25] ["take time"=2.992801ms] [job="ID:49, Type:add index, State:running, SchemaState:delete only, SchemaID:45, TableID:47, RowCount:0, ArgLen:5, start time: 2024-07-23 15:17:54.928 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:54.934 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 4, tp add index"] [job="ID:49, Type:add index, State:running, SchemaState:delete only, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-23 15:17:54.928 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:54.935 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=25] [neededSchemaVersion=26] ["start time"=292.429µs] [phyTblIDs="[47]"] [actionTypes="[128]"]
   > [2024/07/23 15:17:54.937 +00:00] [INFO] [ddl_worker.go:782] ["[ddl] wait latest schema version changed"] [worker="worker 4, tp add index"] [ver=26] ["take time"=2.182494ms] [job="ID:49, Type:add index, State:running, SchemaState:write only, SchemaID:45, TableID:47, RowCount:0, ArgLen:5, start time: 2024-07-23 15:17:54.928 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:54.937 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 4, tp add index"] [job="ID:49, Type:add index, State:running, SchemaState:write only, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-23 15:17:54.928 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:54.938 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=26] [neededSchemaVersion=27] ["start time"=267.006µs] [phyTblIDs="[47]"] [actionTypes="[128]"]
   > [2024/07/23 15:17:54.940 +00:00] [INFO] [ddl_worker.go:782] ["[ddl] wait latest schema version changed"] [worker="worker 4, tp add index"] [ver=27] ["take time"=2.073051ms] [job="ID:49, Type:add index, State:running, SchemaState:write reorganization, SchemaID:45, TableID:47, RowCount:0, ArgLen:5, start time: 2024-07-23 15:17:54.928 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:54.940 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 4, tp add index"] [job="ID:49, Type:add index, State:running, SchemaState:write reorganization, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-23 15:17:54.928 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:54.941 +00:00] [INFO] [reorg.go:430] ["[ddl] job get table range"] [jobID=49] [physicalTableID=47] [startHandle=1] [endHandle=3]
   > [2024/07/23 15:17:54.942 +00:00] [INFO] [ddl_worker.go:749] ["[ddl] schema version doesn't change"] [worker="worker 4, tp add index"]
   > [2024/07/23 15:17:54.942 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 4, tp add index"] [job="ID:49, Type:add index, State:running, SchemaState:write reorganization, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-23 15:17:54.928 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:451345874928533504"]
   > [2024/07/23 15:17:54.942 +00:00] [INFO] [index.go:1373] ["[ddl] start to add table index"] [job="ID:49, Type:add index, State:running, SchemaState:write reorganization, SchemaID:45, TableID:47, RowCount:0, ArgLen:5, start time: 2024-07-23 15:17:54.928 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:451345874928533504"] [reorgInfo=StartHandle:1,EndHandle:3,first:false,PhysicalTableID:47]
   > [2024/07/23 15:17:54.943 +00:00] [INFO] [index.go:1191] ["[ddl] split table range from PD"] [physicalTableID=47] [startHandle=1] [endHandle=3]
   > [2024/07/23 15:17:54.943 +00:00] [INFO] [index.go:1446] ["[ddl] start add index workers to reorg index"] [workerCnt=1] [regionCnt=1] [startHandle=1] [endHandle=3]
   > [2024/07/23 15:17:54.943 +00:00] [INFO] [index.go:1140] ["[ddl] add index worker start"] [workerID=0]
   > [2024/07/23 15:17:54.944 +00:00] [INFO] [index.go:1134] ["[ddl] add index worker finish task"] [workerID=0] [task="physicalTableID47_[1,3]"] [addedCount=2] [scanCount=2] [nextHandle=4] [takeTime=603.086µs]
   > [2024/07/23 15:17:54.944 +00:00] [INFO] [index.go:1290] ["[ddl] add index worker handle batch tasks successful"] [totalAddedCount=2] [startHandle=1] [nextHandle=4] [batchAddedCount=2] [takeTime=678.864µs]
   > [2024/07/23 15:17:54.944 +00:00] [INFO] [reorg.go:143] ["[ddl] run reorg job done"] ["handled rows"=2]
   > [2024/07/23 15:17:54.944 +00:00] [INFO] [index.go:1165] ["[ddl] add index worker exit"] [workerID=0]
   > [2024/07/23 15:17:54.945 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=27] [neededSchemaVersion=28] ["start time"=281.464µs] [phyTblIDs="[47]"] [actionTypes="[128]"]
   > [2024/07/23 15:17:54.947 +00:00] [INFO] [ddl_worker.go:782] ["[ddl] wait latest schema version changed"] [worker="worker 4, tp add index"] [ver=28] ["take time"=2.270983ms] [job="ID:49, Type:add index, State:done, SchemaState:public, SchemaID:45, TableID:47, RowCount:2, ArgLen:5, start time: 2024-07-23 15:17:54.928 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:451345874928533504"]
   > [2024/07/23 15:17:54.948 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 4, tp add index"] [job="ID:49, Type:add index, State:synced, SchemaState:public, SchemaID:45, TableID:47, RowCount:2, ArgLen:0, start time: 2024-07-23 15:17:54.928 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:451345874928533504"]
   > [2024/07/23 15:17:54.949 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=49]
   > [2024/07/23 15:17:54.949 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/07/23 15:17:55.524 +00:00] [WARN] [session.go:472] ["can not retry txn"] [conn=3] [label=general] [error="[kv:9007]Write conflict, txnStartTS=451345874843860992, conflictStartTS=451345874929057793, conflictCommitTS=451345874929319936, key={tableID=47, handle=3} primary=[]byte(nil) [try again later]"] [IsBatchInsert=false] [IsPessimistic=false] [InRestrictedSQL=false] [tidb_retry_limit=10] [tidb_disable_txn_auto_retry=true]
   > [2024/07/23 15:17:55.524 +00:00] [WARN] [session.go:487] ["commit failed"] [conn=3] ["finished txn"="Txn{state=invalid}"] [error="[kv:9007]Write conflict, txnStartTS=451345874843860992, conflictStartTS=451345874929057793, conflictCommitTS=451345874929319936, key={tableID=47, handle=3} primary=[]byte(nil) [try again later]"]
   > [2024/07/23 15:17:55.525 +00:00] [WARN] [session.go:1071] ["run statement failed"] [conn=3] [schemaVersion=24] [error="previous statement:  update t set c = 2 where id = 3;: [kv:9007]Write conflict, txnStartTS=451345874843860992, conflictStartTS=451345874929057793, conflictCommitTS=451345874929319936, key={tableID=47, handle=3} primary=[]byte(nil) [try again later]"] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 3,\n  \"status\": 2,\n  \"strictMode\": true,\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"10.88.0.15\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/07/23 15:17:55.525 +00:00] [INFO] [conn.go:787] ["command dispatched failed"] [conn=3] [connInfo="id:3, addr:10.88.0.15:39602 status:10, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:0, autocommit:1"] [sql=" commit;"] [txn_mode=OPTIMISTIC] [err="[kv:9007]Write conflict, txnStartTS=451345874843860992, conflictStartTS=451345874929057793, conflictCommitTS=451345874929319936, key={tableID=47, handle=3} primary=[]byte(nil) [try again later]\nprevious statement:  update t set c = 2 where id = 3;"]
   > [2024/07/23 15:17:55.525 +00:00] [INFO] [2pc.go:1305] ["2PC clean up done"] [conn=3] [txnStartTS=451345874843860992]
   > [2024/07/23 15:17:55.838 +00:00] [INFO] [domain.go:146] ["full load InfoSchema success"] [usedSchemaVersion=0] [neededSchemaVersion=28] ["start time"=12.544747ms]
   > [2024/07/23 15:17:55.838 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=28]
   > [2024/07/23 15:17:55.838 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=28]
   > [2024/07/23 15:17:55.849 +00:00] [INFO] [domain.go:146] ["full load InfoSchema success"] [usedSchemaVersion=0] [neededSchemaVersion=28] ["start time"=10.054319ms]
   > [2024/07/23 15:17:55.849 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=28]
   > [2024/07/23 15:17:55.850 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=28]
   > [2024/07/23 15:17:55.850 +00:00] [INFO] [admin.go:327] ["check indices count"] [table=t] [cnt=2] [index="\"uk\""] [cnt=2]

### Scenario 1
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 0 / 0
 * Instruction #1:
     - Instruction:  alter table t add unique index uk(c);
     - Transaction: conn_1
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  update t set c = 2 where id = 3;
     - Transaction: conn_0
     - Output: ERROR: 1062 (23000): Duplicate entry '2' for key 'uk'
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #3:
     - Instruction:  admin check table t;
     - Transaction: conn_1
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 0 / 0

 * Container logs:
   > [2024/07/23 15:17:56.656 +00:00] [INFO] [session.go:2166] ["CRUCIAL OPERATION"] [conn=6] [schemaVersion=36] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.15]
   > [2024/07/23 15:17:56.656 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:56, Type:drop schema, State:none, SchemaState:none, SchemaID:51, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:17:56.656 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/23 15:17:56.656 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:56, Type:drop schema, State:none, SchemaState:none, SchemaID:51, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:17:56.656 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/23 15:17:56.657 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:56, Type:drop schema, State:none, SchemaState:none, SchemaID:51, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:17:56.656 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:56.658 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=36] [neededSchemaVersion=37] ["start time"=97.08µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 15:17:56.660 +00:00] [INFO] [ddl_worker.go:782] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=37] ["take time"=2.24172ms] [job="ID:56, Type:drop schema, State:running, SchemaState:write only, SchemaID:51, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:17:56.656 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:56.660 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:56, Type:drop schema, State:running, SchemaState:write only, SchemaID:51, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:17:56.656 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:56.661 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=37] [neededSchemaVersion=38] ["start time"=71.519µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 15:17:56.663 +00:00] [INFO] [ddl_worker.go:782] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=38] ["take time"=2.271123ms] [job="ID:56, Type:drop schema, State:running, SchemaState:delete only, SchemaID:51, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:17:56.656 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:56.664 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:56, Type:drop schema, State:running, SchemaState:delete only, SchemaID:51, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:17:56.656 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:56.665 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=38] [neededSchemaVersion=39] ["start time"=70.471µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 15:17:56.668 +00:00] [INFO] [ddl_worker.go:782] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=39] ["take time"=2.82099ms] [job="ID:56, Type:drop schema, State:done, SchemaState:none, SchemaID:51, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:17:56.656 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:56.668 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=56] [jobType="drop schema"]
   > [2024/07/23 15:17:56.669 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:56, Type:drop schema, State:synced, SchemaState:none, SchemaID:51, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:17:56.656 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:56.670 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=56]
   > [2024/07/23 15:17:56.670 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/07/23 15:17:56.671 +00:00] [INFO] [session.go:2166] ["CRUCIAL OPERATION"] [conn=6] [schemaVersion=39] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.15]
   > [2024/07/23 15:17:56.673 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:58, Type:create schema, State:none, SchemaState:none, SchemaID:57, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 15:17:56.673 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/23 15:17:56.674 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:58, Type:create schema, State:none, SchemaState:none, SchemaID:57, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 15:17:56.673 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/23 15:17:56.674 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:58, Type:create schema, State:none, SchemaState:none, SchemaID:57, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:17:56.673 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:56.676 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=39] [neededSchemaVersion=40] ["start time"=191.298µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 15:17:56.678 +00:00] [INFO] [ddl_worker.go:782] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=40] ["take time"=2.258971ms] [job="ID:58, Type:create schema, State:done, SchemaState:public, SchemaID:57, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 15:17:56.673 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:56.679 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:58, Type:create schema, State:synced, SchemaState:public, SchemaID:57, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:17:56.673 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:56.680 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=58]
   > [2024/07/23 15:17:56.680 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/07/23 15:17:56.682 +00:00] [INFO] [session.go:2166] ["CRUCIAL OPERATION"] [conn=6] [schemaVersion=40] [cur_db=testdb] [sql="create table t (id int auto_increment primary key, c int);"] [user=root@10.88.0.15]
   > [2024/07/23 15:17:56.684 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:60, Type:create table, State:none, SchemaState:none, SchemaID:57, TableID:59, RowCount:0, ArgLen:1, start time: 2024-07-23 15:17:56.683 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/23 15:17:56.684 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:60, Type:create table, State:none, SchemaState:none, SchemaID:57, TableID:59, RowCount:0, ArgLen:1, start time: 2024-07-23 15:17:56.683 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t (id int auto_increment primary key, c int);"]
   > [2024/07/23 15:17:56.684 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:60, Type:create table, State:none, SchemaState:none, SchemaID:57, TableID:59, RowCount:0, ArgLen:0, start time: 2024-07-23 15:17:56.683 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:56.686 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=40] [neededSchemaVersion=41] ["start time"=267.216µs] [phyTblIDs="[59]"] [actionTypes="[8]"]
   > [2024/07/23 15:17:56.688 +00:00] [INFO] [ddl_worker.go:782] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=41] ["take time"=2.257434ms] [job="ID:60, Type:create table, State:done, SchemaState:public, SchemaID:57, TableID:59, RowCount:0, ArgLen:1, start time: 2024-07-23 15:17:56.683 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:56.688 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:60, Type:create table, State:synced, SchemaState:public, SchemaID:57, TableID:59, RowCount:0, ArgLen:0, start time: 2024-07-23 15:17:56.683 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:56.689 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=60]
   > [2024/07/23 15:17:56.690 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/07/23 15:17:56.690 +00:00] [INFO] [split_region.go:60] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=46] ["first split key"=74800000000000003b]
   > [2024/07/23 15:17:56.690 +00:00] [INFO] [split_region.go:157] ["batch split regions complete"] ["batch region ID"=46] ["first at"=74800000000000003b] ["first new region left"="{Id:46 StartKey:7480000000000000ff3500000000000000f8 EndKey: RegionEpoch:{ConfVer:0 Version:1} Peers:[id:47 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/23 15:17:56.690 +00:00] [INFO] [split_region.go:209] ["split regions complete"] ["region count"=1] ["region IDs"="[46]"]
   > [2024/07/23 15:17:57.710 +00:00] [INFO] [set.go:216] ["set global var"] [conn=7] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/07/23 15:17:57.711 +00:00] [INFO] [set.go:216] ["set global var"] [conn=7] [name=transaction_isolation] [val=REPEATABLE-READ]
   > [2024/07/23 15:17:58.018 +00:00] [INFO] [session.go:2166] ["CRUCIAL OPERATION"] [conn=8] [schemaVersion=41] [cur_db=testdb] [sql=" alter table t add unique index uk(c);"] [user=root@10.88.0.15]
   > [2024/07/23 15:17:58.019 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:61, Type:add index, State:none, SchemaState:none, SchemaID:57, TableID:59, RowCount:0, ArgLen:5, start time: 2024-07-23 15:17:58.018 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/23 15:17:58.019 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:61, Type:add index, State:none, SchemaState:none, SchemaID:57, TableID:59, RowCount:0, ArgLen:5, start time: 2024-07-23 15:17:58.018 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query=" alter table t add unique index uk(c);"]
   > [2024/07/23 15:17:58.020 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 4, tp add index"] [job="ID:61, Type:add index, State:none, SchemaState:none, SchemaID:57, TableID:59, RowCount:0, ArgLen:0, start time: 2024-07-23 15:17:58.018 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:58.020 +00:00] [INFO] [index.go:462] ["[ddl] run add index job"] [job="ID:61, Type:add index, State:running, SchemaState:none, SchemaID:57, TableID:59, RowCount:0, ArgLen:5, start time: 2024-07-23 15:17:58.018 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [indexInfo="{\"id\":1,\"idx_name\":{\"O\":\"uk\",\"L\":\"uk\"},\"tbl_name\":{\"O\":\"\",\"L\":\"\"},\"idx_cols\":[{\"name\":{\"O\":\"c\",\"L\":\"c\"},\"offset\":1,\"length\":-1}],\"state\":0,\"comment\":\"\",\"index_type\":1,\"is_unique\":true,\"is_primary\":false,\"is_invisible\":false}"]
   > [2024/07/23 15:17:58.022 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=41] [neededSchemaVersion=42] ["start time"=286.283µs] [phyTblIDs="[59]"] [actionTypes="[128]"]
   > [2024/07/23 15:17:58.023 +00:00] [INFO] [ddl_worker.go:782] ["[ddl] wait latest schema version changed"] [worker="worker 4, tp add index"] [ver=42] ["take time"=2.232361ms] [job="ID:61, Type:add index, State:running, SchemaState:delete only, SchemaID:57, TableID:59, RowCount:0, ArgLen:5, start time: 2024-07-23 15:17:58.018 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:58.024 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 4, tp add index"] [job="ID:61, Type:add index, State:running, SchemaState:delete only, SchemaID:57, TableID:59, RowCount:0, ArgLen:0, start time: 2024-07-23 15:17:58.018 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:58.025 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=42] [neededSchemaVersion=43] ["start time"=268.892µs] [phyTblIDs="[59]"] [actionTypes="[128]"]
   > [2024/07/23 15:17:58.028 +00:00] [INFO] [ddl_worker.go:782] ["[ddl] wait latest schema version changed"] [worker="worker 4, tp add index"] [ver=43] ["take time"=3.003417ms] [job="ID:61, Type:add index, State:running, SchemaState:write only, SchemaID:57, TableID:59, RowCount:0, ArgLen:5, start time: 2024-07-23 15:17:58.018 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:58.028 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 4, tp add index"] [job="ID:61, Type:add index, State:running, SchemaState:write only, SchemaID:57, TableID:59, RowCount:0, ArgLen:0, start time: 2024-07-23 15:17:58.018 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:58.030 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=43] [neededSchemaVersion=44] ["start time"=276.854µs] [phyTblIDs="[59]"] [actionTypes="[128]"]
   > [2024/07/23 15:17:58.032 +00:00] [INFO] [ddl_worker.go:782] ["[ddl] wait latest schema version changed"] [worker="worker 4, tp add index"] [ver=44] ["take time"=2.952851ms] [job="ID:61, Type:add index, State:running, SchemaState:write reorganization, SchemaID:57, TableID:59, RowCount:0, ArgLen:5, start time: 2024-07-23 15:17:58.018 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:58.033 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 4, tp add index"] [job="ID:61, Type:add index, State:running, SchemaState:write reorganization, SchemaID:57, TableID:59, RowCount:0, ArgLen:0, start time: 2024-07-23 15:17:58.018 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:58.033 +00:00] [INFO] [reorg.go:430] ["[ddl] job get table range"] [jobID=61] [physicalTableID=59] [startHandle=1] [endHandle=3]
   > [2024/07/23 15:17:58.034 +00:00] [INFO] [ddl_worker.go:749] ["[ddl] schema version doesn't change"] [worker="worker 4, tp add index"]
   > [2024/07/23 15:17:58.034 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 4, tp add index"] [job="ID:61, Type:add index, State:running, SchemaState:write reorganization, SchemaID:57, TableID:59, RowCount:0, ArgLen:0, start time: 2024-07-23 15:17:58.018 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:451345875739082752"]
   > [2024/07/23 15:17:58.035 +00:00] [INFO] [index.go:1373] ["[ddl] start to add table index"] [job="ID:61, Type:add index, State:running, SchemaState:write reorganization, SchemaID:57, TableID:59, RowCount:0, ArgLen:5, start time: 2024-07-23 15:17:58.018 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:451345875739082752"] [reorgInfo=StartHandle:1,EndHandle:3,first:false,PhysicalTableID:59]
   > [2024/07/23 15:17:58.035 +00:00] [INFO] [index.go:1191] ["[ddl] split table range from PD"] [physicalTableID=59] [startHandle=1] [endHandle=3]
   > [2024/07/23 15:17:58.035 +00:00] [INFO] [index.go:1446] ["[ddl] start add index workers to reorg index"] [workerCnt=1] [regionCnt=1] [startHandle=1] [endHandle=3]
   > [2024/07/23 15:17:58.035 +00:00] [INFO] [index.go:1140] ["[ddl] add index worker start"] [workerID=0]
   > [2024/07/23 15:17:58.036 +00:00] [INFO] [index.go:1134] ["[ddl] add index worker finish task"] [workerID=0] [task="physicalTableID59_[1,3]"] [addedCount=2] [scanCount=2] [nextHandle=4] [takeTime=560.343µs]
   > [2024/07/23 15:17:58.036 +00:00] [INFO] [index.go:1290] ["[ddl] add index worker handle batch tasks successful"] [totalAddedCount=2] [startHandle=1] [nextHandle=4] [batchAddedCount=2] [takeTime=631.093µs]
   > [2024/07/23 15:17:58.036 +00:00] [INFO] [reorg.go:143] ["[ddl] run reorg job done"] ["handled rows"=2]
   > [2024/07/23 15:17:58.036 +00:00] [INFO] [index.go:1165] ["[ddl] add index worker exit"] [workerID=0]
   > [2024/07/23 15:17:58.037 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=44] [neededSchemaVersion=45] ["start time"=298.365µs] [phyTblIDs="[59]"] [actionTypes="[128]"]
   > [2024/07/23 15:17:58.039 +00:00] [INFO] [ddl_worker.go:782] ["[ddl] wait latest schema version changed"] [worker="worker 4, tp add index"] [ver=45] ["take time"=2.270425ms] [job="ID:61, Type:add index, State:done, SchemaState:public, SchemaID:57, TableID:59, RowCount:2, ArgLen:5, start time: 2024-07-23 15:17:58.018 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:451345875739082752"]
   > [2024/07/23 15:17:58.040 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 4, tp add index"] [job="ID:61, Type:add index, State:synced, SchemaState:public, SchemaID:57, TableID:59, RowCount:2, ArgLen:0, start time: 2024-07-23 15:17:58.018 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:451345875739082752"]
   > [2024/07/23 15:17:58.041 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=61]
   > [2024/07/23 15:17:58.041 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/07/23 15:17:58.314 +00:00] [INFO] [tidb.go:218] ["rollbackTxn for ddl/autocommit failed"]
   > [2024/07/23 15:17:58.314 +00:00] [INFO] [conn.go:787] ["command dispatched failed"] [conn=7] [connInfo="id:7, addr:10.88.0.15:39622 status:10, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:0, autocommit:1"] [sql=" update t set c = 2 where id = 3;"] [txn_mode=OPTIMISTIC] [err="[kv:1062]Duplicate entry '2' for key 'uk'"]
   > [2024/07/23 15:17:58.624 +00:00] [INFO] [domain.go:146] ["full load InfoSchema success"] [usedSchemaVersion=0] [neededSchemaVersion=45] ["start time"=10.066263ms]
   > [2024/07/23 15:17:58.624 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=45]
   > [2024/07/23 15:17:58.624 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=45]
   > [2024/07/23 15:17:58.635 +00:00] [INFO] [domain.go:146] ["full load InfoSchema success"] [usedSchemaVersion=0] [neededSchemaVersion=45] ["start time"=9.884743ms]
   > [2024/07/23 15:17:58.635 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=45]
   > [2024/07/23 15:17:58.636 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=45]
   > [2024/07/23 15:17:58.636 +00:00] [INFO] [admin.go:327] ["check indices count"] [table=t] [cnt=2] [index="\"uk\""] [cnt=2]
