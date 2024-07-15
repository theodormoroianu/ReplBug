# Bug ID TIDB-18958-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/18958
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              Duplicate key is ignored in insert The insert statement should fail.


## Details
 * Database: tidb-v4.0.4.tikv
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
     - Instruction:  update t set c_string = 'gray mistress' where c_int = 10;
     - Transaction: conn_0
     - Output: ERROR: 1062 (23000): Duplicate entry 'gray mistress' for key 'c_string'
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #3:
     - Instruction:  insert into t values (10, 0.133544, 0.39, 'cyan fly', '2020-01-05 20:00:00', '2...
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 1 / 0
 * Instruction #4:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 0 / 0
 * Instruction #5:
     - Instruction:  select * from t where c_int = 10;
     - Transaction: conn_0
     - Output: [(10, 0.133544, Decimal('0.390000'), 'cyan fly', datetime.datetime(2020, 1, 5, 20, 0), datetime.datetime(2020, 1, 2, 14, 21, 55), 'c', {'2', '5', '1'}, '{"datetime": "2020-01-07 08:00:00", "enum": "b", "int": 18, "set": "2,3", "str": "cyan trader"}')]
     - Executed order: 4
     - Affected rows / Warnings: 1 / 0

 * Container logs:
   > [2024/07/15 13:27:18.807 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=8]
   > [2024/07/15 13:27:18.811 +00:00] [INFO] [server.go:388] ["new connection"] [conn=9] [remoteAddr=10.88.0.65:44454]
   > [2024/07/15 13:27:18.814 +00:00] [INFO] [session.go:2130] ["CRUCIAL OPERATION"] [conn=9] [schemaVersion=45] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.65]
   > [2024/07/15 13:27:18.821 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:66, Type:drop schema, State:none, SchemaState:none, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 13:27:18.81 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/15 13:27:18.821 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:66, Type:drop schema, State:none, SchemaState:none, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 13:27:18.81 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/15 13:27:18.824 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:drop schema, State:none, SchemaState:none, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 13:27:18.81 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:27:18.836 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=45] [neededSchemaVersion=46] ["start time"=373.306µs] [tblIDs="[]"]
   > [2024/07/15 13:27:18.886 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=46] ["take time"=52.250707ms] [job="ID:66, Type:drop schema, State:running, SchemaState:write only, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 13:27:18.81 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:27:18.887 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:drop schema, State:running, SchemaState:write only, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 13:27:18.81 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:27:18.898 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=46] [neededSchemaVersion=47] ["start time"=565.581µs] [tblIDs="[]"]
   > [2024/07/15 13:27:18.947 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=47] ["take time"=51.972387ms] [job="ID:66, Type:drop schema, State:running, SchemaState:delete only, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 13:27:18.81 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:27:18.949 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:drop schema, State:running, SchemaState:delete only, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 13:27:18.81 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:27:18.960 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=47] [neededSchemaVersion=48] ["start time"=388.951µs] [tblIDs="[]"]
   > [2024/07/15 13:27:19.010 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=48] ["take time"=51.939561ms] [job="ID:66, Type:drop schema, State:done, SchemaState:none, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 13:27:18.81 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:27:19.012 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=66] [jobType="drop schema"]
   > [2024/07/15 13:27:19.013 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:drop schema, State:synced, SchemaState:none, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 13:27:18.81 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:27:19.021 +00:00] [INFO] [ddl.go:509] ["[ddl] DDL job is finished"] [jobID=66]
   > [2024/07/15 13:27:19.022 +00:00] [INFO] [domain.go:624] ["performing DDL change, must reload"]
   > [2024/07/15 13:27:19.024 +00:00] [INFO] [session.go:2130] ["CRUCIAL OPERATION"] [conn=9] [schemaVersion=48] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.65]
   > [2024/07/15 13:27:19.038 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:68, Type:create schema, State:none, SchemaState:none, SchemaID:67, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-15 13:27:19.01 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/15 13:27:19.038 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:68, Type:create schema, State:none, SchemaState:none, SchemaID:67, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-15 13:27:19.01 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/15 13:27:19.040 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:68, Type:create schema, State:none, SchemaState:none, SchemaID:67, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 13:27:19.01 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:27:19.051 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=48] [neededSchemaVersion=49] ["start time"=1.199398ms] [tblIDs="[]"]
   > [2024/07/15 13:27:19.100 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=49] ["take time"=51.735901ms] [job="ID:68, Type:create schema, State:done, SchemaState:public, SchemaID:67, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-15 13:27:19.01 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:27:19.103 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:68, Type:create schema, State:synced, SchemaState:public, SchemaID:67, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 13:27:19.01 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:27:19.111 +00:00] [INFO] [ddl.go:509] ["[ddl] DDL job is finished"] [jobID=68]
   > [2024/07/15 13:27:19.111 +00:00] [INFO] [domain.go:624] ["performing DDL change, must reload"]
   > [2024/07/15 13:27:19.115 +00:00] [INFO] [session.go:2130] ["CRUCIAL OPERATION"] [conn=9] [schemaVersion=49] [cur_db=testdb] [sql="create table t (\n    c_int       int auto_increment,\n    c_double    double,\n    c_decimal   decimal(12, 6),\n    c_string    varchar(40) collate utf8_general_ci,\n    c_datetime  datetime,\n    c_timestamp timestamp,\n    c_enum      enum ('a', 'b', 'c', 'd', 'e'),\n    c_set       set ('1', '2', '3', '4', '5'),\n    c_json      json,\n    primary key (c_int),\n    unique key (c_string),\n    key (c_enum),\n    key (c_set),\n    key (c_timestamp),\n    key (c_datetime),\n    key (c_decimal)\n);"] [user=root@10.88.0.65]
   > [2024/07/15 13:27:19.129 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:70, Type:create table, State:none, SchemaState:none, SchemaID:67, TableID:69, RowCount:0, ArgLen:1, start time: 2024-07-15 13:27:19.11 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/15 13:27:19.129 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:70, Type:create table, State:none, SchemaState:none, SchemaID:67, TableID:69, RowCount:0, ArgLen:1, start time: 2024-07-15 13:27:19.11 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t (\n    c_int       int auto_increment,\n    c_double    double,\n    c_decimal   decimal(12, 6),\n    c_string    varchar(40) collate utf8_general_ci,\n    c_datetime  datetime,\n    c_timestamp timestamp,\n    c_enum      enum ('a', 'b', 'c', 'd', 'e'),\n    c_set       set ('1', '2', '3', '4', '5'),\n    c_json      json,\n    primary key (c_int),\n    unique key (c_string),\n    key (c_enum),\n    key (c_set),\n    key (c_timestamp),\n    key (c_datetime),\n    key (c_decimal)\n);"]
   > [2024/07/15 13:27:19.133 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:70, Type:create table, State:none, SchemaState:none, SchemaID:67, TableID:69, RowCount:0, ArgLen:0, start time: 2024-07-15 13:27:19.11 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:27:19.146 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=49] [neededSchemaVersion=50] ["start time"=1.81813ms] [tblIDs="[69]"]
   > [2024/07/15 13:27:19.194 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=50] ["take time"=51.67877ms] [job="ID:70, Type:create table, State:done, SchemaState:public, SchemaID:67, TableID:69, RowCount:0, ArgLen:1, start time: 2024-07-15 13:27:19.11 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:27:19.198 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:70, Type:create table, State:synced, SchemaState:public, SchemaID:67, TableID:69, RowCount:0, ArgLen:0, start time: 2024-07-15 13:27:19.11 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:27:19.206 +00:00] [INFO] [ddl.go:509] ["[ddl] DDL job is finished"] [jobID=70]
   > [2024/07/15 13:27:19.208 +00:00] [INFO] [domain.go:624] ["performing DDL change, must reload"]
   > [2024/07/15 13:27:19.208 +00:00] [INFO] [split_region.go:56] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=748000000000000045]
   > [2024/07/15 13:27:19.208 +00:00] [INFO] [peer.rs:458] ["on split"] [split_keys="key 7480000000000000FF4500000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/15 13:27:19.209 +00:00] [INFO] [cluster_worker.go:131] ["alloc ids for region split"] [region-id=52] [peer-ids="[53]"]
   > [2024/07/15 13:27:19.209 +00:00] [INFO] [pd.rs:499] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF3F00000000000000F8 region_epoch { conf_ver: 1 version: 25 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 52 new_peer_ids: 53]"] [region_id=2]
   > [2024/07/15 13:27:19.211 +00:00] [INFO] [apply.rs:1144] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF4500000000000000F8 new_region_id: 52 new_peer_ids: 53 } right_derive: true }"] [index=72] [term=6] [peer_id=3] [region_id=2]
   > [2024/07/15 13:27:19.211 +00:00] [INFO] [apply.rs:1712] ["split region"] [keys="key 7480000000000000FF4500000000000000F8"] [region="id: 2 start_key: 7480000000000000FF3F00000000000000F8 region_epoch { conf_ver: 1 version: 25 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/07/15 13:27:19.212 +00:00] [INFO] [peer.rs:1727] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/07/15 13:27:19.212 +00:00] [INFO] [peer.rs:1769] ["insert new region"] [region="id: 52 start_key: 7480000000000000FF3F00000000000000F8 end_key: 7480000000000000FF4500000000000000F8 region_epoch { conf_ver: 1 version: 26 } peers { id: 53 store_id: 1 }"] [region_id=52]
   > [2024/07/15 13:27:19.213 +00:00] [INFO] [peer.rs:158] ["create peer"] [peer_id=53] [region_id=52]
   > [2024/07/15 13:27:19.213 +00:00] [INFO] [split_region.go:153] ["batch split regions complete"] ["batch region ID"=2] ["first at"=748000000000000045] ["first new region left"="{Id:52 StartKey:7480000000000000ff3f00000000000000f8 EndKey:7480000000000000ff4500000000000000f8 RegionEpoch:{ConfVer:1 Version:26} Peers:[id:53 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/15 13:27:19.213 +00:00] [INFO] [split_region.go:205] ["split regions complete"] ["region count"=1] ["region IDs"="[52]"]
   > [2024/07/15 13:27:19.213 +00:00] [INFO] [cluster.go:478] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF3F00000000000000F8} -> {7480000000000000FF4500000000000000F8}, EndKey:{}"] [old-version=25] [new-version=26]
   > [2024/07/15 13:27:19.213 +00:00] [INFO] [cluster_worker.go:218] ["region batch split, generate new regions"] [region-id=2] [origin="id:52 start_key:\"7480000000000000FF3F00000000000000F8\" end_key:\"7480000000000000FF4500000000000000F8\" region_epoch:<conf_ver:1 version:26 > peers:<id:53 store_id:1 >"] [total=1]
   > [2024/07/15 13:27:19.214 +00:00] [INFO] [raft.rs:783] ["became follower at term 5"] [term=5] [raft_id=53] [region_id=52]
   > [2024/07/15 13:27:19.214 +00:00] [INFO] [raft.rs:285] [newRaft] [peers="[(53, Progress { matched: 5, next_idx: 6, state: Probe, paused: false, pending_snapshot: 0, pending_request_snapshot: 0, recent_active: false, ins: Inflights { start: 0, count: 0, buffer: [] } })]"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=53] [region_id=52]
   > [2024/07/15 13:27:19.214 +00:00] [INFO] [raw_node.rs:222] ["RawNode created with id 53."] [id=53] [raft_id=53] [region_id=52]
   > [2024/07/15 13:27:19.214 +00:00] [INFO] [raft.rs:1177] ["starting a new election"] [term=5] [raft_id=53] [region_id=52]
   > [2024/07/15 13:27:19.214 +00:00] [INFO] [raft.rs:833] ["became pre-candidate at term 5"] [term=5] [raft_id=53] [region_id=52]
   > [2024/07/15 13:27:19.214 +00:00] [INFO] [raft.rs:902] ["53 received message from 53"] [term=5] [msg=MsgRequestPreVote] [from=53] [id=53] [raft_id=53] [region_id=52]
   > [2024/07/15 13:27:19.214 +00:00] [INFO] [raft.rs:807] ["became candidate at term 6"] [term=6] [raft_id=53] [region_id=52]
   > [2024/07/15 13:27:19.214 +00:00] [INFO] [raft.rs:902] ["53 received message from 53"] [term=6] [msg=MsgRequestVote] [from=53] [id=53] [raft_id=53] [region_id=52]
   > [2024/07/15 13:27:19.214 +00:00] [INFO] [raft.rs:874] ["became leader at term 6"] [term=6] [raft_id=53] [region_id=52]
   > [2024/07/15 13:27:19.218 +00:00] [INFO] [process.rs:145] ["get snapshot failed"] [err="Request(message: \"EpochNotMatch current epoch of region 2 is conf_ver: 1 version: 26, but you sent conf_ver: 1 version: 25\" epoch_not_match { current_regions { id: 2 start_key: 7480000000000000FF4500000000000000F8 region_epoch { conf_ver: 1 version: 26 } peers { id: 3 store_id: 1 } } current_regions { id: 52 start_key: 7480000000000000FF3F00000000000000F8 end_key: 7480000000000000FF4500000000000000F8 region_epoch { conf_ver: 1 version: 26 } peers { id: 53 store_id: 1 } } })"] [cid=480]
   > [2024/07/15 13:27:19.229 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=9]
   > [2024/07/15 13:27:20.237 +00:00] [INFO] [server.go:388] ["new connection"] [conn=10] [remoteAddr=10.88.0.65:44464]
   > [2024/07/15 13:27:20.245 +00:00] [INFO] [set.go:207] ["set session var"] [conn=10] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/07/15 13:27:20.848 +00:00] [ERROR] [conn.go:730] ["command dispatched failed"] [conn=10] [connInfo="id:10, addr:10.88.0.65:44464 status:11, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:1, autocommit:1"] [sql=" update t set c_string = 'gray mistress' where c_int = 10;"] [txn_mode=PESSIMISTIC] [err="[kv:1062]Duplicate entry 'gray mistress' for key 'c_string'"]
   > [2024/07/15 13:27:32.041 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=10]

### Scenario 1
 * Instruction #0:
     - Instruction:  update t set c_string = 'gray mistress' where c_int = 10;
     - Transaction: conn_0
     - Output: ERROR: 1062 (23000): Duplicate entry 'gray mistress' for key 'c_string'
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #1:
     - Instruction:  insert into t values (10, 0.133544, 0.39, 'cyan fly', '2020-01-05 20:00:00', '2...
     - Transaction: conn_0
     - Output: ERROR: 3140 (22032): Invalid JSON text: The document root must not be followed by other values.
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #2:
     - Instruction:  select * from t where c_int = 10;
     - Transaction: conn_0
     - Output: [(10, 0.277686, Decimal('24.880000'), 'black cat', datetime.datetime(2020, 1, 6, 14, 0), datetime.datetime(2020, 1, 6, 3, 57, 43), 'd', {'3', '1'}, '{"datetime": "2020-01-06 10:00:00", "enum": "c", "int": 6, "set": "2", "str": "gray carpet"}')]
     - Executed order: 0
     - Affected rows / Warnings: 1 / 0

 * Container logs:
   > [2024/07/15 13:27:33.461 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=11]
   > [2024/07/15 13:27:33.463 +00:00] [INFO] [server.go:388] ["new connection"] [conn=12] [remoteAddr=10.88.0.65:56072]
   > [2024/07/15 13:27:33.465 +00:00] [INFO] [session.go:2130] ["CRUCIAL OPERATION"] [conn=12] [schemaVersion=58] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.65]
   > [2024/07/15 13:27:33.480 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:77, Type:drop schema, State:none, SchemaState:none, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 13:27:33.46 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/15 13:27:33.480 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:77, Type:drop schema, State:none, SchemaState:none, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 13:27:33.46 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/15 13:27:33.483 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:none, SchemaState:none, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 13:27:33.46 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:27:33.493 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=58] [neededSchemaVersion=59] ["start time"=389.928µs] [tblIDs="[]"]
   > [2024/07/15 13:27:33.543 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=59] ["take time"=52.00605ms] [job="ID:77, Type:drop schema, State:running, SchemaState:write only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 13:27:33.46 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:27:33.545 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:running, SchemaState:write only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 13:27:33.46 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:27:33.555 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=59] [neededSchemaVersion=60] ["start time"=449.295µs] [tblIDs="[]"]
   > [2024/07/15 13:27:33.605 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=60] ["take time"=52.148807ms] [job="ID:77, Type:drop schema, State:running, SchemaState:delete only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 13:27:33.46 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:27:33.607 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:running, SchemaState:delete only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 13:27:33.46 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:27:33.622 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=60] [neededSchemaVersion=61] ["start time"=1.00845ms] [tblIDs="[]"]
   > [2024/07/15 13:27:33.671 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=61] ["take time"=53.450944ms] [job="ID:77, Type:drop schema, State:done, SchemaState:none, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 13:27:33.46 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:27:33.673 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=77] [jobType="drop schema"]
   > [2024/07/15 13:27:33.675 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:synced, SchemaState:none, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 13:27:33.46 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:27:33.684 +00:00] [INFO] [ddl.go:509] ["[ddl] DDL job is finished"] [jobID=77]
   > [2024/07/15 13:27:33.684 +00:00] [INFO] [domain.go:624] ["performing DDL change, must reload"]
   > [2024/07/15 13:27:33.685 +00:00] [INFO] [session.go:2130] ["CRUCIAL OPERATION"] [conn=12] [schemaVersion=61] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.65]
   > [2024/07/15 13:27:33.698 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:79, Type:create schema, State:none, SchemaState:none, SchemaID:78, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-15 13:27:33.66 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/15 13:27:33.698 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:79, Type:create schema, State:none, SchemaState:none, SchemaID:78, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-15 13:27:33.66 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/15 13:27:33.701 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:79, Type:create schema, State:none, SchemaState:none, SchemaID:78, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 13:27:33.66 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:27:33.711 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=61] [neededSchemaVersion=62] ["start time"=1.364086ms] [tblIDs="[]"]
   > [2024/07/15 13:27:33.759 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=62] ["take time"=51.480279ms] [job="ID:79, Type:create schema, State:done, SchemaState:public, SchemaID:78, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-15 13:27:33.66 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:27:33.762 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:79, Type:create schema, State:synced, SchemaState:public, SchemaID:78, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 13:27:33.66 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:27:33.770 +00:00] [INFO] [ddl.go:509] ["[ddl] DDL job is finished"] [jobID=79]
   > [2024/07/15 13:27:33.770 +00:00] [INFO] [domain.go:624] ["performing DDL change, must reload"]
   > [2024/07/15 13:27:33.772 +00:00] [INFO] [session.go:2130] ["CRUCIAL OPERATION"] [conn=12] [schemaVersion=62] [cur_db=testdb] [sql="create table t (\n    c_int       int auto_increment,\n    c_double    double,\n    c_decimal   decimal(12, 6),\n    c_string    varchar(40) collate utf8_general_ci,\n    c_datetime  datetime,\n    c_timestamp timestamp,\n    c_enum      enum ('a', 'b', 'c', 'd', 'e'),\n    c_set       set ('1', '2', '3', '4', '5'),\n    c_json      json,\n    primary key (c_int),\n    unique key (c_string),\n    key (c_enum),\n    key (c_set),\n    key (c_timestamp),\n    key (c_datetime),\n    key (c_decimal)\n);"] [user=root@10.88.0.65]
   > [2024/07/15 13:27:33.786 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:81, Type:create table, State:none, SchemaState:none, SchemaID:78, TableID:80, RowCount:0, ArgLen:1, start time: 2024-07-15 13:27:33.76 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/15 13:27:33.786 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:81, Type:create table, State:none, SchemaState:none, SchemaID:78, TableID:80, RowCount:0, ArgLen:1, start time: 2024-07-15 13:27:33.76 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t (\n    c_int       int auto_increment,\n    c_double    double,\n    c_decimal   decimal(12, 6),\n    c_string    varchar(40) collate utf8_general_ci,\n    c_datetime  datetime,\n    c_timestamp timestamp,\n    c_enum      enum ('a', 'b', 'c', 'd', 'e'),\n    c_set       set ('1', '2', '3', '4', '5'),\n    c_json      json,\n    primary key (c_int),\n    unique key (c_string),\n    key (c_enum),\n    key (c_set),\n    key (c_timestamp),\n    key (c_datetime),\n    key (c_decimal)\n);"]
   > [2024/07/15 13:27:33.789 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:81, Type:create table, State:none, SchemaState:none, SchemaID:78, TableID:80, RowCount:0, ArgLen:0, start time: 2024-07-15 13:27:33.76 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:27:33.809 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=62] [neededSchemaVersion=63] ["start time"=2.0924ms] [tblIDs="[80]"]
   > [2024/07/15 13:27:33.857 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=63] ["take time"=51.893255ms] [job="ID:81, Type:create table, State:done, SchemaState:public, SchemaID:78, TableID:80, RowCount:0, ArgLen:1, start time: 2024-07-15 13:27:33.76 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:27:33.861 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:81, Type:create table, State:synced, SchemaState:public, SchemaID:78, TableID:80, RowCount:0, ArgLen:0, start time: 2024-07-15 13:27:33.76 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:27:33.870 +00:00] [INFO] [ddl.go:509] ["[ddl] DDL job is finished"] [jobID=81]
   > [2024/07/15 13:27:33.871 +00:00] [INFO] [domain.go:624] ["performing DDL change, must reload"]
   > [2024/07/15 13:27:33.871 +00:00] [INFO] [split_region.go:56] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=748000000000000050]
   > [2024/07/15 13:27:33.872 +00:00] [INFO] [peer.rs:458] ["on split"] [split_keys="key 7480000000000000FF5000000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/15 13:27:33.872 +00:00] [INFO] [cluster_worker.go:131] ["alloc ids for region split"] [region-id=56] [peer-ids="[57]"]
   > [2024/07/15 13:27:33.872 +00:00] [INFO] [pd.rs:499] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF4A00000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 56 new_peer_ids: 57]"] [region_id=2]
   > [2024/07/15 13:27:33.874 +00:00] [INFO] [apply.rs:1144] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF5000000000000000F8 new_region_id: 56 new_peer_ids: 57 } right_derive: true }"] [index=83] [term=6] [peer_id=3] [region_id=2]
   > [2024/07/15 13:27:33.874 +00:00] [INFO] [apply.rs:1712] ["split region"] [keys="key 7480000000000000FF5000000000000000F8"] [region="id: 2 start_key: 7480000000000000FF4A00000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/07/15 13:27:33.876 +00:00] [INFO] [peer.rs:1727] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/07/15 13:27:33.876 +00:00] [INFO] [peer.rs:1769] ["insert new region"] [region="id: 56 start_key: 7480000000000000FF4A00000000000000F8 end_key: 7480000000000000FF5000000000000000F8 region_epoch { conf_ver: 1 version: 28 } peers { id: 57 store_id: 1 }"] [region_id=56]
   > [2024/07/15 13:27:33.876 +00:00] [INFO] [split_region.go:153] ["batch split regions complete"] ["batch region ID"=2] ["first at"=748000000000000050] ["first new region left"="{Id:56 StartKey:7480000000000000ff4a00000000000000f8 EndKey:7480000000000000ff5000000000000000f8 RegionEpoch:{ConfVer:1 Version:28} Peers:[id:57 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/15 13:27:33.877 +00:00] [INFO] [split_region.go:205] ["split regions complete"] ["region count"=1] ["region IDs"="[56]"]
   > [2024/07/15 13:27:33.877 +00:00] [INFO] [peer.rs:158] ["create peer"] [peer_id=57] [region_id=56]
   > [2024/07/15 13:27:33.877 +00:00] [INFO] [cluster.go:478] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF4A00000000000000F8} -> {7480000000000000FF5000000000000000F8}, EndKey:{}"] [old-version=27] [new-version=28]
   > [2024/07/15 13:27:33.877 +00:00] [INFO] [cluster_worker.go:218] ["region batch split, generate new regions"] [region-id=2] [origin="id:56 start_key:\"7480000000000000FF4A00000000000000F8\" end_key:\"7480000000000000FF5000000000000000F8\" region_epoch:<conf_ver:1 version:28 > peers:<id:57 store_id:1 >"] [total=1]
   > [2024/07/15 13:27:33.878 +00:00] [INFO] [raft.rs:783] ["became follower at term 5"] [term=5] [raft_id=57] [region_id=56]
   > [2024/07/15 13:27:33.878 +00:00] [INFO] [raft.rs:285] [newRaft] [peers="[(57, Progress { matched: 5, next_idx: 6, state: Probe, paused: false, pending_snapshot: 0, pending_request_snapshot: 0, recent_active: false, ins: Inflights { start: 0, count: 0, buffer: [] } })]"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=57] [region_id=56]
   > [2024/07/15 13:27:33.878 +00:00] [INFO] [raw_node.rs:222] ["RawNode created with id 57."] [id=57] [raft_id=57] [region_id=56]
   > [2024/07/15 13:27:33.878 +00:00] [INFO] [raft.rs:1177] ["starting a new election"] [term=5] [raft_id=57] [region_id=56]
   > [2024/07/15 13:27:33.878 +00:00] [INFO] [raft.rs:833] ["became pre-candidate at term 5"] [term=5] [raft_id=57] [region_id=56]
   > [2024/07/15 13:27:33.878 +00:00] [INFO] [raft.rs:902] ["57 received message from 57"] [term=5] [msg=MsgRequestPreVote] [from=57] [id=57] [raft_id=57] [region_id=56]
   > [2024/07/15 13:27:33.878 +00:00] [INFO] [raft.rs:807] ["became candidate at term 6"] [term=6] [raft_id=57] [region_id=56]
   > [2024/07/15 13:27:33.879 +00:00] [INFO] [raft.rs:902] ["57 received message from 57"] [term=6] [msg=MsgRequestVote] [from=57] [id=57] [raft_id=57] [region_id=56]
   > [2024/07/15 13:27:33.879 +00:00] [INFO] [raft.rs:874] ["became leader at term 6"] [term=6] [raft_id=57] [region_id=56]
   > [2024/07/15 13:27:33.882 +00:00] [INFO] [process.rs:145] ["get snapshot failed"] [err="Request(message: \"EpochNotMatch current epoch of region 2 is conf_ver: 1 version: 28, but you sent conf_ver: 1 version: 27\" epoch_not_match { current_regions { id: 2 start_key: 7480000000000000FF5000000000000000F8 region_epoch { conf_ver: 1 version: 28 } peers { id: 3 store_id: 1 } } current_regions { id: 56 start_key: 7480000000000000FF4A00000000000000F8 end_key: 7480000000000000FF5000000000000000F8 region_epoch { conf_ver: 1 version: 28 } peers { id: 57 store_id: 1 } } })"] [cid=594]
   > [2024/07/15 13:27:33.893 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=12]
   > [2024/07/15 13:27:34.902 +00:00] [INFO] [server.go:388] ["new connection"] [conn=13] [remoteAddr=10.88.0.65:56076]
   > [2024/07/15 13:27:34.909 +00:00] [INFO] [set.go:207] ["set session var"] [conn=13] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/07/15 13:27:34.911 +00:00] [INFO] [tidb.go:199] ["rollbackTxn for ddl/autocommit failed"]
   > [2024/07/15 13:27:34.911 +00:00] [ERROR] [conn.go:730] ["command dispatched failed"] [conn=13] [connInfo="id:13, addr:10.88.0.65:56076 status:10, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:0, autocommit:1"] [sql=" update t set c_string = 'gray mistress' where c_int = 10;"] [txn_mode=PESSIMISTIC] [err="[kv:1062]Duplicate entry 'gray mistress' for key 'c_string'"]
   > [2024/07/15 13:27:35.201 +00:00] [INFO] [tidb.go:199] ["rollbackTxn for ddl/autocommit failed"]
   > [2024/07/15 13:27:35.201 +00:00] [WARN] [session.go:1041] ["run statement failed"] [conn=13] [schemaVersion=63] [error="[json:3140]Invalid JSON text: The document root must not be followed by other values."] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 13,\n  \"status\": 2,\n  \"strictMode\": true,\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"10.88.0.65\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/07/15 13:27:35.202 +00:00] [ERROR] [conn.go:730] ["command dispatched failed"] [conn=13] [connInfo="id:13, addr:10.88.0.65:56076 status:10, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:0, autocommit:1"] [sql=" insert into t values (10, 0.133544, 0.39, 'cyan fly', '2020-01-05 20:00:00', '2020-01-02 14:21:55', 'c', '1,2,5', '{{\"int\":18,\"str\":\"cyan trader\",\"datetime\":\"2020-01-07 08:00:00\",\"enum\":\"b\",\"set\":\"2,3\"}}');"] [txn_mode=PESSIMISTIC] [err="[json:3140]Invalid JSON text: The document root must not be followed by other values.\ngithub.com/pingcap/errors.AddStack\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.20190809092503-95897b64e011/errors.go:174\ngithub.com/pingcap/parser/terror.(*Error).GenWithStackByArgs\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/pkg/mod/github.com/pingcap/parser@v0.0.0-20200623164729-3a18f1e5dceb/terror/terror.go:243\ngithub.com/pingcap/tidb/types/json.ParseBinaryFromString\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/src/github.com/pingcap/tidb/types/json/binary.go:380\ngithub.com/pingcap/tidb/types.(*Datum).convertToMysqlJSON\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/src/github.com/pingcap/tidb/types/datum.go:1395\ngithub.com/pingcap/tidb/types.(*Datum).ConvertTo\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/src/github.com/pingcap/tidb/types/datum.go:816\ngithub.com/pingcap/tidb/table.CastValue\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/src/github.com/pingcap/tidb/table/column.go:179\ngithub.com/pingcap/tidb/executor.(*InsertValues).fastEvalRow\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/src/github.com/pingcap/tidb/executor/insert_common.go:353\ngithub.com/pingcap/tidb/executor.insertRows\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/src/github.com/pingcap/tidb/executor/insert_common.go:224\ngithub.com/pingcap/tidb/executor.(*InsertExec).Next\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/src/github.com/pingcap/tidb/executor/insert.go:262\ngithub.com/pingcap/tidb/executor.Next\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/src/github.com/pingcap/tidb/executor/executor.go:249\ngithub.com/pingcap/tidb/executor.(*ExecStmt).handleNoDelayExecutor\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/src/github.com/pingcap/tidb/executor/adapter.go:499\ngithub.com/pingcap/tidb/executor.(*ExecStmt).handleNoDelay\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/src/github.com/pingcap/tidb/executor/adapter.go:381\ngithub.com/pingcap/tidb/executor.(*ExecStmt).Exec\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/src/github.com/pingcap/tidb/executor/adapter.go:349\ngithub.com/pingcap/tidb/session.runStmt\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/src/github.com/pingcap/tidb/session/tidb.go:276\ngithub.com/pingcap/tidb/session.(*session).executeStatement\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/src/github.com/pingcap/tidb/session/session.go:1038\ngithub.com/pingcap/tidb/session.(*session).execute\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/src/github.com/pingcap/tidb/session/session.go:1150\ngithub.com/pingcap/tidb/session.(*session).Execute\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/src/github.com/pingcap/tidb/session/session.go:1081\ngithub.com/pingcap/tidb/server.(*TiDBContext).Execute\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/src/github.com/pingcap/tidb/server/driver_tidb.go:248\ngithub.com/pingcap/tidb/server.(*clientConn).handleQuery\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/src/github.com/pingcap/tidb/server/conn.go:1272\ngithub.com/pingcap/tidb/server.(*clientConn).dispatch\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/src/github.com/pingcap/tidb/server/conn.go:906\ngithub.com/pingcap/tidb/server.(*clientConn).Run\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/src/github.com/pingcap/tidb/server/conn.go:715\ngithub.com/pingcap/tidb/server.(*Server).onConn\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/src/github.com/pingcap/tidb/server/server.go:415\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1357"]
   > [2024/07/15 13:27:45.804 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=13]
