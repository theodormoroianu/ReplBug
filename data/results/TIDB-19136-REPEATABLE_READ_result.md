# Bug ID TIDB-19136-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/19136
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              Duplicate key is ignored in insert The insert statement should fail.


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
     - Instruction:  insert into t values (1, 'amazing almeida'), (2, 'boring bardeen'), (3, 'busy w...
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 3 / 0
 * Instruction #3:
     - Instruction:  select c_int, (select t1.c_int from t t1 where t1.c_int = 3 and t1.c_int > t.c_...
     - Transaction: conn_0
     - Output: [(1, 3), (2, None), (3, None)]
     - Executed order: 3
     - Affected rows / Warnings: 3 / 0
 * Instruction #4:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows / Warnings: 0 / 0
 * Instruction #5:
     - Instruction:  select c_int, (select t1.c_int from t t1 where t1.c_int = 3 and t1.c_int > t.c_...
     - Transaction: conn_0
     - Output: [(1, 3), (2, 3), (3, None)]
     - Executed order: 5
     - Affected rows / Warnings: 3 / 0

 * Container logs:
   > [2024/07/16 13:34:06.996 +00:00] [INFO] [server.go:388] ["new connection"] [conn=2] [remoteAddr=10.88.0.72:40992]
   > [2024/07/16 13:34:06.999 +00:00] [INFO] [session.go:2130] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=22] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.72]
   > [2024/07/16 13:34:07.000 +00:00] [INFO] [session.go:2130] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=22] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.72]
   > [2024/07/16 13:34:07.037 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-16 13:34:06.984 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/16 13:34:07.038 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-16 13:34:06.984 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/16 13:34:07.041 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 13:34:06.984 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 13:34:07.061 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=22] [neededSchemaVersion=23] ["start time"=1.089885ms] [tblIDs="[]"]
   > [2024/07/16 13:34:07.110 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=23] ["take time"=52.779075ms] [job="ID:46, Type:create schema, State:done, SchemaState:public, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-16 13:34:06.984 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 13:34:07.113 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:46, Type:create schema, State:synced, SchemaState:public, SchemaID:45, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 13:34:06.984 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 13:34:07.129 +00:00] [INFO] [ddl.go:509] ["[ddl] DDL job is finished"] [jobID=46]
   > [2024/07/16 13:34:07.129 +00:00] [INFO] [domain.go:624] ["performing DDL change, must reload"]
   > [2024/07/16 13:34:07.133 +00:00] [INFO] [session.go:2130] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=23] [cur_db=testdb] [sql="create table t ( c_int int, c_str varchar(40), primary key(c_int, c_str) );"] [user=root@10.88.0.72]
   > [2024/07/16 13:34:07.162 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-07-16 13:34:07.134 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/16 13:34:07.162 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-07-16 13:34:07.134 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t ( c_int int, c_str varchar(40), primary key(c_int, c_str) );"]
   > [2024/07/16 13:34:07.165 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-16 13:34:07.134 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 13:34:07.190 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=23] [neededSchemaVersion=24] ["start time"=1.233341ms] [tblIDs="[47]"]
   > [2024/07/16 13:34:07.239 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=24] ["take time"=52.051879ms] [job="ID:48, Type:create table, State:done, SchemaState:public, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-07-16 13:34:07.134 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 13:34:07.241 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:48, Type:create table, State:synced, SchemaState:public, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-16 13:34:07.134 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 13:34:07.261 +00:00] [INFO] [ddl.go:509] ["[ddl] DDL job is finished"] [jobID=48]
   > [2024/07/16 13:34:07.263 +00:00] [INFO] [domain.go:624] ["performing DDL change, must reload"]
   > [2024/07/16 13:34:07.263 +00:00] [INFO] [split_region.go:56] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=74800000000000002f]
   > [2024/07/16 13:34:07.264 +00:00] [INFO] [peer.rs:458] ["on split"] [split_keys="key 7480000000000000FF2F00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/16 13:34:07.264 +00:00] [INFO] [cluster_worker.go:131] ["alloc ids for region split"] [region-id=44] [peer-ids="[45]"]
   > [2024/07/16 13:34:07.264 +00:00] [INFO] [pd.rs:499] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF2B00000000000000F8 region_epoch { conf_ver: 1 version: 21 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 44 new_peer_ids: 45]"] [region_id=2]
   > [2024/07/16 13:34:07.265 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=2]
   > [2024/07/16 13:34:07.271 +00:00] [INFO] [apply.rs:1144] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF2F00000000000000F8 new_region_id: 44 new_peer_ids: 45 } right_derive: true }"] [index=53] [term=6] [peer_id=3] [region_id=2]
   > [2024/07/16 13:34:07.271 +00:00] [INFO] [apply.rs:1712] ["split region"] [keys="key 7480000000000000FF2F00000000000000F8"] [region="id: 2 start_key: 7480000000000000FF2B00000000000000F8 region_epoch { conf_ver: 1 version: 21 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/07/16 13:34:07.281 +00:00] [INFO] [peer.rs:1727] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/07/16 13:34:07.282 +00:00] [INFO] [peer.rs:1769] ["insert new region"] [region="id: 44 start_key: 7480000000000000FF2B00000000000000F8 end_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 45 store_id: 1 }"] [region_id=44]
   > [2024/07/16 13:34:07.282 +00:00] [INFO] [split_region.go:153] ["batch split regions complete"] ["batch region ID"=2] ["first at"=74800000000000002f] ["first new region left"="{Id:44 StartKey:7480000000000000ff2b00000000000000f8 EndKey:7480000000000000ff2f00000000000000f8 RegionEpoch:{ConfVer:1 Version:22} Peers:[id:45 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/16 13:34:07.282 +00:00] [INFO] [peer.rs:158] ["create peer"] [peer_id=45] [region_id=44]
   > [2024/07/16 13:34:07.282 +00:00] [INFO] [split_region.go:205] ["split regions complete"] ["region count"=1] ["region IDs"="[44]"]
   > [2024/07/16 13:34:07.282 +00:00] [INFO] [raft.rs:783] ["became follower at term 5"] [term=5] [raft_id=45] [region_id=44]
   > [2024/07/16 13:34:07.282 +00:00] [INFO] [cluster.go:478] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF2B00000000000000F8} -> {7480000000000000FF2F00000000000000F8}, EndKey:{}"] [old-version=21] [new-version=22]
   > [2024/07/16 13:34:07.282 +00:00] [INFO] [raft.rs:285] [newRaft] [peers="[(45, Progress { matched: 5, next_idx: 6, state: Probe, paused: false, pending_snapshot: 0, pending_request_snapshot: 0, recent_active: false, ins: Inflights { start: 0, count: 0, buffer: [] } })]"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=45] [region_id=44]
   > [2024/07/16 13:34:07.282 +00:00] [INFO] [raw_node.rs:222] ["RawNode created with id 45."] [id=45] [raft_id=45] [region_id=44]
   > [2024/07/16 13:34:07.282 +00:00] [INFO] [raft.rs:1177] ["starting a new election"] [term=5] [raft_id=45] [region_id=44]
   > [2024/07/16 13:34:07.283 +00:00] [INFO] [raft.rs:833] ["became pre-candidate at term 5"] [term=5] [raft_id=45] [region_id=44]
   > [2024/07/16 13:34:07.283 +00:00] [INFO] [cluster_worker.go:218] ["region batch split, generate new regions"] [region-id=2] [origin="id:44 start_key:\"7480000000000000FF2B00000000000000F8\" end_key:\"7480000000000000FF2F00000000000000F8\" region_epoch:<conf_ver:1 version:22 > peers:<id:45 store_id:1 >"] [total=1]
   > [2024/07/16 13:34:07.283 +00:00] [INFO] [raft.rs:902] ["45 received message from 45"] [term=5] [msg=MsgRequestPreVote] [from=45] [id=45] [raft_id=45] [region_id=44]
   > [2024/07/16 13:34:07.283 +00:00] [INFO] [raft.rs:807] ["became candidate at term 6"] [term=6] [raft_id=45] [region_id=44]
   > [2024/07/16 13:34:07.283 +00:00] [INFO] [raft.rs:902] ["45 received message from 45"] [term=6] [msg=MsgRequestVote] [from=45] [id=45] [raft_id=45] [region_id=44]
   > [2024/07/16 13:34:07.283 +00:00] [INFO] [raft.rs:874] ["became leader at term 6"] [term=6] [raft_id=45] [region_id=44]
   > [2024/07/16 13:34:08.284 +00:00] [INFO] [server.go:388] ["new connection"] [conn=4] [remoteAddr=10.88.0.72:41006]
   > [2024/07/16 13:34:08.292 +00:00] [INFO] [set.go:207] ["set session var"] [conn=4] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/07/16 13:34:08.907 +00:00] [INFO] [process.rs:145] ["get snapshot failed"] [err="Request(message: \"EpochNotMatch current epoch of region 2 is conf_ver: 1 version: 22, but you sent conf_ver: 1 version: 21\" epoch_not_match { current_regions { id: 2 start_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 3 store_id: 1 } } current_regions { id: 44 start_key: 7480000000000000FF2B00000000000000F8 end_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 45 store_id: 1 } } })"] [cid=255]
   > [2024/07/16 13:34:20.089 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=4]
