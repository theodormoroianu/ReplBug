# Bug ID TIDB-19136-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/19136
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              Duplicate key is ignored in insert The insert statement should fail.


## Details
 * Database: tidb-v4.0.4.tikv
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
   > [2024/07/16 13:34:21.552 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=5]
   > [2024/07/16 13:34:21.555 +00:00] [INFO] [server.go:388] ["new connection"] [conn=6] [remoteAddr=10.88.0.72:54852]
   > [2024/07/16 13:34:21.557 +00:00] [INFO] [session.go:2130] ["CRUCIAL OPERATION"] [conn=6] [schemaVersion=32] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.72]
   > [2024/07/16 13:34:21.572 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:55, Type:drop schema, State:none, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 13:34:21.534 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/16 13:34:21.572 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:55, Type:drop schema, State:none, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 13:34:21.534 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/16 13:34:21.575 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:55, Type:drop schema, State:none, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 13:34:21.534 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 13:34:21.593 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=32] [neededSchemaVersion=33] ["start time"=464.59µs] [tblIDs="[]"]
   > [2024/07/16 13:34:21.643 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=33] ["take time"=51.997612ms] [job="ID:55, Type:drop schema, State:running, SchemaState:write only, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 13:34:21.534 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 13:34:21.644 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:55, Type:drop schema, State:running, SchemaState:write only, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 13:34:21.534 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 13:34:21.669 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=33] [neededSchemaVersion=34] ["start time"=553.428µs] [tblIDs="[]"]
   > [2024/07/16 13:34:21.719 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=34] ["take time"=52.202319ms] [job="ID:55, Type:drop schema, State:running, SchemaState:delete only, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 13:34:21.534 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 13:34:21.721 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:55, Type:drop schema, State:running, SchemaState:delete only, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 13:34:21.534 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 13:34:21.740 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=34] [neededSchemaVersion=35] ["start time"=469.897µs] [tblIDs="[]"]
   > [2024/07/16 13:34:21.799 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=35] ["take time"=60.167315ms] [job="ID:55, Type:drop schema, State:done, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 13:34:21.534 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 13:34:21.801 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=55] [jobType="drop schema"]
   > [2024/07/16 13:34:21.802 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:55, Type:drop schema, State:synced, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 13:34:21.534 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 13:34:21.817 +00:00] [INFO] [ddl.go:509] ["[ddl] DDL job is finished"] [jobID=55]
   > [2024/07/16 13:34:21.817 +00:00] [INFO] [domain.go:624] ["performing DDL change, must reload"]
   > [2024/07/16 13:34:21.819 +00:00] [INFO] [session.go:2130] ["CRUCIAL OPERATION"] [conn=6] [schemaVersion=35] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.72]
   > [2024/07/16 13:34:21.848 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:57, Type:create schema, State:none, SchemaState:none, SchemaID:56, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-16 13:34:21.785 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/16 13:34:21.848 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:57, Type:create schema, State:none, SchemaState:none, SchemaID:56, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-16 13:34:21.785 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/16 13:34:21.851 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:57, Type:create schema, State:none, SchemaState:none, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 13:34:21.785 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 13:34:21.870 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=35] [neededSchemaVersion=36] ["start time"=1.214693ms] [tblIDs="[]"]
   > [2024/07/16 13:34:21.919 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=36] ["take time"=52.143582ms] [job="ID:57, Type:create schema, State:done, SchemaState:public, SchemaID:56, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-16 13:34:21.785 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 13:34:21.922 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:57, Type:create schema, State:synced, SchemaState:public, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 13:34:21.785 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 13:34:21.938 +00:00] [INFO] [ddl.go:509] ["[ddl] DDL job is finished"] [jobID=57]
   > [2024/07/16 13:34:21.938 +00:00] [INFO] [domain.go:624] ["performing DDL change, must reload"]
   > [2024/07/16 13:34:21.942 +00:00] [INFO] [session.go:2130] ["CRUCIAL OPERATION"] [conn=6] [schemaVersion=36] [cur_db=testdb] [sql="create table t ( c_int int, c_str varchar(40), primary key(c_int, c_str) );"] [user=root@10.88.0.72]
   > [2024/07/16 13:34:21.972 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:59, Type:create table, State:none, SchemaState:none, SchemaID:56, TableID:58, RowCount:0, ArgLen:1, start time: 2024-07-16 13:34:21.934 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/16 13:34:21.972 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:59, Type:create table, State:none, SchemaState:none, SchemaID:56, TableID:58, RowCount:0, ArgLen:1, start time: 2024-07-16 13:34:21.934 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t ( c_int int, c_str varchar(40), primary key(c_int, c_str) );"]
   > [2024/07/16 13:34:21.975 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:59, Type:create table, State:none, SchemaState:none, SchemaID:56, TableID:58, RowCount:0, ArgLen:0, start time: 2024-07-16 13:34:21.934 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 13:34:21.996 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=36] [neededSchemaVersion=37] ["start time"=1.775524ms] [tblIDs="[58]"]
   > [2024/07/16 13:34:22.044 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=37] ["take time"=51.869033ms] [job="ID:59, Type:create table, State:done, SchemaState:public, SchemaID:56, TableID:58, RowCount:0, ArgLen:1, start time: 2024-07-16 13:34:21.934 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 13:34:22.047 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:59, Type:create table, State:synced, SchemaState:public, SchemaID:56, TableID:58, RowCount:0, ArgLen:0, start time: 2024-07-16 13:34:21.934 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 13:34:22.064 +00:00] [INFO] [ddl.go:509] ["[ddl] DDL job is finished"] [jobID=59]
   > [2024/07/16 13:34:22.066 +00:00] [INFO] [domain.go:624] ["performing DDL change, must reload"]
   > [2024/07/16 13:34:22.067 +00:00] [INFO] [split_region.go:56] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=74800000000000003a]
   > [2024/07/16 13:34:22.067 +00:00] [INFO] [peer.rs:458] ["on split"] [split_keys="key 7480000000000000FF3A00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/16 13:34:22.067 +00:00] [INFO] [cluster_worker.go:131] ["alloc ids for region split"] [region-id=48] [peer-ids="[49]"]
   > [2024/07/16 13:34:22.068 +00:00] [INFO] [pd.rs:499] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF3400000000000000F8 region_epoch { conf_ver: 1 version: 23 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 48 new_peer_ids: 49]"] [region_id=2]
   > [2024/07/16 13:34:22.068 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=6]
   > [2024/07/16 13:34:22.073 +00:00] [INFO] [apply.rs:1144] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF3A00000000000000F8 new_region_id: 48 new_peer_ids: 49 } right_derive: true }"] [index=61] [term=6] [peer_id=3] [region_id=2]
   > [2024/07/16 13:34:22.073 +00:00] [INFO] [apply.rs:1712] ["split region"] [keys="key 7480000000000000FF3A00000000000000F8"] [region="id: 2 start_key: 7480000000000000FF3400000000000000F8 region_epoch { conf_ver: 1 version: 23 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/07/16 13:34:22.079 +00:00] [INFO] [peer.rs:1727] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/07/16 13:34:22.079 +00:00] [INFO] [peer.rs:1769] ["insert new region"] [region="id: 48 start_key: 7480000000000000FF3400000000000000F8 end_key: 7480000000000000FF3A00000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 49 store_id: 1 }"] [region_id=48]
   > [2024/07/16 13:34:22.079 +00:00] [INFO] [peer.rs:158] ["create peer"] [peer_id=49] [region_id=48]
   > [2024/07/16 13:34:22.079 +00:00] [INFO] [raft.rs:783] ["became follower at term 5"] [term=5] [raft_id=49] [region_id=48]
   > [2024/07/16 13:34:22.079 +00:00] [INFO] [split_region.go:153] ["batch split regions complete"] ["batch region ID"=2] ["first at"=74800000000000003a] ["first new region left"="{Id:48 StartKey:7480000000000000ff3400000000000000f8 EndKey:7480000000000000ff3a00000000000000f8 RegionEpoch:{ConfVer:1 Version:24} Peers:[id:49 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/16 13:34:22.079 +00:00] [INFO] [split_region.go:205] ["split regions complete"] ["region count"=1] ["region IDs"="[48]"]
   > [2024/07/16 13:34:22.079 +00:00] [INFO] [raft.rs:285] [newRaft] [peers="[(49, Progress { matched: 5, next_idx: 6, state: Probe, paused: false, pending_snapshot: 0, pending_request_snapshot: 0, recent_active: false, ins: Inflights { start: 0, count: 0, buffer: [] } })]"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=49] [region_id=48]
   > [2024/07/16 13:34:22.079 +00:00] [INFO] [cluster.go:478] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF3400000000000000F8} -> {7480000000000000FF3A00000000000000F8}, EndKey:{}"] [old-version=23] [new-version=24]
   > [2024/07/16 13:34:22.079 +00:00] [INFO] [raw_node.rs:222] ["RawNode created with id 49."] [id=49] [raft_id=49] [region_id=48]
   > [2024/07/16 13:34:22.079 +00:00] [INFO] [cluster_worker.go:218] ["region batch split, generate new regions"] [region-id=2] [origin="id:48 start_key:\"7480000000000000FF3400000000000000F8\" end_key:\"7480000000000000FF3A00000000000000F8\" region_epoch:<conf_ver:1 version:24 > peers:<id:49 store_id:1 >"] [total=1]
   > [2024/07/16 13:34:22.080 +00:00] [INFO] [raft.rs:1177] ["starting a new election"] [term=5] [raft_id=49] [region_id=48]
   > [2024/07/16 13:34:22.080 +00:00] [INFO] [raft.rs:833] ["became pre-candidate at term 5"] [term=5] [raft_id=49] [region_id=48]
   > [2024/07/16 13:34:22.080 +00:00] [INFO] [raft.rs:902] ["49 received message from 49"] [term=5] [msg=MsgRequestPreVote] [from=49] [id=49] [raft_id=49] [region_id=48]
   > [2024/07/16 13:34:22.080 +00:00] [INFO] [raft.rs:807] ["became candidate at term 6"] [term=6] [raft_id=49] [region_id=48]
   > [2024/07/16 13:34:22.080 +00:00] [INFO] [raft.rs:902] ["49 received message from 49"] [term=6] [msg=MsgRequestVote] [from=49] [id=49] [raft_id=49] [region_id=48]
   > [2024/07/16 13:34:22.080 +00:00] [INFO] [raft.rs:874] ["became leader at term 6"] [term=6] [raft_id=49] [region_id=48]
   > [2024/07/16 13:34:23.078 +00:00] [INFO] [server.go:388] ["new connection"] [conn=7] [remoteAddr=10.88.0.72:54854]
   > [2024/07/16 13:34:23.085 +00:00] [INFO] [set.go:207] ["set session var"] [conn=7] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/07/16 13:34:23.699 +00:00] [INFO] [process.rs:145] ["get snapshot failed"] [err="Request(message: \"EpochNotMatch current epoch of region 2 is conf_ver: 1 version: 24, but you sent conf_ver: 1 version: 23\" epoch_not_match { current_regions { id: 2 start_key: 7480000000000000FF3A00000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 3 store_id: 1 } } current_regions { id: 48 start_key: 7480000000000000FF3400000000000000F8 end_key: 7480000000000000FF3A00000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 49 store_id: 1 } } })"] [cid=355]
   > [2024/07/16 13:34:34.881 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=7]
