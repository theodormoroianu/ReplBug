# Bug ID TIDB-37925-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/37925
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              Duplicates in primary key do not throw an error


## Details
 * Database: tidb-v6.3.0
 * Number of scenarios: 2
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
     - Instruction:  begin pessimistic;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  update tbl_4 set tbl_4.col_17 = '11:16:44.00' ,tbl_4.col_17 = '03:51:50.00' ,tb...
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 1 / 0
 * Instruction #3:
     - Instruction:  select col_20 from tbl_4 order by col_20;
     - Transaction: conn_0
     - Output: [(-31298,), (-31298,), (-31136,), (-30900,), (-29720,), (-29720,), (-15820,), (-12681,), (-10830,), (15880,), (26689,), (30926,)]
     - Executed order: 3
     - Affected rows / Warnings: 12 / 0
 * Instruction #4:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows / Warnings: 0 / 0

 * Container logs:
   > [2024/07/23 17:19:02.147 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/23 17:19:02.149 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255969] [schemaVersion=56] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/23 17:19:02.151 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:89, Type:drop schema, State:queueing, SchemaState:public, SchemaID:84, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 17:19:02.149 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/23 17:19:02.151 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:89, Type:drop schema, State:queueing, SchemaState:public, SchemaID:84, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 17:19:02.149 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/23 17:19:02.157 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:89, Type:drop schema, State:queueing, SchemaState:public, SchemaID:84, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 17:19:02.149 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:19:02.159 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=56] [neededSchemaVersion=57] ["start time"=86.325µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 17:19:02.161 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=57] ["take time"=2.259736ms] [job="ID:89, Type:drop schema, State:running, SchemaState:write only, SchemaID:84, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 17:19:02.149 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:19:02.164 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:89, Type:drop schema, State:running, SchemaState:write only, SchemaID:84, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 17:19:02.149 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:19:02.166 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=57] [neededSchemaVersion=58] ["start time"=65.791µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 17:19:02.168 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=58] ["take time"=2.551536ms] [job="ID:89, Type:drop schema, State:running, SchemaState:delete only, SchemaID:84, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 17:19:02.149 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:19:02.171 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:89, Type:drop schema, State:running, SchemaState:delete only, SchemaID:84, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 17:19:02.149 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:19:02.174 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=58] [neededSchemaVersion=59] ["start time"=69.702µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 17:19:02.176 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=59] ["take time"=2.27594ms] [job="ID:89, Type:drop schema, State:done, SchemaState:none, SchemaID:84, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 17:19:02.149 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:19:02.180 +00:00] [INFO] [delete_range.go:109] ["[ddl] add job into delete-range table"] [jobID=89] [jobType="drop schema"]
   > [2024/07/23 17:19:02.180 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:89, Type:drop schema, State:synced, SchemaState:none, SchemaID:84, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 17:19:02.149 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:19:02.182 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=89]
   > [2024/07/23 17:19:02.182 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/23 17:19:02.183 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255969] [schemaVersion=59] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/23 17:19:02.186 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:91, Type:create schema, State:queueing, SchemaState:none, SchemaID:90, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 17:19:02.184 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/23 17:19:02.186 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:91, Type:create schema, State:queueing, SchemaState:none, SchemaID:90, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 17:19:02.184 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/23 17:19:02.193 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:91, Type:create schema, State:queueing, SchemaState:none, SchemaID:90, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 17:19:02.184 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:19:02.197 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=59] [neededSchemaVersion=60] ["start time"=168.32µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 17:19:02.198 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=60] ["take time"=2.269305ms] [job="ID:91, Type:create schema, State:done, SchemaState:public, SchemaID:90, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 17:19:02.184 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:19:02.202 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:91, Type:create schema, State:synced, SchemaState:public, SchemaID:90, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 17:19:02.184 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:19:02.204 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=91]
   > [2024/07/23 17:19:02.204 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/23 17:19:02.207 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255969] [schemaVersion=60] [cur_db=testdb] [sql="create table tbl_4 (\n    col_16 decimal ( 38 , 4 )   not null ,\n    col_17 time    default '23:52:24.00' ,\n    col_18 char ( 235 ) collate utf8_bin ,\n    col_19 tinyint  unsigned not null default 151 ,\n    col_20 smallint    default 9203 ,\n    primary key  ( col_20 ) /*T![clustered_index] nonclustered */ ,\n    key idx_8 ( col_18 ( 1 ) )\n) charset utf8mb4 collate utf8mb4_bin ;"] [user=root@%]
   > [2024/07/23 17:19:02.210 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:93, Type:create table, State:queueing, SchemaState:none, SchemaID:90, TableID:92, RowCount:0, ArgLen:1, start time: 2024-07-23 17:19:02.208 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/23 17:19:02.211 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:93, Type:create table, State:queueing, SchemaState:none, SchemaID:90, TableID:92, RowCount:0, ArgLen:1, start time: 2024-07-23 17:19:02.208 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table tbl_4 (\n    col_16 decimal ( 38 , 4 )   not null ,\n    col_17 time    default '23:52:24.00' ,\n    col_18 char ( 235 ) collate utf8_bin ,\n    col_19 tinyint  unsigned not null default 151 ,\n    col_20 smallint    default 9203 ,\n    primary key  ( col_20 ) /*T![clustered_index] nonclustered */ ,\n    key idx_8 ( col_18 ( 1 ) )\n) charset utf8mb4 collate utf8mb4_bin ;"]
   > [2024/07/23 17:19:02.217 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:93, Type:create table, State:queueing, SchemaState:none, SchemaID:90, TableID:92, RowCount:0, ArgLen:0, start time: 2024-07-23 17:19:02.208 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:19:02.221 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=60] [neededSchemaVersion=61] ["start time"=460.328µs] [phyTblIDs="[92]"] [actionTypes="[8]"]
   > [2024/07/23 17:19:02.222 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=61] ["take time"=2.04176ms] [job="ID:93, Type:create table, State:done, SchemaState:public, SchemaID:90, TableID:92, RowCount:0, ArgLen:1, start time: 2024-07-23 17:19:02.208 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:19:02.226 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:93, Type:create table, State:synced, SchemaState:public, SchemaID:90, TableID:92, RowCount:0, ArgLen:0, start time: 2024-07-23 17:19:02.208 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:19:02.229 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=93]
   > [2024/07/23 17:19:02.229 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/23 17:19:02.229 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=74] ["first split key"=74800000000000005c]
   > [2024/07/23 17:19:02.229 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=74] ["first at"=74800000000000005c] ["first new region left"="{Id:74 StartKey:7480000000000000ff5600000000000000f8 EndKey:7480000000000000ff5c00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:75 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/23 17:19:02.229 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[74]"]
   > [2024/07/23 17:19:02.230 +00:00] [WARN] [2pc.go:1808] ["schemaLeaseChecker is not set for this transaction"] [sessionID=2199023255969] [startTS=451347780004741120] [checkTS=451347780004741121]
   > [2024/07/23 17:19:03.253 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/23 17:19:03.267 +00:00] [INFO] [set.go:149] ["set global var"] [conn=2199023255971] [name=tx_isolation] [val=READ-COMMITTED]

### Scenario 1
 * Instruction #0:
     - Instruction:  update tbl_4 set tbl_4.col_17 = '11:16:44.00' ,tbl_4.col_17 = '03:51:50.00' ,tb...
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 1 / 0
 * Instruction #1:
     - Instruction:  select col_20 from tbl_4 order by col_20;
     - Transaction: conn_0
     - Output: [(-31298,), (-31136,), (-30900,), (-29720,), (-15820,), (-12681,), (-10830,), (15880,), (26689,), (30926,)]
     - Executed order: 1
     - Affected rows / Warnings: 10 / 0

 * Container logs:
   > [2024/07/23 17:19:05.478 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/23 17:19:05.480 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255975] [schemaVersion=69] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/23 17:19:05.482 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:100, Type:drop schema, State:queueing, SchemaState:public, SchemaID:95, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 17:19:05.481 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/23 17:19:05.482 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:100, Type:drop schema, State:queueing, SchemaState:public, SchemaID:95, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 17:19:05.481 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/23 17:19:05.487 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:100, Type:drop schema, State:queueing, SchemaState:public, SchemaID:95, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 17:19:05.481 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:19:05.489 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=69] [neededSchemaVersion=70] ["start time"=91.214µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 17:19:05.492 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=70] ["take time"=2.309325ms] [job="ID:100, Type:drop schema, State:running, SchemaState:write only, SchemaID:95, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 17:19:05.481 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:19:05.495 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:100, Type:drop schema, State:running, SchemaState:write only, SchemaID:95, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 17:19:05.481 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:19:05.496 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=70] [neededSchemaVersion=71] ["start time"=55.664µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 17:19:05.498 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=71] ["take time"=2.224048ms] [job="ID:100, Type:drop schema, State:running, SchemaState:delete only, SchemaID:95, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 17:19:05.481 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:19:05.501 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:100, Type:drop schema, State:running, SchemaState:delete only, SchemaID:95, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 17:19:05.481 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:19:05.502 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=71] [neededSchemaVersion=72] ["start time"=40.019µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 17:19:05.505 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=72] ["take time"=2.385731ms] [job="ID:100, Type:drop schema, State:done, SchemaState:none, SchemaID:95, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 17:19:05.481 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:19:05.508 +00:00] [INFO] [delete_range.go:109] ["[ddl] add job into delete-range table"] [jobID=100] [jobType="drop schema"]
   > [2024/07/23 17:19:05.508 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:100, Type:drop schema, State:synced, SchemaState:none, SchemaID:95, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 17:19:05.481 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:19:05.511 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=100]
   > [2024/07/23 17:19:05.511 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/23 17:19:05.512 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255975] [schemaVersion=72] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/23 17:19:05.515 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:102, Type:create schema, State:queueing, SchemaState:none, SchemaID:101, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 17:19:05.513 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/23 17:19:05.515 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:102, Type:create schema, State:queueing, SchemaState:none, SchemaID:101, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 17:19:05.513 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/23 17:19:05.522 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:102, Type:create schema, State:queueing, SchemaState:none, SchemaID:101, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 17:19:05.513 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:19:05.524 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=72] [neededSchemaVersion=73] ["start time"=141.5µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 17:19:05.526 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=73] ["take time"=2.216435ms] [job="ID:102, Type:create schema, State:done, SchemaState:public, SchemaID:101, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 17:19:05.513 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:19:05.530 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:102, Type:create schema, State:synced, SchemaState:public, SchemaID:101, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 17:19:05.513 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:19:05.532 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=102]
   > [2024/07/23 17:19:05.532 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/23 17:19:05.535 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255975] [schemaVersion=73] [cur_db=testdb] [sql="create table tbl_4 (\n    col_16 decimal ( 38 , 4 )   not null ,\n    col_17 time    default '23:52:24.00' ,\n    col_18 char ( 235 ) collate utf8_bin ,\n    col_19 tinyint  unsigned not null default 151 ,\n    col_20 smallint    default 9203 ,\n    primary key  ( col_20 ) /*T![clustered_index] nonclustered */ ,\n    key idx_8 ( col_18 ( 1 ) )\n) charset utf8mb4 collate utf8mb4_bin ;"] [user=root@%]
   > [2024/07/23 17:19:05.538 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:104, Type:create table, State:queueing, SchemaState:none, SchemaID:101, TableID:103, RowCount:0, ArgLen:1, start time: 2024-07-23 17:19:05.536 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/23 17:19:05.538 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:104, Type:create table, State:queueing, SchemaState:none, SchemaID:101, TableID:103, RowCount:0, ArgLen:1, start time: 2024-07-23 17:19:05.536 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table tbl_4 (\n    col_16 decimal ( 38 , 4 )   not null ,\n    col_17 time    default '23:52:24.00' ,\n    col_18 char ( 235 ) collate utf8_bin ,\n    col_19 tinyint  unsigned not null default 151 ,\n    col_20 smallint    default 9203 ,\n    primary key  ( col_20 ) /*T![clustered_index] nonclustered */ ,\n    key idx_8 ( col_18 ( 1 ) )\n) charset utf8mb4 collate utf8mb4_bin ;"]
   > [2024/07/23 17:19:05.543 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:104, Type:create table, State:queueing, SchemaState:none, SchemaID:101, TableID:103, RowCount:0, ArgLen:0, start time: 2024-07-23 17:19:05.536 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:19:05.547 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=73] [neededSchemaVersion=74] ["start time"=497.554µs] [phyTblIDs="[103]"] [actionTypes="[8]"]
   > [2024/07/23 17:19:05.548 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=74] ["take time"=2.095259ms] [job="ID:104, Type:create table, State:done, SchemaState:public, SchemaID:101, TableID:103, RowCount:0, ArgLen:1, start time: 2024-07-23 17:19:05.536 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:19:05.552 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:104, Type:create table, State:synced, SchemaState:public, SchemaID:101, TableID:103, RowCount:0, ArgLen:0, start time: 2024-07-23 17:19:05.536 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:19:05.554 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=104]
   > [2024/07/23 17:19:05.554 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/23 17:19:05.555 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=78] ["first split key"=748000000000000067]
   > [2024/07/23 17:19:05.555 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=78] ["first at"=748000000000000067] ["first new region left"="{Id:78 StartKey:7480000000000000ff6100000000000000f8 EndKey:7480000000000000ff6700000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:79 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/23 17:19:05.555 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[78]"]
   > [2024/07/23 17:19:05.556 +00:00] [WARN] [2pc.go:1808] ["schemaLeaseChecker is not set for this transaction"] [sessionID=2199023255975] [startTS=451347780876369922] [checkTS=451347780876632064]
   > [2024/07/23 17:19:06.576 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
