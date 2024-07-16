# Bug ID TIDB-21218-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/21218
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              The second select should output the same table as the first one, but it doesn't.


## Details
 * Database: tidb-v4.0.0-beta.2.tikv
 * Number of scenarios: 1
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
     - Instruction:  begin pessimistic;
     - Transaction: conn_1
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 0 / 0
 * Instruction #3:
     - Instruction:  select * from t where id = 1 and v = 1 for update;
     - Transaction: conn_0
     - Output: [(1, 1, 1)]
     - Executed order: 3
     - Affected rows / Warnings: 1 / 0
 * Instruction #4:
     - Instruction:  insert into t values(1, 1, 2);
     - Transaction: conn_1
     - Output: ERROR: 1062 (23000): Duplicate entry '1-1' for key 'PRIMARY'
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #5:
     - Instruction:  update t set v = 2 where id = 1 and v = 1;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows / Warnings: 1 / 0
 * Instruction #6:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: None
     - Executed order: 5
     - Affected rows / Warnings: 0 / 0
 * Instruction #7:
     - Instruction:  commit;
     - Transaction: conn_1
     - Output: None
     - Executed order: 6
     - Affected rows / Warnings: 0 / 0
 * Instruction #8:
     - Instruction:  SELECT * FROM t;
     - Transaction: conn_2
     - Output: [(1, 2, 1)]
     - Executed order: 7
     - Affected rows / Warnings: 1 / 0

 * Container logs:
   > [2024/07/16 17:27:57.352 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=7]
   > [2024/07/16 17:27:57.356 +00:00] [INFO] [server.go:388] ["new connection"] [conn=8] [remoteAddr=10.88.0.94:58226]
   > [2024/07/16 17:27:57.358 +00:00] [INFO] [session.go:2210] ["CRUCIAL OPERATION"] [conn=8] [schemaVersion=32] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.94]
   > [2024/07/16 17:27:57.375 +00:00] [INFO] [ddl_worker.go:253] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:55, Type:drop schema, State:none, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 17:27:57.321 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/16 17:27:57.375 +00:00] [INFO] [ddl.go:500] ["[ddl] start DDL job"] [job="ID:55, Type:drop schema, State:none, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 17:27:57.321 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/16 17:27:57.379 +00:00] [INFO] [ddl_worker.go:568] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:55, Type:drop schema, State:none, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 17:27:57.321 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 17:27:57.402 +00:00] [INFO] [domain.go:126] ["diff load InfoSchema success"] [usedSchemaVersion=32] [neededSchemaVersion=33] ["start time"=511.662µs] [tblIDs="[]"]
   > [2024/07/16 17:27:57.461 +00:00] [INFO] [ddl_worker.go:759] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=33] ["take time"=65.655987ms] [job="ID:55, Type:drop schema, State:running, SchemaState:write only, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 17:27:57.321 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 17:27:57.463 +00:00] [INFO] [ddl_worker.go:568] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:55, Type:drop schema, State:running, SchemaState:write only, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 17:27:57.321 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 17:27:57.489 +00:00] [INFO] [domain.go:126] ["diff load InfoSchema success"] [usedSchemaVersion=33] [neededSchemaVersion=34] ["start time"=604.413µs] [tblIDs="[]"]
   > [2024/07/16 17:27:57.539 +00:00] [INFO] [ddl_worker.go:759] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=34] ["take time"=58.101453ms] [job="ID:55, Type:drop schema, State:running, SchemaState:delete only, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 17:27:57.321 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 17:27:57.541 +00:00] [INFO] [ddl_worker.go:568] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:55, Type:drop schema, State:running, SchemaState:delete only, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 17:27:57.321 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 17:27:57.577 +00:00] [INFO] [domain.go:126] ["diff load InfoSchema success"] [usedSchemaVersion=34] [neededSchemaVersion=35] ["start time"=470.526µs] [tblIDs="[]"]
   > [2024/07/16 17:27:57.627 +00:00] [INFO] [ddl_worker.go:759] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=35] ["take time"=66.09229ms] [job="ID:55, Type:drop schema, State:done, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 17:27:57.321 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 17:27:57.630 +00:00] [INFO] [delete_range.go:98] ["[ddl] add job into delete-range table"] [jobID=55] [jobType="drop schema"]
   > [2024/07/16 17:27:57.631 +00:00] [INFO] [ddl_worker.go:359] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:55, Type:drop schema, State:synced, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 17:27:57.321 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 17:27:57.648 +00:00] [INFO] [ddl.go:532] ["[ddl] DDL job is finished"] [jobID=55]
   > [2024/07/16 17:27:57.648 +00:00] [INFO] [domain.go:631] ["performing DDL change, must reload"]
   > [2024/07/16 17:27:57.650 +00:00] [INFO] [session.go:2210] ["CRUCIAL OPERATION"] [conn=8] [schemaVersion=35] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.94]
   > [2024/07/16 17:27:57.678 +00:00] [INFO] [ddl_worker.go:253] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:57, Type:create schema, State:none, SchemaState:none, SchemaID:56, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-16 17:27:57.622 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/16 17:27:57.678 +00:00] [INFO] [ddl.go:500] ["[ddl] start DDL job"] [job="ID:57, Type:create schema, State:none, SchemaState:none, SchemaID:56, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-16 17:27:57.622 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/16 17:27:57.681 +00:00] [INFO] [ddl_worker.go:568] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:57, Type:create schema, State:none, SchemaState:none, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 17:27:57.622 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 17:27:57.707 +00:00] [INFO] [domain.go:126] ["diff load InfoSchema success"] [usedSchemaVersion=35] [neededSchemaVersion=36] ["start time"=952.366µs] [tblIDs="[]"]
   > [2024/07/16 17:27:57.756 +00:00] [INFO] [ddl_worker.go:759] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=36] ["take time"=57.965471ms] [job="ID:57, Type:create schema, State:done, SchemaState:public, SchemaID:56, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-16 17:27:57.622 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 17:27:57.760 +00:00] [INFO] [ddl_worker.go:359] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:57, Type:create schema, State:synced, SchemaState:public, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 17:27:57.622 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 17:27:57.776 +00:00] [INFO] [ddl.go:532] ["[ddl] DDL job is finished"] [jobID=57]
   > [2024/07/16 17:27:57.776 +00:00] [INFO] [domain.go:631] ["performing DDL change, must reload"]
   > [2024/07/16 17:27:57.779 +00:00] [INFO] [session.go:2210] ["CRUCIAL OPERATION"] [conn=8] [schemaVersion=36] [cur_db=testdb] [sql="drop table if exists t;"] [user=root@10.88.0.94]
   > [2024/07/16 17:27:57.780 +00:00] [INFO] [session.go:2210] ["CRUCIAL OPERATION"] [conn=8] [schemaVersion=36] [cur_db=testdb] [sql="create table t(id int, v int, val int, primary key(id, v));"] [user=root@10.88.0.94]
   > [2024/07/16 17:27:57.816 +00:00] [INFO] [ddl_worker.go:253] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:59, Type:create table, State:none, SchemaState:none, SchemaID:56, TableID:58, RowCount:0, ArgLen:1, start time: 2024-07-16 17:27:57.772 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/16 17:27:57.816 +00:00] [INFO] [ddl.go:500] ["[ddl] start DDL job"] [job="ID:59, Type:create table, State:none, SchemaState:none, SchemaID:56, TableID:58, RowCount:0, ArgLen:1, start time: 2024-07-16 17:27:57.772 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t(id int, v int, val int, primary key(id, v));"]
   > [2024/07/16 17:27:57.820 +00:00] [INFO] [ddl_worker.go:568] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:59, Type:create table, State:none, SchemaState:none, SchemaID:56, TableID:58, RowCount:0, ArgLen:0, start time: 2024-07-16 17:27:57.772 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 17:27:57.854 +00:00] [INFO] [domain.go:126] ["diff load InfoSchema success"] [usedSchemaVersion=36] [neededSchemaVersion=37] ["start time"=2.550841ms] [tblIDs="[58]"]
   > [2024/07/16 17:27:57.902 +00:00] [INFO] [ddl_worker.go:759] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=37] ["take time"=60.914131ms] [job="ID:59, Type:create table, State:done, SchemaState:public, SchemaID:56, TableID:58, RowCount:0, ArgLen:1, start time: 2024-07-16 17:27:57.772 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 17:27:57.906 +00:00] [INFO] [ddl_worker.go:359] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:59, Type:create table, State:synced, SchemaState:public, SchemaID:56, TableID:58, RowCount:0, ArgLen:0, start time: 2024-07-16 17:27:57.772 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 17:27:57.925 +00:00] [INFO] [ddl.go:532] ["[ddl] DDL job is finished"] [jobID=59]
   > [2024/07/16 17:27:57.927 +00:00] [INFO] [domain.go:631] ["performing DDL change, must reload"]
   > [2024/07/16 17:27:57.927 +00:00] [INFO] [split_region.go:56] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=74800000000000003a]
   > [2024/07/16 17:27:57.928 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:58184] [split_keys="key 7480000000000000FF3A00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/16 17:27:57.928 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=48] [peer-ids="[49]"]
   > [2024/07/16 17:27:57.929 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF3400000000000000F8 region_epoch { conf_ver: 1 version: 23 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 48 new_peer_ids: 49]"] [region_id=2]
   > [2024/07/16 17:27:57.934 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF3A00000000000000F8 new_region_id: 48 new_peer_ids: 49 } right_derive: true }"] [index=63] [term=6] [peer_id=3] [region_id=2]
   > [2024/07/16 17:27:57.935 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF3A00000000000000F8"] [region="id: 2 start_key: 7480000000000000FF3400000000000000F8 region_epoch { conf_ver: 1 version: 23 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/07/16 17:27:57.944 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=2]
   > [2024/07/16 17:27:57.944 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/16 17:27:57.944 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/07/16 17:27:57.944 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(43)] [region_id=2] [store_id=Some(1)]
   > [2024/07/16 17:27:57.944 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 48 start_key: 7480000000000000FF3400000000000000F8 end_key: 7480000000000000FF3A00000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 49 store_id: 1 }"] [region_id=48]
   > [2024/07/16 17:27:57.944 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF3A00000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 3 store_id: 1 }"]
   > [2024/07/16 17:27:57.944 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=49] [region_id=48]
   > [2024/07/16 17:27:57.944 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF3400000000000000F8} -> {7480000000000000FF3A00000000000000F8}, EndKey:{}"] [old-version=23] [new-version=24]
   > [2024/07/16 17:27:57.944 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {49} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=49] [region_id=48]
   > [2024/07/16 17:27:57.945 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=49] [region_id=48]
   > [2024/07/16 17:27:57.945 +00:00] [INFO] [split_region.go:153] ["batch split regions complete"] ["batch region ID"=2] ["first at"=74800000000000003a] ["first new region left"="{Id:48 StartKey:7480000000000000ff3400000000000000f8 EndKey:7480000000000000ff3a00000000000000f8 RegionEpoch:{ConfVer:1 Version:24} Peers:[id:49 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/16 17:27:57.945 +00:00] [INFO] [split_region.go:205] ["split regions complete"] ["region count"=1] ["region IDs"="[48]"]
   > [2024/07/16 17:27:57.945 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {49} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=49] [region_id=48]
   > [2024/07/16 17:27:57.945 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=2] [origin="id:48 start_key:\"7480000000000000FF3400000000000000F8\" end_key:\"7480000000000000FF3A00000000000000F8\" region_epoch:<conf_ver:1 version:24 > peers:<id:49 store_id:1 >"] [total=1]
   > [2024/07/16 17:27:57.945 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 49."] [id=49] [raft_id=49] [region_id=48]
   > [2024/07/16 17:27:57.945 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 2 start_key: 7480000000000000FF3A00000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 3 store_id: 1 } }"]
   > [2024/07/16 17:27:57.945 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=49] [region_id=48]
   > [2024/07/16 17:27:57.945 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=49] [region_id=48]
   > [2024/07/16 17:27:57.945 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=49] [region_id=48]
   > [2024/07/16 17:27:57.945 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 2 start_key: 7480000000000000FF3A00000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 3 store_id: 1 }"]
   > [2024/07/16 17:27:57.945 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=49] [region_id=48]
   > [2024/07/16 17:27:57.945 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803824] [region_id=48]
   > [2024/07/16 17:27:57.946 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=48]
   > [2024/07/16 17:27:57.951 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 48 start_key: 7480000000000000FF3400000000000000F8 end_key: 7480000000000000FF3A00000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 49 store_id: 1 }"]
   > [2024/07/16 17:27:57.951 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=63] [observe_id=ObserveId(45)] [region=2]
   > [2024/07/16 17:27:57.951 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(46)] [region=48]
   > [2024/07/16 17:27:57.957 +00:00] [INFO] [scheduler.rs:640] ["get snapshot failed"] [err="Error(Request(message: \"EpochNotMatch current epoch of region 2 is conf_ver: 1 version: 24, but you sent conf_ver: 1 version: 23\" epoch_not_match { current_regions { id: 2 start_key: 7480000000000000FF3A00000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 3 store_id: 1 } } current_regions { id: 48 start_key: 7480000000000000FF3400000000000000F8 end_key: 7480000000000000FF3A00000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 49 store_id: 1 } } }))"] [cid=354]
   > [2024/07/16 17:27:57.973 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=8]
   > [2024/07/16 17:27:58.985 +00:00] [INFO] [server.go:388] ["new connection"] [conn=9] [remoteAddr=10.88.0.94:58238]
   > [2024/07/16 17:27:58.996 +00:00] [INFO] [set.go:207] ["set session var"] [conn=9] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/07/16 17:27:59.594 +00:00] [INFO] [server.go:388] ["new connection"] [conn=10] [remoteAddr=10.88.0.94:58244]
   > [2024/07/16 17:27:59.598 +00:00] [INFO] [set.go:207] ["set session var"] [conn=10] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/07/16 17:28:00.195 +00:00] [ERROR] [conn.go:730] ["command dispatched failed"] [conn=10] [connInfo="id:10, addr:10.88.0.94:58244 status:11, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:1, autocommit:1"] [sql=" insert into t values(1, 1, 2);"] [txn_mode=PESSIMISTIC] [err="[kv:1062]Duplicate entry '1-1' for key 'PRIMARY'"]
   > [2024/07/16 17:28:01.405 +00:00] [INFO] [server.go:388] ["new connection"] [conn=11] [remoteAddr=10.88.0.94:46748]
   > [2024/07/16 17:28:01.415 +00:00] [INFO] [set.go:207] ["set session var"] [conn=11] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/07/16 17:28:01.803 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=9]
   > [2024/07/16 17:28:01.803 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=10]
   > [2024/07/16 17:28:01.803 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=11]
