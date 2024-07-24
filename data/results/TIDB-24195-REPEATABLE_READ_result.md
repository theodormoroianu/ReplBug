# Bug ID TIDB-24195-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/24195
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              Query in optimistic transaction returns rows with same PK


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
   > [2024/07/24 12:46:54.214 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/24 12:46:54.218 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=8690506920592671127] [schemaVersion=34] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/24 12:46:54.219 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=8690506920592671127] [schemaVersion=34] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/24 12:46:54.275 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:71, Type:create schema, State:queueing, SchemaState:none, SchemaID:70, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:46:54.227 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 12:46:54.275 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:71, Type:create schema, State:queueing, SchemaState:none, SchemaID:70, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:46:54.227 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/24 12:46:54.298 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:71, Type:create schema, State:queueing, SchemaState:none, SchemaID:70, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:46:54.227 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:46:54.339 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=34] [neededSchemaVersion=35] ["start time"=1.563343ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:46:54.386 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=35] ["take time"=56.652119ms] [job="ID:71, Type:create schema, State:done, SchemaState:public, SchemaID:70, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:46:54.227 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:46:54.392 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:71, Type:create schema, State:synced, SchemaState:public, SchemaID:70, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:46:54.227 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:46:54.411 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=71]
   > [2024/07/24 12:46:54.411 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 12:46:54.412 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000047FF0000000000000000F7 lock_version: 451366148997906434 key: 748000FFFFFFFFFFFE5F728000000000000047 lock_ttl: 3003 txn_size: 1 lock_type: Del min_commit_ts: 451366148997906435"]
   > [2024/07/24 12:46:54.413 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000047FF0000000000000000F7 lock_version: 451366148997906434 key: 748000FFFFFFFFFFFE5F728000000000000047 lock_ttl: 3003 txn_size: 1 lock_type: Del min_commit_ts: 451366148997906435"]
   > [2024/07/24 12:46:54.416 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=8690506920592671127] [schemaVersion=35] [cur_db=testdb] [sql="create table t (a int, b int, primary key (a, b) /*T![clustered_index] nonclustered */);"] [user=root@%]
   > [2024/07/24 12:46:54.457 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:73, Type:create table, State:queueing, SchemaState:none, SchemaID:70, TableID:72, RowCount:0, ArgLen:2, start time: 2024-07-24 12:46:54.428 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 12:46:54.457 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:73, Type:create table, State:queueing, SchemaState:none, SchemaID:70, TableID:72, RowCount:0, ArgLen:2, start time: 2024-07-24 12:46:54.428 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t (a int, b int, primary key (a, b) /*T![clustered_index] nonclustered */);"]
   > [2024/07/24 12:46:54.478 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:73, Type:create table, State:queueing, SchemaState:none, SchemaID:70, TableID:72, RowCount:0, ArgLen:0, start time: 2024-07-24 12:46:54.428 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:46:54.530 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=35] [neededSchemaVersion=36] ["start time"=2.186124ms] [phyTblIDs="[72]"] [actionTypes="[8]"]
   > [2024/07/24 12:46:54.577 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=36] ["take time"=58.186757ms] [job="ID:73, Type:create table, State:done, SchemaState:public, SchemaID:70, TableID:72, RowCount:0, ArgLen:2, start time: 2024-07-24 12:46:54.428 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:46:54.584 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:73, Type:create table, State:synced, SchemaState:public, SchemaID:70, TableID:72, RowCount:0, ArgLen:0, start time: 2024-07-24 12:46:54.428 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:46:54.604 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=73]
   > [2024/07/24 12:46:54.604 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 12:46:54.604 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=10] ["first split key"=748000000000000048]
   > [2024/07/24 12:46:54.604 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000049FF0000000000000000F7 lock_version: 451366149050335233 key: 748000FFFFFFFFFFFE5F728000000000000049 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451366149050335234"]
   > [2024/07/24 12:46:54.605 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000049FF0000000000000000F7 lock_version: 451366149050335233 key: 748000FFFFFFFFFFFE5F728000000000000049 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451366149050335234"]
   > [2024/07/24 12:46:54.606 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:53386] [split_keys="key 7480000000000000FF4800000000000000F8"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:46:54.606 +00:00] [INFO] [peer.rs:5566] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 37"] [prev_epoch="conf_ver: 1 version: 38"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:46:54.610 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:53392] [split_keys="key 7480000000000000FF4800000000000000F8"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:46:54.610 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=78] [peer-ids="[79]"]
   > [2024/07/24 12:46:54.611 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 10 start_key: 7480000000000000FF4400000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 38 } peers { id: 11 store_id: 1 }"] [new_region_ids="[new_region_id: 78 new_peer_ids: 79]"] [region_id=10]
   > [2024/07/24 12:46:54.615 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF4800000000000000F8 new_region_id: 78 new_peer_ids: 79 } right_derive: true }"] [index=66] [term=6] [peer_id=11] [region_id=10]
   > [2024/07/24 12:46:54.615 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF4800000000000000F8"] [region="id: 10 start_key: 7480000000000000FF4400000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 38 } peers { id: 11 store_id: 1 }"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:46:54.621 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/24 12:46:54.621 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=10]
   > [2024/07/24 12:46:54.621 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(73)] [region_id=10] [store_id=Some(1)]
   > [2024/07/24 12:46:54.622 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 10 start_key: 7480000000000000FF4800000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 12:46:54.622 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=10] ["first at"=748000000000000048] ["first new region left"="{Id:78 StartKey:7480000000000000ff4400000000000000f8 EndKey:7480000000000000ff4800000000000000f8 RegionEpoch:{ConfVer:1 Version:39} Peers:[id:79 store_id:1 ] EncryptionMeta:<nil> IsInFlashback:false}"] ["new region count"=1]
   > [2024/07/24 12:46:54.622 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=11] [region_id=10]
   > [2024/07/24 12:46:54.622 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[78]"]
   > [2024/07/24 12:46:54.622 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 78 start_key: 7480000000000000FF4400000000000000F8 end_key: 7480000000000000FF4800000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 79 store_id: 1 }"] [region_id=78]
   > [2024/07/24 12:46:54.622 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=79] [region_id=78]
   > [2024/07/24 12:46:54.622 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 10 start_key: 7480000000000000FF4800000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 11 store_id: 1 } }"]
   > [2024/07/24 12:46:54.622 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 10 start_key: 7480000000000000FF4800000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 12:46:54.622 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=10] [detail="StartKey Changed:{7480000000000000FF4400000000000000F8} -> {7480000000000000FF4800000000000000F8}, EndKey:{748000FFFFFFFFFFFFFB00000000000000F8}"] [old-version=38] [new-version=39]
   > [2024/07/24 12:46:54.622 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {79} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=79] [region_id=78]
   > [2024/07/24 12:46:54.622 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=10] [origin="id:78 start_key:\"7480000000000000FF4400000000000000F8\" end_key:\"7480000000000000FF4800000000000000F8\" region_epoch:<conf_ver:1 version:39 > peers:<id:79 store_id:1 >"] [total=1]
   > [2024/07/24 12:46:54.622 +00:00] [WARN] [2pc.go:1873] ["schemaLeaseChecker is not set for this transaction"] [sessionID=8690506920592671127] [startTS=451366149050335240] [checkTS=451366149050335242]
   > [2024/07/24 12:46:54.622 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=79] [region_id=78]
   > [2024/07/24 12:46:54.622 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {79} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=79] [region_id=78]
   > [2024/07/24 12:46:54.622 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 79."] [id=79] [raft_id=79] [region_id=78]
   > [2024/07/24 12:46:54.623 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=79] [region_id=78]
   > [2024/07/24 12:46:54.623 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=79] [region_id=78]
   > [2024/07/24 12:46:54.623 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=79] [region_id=78]
   > [2024/07/24 12:46:54.623 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=79] [region_id=78]
   > [2024/07/24 12:46:54.623 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803854] [region_id=78]
   > [2024/07/24 12:46:54.623 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=78]
   > [2024/07/24 12:46:54.626 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 78 start_key: 7480000000000000FF4400000000000000F8 end_key: 7480000000000000FF4800000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 79 store_id: 1 }"]
   > [2024/07/24 12:46:54.626 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=66] [observe_id=ObserveId(75)] [region=10]
   > [2024/07/24 12:46:54.626 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(76)] [region=78]
   > [2024/07/24 12:46:54.631 +00:00] [INFO] [scheduler.rs:640] ["get snapshot failed"] [err="Error(Request(message: \"EpochNotMatch current epoch of region 10 is conf_ver: 1 version: 39, but you sent conf_ver: 1 version: 38\" epoch_not_match { current_regions { id: 10 start_key: 7480000000000000FF4800000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 11 store_id: 1 } } current_regions { id: 78 start_key: 7480000000000000FF4400000000000000F8 end_key: 7480000000000000FF4800000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 79 store_id: 1 } } }))"] [cid=954]
   > [2024/07/24 12:46:55.241 +00:00] [INFO] [info.go:1085] [SetTiFlashGroupConfig]
   > [2024/07/24 12:46:55.656 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/24 12:46:55.685 +00:00] [INFO] [set.go:141] ["set global var"] [conn=8690506920592671129] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/07/24 12:46:55.697 +00:00] [INFO] [manager.go:272] ["revoke session"] ["owner info"="[log-backup] /tidb/br-stream/owner ownerManager 6cf2f012-c9a0-49c4-a69a-4180ab6cf215"] [error="rpc error: code = Canceled desc = grpc: the client connection is closing"]
   > [2024/07/24 12:46:56.860 +00:00] [INFO] [conn.go:1152] ["command dispatched failed"] [conn=8690506920592671129] [connInfo="id:8690506920592671129, addr:10.88.0.83:54848 status:10, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:0, autocommit:1"] [sql=" commit;"] [txn_mode=PESSIMISTIC] [timestamp=451366149404229633] [err="previous statement:  select * from t;: [kv:1062]Duplicate entry '1-10' for key 't.PRIMARY'"]

### Scenario 1
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
   > [2024/07/24 12:47:00.039 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/24 12:47:00.042 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=8690506920592671133] [schemaVersion=44] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/24 12:47:00.083 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:80, Type:drop schema, State:queueing, SchemaState:public, SchemaID:75, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:47:00.028 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 12:47:00.084 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:80, Type:drop schema, State:queueing, SchemaState:public, SchemaID:75, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:47:00.028 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/24 12:47:00.109 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:80, Type:drop schema, State:queueing, SchemaState:public, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:00.028 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:00.160 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=44] [neededSchemaVersion=45] ["start time"=957.743µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:47:00.215 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=45] ["take time"=64.66104ms] [job="ID:80, Type:drop schema, State:running, SchemaState:write only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:00.028 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:00.220 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:80, Type:drop schema, State:running, SchemaState:write only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:00.028 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:00.270 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=45] [neededSchemaVersion=46] ["start time"=766.935µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:47:00.326 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=46] ["take time"=65.417359ms] [job="ID:80, Type:drop schema, State:running, SchemaState:delete only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:00.028 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:00.332 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:80, Type:drop schema, State:running, SchemaState:delete only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:00.028 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:00.383 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=46] [neededSchemaVersion=47] ["start time"=913.114µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:47:00.437 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=47] ["take time"=63.373502ms] [job="ID:80, Type:drop schema, State:done, SchemaState:none, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:00.028 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:00.443 +00:00] [INFO] [delete_range.go:109] ["[ddl] add job into delete-range table"] [jobID=80] [jobType="drop schema"]
   > [2024/07/24 12:47:00.444 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:80, Type:drop schema, State:synced, SchemaState:none, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:00.028 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:00.468 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=80]
   > [2024/07/24 12:47:00.468 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 12:47:00.469 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000050FF0000000000000000F7 lock_version: 451366150583877634 key: 748000FFFFFFFFFFFE5F728000000000000050 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451366150583877635"]
   > [2024/07/24 12:47:00.469 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000050FF0000000000000000F7 lock_version: 451366150583877634 key: 748000FFFFFFFFFFFE5F728000000000000050 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451366150583877635"]
   > [2024/07/24 12:47:00.472 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=8690506920592671133] [schemaVersion=47] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/24 12:47:00.530 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:82, Type:create schema, State:queueing, SchemaState:none, SchemaID:81, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:47:00.478 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 12:47:00.530 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:82, Type:create schema, State:queueing, SchemaState:none, SchemaID:81, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:47:00.478 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/24 12:47:00.556 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:82, Type:create schema, State:queueing, SchemaState:none, SchemaID:81, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:00.478 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:00.602 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=47] [neededSchemaVersion=48] ["start time"=1.477368ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:47:00.650 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=48] ["take time"=57.577666ms] [job="ID:82, Type:create schema, State:done, SchemaState:public, SchemaID:81, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:47:00.478 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:00.657 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:82, Type:create schema, State:synced, SchemaState:public, SchemaID:81, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:00.478 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:00.682 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=82]
   > [2024/07/24 12:47:00.682 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 12:47:00.683 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000052FF0000000000000000F7 lock_version: 451366150636044290 key: 748000FFFFFFFFFFFE5F728000000000000052 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451366150636044291"]
   > [2024/07/24 12:47:00.683 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000052FF0000000000000000F7 lock_version: 451366150636044290 key: 748000FFFFFFFFFFFE5F728000000000000052 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451366150636044291"]
   > [2024/07/24 12:47:00.687 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=8690506920592671133] [schemaVersion=48] [cur_db=testdb] [sql="create table t (a int, b int, primary key (a, b) /*T![clustered_index] nonclustered */);"] [user=root@%]
   > [2024/07/24 12:47:00.746 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:84, Type:create table, State:queueing, SchemaState:none, SchemaID:81, TableID:83, RowCount:0, ArgLen:2, start time: 2024-07-24 12:47:00.678 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 12:47:00.746 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:84, Type:create table, State:queueing, SchemaState:none, SchemaID:81, TableID:83, RowCount:0, ArgLen:2, start time: 2024-07-24 12:47:00.678 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t (a int, b int, primary key (a, b) /*T![clustered_index] nonclustered */);"]
   > [2024/07/24 12:47:00.774 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:84, Type:create table, State:queueing, SchemaState:none, SchemaID:81, TableID:83, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:00.678 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:00.836 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=48] [neededSchemaVersion=49] ["start time"=2.806531ms] [phyTblIDs="[83]"] [actionTypes="[8]"]
   > [2024/07/24 12:47:00.883 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=49] ["take time"=61.746114ms] [job="ID:84, Type:create table, State:done, SchemaState:public, SchemaID:81, TableID:83, RowCount:0, ArgLen:2, start time: 2024-07-24 12:47:00.678 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:00.890 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:84, Type:create table, State:synced, SchemaState:public, SchemaID:81, TableID:83, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:00.678 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:00.915 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=84]
   > [2024/07/24 12:47:00.915 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 12:47:00.915 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=10] ["first split key"=748000000000000053]
   > [2024/07/24 12:47:00.916 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000054FF0000000000000000F7 lock_version: 451366150701580290 key: 748000FFFFFFFFFFFE5F728000000000000054 lock_ttl: 3005 txn_size: 1 lock_type: Del min_commit_ts: 451366150701580291"]
   > [2024/07/24 12:47:00.916 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000054FF0000000000000000F7 lock_version: 451366150701580290 key: 748000FFFFFFFFFFFE5F728000000000000054 lock_ttl: 3005 txn_size: 1 lock_type: Del min_commit_ts: 451366150701580291"]
   > [2024/07/24 12:47:00.919 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:53372] [split_keys="key 7480000000000000FF5300000000000000F8"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:47:00.920 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=82] [peer-ids="[83]"]
   > [2024/07/24 12:47:00.920 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 10 start_key: 7480000000000000FF4D00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 40 } peers { id: 11 store_id: 1 }"] [new_region_ids="[new_region_id: 82 new_peer_ids: 83]"] [region_id=10]
   > [2024/07/24 12:47:00.931 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF5300000000000000F8 new_region_id: 82 new_peer_ids: 83 } right_derive: true }"] [index=70] [term=6] [peer_id=11] [region_id=10]
   > [2024/07/24 12:47:00.931 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF5300000000000000F8"] [region="id: 10 start_key: 7480000000000000FF4D00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 40 } peers { id: 11 store_id: 1 }"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:47:00.941 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/24 12:47:00.941 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=10]
   > [2024/07/24 12:47:00.941 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(77)] [region_id=10] [store_id=Some(1)]
   > [2024/07/24 12:47:00.941 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=11] [region_id=10]
   > [2024/07/24 12:47:00.941 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 10 start_key: 7480000000000000FF5300000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 12:47:00.941 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 82 start_key: 7480000000000000FF4D00000000000000F8 end_key: 7480000000000000FF5300000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 83 store_id: 1 }"] [region_id=82]
   > [2024/07/24 12:47:00.941 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=83] [region_id=82]
   > [2024/07/24 12:47:00.941 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 10 start_key: 7480000000000000FF5300000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 11 store_id: 1 } }"]
   > [2024/07/24 12:47:00.941 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=10] ["first at"=748000000000000053] ["first new region left"="{Id:82 StartKey:7480000000000000ff4d00000000000000f8 EndKey:7480000000000000ff5300000000000000f8 RegionEpoch:{ConfVer:1 Version:41} Peers:[id:83 store_id:1 ] EncryptionMeta:<nil> IsInFlashback:false}"] ["new region count"=1]
   > [2024/07/24 12:47:00.941 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 10 start_key: 7480000000000000FF5300000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 12:47:00.941 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {83} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=83] [region_id=82]
   > [2024/07/24 12:47:00.941 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[82]"]
   > [2024/07/24 12:47:00.941 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=83] [region_id=82]
   > [2024/07/24 12:47:00.941 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=10] [detail="StartKey Changed:{7480000000000000FF4D00000000000000F8} -> {7480000000000000FF5300000000000000F8}, EndKey:{748000FFFFFFFFFFFFFB00000000000000F8}"] [old-version=40] [new-version=41]
   > [2024/07/24 12:47:00.941 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {83} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=83] [region_id=82]
   > [2024/07/24 12:47:00.942 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 83."] [id=83] [raft_id=83] [region_id=82]
   > [2024/07/24 12:47:00.942 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=83] [region_id=82]
   > [2024/07/24 12:47:00.942 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=83] [region_id=82]
   > [2024/07/24 12:47:00.942 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=83] [region_id=82]
   > [2024/07/24 12:47:00.942 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=83] [region_id=82]
   > [2024/07/24 12:47:00.942 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803858] [region_id=82]
   > [2024/07/24 12:47:00.942 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=10] [origin="id:82 start_key:\"7480000000000000FF4D00000000000000F8\" end_key:\"7480000000000000FF5300000000000000F8\" region_epoch:<conf_ver:1 version:41 > peers:<id:83 store_id:1 >"] [total=1]
   > [2024/07/24 12:47:00.942 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=70] [observe_id=ObserveId(79)] [region=10]
   > [2024/07/24 12:47:00.942 +00:00] [WARN] [2pc.go:1873] ["schemaLeaseChecker is not set for this transaction"] [sessionID=8690506920592671133] [startTS=451366150701580297] [checkTS=451366150714949633]
   > [2024/07/24 12:47:00.942 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=82]
   > [2024/07/24 12:47:00.947 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 82 start_key: 7480000000000000FF4D00000000000000F8 end_key: 7480000000000000FF5300000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 83 store_id: 1 }"]
   > [2024/07/24 12:47:00.948 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(80)] [region=82]
   > [2024/07/24 12:47:00.954 +00:00] [INFO] [scheduler.rs:640] ["get snapshot failed"] [err="Error(Request(message: \"EpochNotMatch current epoch of region 10 is conf_ver: 1 version: 41, but you sent conf_ver: 1 version: 40\" epoch_not_match { current_regions { id: 10 start_key: 7480000000000000FF5300000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 11 store_id: 1 } } current_regions { id: 82 start_key: 7480000000000000FF4D00000000000000F8 end_key: 7480000000000000FF5300000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 83 store_id: 1 } } }))"] [cid=1188]
   > [2024/07/24 12:47:01.974 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/24 12:47:02.015 +00:00] [INFO] [set.go:141] ["set global var"] [conn=8690506920592671135] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/07/24 12:47:02.576 +00:00] [INFO] [conn.go:1152] ["command dispatched failed"] [conn=8690506920592671135] [connInfo="id:8690506920592671135, addr:10.88.0.83:36084 status:11, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:1, autocommit:1"] [sql=" insert into t values (1, 10);"] [txn_mode=PESSIMISTIC] [timestamp=451366151055736838] [err="[kv:1062]Duplicate entry '1-10' for key 't.PRIMARY'"]

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
   > [2024/07/24 12:47:06.422 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/24 12:47:06.425 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=8690506920592671139] [schemaVersion=57] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/24 12:47:06.463 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:91, Type:drop schema, State:queueing, SchemaState:public, SchemaID:86, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:47:06.428 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 12:47:06.463 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:91, Type:drop schema, State:queueing, SchemaState:public, SchemaID:86, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:47:06.428 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/24 12:47:06.487 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:91, Type:drop schema, State:queueing, SchemaState:public, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:06.428 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:06.536 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=57] [neededSchemaVersion=58] ["start time"=802.694µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:47:06.584 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=58] ["take time"=57.604903ms] [job="ID:91, Type:drop schema, State:running, SchemaState:write only, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:06.428 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:06.589 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:91, Type:drop schema, State:running, SchemaState:write only, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:06.428 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:06.646 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=58] [neededSchemaVersion=59] ["start time"=947.896µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:47:06.695 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=59] ["take time"=57.788657ms] [job="ID:91, Type:drop schema, State:running, SchemaState:delete only, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:06.428 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:06.700 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:91, Type:drop schema, State:running, SchemaState:delete only, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:06.428 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:06.755 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=59] [neededSchemaVersion=60] ["start time"=837.476µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:47:06.804 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=60] ["take time"=66.26964ms] [job="ID:91, Type:drop schema, State:done, SchemaState:none, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:06.428 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:06.810 +00:00] [INFO] [delete_range.go:109] ["[ddl] add job into delete-range table"] [jobID=91] [jobType="drop schema"]
   > [2024/07/24 12:47:06.811 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:91, Type:drop schema, State:synced, SchemaState:none, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:06.428 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:06.832 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=91]
   > [2024/07/24 12:47:06.832 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 12:47:06.833 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000005BFF0000000000000000F7 lock_version: 451366152248492034 key: 748000FFFFFFFFFFFE5F72800000000000005B lock_ttl: 3005 txn_size: 1 lock_type: Del min_commit_ts: 451366152248492035"]
   > [2024/07/24 12:47:06.833 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000005BFF0000000000000000F7 lock_version: 451366152248492034 key: 748000FFFFFFFFFFFE5F72800000000000005B lock_ttl: 3005 txn_size: 1 lock_type: Del min_commit_ts: 451366152248492035"]
   > [2024/07/24 12:47:06.836 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=8690506920592671139] [schemaVersion=60] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/24 12:47:06.839 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000005BFF0000000000000000F7 lock_version: 451366152248492034 key: 748000FFFFFFFFFFFE5F72800000000000005B lock_ttl: 3005 txn_size: 1 lock_type: Del min_commit_ts: 451366152248492035"]
   > [2024/07/24 12:47:06.839 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000005BFF0000000000000000F7 lock_version: 451366152248492034 key: 748000FFFFFFFFFFFE5F72800000000000005B lock_ttl: 3005 txn_size: 1 lock_type: Del min_commit_ts: 451366152248492035"]
   > [2024/07/24 12:47:06.899 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:93, Type:create schema, State:queueing, SchemaState:none, SchemaID:92, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:47:06.827 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 12:47:06.899 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:93, Type:create schema, State:queueing, SchemaState:none, SchemaID:92, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:47:06.827 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/24 12:47:06.925 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:93, Type:create schema, State:queueing, SchemaState:none, SchemaID:92, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:06.827 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:06.976 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=60] [neededSchemaVersion=61] ["start time"=1.486866ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:47:07.024 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=61] ["take time"=57.975694ms] [job="ID:93, Type:create schema, State:done, SchemaState:public, SchemaID:92, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:47:06.827 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:07.032 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:93, Type:create schema, State:synced, SchemaState:public, SchemaID:92, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:06.827 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:07.061 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=93]
   > [2024/07/24 12:47:07.061 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 12:47:07.062 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000005DFF0000000000000000F7 lock_version: 451366152314028033 key: 748000FFFFFFFFFFFE5F72800000000000005D lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451366152314028034"]
   > [2024/07/24 12:47:07.062 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000005DFF0000000000000000F7 lock_version: 451366152314028033 key: 748000FFFFFFFFFFFE5F72800000000000005D lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451366152314028034"]
   > [2024/07/24 12:47:07.066 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=8690506920592671139] [schemaVersion=61] [cur_db=testdb] [sql="create table t (a int, b int, primary key (a, b) /*T![clustered_index] nonclustered */);"] [user=root@%]
   > [2024/07/24 12:47:07.122 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:95, Type:create table, State:queueing, SchemaState:none, SchemaID:92, TableID:94, RowCount:0, ArgLen:2, start time: 2024-07-24 12:47:07.078 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 12:47:07.122 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:95, Type:create table, State:queueing, SchemaState:none, SchemaID:92, TableID:94, RowCount:0, ArgLen:2, start time: 2024-07-24 12:47:07.078 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t (a int, b int, primary key (a, b) /*T![clustered_index] nonclustered */);"]
   > [2024/07/24 12:47:07.148 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:95, Type:create table, State:queueing, SchemaState:none, SchemaID:92, TableID:94, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:07.078 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:07.215 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=61] [neededSchemaVersion=62] ["start time"=2.199395ms] [phyTblIDs="[94]"] [actionTypes="[8]"]
   > [2024/07/24 12:47:07.262 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=62] ["take time"=63.256797ms] [job="ID:95, Type:create table, State:done, SchemaState:public, SchemaID:92, TableID:94, RowCount:0, ArgLen:2, start time: 2024-07-24 12:47:07.078 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:07.268 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:95, Type:create table, State:synced, SchemaState:public, SchemaID:92, TableID:94, RowCount:0, ArgLen:0, start time: 2024-07-24 12:47:07.078 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:47:07.304 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=95]
   > [2024/07/24 12:47:07.304 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000005FFF0000000000000000F7 lock_version: 451366152366456838 key: 748000FFFFFFFFFFFE5F72800000000000005F lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451366152366456839"]
   > [2024/07/24 12:47:07.304 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000005FFF0000000000000000F7 lock_version: 451366152366456838 key: 748000FFFFFFFFFFFE5F72800000000000005F lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451366152366456839"]
   > [2024/07/24 12:47:07.304 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=10] ["first split key"=74800000000000005e]
   > [2024/07/24 12:47:07.304 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 12:47:07.310 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000005FFF0000000000000000F7 lock_version: 451366152366456838 key: 748000FFFFFFFFFFFE5F72800000000000005F lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451366152366456839"]
   > [2024/07/24 12:47:07.310 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000005FFF0000000000000000F7 lock_version: 451366152366456838 key: 748000FFFFFFFFFFFE5F72800000000000005F lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451366152366456839"]
   > [2024/07/24 12:47:07.311 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:53386] [split_keys="key 7480000000000000FF5E00000000000000F8"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:47:07.311 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=86] [peer-ids="[87]"]
   > [2024/07/24 12:47:07.312 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 10 start_key: 7480000000000000FF5800000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 42 } peers { id: 11 store_id: 1 }"] [new_region_ids="[new_region_id: 86 new_peer_ids: 87]"] [region_id=10]
   > [2024/07/24 12:47:07.324 +00:00] [WARN] [2pc.go:1873] ["schemaLeaseChecker is not set for this transaction"] [sessionID=8690506920592671139] [startTS=451366152379564038] [checkTS=451366152379564040]
   > [2024/07/24 12:47:07.328 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF5E00000000000000F8 new_region_id: 86 new_peer_ids: 87 } right_derive: true }"] [index=74] [term=6] [peer_id=11] [region_id=10]
   > [2024/07/24 12:47:07.328 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF5E00000000000000F8"] [region="id: 10 start_key: 7480000000000000FF5800000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 42 } peers { id: 11 store_id: 1 }"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:47:07.339 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/24 12:47:07.339 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=10]
   > [2024/07/24 12:47:07.339 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(81)] [region_id=10] [store_id=Some(1)]
   > [2024/07/24 12:47:07.339 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=11] [region_id=10]
   > [2024/07/24 12:47:07.340 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 10 start_key: 7480000000000000FF5E00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 43 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 12:47:07.340 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=10] [detail="StartKey Changed:{7480000000000000FF5800000000000000F8} -> {7480000000000000FF5E00000000000000F8}, EndKey:{748000FFFFFFFFFFFFFB00000000000000F8}"] [old-version=42] [new-version=43]
   > [2024/07/24 12:47:07.340 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=10] ["first at"=74800000000000005e] ["first new region left"="{Id:86 StartKey:7480000000000000ff5800000000000000f8 EndKey:7480000000000000ff5e00000000000000f8 RegionEpoch:{ConfVer:1 Version:43} Peers:[id:87 store_id:1 ] EncryptionMeta:<nil> IsInFlashback:false}"] ["new region count"=1]
   > [2024/07/24 12:47:07.340 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 86 start_key: 7480000000000000FF5800000000000000F8 end_key: 7480000000000000FF5E00000000000000F8 region_epoch { conf_ver: 1 version: 43 } peers { id: 87 store_id: 1 }"] [region_id=86]
   > [2024/07/24 12:47:07.340 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[86]"]
   > [2024/07/24 12:47:07.340 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=87] [region_id=86]
   > [2024/07/24 12:47:07.340 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 10 start_key: 7480000000000000FF5E00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 43 } peers { id: 11 store_id: 1 } }"]
   > [2024/07/24 12:47:07.340 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 10 start_key: 7480000000000000FF5E00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 43 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 12:47:07.340 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {87} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=87] [region_id=86]
   > [2024/07/24 12:47:07.340 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=10] [origin="id:86 start_key:\"7480000000000000FF5800000000000000F8\" end_key:\"7480000000000000FF5E00000000000000F8\" region_epoch:<conf_ver:1 version:43 > peers:<id:87 store_id:1 >"] [total=1]
   > [2024/07/24 12:47:07.340 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=87] [region_id=86]
   > [2024/07/24 12:47:07.340 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {87} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=87] [region_id=86]
   > [2024/07/24 12:47:07.340 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 87."] [id=87] [raft_id=87] [region_id=86]
   > [2024/07/24 12:47:07.340 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=87] [region_id=86]
   > [2024/07/24 12:47:07.340 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=87] [region_id=86]
   > [2024/07/24 12:47:07.341 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=87] [region_id=86]
   > [2024/07/24 12:47:07.341 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=87] [region_id=86]
   > [2024/07/24 12:47:07.341 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803862] [region_id=86]
   > [2024/07/24 12:47:07.341 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=74] [observe_id=ObserveId(83)] [region=10]
   > [2024/07/24 12:47:07.341 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=86]
   > [2024/07/24 12:47:07.341 +00:00] [INFO] [scheduler.rs:640] ["get snapshot failed"] [err="Error(Request(message: \"EpochNotMatch current epoch of region 10 is conf_ver: 1 version: 43, but you sent conf_ver: 1 version: 42\" epoch_not_match { current_regions { id: 10 start_key: 7480000000000000FF5E00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 43 } peers { id: 11 store_id: 1 } } current_regions { id: 86 start_key: 7480000000000000FF5800000000000000F8 end_key: 7480000000000000FF5E00000000000000F8 region_epoch { conf_ver: 1 version: 43 } peers { id: 87 store_id: 1 } } }))"] [cid=1423]
   > [2024/07/24 12:47:07.346 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 86 start_key: 7480000000000000FF5800000000000000F8 end_key: 7480000000000000FF5E00000000000000F8 region_epoch { conf_ver: 1 version: 43 } peers { id: 87 store_id: 1 }"]
   > [2024/07/24 12:47:07.346 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(84)] [region=86]
   > [2024/07/24 12:47:08.365 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/24 12:47:08.373 +00:00] [INFO] [conn.go:1152] ["command dispatched failed"] [conn=8690506920592671141] [connInfo="id:8690506920592671141, addr:10.88.0.83:36128 status:10, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:0, autocommit:1"] [sql=" insert into t values (1, 10);"] [txn_mode=PESSIMISTIC] [timestamp=451366152654815241] [err="[kv:1062]Duplicate entry '1-10' for key 't.PRIMARY'"]
