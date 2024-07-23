# Bug ID TIDB-20910-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/20910
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
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
     - Output: ERROR: 9007 (HY000): Write conflict, txnStartTS=451345876397588480, conflictStartTS=451345876483833857, conflictCommitTS=451345876484096000, key={tableID=71, handle=3} primary=[]byte(nil) [try again later]
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #4:
     - Instruction:  admin check table t;
     - Transaction: conn_1
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 0 / 0

 * Container logs:
   > [2024/07/23 15:17:59.489 +00:00] [INFO] [session.go:2166] ["CRUCIAL OPERATION"] [conn=10] [schemaVersion=53] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.15]
   > [2024/07/23 15:17:59.490 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:68, Type:drop schema, State:none, SchemaState:none, SchemaID:63, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:17:59.489 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/23 15:17:59.490 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:68, Type:drop schema, State:none, SchemaState:none, SchemaID:63, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:17:59.489 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/23 15:17:59.491 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:68, Type:drop schema, State:none, SchemaState:none, SchemaID:63, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:17:59.489 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:59.492 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=53] [neededSchemaVersion=54] ["start time"=98.547µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 15:17:59.494 +00:00] [INFO] [ddl_worker.go:782] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=54] ["take time"=2.154976ms] [job="ID:68, Type:drop schema, State:running, SchemaState:write only, SchemaID:63, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:17:59.489 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:59.495 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:68, Type:drop schema, State:running, SchemaState:write only, SchemaID:63, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:17:59.489 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:59.496 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=54] [neededSchemaVersion=55] ["start time"=84.928µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 15:17:59.499 +00:00] [INFO] [ddl_worker.go:782] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=55] ["take time"=3.075494ms] [job="ID:68, Type:drop schema, State:running, SchemaState:delete only, SchemaID:63, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:17:59.489 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:59.499 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:68, Type:drop schema, State:running, SchemaState:delete only, SchemaID:63, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:17:59.489 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:59.501 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=55] [neededSchemaVersion=56] ["start time"=106.37µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 15:17:59.503 +00:00] [INFO] [ddl_worker.go:782] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=56] ["take time"=2.358984ms] [job="ID:68, Type:drop schema, State:done, SchemaState:none, SchemaID:63, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:17:59.489 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:59.504 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=68] [jobType="drop schema"]
   > [2024/07/23 15:17:59.504 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:68, Type:drop schema, State:synced, SchemaState:none, SchemaID:63, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:17:59.489 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:59.506 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=68]
   > [2024/07/23 15:17:59.506 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/07/23 15:17:59.507 +00:00] [INFO] [session.go:2166] ["CRUCIAL OPERATION"] [conn=10] [schemaVersion=56] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.15]
   > [2024/07/23 15:17:59.509 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:70, Type:create schema, State:none, SchemaState:none, SchemaID:69, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 15:17:59.508 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/23 15:17:59.509 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:70, Type:create schema, State:none, SchemaState:none, SchemaID:69, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 15:17:59.508 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/23 15:17:59.510 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:70, Type:create schema, State:none, SchemaState:none, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:17:59.508 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:59.511 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=56] [neededSchemaVersion=57] ["start time"=142.338µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 15:17:59.513 +00:00] [INFO] [ddl_worker.go:782] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=57] ["take time"=2.253383ms] [job="ID:70, Type:create schema, State:done, SchemaState:public, SchemaID:69, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 15:17:59.508 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:59.514 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:70, Type:create schema, State:synced, SchemaState:public, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:17:59.508 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:59.515 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=70]
   > [2024/07/23 15:17:59.515 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/07/23 15:17:59.518 +00:00] [INFO] [session.go:2166] ["CRUCIAL OPERATION"] [conn=10] [schemaVersion=57] [cur_db=testdb] [sql="create table t (id int auto_increment primary key, c int);"] [user=root@10.88.0.15]
   > [2024/07/23 15:17:59.519 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:72, Type:create table, State:none, SchemaState:none, SchemaID:69, TableID:71, RowCount:0, ArgLen:1, start time: 2024-07-23 15:17:59.518 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/23 15:17:59.519 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:72, Type:create table, State:none, SchemaState:none, SchemaID:69, TableID:71, RowCount:0, ArgLen:1, start time: 2024-07-23 15:17:59.518 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t (id int auto_increment primary key, c int);"]
   > [2024/07/23 15:17:59.520 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:72, Type:create table, State:none, SchemaState:none, SchemaID:69, TableID:71, RowCount:0, ArgLen:0, start time: 2024-07-23 15:17:59.518 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:59.521 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=57] [neededSchemaVersion=58] ["start time"=268.962µs] [phyTblIDs="[71]"] [actionTypes="[8]"]
   > [2024/07/23 15:17:59.523 +00:00] [INFO] [ddl_worker.go:782] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=58] ["take time"=2.235015ms] [job="ID:72, Type:create table, State:done, SchemaState:public, SchemaID:69, TableID:71, RowCount:0, ArgLen:1, start time: 2024-07-23 15:17:59.518 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:59.524 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:72, Type:create table, State:synced, SchemaState:public, SchemaID:69, TableID:71, RowCount:0, ArgLen:0, start time: 2024-07-23 15:17:59.518 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:17:59.525 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=72]
   > [2024/07/23 15:17:59.525 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/07/23 15:17:59.526 +00:00] [INFO] [split_region.go:60] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=50] ["first split key"=748000000000000047]
   > [2024/07/23 15:17:59.526 +00:00] [INFO] [split_region.go:157] ["batch split regions complete"] ["batch region ID"=50] ["first at"=748000000000000047] ["first new region left"="{Id:50 StartKey:7480000000000000ff4100000000000000f8 EndKey: RegionEpoch:{ConfVer:0 Version:1} Peers:[id:51 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/23 15:17:59.526 +00:00] [INFO] [split_region.go:209] ["split regions complete"] ["region count"=1] ["region IDs"="[50]"]
   > [2024/07/23 15:18:00.857 +00:00] [INFO] [session.go:2166] ["CRUCIAL OPERATION"] [conn=12] [schemaVersion=58] [cur_db=testdb] [sql=" alter table t add unique index uk(c);"] [user=root@10.88.0.15]
   > [2024/07/23 15:18:00.858 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:73, Type:add index, State:none, SchemaState:none, SchemaID:69, TableID:71, RowCount:0, ArgLen:5, start time: 2024-07-23 15:18:00.857 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/23 15:18:00.858 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:73, Type:add index, State:none, SchemaState:none, SchemaID:69, TableID:71, RowCount:0, ArgLen:5, start time: 2024-07-23 15:18:00.857 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query=" alter table t add unique index uk(c);"]
   > [2024/07/23 15:18:00.858 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 4, tp add index"] [job="ID:73, Type:add index, State:none, SchemaState:none, SchemaID:69, TableID:71, RowCount:0, ArgLen:0, start time: 2024-07-23 15:18:00.857 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:18:00.859 +00:00] [INFO] [index.go:462] ["[ddl] run add index job"] [job="ID:73, Type:add index, State:running, SchemaState:none, SchemaID:69, TableID:71, RowCount:0, ArgLen:5, start time: 2024-07-23 15:18:00.857 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [indexInfo="{\"id\":1,\"idx_name\":{\"O\":\"uk\",\"L\":\"uk\"},\"tbl_name\":{\"O\":\"\",\"L\":\"\"},\"idx_cols\":[{\"name\":{\"O\":\"c\",\"L\":\"c\"},\"offset\":1,\"length\":-1}],\"state\":0,\"comment\":\"\",\"index_type\":1,\"is_unique\":true,\"is_primary\":false,\"is_invisible\":false}"]
   > [2024/07/23 15:18:00.860 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=58] [neededSchemaVersion=59] ["start time"=331.959µs] [phyTblIDs="[71]"] [actionTypes="[128]"]
   > [2024/07/23 15:18:00.862 +00:00] [INFO] [ddl_worker.go:782] ["[ddl] wait latest schema version changed"] [worker="worker 4, tp add index"] [ver=59] ["take time"=2.237459ms] [job="ID:73, Type:add index, State:running, SchemaState:delete only, SchemaID:69, TableID:71, RowCount:0, ArgLen:5, start time: 2024-07-23 15:18:00.857 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:18:00.862 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 4, tp add index"] [job="ID:73, Type:add index, State:running, SchemaState:delete only, SchemaID:69, TableID:71, RowCount:0, ArgLen:0, start time: 2024-07-23 15:18:00.857 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:18:00.864 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=59] [neededSchemaVersion=60] ["start time"=333.985µs] [phyTblIDs="[71]"] [actionTypes="[128]"]
   > [2024/07/23 15:18:00.866 +00:00] [INFO] [ddl_worker.go:782] ["[ddl] wait latest schema version changed"] [worker="worker 4, tp add index"] [ver=60] ["take time"=2.940909ms] [job="ID:73, Type:add index, State:running, SchemaState:write only, SchemaID:69, TableID:71, RowCount:0, ArgLen:5, start time: 2024-07-23 15:18:00.857 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:18:00.867 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 4, tp add index"] [job="ID:73, Type:add index, State:running, SchemaState:write only, SchemaID:69, TableID:71, RowCount:0, ArgLen:0, start time: 2024-07-23 15:18:00.857 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:18:00.869 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=60] [neededSchemaVersion=61] ["start time"=327.699µs] [phyTblIDs="[71]"] [actionTypes="[128]"]
   > [2024/07/23 15:18:00.871 +00:00] [INFO] [ddl_worker.go:782] ["[ddl] wait latest schema version changed"] [worker="worker 4, tp add index"] [ver=61] ["take time"=2.25492ms] [job="ID:73, Type:add index, State:running, SchemaState:write reorganization, SchemaID:69, TableID:71, RowCount:0, ArgLen:5, start time: 2024-07-23 15:18:00.857 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:18:00.871 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 4, tp add index"] [job="ID:73, Type:add index, State:running, SchemaState:write reorganization, SchemaID:69, TableID:71, RowCount:0, ArgLen:0, start time: 2024-07-23 15:18:00.857 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:18:00.872 +00:00] [INFO] [reorg.go:430] ["[ddl] job get table range"] [jobID=73] [physicalTableID=71] [startHandle=1] [endHandle=3]
   > [2024/07/23 15:18:00.872 +00:00] [INFO] [ddl_worker.go:749] ["[ddl] schema version doesn't change"] [worker="worker 4, tp add index"]
   > [2024/07/23 15:18:00.873 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 4, tp add index"] [job="ID:73, Type:add index, State:running, SchemaState:write reorganization, SchemaID:69, TableID:71, RowCount:0, ArgLen:0, start time: 2024-07-23 15:18:00.857 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:451345876483047425"]
   > [2024/07/23 15:18:00.873 +00:00] [INFO] [index.go:1373] ["[ddl] start to add table index"] [job="ID:73, Type:add index, State:running, SchemaState:write reorganization, SchemaID:69, TableID:71, RowCount:0, ArgLen:5, start time: 2024-07-23 15:18:00.857 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:451345876483047425"] [reorgInfo=StartHandle:1,EndHandle:3,first:false,PhysicalTableID:71]
   > [2024/07/23 15:18:00.873 +00:00] [INFO] [index.go:1191] ["[ddl] split table range from PD"] [physicalTableID=71] [startHandle=1] [endHandle=3]
   > [2024/07/23 15:18:00.874 +00:00] [INFO] [index.go:1446] ["[ddl] start add index workers to reorg index"] [workerCnt=1] [regionCnt=1] [startHandle=1] [endHandle=3]
   > [2024/07/23 15:18:00.874 +00:00] [INFO] [index.go:1140] ["[ddl] add index worker start"] [workerID=0]
   > [2024/07/23 15:18:00.875 +00:00] [INFO] [index.go:1134] ["[ddl] add index worker finish task"] [workerID=0] [task="physicalTableID71_[1,3]"] [addedCount=2] [scanCount=2] [nextHandle=4] [takeTime=618.032µs]
   > [2024/07/23 15:18:00.875 +00:00] [INFO] [index.go:1290] ["[ddl] add index worker handle batch tasks successful"] [totalAddedCount=2] [startHandle=1] [nextHandle=4] [batchAddedCount=2] [takeTime=712.179µs]
   > [2024/07/23 15:18:00.875 +00:00] [INFO] [reorg.go:143] ["[ddl] run reorg job done"] ["handled rows"=2]
   > [2024/07/23 15:18:00.875 +00:00] [INFO] [index.go:1165] ["[ddl] add index worker exit"] [workerID=0]
   > [2024/07/23 15:18:00.876 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=61] [neededSchemaVersion=62] ["start time"=305.978µs] [phyTblIDs="[71]"] [actionTypes="[128]"]
   > [2024/07/23 15:18:00.878 +00:00] [INFO] [ddl_worker.go:782] ["[ddl] wait latest schema version changed"] [worker="worker 4, tp add index"] [ver=62] ["take time"=2.261345ms] [job="ID:73, Type:add index, State:done, SchemaState:public, SchemaID:69, TableID:71, RowCount:2, ArgLen:5, start time: 2024-07-23 15:18:00.857 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:451345876483047425"]
   > [2024/07/23 15:18:00.879 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 4, tp add index"] [job="ID:73, Type:add index, State:synced, SchemaState:public, SchemaID:69, TableID:71, RowCount:2, ArgLen:0, start time: 2024-07-23 15:18:00.857 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:451345876483047425"]
   > [2024/07/23 15:18:00.880 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=73]
   > [2024/07/23 15:18:00.880 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/07/23 15:18:01.451 +00:00] [WARN] [session.go:472] ["can not retry txn"] [conn=11] [label=general] [error="[kv:9007]Write conflict, txnStartTS=451345876397588480, conflictStartTS=451345876483833857, conflictCommitTS=451345876484096000, key={tableID=71, handle=3} primary=[]byte(nil) [try again later]"] [IsBatchInsert=false] [IsPessimistic=false] [InRestrictedSQL=false] [tidb_retry_limit=10] [tidb_disable_txn_auto_retry=true]
   > [2024/07/23 15:18:01.451 +00:00] [WARN] [session.go:487] ["commit failed"] [conn=11] ["finished txn"="Txn{state=invalid}"] [error="[kv:9007]Write conflict, txnStartTS=451345876397588480, conflictStartTS=451345876483833857, conflictCommitTS=451345876484096000, key={tableID=71, handle=3} primary=[]byte(nil) [try again later]"]
   > [2024/07/23 15:18:01.451 +00:00] [WARN] [session.go:1071] ["run statement failed"] [conn=11] [schemaVersion=58] [error="previous statement:  update t set c = 2 where id = 3;: [kv:9007]Write conflict, txnStartTS=451345876397588480, conflictStartTS=451345876483833857, conflictCommitTS=451345876484096000, key={tableID=71, handle=3} primary=[]byte(nil) [try again later]"] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 11,\n  \"status\": 2,\n  \"strictMode\": true,\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"10.88.0.15\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/07/23 15:18:01.451 +00:00] [INFO] [conn.go:787] ["command dispatched failed"] [conn=11] [connInfo="id:11, addr:10.88.0.15:39680 status:10, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:0, autocommit:1"] [sql=" commit;"] [txn_mode=OPTIMISTIC] [err="[kv:9007]Write conflict, txnStartTS=451345876397588480, conflictStartTS=451345876483833857, conflictCommitTS=451345876484096000, key={tableID=71, handle=3} primary=[]byte(nil) [try again later]\nprevious statement:  update t set c = 2 where id = 3;"]
   > [2024/07/23 15:18:01.451 +00:00] [INFO] [2pc.go:1305] ["2PC clean up done"] [conn=11] [txnStartTS=451345876397588480]
   > [2024/07/23 15:18:01.761 +00:00] [INFO] [domain.go:146] ["full load InfoSchema success"] [usedSchemaVersion=0] [neededSchemaVersion=62] ["start time"=10.007945ms]
   > [2024/07/23 15:18:01.761 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=62]
   > [2024/07/23 15:18:01.762 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=62]
   > [2024/07/23 15:18:01.772 +00:00] [INFO] [domain.go:146] ["full load InfoSchema success"] [usedSchemaVersion=0] [neededSchemaVersion=62] ["start time"=9.753021ms]
   > [2024/07/23 15:18:01.773 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=62]
   > [2024/07/23 15:18:01.773 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=62]
   > [2024/07/23 15:18:01.774 +00:00] [INFO] [admin.go:327] ["check indices count"] [table=t] [cnt=2] [index="\"uk\""] [cnt=2]

### Scenario 1
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
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
   > [2024/07/23 15:18:02.687 +00:00] [INFO] [session.go:2166] ["CRUCIAL OPERATION"] [conn=14] [schemaVersion=70] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.15]
   > [2024/07/23 15:18:02.687 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:80, Type:drop schema, State:none, SchemaState:none, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:18:02.687 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/23 15:18:02.687 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:80, Type:drop schema, State:none, SchemaState:none, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:18:02.687 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/23 15:18:02.687 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:80, Type:drop schema, State:none, SchemaState:none, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:18:02.687 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:18:02.688 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=70] [neededSchemaVersion=71] ["start time"=42.744µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 15:18:02.690 +00:00] [INFO] [ddl_worker.go:782] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=71] ["take time"=2.242628ms] [job="ID:80, Type:drop schema, State:running, SchemaState:write only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:18:02.687 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:18:02.691 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:80, Type:drop schema, State:running, SchemaState:write only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:18:02.687 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:18:02.692 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=71] [neededSchemaVersion=72] ["start time"=57.689µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 15:18:02.694 +00:00] [INFO] [ddl_worker.go:782] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=72] ["take time"=2.831815ms] [job="ID:80, Type:drop schema, State:running, SchemaState:delete only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:18:02.687 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:18:02.695 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:80, Type:drop schema, State:running, SchemaState:delete only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:18:02.687 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:18:02.695 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=72] [neededSchemaVersion=73] ["start time"=33.454µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 15:18:02.698 +00:00] [INFO] [ddl_worker.go:782] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=73] ["take time"=2.554542ms] [job="ID:80, Type:drop schema, State:done, SchemaState:none, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:18:02.687 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:18:02.698 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=80] [jobType="drop schema"]
   > [2024/07/23 15:18:02.698 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:80, Type:drop schema, State:synced, SchemaState:none, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:18:02.687 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:18:02.699 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=80]
   > [2024/07/23 15:18:02.699 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/07/23 15:18:02.700 +00:00] [INFO] [session.go:2166] ["CRUCIAL OPERATION"] [conn=14] [schemaVersion=73] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.15]
   > [2024/07/23 15:18:02.702 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:82, Type:create schema, State:none, SchemaState:none, SchemaID:81, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 15:18:02.701 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/23 15:18:02.702 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:82, Type:create schema, State:none, SchemaState:none, SchemaID:81, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 15:18:02.701 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/23 15:18:02.702 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:82, Type:create schema, State:none, SchemaState:none, SchemaID:81, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:18:02.701 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:18:02.704 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=73] [neededSchemaVersion=74] ["start time"=122.992µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 15:18:02.706 +00:00] [INFO] [ddl_worker.go:782] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=74] ["take time"=2.28153ms] [job="ID:82, Type:create schema, State:done, SchemaState:public, SchemaID:81, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 15:18:02.701 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:18:02.706 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:82, Type:create schema, State:synced, SchemaState:public, SchemaID:81, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:18:02.701 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:18:02.708 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=82]
   > [2024/07/23 15:18:02.708 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/07/23 15:18:02.710 +00:00] [INFO] [session.go:2166] ["CRUCIAL OPERATION"] [conn=14] [schemaVersion=74] [cur_db=testdb] [sql="create table t (id int auto_increment primary key, c int);"] [user=root@10.88.0.15]
   > [2024/07/23 15:18:02.712 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:84, Type:create table, State:none, SchemaState:none, SchemaID:81, TableID:83, RowCount:0, ArgLen:1, start time: 2024-07-23 15:18:02.711 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/23 15:18:02.712 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:84, Type:create table, State:none, SchemaState:none, SchemaID:81, TableID:83, RowCount:0, ArgLen:1, start time: 2024-07-23 15:18:02.711 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t (id int auto_increment primary key, c int);"]
   > [2024/07/23 15:18:02.713 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:84, Type:create table, State:none, SchemaState:none, SchemaID:81, TableID:83, RowCount:0, ArgLen:0, start time: 2024-07-23 15:18:02.711 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:18:02.714 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=74] [neededSchemaVersion=75] ["start time"=258.345µs] [phyTblIDs="[83]"] [actionTypes="[8]"]
   > [2024/07/23 15:18:02.716 +00:00] [INFO] [ddl_worker.go:782] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=75] ["take time"=2.262533ms] [job="ID:84, Type:create table, State:done, SchemaState:public, SchemaID:81, TableID:83, RowCount:0, ArgLen:1, start time: 2024-07-23 15:18:02.711 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:18:02.717 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:84, Type:create table, State:synced, SchemaState:public, SchemaID:81, TableID:83, RowCount:0, ArgLen:0, start time: 2024-07-23 15:18:02.711 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:18:02.719 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=84]
   > [2024/07/23 15:18:02.719 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/07/23 15:18:02.719 +00:00] [INFO] [split_region.go:60] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=54] ["first split key"=748000000000000053]
   > [2024/07/23 15:18:02.719 +00:00] [INFO] [split_region.go:157] ["batch split regions complete"] ["batch region ID"=54] ["first at"=748000000000000053] ["first new region left"="{Id:54 StartKey:7480000000000000ff4d00000000000000f8 EndKey: RegionEpoch:{ConfVer:0 Version:1} Peers:[id:55 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/23 15:18:02.720 +00:00] [INFO] [split_region.go:209] ["split regions complete"] ["region count"=1] ["region IDs"="[54]"]
   > [2024/07/23 15:18:03.743 +00:00] [INFO] [set.go:216] ["set global var"] [conn=15] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/07/23 15:18:03.744 +00:00] [INFO] [set.go:216] ["set global var"] [conn=15] [name=transaction_isolation] [val=READ-COMMITTED]
   > [2024/07/23 15:18:04.049 +00:00] [INFO] [session.go:2166] ["CRUCIAL OPERATION"] [conn=16] [schemaVersion=75] [cur_db=testdb] [sql=" alter table t add unique index uk(c);"] [user=root@10.88.0.15]
   > [2024/07/23 15:18:04.050 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:85, Type:add index, State:none, SchemaState:none, SchemaID:81, TableID:83, RowCount:0, ArgLen:5, start time: 2024-07-23 15:18:04.049 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/23 15:18:04.051 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:85, Type:add index, State:none, SchemaState:none, SchemaID:81, TableID:83, RowCount:0, ArgLen:5, start time: 2024-07-23 15:18:04.049 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query=" alter table t add unique index uk(c);"]
   > [2024/07/23 15:18:04.051 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 4, tp add index"] [job="ID:85, Type:add index, State:none, SchemaState:none, SchemaID:81, TableID:83, RowCount:0, ArgLen:0, start time: 2024-07-23 15:18:04.049 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:18:04.051 +00:00] [INFO] [index.go:462] ["[ddl] run add index job"] [job="ID:85, Type:add index, State:running, SchemaState:none, SchemaID:81, TableID:83, RowCount:0, ArgLen:5, start time: 2024-07-23 15:18:04.049 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [indexInfo="{\"id\":1,\"idx_name\":{\"O\":\"uk\",\"L\":\"uk\"},\"tbl_name\":{\"O\":\"\",\"L\":\"\"},\"idx_cols\":[{\"name\":{\"O\":\"c\",\"L\":\"c\"},\"offset\":1,\"length\":-1}],\"state\":0,\"comment\":\"\",\"index_type\":1,\"is_unique\":true,\"is_primary\":false,\"is_invisible\":false}"]
   > [2024/07/23 15:18:04.053 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=75] [neededSchemaVersion=76] ["start time"=326.582µs] [phyTblIDs="[83]"] [actionTypes="[128]"]
   > [2024/07/23 15:18:04.055 +00:00] [INFO] [ddl_worker.go:782] ["[ddl] wait latest schema version changed"] [worker="worker 4, tp add index"] [ver=76] ["take time"=2.279993ms] [job="ID:85, Type:add index, State:running, SchemaState:delete only, SchemaID:81, TableID:83, RowCount:0, ArgLen:5, start time: 2024-07-23 15:18:04.049 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:18:04.055 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 4, tp add index"] [job="ID:85, Type:add index, State:running, SchemaState:delete only, SchemaID:81, TableID:83, RowCount:0, ArgLen:0, start time: 2024-07-23 15:18:04.049 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:18:04.056 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=76] [neededSchemaVersion=77] ["start time"=245.705µs] [phyTblIDs="[83]"] [actionTypes="[128]"]
   > [2024/07/23 15:18:04.059 +00:00] [INFO] [ddl_worker.go:782] ["[ddl] wait latest schema version changed"] [worker="worker 4, tp add index"] [ver=77] ["take time"=2.888038ms] [job="ID:85, Type:add index, State:running, SchemaState:write only, SchemaID:81, TableID:83, RowCount:0, ArgLen:5, start time: 2024-07-23 15:18:04.049 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:18:04.059 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 4, tp add index"] [job="ID:85, Type:add index, State:running, SchemaState:write only, SchemaID:81, TableID:83, RowCount:0, ArgLen:0, start time: 2024-07-23 15:18:04.049 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:18:04.061 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=77] [neededSchemaVersion=78] ["start time"=285.026µs] [phyTblIDs="[83]"] [actionTypes="[128]"]
   > [2024/07/23 15:18:04.063 +00:00] [INFO] [ddl_worker.go:782] ["[ddl] wait latest schema version changed"] [worker="worker 4, tp add index"] [ver=78] ["take time"=2.230964ms] [job="ID:85, Type:add index, State:running, SchemaState:write reorganization, SchemaID:81, TableID:83, RowCount:0, ArgLen:5, start time: 2024-07-23 15:18:04.049 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:18:04.063 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 4, tp add index"] [job="ID:85, Type:add index, State:running, SchemaState:write reorganization, SchemaID:81, TableID:83, RowCount:0, ArgLen:0, start time: 2024-07-23 15:18:04.049 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:18:04.063 +00:00] [INFO] [reorg.go:430] ["[ddl] job get table range"] [jobID=85] [physicalTableID=83] [startHandle=1] [endHandle=3]
   > [2024/07/23 15:18:04.064 +00:00] [INFO] [ddl_worker.go:749] ["[ddl] schema version doesn't change"] [worker="worker 4, tp add index"]
   > [2024/07/23 15:18:04.064 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 4, tp add index"] [job="ID:85, Type:add index, State:running, SchemaState:write reorganization, SchemaID:81, TableID:83, RowCount:0, ArgLen:0, start time: 2024-07-23 15:18:04.049 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:451345877319811073"]
   > [2024/07/23 15:18:04.064 +00:00] [INFO] [index.go:1373] ["[ddl] start to add table index"] [job="ID:85, Type:add index, State:running, SchemaState:write reorganization, SchemaID:81, TableID:83, RowCount:0, ArgLen:5, start time: 2024-07-23 15:18:04.049 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:451345877319811073"] [reorgInfo=StartHandle:1,EndHandle:3,first:false,PhysicalTableID:83]
   > [2024/07/23 15:18:04.065 +00:00] [INFO] [index.go:1191] ["[ddl] split table range from PD"] [physicalTableID=83] [startHandle=1] [endHandle=3]
   > [2024/07/23 15:18:04.065 +00:00] [INFO] [index.go:1446] ["[ddl] start add index workers to reorg index"] [workerCnt=1] [regionCnt=1] [startHandle=1] [endHandle=3]
   > [2024/07/23 15:18:04.065 +00:00] [INFO] [index.go:1140] ["[ddl] add index worker start"] [workerID=0]
   > [2024/07/23 15:18:04.065 +00:00] [INFO] [index.go:1134] ["[ddl] add index worker finish task"] [workerID=0] [task="physicalTableID83_[1,3]"] [addedCount=2] [scanCount=2] [nextHandle=4] [takeTime=382.175µs]
   > [2024/07/23 15:18:04.066 +00:00] [INFO] [index.go:1290] ["[ddl] add index worker handle batch tasks successful"] [totalAddedCount=2] [startHandle=1] [nextHandle=4] [batchAddedCount=2] [takeTime=434.138µs]
   > [2024/07/23 15:18:04.066 +00:00] [INFO] [reorg.go:143] ["[ddl] run reorg job done"] ["handled rows"=2]
   > [2024/07/23 15:18:04.066 +00:00] [INFO] [index.go:1165] ["[ddl] add index worker exit"] [workerID=0]
   > [2024/07/23 15:18:04.067 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=78] [neededSchemaVersion=79] ["start time"=224.263µs] [phyTblIDs="[83]"] [actionTypes="[128]"]
   > [2024/07/23 15:18:04.069 +00:00] [INFO] [ddl_worker.go:782] ["[ddl] wait latest schema version changed"] [worker="worker 4, tp add index"] [ver=79] ["take time"=2.229218ms] [job="ID:85, Type:add index, State:done, SchemaState:public, SchemaID:81, TableID:83, RowCount:2, ArgLen:5, start time: 2024-07-23 15:18:04.049 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:451345877319811073"]
   > [2024/07/23 15:18:04.069 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 4, tp add index"] [job="ID:85, Type:add index, State:synced, SchemaState:public, SchemaID:81, TableID:83, RowCount:2, ArgLen:0, start time: 2024-07-23 15:18:04.049 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:451345877319811073"]
   > [2024/07/23 15:18:04.070 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=85]
   > [2024/07/23 15:18:04.071 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/07/23 15:18:04.344 +00:00] [INFO] [tidb.go:218] ["rollbackTxn for ddl/autocommit failed"]
   > [2024/07/23 15:18:04.344 +00:00] [INFO] [conn.go:787] ["command dispatched failed"] [conn=15] [connInfo="id:15, addr:10.88.0.15:58336 status:10, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:0, autocommit:1"] [sql=" update t set c = 2 where id = 3;"] [txn_mode=OPTIMISTIC] [err="[kv:1062]Duplicate entry '2' for key 'uk'"]
   > [2024/07/23 15:18:04.658 +00:00] [INFO] [domain.go:146] ["full load InfoSchema success"] [usedSchemaVersion=0] [neededSchemaVersion=79] ["start time"=12.983635ms]
   > [2024/07/23 15:18:04.658 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=79]
   > [2024/07/23 15:18:04.658 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=79]
   > [2024/07/23 15:18:04.669 +00:00] [INFO] [domain.go:146] ["full load InfoSchema success"] [usedSchemaVersion=0] [neededSchemaVersion=79] ["start time"=9.929722ms]
   > [2024/07/23 15:18:04.669 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=79]
   > [2024/07/23 15:18:04.670 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=79]
   > [2024/07/23 15:18:04.670 +00:00] [INFO] [admin.go:327] ["check indices count"] [table=t] [cnt=2] [index="\"uk\""] [cnt=2]
