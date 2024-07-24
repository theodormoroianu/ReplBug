# Bug ID TIDB-39851-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/39851
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              Select does not throw errors when running concurently.


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
     - Instruction:  BEGIN;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows: 0
 * Instruction #2:
     - Instruction:  BEGIN;
     - Transaction: conn_1
     - Output: None
     - Executed order: 2
     - Affected rows: 0
 * Instruction #3:
     - Instruction:  SELECT c1 FROM t WHERE c2 FOR UPDATE;
     - Transaction: conn_0
     - Output: [(1,)]
     - Executed order: 3
     - Affected rows: 1
 * Instruction #4:
     - Instruction:  SELECT /*+ INL_JOIN(t)*/c1 FROM t WHERE c2<=c1 FOR UPDATE;
     - Transaction: conn_1
     - Output: [(1,)]
     - Executed order: 5
     - Affected rows: 1
 * Instruction #5:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows: 0
 * Instruction #6:
     - Instruction:  COMMIT;
     - Transaction: conn_1
     - Output: None
     - Executed order: 6
     - Affected rows: 0

 * Container logs:
   > [2024/07/24 09:49:34.288 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/24 09:49:34.291 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=4672033813629501867] [schemaVersion=70] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/24 09:49:34.319 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:102, Type:drop schema, State:queueing, SchemaState:public, SchemaID:97, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 09:49:34.29 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 09:49:34.319 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:102, Type:drop schema, State:queueing, SchemaState:public, SchemaID:97, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 09:49:34.29 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/24 09:49:34.339 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:102, Type:drop schema, State:queueing, SchemaState:public, SchemaID:97, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:34.29 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:34.381 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=70] [neededSchemaVersion=71] ["start time"=791.52µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 09:49:34.430 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=71] ["take time"=56.557163ms] [job="ID:102, Type:drop schema, State:running, SchemaState:write only, SchemaID:97, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:34.29 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:34.436 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:102, Type:drop schema, State:running, SchemaState:write only, SchemaID:97, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:34.29 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:34.471 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=71] [neededSchemaVersion=72] ["start time"=619.918µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 09:49:34.520 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=72] ["take time"=56.037956ms] [job="ID:102, Type:drop schema, State:running, SchemaState:delete only, SchemaID:97, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:34.29 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:34.526 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:102, Type:drop schema, State:running, SchemaState:delete only, SchemaID:97, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:34.29 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:34.566 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=72] [neededSchemaVersion=73] ["start time"=1.066419ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 09:49:34.615 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=73] ["take time"=56.532438ms] [job="ID:102, Type:drop schema, State:done, SchemaState:none, SchemaID:97, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:34.29 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:34.621 +00:00] [INFO] [delete_range.go:109] ["[ddl] add job into delete-range table"] [jobID=102] [jobType="drop schema"]
   > [2024/07/24 09:49:34.623 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:102, Type:drop schema, State:synced, SchemaState:none, SchemaID:97, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:34.29 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:34.651 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=102]
   > [2024/07/24 09:49:34.651 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 09:49:34.652 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000066FF0000000000000000F7 lock_version: 451363359841320962 key: 748000FFFFFFFFFFFE5F728000000000000066 lock_ttl: 3006 txn_size: 1 lock_type: Del min_commit_ts: 451363359841320963"]
   > [2024/07/24 09:49:34.652 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000066FF0000000000000000F7 lock_version: 451363359841320962 key: 748000FFFFFFFFFFFE5F728000000000000066 lock_ttl: 3006 txn_size: 1 lock_type: Del min_commit_ts: 451363359841320963"]
   > [2024/07/24 09:49:34.655 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=4672033813629501867] [schemaVersion=73] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/24 09:49:34.696 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:104, Type:create schema, State:queueing, SchemaState:none, SchemaID:103, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 09:49:34.64 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 09:49:34.696 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:104, Type:create schema, State:queueing, SchemaState:none, SchemaID:103, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 09:49:34.64 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/24 09:49:34.718 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:104, Type:create schema, State:queueing, SchemaState:none, SchemaID:103, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:34.64 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:34.754 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=73] [neededSchemaVersion=74] ["start time"=1.519345ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 09:49:34.803 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=74] ["take time"=57.005269ms] [job="ID:104, Type:create schema, State:done, SchemaState:public, SchemaID:103, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 09:49:34.64 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:34.810 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:104, Type:create schema, State:synced, SchemaState:public, SchemaID:103, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:34.64 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:34.830 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=104]
   > [2024/07/24 09:49:34.830 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 09:49:34.831 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000068FF0000000000000000F7 lock_version: 451363359893749762 key: 748000FFFFFFFFFFFE5F728000000000000068 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451363359893749763"]
   > [2024/07/24 09:49:34.831 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000068FF0000000000000000F7 lock_version: 451363359893749762 key: 748000FFFFFFFFFFFE5F728000000000000068 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451363359893749763"]
   > [2024/07/24 09:49:34.835 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=4672033813629501867] [schemaVersion=74] [cur_db=testdb] [sql="CREATE TABLE t (c1 INT, c2 INT);"] [user=root@%]
   > [2024/07/24 09:49:34.877 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:106, Type:create table, State:queueing, SchemaState:none, SchemaID:103, TableID:105, RowCount:0, ArgLen:2, start time: 2024-07-24 09:49:34.84 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 09:49:34.877 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:106, Type:create table, State:queueing, SchemaState:none, SchemaID:103, TableID:105, RowCount:0, ArgLen:2, start time: 2024-07-24 09:49:34.84 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE t (c1 INT, c2 INT);"]
   > [2024/07/24 09:49:34.900 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:106, Type:create table, State:queueing, SchemaState:none, SchemaID:103, TableID:105, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:34.84 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:34.947 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=74] [neededSchemaVersion=75] ["start time"=2.578152ms] [phyTblIDs="[105]"] [actionTypes="[8]"]
   > [2024/07/24 09:49:34.994 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=75] ["take time"=58.3674ms] [job="ID:106, Type:create table, State:done, SchemaState:public, SchemaID:103, TableID:105, RowCount:0, ArgLen:2, start time: 2024-07-24 09:49:34.84 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:35.002 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:106, Type:create table, State:synced, SchemaState:public, SchemaID:103, TableID:105, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:34.84 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:35.023 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=106]
   > [2024/07/24 09:49:35.023 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 09:49:35.023 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=10] ["first split key"=748000000000000069]
   > [2024/07/24 09:49:35.024 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000006AFF0000000000000000F7 lock_version: 451363359946178562 key: 748000FFFFFFFFFFFE5F72800000000000006A lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451363359946178563"]
   > [2024/07/24 09:49:35.025 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000006AFF0000000000000000F7 lock_version: 451363359946178562 key: 748000FFFFFFFFFFFE5F72800000000000006A lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451363359946178563"]
   > [2024/07/24 09:49:35.026 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:57862] [split_keys="key 7480000000000000FF6900000000000000F8"] [peer_id=11] [region_id=10]
   > [2024/07/24 09:49:35.027 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=90] [peer-ids="[91]"]
   > [2024/07/24 09:49:35.027 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 10 start_key: 7480000000000000FF6300000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 44 } peers { id: 11 store_id: 1 }"] [new_region_ids="[new_region_id: 90 new_peer_ids: 91]"] [region_id=10]
   > [2024/07/24 09:49:35.031 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000006AFF0000000000000000F7 lock_version: 451363359946178562 key: 748000FFFFFFFFFFFE5F72800000000000006A lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451363359946178563"]
   > [2024/07/24 09:49:35.031 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000006AFF0000000000000000F7 lock_version: 451363359946178562 key: 748000FFFFFFFFFFFE5F72800000000000006A lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451363359946178563"]
   > [2024/07/24 09:49:35.035 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF6900000000000000F8 new_region_id: 90 new_peer_ids: 91 } right_derive: true }"] [index=81] [term=6] [peer_id=11] [region_id=10]
   > [2024/07/24 09:49:35.035 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF6900000000000000F8"] [region="id: 10 start_key: 7480000000000000FF6300000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 44 } peers { id: 11 store_id: 1 }"] [peer_id=11] [region_id=10]
   > [2024/07/24 09:49:35.042 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/24 09:49:35.042 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=10]
   > [2024/07/24 09:49:35.042 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(85)] [region_id=10] [store_id=Some(1)]
   > [2024/07/24 09:49:35.042 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 10 start_key: 7480000000000000FF6900000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 45 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 09:49:35.042 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=10] ["first at"=748000000000000069] ["first new region left"="{Id:90 StartKey:7480000000000000ff6300000000000000f8 EndKey:7480000000000000ff6900000000000000f8 RegionEpoch:{ConfVer:1 Version:45} Peers:[id:91 store_id:1 ] EncryptionMeta:<nil> IsInFlashback:false}"] ["new region count"=1]
   > [2024/07/24 09:49:35.042 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=11] [region_id=10]
   > [2024/07/24 09:49:35.042 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[90]"]
   > [2024/07/24 09:49:35.042 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 90 start_key: 7480000000000000FF6300000000000000F8 end_key: 7480000000000000FF6900000000000000F8 region_epoch { conf_ver: 1 version: 45 } peers { id: 91 store_id: 1 }"] [region_id=90]
   > [2024/07/24 09:49:35.042 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=10] [detail="StartKey Changed:{7480000000000000FF6300000000000000F8} -> {7480000000000000FF6900000000000000F8}, EndKey:{748000FFFFFFFFFFFFFB00000000000000F8}"] [old-version=44] [new-version=45]
   > [2024/07/24 09:49:35.042 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=91] [region_id=90]
   > [2024/07/24 09:49:35.042 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 10 start_key: 7480000000000000FF6900000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 45 } peers { id: 11 store_id: 1 } }"]
   > [2024/07/24 09:49:35.042 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=10] [origin="id:90 start_key:\"7480000000000000FF6300000000000000F8\" end_key:\"7480000000000000FF6900000000000000F8\" region_epoch:<conf_ver:1 version:45 > peers:<id:91 store_id:1 >"] [total=1]
   > [2024/07/24 09:49:35.042 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 10 start_key: 7480000000000000FF6900000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 45 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 09:49:35.043 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {91} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=91] [region_id=90]
   > [2024/07/24 09:49:35.043 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=91] [region_id=90]
   > [2024/07/24 09:49:35.043 +00:00] [WARN] [2pc.go:1873] ["schemaLeaseChecker is not set for this transaction"] [sessionID=4672033813629501867] [startTS=451363359946178569] [checkTS=451363359959023618]
   > [2024/07/24 09:49:35.043 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {91} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=91] [region_id=90]
   > [2024/07/24 09:49:35.043 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 91."] [id=91] [raft_id=91] [region_id=90]
   > [2024/07/24 09:49:35.043 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=91] [region_id=90]
   > [2024/07/24 09:49:35.043 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=91] [region_id=90]
   > [2024/07/24 09:49:35.043 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=91] [region_id=90]
   > [2024/07/24 09:49:35.043 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=91] [region_id=90]
   > [2024/07/24 09:49:35.043 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803866] [region_id=90]
   > [2024/07/24 09:49:35.044 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=81] [observe_id=ObserveId(87)] [region=10]
   > [2024/07/24 09:49:35.044 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=90]
   > [2024/07/24 09:49:35.047 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 90 start_key: 7480000000000000FF6300000000000000F8 end_key: 7480000000000000FF6900000000000000F8 region_epoch { conf_ver: 1 version: 45 } peers { id: 91 store_id: 1 }"]
   > [2024/07/24 09:49:35.047 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(88)] [region=90]
   > [2024/07/24 09:49:35.051 +00:00] [INFO] [scheduler.rs:640] ["get snapshot failed"] [err="Error(Request(message: \"EpochNotMatch current epoch of region 10 is conf_ver: 1 version: 45, but you sent conf_ver: 1 version: 44\" epoch_not_match { current_regions { id: 10 start_key: 7480000000000000FF6900000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 45 } peers { id: 11 store_id: 1 } } current_regions { id: 90 start_key: 7480000000000000FF6300000000000000F8 end_key: 7480000000000000FF6900000000000000F8 region_epoch { conf_ver: 1 version: 45 } peers { id: 91 store_id: 1 } } }))"] [cid=1658]
   > [2024/07/24 09:49:36.072 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/24 09:49:36.154 +00:00] [INFO] [set.go:141] ["set global var"] [conn=4672033813629501869] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/07/24 09:49:36.681 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/24 09:49:39.034 +00:00] [WARN] [grpclog.go:60] ["transport: http2Server.HandleStreams failed to read frame: read tcp 127.0.0.1:2379->127.0.0.1:41550: read: connection reset by peer"]

### Scenario 1
 * Instruction #0:
     - Instruction:  SELECT /*+ INL_JOIN(t)*/c1 FROM t WHERE c2<=c1 FOR UPDATE;
     - Transaction: conn_0
     - Output: [(1,)]
     - Executed order: 0
     - Affected rows: 1
     - Warnings: [('Warning', 1815, 'There are no matching table names for (t) in optimizer hint /*+ INL_JOIN(t) */ or /*+ TIDB_INLJ(t) */. Maybe you can use the table alias name')]

 * Container logs:
   > [2024/07/24 09:49:41.087 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/24 09:49:41.090 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=4672033813629501875] [schemaVersion=83] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/24 09:49:41.125 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:113, Type:drop schema, State:queueing, SchemaState:public, SchemaID:108, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 09:49:41.09 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 09:49:41.125 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:113, Type:drop schema, State:queueing, SchemaState:public, SchemaID:108, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 09:49:41.09 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/24 09:49:41.145 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:113, Type:drop schema, State:queueing, SchemaState:public, SchemaID:108, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:41.09 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:41.187 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=83] [neededSchemaVersion=84] ["start time"=756.809µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 09:49:41.236 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=84] ["take time"=56.693703ms] [job="ID:113, Type:drop schema, State:running, SchemaState:write only, SchemaID:108, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:41.09 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:41.241 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:113, Type:drop schema, State:running, SchemaState:write only, SchemaID:108, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:41.09 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:41.283 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=84] [neededSchemaVersion=85] ["start time"=851.096µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 09:49:41.331 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=85] ["take time"=56.566452ms] [job="ID:113, Type:drop schema, State:running, SchemaState:delete only, SchemaID:108, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:41.09 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:41.336 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:113, Type:drop schema, State:running, SchemaState:delete only, SchemaID:108, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:41.09 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:41.377 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=85] [neededSchemaVersion=86] ["start time"=761.139µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 09:49:41.426 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=86] ["take time"=56.504083ms] [job="ID:113, Type:drop schema, State:done, SchemaState:none, SchemaID:108, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:41.09 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:41.431 +00:00] [INFO] [delete_range.go:109] ["[ddl] add job into delete-range table"] [jobID=113] [jobType="drop schema"]
   > [2024/07/24 09:49:41.432 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:113, Type:drop schema, State:synced, SchemaState:none, SchemaID:108, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:41.09 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:41.451 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=113]
   > [2024/07/24 09:49:41.451 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 09:49:41.452 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000071FF0000000000000000F7 lock_version: 451363361623900162 key: 748000FFFFFFFFFFFE5F728000000000000071 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451363361623900163"]
   > [2024/07/24 09:49:41.452 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000071FF0000000000000000F7 lock_version: 451363361623900162 key: 748000FFFFFFFFFFFE5F728000000000000071 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451363361623900163"]
   > [2024/07/24 09:49:41.454 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=4672033813629501875] [schemaVersion=86] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/24 09:49:41.495 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:115, Type:create schema, State:queueing, SchemaState:none, SchemaID:114, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 09:49:41.44 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 09:49:41.495 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:115, Type:create schema, State:queueing, SchemaState:none, SchemaID:114, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 09:49:41.44 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/24 09:49:41.514 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:115, Type:create schema, State:queueing, SchemaState:none, SchemaID:114, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:41.44 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:41.554 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=86] [neededSchemaVersion=87] ["start time"=1.81352ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 09:49:41.608 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=87] ["take time"=63.151096ms] [job="ID:115, Type:create schema, State:done, SchemaState:public, SchemaID:114, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 09:49:41.44 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:41.614 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:115, Type:create schema, State:synced, SchemaState:public, SchemaID:114, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:41.44 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:41.632 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=115]
   > [2024/07/24 09:49:41.632 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 09:49:41.633 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000073FF0000000000000000F7 lock_version: 451363361676328962 key: 748000FFFFFFFFFFFE5F728000000000000073 lock_ttl: 3003 txn_size: 1 lock_type: Del min_commit_ts: 451363361676328963"]
   > [2024/07/24 09:49:41.633 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000073FF0000000000000000F7 lock_version: 451363361676328962 key: 748000FFFFFFFFFFFE5F728000000000000073 lock_ttl: 3003 txn_size: 1 lock_type: Del min_commit_ts: 451363361676328963"]
   > [2024/07/24 09:49:41.637 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=4672033813629501875] [schemaVersion=87] [cur_db=testdb] [sql="CREATE TABLE t (c1 INT, c2 INT);"] [user=root@%]
   > [2024/07/24 09:49:41.675 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:117, Type:create table, State:queueing, SchemaState:none, SchemaID:114, TableID:116, RowCount:0, ArgLen:2, start time: 2024-07-24 09:49:41.64 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 09:49:41.675 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:117, Type:create table, State:queueing, SchemaState:none, SchemaID:114, TableID:116, RowCount:0, ArgLen:2, start time: 2024-07-24 09:49:41.64 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE t (c1 INT, c2 INT);"]
   > [2024/07/24 09:49:41.695 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:117, Type:create table, State:queueing, SchemaState:none, SchemaID:114, TableID:116, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:41.64 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:41.738 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=87] [neededSchemaVersion=88] ["start time"=2.488335ms] [phyTblIDs="[116]"] [actionTypes="[8]"]
   > [2024/07/24 09:49:41.785 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=88] ["take time"=58.096483ms] [job="ID:117, Type:create table, State:done, SchemaState:public, SchemaID:114, TableID:116, RowCount:0, ArgLen:2, start time: 2024-07-24 09:49:41.64 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:41.792 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:117, Type:create table, State:synced, SchemaState:public, SchemaID:114, TableID:116, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:41.64 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:41.811 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=117]
   > [2024/07/24 09:49:41.811 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 09:49:41.811 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=10] ["first split key"=748000000000000074]
   > [2024/07/24 09:49:41.812 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000075FF0000000000000000F7 lock_version: 451363361728757761 key: 748000FFFFFFFFFFFE5F728000000000000075 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451363361728757762"]
   > [2024/07/24 09:49:41.812 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000075FF0000000000000000F7 lock_version: 451363361728757761 key: 748000FFFFFFFFFFFE5F728000000000000075 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451363361728757762"]
   > [2024/07/24 09:49:41.815 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:57880] [split_keys="key 7480000000000000FF7400000000000000F8"] [peer_id=11] [region_id=10]
   > [2024/07/24 09:49:41.816 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=94] [peer-ids="[95]"]
   > [2024/07/24 09:49:41.816 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 10 start_key: 7480000000000000FF6E00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 46 } peers { id: 11 store_id: 1 }"] [new_region_ids="[new_region_id: 94 new_peer_ids: 95]"] [region_id=10]
   > [2024/07/24 09:49:41.818 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000075FF0000000000000000F7 lock_version: 451363361728757761 key: 748000FFFFFFFFFFFE5F728000000000000075 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451363361728757762"]
   > [2024/07/24 09:49:41.818 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000075FF0000000000000000F7 lock_version: 451363361728757761 key: 748000FFFFFFFFFFFE5F728000000000000075 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451363361728757762"]
   > [2024/07/24 09:49:41.825 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF7400000000000000F8 new_region_id: 94 new_peer_ids: 95 } right_derive: true }"] [index=88] [term=6] [peer_id=11] [region_id=10]
   > [2024/07/24 09:49:41.825 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF7400000000000000F8"] [region="id: 10 start_key: 7480000000000000FF6E00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 46 } peers { id: 11 store_id: 1 }"] [peer_id=11] [region_id=10]
   > [2024/07/24 09:49:41.832 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/24 09:49:41.832 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=10]
   > [2024/07/24 09:49:41.832 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(89)] [region_id=10] [store_id=Some(1)]
   > [2024/07/24 09:49:41.832 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 10 start_key: 7480000000000000FF7400000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 47 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 09:49:41.832 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=11] [region_id=10]
   > [2024/07/24 09:49:41.832 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=10] [detail="StartKey Changed:{7480000000000000FF6E00000000000000F8} -> {7480000000000000FF7400000000000000F8}, EndKey:{748000FFFFFFFFFFFFFB00000000000000F8}"] [old-version=46] [new-version=47]
   > [2024/07/24 09:49:41.832 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=10] ["first at"=748000000000000074] ["first new region left"="{Id:94 StartKey:7480000000000000ff6e00000000000000f8 EndKey:7480000000000000ff7400000000000000f8 RegionEpoch:{ConfVer:1 Version:47} Peers:[id:95 store_id:1 ] EncryptionMeta:<nil> IsInFlashback:false}"] ["new region count"=1]
   > [2024/07/24 09:49:41.832 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 94 start_key: 7480000000000000FF6E00000000000000F8 end_key: 7480000000000000FF7400000000000000F8 region_epoch { conf_ver: 1 version: 47 } peers { id: 95 store_id: 1 }"] [region_id=94]
   > [2024/07/24 09:49:41.832 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[94]"]
   > [2024/07/24 09:49:41.832 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=95] [region_id=94]
   > [2024/07/24 09:49:41.832 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 10 start_key: 7480000000000000FF7400000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 47 } peers { id: 11 store_id: 1 } }"]
   > [2024/07/24 09:49:41.832 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=10] [origin="id:94 start_key:\"7480000000000000FF6E00000000000000F8\" end_key:\"7480000000000000FF7400000000000000F8\" region_epoch:<conf_ver:1 version:47 > peers:<id:95 store_id:1 >"] [total=1]
   > [2024/07/24 09:49:41.832 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 10 start_key: 7480000000000000FF7400000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 47 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 09:49:41.832 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {95} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=95] [region_id=94]
   > [2024/07/24 09:49:41.832 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=95] [region_id=94]
   > [2024/07/24 09:49:41.833 +00:00] [WARN] [2pc.go:1873] ["schemaLeaseChecker is not set for this transaction"] [sessionID=4672033813629501875] [startTS=451363361728757768] [checkTS=451363361728757771]
   > [2024/07/24 09:49:41.833 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {95} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=95] [region_id=94]
   > [2024/07/24 09:49:41.833 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 95."] [id=95] [raft_id=95] [region_id=94]
   > [2024/07/24 09:49:41.833 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=95] [region_id=94]
   > [2024/07/24 09:49:41.833 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=95] [region_id=94]
   > [2024/07/24 09:49:41.833 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=95] [region_id=94]
   > [2024/07/24 09:49:41.833 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=95] [region_id=94]
   > [2024/07/24 09:49:41.833 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803870] [region_id=94]
   > [2024/07/24 09:49:41.833 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=94]
   > [2024/07/24 09:49:41.836 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 94 start_key: 7480000000000000FF6E00000000000000F8 end_key: 7480000000000000FF7400000000000000F8 region_epoch { conf_ver: 1 version: 47 } peers { id: 95 store_id: 1 }"]
   > [2024/07/24 09:49:41.836 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=88] [observe_id=ObserveId(91)] [region=10]
   > [2024/07/24 09:49:41.836 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(92)] [region=94]
   > [2024/07/24 09:49:41.841 +00:00] [INFO] [scheduler.rs:640] ["get snapshot failed"] [err="Error(Request(message: \"EpochNotMatch current epoch of region 10 is conf_ver: 1 version: 47, but you sent conf_ver: 1 version: 46\" epoch_not_match { current_regions { id: 10 start_key: 7480000000000000FF7400000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 47 } peers { id: 11 store_id: 1 } } current_regions { id: 94 start_key: 7480000000000000FF6E00000000000000F8 end_key: 7480000000000000FF7400000000000000F8 region_epoch { conf_ver: 1 version: 47 } peers { id: 95 store_id: 1 } } }))"] [cid=1894]
   > [2024/07/24 09:49:42.860 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]

### Scenario 2
 * Instruction #0:
     - Instruction:  BEGIN;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows: 0
 * Instruction #1:
     - Instruction:  SELECT /*+ INL_JOIN(t)*/c1 FROM t WHERE c2<=c1 FOR UPDATE;
     - Transaction: conn_0
     - Output: [(1,)]
     - Executed order: 1
     - Affected rows: 1
     - Warnings: [('Warning', 1815, 'There are no matching table names for (t) in optimizer hint /*+ INL_JOIN(t) */ or /*+ TIDB_INLJ(t) */. Maybe you can use the table alias name')]

 * Container logs:
   > [2024/07/24 09:49:46.203 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/24 09:49:46.206 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=4672033813629501881] [schemaVersion=96] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/24 09:49:46.235 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:124, Type:drop schema, State:queueing, SchemaState:public, SchemaID:119, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 09:49:46.19 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 09:49:46.235 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:124, Type:drop schema, State:queueing, SchemaState:public, SchemaID:119, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 09:49:46.19 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/24 09:49:46.257 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:124, Type:drop schema, State:queueing, SchemaState:public, SchemaID:119, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:46.19 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:46.293 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=96] [neededSchemaVersion=97] ["start time"=773.361µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 09:49:46.342 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=97] ["take time"=56.367751ms] [job="ID:124, Type:drop schema, State:running, SchemaState:write only, SchemaID:119, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:46.19 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:46.347 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:124, Type:drop schema, State:running, SchemaState:write only, SchemaID:119, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:46.19 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:46.385 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=97] [neededSchemaVersion=98] ["start time"=742.841µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 09:49:46.434 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=98] ["take time"=57.425369ms] [job="ID:124, Type:drop schema, State:running, SchemaState:delete only, SchemaID:119, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:46.19 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:46.439 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:124, Type:drop schema, State:running, SchemaState:delete only, SchemaID:119, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:46.19 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:46.477 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=98] [neededSchemaVersion=99] ["start time"=815.406µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 09:49:46.526 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=99] ["take time"=55.838208ms] [job="ID:124, Type:drop schema, State:done, SchemaState:none, SchemaID:119, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:46.19 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:46.532 +00:00] [INFO] [delete_range.go:109] ["[ddl] add job into delete-range table"] [jobID=124] [jobType="drop schema"]
   > [2024/07/24 09:49:46.533 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:124, Type:drop schema, State:synced, SchemaState:none, SchemaID:119, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:46.19 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:46.552 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=124]
   > [2024/07/24 09:49:46.552 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 09:49:46.553 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000007CFF0000000000000000F7 lock_version: 451363362960834562 key: 748000FFFFFFFFFFFE5F72800000000000007C lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451363362960834563"]
   > [2024/07/24 09:49:46.553 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000007CFF0000000000000000F7 lock_version: 451363362960834562 key: 748000FFFFFFFFFFFE5F72800000000000007C lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451363362960834563"]
   > [2024/07/24 09:49:46.556 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=4672033813629501881] [schemaVersion=99] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/24 09:49:46.596 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:126, Type:create schema, State:queueing, SchemaState:none, SchemaID:125, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 09:49:46.54 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 09:49:46.597 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:126, Type:create schema, State:queueing, SchemaState:none, SchemaID:125, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 09:49:46.54 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/24 09:49:46.615 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:126, Type:create schema, State:queueing, SchemaState:none, SchemaID:125, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:46.54 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:46.653 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=99] [neededSchemaVersion=100] ["start time"=1.359477ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 09:49:46.706 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=100] ["take time"=62.599483ms] [job="ID:126, Type:create schema, State:done, SchemaState:public, SchemaID:125, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 09:49:46.54 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:46.712 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:126, Type:create schema, State:synced, SchemaState:public, SchemaID:125, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:46.54 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:46.730 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=126]
   > [2024/07/24 09:49:46.730 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 09:49:46.731 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000007EFF0000000000000000F7 lock_version: 451363363013263362 key: 748000FFFFFFFFFFFE5F72800000000000007E lock_ttl: 3003 txn_size: 1 lock_type: Del min_commit_ts: 451363363013263363"]
   > [2024/07/24 09:49:46.731 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000007EFF0000000000000000F7 lock_version: 451363363013263362 key: 748000FFFFFFFFFFFE5F72800000000000007E lock_ttl: 3003 txn_size: 1 lock_type: Del min_commit_ts: 451363363013263363"]
   > [2024/07/24 09:49:46.735 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=4672033813629501881] [schemaVersion=100] [cur_db=testdb] [sql="CREATE TABLE t (c1 INT, c2 INT);"] [user=root@%]
   > [2024/07/24 09:49:46.773 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:128, Type:create table, State:queueing, SchemaState:none, SchemaID:125, TableID:127, RowCount:0, ArgLen:2, start time: 2024-07-24 09:49:46.74 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 09:49:46.774 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:128, Type:create table, State:queueing, SchemaState:none, SchemaID:125, TableID:127, RowCount:0, ArgLen:2, start time: 2024-07-24 09:49:46.74 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE t (c1 INT, c2 INT);"]
   > [2024/07/24 09:49:46.794 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:128, Type:create table, State:queueing, SchemaState:none, SchemaID:125, TableID:127, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:46.74 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:46.838 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=100] [neededSchemaVersion=101] ["start time"=2.23837ms] [phyTblIDs="[127]"] [actionTypes="[8]"]
   > [2024/07/24 09:49:46.885 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=101] ["take time"=57.624419ms] [job="ID:128, Type:create table, State:done, SchemaState:public, SchemaID:125, TableID:127, RowCount:0, ArgLen:2, start time: 2024-07-24 09:49:46.74 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:46.891 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:128, Type:create table, State:synced, SchemaState:public, SchemaID:125, TableID:127, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:46.74 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:46.914 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=128]
   > [2024/07/24 09:49:46.914 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 09:49:46.914 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=10] ["first split key"=74800000000000007f]
   > [2024/07/24 09:49:46.915 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000080FF0000000000000000F7 lock_version: 451363363065692161 key: 748000FFFFFFFFFFFE5F728000000000000080 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451363363065692162"]
   > [2024/07/24 09:49:46.915 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000080FF0000000000000000F7 lock_version: 451363363065692161 key: 748000FFFFFFFFFFFE5F728000000000000080 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451363363065692162"]
   > [2024/07/24 09:49:46.918 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:57880] [split_keys="key 7480000000000000FF7F00000000000000F8"] [peer_id=11] [region_id=10]
   > [2024/07/24 09:49:46.918 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=98] [peer-ids="[99]"]
   > [2024/07/24 09:49:46.919 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 10 start_key: 7480000000000000FF7900000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 48 } peers { id: 11 store_id: 1 }"] [new_region_ids="[new_region_id: 98 new_peer_ids: 99]"] [region_id=10]
   > [2024/07/24 09:49:46.925 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF7F00000000000000F8 new_region_id: 98 new_peer_ids: 99 } right_derive: true }"] [index=92] [term=6] [peer_id=11] [region_id=10]
   > [2024/07/24 09:49:46.925 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF7F00000000000000F8"] [region="id: 10 start_key: 7480000000000000FF7900000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 48 } peers { id: 11 store_id: 1 }"] [peer_id=11] [region_id=10]
   > [2024/07/24 09:49:46.932 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=10]
   > [2024/07/24 09:49:46.932 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/24 09:49:46.932 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(93)] [region_id=10] [store_id=Some(1)]
   > [2024/07/24 09:49:46.932 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=10] [detail="StartKey Changed:{7480000000000000FF7900000000000000F8} -> {7480000000000000FF7F00000000000000F8}, EndKey:{748000FFFFFFFFFFFFFB00000000000000F8}"] [old-version=48] [new-version=49]
   > [2024/07/24 09:49:46.932 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=10] ["first at"=74800000000000007f] ["first new region left"="{Id:98 StartKey:7480000000000000ff7900000000000000f8 EndKey:7480000000000000ff7f00000000000000f8 RegionEpoch:{ConfVer:1 Version:49} Peers:[id:99 store_id:1 ] EncryptionMeta:<nil> IsInFlashback:false}"] ["new region count"=1]
   > [2024/07/24 09:49:46.932 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[98]"]
   > [2024/07/24 09:49:46.932 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 10 start_key: 7480000000000000FF7F00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 49 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 09:49:46.932 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=11] [region_id=10]
   > [2024/07/24 09:49:46.932 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 98 start_key: 7480000000000000FF7900000000000000F8 end_key: 7480000000000000FF7F00000000000000F8 region_epoch { conf_ver: 1 version: 49 } peers { id: 99 store_id: 1 }"] [region_id=98]
   > [2024/07/24 09:49:46.932 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=99] [region_id=98]
   > [2024/07/24 09:49:46.932 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 10 start_key: 7480000000000000FF7F00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 49 } peers { id: 11 store_id: 1 } }"]
   > [2024/07/24 09:49:46.932 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 10 start_key: 7480000000000000FF7F00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 49 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 09:49:46.932 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=10] [origin="id:98 start_key:\"7480000000000000FF7900000000000000F8\" end_key:\"7480000000000000FF7F00000000000000F8\" region_epoch:<conf_ver:1 version:49 > peers:<id:99 store_id:1 >"] [total=1]
   > [2024/07/24 09:49:46.933 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {99} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=99] [region_id=98]
   > [2024/07/24 09:49:46.933 +00:00] [WARN] [2pc.go:1873] ["schemaLeaseChecker is not set for this transaction"] [sessionID=4672033813629501881] [startTS=451363363065692168] [checkTS=451363363065692170]
   > [2024/07/24 09:49:46.933 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=99] [region_id=98]
   > [2024/07/24 09:49:46.933 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {99} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=99] [region_id=98]
   > [2024/07/24 09:49:46.933 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 99."] [id=99] [raft_id=99] [region_id=98]
   > [2024/07/24 09:49:46.933 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=99] [region_id=98]
   > [2024/07/24 09:49:46.933 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=99] [region_id=98]
   > [2024/07/24 09:49:46.933 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=99] [region_id=98]
   > [2024/07/24 09:49:46.933 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=99] [region_id=98]
   > [2024/07/24 09:49:46.933 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803874] [region_id=98]
   > [2024/07/24 09:49:46.933 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=98]
   > [2024/07/24 09:49:46.936 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 98 start_key: 7480000000000000FF7900000000000000F8 end_key: 7480000000000000FF7F00000000000000F8 region_epoch { conf_ver: 1 version: 49 } peers { id: 99 store_id: 1 }"]
   > [2024/07/24 09:49:46.936 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=92] [observe_id=ObserveId(95)] [region=10]
   > [2024/07/24 09:49:46.936 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(96)] [region=98]
   > [2024/07/24 09:49:46.941 +00:00] [INFO] [scheduler.rs:640] ["get snapshot failed"] [err="Error(Request(message: \"EpochNotMatch current epoch of region 10 is conf_ver: 1 version: 49, but you sent conf_ver: 1 version: 48\" epoch_not_match { current_regions { id: 10 start_key: 7480000000000000FF7F00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 49 } peers { id: 11 store_id: 1 } } current_regions { id: 98 start_key: 7480000000000000FF7900000000000000F8 end_key: 7480000000000000FF7F00000000000000F8 region_epoch { conf_ver: 1 version: 49 } peers { id: 99 store_id: 1 } } }))"] [cid=2118]
   > [2024/07/24 09:49:47.960 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
