# Bug ID TIDB-8393-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/8393
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              Gets warnings when running in a transaction.


## Details
 * Database: tidb-v6.4.0
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
     - Instruction:  set @a = 100;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 0 / 0
 * Instruction #3:
     - Instruction:  insert into t values(1, 1);
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 1 / 0
 * Instruction #4:
     - Instruction:  rollback;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows / Warnings: 0 / 0
 * Instruction #5:
     - Instruction:  select @a;
     - Transaction: conn_0
     - Output: [(100,)]
     - Executed order: 5
     - Affected rows / Warnings: 1 / 0

 * Container logs:
   > [2024/07/12 14:19:17.112 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/12 14:19:17.114 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=2199023255963] [schemaVersion=44] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/12 14:19:17.117 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:80, Type:drop schema, State:queueing, SchemaState:public, SchemaID:75, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-12 14:19:17.116 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/12 14:19:17.117 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:80, Type:drop schema, State:queueing, SchemaState:public, SchemaID:75, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-12 14:19:17.116 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/12 14:19:17.123 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:80, Type:drop schema, State:queueing, SchemaState:public, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-12 14:19:17.116 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/12 14:19:17.126 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=44] [neededSchemaVersion=45] ["start time"=77.106µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/12 14:19:17.128 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=45] ["take time"=2.337265ms] [job="ID:80, Type:drop schema, State:running, SchemaState:write only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-12 14:19:17.116 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/12 14:19:17.131 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:80, Type:drop schema, State:running, SchemaState:write only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-12 14:19:17.116 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/12 14:19:17.134 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=45] [neededSchemaVersion=46] ["start time"=71.378µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/12 14:19:17.136 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=46] ["take time"=2.324903ms] [job="ID:80, Type:drop schema, State:running, SchemaState:delete only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-12 14:19:17.116 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/12 14:19:17.140 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:80, Type:drop schema, State:running, SchemaState:delete only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-12 14:19:17.116 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/12 14:19:17.142 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=46] [neededSchemaVersion=47] ["start time"=73.823µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/12 14:19:17.144 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=47] ["take time"=2.181796ms] [job="ID:80, Type:drop schema, State:done, SchemaState:none, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-12 14:19:17.116 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/12 14:19:17.148 +00:00] [INFO] [delete_range.go:109] ["[ddl] add job into delete-range table"] [jobID=80] [jobType="drop schema"]
   > [2024/07/12 14:19:17.149 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:80, Type:drop schema, State:synced, SchemaState:none, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-12 14:19:17.116 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/12 14:19:17.151 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=80]
   > [2024/07/12 14:19:17.151 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/12 14:19:17.152 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=2199023255963] [schemaVersion=47] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/12 14:19:17.156 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:82, Type:create schema, State:queueing, SchemaState:none, SchemaID:81, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-12 14:19:17.154 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/12 14:19:17.156 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:82, Type:create schema, State:queueing, SchemaState:none, SchemaID:81, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-12 14:19:17.154 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/12 14:19:17.163 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:82, Type:create schema, State:queueing, SchemaState:none, SchemaID:81, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-12 14:19:17.154 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/12 14:19:17.166 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=47] [neededSchemaVersion=48] ["start time"=141.081µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/12 14:19:17.168 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=48] ["take time"=2.431621ms] [job="ID:82, Type:create schema, State:done, SchemaState:public, SchemaID:81, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-12 14:19:17.154 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/12 14:19:17.172 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:82, Type:create schema, State:synced, SchemaState:public, SchemaID:81, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-12 14:19:17.154 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/12 14:19:17.174 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=82]
   > [2024/07/12 14:19:17.174 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/12 14:19:17.177 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=2199023255963] [schemaVersion=48] [cur_db=testdb] [sql="create table t(a bigint, b bigint);"] [user=root@%]
   > [2024/07/12 14:19:17.180 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:84, Type:create table, State:queueing, SchemaState:none, SchemaID:81, TableID:83, RowCount:0, ArgLen:2, start time: 2024-07-12 14:19:17.178 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/12 14:19:17.180 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:84, Type:create table, State:queueing, SchemaState:none, SchemaID:81, TableID:83, RowCount:0, ArgLen:2, start time: 2024-07-12 14:19:17.178 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t(a bigint, b bigint);"]
   > [2024/07/12 14:19:17.187 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:84, Type:create table, State:queueing, SchemaState:none, SchemaID:81, TableID:83, RowCount:0, ArgLen:0, start time: 2024-07-12 14:19:17.178 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/12 14:19:17.191 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=48] [neededSchemaVersion=49] ["start time"=328.397µs] [phyTblIDs="[83]"] [actionTypes="[8]"]
   > [2024/07/12 14:19:17.193 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=49] ["take time"=2.310446ms] [job="ID:84, Type:create table, State:done, SchemaState:public, SchemaID:81, TableID:83, RowCount:0, ArgLen:2, start time: 2024-07-12 14:19:17.178 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/12 14:19:17.197 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:84, Type:create table, State:synced, SchemaState:public, SchemaID:81, TableID:83, RowCount:0, ArgLen:0, start time: 2024-07-12 14:19:17.178 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/12 14:19:17.199 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=84]
   > [2024/07/12 14:19:17.199 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/12 14:19:17.200 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=80] ["first split key"=748000000000000053]
   > [2024/07/12 14:19:17.200 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=80] ["first at"=748000000000000053] ["first new region left"="{Id:80 StartKey:7480000000000000ff4d00000000000000f8 EndKey:7480000000000000ff5300000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:81 store_id:1 ] EncryptionMeta:<nil> IsInFlashback:false}"] ["new region count"=1]
   > [2024/07/12 14:19:17.200 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[80]"]
   > [2024/07/12 14:19:18.211 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/12 14:19:18.225 +00:00] [INFO] [set.go:141] ["set global var"] [conn=2199023255965] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/07/12 14:19:19.112 +00:00] [WARN] [2pc.go:1873] ["schemaLeaseChecker is not set for this transaction"] [sessionID=2199023255965] [startTS=451095811617193984] [checkTS=451095811617456128]
