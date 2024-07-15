# Bug ID TIDB-18958-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/18958
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              Duplicate key is ignored in insert The insert statement should fail.


## Details
 * Database: tidb-v4.0.4.tikv
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
   > [2024/07/15 13:26:50.644 +00:00] [INFO] [server.go:388] ["new connection"] [conn=2] [remoteAddr=10.88.0.65:45236]
   > [2024/07/15 13:26:50.646 +00:00] [INFO] [session.go:2130] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=22] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.65]
   > [2024/07/15 13:26:50.647 +00:00] [INFO] [session.go:2130] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=22] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.65]
   > [2024/07/15 13:26:50.669 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-15 13:26:50.61 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/15 13:26:50.669 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-15 13:26:50.61 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/15 13:26:50.672 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 13:26:50.61 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:26:50.687 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=22] [neededSchemaVersion=23] ["start time"=814.01µs] [tblIDs="[]"]
   > [2024/07/15 13:26:50.736 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=23] ["take time"=51.861966ms] [job="ID:46, Type:create schema, State:done, SchemaState:public, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-15 13:26:50.61 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:26:50.739 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:46, Type:create schema, State:synced, SchemaState:public, SchemaID:45, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 13:26:50.61 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:26:50.751 +00:00] [INFO] [ddl.go:509] ["[ddl] DDL job is finished"] [jobID=46]
   > [2024/07/15 13:26:50.751 +00:00] [INFO] [domain.go:624] ["performing DDL change, must reload"]
   > [2024/07/15 13:26:50.755 +00:00] [INFO] [session.go:2130] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=23] [cur_db=testdb] [sql="create table t (\n    c_int       int auto_increment,\n    c_double    double,\n    c_decimal   decimal(12, 6),\n    c_string    varchar(40) collate utf8_general_ci,\n    c_datetime  datetime,\n    c_timestamp timestamp,\n    c_enum      enum ('a', 'b', 'c', 'd', 'e'),\n    c_set       set ('1', '2', '3', '4', '5'),\n    c_json      json,\n    primary key (c_int),\n    unique key (c_string),\n    key (c_enum),\n    key (c_set),\n    key (c_timestamp),\n    key (c_datetime),\n    key (c_decimal)\n);"] [user=root@10.88.0.65]
   > [2024/07/15 13:26:50.780 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-07-15 13:26:50.76 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/15 13:26:50.780 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-07-15 13:26:50.76 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t (\n    c_int       int auto_increment,\n    c_double    double,\n    c_decimal   decimal(12, 6),\n    c_string    varchar(40) collate utf8_general_ci,\n    c_datetime  datetime,\n    c_timestamp timestamp,\n    c_enum      enum ('a', 'b', 'c', 'd', 'e'),\n    c_set       set ('1', '2', '3', '4', '5'),\n    c_json      json,\n    primary key (c_int),\n    unique key (c_string),\n    key (c_enum),\n    key (c_set),\n    key (c_timestamp),\n    key (c_datetime),\n    key (c_decimal)\n);"]
   > [2024/07/15 13:26:50.783 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-15 13:26:50.76 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:26:50.806 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=23] [neededSchemaVersion=24] ["start time"=1.354518ms] [tblIDs="[47]"]
   > [2024/07/15 13:26:50.856 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=24] ["take time"=52.000532ms] [job="ID:48, Type:create table, State:done, SchemaState:public, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-07-15 13:26:50.76 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:26:50.860 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:48, Type:create table, State:synced, SchemaState:public, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-15 13:26:50.76 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:26:50.876 +00:00] [INFO] [ddl.go:509] ["[ddl] DDL job is finished"] [jobID=48]
   > [2024/07/15 13:26:50.878 +00:00] [INFO] [domain.go:624] ["performing DDL change, must reload"]
   > [2024/07/15 13:26:50.878 +00:00] [INFO] [split_region.go:56] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=74800000000000002f]
   > [2024/07/15 13:26:50.879 +00:00] [INFO] [peer.rs:458] ["on split"] [split_keys="key 7480000000000000FF2F00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/15 13:26:50.879 +00:00] [INFO] [cluster_worker.go:131] ["alloc ids for region split"] [region-id=44] [peer-ids="[45]"]
   > [2024/07/15 13:26:50.879 +00:00] [INFO] [pd.rs:499] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF2B00000000000000F8 region_epoch { conf_ver: 1 version: 21 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 44 new_peer_ids: 45]"] [region_id=2]
   > [2024/07/15 13:26:50.886 +00:00] [INFO] [apply.rs:1144] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF2F00000000000000F8 new_region_id: 44 new_peer_ids: 45 } right_derive: true }"] [index=53] [term=6] [peer_id=3] [region_id=2]
   > [2024/07/15 13:26:50.887 +00:00] [INFO] [apply.rs:1712] ["split region"] [keys="key 7480000000000000FF2F00000000000000F8"] [region="id: 2 start_key: 7480000000000000FF2B00000000000000F8 region_epoch { conf_ver: 1 version: 21 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/07/15 13:26:50.893 +00:00] [INFO] [peer.rs:1727] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/07/15 13:26:50.893 +00:00] [INFO] [peer.rs:1769] ["insert new region"] [region="id: 44 start_key: 7480000000000000FF2B00000000000000F8 end_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 45 store_id: 1 }"] [region_id=44]
   > [2024/07/15 13:26:50.893 +00:00] [INFO] [peer.rs:158] ["create peer"] [peer_id=45] [region_id=44]
   > [2024/07/15 13:26:50.893 +00:00] [INFO] [split_region.go:153] ["batch split regions complete"] ["batch region ID"=2] ["first at"=74800000000000002f] ["first new region left"="{Id:44 StartKey:7480000000000000ff2b00000000000000f8 EndKey:7480000000000000ff2f00000000000000f8 RegionEpoch:{ConfVer:1 Version:22} Peers:[id:45 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/15 13:26:50.894 +00:00] [INFO] [split_region.go:205] ["split regions complete"] ["region count"=1] ["region IDs"="[44]"]
   > [2024/07/15 13:26:50.894 +00:00] [INFO] [cluster.go:478] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF2B00000000000000F8} -> {7480000000000000FF2F00000000000000F8}, EndKey:{}"] [old-version=21] [new-version=22]
   > [2024/07/15 13:26:50.894 +00:00] [INFO] [cluster_worker.go:218] ["region batch split, generate new regions"] [region-id=2] [origin="id:44 start_key:\"7480000000000000FF2B00000000000000F8\" end_key:\"7480000000000000FF2F00000000000000F8\" region_epoch:<conf_ver:1 version:22 > peers:<id:45 store_id:1 >"] [total=1]
   > [2024/07/15 13:26:50.896 +00:00] [INFO] [raft.rs:783] ["became follower at term 5"] [term=5] [raft_id=45] [region_id=44]
   > [2024/07/15 13:26:50.897 +00:00] [INFO] [raft.rs:285] [newRaft] [peers="[(45, Progress { matched: 5, next_idx: 6, state: Probe, paused: false, pending_snapshot: 0, pending_request_snapshot: 0, recent_active: false, ins: Inflights { start: 0, count: 0, buffer: [] } })]"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=45] [region_id=44]
   > [2024/07/15 13:26:50.897 +00:00] [INFO] [raw_node.rs:222] ["RawNode created with id 45."] [id=45] [raft_id=45] [region_id=44]
   > [2024/07/15 13:26:50.897 +00:00] [INFO] [raft.rs:1177] ["starting a new election"] [term=5] [raft_id=45] [region_id=44]
   > [2024/07/15 13:26:50.897 +00:00] [INFO] [raft.rs:833] ["became pre-candidate at term 5"] [term=5] [raft_id=45] [region_id=44]
   > [2024/07/15 13:26:50.897 +00:00] [INFO] [raft.rs:902] ["45 received message from 45"] [term=5] [msg=MsgRequestPreVote] [from=45] [id=45] [raft_id=45] [region_id=44]
   > [2024/07/15 13:26:50.897 +00:00] [INFO] [raft.rs:807] ["became candidate at term 6"] [term=6] [raft_id=45] [region_id=44]
   > [2024/07/15 13:26:50.897 +00:00] [INFO] [raft.rs:902] ["45 received message from 45"] [term=6] [msg=MsgRequestVote] [from=45] [id=45] [raft_id=45] [region_id=44]
   > [2024/07/15 13:26:50.898 +00:00] [INFO] [raft.rs:874] ["became leader at term 6"] [term=6] [raft_id=45] [region_id=44]
   > [2024/07/15 13:26:50.907 +00:00] [INFO] [process.rs:145] ["get snapshot failed"] [err="Request(message: \"EpochNotMatch current epoch of region 2 is conf_ver: 1 version: 22, but you sent conf_ver: 1 version: 21\" epoch_not_match { current_regions { id: 2 start_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 3 store_id: 1 } } current_regions { id: 44 start_key: 7480000000000000FF2B00000000000000F8 end_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 45 store_id: 1 } } })"] [cid=261]
   > [2024/07/15 13:26:50.933 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=2]
   > [2024/07/15 13:26:51.957 +00:00] [INFO] [server.go:388] ["new connection"] [conn=4] [remoteAddr=10.88.0.65:45242]
   > [2024/07/15 13:26:51.960 +00:00] [INFO] [set.go:207] ["set session var"] [conn=4] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/07/15 13:26:52.572 +00:00] [ERROR] [conn.go:730] ["command dispatched failed"] [conn=4] [connInfo="id:4, addr:10.88.0.65:45242 status:11, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:1, autocommit:1"] [sql=" update t set c_string = 'gray mistress' where c_int = 10;"] [txn_mode=PESSIMISTIC] [err="[kv:1062]Duplicate entry 'gray mistress' for key 'c_string'"]
   > [2024/07/15 13:27:03.764 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=4]

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
   > [2024/07/15 13:27:05.100 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=5]
   > [2024/07/15 13:27:05.102 +00:00] [INFO] [server.go:388] ["new connection"] [conn=6] [remoteAddr=10.88.0.65:41584]
   > [2024/07/15 13:27:05.104 +00:00] [INFO] [session.go:2130] ["CRUCIAL OPERATION"] [conn=6] [schemaVersion=32] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.65]
   > [2024/07/15 13:27:05.112 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:55, Type:drop schema, State:none, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 13:27:05.06 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/15 13:27:05.112 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:55, Type:drop schema, State:none, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 13:27:05.06 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/15 13:27:05.114 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:55, Type:drop schema, State:none, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 13:27:05.06 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:27:05.124 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=32] [neededSchemaVersion=33] ["start time"=581.295µs] [tblIDs="[]"]
   > [2024/07/15 13:27:05.174 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=33] ["take time"=51.681704ms] [job="ID:55, Type:drop schema, State:running, SchemaState:write only, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 13:27:05.06 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:27:05.175 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:55, Type:drop schema, State:running, SchemaState:write only, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 13:27:05.06 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:27:05.186 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=33] [neededSchemaVersion=34] ["start time"=607.836µs] [tblIDs="[]"]
   > [2024/07/15 13:27:05.235 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=34] ["take time"=51.878309ms] [job="ID:55, Type:drop schema, State:running, SchemaState:delete only, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 13:27:05.06 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:27:05.237 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:55, Type:drop schema, State:running, SchemaState:delete only, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 13:27:05.06 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:27:05.250 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=34] [neededSchemaVersion=35] ["start time"=414.233µs] [tblIDs="[]"]
   > [2024/07/15 13:27:05.300 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=35] ["take time"=51.901077ms] [job="ID:55, Type:drop schema, State:done, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 13:27:05.06 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:27:05.302 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=55] [jobType="drop schema"]
   > [2024/07/15 13:27:05.304 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:55, Type:drop schema, State:synced, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 13:27:05.06 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:27:05.313 +00:00] [INFO] [ddl.go:509] ["[ddl] DDL job is finished"] [jobID=55]
   > [2024/07/15 13:27:05.313 +00:00] [INFO] [domain.go:624] ["performing DDL change, must reload"]
   > [2024/07/15 13:27:05.315 +00:00] [INFO] [session.go:2130] ["CRUCIAL OPERATION"] [conn=6] [schemaVersion=35] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.65]
   > [2024/07/15 13:27:05.328 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:57, Type:create schema, State:none, SchemaState:none, SchemaID:56, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-15 13:27:05.31 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/15 13:27:05.328 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:57, Type:create schema, State:none, SchemaState:none, SchemaID:56, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-15 13:27:05.31 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/15 13:27:05.330 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:57, Type:create schema, State:none, SchemaState:none, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 13:27:05.31 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:27:05.341 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=35] [neededSchemaVersion=36] ["start time"=947.408µs] [tblIDs="[]"]
   > [2024/07/15 13:27:05.390 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=36] ["take time"=51.644617ms] [job="ID:57, Type:create schema, State:done, SchemaState:public, SchemaID:56, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-15 13:27:05.31 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:27:05.393 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:57, Type:create schema, State:synced, SchemaState:public, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 13:27:05.31 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:27:05.403 +00:00] [INFO] [ddl.go:509] ["[ddl] DDL job is finished"] [jobID=57]
   > [2024/07/15 13:27:05.403 +00:00] [INFO] [domain.go:624] ["performing DDL change, must reload"]
   > [2024/07/15 13:27:05.406 +00:00] [INFO] [session.go:2130] ["CRUCIAL OPERATION"] [conn=6] [schemaVersion=36] [cur_db=testdb] [sql="create table t (\n    c_int       int auto_increment,\n    c_double    double,\n    c_decimal   decimal(12, 6),\n    c_string    varchar(40) collate utf8_general_ci,\n    c_datetime  datetime,\n    c_timestamp timestamp,\n    c_enum      enum ('a', 'b', 'c', 'd', 'e'),\n    c_set       set ('1', '2', '3', '4', '5'),\n    c_json      json,\n    primary key (c_int),\n    unique key (c_string),\n    key (c_enum),\n    key (c_set),\n    key (c_timestamp),\n    key (c_datetime),\n    key (c_decimal)\n);"] [user=root@10.88.0.65]
   > [2024/07/15 13:27:05.424 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:59, Type:create table, State:none, SchemaState:none, SchemaID:56, TableID:58, RowCount:0, ArgLen:1, start time: 2024-07-15 13:27:05.41 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/15 13:27:05.424 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:59, Type:create table, State:none, SchemaState:none, SchemaID:56, TableID:58, RowCount:0, ArgLen:1, start time: 2024-07-15 13:27:05.41 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t (\n    c_int       int auto_increment,\n    c_double    double,\n    c_decimal   decimal(12, 6),\n    c_string    varchar(40) collate utf8_general_ci,\n    c_datetime  datetime,\n    c_timestamp timestamp,\n    c_enum      enum ('a', 'b', 'c', 'd', 'e'),\n    c_set       set ('1', '2', '3', '4', '5'),\n    c_json      json,\n    primary key (c_int),\n    unique key (c_string),\n    key (c_enum),\n    key (c_set),\n    key (c_timestamp),\n    key (c_datetime),\n    key (c_decimal)\n);"]
   > [2024/07/15 13:27:05.426 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:59, Type:create table, State:none, SchemaState:none, SchemaID:56, TableID:58, RowCount:0, ArgLen:0, start time: 2024-07-15 13:27:05.41 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:27:05.441 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=36] [neededSchemaVersion=37] ["start time"=1.454462ms] [tblIDs="[58]"]
   > [2024/07/15 13:27:05.490 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=37] ["take time"=51.623175ms] [job="ID:59, Type:create table, State:done, SchemaState:public, SchemaID:56, TableID:58, RowCount:0, ArgLen:1, start time: 2024-07-15 13:27:05.41 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:27:05.494 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:59, Type:create table, State:synced, SchemaState:public, SchemaID:56, TableID:58, RowCount:0, ArgLen:0, start time: 2024-07-15 13:27:05.41 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 13:27:05.500 +00:00] [INFO] [ddl.go:509] ["[ddl] DDL job is finished"] [jobID=59]
   > [2024/07/15 13:27:05.501 +00:00] [INFO] [domain.go:624] ["performing DDL change, must reload"]
   > [2024/07/15 13:27:05.502 +00:00] [INFO] [split_region.go:56] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=74800000000000003a]
   > [2024/07/15 13:27:05.502 +00:00] [INFO] [peer.rs:458] ["on split"] [split_keys="key 7480000000000000FF3A00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/15 13:27:05.502 +00:00] [INFO] [cluster_worker.go:131] ["alloc ids for region split"] [region-id=48] [peer-ids="[49]"]
   > [2024/07/15 13:27:05.503 +00:00] [INFO] [pd.rs:499] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF3400000000000000F8 region_epoch { conf_ver: 1 version: 23 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 48 new_peer_ids: 49]"] [region_id=2]
   > [2024/07/15 13:27:05.504 +00:00] [INFO] [apply.rs:1144] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF3A00000000000000F8 new_region_id: 48 new_peer_ids: 49 } right_derive: true }"] [index=65] [term=6] [peer_id=3] [region_id=2]
   > [2024/07/15 13:27:05.505 +00:00] [INFO] [apply.rs:1712] ["split region"] [keys="key 7480000000000000FF3A00000000000000F8"] [region="id: 2 start_key: 7480000000000000FF3400000000000000F8 region_epoch { conf_ver: 1 version: 23 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/07/15 13:27:05.506 +00:00] [INFO] [peer.rs:1727] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/07/15 13:27:05.506 +00:00] [INFO] [peer.rs:1769] ["insert new region"] [region="id: 48 start_key: 7480000000000000FF3400000000000000F8 end_key: 7480000000000000FF3A00000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 49 store_id: 1 }"] [region_id=48]
   > [2024/07/15 13:27:05.506 +00:00] [INFO] [split_region.go:153] ["batch split regions complete"] ["batch region ID"=2] ["first at"=74800000000000003a] ["first new region left"="{Id:48 StartKey:7480000000000000ff3400000000000000f8 EndKey:7480000000000000ff3a00000000000000f8 RegionEpoch:{ConfVer:1 Version:24} Peers:[id:49 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/15 13:27:05.506 +00:00] [INFO] [split_region.go:205] ["split regions complete"] ["region count"=1] ["region IDs"="[48]"]
   > [2024/07/15 13:27:05.506 +00:00] [INFO] [peer.rs:158] ["create peer"] [peer_id=49] [region_id=48]
   > [2024/07/15 13:27:05.506 +00:00] [INFO] [cluster.go:478] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF3400000000000000F8} -> {7480000000000000FF3A00000000000000F8}, EndKey:{}"] [old-version=23] [new-version=24]
   > [2024/07/15 13:27:05.506 +00:00] [INFO] [raft.rs:783] ["became follower at term 5"] [term=5] [raft_id=49] [region_id=48]
   > [2024/07/15 13:27:05.506 +00:00] [INFO] [raft.rs:285] [newRaft] [peers="[(49, Progress { matched: 5, next_idx: 6, state: Probe, paused: false, pending_snapshot: 0, pending_request_snapshot: 0, recent_active: false, ins: Inflights { start: 0, count: 0, buffer: [] } })]"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=49] [region_id=48]
   > [2024/07/15 13:27:05.506 +00:00] [INFO] [raw_node.rs:222] ["RawNode created with id 49."] [id=49] [raft_id=49] [region_id=48]
   > [2024/07/15 13:27:05.506 +00:00] [INFO] [cluster_worker.go:218] ["region batch split, generate new regions"] [region-id=2] [origin="id:48 start_key:\"7480000000000000FF3400000000000000F8\" end_key:\"7480000000000000FF3A00000000000000F8\" region_epoch:<conf_ver:1 version:24 > peers:<id:49 store_id:1 >"] [total=1]
   > [2024/07/15 13:27:05.507 +00:00] [INFO] [raft.rs:1177] ["starting a new election"] [term=5] [raft_id=49] [region_id=48]
   > [2024/07/15 13:27:05.507 +00:00] [INFO] [raft.rs:833] ["became pre-candidate at term 5"] [term=5] [raft_id=49] [region_id=48]
   > [2024/07/15 13:27:05.507 +00:00] [INFO] [raft.rs:902] ["49 received message from 49"] [term=5] [msg=MsgRequestPreVote] [from=49] [id=49] [raft_id=49] [region_id=48]
   > [2024/07/15 13:27:05.507 +00:00] [INFO] [raft.rs:807] ["became candidate at term 6"] [term=6] [raft_id=49] [region_id=48]
   > [2024/07/15 13:27:05.507 +00:00] [INFO] [raft.rs:902] ["49 received message from 49"] [term=6] [msg=MsgRequestVote] [from=49] [id=49] [raft_id=49] [region_id=48]
   > [2024/07/15 13:27:05.507 +00:00] [INFO] [raft.rs:874] ["became leader at term 6"] [term=6] [raft_id=49] [region_id=48]
   > [2024/07/15 13:27:05.512 +00:00] [INFO] [process.rs:145] ["get snapshot failed"] [err="Request(message: \"EpochNotMatch current epoch of region 2 is conf_ver: 1 version: 24, but you sent conf_ver: 1 version: 23\" epoch_not_match { current_regions { id: 2 start_key: 7480000000000000FF3A00000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 3 store_id: 1 } } current_regions { id: 48 start_key: 7480000000000000FF3400000000000000F8 end_key: 7480000000000000FF3A00000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 49 store_id: 1 } } })"] [cid=376]
   > [2024/07/15 13:27:05.523 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=6]
   > [2024/07/15 13:27:06.534 +00:00] [INFO] [server.go:388] ["new connection"] [conn=7] [remoteAddr=10.88.0.65:41598]
   > [2024/07/15 13:27:06.540 +00:00] [INFO] [set.go:207] ["set session var"] [conn=7] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/07/15 13:27:06.542 +00:00] [INFO] [tidb.go:199] ["rollbackTxn for ddl/autocommit failed"]
   > [2024/07/15 13:27:06.543 +00:00] [ERROR] [conn.go:730] ["command dispatched failed"] [conn=7] [connInfo="id:7, addr:10.88.0.65:41598 status:10, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:0, autocommit:1"] [sql=" update t set c_string = 'gray mistress' where c_int = 10;"] [txn_mode=PESSIMISTIC] [err="[kv:1062]Duplicate entry 'gray mistress' for key 'c_string'"]
   > [2024/07/15 13:27:06.833 +00:00] [INFO] [tidb.go:199] ["rollbackTxn for ddl/autocommit failed"]
   > [2024/07/15 13:27:06.833 +00:00] [WARN] [session.go:1041] ["run statement failed"] [conn=7] [schemaVersion=37] [error="[json:3140]Invalid JSON text: The document root must not be followed by other values."] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 7,\n  \"status\": 2,\n  \"strictMode\": true,\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"10.88.0.65\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/07/15 13:27:06.833 +00:00] [ERROR] [conn.go:730] ["command dispatched failed"] [conn=7] [connInfo="id:7, addr:10.88.0.65:41598 status:10, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:0, autocommit:1"] [sql=" insert into t values (10, 0.133544, 0.39, 'cyan fly', '2020-01-05 20:00:00', '2020-01-02 14:21:55', 'c', '1,2,5', '{{\"int\":18,\"str\":\"cyan trader\",\"datetime\":\"2020-01-07 08:00:00\",\"enum\":\"b\",\"set\":\"2,3\"}}');"] [txn_mode=PESSIMISTIC] [err="[json:3140]Invalid JSON text: The document root must not be followed by other values.\ngithub.com/pingcap/errors.AddStack\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.20190809092503-95897b64e011/errors.go:174\ngithub.com/pingcap/parser/terror.(*Error).GenWithStackByArgs\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/pkg/mod/github.com/pingcap/parser@v0.0.0-20200623164729-3a18f1e5dceb/terror/terror.go:243\ngithub.com/pingcap/tidb/types/json.ParseBinaryFromString\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/src/github.com/pingcap/tidb/types/json/binary.go:380\ngithub.com/pingcap/tidb/types.(*Datum).convertToMysqlJSON\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/src/github.com/pingcap/tidb/types/datum.go:1395\ngithub.com/pingcap/tidb/types.(*Datum).ConvertTo\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/src/github.com/pingcap/tidb/types/datum.go:816\ngithub.com/pingcap/tidb/table.CastValue\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/src/github.com/pingcap/tidb/table/column.go:179\ngithub.com/pingcap/tidb/executor.(*InsertValues).fastEvalRow\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/src/github.com/pingcap/tidb/executor/insert_common.go:353\ngithub.com/pingcap/tidb/executor.insertRows\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/src/github.com/pingcap/tidb/executor/insert_common.go:224\ngithub.com/pingcap/tidb/executor.(*InsertExec).Next\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/src/github.com/pingcap/tidb/executor/insert.go:262\ngithub.com/pingcap/tidb/executor.Next\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/src/github.com/pingcap/tidb/executor/executor.go:249\ngithub.com/pingcap/tidb/executor.(*ExecStmt).handleNoDelayExecutor\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/src/github.com/pingcap/tidb/executor/adapter.go:499\ngithub.com/pingcap/tidb/executor.(*ExecStmt).handleNoDelay\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/src/github.com/pingcap/tidb/executor/adapter.go:381\ngithub.com/pingcap/tidb/executor.(*ExecStmt).Exec\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/src/github.com/pingcap/tidb/executor/adapter.go:349\ngithub.com/pingcap/tidb/session.runStmt\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/src/github.com/pingcap/tidb/session/tidb.go:276\ngithub.com/pingcap/tidb/session.(*session).executeStatement\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/src/github.com/pingcap/tidb/session/session.go:1038\ngithub.com/pingcap/tidb/session.(*session).execute\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/src/github.com/pingcap/tidb/session/session.go:1150\ngithub.com/pingcap/tidb/session.(*session).Execute\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/src/github.com/pingcap/tidb/session/session.go:1081\ngithub.com/pingcap/tidb/server.(*TiDBContext).Execute\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/src/github.com/pingcap/tidb/server/driver_tidb.go:248\ngithub.com/pingcap/tidb/server.(*clientConn).handleQuery\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/src/github.com/pingcap/tidb/server/conn.go:1272\ngithub.com/pingcap/tidb/server.(*clientConn).dispatch\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/src/github.com/pingcap/tidb/server/conn.go:906\ngithub.com/pingcap/tidb/server.(*clientConn).Run\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/src/github.com/pingcap/tidb/server/conn.go:715\ngithub.com/pingcap/tidb/server.(*Server).onConn\n\t/home/jenkins/agent/workspace/tidb_v4.0.4/go/src/github.com/pingcap/tidb/server/server.go:415\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1357"]
   > [2024/07/15 13:27:17.436 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=7]
