# Bug ID TIDB-20881-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/20881
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              The insert should block until the other transaction is committed, but it doesn't.


## Details
 * Database: tidb-v4.0.4
 * Number of scenarios: 1
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
   > [2024/07/17 14:01:48.622 +00:00] [INFO] [server.go:388] ["new connection"] [conn=2] [remoteAddr=10.88.0.13:38014]
   > [2024/07/17 14:01:48.624 +00:00] [INFO] [session.go:2130] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=22] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.13]
   > [2024/07/17 14:01:48.625 +00:00] [INFO] [session.go:2130] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=22] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.13]
   > [2024/07/17 14:01:48.627 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-17 14:01:48.626 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/17 14:01:48.627 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-17 14:01:48.626 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/17 14:01:48.627 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-17 14:01:48.626 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 14:01:48.629 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=22] [neededSchemaVersion=23] ["start time"=136.052µs] [tblIDs="[]"]
   > [2024/07/17 14:01:48.630 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=23] ["take time"=2.142611ms] [job="ID:46, Type:create schema, State:done, SchemaState:public, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-17 14:01:48.626 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 14:01:48.631 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:46, Type:create schema, State:synced, SchemaState:public, SchemaID:45, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-17 14:01:48.626 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 14:01:48.632 +00:00] [INFO] [ddl.go:509] ["[ddl] DDL job is finished"] [jobID=46]
   > [2024/07/17 14:01:48.632 +00:00] [INFO] [domain.go:624] ["performing DDL change, must reload"]
   > [2024/07/17 14:01:48.635 +00:00] [INFO] [session.go:2130] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=23] [cur_db=testdb] [sql="create table t (a char(10) collate utf8mb4_unicode_ci, b char(20) collate utf8mb4_general_ci, c int, primary key (a, b, c));"] [user=root@10.88.0.13]
   > [2024/07/17 14:01:48.637 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-07-17 14:01:48.635 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/17 14:01:48.637 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-07-17 14:01:48.635 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t (a char(10) collate utf8mb4_unicode_ci, b char(20) collate utf8mb4_general_ci, c int, primary key (a, b, c));"]
   > [2024/07/17 14:01:48.638 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-17 14:01:48.635 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 14:01:48.642 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=23] [neededSchemaVersion=24] ["start time"=642.406µs] [tblIDs="[47]"]
   > [2024/07/17 14:01:48.643 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=24] ["take time"=2.146801ms] [job="ID:48, Type:create table, State:done, SchemaState:public, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-07-17 14:01:48.635 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 14:01:48.645 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:48, Type:create table, State:synced, SchemaState:public, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-17 14:01:48.635 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 14:01:48.646 +00:00] [INFO] [ddl.go:509] ["[ddl] DDL job is finished"] [jobID=48]
   > [2024/07/17 14:01:48.646 +00:00] [INFO] [domain.go:624] ["performing DDL change, must reload"]
   > [2024/07/17 14:01:48.647 +00:00] [INFO] [split_region.go:56] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=42] ["first split key"=74800000000000002f]
   > [2024/07/17 14:01:48.647 +00:00] [INFO] [split_region.go:153] ["batch split regions complete"] ["batch region ID"=42] ["first at"=74800000000000002f] ["first new region left"="{Id:42 StartKey:7480000000000000ff2b00000000000000f8 EndKey: RegionEpoch:{ConfVer:0 Version:1} Peers:[id:43 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/17 14:01:48.647 +00:00] [INFO] [split_region.go:205] ["split regions complete"] ["region count"=1] ["region IDs"="[42]"]
   > [2024/07/17 14:01:48.647 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=2]
   > [2024/07/17 14:01:49.666 +00:00] [INFO] [server.go:388] ["new connection"] [conn=3] [remoteAddr=10.88.0.13:38016]
   > [2024/07/17 14:01:49.669 +00:00] [INFO] [set.go:207] ["set session var"] [conn=3] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/07/17 14:01:50.966 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=3]
