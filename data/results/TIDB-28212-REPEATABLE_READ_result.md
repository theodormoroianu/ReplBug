# Bug ID TIDB-28212-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/28212
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              Incorrect SELECT value when row is updated by 2 transactions.


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
   > [2024/08/06 12:44:23.457 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/08/06 12:44:23.460 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=4993064820661027221] [schemaVersion=34] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/08/06 12:44:23.462 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=4993064820661027221] [schemaVersion=34] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/08/06 12:44:23.504 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:71, Type:create schema, State:queueing, SchemaState:none, SchemaID:70, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-06 12:44:23.476 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/08/06 12:44:23.504 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:71, Type:create schema, State:queueing, SchemaState:none, SchemaID:70, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-06 12:44:23.476 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/08/06 12:44:23.525 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:71, Type:create schema, State:queueing, SchemaState:none, SchemaID:70, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-06 12:44:23.476 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 12:44:23.563 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=34] [neededSchemaVersion=35] ["start time"=1.463819ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/06 12:44:23.611 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=35] ["take time"=56.928735ms] [job="ID:71, Type:create schema, State:done, SchemaState:public, SchemaID:70, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-06 12:44:23.476 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 12:44:23.618 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:71, Type:create schema, State:synced, SchemaState:public, SchemaID:70, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-06 12:44:23.476 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 12:44:23.639 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=71]
   > [2024/08/06 12:44:23.639 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/08/06 12:44:23.639 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000047FF0000000000000000F7 lock_version: 451660549606604802 key: 748000FFFFFFFFFFFE5F728000000000000047 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451660549606604803"]
   > [2024/08/06 12:44:23.640 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000047FF0000000000000000F7 lock_version: 451660549606604802 key: 748000FFFFFFFFFFFE5F728000000000000047 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451660549606604803"]
   > [2024/08/06 12:44:23.644 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=4993064820661027221] [schemaVersion=35] [cur_db=testdb] [sql="create table t(a int, b int);"] [user=root@%]
   > [2024/08/06 12:44:23.645 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000047FF0000000000000000F7 lock_version: 451660549606604802 key: 748000FFFFFFFFFFFE5F728000000000000047 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451660549606604803"]
   > [2024/08/06 12:44:23.645 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000047FF0000000000000000F7 lock_version: 451660549606604802 key: 748000FFFFFFFFFFFE5F728000000000000047 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451660549606604803"]
   > [2024/08/06 12:44:23.687 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:73, Type:create table, State:queueing, SchemaState:none, SchemaID:70, TableID:72, RowCount:0, ArgLen:2, start time: 2024-08-06 12:44:23.625 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/08/06 12:44:23.687 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:73, Type:create table, State:queueing, SchemaState:none, SchemaID:70, TableID:72, RowCount:0, ArgLen:2, start time: 2024-08-06 12:44:23.625 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t(a int, b int);"]
   > [2024/08/06 12:44:23.710 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:73, Type:create table, State:queueing, SchemaState:none, SchemaID:70, TableID:72, RowCount:0, ArgLen:0, start time: 2024-08-06 12:44:23.625 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 12:44:23.759 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=35] [neededSchemaVersion=36] ["start time"=4.063969ms] [phyTblIDs="[72]"] [actionTypes="[8]"]
   > [2024/08/06 12:44:23.804 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=36] ["take time"=58.877328ms] [job="ID:73, Type:create table, State:done, SchemaState:public, SchemaID:70, TableID:72, RowCount:0, ArgLen:2, start time: 2024-08-06 12:44:23.625 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 12:44:23.811 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:73, Type:create table, State:synced, SchemaState:public, SchemaID:70, TableID:72, RowCount:0, ArgLen:0, start time: 2024-08-06 12:44:23.625 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 12:44:23.835 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=73]
   > [2024/08/06 12:44:23.835 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/08/06 12:44:23.835 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=10] ["first split key"=748000000000000048]
   > [2024/08/06 12:44:23.836 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:38448] [split_keys="key 7480000000000000FF4800000000000000F8"] [peer_id=11] [region_id=10]
   > [2024/08/06 12:44:23.836 +00:00] [INFO] [peer.rs:5566] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 37"] [prev_epoch="conf_ver: 1 version: 38"] [peer_id=11] [region_id=10]
   > [2024/08/06 12:44:23.837 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000049FF0000000000000000F7 lock_version: 451660549659295746 key: 748000FFFFFFFFFFFE5F728000000000000049 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451660549659295747"]
   > [2024/08/06 12:44:23.837 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000049FF0000000000000000F7 lock_version: 451660549659295746 key: 748000FFFFFFFFFFFE5F728000000000000049 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451660549659295747"]
   > [2024/08/06 12:44:23.839 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:38450] [split_keys="key 7480000000000000FF4800000000000000F8"] [peer_id=11] [region_id=10]
   > [2024/08/06 12:44:23.839 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=78] [peer-ids="[79]"]
   > [2024/08/06 12:44:23.840 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 10 start_key: 7480000000000000FF4400000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 38 } peers { id: 11 store_id: 1 }"] [new_region_ids="[new_region_id: 78 new_peer_ids: 79]"] [region_id=10]
   > [2024/08/06 12:44:23.845 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF4800000000000000F8 new_region_id: 78 new_peer_ids: 79 } right_derive: true }"] [index=66] [term=6] [peer_id=11] [region_id=10]
   > [2024/08/06 12:44:23.846 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF4800000000000000F8"] [region="id: 10 start_key: 7480000000000000FF4400000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 38 } peers { id: 11 store_id: 1 }"] [peer_id=11] [region_id=10]
   > [2024/08/06 12:44:23.853 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/08/06 12:44:23.853 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=10]
   > [2024/08/06 12:44:23.853 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(73)] [region_id=10] [store_id=Some(1)]
   > [2024/08/06 12:44:23.853 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=11] [region_id=10]
   > [2024/08/06 12:44:23.853 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=10] ["first at"=748000000000000048] ["first new region left"="{Id:78 StartKey:7480000000000000ff4400000000000000f8 EndKey:7480000000000000ff4800000000000000f8 RegionEpoch:{ConfVer:1 Version:39} Peers:[id:79 store_id:1 ] EncryptionMeta:<nil> IsInFlashback:false}"] ["new region count"=1]
   > [2024/08/06 12:44:23.853 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[78]"]
   > [2024/08/06 12:44:23.853 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 10 start_key: 7480000000000000FF4800000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 11 store_id: 1 }"]
   > [2024/08/06 12:44:23.853 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=10] [detail="StartKey Changed:{7480000000000000FF4400000000000000F8} -> {7480000000000000FF4800000000000000F8}, EndKey:{748000FFFFFFFFFFFFFB00000000000000F8}"] [old-version=38] [new-version=39]
   > [2024/08/06 12:44:23.853 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 78 start_key: 7480000000000000FF4400000000000000F8 end_key: 7480000000000000FF4800000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 79 store_id: 1 }"] [region_id=78]
   > [2024/08/06 12:44:23.853 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=79] [region_id=78]
   > [2024/08/06 12:44:23.853 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 10 start_key: 7480000000000000FF4800000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 11 store_id: 1 } }"]
   > [2024/08/06 12:44:23.853 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=10] [origin="id:78 start_key:\"7480000000000000FF4400000000000000F8\" end_key:\"7480000000000000FF4800000000000000F8\" region_epoch:<conf_ver:1 version:39 > peers:<id:79 store_id:1 >"] [total=1]
   > [2024/08/06 12:44:23.854 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 10 start_key: 7480000000000000FF4800000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 11 store_id: 1 }"]
   > [2024/08/06 12:44:23.854 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {79} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=79] [region_id=78]
   > [2024/08/06 12:44:23.854 +00:00] [WARN] [2pc.go:1873] ["schemaLeaseChecker is not set for this transaction"] [sessionID=4993064820661027221] [startTS=451660549672140805] [checkTS=451660549672140808]
   > [2024/08/06 12:44:23.854 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=79] [region_id=78]
   > [2024/08/06 12:44:23.854 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {79} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=79] [region_id=78]
   > [2024/08/06 12:44:23.854 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 79."] [id=79] [raft_id=79] [region_id=78]
   > [2024/08/06 12:44:23.854 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=79] [region_id=78]
   > [2024/08/06 12:44:23.854 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=79] [region_id=78]
   > [2024/08/06 12:44:23.854 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=79] [region_id=78]
   > [2024/08/06 12:44:23.854 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=79] [region_id=78]
   > [2024/08/06 12:44:23.854 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803854] [region_id=78]
   > [2024/08/06 12:44:23.855 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=78]
   > [2024/08/06 12:44:23.858 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 78 start_key: 7480000000000000FF4400000000000000F8 end_key: 7480000000000000FF4800000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 79 store_id: 1 }"]
   > [2024/08/06 12:44:23.858 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=66] [observe_id=ObserveId(75)] [region=10]
   > [2024/08/06 12:44:23.858 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(76)] [region=78]
   > [2024/08/06 12:44:23.863 +00:00] [INFO] [scheduler.rs:640] ["get snapshot failed"] [err="Error(Request(message: \"EpochNotMatch current epoch of region 10 is conf_ver: 1 version: 39, but you sent conf_ver: 1 version: 38\" epoch_not_match { current_regions { id: 10 start_key: 7480000000000000FF4800000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 11 store_id: 1 } } current_regions { id: 78 start_key: 7480000000000000FF4400000000000000F8 end_key: 7480000000000000FF4800000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 79 store_id: 1 } } }))"] [cid=969]
   > [2024/08/06 12:44:24.359 +00:00] [INFO] [info.go:1085] [SetTiFlashGroupConfig]
   > [2024/08/06 12:44:24.779 +00:00] [INFO] [manager.go:272] ["revoke session"] ["owner info"="[log-backup] /tidb/br-stream/owner ownerManager 028328cb-6b68-45ee-9acd-bca749a8a952"] [error="rpc error: code = Canceled desc = grpc: the client connection is closing"]
   > [2024/08/06 12:44:24.897 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/08/06 12:44:24.932 +00:00] [INFO] [set.go:141] ["set global var"] [conn=4993064820661027225] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/08/06 12:44:25.808 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
