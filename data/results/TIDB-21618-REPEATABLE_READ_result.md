# Bug ID TIDB-21618-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/21618
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              pessimistic lock doesn't work on the partition for subquery/joins


## Details
 * Database: tidb-v6.4.0.tikv
 * Number of scenarios: 1
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
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
     - Instruction:  select * from t where d_int in (select d_int from t where c_int = 1) for update...
     - Transaction: conn_0
     - Output: [(1, 2)]
     - Executed order: 2
     - Affected rows: 1
     - Warnings: [('Warning', 1105, 'disable dynamic pruning due to t has no global stats'), ('Warning', 1105, 'disable dynamic pruning due to t has no global stats')]
 * Instruction #3:
     - Instruction:  begin pessimistic;
     - Transaction: conn_1
     - Output: None
     - Executed order: 3
     - Affected rows: 0
 * Instruction #4:
     - Instruction:  select * from t where d_int = 2 for update;
     - Transaction: conn_1
     - Output: [(1, 2)]
     - Executed order: 4
     - Affected rows: 1
     - Warnings: [('Warning', 1105, 'disable dynamic pruning due to t has no global stats')]
 * Instruction #5:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 5
     - Affected rows: 0
 * Instruction #6:
     - Instruction:  COMMIT;
     - Transaction: conn_1
     - Output: None
     - Executed order: 6
     - Affected rows: 0

 * Container logs:
   > [2024/07/24 12:12:14.528 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/24 12:12:14.531 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=6993195218841371031] [schemaVersion=34] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/24 12:12:14.533 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=6993195218841371031] [schemaVersion=34] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/24 12:12:14.585 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 748000FFFFFFFFFFFE5F728000000000000047 lock_version: 451365603778494476 key: 748000FFFFFFFFFFFE5F728000000000000047 lock_ttl: 3000 txn_size: 1 min_commit_ts: 451365603778494477"]
   > [2024/07/24 12:12:14.585 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 748000FFFFFFFFFFFE5F728000000000000047 lock_version: 451365603778494476 key: 748000FFFFFFFFFFFE5F728000000000000047 lock_ttl: 3000 txn_size: 1 min_commit_ts: 451365603778494477"]
   > [2024/07/24 12:12:14.595 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:71, Type:create schema, State:queueing, SchemaState:none, SchemaID:70, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:12:14.531 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 12:12:14.595 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:71, Type:create schema, State:queueing, SchemaState:none, SchemaID:70, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:12:14.531 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/24 12:12:14.622 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:71, Type:create schema, State:queueing, SchemaState:none, SchemaID:70, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:12:14.531 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:12:14.672 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=34] [neededSchemaVersion=35] ["start time"=1.470733ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:12:14.720 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=35] ["take time"=57.386306ms] [job="ID:71, Type:create schema, State:done, SchemaState:public, SchemaID:70, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:12:14.531 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:12:14.726 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:71, Type:create schema, State:synced, SchemaState:public, SchemaID:70, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:12:14.531 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:12:14.750 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=71]
   > [2024/07/24 12:12:14.750 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 12:12:14.751 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000047FF0000000000000000F7 lock_version: 451365603818078211 key: 748000FFFFFFFFFFFE5F728000000000000047 lock_ttl: 3003 txn_size: 1 lock_type: Del min_commit_ts: 451365603818078212"]
   > [2024/07/24 12:12:14.752 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000047FF0000000000000000F7 lock_version: 451365603818078211 key: 748000FFFFFFFFFFFE5F728000000000000047 lock_ttl: 3003 txn_size: 1 lock_type: Del min_commit_ts: 451365603818078212"]
   > [2024/07/24 12:12:14.756 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=6993195218841371031] [schemaVersion=35] [cur_db=testdb] [sql="create table t (c_int int, d_int int, primary key (c_int), key(d_int)) partition by hash (c_int) partitions 4 ;"] [user=root@%]
   > [2024/07/24 12:12:14.827 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:77, Type:create table, State:queueing, SchemaState:none, SchemaID:70, TableID:72, RowCount:0, ArgLen:2, start time: 2024-07-24 12:12:14.781 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 12:12:14.827 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:77, Type:create table, State:queueing, SchemaState:none, SchemaID:70, TableID:72, RowCount:0, ArgLen:2, start time: 2024-07-24 12:12:14.781 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t (c_int int, d_int int, primary key (c_int), key(d_int)) partition by hash (c_int) partitions 4 ;"]
   > [2024/07/24 12:12:14.851 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:77, Type:create table, State:queueing, SchemaState:none, SchemaID:70, TableID:72, RowCount:0, ArgLen:0, start time: 2024-07-24 12:12:14.781 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:12:14.912 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=35] [neededSchemaVersion=36] ["start time"=2.449429ms] [phyTblIDs="[72,73,74,75,76]"] [actionTypes="[8,8,8,8,8]"]
   > [2024/07/24 12:12:14.959 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=36] ["take time"=61.351166ms] [job="ID:77, Type:create table, State:done, SchemaState:public, SchemaID:70, TableID:72, RowCount:0, ArgLen:2, start time: 2024-07-24 12:12:14.781 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:12:14.966 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:77, Type:create table, State:synced, SchemaState:public, SchemaID:70, TableID:72, RowCount:0, ArgLen:0, start time: 2024-07-24 12:12:14.781 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:12:14.992 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=77]
   > [2024/07/24 12:12:14.992 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 12:12:14.992 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=10] ["first split key"=748000000000000049]
   > [2024/07/24 12:12:14.993 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000004DFF0000000000000000F7 lock_version: 451365603883614212 key: 748000FFFFFFFFFFFE5F72800000000000004D lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451365603883614213"]
   > [2024/07/24 12:12:14.993 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000004DFF0000000000000000F7 lock_version: 451365603883614212 key: 748000FFFFFFFFFFFE5F72800000000000004D lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451365603883614213"]
   > [2024/07/24 12:12:14.995 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:60178] [split_keys="key 7480000000000000FF4900000000000000F8"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:14.995 +00:00] [INFO] [peer.rs:5566] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 37"] [prev_epoch="conf_ver: 1 version: 38"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:14.998 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000004DFF0000000000000000F7 lock_version: 451365603883614212 key: 748000FFFFFFFFFFFE5F72800000000000004D lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451365603883614213"]
   > [2024/07/24 12:12:14.998 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000004DFF0000000000000000F7 lock_version: 451365603883614212 key: 748000FFFFFFFFFFFE5F72800000000000004D lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451365603883614213"]
   > [2024/07/24 12:12:15.006 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:60142] [split_keys="key 7480000000000000FF4900000000000000F8"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:15.007 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=78] [peer-ids="[79]"]
   > [2024/07/24 12:12:15.007 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 10 start_key: 7480000000000000FF4400000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 38 } peers { id: 11 store_id: 1 }"] [new_region_ids="[new_region_id: 78 new_peer_ids: 79]"] [region_id=10]
   > [2024/07/24 12:12:15.028 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF4900000000000000F8 new_region_id: 78 new_peer_ids: 79 } right_derive: true }"] [index=66] [term=6] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:15.028 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF4900000000000000F8"] [region="id: 10 start_key: 7480000000000000FF4400000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 38 } peers { id: 11 store_id: 1 }"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:15.038 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/24 12:12:15.038 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=10]
   > [2024/07/24 12:12:15.038 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:15.038 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(73)] [region_id=10] [store_id=Some(1)]
   > [2024/07/24 12:12:15.038 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 78 start_key: 7480000000000000FF4400000000000000F8 end_key: 7480000000000000FF4900000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 79 store_id: 1 }"] [region_id=78]
   > [2024/07/24 12:12:15.038 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=10] ["first at"=748000000000000049] ["first new region left"="{Id:78 StartKey:7480000000000000ff4400000000000000f8 EndKey:7480000000000000ff4900000000000000f8 RegionEpoch:{ConfVer:1 Version:39} Peers:[id:79 store_id:1 ] EncryptionMeta:<nil> IsInFlashback:false}"] ["new region count"=1]
   > [2024/07/24 12:12:15.038 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=79] [region_id=78]
   > [2024/07/24 12:12:15.038 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[78]"]
   > [2024/07/24 12:12:15.038 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=10] ["first split key"=74800000000000004a]
   > [2024/07/24 12:12:15.038 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 10 start_key: 7480000000000000FF4900000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 12:12:15.038 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 10 start_key: 7480000000000000FF4900000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 11 store_id: 1 } }"]
   > [2024/07/24 12:12:15.038 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=10] [detail="StartKey Changed:{7480000000000000FF4400000000000000F8} -> {7480000000000000FF4900000000000000F8}, EndKey:{748000FFFFFFFFFFFFFB00000000000000F8}"] [old-version=38] [new-version=39]
   > [2024/07/24 12:12:15.038 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 10 start_key: 7480000000000000FF4900000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 12:12:15.038 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=10] [origin="id:78 start_key:\"7480000000000000FF4400000000000000F8\" end_key:\"7480000000000000FF4900000000000000F8\" region_epoch:<conf_ver:1 version:39 > peers:<id:79 store_id:1 >"] [total=1]
   > [2024/07/24 12:12:15.043 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {79} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=79] [region_id=78]
   > [2024/07/24 12:12:15.043 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=79] [region_id=78]
   > [2024/07/24 12:12:15.043 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {79} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=79] [region_id=78]
   > [2024/07/24 12:12:15.043 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 79."] [id=79] [raft_id=79] [region_id=78]
   > [2024/07/24 12:12:15.044 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=79] [region_id=78]
   > [2024/07/24 12:12:15.044 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=79] [region_id=78]
   > [2024/07/24 12:12:15.044 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=79] [region_id=78]
   > [2024/07/24 12:12:15.044 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=79] [region_id=78]
   > [2024/07/24 12:12:15.044 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803854] [region_id=78]
   > [2024/07/24 12:12:15.044 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=78]
   > [2024/07/24 12:12:15.049 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:60164] [split_keys="key 7480000000000000FF4A00000000000000F8"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:15.049 +00:00] [INFO] [peer.rs:5566] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 38"] [prev_epoch="conf_ver: 1 version: 39"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:15.050 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=66] [observe_id=ObserveId(75)] [region=10]
   > [2024/07/24 12:12:15.050 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 78 start_key: 7480000000000000FF4400000000000000F8 end_key: 7480000000000000FF4900000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 79 store_id: 1 }"]
   > [2024/07/24 12:12:15.050 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(76)] [region=78]
   > [2024/07/24 12:12:15.053 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:60150] [split_keys="key 7480000000000000FF4A00000000000000F8"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:15.053 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=80] [peer-ids="[81]"]
   > [2024/07/24 12:12:15.054 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 10 start_key: 7480000000000000FF4900000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 11 store_id: 1 }"] [new_region_ids="[new_region_id: 80 new_peer_ids: 81]"] [region_id=10]
   > [2024/07/24 12:12:15.061 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF4A00000000000000F8 new_region_id: 80 new_peer_ids: 81 } right_derive: true }"] [index=67] [term=6] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:15.061 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF4A00000000000000F8"] [region="id: 10 start_key: 7480000000000000FF4900000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 11 store_id: 1 }"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:15.066 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/24 12:12:15.066 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=10]
   > [2024/07/24 12:12:15.066 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(75)] [region_id=10] [store_id=Some(1)]
   > [2024/07/24 12:12:15.066 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 10 start_key: 7480000000000000FF4A00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 40 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 12:12:15.067 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:15.067 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 80 start_key: 7480000000000000FF4900000000000000F8 end_key: 7480000000000000FF4A00000000000000F8 region_epoch { conf_ver: 1 version: 40 } peers { id: 81 store_id: 1 }"] [region_id=80]
   > [2024/07/24 12:12:15.067 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=10] ["first at"=74800000000000004a] ["first new region left"="{Id:80 StartKey:7480000000000000ff4900000000000000f8 EndKey:7480000000000000ff4a00000000000000f8 RegionEpoch:{ConfVer:1 Version:40} Peers:[id:81 store_id:1 ] EncryptionMeta:<nil> IsInFlashback:false}"] ["new region count"=1]
   > [2024/07/24 12:12:15.067 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[80]"]
   > [2024/07/24 12:12:15.067 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=81] [region_id=80]
   > [2024/07/24 12:12:15.067 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=10] ["first split key"=74800000000000004b]
   > [2024/07/24 12:12:15.067 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 10 start_key: 7480000000000000FF4A00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 40 } peers { id: 11 store_id: 1 } }"]
   > [2024/07/24 12:12:15.067 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=10] [detail="StartKey Changed:{7480000000000000FF4900000000000000F8} -> {7480000000000000FF4A00000000000000F8}, EndKey:{748000FFFFFFFFFFFFFB00000000000000F8}"] [old-version=39] [new-version=40]
   > [2024/07/24 12:12:15.067 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 10 start_key: 7480000000000000FF4A00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 40 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 12:12:15.067 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {81} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=81] [region_id=80]
   > [2024/07/24 12:12:15.067 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=10] [origin="id:80 start_key:\"7480000000000000FF4900000000000000F8\" end_key:\"7480000000000000FF4A00000000000000F8\" region_epoch:<conf_ver:1 version:40 > peers:<id:81 store_id:1 >"] [total=1]
   > [2024/07/24 12:12:15.067 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=81] [region_id=80]
   > [2024/07/24 12:12:15.067 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {81} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=81] [region_id=80]
   > [2024/07/24 12:12:15.067 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 81."] [id=81] [raft_id=81] [region_id=80]
   > [2024/07/24 12:12:15.067 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=81] [region_id=80]
   > [2024/07/24 12:12:15.068 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=81] [region_id=80]
   > [2024/07/24 12:12:15.068 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=81] [region_id=80]
   > [2024/07/24 12:12:15.068 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=81] [region_id=80]
   > [2024/07/24 12:12:15.068 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803856] [region_id=80]
   > [2024/07/24 12:12:15.068 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=80]
   > [2024/07/24 12:12:15.073 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:60178] [split_keys="key 7480000000000000FF4B00000000000000F8"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:15.073 +00:00] [INFO] [peer.rs:5566] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 39"] [prev_epoch="conf_ver: 1 version: 40"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:15.073 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=67] [observe_id=ObserveId(77)] [region=10]
   > [2024/07/24 12:12:15.073 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 80 start_key: 7480000000000000FF4900000000000000F8 end_key: 7480000000000000FF4A00000000000000F8 region_epoch { conf_ver: 1 version: 40 } peers { id: 81 store_id: 1 }"]
   > [2024/07/24 12:12:15.073 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(78)] [region=80]
   > [2024/07/24 12:12:15.076 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:60142] [split_keys="key 7480000000000000FF4B00000000000000F8"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:15.077 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=82] [peer-ids="[83]"]
   > [2024/07/24 12:12:15.077 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 10 start_key: 7480000000000000FF4A00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 40 } peers { id: 11 store_id: 1 }"] [new_region_ids="[new_region_id: 82 new_peer_ids: 83]"] [region_id=10]
   > [2024/07/24 12:12:15.083 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF4B00000000000000F8 new_region_id: 82 new_peer_ids: 83 } right_derive: true }"] [index=68] [term=6] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:15.083 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF4B00000000000000F8"] [region="id: 10 start_key: 7480000000000000FF4A00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 40 } peers { id: 11 store_id: 1 }"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:15.089 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/24 12:12:15.089 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=10]
   > [2024/07/24 12:12:15.089 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(77)] [region_id=10] [store_id=Some(1)]
   > [2024/07/24 12:12:15.089 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:15.089 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 10 start_key: 7480000000000000FF4B00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 12:12:15.089 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 82 start_key: 7480000000000000FF4A00000000000000F8 end_key: 7480000000000000FF4B00000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 83 store_id: 1 }"] [region_id=82]
   > [2024/07/24 12:12:15.089 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=83] [region_id=82]
   > [2024/07/24 12:12:15.089 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=10] ["first at"=74800000000000004b] ["first new region left"="{Id:82 StartKey:7480000000000000ff4a00000000000000f8 EndKey:7480000000000000ff4b00000000000000f8 RegionEpoch:{ConfVer:1 Version:41} Peers:[id:83 store_id:1 ] EncryptionMeta:<nil> IsInFlashback:false}"] ["new region count"=1]
   > [2024/07/24 12:12:15.089 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[82]"]
   > [2024/07/24 12:12:15.089 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 10 start_key: 7480000000000000FF4B00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 11 store_id: 1 } }"]
   > [2024/07/24 12:12:15.089 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=10] ["first split key"=74800000000000004c]
   > [2024/07/24 12:12:15.089 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 10 start_key: 7480000000000000FF4B00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 12:12:15.089 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=10] [detail="StartKey Changed:{7480000000000000FF4A00000000000000F8} -> {7480000000000000FF4B00000000000000F8}, EndKey:{748000FFFFFFFFFFFFFB00000000000000F8}"] [old-version=40] [new-version=41]
   > [2024/07/24 12:12:15.089 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {83} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=83] [region_id=82]
   > [2024/07/24 12:12:15.089 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=10] [origin="id:82 start_key:\"7480000000000000FF4A00000000000000F8\" end_key:\"7480000000000000FF4B00000000000000F8\" region_epoch:<conf_ver:1 version:41 > peers:<id:83 store_id:1 >"] [total=1]
   > [2024/07/24 12:12:15.090 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=83] [region_id=82]
   > [2024/07/24 12:12:15.090 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {83} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=83] [region_id=82]
   > [2024/07/24 12:12:15.090 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 83."] [id=83] [raft_id=83] [region_id=82]
   > [2024/07/24 12:12:15.090 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=83] [region_id=82]
   > [2024/07/24 12:12:15.090 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=83] [region_id=82]
   > [2024/07/24 12:12:15.090 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=83] [region_id=82]
   > [2024/07/24 12:12:15.090 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=83] [region_id=82]
   > [2024/07/24 12:12:15.090 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803858] [region_id=82]
   > [2024/07/24 12:12:15.090 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=68] [observe_id=ObserveId(79)] [region=10]
   > [2024/07/24 12:12:15.091 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:60164] [split_keys="key 7480000000000000FF4C00000000000000F8"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:15.091 +00:00] [INFO] [peer.rs:5566] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 40"] [prev_epoch="conf_ver: 1 version: 41"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:15.091 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=82]
   > [2024/07/24 12:12:15.094 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:60150] [split_keys="key 7480000000000000FF4C00000000000000F8"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:15.094 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=84] [peer-ids="[85]"]
   > [2024/07/24 12:12:15.094 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 10 start_key: 7480000000000000FF4B00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 11 store_id: 1 }"] [new_region_ids="[new_region_id: 84 new_peer_ids: 85]"] [region_id=10]
   > [2024/07/24 12:12:15.095 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 82 start_key: 7480000000000000FF4A00000000000000F8 end_key: 7480000000000000FF4B00000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 83 store_id: 1 }"]
   > [2024/07/24 12:12:15.096 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(80)] [region=82]
   > [2024/07/24 12:12:15.101 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF4C00000000000000F8 new_region_id: 84 new_peer_ids: 85 } right_derive: true }"] [index=69] [term=6] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:15.101 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF4C00000000000000F8"] [region="id: 10 start_key: 7480000000000000FF4B00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 11 store_id: 1 }"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:15.106 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/24 12:12:15.107 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=10]
   > [2024/07/24 12:12:15.107 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(79)] [region_id=10] [store_id=Some(1)]
   > [2024/07/24 12:12:15.107 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:15.107 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 10 start_key: 7480000000000000FF4C00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 42 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 12:12:15.107 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=10] ["first at"=74800000000000004c] ["first new region left"="{Id:84 StartKey:7480000000000000ff4b00000000000000f8 EndKey:7480000000000000ff4c00000000000000f8 RegionEpoch:{ConfVer:1 Version:42} Peers:[id:85 store_id:1 ] EncryptionMeta:<nil> IsInFlashback:false}"] ["new region count"=1]
   > [2024/07/24 12:12:15.107 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 84 start_key: 7480000000000000FF4B00000000000000F8 end_key: 7480000000000000FF4C00000000000000F8 region_epoch { conf_ver: 1 version: 42 } peers { id: 85 store_id: 1 }"] [region_id=84]
   > [2024/07/24 12:12:15.107 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[84]"]
   > [2024/07/24 12:12:15.107 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=85] [region_id=84]
   > [2024/07/24 12:12:15.107 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 10 start_key: 7480000000000000FF4C00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 42 } peers { id: 11 store_id: 1 } }"]
   > [2024/07/24 12:12:15.107 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=10] [detail="StartKey Changed:{7480000000000000FF4B00000000000000F8} -> {7480000000000000FF4C00000000000000F8}, EndKey:{748000FFFFFFFFFFFFFB00000000000000F8}"] [old-version=41] [new-version=42]
   > [2024/07/24 12:12:15.107 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 10 start_key: 7480000000000000FF4C00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 42 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 12:12:15.107 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=10] [origin="id:84 start_key:\"7480000000000000FF4B00000000000000F8\" end_key:\"7480000000000000FF4C00000000000000F8\" region_epoch:<conf_ver:1 version:42 > peers:<id:85 store_id:1 >"] [total=1]
   > [2024/07/24 12:12:15.107 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {85} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=85] [region_id=84]
   > [2024/07/24 12:12:15.107 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=85] [region_id=84]
   > [2024/07/24 12:12:15.107 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {85} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=85] [region_id=84]
   > [2024/07/24 12:12:15.108 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 85."] [id=85] [raft_id=85] [region_id=84]
   > [2024/07/24 12:12:15.108 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=85] [region_id=84]
   > [2024/07/24 12:12:15.108 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=85] [region_id=84]
   > [2024/07/24 12:12:15.108 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=85] [region_id=84]
   > [2024/07/24 12:12:15.108 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=85] [region_id=84]
   > [2024/07/24 12:12:15.108 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803860] [region_id=84]
   > [2024/07/24 12:12:15.108 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=69] [observe_id=ObserveId(81)] [region=10]
   > [2024/07/24 12:12:15.108 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=84]
   > [2024/07/24 12:12:15.113 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 84 start_key: 7480000000000000FF4B00000000000000F8 end_key: 7480000000000000FF4C00000000000000F8 region_epoch { conf_ver: 1 version: 42 } peers { id: 85 store_id: 1 }"]
   > [2024/07/24 12:12:15.114 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(82)] [region=84]
   > [2024/07/24 12:12:15.585 +00:00] [INFO] [info.go:1085] [SetTiFlashGroupConfig]
   > [2024/07/24 12:12:16.027 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/24 12:12:16.031 +00:00] [INFO] [manager.go:272] ["revoke session"] ["owner info"="[log-backup] /tidb/br-stream/owner ownerManager a34b2cd4-fbcd-4183-8575-f4d1c230fd54"] [error="rpc error: code = Canceled desc = grpc: the client connection is closing"]
   > [2024/07/24 12:12:16.080 +00:00] [INFO] [set.go:141] ["set global var"] [conn=6993195218841371033] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/07/24 12:12:16.630 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Region error (will back off and retry) message: \"EpochNotMatch current epoch of region 10 is conf_ver: 1 version: 42, but you sent conf_ver: 1 version: 41\" epoch_not_match { current_regions { id: 10 start_key: 7480000000000000FF4C00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 42 } peers { id: 11 store_id: 1 } } current_regions { id: 84 start_key: 7480000000000000FF4B00000000000000F8 end_key: 7480000000000000FF4C00000000000000F8 region_epoch { conf_ver: 1 version: 42 } peers { id: 85 store_id: 1 } } }"]
   > [2024/07/24 12:12:16.630 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Region error (will back off and retry) message: \"EpochNotMatch current epoch of region 10 is conf_ver: 1 version: 42, but you sent conf_ver: 1 version: 41\" epoch_not_match { current_regions { id: 10 start_key: 7480000000000000FF4C00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 42 } peers { id: 11 store_id: 1 } } current_regions { id: 84 start_key: 7480000000000000FF4B00000000000000F8 end_key: 7480000000000000FF4C00000000000000F8 region_epoch { conf_ver: 1 version: 42 } peers { id: 85 store_id: 1 } } }"]
   > [2024/07/24 12:12:16.936 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
