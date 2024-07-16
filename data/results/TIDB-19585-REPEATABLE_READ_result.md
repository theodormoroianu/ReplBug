# Bug ID TIDB-19585-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/19585
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              The second select should output the same table as the first one, but it doesn't.


## Details
 * Database: tidb-b0c3fe7b.tikv
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
     - Instruction:  begin;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  insert into t1 values (10);
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 1 / 0
 * Instruction #3:
     - Instruction:  update t1 set c_int = c_int + 10 where c_int in (1, 11);
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 2 / 0
 * Instruction #4:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows / Warnings: 0 / 0
 * Instruction #5:
     - Instruction:  select * from t1 order by c_int;
     - Transaction: conn_0
     - Output: [(10,), (21,)]
     - Executed order: 5
     - Affected rows / Warnings: 2 / 0

 * Container logs:
   > [2024/07/16 15:37:58.604 +00:00] [INFO] [session.go:2269] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=24] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.77]
   > [2024/07/16 15:37:58.606 +00:00] [INFO] [session.go:2269] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=24] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.77]
   > [2024/07/16 15:37:58.643 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:50, Type:create schema, State:none, SchemaState:none, SchemaID:49, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-16 15:37:58.6 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/16 15:37:58.643 +00:00] [INFO] [ddl.go:475] ["[ddl] start DDL job"] [job="ID:50, Type:create schema, State:none, SchemaState:none, SchemaID:49, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-16 15:37:58.6 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/16 15:37:58.647 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:50, Type:create schema, State:none, SchemaState:none, SchemaID:49, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 15:37:58.6 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:37:58.674 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=24] [neededSchemaVersion=25] ["start time"=1.550424ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/16 15:37:58.723 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=25] ["take time"=57.27721ms] [job="ID:50, Type:create schema, State:done, SchemaState:public, SchemaID:49, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-16 15:37:58.6 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:37:58.726 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:50, Type:create schema, State:synced, SchemaState:public, SchemaID:49, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 15:37:58.6 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:37:58.743 +00:00] [INFO] [ddl.go:507] ["[ddl] DDL job is finished"] [jobID=50]
   > [2024/07/16 15:37:58.743 +00:00] [INFO] [domain.go:646] ["performing DDL change, must reload"]
   > [2024/07/16 15:37:58.746 +00:00] [INFO] [session.go:2269] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=25] [cur_db=testdb] [sql="create table t1  (c_int int, primary key (c_int)) partition by range (c_int) (partition p0 values less than (10), partition p1 values less than maxvalue) ;"] [user=root@10.88.0.77]
   > [2024/07/16 15:37:58.793 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:54, Type:create table, State:none, SchemaState:none, SchemaID:49, TableID:51, RowCount:0, ArgLen:1, start time: 2024-07-16 15:37:58.751 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/16 15:37:58.793 +00:00] [INFO] [ddl.go:475] ["[ddl] start DDL job"] [job="ID:54, Type:create table, State:none, SchemaState:none, SchemaID:49, TableID:51, RowCount:0, ArgLen:1, start time: 2024-07-16 15:37:58.751 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t1  (c_int int, primary key (c_int)) partition by range (c_int) (partition p0 values less than (10), partition p1 values less than maxvalue) ;"]
   > [2024/07/16 15:37:58.797 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:54, Type:create table, State:none, SchemaState:none, SchemaID:49, TableID:51, RowCount:0, ArgLen:0, start time: 2024-07-16 15:37:58.751 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:37:58.833 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=25] [neededSchemaVersion=26] ["start time"=2.313449ms] [phyTblIDs="[51,52,53]"] [actionTypes="[8,8,8]"]
   > [2024/07/16 15:37:58.881 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=26] ["take time"=60.753949ms] [job="ID:54, Type:create table, State:done, SchemaState:public, SchemaID:49, TableID:51, RowCount:0, ArgLen:1, start time: 2024-07-16 15:37:58.751 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:37:58.885 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:54, Type:create table, State:synced, SchemaState:public, SchemaID:49, TableID:51, RowCount:0, ArgLen:0, start time: 2024-07-16 15:37:58.751 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:37:58.914 +00:00] [INFO] [ddl.go:507] ["[ddl] DDL job is finished"] [jobID=54]
   > [2024/07/16 15:37:58.915 +00:00] [INFO] [domain.go:646] ["performing DDL change, must reload"]
   > [2024/07/16 15:37:58.915 +00:00] [INFO] [split_region.go:59] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=748000000000000034]
   > [2024/07/16 15:37:58.916 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:46954] [split_keys="key 7480000000000000FF3400000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/16 15:37:58.916 +00:00] [INFO] [peer.rs:5566] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 22"] [prev_epoch="conf_ver: 1 version: 23"] [peer_id=3] [region_id=2]
   > [2024/07/16 15:37:58.926 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:46910] [split_keys="key 7480000000000000FF3400000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/16 15:37:58.927 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=48] [peer-ids="[49]"]
   > [2024/07/16 15:37:58.927 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 23 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 48 new_peer_ids: 49]"] [region_id=2]
   > [2024/07/16 15:37:58.938 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF3400000000000000F8 new_region_id: 48 new_peer_ids: 49 } right_derive: true }"] [index=57] [term=6] [peer_id=3] [region_id=2]
   > [2024/07/16 15:37:58.939 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF3400000000000000F8"] [region="id: 2 start_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 23 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/07/16 15:37:58.945 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/16 15:37:58.945 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=2]
   > [2024/07/16 15:37:58.945 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/07/16 15:37:58.945 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(43)] [region_id=2] [store_id=Some(1)]
   > [2024/07/16 15:37:58.945 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF3400000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 3 store_id: 1 }"]
   > [2024/07/16 15:37:58.945 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 48 start_key: 7480000000000000FF2F00000000000000F8 end_key: 7480000000000000FF3400000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 49 store_id: 1 }"] [region_id=48]
   > [2024/07/16 15:37:58.945 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=49] [region_id=48]
   > [2024/07/16 15:37:58.945 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 2 start_key: 7480000000000000FF3400000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 3 store_id: 1 } }"]
   > [2024/07/16 15:37:58.945 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 2 start_key: 7480000000000000FF3400000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 3 store_id: 1 }"]
   > [2024/07/16 15:37:58.945 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {49} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=49] [region_id=48]
   > [2024/07/16 15:37:58.945 +00:00] [INFO] [split_region.go:156] ["batch split regions complete"] ["batch region ID"=2] ["first at"=748000000000000034] ["first new region left"="{Id:48 StartKey:7480000000000000ff2f00000000000000f8 EndKey:7480000000000000ff3400000000000000f8 RegionEpoch:{ConfVer:1 Version:24} Peers:[id:49 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/16 15:37:58.945 +00:00] [INFO] [split_region.go:205] ["split regions complete"] ["region count"=1] ["region IDs"="[48]"]
   > [2024/07/16 15:37:58.945 +00:00] [INFO] [split_region.go:59] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=748000000000000035]
   > [2024/07/16 15:37:58.945 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=49] [region_id=48]
   > [2024/07/16 15:37:58.945 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=2] [origin="id:48 start_key:\"7480000000000000FF2F00000000000000F8\" end_key:\"7480000000000000FF3400000000000000F8\" region_epoch:<conf_ver:1 version:24 > peers:<id:49 store_id:1 >"] [total=1]
   > [2024/07/16 15:37:58.945 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {49} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=49] [region_id=48]
   > [2024/07/16 15:37:58.945 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF2F00000000000000F8} -> {7480000000000000FF3400000000000000F8}, EndKey:{}"] [old-version=23] [new-version=24]
   > [2024/07/16 15:37:58.945 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 49."] [id=49] [raft_id=49] [region_id=48]
   > [2024/07/16 15:37:58.945 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=49] [region_id=48]
   > [2024/07/16 15:37:58.945 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=49] [region_id=48]
   > [2024/07/16 15:37:58.945 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=49] [region_id=48]
   > [2024/07/16 15:37:58.945 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=49] [region_id=48]
   > [2024/07/16 15:37:58.946 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803824] [region_id=48]
   > [2024/07/16 15:37:58.946 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=57] [observe_id=ObserveId(45)] [region=2]
   > [2024/07/16 15:37:58.946 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:46926] [split_keys="key 7480000000000000FF3500000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/16 15:37:58.946 +00:00] [INFO] [peer.rs:5566] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 23"] [prev_epoch="conf_ver: 1 version: 24"] [peer_id=3] [region_id=2]
   > [2024/07/16 15:37:58.946 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=48]
   > [2024/07/16 15:37:58.948 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:46940] [split_keys="key 7480000000000000FF3500000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/16 15:37:58.949 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=50] [peer-ids="[51]"]
   > [2024/07/16 15:37:58.949 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF3400000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 50 new_peer_ids: 51]"] [region_id=2]
   > [2024/07/16 15:37:58.951 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 48 start_key: 7480000000000000FF2F00000000000000F8 end_key: 7480000000000000FF3400000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 49 store_id: 1 }"]
   > [2024/07/16 15:37:58.951 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(46)] [region=48]
   > [2024/07/16 15:37:58.961 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF3500000000000000F8 new_region_id: 50 new_peer_ids: 51 } right_derive: true }"] [index=59] [term=6] [peer_id=3] [region_id=2]
   > [2024/07/16 15:37:58.961 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF3500000000000000F8"] [region="id: 2 start_key: 7480000000000000FF3400000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/07/16 15:37:58.967 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/16 15:37:58.967 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=2]
   > [2024/07/16 15:37:58.967 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(45)] [region_id=2] [store_id=Some(1)]
   > [2024/07/16 15:37:58.967 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF3500000000000000F8 region_epoch { conf_ver: 1 version: 25 } peers { id: 3 store_id: 1 }"]
   > [2024/07/16 15:37:58.967 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/07/16 15:37:58.967 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 50 start_key: 7480000000000000FF3400000000000000F8 end_key: 7480000000000000FF3500000000000000F8 region_epoch { conf_ver: 1 version: 25 } peers { id: 51 store_id: 1 }"] [region_id=50]
   > [2024/07/16 15:37:58.967 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=51] [region_id=50]
   > [2024/07/16 15:37:58.967 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 2 start_key: 7480000000000000FF3500000000000000F8 region_epoch { conf_ver: 1 version: 25 } peers { id: 3 store_id: 1 } }"]
   > [2024/07/16 15:37:58.967 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 2 start_key: 7480000000000000FF3500000000000000F8 region_epoch { conf_ver: 1 version: 25 } peers { id: 3 store_id: 1 }"]
   > [2024/07/16 15:37:58.967 +00:00] [INFO] [split_region.go:156] ["batch split regions complete"] ["batch region ID"=2] ["first at"=748000000000000035] ["first new region left"="{Id:50 StartKey:7480000000000000ff3400000000000000f8 EndKey:7480000000000000ff3500000000000000f8 RegionEpoch:{ConfVer:1 Version:25} Peers:[id:51 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/16 15:37:58.967 +00:00] [INFO] [split_region.go:205] ["split regions complete"] ["region count"=1] ["region IDs"="[50]"]
   > [2024/07/16 15:37:58.967 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {51} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=51] [region_id=50]
   > [2024/07/16 15:37:58.967 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=51] [region_id=50]
   > [2024/07/16 15:37:58.967 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF3400000000000000F8} -> {7480000000000000FF3500000000000000F8}, EndKey:{}"] [old-version=24] [new-version=25]
   > [2024/07/16 15:37:58.967 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=2] [origin="id:50 start_key:\"7480000000000000FF3400000000000000F8\" end_key:\"7480000000000000FF3500000000000000F8\" region_epoch:<conf_ver:1 version:25 > peers:<id:51 store_id:1 >"] [total=1]
   > [2024/07/16 15:37:58.967 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {51} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=51] [region_id=50]
   > [2024/07/16 15:37:58.967 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 51."] [id=51] [raft_id=51] [region_id=50]
   > [2024/07/16 15:37:58.968 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=51] [region_id=50]
   > [2024/07/16 15:37:58.968 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=51] [region_id=50]
   > [2024/07/16 15:37:58.968 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=51] [region_id=50]
   > [2024/07/16 15:37:58.968 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=51] [region_id=50]
   > [2024/07/16 15:37:58.968 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803826] [region_id=50]
   > [2024/07/16 15:37:58.968 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=50]
   > [2024/07/16 15:37:58.973 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=59] [observe_id=ObserveId(47)] [region=2]
   > [2024/07/16 15:37:58.973 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 50 start_key: 7480000000000000FF3400000000000000F8 end_key: 7480000000000000FF3500000000000000F8 region_epoch { conf_ver: 1 version: 25 } peers { id: 51 store_id: 1 }"]
   > [2024/07/16 15:37:58.973 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(48)] [region=50]
   > [2024/07/16 15:37:59.996 +00:00] [INFO] [set.go:216] ["set global var"] [conn=4] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/07/16 15:37:59.998 +00:00] [INFO] [set.go:216] ["set global var"] [conn=4] [name=transaction_isolation] [val=REPEATABLE-READ]
   > [2024/07/16 15:38:00.586 +00:00] [INFO] [scheduler.rs:640] ["get snapshot failed"] [err="Error(Request(message: \"EpochNotMatch current epoch of region 2 is conf_ver: 1 version: 25, but you sent conf_ver: 1 version: 24\" epoch_not_match { current_regions { id: 2 start_key: 7480000000000000FF3500000000000000F8 region_epoch { conf_ver: 1 version: 25 } peers { id: 3 store_id: 1 } } current_regions { id: 50 start_key: 7480000000000000FF3400000000000000F8 end_key: 7480000000000000FF3500000000000000F8 region_epoch { conf_ver: 1 version: 25 } peers { id: 51 store_id: 1 } } }))"] [cid=279]
   > [2024/07/16 15:38:01.157 +00:00] [INFO] [cluster.go:1469] ["store has changed to serving"] [store-id=1] [store-address=127.0.0.1:20160]
   > [2024/07/16 15:38:01.207 +00:00] [INFO] [client.rs:789] ["set cluster version to 6.4.0"]

### Scenario 1
 * Instruction #0:
     - Instruction:  insert into t1 values (10);
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 1 / 0
 * Instruction #1:
     - Instruction:  update t1 set c_int = c_int + 10 where c_int in (1, 11);
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 1 / 0
 * Instruction #2:
     - Instruction:  select * from t1 order by c_int;
     - Transaction: conn_0
     - Output: [(10,), (11,)]
     - Executed order: 2
     - Affected rows / Warnings: 2 / 0

 * Container logs:
   > [2024/07/16 15:38:13.638 +00:00] [INFO] [session.go:2269] ["CRUCIAL OPERATION"] [conn=6] [schemaVersion=34] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.77]
   > [2024/07/16 15:38:13.660 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:61, Type:drop schema, State:none, SchemaState:none, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 15:38:13.601 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/16 15:38:13.660 +00:00] [INFO] [ddl.go:475] ["[ddl] start DDL job"] [job="ID:61, Type:drop schema, State:none, SchemaState:none, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 15:38:13.601 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/16 15:38:13.663 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:61, Type:drop schema, State:none, SchemaState:none, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 15:38:13.601 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:38:13.688 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=34] [neededSchemaVersion=35] ["start time"=735.157µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/16 15:38:13.738 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=35] ["take time"=58.024102ms] [job="ID:61, Type:drop schema, State:running, SchemaState:write only, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 15:38:13.601 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:38:13.740 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:61, Type:drop schema, State:running, SchemaState:write only, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 15:38:13.601 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:38:13.773 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=35] [neededSchemaVersion=36] ["start time"=788.377µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/16 15:38:13.823 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=36] ["take time"=65.076825ms] [job="ID:61, Type:drop schema, State:running, SchemaState:delete only, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 15:38:13.601 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:38:13.825 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:61, Type:drop schema, State:running, SchemaState:delete only, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 15:38:13.601 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:38:13.853 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=36] [neededSchemaVersion=37] ["start time"=814.498µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/16 15:38:13.903 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=37] ["take time"=58.202129ms] [job="ID:61, Type:drop schema, State:done, SchemaState:none, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 15:38:13.601 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:38:13.905 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=61] [jobType="drop schema"]
   > [2024/07/16 15:38:13.907 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:61, Type:drop schema, State:synced, SchemaState:none, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 15:38:13.601 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:38:13.924 +00:00] [INFO] [ddl.go:507] ["[ddl] DDL job is finished"] [jobID=61]
   > [2024/07/16 15:38:13.924 +00:00] [INFO] [domain.go:646] ["performing DDL change, must reload"]
   > [2024/07/16 15:38:13.926 +00:00] [INFO] [session.go:2269] ["CRUCIAL OPERATION"] [conn=6] [schemaVersion=37] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.77]
   > [2024/07/16 15:38:13.957 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:63, Type:create schema, State:none, SchemaState:none, SchemaID:62, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-16 15:38:13.9 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/16 15:38:13.957 +00:00] [INFO] [ddl.go:475] ["[ddl] start DDL job"] [job="ID:63, Type:create schema, State:none, SchemaState:none, SchemaID:62, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-16 15:38:13.9 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/16 15:38:13.960 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:63, Type:create schema, State:none, SchemaState:none, SchemaID:62, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 15:38:13.9 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:38:13.986 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=37] [neededSchemaVersion=38] ["start time"=1.231875ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/16 15:38:14.035 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=38] ["take time"=57.741102ms] [job="ID:63, Type:create schema, State:done, SchemaState:public, SchemaID:62, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-16 15:38:13.9 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:38:14.039 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:63, Type:create schema, State:synced, SchemaState:public, SchemaID:62, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 15:38:13.9 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:38:14.056 +00:00] [INFO] [ddl.go:507] ["[ddl] DDL job is finished"] [jobID=63]
   > [2024/07/16 15:38:14.056 +00:00] [INFO] [domain.go:646] ["performing DDL change, must reload"]
   > [2024/07/16 15:38:14.060 +00:00] [INFO] [session.go:2269] ["CRUCIAL OPERATION"] [conn=6] [schemaVersion=38] [cur_db=testdb] [sql="create table t1  (c_int int, primary key (c_int)) partition by range (c_int) (partition p0 values less than (10), partition p1 values less than maxvalue) ;"] [user=root@10.88.0.77]
   > [2024/07/16 15:38:14.110 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:67, Type:create table, State:none, SchemaState:none, SchemaID:62, TableID:64, RowCount:0, ArgLen:1, start time: 2024-07-16 15:38:14.05 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/16 15:38:14.110 +00:00] [INFO] [ddl.go:475] ["[ddl] start DDL job"] [job="ID:67, Type:create table, State:none, SchemaState:none, SchemaID:62, TableID:64, RowCount:0, ArgLen:1, start time: 2024-07-16 15:38:14.05 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t1  (c_int int, primary key (c_int)) partition by range (c_int) (partition p0 values less than (10), partition p1 values less than maxvalue) ;"]
   > [2024/07/16 15:38:14.114 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:create table, State:none, SchemaState:none, SchemaID:62, TableID:64, RowCount:0, ArgLen:0, start time: 2024-07-16 15:38:14.05 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:38:14.155 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=38] [neededSchemaVersion=39] ["start time"=2.274197ms] [phyTblIDs="[64,65,66]"] [actionTypes="[8,8,8]"]
   > [2024/07/16 15:38:14.209 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=39] ["take time"=66.61845ms] [job="ID:67, Type:create table, State:done, SchemaState:public, SchemaID:62, TableID:64, RowCount:0, ArgLen:1, start time: 2024-07-16 15:38:14.05 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:38:14.212 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:create table, State:synced, SchemaState:public, SchemaID:62, TableID:64, RowCount:0, ArgLen:0, start time: 2024-07-16 15:38:14.05 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:38:14.229 +00:00] [INFO] [ddl.go:507] ["[ddl] DDL job is finished"] [jobID=67]
   > [2024/07/16 15:38:14.232 +00:00] [INFO] [domain.go:646] ["performing DDL change, must reload"]
   > [2024/07/16 15:38:14.232 +00:00] [INFO] [split_region.go:59] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=748000000000000041]
   > [2024/07/16 15:38:14.232 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:46910] [split_keys="key 7480000000000000FF4100000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/16 15:38:14.233 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=54] [peer-ids="[55]"]
   > [2024/07/16 15:38:14.233 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF3A00000000000000F8 region_epoch { conf_ver: 1 version: 26 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 54 new_peer_ids: 55]"] [region_id=2]
   > [2024/07/16 15:38:14.239 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF4100000000000000F8 new_region_id: 54 new_peer_ids: 55 } right_derive: true }"] [index=69] [term=6] [peer_id=3] [region_id=2]
   > [2024/07/16 15:38:14.239 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF4100000000000000F8"] [region="id: 2 start_key: 7480000000000000FF3A00000000000000F8 region_epoch { conf_ver: 1 version: 26 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/07/16 15:38:14.245 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/16 15:38:14.245 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=2]
   > [2024/07/16 15:38:14.245 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/07/16 15:38:14.245 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(49)] [region_id=2] [store_id=Some(1)]
   > [2024/07/16 15:38:14.245 +00:00] [INFO] [split_region.go:156] ["batch split regions complete"] ["batch region ID"=2] ["first at"=748000000000000041] ["first new region left"="{Id:54 StartKey:7480000000000000ff3a00000000000000f8 EndKey:7480000000000000ff4100000000000000f8 RegionEpoch:{ConfVer:1 Version:27} Peers:[id:55 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/16 15:38:14.245 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF4100000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 3 store_id: 1 }"]
   > [2024/07/16 15:38:14.245 +00:00] [INFO] [split_region.go:205] ["split regions complete"] ["region count"=1] ["region IDs"="[54]"]
   > [2024/07/16 15:38:14.245 +00:00] [INFO] [split_region.go:59] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=748000000000000042]
   > [2024/07/16 15:38:14.245 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 54 start_key: 7480000000000000FF3A00000000000000F8 end_key: 7480000000000000FF4100000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 55 store_id: 1 }"] [region_id=54]
   > [2024/07/16 15:38:14.245 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=55] [region_id=54]
   > [2024/07/16 15:38:14.245 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 2 start_key: 7480000000000000FF4100000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 3 store_id: 1 } }"]
   > [2024/07/16 15:38:14.245 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 2 start_key: 7480000000000000FF4100000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 3 store_id: 1 }"]
   > [2024/07/16 15:38:14.246 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF3A00000000000000F8} -> {7480000000000000FF4100000000000000F8}, EndKey:{}"] [old-version=26] [new-version=27]
   > [2024/07/16 15:38:14.246 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {55} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=55] [region_id=54]
   > [2024/07/16 15:38:14.246 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=2] [origin="id:54 start_key:\"7480000000000000FF3A00000000000000F8\" end_key:\"7480000000000000FF4100000000000000F8\" region_epoch:<conf_ver:1 version:27 > peers:<id:55 store_id:1 >"] [total=1]
   > [2024/07/16 15:38:14.246 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=55] [region_id=54]
   > [2024/07/16 15:38:14.246 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {55} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=55] [region_id=54]
   > [2024/07/16 15:38:14.246 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 55."] [id=55] [raft_id=55] [region_id=54]
   > [2024/07/16 15:38:14.246 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=55] [region_id=54]
   > [2024/07/16 15:38:14.246 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=55] [region_id=54]
   > [2024/07/16 15:38:14.246 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=55] [region_id=54]
   > [2024/07/16 15:38:14.246 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=55] [region_id=54]
   > [2024/07/16 15:38:14.246 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803830] [region_id=54]
   > [2024/07/16 15:38:14.246 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=69] [observe_id=ObserveId(51)] [region=2]
   > [2024/07/16 15:38:14.247 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:46926] [split_keys="key 7480000000000000FF4200000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/16 15:38:14.247 +00:00] [INFO] [peer.rs:5566] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 26"] [prev_epoch="conf_ver: 1 version: 27"] [peer_id=3] [region_id=2]
   > [2024/07/16 15:38:14.247 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=54]
   > [2024/07/16 15:38:14.249 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:46940] [split_keys="key 7480000000000000FF4200000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/16 15:38:14.249 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=56] [peer-ids="[57]"]
   > [2024/07/16 15:38:14.250 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF4100000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 56 new_peer_ids: 57]"] [region_id=2]
   > [2024/07/16 15:38:14.251 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 54 start_key: 7480000000000000FF3A00000000000000F8 end_key: 7480000000000000FF4100000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 55 store_id: 1 }"]
   > [2024/07/16 15:38:14.252 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(52)] [region=54]
   > [2024/07/16 15:38:14.262 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF4200000000000000F8 new_region_id: 56 new_peer_ids: 57 } right_derive: true }"] [index=71] [term=6] [peer_id=3] [region_id=2]
   > [2024/07/16 15:38:14.262 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF4200000000000000F8"] [region="id: 2 start_key: 7480000000000000FF4100000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/07/16 15:38:14.267 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/16 15:38:14.268 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=2]
   > [2024/07/16 15:38:14.268 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/07/16 15:38:14.268 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(51)] [region_id=2] [store_id=Some(1)]
   > [2024/07/16 15:38:14.268 +00:00] [INFO] [split_region.go:156] ["batch split regions complete"] ["batch region ID"=2] ["first at"=748000000000000042] ["first new region left"="{Id:56 StartKey:7480000000000000ff4100000000000000f8 EndKey:7480000000000000ff4200000000000000f8 RegionEpoch:{ConfVer:1 Version:28} Peers:[id:57 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/16 15:38:14.268 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF4200000000000000F8 region_epoch { conf_ver: 1 version: 28 } peers { id: 3 store_id: 1 }"]
   > [2024/07/16 15:38:14.268 +00:00] [INFO] [split_region.go:205] ["split regions complete"] ["region count"=1] ["region IDs"="[56]"]
   > [2024/07/16 15:38:14.268 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 56 start_key: 7480000000000000FF4100000000000000F8 end_key: 7480000000000000FF4200000000000000F8 region_epoch { conf_ver: 1 version: 28 } peers { id: 57 store_id: 1 }"] [region_id=56]
   > [2024/07/16 15:38:14.268 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=57] [region_id=56]
   > [2024/07/16 15:38:14.268 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 2 start_key: 7480000000000000FF4200000000000000F8 region_epoch { conf_ver: 1 version: 28 } peers { id: 3 store_id: 1 } }"]
   > [2024/07/16 15:38:14.268 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF4100000000000000F8} -> {7480000000000000FF4200000000000000F8}, EndKey:{}"] [old-version=27] [new-version=28]
   > [2024/07/16 15:38:14.268 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 2 start_key: 7480000000000000FF4200000000000000F8 region_epoch { conf_ver: 1 version: 28 } peers { id: 3 store_id: 1 }"]
   > [2024/07/16 15:38:14.268 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {57} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=57] [region_id=56]
   > [2024/07/16 15:38:14.268 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=2] [origin="id:56 start_key:\"7480000000000000FF4100000000000000F8\" end_key:\"7480000000000000FF4200000000000000F8\" region_epoch:<conf_ver:1 version:28 > peers:<id:57 store_id:1 >"] [total=1]
   > [2024/07/16 15:38:14.268 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=57] [region_id=56]
   > [2024/07/16 15:38:14.268 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {57} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=57] [region_id=56]
   > [2024/07/16 15:38:14.269 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 57."] [id=57] [raft_id=57] [region_id=56]
   > [2024/07/16 15:38:14.269 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=57] [region_id=56]
   > [2024/07/16 15:38:14.269 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=57] [region_id=56]
   > [2024/07/16 15:38:14.269 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=57] [region_id=56]
   > [2024/07/16 15:38:14.269 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=57] [region_id=56]
   > [2024/07/16 15:38:14.269 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803832] [region_id=56]
   > [2024/07/16 15:38:14.269 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=71] [observe_id=ObserveId(53)] [region=2]
   > [2024/07/16 15:38:14.269 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=56]
   > [2024/07/16 15:38:14.274 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 56 start_key: 7480000000000000FF4100000000000000F8 end_key: 7480000000000000FF4200000000000000F8 region_epoch { conf_ver: 1 version: 28 } peers { id: 57 store_id: 1 }"]
   > [2024/07/16 15:38:14.274 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(54)] [region=56]
