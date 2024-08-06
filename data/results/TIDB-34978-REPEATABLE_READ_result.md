# Bug ID TIDB-34978-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/34978
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              A SELECT throws an error after a DML operation in another transaction.


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
   > [2024/08/06 16:16:30.644 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/08/06 16:16:30.649 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=5357761832478048661] [schemaVersion=34] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/08/06 16:16:30.650 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=5357761832478048661] [schemaVersion=34] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/08/06 16:16:30.702 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:71, Type:create schema, State:queueing, SchemaState:none, SchemaID:70, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-06 16:16:30.652 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/08/06 16:16:30.702 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:71, Type:create schema, State:queueing, SchemaState:none, SchemaID:70, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-06 16:16:30.652 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/08/06 16:16:30.708 +00:00] [INFO] [manager.go:151] ["start campaign owner"] [ownerInfo="[telemetry] /tidb/telemetry/owner"]
   > [2024/08/06 16:16:30.727 +00:00] [INFO] [manager.go:296] ["get owner"] ["owner info"="[telemetry] /tidb/telemetry/owner ownerManager 6f399a05-7147-4bc5-94a8-144c927cf2bf"] [ownerID=6f399a05-7147-4bc5-94a8-144c927cf2bf]
   > [2024/08/06 16:16:30.731 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:71, Type:create schema, State:queueing, SchemaState:none, SchemaID:70, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-06 16:16:30.652 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:16:30.790 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=34] [neededSchemaVersion=35] ["start time"=1.570745ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/06 16:16:30.838 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=35] ["take time"=58.493311ms] [job="ID:71, Type:create schema, State:done, SchemaState:public, SchemaID:70, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-06 16:16:30.652 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:16:30.844 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:71, Type:create schema, State:synced, SchemaState:public, SchemaID:70, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-06 16:16:30.652 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:16:30.869 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=71]
   > [2024/08/06 16:16:30.869 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/08/06 16:16:30.870 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000047FF0000000000000000F7 lock_version: 451663885972799490 key: 748000FFFFFFFFFFFE5F728000000000000047 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451663885972799491"]
   > [2024/08/06 16:16:30.870 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000047FF0000000000000000F7 lock_version: 451663885972799490 key: 748000FFFFFFFFFFFE5F728000000000000047 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451663885972799491"]
   > [2024/08/06 16:16:30.874 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=5357761832478048661] [schemaVersion=35] [cur_db=testdb] [sql="create table t (id int primary key, c int not null);"] [user=root@%]
   > [2024/08/06 16:16:30.876 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000047FF0000000000000000F7 lock_version: 451663885972799490 key: 748000FFFFFFFFFFFE5F728000000000000047 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451663885972799491"]
   > [2024/08/06 16:16:30.876 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000047FF0000000000000000F7 lock_version: 451663885972799490 key: 748000FFFFFFFFFFFE5F728000000000000047 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451663885972799491"]
   > [2024/08/06 16:16:30.935 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:73, Type:create table, State:queueing, SchemaState:none, SchemaID:70, TableID:72, RowCount:0, ArgLen:2, start time: 2024-08-06 16:16:30.902 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/08/06 16:16:30.935 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:73, Type:create table, State:queueing, SchemaState:none, SchemaID:70, TableID:72, RowCount:0, ArgLen:2, start time: 2024-08-06 16:16:30.902 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t (id int primary key, c int not null);"]
   > [2024/08/06 16:16:30.960 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:73, Type:create table, State:queueing, SchemaState:none, SchemaID:70, TableID:72, RowCount:0, ArgLen:0, start time: 2024-08-06 16:16:30.902 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:16:31.021 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=35] [neededSchemaVersion=36] ["start time"=2.571719ms] [phyTblIDs="[72]"] [actionTypes="[8]"]
   > [2024/08/06 16:16:31.068 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=36] ["take time"=61.464038ms] [job="ID:73, Type:create table, State:done, SchemaState:public, SchemaID:70, TableID:72, RowCount:0, ArgLen:2, start time: 2024-08-06 16:16:30.902 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:16:31.075 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:73, Type:create table, State:synced, SchemaState:public, SchemaID:70, TableID:72, RowCount:0, ArgLen:0, start time: 2024-08-06 16:16:30.902 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:16:31.104 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=73]
   > [2024/08/06 16:16:31.104 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/08/06 16:16:31.105 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=10] ["first split key"=748000000000000048]
   > [2024/08/06 16:16:31.106 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000049FF0000000000000000F7 lock_version: 451663886038597634 key: 748000FFFFFFFFFFFE5F728000000000000049 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451663886038597635"]
   > [2024/08/06 16:16:31.106 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000049FF0000000000000000F7 lock_version: 451663886038597634 key: 748000FFFFFFFFFFFE5F728000000000000049 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451663886038597635"]
   > [2024/08/06 16:16:31.111 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000049FF0000000000000000F7 lock_version: 451663886038597634 key: 748000FFFFFFFFFFFE5F728000000000000049 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451663886038597635"]
   > [2024/08/06 16:16:31.111 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000049FF0000000000000000F7 lock_version: 451663886038597634 key: 748000FFFFFFFFFFFE5F728000000000000049 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451663886038597635"]
   > [2024/08/06 16:16:31.112 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:40772] [split_keys="key 7480000000000000FF4800000000000000F8"] [peer_id=11] [region_id=10]
   > [2024/08/06 16:16:31.112 +00:00] [INFO] [peer.rs:5566] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 37"] [prev_epoch="conf_ver: 1 version: 38"] [peer_id=11] [region_id=10]
   > [2024/08/06 16:16:31.112 +00:00] [INFO] [scheduler.rs:640] ["get snapshot failed"] [err="Error(Request(message: \"EpochNotMatch current epoch of region 10 is conf_ver: 1 version: 38, but you sent conf_ver: 1 version: 37\" epoch_not_match { current_regions { id: 10 start_key: 7480000000000000FF4400000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 38 } peers { id: 11 store_id: 1 } } current_regions { id: 76 start_key: 7480000000000000FF4200000000000000F8 end_key: 7480000000000000FF4400000000000000F8 region_epoch { conf_ver: 1 version: 38 } peers { id: 77 store_id: 1 } } }))"] [cid=979]
   > [2024/08/06 16:16:31.123 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:40752] [split_keys="key 7480000000000000FF4800000000000000F8"] [peer_id=11] [region_id=10]
   > [2024/08/06 16:16:31.124 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=78] [peer-ids="[79]"]
   > [2024/08/06 16:16:31.124 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 10 start_key: 7480000000000000FF4400000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 38 } peers { id: 11 store_id: 1 }"] [new_region_ids="[new_region_id: 78 new_peer_ids: 79]"] [region_id=10]
   > [2024/08/06 16:16:31.130 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF4800000000000000F8 new_region_id: 78 new_peer_ids: 79 } right_derive: true }"] [index=67] [term=6] [peer_id=11] [region_id=10]
   > [2024/08/06 16:16:31.131 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF4800000000000000F8"] [region="id: 10 start_key: 7480000000000000FF4400000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 38 } peers { id: 11 store_id: 1 }"] [peer_id=11] [region_id=10]
   > [2024/08/06 16:16:31.138 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/08/06 16:16:31.138 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=10]
   > [2024/08/06 16:16:31.138 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(73)] [region_id=10] [store_id=Some(1)]
   > [2024/08/06 16:16:31.138 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=11] [region_id=10]
   > [2024/08/06 16:16:31.138 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=10] ["first at"=748000000000000048] ["first new region left"="{Id:78 StartKey:7480000000000000ff4400000000000000f8 EndKey:7480000000000000ff4800000000000000f8 RegionEpoch:{ConfVer:1 Version:39} Peers:[id:79 store_id:1 ] EncryptionMeta:<nil> IsInFlashback:false}"] ["new region count"=1]
   > [2024/08/06 16:16:31.138 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 10 start_key: 7480000000000000FF4800000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 11 store_id: 1 }"]
   > [2024/08/06 16:16:31.138 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[78]"]
   > [2024/08/06 16:16:31.138 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 78 start_key: 7480000000000000FF4400000000000000F8 end_key: 7480000000000000FF4800000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 79 store_id: 1 }"] [region_id=78]
   > [2024/08/06 16:16:31.139 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=10] [detail="StartKey Changed:{7480000000000000FF4400000000000000F8} -> {7480000000000000FF4800000000000000F8}, EndKey:{748000FFFFFFFFFFFFFB00000000000000F8}"] [old-version=38] [new-version=39]
   > [2024/08/06 16:16:31.139 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=79] [region_id=78]
   > [2024/08/06 16:16:31.139 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 10 start_key: 7480000000000000FF4800000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 11 store_id: 1 } }"]
   > [2024/08/06 16:16:31.139 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {79} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=79] [region_id=78]
   > [2024/08/06 16:16:31.139 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=79] [region_id=78]
   > [2024/08/06 16:16:31.139 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {79} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=79] [region_id=78]
   > [2024/08/06 16:16:31.139 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 79."] [id=79] [raft_id=79] [region_id=78]
   > [2024/08/06 16:16:31.139 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=79] [region_id=78]
   > [2024/08/06 16:16:31.139 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=79] [region_id=78]
   > [2024/08/06 16:16:31.139 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=79] [region_id=78]
   > [2024/08/06 16:16:31.140 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=79] [region_id=78]
   > [2024/08/06 16:16:31.140 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803854] [region_id=78]
   > [2024/08/06 16:16:31.140 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 10 start_key: 7480000000000000FF4800000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 11 store_id: 1 }"]
   > [2024/08/06 16:16:31.141 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=10] [origin="id:78 start_key:\"7480000000000000FF4400000000000000F8\" end_key:\"7480000000000000FF4800000000000000F8\" region_epoch:<conf_ver:1 version:39 > peers:<id:79 store_id:1 >"] [total=1]
   > [2024/08/06 16:16:31.141 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=78]
   > [2024/08/06 16:16:31.145 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=67] [observe_id=ObserveId(75)] [region=10]
   > [2024/08/06 16:16:31.145 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 78 start_key: 7480000000000000FF4400000000000000F8 end_key: 7480000000000000FF4800000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 79 store_id: 1 }"]
   > [2024/08/06 16:16:31.145 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(76)] [region=78]
   > [2024/08/06 16:16:31.577 +00:00] [INFO] [info.go:1085] [SetTiFlashGroupConfig]
   > [2024/08/06 16:16:31.842 +00:00] [WARN] [server.go:591] ["Server.onConn handshake"] [conn=5357761832478048663] [error="read tcp 192.168.100.114:4000->192.168.100.114:43396: read: connection reset by peer"] ["remote addr"=192.168.100.114:43396]
   > [2024/08/06 16:16:32.030 +00:00] [INFO] [manager.go:272] ["revoke session"] ["owner info"="[log-backup] /tidb/br-stream/owner ownerManager e4fbf86f-07d5-41c9-b9d1-00246b57e653"] [error="rpc error: code = Canceled desc = grpc: the client connection is closing"]
   > [2024/08/06 16:16:32.167 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/08/06 16:16:32.218 +00:00] [INFO] [set.go:141] ["set global var"] [conn=5357761832478048665] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/08/06 16:16:32.776 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/08/06 16:16:32.781 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=5357761832478048667] [schemaVersion=36] [cur_db=testdb] [sql=" alter table t drop column c;"] [user=root@%]
   > [2024/08/06 16:16:32.822 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:74, Type:drop column, State:queueing, SchemaState:public, SchemaID:70, TableID:72, RowCount:0, ArgLen:2, start time: 2024-08-06 16:16:32.752 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/08/06 16:16:32.823 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:74, Type:drop column, State:queueing, SchemaState:public, SchemaID:70, TableID:72, RowCount:0, ArgLen:2, start time: 2024-08-06 16:16:32.752 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query=" alter table t drop column c;"]
   > [2024/08/06 16:16:32.848 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:74, Type:drop column, State:queueing, SchemaState:public, SchemaID:70, TableID:72, RowCount:0, ArgLen:0, start time: 2024-08-06 16:16:32.752 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:16:32.903 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=36] [neededSchemaVersion=37] ["start time"=2.439787ms] [phyTblIDs="[72]"] [actionTypes="[64]"]
   > [2024/08/06 16:16:32.950 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=37] ["take time"=58.570487ms] [job="ID:74, Type:drop column, State:running, SchemaState:write only, SchemaID:70, TableID:72, RowCount:0, ArgLen:2, start time: 2024-08-06 16:16:32.752 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:16:32.955 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:74, Type:drop column, State:running, SchemaState:write only, SchemaID:70, TableID:72, RowCount:0, ArgLen:0, start time: 2024-08-06 16:16:32.752 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:16:33.016 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=37] [neededSchemaVersion=38] ["start time"=2.516544ms] [phyTblIDs="[72]"] [actionTypes="[64]"]
   > [2024/08/06 16:16:33.063 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=38] ["take time"=59.015938ms] [job="ID:74, Type:drop column, State:running, SchemaState:delete only, SchemaID:70, TableID:72, RowCount:0, ArgLen:3, start time: 2024-08-06 16:16:32.752 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:16:33.068 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:74, Type:drop column, State:running, SchemaState:delete only, SchemaID:70, TableID:72, RowCount:0, ArgLen:0, start time: 2024-08-06 16:16:32.752 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:16:33.125 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=38] [neededSchemaVersion=39] ["start time"=2.371553ms] [phyTblIDs="[72]"] [actionTypes="[64]"]
   > [2024/08/06 16:16:33.172 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=39] ["take time"=59.189566ms] [job="ID:74, Type:drop column, State:running, SchemaState:delete reorganization, SchemaID:70, TableID:72, RowCount:0, ArgLen:3, start time: 2024-08-06 16:16:32.752 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:16:33.178 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:74, Type:drop column, State:running, SchemaState:delete reorganization, SchemaID:70, TableID:72, RowCount:0, ArgLen:0, start time: 2024-08-06 16:16:32.752 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:16:33.235 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=39] [neededSchemaVersion=40] ["start time"=2.227818ms] [phyTblIDs="[72]"] [actionTypes="[64]"]
   > [2024/08/06 16:16:33.282 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=40] ["take time"=59.158555ms] [job="ID:74, Type:drop column, State:done, SchemaState:none, SchemaID:70, TableID:72, RowCount:0, ArgLen:4, start time: 2024-08-06 16:16:32.752 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:16:33.288 +00:00] [INFO] [delete_range.go:109] ["[ddl] add job into delete-range table"] [jobID=74] [jobType="drop column"]
   > [2024/08/06 16:16:33.290 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:74, Type:drop column, State:synced, SchemaState:none, SchemaID:70, TableID:72, RowCount:0, ArgLen:4, start time: 2024-08-06 16:16:32.752 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:16:33.319 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=74]
   > [2024/08/06 16:16:33.319 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/08/06 16:16:33.321 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000004AFF0000000000000000F7 lock_version: 451663886615052290 key: 748000FFFFFFFFFFFE5F72800000000000004A lock_ttl: 3005 txn_size: 1 lock_type: Del min_commit_ts: 451663886615052291"]
   > [2024/08/06 16:16:33.321 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000004AFF0000000000000000F7 lock_version: 451663886615052290 key: 748000FFFFFFFFFFFE5F72800000000000004A lock_ttl: 3005 txn_size: 1 lock_type: Del min_commit_ts: 451663886615052291"]
   > [2024/08/06 16:16:33.326 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000004AFF0000000000000000F7 lock_version: 451663886615052290 key: 748000FFFFFFFFFFFE5F72800000000000004A lock_ttl: 3005 txn_size: 1 lock_type: Del min_commit_ts: 451663886615052291"]
   > [2024/08/06 16:16:33.326 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000004AFF0000000000000000F7 lock_version: 451663886615052290 key: 748000FFFFFFFFFFFE5F72800000000000004A lock_ttl: 3005 txn_size: 1 lock_type: Del min_commit_ts: 451663886615052291"]
   > [2024/08/06 16:16:33.327 +00:00] [INFO] [scheduler.rs:640] ["get snapshot failed"] [err="Error(Request(message: \"EpochNotMatch current epoch of region 10 is conf_ver: 1 version: 39, but you sent conf_ver: 1 version: 38\" epoch_not_match { current_regions { id: 10 start_key: 7480000000000000FF4800000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 11 store_id: 1 } } current_regions { id: 78 start_key: 7480000000000000FF4400000000000000F8 end_key: 7480000000000000FF4800000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 79 store_id: 1 } } }))"] [cid=1023]
   > [2024/08/06 16:16:33.378 +00:00] [WARN] [session.go:2191] ["run statement failed"] [conn=5357761832478048665] [schemaVersion=36] [error="[tikv:10000][components/tidb_query_executors/src/table_scan_executor.rs:422]: Data is corrupted, missing data for NOT NULL column (offset = 1)"] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 5357761832478048665,\n  \"status\": 3,\n  \"strictMode\": true,\n  \"txn\": \"451663886405599233\",\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"127.0.0.1\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/08/06 16:16:33.379 +00:00] [INFO] [conn.go:1152] ["command dispatched failed"] [conn=5357761832478048665] [connInfo="id:5357761832478048665, addr:127.0.0.1:51780 status:11, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:1, autocommit:1"] [sql=" select * from t for update;"] [txn_mode=PESSIMISTIC] [timestamp=451663886405599233] [err="[tikv:10000][components/tidb_query_executors/src/table_scan_executor.rs:422]: Data is corrupted, missing data for NOT NULL column (offset = 1)"]
