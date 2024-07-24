# Bug ID TIDB-39851-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/39851
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              Select does not throw errors when running concurently.


## Details
 * Database: tidb-v6.4.0.tikv
 * Number of scenarios: 3
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
   > [2024/07/24 09:49:17.974 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/24 09:49:17.977 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=4672033813629501845] [schemaVersion=34] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/24 09:49:17.978 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=4672033813629501845] [schemaVersion=34] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/24 09:49:18.022 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:71, Type:create schema, State:queueing, SchemaState:none, SchemaID:70, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 09:49:17.99 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 09:49:18.022 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:71, Type:create schema, State:queueing, SchemaState:none, SchemaID:70, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 09:49:17.99 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/24 09:49:18.071 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:71, Type:create schema, State:queueing, SchemaState:none, SchemaID:70, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:17.99 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:18.108 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=34] [neededSchemaVersion=35] ["start time"=1.12369ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 09:49:18.156 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=35] ["take time"=56.035023ms] [job="ID:71, Type:create schema, State:done, SchemaState:public, SchemaID:70, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 09:49:17.99 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:18.162 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:71, Type:create schema, State:synced, SchemaState:public, SchemaID:70, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:17.99 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:18.182 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=71]
   > [2024/07/24 09:49:18.182 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 09:49:18.183 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000047FF0000000000000000F7 lock_version: 451363355529052162 key: 748000FFFFFFFFFFFE5F728000000000000047 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451363355529052163"]
   > [2024/07/24 09:49:18.183 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000047FF0000000000000000F7 lock_version: 451363355529052162 key: 748000FFFFFFFFFFFE5F728000000000000047 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451363355529052163"]
   > [2024/07/24 09:49:18.187 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=4672033813629501845] [schemaVersion=35] [cur_db=testdb] [sql="CREATE TABLE t (c1 INT, c2 INT);"] [user=root@%]
   > [2024/07/24 09:49:18.189 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000047FF0000000000000000F7 lock_version: 451363355529052162 key: 748000FFFFFFFFFFFE5F728000000000000047 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451363355529052163"]
   > [2024/07/24 09:49:18.189 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000047FF0000000000000000F7 lock_version: 451363355529052162 key: 748000FFFFFFFFFFFE5F728000000000000047 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451363355529052163"]
   > [2024/07/24 09:49:18.231 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:73, Type:create table, State:queueing, SchemaState:none, SchemaID:70, TableID:72, RowCount:0, ArgLen:2, start time: 2024-07-24 09:49:18.19 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 09:49:18.231 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:73, Type:create table, State:queueing, SchemaState:none, SchemaID:70, TableID:72, RowCount:0, ArgLen:2, start time: 2024-07-24 09:49:18.19 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE t (c1 INT, c2 INT);"]
   > [2024/07/24 09:49:18.256 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:73, Type:create table, State:queueing, SchemaState:none, SchemaID:70, TableID:72, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:18.19 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:18.304 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=35] [neededSchemaVersion=36] ["start time"=2.214554ms] [phyTblIDs="[72]"] [actionTypes="[8]"]
   > [2024/07/24 09:49:18.352 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=36] ["take time"=57.627912ms] [job="ID:73, Type:create table, State:done, SchemaState:public, SchemaID:70, TableID:72, RowCount:0, ArgLen:2, start time: 2024-07-24 09:49:18.19 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:18.358 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:73, Type:create table, State:synced, SchemaState:public, SchemaID:70, TableID:72, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:18.19 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:18.380 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=73]
   > [2024/07/24 09:49:18.380 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 09:49:18.381 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=10] ["first split key"=748000000000000048]
   > [2024/07/24 09:49:18.382 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000049FF0000000000000000F7 lock_version: 451363355581480962 key: 748000FFFFFFFFFFFE5F728000000000000049 lock_ttl: 3005 txn_size: 1 lock_type: Del min_commit_ts: 451363355581480963"]
   > [2024/07/24 09:49:18.382 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000049FF0000000000000000F7 lock_version: 451363355581480962 key: 748000FFFFFFFFFFFE5F728000000000000049 lock_ttl: 3005 txn_size: 1 lock_type: Del min_commit_ts: 451363355581480963"]
   > [2024/07/24 09:49:18.386 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:57864] [split_keys="key 7480000000000000FF4800000000000000F8"] [peer_id=11] [region_id=10]
   > [2024/07/24 09:49:18.386 +00:00] [INFO] [peer.rs:5566] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 37"] [prev_epoch="conf_ver: 1 version: 38"] [peer_id=11] [region_id=10]
   > [2024/07/24 09:49:18.391 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:57880] [split_keys="key 7480000000000000FF4800000000000000F8"] [peer_id=11] [region_id=10]
   > [2024/07/24 09:49:18.391 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=78] [peer-ids="[79]"]
   > [2024/07/24 09:49:18.391 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 10 start_key: 7480000000000000FF4400000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 38 } peers { id: 11 store_id: 1 }"] [new_region_ids="[new_region_id: 78 new_peer_ids: 79]"] [region_id=10]
   > [2024/07/24 09:49:18.395 +00:00] [WARN] [2pc.go:1873] ["schemaLeaseChecker is not set for this transaction"] [sessionID=4672033813629501845] [startTS=451363355581480969] [checkTS=451363355594588161]
   > [2024/07/24 09:49:18.398 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF4800000000000000F8 new_region_id: 78 new_peer_ids: 79 } right_derive: true }"] [index=66] [term=6] [peer_id=11] [region_id=10]
   > [2024/07/24 09:49:18.398 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF4800000000000000F8"] [region="id: 10 start_key: 7480000000000000FF4400000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 38 } peers { id: 11 store_id: 1 }"] [peer_id=11] [region_id=10]
   > [2024/07/24 09:49:18.405 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=10]
   > [2024/07/24 09:49:18.405 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/24 09:49:18.405 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=11] [region_id=10]
   > [2024/07/24 09:49:18.405 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 78 start_key: 7480000000000000FF4400000000000000F8 end_key: 7480000000000000FF4800000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 79 store_id: 1 }"] [region_id=78]
   > [2024/07/24 09:49:18.405 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=10] [detail="StartKey Changed:{7480000000000000FF4400000000000000F8} -> {7480000000000000FF4800000000000000F8}, EndKey:{748000FFFFFFFFFFFFFB00000000000000F8}"] [old-version=38] [new-version=39]
   > [2024/07/24 09:49:18.405 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(73)] [region_id=10] [store_id=Some(1)]
   > [2024/07/24 09:49:18.405 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=79] [region_id=78]
   > [2024/07/24 09:49:18.405 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=10] ["first at"=748000000000000048] ["first new region left"="{Id:78 StartKey:7480000000000000ff4400000000000000f8 EndKey:7480000000000000ff4800000000000000f8 RegionEpoch:{ConfVer:1 Version:39} Peers:[id:79 store_id:1 ] EncryptionMeta:<nil> IsInFlashback:false}"] ["new region count"=1]
   > [2024/07/24 09:49:18.405 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[78]"]
   > [2024/07/24 09:49:18.405 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 10 start_key: 7480000000000000FF4800000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 09:49:18.405 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=10] [origin="id:78 start_key:\"7480000000000000FF4400000000000000F8\" end_key:\"7480000000000000FF4800000000000000F8\" region_epoch:<conf_ver:1 version:39 > peers:<id:79 store_id:1 >"] [total=1]
   > [2024/07/24 09:49:18.405 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 10 start_key: 7480000000000000FF4800000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 11 store_id: 1 } }"]
   > [2024/07/24 09:49:18.405 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 10 start_key: 7480000000000000FF4800000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 09:49:18.406 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {79} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=79] [region_id=78]
   > [2024/07/24 09:49:18.406 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=79] [region_id=78]
   > [2024/07/24 09:49:18.406 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {79} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=79] [region_id=78]
   > [2024/07/24 09:49:18.406 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 79."] [id=79] [raft_id=79] [region_id=78]
   > [2024/07/24 09:49:18.406 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=79] [region_id=78]
   > [2024/07/24 09:49:18.406 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=79] [region_id=78]
   > [2024/07/24 09:49:18.406 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=79] [region_id=78]
   > [2024/07/24 09:49:18.406 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=79] [region_id=78]
   > [2024/07/24 09:49:18.406 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803854] [region_id=78]
   > [2024/07/24 09:49:18.406 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=66] [observe_id=ObserveId(75)] [region=10]
   > [2024/07/24 09:49:18.407 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=78]
   > [2024/07/24 09:49:18.410 +00:00] [INFO] [scheduler.rs:640] ["get snapshot failed"] [err="Error(Request(message: \"EpochNotMatch current epoch of region 10 is conf_ver: 1 version: 39, but you sent conf_ver: 1 version: 38\" epoch_not_match { current_regions { id: 10 start_key: 7480000000000000FF4800000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 11 store_id: 1 } } current_regions { id: 78 start_key: 7480000000000000FF4400000000000000F8 end_key: 7480000000000000FF4800000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 79 store_id: 1 } } }))"] [cid=965]
   > [2024/07/24 09:49:18.410 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 78 start_key: 7480000000000000FF4400000000000000F8 end_key: 7480000000000000FF4800000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 79 store_id: 1 }"]
   > [2024/07/24 09:49:18.410 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(76)] [region=78]
   > [2024/07/24 09:49:19.056 +00:00] [INFO] [info.go:1085] [SetTiFlashGroupConfig]
   > [2024/07/24 09:49:19.441 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/24 09:49:19.478 +00:00] [INFO] [set.go:141] ["set global var"] [conn=4672033813629501849] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/07/24 09:49:19.502 +00:00] [INFO] [manager.go:272] ["revoke session"] ["owner info"="[log-backup] /tidb/br-stream/owner ownerManager 4d3bd523-9a96-4b34-aba4-a30651c11b2b"] [error="rpc error: code = Canceled desc = grpc: the client connection is closing"]
   > [2024/07/24 09:49:20.051 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]

### Scenario 1
 * Instruction #0:
     - Instruction:  SELECT /*+ INL_JOIN(t)*/c1 FROM t WHERE c2<=c1 FOR UPDATE;
     - Transaction: conn_0
     - Output: [(1,)]
     - Executed order: 0
     - Affected rows: 1
     - Warnings: [('Warning', 1815, 'There are no matching table names for (t) in optimizer hint /*+ INL_JOIN(t) */ or /*+ TIDB_INLJ(t) */. Maybe you can use the table alias name')]

 * Container logs:
   > [2024/07/24 09:49:24.209 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/24 09:49:24.212 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=4672033813629501855] [schemaVersion=44] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/24 09:49:24.244 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:80, Type:drop schema, State:queueing, SchemaState:public, SchemaID:75, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 09:49:24.19 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 09:49:24.244 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:80, Type:drop schema, State:queueing, SchemaState:public, SchemaID:75, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 09:49:24.19 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/24 09:49:24.265 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:80, Type:drop schema, State:queueing, SchemaState:public, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:24.19 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:24.305 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=44] [neededSchemaVersion=45] ["start time"=825.324µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 09:49:24.354 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=45] ["take time"=57.14195ms] [job="ID:80, Type:drop schema, State:running, SchemaState:write only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:24.19 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:24.358 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:80, Type:drop schema, State:running, SchemaState:write only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:24.19 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:24.398 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=45] [neededSchemaVersion=46] ["start time"=823.159µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 09:49:24.447 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=46] ["take time"=56.736517ms] [job="ID:80, Type:drop schema, State:running, SchemaState:delete only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:24.19 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:24.452 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:80, Type:drop schema, State:running, SchemaState:delete only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:24.19 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:24.496 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=46] [neededSchemaVersion=47] ["start time"=748.428µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 09:49:24.545 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=47] ["take time"=57.351616ms] [job="ID:80, Type:drop schema, State:done, SchemaState:none, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:24.19 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:24.551 +00:00] [INFO] [delete_range.go:109] ["[ddl] add job into delete-range table"] [jobID=80] [jobType="drop schema"]
   > [2024/07/24 09:49:24.553 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:80, Type:drop schema, State:synced, SchemaState:none, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:24.19 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:24.574 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=80]
   > [2024/07/24 09:49:24.574 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 09:49:24.575 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000050FF0000000000000000F7 lock_version: 451363357206773762 key: 748000FFFFFFFFFFFE5F728000000000000050 lock_ttl: 3005 txn_size: 1 lock_type: Del min_commit_ts: 451363357206773763"]
   > [2024/07/24 09:49:24.575 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000050FF0000000000000000F7 lock_version: 451363357206773762 key: 748000FFFFFFFFFFFE5F728000000000000050 lock_ttl: 3005 txn_size: 1 lock_type: Del min_commit_ts: 451363357206773763"]
   > [2024/07/24 09:49:24.577 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=4672033813629501855] [schemaVersion=47] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/24 09:49:24.581 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000050FF0000000000000000F7 lock_version: 451363357206773762 key: 748000FFFFFFFFFFFE5F728000000000000050 lock_ttl: 3005 txn_size: 1 lock_type: Del min_commit_ts: 451363357206773763"]
   > [2024/07/24 09:49:24.581 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000050FF0000000000000000F7 lock_version: 451363357206773762 key: 748000FFFFFFFFFFFE5F728000000000000050 lock_ttl: 3005 txn_size: 1 lock_type: Del min_commit_ts: 451363357206773763"]
   > [2024/07/24 09:49:24.619 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:82, Type:create schema, State:queueing, SchemaState:none, SchemaID:81, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 09:49:24.589 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 09:49:24.619 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:82, Type:create schema, State:queueing, SchemaState:none, SchemaID:81, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 09:49:24.589 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/24 09:49:24.640 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:82, Type:create schema, State:queueing, SchemaState:none, SchemaID:81, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:24.589 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:24.679 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=47] [neededSchemaVersion=48] ["start time"=1.458443ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 09:49:24.727 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=48] ["take time"=55.937663ms] [job="ID:82, Type:create schema, State:done, SchemaState:public, SchemaID:81, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 09:49:24.589 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:24.734 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:82, Type:create schema, State:synced, SchemaState:public, SchemaID:81, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:24.589 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:24.754 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=82]
   > [2024/07/24 09:49:24.754 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 09:49:24.754 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000052FF0000000000000000F7 lock_version: 451363357246095362 key: 748000FFFFFFFFFFFE5F728000000000000052 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451363357246095363"]
   > [2024/07/24 09:49:24.754 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000052FF0000000000000000F7 lock_version: 451363357246095362 key: 748000FFFFFFFFFFFE5F728000000000000052 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451363357246095363"]
   > [2024/07/24 09:49:24.759 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=4672033813629501855] [schemaVersion=48] [cur_db=testdb] [sql="CREATE TABLE t (c1 INT, c2 INT);"] [user=root@%]
   > [2024/07/24 09:49:24.801 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:84, Type:create table, State:queueing, SchemaState:none, SchemaID:81, TableID:83, RowCount:0, ArgLen:2, start time: 2024-07-24 09:49:24.74 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 09:49:24.801 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:84, Type:create table, State:queueing, SchemaState:none, SchemaID:81, TableID:83, RowCount:0, ArgLen:2, start time: 2024-07-24 09:49:24.74 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE t (c1 INT, c2 INT);"]
   > [2024/07/24 09:49:24.825 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:84, Type:create table, State:queueing, SchemaState:none, SchemaID:81, TableID:83, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:24.74 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:24.867 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=48] [neededSchemaVersion=49] ["start time"=2.237392ms] [phyTblIDs="[83]"] [actionTypes="[8]"]
   > [2024/07/24 09:49:24.914 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=49] ["take time"=57.716542ms] [job="ID:84, Type:create table, State:done, SchemaState:public, SchemaID:81, TableID:83, RowCount:0, ArgLen:2, start time: 2024-07-24 09:49:24.74 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:24.922 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:84, Type:create table, State:synced, SchemaState:public, SchemaID:81, TableID:83, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:24.74 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:24.946 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=84]
   > [2024/07/24 09:49:24.946 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 09:49:24.946 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=10] ["first split key"=748000000000000053]
   > [2024/07/24 09:49:24.947 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000054FF0000000000000000F7 lock_version: 451363357298262018 key: 748000FFFFFFFFFFFE5F728000000000000054 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451363357298262019"]
   > [2024/07/24 09:49:24.947 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000054FF0000000000000000F7 lock_version: 451363357298262018 key: 748000FFFFFFFFFFFE5F728000000000000054 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451363357298262019"]
   > [2024/07/24 09:49:24.949 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:57846] [split_keys="key 7480000000000000FF5300000000000000F8"] [peer_id=11] [region_id=10]
   > [2024/07/24 09:49:24.949 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=82] [peer-ids="[83]"]
   > [2024/07/24 09:49:24.950 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 10 start_key: 7480000000000000FF4D00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 40 } peers { id: 11 store_id: 1 }"] [new_region_ids="[new_region_id: 82 new_peer_ids: 83]"] [region_id=10]
   > [2024/07/24 09:49:24.958 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF5300000000000000F8 new_region_id: 82 new_peer_ids: 83 } right_derive: true }"] [index=72] [term=6] [peer_id=11] [region_id=10]
   > [2024/07/24 09:49:24.959 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF5300000000000000F8"] [region="id: 10 start_key: 7480000000000000FF4D00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 40 } peers { id: 11 store_id: 1 }"] [peer_id=11] [region_id=10]
   > [2024/07/24 09:49:24.963 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=10]
   > [2024/07/24 09:49:24.963 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/24 09:49:24.963 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=11] [region_id=10]
   > [2024/07/24 09:49:24.963 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 82 start_key: 7480000000000000FF4D00000000000000F8 end_key: 7480000000000000FF5300000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 83 store_id: 1 }"] [region_id=82]
   > [2024/07/24 09:49:24.963 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=10] ["first at"=748000000000000053] ["first new region left"="{Id:82 StartKey:7480000000000000ff4d00000000000000f8 EndKey:7480000000000000ff5300000000000000f8 RegionEpoch:{ConfVer:1 Version:41} Peers:[id:83 store_id:1 ] EncryptionMeta:<nil> IsInFlashback:false}"] ["new region count"=1]
   > [2024/07/24 09:49:24.963 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[82]"]
   > [2024/07/24 09:49:24.963 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=83] [region_id=82]
   > [2024/07/24 09:49:24.963 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=10] [detail="StartKey Changed:{7480000000000000FF4D00000000000000F8} -> {7480000000000000FF5300000000000000F8}, EndKey:{748000FFFFFFFFFFFFFB00000000000000F8}"] [old-version=40] [new-version=41]
   > [2024/07/24 09:49:24.963 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(77)] [region_id=10] [store_id=Some(1)]
   > [2024/07/24 09:49:24.963 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 10 start_key: 7480000000000000FF5300000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 09:49:24.963 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=10] [origin="id:82 start_key:\"7480000000000000FF4D00000000000000F8\" end_key:\"7480000000000000FF5300000000000000F8\" region_epoch:<conf_ver:1 version:41 > peers:<id:83 store_id:1 >"] [total=1]
   > [2024/07/24 09:49:24.964 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 10 start_key: 7480000000000000FF5300000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 11 store_id: 1 } }"]
   > [2024/07/24 09:49:24.964 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 10 start_key: 7480000000000000FF5300000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 09:49:24.964 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {83} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=83] [region_id=82]
   > [2024/07/24 09:49:24.964 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=83] [region_id=82]
   > [2024/07/24 09:49:24.964 +00:00] [WARN] [2pc.go:1873] ["schemaLeaseChecker is not set for this transaction"] [sessionID=4672033813629501855] [startTS=451363357311631365] [checkTS=451363357311631368]
   > [2024/07/24 09:49:24.964 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {83} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=83] [region_id=82]
   > [2024/07/24 09:49:24.964 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 83."] [id=83] [raft_id=83] [region_id=82]
   > [2024/07/24 09:49:24.964 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=83] [region_id=82]
   > [2024/07/24 09:49:24.964 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=83] [region_id=82]
   > [2024/07/24 09:49:24.964 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=83] [region_id=82]
   > [2024/07/24 09:49:24.964 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=83] [region_id=82]
   > [2024/07/24 09:49:24.965 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803858] [region_id=82]
   > [2024/07/24 09:49:24.965 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=72] [observe_id=ObserveId(79)] [region=10]
   > [2024/07/24 09:49:24.965 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=82]
   > [2024/07/24 09:49:24.968 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 82 start_key: 7480000000000000FF4D00000000000000F8 end_key: 7480000000000000FF5300000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 83 store_id: 1 }"]
   > [2024/07/24 09:49:24.968 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(80)] [region=82]
   > [2024/07/24 09:49:24.973 +00:00] [INFO] [scheduler.rs:640] ["get snapshot failed"] [err="Error(Request(message: \"EpochNotMatch current epoch of region 10 is conf_ver: 1 version: 41, but you sent conf_ver: 1 version: 40\" epoch_not_match { current_regions { id: 10 start_key: 7480000000000000FF5300000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 11 store_id: 1 } } current_regions { id: 82 start_key: 7480000000000000FF4D00000000000000F8 end_key: 7480000000000000FF5300000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 83 store_id: 1 } } }))"] [cid=1202]
   > [2024/07/24 09:49:25.991 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]

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
   > [2024/07/24 09:49:29.062 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/24 09:49:29.064 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=4672033813629501861] [schemaVersion=57] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/24 09:49:29.093 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:91, Type:drop schema, State:queueing, SchemaState:public, SchemaID:86, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 09:49:29.04 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 09:49:29.093 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:91, Type:drop schema, State:queueing, SchemaState:public, SchemaID:86, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 09:49:29.04 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/24 09:49:29.114 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:91, Type:drop schema, State:queueing, SchemaState:public, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:29.04 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:29.154 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=57] [neededSchemaVersion=58] ["start time"=780.277µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 09:49:29.203 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=58] ["take time"=56.834925ms] [job="ID:91, Type:drop schema, State:running, SchemaState:write only, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:29.04 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:29.207 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:91, Type:drop schema, State:running, SchemaState:write only, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:29.04 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:29.247 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=58] [neededSchemaVersion=59] ["start time"=894.398µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 09:49:29.296 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=59] ["take time"=56.883953ms] [job="ID:91, Type:drop schema, State:running, SchemaState:delete only, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:29.04 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:29.301 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:91, Type:drop schema, State:running, SchemaState:delete only, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:29.04 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:29.344 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=59] [neededSchemaVersion=60] ["start time"=806.956µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 09:49:29.393 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=60] ["take time"=57.131335ms] [job="ID:91, Type:drop schema, State:done, SchemaState:none, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:29.04 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:29.399 +00:00] [INFO] [delete_range.go:109] ["[ddl] add job into delete-range table"] [jobID=91] [jobType="drop schema"]
   > [2024/07/24 09:49:29.400 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:91, Type:drop schema, State:synced, SchemaState:none, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:29.04 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:29.424 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=91]
   > [2024/07/24 09:49:29.424 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 09:49:29.425 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000005BFF0000000000000000F7 lock_version: 451363358477910018 key: 748000FFFFFFFFFFFE5F72800000000000005B lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451363358477910019"]
   > [2024/07/24 09:49:29.425 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000005BFF0000000000000000F7 lock_version: 451363358477910018 key: 748000FFFFFFFFFFFE5F72800000000000005B lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451363358477910019"]
   > [2024/07/24 09:49:29.427 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=4672033813629501861] [schemaVersion=60] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/24 09:49:29.469 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:93, Type:create schema, State:queueing, SchemaState:none, SchemaID:92, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 09:49:29.44 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 09:49:29.469 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:93, Type:create schema, State:queueing, SchemaState:none, SchemaID:92, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 09:49:29.44 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/24 09:49:29.492 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:93, Type:create schema, State:queueing, SchemaState:none, SchemaID:92, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:29.44 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:29.530 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=60] [neededSchemaVersion=61] ["start time"=1.65449ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 09:49:29.578 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=61] ["take time"=57.103467ms] [job="ID:93, Type:create schema, State:done, SchemaState:public, SchemaID:92, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 09:49:29.44 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:29.585 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:93, Type:create schema, State:synced, SchemaState:public, SchemaID:92, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:29.44 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:29.605 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=93]
   > [2024/07/24 09:49:29.605 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 09:49:29.606 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000005DFF0000000000000000F7 lock_version: 451363358517231618 key: 748000FFFFFFFFFFFE5F72800000000000005D lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451363358517231619"]
   > [2024/07/24 09:49:29.606 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000005DFF0000000000000000F7 lock_version: 451363358517231618 key: 748000FFFFFFFFFFFE5F72800000000000005D lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451363358517231619"]
   > [2024/07/24 09:49:29.610 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=4672033813629501861] [schemaVersion=61] [cur_db=testdb] [sql="CREATE TABLE t (c1 INT, c2 INT);"] [user=root@%]
   > [2024/07/24 09:49:29.653 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:95, Type:create table, State:queueing, SchemaState:none, SchemaID:92, TableID:94, RowCount:0, ArgLen:2, start time: 2024-07-24 09:49:29.59 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 09:49:29.653 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:95, Type:create table, State:queueing, SchemaState:none, SchemaID:92, TableID:94, RowCount:0, ArgLen:2, start time: 2024-07-24 09:49:29.59 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE t (c1 INT, c2 INT);"]
   > [2024/07/24 09:49:29.675 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:95, Type:create table, State:queueing, SchemaState:none, SchemaID:92, TableID:94, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:29.59 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:29.723 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=61] [neededSchemaVersion=62] ["start time"=2.263164ms] [phyTblIDs="[94]"] [actionTypes="[8]"]
   > [2024/07/24 09:49:29.771 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=62] ["take time"=59.283449ms] [job="ID:95, Type:create table, State:done, SchemaState:public, SchemaID:92, TableID:94, RowCount:0, ArgLen:2, start time: 2024-07-24 09:49:29.59 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:29.777 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:95, Type:create table, State:synced, SchemaState:public, SchemaID:92, TableID:94, RowCount:0, ArgLen:0, start time: 2024-07-24 09:49:29.59 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:49:29.798 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=95]
   > [2024/07/24 09:49:29.798 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 09:49:29.798 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=10] ["first split key"=74800000000000005e]
   > [2024/07/24 09:49:29.799 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000005FFF0000000000000000F7 lock_version: 451363358569922562 key: 748000FFFFFFFFFFFE5F72800000000000005F lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451363358569922563"]
   > [2024/07/24 09:49:29.799 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000005FFF0000000000000000F7 lock_version: 451363358569922562 key: 748000FFFFFFFFFFFE5F72800000000000005F lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451363358569922563"]
   > [2024/07/24 09:49:29.801 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:57862] [split_keys="key 7480000000000000FF5E00000000000000F8"] [peer_id=11] [region_id=10]
   > [2024/07/24 09:49:29.801 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=86] [peer-ids="[87]"]
   > [2024/07/24 09:49:29.802 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 10 start_key: 7480000000000000FF5800000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 42 } peers { id: 11 store_id: 1 }"] [new_region_ids="[new_region_id: 86 new_peer_ids: 87]"] [region_id=10]
   > [2024/07/24 09:49:29.809 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF5E00000000000000F8 new_region_id: 86 new_peer_ids: 87 } right_derive: true }"] [index=76] [term=6] [peer_id=11] [region_id=10]
   > [2024/07/24 09:49:29.809 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF5E00000000000000F8"] [region="id: 10 start_key: 7480000000000000FF5800000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 42 } peers { id: 11 store_id: 1 }"] [peer_id=11] [region_id=10]
   > [2024/07/24 09:49:29.816 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=10]
   > [2024/07/24 09:49:29.816 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/24 09:49:29.816 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(81)] [region_id=10] [store_id=Some(1)]
   > [2024/07/24 09:49:29.816 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=10] ["first at"=74800000000000005e] ["first new region left"="{Id:86 StartKey:7480000000000000ff5800000000000000f8 EndKey:7480000000000000ff5e00000000000000f8 RegionEpoch:{ConfVer:1 Version:43} Peers:[id:87 store_id:1 ] EncryptionMeta:<nil> IsInFlashback:false}"] ["new region count"=1]
   > [2024/07/24 09:49:29.816 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[86]"]
   > [2024/07/24 09:49:29.816 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=11] [region_id=10]
   > [2024/07/24 09:49:29.816 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 10 start_key: 7480000000000000FF5E00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 43 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 09:49:29.816 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 86 start_key: 7480000000000000FF5800000000000000F8 end_key: 7480000000000000FF5E00000000000000F8 region_epoch { conf_ver: 1 version: 43 } peers { id: 87 store_id: 1 }"] [region_id=86]
   > [2024/07/24 09:49:29.816 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=87] [region_id=86]
   > [2024/07/24 09:49:29.816 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=10] [detail="StartKey Changed:{7480000000000000FF5800000000000000F8} -> {7480000000000000FF5E00000000000000F8}, EndKey:{748000FFFFFFFFFFFFFB00000000000000F8}"] [old-version=42] [new-version=43]
   > [2024/07/24 09:49:29.817 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 10 start_key: 7480000000000000FF5E00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 43 } peers { id: 11 store_id: 1 } }"]
   > [2024/07/24 09:49:29.817 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 10 start_key: 7480000000000000FF5E00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 43 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 09:49:29.817 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=10] [origin="id:86 start_key:\"7480000000000000FF5800000000000000F8\" end_key:\"7480000000000000FF5E00000000000000F8\" region_epoch:<conf_ver:1 version:43 > peers:<id:87 store_id:1 >"] [total=1]
   > [2024/07/24 09:49:29.817 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {87} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=87] [region_id=86]
   > [2024/07/24 09:49:29.817 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=87] [region_id=86]
   > [2024/07/24 09:49:29.817 +00:00] [WARN] [2pc.go:1873] ["schemaLeaseChecker is not set for this transaction"] [sessionID=4672033813629501861] [startTS=451363358582767622] [checkTS=451363358582767625]
   > [2024/07/24 09:49:29.817 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {87} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=87] [region_id=86]
   > [2024/07/24 09:49:29.817 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 87."] [id=87] [raft_id=87] [region_id=86]
   > [2024/07/24 09:49:29.817 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=87] [region_id=86]
   > [2024/07/24 09:49:29.817 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=87] [region_id=86]
   > [2024/07/24 09:49:29.817 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=87] [region_id=86]
   > [2024/07/24 09:49:29.818 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=87] [region_id=86]
   > [2024/07/24 09:49:29.818 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803862] [region_id=86]
   > [2024/07/24 09:49:29.818 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=86]
   > [2024/07/24 09:49:29.821 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=76] [observe_id=ObserveId(83)] [region=10]
   > [2024/07/24 09:49:29.821 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 86 start_key: 7480000000000000FF5800000000000000F8 end_key: 7480000000000000FF5E00000000000000F8 region_epoch { conf_ver: 1 version: 43 } peers { id: 87 store_id: 1 }"]
   > [2024/07/24 09:49:29.821 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(84)] [region=86]
   > [2024/07/24 09:49:29.826 +00:00] [INFO] [scheduler.rs:640] ["get snapshot failed"] [err="Error(Request(message: \"EpochNotMatch current epoch of region 10 is conf_ver: 1 version: 43, but you sent conf_ver: 1 version: 42\" epoch_not_match { current_regions { id: 10 start_key: 7480000000000000FF5E00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 43 } peers { id: 11 store_id: 1 } } current_regions { id: 86 start_key: 7480000000000000FF5800000000000000F8 end_key: 7480000000000000FF5E00000000000000F8 region_epoch { conf_ver: 1 version: 43 } peers { id: 87 store_id: 1 } } }))"] [cid=1426]
   > [2024/07/24 09:49:30.845 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
