# Bug ID TIDB-36581-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/36581
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              Issuing autocommit=on instructions makes rollback fail


## Details
 * Database: tidb-v6.1.0
 * Number of scenarios: 1
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows: 0
 * Instruction #1:
     - Instruction:  set autocommit = ON;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows: 0
 * Instruction #2:
     - Instruction:  begin;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows: 0
 * Instruction #3:
     - Instruction:  select * from test;
     - Transaction: conn_0
     - Output: [(590,)]
     - Executed order: 3
     - Affected rows: 1
 * Instruction #4:
     - Instruction:  update test set a=a+1;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows: 1
 * Instruction #5:
     - Instruction:  select * from test;
     - Transaction: conn_0
     - Output: [(591,)]
     - Executed order: 5
     - Affected rows: 1
 * Instruction #6:
     - Instruction:  set autocommit=ON;
     - Transaction: conn_0
     - Output: None
     - Executed order: 6
     - Affected rows: 0
 * Instruction #7:
     - Instruction:  rollback;
     - Transaction: conn_0
     - Output: None
     - Executed order: 7
     - Affected rows: 0
 * Instruction #8:
     - Instruction:  select * from test;
     - Transaction: conn_0
     - Output: [(591,)]
     - Executed order: 8
     - Affected rows: 1

 * Container logs:
   > [2024/07/24 12:53:09.004 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/07/24 12:53:09.007 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=42] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/24 12:53:09.008 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:75, Type:drop schema, State:none, SchemaState:queueing, SchemaID:70, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:53:09.007 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 12:53:09.008 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:75, Type:drop schema, State:none, SchemaState:queueing, SchemaID:70, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:53:09.007 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/24 12:53:09.009 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:75, Type:drop schema, State:none, SchemaState:queueing, SchemaID:70, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:53:09.007 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:53:09.010 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=42] [neededSchemaVersion=43] ["start time"=111.328µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:53:09.013 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=43] ["take time"=3.021574ms] [job="ID:75, Type:drop schema, State:running, SchemaState:write only, SchemaID:70, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:53:09.007 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:53:09.013 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:75, Type:drop schema, State:running, SchemaState:write only, SchemaID:70, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:53:09.007 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:53:09.014 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=43] [neededSchemaVersion=44] ["start time"=77.036µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:53:09.016 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=44] ["take time"=2.208893ms] [job="ID:75, Type:drop schema, State:running, SchemaState:delete only, SchemaID:70, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:53:09.007 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:53:09.016 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:75, Type:drop schema, State:running, SchemaState:delete only, SchemaID:70, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:53:09.007 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:53:09.017 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=44] [neededSchemaVersion=45] ["start time"=56.712µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:53:09.019 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=45] ["take time"=2.321547ms] [job="ID:75, Type:drop schema, State:done, SchemaState:queueing, SchemaID:70, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:53:09.007 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:53:09.020 +00:00] [INFO] [delete_range.go:103] ["[ddl] add job into delete-range table"] [jobID=75] [jobType="drop schema"]
   > [2024/07/24 12:53:09.020 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:75, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:70, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:53:09.007 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:53:09.021 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=75]
   > [2024/07/24 12:53:09.021 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/24 12:53:09.022 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=45] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/24 12:53:09.024 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:77, Type:create schema, State:none, SchemaState:queueing, SchemaID:76, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:53:09.023 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 12:53:09.024 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:77, Type:create schema, State:none, SchemaState:queueing, SchemaID:76, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:53:09.023 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/24 12:53:09.024 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:create schema, State:none, SchemaState:queueing, SchemaID:76, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:53:09.023 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:53:09.026 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=45] [neededSchemaVersion=46] ["start time"=181.659µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:53:09.028 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=46] ["take time"=2.253591ms] [job="ID:77, Type:create schema, State:done, SchemaState:public, SchemaID:76, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:53:09.023 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:53:09.028 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:create schema, State:synced, SchemaState:public, SchemaID:76, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:53:09.023 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:53:09.029 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=77]
   > [2024/07/24 12:53:09.029 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/24 12:53:09.031 +00:00] [INFO] [session.go:3244] ["CRUCIAL OPERATION"] [conn=411] [schemaVersion=46] [cur_db=testdb] [sql="create table test(a int);"] [user=root@%]
   > [2024/07/24 12:53:09.033 +00:00] [INFO] [ddl_worker.go:327] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:79, Type:create table, State:none, SchemaState:queueing, SchemaID:76, TableID:78, RowCount:0, ArgLen:1, start time: 2024-07-24 12:53:09.032 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 12:53:09.033 +00:00] [INFO] [ddl.go:705] ["[ddl] start DDL job"] [job="ID:79, Type:create table, State:none, SchemaState:queueing, SchemaID:76, TableID:78, RowCount:0, ArgLen:1, start time: 2024-07-24 12:53:09.032 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table test(a int);"]
   > [2024/07/24 12:53:09.033 +00:00] [INFO] [ddl_worker.go:774] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:79, Type:create table, State:none, SchemaState:queueing, SchemaID:76, TableID:78, RowCount:0, ArgLen:0, start time: 2024-07-24 12:53:09.032 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:53:09.035 +00:00] [INFO] [domain.go:140] ["diff load InfoSchema success"] [currentSchemaVersion=46] [neededSchemaVersion=47] ["start time"=258.136µs] [phyTblIDs="[78]"] [actionTypes="[8]"]
   > [2024/07/24 12:53:09.037 +00:00] [INFO] [ddl_worker.go:982] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=47] ["take time"=2.295287ms] [job="ID:79, Type:create table, State:done, SchemaState:public, SchemaID:76, TableID:78, RowCount:0, ArgLen:1, start time: 2024-07-24 12:53:09.032 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:53:09.037 +00:00] [INFO] [ddl_worker.go:441] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:79, Type:create table, State:synced, SchemaState:public, SchemaID:76, TableID:78, RowCount:0, ArgLen:0, start time: 2024-07-24 12:53:09.032 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:53:09.038 +00:00] [INFO] [ddl.go:771] ["[ddl] DDL job is finished"] [jobID=79]
   > [2024/07/24 12:53:09.038 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/24 12:53:09.038 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=66] ["first split key"=74800000000000004e]
   > [2024/07/24 12:53:09.039 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=66] ["first at"=74800000000000004e] ["first new region left"="{Id:66 StartKey:7480000000000000ff4800000000000000f8 EndKey:7480000000000000ff4e00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:67 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/24 12:53:09.039 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[66]"]
   > [2024/07/24 12:53:09.039 +00:00] [WARN] [2pc.go:1800] ["schemaLeaseChecker is not set for this transaction"] [sessionID=411] [startTS=451366247213039617] [checkTS=451366247213039618]
   > [2024/07/24 12:53:10.053 +00:00] [WARN] [collate.go:220] ["[ddl:1273]Unsupported collation when new collation is enabled: 'utf8mb4_0900_ai_ci'"]
   > [2024/07/24 12:53:10.064 +00:00] [INFO] [set.go:147] ["set global var"] [conn=413] [name=tx_isolation] [val=READ-COMMITTED]
