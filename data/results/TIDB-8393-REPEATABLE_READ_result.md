# Bug ID TIDB-8393-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/8393
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              Gets warnings when running in a transaction.


## Details
 * Database: tidb-v6.4.0
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
   > [2024/07/12 14:19:12.918 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/12 14:19:12.921 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=2199023255957] [schemaVersion=34] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/12 14:19:12.922 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=2199023255957] [schemaVersion=34] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/12 14:19:12.926 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:71, Type:create schema, State:queueing, SchemaState:none, SchemaID:70, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-12 14:19:12.924 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/12 14:19:12.926 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:71, Type:create schema, State:queueing, SchemaState:none, SchemaID:70, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-12 14:19:12.924 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/12 14:19:13.652 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:71, Type:create schema, State:queueing, SchemaState:none, SchemaID:70, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-12 14:19:12.924 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/12 14:19:13.655 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=34] [neededSchemaVersion=35] ["start time"=168.389µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/12 14:19:13.657 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=35] ["take time"=2.128298ms] [job="ID:71, Type:create schema, State:done, SchemaState:public, SchemaID:70, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-12 14:19:12.924 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/12 14:19:13.666 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:71, Type:create schema, State:synced, SchemaState:public, SchemaID:70, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-12 14:19:12.924 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/12 14:19:13.668 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=71]
   > [2024/07/12 14:19:13.668 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/12 14:19:13.671 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=2199023255957] [schemaVersion=35] [cur_db=testdb] [sql="create table t(a bigint, b bigint);"] [user=root@%]
   > [2024/07/12 14:19:13.675 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:73, Type:create table, State:queueing, SchemaState:none, SchemaID:70, TableID:72, RowCount:0, ArgLen:2, start time: 2024-07-12 14:19:13.674 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/12 14:19:13.676 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:73, Type:create table, State:queueing, SchemaState:none, SchemaID:70, TableID:72, RowCount:0, ArgLen:2, start time: 2024-07-12 14:19:13.674 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t(a bigint, b bigint);"]
   > [2024/07/12 14:19:13.683 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:73, Type:create table, State:queueing, SchemaState:none, SchemaID:70, TableID:72, RowCount:0, ArgLen:0, start time: 2024-07-12 14:19:13.674 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/12 14:19:13.686 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=35] [neededSchemaVersion=36] ["start time"=318.2µs] [phyTblIDs="[72]"] [actionTypes="[8]"]
   > [2024/07/12 14:19:13.688 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=36] ["take time"=2.059852ms] [job="ID:73, Type:create table, State:done, SchemaState:public, SchemaID:70, TableID:72, RowCount:0, ArgLen:2, start time: 2024-07-12 14:19:13.674 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/12 14:19:13.692 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:73, Type:create table, State:synced, SchemaState:public, SchemaID:70, TableID:72, RowCount:0, ArgLen:0, start time: 2024-07-12 14:19:13.674 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/12 14:19:13.695 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=73]
   > [2024/07/12 14:19:13.695 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/12 14:19:13.695 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=74] ["first split key"=748000000000000048]
   > [2024/07/12 14:19:13.698 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=76] ["first at"=748000000000000048] ["first new region left"="{Id:76 StartKey:7480000000000000ff4400000000000000f8 EndKey:7480000000000000ff4800000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:77 store_id:1 ] EncryptionMeta:<nil> IsInFlashback:false}"] ["new region count"=1]
   > [2024/07/12 14:19:13.698 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[76]"]
   > [2024/07/12 14:19:14.645 +00:00] [INFO] [info.go:1085] [SetTiFlashGroupConfig]
   > [2024/07/12 14:19:14.725 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/12 14:19:14.737 +00:00] [INFO] [set.go:141] ["set global var"] [conn=2199023255959] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/07/12 14:19:15.626 +00:00] [WARN] [2pc.go:1873] ["schemaLeaseChecker is not set for this transaction"] [sessionID=2199023255959] [startTS=451095810703622144] [checkTS=451095810703622145]
