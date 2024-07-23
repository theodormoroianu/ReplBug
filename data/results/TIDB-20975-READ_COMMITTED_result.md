# Bug ID TIDB-20975-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/20975
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              Unexpected "Information schema is changed" when commits


## Details
 * Database: tidb-fa6baa9f.tikv
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
     - Instruction:  begin pessimistic;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  update t1 set a=a;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 0 / 0
 * Instruction #3:
     - Instruction:  create table t2(a int);
     - Transaction: conn_1
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 0 / 0
 * Instruction #4:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: ERROR: 8028 (HY000): Information schema is changed during the execution of the statement(for example, table definition may be updated by other DDL ran in parallel). If you see this error often, try increasing `tidb_max_delta_schema_count`. [try again later]
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0

 * Container logs:
   > [2024/07/23 15:32:07.145 +00:00] [INFO] [session.go:2271] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=49] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.19]
   > [2024/07/23 15:32:07.154 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:74, Type:drop schema, State:none, SchemaState:none, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:07.139 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/23 15:32:07.154 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:74, Type:drop schema, State:none, SchemaState:none, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:07.139 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/23 15:32:07.157 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:74, Type:drop schema, State:none, SchemaState:none, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:07.139 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:07.171 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=49] [neededSchemaVersion=50] ["start time"=670.763µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 15:32:07.221 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=50] ["take time"=54.165428ms] [job="ID:74, Type:drop schema, State:running, SchemaState:write only, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:07.139 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:07.222 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:74, Type:drop schema, State:running, SchemaState:write only, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:07.139 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:07.235 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=50] [neededSchemaVersion=51] ["start time"=529.333µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 15:32:07.285 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=51] ["take time"=53.613397ms] [job="ID:74, Type:drop schema, State:running, SchemaState:delete only, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:07.139 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:07.287 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:74, Type:drop schema, State:running, SchemaState:delete only, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:07.139 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:07.306 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=51] [neededSchemaVersion=52] ["start time"=808.421µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 15:32:07.355 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=52] ["take time"=54.353163ms] [job="ID:74, Type:drop schema, State:done, SchemaState:none, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:07.139 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:07.358 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=74] [jobType="drop schema"]
   > [2024/07/23 15:32:07.359 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:74, Type:drop schema, State:synced, SchemaState:none, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:07.139 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:07.370 +00:00] [INFO] [ddl.go:517] ["[ddl] DDL job is finished"] [jobID=74]
   > [2024/07/23 15:32:07.370 +00:00] [INFO] [domain.go:646] ["performing DDL change, must reload"]
   > [2024/07/23 15:32:07.372 +00:00] [INFO] [session.go:2271] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=52] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.19]
   > [2024/07/23 15:32:07.389 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:76, Type:create schema, State:none, SchemaState:none, SchemaID:75, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 15:32:07.338 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/23 15:32:07.389 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:76, Type:create schema, State:none, SchemaState:none, SchemaID:75, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 15:32:07.338 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/23 15:32:07.393 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:76, Type:create schema, State:none, SchemaState:none, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:07.338 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:07.410 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=52] [neededSchemaVersion=53] ["start time"=1.443215ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 15:32:07.459 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=53] ["take time"=54.443819ms] [job="ID:76, Type:create schema, State:done, SchemaState:public, SchemaID:75, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 15:32:07.338 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:07.462 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:76, Type:create schema, State:synced, SchemaState:public, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:07.338 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:07.472 +00:00] [INFO] [ddl.go:517] ["[ddl] DDL job is finished"] [jobID=76]
   > [2024/07/23 15:32:07.472 +00:00] [INFO] [domain.go:646] ["performing DDL change, must reload"]
   > [2024/07/23 15:32:07.476 +00:00] [INFO] [session.go:2271] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=53] [cur_db=testdb] [sql="create table t1(a int);"] [user=root@10.88.0.19]
   > [2024/07/23 15:32:07.495 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:78, Type:create table, State:none, SchemaState:none, SchemaID:75, TableID:77, RowCount:0, ArgLen:1, start time: 2024-07-23 15:32:07.439 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/23 15:32:07.495 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:78, Type:create table, State:none, SchemaState:none, SchemaID:75, TableID:77, RowCount:0, ArgLen:1, start time: 2024-07-23 15:32:07.439 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t1(a int);"]
   > [2024/07/23 15:32:07.499 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:78, Type:create table, State:none, SchemaState:none, SchemaID:75, TableID:77, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:07.439 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:07.519 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=53] [neededSchemaVersion=54] ["start time"=2.240812ms] [phyTblIDs="[77]"] [actionTypes="[8]"]
   > [2024/07/23 15:32:07.567 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=54] ["take time"=54.190223ms] [job="ID:78, Type:create table, State:done, SchemaState:public, SchemaID:75, TableID:77, RowCount:0, ArgLen:1, start time: 2024-07-23 15:32:07.439 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:07.571 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:78, Type:create table, State:synced, SchemaState:public, SchemaID:75, TableID:77, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:07.439 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:07.581 +00:00] [INFO] [ddl.go:517] ["[ddl] DDL job is finished"] [jobID=78]
   > [2024/07/23 15:32:07.584 +00:00] [INFO] [domain.go:646] ["performing DDL change, must reload"]
   > [2024/07/23 15:32:07.584 +00:00] [INFO] [split_region.go:61] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=74800000000000004d]
   > [2024/07/23 15:32:07.586 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:32934] [split_keys="key 7480000000000000FF4D00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/23 15:32:07.587 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=60] [peer-ids="[61]"]
   > [2024/07/23 15:32:07.587 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF4700000000000000F8 region_epoch { conf_ver: 1 version: 29 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 60 new_peer_ids: 61]"] [region_id=2]
   > [2024/07/23 15:32:07.589 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF4D00000000000000F8 new_region_id: 60 new_peer_ids: 61 } right_derive: true }"] [index=73] [term=6] [peer_id=3] [region_id=2]
   > [2024/07/23 15:32:07.590 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF4D00000000000000F8"] [region="id: 2 start_key: 7480000000000000FF4700000000000000F8 region_epoch { conf_ver: 1 version: 29 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/07/23 15:32:07.592 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/23 15:32:07.592 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=2]
   > [2024/07/23 15:32:07.592 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(55)] [region_id=2] [store_id=Some(1)]
   > [2024/07/23 15:32:07.592 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF4D00000000000000F8 region_epoch { conf_ver: 1 version: 30 } peers { id: 3 store_id: 1 }"]
   > [2024/07/23 15:32:07.592 +00:00] [INFO] [split_region.go:158] ["batch split regions complete"] ["batch region ID"=2] ["first at"=74800000000000004d] ["first new region left"="{Id:60 StartKey:7480000000000000ff4700000000000000f8 EndKey:7480000000000000ff4d00000000000000f8 RegionEpoch:{ConfVer:1 Version:30} Peers:[id:61 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/23 15:32:07.592 +00:00] [INFO] [split_region.go:207] ["split regions complete"] ["region count"=1] ["region IDs"="[60]"]
   > [2024/07/23 15:32:07.592 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/07/23 15:32:07.592 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 60 start_key: 7480000000000000FF4700000000000000F8 end_key: 7480000000000000FF4D00000000000000F8 region_epoch { conf_ver: 1 version: 30 } peers { id: 61 store_id: 1 }"] [region_id=60]
   > [2024/07/23 15:32:07.592 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=61] [region_id=60]
   > [2024/07/23 15:32:07.592 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 2 start_key: 7480000000000000FF4D00000000000000F8 region_epoch { conf_ver: 1 version: 30 } peers { id: 3 store_id: 1 } }"]
   > [2024/07/23 15:32:07.592 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 2 start_key: 7480000000000000FF4D00000000000000F8 region_epoch { conf_ver: 1 version: 30 } peers { id: 3 store_id: 1 }"]
   > [2024/07/23 15:32:07.592 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF4700000000000000F8} -> {7480000000000000FF4D00000000000000F8}, EndKey:{}"] [old-version=29] [new-version=30]
   > [2024/07/23 15:32:07.592 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {61} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=61] [region_id=60]
   > [2024/07/23 15:32:07.592 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=2] [origin="id:60 start_key:\"7480000000000000FF4700000000000000F8\" end_key:\"7480000000000000FF4D00000000000000F8\" region_epoch:<conf_ver:1 version:30 > peers:<id:61 store_id:1 >"] [total=1]
   > [2024/07/23 15:32:07.593 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=61] [region_id=60]
   > [2024/07/23 15:32:07.593 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {61} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=61] [region_id=60]
   > [2024/07/23 15:32:07.593 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 61."] [id=61] [raft_id=61] [region_id=60]
   > [2024/07/23 15:32:07.593 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=61] [region_id=60]
   > [2024/07/23 15:32:07.593 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=61] [region_id=60]
   > [2024/07/23 15:32:07.593 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=61] [region_id=60]
   > [2024/07/23 15:32:07.593 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=61] [region_id=60]
   > [2024/07/23 15:32:07.593 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803836] [region_id=60]
   > [2024/07/23 15:32:07.593 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=60]
   > [2024/07/23 15:32:07.594 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 60 start_key: 7480000000000000FF4700000000000000F8 end_key: 7480000000000000FF4D00000000000000F8 region_epoch { conf_ver: 1 version: 30 } peers { id: 61 store_id: 1 }"]
   > [2024/07/23 15:32:07.594 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=73] [observe_id=ObserveId(57)] [region=2]
   > [2024/07/23 15:32:07.595 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(58)] [region=60]
   > [2024/07/23 15:32:07.601 +00:00] [INFO] [scheduler.rs:640] ["get snapshot failed"] [err="Error(Request(message: \"EpochNotMatch current epoch of region 2 is conf_ver: 1 version: 30, but you sent conf_ver: 1 version: 29\" epoch_not_match { current_regions { id: 2 start_key: 7480000000000000FF4D00000000000000F8 region_epoch { conf_ver: 1 version: 30 } peers { id: 3 store_id: 1 } } current_regions { id: 60 start_key: 7480000000000000FF4700000000000000F8 end_key: 7480000000000000FF4D00000000000000F8 region_epoch { conf_ver: 1 version: 30 } peers { id: 61 store_id: 1 } } }))"] [cid=482]
   > [2024/07/23 15:32:08.645 +00:00] [INFO] [set.go:216] ["set global var"] [conn=12] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/07/23 15:32:08.655 +00:00] [INFO] [set.go:216] ["set global var"] [conn=12] [name=transaction_isolation] [val=READ-COMMITTED]
   > [2024/07/23 15:32:09.537 +00:00] [INFO] [session.go:2271] ["CRUCIAL OPERATION"] [conn=13] [schemaVersion=54] [cur_db=testdb] [sql=" create table t2(a int);"] [user=root@10.88.0.19]
   > [2024/07/23 15:32:09.560 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:80, Type:create table, State:none, SchemaState:none, SchemaID:75, TableID:79, RowCount:0, ArgLen:1, start time: 2024-07-23 15:32:09.539 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/23 15:32:09.560 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:80, Type:create table, State:none, SchemaState:none, SchemaID:75, TableID:79, RowCount:0, ArgLen:1, start time: 2024-07-23 15:32:09.539 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query=" create table t2(a int);"]
   > [2024/07/23 15:32:09.563 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:80, Type:create table, State:none, SchemaState:none, SchemaID:75, TableID:79, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:09.539 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:09.581 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=54] [neededSchemaVersion=55] ["start time"=1.94538ms] [phyTblIDs="[79]"] [actionTypes="[8]"]
   > [2024/07/23 15:32:09.629 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=55] ["take time"=54.572398ms] [job="ID:80, Type:create table, State:done, SchemaState:public, SchemaID:75, TableID:79, RowCount:0, ArgLen:1, start time: 2024-07-23 15:32:09.539 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:09.633 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:80, Type:create table, State:synced, SchemaState:public, SchemaID:75, TableID:79, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:09.539 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:09.647 +00:00] [INFO] [ddl.go:517] ["[ddl] DDL job is finished"] [jobID=80]
   > [2024/07/23 15:32:09.649 +00:00] [INFO] [domain.go:646] ["performing DDL change, must reload"]
   > [2024/07/23 15:32:09.649 +00:00] [INFO] [split_region.go:61] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=74800000000000004f]
   > [2024/07/23 15:32:09.650 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:32906] [split_keys="key 7480000000000000FF4F00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/23 15:32:09.650 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=62] [peer-ids="[63]"]
   > [2024/07/23 15:32:09.650 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF4D00000000000000F8 region_epoch { conf_ver: 1 version: 30 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 62 new_peer_ids: 63]"] [region_id=2]
   > [2024/07/23 15:32:09.652 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF4F00000000000000F8 new_region_id: 62 new_peer_ids: 63 } right_derive: true }"] [index=76] [term=6] [peer_id=3] [region_id=2]
   > [2024/07/23 15:32:09.652 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF4F00000000000000F8"] [region="id: 2 start_key: 7480000000000000FF4D00000000000000F8 region_epoch { conf_ver: 1 version: 30 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/07/23 15:32:09.654 +00:00] [INFO] [peer.rs:3840] ["moving 1 locks to new regions"] [region_id=2]
   > [2024/07/23 15:32:09.654 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/23 15:32:09.654 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(57)] [region_id=2] [store_id=Some(1)]
   > [2024/07/23 15:32:09.654 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF4F00000000000000F8 region_epoch { conf_ver: 1 version: 31 } peers { id: 3 store_id: 1 }"]
   > [2024/07/23 15:32:09.654 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/07/23 15:32:09.654 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 62 start_key: 7480000000000000FF4D00000000000000F8 end_key: 7480000000000000FF4F00000000000000F8 region_epoch { conf_ver: 1 version: 31 } peers { id: 63 store_id: 1 }"] [region_id=62]
   > [2024/07/23 15:32:09.654 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=63] [region_id=62]
   > [2024/07/23 15:32:09.654 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 2 start_key: 7480000000000000FF4F00000000000000F8 region_epoch { conf_ver: 1 version: 31 } peers { id: 3 store_id: 1 } }"]
   > [2024/07/23 15:32:09.654 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 2 start_key: 7480000000000000FF4F00000000000000F8 region_epoch { conf_ver: 1 version: 31 } peers { id: 3 store_id: 1 }"]
   > [2024/07/23 15:32:09.654 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {63} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=63] [region_id=62]
   > [2024/07/23 15:32:09.654 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=63] [region_id=62]
   > [2024/07/23 15:32:09.654 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {63} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=63] [region_id=62]
   > [2024/07/23 15:32:09.654 +00:00] [INFO] [split_region.go:158] ["batch split regions complete"] ["batch region ID"=2] ["first at"=74800000000000004f] ["first new region left"="{Id:62 StartKey:7480000000000000ff4d00000000000000f8 EndKey:7480000000000000ff4f00000000000000f8 RegionEpoch:{ConfVer:1 Version:31} Peers:[id:63 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/23 15:32:09.655 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 63."] [id=63] [raft_id=63] [region_id=62]
   > [2024/07/23 15:32:09.655 +00:00] [INFO] [split_region.go:207] ["split regions complete"] ["region count"=1] ["region IDs"="[62]"]
   > [2024/07/23 15:32:09.655 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=63] [region_id=62]
   > [2024/07/23 15:32:09.655 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=63] [region_id=62]
   > [2024/07/23 15:32:09.655 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=63] [region_id=62]
   > [2024/07/23 15:32:09.655 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=63] [region_id=62]
   > [2024/07/23 15:32:09.655 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803838] [region_id=62]
   > [2024/07/23 15:32:09.655 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF4D00000000000000F8} -> {7480000000000000FF4F00000000000000F8}, EndKey:{}"] [old-version=30] [new-version=31]
   > [2024/07/23 15:32:09.655 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=2] [origin="id:62 start_key:\"7480000000000000FF4D00000000000000F8\" end_key:\"7480000000000000FF4F00000000000000F8\" region_epoch:<conf_ver:1 version:31 > peers:<id:63 store_id:1 >"] [total=1]
   > [2024/07/23 15:32:09.655 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=62]
   > [2024/07/23 15:32:09.657 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=76] [observe_id=ObserveId(59)] [region=2]
   > [2024/07/23 15:32:09.657 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 62 start_key: 7480000000000000FF4D00000000000000F8 end_key: 7480000000000000FF4F00000000000000F8 region_epoch { conf_ver: 1 version: 31 } peers { id: 63 store_id: 1 }"]
   > [2024/07/23 15:32:09.657 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(60)] [region=62]
   > [2024/07/23 15:32:09.829 +00:00] [INFO] [scheduler.rs:640] ["get snapshot failed"] [err="Error(Request(message: \"EpochNotMatch current epoch of region 2 is conf_ver: 1 version: 31, but you sent conf_ver: 1 version: 30\" epoch_not_match { current_regions { id: 2 start_key: 7480000000000000FF4F00000000000000F8 region_epoch { conf_ver: 1 version: 31 } peers { id: 3 store_id: 1 } } current_regions { id: 62 start_key: 7480000000000000FF4D00000000000000F8 end_key: 7480000000000000FF4F00000000000000F8 region_epoch { conf_ver: 1 version: 31 } peers { id: 63 store_id: 1 } } }))"] [cid=506]
   > [2024/07/23 15:32:09.835 +00:00] [INFO] [schema_validator.go:232] ["the related physical table ID is empty"] [schemaVer=54] [latestSchemaVer=55]
   > [2024/07/23 15:32:09.835 +00:00] [WARN] [session.go:490] ["can not retry txn"] [conn=12] [label=general] [error="[domain:8028]Information schema is changed during the execution of the statement(for example, table definition may be updated by other DDL ran in parallel). If you see this error often, try increasing `tidb_max_delta_schema_count`. [try again later]"] [IsBatchInsert=false] [IsPessimistic=true] [InRestrictedSQL=false] [tidb_retry_limit=10] [tidb_disable_txn_auto_retry=true]
   > [2024/07/23 15:32:09.835 +00:00] [WARN] [session.go:506] ["commit failed"] [conn=12] ["finished txn"="Txn{state=invalid}"] [error="[domain:8028]Information schema is changed during the execution of the statement(for example, table definition may be updated by other DDL ran in parallel). If you see this error often, try increasing `tidb_max_delta_schema_count`. [try again later]"]
   > [2024/07/23 15:32:09.835 +00:00] [WARN] [session.go:1175] ["run statement failed"] [conn=12] [schemaVersion=54] [error="previous statement:  update t1 set a=a;: [domain:8028]Information schema is changed during the execution of the statement(for example, table definition may be updated by other DDL ran in parallel). If you see this error often, try increasing `tidb_max_delta_schema_count`. [try again later]"] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 12,\n  \"status\": 2,\n  \"strictMode\": true,\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"10.88.0.19\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/07/23 15:32:09.835 +00:00] [INFO] [conn.go:793] ["command dispatched failed"] [conn=12] [connInfo="id:12, addr:10.88.0.19:52060 status:10, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:0, autocommit:1"] [sql=" commit;"] [txn_mode=PESSIMISTIC] [err="[domain:8028]Information schema is changed during the execution of the statement(for example, table definition may be updated by other DDL ran in parallel). If you see this error often, try increasing `tidb_max_delta_schema_count`. [try again later]\ngithub.com/pingcap/errors.AddStack\n\t/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.20200902104258-eba4f1d8f6de/errors.go:174\ngithub.com/pingcap/errors.Trace\n\t/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.20200902104258-eba4f1d8f6de/juju_adaptor.go:15\ngithub.com/pingcap/tidb/store/tikv.(*twoPhaseCommitter).checkSchemaValid\n\t/go/src/github.com/pingcap/tidb/store/tikv/2pc.go:1037\ngithub.com/pingcap/tidb/store/tikv.(*twoPhaseCommitter).execute\n\t/go/src/github.com/pingcap/tidb/store/tikv/2pc.go:831\ngithub.com/pingcap/tidb/store/tikv.(*tikvTxn).Commit\n\t/go/src/github.com/pingcap/tidb/store/tikv/txn.go:274\ngithub.com/pingcap/tidb/session.(*TxnState).Commit\n\t/go/src/github.com/pingcap/tidb/session/txn.go:244\ngithub.com/pingcap/tidb/session.(*session).doCommit\n\t/go/src/github.com/pingcap/tidb/session/session.go:450\ngithub.com/pingcap/tidb/session.(*session).doCommitWithRetry\n\t/go/src/github.com/pingcap/tidb/session/session.go:470\ngithub.com/pingcap/tidb/session.(*session).CommitTxn\n\t/go/src/github.com/pingcap/tidb/session/session.go:529\ngithub.com/pingcap/tidb/session.autoCommitAfterStmt\n\t/go/src/github.com/pingcap/tidb/session/tidb.go:229\ngithub.com/pingcap/tidb/session.finishStmt\n\t/go/src/github.com/pingcap/tidb/session/tidb.go:195\ngithub.com/pingcap/tidb/session.runStmt\n\t/go/src/github.com/pingcap/tidb/session/session.go:1232\ngithub.com/pingcap/tidb/session.(*session).ExecuteStmt\n\t/go/src/github.com/pingcap/tidb/session/session.go:1172\ngithub.com/pingcap/tidb/server.(*TiDBContext).ExecuteStmt\n\t/go/src/github.com/pingcap/tidb/server/driver_tidb.go:198\ngithub.com/pingcap/tidb/server.(*clientConn).handleStmt\n\t/go/src/github.com/pingcap/tidb/server/conn.go:1505\ngithub.com/pingcap/tidb/server.(*clientConn).handleQuery\n\t/go/src/github.com/pingcap/tidb/server/conn.go:1397\ngithub.com/pingcap/tidb/server.(*clientConn).dispatch\n\t/go/src/github.com/pingcap/tidb/server/conn.go:984\ngithub.com/pingcap/tidb/server.(*clientConn).Run\n\t/go/src/github.com/pingcap/tidb/server/conn.go:776\ngithub.com/pingcap/tidb/server.(*Server).onConn\n\t/go/src/github.com/pingcap/tidb/server/server.go:421\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1594\nprevious statement:  update t1 set a=a;"]
   > [2024/07/23 15:32:09.837 +00:00] [INFO] [2pc.go:725] ["2PC clean up done"] [conn=12] [txnStartTS=451346098785878017]

### Scenario 1
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 0 / 0
 * Instruction #1:
     - Instruction:  update t1 set a=a;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  create table t2(a int);
     - Transaction: conn_1
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 0 / 0

 * Container logs:
   > [2024/07/23 15:32:12.023 +00:00] [INFO] [session.go:2271] ["CRUCIAL OPERATION"] [conn=15] [schemaVersion=63] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.19]
   > [2024/07/23 15:32:12.038 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:87, Type:drop schema, State:none, SchemaState:none, SchemaID:82, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:11.989 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/23 15:32:12.038 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:87, Type:drop schema, State:none, SchemaState:none, SchemaID:82, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:11.989 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/23 15:32:12.041 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:87, Type:drop schema, State:none, SchemaState:none, SchemaID:82, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:11.989 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:12.056 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=63] [neededSchemaVersion=64] ["start time"=650.299µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 15:32:12.106 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=64] ["take time"=55.08413ms] [job="ID:87, Type:drop schema, State:running, SchemaState:write only, SchemaID:82, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:11.989 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:12.109 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:87, Type:drop schema, State:running, SchemaState:write only, SchemaID:82, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:11.989 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:12.125 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=64] [neededSchemaVersion=65] ["start time"=730.128µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 15:32:12.175 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=65] ["take time"=54.15132ms] [job="ID:87, Type:drop schema, State:running, SchemaState:delete only, SchemaID:82, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:11.989 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:12.177 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:87, Type:drop schema, State:running, SchemaState:delete only, SchemaID:82, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:11.989 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:12.196 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=65] [neededSchemaVersion=66] ["start time"=645.689µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 15:32:12.245 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=66] ["take time"=54.285277ms] [job="ID:87, Type:drop schema, State:done, SchemaState:none, SchemaID:82, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:11.989 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:12.247 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=87] [jobType="drop schema"]
   > [2024/07/23 15:32:12.249 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:87, Type:drop schema, State:synced, SchemaState:none, SchemaID:82, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:11.989 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:12.258 +00:00] [INFO] [ddl.go:517] ["[ddl] DDL job is finished"] [jobID=87]
   > [2024/07/23 15:32:12.258 +00:00] [INFO] [domain.go:646] ["performing DDL change, must reload"]
   > [2024/07/23 15:32:12.260 +00:00] [INFO] [session.go:2271] ["CRUCIAL OPERATION"] [conn=15] [schemaVersion=66] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.19]
   > [2024/07/23 15:32:12.277 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:89, Type:create schema, State:none, SchemaState:none, SchemaID:88, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 15:32:12.239 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/23 15:32:12.277 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:89, Type:create schema, State:none, SchemaState:none, SchemaID:88, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 15:32:12.239 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/23 15:32:12.281 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:89, Type:create schema, State:none, SchemaState:none, SchemaID:88, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:12.239 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:12.297 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=66] [neededSchemaVersion=67] ["start time"=1.377284ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 15:32:12.346 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=67] ["take time"=54.492778ms] [job="ID:89, Type:create schema, State:done, SchemaState:public, SchemaID:88, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 15:32:12.239 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:12.350 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:89, Type:create schema, State:synced, SchemaState:public, SchemaID:88, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:12.239 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:12.360 +00:00] [INFO] [ddl.go:517] ["[ddl] DDL job is finished"] [jobID=89]
   > [2024/07/23 15:32:12.360 +00:00] [INFO] [domain.go:646] ["performing DDL change, must reload"]
   > [2024/07/23 15:32:12.363 +00:00] [INFO] [session.go:2271] ["CRUCIAL OPERATION"] [conn=15] [schemaVersion=67] [cur_db=testdb] [sql="create table t1(a int);"] [user=root@10.88.0.19]
   > [2024/07/23 15:32:12.378 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:91, Type:create table, State:none, SchemaState:none, SchemaID:88, TableID:90, RowCount:0, ArgLen:1, start time: 2024-07-23 15:32:12.339 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/23 15:32:12.378 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:91, Type:create table, State:none, SchemaState:none, SchemaID:88, TableID:90, RowCount:0, ArgLen:1, start time: 2024-07-23 15:32:12.339 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t1(a int);"]
   > [2024/07/23 15:32:12.381 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:91, Type:create table, State:none, SchemaState:none, SchemaID:88, TableID:90, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:12.339 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:12.402 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=67] [neededSchemaVersion=68] ["start time"=1.896281ms] [phyTblIDs="[90]"] [actionTypes="[8]"]
   > [2024/07/23 15:32:12.450 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=68] ["take time"=55.297149ms] [job="ID:91, Type:create table, State:done, SchemaState:public, SchemaID:88, TableID:90, RowCount:0, ArgLen:1, start time: 2024-07-23 15:32:12.339 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:12.454 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:91, Type:create table, State:synced, SchemaState:public, SchemaID:88, TableID:90, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:12.339 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:12.465 +00:00] [INFO] [ddl.go:517] ["[ddl] DDL job is finished"] [jobID=91]
   > [2024/07/23 15:32:12.467 +00:00] [INFO] [domain.go:646] ["performing DDL change, must reload"]
   > [2024/07/23 15:32:12.467 +00:00] [INFO] [split_region.go:61] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=74800000000000005a]
   > [2024/07/23 15:32:12.468 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:32928] [split_keys="key 7480000000000000FF5A00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/23 15:32:12.468 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=66] [peer-ids="[67]"]
   > [2024/07/23 15:32:12.468 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF5400000000000000F8 region_epoch { conf_ver: 1 version: 32 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 66 new_peer_ids: 67]"] [region_id=2]
   > [2024/07/23 15:32:12.471 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF5A00000000000000F8 new_region_id: 66 new_peer_ids: 67 } right_derive: true }"] [index=80] [term=6] [peer_id=3] [region_id=2]
   > [2024/07/23 15:32:12.471 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF5A00000000000000F8"] [region="id: 2 start_key: 7480000000000000FF5400000000000000F8 region_epoch { conf_ver: 1 version: 32 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/07/23 15:32:12.473 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/23 15:32:12.473 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=2]
   > [2024/07/23 15:32:12.473 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(61)] [region_id=2] [store_id=Some(1)]
   > [2024/07/23 15:32:12.473 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/07/23 15:32:12.474 +00:00] [INFO] [split_region.go:158] ["batch split regions complete"] ["batch region ID"=2] ["first at"=74800000000000005a] ["first new region left"="{Id:66 StartKey:7480000000000000ff5400000000000000f8 EndKey:7480000000000000ff5a00000000000000f8 RegionEpoch:{ConfVer:1 Version:33} Peers:[id:67 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/23 15:32:12.474 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF5A00000000000000F8 region_epoch { conf_ver: 1 version: 33 } peers { id: 3 store_id: 1 }"]
   > [2024/07/23 15:32:12.474 +00:00] [INFO] [split_region.go:207] ["split regions complete"] ["region count"=1] ["region IDs"="[66]"]
   > [2024/07/23 15:32:12.474 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF5400000000000000F8} -> {7480000000000000FF5A00000000000000F8}, EndKey:{}"] [old-version=32] [new-version=33]
   > [2024/07/23 15:32:12.474 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 66 start_key: 7480000000000000FF5400000000000000F8 end_key: 7480000000000000FF5A00000000000000F8 region_epoch { conf_ver: 1 version: 33 } peers { id: 67 store_id: 1 }"] [region_id=66]
   > [2024/07/23 15:32:12.474 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=67] [region_id=66]
   > [2024/07/23 15:32:12.474 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 2 start_key: 7480000000000000FF5A00000000000000F8 region_epoch { conf_ver: 1 version: 33 } peers { id: 3 store_id: 1 } }"]
   > [2024/07/23 15:32:12.474 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 2 start_key: 7480000000000000FF5A00000000000000F8 region_epoch { conf_ver: 1 version: 33 } peers { id: 3 store_id: 1 }"]
   > [2024/07/23 15:32:12.474 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {67} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=67] [region_id=66]
   > [2024/07/23 15:32:12.474 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=67] [region_id=66]
   > [2024/07/23 15:32:12.474 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=2] [origin="id:66 start_key:\"7480000000000000FF5400000000000000F8\" end_key:\"7480000000000000FF5A00000000000000F8\" region_epoch:<conf_ver:1 version:33 > peers:<id:67 store_id:1 >"] [total=1]
   > [2024/07/23 15:32:12.474 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {67} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=67] [region_id=66]
   > [2024/07/23 15:32:12.474 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 67."] [id=67] [raft_id=67] [region_id=66]
   > [2024/07/23 15:32:12.474 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=67] [region_id=66]
   > [2024/07/23 15:32:12.475 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=67] [region_id=66]
   > [2024/07/23 15:32:12.475 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=67] [region_id=66]
   > [2024/07/23 15:32:12.475 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=67] [region_id=66]
   > [2024/07/23 15:32:12.475 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803842] [region_id=66]
   > [2024/07/23 15:32:12.475 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=66]
   > [2024/07/23 15:32:12.478 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 66 start_key: 7480000000000000FF5400000000000000F8 end_key: 7480000000000000FF5A00000000000000F8 region_epoch { conf_ver: 1 version: 33 } peers { id: 67 store_id: 1 }"]
   > [2024/07/23 15:32:12.478 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=80] [observe_id=ObserveId(63)] [region=2]
   > [2024/07/23 15:32:12.478 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(64)] [region=66]
   > [2024/07/23 15:32:12.481 +00:00] [INFO] [scheduler.rs:640] ["get snapshot failed"] [err="Error(Request(message: \"EpochNotMatch current epoch of region 2 is conf_ver: 1 version: 33, but you sent conf_ver: 1 version: 32\" epoch_not_match { current_regions { id: 2 start_key: 7480000000000000FF5A00000000000000F8 region_epoch { conf_ver: 1 version: 33 } peers { id: 3 store_id: 1 } } current_regions { id: 66 start_key: 7480000000000000FF5400000000000000F8 end_key: 7480000000000000FF5A00000000000000F8 region_epoch { conf_ver: 1 version: 33 } peers { id: 67 store_id: 1 } } }))"] [cid=595]
   > [2024/07/23 15:32:13.514 +00:00] [INFO] [set.go:216] ["set global var"] [conn=16] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/07/23 15:32:13.516 +00:00] [INFO] [set.go:216] ["set global var"] [conn=16] [name=transaction_isolation] [val=READ-COMMITTED]
   > [2024/07/23 15:32:14.124 +00:00] [INFO] [session.go:2271] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=68] [cur_db=testdb] [sql=" create table t2(a int);"] [user=root@10.88.0.19]
   > [2024/07/23 15:32:14.150 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:93, Type:create table, State:none, SchemaState:none, SchemaID:88, TableID:92, RowCount:0, ArgLen:1, start time: 2024-07-23 15:32:14.139 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/23 15:32:14.150 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:93, Type:create table, State:none, SchemaState:none, SchemaID:88, TableID:92, RowCount:0, ArgLen:1, start time: 2024-07-23 15:32:14.139 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query=" create table t2(a int);"]
   > [2024/07/23 15:32:14.153 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:93, Type:create table, State:none, SchemaState:none, SchemaID:88, TableID:92, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:14.139 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:14.173 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=68] [neededSchemaVersion=69] ["start time"=1.728102ms] [phyTblIDs="[92]"] [actionTypes="[8]"]
   > [2024/07/23 15:32:14.222 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=69] ["take time"=54.142381ms] [job="ID:93, Type:create table, State:done, SchemaState:public, SchemaID:88, TableID:92, RowCount:0, ArgLen:1, start time: 2024-07-23 15:32:14.139 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:14.226 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:93, Type:create table, State:synced, SchemaState:public, SchemaID:88, TableID:92, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:14.139 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:14.237 +00:00] [INFO] [ddl.go:517] ["[ddl] DDL job is finished"] [jobID=93]
   > [2024/07/23 15:32:14.239 +00:00] [INFO] [domain.go:646] ["performing DDL change, must reload"]
   > [2024/07/23 15:32:14.239 +00:00] [INFO] [split_region.go:61] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=74800000000000005c]
   > [2024/07/23 15:32:14.240 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:32934] [split_keys="key 7480000000000000FF5C00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/23 15:32:14.240 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=68] [peer-ids="[69]"]
   > [2024/07/23 15:32:14.241 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF5A00000000000000F8 region_epoch { conf_ver: 1 version: 33 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 68 new_peer_ids: 69]"] [region_id=2]
   > [2024/07/23 15:32:14.243 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF5C00000000000000F8 new_region_id: 68 new_peer_ids: 69 } right_derive: true }"] [index=83] [term=6] [peer_id=3] [region_id=2]
   > [2024/07/23 15:32:14.244 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF5C00000000000000F8"] [region="id: 2 start_key: 7480000000000000FF5A00000000000000F8 region_epoch { conf_ver: 1 version: 33 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/07/23 15:32:14.246 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/23 15:32:14.246 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=2]
   > [2024/07/23 15:32:14.246 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/07/23 15:32:14.246 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(63)] [region_id=2] [store_id=Some(1)]
   > [2024/07/23 15:32:14.246 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF5C00000000000000F8 region_epoch { conf_ver: 1 version: 34 } peers { id: 3 store_id: 1 }"]
   > [2024/07/23 15:32:14.246 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 68 start_key: 7480000000000000FF5A00000000000000F8 end_key: 7480000000000000FF5C00000000000000F8 region_epoch { conf_ver: 1 version: 34 } peers { id: 69 store_id: 1 }"] [region_id=68]
   > [2024/07/23 15:32:14.246 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=69] [region_id=68]
   > [2024/07/23 15:32:14.246 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 2 start_key: 7480000000000000FF5C00000000000000F8 region_epoch { conf_ver: 1 version: 34 } peers { id: 3 store_id: 1 } }"]
   > [2024/07/23 15:32:14.246 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 2 start_key: 7480000000000000FF5C00000000000000F8 region_epoch { conf_ver: 1 version: 34 } peers { id: 3 store_id: 1 }"]
   > [2024/07/23 15:32:14.246 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {69} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=69] [region_id=68]
   > [2024/07/23 15:32:14.246 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=69] [region_id=68]
   > [2024/07/23 15:32:14.246 +00:00] [INFO] [split_region.go:158] ["batch split regions complete"] ["batch region ID"=2] ["first at"=74800000000000005c] ["first new region left"="{Id:68 StartKey:7480000000000000ff5a00000000000000f8 EndKey:7480000000000000ff5c00000000000000f8 RegionEpoch:{ConfVer:1 Version:34} Peers:[id:69 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/23 15:32:14.246 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {69} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=69] [region_id=68]
   > [2024/07/23 15:32:14.246 +00:00] [INFO] [split_region.go:207] ["split regions complete"] ["region count"=1] ["region IDs"="[68]"]
   > [2024/07/23 15:32:14.246 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 69."] [id=69] [raft_id=69] [region_id=68]
   > [2024/07/23 15:32:14.246 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=69] [region_id=68]
   > [2024/07/23 15:32:14.246 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=69] [region_id=68]
   > [2024/07/23 15:32:14.246 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF5A00000000000000F8} -> {7480000000000000FF5C00000000000000F8}, EndKey:{}"] [old-version=33] [new-version=34]
   > [2024/07/23 15:32:14.246 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=69] [region_id=68]
   > [2024/07/23 15:32:14.246 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=69] [region_id=68]
   > [2024/07/23 15:32:14.247 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803844] [region_id=68]
   > [2024/07/23 15:32:14.247 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=83] [observe_id=ObserveId(65)] [region=2]
   > [2024/07/23 15:32:14.246 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=2] [origin="id:68 start_key:\"7480000000000000FF5A00000000000000F8\" end_key:\"7480000000000000FF5C00000000000000F8\" region_epoch:<conf_ver:1 version:34 > peers:<id:69 store_id:1 >"] [total=1]
   > [2024/07/23 15:32:14.247 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=68]
   > [2024/07/23 15:32:14.248 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 68 start_key: 7480000000000000FF5A00000000000000F8 end_key: 7480000000000000FF5C00000000000000F8 region_epoch { conf_ver: 1 version: 34 } peers { id: 69 store_id: 1 }"]
   > [2024/07/23 15:32:14.249 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(66)] [region=68]
