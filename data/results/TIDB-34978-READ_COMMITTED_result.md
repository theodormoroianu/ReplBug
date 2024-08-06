# Bug ID TIDB-34978-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/34978
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              A SELECT throws an error after a DML operation in another transaction.


## Details
 * Database: tidb-v6.4.0.tikv
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
     - Instruction:  begin;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows: 0
 * Instruction #2:
     - Instruction:  alter table t drop column c;
     - Transaction: conn_1
     - Output: None
     - Executed order: 2
     - Affected rows: 0
 * Instruction #3:
     - Instruction:  insert into t values (3);
     - Transaction: conn_1
     - Output: None
     - Executed order: 3
     - Affected rows: 1
 * Instruction #4:
     - Instruction:  select * from t for update;
     - Transaction: conn_0
     - Output: ERROR: 1105 (HY000): [components/tidb_query_executors/src/table_scan_executor.rs:422]: Data is corrupted, missing data for NOT NULL column (offset = 1)
     - Executed order: Not executed
     - Affected rows: -1

 * Container logs:
   > [2024/08/06 16:16:36.523 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/08/06 16:16:36.525 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=5357761832478048671] [schemaVersion=48] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/08/06 16:16:36.561 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:81, Type:drop schema, State:queueing, SchemaState:public, SchemaID:76, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-06 16:16:36.502 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/08/06 16:16:36.561 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:81, Type:drop schema, State:queueing, SchemaState:public, SchemaID:76, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-06 16:16:36.502 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/08/06 16:16:36.584 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:81, Type:drop schema, State:queueing, SchemaState:public, SchemaID:76, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-06 16:16:36.502 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:16:36.631 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=48] [neededSchemaVersion=49] ["start time"=897.189µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/06 16:16:36.679 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=49] ["take time"=57.784206ms] [job="ID:81, Type:drop schema, State:running, SchemaState:write only, SchemaID:76, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-06 16:16:36.502 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:16:36.685 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:81, Type:drop schema, State:running, SchemaState:write only, SchemaID:76, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-06 16:16:36.502 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:16:36.730 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=49] [neededSchemaVersion=50] ["start time"=839.989µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/06 16:16:36.778 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=50] ["take time"=58.396789ms] [job="ID:81, Type:drop schema, State:running, SchemaState:delete only, SchemaID:76, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-06 16:16:36.502 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:16:36.783 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:81, Type:drop schema, State:running, SchemaState:delete only, SchemaID:76, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-06 16:16:36.502 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:16:36.836 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=50] [neededSchemaVersion=51] ["start time"=749.265µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/06 16:16:36.885 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=51] ["take time"=59.01978ms] [job="ID:81, Type:drop schema, State:done, SchemaState:none, SchemaID:76, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-06 16:16:36.502 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:16:36.891 +00:00] [INFO] [delete_range.go:109] ["[ddl] add job into delete-range table"] [jobID=81] [jobType="drop schema"]
   > [2024/08/06 16:16:36.893 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:81, Type:drop schema, State:synced, SchemaState:none, SchemaID:76, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-06 16:16:36.502 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:16:36.917 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=81]
   > [2024/08/06 16:16:36.917 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/08/06 16:16:36.918 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000051FF0000000000000000F7 lock_version: 451663887558770690 key: 748000FFFFFFFFFFFE5F728000000000000051 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451663887558770691"]
   > [2024/08/06 16:16:36.918 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000051FF0000000000000000F7 lock_version: 451663887558770690 key: 748000FFFFFFFFFFFE5F728000000000000051 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451663887558770691"]
   > [2024/08/06 16:16:36.921 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=5357761832478048671] [schemaVersion=51] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/08/06 16:16:36.976 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:83, Type:create schema, State:queueing, SchemaState:none, SchemaID:82, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-06 16:16:36.903 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/08/06 16:16:36.977 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:83, Type:create schema, State:queueing, SchemaState:none, SchemaID:82, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-06 16:16:36.903 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/08/06 16:16:37.001 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:83, Type:create schema, State:queueing, SchemaState:none, SchemaID:82, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-06 16:16:36.903 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:16:37.053 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=51] [neededSchemaVersion=52] ["start time"=1.701908ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/06 16:16:37.101 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=52] ["take time"=59.372272ms] [job="ID:83, Type:create schema, State:done, SchemaState:public, SchemaID:82, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-06 16:16:36.903 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:16:37.108 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:83, Type:create schema, State:synced, SchemaState:public, SchemaID:82, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-06 16:16:36.903 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:16:37.131 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=83]
   > [2024/08/06 16:16:37.131 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/08/06 16:16:37.133 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000053FF0000000000000000F7 lock_version: 451663887624306689 key: 748000FFFFFFFFFFFE5F728000000000000053 lock_ttl: 3003 txn_size: 1 lock_type: Del min_commit_ts: 451663887624306690"]
   > [2024/08/06 16:16:37.133 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000053FF0000000000000000F7 lock_version: 451663887624306689 key: 748000FFFFFFFFFFFE5F728000000000000053 lock_ttl: 3003 txn_size: 1 lock_type: Del min_commit_ts: 451663887624306690"]
   > [2024/08/06 16:16:37.137 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=5357761832478048671] [schemaVersion=52] [cur_db=testdb] [sql="create table t (id int primary key, c int not null);"] [user=root@%]
   > [2024/08/06 16:16:37.190 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:85, Type:create table, State:queueing, SchemaState:none, SchemaID:82, TableID:84, RowCount:0, ArgLen:2, start time: 2024-08-06 16:16:37.152 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/08/06 16:16:37.191 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:85, Type:create table, State:queueing, SchemaState:none, SchemaID:82, TableID:84, RowCount:0, ArgLen:2, start time: 2024-08-06 16:16:37.152 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t (id int primary key, c int not null);"]
   > [2024/08/06 16:16:37.216 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:85, Type:create table, State:queueing, SchemaState:none, SchemaID:82, TableID:84, RowCount:0, ArgLen:0, start time: 2024-08-06 16:16:37.152 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:16:37.277 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=52] [neededSchemaVersion=53] ["start time"=2.552652ms] [phyTblIDs="[84]"] [actionTypes="[8]"]
   > [2024/08/06 16:16:37.324 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=53] ["take time"=61.944131ms] [job="ID:85, Type:create table, State:done, SchemaState:public, SchemaID:82, TableID:84, RowCount:0, ArgLen:2, start time: 2024-08-06 16:16:37.152 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:16:37.331 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:85, Type:create table, State:synced, SchemaState:public, SchemaID:82, TableID:84, RowCount:0, ArgLen:0, start time: 2024-08-06 16:16:37.152 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:16:37.357 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=85]
   > [2024/08/06 16:16:37.357 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/08/06 16:16:37.358 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=10] ["first split key"=748000000000000054]
   > [2024/08/06 16:16:37.359 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000055FF0000000000000000F7 lock_version: 451663887676997634 key: 748000FFFFFFFFFFFE5F728000000000000055 lock_ttl: 3005 txn_size: 1 lock_type: Del min_commit_ts: 451663887676997635"]
   > [2024/08/06 16:16:37.359 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000055FF0000000000000000F7 lock_version: 451663887676997634 key: 748000FFFFFFFFFFFE5F728000000000000055 lock_ttl: 3005 txn_size: 1 lock_type: Del min_commit_ts: 451663887676997635"]
   > [2024/08/06 16:16:37.362 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:40758] [split_keys="key 7480000000000000FF5400000000000000F8"] [peer_id=11] [region_id=10]
   > [2024/08/06 16:16:37.363 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=82] [peer-ids="[83]"]
   > [2024/08/06 16:16:37.363 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 10 start_key: 7480000000000000FF4E00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 40 } peers { id: 11 store_id: 1 }"] [new_region_ids="[new_region_id: 82 new_peer_ids: 83]"] [region_id=10]
   > [2024/08/06 16:16:37.378 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF5400000000000000F8 new_region_id: 82 new_peer_ids: 83 } right_derive: true }"] [index=72] [term=6] [peer_id=11] [region_id=10]
   > [2024/08/06 16:16:37.378 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF5400000000000000F8"] [region="id: 10 start_key: 7480000000000000FF4E00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 40 } peers { id: 11 store_id: 1 }"] [peer_id=11] [region_id=10]
   > [2024/08/06 16:16:37.384 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/08/06 16:16:37.385 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=10] ["first at"=748000000000000054] ["first new region left"="{Id:82 StartKey:7480000000000000ff4e00000000000000f8 EndKey:7480000000000000ff5400000000000000f8 RegionEpoch:{ConfVer:1 Version:41} Peers:[id:83 store_id:1 ] EncryptionMeta:<nil> IsInFlashback:false}"] ["new region count"=1]
   > [2024/08/06 16:16:37.385 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[82]"]
   > [2024/08/06 16:16:37.384 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=10]
   > [2024/08/06 16:16:37.384 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(77)] [region_id=10] [store_id=Some(1)]
   > [2024/08/06 16:16:37.384 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=11] [region_id=10]
   > [2024/08/06 16:16:37.384 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 10 start_key: 7480000000000000FF5400000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 11 store_id: 1 }"]
   > [2024/08/06 16:16:37.384 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 82 start_key: 7480000000000000FF4E00000000000000F8 end_key: 7480000000000000FF5400000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 83 store_id: 1 }"] [region_id=82]
   > [2024/08/06 16:16:37.384 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=83] [region_id=82]
   > [2024/08/06 16:16:37.385 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 10 start_key: 7480000000000000FF5400000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 11 store_id: 1 } }"]
   > [2024/08/06 16:16:37.385 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 10 start_key: 7480000000000000FF5400000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 11 store_id: 1 }"]
   > [2024/08/06 16:16:37.385 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {83} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=83] [region_id=82]
   > [2024/08/06 16:16:37.385 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=83] [region_id=82]
   > [2024/08/06 16:16:37.385 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {83} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=83] [region_id=82]
   > [2024/08/06 16:16:37.385 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=10] [origin="id:82 start_key:\"7480000000000000FF4E00000000000000F8\" end_key:\"7480000000000000FF5400000000000000F8\" region_epoch:<conf_ver:1 version:41 > peers:<id:83 store_id:1 >"] [total=1]
   > [2024/08/06 16:16:37.385 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=10] [detail="StartKey Changed:{7480000000000000FF4E00000000000000F8} -> {7480000000000000FF5400000000000000F8}, EndKey:{748000FFFFFFFFFFFFFB00000000000000F8}"] [old-version=40] [new-version=41]
   > [2024/08/06 16:16:37.385 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 83."] [id=83] [raft_id=83] [region_id=82]
   > [2024/08/06 16:16:37.385 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=83] [region_id=82]
   > [2024/08/06 16:16:37.385 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=83] [region_id=82]
   > [2024/08/06 16:16:37.385 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=83] [region_id=82]
   > [2024/08/06 16:16:37.385 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=83] [region_id=82]
   > [2024/08/06 16:16:37.385 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803858] [region_id=82]
   > [2024/08/06 16:16:37.386 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=82]
   > [2024/08/06 16:16:37.391 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 82 start_key: 7480000000000000FF4E00000000000000F8 end_key: 7480000000000000FF5400000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 83 store_id: 1 }"]
   > [2024/08/06 16:16:37.391 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=72] [observe_id=ObserveId(79)] [region=10]
   > [2024/08/06 16:16:37.391 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(80)] [region=82]
   > [2024/08/06 16:16:38.412 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/08/06 16:16:38.510 +00:00] [INFO] [set.go:141] ["set global var"] [conn=5357761832478048673] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/08/06 16:16:39.023 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/08/06 16:16:39.028 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=5357761832478048675] [schemaVersion=53] [cur_db=testdb] [sql=" alter table t drop column c;"] [user=root@%]
   > [2024/08/06 16:16:39.068 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:86, Type:drop column, State:queueing, SchemaState:public, SchemaID:82, TableID:84, RowCount:0, ArgLen:2, start time: 2024-08-06 16:16:39.003 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/08/06 16:16:39.068 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:86, Type:drop column, State:queueing, SchemaState:public, SchemaID:82, TableID:84, RowCount:0, ArgLen:2, start time: 2024-08-06 16:16:39.003 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query=" alter table t drop column c;"]
   > [2024/08/06 16:16:39.093 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:86, Type:drop column, State:queueing, SchemaState:public, SchemaID:82, TableID:84, RowCount:0, ArgLen:0, start time: 2024-08-06 16:16:39.003 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:16:39.141 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=53] [neededSchemaVersion=54] ["start time"=2.504252ms] [phyTblIDs="[84]"] [actionTypes="[64]"]
   > [2024/08/06 16:16:39.188 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=54] ["take time"=58.499038ms] [job="ID:86, Type:drop column, State:running, SchemaState:write only, SchemaID:82, TableID:84, RowCount:0, ArgLen:2, start time: 2024-08-06 16:16:39.003 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:16:39.194 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:86, Type:drop column, State:running, SchemaState:write only, SchemaID:82, TableID:84, RowCount:0, ArgLen:0, start time: 2024-08-06 16:16:39.003 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:16:39.248 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=54] [neededSchemaVersion=55] ["start time"=2.37707ms] [phyTblIDs="[84]"] [actionTypes="[64]"]
   > [2024/08/06 16:16:39.301 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=55] ["take time"=64.300108ms] [job="ID:86, Type:drop column, State:running, SchemaState:delete only, SchemaID:82, TableID:84, RowCount:0, ArgLen:3, start time: 2024-08-06 16:16:39.003 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:16:39.306 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:86, Type:drop column, State:running, SchemaState:delete only, SchemaID:82, TableID:84, RowCount:0, ArgLen:0, start time: 2024-08-06 16:16:39.003 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:16:39.359 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=55] [neededSchemaVersion=56] ["start time"=2.486024ms] [phyTblIDs="[84]"] [actionTypes="[64]"]
   > [2024/08/06 16:16:39.413 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=56] ["take time"=64.721045ms] [job="ID:86, Type:drop column, State:running, SchemaState:delete reorganization, SchemaID:82, TableID:84, RowCount:0, ArgLen:3, start time: 2024-08-06 16:16:39.003 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:16:39.418 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:86, Type:drop column, State:running, SchemaState:delete reorganization, SchemaID:82, TableID:84, RowCount:0, ArgLen:0, start time: 2024-08-06 16:16:39.003 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:16:39.473 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=56] [neededSchemaVersion=57] ["start time"=2.565783ms] [phyTblIDs="[84]"] [actionTypes="[64]"]
   > [2024/08/06 16:16:39.524 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=57] ["take time"=62.269314ms] [job="ID:86, Type:drop column, State:done, SchemaState:none, SchemaID:82, TableID:84, RowCount:0, ArgLen:4, start time: 2024-08-06 16:16:39.003 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:16:39.530 +00:00] [INFO] [delete_range.go:109] ["[ddl] add job into delete-range table"] [jobID=86] [jobType="drop column"]
   > [2024/08/06 16:16:39.532 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:86, Type:drop column, State:synced, SchemaState:none, SchemaID:82, TableID:84, RowCount:0, ArgLen:4, start time: 2024-08-06 16:16:39.003 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:16:39.560 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=86]
   > [2024/08/06 16:16:39.560 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/08/06 16:16:39.560 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000056FF0000000000000000F7 lock_version: 451663888253452290 key: 748000FFFFFFFFFFFE5F728000000000000056 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451663888253452291"]
   > [2024/08/06 16:16:39.561 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000056FF0000000000000000F7 lock_version: 451663888253452290 key: 748000FFFFFFFFFFFE5F728000000000000056 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451663888253452291"]
   > [2024/08/06 16:16:39.566 +00:00] [INFO] [scheduler.rs:640] ["get snapshot failed"] [err="Error(Request(message: \"EpochNotMatch current epoch of region 10 is conf_ver: 1 version: 41, but you sent conf_ver: 1 version: 40\" epoch_not_match { current_regions { id: 10 start_key: 7480000000000000FF5400000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 11 store_id: 1 } } current_regions { id: 82 start_key: 7480000000000000FF4E00000000000000F8 end_key: 7480000000000000FF5400000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 83 store_id: 1 } } }))"] [cid=1298]
   > [2024/08/06 16:16:39.566 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000056FF0000000000000000F7 lock_version: 451663888253452290 key: 748000FFFFFFFFFFFE5F728000000000000056 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451663888253452291"]
   > [2024/08/06 16:16:39.566 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000056FF0000000000000000F7 lock_version: 451663888253452290 key: 748000FFFFFFFFFFFE5F728000000000000056 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451663888253452291"]
   > [2024/08/06 16:16:39.624 +00:00] [WARN] [session.go:2191] ["run statement failed"] [conn=5357761832478048673] [schemaVersion=53] [error="[tikv:10000][components/tidb_query_executors/src/table_scan_executor.rs:422]: Data is corrupted, missing data for NOT NULL column (offset = 1)"] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 5357761832478048673,\n  \"status\": 3,\n  \"strictMode\": true,\n  \"txn\": \"451663888043999233\",\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"127.0.0.1\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/08/06 16:16:39.624 +00:00] [INFO] [conn.go:1152] ["command dispatched failed"] [conn=5357761832478048673] [connInfo="id:5357761832478048673, addr:127.0.0.1:51810 status:11, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:1, autocommit:1"] [sql=" select * from t for update;"] [txn_mode=PESSIMISTIC] [timestamp=451663888043999233] [err="[tikv:10000][components/tidb_query_executors/src/table_scan_executor.rs:422]: Data is corrupted, missing data for NOT NULL column (offset = 1)"]
