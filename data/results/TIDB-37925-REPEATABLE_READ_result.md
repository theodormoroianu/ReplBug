# Bug ID TIDB-37925-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/37925
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              Duplicates in primary key do not throw an error


## Details
 * Database: tidb-v6.3.0
 * Number of scenarios: 2
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
   > [2024/07/23 17:18:55.671 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/23 17:18:55.674 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255957] [schemaVersion=33] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/23 17:18:55.674 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255957] [schemaVersion=33] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/23 17:18:55.677 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:69, Type:create schema, State:queueing, SchemaState:none, SchemaID:68, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 17:18:55.675 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/23 17:18:55.677 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:69, Type:create schema, State:queueing, SchemaState:none, SchemaID:68, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 17:18:55.675 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/23 17:18:56.477 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:69, Type:create schema, State:queueing, SchemaState:none, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 17:18:55.675 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:18:56.480 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=33] [neededSchemaVersion=34] ["start time"=166.643µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 17:18:56.482 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=34] ["take time"=2.651061ms] [job="ID:69, Type:create schema, State:done, SchemaState:public, SchemaID:68, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 17:18:55.675 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:18:56.489 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:69, Type:create schema, State:synced, SchemaState:public, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 17:18:55.675 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:18:56.491 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=69]
   > [2024/07/23 17:18:56.491 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/23 17:18:56.495 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255957] [schemaVersion=34] [cur_db=testdb] [sql="create table tbl_4 (\n    col_16 decimal ( 38 , 4 )   not null ,\n    col_17 time    default '23:52:24.00' ,\n    col_18 char ( 235 ) collate utf8_bin ,\n    col_19 tinyint  unsigned not null default 151 ,\n    col_20 smallint    default 9203 ,\n    primary key  ( col_20 ) /*T![clustered_index] nonclustered */ ,\n    key idx_8 ( col_18 ( 1 ) )\n) charset utf8mb4 collate utf8mb4_bin ;"] [user=root@%]
   > [2024/07/23 17:18:56.498 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:71, Type:create table, State:queueing, SchemaState:none, SchemaID:68, TableID:70, RowCount:0, ArgLen:1, start time: 2024-07-23 17:18:56.496 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/23 17:18:56.499 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:71, Type:create table, State:queueing, SchemaState:none, SchemaID:68, TableID:70, RowCount:0, ArgLen:1, start time: 2024-07-23 17:18:56.496 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table tbl_4 (\n    col_16 decimal ( 38 , 4 )   not null ,\n    col_17 time    default '23:52:24.00' ,\n    col_18 char ( 235 ) collate utf8_bin ,\n    col_19 tinyint  unsigned not null default 151 ,\n    col_20 smallint    default 9203 ,\n    primary key  ( col_20 ) /*T![clustered_index] nonclustered */ ,\n    key idx_8 ( col_18 ( 1 ) )\n) charset utf8mb4 collate utf8mb4_bin ;"]
   > [2024/07/23 17:18:56.506 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:71, Type:create table, State:queueing, SchemaState:none, SchemaID:68, TableID:70, RowCount:0, ArgLen:0, start time: 2024-07-23 17:18:56.496 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:18:56.511 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=34] [neededSchemaVersion=35] ["start time"=614.26µs] [phyTblIDs="[70]"] [actionTypes="[8]"]
   > [2024/07/23 17:18:56.513 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=35] ["take time"=2.128714ms] [job="ID:71, Type:create table, State:done, SchemaState:public, SchemaID:68, TableID:70, RowCount:0, ArgLen:1, start time: 2024-07-23 17:18:56.496 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:18:56.518 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:71, Type:create table, State:synced, SchemaState:public, SchemaID:68, TableID:70, RowCount:0, ArgLen:0, start time: 2024-07-23 17:18:56.496 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:18:56.522 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=71]
   > [2024/07/23 17:18:56.522 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/23 17:18:56.522 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=66] ["first split key"=748000000000000046]
   > [2024/07/23 17:18:56.522 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=66] ["first at"=748000000000000046] ["first new region left"="{Id:66 StartKey:7480000000000000ff4200000000000000f8 EndKey:7480000000000000ff4600000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:67 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/23 17:18:56.522 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[66]"]
   > [2024/07/23 17:18:56.523 +00:00] [WARN] [2pc.go:1808] ["schemaLeaseChecker is not set for this transaction"] [sessionID=2199023255957] [startTS=451347778508423171] [checkTS=451347778508685312]
   > [2024/07/23 17:18:57.553 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/23 17:18:57.565 +00:00] [INFO] [set.go:149] ["set global var"] [conn=2199023255959] [name=tx_isolation] [val=REPEATABLE-READ]

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
   > [2024/07/23 17:18:59.729 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/23 17:18:59.732 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255963] [schemaVersion=43] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/23 17:18:59.734 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:78, Type:drop schema, State:queueing, SchemaState:public, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 17:18:59.732 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/23 17:18:59.734 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:78, Type:drop schema, State:queueing, SchemaState:public, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 17:18:59.732 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/23 17:18:59.740 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:78, Type:drop schema, State:queueing, SchemaState:public, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 17:18:59.732 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:18:59.743 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=43] [neededSchemaVersion=44] ["start time"=105.531µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 17:18:59.745 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=44] ["take time"=2.353814ms] [job="ID:78, Type:drop schema, State:running, SchemaState:write only, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 17:18:59.732 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:18:59.749 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:78, Type:drop schema, State:running, SchemaState:write only, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 17:18:59.732 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:18:59.752 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=44] [neededSchemaVersion=45] ["start time"=105.461µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 17:18:59.754 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=45] ["take time"=2.251914ms] [job="ID:78, Type:drop schema, State:running, SchemaState:delete only, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 17:18:59.732 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:18:59.757 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:78, Type:drop schema, State:running, SchemaState:delete only, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 17:18:59.732 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:18:59.762 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=45] [neededSchemaVersion=46] ["start time"=173.837µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 17:18:59.764 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=46] ["take time"=2.036521ms] [job="ID:78, Type:drop schema, State:done, SchemaState:none, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 17:18:59.732 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:18:59.768 +00:00] [INFO] [delete_range.go:109] ["[ddl] add job into delete-range table"] [jobID=78] [jobType="drop schema"]
   > [2024/07/23 17:18:59.768 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:78, Type:drop schema, State:synced, SchemaState:none, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 17:18:59.732 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:18:59.770 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=78]
   > [2024/07/23 17:18:59.770 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/23 17:18:59.771 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255963] [schemaVersion=46] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/23 17:18:59.772 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:80, Type:create schema, State:queueing, SchemaState:none, SchemaID:79, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 17:18:59.771 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/23 17:18:59.772 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:80, Type:create schema, State:queueing, SchemaState:none, SchemaID:79, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 17:18:59.771 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/23 17:18:59.778 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:80, Type:create schema, State:queueing, SchemaState:none, SchemaID:79, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 17:18:59.771 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:18:59.780 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=46] [neededSchemaVersion=47] ["start time"=90.446µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 17:18:59.782 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=47] ["take time"=2.190313ms] [job="ID:80, Type:create schema, State:done, SchemaState:public, SchemaID:79, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 17:18:59.771 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:18:59.785 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:80, Type:create schema, State:synced, SchemaState:public, SchemaID:79, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 17:18:59.771 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:18:59.786 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=80]
   > [2024/07/23 17:18:59.786 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/23 17:18:59.788 +00:00] [INFO] [session.go:3149] ["CRUCIAL OPERATION"] [conn=2199023255963] [schemaVersion=47] [cur_db=testdb] [sql="create table tbl_4 (\n    col_16 decimal ( 38 , 4 )   not null ,\n    col_17 time    default '23:52:24.00' ,\n    col_18 char ( 235 ) collate utf8_bin ,\n    col_19 tinyint  unsigned not null default 151 ,\n    col_20 smallint    default 9203 ,\n    primary key  ( col_20 ) /*T![clustered_index] nonclustered */ ,\n    key idx_8 ( col_18 ( 1 ) )\n) charset utf8mb4 collate utf8mb4_bin ;"] [user=root@%]
   > [2024/07/23 17:18:59.791 +00:00] [INFO] [ddl_worker.go:312] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:82, Type:create table, State:queueing, SchemaState:none, SchemaID:79, TableID:81, RowCount:0, ArgLen:1, start time: 2024-07-23 17:18:59.789 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/23 17:18:59.791 +00:00] [INFO] [ddl.go:955] ["[ddl] start DDL job"] [job="ID:82, Type:create table, State:queueing, SchemaState:none, SchemaID:79, TableID:81, RowCount:0, ArgLen:1, start time: 2024-07-23 17:18:59.789 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table tbl_4 (\n    col_16 decimal ( 38 , 4 )   not null ,\n    col_17 time    default '23:52:24.00' ,\n    col_18 char ( 235 ) collate utf8_bin ,\n    col_19 tinyint  unsigned not null default 151 ,\n    col_20 smallint    default 9203 ,\n    primary key  ( col_20 ) /*T![clustered_index] nonclustered */ ,\n    key idx_8 ( col_18 ( 1 ) )\n) charset utf8mb4 collate utf8mb4_bin ;"]
   > [2024/07/23 17:18:59.796 +00:00] [INFO] [ddl_worker.go:1082] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:82, Type:create table, State:queueing, SchemaState:none, SchemaID:79, TableID:81, RowCount:0, ArgLen:0, start time: 2024-07-23 17:18:59.789 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:18:59.800 +00:00] [INFO] [domain.go:155] ["diff load InfoSchema success"] [currentSchemaVersion=47] [neededSchemaVersion=48] ["start time"=371.28µs] [phyTblIDs="[81]"] [actionTypes="[8]"]
   > [2024/07/23 17:18:59.801 +00:00] [INFO] [ddl_worker.go:1290] ["[ddl] wait latest schema version changed"] [worker="worker 10, tp general"] [ver=48] ["take time"=2.181584ms] [job="ID:82, Type:create table, State:done, SchemaState:public, SchemaID:79, TableID:81, RowCount:0, ArgLen:1, start time: 2024-07-23 17:18:59.789 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:18:59.806 +00:00] [INFO] [ddl_worker.go:562] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:82, Type:create table, State:synced, SchemaState:public, SchemaID:79, TableID:81, RowCount:0, ArgLen:0, start time: 2024-07-23 17:18:59.789 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 17:18:59.808 +00:00] [INFO] [ddl.go:1048] ["[ddl] DDL job is finished"] [jobID=82]
   > [2024/07/23 17:18:59.808 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/23 17:18:59.809 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=70] ["first split key"=748000000000000051]
   > [2024/07/23 17:18:59.809 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=70] ["first at"=748000000000000051] ["first new region left"="{Id:70 StartKey:7480000000000000ff4b00000000000000f8 EndKey:7480000000000000ff5100000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:71 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/23 17:18:59.809 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[70]"]
   > [2024/07/23 17:18:59.810 +00:00] [WARN] [2pc.go:1808] ["schemaLeaseChecker is not set for this transaction"] [sessionID=2199023255963] [startTS=451347779370090498] [checkTS=451347779370352640]
   > [2024/07/23 17:19:00.833 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
