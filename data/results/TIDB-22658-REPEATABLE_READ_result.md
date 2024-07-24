# Bug ID TIDB-22658-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/22658
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              read only transactions are read/write


## Details
 * Database: tidb-v4.0.0-beta.2.tikv
 * Number of scenarios: 1
 * Initial setup script: No

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows: 0
 * Instruction #1:
     - Instruction:  CREATE TABLE t1 (a int);
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows: 0
 * Instruction #2:
     - Instruction:  start transaction read only;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows: 0
 * Instruction #3:
     - Instruction:  insert into t1 values (1);
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows: 1

 * Container logs:
   > [2024/07/24 12:31:40.663 +00:00] [INFO] [server.go:388] ["new connection"] [conn=2] [remoteAddr=10.88.0.78:54732]
   > [2024/07/24 12:31:40.665 +00:00] [INFO] [session.go:2210] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=22] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.78]
   > [2024/07/24 12:31:40.666 +00:00] [INFO] [session.go:2210] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=22] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.78]
   > [2024/07/24 12:31:40.690 +00:00] [INFO] [ddl_worker.go:253] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:31:40.677 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 12:31:40.690 +00:00] [INFO] [ddl.go:500] ["[ddl] start DDL job"] [job="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:31:40.677 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/24 12:31:40.694 +00:00] [INFO] [ddl_worker.go:568] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:31:40.677 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:31:40.710 +00:00] [INFO] [domain.go:126] ["diff load InfoSchema success"] [usedSchemaVersion=22] [neededSchemaVersion=23] ["start time"=1.243676ms] [tblIDs="[]"]
   > [2024/07/24 12:31:40.759 +00:00] [INFO] [ddl_worker.go:759] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=23] ["take time"=54.737473ms] [job="ID:46, Type:create schema, State:done, SchemaState:public, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:31:40.677 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:31:40.763 +00:00] [INFO] [ddl_worker.go:359] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:46, Type:create schema, State:synced, SchemaState:public, SchemaID:45, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:31:40.677 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:31:40.773 +00:00] [INFO] [ddl.go:532] ["[ddl] DDL job is finished"] [jobID=46]
   > [2024/07/24 12:31:40.773 +00:00] [INFO] [domain.go:631] ["performing DDL change, must reload"]
   > [2024/07/24 12:31:40.776 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=2]
   > [2024/07/24 12:31:41.270 +00:00] [INFO] [conn.go:497] ["wait handshake response fail due to connection has be closed by client-side"] [conn=3]
   > [2024/07/24 12:31:41.794 +00:00] [INFO] [server.go:388] ["new connection"] [conn=4] [remoteAddr=10.88.0.78:54736]
   > [2024/07/24 12:31:41.797 +00:00] [INFO] [set.go:207] ["set session var"] [conn=4] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/07/24 12:31:42.092 +00:00] [INFO] [session.go:2210] ["CRUCIAL OPERATION"] [conn=4] [schemaVersion=23] [cur_db=testdb] [sql=" CREATE TABLE t1 (a int);"] [user=root@10.88.0.78]
   > [2024/07/24 12:31:42.110 +00:00] [INFO] [ddl_worker.go:253] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-07-24 12:31:42.077 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 12:31:42.110 +00:00] [INFO] [ddl.go:500] ["[ddl] start DDL job"] [job="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-07-24 12:31:42.077 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query=" CREATE TABLE t1 (a int);"]
   > [2024/07/24 12:31:42.114 +00:00] [INFO] [ddl_worker.go:568] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-24 12:31:42.077 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:31:42.134 +00:00] [INFO] [domain.go:126] ["diff load InfoSchema success"] [usedSchemaVersion=23] [neededSchemaVersion=24] ["start time"=1.862756ms] [tblIDs="[47]"]
   > [2024/07/24 12:31:42.183 +00:00] [INFO] [ddl_worker.go:759] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=24] ["take time"=55.249414ms] [job="ID:48, Type:create table, State:done, SchemaState:public, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-07-24 12:31:42.077 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:31:42.186 +00:00] [INFO] [ddl_worker.go:359] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:48, Type:create table, State:synced, SchemaState:public, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-24 12:31:42.077 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:31:42.196 +00:00] [INFO] [ddl.go:532] ["[ddl] DDL job is finished"] [jobID=48]
   > [2024/07/24 12:31:42.198 +00:00] [INFO] [domain.go:631] ["performing DDL change, must reload"]
   > [2024/07/24 12:31:42.199 +00:00] [INFO] [split_region.go:56] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=74800000000000002f]
   > [2024/07/24 12:31:42.199 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:42364] [split_keys="key 7480000000000000FF2F00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/24 12:31:42.199 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=44] [peer-ids="[45]"]
   > [2024/07/24 12:31:42.200 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF2B00000000000000F8 region_epoch { conf_ver: 1 version: 21 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 44 new_peer_ids: 45]"] [region_id=2]
   > [2024/07/24 12:31:42.202 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF2F00000000000000F8 new_region_id: 44 new_peer_ids: 45 } right_derive: true }"] [index=52] [term=6] [peer_id=3] [region_id=2]
   > [2024/07/24 12:31:42.202 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF2F00000000000000F8"] [region="id: 2 start_key: 7480000000000000FF2B00000000000000F8 region_epoch { conf_ver: 1 version: 21 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/07/24 12:31:42.205 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/24 12:31:42.205 +00:00] [INFO] [split_region.go:153] ["batch split regions complete"] ["batch region ID"=2] ["first at"=74800000000000002f] ["first new region left"="{Id:44 StartKey:7480000000000000ff2b00000000000000f8 EndKey:7480000000000000ff2f00000000000000f8 RegionEpoch:{ConfVer:1 Version:22} Peers:[id:45 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/24 12:31:42.205 +00:00] [INFO] [split_region.go:205] ["split regions complete"] ["region count"=1] ["region IDs"="[44]"]
   > [2024/07/24 12:31:42.205 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF2B00000000000000F8} -> {7480000000000000FF2F00000000000000F8}, EndKey:{}"] [old-version=21] [new-version=22]
   > [2024/07/24 12:31:42.205 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=2]
   > [2024/07/24 12:31:42.205 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(39)] [region_id=2] [store_id=Some(1)]
   > [2024/07/24 12:31:42.205 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/07/24 12:31:42.205 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 3 store_id: 1 }"]
   > [2024/07/24 12:31:42.205 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 44 start_key: 7480000000000000FF2B00000000000000F8 end_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 45 store_id: 1 }"] [region_id=44]
   > [2024/07/24 12:31:42.205 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=45] [region_id=44]
   > [2024/07/24 12:31:42.205 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 2 start_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 3 store_id: 1 } }"]
   > [2024/07/24 12:31:42.206 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 2 start_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 3 store_id: 1 }"]
   > [2024/07/24 12:31:42.206 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=2] [origin="id:44 start_key:\"7480000000000000FF2B00000000000000F8\" end_key:\"7480000000000000FF2F00000000000000F8\" region_epoch:<conf_ver:1 version:22 > peers:<id:45 store_id:1 >"] [total=1]
   > [2024/07/24 12:31:42.206 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {45} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=45] [region_id=44]
   > [2024/07/24 12:31:42.206 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=45] [region_id=44]
   > [2024/07/24 12:31:42.206 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {45} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=45] [region_id=44]
   > [2024/07/24 12:31:42.206 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 45."] [id=45] [raft_id=45] [region_id=44]
   > [2024/07/24 12:31:42.206 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=45] [region_id=44]
   > [2024/07/24 12:31:42.206 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=45] [region_id=44]
   > [2024/07/24 12:31:42.206 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=45] [region_id=44]
   > [2024/07/24 12:31:42.207 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=45] [region_id=44]
   > [2024/07/24 12:31:42.207 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803820] [region_id=44]
   > [2024/07/24 12:31:42.207 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=44]
   > [2024/07/24 12:31:42.207 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=52] [observe_id=ObserveId(41)] [region=2]
   > [2024/07/24 12:31:42.208 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 44 start_key: 7480000000000000FF2B00000000000000F8 end_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 45 store_id: 1 }"]
   > [2024/07/24 12:31:42.208 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(42)] [region=44]
   > [2024/07/24 12:31:42.711 +00:00] [INFO] [scheduler.rs:640] ["get snapshot failed"] [err="Error(Request(message: \"EpochNotMatch current epoch of region 2 is conf_ver: 1 version: 22, but you sent conf_ver: 1 version: 21\" epoch_not_match { current_regions { id: 2 start_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 3 store_id: 1 } } current_regions { id: 44 start_key: 7480000000000000FF2B00000000000000F8 end_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 45 store_id: 1 } } }))"] [cid=253]
   > [2024/07/24 12:31:43.097 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=4]
