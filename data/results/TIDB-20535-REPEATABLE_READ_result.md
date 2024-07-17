# Bug ID TIDB-20535-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/20535
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              The second select should output the same table as the first one, but it doesn't.


## Details
 * Database: tidb-v4.0.4.tikv
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
     - Instruction:  delete from t2 where k = 1;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 1 / 0
 * Instruction #4:
     - Instruction:  insert into t2 values(1, 1, 2);
     - Transaction: conn_1
     - Output: ERROR: 1062 (23000): Duplicate entry '1-1' for key 'PRIMARY'
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0

 * Container logs:
   > [2024/07/17 07:43:18.116 +00:00] [INFO] [server.go:388] ["new connection"] [conn=2] [remoteAddr=10.88.0.188:54650]
   > [2024/07/17 07:43:18.118 +00:00] [INFO] [session.go:2130] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=22] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.188]
   > [2024/07/17 07:43:18.119 +00:00] [INFO] [session.go:2130] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=22] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.188]
   > [2024/07/17 07:43:18.148 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-17 07:43:18.128 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/17 07:43:18.148 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-17 07:43:18.128 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/17 07:43:18.151 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-17 07:43:18.128 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 07:43:18.165 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=22] [neededSchemaVersion=23] ["start time"=954.95µs] [tblIDs="[]"]
   > [2024/07/17 07:43:18.215 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=23] ["take time"=52.136874ms] [job="ID:46, Type:create schema, State:done, SchemaState:public, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-17 07:43:18.128 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 07:43:18.218 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:46, Type:create schema, State:synced, SchemaState:public, SchemaID:45, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-17 07:43:18.128 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 07:43:18.230 +00:00] [INFO] [ddl.go:509] ["[ddl] DDL job is finished"] [jobID=46]
   > [2024/07/17 07:43:18.230 +00:00] [INFO] [domain.go:624] ["performing DDL change, must reload"]
   > [2024/07/17 07:43:18.234 +00:00] [INFO] [session.go:2130] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=23] [cur_db=testdb] [sql="create table t2(k int, kk int, val int, primary key(k, kk));"] [user=root@10.88.0.188]
   > [2024/07/17 07:43:18.258 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-07-17 07:43:18.228 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/17 07:43:18.258 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-07-17 07:43:18.228 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t2(k int, kk int, val int, primary key(k, kk));"]
   > [2024/07/17 07:43:18.262 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-17 07:43:18.228 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 07:43:18.282 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=23] [neededSchemaVersion=24] ["start time"=1.533871ms] [tblIDs="[47]"]
   > [2024/07/17 07:43:18.331 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=24] ["take time"=52.14358ms] [job="ID:48, Type:create table, State:done, SchemaState:public, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-07-17 07:43:18.228 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 07:43:18.334 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:48, Type:create table, State:synced, SchemaState:public, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-17 07:43:18.228 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 07:43:18.347 +00:00] [INFO] [ddl.go:509] ["[ddl] DDL job is finished"] [jobID=48]
   > [2024/07/17 07:43:18.349 +00:00] [INFO] [domain.go:624] ["performing DDL change, must reload"]
   > [2024/07/17 07:43:18.349 +00:00] [INFO] [split_region.go:56] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=74800000000000002f]
   > [2024/07/17 07:43:18.349 +00:00] [INFO] [peer.rs:458] ["on split"] [split_keys="key 7480000000000000FF2F00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/17 07:43:18.350 +00:00] [INFO] [cluster_worker.go:131] ["alloc ids for region split"] [region-id=44] [peer-ids="[45]"]
   > [2024/07/17 07:43:18.350 +00:00] [INFO] [pd.rs:499] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF2B00000000000000F8 region_epoch { conf_ver: 1 version: 21 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 44 new_peer_ids: 45]"] [region_id=2]
   > [2024/07/17 07:43:18.354 +00:00] [INFO] [apply.rs:1144] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF2F00000000000000F8 new_region_id: 44 new_peer_ids: 45 } right_derive: true }"] [index=53] [term=6] [peer_id=3] [region_id=2]
   > [2024/07/17 07:43:18.354 +00:00] [INFO] [apply.rs:1712] ["split region"] [keys="key 7480000000000000FF2F00000000000000F8"] [region="id: 2 start_key: 7480000000000000FF2B00000000000000F8 region_epoch { conf_ver: 1 version: 21 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/07/17 07:43:18.361 +00:00] [INFO] [peer.rs:1727] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/07/17 07:43:18.362 +00:00] [INFO] [peer.rs:1769] ["insert new region"] [region="id: 44 start_key: 7480000000000000FF2B00000000000000F8 end_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 45 store_id: 1 }"] [region_id=44]
   > [2024/07/17 07:43:18.362 +00:00] [INFO] [peer.rs:158] ["create peer"] [peer_id=45] [region_id=44]
   > [2024/07/17 07:43:18.362 +00:00] [INFO] [split_region.go:153] ["batch split regions complete"] ["batch region ID"=2] ["first at"=74800000000000002f] ["first new region left"="{Id:44 StartKey:7480000000000000ff2b00000000000000f8 EndKey:7480000000000000ff2f00000000000000f8 RegionEpoch:{ConfVer:1 Version:22} Peers:[id:45 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/17 07:43:18.362 +00:00] [INFO] [raft.rs:783] ["became follower at term 5"] [term=5] [raft_id=45] [region_id=44]
   > [2024/07/17 07:43:18.362 +00:00] [INFO] [split_region.go:205] ["split regions complete"] ["region count"=1] ["region IDs"="[44]"]
   > [2024/07/17 07:43:18.362 +00:00] [INFO] [raft.rs:285] [newRaft] [peers="[(45, Progress { matched: 5, next_idx: 6, state: Probe, paused: false, pending_snapshot: 0, pending_request_snapshot: 0, recent_active: false, ins: Inflights { start: 0, count: 0, buffer: [] } })]"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=45] [region_id=44]
   > [2024/07/17 07:43:18.362 +00:00] [INFO] [cluster.go:478] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF2B00000000000000F8} -> {7480000000000000FF2F00000000000000F8}, EndKey:{}"] [old-version=21] [new-version=22]
   > [2024/07/17 07:43:18.362 +00:00] [INFO] [raw_node.rs:222] ["RawNode created with id 45."] [id=45] [raft_id=45] [region_id=44]
   > [2024/07/17 07:43:18.362 +00:00] [INFO] [raft.rs:1177] ["starting a new election"] [term=5] [raft_id=45] [region_id=44]
   > [2024/07/17 07:43:18.362 +00:00] [INFO] [cluster_worker.go:218] ["region batch split, generate new regions"] [region-id=2] [origin="id:44 start_key:\"7480000000000000FF2B00000000000000F8\" end_key:\"7480000000000000FF2F00000000000000F8\" region_epoch:<conf_ver:1 version:22 > peers:<id:45 store_id:1 >"] [total=1]
   > [2024/07/17 07:43:18.362 +00:00] [INFO] [raft.rs:833] ["became pre-candidate at term 5"] [term=5] [raft_id=45] [region_id=44]
   > [2024/07/17 07:43:18.362 +00:00] [INFO] [raft.rs:902] ["45 received message from 45"] [term=5] [msg=MsgRequestPreVote] [from=45] [id=45] [raft_id=45] [region_id=44]
   > [2024/07/17 07:43:18.362 +00:00] [INFO] [raft.rs:807] ["became candidate at term 6"] [term=6] [raft_id=45] [region_id=44]
   > [2024/07/17 07:43:18.363 +00:00] [INFO] [raft.rs:902] ["45 received message from 45"] [term=6] [msg=MsgRequestVote] [from=45] [id=45] [raft_id=45] [region_id=44]
   > [2024/07/17 07:43:18.363 +00:00] [INFO] [raft.rs:874] ["became leader at term 6"] [term=6] [raft_id=45] [region_id=44]
   > [2024/07/17 07:43:18.368 +00:00] [INFO] [process.rs:145] ["get snapshot failed"] [err="Request(message: \"EpochNotMatch current epoch of region 2 is conf_ver: 1 version: 22, but you sent conf_ver: 1 version: 21\" epoch_not_match { current_regions { id: 2 start_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 3 store_id: 1 } } current_regions { id: 44 start_key: 7480000000000000FF2B00000000000000F8 end_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 45 store_id: 1 } } })"] [cid=254]
   > [2024/07/17 07:43:18.383 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=2]
   > [2024/07/17 07:43:19.397 +00:00] [INFO] [server.go:388] ["new connection"] [conn=4] [remoteAddr=10.88.0.188:54660]
   > [2024/07/17 07:43:19.400 +00:00] [INFO] [set.go:207] ["set session var"] [conn=4] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/07/17 07:43:20.008 +00:00] [INFO] [server.go:388] ["new connection"] [conn=5] [remoteAddr=10.88.0.188:54668]
   > [2024/07/17 07:43:20.017 +00:00] [INFO] [set.go:207] ["set session var"] [conn=5] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/07/17 07:43:20.609 +00:00] [ERROR] [conn.go:730] ["command dispatched failed"] [conn=5] [connInfo="id:5, addr:10.88.0.188:54668 status:11, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:1, autocommit:1"] [sql=" insert into t2 values(1, 1, 2);"] [txn_mode=PESSIMISTIC] [err="[kv:1062]Duplicate entry '1-1' for key 'PRIMARY'"]
   > [2024/07/17 07:43:21.009 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=5]
   > [2024/07/17 07:43:21.020 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=4]
