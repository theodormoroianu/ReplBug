# Bug ID TIDB-21470-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/21470
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              Amending transaction accepts DDLs that changes column types but gives wrong result


## Details
 * Database: tidb-c9288d24
 * Number of scenarios: 2
 * Initial setup script: No

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
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
   > [2024/07/24 11:52:39.973 +00:00] [INFO] [session.go:2455] ["CRUCIAL OPERATION"] [conn=2199023255573] [schemaVersion=55] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.74]
   > [2024/07/24 11:52:39.974 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:72, Type:drop schema, State:none, SchemaState:none, SchemaID:67, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:39.973 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 11:52:39.974 +00:00] [INFO] [ddl.go:491] ["[ddl] start DDL job"] [job="ID:72, Type:drop schema, State:none, SchemaState:none, SchemaID:67, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:39.973 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/24 11:52:39.975 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:72, Type:drop schema, State:none, SchemaState:none, SchemaID:67, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:39.973 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:39.975 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=55] [neededSchemaVersion=56] ["start time"=81.017µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 11:52:39.977 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=56] ["take time"=2.302904ms] [job="ID:72, Type:drop schema, State:running, SchemaState:write only, SchemaID:67, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:39.973 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:39.978 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:72, Type:drop schema, State:running, SchemaState:write only, SchemaID:67, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:39.973 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:39.979 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=56] [neededSchemaVersion=57] ["start time"=113.144µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 11:52:39.981 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=57] ["take time"=2.236903ms] [job="ID:72, Type:drop schema, State:running, SchemaState:delete only, SchemaID:67, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:39.973 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:39.981 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:72, Type:drop schema, State:running, SchemaState:delete only, SchemaID:67, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:39.973 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:39.982 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=57] [neededSchemaVersion=58] ["start time"=86.465µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 11:52:39.984 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=58] ["take time"=2.106368ms] [job="ID:72, Type:drop schema, State:done, SchemaState:none, SchemaID:67, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:39.973 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:39.985 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=72] [jobType="drop schema"]
   > [2024/07/24 11:52:39.985 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:72, Type:drop schema, State:synced, SchemaState:none, SchemaID:67, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:39.973 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:39.985 +00:00] [INFO] [ddl.go:543] ["[ddl] DDL job is finished"] [jobID=72]
   > [2024/07/24 11:52:39.986 +00:00] [INFO] [domain.go:659] ["performing DDL change, must reload"]
   > [2024/07/24 11:52:39.987 +00:00] [INFO] [session.go:2455] ["CRUCIAL OPERATION"] [conn=2199023255573] [schemaVersion=58] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.74]
   > [2024/07/24 11:52:39.988 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:74, Type:create schema, State:none, SchemaState:none, SchemaID:73, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 11:52:39.988 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 11:52:39.988 +00:00] [INFO] [ddl.go:491] ["[ddl] start DDL job"] [job="ID:74, Type:create schema, State:none, SchemaState:none, SchemaID:73, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 11:52:39.988 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/24 11:52:39.989 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:74, Type:create schema, State:none, SchemaState:none, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:39.988 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:39.990 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=58] [neededSchemaVersion=59] ["start time"=150.231µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 11:52:39.992 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=59] ["take time"=2.266796ms] [job="ID:74, Type:create schema, State:done, SchemaState:public, SchemaID:73, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 11:52:39.988 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:39.992 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:74, Type:create schema, State:synced, SchemaState:public, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:39.988 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:39.993 +00:00] [INFO] [ddl.go:543] ["[ddl] DDL job is finished"] [jobID=74]
   > [2024/07/24 11:52:39.993 +00:00] [INFO] [domain.go:659] ["performing DDL change, must reload"]
   > [2024/07/24 11:52:41.014 +00:00] [INFO] [set.go:217] ["set global var"] [conn=2199023255575] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/07/24 11:52:41.015 +00:00] [INFO] [set.go:217] ["set global var"] [conn=2199023255575] [name=transaction_isolation] [val=READ-COMMITTED]
   > [2024/07/24 11:52:41.309 +00:00] [INFO] [set.go:217] ["set global var"] [conn=2199023255575] [name=tidb_enable_change_column_type] [val=1]
   > [2024/07/24 11:52:41.609 +00:00] [INFO] [session.go:2455] ["CRUCIAL OPERATION"] [conn=2199023255575] [schemaVersion=59] [cur_db=testdb] [sql=" create table t (id int primary key, v varchar(10));"] [user=root@10.88.0.74]
   > [2024/07/24 11:52:41.611 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:76, Type:create table, State:none, SchemaState:none, SchemaID:73, TableID:75, RowCount:0, ArgLen:1, start time: 2024-07-24 11:52:41.61 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 11:52:41.611 +00:00] [INFO] [ddl.go:491] ["[ddl] start DDL job"] [job="ID:76, Type:create table, State:none, SchemaState:none, SchemaID:73, TableID:75, RowCount:0, ArgLen:1, start time: 2024-07-24 11:52:41.61 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query=" create table t (id int primary key, v varchar(10));"]
   > [2024/07/24 11:52:41.612 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:76, Type:create table, State:none, SchemaState:none, SchemaID:73, TableID:75, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:41.61 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:41.614 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=59] [neededSchemaVersion=60] ["start time"=307.515µs] [phyTblIDs="[75]"] [actionTypes="[8]"]
   > [2024/07/24 11:52:41.616 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=60] ["take time"=2.262186ms] [job="ID:76, Type:create table, State:done, SchemaState:public, SchemaID:73, TableID:75, RowCount:0, ArgLen:1, start time: 2024-07-24 11:52:41.61 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:41.617 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:76, Type:create table, State:synced, SchemaState:public, SchemaID:73, TableID:75, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:41.61 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:41.618 +00:00] [INFO] [ddl.go:543] ["[ddl] DDL job is finished"] [jobID=76]
   > [2024/07/24 11:52:41.618 +00:00] [INFO] [domain.go:659] ["performing DDL change, must reload"]
   > [2024/07/24 11:52:41.619 +00:00] [INFO] [split_region.go:61] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=54] ["first split key"=74800000000000004b]
   > [2024/07/24 11:52:41.619 +00:00] [INFO] [split_region.go:158] ["batch split regions complete"] ["batch region ID"=54] ["first at"=74800000000000004b] ["first new region left"="{Id:54 StartKey:7480000000000000ff4500000000000000f8 EndKey:7480000000000000ff4b00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:55 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/24 11:52:41.619 +00:00] [INFO] [split_region.go:207] ["split regions complete"] ["region count"=1] ["region IDs"="[54]"]
   > [2024/07/24 11:52:42.528 +00:00] [INFO] [session.go:2455] ["CRUCIAL OPERATION"] [conn=2199023255577] [schemaVersion=60] [cur_db=testdb] [sql=" alter table t modify column v varchar(5);"] [user=root@10.88.0.74]
   > [2024/07/24 11:52:42.529 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:77, Type:modify column, State:none, SchemaState:none, SchemaID:73, TableID:75, RowCount:0, ArgLen:5, start time: 2024-07-24 11:52:42.529 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 11:52:42.529 +00:00] [INFO] [ddl.go:491] ["[ddl] start DDL job"] [job="ID:77, Type:modify column, State:none, SchemaState:none, SchemaID:73, TableID:75, RowCount:0, ArgLen:5, start time: 2024-07-24 11:52:42.529 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query=" alter table t modify column v varchar(5);"]
   > [2024/07/24 11:52:42.530 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:modify column, State:none, SchemaState:none, SchemaID:73, TableID:75, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:42.529 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:42.531 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=60] [neededSchemaVersion=61] ["start time"=206.663µs] [phyTblIDs="[75]"] [actionTypes="[4096]"]
   > [2024/07/24 11:52:42.533 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=61] ["take time"=2.287189ms] [job="ID:77, Type:modify column, State:running, SchemaState:delete only, SchemaID:73, TableID:75, RowCount:0, ArgLen:7, start time: 2024-07-24 11:52:42.529 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:42.533 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:modify column, State:running, SchemaState:delete only, SchemaID:73, TableID:75, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:42.529 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:42.535 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=61] [neededSchemaVersion=62] ["start time"=274.759µs] [phyTblIDs="[75]"] [actionTypes="[4096]"]
   > [2024/07/24 11:52:42.537 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=62] ["take time"=2.4106ms] [job="ID:77, Type:modify column, State:running, SchemaState:write only, SchemaID:73, TableID:75, RowCount:0, ArgLen:7, start time: 2024-07-24 11:52:42.529 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:42.537 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:modify column, State:running, SchemaState:write only, SchemaID:73, TableID:75, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:42.529 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:42.539 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=62] [neededSchemaVersion=63] ["start time"=327.629µs] [phyTblIDs="[75]"] [actionTypes="[4096]"]
   > [2024/07/24 11:52:42.542 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=63] ["take time"=2.706941ms] [job="ID:77, Type:modify column, State:running, SchemaState:write reorganization, SchemaID:73, TableID:75, RowCount:0, ArgLen:7, start time: 2024-07-24 11:52:42.529 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:42.542 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:modify column, State:running, SchemaState:write reorganization, SchemaID:73, TableID:75, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:42.529 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:42.543 +00:00] [INFO] [reorg.go:524] ["[ddl] get table range, endHandle < startHandle"] [table="&{75 t utf8mb4 utf8mb4_bin [int(11) varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin varchar(5) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin] [] [] [] public true false  0 0 0 3 0 0 451365296547299328 0 0 0 0 0 <nil>  <nil> <nil> <nil> 3 <nil> false}"] ["table/partition ID"=75] [endHandle="key: "] [startHandle="key: "]
   > [2024/07/24 11:52:42.543 +00:00] [INFO] [reorg.go:584] ["[ddl] job get table range"] [jobID=77] [physicalTableID=75] [startHandle="key: "] [endHandle="key: "]
   > [2024/07/24 11:52:42.544 +00:00] [INFO] [ddl_worker.go:768] ["[ddl] schema version doesn't change"] [worker="worker 3, tp general"]
   > [2024/07/24 11:52:42.545 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:modify column, State:running, SchemaState:write reorganization, SchemaID:73, TableID:75, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:42.529 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:451365296548872192"]
   > [2024/07/24 11:52:42.545 +00:00] [INFO] [reorg.go:165] ["sleep before reorganization to make async commit safe"] [duration=2.5s]
   > [2024/07/24 11:52:45.046 +00:00] [INFO] [column.go:1078] ["[ddl] start to update table row"] [job="ID:77, Type:modify column, State:running, SchemaState:write reorganization, SchemaID:73, TableID:75, RowCount:0, ArgLen:7, start time: 2024-07-24 11:52:42.529 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:451365296548872192"] [reorgInfo="CurrElementType:_col_,CurrElementID:3,StartHandle:key: ,EndHandle:key: ,First:false,PhysicalTableID:75"]
   > [2024/07/24 11:52:45.047 +00:00] [INFO] [reorg.go:524] ["[ddl] get table range, endHandle < startHandle"] [table="&{75 t utf8mb4 utf8mb4_bin [int(11) varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin varchar(5) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin] [] [] [] public true false  0 0 0 3 0 0 451365296547299328 0 0 0 0 0 <nil>  <nil> <nil> <nil> 3 <nil> false}"] ["table/partition ID"=75] [endHandle="key: "] [startHandle="key: "]
   > [2024/07/24 11:52:45.047 +00:00] [INFO] [reorg.go:209] ["[ddl] run reorg job done"] ["handled rows"=0]
   > [2024/07/24 11:52:45.049 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=63] [neededSchemaVersion=64] ["start time"=283.419µs] [phyTblIDs="[75]"] [actionTypes="[4096]"]
   > [2024/07/24 11:52:45.051 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=64] ["take time"=2.275735ms] [job="ID:77, Type:modify column, State:done, SchemaState:public, SchemaID:73, TableID:75, RowCount:0, ArgLen:2, start time: 2024-07-24 11:52:42.529 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:451365296548872192"]
   > [2024/07/24 11:52:45.051 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=77] [jobType="modify column"]
   > [2024/07/24 11:52:45.051 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:modify column, State:synced, SchemaState:public, SchemaID:73, TableID:75, RowCount:0, ArgLen:2, start time: 2024-07-24 11:52:42.529 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:451365296548872192"]
   > [2024/07/24 11:52:45.053 +00:00] [INFO] [ddl.go:543] ["[ddl] DDL job is finished"] [jobID=77]
   > [2024/07/24 11:52:45.053 +00:00] [INFO] [domain.go:659] ["performing DDL change, must reload"]
   > [2024/07/24 11:52:47.823 +00:00] [INFO] [2pc.go:1353] ["amend txn successfully"] [conn=2199023255575] [connID=2199023255575] ["txn startTS"=451365296383197184] [memAmended=false] [checkTS=451365297932992512] [startInfoSchemaVer=60] ["table ids"="[75]"] ["action types"="[4096]"]

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
   > [2024/07/24 11:52:49.460 +00:00] [INFO] [session.go:2455] ["CRUCIAL OPERATION"] [conn=2199023255581] [schemaVersion=72] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.74]
   > [2024/07/24 11:52:49.461 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:84, Type:drop schema, State:none, SchemaState:none, SchemaID:79, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:49.46 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 11:52:49.461 +00:00] [INFO] [ddl.go:491] ["[ddl] start DDL job"] [job="ID:84, Type:drop schema, State:none, SchemaState:none, SchemaID:79, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:49.46 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/24 11:52:49.461 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:84, Type:drop schema, State:none, SchemaState:none, SchemaID:79, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:49.46 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:49.462 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=72] [neededSchemaVersion=73] ["start time"=96.172µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 11:52:49.464 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=73] ["take time"=2.07012ms] [job="ID:84, Type:drop schema, State:running, SchemaState:write only, SchemaID:79, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:49.46 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:49.465 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:84, Type:drop schema, State:running, SchemaState:write only, SchemaID:79, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:49.46 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:49.466 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=73] [neededSchemaVersion=74] ["start time"=90.236µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 11:52:49.468 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=74] ["take time"=2.266097ms] [job="ID:84, Type:drop schema, State:running, SchemaState:delete only, SchemaID:79, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:49.46 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:49.468 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:84, Type:drop schema, State:running, SchemaState:delete only, SchemaID:79, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:49.46 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:49.469 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=74] [neededSchemaVersion=75] ["start time"=83.182µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 11:52:49.471 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=75] ["take time"=2.226496ms] [job="ID:84, Type:drop schema, State:done, SchemaState:none, SchemaID:79, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:49.46 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:49.471 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=84] [jobType="drop schema"]
   > [2024/07/24 11:52:49.471 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:84, Type:drop schema, State:synced, SchemaState:none, SchemaID:79, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:49.46 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:49.472 +00:00] [INFO] [ddl.go:543] ["[ddl] DDL job is finished"] [jobID=84]
   > [2024/07/24 11:52:49.473 +00:00] [INFO] [domain.go:659] ["performing DDL change, must reload"]
   > [2024/07/24 11:52:49.474 +00:00] [INFO] [session.go:2455] ["CRUCIAL OPERATION"] [conn=2199023255581] [schemaVersion=75] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.74]
   > [2024/07/24 11:52:49.476 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:86, Type:create schema, State:none, SchemaState:none, SchemaID:85, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 11:52:49.475 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 11:52:49.476 +00:00] [INFO] [ddl.go:491] ["[ddl] start DDL job"] [job="ID:86, Type:create schema, State:none, SchemaState:none, SchemaID:85, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 11:52:49.475 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/24 11:52:49.476 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:86, Type:create schema, State:none, SchemaState:none, SchemaID:85, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:49.475 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:49.478 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=75] [neededSchemaVersion=76] ["start time"=131.094µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 11:52:49.480 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=76] ["take time"=2.227404ms] [job="ID:86, Type:create schema, State:done, SchemaState:public, SchemaID:85, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 11:52:49.475 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:49.480 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:86, Type:create schema, State:synced, SchemaState:public, SchemaID:85, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:49.475 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:49.481 +00:00] [INFO] [ddl.go:543] ["[ddl] DDL job is finished"] [jobID=86]
   > [2024/07/24 11:52:49.481 +00:00] [INFO] [domain.go:659] ["performing DDL change, must reload"]
   > [2024/07/24 11:52:50.503 +00:00] [INFO] [set.go:217] ["set global var"] [conn=2199023255583] [name=tidb_enable_change_column_type] [val=1]
   > [2024/07/24 11:52:50.796 +00:00] [INFO] [session.go:2455] ["CRUCIAL OPERATION"] [conn=2199023255583] [schemaVersion=76] [cur_db=testdb] [sql=" create table t (id int primary key, v varchar(10));"] [user=root@10.88.0.74]
   > [2024/07/24 11:52:50.797 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:88, Type:create table, State:none, SchemaState:none, SchemaID:85, TableID:87, RowCount:0, ArgLen:1, start time: 2024-07-24 11:52:50.796 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 11:52:50.797 +00:00] [INFO] [ddl.go:491] ["[ddl] start DDL job"] [job="ID:88, Type:create table, State:none, SchemaState:none, SchemaID:85, TableID:87, RowCount:0, ArgLen:1, start time: 2024-07-24 11:52:50.796 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query=" create table t (id int primary key, v varchar(10));"]
   > [2024/07/24 11:52:50.798 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:88, Type:create table, State:none, SchemaState:none, SchemaID:85, TableID:87, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:50.796 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:50.800 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=76] [neededSchemaVersion=77] ["start time"=268.962µs] [phyTblIDs="[87]"] [actionTypes="[8]"]
   > [2024/07/24 11:52:50.802 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=77] ["take time"=2.327348ms] [job="ID:88, Type:create table, State:done, SchemaState:public, SchemaID:85, TableID:87, RowCount:0, ArgLen:1, start time: 2024-07-24 11:52:50.796 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:50.802 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:88, Type:create table, State:synced, SchemaState:public, SchemaID:85, TableID:87, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:50.796 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:50.803 +00:00] [INFO] [ddl.go:543] ["[ddl] DDL job is finished"] [jobID=88]
   > [2024/07/24 11:52:50.803 +00:00] [INFO] [domain.go:659] ["performing DDL change, must reload"]
   > [2024/07/24 11:52:50.803 +00:00] [INFO] [split_region.go:61] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=58] ["first split key"=748000000000000057]
   > [2024/07/24 11:52:50.804 +00:00] [INFO] [split_region.go:158] ["batch split regions complete"] ["batch region ID"=58] ["first at"=748000000000000057] ["first new region left"="{Id:58 StartKey:7480000000000000ff5100000000000000f8 EndKey:7480000000000000ff5700000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:59 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/24 11:52:50.804 +00:00] [INFO] [split_region.go:207] ["split regions complete"] ["region count"=1] ["region IDs"="[58]"]
   > [2024/07/24 11:52:51.416 +00:00] [INFO] [session.go:2455] ["CRUCIAL OPERATION"] [conn=2199023255585] [schemaVersion=77] [cur_db=testdb] [sql=" alter table t modify column v varchar(5);"] [user=root@10.88.0.74]
   > [2024/07/24 11:52:51.418 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:89, Type:modify column, State:none, SchemaState:none, SchemaID:85, TableID:87, RowCount:0, ArgLen:5, start time: 2024-07-24 11:52:51.417 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 11:52:51.418 +00:00] [INFO] [ddl.go:491] ["[ddl] start DDL job"] [job="ID:89, Type:modify column, State:none, SchemaState:none, SchemaID:85, TableID:87, RowCount:0, ArgLen:5, start time: 2024-07-24 11:52:51.417 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query=" alter table t modify column v varchar(5);"]
   > [2024/07/24 11:52:51.418 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:89, Type:modify column, State:none, SchemaState:none, SchemaID:85, TableID:87, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:51.417 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:51.419 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=77] [neededSchemaVersion=78] ["start time"=204.916µs] [phyTblIDs="[87]"] [actionTypes="[4096]"]
   > [2024/07/24 11:52:51.421 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=78] ["take time"=2.285373ms] [job="ID:89, Type:modify column, State:running, SchemaState:delete only, SchemaID:85, TableID:87, RowCount:0, ArgLen:7, start time: 2024-07-24 11:52:51.417 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:51.421 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:89, Type:modify column, State:running, SchemaState:delete only, SchemaID:85, TableID:87, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:51.417 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:51.423 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=78] [neededSchemaVersion=79] ["start time"=211.831µs] [phyTblIDs="[87]"] [actionTypes="[4096]"]
   > [2024/07/24 11:52:51.425 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=79] ["take time"=2.738998ms] [job="ID:89, Type:modify column, State:running, SchemaState:write only, SchemaID:85, TableID:87, RowCount:0, ArgLen:7, start time: 2024-07-24 11:52:51.417 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:51.426 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:89, Type:modify column, State:running, SchemaState:write only, SchemaID:85, TableID:87, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:51.417 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:51.428 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=79] [neededSchemaVersion=80] ["start time"=333.845µs] [phyTblIDs="[87]"] [actionTypes="[4096]"]
   > [2024/07/24 11:52:51.430 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=80] ["take time"=2.249474ms] [job="ID:89, Type:modify column, State:running, SchemaState:write reorganization, SchemaID:85, TableID:87, RowCount:0, ArgLen:7, start time: 2024-07-24 11:52:51.417 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:51.430 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:89, Type:modify column, State:running, SchemaState:write reorganization, SchemaID:85, TableID:87, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:51.417 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:52:51.431 +00:00] [INFO] [reorg.go:584] ["[ddl] job get table range"] [jobID=89] [physicalTableID=87] [startHandle=1] [endHandle=1]
   > [2024/07/24 11:52:51.432 +00:00] [INFO] [ddl_worker.go:768] ["[ddl] schema version doesn't change"] [worker="worker 3, tp general"]
   > [2024/07/24 11:52:51.433 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:89, Type:modify column, State:running, SchemaState:write reorganization, SchemaID:85, TableID:87, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:51.417 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:451365298878808064"]
   > [2024/07/24 11:52:51.434 +00:00] [INFO] [reorg.go:165] ["sleep before reorganization to make async commit safe"] [duration=2.5s]
   > [2024/07/24 11:52:53.935 +00:00] [INFO] [column.go:1078] ["[ddl] start to update table row"] [job="ID:89, Type:modify column, State:running, SchemaState:write reorganization, SchemaID:85, TableID:87, RowCount:0, ArgLen:7, start time: 2024-07-24 11:52:51.417 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:451365298878808064"] [reorgInfo=CurrElementType:_col_,CurrElementID:3,StartHandle:1,EndHandle:1,First:false,PhysicalTableID:87]
   > [2024/07/24 11:52:53.935 +00:00] [INFO] [backfilling.go:320] ["[ddl] split table range from PD"] [physicalTableID=87] [startHandle=1] [endHandle=1]
   > [2024/07/24 11:52:53.936 +00:00] [INFO] [backfilling.go:633] ["[ddl] start backfill workers to reorg record"] [workerCnt=1] [regionCnt=1] [startHandle=1] [endHandle=1]
   > [2024/07/24 11:52:53.936 +00:00] [INFO] [backfilling.go:288] ["[ddl] backfill worker start"] [workerID=0]
   > [2024/07/24 11:52:53.936 +00:00] [WARN] [backfilling.go:394] ["[ddl] backfill worker handle batch tasks failed"] [elementType=_col_] [elementID=3] [totalAddedCount=0] [startHandle=1] [nextHandle=1] [batchAddedCount=0] [taskFailedError="[types:1406]Data Too Long, field len 5, data len 9"] [takeTime=355.147µs] []
   > [2024/07/24 11:52:53.936 +00:00] [INFO] [reorg.go:209] ["[ddl] run reorg job done"] ["handled rows"=0]
   > [2024/07/24 11:52:53.936 +00:00] [INFO] [backfilling.go:313] ["[ddl] backfill worker exit"] [workerID=0]
   > [2024/07/24 11:52:53.936 +00:00] [WARN] [column.go:1006] ["[ddl] run modify column job failed, convert job to rollback"] [job="ID:89, Type:modify column, State:running, SchemaState:write reorganization, SchemaID:85, TableID:87, RowCount:0, ArgLen:7, start time: 2024-07-24 11:52:51.417 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:451365298878808064"] [error="[types:1406]Data Too Long, field len 5, data len 9"]
   > [2024/07/24 11:52:53.936 +00:00] [ERROR] [ddl_worker.go:714] ["[ddl] run DDL job error"] [worker="worker 3, tp general"] [error="[types:1406]Data Too Long, field len 5, data len 9"]
   > [2024/07/24 11:52:53.938 +00:00] [INFO] [ddl_worker.go:500] ["[ddl] run DDL job failed, sleeps a while then retries it."] [worker="worker 3, tp general"] [waitTime=1s] [error="[types:1406]Data Too Long, field len 5, data len 9"]
   > [2024/07/24 11:52:54.938 +00:00] [INFO] [ddl_worker.go:768] ["[ddl] schema version doesn't change"] [worker="worker 3, tp general"]
   > [2024/07/24 11:52:54.938 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:89, Type:modify column, State:rollingback, SchemaState:write reorganization, SchemaID:85, TableID:87, RowCount:0, ArgLen:0, start time: 2024-07-24 11:52:51.417 +0000 UTC, Err:[types:1406]Data Too Long, field len 5, data len 9, ErrCount:1, SnapshotVersion:451365298878808064"]
   > [2024/07/24 11:52:54.940 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=80] [neededSchemaVersion=81] ["start time"=256.949µs] [phyTblIDs="[87]"] [actionTypes="[4096]"]
   > [2024/07/24 11:52:54.942 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=81] ["take time"=2.225518ms] [job="ID:89, Type:modify column, State:rollback done, SchemaState:none, SchemaID:85, TableID:87, RowCount:0, ArgLen:2, start time: 2024-07-24 11:52:51.417 +0000 UTC, Err:[types:1406]Data Too Long, field len 5, data len 9, ErrCount:1, SnapshotVersion:451365298878808064"]
   > [2024/07/24 11:52:54.942 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=89] [jobType="modify column"]
   > [2024/07/24 11:52:54.942 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:89, Type:modify column, State:rollback done, SchemaState:none, SchemaID:85, TableID:87, RowCount:0, ArgLen:2, start time: 2024-07-24 11:52:51.417 +0000 UTC, Err:[types:1406]Data Too Long, field len 5, data len 9, ErrCount:1, SnapshotVersion:451365298878808064"]
   > [2024/07/24 11:52:54.943 +00:00] [INFO] [ddl_worker.go:768] ["[ddl] schema version doesn't change"] [worker="worker 3, tp general"]
   > [2024/07/24 11:52:55.418 +00:00] [INFO] [tidb.go:222] ["rollbackTxn for ddl/autocommit failed"]
   > [2024/07/24 11:52:55.418 +00:00] [WARN] [session.go:1261] ["run statement failed"] [conn=2199023255585] [schemaVersion=77] [error="[types:1406]Data Too Long, field len 5, data len 9"] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 2199023255585,\n  \"status\": 2,\n  \"strictMode\": true,\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"10.88.0.74\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/07/24 11:52:55.419 +00:00] [INFO] [conn.go:806] ["command dispatched failed"] [conn=2199023255585] [connInfo="id:2199023255585, addr:10.88.0.74:42476 status:10, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:0, autocommit:1"] [sql=" alter table t modify column v varchar(5);"] [txn_mode=OPTIMISTIC] [err="[types:1406]Data Too Long, field len 5, data len 9\ngithub.com/pingcap/errors.AddStack\n\t/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.20201029093017-5a7df2af2ac7/errors.go:174\ngithub.com/pingcap/errors.Trace\n\t/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.20201029093017-5a7df2af2ac7/juju_adaptor.go:15\ngithub.com/pingcap/tidb/ddl.(*ddl).doDDLJob\n\t/go/src/github.com/pingcap/tidb/ddl/ddl.go:548\ngithub.com/pingcap/tidb/ddl.(*ddl).ModifyColumn\n\t/go/src/github.com/pingcap/tidb/ddl/ddl_api.go:4039\ngithub.com/pingcap/tidb/ddl.(*ddl).AlterTable\n\t/go/src/github.com/pingcap/tidb/ddl/ddl_api.go:2431\ngithub.com/pingcap/tidb/executor.(*DDLExec).executeAlterTable\n\t/go/src/github.com/pingcap/tidb/executor/ddl.go:372\ngithub.com/pingcap/tidb/executor.(*DDLExec).Next\n\t/go/src/github.com/pingcap/tidb/executor/ddl.go:86\ngithub.com/pingcap/tidb/executor.Next\n\t/go/src/github.com/pingcap/tidb/executor/executor.go:277\ngithub.com/pingcap/tidb/executor.(*ExecStmt).handleNoDelayExecutor\n\t/go/src/github.com/pingcap/tidb/executor/adapter.go:524\ngithub.com/pingcap/tidb/executor.(*ExecStmt).handleNoDelay\n\t/go/src/github.com/pingcap/tidb/executor/adapter.go:405\ngithub.com/pingcap/tidb/executor.(*ExecStmt).Exec\n\t/go/src/github.com/pingcap/tidb/executor/adapter.go:355\ngithub.com/pingcap/tidb/session.runStmt\n\t/go/src/github.com/pingcap/tidb/session/session.go:1314\ngithub.com/pingcap/tidb/session.(*session).ExecuteStmt\n\t/go/src/github.com/pingcap/tidb/session/session.go:1258\ngithub.com/pingcap/tidb/server.(*TiDBContext).ExecuteStmt\n\t/go/src/github.com/pingcap/tidb/server/driver_tidb.go:212\ngithub.com/pingcap/tidb/server.(*clientConn).handleStmt\n\t/go/src/github.com/pingcap/tidb/server/conn.go:1556\ngithub.com/pingcap/tidb/server.(*clientConn).handleQuery\n\t/go/src/github.com/pingcap/tidb/server/conn.go:1448\ngithub.com/pingcap/tidb/server.(*clientConn).dispatch\n\t/go/src/github.com/pingcap/tidb/server/conn.go:1024\ngithub.com/pingcap/tidb/server.(*clientConn).Run\n\t/go/src/github.com/pingcap/tidb/server/conn.go:789\ngithub.com/pingcap/tidb/server.(*Server).onConn\n\t/go/src/github.com/pingcap/tidb/server/server.go:459\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1594"]
