# Bug ID TIDB-20881-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/20881
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              The insert should block until the other transaction is committed, but it doesn't.


## Details
 * Database: tidb-v4.0.4
 * Number of scenarios: 1
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
     - Instruction:  begin;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  insert into t values ("$", "c", 20);
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 1 / 0
 * Instruction #3:
     - Instruction:  select * from t;
     - Transaction: conn_0
     - Output: [('$', 'c', 20)]
     - Executed order: 3
     - Affected rows / Warnings: 1 / 0

 * Container logs:
   > [2024/07/17 14:01:51.396 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=4]
   > [2024/07/17 14:01:51.400 +00:00] [INFO] [server.go:388] ["new connection"] [conn=5] [remoteAddr=10.88.0.13:38034]
   > [2024/07/17 14:01:51.402 +00:00] [INFO] [session.go:2130] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=32] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.13]
   > [2024/07/17 14:01:51.403 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:55, Type:drop schema, State:none, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-17 14:01:51.402 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/17 14:01:51.403 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:55, Type:drop schema, State:none, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-17 14:01:51.402 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/17 14:01:51.404 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:55, Type:drop schema, State:none, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-17 14:01:51.402 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 14:01:51.405 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=32] [neededSchemaVersion=33] ["start time"=77.315µs] [tblIDs="[]"]
   > [2024/07/17 14:01:51.407 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=33] ["take time"=2.148687ms] [job="ID:55, Type:drop schema, State:running, SchemaState:write only, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-17 14:01:51.402 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 14:01:51.408 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:55, Type:drop schema, State:running, SchemaState:write only, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-17 14:01:51.402 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 14:01:51.409 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=33] [neededSchemaVersion=34] ["start time"=95.404µs] [tblIDs="[]"]
   > [2024/07/17 14:01:51.411 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=34] ["take time"=2.144846ms] [job="ID:55, Type:drop schema, State:running, SchemaState:delete only, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-17 14:01:51.402 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 14:01:51.412 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:55, Type:drop schema, State:running, SchemaState:delete only, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-17 14:01:51.402 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 14:01:51.413 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=34] [neededSchemaVersion=35] ["start time"=81.646µs] [tblIDs="[]"]
   > [2024/07/17 14:01:51.415 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=35] ["take time"=2.140865ms] [job="ID:55, Type:drop schema, State:done, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-17 14:01:51.402 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 14:01:51.416 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=55] [jobType="drop schema"]
   > [2024/07/17 14:01:51.416 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:55, Type:drop schema, State:synced, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-17 14:01:51.402 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 14:01:51.418 +00:00] [INFO] [ddl.go:509] ["[ddl] DDL job is finished"] [jobID=55]
   > [2024/07/17 14:01:51.418 +00:00] [INFO] [domain.go:624] ["performing DDL change, must reload"]
   > [2024/07/17 14:01:51.419 +00:00] [INFO] [session.go:2130] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=35] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.13]
   > [2024/07/17 14:01:51.421 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:57, Type:create schema, State:none, SchemaState:none, SchemaID:56, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-17 14:01:51.42 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/17 14:01:51.421 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:57, Type:create schema, State:none, SchemaState:none, SchemaID:56, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-17 14:01:51.42 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/17 14:01:51.422 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:57, Type:create schema, State:none, SchemaState:none, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-17 14:01:51.42 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 14:01:51.423 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=35] [neededSchemaVersion=36] ["start time"=233.831µs] [tblIDs="[]"]
   > [2024/07/17 14:01:51.425 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=36] ["take time"=2.149106ms] [job="ID:57, Type:create schema, State:done, SchemaState:public, SchemaID:56, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-17 14:01:51.42 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 14:01:51.426 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:57, Type:create schema, State:synced, SchemaState:public, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-17 14:01:51.42 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 14:01:51.427 +00:00] [INFO] [ddl.go:509] ["[ddl] DDL job is finished"] [jobID=57]
   > [2024/07/17 14:01:51.427 +00:00] [INFO] [domain.go:624] ["performing DDL change, must reload"]
   > [2024/07/17 14:01:51.430 +00:00] [INFO] [session.go:2130] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=36] [cur_db=testdb] [sql="create table t (a char(10) collate utf8mb4_unicode_ci, b char(20) collate utf8mb4_general_ci, c int, primary key (a, b, c));"] [user=root@10.88.0.13]
   > [2024/07/17 14:01:51.431 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:59, Type:create table, State:none, SchemaState:none, SchemaID:56, TableID:58, RowCount:0, ArgLen:1, start time: 2024-07-17 14:01:51.43 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/17 14:01:51.431 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:59, Type:create table, State:none, SchemaState:none, SchemaID:56, TableID:58, RowCount:0, ArgLen:1, start time: 2024-07-17 14:01:51.43 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t (a char(10) collate utf8mb4_unicode_ci, b char(20) collate utf8mb4_general_ci, c int, primary key (a, b, c));"]
   > [2024/07/17 14:01:51.431 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:59, Type:create table, State:none, SchemaState:none, SchemaID:56, TableID:58, RowCount:0, ArgLen:0, start time: 2024-07-17 14:01:51.43 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 14:01:51.432 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=36] [neededSchemaVersion=37] ["start time"=208.757µs] [tblIDs="[58]"]
   > [2024/07/17 14:01:51.434 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=37] ["take time"=2.13011ms] [job="ID:59, Type:create table, State:done, SchemaState:public, SchemaID:56, TableID:58, RowCount:0, ArgLen:1, start time: 2024-07-17 14:01:51.43 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 14:01:51.435 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:59, Type:create table, State:synced, SchemaState:public, SchemaID:56, TableID:58, RowCount:0, ArgLen:0, start time: 2024-07-17 14:01:51.43 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 14:01:51.436 +00:00] [INFO] [ddl.go:509] ["[ddl] DDL job is finished"] [jobID=59]
   > [2024/07/17 14:01:51.436 +00:00] [INFO] [domain.go:624] ["performing DDL change, must reload"]
   > [2024/07/17 14:01:51.436 +00:00] [INFO] [split_region.go:56] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=46] ["first split key"=74800000000000003a]
   > [2024/07/17 14:01:51.436 +00:00] [INFO] [split_region.go:153] ["batch split regions complete"] ["batch region ID"=46] ["first at"=74800000000000003a] ["first new region left"="{Id:46 StartKey:7480000000000000ff3400000000000000f8 EndKey: RegionEpoch:{ConfVer:0 Version:1} Peers:[id:47 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/17 14:01:51.437 +00:00] [INFO] [split_region.go:205] ["split regions complete"] ["region count"=1] ["region IDs"="[46]"]
   > [2024/07/17 14:01:51.437 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=5]
   > [2024/07/17 14:01:52.448 +00:00] [INFO] [server.go:388] ["new connection"] [conn=6] [remoteAddr=10.88.0.13:38040]
   > [2024/07/17 14:01:52.451 +00:00] [INFO] [set.go:207] ["set session var"] [conn=6] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/07/17 14:01:53.748 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=6]
