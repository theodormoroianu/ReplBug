# Bug ID TIDB-39977-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/39977
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              Gets warnings when running in a transaction.


## Details
 * Database: tidb-v6.4.0
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
     - Instruction:  BEGIN;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  DELETE FROM t;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 2 / 0
 * Instruction #3:
     - Instruction:  SELECT /*+ STREAM_AGG()*/c0 FROM t WHERE c1 FOR UPDATE; -- Warning
     - Transaction: conn_0
     - Output: []
     - Executed order: 3
     - Affected rows / Warnings: 0 / 2
 * Instruction #4:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows / Warnings: 0 / 0

 * Container logs:
   > [2024/07/10 13:46:04.056 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/10 13:46:04.059 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=2199023255957] [schemaVersion=34] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/10 13:46:04.060 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=2199023255957] [schemaVersion=34] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/10 13:46:04.064 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:71, Type:create schema, State:queueing, SchemaState:none, SchemaID:70, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-10 13:46:04.063 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/10 13:46:04.064 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:71, Type:create schema, State:queueing, SchemaState:none, SchemaID:70, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-10 13:46:04.063 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/10 13:46:04.786 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:71, Type:create schema, State:queueing, SchemaState:none, SchemaID:70, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-10 13:46:04.063 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:04.789 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=34] [neededSchemaVersion=35] ["start time"=162.313µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/10 13:46:04.791 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=35] ["take time"=2.037154ms] [job="ID:71, Type:create schema, State:done, SchemaState:public, SchemaID:70, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-10 13:46:04.063 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:04.801 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:71, Type:create schema, State:synced, SchemaState:public, SchemaID:70, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-10 13:46:04.063 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:04.804 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=71]
   > [2024/07/10 13:46:04.804 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/10 13:46:04.808 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=2199023255957] [schemaVersion=35] [cur_db=testdb] [sql="CREATE TABLE t(c0 DECIMAL, c1 BLOB(79));"] [user=root@%]
   > [2024/07/10 13:46:04.808 +00:00] [INFO] [ddl_api.go:1033] ["Automatically convert BLOB(79) to TINYBLOB"]
   > [2024/07/10 13:46:04.813 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:73, Type:create table, State:queueing, SchemaState:none, SchemaID:70, TableID:72, RowCount:0, ArgLen:2, start time: 2024-07-10 13:46:04.811 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/10 13:46:04.813 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:73, Type:create table, State:queueing, SchemaState:none, SchemaID:70, TableID:72, RowCount:0, ArgLen:2, start time: 2024-07-10 13:46:04.811 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE t(c0 DECIMAL, c1 BLOB(79));"]
   > [2024/07/10 13:46:04.821 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:73, Type:create table, State:queueing, SchemaState:none, SchemaID:70, TableID:72, RowCount:0, ArgLen:0, start time: 2024-07-10 13:46:04.811 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:04.825 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=35] [neededSchemaVersion=36] ["start time"=354.867µs] [phyTblIDs="[72]"] [actionTypes="[8]"]
   > [2024/07/10 13:46:04.827 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=36] ["take time"=2.208895ms] [job="ID:73, Type:create table, State:done, SchemaState:public, SchemaID:70, TableID:72, RowCount:0, ArgLen:2, start time: 2024-07-10 13:46:04.811 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:04.831 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:73, Type:create table, State:synced, SchemaState:public, SchemaID:70, TableID:72, RowCount:0, ArgLen:0, start time: 2024-07-10 13:46:04.811 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:04.834 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=73]
   > [2024/07/10 13:46:04.834 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/10 13:46:04.834 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=74] ["first split key"=748000000000000048]
   > [2024/07/10 13:46:04.835 +00:00] [WARN] [2pc.go:1873] ["schemaLeaseChecker is not set for this transaction"] [sessionID=2199023255957] [startTS=451049990346506241] [checkTS=451049990346506242]
   > [2024/07/10 13:46:04.837 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=76] ["first at"=748000000000000048] ["first new region left"="{Id:76 StartKey:7480000000000000ff4400000000000000f8 EndKey:7480000000000000ff4800000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:77 store_id:1 ] EncryptionMeta:<nil> IsInFlashback:false}"] ["new region count"=1]
   > [2024/07/10 13:46:04.837 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[76]"]
   > [2024/07/10 13:46:05.778 +00:00] [INFO] [info.go:1085] [SetTiFlashGroupConfig]
   > [2024/07/10 13:46:05.875 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/10 13:46:05.891 +00:00] [INFO] [set.go:141] ["set global var"] [conn=2199023255959] [name=tx_isolation] [val=REPEATABLE-READ]

### Scenario 1
 * Instruction #0:
     - Instruction:  DELETE FROM t;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 2 / 0
 * Instruction #1:
     - Instruction:  SELECT /*+ STREAM_AGG()*/c0 FROM t WHERE c1 FOR UPDATE; -- Warning
     - Transaction: conn_0
     - Output: []
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0

 * Container logs:
   > [2024/07/10 13:46:08.940 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/10 13:46:08.943 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=2199023255963] [schemaVersion=44] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/10 13:46:08.947 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:80, Type:drop schema, State:queueing, SchemaState:public, SchemaID:75, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-10 13:46:08.945 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/10 13:46:08.947 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:80, Type:drop schema, State:queueing, SchemaState:public, SchemaID:75, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-10 13:46:08.945 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/10 13:46:08.954 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:80, Type:drop schema, State:queueing, SchemaState:public, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-10 13:46:08.945 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:08.957 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=44] [neededSchemaVersion=45] ["start time"=78.852µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/10 13:46:08.959 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=45] ["take time"=2.053986ms] [job="ID:80, Type:drop schema, State:running, SchemaState:write only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-10 13:46:08.945 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:08.963 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:80, Type:drop schema, State:running, SchemaState:write only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-10 13:46:08.945 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:08.966 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=45] [neededSchemaVersion=46] ["start time"=91.702µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/10 13:46:08.968 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=46] ["take time"=2.117263ms] [job="ID:80, Type:drop schema, State:running, SchemaState:delete only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-10 13:46:08.945 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:08.972 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:80, Type:drop schema, State:running, SchemaState:delete only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-10 13:46:08.945 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:08.974 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=46] [neededSchemaVersion=47] ["start time"=79.34µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/10 13:46:08.976 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=47] ["take time"=2.014525ms] [job="ID:80, Type:drop schema, State:done, SchemaState:none, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-10 13:46:08.945 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:08.980 +00:00] [INFO] [delete_range.go:109] ["[ddl] add job into delete-range table"] [jobID=80] [jobType="drop schema"]
   > [2024/07/10 13:46:08.981 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:80, Type:drop schema, State:synced, SchemaState:none, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-10 13:46:08.945 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:08.983 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=80]
   > [2024/07/10 13:46:08.983 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/10 13:46:08.985 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=2199023255963] [schemaVersion=47] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/10 13:46:08.989 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:82, Type:create schema, State:queueing, SchemaState:none, SchemaID:81, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-10 13:46:08.987 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/10 13:46:08.989 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:82, Type:create schema, State:queueing, SchemaState:none, SchemaID:81, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-10 13:46:08.987 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/10 13:46:08.996 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:82, Type:create schema, State:queueing, SchemaState:none, SchemaID:81, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-10 13:46:08.987 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:08.999 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=47] [neededSchemaVersion=48] ["start time"=145.83µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/10 13:46:09.000 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=48] ["take time"=2.125295ms] [job="ID:82, Type:create schema, State:done, SchemaState:public, SchemaID:81, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-10 13:46:08.987 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:09.005 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:82, Type:create schema, State:synced, SchemaState:public, SchemaID:81, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-10 13:46:08.987 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:09.007 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=82]
   > [2024/07/10 13:46:09.007 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/10 13:46:09.010 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=2199023255963] [schemaVersion=48] [cur_db=testdb] [sql="CREATE TABLE t(c0 DECIMAL, c1 BLOB(79));"] [user=root@%]
   > [2024/07/10 13:46:09.010 +00:00] [INFO] [ddl_api.go:1033] ["Automatically convert BLOB(79) to TINYBLOB"]
   > [2024/07/10 13:46:09.015 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:84, Type:create table, State:queueing, SchemaState:none, SchemaID:81, TableID:83, RowCount:0, ArgLen:2, start time: 2024-07-10 13:46:09.013 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/10 13:46:09.015 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:84, Type:create table, State:queueing, SchemaState:none, SchemaID:81, TableID:83, RowCount:0, ArgLen:2, start time: 2024-07-10 13:46:09.013 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE t(c0 DECIMAL, c1 BLOB(79));"]
   > [2024/07/10 13:46:09.022 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:84, Type:create table, State:queueing, SchemaState:none, SchemaID:81, TableID:83, RowCount:0, ArgLen:0, start time: 2024-07-10 13:46:09.013 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:09.026 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=48] [neededSchemaVersion=49] ["start time"=392.582µs] [phyTblIDs="[83]"] [actionTypes="[8]"]
   > [2024/07/10 13:46:09.028 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=49] ["take time"=2.046652ms] [job="ID:84, Type:create table, State:done, SchemaState:public, SchemaID:81, TableID:83, RowCount:0, ArgLen:2, start time: 2024-07-10 13:46:09.013 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:09.032 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:84, Type:create table, State:synced, SchemaState:public, SchemaID:81, TableID:83, RowCount:0, ArgLen:0, start time: 2024-07-10 13:46:09.013 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/10 13:46:09.034 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=84]
   > [2024/07/10 13:46:09.034 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/10 13:46:09.034 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=80] ["first split key"=748000000000000053]
   > [2024/07/10 13:46:09.035 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=80] ["first at"=748000000000000053] ["first new region left"="{Id:80 StartKey:7480000000000000ff4d00000000000000f8 EndKey:7480000000000000ff5300000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:81 store_id:1 ] EncryptionMeta:<nil> IsInFlashback:false}"] ["new region count"=1]
   > [2024/07/10 13:46:09.035 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[80]"]
   > [2024/07/10 13:46:09.035 +00:00] [WARN] [2pc.go:1873] ["schemaLeaseChecker is not set for this transaction"] [sessionID=2199023255963] [startTS=451049991447511041] [checkTS=451049991447511043]
   > [2024/07/10 13:46:10.052 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
