# Bug ID TIDB-20692-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/20692
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              The update should block, but it doesn't.


## Details
 * Database: tidb-v4.0.0-beta.2.tikv
 * Number of scenarios: 1
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
     - Instruction:  begin;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  begin;
     - Transaction: conn_1
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 0 / 0
 * Instruction #3:
     - Instruction:  begin;
     - Transaction: conn_2
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 0 / 0
 * Instruction #4:
     - Instruction:  delete from t where id = 1 and v = 1 and vv = 1;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows / Warnings: 1 / 0
 * Instruction #5:
     - Instruction:  insert into t values(1, 2, 3, 4);
     - Transaction: conn_1
     - Output: None
     - Executed order: 8
     - Affected rows / Warnings: 1 / 0
 * Instruction #6:
     - Instruction:  update t set id = 10, v = 20, vv = 30, vvv = 40 where id = 1 and v = 2 and vv =...
     - Transaction: conn_2
     - Output: None
     - Executed order: 5
     - Affected rows / Warnings: 0 / 0
 * Instruction #7:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: None
     - Executed order: 6
     - Affected rows / Warnings: 0 / 0
 * Instruction #8:
     - Instruction:  commit;
     - Transaction: conn_2
     - Output: None
     - Executed order: 7
     - Affected rows / Warnings: 0 / 0
 * Instruction #9:
     - Instruction:  commit;
     - Transaction: conn_1
     - Output: None
     - Executed order: 9
     - Affected rows / Warnings: 0 / 0

 * Container logs:
   > [2024/07/17 12:30:15.192 +00:00] [INFO] [server.go:388] ["new connection"] [conn=3] [remoteAddr=10.88.0.197:38938]
   > [2024/07/17 12:30:15.195 +00:00] [INFO] [session.go:2210] ["CRUCIAL OPERATION"] [conn=3] [schemaVersion=22] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.197]
   > [2024/07/17 12:30:15.196 +00:00] [INFO] [session.go:2210] ["CRUCIAL OPERATION"] [conn=3] [schemaVersion=22] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.197]
   > [2024/07/17 12:30:15.235 +00:00] [INFO] [ddl_worker.go:253] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-17 12:30:15.186 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/17 12:30:15.235 +00:00] [INFO] [ddl.go:500] ["[ddl] start DDL job"] [job="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-17 12:30:15.186 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/17 12:30:15.238 +00:00] [INFO] [ddl_worker.go:568] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-17 12:30:15.186 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 12:30:15.264 +00:00] [INFO] [domain.go:126] ["diff load InfoSchema success"] [usedSchemaVersion=22] [neededSchemaVersion=23] ["start time"=1.236203ms] [tblIDs="[]"]
   > [2024/07/17 12:30:15.313 +00:00] [INFO] [ddl_worker.go:759] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=23] ["take time"=57.59025ms] [job="ID:46, Type:create schema, State:done, SchemaState:public, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-17 12:30:15.186 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 12:30:15.316 +00:00] [INFO] [ddl_worker.go:359] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:46, Type:create schema, State:synced, SchemaState:public, SchemaID:45, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-17 12:30:15.186 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 12:30:15.333 +00:00] [INFO] [ddl.go:532] ["[ddl] DDL job is finished"] [jobID=46]
   > [2024/07/17 12:30:15.333 +00:00] [INFO] [domain.go:631] ["performing DDL change, must reload"]
   > [2024/07/17 12:30:15.336 +00:00] [INFO] [session.go:2210] ["CRUCIAL OPERATION"] [conn=3] [schemaVersion=23] [cur_db=testdb] [sql="create table t (id int primary key, v int, vv int, vvv int, unique key u0(id, v, vv));"] [user=root@10.88.0.197]
   > [2024/07/17 12:30:15.371 +00:00] [INFO] [ddl_worker.go:253] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-07-17 12:30:15.336 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/17 12:30:15.371 +00:00] [INFO] [ddl.go:500] ["[ddl] start DDL job"] [job="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-07-17 12:30:15.336 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t (id int primary key, v int, vv int, vvv int, unique key u0(id, v, vv));"]
   > [2024/07/17 12:30:15.374 +00:00] [INFO] [ddl_worker.go:568] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-17 12:30:15.336 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 12:30:15.410 +00:00] [INFO] [domain.go:126] ["diff load InfoSchema success"] [usedSchemaVersion=23] [neededSchemaVersion=24] ["start time"=1.908642ms] [tblIDs="[47]"]
   > [2024/07/17 12:30:15.460 +00:00] [INFO] [ddl_worker.go:759] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=24] ["take time"=63.217978ms] [job="ID:48, Type:create table, State:done, SchemaState:public, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-07-17 12:30:15.336 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 12:30:15.464 +00:00] [INFO] [ddl_worker.go:359] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:48, Type:create table, State:synced, SchemaState:public, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-17 12:30:15.336 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 12:30:15.493 +00:00] [INFO] [ddl.go:532] ["[ddl] DDL job is finished"] [jobID=48]
   > [2024/07/17 12:30:15.495 +00:00] [INFO] [domain.go:631] ["performing DDL change, must reload"]
   > [2024/07/17 12:30:15.495 +00:00] [INFO] [split_region.go:56] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=74800000000000002f]
   > [2024/07/17 12:30:15.495 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:55794] [split_keys="key 7480000000000000FF2F00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/17 12:30:15.496 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=44] [peer-ids="[45]"]
   > [2024/07/17 12:30:15.496 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF2B00000000000000F8 region_epoch { conf_ver: 1 version: 21 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 44 new_peer_ids: 45]"] [region_id=2]
   > [2024/07/17 12:30:15.502 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF2F00000000000000F8 new_region_id: 44 new_peer_ids: 45 } right_derive: true }"] [index=52] [term=6] [peer_id=3] [region_id=2]
   > [2024/07/17 12:30:15.502 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF2F00000000000000F8"] [region="id: 2 start_key: 7480000000000000FF2B00000000000000F8 region_epoch { conf_ver: 1 version: 21 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/07/17 12:30:15.508 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/17 12:30:15.508 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=2]
   > [2024/07/17 12:30:15.508 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/07/17 12:30:15.508 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(39)] [region_id=2] [store_id=Some(1)]
   > [2024/07/17 12:30:15.508 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 3 store_id: 1 }"]
   > [2024/07/17 12:30:15.508 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 44 start_key: 7480000000000000FF2B00000000000000F8 end_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 45 store_id: 1 }"] [region_id=44]
   > [2024/07/17 12:30:15.508 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=45] [region_id=44]
   > [2024/07/17 12:30:15.508 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 2 start_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 3 store_id: 1 } }"]
   > [2024/07/17 12:30:15.508 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 2 start_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 3 store_id: 1 }"]
   > [2024/07/17 12:30:15.508 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {45} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=45] [region_id=44]
   > [2024/07/17 12:30:15.508 +00:00] [INFO] [split_region.go:153] ["batch split regions complete"] ["batch region ID"=2] ["first at"=74800000000000002f] ["first new region left"="{Id:44 StartKey:7480000000000000ff2b00000000000000f8 EndKey:7480000000000000ff2f00000000000000f8 RegionEpoch:{ConfVer:1 Version:22} Peers:[id:45 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/17 12:30:15.508 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=45] [region_id=44]
   > [2024/07/17 12:30:15.508 +00:00] [INFO] [split_region.go:205] ["split regions complete"] ["region count"=1] ["region IDs"="[44]"]
   > [2024/07/17 12:30:15.508 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {45} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=45] [region_id=44]
   > [2024/07/17 12:30:15.509 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 45."] [id=45] [raft_id=45] [region_id=44]
   > [2024/07/17 12:30:15.509 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF2B00000000000000F8} -> {7480000000000000FF2F00000000000000F8}, EndKey:{}"] [old-version=21] [new-version=22]
   > [2024/07/17 12:30:15.509 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=45] [region_id=44]
   > [2024/07/17 12:30:15.509 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=45] [region_id=44]
   > [2024/07/17 12:30:15.509 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=45] [region_id=44]
   > [2024/07/17 12:30:15.509 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=2] [origin="id:44 start_key:\"7480000000000000FF2B00000000000000F8\" end_key:\"7480000000000000FF2F00000000000000F8\" region_epoch:<conf_ver:1 version:22 > peers:<id:45 store_id:1 >"] [total=1]
   > [2024/07/17 12:30:15.509 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=45] [region_id=44]
   > [2024/07/17 12:30:15.509 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803820] [region_id=44]
   > [2024/07/17 12:30:15.509 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=52] [observe_id=ObserveId(41)] [region=2]
   > [2024/07/17 12:30:15.509 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=44]
   > [2024/07/17 12:30:15.514 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 44 start_key: 7480000000000000FF2B00000000000000F8 end_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 45 store_id: 1 }"]
   > [2024/07/17 12:30:15.514 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(42)] [region=44]
   > [2024/07/17 12:30:15.528 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=3]
   > [2024/07/17 12:30:16.548 +00:00] [INFO] [server.go:388] ["new connection"] [conn=4] [remoteAddr=10.88.0.197:38944]
   > [2024/07/17 12:30:16.556 +00:00] [INFO] [set.go:207] ["set session var"] [conn=4] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/07/17 12:30:17.155 +00:00] [INFO] [server.go:388] ["new connection"] [conn=5] [remoteAddr=10.88.0.197:34218]
   > [2024/07/17 12:30:17.159 +00:00] [INFO] [set.go:207] ["set session var"] [conn=5] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/07/17 12:30:17.466 +00:00] [INFO] [server.go:388] ["new connection"] [conn=6] [remoteAddr=10.88.0.197:34222]
   > [2024/07/17 12:30:17.469 +00:00] [INFO] [set.go:207] ["set session var"] [conn=6] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/07/17 12:30:17.728 +00:00] [INFO] [cluster.go:1469] ["store has changed to serving"] [store-id=1] [store-address=127.0.0.1:20160]
   > [2024/07/17 12:30:17.773 +00:00] [INFO] [client.rs:789] ["set cluster version to 6.4.0"]
   > [2024/07/17 12:30:18.675 +00:00] [INFO] [adapter.go:607] ["pessimistic write conflict, retry statement"] [conn=5] [txn=451207342885961735] [forUpdateTS=451207342885961735] [err="[kv:9007]Write conflict, txnStartTS=451207342885961735, conflictStartTS=451207342807056385, conflictCommitTS=451207343279177729, key={tableID=47, handle=1} primary={tableID=47, indexID=1, indexValues={1, 2, 3, }} [try again later]"]
   > [2024/07/17 12:30:18.974 +00:00] [INFO] [adapter.go:607] ["pessimistic write conflict, retry statement"] [conn=5] [txn=451207342885961735] [forUpdateTS=451207343279177729] [err="[kv:9007]Write conflict, txnStartTS=451207342885961735, conflictStartTS=451207342964342790, conflictCommitTS=451207343357820929, key={tableID=47, indexID=1, indexValues={1, 2, 3, }} primary={tableID=47, indexID=1, indexValues={1, 2, 3, }} [try again later]"]
   > [2024/07/17 12:30:19.668 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=4]
   > [2024/07/17 12:30:19.668 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=6]
   > [2024/07/17 12:30:19.668 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=5]
