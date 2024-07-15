# Bug ID TIDB-17797-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/17797
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              The error message is not correct.


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
     - Instruction:  BEGIN PESSIMISTIC;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  BEGIN PESSIMISTIC;
     - Transaction: conn_1
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 0 / 0
 * Instruction #3:
     - Instruction:  UPDATE t1 SET t='new...' WHERE id = 1;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 1 / 0
 * Instruction #4:
     - Instruction:  UPDATE t1 SET t='newval' WHERE id = 1;
     - Transaction: conn_1
     - Output: ERROR: 1205 (HY000): Lock wait timeout exceeded; try restarting transaction
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0

 * Container logs:
   > [2024/07/15 12:51:08.381 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=6]
   > [2024/07/15 12:51:08.386 +00:00] [INFO] [server.go:388] ["new connection"] [conn=7] [remoteAddr=10.88.0.53:42078]
   > [2024/07/15 12:51:08.388 +00:00] [INFO] [session.go:2210] ["CRUCIAL OPERATION"] [conn=7] [schemaVersion=32] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.53]
   > [2024/07/15 12:51:08.410 +00:00] [INFO] [ddl_worker.go:253] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:55, Type:drop schema, State:none, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 12:51:08.366 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/15 12:51:08.411 +00:00] [INFO] [ddl.go:500] ["[ddl] start DDL job"] [job="ID:55, Type:drop schema, State:none, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 12:51:08.366 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/15 12:51:08.414 +00:00] [INFO] [ddl_worker.go:568] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:55, Type:drop schema, State:none, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 12:51:08.366 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 12:51:08.440 +00:00] [INFO] [domain.go:126] ["diff load InfoSchema success"] [usedSchemaVersion=32] [neededSchemaVersion=33] ["start time"=585.766µs] [tblIDs="[]"]
   > [2024/07/15 12:51:08.501 +00:00] [INFO] [ddl_worker.go:759] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=33] ["take time"=68.197207ms] [job="ID:55, Type:drop schema, State:running, SchemaState:write only, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 12:51:08.366 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 12:51:08.502 +00:00] [INFO] [ddl_worker.go:568] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:55, Type:drop schema, State:running, SchemaState:write only, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 12:51:08.366 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 12:51:08.530 +00:00] [INFO] [domain.go:126] ["diff load InfoSchema success"] [usedSchemaVersion=33] [neededSchemaVersion=34] ["start time"=676.282µs] [tblIDs="[]"]
   > [2024/07/15 12:51:08.580 +00:00] [INFO] [ddl_worker.go:759] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=34] ["take time"=60.932996ms] [job="ID:55, Type:drop schema, State:running, SchemaState:delete only, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 12:51:08.366 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 12:51:08.581 +00:00] [INFO] [ddl_worker.go:568] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:55, Type:drop schema, State:running, SchemaState:delete only, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 12:51:08.366 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 12:51:08.618 +00:00] [INFO] [domain.go:126] ["diff load InfoSchema success"] [usedSchemaVersion=34] [neededSchemaVersion=35] ["start time"=523.537µs] [tblIDs="[]"]
   > [2024/07/15 12:51:08.668 +00:00] [INFO] [ddl_worker.go:759] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=35] ["take time"=66.275989ms] [job="ID:55, Type:drop schema, State:done, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 12:51:08.366 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 12:51:08.670 +00:00] [INFO] [delete_range.go:98] ["[ddl] add job into delete-range table"] [jobID=55] [jobType="drop schema"]
   > [2024/07/15 12:51:08.671 +00:00] [INFO] [ddl_worker.go:359] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:55, Type:drop schema, State:synced, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 12:51:08.366 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 12:51:08.689 +00:00] [INFO] [ddl.go:532] ["[ddl] DDL job is finished"] [jobID=55]
   > [2024/07/15 12:51:08.689 +00:00] [INFO] [domain.go:631] ["performing DDL change, must reload"]
   > [2024/07/15 12:51:08.691 +00:00] [INFO] [session.go:2210] ["CRUCIAL OPERATION"] [conn=7] [schemaVersion=35] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.53]
   > [2024/07/15 12:51:08.726 +00:00] [INFO] [ddl_worker.go:253] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:57, Type:create schema, State:none, SchemaState:none, SchemaID:56, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-15 12:51:08.666 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/15 12:51:08.726 +00:00] [INFO] [ddl.go:500] ["[ddl] start DDL job"] [job="ID:57, Type:create schema, State:none, SchemaState:none, SchemaID:56, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-15 12:51:08.666 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/15 12:51:08.730 +00:00] [INFO] [ddl_worker.go:568] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:57, Type:create schema, State:none, SchemaState:none, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 12:51:08.666 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 12:51:08.753 +00:00] [INFO] [domain.go:126] ["diff load InfoSchema success"] [usedSchemaVersion=35] [neededSchemaVersion=36] ["start time"=758.415µs] [tblIDs="[]"]
   > [2024/07/15 12:51:08.803 +00:00] [INFO] [ddl_worker.go:759] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=36] ["take time"=57.14043ms] [job="ID:57, Type:create schema, State:done, SchemaState:public, SchemaID:56, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-15 12:51:08.666 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 12:51:08.806 +00:00] [INFO] [ddl_worker.go:359] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:57, Type:create schema, State:synced, SchemaState:public, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 12:51:08.666 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 12:51:08.824 +00:00] [INFO] [ddl.go:532] ["[ddl] DDL job is finished"] [jobID=57]
   > [2024/07/15 12:51:08.824 +00:00] [INFO] [domain.go:631] ["performing DDL change, must reload"]
   > [2024/07/15 12:51:08.827 +00:00] [INFO] [session.go:2210] ["CRUCIAL OPERATION"] [conn=7] [schemaVersion=36] [cur_db=testdb] [sql="CREATE TABLE t1 (\n id int not null primary key auto_increment,\n t varchar(100)\n);"] [user=root@10.88.0.53]
   > [2024/07/15 12:51:08.859 +00:00] [INFO] [ddl_worker.go:253] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:59, Type:create table, State:none, SchemaState:none, SchemaID:56, TableID:58, RowCount:0, ArgLen:1, start time: 2024-07-15 12:51:08.816 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/15 12:51:08.859 +00:00] [INFO] [ddl.go:500] ["[ddl] start DDL job"] [job="ID:59, Type:create table, State:none, SchemaState:none, SchemaID:56, TableID:58, RowCount:0, ArgLen:1, start time: 2024-07-15 12:51:08.816 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE t1 (\n id int not null primary key auto_increment,\n t varchar(100)\n);"]
   > [2024/07/15 12:51:08.862 +00:00] [INFO] [ddl_worker.go:568] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:59, Type:create table, State:none, SchemaState:none, SchemaID:56, TableID:58, RowCount:0, ArgLen:0, start time: 2024-07-15 12:51:08.816 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 12:51:08.895 +00:00] [INFO] [domain.go:126] ["diff load InfoSchema success"] [usedSchemaVersion=36] [neededSchemaVersion=37] ["start time"=1.453904ms] [tblIDs="[58]"]
   > [2024/07/15 12:51:08.945 +00:00] [INFO] [ddl_worker.go:759] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=37] ["take time"=62.013385ms] [job="ID:59, Type:create table, State:done, SchemaState:public, SchemaID:56, TableID:58, RowCount:0, ArgLen:1, start time: 2024-07-15 12:51:08.816 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 12:51:08.949 +00:00] [INFO] [ddl_worker.go:359] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:59, Type:create table, State:synced, SchemaState:public, SchemaID:56, TableID:58, RowCount:0, ArgLen:0, start time: 2024-07-15 12:51:08.816 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 12:51:08.970 +00:00] [INFO] [ddl.go:532] ["[ddl] DDL job is finished"] [jobID=59]
   > [2024/07/15 12:51:08.972 +00:00] [INFO] [domain.go:631] ["performing DDL change, must reload"]
   > [2024/07/15 12:51:08.972 +00:00] [INFO] [split_region.go:56] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=74800000000000003a]
   > [2024/07/15 12:51:08.973 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:47584] [split_keys="key 7480000000000000FF3A00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/15 12:51:08.973 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=48] [peer-ids="[49]"]
   > [2024/07/15 12:51:08.973 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF3400000000000000F8 region_epoch { conf_ver: 1 version: 23 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 48 new_peer_ids: 49]"] [region_id=2]
   > [2024/07/15 12:51:08.979 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF3A00000000000000F8 new_region_id: 48 new_peer_ids: 49 } right_derive: true }"] [index=62] [term=6] [peer_id=3] [region_id=2]
   > [2024/07/15 12:51:08.979 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF3A00000000000000F8"] [region="id: 2 start_key: 7480000000000000FF3400000000000000F8 region_epoch { conf_ver: 1 version: 23 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/07/15 12:51:08.989 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/15 12:51:08.989 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=2]
   > [2024/07/15 12:51:08.989 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/07/15 12:51:08.989 +00:00] [INFO] [split_region.go:153] ["batch split regions complete"] ["batch region ID"=2] ["first at"=74800000000000003a] ["first new region left"="{Id:48 StartKey:7480000000000000ff3400000000000000f8 EndKey:7480000000000000ff3a00000000000000f8 RegionEpoch:{ConfVer:1 Version:24} Peers:[id:49 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/15 12:51:08.989 +00:00] [INFO] [split_region.go:205] ["split regions complete"] ["region count"=1] ["region IDs"="[48]"]
   > [2024/07/15 12:51:08.989 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 48 start_key: 7480000000000000FF3400000000000000F8 end_key: 7480000000000000FF3A00000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 49 store_id: 1 }"] [region_id=48]
   > [2024/07/15 12:51:08.989 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=49] [region_id=48]
   > [2024/07/15 12:51:08.990 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 2 start_key: 7480000000000000FF3A00000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 3 store_id: 1 } }"]
   > [2024/07/15 12:51:08.990 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 2 start_key: 7480000000000000FF3A00000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 3 store_id: 1 }"]
   > [2024/07/15 12:51:08.990 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {49} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=49] [region_id=48]
   > [2024/07/15 12:51:08.990 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF3400000000000000F8} -> {7480000000000000FF3A00000000000000F8}, EndKey:{}"] [old-version=23] [new-version=24]
   > [2024/07/15 12:51:08.990 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=2] [origin="id:48 start_key:\"7480000000000000FF3400000000000000F8\" end_key:\"7480000000000000FF3A00000000000000F8\" region_epoch:<conf_ver:1 version:24 > peers:<id:49 store_id:1 >"] [total=1]
   > [2024/07/15 12:51:08.990 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=49] [region_id=48]
   > [2024/07/15 12:51:08.990 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {49} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=49] [region_id=48]
   > [2024/07/15 12:51:08.990 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 49."] [id=49] [raft_id=49] [region_id=48]
   > [2024/07/15 12:51:08.990 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=49] [region_id=48]
   > [2024/07/15 12:51:08.991 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=49] [region_id=48]
   > [2024/07/15 12:51:08.991 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=49] [region_id=48]
   > [2024/07/15 12:51:08.991 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=49] [region_id=48]
   > [2024/07/15 12:51:08.991 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803824] [region_id=48]
   > [2024/07/15 12:51:08.991 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(43)] [region_id=2] [store_id=Some(1)]
   > [2024/07/15 12:51:08.991 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF3A00000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 3 store_id: 1 }"]
   > [2024/07/15 12:51:08.991 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=62] [observe_id=ObserveId(45)] [region=2]
   > [2024/07/15 12:51:08.991 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=48]
   > [2024/07/15 12:51:08.995 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 48 start_key: 7480000000000000FF3400000000000000F8 end_key: 7480000000000000FF3A00000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 49 store_id: 1 }"]
   > [2024/07/15 12:51:08.995 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(46)] [region=48]
   > [2024/07/15 12:51:09.006 +00:00] [INFO] [scheduler.rs:640] ["get snapshot failed"] [err="Error(Request(message: \"EpochNotMatch current epoch of region 2 is conf_ver: 1 version: 24, but you sent conf_ver: 1 version: 23\" epoch_not_match { current_regions { id: 2 start_key: 7480000000000000FF3A00000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 3 store_id: 1 } } current_regions { id: 48 start_key: 7480000000000000FF3400000000000000F8 end_key: 7480000000000000FF3A00000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 49 store_id: 1 } } }))"] [cid=354]
   > [2024/07/15 12:51:09.026 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=7]
   > [2024/07/15 12:51:10.041 +00:00] [INFO] [server.go:388] ["new connection"] [conn=8] [remoteAddr=10.88.0.53:42084]
   > [2024/07/15 12:51:10.052 +00:00] [INFO] [set.go:207] ["set session var"] [conn=8] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/07/15 12:51:10.654 +00:00] [INFO] [server.go:388] ["new connection"] [conn=9] [remoteAddr=10.88.0.53:42088]
   > [2024/07/15 12:51:10.657 +00:00] [INFO] [set.go:207] ["set session var"] [conn=9] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/07/15 12:51:14.255 +00:00] [WARN] [session.go:1162] ["run statement failed"] [conn=9] [schemaVersion=37] [error="[tikv:1205]Lock wait timeout exceeded; try restarting transaction"] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 9,\n  \"status\": 3,\n  \"strictMode\": true,\n  \"txn\": \"451162372994760710\",\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"10.88.0.53\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/07/15 12:51:14.255 +00:00] [ERROR] [conn.go:730] ["command dispatched failed"] [conn=9] [connInfo="id:9, addr:10.88.0.53:42088 status:11, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:1, autocommit:1"] [sql=" UPDATE t1 SET t='newval' WHERE id = 1;"] [txn_mode=PESSIMISTIC] [err="[tikv:1205]Lock wait timeout exceeded; try restarting transaction\ngithub.com/pingcap/errors.AddStack\n\t/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.20190809092503-95897b64e011/errors.go:174\ngithub.com/pingcap/errors.Trace\n\t/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.20190809092503-95897b64e011/juju_adaptor.go:15\ngithub.com/pingcap/tidb/store/tikv.actionPessimisticLock.handleSingleBatch\n\t/go/src/github.com/pingcap/tidb/store/tikv/2pc.go:875\ngithub.com/pingcap/tidb/store/tikv.(*twoPhaseCommitter).doActionOnBatches\n\t/go/src/github.com/pingcap/tidb/store/tikv/2pc.go:530\ngithub.com/pingcap/tidb/store/tikv.(*twoPhaseCommitter).doActionOnMutations\n\t/go/src/github.com/pingcap/tidb/store/tikv/2pc.go:495\ngithub.com/pingcap/tidb/store/tikv.(*twoPhaseCommitter).pessimisticLockMutations\n\t/go/src/github.com/pingcap/tidb/store/tikv/2pc.go:1123\ngithub.com/pingcap/tidb/store/tikv.(*tikvTxn).LockKeys\n\t/go/src/github.com/pingcap/tidb/store/tikv/txn.go:385\ngithub.com/pingcap/tidb/executor.doLockKeys\n\t/go/src/github.com/pingcap/tidb/executor/executor.go:981\ngithub.com/pingcap/tidb/executor.(*PointGetExecutor).lockKeyIfNeeded\n\t/go/src/github.com/pingcap/tidb/executor/point_get.go:252\ngithub.com/pingcap/tidb/executor.(*PointGetExecutor).getAndLock\n\t/go/src/github.com/pingcap/tidb/executor/point_get.go:235\ngithub.com/pingcap/tidb/executor.(*PointGetExecutor).Next\n\t/go/src/github.com/pingcap/tidb/executor/point_get.go:194\ngithub.com/pingcap/tidb/executor.Next\n\t/go/src/github.com/pingcap/tidb/executor/executor.go:249\ngithub.com/pingcap/tidb/executor.(*UpdateExec).updateRows\n\t/go/src/github.com/pingcap/tidb/executor/update.go:157\ngithub.com/pingcap/tidb/executor.(*UpdateExec).Next\n\t/go/src/github.com/pingcap/tidb/executor/update.go:125\ngithub.com/pingcap/tidb/executor.Next\n\t/go/src/github.com/pingcap/tidb/executor/executor.go:249\ngithub.com/pingcap/tidb/executor.(*ExecStmt).handleNoDelayExecutor\n\t/go/src/github.com/pingcap/tidb/executor/adapter.go:510\ngithub.com/pingcap/tidb/executor.(*ExecStmt).handlePessimisticDML\n\t/go/src/github.com/pingcap/tidb/executor/adapter.go:529\ngithub.com/pingcap/tidb/executor.(*ExecStmt).handleNoDelay\n\t/go/src/github.com/pingcap/tidb/executor/adapter.go:392\ngithub.com/pingcap/tidb/executor.(*ExecStmt).Exec\n\t/go/src/github.com/pingcap/tidb/executor/adapter.go:362\ngithub.com/pingcap/tidb/session.runStmt\n\t/go/src/github.com/pingcap/tidb/session/tidb.go:276\ngithub.com/pingcap/tidb/session.(*session).ExecuteStmt\n\t/go/src/github.com/pingcap/tidb/session/session.go:1159\ngithub.com/pingcap/tidb/server.(*TiDBContext).ExecuteStmt\n\t/go/src/github.com/pingcap/tidb/server/driver_tidb.go:248\ngithub.com/pingcap/tidb/server.(*clientConn).handleStmt\n\t/go/src/github.com/pingcap/tidb/server/conn.go:1290\ngithub.com/pingcap/tidb/server.(*clientConn).handleQuery\n\t/go/src/github.com/pingcap/tidb/server/conn.go:1278\ngithub.com/pingcap/tidb/server.(*clientConn).dispatch\n\t/go/src/github.com/pingcap/tidb/server/conn.go:901\ngithub.com/pingcap/tidb/server.(*clientConn).Run\n\t/go/src/github.com/pingcap/tidb/server/conn.go:715\ngithub.com/pingcap/tidb/server.(*Server).onConn\n\t/go/src/github.com/pingcap/tidb/server/server.go:415\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1594"]
   > [2024/07/15 12:51:19.643 +00:00] [ERROR] [grpclog.go:75] ["transport: Got too many pings from the client, closing the connection."]
   > [2024/07/15 12:51:19.643 +00:00] [ERROR] [grpclog.go:75] ["transport: loopyWriter.run returning. Err: transport: Connection closing"]
   > [2024/07/15 12:51:19.643 +00:00] [WARN] [grpclog.go:60] ["transport: http2Server.HandleStreams failed to read frame: read tcp 127.0.0.1:2379->127.0.0.1:38200: use of closed network connection"]
   > [2024/07/15 12:51:20.952 +00:00] [INFO] [2pc.go:748] ["send TxnHeartBeat"] [startTS=451162372916117505] [newTTL=30599]
   > [2024/07/15 12:51:21.554 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=9]
   > [2024/07/15 12:51:21.560 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=8]
