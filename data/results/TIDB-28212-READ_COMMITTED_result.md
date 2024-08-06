# Bug ID TIDB-28212-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/28212
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              Incorrect SELECT value when row is updated by 2 transactions.


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
     - Instruction:  select * from t;
     - Transaction: conn_0
     - Output: [(0, 0), (1, 1), (2, 2)]
     - Executed order: 2
     - Affected rows: 3
 * Instruction #3:
     - Instruction:  begin;
     - Transaction: conn_1
     - Output: None
     - Executed order: 3
     - Affected rows: 0
 * Instruction #4:
     - Instruction:  update t set a = 10 where b = 1;
     - Transaction: conn_1
     - Output: None
     - Executed order: 4
     - Affected rows: 1
 * Instruction #5:
     - Instruction:  commit;
     - Transaction: conn_1
     - Output: None
     - Executed order: 5
     - Affected rows: 0
 * Instruction #6:
     - Instruction:  select * from t;
     - Transaction: conn_0
     - Output: [(0, 0), (1, 1), (2, 2)]
     - Executed order: 6
     - Affected rows: 3
 * Instruction #7:
     - Instruction:  update t set a = 10 where true;
     - Transaction: conn_0
     - Output: None
     - Executed order: 7
     - Affected rows: 2
 * Instruction #8:
     - Instruction:  select * from t;
     - Transaction: conn_0
     - Output: [(10, 0), (1, 1), (10, 2)]
     - Executed order: 8
     - Affected rows: 3
 * Instruction #9:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: None
     - Executed order: 9
     - Affected rows: 0

 * Container logs:
   > [2024/08/06 12:44:30.889 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/08/06 12:44:30.893 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=4993064820661027231] [schemaVersion=44] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/08/06 12:44:30.921 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:80, Type:drop schema, State:queueing, SchemaState:public, SchemaID:75, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-06 12:44:30.875 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/08/06 12:44:30.921 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:80, Type:drop schema, State:queueing, SchemaState:public, SchemaID:75, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-06 12:44:30.875 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/08/06 12:44:30.941 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:80, Type:drop schema, State:queueing, SchemaState:public, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-06 12:44:30.875 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 12:44:30.990 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=44] [neededSchemaVersion=45] ["start time"=666.013µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/06 12:44:31.039 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=45] ["take time"=63.039076ms] [job="ID:80, Type:drop schema, State:running, SchemaState:write only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-06 12:44:30.875 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 12:44:31.043 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:80, Type:drop schema, State:running, SchemaState:write only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-06 12:44:30.875 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 12:44:31.089 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=45] [neededSchemaVersion=46] ["start time"=709.246µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/06 12:44:31.138 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=46] ["take time"=61.332486ms] [job="ID:80, Type:drop schema, State:running, SchemaState:delete only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-06 12:44:30.875 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 12:44:31.143 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:80, Type:drop schema, State:running, SchemaState:delete only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-06 12:44:30.875 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 12:44:31.183 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=46] [neededSchemaVersion=47] ["start time"=760.3µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/06 12:44:31.232 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=47] ["take time"=57.246586ms] [job="ID:80, Type:drop schema, State:done, SchemaState:none, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-06 12:44:30.875 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 12:44:31.238 +00:00] [INFO] [delete_range.go:109] ["[ddl] add job into delete-range table"] [jobID=80] [jobType="drop schema"]
   > [2024/08/06 12:44:31.240 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:80, Type:drop schema, State:synced, SchemaState:none, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-06 12:44:30.875 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 12:44:31.260 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=80]
   > [2024/08/06 12:44:31.261 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/08/06 12:44:31.262 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000050FF0000000000000000F7 lock_version: 451660551612006404 key: 748000FFFFFFFFFFFE5F728000000000000050 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451660551612006405"]
   > [2024/08/06 12:44:31.262 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000050FF0000000000000000F7 lock_version: 451660551612006404 key: 748000FFFFFFFFFFFE5F728000000000000050 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451660551612006405"]
   > [2024/08/06 12:44:31.265 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=4993064820661027231] [schemaVersion=47] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/08/06 12:44:31.311 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:82, Type:create schema, State:queueing, SchemaState:none, SchemaID:81, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-06 12:44:31.275 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/08/06 12:44:31.311 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:82, Type:create schema, State:queueing, SchemaState:none, SchemaID:81, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-06 12:44:31.275 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/08/06 12:44:31.333 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:82, Type:create schema, State:queueing, SchemaState:none, SchemaID:81, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-06 12:44:31.275 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 12:44:31.359 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D4442730000000000FA000000000000006844423A3831000000FC lock_version: 451660551638482946 key: 748000FFFFFFFFFFFE5F728000000000000052 lock_ttl: 3017 txn_size: 1 min_commit_ts: 451660551638482947"]
   > [2024/08/06 12:44:31.372 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=47] [neededSchemaVersion=48] ["start time"=1.336078ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/06 12:44:31.420 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=48] ["take time"=57.800574ms] [job="ID:82, Type:create schema, State:done, SchemaState:public, SchemaID:81, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-06 12:44:31.275 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 12:44:31.426 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:82, Type:create schema, State:synced, SchemaState:public, SchemaID:81, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-06 12:44:31.275 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 12:44:31.448 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=82]
   > [2024/08/06 12:44:31.448 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/08/06 12:44:31.449 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000052FF0000000000000000F7 lock_version: 451660551651590148 key: 748000FFFFFFFFFFFE5F728000000000000052 lock_ttl: 3003 txn_size: 1 lock_type: Del min_commit_ts: 451660551651590149"]
   > [2024/08/06 12:44:31.449 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000052FF0000000000000000F7 lock_version: 451660551651590148 key: 748000FFFFFFFFFFFE5F728000000000000052 lock_ttl: 3003 txn_size: 1 lock_type: Del min_commit_ts: 451660551651590149"]
   > [2024/08/06 12:44:31.453 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=4993064820661027231] [schemaVersion=48] [cur_db=testdb] [sql="create table t(a int, b int);"] [user=root@%]
   > [2024/08/06 12:44:31.454 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000052FF0000000000000000F7 lock_version: 451660551651590148 key: 748000FFFFFFFFFFFE5F728000000000000052 lock_ttl: 3003 txn_size: 1 lock_type: Del min_commit_ts: 451660551651590149"]
   > [2024/08/06 12:44:31.454 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000052FF0000000000000000F7 lock_version: 451660551651590148 key: 748000FFFFFFFFFFFE5F728000000000000052 lock_ttl: 3003 txn_size: 1 lock_type: Del min_commit_ts: 451660551651590149"]
   > [2024/08/06 12:44:31.497 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:84, Type:create table, State:queueing, SchemaState:none, SchemaID:81, TableID:83, RowCount:0, ArgLen:2, start time: 2024-08-06 12:44:31.426 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/08/06 12:44:31.497 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:84, Type:create table, State:queueing, SchemaState:none, SchemaID:81, TableID:83, RowCount:0, ArgLen:2, start time: 2024-08-06 12:44:31.426 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t(a int, b int);"]
   > [2024/08/06 12:44:31.520 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:84, Type:create table, State:queueing, SchemaState:none, SchemaID:81, TableID:83, RowCount:0, ArgLen:0, start time: 2024-08-06 12:44:31.426 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 12:44:31.570 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=48] [neededSchemaVersion=49] ["start time"=2.164755ms] [phyTblIDs="[83]"] [actionTypes="[8]"]
   > [2024/08/06 12:44:31.617 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=49] ["take time"=58.896185ms] [job="ID:84, Type:create table, State:done, SchemaState:public, SchemaID:81, TableID:83, RowCount:0, ArgLen:2, start time: 2024-08-06 12:44:31.426 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 12:44:31.623 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:84, Type:create table, State:synced, SchemaState:public, SchemaID:81, TableID:83, RowCount:0, ArgLen:0, start time: 2024-08-06 12:44:31.426 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 12:44:31.646 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=84]
   > [2024/08/06 12:44:31.646 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/08/06 12:44:31.646 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=10] ["first split key"=748000000000000053]
   > [2024/08/06 12:44:31.648 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000054FF0000000000000000F7 lock_version: 451660551703756803 key: 748000FFFFFFFFFFFE5F728000000000000054 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451660551703756804"]
   > [2024/08/06 12:44:31.648 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000054FF0000000000000000F7 lock_version: 451660551703756803 key: 748000FFFFFFFFFFFE5F728000000000000054 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451660551703756804"]
   > [2024/08/06 12:44:31.649 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:38434] [split_keys="key 7480000000000000FF5300000000000000F8"] [peer_id=11] [region_id=10]
   > [2024/08/06 12:44:31.650 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=82] [peer-ids="[83]"]
   > [2024/08/06 12:44:31.651 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 10 start_key: 7480000000000000FF4D00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 40 } peers { id: 11 store_id: 1 }"] [new_region_ids="[new_region_id: 82 new_peer_ids: 83]"] [region_id=10]
   > [2024/08/06 12:44:31.654 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000054FF0000000000000000F7 lock_version: 451660551703756803 key: 748000FFFFFFFFFFFE5F728000000000000054 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451660551703756804"]
   > [2024/08/06 12:44:31.654 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000054FF0000000000000000F7 lock_version: 451660551703756803 key: 748000FFFFFFFFFFFE5F728000000000000054 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451660551703756804"]
   > [2024/08/06 12:44:31.658 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF5300000000000000F8 new_region_id: 82 new_peer_ids: 83 } right_derive: true }"] [index=72] [term=6] [peer_id=11] [region_id=10]
   > [2024/08/06 12:44:31.658 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF5300000000000000F8"] [region="id: 10 start_key: 7480000000000000FF4D00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 40 } peers { id: 11 store_id: 1 }"] [peer_id=11] [region_id=10]
   > [2024/08/06 12:44:31.663 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=10] ["first at"=748000000000000053] ["first new region left"="{Id:82 StartKey:7480000000000000ff4d00000000000000f8 EndKey:7480000000000000ff5300000000000000f8 RegionEpoch:{ConfVer:1 Version:41} Peers:[id:83 store_id:1 ] EncryptionMeta:<nil> IsInFlashback:false}"] ["new region count"=1]
   > [2024/08/06 12:44:31.663 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[82]"]
   > [2024/08/06 12:44:31.663 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=10]
   > [2024/08/06 12:44:31.663 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/08/06 12:44:31.663 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(77)] [region_id=10] [store_id=Some(1)]
   > [2024/08/06 12:44:31.663 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=11] [region_id=10]
   > [2024/08/06 12:44:31.663 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 10 start_key: 7480000000000000FF5300000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 11 store_id: 1 }"]
   > [2024/08/06 12:44:31.663 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 82 start_key: 7480000000000000FF4D00000000000000F8 end_key: 7480000000000000FF5300000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 83 store_id: 1 }"] [region_id=82]
   > [2024/08/06 12:44:31.663 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=83] [region_id=82]
   > [2024/08/06 12:44:31.663 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 10 start_key: 7480000000000000FF5300000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 11 store_id: 1 } }"]
   > [2024/08/06 12:44:31.663 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 10 start_key: 7480000000000000FF5300000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 11 store_id: 1 }"]
   > [2024/08/06 12:44:31.663 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {83} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=83] [region_id=82]
   > [2024/08/06 12:44:31.663 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=83] [region_id=82]
   > [2024/08/06 12:44:31.663 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {83} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=83] [region_id=82]
   > [2024/08/06 12:44:31.664 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 83."] [id=83] [raft_id=83] [region_id=82]
   > [2024/08/06 12:44:31.664 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=83] [region_id=82]
   > [2024/08/06 12:44:31.664 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=83] [region_id=82]
   > [2024/08/06 12:44:31.664 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=83] [region_id=82]
   > [2024/08/06 12:44:31.664 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=83] [region_id=82]
   > [2024/08/06 12:44:31.664 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803858] [region_id=82]
   > [2024/08/06 12:44:31.664 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=10] [detail="StartKey Changed:{7480000000000000FF4D00000000000000F8} -> {7480000000000000FF5300000000000000F8}, EndKey:{748000FFFFFFFFFFFFFB00000000000000F8}"] [old-version=40] [new-version=41]
   > [2024/08/06 12:44:31.664 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=10] [origin="id:82 start_key:\"7480000000000000FF4D00000000000000F8\" end_key:\"7480000000000000FF5300000000000000F8\" region_epoch:<conf_ver:1 version:41 > peers:<id:83 store_id:1 >"] [total=1]
   > [2024/08/06 12:44:31.664 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=82]
   > [2024/08/06 12:44:31.664 +00:00] [WARN] [2pc.go:1873] ["schemaLeaseChecker is not set for this transaction"] [sessionID=4993064820661027231] [startTS=451660551716864006] [checkTS=451660551716864009]
   > [2024/08/06 12:44:31.668 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 82 start_key: 7480000000000000FF4D00000000000000F8 end_key: 7480000000000000FF5300000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 83 store_id: 1 }"]
   > [2024/08/06 12:44:31.668 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=72] [observe_id=ObserveId(79)] [region=10]
   > [2024/08/06 12:44:31.668 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(80)] [region=82]
   > [2024/08/06 12:44:31.673 +00:00] [INFO] [scheduler.rs:640] ["get snapshot failed"] [err="Error(Request(message: \"EpochNotMatch current epoch of region 10 is conf_ver: 1 version: 41, but you sent conf_ver: 1 version: 40\" epoch_not_match { current_regions { id: 10 start_key: 7480000000000000FF5300000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 11 store_id: 1 } } current_regions { id: 82 start_key: 7480000000000000FF4D00000000000000F8 end_key: 7480000000000000FF5300000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 83 store_id: 1 } } }))"] [cid=1205]
   > [2024/08/06 12:44:32.701 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/08/06 12:44:32.786 +00:00] [INFO] [set.go:141] ["set global var"] [conn=4993064820661027233] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/08/06 12:44:33.611 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
