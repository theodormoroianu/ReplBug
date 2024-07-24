# Bug ID TIDB-24195-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/24195
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              Query in optimistic transaction returns rows with same PK


## Details
 * Database: tidb-v6.4.0.tikv
 * Number of scenarios: 3
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
     - Instruction:  begin optimistic;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows: 0
 * Instruction #2:
     - Instruction:  insert into t values (1, 10);
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows: 1
 * Instruction #3:
     - Instruction:  select * from t;
     - Transaction: conn_0
     - Output: [(1, 10), (1, 10)]
     - Executed order: 3
     - Affected rows: 2
 * Instruction #4:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: ERROR: 1062 (23000): Duplicate entry '1-10' for key 't.PRIMARY'
     - Executed order: Not executed
     - Affected rows: -1

 * Container logs:
   > [2024/07/24 12:47:12.042 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/24 12:47:12.046 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=8690506920592671145] [schemaVersion=70] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/24 12:47:12.082 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:102, Type:drop schema, State:queueing, SchemaState:public, SchemaID:97, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:47:12.028 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 12:47:12.082 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:102, Type:drop schema, State:queueing, SchemaState:public, SchemaID:97, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:47:12.028 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/24 12:47:12.106 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:102, Type:drop schema, State:queueing, SchemaState:public, SchemaID:97, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:12.028 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:12.161 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=70] [neededSchemaVersion=71] ["start time"=768.332µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:47:12.210 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=71] ["take time"=58.728382ms] [job="ID:102, Type:drop schema, State:running, SchemaState:write only, SchemaID:97, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:12.028 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:12.215 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:102, Type:drop schema, State:running, SchemaState:write only, SchemaID:97, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:12.028 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:12.275 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=71] [neededSchemaVersion=72] ["start time"=794.802µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:47:12.325 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=72] ["take time"=59.165732ms] [job="ID:102, Type:drop schema, State:running, SchemaState:delete only, SchemaID:97, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:12.028 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:12.329 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:102, Type:drop schema, State:running, SchemaState:delete only, SchemaID:97, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:12.028 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:12.384 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=72] [neededSchemaVersion=73] ["start time"=800.739µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:47:12.432 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=73] ["take time"=61.147289ms] [job="ID:102, Type:drop schema, State:done, SchemaState:none, SchemaID:97, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:12.028 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:12.438 +00:00] [INFO] [delete_range.go:109] ["[ddl] add job into delete-range table"] [jobID=102] [jobType="drop schema"]
   > [2024/07/24 12:47:12.440 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:102, Type:drop schema, State:synced, SchemaState:none, SchemaID:97, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:12.028 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:12.465 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=102]
   > [2024/07/24 12:47:12.465 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 12:47:12.466 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000066FF0000000000000000F7 lock_version: 451366153729343490 key: 748000FFFFFFFFFFFE5F728000000000000066 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451366153729343491"]
   > [2024/07/24 12:47:12.466 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000066FF0000000000000000F7 lock_version: 451366153729343490 key: 748000FFFFFFFFFFFE5F728000000000000066 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451366153729343491"]
   > [2024/07/24 12:47:12.469 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=8690506920592671145] [schemaVersion=73] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/24 12:47:12.472 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000066FF0000000000000000F7 lock_version: 451366153729343490 key: 748000FFFFFFFFFFFE5F728000000000000066 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451366153729343491"]
   > [2024/07/24 12:47:12.472 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000066FF0000000000000000F7 lock_version: 451366153729343490 key: 748000FFFFFFFFFFFE5F728000000000000066 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451366153729343491"]
   > [2024/07/24 12:47:12.532 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:104, Type:create schema, State:queueing, SchemaState:none, SchemaID:103, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:47:12.478 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 12:47:12.532 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:104, Type:create schema, State:queueing, SchemaState:none, SchemaID:103, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:47:12.478 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/24 12:47:12.560 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:104, Type:create schema, State:queueing, SchemaState:none, SchemaID:103, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:12.478 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:12.616 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=73] [neededSchemaVersion=74] ["start time"=1.5602ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:47:12.664 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=74] ["take time"=58.194929ms] [job="ID:104, Type:create schema, State:done, SchemaState:public, SchemaID:103, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:47:12.478 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:12.671 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:104, Type:create schema, State:synced, SchemaState:public, SchemaID:103, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:12.478 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:12.696 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=104]
   > [2024/07/24 12:47:12.696 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 12:47:12.697 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000068FF0000000000000000F7 lock_version: 451366153781772290 key: 748000FFFFFFFFFFFE5F728000000000000068 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451366153781772291"]
   > [2024/07/24 12:47:12.697 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000068FF0000000000000000F7 lock_version: 451366153781772290 key: 748000FFFFFFFFFFFE5F728000000000000068 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451366153781772291"]
   > [2024/07/24 12:47:12.701 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=8690506920592671145] [schemaVersion=74] [cur_db=testdb] [sql="create table t (a int, b int, primary key (a, b) /*T![clustered_index] nonclustered */);"] [user=root@%]
   > [2024/07/24 12:47:12.703 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000068FF0000000000000000F7 lock_version: 451366153781772290 key: 748000FFFFFFFFFFFE5F728000000000000068 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451366153781772291"]
   > [2024/07/24 12:47:12.703 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000068FF0000000000000000F7 lock_version: 451366153781772290 key: 748000FFFFFFFFFFFE5F728000000000000068 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451366153781772291"]
   > [2024/07/24 12:47:12.767 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:106, Type:create table, State:queueing, SchemaState:none, SchemaID:103, TableID:105, RowCount:0, ArgLen:2, start time: 2024-07-24 12:47:12.728 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 12:47:12.767 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:106, Type:create table, State:queueing, SchemaState:none, SchemaID:103, TableID:105, RowCount:0, ArgLen:2, start time: 2024-07-24 12:47:12.728 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t (a int, b int, primary key (a, b) /*T![clustered_index] nonclustered */);"]
   > [2024/07/24 12:47:12.794 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:106, Type:create table, State:queueing, SchemaState:none, SchemaID:103, TableID:105, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:12.728 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:12.861 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=74] [neededSchemaVersion=75] ["start time"=2.409409ms] [phyTblIDs="[105]"] [actionTypes="[8]"]
   > [2024/07/24 12:47:12.908 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=75] ["take time"=62.050416ms] [job="ID:106, Type:create table, State:done, SchemaState:public, SchemaID:103, TableID:105, RowCount:0, ArgLen:2, start time: 2024-07-24 12:47:12.728 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:12.915 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:106, Type:create table, State:synced, SchemaState:public, SchemaID:103, TableID:105, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:12.728 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:12.944 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=106]
   > [2024/07/24 12:47:12.944 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 12:47:12.944 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=10] ["first split key"=748000000000000069]
   > [2024/07/24 12:47:12.945 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000006AFF0000000000000000F7 lock_version: 451366153847570434 key: 748000FFFFFFFFFFFE5F72800000000000006A lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451366153847570435"]
   > [2024/07/24 12:47:12.945 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000006AFF0000000000000000F7 lock_version: 451366153847570434 key: 748000FFFFFFFFFFFE5F72800000000000006A lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451366153847570435"]
   > [2024/07/24 12:47:12.951 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000006AFF0000000000000000F7 lock_version: 451366153847570434 key: 748000FFFFFFFFFFFE5F72800000000000006A lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451366153847570435"]
   > [2024/07/24 12:47:12.951 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000006AFF0000000000000000F7 lock_version: 451366153847570434 key: 748000FFFFFFFFFFFE5F72800000000000006A lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451366153847570435"]
   > [2024/07/24 12:47:12.951 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:53386] [split_keys="key 7480000000000000FF6900000000000000F8"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:47:12.952 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=90] [peer-ids="[91]"]
   > [2024/07/24 12:47:12.952 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 10 start_key: 7480000000000000FF6300000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 44 } peers { id: 11 store_id: 1 }"] [new_region_ids="[new_region_id: 90 new_peer_ids: 91]"] [region_id=10]
   > [2024/07/24 12:47:12.964 +00:00] [WARN] [2pc.go:1873] ["schemaLeaseChecker is not set for this transaction"] [sessionID=8690506920592671145] [startTS=451366153860677638] [checkTS=451366153860677640]
   > [2024/07/24 12:47:12.969 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF6900000000000000F8 new_region_id: 90 new_peer_ids: 91 } right_derive: true }"] [index=78] [term=6] [peer_id=11] [region_id=10]
   > [2024/07/24 12:47:12.969 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF6900000000000000F8"] [region="id: 10 start_key: 7480000000000000FF6300000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 44 } peers { id: 11 store_id: 1 }"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:47:12.980 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/24 12:47:12.980 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=10]
   > [2024/07/24 12:47:12.980 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=11] [region_id=10]
   > [2024/07/24 12:47:12.980 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(85)] [region_id=10] [store_id=Some(1)]
   > [2024/07/24 12:47:12.980 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 10 start_key: 7480000000000000FF6900000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 45 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 12:47:12.981 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=10] ["first at"=748000000000000069] ["first new region left"="{Id:90 StartKey:7480000000000000ff6300000000000000f8 EndKey:7480000000000000ff6900000000000000f8 RegionEpoch:{ConfVer:1 Version:45} Peers:[id:91 store_id:1 ] EncryptionMeta:<nil> IsInFlashback:false}"] ["new region count"=1]
   > [2024/07/24 12:47:12.981 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 90 start_key: 7480000000000000FF6300000000000000F8 end_key: 7480000000000000FF6900000000000000F8 region_epoch { conf_ver: 1 version: 45 } peers { id: 91 store_id: 1 }"] [region_id=90]
   > [2024/07/24 12:47:12.981 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[90]"]
   > [2024/07/24 12:47:12.981 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=91] [region_id=90]
   > [2024/07/24 12:47:12.981 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {91} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=91] [region_id=90]
   > [2024/07/24 12:47:12.981 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=91] [region_id=90]
   > [2024/07/24 12:47:12.981 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {91} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=91] [region_id=90]
   > [2024/07/24 12:47:12.981 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 91."] [id=91] [raft_id=91] [region_id=90]
   > [2024/07/24 12:47:12.981 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=10] [detail="StartKey Changed:{7480000000000000FF6300000000000000F8} -> {7480000000000000FF6900000000000000F8}, EndKey:{748000FFFFFFFFFFFFFB00000000000000F8}"] [old-version=44] [new-version=45]
   > [2024/07/24 12:47:12.981 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=91] [region_id=90]
   > [2024/07/24 12:47:12.981 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=10] [origin="id:90 start_key:\"7480000000000000FF6300000000000000F8\" end_key:\"7480000000000000FF6900000000000000F8\" region_epoch:<conf_ver:1 version:45 > peers:<id:91 store_id:1 >"] [total=1]
   > [2024/07/24 12:47:12.981 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=91] [region_id=90]
   > [2024/07/24 12:47:12.981 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=91] [region_id=90]
   > [2024/07/24 12:47:12.982 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=91] [region_id=90]
   > [2024/07/24 12:47:12.982 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 10 start_key: 7480000000000000FF6900000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 45 } peers { id: 11 store_id: 1 } }"]
   > [2024/07/24 12:47:12.982 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 10 start_key: 7480000000000000FF6900000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 45 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 12:47:12.982 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803866] [region_id=90]
   > [2024/07/24 12:47:12.982 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=90]
   > [2024/07/24 12:47:12.987 +00:00] [INFO] [scheduler.rs:640] ["get snapshot failed"] [err="Error(Request(message: \"EpochNotMatch current epoch of region 10 is conf_ver: 1 version: 45, but you sent conf_ver: 1 version: 44\" epoch_not_match { current_regions { id: 10 start_key: 7480000000000000FF6900000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 45 } peers { id: 11 store_id: 1 } } current_regions { id: 90 start_key: 7480000000000000FF6300000000000000F8 end_key: 7480000000000000FF6900000000000000F8 region_epoch { conf_ver: 1 version: 45 } peers { id: 91 store_id: 1 } } }))"] [cid=1663]
   > [2024/07/24 12:47:12.987 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 90 start_key: 7480000000000000FF6300000000000000F8 end_key: 7480000000000000FF6900000000000000F8 region_epoch { conf_ver: 1 version: 45 } peers { id: 91 store_id: 1 }"]
   > [2024/07/24 12:47:12.987 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=78] [observe_id=ObserveId(87)] [region=10]
   > [2024/07/24 12:47:12.988 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(88)] [region=90]
   > [2024/07/24 12:47:14.007 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/24 12:47:14.101 +00:00] [INFO] [set.go:141] ["set global var"] [conn=8690506920592671147] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/07/24 12:47:15.209 +00:00] [INFO] [conn.go:1152] ["command dispatched failed"] [conn=8690506920592671147] [connInfo="id:8690506920592671147, addr:10.88.0.83:52222 status:10, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:0, autocommit:1"] [sql=" commit;"] [txn_mode=PESSIMISTIC] [timestamp=451366154214309890] [err="previous statement:  select * from t;: [kv:1062]Duplicate entry '1-10' for key 't.PRIMARY'"]

### Scenario 1
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows: 0
 * Instruction #1:
     - Instruction:  begin pessimistic;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows: 0
 * Instruction #2:
     - Instruction:  insert into t values (1, 10);
     - Transaction: conn_0
     - Output: ERROR: 1062 (23000): Duplicate entry '1-10' for key 't.PRIMARY'
     - Executed order: Not executed
     - Affected rows: -1
 * Instruction #3:
     - Instruction:  select * from t;
     - Transaction: conn_0
     - Output: [(1, 10)]
     - Executed order: 2
     - Affected rows: 1
 * Instruction #4:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows: 0

 * Container logs:
   > [2024/07/24 12:47:18.610 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/24 12:47:18.613 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=8690506920592671151] [schemaVersion=83] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/24 12:47:18.654 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:113, Type:drop schema, State:queueing, SchemaState:public, SchemaID:108, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:47:18.577 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 12:47:18.654 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:113, Type:drop schema, State:queueing, SchemaState:public, SchemaID:108, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:47:18.577 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/24 12:47:18.677 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:113, Type:drop schema, State:queueing, SchemaState:public, SchemaID:108, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:18.577 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:18.731 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=83] [neededSchemaVersion=84] ["start time"=831.748µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:47:18.779 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=84] ["take time"=57.521582ms] [job="ID:113, Type:drop schema, State:running, SchemaState:write only, SchemaID:108, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:18.577 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:18.784 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:113, Type:drop schema, State:running, SchemaState:write only, SchemaID:108, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:18.577 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:18.830 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=84] [neededSchemaVersion=85] ["start time"=794.103µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:47:18.879 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=85] ["take time"=58.271965ms] [job="ID:113, Type:drop schema, State:running, SchemaState:delete only, SchemaID:108, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:18.577 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:18.884 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:113, Type:drop schema, State:running, SchemaState:delete only, SchemaID:108, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:18.577 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:18.945 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=85] [neededSchemaVersion=86] ["start time"=707.569µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:47:18.994 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=86] ["take time"=57.686199ms] [job="ID:113, Type:drop schema, State:done, SchemaState:none, SchemaID:108, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:18.577 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:18.999 +00:00] [INFO] [delete_range.go:109] ["[ddl] add job into delete-range table"] [jobID=113] [jobType="drop schema"]
   > [2024/07/24 12:47:19.001 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:113, Type:drop schema, State:synced, SchemaState:none, SchemaID:108, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:18.577 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:19.025 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=113]
   > [2024/07/24 12:47:19.025 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 12:47:19.026 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000071FF0000000000000000F7 lock_version: 451366155446386690 key: 748000FFFFFFFFFFFE5F728000000000000071 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451366155446386691"]
   > [2024/07/24 12:47:19.026 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000071FF0000000000000000F7 lock_version: 451366155446386690 key: 748000FFFFFFFFFFFE5F728000000000000071 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451366155446386691"]
   > [2024/07/24 12:47:19.029 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=8690506920592671151] [schemaVersion=86] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/24 12:47:19.032 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000071FF0000000000000000F7 lock_version: 451366155446386690 key: 748000FFFFFFFFFFFE5F728000000000000071 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451366155446386691"]
   > [2024/07/24 12:47:19.032 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000071FF0000000000000000F7 lock_version: 451366155446386690 key: 748000FFFFFFFFFFFE5F728000000000000071 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451366155446386691"]
   > [2024/07/24 12:47:19.094 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:115, Type:create schema, State:queueing, SchemaState:none, SchemaID:114, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:47:19.028 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 12:47:19.094 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:115, Type:create schema, State:queueing, SchemaState:none, SchemaID:114, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:47:19.028 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/24 12:47:19.118 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:115, Type:create schema, State:queueing, SchemaState:none, SchemaID:114, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:19.028 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:19.168 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=86] [neededSchemaVersion=87] ["start time"=1.598613ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:47:19.216 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=87] ["take time"=57.695838ms] [job="ID:115, Type:create schema, State:done, SchemaState:public, SchemaID:114, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:47:19.028 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:19.223 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:115, Type:create schema, State:synced, SchemaState:public, SchemaID:114, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:19.028 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:19.240 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000073FF0000000000000000F7 lock_version: 451366155498815490 key: 748000FFFFFFFFFFFE5F728000000000000073 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451366155498815491"]
   > [2024/07/24 12:47:19.248 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=115]
   > [2024/07/24 12:47:19.248 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 12:47:19.252 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000073FF0000000000000000F7 lock_version: 451366155498815490 key: 748000FFFFFFFFFFFE5F728000000000000073 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451366155498815491"]
   > [2024/07/24 12:47:19.252 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000073FF0000000000000000F7 lock_version: 451366155498815490 key: 748000FFFFFFFFFFFE5F728000000000000073 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451366155498815491"]
   > [2024/07/24 12:47:19.253 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=8690506920592671151] [schemaVersion=87] [cur_db=testdb] [sql="create table t (a int, b int, primary key (a, b) /*T![clustered_index] nonclustered */);"] [user=root@%]
   > [2024/07/24 12:47:19.314 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:117, Type:create table, State:queueing, SchemaState:none, SchemaID:114, TableID:116, RowCount:0, ArgLen:2, start time: 2024-07-24 12:47:19.278 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 12:47:19.314 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:117, Type:create table, State:queueing, SchemaState:none, SchemaID:114, TableID:116, RowCount:0, ArgLen:2, start time: 2024-07-24 12:47:19.278 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t (a int, b int, primary key (a, b) /*T![clustered_index] nonclustered */);"]
   > [2024/07/24 12:47:19.339 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:117, Type:create table, State:queueing, SchemaState:none, SchemaID:114, TableID:116, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:19.278 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:19.395 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=87] [neededSchemaVersion=88] ["start time"=2.937414ms] [phyTblIDs="[116]"] [actionTypes="[8]"]
   > [2024/07/24 12:47:19.441 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=88] ["take time"=62.341796ms] [job="ID:117, Type:create table, State:done, SchemaState:public, SchemaID:114, TableID:116, RowCount:0, ArgLen:2, start time: 2024-07-24 12:47:19.278 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:19.447 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:117, Type:create table, State:synced, SchemaState:public, SchemaID:114, TableID:116, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:19.278 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:19.466 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=117]
   > [2024/07/24 12:47:19.466 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 12:47:19.466 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=10] ["first split key"=748000000000000074]
   > [2024/07/24 12:47:19.467 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:53372] [split_keys="key 7480000000000000FF7400000000000000F8"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:47:19.467 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000075FF0000000000000000F7 lock_version: 451366155564613634 key: 748000FFFFFFFFFFFE5F728000000000000075 lock_ttl: 3003 txn_size: 1 lock_type: Del min_commit_ts: 451366155564613635"]
   > [2024/07/24 12:47:19.467 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000075FF0000000000000000F7 lock_version: 451366155564613634 key: 748000FFFFFFFFFFFE5F728000000000000075 lock_ttl: 3003 txn_size: 1 lock_type: Del min_commit_ts: 451366155564613635"]
   > [2024/07/24 12:47:19.467 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=94] [peer-ids="[95]"]
   > [2024/07/24 12:47:19.468 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 10 start_key: 7480000000000000FF6E00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 46 } peers { id: 11 store_id: 1 }"] [new_region_ids="[new_region_id: 94 new_peer_ids: 95]"] [region_id=10]
   > [2024/07/24 12:47:19.474 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000075FF0000000000000000F7 lock_version: 451366155564613634 key: 748000FFFFFFFFFFFE5F728000000000000075 lock_ttl: 3003 txn_size: 1 lock_type: Del min_commit_ts: 451366155564613635"]
   > [2024/07/24 12:47:19.474 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000075FF0000000000000000F7 lock_version: 451366155564613634 key: 748000FFFFFFFFFFFE5F728000000000000075 lock_ttl: 3003 txn_size: 1 lock_type: Del min_commit_ts: 451366155564613635"]
   > [2024/07/24 12:47:19.485 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF7400000000000000F8 new_region_id: 94 new_peer_ids: 95 } right_derive: true }"] [index=83] [term=6] [peer_id=11] [region_id=10]
   > [2024/07/24 12:47:19.485 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF7400000000000000F8"] [region="id: 10 start_key: 7480000000000000FF6E00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 46 } peers { id: 11 store_id: 1 }"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:47:19.495 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=10]
   > [2024/07/24 12:47:19.495 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=11] [region_id=10]
   > [2024/07/24 12:47:19.495 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/24 12:47:19.495 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=10] ["first at"=748000000000000074] ["first new region left"="{Id:94 StartKey:7480000000000000ff6e00000000000000f8 EndKey:7480000000000000ff7400000000000000f8 RegionEpoch:{ConfVer:1 Version:47} Peers:[id:95 store_id:1 ] EncryptionMeta:<nil> IsInFlashback:false}"] ["new region count"=1]
   > [2024/07/24 12:47:19.495 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 94 start_key: 7480000000000000FF6E00000000000000F8 end_key: 7480000000000000FF7400000000000000F8 region_epoch { conf_ver: 1 version: 47 } peers { id: 95 store_id: 1 }"] [region_id=94]
   > [2024/07/24 12:47:19.495 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[94]"]
   > [2024/07/24 12:47:19.495 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=95] [region_id=94]
   > [2024/07/24 12:47:19.495 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=10] [detail="StartKey Changed:{7480000000000000FF6E00000000000000F8} -> {7480000000000000FF7400000000000000F8}, EndKey:{748000FFFFFFFFFFFFFB00000000000000F8}"] [old-version=46] [new-version=47]
   > [2024/07/24 12:47:19.495 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(89)] [region_id=10] [store_id=Some(1)]
   > [2024/07/24 12:47:19.496 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 10 start_key: 7480000000000000FF7400000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 47 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 12:47:19.495 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=10] [origin="id:94 start_key:\"7480000000000000FF6E00000000000000F8\" end_key:\"7480000000000000FF7400000000000000F8\" region_epoch:<conf_ver:1 version:47 > peers:<id:95 store_id:1 >"] [total=1]
   > [2024/07/24 12:47:19.496 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 10 start_key: 7480000000000000FF7400000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 47 } peers { id: 11 store_id: 1 } }"]
   > [2024/07/24 12:47:19.496 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 10 start_key: 7480000000000000FF7400000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 47 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 12:47:19.496 +00:00] [WARN] [2pc.go:1873] ["schemaLeaseChecker is not set for this transaction"] [sessionID=8690506920592671151] [startTS=451366155564613641] [checkTS=451366155577458689]
   > [2024/07/24 12:47:19.496 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {95} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=95] [region_id=94]
   > [2024/07/24 12:47:19.496 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=95] [region_id=94]
   > [2024/07/24 12:47:19.496 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {95} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=95] [region_id=94]
   > [2024/07/24 12:47:19.496 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 95."] [id=95] [raft_id=95] [region_id=94]
   > [2024/07/24 12:47:19.496 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=95] [region_id=94]
   > [2024/07/24 12:47:19.496 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=95] [region_id=94]
   > [2024/07/24 12:47:19.496 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=95] [region_id=94]
   > [2024/07/24 12:47:19.496 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=95] [region_id=94]
   > [2024/07/24 12:47:19.497 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803870] [region_id=94]
   > [2024/07/24 12:47:19.497 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=83] [observe_id=ObserveId(91)] [region=10]
   > [2024/07/24 12:47:19.497 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=94]
   > [2024/07/24 12:47:19.501 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 94 start_key: 7480000000000000FF6E00000000000000F8 end_key: 7480000000000000FF7400000000000000F8 region_epoch { conf_ver: 1 version: 47 } peers { id: 95 store_id: 1 }"]
   > [2024/07/24 12:47:19.502 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(92)] [region=94]
   > [2024/07/24 12:47:19.508 +00:00] [INFO] [scheduler.rs:640] ["get snapshot failed"] [err="Error(Request(message: \"EpochNotMatch current epoch of region 10 is conf_ver: 1 version: 47, but you sent conf_ver: 1 version: 46\" epoch_not_match { current_regions { id: 10 start_key: 7480000000000000FF7400000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 47 } peers { id: 11 store_id: 1 } } current_regions { id: 94 start_key: 7480000000000000FF6E00000000000000F8 end_key: 7480000000000000FF7400000000000000F8 region_epoch { conf_ver: 1 version: 47 } peers { id: 95 store_id: 1 } } }))"] [cid=1903]
   > [2024/07/24 12:47:20.529 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/24 12:47:20.571 +00:00] [INFO] [set.go:141] ["set global var"] [conn=8690506920592671153] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/07/24 12:47:21.129 +00:00] [INFO] [conn.go:1152] ["command dispatched failed"] [conn=8690506920592671153] [connInfo="id:8690506920592671153, addr:10.88.0.83:45610 status:11, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:1, autocommit:1"] [sql=" insert into t values (1, 10);"] [txn_mode=PESSIMISTIC] [timestamp=451366155918508033] [err="[kv:1062]Duplicate entry '1-10' for key 't.PRIMARY'"]

### Scenario 2
 * Instruction #0:
     - Instruction:  insert into t values (1, 10);
     - Transaction: conn_0
     - Output: ERROR: 1062 (23000): Duplicate entry '1-10' for key 't.PRIMARY'
     - Executed order: Not executed
     - Affected rows: -1
 * Instruction #1:
     - Instruction:  select * from t;
     - Transaction: conn_0
     - Output: [(1, 10)]
     - Executed order: 0
     - Affected rows: 1

 * Container logs:
   > [2024/07/24 12:47:25.310 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/24 12:47:25.314 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=8690506920592671157] [schemaVersion=96] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/24 12:47:25.350 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:124, Type:drop schema, State:queueing, SchemaState:public, SchemaID:119, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:47:25.278 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 12:47:25.350 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:124, Type:drop schema, State:queueing, SchemaState:public, SchemaID:119, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:47:25.278 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/24 12:47:25.374 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:124, Type:drop schema, State:queueing, SchemaState:public, SchemaID:119, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:25.278 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:25.421 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=96] [neededSchemaVersion=97] ["start time"=753.595µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:47:25.470 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=97] ["take time"=57.342088ms] [job="ID:124, Type:drop schema, State:running, SchemaState:write only, SchemaID:119, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:25.278 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:25.474 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:124, Type:drop schema, State:running, SchemaState:write only, SchemaID:119, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:25.278 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:25.522 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=97] [neededSchemaVersion=98] ["start time"=728.173µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:47:25.578 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=98] ["take time"=65.038955ms] [job="ID:124, Type:drop schema, State:running, SchemaState:delete only, SchemaID:119, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:25.278 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:25.583 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:124, Type:drop schema, State:running, SchemaState:delete only, SchemaID:119, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:25.278 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:25.636 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=98] [neededSchemaVersion=99] ["start time"=649.81µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:47:25.689 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=99] ["take time"=63.576045ms] [job="ID:124, Type:drop schema, State:done, SchemaState:none, SchemaID:119, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:25.278 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:25.694 +00:00] [INFO] [delete_range.go:109] ["[ddl] add job into delete-range table"] [jobID=124] [jobType="drop schema"]
   > [2024/07/24 12:47:25.696 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:124, Type:drop schema, State:synced, SchemaState:none, SchemaID:119, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:25.278 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:25.721 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=124]
   > [2024/07/24 12:47:25.721 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 12:47:25.722 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000007CFF0000000000000000F7 lock_version: 451366157203013634 key: 748000FFFFFFFFFFFE5F72800000000000007C lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451366157203013635"]
   > [2024/07/24 12:47:25.722 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000007CFF0000000000000000F7 lock_version: 451366157203013634 key: 748000FFFFFFFFFFFE5F72800000000000007C lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451366157203013635"]
   > [2024/07/24 12:47:25.725 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=8690506920592671157] [schemaVersion=99] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/24 12:47:25.782 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:126, Type:create schema, State:queueing, SchemaState:none, SchemaID:125, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:47:25.728 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 12:47:25.782 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:126, Type:create schema, State:queueing, SchemaState:none, SchemaID:125, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:47:25.728 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/24 12:47:25.805 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:126, Type:create schema, State:queueing, SchemaState:none, SchemaID:125, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:25.728 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:25.848 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=99] [neededSchemaVersion=100] ["start time"=1.353817ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:47:25.901 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=100] ["take time"=62.877974ms] [job="ID:126, Type:create schema, State:done, SchemaState:public, SchemaID:125, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:47:25.728 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:25.908 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:126, Type:create schema, State:synced, SchemaState:public, SchemaID:125, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:25.728 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:25.931 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=126]
   > [2024/07/24 12:47:25.931 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 12:47:25.932 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000007EFF0000000000000000F7 lock_version: 451366157255180290 key: 748000FFFFFFFFFFFE5F72800000000000007E lock_ttl: 3003 txn_size: 1 lock_type: Del min_commit_ts: 451366157255180291"]
   > [2024/07/24 12:47:25.933 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000007EFF0000000000000000F7 lock_version: 451366157255180290 key: 748000FFFFFFFFFFFE5F72800000000000007E lock_ttl: 3003 txn_size: 1 lock_type: Del min_commit_ts: 451366157255180291"]
   > [2024/07/24 12:47:25.937 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=8690506920592671157] [schemaVersion=100] [cur_db=testdb] [sql="create table t (a int, b int, primary key (a, b) /*T![clustered_index] nonclustered */);"] [user=root@%]
   > [2024/07/24 12:47:25.990 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:128, Type:create table, State:queueing, SchemaState:none, SchemaID:125, TableID:127, RowCount:0, ArgLen:2, start time: 2024-07-24 12:47:25.927 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 12:47:25.990 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:128, Type:create table, State:queueing, SchemaState:none, SchemaID:125, TableID:127, RowCount:0, ArgLen:2, start time: 2024-07-24 12:47:25.927 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t (a int, b int, primary key (a, b) /*T![clustered_index] nonclustered */);"]
   > [2024/07/24 12:47:26.016 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:128, Type:create table, State:queueing, SchemaState:none, SchemaID:125, TableID:127, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:25.927 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:26.076 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=100] [neededSchemaVersion=101] ["start time"=1.976598ms] [phyTblIDs="[127]"] [actionTypes="[8]"]
   > [2024/07/24 12:47:26.131 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=101] ["take time"=68.478603ms] [job="ID:128, Type:create table, State:done, SchemaState:public, SchemaID:125, TableID:127, RowCount:0, ArgLen:2, start time: 2024-07-24 12:47:25.927 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:26.138 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:128, Type:create table, State:synced, SchemaState:public, SchemaID:125, TableID:127, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:25.927 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:26.163 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=128]
   > [2024/07/24 12:47:26.163 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 12:47:26.164 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=10] ["first split key"=74800000000000007f]
   > [2024/07/24 12:47:26.165 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000080FF0000000000000000F7 lock_version: 451366157320978434 key: 748000FFFFFFFFFFFE5F728000000000000080 lock_ttl: 3005 txn_size: 1 lock_type: Del min_commit_ts: 451366157320978435"]
   > [2024/07/24 12:47:26.165 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000080FF0000000000000000F7 lock_version: 451366157320978434 key: 748000FFFFFFFFFFFE5F728000000000000080 lock_ttl: 3005 txn_size: 1 lock_type: Del min_commit_ts: 451366157320978435"]
   > [2024/07/24 12:47:26.168 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:53370] [split_keys="key 7480000000000000FF7F00000000000000F8"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:47:26.168 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=98] [peer-ids="[99]"]
   > [2024/07/24 12:47:26.169 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 10 start_key: 7480000000000000FF7900000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 48 } peers { id: 11 store_id: 1 }"] [new_region_ids="[new_region_id: 98 new_peer_ids: 99]"] [region_id=10]
   > [2024/07/24 12:47:26.171 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000080FF0000000000000000F7 lock_version: 451366157320978434 key: 748000FFFFFFFFFFFE5F728000000000000080 lock_ttl: 3005 txn_size: 1 lock_type: Del min_commit_ts: 451366157320978435"]
   > [2024/07/24 12:47:26.171 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000080FF0000000000000000F7 lock_version: 451366157320978434 key: 748000FFFFFFFFFFFE5F728000000000000080 lock_ttl: 3005 txn_size: 1 lock_type: Del min_commit_ts: 451366157320978435"]
   > [2024/07/24 12:47:26.179 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF7F00000000000000F8 new_region_id: 98 new_peer_ids: 99 } right_derive: true }"] [index=87] [term=6] [peer_id=11] [region_id=10]
   > [2024/07/24 12:47:26.179 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF7F00000000000000F8"] [region="id: 10 start_key: 7480000000000000FF7900000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 48 } peers { id: 11 store_id: 1 }"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:47:26.190 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/24 12:47:26.190 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=10]
   > [2024/07/24 12:47:26.190 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(93)] [region_id=10] [store_id=Some(1)]
   > [2024/07/24 12:47:26.190 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=11] [region_id=10]
   > [2024/07/24 12:47:26.190 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 10 start_key: 7480000000000000FF7F00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 49 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 12:47:26.190 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 98 start_key: 7480000000000000FF7900000000000000F8 end_key: 7480000000000000FF7F00000000000000F8 region_epoch { conf_ver: 1 version: 49 } peers { id: 99 store_id: 1 }"] [region_id=98]
   > [2024/07/24 12:47:26.190 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=99] [region_id=98]
   > [2024/07/24 12:47:26.190 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 10 start_key: 7480000000000000FF7F00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 49 } peers { id: 11 store_id: 1 } }"]
   > [2024/07/24 12:47:26.190 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=10] ["first at"=74800000000000007f] ["first new region left"="{Id:98 StartKey:7480000000000000ff7900000000000000f8 EndKey:7480000000000000ff7f00000000000000f8 RegionEpoch:{ConfVer:1 Version:49} Peers:[id:99 store_id:1 ] EncryptionMeta:<nil> IsInFlashback:false}"] ["new region count"=1]
   > [2024/07/24 12:47:26.190 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 10 start_key: 7480000000000000FF7F00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 49 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 12:47:26.190 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[98]"]
   > [2024/07/24 12:47:26.190 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=10] [detail="StartKey Changed:{7480000000000000FF7900000000000000F8} -> {7480000000000000FF7F00000000000000F8}, EndKey:{748000FFFFFFFFFFFFFB00000000000000F8}"] [old-version=48] [new-version=49]
   > [2024/07/24 12:47:26.190 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {99} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=99] [region_id=98]
   > [2024/07/24 12:47:26.190 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=10] [origin="id:98 start_key:\"7480000000000000FF7900000000000000F8\" end_key:\"7480000000000000FF7F00000000000000F8\" region_epoch:<conf_ver:1 version:49 > peers:<id:99 store_id:1 >"] [total=1]
   > [2024/07/24 12:47:26.191 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=99] [region_id=98]
   > [2024/07/24 12:47:26.191 +00:00] [WARN] [2pc.go:1873] ["schemaLeaseChecker is not set for this transaction"] [sessionID=8690506920592671157] [startTS=451366157320978441] [checkTS=451366157333823489]
   > [2024/07/24 12:47:26.191 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {99} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=99] [region_id=98]
   > [2024/07/24 12:47:26.191 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 99."] [id=99] [raft_id=99] [region_id=98]
   > [2024/07/24 12:47:26.191 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=99] [region_id=98]
   > [2024/07/24 12:47:26.191 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=99] [region_id=98]
   > [2024/07/24 12:47:26.191 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=99] [region_id=98]
   > [2024/07/24 12:47:26.191 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=99] [region_id=98]
   > [2024/07/24 12:47:26.191 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803874] [region_id=98]
   > [2024/07/24 12:47:26.191 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=98]
   > [2024/07/24 12:47:26.196 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 98 start_key: 7480000000000000FF7900000000000000F8 end_key: 7480000000000000FF7F00000000000000F8 region_epoch { conf_ver: 1 version: 49 } peers { id: 99 store_id: 1 }"]
   > [2024/07/24 12:47:26.196 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=87] [observe_id=ObserveId(95)] [region=10]
   > [2024/07/24 12:47:26.197 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(96)] [region=98]
   > [2024/07/24 12:47:26.203 +00:00] [INFO] [scheduler.rs:640] ["get snapshot failed"] [err="Error(Request(message: \"EpochNotMatch current epoch of region 10 is conf_ver: 1 version: 49, but you sent conf_ver: 1 version: 48\" epoch_not_match { current_regions { id: 10 start_key: 7480000000000000FF7F00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 49 } peers { id: 11 store_id: 1 } } current_regions { id: 98 start_key: 7480000000000000FF7900000000000000F8 end_key: 7480000000000000FF7F00000000000000F8 region_epoch { conf_ver: 1 version: 49 } peers { id: 99 store_id: 1 } } }))"] [cid=2138]
   > [2024/07/24 12:47:27.225 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/24 12:47:27.232 +00:00] [INFO] [conn.go:1152] ["command dispatched failed"] [conn=8690506920592671159] [connInfo="id:8690506920592671159, addr:10.88.0.83:45642 status:10, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:0, autocommit:1"] [sql=" insert into t values (1, 10);"] [txn_mode=PESSIMISTIC] [timestamp=451366157609074693] [err="[kv:1062]Duplicate entry '1-10' for key 't.PRIMARY'"]
