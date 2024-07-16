# Bug ID TIDB-19585-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/19585
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              The second select should output the same table as the first one, but it doesn't.


## Details
 * Database: tidb-b0c3fe7b.tikv
 * Number of scenarios: 2
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
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
   > [2024/07/16 15:38:28.041 +00:00] [INFO] [session.go:2269] ["CRUCIAL OPERATION"] [conn=9] [schemaVersion=47] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.77]
   > [2024/07/16 15:38:28.056 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:74, Type:drop schema, State:none, SchemaState:none, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 15:38:28.001 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/16 15:38:28.056 +00:00] [INFO] [ddl.go:475] ["[ddl] start DDL job"] [job="ID:74, Type:drop schema, State:none, SchemaState:none, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 15:38:28.001 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/16 15:38:28.059 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:74, Type:drop schema, State:none, SchemaState:none, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 15:38:28.001 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:38:28.084 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=47] [neededSchemaVersion=48] ["start time"=844.531µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/16 15:38:28.134 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=48] ["take time"=57.529759ms] [job="ID:74, Type:drop schema, State:running, SchemaState:write only, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 15:38:28.001 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:38:28.136 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:74, Type:drop schema, State:running, SchemaState:write only, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 15:38:28.001 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:38:28.159 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=48] [neededSchemaVersion=49] ["start time"=619.359µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/16 15:38:28.209 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=49] ["take time"=56.87492ms] [job="ID:74, Type:drop schema, State:running, SchemaState:delete only, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 15:38:28.001 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:38:28.211 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:74, Type:drop schema, State:running, SchemaState:delete only, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 15:38:28.001 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:38:28.244 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=49] [neededSchemaVersion=50] ["start time"=599.105µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/16 15:38:28.293 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=50] ["take time"=65.07885ms] [job="ID:74, Type:drop schema, State:done, SchemaState:none, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 15:38:28.001 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:38:28.296 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=74] [jobType="drop schema"]
   > [2024/07/16 15:38:28.298 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:74, Type:drop schema, State:synced, SchemaState:none, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 15:38:28.001 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:38:28.314 +00:00] [INFO] [ddl.go:507] ["[ddl] DDL job is finished"] [jobID=74]
   > [2024/07/16 15:38:28.314 +00:00] [INFO] [domain.go:646] ["performing DDL change, must reload"]
   > [2024/07/16 15:38:28.316 +00:00] [INFO] [session.go:2269] ["CRUCIAL OPERATION"] [conn=9] [schemaVersion=50] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.77]
   > [2024/07/16 15:38:28.346 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:76, Type:create schema, State:none, SchemaState:none, SchemaID:75, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-16 15:38:28.3 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/16 15:38:28.346 +00:00] [INFO] [ddl.go:475] ["[ddl] start DDL job"] [job="ID:76, Type:create schema, State:none, SchemaState:none, SchemaID:75, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-16 15:38:28.3 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/16 15:38:28.350 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:76, Type:create schema, State:none, SchemaState:none, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 15:38:28.3 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:38:28.374 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=50] [neededSchemaVersion=51] ["start time"=1.371419ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/16 15:38:28.423 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=51] ["take time"=56.847263ms] [job="ID:76, Type:create schema, State:done, SchemaState:public, SchemaID:75, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-16 15:38:28.3 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:38:28.427 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:76, Type:create schema, State:synced, SchemaState:public, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 15:38:28.3 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:38:28.443 +00:00] [INFO] [ddl.go:507] ["[ddl] DDL job is finished"] [jobID=76]
   > [2024/07/16 15:38:28.443 +00:00] [INFO] [domain.go:646] ["performing DDL change, must reload"]
   > [2024/07/16 15:38:28.446 +00:00] [INFO] [session.go:2269] ["CRUCIAL OPERATION"] [conn=9] [schemaVersion=51] [cur_db=testdb] [sql="create table t1  (c_int int, primary key (c_int)) partition by range (c_int) (partition p0 values less than (10), partition p1 values less than maxvalue) ;"] [user=root@10.88.0.77]
   > [2024/07/16 15:38:28.500 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:80, Type:create table, State:none, SchemaState:none, SchemaID:75, TableID:77, RowCount:0, ArgLen:1, start time: 2024-07-16 15:38:28.451 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/16 15:38:28.500 +00:00] [INFO] [ddl.go:475] ["[ddl] start DDL job"] [job="ID:80, Type:create table, State:none, SchemaState:none, SchemaID:75, TableID:77, RowCount:0, ArgLen:1, start time: 2024-07-16 15:38:28.451 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t1  (c_int int, primary key (c_int)) partition by range (c_int) (partition p0 values less than (10), partition p1 values less than maxvalue) ;"]
   > [2024/07/16 15:38:28.504 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:80, Type:create table, State:none, SchemaState:none, SchemaID:75, TableID:77, RowCount:0, ArgLen:0, start time: 2024-07-16 15:38:28.451 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:38:28.537 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=51] [neededSchemaVersion=52] ["start time"=2.120685ms] [phyTblIDs="[77,78,79]"] [actionTypes="[8,8,8]"]
   > [2024/07/16 15:38:28.586 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=52] ["take time"=61.193116ms] [job="ID:80, Type:create table, State:done, SchemaState:public, SchemaID:75, TableID:77, RowCount:0, ArgLen:1, start time: 2024-07-16 15:38:28.451 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:38:28.590 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:80, Type:create table, State:synced, SchemaState:public, SchemaID:75, TableID:77, RowCount:0, ArgLen:0, start time: 2024-07-16 15:38:28.451 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:38:28.606 +00:00] [INFO] [ddl.go:507] ["[ddl] DDL job is finished"] [jobID=80]
   > [2024/07/16 15:38:28.608 +00:00] [INFO] [domain.go:646] ["performing DDL change, must reload"]
   > [2024/07/16 15:38:28.608 +00:00] [INFO] [split_region.go:59] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=74800000000000004e]
   > [2024/07/16 15:38:28.609 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:46910] [split_keys="key 7480000000000000FF4E00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/16 15:38:28.609 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=60] [peer-ids="[61]"]
   > [2024/07/16 15:38:28.610 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF4700000000000000F8 region_epoch { conf_ver: 1 version: 29 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 60 new_peer_ids: 61]"] [region_id=2]
   > [2024/07/16 15:38:28.615 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF4E00000000000000F8 new_region_id: 60 new_peer_ids: 61 } right_derive: true }"] [index=80] [term=6] [peer_id=3] [region_id=2]
   > [2024/07/16 15:38:28.615 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF4E00000000000000F8"] [region="id: 2 start_key: 7480000000000000FF4700000000000000F8 region_epoch { conf_ver: 1 version: 29 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/07/16 15:38:28.620 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/16 15:38:28.620 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=2]
   > [2024/07/16 15:38:28.620 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(55)] [region_id=2] [store_id=Some(1)]
   > [2024/07/16 15:38:28.620 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/07/16 15:38:28.620 +00:00] [INFO] [split_region.go:156] ["batch split regions complete"] ["batch region ID"=2] ["first at"=74800000000000004e] ["first new region left"="{Id:60 StartKey:7480000000000000ff4700000000000000f8 EndKey:7480000000000000ff4e00000000000000f8 RegionEpoch:{ConfVer:1 Version:30} Peers:[id:61 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/16 15:38:28.621 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF4E00000000000000F8 region_epoch { conf_ver: 1 version: 30 } peers { id: 3 store_id: 1 }"]
   > [2024/07/16 15:38:28.621 +00:00] [INFO] [split_region.go:205] ["split regions complete"] ["region count"=1] ["region IDs"="[60]"]
   > [2024/07/16 15:38:28.621 +00:00] [INFO] [split_region.go:59] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=74800000000000004f]
   > [2024/07/16 15:38:28.621 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 60 start_key: 7480000000000000FF4700000000000000F8 end_key: 7480000000000000FF4E00000000000000F8 region_epoch { conf_ver: 1 version: 30 } peers { id: 61 store_id: 1 }"] [region_id=60]
   > [2024/07/16 15:38:28.621 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=61] [region_id=60]
   > [2024/07/16 15:38:28.621 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 2 start_key: 7480000000000000FF4E00000000000000F8 region_epoch { conf_ver: 1 version: 30 } peers { id: 3 store_id: 1 } }"]
   > [2024/07/16 15:38:28.621 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 2 start_key: 7480000000000000FF4E00000000000000F8 region_epoch { conf_ver: 1 version: 30 } peers { id: 3 store_id: 1 }"]
   > [2024/07/16 15:38:28.621 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF4700000000000000F8} -> {7480000000000000FF4E00000000000000F8}, EndKey:{}"] [old-version=29] [new-version=30]
   > [2024/07/16 15:38:28.621 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {61} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=61] [region_id=60]
   > [2024/07/16 15:38:28.621 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=2] [origin="id:60 start_key:\"7480000000000000FF4700000000000000F8\" end_key:\"7480000000000000FF4E00000000000000F8\" region_epoch:<conf_ver:1 version:30 > peers:<id:61 store_id:1 >"] [total=1]
   > [2024/07/16 15:38:28.621 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=61] [region_id=60]
   > [2024/07/16 15:38:28.621 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {61} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=61] [region_id=60]
   > [2024/07/16 15:38:28.621 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 61."] [id=61] [raft_id=61] [region_id=60]
   > [2024/07/16 15:38:28.621 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=61] [region_id=60]
   > [2024/07/16 15:38:28.622 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=61] [region_id=60]
   > [2024/07/16 15:38:28.622 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=61] [region_id=60]
   > [2024/07/16 15:38:28.622 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=61] [region_id=60]
   > [2024/07/16 15:38:28.622 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803836] [region_id=60]
   > [2024/07/16 15:38:28.622 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=80] [observe_id=ObserveId(57)] [region=2]
   > [2024/07/16 15:38:28.622 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:46926] [split_keys="key 7480000000000000FF4F00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/16 15:38:28.622 +00:00] [INFO] [peer.rs:5566] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 29"] [prev_epoch="conf_ver: 1 version: 30"] [peer_id=3] [region_id=2]
   > [2024/07/16 15:38:28.622 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=60]
   > [2024/07/16 15:38:28.624 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:46940] [split_keys="key 7480000000000000FF4F00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/16 15:38:28.625 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=62] [peer-ids="[63]"]
   > [2024/07/16 15:38:28.625 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF4E00000000000000F8 region_epoch { conf_ver: 1 version: 30 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 62 new_peer_ids: 63]"] [region_id=2]
   > [2024/07/16 15:38:28.626 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 60 start_key: 7480000000000000FF4700000000000000F8 end_key: 7480000000000000FF4E00000000000000F8 region_epoch { conf_ver: 1 version: 30 } peers { id: 61 store_id: 1 }"]
   > [2024/07/16 15:38:28.626 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(58)] [region=60]
   > [2024/07/16 15:38:28.636 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF4F00000000000000F8 new_region_id: 62 new_peer_ids: 63 } right_derive: true }"] [index=82] [term=6] [peer_id=3] [region_id=2]
   > [2024/07/16 15:38:28.636 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF4F00000000000000F8"] [region="id: 2 start_key: 7480000000000000FF4E00000000000000F8 region_epoch { conf_ver: 1 version: 30 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/07/16 15:38:28.641 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/16 15:38:28.641 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=2]
   > [2024/07/16 15:38:28.641 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/07/16 15:38:28.641 +00:00] [INFO] [split_region.go:156] ["batch split regions complete"] ["batch region ID"=2] ["first at"=74800000000000004f] ["first new region left"="{Id:62 StartKey:7480000000000000ff4e00000000000000f8 EndKey:7480000000000000ff4f00000000000000f8 RegionEpoch:{ConfVer:1 Version:31} Peers:[id:63 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/16 15:38:28.641 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(57)] [region_id=2] [store_id=Some(1)]
   > [2024/07/16 15:38:28.641 +00:00] [INFO] [split_region.go:205] ["split regions complete"] ["region count"=1] ["region IDs"="[62]"]
   > [2024/07/16 15:38:28.641 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF4F00000000000000F8 region_epoch { conf_ver: 1 version: 31 } peers { id: 3 store_id: 1 }"]
   > [2024/07/16 15:38:28.641 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF4E00000000000000F8} -> {7480000000000000FF4F00000000000000F8}, EndKey:{}"] [old-version=30] [new-version=31]
   > [2024/07/16 15:38:28.641 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 62 start_key: 7480000000000000FF4E00000000000000F8 end_key: 7480000000000000FF4F00000000000000F8 region_epoch { conf_ver: 1 version: 31 } peers { id: 63 store_id: 1 }"] [region_id=62]
   > [2024/07/16 15:38:28.641 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=63] [region_id=62]
   > [2024/07/16 15:38:28.641 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 2 start_key: 7480000000000000FF4F00000000000000F8 region_epoch { conf_ver: 1 version: 31 } peers { id: 3 store_id: 1 } }"]
   > [2024/07/16 15:38:28.641 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 2 start_key: 7480000000000000FF4F00000000000000F8 region_epoch { conf_ver: 1 version: 31 } peers { id: 3 store_id: 1 }"]
   > [2024/07/16 15:38:28.642 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {63} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=63] [region_id=62]
   > [2024/07/16 15:38:28.642 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=2] [origin="id:62 start_key:\"7480000000000000FF4E00000000000000F8\" end_key:\"7480000000000000FF4F00000000000000F8\" region_epoch:<conf_ver:1 version:31 > peers:<id:63 store_id:1 >"] [total=1]
   > [2024/07/16 15:38:28.642 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=63] [region_id=62]
   > [2024/07/16 15:38:28.642 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {63} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=63] [region_id=62]
   > [2024/07/16 15:38:28.642 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 63."] [id=63] [raft_id=63] [region_id=62]
   > [2024/07/16 15:38:28.642 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=63] [region_id=62]
   > [2024/07/16 15:38:28.642 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=63] [region_id=62]
   > [2024/07/16 15:38:28.642 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=63] [region_id=62]
   > [2024/07/16 15:38:28.642 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=63] [region_id=62]
   > [2024/07/16 15:38:28.642 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803838] [region_id=62]
   > [2024/07/16 15:38:28.643 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=82] [observe_id=ObserveId(59)] [region=2]
   > [2024/07/16 15:38:28.643 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=62]
   > [2024/07/16 15:38:28.647 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 62 start_key: 7480000000000000FF4E00000000000000F8 end_key: 7480000000000000FF4F00000000000000F8 region_epoch { conf_ver: 1 version: 31 } peers { id: 63 store_id: 1 }"]
   > [2024/07/16 15:38:28.647 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(60)] [region=62]
   > [2024/07/16 15:38:29.702 +00:00] [INFO] [set.go:216] ["set global var"] [conn=10] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/07/16 15:38:29.718 +00:00] [INFO] [set.go:216] ["set global var"] [conn=10] [name=transaction_isolation] [val=READ-COMMITTED]

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
   > [2024/07/16 15:38:43.374 +00:00] [INFO] [session.go:2269] ["CRUCIAL OPERATION"] [conn=12] [schemaVersion=60] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.77]
   > [2024/07/16 15:38:43.396 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:87, Type:drop schema, State:none, SchemaState:none, SchemaID:82, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 15:38:43.351 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/16 15:38:43.397 +00:00] [INFO] [ddl.go:475] ["[ddl] start DDL job"] [job="ID:87, Type:drop schema, State:none, SchemaState:none, SchemaID:82, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 15:38:43.351 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/16 15:38:43.400 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:87, Type:drop schema, State:none, SchemaState:none, SchemaID:82, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 15:38:43.351 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:38:43.426 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=60] [neededSchemaVersion=61] ["start time"=732.713µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/16 15:38:43.477 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=61] ["take time"=58.898664ms] [job="ID:87, Type:drop schema, State:running, SchemaState:write only, SchemaID:82, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 15:38:43.351 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:38:43.479 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:87, Type:drop schema, State:running, SchemaState:write only, SchemaID:82, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 15:38:43.351 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:38:43.505 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=61] [neededSchemaVersion=62] ["start time"=739.279µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/16 15:38:43.555 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=62] ["take time"=58.078299ms] [job="ID:87, Type:drop schema, State:running, SchemaState:delete only, SchemaID:82, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 15:38:43.351 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:38:43.557 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:87, Type:drop schema, State:running, SchemaState:delete only, SchemaID:82, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 15:38:43.351 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:38:43.593 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=62] [neededSchemaVersion=63] ["start time"=885.248µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/16 15:38:43.643 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=63] ["take time"=65.441331ms] [job="ID:87, Type:drop schema, State:done, SchemaState:none, SchemaID:82, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 15:38:43.351 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:38:43.646 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=87] [jobType="drop schema"]
   > [2024/07/16 15:38:43.647 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:87, Type:drop schema, State:synced, SchemaState:none, SchemaID:82, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 15:38:43.351 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:38:43.664 +00:00] [INFO] [ddl.go:507] ["[ddl] DDL job is finished"] [jobID=87]
   > [2024/07/16 15:38:43.664 +00:00] [INFO] [domain.go:646] ["performing DDL change, must reload"]
   > [2024/07/16 15:38:43.666 +00:00] [INFO] [session.go:2269] ["CRUCIAL OPERATION"] [conn=12] [schemaVersion=63] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.77]
   > [2024/07/16 15:38:43.695 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:89, Type:create schema, State:none, SchemaState:none, SchemaID:88, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-16 15:38:43.651 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/16 15:38:43.695 +00:00] [INFO] [ddl.go:475] ["[ddl] start DDL job"] [job="ID:89, Type:create schema, State:none, SchemaState:none, SchemaID:88, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-16 15:38:43.651 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/16 15:38:43.698 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:89, Type:create schema, State:none, SchemaState:none, SchemaID:88, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 15:38:43.651 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:38:43.729 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=63] [neededSchemaVersion=64] ["start time"=1.473807ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/16 15:38:43.778 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=64] ["take time"=57.257446ms] [job="ID:89, Type:create schema, State:done, SchemaState:public, SchemaID:88, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-16 15:38:43.651 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:38:43.782 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:89, Type:create schema, State:synced, SchemaState:public, SchemaID:88, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 15:38:43.651 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:38:43.798 +00:00] [INFO] [ddl.go:507] ["[ddl] DDL job is finished"] [jobID=89]
   > [2024/07/16 15:38:43.798 +00:00] [INFO] [domain.go:646] ["performing DDL change, must reload"]
   > [2024/07/16 15:38:43.802 +00:00] [INFO] [session.go:2269] ["CRUCIAL OPERATION"] [conn=12] [schemaVersion=64] [cur_db=testdb] [sql="create table t1  (c_int int, primary key (c_int)) partition by range (c_int) (partition p0 values less than (10), partition p1 values less than maxvalue) ;"] [user=root@10.88.0.77]
   > [2024/07/16 15:38:43.851 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:93, Type:create table, State:none, SchemaState:none, SchemaID:88, TableID:90, RowCount:0, ArgLen:1, start time: 2024-07-16 15:38:43.8 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/16 15:38:43.851 +00:00] [INFO] [ddl.go:475] ["[ddl] start DDL job"] [job="ID:93, Type:create table, State:none, SchemaState:none, SchemaID:88, TableID:90, RowCount:0, ArgLen:1, start time: 2024-07-16 15:38:43.8 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t1  (c_int int, primary key (c_int)) partition by range (c_int) (partition p0 values less than (10), partition p1 values less than maxvalue) ;"]
   > [2024/07/16 15:38:43.854 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:93, Type:create table, State:none, SchemaState:none, SchemaID:88, TableID:90, RowCount:0, ArgLen:0, start time: 2024-07-16 15:38:43.8 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:38:43.895 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=64] [neededSchemaVersion=65] ["start time"=3.343061ms] [phyTblIDs="[90,91,92]"] [actionTypes="[8,8,8]"]
   > [2024/07/16 15:38:43.942 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=65] ["take time"=60.55434ms] [job="ID:93, Type:create table, State:done, SchemaState:public, SchemaID:88, TableID:90, RowCount:0, ArgLen:1, start time: 2024-07-16 15:38:43.8 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:38:43.944 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:93, Type:create table, State:synced, SchemaState:public, SchemaID:88, TableID:90, RowCount:0, ArgLen:0, start time: 2024-07-16 15:38:43.8 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 15:38:43.959 +00:00] [INFO] [ddl.go:507] ["[ddl] DDL job is finished"] [jobID=93]
   > [2024/07/16 15:38:43.961 +00:00] [INFO] [domain.go:646] ["performing DDL change, must reload"]
   > [2024/07/16 15:38:43.961 +00:00] [INFO] [split_region.go:59] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=74800000000000005b]
   > [2024/07/16 15:38:43.962 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:46910] [split_keys="key 7480000000000000FF5B00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/16 15:38:43.962 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=66] [peer-ids="[67]"]
   > [2024/07/16 15:38:43.963 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF5400000000000000F8 region_epoch { conf_ver: 1 version: 32 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 66 new_peer_ids: 67]"] [region_id=2]
   > [2024/07/16 15:38:43.968 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF5B00000000000000F8 new_region_id: 66 new_peer_ids: 67 } right_derive: true }"] [index=88] [term=6] [peer_id=3] [region_id=2]
   > [2024/07/16 15:38:43.968 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF5B00000000000000F8"] [region="id: 2 start_key: 7480000000000000FF5400000000000000F8 region_epoch { conf_ver: 1 version: 32 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/07/16 15:38:43.974 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/16 15:38:43.974 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=2]
   > [2024/07/16 15:38:43.974 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/07/16 15:38:43.974 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(61)] [region_id=2] [store_id=Some(1)]
   > [2024/07/16 15:38:43.974 +00:00] [INFO] [split_region.go:156] ["batch split regions complete"] ["batch region ID"=2] ["first at"=74800000000000005b] ["first new region left"="{Id:66 StartKey:7480000000000000ff5400000000000000f8 EndKey:7480000000000000ff5b00000000000000f8 RegionEpoch:{ConfVer:1 Version:33} Peers:[id:67 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/16 15:38:43.974 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 66 start_key: 7480000000000000FF5400000000000000F8 end_key: 7480000000000000FF5B00000000000000F8 region_epoch { conf_ver: 1 version: 33 } peers { id: 67 store_id: 1 }"] [region_id=66]
   > [2024/07/16 15:38:43.974 +00:00] [INFO] [split_region.go:205] ["split regions complete"] ["region count"=1] ["region IDs"="[66]"]
   > [2024/07/16 15:38:43.974 +00:00] [INFO] [split_region.go:59] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=74800000000000005c]
   > [2024/07/16 15:38:43.974 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF5B00000000000000F8 region_epoch { conf_ver: 1 version: 33 } peers { id: 3 store_id: 1 }"]
   > [2024/07/16 15:38:43.974 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=67] [region_id=66]
   > [2024/07/16 15:38:43.974 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF5400000000000000F8} -> {7480000000000000FF5B00000000000000F8}, EndKey:{}"] [old-version=32] [new-version=33]
   > [2024/07/16 15:38:43.974 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 2 start_key: 7480000000000000FF5B00000000000000F8 region_epoch { conf_ver: 1 version: 33 } peers { id: 3 store_id: 1 } }"]
   > [2024/07/16 15:38:43.974 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=2] [origin="id:66 start_key:\"7480000000000000FF5400000000000000F8\" end_key:\"7480000000000000FF5B00000000000000F8\" region_epoch:<conf_ver:1 version:33 > peers:<id:67 store_id:1 >"] [total=1]
   > [2024/07/16 15:38:43.974 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 2 start_key: 7480000000000000FF5B00000000000000F8 region_epoch { conf_ver: 1 version: 33 } peers { id: 3 store_id: 1 }"]
   > [2024/07/16 15:38:43.974 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {67} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=67] [region_id=66]
   > [2024/07/16 15:38:43.975 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=67] [region_id=66]
   > [2024/07/16 15:38:43.975 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {67} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=67] [region_id=66]
   > [2024/07/16 15:38:43.975 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 67."] [id=67] [raft_id=67] [region_id=66]
   > [2024/07/16 15:38:43.975 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=67] [region_id=66]
   > [2024/07/16 15:38:43.975 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=67] [region_id=66]
   > [2024/07/16 15:38:43.975 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=67] [region_id=66]
   > [2024/07/16 15:38:43.975 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=67] [region_id=66]
   > [2024/07/16 15:38:43.975 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803842] [region_id=66]
   > [2024/07/16 15:38:43.975 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=88] [observe_id=ObserveId(63)] [region=2]
   > [2024/07/16 15:38:43.975 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:46926] [split_keys="key 7480000000000000FF5C00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/16 15:38:43.976 +00:00] [INFO] [peer.rs:5566] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 32"] [prev_epoch="conf_ver: 1 version: 33"] [peer_id=3] [region_id=2]
   > [2024/07/16 15:38:43.976 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=66]
   > [2024/07/16 15:38:43.977 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:46940] [split_keys="key 7480000000000000FF5C00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/16 15:38:43.978 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=68] [peer-ids="[69]"]
   > [2024/07/16 15:38:43.978 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF5B00000000000000F8 region_epoch { conf_ver: 1 version: 33 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 68 new_peer_ids: 69]"] [region_id=2]
   > [2024/07/16 15:38:43.980 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 66 start_key: 7480000000000000FF5400000000000000F8 end_key: 7480000000000000FF5B00000000000000F8 region_epoch { conf_ver: 1 version: 33 } peers { id: 67 store_id: 1 }"]
   > [2024/07/16 15:38:43.980 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(64)] [region=66]
   > [2024/07/16 15:38:43.990 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF5C00000000000000F8 new_region_id: 68 new_peer_ids: 69 } right_derive: true }"] [index=90] [term=6] [peer_id=3] [region_id=2]
   > [2024/07/16 15:38:43.990 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF5C00000000000000F8"] [region="id: 2 start_key: 7480000000000000FF5B00000000000000F8 region_epoch { conf_ver: 1 version: 33 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/07/16 15:38:43.995 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/16 15:38:43.995 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=2]
   > [2024/07/16 15:38:43.995 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/07/16 15:38:43.995 +00:00] [INFO] [split_region.go:156] ["batch split regions complete"] ["batch region ID"=2] ["first at"=74800000000000005c] ["first new region left"="{Id:68 StartKey:7480000000000000ff5b00000000000000f8 EndKey:7480000000000000ff5c00000000000000f8 RegionEpoch:{ConfVer:1 Version:34} Peers:[id:69 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/16 15:38:43.996 +00:00] [INFO] [split_region.go:205] ["split regions complete"] ["region count"=1] ["region IDs"="[68]"]
   > [2024/07/16 15:38:43.995 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(63)] [region_id=2] [store_id=Some(1)]
   > [2024/07/16 15:38:43.996 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF5C00000000000000F8 region_epoch { conf_ver: 1 version: 34 } peers { id: 3 store_id: 1 }"]
   > [2024/07/16 15:38:43.996 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF5B00000000000000F8} -> {7480000000000000FF5C00000000000000F8}, EndKey:{}"] [old-version=33] [new-version=34]
   > [2024/07/16 15:38:43.996 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 68 start_key: 7480000000000000FF5B00000000000000F8 end_key: 7480000000000000FF5C00000000000000F8 region_epoch { conf_ver: 1 version: 34 } peers { id: 69 store_id: 1 }"] [region_id=68]
   > [2024/07/16 15:38:43.996 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=2] [origin="id:68 start_key:\"7480000000000000FF5B00000000000000F8\" end_key:\"7480000000000000FF5C00000000000000F8\" region_epoch:<conf_ver:1 version:34 > peers:<id:69 store_id:1 >"] [total=1]
   > [2024/07/16 15:38:43.996 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=69] [region_id=68]
   > [2024/07/16 15:38:43.996 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 2 start_key: 7480000000000000FF5C00000000000000F8 region_epoch { conf_ver: 1 version: 34 } peers { id: 3 store_id: 1 } }"]
   > [2024/07/16 15:38:43.996 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 2 start_key: 7480000000000000FF5C00000000000000F8 region_epoch { conf_ver: 1 version: 34 } peers { id: 3 store_id: 1 }"]
   > [2024/07/16 15:38:43.996 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {69} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=69] [region_id=68]
   > [2024/07/16 15:38:43.996 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=69] [region_id=68]
   > [2024/07/16 15:38:43.996 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {69} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=69] [region_id=68]
   > [2024/07/16 15:38:43.996 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 69."] [id=69] [raft_id=69] [region_id=68]
   > [2024/07/16 15:38:43.996 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=69] [region_id=68]
   > [2024/07/16 15:38:43.996 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=69] [region_id=68]
   > [2024/07/16 15:38:43.996 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=69] [region_id=68]
   > [2024/07/16 15:38:43.996 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=69] [region_id=68]
   > [2024/07/16 15:38:43.996 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803844] [region_id=68]
   > [2024/07/16 15:38:43.997 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=90] [observe_id=ObserveId(65)] [region=2]
   > [2024/07/16 15:38:43.997 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=68]
   > [2024/07/16 15:38:44.001 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 68 start_key: 7480000000000000FF5B00000000000000F8 end_key: 7480000000000000FF5C00000000000000F8 region_epoch { conf_ver: 1 version: 34 } peers { id: 69 store_id: 1 }"]
   > [2024/07/16 15:38:44.001 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(66)] [region=68]
   > [2024/07/16 15:38:51.158 +00:00] [INFO] [store_config.go:201] ["sync the store config successful"] [store-address=127.0.0.1:20180] [store-config="{\n  \"coprocessor\": {\n    \"region-max-size\": \"144MiB\",\n    \"region-split-size\": \"96MiB\",\n    \"region-max-keys\": 1440000,\n    \"region-split-keys\": 960000,\n    \"enable-region-bucket\": false,\n    \"region-bucket-size\": \"96MiB\"\n  }\n}"]
