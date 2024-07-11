# Bug ID TIDB-39976-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/39976
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              Reports error instead of warning when running in a transaction.


## Details
 * Database: tidb-v6.4.0.tikv
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
     - Instruction:  REPLACE INTO t VALUES ('G6y*k]88]');
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 1 / 0
 * Instruction #3:
     - Instruction:  DELETE FROM t WHERE CAST(TIDB_VERSION() AS DATE);
     - Transaction: conn_0
     - Output: ERROR: 1292 (22007): Incorrect datetime value: 'Release Version: v6.4.0
Edition: Community
Git Commit Hash: cf36a9ce2fe1039db3cf3444d51930b887df18a1
Git Branch: heads/refs/tags'
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #4:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 0 / 0

 * Container logs:
   > [2024/07/11 15:25:44.788 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/11 15:25:44.792 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=8833764489598861719] [schemaVersion=34] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/11 15:25:44.794 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=8833764489598861719] [schemaVersion=34] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/11 15:25:44.833 +00:00] [INFO] [info.go:1085] [SetTiFlashGroupConfig]
   > [2024/07/11 15:25:44.834 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 748000FFFFFFFFFFFE5F728000000000000047 lock_version: 451074207206866945 key: 748000FFFFFFFFFFFE5F728000000000000047 lock_ttl: 3000 txn_size: 1 min_commit_ts: 451074207206866946"]
   > [2024/07/11 15:25:44.835 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 748000FFFFFFFFFFFE5F728000000000000047 lock_version: 451074207206866945 key: 748000FFFFFFFFFFFE5F728000000000000047 lock_ttl: 3000 txn_size: 1 min_commit_ts: 451074207206866946"]
   > [2024/07/11 15:25:44.842 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:71, Type:create schema, State:queueing, SchemaState:none, SchemaID:70, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-11 15:25:44.776 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/11 15:25:44.842 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:71, Type:create schema, State:queueing, SchemaState:none, SchemaID:70, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-11 15:25:44.776 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/11 15:25:44.871 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:71, Type:create schema, State:queueing, SchemaState:none, SchemaID:70, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-11 15:25:44.776 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/11 15:25:44.920 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=34] [neededSchemaVersion=35] ["start time"=1.774828ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/11 15:25:44.967 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=35] ["take time"=57.872017ms] [job="ID:71, Type:create schema, State:done, SchemaState:public, SchemaID:70, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-11 15:25:44.776 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/11 15:25:44.973 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:71, Type:create schema, State:synced, SchemaState:public, SchemaID:70, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-11 15:25:44.776 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/11 15:25:44.999 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=71]
   > [2024/07/11 15:25:44.999 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/11 15:25:45.000 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000047FF0000000000000000F7 lock_version: 451074207233081347 key: 748000FFFFFFFFFFFE5F728000000000000047 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451074207233081348"]
   > [2024/07/11 15:25:45.000 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000047FF0000000000000000F7 lock_version: 451074207233081347 key: 748000FFFFFFFFFFFE5F728000000000000047 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451074207233081348"]
   > [2024/07/11 15:25:45.004 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=8833764489598861719] [schemaVersion=35] [cur_db=testdb] [sql="CREATE TABLE t(c0 TEXT(284));"] [user=root@%]
   > [2024/07/11 15:25:45.054 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:73, Type:create table, State:queueing, SchemaState:none, SchemaID:70, TableID:72, RowCount:0, ArgLen:2, start time: 2024-07-11 15:25:44.977 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/11 15:25:45.055 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:73, Type:create table, State:queueing, SchemaState:none, SchemaID:70, TableID:72, RowCount:0, ArgLen:2, start time: 2024-07-11 15:25:44.977 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE t(c0 TEXT(284));"]
   > [2024/07/11 15:25:45.078 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:73, Type:create table, State:queueing, SchemaState:none, SchemaID:70, TableID:72, RowCount:0, ArgLen:0, start time: 2024-07-11 15:25:44.977 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/11 15:25:45.130 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=35] [neededSchemaVersion=36] ["start time"=2.110629ms] [phyTblIDs="[72]"] [actionTypes="[8]"]
   > [2024/07/11 15:25:45.181 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=36] ["take time"=64.689585ms] [job="ID:73, Type:create table, State:done, SchemaState:public, SchemaID:70, TableID:72, RowCount:0, ArgLen:2, start time: 2024-07-11 15:25:44.977 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/11 15:25:45.187 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:73, Type:create table, State:synced, SchemaState:public, SchemaID:70, TableID:72, RowCount:0, ArgLen:0, start time: 2024-07-11 15:25:44.977 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/11 15:25:45.212 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=73]
   > [2024/07/11 15:25:45.212 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/11 15:25:45.212 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=10] ["first split key"=748000000000000048]
   > [2024/07/11 15:25:45.212 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:59892] [split_keys="key 7480000000000000FF4800000000000000F8"] [peer_id=11] [region_id=10]
   > [2024/07/11 15:25:45.213 +00:00] [INFO] [peer.rs:5566] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 37"] [prev_epoch="conf_ver: 1 version: 38"] [peer_id=11] [region_id=10]
   > [2024/07/11 15:25:45.213 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000049FF0000000000000000F7 lock_version: 451074207298879490 key: 748000FFFFFFFFFFFE5F728000000000000049 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451074207298879491"]
   > [2024/07/11 15:25:45.213 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000049FF0000000000000000F7 lock_version: 451074207298879490 key: 748000FFFFFFFFFFFE5F728000000000000049 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451074207298879491"]
   > [2024/07/11 15:25:45.215 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:59896] [split_keys="key 7480000000000000FF4800000000000000F8"] [peer_id=11] [region_id=10]
   > [2024/07/11 15:25:45.216 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=78] [peer-ids="[79]"]
   > [2024/07/11 15:25:45.216 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 10 start_key: 7480000000000000FF4400000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 38 } peers { id: 11 store_id: 1 }"] [new_region_ids="[new_region_id: 78 new_peer_ids: 79]"] [region_id=10]
   > [2024/07/11 15:25:45.222 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF4800000000000000F8 new_region_id: 78 new_peer_ids: 79 } right_derive: true }"] [index=65] [term=6] [peer_id=11] [region_id=10]
   > [2024/07/11 15:25:45.222 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF4800000000000000F8"] [region="id: 10 start_key: 7480000000000000FF4400000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 38 } peers { id: 11 store_id: 1 }"] [peer_id=11] [region_id=10]
   > [2024/07/11 15:25:45.228 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/11 15:25:45.228 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=10]
   > [2024/07/11 15:25:45.228 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(73)] [region_id=10] [store_id=Some(1)]
   > [2024/07/11 15:25:45.228 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 10 start_key: 7480000000000000FF4800000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 11 store_id: 1 }"]
   > [2024/07/11 15:25:45.228 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=11] [region_id=10]
   > [2024/07/11 15:25:45.228 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=10] ["first at"=748000000000000048] ["first new region left"="{Id:78 StartKey:7480000000000000ff4400000000000000f8 EndKey:7480000000000000ff4800000000000000f8 RegionEpoch:{ConfVer:1 Version:39} Peers:[id:79 store_id:1 ] EncryptionMeta:<nil> IsInFlashback:false}"] ["new region count"=1]
   > [2024/07/11 15:25:45.228 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[78]"]
   > [2024/07/11 15:25:45.228 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 78 start_key: 7480000000000000FF4400000000000000F8 end_key: 7480000000000000FF4800000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 79 store_id: 1 }"] [region_id=78]
   > [2024/07/11 15:25:45.228 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=79] [region_id=78]
   > [2024/07/11 15:25:45.228 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 10 start_key: 7480000000000000FF4800000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 11 store_id: 1 } }"]
   > [2024/07/11 15:25:45.228 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=10] [detail="StartKey Changed:{7480000000000000FF4400000000000000F8} -> {7480000000000000FF4800000000000000F8}, EndKey:{748000FFFFFFFFFFFFFB00000000000000F8}"] [old-version=38] [new-version=39]
   > [2024/07/11 15:25:45.228 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 10 start_key: 7480000000000000FF4800000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 11 store_id: 1 }"]
   > [2024/07/11 15:25:45.228 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {79} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=79] [region_id=78]
   > [2024/07/11 15:25:45.228 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=10] [origin="id:78 start_key:\"7480000000000000FF4400000000000000F8\" end_key:\"7480000000000000FF4800000000000000F8\" region_epoch:<conf_ver:1 version:39 > peers:<id:79 store_id:1 >"] [total=1]
   > [2024/07/11 15:25:45.229 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=79] [region_id=78]
   > [2024/07/11 15:25:45.229 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {79} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=79] [region_id=78]
   > [2024/07/11 15:25:45.229 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 79."] [id=79] [raft_id=79] [region_id=78]
   > [2024/07/11 15:25:45.229 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=79] [region_id=78]
   > [2024/07/11 15:25:45.229 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=79] [region_id=78]
   > [2024/07/11 15:25:45.229 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=79] [region_id=78]
   > [2024/07/11 15:25:45.229 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=79] [region_id=78]
   > [2024/07/11 15:25:45.229 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803854] [region_id=78]
   > [2024/07/11 15:25:45.229 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=65] [observe_id=ObserveId(75)] [region=10]
   > [2024/07/11 15:25:45.229 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=78]
   > [2024/07/11 15:25:45.234 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 78 start_key: 7480000000000000FF4400000000000000F8 end_key: 7480000000000000FF4800000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 79 store_id: 1 }"]
   > [2024/07/11 15:25:45.234 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(76)] [region=78]
   > [2024/07/11 15:25:45.325 +00:00] [INFO] [manager.go:272] ["revoke session"] ["owner info"="[log-backup] /tidb/br-stream/owner ownerManager 44d5e9c8-9be2-479f-b003-b20f9cd9d296"] [error="rpc error: code = Canceled desc = grpc: the client connection is closing"]
   > [2024/07/11 15:25:45.634 +00:00] [INFO] [cluster.go:1469] ["store has changed to serving"] [store-id=1] [store-address=127.0.0.1:20160]
   > [2024/07/11 15:25:45.667 +00:00] [INFO] [client.rs:789] ["set cluster version to 6.4.0"]
   > [2024/07/11 15:25:46.240 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/11 15:25:46.275 +00:00] [INFO] [set.go:141] ["set global var"] [conn=8833764489598861721] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/07/11 15:25:46.852 +00:00] [WARN] [2pc.go:1873] ["schemaLeaseChecker is not set for this transaction"] [sessionID=8833764489598861721] [startTS=451074207731154949] [checkTS=451074207731154950]
   > [2024/07/11 15:25:46.860 +00:00] [INFO] [scheduler.rs:640] ["get snapshot failed"] [err="Error(Request(message: \"EpochNotMatch current epoch of region 10 is conf_ver: 1 version: 39, but you sent conf_ver: 1 version: 38\" epoch_not_match { current_regions { id: 10 start_key: 7480000000000000FF4800000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 11 store_id: 1 } } current_regions { id: 78 start_key: 7480000000000000FF4400000000000000F8 end_key: 7480000000000000FF4800000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 79 store_id: 1 } } }))"] [cid=935]
   > [2024/07/11 15:25:47.150 +00:00] [WARN] [session.go:2191] ["run statement failed"] [conn=8833764489598861721] [schemaVersion=36] [error="[types:1292]Incorrect datetime value: 'Release Version: v6.4.0\nEdition: Community\nGit Commit Hash: cf36a9ce2fe1039db3cf3444d51930b887df18a1\nGit Branch: heads/refs/tags'"] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 8833764489598861721,\n  \"status\": 3,\n  \"strictMode\": true,\n  \"txn\": \"451074207652511745\",\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"10.88.0.21\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/07/11 15:25:47.151 +00:00] [INFO] [conn.go:1152] ["command dispatched failed"] [conn=8833764489598861721] [connInfo="id:8833764489598861721, addr:10.88.0.21:48756 status:11, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:1, autocommit:1"] [sql=" DELETE FROM t WHERE CAST(TIDB_VERSION() AS DATE);"] [txn_mode=PESSIMISTIC] [timestamp=451074207652511745] [err="[types:1292]Incorrect datetime value: 'Release Version: v6.4.0\nEdition: Community\nGit Commit Hash: cf36a9ce2fe1039db3cf3444d51930b887df18a1\nGit Branch: heads/refs/tags'\ngithub.com/pingcap/errors.AddStack\n\t/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.20220729040631-518f63d66278/errors.go:174\ngithub.com/pingcap/errors.(*Error).GenWithStackByArgs\n\t/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.20220729040631-518f63d66278/normalize.go:164\ngithub.com/pingcap/tidb/types.parseDatetime\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/tidb/types/time.go:1041\ngithub.com/pingcap/tidb/types.parseTime\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/tidb/types/time.go:1988\ngithub.com/pingcap/tidb/types.ParseTime\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/tidb/types/time.go:1970\ngithub.com/pingcap/tidb/expression.(*builtinCastStringAsTimeSig).evalTime\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/tidb/expression/builtin_cast.go:1302\ngithub.com/pingcap/tidb/expression.(*ScalarFunction).EvalTime\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/tidb/expression/scalar_function.go:426\ngithub.com/pingcap/tidb/expression.(*ScalarFunction).Eval\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/tidb/expression/scalar_function.go:373\ngithub.com/pingcap/tidb/expression.EvalBool\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/tidb/expression/expression.go:252\ngithub.com/pingcap/tidb/executor.(*memTableReader).getMemRows.func1\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/tidb/executor/mem_reader.go:257\ngithub.com/pingcap/tidb/executor.iterTxnMemBuffer\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/tidb/executor/mem_reader.go:417\ngithub.com/pingcap/tidb/executor.(*memTableReader).getMemRows\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/tidb/executor/mem_reader.go:249\ngithub.com/pingcap/tidb/executor.(*UnionScanExec).open\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/tidb/executor/union_scan.go:119\ngithub.com/pingcap/tidb/executor.(*UnionScanExec).Open\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/tidb/executor/union_scan.go:82\ngithub.com/pingcap/tidb/executor.(*baseExecutor).Open\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/tidb/executor/executor.go:199\ngithub.com/pingcap/tidb/executor.(*SelectLockExec).Open\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/tidb/executor/executor.go:1144\ngithub.com/pingcap/tidb/executor.(*DeleteExec).Open\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/tidb/executor/delete.go:285\ngithub.com/pingcap/tidb/executor.(*ExecStmt).openExecutor\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/tidb/executor/adapter.go:1111\ngithub.com/pingcap/tidb/executor.(*ExecStmt).Exec\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/tidb/executor/adapter.go:494\ngithub.com/pingcap/tidb/session.runStmt\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/tidb/session/session.go:2322\ngithub.com/pingcap/tidb/session.(*session).ExecuteStmt\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/tidb/session/session.go:2186\ngithub.com/pingcap/tidb/server.(*TiDBContext).ExecuteStmt\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/tidb/server/driver_tidb.go:233\ngithub.com/pingcap/tidb/server.(*clientConn).handleStmt\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/tidb/server/conn.go:2065\ngithub.com/pingcap/tidb/server.(*clientConn).handleQuery\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/tidb/server/conn.go:1920\ngithub.com/pingcap/tidb/server.(*clientConn).dispatch\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/tidb/server/conn.go:1374\ngithub.com/pingcap/tidb/server.(*clientConn).Run\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/tidb/server/conn.go:1123\ngithub.com/pingcap/tidb/server.(*Server).onConn\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/tidb/server/server.go:625\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1594"]

### Scenario 1
 * Instruction #0:
     - Instruction:  REPLACE INTO t VALUES ('G6y*k]88]');
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 1 / 0
 * Instruction #1:
     - Instruction:  DELETE FROM t WHERE CAST(TIDB_VERSION() AS DATE);
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 1

 * Container logs:
   > [2024/07/11 15:25:50.172 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/11 15:25:50.175 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=8833764489598861725] [schemaVersion=44] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/11 15:25:50.208 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:80, Type:drop schema, State:queueing, SchemaState:public, SchemaID:75, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-11 15:25:50.127 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/11 15:25:50.209 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:80, Type:drop schema, State:queueing, SchemaState:public, SchemaID:75, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-11 15:25:50.127 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/11 15:25:50.233 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:80, Type:drop schema, State:queueing, SchemaState:public, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-11 15:25:50.127 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/11 15:25:50.284 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=44] [neededSchemaVersion=45] ["start time"=804.092µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/11 15:25:50.333 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=45] ["take time"=57.994031ms] [job="ID:80, Type:drop schema, State:running, SchemaState:write only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-11 15:25:50.127 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/11 15:25:50.337 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:80, Type:drop schema, State:running, SchemaState:write only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-11 15:25:50.127 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/11 15:25:50.383 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=45] [neededSchemaVersion=46] ["start time"=664.967µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/11 15:25:50.431 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=46] ["take time"=59.407566ms] [job="ID:80, Type:drop schema, State:running, SchemaState:delete only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-11 15:25:50.127 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/11 15:25:50.436 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:80, Type:drop schema, State:running, SchemaState:delete only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-11 15:25:50.127 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/11 15:25:50.492 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=46] [neededSchemaVersion=47] ["start time"=524.584µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/11 15:25:50.541 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=47] ["take time"=65.146353ms] [job="ID:80, Type:drop schema, State:done, SchemaState:none, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-11 15:25:50.127 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/11 15:25:50.546 +00:00] [INFO] [delete_range.go:109] ["[ddl] add job into delete-range table"] [jobID=80] [jobType="drop schema"]
   > [2024/07/11 15:25:50.548 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:80, Type:drop schema, State:synced, SchemaState:none, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-11 15:25:50.127 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/11 15:25:50.570 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=80]
   > [2024/07/11 15:25:50.570 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/11 15:25:50.571 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000050FF0000000000000000F7 lock_version: 451074208701087746 key: 748000FFFFFFFFFFFE5F728000000000000050 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451074208701087747"]
   > [2024/07/11 15:25:50.571 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000050FF0000000000000000F7 lock_version: 451074208701087746 key: 748000FFFFFFFFFFFE5F728000000000000050 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451074208701087747"]
   > [2024/07/11 15:25:50.573 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=8833764489598861725] [schemaVersion=47] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/11 15:25:50.623 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:82, Type:create schema, State:queueing, SchemaState:none, SchemaID:81, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-11 15:25:50.576 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/11 15:25:50.623 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:82, Type:create schema, State:queueing, SchemaState:none, SchemaID:81, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-11 15:25:50.576 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/11 15:25:50.644 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:82, Type:create schema, State:queueing, SchemaState:none, SchemaID:81, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-11 15:25:50.576 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/11 15:25:50.690 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=47] [neededSchemaVersion=48] ["start time"=1.317851ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/11 15:25:50.738 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=48] ["take time"=56.594884ms] [job="ID:82, Type:create schema, State:done, SchemaState:public, SchemaID:81, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-11 15:25:50.576 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/11 15:25:50.745 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:82, Type:create schema, State:synced, SchemaState:public, SchemaID:81, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-11 15:25:50.576 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/11 15:25:50.768 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=82]
   > [2024/07/11 15:25:50.768 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/11 15:25:50.769 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000052FF0000000000000000F7 lock_version: 451074208753516546 key: 748000FFFFFFFFFFFE5F728000000000000052 lock_ttl: 3003 txn_size: 1 lock_type: Del min_commit_ts: 451074208753516547"]
   > [2024/07/11 15:25:50.769 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000052FF0000000000000000F7 lock_version: 451074208753516546 key: 748000FFFFFFFFFFFE5F728000000000000052 lock_ttl: 3003 txn_size: 1 lock_type: Del min_commit_ts: 451074208753516547"]
   > [2024/07/11 15:25:50.773 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=8833764489598861725] [schemaVersion=48] [cur_db=testdb] [sql="CREATE TABLE t(c0 TEXT(284));"] [user=root@%]
   > [2024/07/11 15:25:50.828 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:84, Type:create table, State:queueing, SchemaState:none, SchemaID:81, TableID:83, RowCount:0, ArgLen:2, start time: 2024-07-11 15:25:50.776 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/11 15:25:50.828 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:84, Type:create table, State:queueing, SchemaState:none, SchemaID:81, TableID:83, RowCount:0, ArgLen:2, start time: 2024-07-11 15:25:50.776 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE t(c0 TEXT(284));"]
   > [2024/07/11 15:25:50.851 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:84, Type:create table, State:queueing, SchemaState:none, SchemaID:81, TableID:83, RowCount:0, ArgLen:0, start time: 2024-07-11 15:25:50.776 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/11 15:25:50.907 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=48] [neededSchemaVersion=49] ["start time"=2.348302ms] [phyTblIDs="[83]"] [actionTypes="[8]"]
   > [2024/07/11 15:25:50.953 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=49] ["take time"=60.759569ms] [job="ID:84, Type:create table, State:done, SchemaState:public, SchemaID:81, TableID:83, RowCount:0, ArgLen:2, start time: 2024-07-11 15:25:50.776 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/11 15:25:50.958 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:84, Type:create table, State:synced, SchemaState:public, SchemaID:81, TableID:83, RowCount:0, ArgLen:0, start time: 2024-07-11 15:25:50.776 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/11 15:25:50.982 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=84]
   > [2024/07/11 15:25:50.982 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/11 15:25:50.982 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=10] ["first split key"=748000000000000053]
   > [2024/07/11 15:25:50.983 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000054FF0000000000000000F7 lock_version: 451074208805945346 key: 748000FFFFFFFFFFFE5F728000000000000054 lock_ttl: 3003 txn_size: 1 lock_type: Del min_commit_ts: 451074208805945347"]
   > [2024/07/11 15:25:50.983 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000054FF0000000000000000F7 lock_version: 451074208805945346 key: 748000FFFFFFFFFFFE5F728000000000000054 lock_ttl: 3003 txn_size: 1 lock_type: Del min_commit_ts: 451074208805945347"]
   > [2024/07/11 15:25:50.986 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:59872] [split_keys="key 7480000000000000FF5300000000000000F8"] [peer_id=11] [region_id=10]
   > [2024/07/11 15:25:50.987 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=82] [peer-ids="[83]"]
   > [2024/07/11 15:25:50.987 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 10 start_key: 7480000000000000FF4D00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 40 } peers { id: 11 store_id: 1 }"] [new_region_ids="[new_region_id: 82 new_peer_ids: 83]"] [region_id=10]
   > [2024/07/11 15:25:50.997 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF5300000000000000F8 new_region_id: 82 new_peer_ids: 83 } right_derive: true }"] [index=69] [term=6] [peer_id=11] [region_id=10]
   > [2024/07/11 15:25:50.997 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF5300000000000000F8"] [region="id: 10 start_key: 7480000000000000FF4D00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 40 } peers { id: 11 store_id: 1 }"] [peer_id=11] [region_id=10]
   > [2024/07/11 15:25:51.003 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/11 15:25:51.003 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=10]
   > [2024/07/11 15:25:51.003 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(77)] [region_id=10] [store_id=Some(1)]
   > [2024/07/11 15:25:51.003 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=11] [region_id=10]
   > [2024/07/11 15:25:51.003 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 10 start_key: 7480000000000000FF5300000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 11 store_id: 1 }"]
   > [2024/07/11 15:25:51.003 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 82 start_key: 7480000000000000FF4D00000000000000F8 end_key: 7480000000000000FF5300000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 83 store_id: 1 }"] [region_id=82]
   > [2024/07/11 15:25:51.003 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=10] [detail="StartKey Changed:{7480000000000000FF4D00000000000000F8} -> {7480000000000000FF5300000000000000F8}, EndKey:{748000FFFFFFFFFFFFFB00000000000000F8}"] [old-version=40] [new-version=41]
   > [2024/07/11 15:25:51.003 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=10] ["first at"=748000000000000053] ["first new region left"="{Id:82 StartKey:7480000000000000ff4d00000000000000f8 EndKey:7480000000000000ff5300000000000000f8 RegionEpoch:{ConfVer:1 Version:41} Peers:[id:83 store_id:1 ] EncryptionMeta:<nil> IsInFlashback:false}"] ["new region count"=1]
   > [2024/07/11 15:25:51.003 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=83] [region_id=82]
   > [2024/07/11 15:25:51.003 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=10] [origin="id:82 start_key:\"7480000000000000FF4D00000000000000F8\" end_key:\"7480000000000000FF5300000000000000F8\" region_epoch:<conf_ver:1 version:41 > peers:<id:83 store_id:1 >"] [total=1]
   > [2024/07/11 15:25:51.003 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[82]"]
   > [2024/07/11 15:25:51.003 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 10 start_key: 7480000000000000FF5300000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 11 store_id: 1 } }"]
   > [2024/07/11 15:25:51.003 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 10 start_key: 7480000000000000FF5300000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 11 store_id: 1 }"]
   > [2024/07/11 15:25:51.003 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {83} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=83] [region_id=82]
   > [2024/07/11 15:25:51.003 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=83] [region_id=82]
   > [2024/07/11 15:25:51.003 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {83} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=83] [region_id=82]
   > [2024/07/11 15:25:51.003 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 83."] [id=83] [raft_id=83] [region_id=82]
   > [2024/07/11 15:25:51.003 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=83] [region_id=82]
   > [2024/07/11 15:25:51.003 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=83] [region_id=82]
   > [2024/07/11 15:25:51.004 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=83] [region_id=82]
   > [2024/07/11 15:25:51.004 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=83] [region_id=82]
   > [2024/07/11 15:25:51.004 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803858] [region_id=82]
   > [2024/07/11 15:25:51.004 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=69] [observe_id=ObserveId(79)] [region=10]
   > [2024/07/11 15:25:51.004 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=82]
   > [2024/07/11 15:25:51.009 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 82 start_key: 7480000000000000FF4D00000000000000F8 end_key: 7480000000000000FF5300000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 83 store_id: 1 }"]
   > [2024/07/11 15:25:51.009 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(80)] [region=82]
   > [2024/07/11 15:25:51.993 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/11 15:25:52.015 +00:00] [WARN] [2pc.go:1873] ["schemaLeaseChecker is not set for this transaction"] [sessionID=8833764489598861727] [startTS=451074209081458695] [checkTS=451074209081458696]
   > [2024/07/11 15:25:52.023 +00:00] [INFO] [scheduler.rs:640] ["get snapshot failed"] [err="Error(Request(message: \"EpochNotMatch current epoch of region 10 is conf_ver: 1 version: 41, but you sent conf_ver: 1 version: 40\" epoch_not_match { current_regions { id: 10 start_key: 7480000000000000FF5300000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 11 store_id: 1 } } current_regions { id: 82 start_key: 7480000000000000FF4D00000000000000F8 end_key: 7480000000000000FF5300000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 83 store_id: 1 } } }))"] [cid=1163]
