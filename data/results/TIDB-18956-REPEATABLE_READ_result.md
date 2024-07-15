# Bug ID TIDB-18956-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/18956
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              Delete should not report any error.


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
     - Instruction:  update t set c_decimal = c_decimal + 5 where c_decimal <= 20;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 6 / 0
 * Instruction #3:
     - Instruction:  insert into t values (5, 0.157960, 67.26, 'brown cat', '2019-12-28 15:00:00', '...
     - Transaction: conn_0
     - Output: ERROR: 1062 (23000): Duplicate entry 'brown cat' for key 'c_string'
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #4:
     - Instruction:  delete from t where c_int = 5;
     - Transaction: conn_0
     - Output: ERROR: 1062 (23000): Duplicate entry '5' for key 'PRIMARY'
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #5:
     - Instruction:  rollback;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 0 / 0

 * Container logs:
   > [2024/07/15 13:14:23.470 +00:00] [INFO] [server.go:388] ["new connection"] [conn=2] [remoteAddr=10.88.0.63:40434]
   > [2024/07/15 13:14:23.473 +00:00] [INFO] [session.go:2130] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=22] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.63]
   > [2024/07/15 13:14:23.474 +00:00] [INFO] [session.go:2130] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=22] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.63]
   > [2024/07/15 13:14:23.511 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-15 13:14:23.481 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/15 13:14:23.511 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-15 13:14:23.481 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/15 13:14:23.515 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 13:14:23.481 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:14:23.534 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=22] [neededSchemaVersion=23] ["start time"=1.144643ms] [tblIDs="[]"]
   > [2024/07/15 13:14:23.583 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=23] ["take time"=52.150486ms] [job="ID:46, Type:create schema, State:done, SchemaState:public, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-15 13:14:23.481 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:14:23.586 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:46, Type:create schema, State:synced, SchemaState:public, SchemaID:45, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 13:14:23.481 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:14:23.603 +00:00] [INFO] [ddl.go:509] ["[ddl] DDL job is finished"] [jobID=46]
   > [2024/07/15 13:14:23.603 +00:00] [INFO] [domain.go:624] ["performing DDL change, must reload"]
   > [2024/07/15 13:14:23.606 +00:00] [INFO] [session.go:2130] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=23] [cur_db=testdb] [sql="create table t (\n    c_int       int,\n    c_double    double,\n    c_decimal   decimal(12, 6),\n    c_string    varchar(40),\n    c_datetime  datetime,\n    c_timestamp timestamp,\n    c_enum      enum ('a', 'b', 'c', 'd', 'e'),\n    c_set       set ('1', '2', '3', '4', '5'),\n    c_json      json,\n    primary key (c_int),\n    unique key (c_string),\n    key (c_enum),\n    key (c_set),\n    key (c_timestamp),\n    key (c_datetime),\n    key (c_decimal)\n);"] [user=root@10.88.0.63]
   > [2024/07/15 13:14:23.640 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-07-15 13:14:23.581 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/15 13:14:23.640 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-07-15 13:14:23.581 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t (\n    c_int       int,\n    c_double    double,\n    c_decimal   decimal(12, 6),\n    c_string    varchar(40),\n    c_datetime  datetime,\n    c_timestamp timestamp,\n    c_enum      enum ('a', 'b', 'c', 'd', 'e'),\n    c_set       set ('1', '2', '3', '4', '5'),\n    c_json      json,\n    primary key (c_int),\n    unique key (c_string),\n    key (c_enum),\n    key (c_set),\n    key (c_timestamp),\n    key (c_datetime),\n    key (c_decimal)\n);"]
   > [2024/07/15 13:14:23.643 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-15 13:14:23.581 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:14:23.682 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=23] [neededSchemaVersion=24] ["start time"=2.850397ms] [tblIDs="[47]"]
   > [2024/07/15 13:14:23.731 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=24] ["take time"=53.838292ms] [job="ID:48, Type:create table, State:done, SchemaState:public, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-07-15 13:14:23.581 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:14:23.734 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:48, Type:create table, State:synced, SchemaState:public, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-15 13:14:23.581 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:14:23.754 +00:00] [INFO] [ddl.go:509] ["[ddl] DDL job is finished"] [jobID=48]
   > [2024/07/15 13:14:23.755 +00:00] [INFO] [domain.go:624] ["performing DDL change, must reload"]
   > [2024/07/15 13:14:23.755 +00:00] [INFO] [split_region.go:56] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=74800000000000002f]
   > [2024/07/15 13:14:23.756 +00:00] [INFO] [peer.rs:458] ["on split"] [split_keys="key 7480000000000000FF2F00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/15 13:14:23.756 +00:00] [INFO] [cluster_worker.go:131] ["alloc ids for region split"] [region-id=44] [peer-ids="[45]"]
   > [2024/07/15 13:14:23.756 +00:00] [INFO] [pd.rs:499] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF2B00000000000000F8 region_epoch { conf_ver: 1 version: 21 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 44 new_peer_ids: 45]"] [region_id=2]
   > [2024/07/15 13:14:23.763 +00:00] [INFO] [apply.rs:1144] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF2F00000000000000F8 new_region_id: 44 new_peer_ids: 45 } right_derive: true }"] [index=53] [term=6] [peer_id=3] [region_id=2]
   > [2024/07/15 13:14:23.763 +00:00] [INFO] [apply.rs:1712] ["split region"] [keys="key 7480000000000000FF2F00000000000000F8"] [region="id: 2 start_key: 7480000000000000FF2B00000000000000F8 region_epoch { conf_ver: 1 version: 21 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/07/15 13:14:23.774 +00:00] [INFO] [split_region.go:153] ["batch split regions complete"] ["batch region ID"=2] ["first at"=74800000000000002f] ["first new region left"="{Id:44 StartKey:7480000000000000ff2b00000000000000f8 EndKey:7480000000000000ff2f00000000000000f8 RegionEpoch:{ConfVer:1 Version:22} Peers:[id:45 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/15 13:14:23.774 +00:00] [INFO] [split_region.go:205] ["split regions complete"] ["region count"=1] ["region IDs"="[44]"]
   > [2024/07/15 13:14:23.778 +00:00] [INFO] [peer.rs:1727] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/07/15 13:14:23.779 +00:00] [INFO] [peer.rs:1769] ["insert new region"] [region="id: 44 start_key: 7480000000000000FF2B00000000000000F8 end_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 45 store_id: 1 }"] [region_id=44]
   > [2024/07/15 13:14:23.779 +00:00] [INFO] [peer.rs:158] ["create peer"] [peer_id=45] [region_id=44]
   > [2024/07/15 13:14:23.779 +00:00] [INFO] [cluster.go:478] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF2B00000000000000F8} -> {7480000000000000FF2F00000000000000F8}, EndKey:{}"] [old-version=21] [new-version=22]
   > [2024/07/15 13:14:23.780 +00:00] [INFO] [cluster_worker.go:218] ["region batch split, generate new regions"] [region-id=2] [origin="id:44 start_key:\"7480000000000000FF2B00000000000000F8\" end_key:\"7480000000000000FF2F00000000000000F8\" region_epoch:<conf_ver:1 version:22 > peers:<id:45 store_id:1 >"] [total=1]
   > [2024/07/15 13:14:23.784 +00:00] [INFO] [raft.rs:783] ["became follower at term 5"] [term=5] [raft_id=45] [region_id=44]
   > [2024/07/15 13:14:23.784 +00:00] [INFO] [raft.rs:285] [newRaft] [peers="[(45, Progress { matched: 5, next_idx: 6, state: Probe, paused: false, pending_snapshot: 0, pending_request_snapshot: 0, recent_active: false, ins: Inflights { start: 0, count: 0, buffer: [] } })]"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=45] [region_id=44]
   > [2024/07/15 13:14:23.784 +00:00] [INFO] [raw_node.rs:222] ["RawNode created with id 45."] [id=45] [raft_id=45] [region_id=44]
   > [2024/07/15 13:14:23.784 +00:00] [INFO] [raft.rs:1177] ["starting a new election"] [term=5] [raft_id=45] [region_id=44]
   > [2024/07/15 13:14:23.784 +00:00] [INFO] [raft.rs:833] ["became pre-candidate at term 5"] [term=5] [raft_id=45] [region_id=44]
   > [2024/07/15 13:14:23.784 +00:00] [INFO] [raft.rs:902] ["45 received message from 45"] [term=5] [msg=MsgRequestPreVote] [from=45] [id=45] [raft_id=45] [region_id=44]
   > [2024/07/15 13:14:23.784 +00:00] [INFO] [raft.rs:807] ["became candidate at term 6"] [term=6] [raft_id=45] [region_id=44]
   > [2024/07/15 13:14:23.785 +00:00] [INFO] [raft.rs:902] ["45 received message from 45"] [term=6] [msg=MsgRequestVote] [from=45] [id=45] [raft_id=45] [region_id=44]
   > [2024/07/15 13:14:23.785 +00:00] [INFO] [raft.rs:874] ["became leader at term 6"] [term=6] [raft_id=45] [region_id=44]
   > [2024/07/15 13:14:23.805 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=2]
   > [2024/07/15 13:14:24.823 +00:00] [INFO] [server.go:388] ["new connection"] [conn=3] [remoteAddr=10.88.0.63:40442]
   > [2024/07/15 13:14:24.825 +00:00] [INFO] [set.go:207] ["set session var"] [conn=3] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/07/15 13:14:25.723 +00:00] [ERROR] [conn.go:730] ["command dispatched failed"] [conn=3] [connInfo="id:3, addr:10.88.0.63:40442 status:11, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:1, autocommit:1"] [sql=" insert into t values (5, 0.157960, 67.26, 'brown cat', '2019-12-28 15:00:00', '2020-01-07 07:22:43', 'c', '1', '{\"int\":13,\"str\":\"ivory vulture\",\"datetime\":\"2019-12-31 05:00:00\",\"enum\":\"b\",\"set\":\"3,5\"}');"] [txn_mode=PESSIMISTIC] [err="[kv:1062]Duplicate entry 'brown cat' for key 'c_string'"]
   > [2024/07/15 13:14:26.024 +00:00] [ERROR] [conn.go:730] ["command dispatched failed"] [conn=3] [connInfo="id:3, addr:10.88.0.63:40442 status:11, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:1, autocommit:1"] [sql=" delete from t where c_int = 5;"] [txn_mode=PESSIMISTIC] [err="[kv:1062]Duplicate entry '5' for key 'PRIMARY'"]
   > [2024/07/15 13:14:36.626 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=3]
