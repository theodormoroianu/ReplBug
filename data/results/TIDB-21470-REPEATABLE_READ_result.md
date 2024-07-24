# Bug ID TIDB-21470-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/21470
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              Amending transaction accepts DDLs that changes column types but gives wrong result


## Details
 * Database: tidb-c9288d24
 * Number of scenarios: 2
 * Initial setup script: No

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows: 0
 * Instruction #1:
     - Instruction:  set @@global.tidb_enable_change_column_type=true;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows: 0
 * Instruction #2:
     - Instruction:  create table t (id int primary key, v varchar(10));
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows: 0
 * Instruction #3:
     - Instruction:  begin pessimistic;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows: 0
 * Instruction #4:
     - Instruction:  insert into t values (1, "123456789");
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows: 1
 * Instruction #5:
     - Instruction:  alter table t modify column v varchar(5);
     - Transaction: conn_1
     - Output: None
     - Executed order: 5
     - Affected rows: 0
 * Instruction #6:
     - Instruction:  select sleep(5);
     - Transaction: conn_0
     - Output: [(0,)]
     - Executed order: 6
     - Affected rows: 1
 * Instruction #7:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: None
     - Executed order: 7
     - Affected rows: 0
 * Instruction #8:
     - Instruction:  select * from t;
     - Transaction: conn_0
     - Output: [(1, None)]
     - Executed order: 8
     - Affected rows: 1

 * Container logs:
   > [2024/07/24 11:52:22.118 +00:00] [INFO] [session.go:2455] ["CRUCIAL OPERATION"] [conn=2199023255557] [schemaVersion=24] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.74]
   > [2024/07/24 11:52:22.119 +00:00] [INFO] [session.go:2455] ["CRUCIAL OPERATION"] [conn=2199023255557] [schemaVersion=24] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.74]
   > [2024/07/24 11:52:22.120 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:50, Type:create schema, State:none, SchemaState:none, SchemaID:49, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 11:52:22.12 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 11:52:22.120 +00:00] [INFO] [ddl.go:491] ["[ddl] start DDL job"] [job="ID:50, Type:create schema, State:none, SchemaState:none, SchemaID:49, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 11:52:22.12 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/24 11:52:22.121 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:50, Type:create schema, State:none, SchemaState:none, SchemaID:49, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:22.12 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:22.122 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=24] [neededSchemaVersion=25] ["start time"=178.586µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 11:52:22.124 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=25] ["take time"=2.036526ms] [job="ID:50, Type:create schema, State:done, SchemaState:public, SchemaID:49, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 11:52:22.12 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:22.124 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:50, Type:create schema, State:synced, SchemaState:public, SchemaID:49, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:22.12 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:22.125 +00:00] [INFO] [ddl.go:543] ["[ddl] DDL job is finished"] [jobID=50]
   > [2024/07/24 11:52:22.125 +00:00] [INFO] [domain.go:659] ["performing DDL change, must reload"]
   > [2024/07/24 11:52:23.151 +00:00] [INFO] [set.go:217] ["set global var"] [conn=2199023255559] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/07/24 11:52:23.151 +00:00] [INFO] [set.go:217] ["set global var"] [conn=2199023255559] [name=transaction_isolation] [val=REPEATABLE-READ]
   > [2024/07/24 11:52:23.447 +00:00] [INFO] [set.go:217] ["set global var"] [conn=2199023255559] [name=tidb_enable_change_column_type] [val=1]
   > [2024/07/24 11:52:23.746 +00:00] [INFO] [session.go:2455] ["CRUCIAL OPERATION"] [conn=2199023255559] [schemaVersion=25] [cur_db=testdb] [sql=" create table t (id int primary key, v varchar(10));"] [user=root@10.88.0.74]
   > [2024/07/24 11:52:23.747 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:52, Type:create table, State:none, SchemaState:none, SchemaID:49, TableID:51, RowCount:0, ArgLen:1, start time: 2024-07-24 11:52:23.747 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 11:52:23.747 +00:00] [INFO] [ddl.go:491] ["[ddl] start DDL job"] [job="ID:52, Type:create table, State:none, SchemaState:none, SchemaID:49, TableID:51, RowCount:0, ArgLen:1, start time: 2024-07-24 11:52:23.747 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query=" create table t (id int primary key, v varchar(10));"]
   > [2024/07/24 11:52:23.748 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:52, Type:create table, State:none, SchemaState:none, SchemaID:49, TableID:51, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:23.747 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:23.749 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=25] [neededSchemaVersion=26] ["start time"=336.22µs] [phyTblIDs="[51]"] [actionTypes="[8]"]
   > [2024/07/24 11:52:23.751 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=26] ["take time"=2.088419ms] [job="ID:52, Type:create table, State:done, SchemaState:public, SchemaID:49, TableID:51, RowCount:0, ArgLen:1, start time: 2024-07-24 11:52:23.747 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:23.752 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:52, Type:create table, State:synced, SchemaState:public, SchemaID:49, TableID:51, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:23.747 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:23.753 +00:00] [INFO] [ddl.go:543] ["[ddl] DDL job is finished"] [jobID=52]
   > [2024/07/24 11:52:23.753 +00:00] [INFO] [domain.go:659] ["performing DDL change, must reload"]
   > [2024/07/24 11:52:23.754 +00:00] [INFO] [split_region.go:61] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=44] ["first split key"=748000000000000033]
   > [2024/07/24 11:52:23.757 +00:00] [INFO] [split_region.go:158] ["batch split regions complete"] ["batch region ID"=46] ["first at"=748000000000000033] ["first new region left"="{Id:46 StartKey:7480000000000000ff2f00000000000000f8 EndKey:7480000000000000ff3300000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:47 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/24 11:52:23.757 +00:00] [INFO] [split_region.go:207] ["split regions complete"] ["region count"=1] ["region IDs"="[46]"]
   > [2024/07/24 11:52:24.666 +00:00] [INFO] [session.go:2455] ["CRUCIAL OPERATION"] [conn=2199023255561] [schemaVersion=26] [cur_db=testdb] [sql=" alter table t modify column v varchar(5);"] [user=root@10.88.0.74]
   > [2024/07/24 11:52:24.667 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:53, Type:modify column, State:none, SchemaState:none, SchemaID:49, TableID:51, RowCount:0, ArgLen:5, start time: 2024-07-24 11:52:24.666 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 11:52:24.667 +00:00] [INFO] [ddl.go:491] ["[ddl] start DDL job"] [job="ID:53, Type:modify column, State:none, SchemaState:none, SchemaID:49, TableID:51, RowCount:0, ArgLen:5, start time: 2024-07-24 11:52:24.666 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query=" alter table t modify column v varchar(5);"]
   > [2024/07/24 11:52:24.667 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:53, Type:modify column, State:none, SchemaState:none, SchemaID:49, TableID:51, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:24.666 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:24.668 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=26] [neededSchemaVersion=27] ["start time"=222.238µs] [phyTblIDs="[51]"] [actionTypes="[4096]"]
   > [2024/07/24 11:52:24.670 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=27] ["take time"=2.30451ms] [job="ID:53, Type:modify column, State:running, SchemaState:delete only, SchemaID:49, TableID:51, RowCount:0, ArgLen:7, start time: 2024-07-24 11:52:24.666 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:24.671 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:53, Type:modify column, State:running, SchemaState:delete only, SchemaID:49, TableID:51, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:24.666 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:24.672 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=27] [neededSchemaVersion=28] ["start time"=336.219µs] [phyTblIDs="[51]"] [actionTypes="[4096]"]
   > [2024/07/24 11:52:24.675 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=28] ["take time"=2.62753ms] [job="ID:53, Type:modify column, State:running, SchemaState:write only, SchemaID:49, TableID:51, RowCount:0, ArgLen:7, start time: 2024-07-24 11:52:24.666 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:24.675 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:53, Type:modify column, State:running, SchemaState:write only, SchemaID:49, TableID:51, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:24.666 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:24.677 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=28] [neededSchemaVersion=29] ["start time"=332.938µs] [phyTblIDs="[51]"] [actionTypes="[4096]"]
   > [2024/07/24 11:52:24.679 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=29] ["take time"=2.685778ms] [job="ID:53, Type:modify column, State:running, SchemaState:write reorganization, SchemaID:49, TableID:51, RowCount:0, ArgLen:7, start time: 2024-07-24 11:52:24.666 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:24.680 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:53, Type:modify column, State:running, SchemaState:write reorganization, SchemaID:49, TableID:51, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:24.666 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:24.681 +00:00] [INFO] [reorg.go:524] ["[ddl] get table range, endHandle < startHandle"] [table="&{51 t utf8mb4 utf8mb4_bin [int(11) varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin varchar(5) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin] [] [] [] public true false  0 0 0 3 0 0 451365291864883200 0 0 0 0 0 <nil>  <nil> <nil> <nil> 3 <nil> false}"] ["table/partition ID"=51] [endHandle="key: "] [startHandle="key: "]
   > [2024/07/24 11:52:24.681 +00:00] [INFO] [reorg.go:584] ["[ddl] job get table range"] [jobID=53] [physicalTableID=51] [startHandle="key: "] [endHandle="key: "]
   > [2024/07/24 11:52:24.682 +00:00] [INFO] [ddl_worker.go:768] ["[ddl] schema version doesn't change"] [worker="worker 3, tp general"]
   > [2024/07/24 11:52:24.682 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:53, Type:modify column, State:running, SchemaState:write reorganization, SchemaID:49, TableID:51, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:24.666 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:451365291866193920"]
   > [2024/07/24 11:52:24.683 +00:00] [INFO] [reorg.go:165] ["sleep before reorganization to make async commit safe"] [duration=2.5s]
   > [2024/07/24 11:52:27.184 +00:00] [INFO] [column.go:1078] ["[ddl] start to update table row"] [job="ID:53, Type:modify column, State:running, SchemaState:write reorganization, SchemaID:49, TableID:51, RowCount:0, ArgLen:7, start time: 2024-07-24 11:52:24.666 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:451365291866193920"] [reorgInfo="CurrElementType:_col_,CurrElementID:3,StartHandle:key: ,EndHandle:key: ,First:false,PhysicalTableID:51"]
   > [2024/07/24 11:52:27.185 +00:00] [INFO] [reorg.go:524] ["[ddl] get table range, endHandle < startHandle"] [table="&{51 t utf8mb4 utf8mb4_bin [int(11) varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin varchar(5) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin] [] [] [] public true false  0 0 0 3 0 0 451365291864883200 0 0 0 0 0 <nil>  <nil> <nil> <nil> 3 <nil> false}"] ["table/partition ID"=51] [endHandle="key: "] [startHandle="key: "]
   > [2024/07/24 11:52:27.185 +00:00] [INFO] [reorg.go:209] ["[ddl] run reorg job done"] ["handled rows"=0]
   > [2024/07/24 11:52:27.187 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=29] [neededSchemaVersion=30] ["start time"=458.443µs] [phyTblIDs="[51]"] [actionTypes="[4096]"]
   > [2024/07/24 11:52:27.189 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=30] ["take time"=2.639123ms] [job="ID:53, Type:modify column, State:done, SchemaState:public, SchemaID:49, TableID:51, RowCount:0, ArgLen:2, start time: 2024-07-24 11:52:24.666 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:451365291866193920"]
   > [2024/07/24 11:52:27.190 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=53] [jobType="modify column"]
   > [2024/07/24 11:52:27.190 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:53, Type:modify column, State:synced, SchemaState:public, SchemaID:49, TableID:51, RowCount:0, ArgLen:2, start time: 2024-07-24 11:52:24.666 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:451365291866193920"]
   > [2024/07/24 11:52:27.192 +00:00] [INFO] [ddl.go:543] ["[ddl] DDL job is finished"] [jobID=53]
   > [2024/07/24 11:52:27.192 +00:00] [INFO] [domain.go:659] ["performing DDL change, must reload"]
   > [2024/07/24 11:52:29.962 +00:00] [INFO] [2pc.go:1353] ["amend txn successfully"] [conn=2199023255559] [connID=2199023255559] ["txn startTS"=451365291700256768] [memAmended=false] [checkTS=451365293250838528] [startInfoSchemaVer=26] ["table ids"="[51]"] ["action types"="[4096]"]

### Scenario 1
 * Instruction #0:
     - Instruction:  set @@global.tidb_enable_change_column_type=true;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows: 0
 * Instruction #1:
     - Instruction:  create table t (id int primary key, v varchar(10));
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows: 0
 * Instruction #2:
     - Instruction:  insert into t values (1, "123456789");
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows: 1
 * Instruction #3:
     - Instruction:  alter table t modify column v varchar(5);
     - Transaction: conn_1
     - Output: ERROR: 1406 (22001): Data Too Long, field len 5, data len 9
     - Executed order: Not executed
     - Affected rows: -1
 * Instruction #4:
     - Instruction:  select sleep(5);
     - Transaction: conn_0
     - Output: [(0,)]
     - Executed order: 3
     - Affected rows: 1
 * Instruction #5:
     - Instruction:  select * from t;
     - Transaction: conn_0
     - Output: [(1, '123456789')]
     - Executed order: 4
     - Affected rows: 1

 * Container logs:
   > [2024/07/24 11:52:31.459 +00:00] [INFO] [session.go:2455] ["CRUCIAL OPERATION"] [conn=2199023255565] [schemaVersion=38] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.74]
   > [2024/07/24 11:52:31.459 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:60, Type:drop schema, State:none, SchemaState:none, SchemaID:55, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:31.459 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 11:52:31.459 +00:00] [INFO] [ddl.go:491] ["[ddl] start DDL job"] [job="ID:60, Type:drop schema, State:none, SchemaState:none, SchemaID:55, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:31.459 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/24 11:52:31.460 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:60, Type:drop schema, State:none, SchemaState:none, SchemaID:55, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:31.459 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:31.460 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=38] [neededSchemaVersion=39] ["start time"=75.29µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 11:52:31.463 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=39] ["take time"=2.274129ms] [job="ID:60, Type:drop schema, State:running, SchemaState:write only, SchemaID:55, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:31.459 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:31.463 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:60, Type:drop schema, State:running, SchemaState:write only, SchemaID:55, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:31.459 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:31.464 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=39] [neededSchemaVersion=40] ["start time"=94.846µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 11:52:31.466 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=40] ["take time"=2.256458ms] [job="ID:60, Type:drop schema, State:running, SchemaState:delete only, SchemaID:55, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:31.459 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:31.467 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:60, Type:drop schema, State:running, SchemaState:delete only, SchemaID:55, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:31.459 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:31.468 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=40] [neededSchemaVersion=41] ["start time"=150.789µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 11:52:31.471 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=41] ["take time"=2.674813ms] [job="ID:60, Type:drop schema, State:done, SchemaState:none, SchemaID:55, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:31.459 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:31.471 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=60] [jobType="drop schema"]
   > [2024/07/24 11:52:31.471 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:60, Type:drop schema, State:synced, SchemaState:none, SchemaID:55, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:31.459 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:31.472 +00:00] [INFO] [ddl.go:543] ["[ddl] DDL job is finished"] [jobID=60]
   > [2024/07/24 11:52:31.472 +00:00] [INFO] [domain.go:659] ["performing DDL change, must reload"]
   > [2024/07/24 11:52:31.474 +00:00] [INFO] [session.go:2455] ["CRUCIAL OPERATION"] [conn=2199023255565] [schemaVersion=41] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.74]
   > [2024/07/24 11:52:31.475 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:62, Type:create schema, State:none, SchemaState:none, SchemaID:61, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 11:52:31.474 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 11:52:31.475 +00:00] [INFO] [ddl.go:491] ["[ddl] start DDL job"] [job="ID:62, Type:create schema, State:none, SchemaState:none, SchemaID:61, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 11:52:31.474 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/24 11:52:31.475 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:62, Type:create schema, State:none, SchemaState:none, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:31.474 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:31.476 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=41] [neededSchemaVersion=42] ["start time"=102.808µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 11:52:31.478 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=42] ["take time"=2.264141ms] [job="ID:62, Type:create schema, State:done, SchemaState:public, SchemaID:61, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 11:52:31.474 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:31.478 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:62, Type:create schema, State:synced, SchemaState:public, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:31.474 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:31.479 +00:00] [INFO] [ddl.go:543] ["[ddl] DDL job is finished"] [jobID=62]
   > [2024/07/24 11:52:31.479 +00:00] [INFO] [domain.go:659] ["performing DDL change, must reload"]
   > [2024/07/24 11:52:32.500 +00:00] [INFO] [set.go:217] ["set global var"] [conn=2199023255567] [name=tidb_enable_change_column_type] [val=1]
   > [2024/07/24 11:52:32.794 +00:00] [INFO] [session.go:2455] ["CRUCIAL OPERATION"] [conn=2199023255567] [schemaVersion=42] [cur_db=testdb] [sql=" create table t (id int primary key, v varchar(10));"] [user=root@10.88.0.74]
   > [2024/07/24 11:52:32.795 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:64, Type:create table, State:none, SchemaState:none, SchemaID:61, TableID:63, RowCount:0, ArgLen:1, start time: 2024-07-24 11:52:32.794 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 11:52:32.795 +00:00] [INFO] [ddl.go:491] ["[ddl] start DDL job"] [job="ID:64, Type:create table, State:none, SchemaState:none, SchemaID:61, TableID:63, RowCount:0, ArgLen:1, start time: 2024-07-24 11:52:32.794 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query=" create table t (id int primary key, v varchar(10));"]
   > [2024/07/24 11:52:32.796 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:64, Type:create table, State:none, SchemaState:none, SchemaID:61, TableID:63, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:32.794 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:32.797 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=42] [neededSchemaVersion=43] ["start time"=294.663µs] [phyTblIDs="[63]"] [actionTypes="[8]"]
   > [2024/07/24 11:52:32.799 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=43] ["take time"=2.30472ms] [job="ID:64, Type:create table, State:done, SchemaState:public, SchemaID:61, TableID:63, RowCount:0, ArgLen:1, start time: 2024-07-24 11:52:32.794 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:32.800 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:64, Type:create table, State:synced, SchemaState:public, SchemaID:61, TableID:63, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:32.794 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:32.801 +00:00] [INFO] [ddl.go:543] ["[ddl] DDL job is finished"] [jobID=64]
   > [2024/07/24 11:52:32.802 +00:00] [INFO] [domain.go:659] ["performing DDL change, must reload"]
   > [2024/07/24 11:52:32.802 +00:00] [INFO] [split_region.go:61] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=50] ["first split key"=74800000000000003f]
   > [2024/07/24 11:52:32.802 +00:00] [INFO] [split_region.go:158] ["batch split regions complete"] ["batch region ID"=50] ["first at"=74800000000000003f] ["first new region left"="{Id:50 StartKey:7480000000000000ff3900000000000000f8 EndKey:7480000000000000ff3f00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:51 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/24 11:52:32.802 +00:00] [INFO] [split_region.go:207] ["split regions complete"] ["region count"=1] ["region IDs"="[50]"]
   > [2024/07/24 11:52:33.412 +00:00] [INFO] [session.go:2455] ["CRUCIAL OPERATION"] [conn=2199023255569] [schemaVersion=43] [cur_db=testdb] [sql=" alter table t modify column v varchar(5);"] [user=root@10.88.0.74]
   > [2024/07/24 11:52:33.414 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:65, Type:modify column, State:none, SchemaState:none, SchemaID:61, TableID:63, RowCount:0, ArgLen:5, start time: 2024-07-24 11:52:33.413 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 11:52:33.414 +00:00] [INFO] [ddl.go:491] ["[ddl] start DDL job"] [job="ID:65, Type:modify column, State:none, SchemaState:none, SchemaID:61, TableID:63, RowCount:0, ArgLen:5, start time: 2024-07-24 11:52:33.413 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query=" alter table t modify column v varchar(5);"]
   > [2024/07/24 11:52:33.414 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:modify column, State:none, SchemaState:none, SchemaID:61, TableID:63, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:33.413 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:33.416 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=43] [neededSchemaVersion=44] ["start time"=283.838µs] [phyTblIDs="[63]"] [actionTypes="[4096]"]
   > [2024/07/24 11:52:33.418 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=44] ["take time"=2.244027ms] [job="ID:65, Type:modify column, State:running, SchemaState:delete only, SchemaID:61, TableID:63, RowCount:0, ArgLen:7, start time: 2024-07-24 11:52:33.413 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:33.418 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:modify column, State:running, SchemaState:delete only, SchemaID:61, TableID:63, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:33.413 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:33.420 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=44] [neededSchemaVersion=45] ["start time"=264.282µs] [phyTblIDs="[63]"] [actionTypes="[4096]"]
   > [2024/07/24 11:52:33.422 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=45] ["take time"=2.873793ms] [job="ID:65, Type:modify column, State:running, SchemaState:write only, SchemaID:61, TableID:63, RowCount:0, ArgLen:7, start time: 2024-07-24 11:52:33.413 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:33.422 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:modify column, State:running, SchemaState:write only, SchemaID:61, TableID:63, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:33.413 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:33.424 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=45] [neededSchemaVersion=46] ["start time"=255.692µs] [phyTblIDs="[63]"] [actionTypes="[4096]"]
   > [2024/07/24 11:52:33.426 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=46] ["take time"=2.283278ms] [job="ID:65, Type:modify column, State:running, SchemaState:write reorganization, SchemaID:61, TableID:63, RowCount:0, ArgLen:7, start time: 2024-07-24 11:52:33.413 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:33.426 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:modify column, State:running, SchemaState:write reorganization, SchemaID:61, TableID:63, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:33.413 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:33.427 +00:00] [INFO] [reorg.go:584] ["[ddl] job get table range"] [jobID=65] [physicalTableID=63] [startHandle=1] [endHandle=1]
   > [2024/07/24 11:52:33.428 +00:00] [INFO] [ddl_worker.go:768] ["[ddl] schema version doesn't change"] [worker="worker 3, tp general"]
   > [2024/07/24 11:52:33.429 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:modify column, State:running, SchemaState:write reorganization, SchemaID:61, TableID:63, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:33.413 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:451365294159167488"]
   > [2024/07/24 11:52:33.429 +00:00] [INFO] [reorg.go:165] ["sleep before reorganization to make async commit safe"] [duration=2.5s]
   > [2024/07/24 11:52:35.930 +00:00] [INFO] [column.go:1078] ["[ddl] start to update table row"] [job="ID:65, Type:modify column, State:running, SchemaState:write reorganization, SchemaID:61, TableID:63, RowCount:0, ArgLen:7, start time: 2024-07-24 11:52:33.413 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:451365294159167488"] [reorgInfo=CurrElementType:_col_,CurrElementID:3,StartHandle:1,EndHandle:1,First:false,PhysicalTableID:63]
   > [2024/07/24 11:52:35.930 +00:00] [INFO] [backfilling.go:320] ["[ddl] split table range from PD"] [physicalTableID=63] [startHandle=1] [endHandle=1]
   > [2024/07/24 11:52:35.931 +00:00] [INFO] [backfilling.go:633] ["[ddl] start backfill workers to reorg record"] [workerCnt=1] [regionCnt=1] [startHandle=1] [endHandle=1]
   > [2024/07/24 11:52:35.931 +00:00] [INFO] [backfilling.go:288] ["[ddl] backfill worker start"] [workerID=0]
   > [2024/07/24 11:52:35.932 +00:00] [WARN] [backfilling.go:394] ["[ddl] backfill worker handle batch tasks failed"] [elementType=_col_] [elementID=3] [totalAddedCount=0] [startHandle=1] [nextHandle=1] [batchAddedCount=0] [taskFailedError="[types:1406]Data Too Long, field len 5, data len 9"] [takeTime=308.074µs] []
   > [2024/07/24 11:52:35.932 +00:00] [INFO] [reorg.go:209] ["[ddl] run reorg job done"] ["handled rows"=0]
   > [2024/07/24 11:52:35.932 +00:00] [INFO] [backfilling.go:313] ["[ddl] backfill worker exit"] [workerID=0]
   > [2024/07/24 11:52:35.932 +00:00] [WARN] [column.go:1006] ["[ddl] run modify column job failed, convert job to rollback"] [job="ID:65, Type:modify column, State:running, SchemaState:write reorganization, SchemaID:61, TableID:63, RowCount:0, ArgLen:7, start time: 2024-07-24 11:52:33.413 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:451365294159167488"] [error="[types:1406]Data Too Long, field len 5, data len 9"]
   > [2024/07/24 11:52:35.932 +00:00] [ERROR] [ddl_worker.go:714] ["[ddl] run DDL job error"] [worker="worker 3, tp general"] [error="[types:1406]Data Too Long, field len 5, data len 9"]
   > [2024/07/24 11:52:35.933 +00:00] [INFO] [ddl_worker.go:500] ["[ddl] run DDL job failed, sleeps a while then retries it."] [worker="worker 3, tp general"] [waitTime=1s] [error="[types:1406]Data Too Long, field len 5, data len 9"]
   > [2024/07/24 11:52:36.934 +00:00] [INFO] [ddl_worker.go:768] ["[ddl] schema version doesn't change"] [worker="worker 3, tp general"]
   > [2024/07/24 11:52:36.934 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:modify column, State:rollingback, SchemaState:write reorganization, SchemaID:61, TableID:63, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:33.413 +0000 UTC, Err:[types:1406]Data Too Long, field len 5, data len 9, ErrCount:1, SnapshotVersion:451365294159167488"]
   > [2024/07/24 11:52:36.936 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=46] [neededSchemaVersion=47] ["start time"=275.318µs] [phyTblIDs="[63]"] [actionTypes="[4096]"]
   > [2024/07/24 11:52:36.938 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=47] ["take time"=2.272173ms] [job="ID:65, Type:modify column, State:rollback done, SchemaState:none, SchemaID:61, TableID:63, RowCount:0, ArgLen:2, start time: 2024-07-24 11:52:33.413 +0000 UTC, Err:[types:1406]Data Too Long, field len 5, data len 9, ErrCount:1, SnapshotVersion:451365294159167488"]
   > [2024/07/24 11:52:36.938 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=65] [jobType="modify column"]
   > [2024/07/24 11:52:36.939 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:modify column, State:rollback done, SchemaState:none, SchemaID:61, TableID:63, RowCount:0, ArgLen:2, start time: 2024-07-24 11:52:33.413 +0000 UTC, Err:[types:1406]Data Too Long, field len 5, data len 9, ErrCount:1, SnapshotVersion:451365294159167488"]
   > [2024/07/24 11:52:36.939 +00:00] [INFO] [ddl_worker.go:768] ["[ddl] schema version doesn't change"] [worker="worker 3, tp general"]
   > [2024/07/24 11:52:37.414 +00:00] [INFO] [tidb.go:222] ["rollbackTxn for ddl/autocommit failed"]
   > [2024/07/24 11:52:37.415 +00:00] [WARN] [session.go:1261] ["run statement failed"] [conn=2199023255569] [schemaVersion=43] [error="[types:1406]Data Too Long, field len 5, data len 9"] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 2199023255569,\n  \"status\": 2,\n  \"strictMode\": true,\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"10.88.0.74\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/07/24 11:52:37.415 +00:00] [INFO] [conn.go:806] ["command dispatched failed"] [conn=2199023255569] [connInfo="id:2199023255569, addr:10.88.0.74:39074 status:10, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:0, autocommit:1"] [sql=" alter table t modify column v varchar(5);"] [txn_mode=OPTIMISTIC] [err="[types:1406]Data Too Long, field len 5, data len 9\ngithub.com/pingcap/errors.AddStack\n\t/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.20201029093017-5a7df2af2ac7/errors.go:174\ngithub.com/pingcap/errors.Trace\n\t/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.20201029093017-5a7df2af2ac7/juju_adaptor.go:15\ngithub.com/pingcap/tidb/ddl.(*ddl).doDDLJob\n\t/go/src/github.com/pingcap/tidb/ddl/ddl.go:548\ngithub.com/pingcap/tidb/ddl.(*ddl).ModifyColumn\n\t/go/src/github.com/pingcap/tidb/ddl/ddl_api.go:4039\ngithub.com/pingcap/tidb/ddl.(*ddl).AlterTable\n\t/go/src/github.com/pingcap/tidb/ddl/ddl_api.go:2431\ngithub.com/pingcap/tidb/executor.(*DDLExec).executeAlterTable\n\t/go/src/github.com/pingcap/tidb/executor/ddl.go:372\ngithub.com/pingcap/tidb/executor.(*DDLExec).Next\n\t/go/src/github.com/pingcap/tidb/executor/ddl.go:86\ngithub.com/pingcap/tidb/executor.Next\n\t/go/src/github.com/pingcap/tidb/executor/executor.go:277\ngithub.com/pingcap/tidb/executor.(*ExecStmt).handleNoDelayExecutor\n\t/go/src/github.com/pingcap/tidb/executor/adapter.go:524\ngithub.com/pingcap/tidb/executor.(*ExecStmt).handleNoDelay\n\t/go/src/github.com/pingcap/tidb/executor/adapter.go:405\ngithub.com/pingcap/tidb/executor.(*ExecStmt).Exec\n\t/go/src/github.com/pingcap/tidb/executor/adapter.go:355\ngithub.com/pingcap/tidb/session.runStmt\n\t/go/src/github.com/pingcap/tidb/session/session.go:1314\ngithub.com/pingcap/tidb/session.(*session).ExecuteStmt\n\t/go/src/github.com/pingcap/tidb/session/session.go:1258\ngithub.com/pingcap/tidb/server.(*TiDBContext).ExecuteStmt\n\t/go/src/github.com/pingcap/tidb/server/driver_tidb.go:212\ngithub.com/pingcap/tidb/server.(*clientConn).handleStmt\n\t/go/src/github.com/pingcap/tidb/server/conn.go:1556\ngithub.com/pingcap/tidb/server.(*clientConn).handleQuery\n\t/go/src/github.com/pingcap/tidb/server/conn.go:1448\ngithub.com/pingcap/tidb/server.(*clientConn).dispatch\n\t/go/src/github.com/pingcap/tidb/server/conn.go:1024\ngithub.com/pingcap/tidb/server.(*clientConn).Run\n\t/go/src/github.com/pingcap/tidb/server/conn.go:789\ngithub.com/pingcap/tidb/server.(*Server).onConn\n\t/go/src/github.com/pingcap/tidb/server/server.go:459\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1594"]
