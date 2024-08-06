# Bug ID TIDB-27156-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/27156
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              Playing with lock_wait_timeout and txn_mode makes the same commit succeed / fail.


## Details
 * Database: tidb-v5.2.0-alpha-26237b35.tikv
 * Number of scenarios: 1
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows: 0
 * Instruction #1:
     - Instruction:  set autocommit = 0;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows: 0
 * Instruction #2:
     - Instruction:  set innodb_lock_wait_timeout = 0;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows: 0
     - Warnings: [('Warning', 1292, "Truncated incorrect innodb_lock_wait_timeout value: '0'")]
 * Instruction #3:
     - Instruction:  set tidb_txn_mode = pessimistic;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows: 0
 * Instruction #4:
     - Instruction:  set autocommit = 0;
     - Transaction: conn_1
     - Output: None
     - Executed order: 4
     - Affected rows: 0
 * Instruction #5:
     - Instruction:  set innodb_lock_wait_timeout = 0;
     - Transaction: conn_1
     - Output: None
     - Executed order: 5
     - Affected rows: 0
     - Warnings: [('Warning', 1292, "Truncated incorrect innodb_lock_wait_timeout value: '0'")]
 * Instruction #6:
     - Instruction:  set tidb_txn_mode = pessimistic;
     - Transaction: conn_1
     - Output: None
     - Executed order: 6
     - Affected rows: 0
 * Instruction #7:
     - Instruction:  set autocommit = 0;
     - Transaction: conn_2
     - Output: None
     - Executed order: 7
     - Affected rows: 0
 * Instruction #8:
     - Instruction:  set tidb_txn_mode = optimistic;
     - Transaction: conn_2
     - Output: None
     - Executed order: 8
     - Affected rows: 0
 * Instruction #9:
     - Instruction:  select * from t2 where c4 > 2 for update;
     - Transaction: conn_0
     - Output: [(4, 4, 4, 4), (3, 3, 3, 3)]
     - Executed order: 9
     - Affected rows: 2
 * Instruction #10:
     - Instruction:  insert into t2 values(5,5,5,5);
     - Transaction: conn_1
     - Output: None
     - Executed order: 10
     - Affected rows: 1
 * Instruction #11:
     - Instruction:  update t2 set c4 = c4 + 1 where c3 = 3;
     - Transaction: conn_1
     - Output: None
     - Executed order: 13
     - Affected rows: 1
 * Instruction #12:
     - Instruction:  select c1, c3 from t2 where c3 = 4 for update nowait;
     - Transaction: conn_1
     - Output: [(4, 4)]
     - Executed order: 14
     - Affected rows: 1
 * Instruction #13:
     - Instruction:  update t2 set c4 = c4 * 10 where c4 = 4;
     - Transaction: conn_2
     - Output: None
     - Executed order: 11
     - Affected rows: 0
 * Instruction #14:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: None
     - Executed order: 12
     - Affected rows: 0
 * Instruction #15:
     - Instruction:  commit;
     - Transaction: conn_2
     - Output: None
     - Executed order: 15
     - Affected rows: 0

 * Container logs:
   > [2024/08/06 12:14:04.941 +00:00] [INFO] [session.go:2945] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=36] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/08/06 12:14:04.952 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:73, Type:drop schema, State:none, SchemaState:queueing, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-06 12:14:04.919 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/06 12:14:04.952 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:73, Type:drop schema, State:none, SchemaState:queueing, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-06 12:14:04.919 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/08/06 12:14:04.956 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:73, Type:drop schema, State:none, SchemaState:queueing, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-06 12:14:04.919 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 12:14:04.973 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=36] [neededSchemaVersion=37] ["start time"=782.44µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/06 12:14:05.022 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=37] ["take time"=52.57326ms] [job="ID:73, Type:drop schema, State:running, SchemaState:write only, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-06 12:14:04.919 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 12:14:05.024 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:73, Type:drop schema, State:running, SchemaState:write only, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-06 12:14:04.919 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 12:14:05.039 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=37] [neededSchemaVersion=38] ["start time"=720.63µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/06 12:14:05.089 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=38] ["take time"=52.926521ms] [job="ID:73, Type:drop schema, State:running, SchemaState:delete only, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-06 12:14:04.919 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 12:14:05.091 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:73, Type:drop schema, State:running, SchemaState:delete only, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-06 12:14:04.919 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 12:14:05.107 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=38] [neededSchemaVersion=39] ["start time"=771.405µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/06 12:14:05.156 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=39] ["take time"=52.366108ms] [job="ID:73, Type:drop schema, State:done, SchemaState:queueing, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-06 12:14:04.919 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 12:14:05.159 +00:00] [INFO] [delete_range.go:106] ["[ddl] add job into delete-range table"] [jobID=73] [jobType="drop schema"]
   > [2024/08/06 12:14:05.160 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:73, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-06 12:14:04.919 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 12:14:05.171 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=73]
   > [2024/08/06 12:14:05.171 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/08/06 12:14:05.173 +00:00] [INFO] [session.go:2945] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=39] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/08/06 12:14:05.192 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:75, Type:create schema, State:none, SchemaState:queueing, SchemaID:74, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-06 12:14:05.168 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/06 12:14:05.192 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:75, Type:create schema, State:none, SchemaState:queueing, SchemaID:74, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-06 12:14:05.168 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/08/06 12:14:05.197 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:75, Type:create schema, State:none, SchemaState:queueing, SchemaID:74, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-06 12:14:05.168 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 12:14:05.212 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=39] [neededSchemaVersion=40] ["start time"=1.336638ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/06 12:14:05.261 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=40] ["take time"=52.459767ms] [job="ID:75, Type:create schema, State:done, SchemaState:public, SchemaID:74, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-06 12:14:05.168 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 12:14:05.265 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:75, Type:create schema, State:synced, SchemaState:public, SchemaID:74, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-06 12:14:05.168 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 12:14:05.275 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=75]
   > [2024/08/06 12:14:05.275 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/08/06 12:14:05.278 +00:00] [INFO] [session.go:2945] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=40] [cur_db=testdb] [sql="create table t2(c1 int primary key, c2 int, c3 int, c4 int, key k2(c2), key k3(c3)) partition by hash(c1) partitions 10;"] [user=root@127.0.0.1]
   > [2024/08/06 12:14:05.302 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:87, Type:create table, State:none, SchemaState:queueing, SchemaID:74, TableID:76, RowCount:0, ArgLen:1, start time: 2024-08-06 12:14:05.268 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/06 12:14:05.302 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:87, Type:create table, State:none, SchemaState:queueing, SchemaID:74, TableID:76, RowCount:0, ArgLen:1, start time: 2024-08-06 12:14:05.268 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t2(c1 int primary key, c2 int, c3 int, c4 int, key k2(c2), key k3(c3)) partition by hash(c1) partitions 10;"]
   > [2024/08/06 12:14:05.306 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:87, Type:create table, State:none, SchemaState:queueing, SchemaID:74, TableID:76, RowCount:0, ArgLen:0, start time: 2024-08-06 12:14:05.268 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 12:14:05.333 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=40] [neededSchemaVersion=41] ["start time"=7.062569ms] [phyTblIDs="[76,77,78,79,80,81,82,83,84,85,86]"] [actionTypes="[8,8,8,8,8,8,8,8,8,8,8]"]
   > [2024/08/06 12:14:05.377 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=41] ["take time"=52.521018ms] [job="ID:87, Type:create table, State:done, SchemaState:public, SchemaID:74, TableID:76, RowCount:0, ArgLen:1, start time: 2024-08-06 12:14:05.268 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 12:14:05.381 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:87, Type:create table, State:synced, SchemaState:public, SchemaID:74, TableID:76, RowCount:0, ArgLen:0, start time: 2024-08-06 12:14:05.268 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 12:14:05.393 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=87]
   > [2024/08/06 12:14:05.394 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/08/06 12:14:05.394 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=74800000000000004d]
   > [2024/08/06 12:14:05.394 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56014] [split_keys="key 7480000000000000FF4D00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.395 +00:00] [INFO] [cluster_worker.go:127] ["alloc ids for region split"] [region-id=74] [peer-ids="[75]"]
   > [2024/08/06 12:14:05.395 +00:00] [INFO] [pd.rs:749] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF4600000000000000F8 region_epoch { conf_ver: 1 version: 36 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 74 new_peer_ids: 75]"] [region_id=2]
   > [2024/08/06 12:14:05.399 +00:00] [INFO] [apply.rs:1394] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF4D00000000000000F8 new_region_id: 74 new_peer_ids: 75 } right_derive: true }"] [index=75] [term=6] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.399 +00:00] [INFO] [apply.rs:2242] ["split region"] [keys="key 7480000000000000FF4D00000000000000F8"] [region="id: 2 start_key: 7480000000000000FF4600000000000000F8 region_epoch { conf_ver: 1 version: 36 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.403 +00:00] [INFO] [endpoint.rs:158] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/08/06 12:14:05.403 +00:00] [INFO] [peer.rs:2411] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.403 +00:00] [INFO] [peer.rs:2476] ["insert new region"] [region="id: 74 start_key: 7480000000000000FF4600000000000000F8 end_key: 7480000000000000FF4D00000000000000F8 region_epoch { conf_ver: 1 version: 37 } peers { id: 75 store_id: 1 }"] [region_id=74]
   > [2024/08/06 12:14:05.403 +00:00] [INFO] [peer.rs:219] ["create peer"] [peer_id=75] [region_id=74]
   > [2024/08/06 12:14:05.403 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=2] ["first at"=74800000000000004d] ["first new region left"="{Id:74 StartKey:7480000000000000ff4600000000000000f8 EndKey:7480000000000000ff4d00000000000000f8 RegionEpoch:{ConfVer:1 Version:37} Peers:[id:75 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/08/06 12:14:05.403 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[74]"]
   > [2024/08/06 12:14:05.403 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=74800000000000004e]
   > [2024/08/06 12:14:05.403 +00:00] [INFO] [region.go:505] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF4600000000000000F8} -> {7480000000000000FF4D00000000000000F8}, EndKey:{}"] [old-version=36] [new-version=37]
   > [2024/08/06 12:14:05.403 +00:00] [INFO] [cluster_worker.go:219] ["region batch split, generate new regions"] [region-id=2] [origin="id:74 start_key:\"7480000000000000FF4600000000000000F8\" end_key:\"7480000000000000FF4D00000000000000F8\" region_epoch:<conf_ver:1 version:37 > peers:<id:75 store_id:1 >"] [total=1]
   > [2024/08/06 12:14:05.405 +00:00] [INFO] [raft.rs:2609] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {75} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=75] [region_id=74]
   > [2024/08/06 12:14:05.405 +00:00] [INFO] [raft.rs:1092] ["became follower at term 5"] [term=5] [raft_id=75] [region_id=74]
   > [2024/08/06 12:14:05.405 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {75} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=75] [region_id=74]
   > [2024/08/06 12:14:05.405 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 75."] [id=75] [raft_id=75] [region_id=74]
   > [2024/08/06 12:14:05.405 +00:00] [INFO] [raft.rs:1517] ["starting a new election"] [term=5] [raft_id=75] [region_id=74]
   > [2024/08/06 12:14:05.405 +00:00] [INFO] [raft.rs:1142] ["became pre-candidate at term 5"] [term=5] [raft_id=75] [region_id=74]
   > [2024/08/06 12:14:05.405 +00:00] [INFO] [raft.rs:1116] ["became candidate at term 6"] [term=6] [raft_id=75] [region_id=74]
   > [2024/08/06 12:14:05.406 +00:00] [INFO] [raft.rs:1200] ["became leader at term 6"] [term=6] [raft_id=75] [region_id=74]
   > [2024/08/06 12:14:05.406 +00:00] [INFO] [peer.rs:3778] ["require updating max ts"] [initial_status=25769803850] [region_id=74]
   > [2024/08/06 12:14:05.406 +00:00] [INFO] [endpoint.rs:382] ["deregister observe region"] [observe_id=ObserveID(69)] [region_id=2] [store_id=Some(1)]
   > [2024/08/06 12:14:05.406 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF4D00000000000000F8 region_epoch { conf_ver: 1 version: 37 } peers { id: 3 store_id: 1 }"]
   > [2024/08/06 12:14:05.406 +00:00] [INFO] [pd.rs:1246] ["succeed to update max timestamp"] [region_id=74]
   > [2024/08/06 12:14:05.409 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56024] [split_keys="key 7480000000000000FF4E00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.409 +00:00] [INFO] [peer.rs:3911] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 36"] [prev_epoch="conf_ver: 1 version: 37"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.409 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=75] [observe_id=ObserveID(71)] [region=2]
   > [2024/08/06 12:14:05.411 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 74 start_key: 7480000000000000FF4600000000000000F8 end_key: 7480000000000000FF4D00000000000000F8 region_epoch { conf_ver: 1 version: 37 } peers { id: 75 store_id: 1 }"]
   > [2024/08/06 12:14:05.413 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveID(72)] [region=74]
   > [2024/08/06 12:14:05.415 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56032] [split_keys="key 7480000000000000FF4E00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.416 +00:00] [INFO] [cluster_worker.go:127] ["alloc ids for region split"] [region-id=76] [peer-ids="[77]"]
   > [2024/08/06 12:14:05.416 +00:00] [INFO] [pd.rs:749] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF4D00000000000000F8 region_epoch { conf_ver: 1 version: 37 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 76 new_peer_ids: 77]"] [region_id=2]
   > [2024/08/06 12:14:05.420 +00:00] [INFO] [apply.rs:1394] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF4E00000000000000F8 new_region_id: 76 new_peer_ids: 77 } right_derive: true }"] [index=77] [term=6] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.420 +00:00] [INFO] [apply.rs:2242] ["split region"] [keys="key 7480000000000000FF4E00000000000000F8"] [region="id: 2 start_key: 7480000000000000FF4D00000000000000F8 region_epoch { conf_ver: 1 version: 37 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.423 +00:00] [INFO] [endpoint.rs:158] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/08/06 12:14:05.423 +00:00] [INFO] [peer.rs:2411] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.423 +00:00] [INFO] [peer.rs:2476] ["insert new region"] [region="id: 76 start_key: 7480000000000000FF4D00000000000000F8 end_key: 7480000000000000FF4E00000000000000F8 region_epoch { conf_ver: 1 version: 38 } peers { id: 77 store_id: 1 }"] [region_id=76]
   > [2024/08/06 12:14:05.423 +00:00] [INFO] [peer.rs:219] ["create peer"] [peer_id=77] [region_id=76]
   > [2024/08/06 12:14:05.424 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=2] ["first at"=74800000000000004e] ["first new region left"="{Id:76 StartKey:7480000000000000ff4d00000000000000f8 EndKey:7480000000000000ff4e00000000000000f8 RegionEpoch:{ConfVer:1 Version:38} Peers:[id:77 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/08/06 12:14:05.424 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[76]"]
   > [2024/08/06 12:14:05.424 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=74800000000000004f]
   > [2024/08/06 12:14:05.424 +00:00] [INFO] [region.go:505] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF4D00000000000000F8} -> {7480000000000000FF4E00000000000000F8}, EndKey:{}"] [old-version=37] [new-version=38]
   > [2024/08/06 12:14:05.424 +00:00] [INFO] [cluster_worker.go:219] ["region batch split, generate new regions"] [region-id=2] [origin="id:76 start_key:\"7480000000000000FF4D00000000000000F8\" end_key:\"7480000000000000FF4E00000000000000F8\" region_epoch:<conf_ver:1 version:38 > peers:<id:77 store_id:1 >"] [total=1]
   > [2024/08/06 12:14:05.425 +00:00] [INFO] [raft.rs:2609] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {77} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=77] [region_id=76]
   > [2024/08/06 12:14:05.425 +00:00] [INFO] [raft.rs:1092] ["became follower at term 5"] [term=5] [raft_id=77] [region_id=76]
   > [2024/08/06 12:14:05.425 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {77} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=77] [region_id=76]
   > [2024/08/06 12:14:05.425 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 77."] [id=77] [raft_id=77] [region_id=76]
   > [2024/08/06 12:14:05.425 +00:00] [INFO] [raft.rs:1517] ["starting a new election"] [term=5] [raft_id=77] [region_id=76]
   > [2024/08/06 12:14:05.425 +00:00] [INFO] [raft.rs:1142] ["became pre-candidate at term 5"] [term=5] [raft_id=77] [region_id=76]
   > [2024/08/06 12:14:05.425 +00:00] [INFO] [raft.rs:1116] ["became candidate at term 6"] [term=6] [raft_id=77] [region_id=76]
   > [2024/08/06 12:14:05.425 +00:00] [INFO] [raft.rs:1200] ["became leader at term 6"] [term=6] [raft_id=77] [region_id=76]
   > [2024/08/06 12:14:05.426 +00:00] [INFO] [endpoint.rs:382] ["deregister observe region"] [observe_id=ObserveID(71)] [region_id=2] [store_id=Some(1)]
   > [2024/08/06 12:14:05.426 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF4E00000000000000F8 region_epoch { conf_ver: 1 version: 38 } peers { id: 3 store_id: 1 }"]
   > [2024/08/06 12:14:05.426 +00:00] [INFO] [peer.rs:3778] ["require updating max ts"] [initial_status=25769803852] [region_id=76]
   > [2024/08/06 12:14:05.426 +00:00] [INFO] [pd.rs:1246] ["succeed to update max timestamp"] [region_id=76]
   > [2024/08/06 12:14:05.430 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56000] [split_keys="key 7480000000000000FF4F00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.430 +00:00] [INFO] [peer.rs:3911] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 37"] [prev_epoch="conf_ver: 1 version: 38"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.430 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 76 start_key: 7480000000000000FF4D00000000000000F8 end_key: 7480000000000000FF4E00000000000000F8 region_epoch { conf_ver: 1 version: 38 } peers { id: 77 store_id: 1 }"]
   > [2024/08/06 12:14:05.430 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=77] [observe_id=ObserveID(73)] [region=2]
   > [2024/08/06 12:14:05.430 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveID(74)] [region=76]
   > [2024/08/06 12:14:05.433 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56014] [split_keys="key 7480000000000000FF4F00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.433 +00:00] [INFO] [cluster_worker.go:127] ["alloc ids for region split"] [region-id=78] [peer-ids="[79]"]
   > [2024/08/06 12:14:05.434 +00:00] [INFO] [pd.rs:749] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF4E00000000000000F8 region_epoch { conf_ver: 1 version: 38 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 78 new_peer_ids: 79]"] [region_id=2]
   > [2024/08/06 12:14:05.440 +00:00] [INFO] [apply.rs:1394] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF4F00000000000000F8 new_region_id: 78 new_peer_ids: 79 } right_derive: true }"] [index=78] [term=6] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.440 +00:00] [INFO] [apply.rs:2242] ["split region"] [keys="key 7480000000000000FF4F00000000000000F8"] [region="id: 2 start_key: 7480000000000000FF4E00000000000000F8 region_epoch { conf_ver: 1 version: 38 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.443 +00:00] [INFO] [endpoint.rs:158] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/08/06 12:14:05.444 +00:00] [INFO] [peer.rs:2411] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.444 +00:00] [INFO] [peer.rs:2476] ["insert new region"] [region="id: 78 start_key: 7480000000000000FF4E00000000000000F8 end_key: 7480000000000000FF4F00000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 79 store_id: 1 }"] [region_id=78]
   > [2024/08/06 12:14:05.444 +00:00] [INFO] [peer.rs:219] ["create peer"] [peer_id=79] [region_id=78]
   > [2024/08/06 12:14:05.444 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=2] ["first at"=74800000000000004f] ["first new region left"="{Id:78 StartKey:7480000000000000ff4e00000000000000f8 EndKey:7480000000000000ff4f00000000000000f8 RegionEpoch:{ConfVer:1 Version:39} Peers:[id:79 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/08/06 12:14:05.444 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[78]"]
   > [2024/08/06 12:14:05.444 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=748000000000000050]
   > [2024/08/06 12:14:05.444 +00:00] [INFO] [region.go:505] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF4E00000000000000F8} -> {7480000000000000FF4F00000000000000F8}, EndKey:{}"] [old-version=38] [new-version=39]
   > [2024/08/06 12:14:05.444 +00:00] [INFO] [cluster_worker.go:219] ["region batch split, generate new regions"] [region-id=2] [origin="id:78 start_key:\"7480000000000000FF4E00000000000000F8\" end_key:\"7480000000000000FF4F00000000000000F8\" region_epoch:<conf_ver:1 version:39 > peers:<id:79 store_id:1 >"] [total=1]
   > [2024/08/06 12:14:05.445 +00:00] [INFO] [raft.rs:2609] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {79} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=79] [region_id=78]
   > [2024/08/06 12:14:05.446 +00:00] [INFO] [raft.rs:1092] ["became follower at term 5"] [term=5] [raft_id=79] [region_id=78]
   > [2024/08/06 12:14:05.446 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {79} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=79] [region_id=78]
   > [2024/08/06 12:14:05.446 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 79."] [id=79] [raft_id=79] [region_id=78]
   > [2024/08/06 12:14:05.446 +00:00] [INFO] [raft.rs:1517] ["starting a new election"] [term=5] [raft_id=79] [region_id=78]
   > [2024/08/06 12:14:05.446 +00:00] [INFO] [raft.rs:1142] ["became pre-candidate at term 5"] [term=5] [raft_id=79] [region_id=78]
   > [2024/08/06 12:14:05.446 +00:00] [INFO] [raft.rs:1116] ["became candidate at term 6"] [term=6] [raft_id=79] [region_id=78]
   > [2024/08/06 12:14:05.446 +00:00] [INFO] [raft.rs:1200] ["became leader at term 6"] [term=6] [raft_id=79] [region_id=78]
   > [2024/08/06 12:14:05.446 +00:00] [INFO] [peer.rs:3778] ["require updating max ts"] [initial_status=25769803854] [region_id=78]
   > [2024/08/06 12:14:05.446 +00:00] [INFO] [endpoint.rs:382] ["deregister observe region"] [observe_id=ObserveID(73)] [region_id=2] [store_id=Some(1)]
   > [2024/08/06 12:14:05.446 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF4F00000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 3 store_id: 1 }"]
   > [2024/08/06 12:14:05.447 +00:00] [INFO] [pd.rs:1246] ["succeed to update max timestamp"] [region_id=78]
   > [2024/08/06 12:14:05.450 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56024] [split_keys="key 7480000000000000FF5000000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.450 +00:00] [INFO] [peer.rs:3911] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 38"] [prev_epoch="conf_ver: 1 version: 39"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.450 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 78 start_key: 7480000000000000FF4E00000000000000F8 end_key: 7480000000000000FF4F00000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 79 store_id: 1 }"]
   > [2024/08/06 12:14:05.450 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=78] [observe_id=ObserveID(75)] [region=2]
   > [2024/08/06 12:14:05.453 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveID(76)] [region=78]
   > [2024/08/06 12:14:05.453 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56032] [split_keys="key 7480000000000000FF5000000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.454 +00:00] [INFO] [cluster_worker.go:127] ["alloc ids for region split"] [region-id=80] [peer-ids="[81]"]
   > [2024/08/06 12:14:05.454 +00:00] [INFO] [pd.rs:749] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF4F00000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 80 new_peer_ids: 81]"] [region_id=2]
   > [2024/08/06 12:14:05.457 +00:00] [INFO] [apply.rs:1394] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF5000000000000000F8 new_region_id: 80 new_peer_ids: 81 } right_derive: true }"] [index=79] [term=6] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.457 +00:00] [INFO] [apply.rs:2242] ["split region"] [keys="key 7480000000000000FF5000000000000000F8"] [region="id: 2 start_key: 7480000000000000FF4F00000000000000F8 region_epoch { conf_ver: 1 version: 39 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.460 +00:00] [INFO] [endpoint.rs:158] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/08/06 12:14:05.460 +00:00] [INFO] [peer.rs:2411] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.460 +00:00] [INFO] [peer.rs:2476] ["insert new region"] [region="id: 80 start_key: 7480000000000000FF4F00000000000000F8 end_key: 7480000000000000FF5000000000000000F8 region_epoch { conf_ver: 1 version: 40 } peers { id: 81 store_id: 1 }"] [region_id=80]
   > [2024/08/06 12:14:05.460 +00:00] [INFO] [peer.rs:219] ["create peer"] [peer_id=81] [region_id=80]
   > [2024/08/06 12:14:05.460 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=2] ["first at"=748000000000000050] ["first new region left"="{Id:80 StartKey:7480000000000000ff4f00000000000000f8 EndKey:7480000000000000ff5000000000000000f8 RegionEpoch:{ConfVer:1 Version:40} Peers:[id:81 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/08/06 12:14:05.460 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[80]"]
   > [2024/08/06 12:14:05.460 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=748000000000000051]
   > [2024/08/06 12:14:05.460 +00:00] [INFO] [region.go:505] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF4F00000000000000F8} -> {7480000000000000FF5000000000000000F8}, EndKey:{}"] [old-version=39] [new-version=40]
   > [2024/08/06 12:14:05.460 +00:00] [INFO] [cluster_worker.go:219] ["region batch split, generate new regions"] [region-id=2] [origin="id:80 start_key:\"7480000000000000FF4F00000000000000F8\" end_key:\"7480000000000000FF5000000000000000F8\" region_epoch:<conf_ver:1 version:40 > peers:<id:81 store_id:1 >"] [total=1]
   > [2024/08/06 12:14:05.462 +00:00] [INFO] [raft.rs:2609] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {81} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=81] [region_id=80]
   > [2024/08/06 12:14:05.462 +00:00] [INFO] [raft.rs:1092] ["became follower at term 5"] [term=5] [raft_id=81] [region_id=80]
   > [2024/08/06 12:14:05.462 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {81} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=81] [region_id=80]
   > [2024/08/06 12:14:05.462 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 81."] [id=81] [raft_id=81] [region_id=80]
   > [2024/08/06 12:14:05.463 +00:00] [INFO] [raft.rs:1517] ["starting a new election"] [term=5] [raft_id=81] [region_id=80]
   > [2024/08/06 12:14:05.463 +00:00] [INFO] [raft.rs:1142] ["became pre-candidate at term 5"] [term=5] [raft_id=81] [region_id=80]
   > [2024/08/06 12:14:05.463 +00:00] [INFO] [raft.rs:1116] ["became candidate at term 6"] [term=6] [raft_id=81] [region_id=80]
   > [2024/08/06 12:14:05.463 +00:00] [INFO] [raft.rs:1200] ["became leader at term 6"] [term=6] [raft_id=81] [region_id=80]
   > [2024/08/06 12:14:05.463 +00:00] [INFO] [peer.rs:3778] ["require updating max ts"] [initial_status=25769803856] [region_id=80]
   > [2024/08/06 12:14:05.463 +00:00] [INFO] [endpoint.rs:382] ["deregister observe region"] [observe_id=ObserveID(75)] [region_id=2] [store_id=Some(1)]
   > [2024/08/06 12:14:05.463 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF5000000000000000F8 region_epoch { conf_ver: 1 version: 40 } peers { id: 3 store_id: 1 }"]
   > [2024/08/06 12:14:05.463 +00:00] [INFO] [pd.rs:1246] ["succeed to update max timestamp"] [region_id=80]
   > [2024/08/06 12:14:05.466 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56000] [split_keys="key 7480000000000000FF5100000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.467 +00:00] [INFO] [peer.rs:3911] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 39"] [prev_epoch="conf_ver: 1 version: 40"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.467 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 80 start_key: 7480000000000000FF4F00000000000000F8 end_key: 7480000000000000FF5000000000000000F8 region_epoch { conf_ver: 1 version: 40 } peers { id: 81 store_id: 1 }"]
   > [2024/08/06 12:14:05.467 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=79] [observe_id=ObserveID(77)] [region=2]
   > [2024/08/06 12:14:05.467 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveID(78)] [region=80]
   > [2024/08/06 12:14:05.470 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56014] [split_keys="key 7480000000000000FF5100000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.471 +00:00] [INFO] [cluster_worker.go:127] ["alloc ids for region split"] [region-id=82] [peer-ids="[83]"]
   > [2024/08/06 12:14:05.471 +00:00] [INFO] [pd.rs:749] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF5000000000000000F8 region_epoch { conf_ver: 1 version: 40 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 82 new_peer_ids: 83]"] [region_id=2]
   > [2024/08/06 12:14:05.473 +00:00] [INFO] [apply.rs:1394] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF5100000000000000F8 new_region_id: 82 new_peer_ids: 83 } right_derive: true }"] [index=80] [term=6] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.474 +00:00] [INFO] [apply.rs:2242] ["split region"] [keys="key 7480000000000000FF5100000000000000F8"] [region="id: 2 start_key: 7480000000000000FF5000000000000000F8 region_epoch { conf_ver: 1 version: 40 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.477 +00:00] [INFO] [endpoint.rs:158] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/08/06 12:14:05.477 +00:00] [INFO] [peer.rs:2411] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.478 +00:00] [INFO] [peer.rs:2476] ["insert new region"] [region="id: 82 start_key: 7480000000000000FF5000000000000000F8 end_key: 7480000000000000FF5100000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 83 store_id: 1 }"] [region_id=82]
   > [2024/08/06 12:14:05.478 +00:00] [INFO] [peer.rs:219] ["create peer"] [peer_id=83] [region_id=82]
   > [2024/08/06 12:14:05.478 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=2] ["first at"=748000000000000051] ["first new region left"="{Id:82 StartKey:7480000000000000ff5000000000000000f8 EndKey:7480000000000000ff5100000000000000f8 RegionEpoch:{ConfVer:1 Version:41} Peers:[id:83 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/08/06 12:14:05.478 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[82]"]
   > [2024/08/06 12:14:05.478 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=748000000000000052]
   > [2024/08/06 12:14:05.478 +00:00] [INFO] [region.go:505] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF5000000000000000F8} -> {7480000000000000FF5100000000000000F8}, EndKey:{}"] [old-version=40] [new-version=41]
   > [2024/08/06 12:14:05.478 +00:00] [INFO] [cluster_worker.go:219] ["region batch split, generate new regions"] [region-id=2] [origin="id:82 start_key:\"7480000000000000FF5000000000000000F8\" end_key:\"7480000000000000FF5100000000000000F8\" region_epoch:<conf_ver:1 version:41 > peers:<id:83 store_id:1 >"] [total=1]
   > [2024/08/06 12:14:05.479 +00:00] [INFO] [raft.rs:2609] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {83} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=83] [region_id=82]
   > [2024/08/06 12:14:05.479 +00:00] [INFO] [raft.rs:1092] ["became follower at term 5"] [term=5] [raft_id=83] [region_id=82]
   > [2024/08/06 12:14:05.480 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {83} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=83] [region_id=82]
   > [2024/08/06 12:14:05.480 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 83."] [id=83] [raft_id=83] [region_id=82]
   > [2024/08/06 12:14:05.480 +00:00] [INFO] [raft.rs:1517] ["starting a new election"] [term=5] [raft_id=83] [region_id=82]
   > [2024/08/06 12:14:05.480 +00:00] [INFO] [raft.rs:1142] ["became pre-candidate at term 5"] [term=5] [raft_id=83] [region_id=82]
   > [2024/08/06 12:14:05.480 +00:00] [INFO] [raft.rs:1116] ["became candidate at term 6"] [term=6] [raft_id=83] [region_id=82]
   > [2024/08/06 12:14:05.480 +00:00] [INFO] [raft.rs:1200] ["became leader at term 6"] [term=6] [raft_id=83] [region_id=82]
   > [2024/08/06 12:14:05.480 +00:00] [INFO] [endpoint.rs:382] ["deregister observe region"] [observe_id=ObserveID(77)] [region_id=2] [store_id=Some(1)]
   > [2024/08/06 12:14:05.480 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF5100000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 3 store_id: 1 }"]
   > [2024/08/06 12:14:05.480 +00:00] [INFO] [peer.rs:3778] ["require updating max ts"] [initial_status=25769803858] [region_id=82]
   > [2024/08/06 12:14:05.481 +00:00] [INFO] [pd.rs:1246] ["succeed to update max timestamp"] [region_id=82]
   > [2024/08/06 12:14:05.483 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56024] [split_keys="key 7480000000000000FF5200000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.484 +00:00] [INFO] [peer.rs:3911] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 40"] [prev_epoch="conf_ver: 1 version: 41"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.484 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=80] [observe_id=ObserveID(79)] [region=2]
   > [2024/08/06 12:14:05.486 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 82 start_key: 7480000000000000FF5000000000000000F8 end_key: 7480000000000000FF5100000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 83 store_id: 1 }"]
   > [2024/08/06 12:14:05.486 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveID(80)] [region=82]
   > [2024/08/06 12:14:05.487 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56032] [split_keys="key 7480000000000000FF5200000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.487 +00:00] [INFO] [cluster_worker.go:127] ["alloc ids for region split"] [region-id=84] [peer-ids="[85]"]
   > [2024/08/06 12:14:05.487 +00:00] [INFO] [pd.rs:749] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF5100000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 84 new_peer_ids: 85]"] [region_id=2]
   > [2024/08/06 12:14:05.490 +00:00] [INFO] [apply.rs:1394] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF5200000000000000F8 new_region_id: 84 new_peer_ids: 85 } right_derive: true }"] [index=81] [term=6] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.490 +00:00] [INFO] [apply.rs:2242] ["split region"] [keys="key 7480000000000000FF5200000000000000F8"] [region="id: 2 start_key: 7480000000000000FF5100000000000000F8 region_epoch { conf_ver: 1 version: 41 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.493 +00:00] [INFO] [endpoint.rs:158] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/08/06 12:14:05.493 +00:00] [INFO] [peer.rs:2411] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.493 +00:00] [INFO] [peer.rs:2476] ["insert new region"] [region="id: 84 start_key: 7480000000000000FF5100000000000000F8 end_key: 7480000000000000FF5200000000000000F8 region_epoch { conf_ver: 1 version: 42 } peers { id: 85 store_id: 1 }"] [region_id=84]
   > [2024/08/06 12:14:05.493 +00:00] [INFO] [peer.rs:219] ["create peer"] [peer_id=85] [region_id=84]
   > [2024/08/06 12:14:05.493 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=2] ["first at"=748000000000000052] ["first new region left"="{Id:84 StartKey:7480000000000000ff5100000000000000f8 EndKey:7480000000000000ff5200000000000000f8 RegionEpoch:{ConfVer:1 Version:42} Peers:[id:85 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/08/06 12:14:05.493 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[84]"]
   > [2024/08/06 12:14:05.493 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=748000000000000053]
   > [2024/08/06 12:14:05.494 +00:00] [INFO] [region.go:505] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF5100000000000000F8} -> {7480000000000000FF5200000000000000F8}, EndKey:{}"] [old-version=41] [new-version=42]
   > [2024/08/06 12:14:05.494 +00:00] [INFO] [cluster_worker.go:219] ["region batch split, generate new regions"] [region-id=2] [origin="id:84 start_key:\"7480000000000000FF5100000000000000F8\" end_key:\"7480000000000000FF5200000000000000F8\" region_epoch:<conf_ver:1 version:42 > peers:<id:85 store_id:1 >"] [total=1]
   > [2024/08/06 12:14:05.496 +00:00] [INFO] [raft.rs:2609] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {85} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=85] [region_id=84]
   > [2024/08/06 12:14:05.496 +00:00] [INFO] [raft.rs:1092] ["became follower at term 5"] [term=5] [raft_id=85] [region_id=84]
   > [2024/08/06 12:14:05.496 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {85} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=85] [region_id=84]
   > [2024/08/06 12:14:05.496 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 85."] [id=85] [raft_id=85] [region_id=84]
   > [2024/08/06 12:14:05.496 +00:00] [INFO] [raft.rs:1517] ["starting a new election"] [term=5] [raft_id=85] [region_id=84]
   > [2024/08/06 12:14:05.496 +00:00] [INFO] [raft.rs:1142] ["became pre-candidate at term 5"] [term=5] [raft_id=85] [region_id=84]
   > [2024/08/06 12:14:05.496 +00:00] [INFO] [raft.rs:1116] ["became candidate at term 6"] [term=6] [raft_id=85] [region_id=84]
   > [2024/08/06 12:14:05.496 +00:00] [INFO] [raft.rs:1200] ["became leader at term 6"] [term=6] [raft_id=85] [region_id=84]
   > [2024/08/06 12:14:05.497 +00:00] [INFO] [peer.rs:3778] ["require updating max ts"] [initial_status=25769803860] [region_id=84]
   > [2024/08/06 12:14:05.497 +00:00] [INFO] [endpoint.rs:382] ["deregister observe region"] [observe_id=ObserveID(79)] [region_id=2] [store_id=Some(1)]
   > [2024/08/06 12:14:05.497 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF5200000000000000F8 region_epoch { conf_ver: 1 version: 42 } peers { id: 3 store_id: 1 }"]
   > [2024/08/06 12:14:05.497 +00:00] [INFO] [pd.rs:1246] ["succeed to update max timestamp"] [region_id=84]
   > [2024/08/06 12:14:05.500 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56000] [split_keys="key 7480000000000000FF5300000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.501 +00:00] [INFO] [peer.rs:3911] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 41"] [prev_epoch="conf_ver: 1 version: 42"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.501 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 84 start_key: 7480000000000000FF5100000000000000F8 end_key: 7480000000000000FF5200000000000000F8 region_epoch { conf_ver: 1 version: 42 } peers { id: 85 store_id: 1 }"]
   > [2024/08/06 12:14:05.501 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=81] [observe_id=ObserveID(81)] [region=2]
   > [2024/08/06 12:14:05.502 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveID(82)] [region=84]
   > [2024/08/06 12:14:05.504 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56014] [split_keys="key 7480000000000000FF5300000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.504 +00:00] [INFO] [cluster_worker.go:127] ["alloc ids for region split"] [region-id=86] [peer-ids="[87]"]
   > [2024/08/06 12:14:05.505 +00:00] [INFO] [pd.rs:749] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF5200000000000000F8 region_epoch { conf_ver: 1 version: 42 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 86 new_peer_ids: 87]"] [region_id=2]
   > [2024/08/06 12:14:05.509 +00:00] [INFO] [apply.rs:1394] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF5300000000000000F8 new_region_id: 86 new_peer_ids: 87 } right_derive: true }"] [index=82] [term=6] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.509 +00:00] [INFO] [apply.rs:2242] ["split region"] [keys="key 7480000000000000FF5300000000000000F8"] [region="id: 2 start_key: 7480000000000000FF5200000000000000F8 region_epoch { conf_ver: 1 version: 42 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.511 +00:00] [INFO] [endpoint.rs:158] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/08/06 12:14:05.512 +00:00] [INFO] [peer.rs:2411] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.512 +00:00] [INFO] [peer.rs:2476] ["insert new region"] [region="id: 86 start_key: 7480000000000000FF5200000000000000F8 end_key: 7480000000000000FF5300000000000000F8 region_epoch { conf_ver: 1 version: 43 } peers { id: 87 store_id: 1 }"] [region_id=86]
   > [2024/08/06 12:14:05.512 +00:00] [INFO] [peer.rs:219] ["create peer"] [peer_id=87] [region_id=86]
   > [2024/08/06 12:14:05.512 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=2] ["first at"=748000000000000053] ["first new region left"="{Id:86 StartKey:7480000000000000ff5200000000000000f8 EndKey:7480000000000000ff5300000000000000f8 RegionEpoch:{ConfVer:1 Version:43} Peers:[id:87 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/08/06 12:14:05.512 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[86]"]
   > [2024/08/06 12:14:05.512 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=748000000000000054]
   > [2024/08/06 12:14:05.512 +00:00] [INFO] [region.go:505] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF5200000000000000F8} -> {7480000000000000FF5300000000000000F8}, EndKey:{}"] [old-version=42] [new-version=43]
   > [2024/08/06 12:14:05.512 +00:00] [INFO] [cluster_worker.go:219] ["region batch split, generate new regions"] [region-id=2] [origin="id:86 start_key:\"7480000000000000FF5200000000000000F8\" end_key:\"7480000000000000FF5300000000000000F8\" region_epoch:<conf_ver:1 version:43 > peers:<id:87 store_id:1 >"] [total=1]
   > [2024/08/06 12:14:05.514 +00:00] [INFO] [raft.rs:2609] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {87} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=87] [region_id=86]
   > [2024/08/06 12:14:05.514 +00:00] [INFO] [raft.rs:1092] ["became follower at term 5"] [term=5] [raft_id=87] [region_id=86]
   > [2024/08/06 12:14:05.514 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {87} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=87] [region_id=86]
   > [2024/08/06 12:14:05.514 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 87."] [id=87] [raft_id=87] [region_id=86]
   > [2024/08/06 12:14:05.514 +00:00] [INFO] [raft.rs:1517] ["starting a new election"] [term=5] [raft_id=87] [region_id=86]
   > [2024/08/06 12:14:05.514 +00:00] [INFO] [raft.rs:1142] ["became pre-candidate at term 5"] [term=5] [raft_id=87] [region_id=86]
   > [2024/08/06 12:14:05.514 +00:00] [INFO] [raft.rs:1116] ["became candidate at term 6"] [term=6] [raft_id=87] [region_id=86]
   > [2024/08/06 12:14:05.514 +00:00] [INFO] [raft.rs:1200] ["became leader at term 6"] [term=6] [raft_id=87] [region_id=86]
   > [2024/08/06 12:14:05.515 +00:00] [INFO] [peer.rs:3778] ["require updating max ts"] [initial_status=25769803862] [region_id=86]
   > [2024/08/06 12:14:05.515 +00:00] [INFO] [endpoint.rs:382] ["deregister observe region"] [observe_id=ObserveID(81)] [region_id=2] [store_id=Some(1)]
   > [2024/08/06 12:14:05.515 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF5300000000000000F8 region_epoch { conf_ver: 1 version: 43 } peers { id: 3 store_id: 1 }"]
   > [2024/08/06 12:14:05.515 +00:00] [INFO] [pd.rs:1246] ["succeed to update max timestamp"] [region_id=86]
   > [2024/08/06 12:14:05.518 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56024] [split_keys="key 7480000000000000FF5400000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.518 +00:00] [INFO] [peer.rs:3911] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 42"] [prev_epoch="conf_ver: 1 version: 43"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.518 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 86 start_key: 7480000000000000FF5200000000000000F8 end_key: 7480000000000000FF5300000000000000F8 region_epoch { conf_ver: 1 version: 43 } peers { id: 87 store_id: 1 }"]
   > [2024/08/06 12:14:05.518 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=82] [observe_id=ObserveID(83)] [region=2]
   > [2024/08/06 12:14:05.518 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveID(84)] [region=86]
   > [2024/08/06 12:14:05.522 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56032] [split_keys="key 7480000000000000FF5400000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.523 +00:00] [INFO] [cluster_worker.go:127] ["alloc ids for region split"] [region-id=88] [peer-ids="[89]"]
   > [2024/08/06 12:14:05.523 +00:00] [INFO] [pd.rs:749] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF5300000000000000F8 region_epoch { conf_ver: 1 version: 43 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 88 new_peer_ids: 89]"] [region_id=2]
   > [2024/08/06 12:14:05.529 +00:00] [INFO] [apply.rs:1394] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF5400000000000000F8 new_region_id: 88 new_peer_ids: 89 } right_derive: true }"] [index=83] [term=6] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.529 +00:00] [INFO] [apply.rs:2242] ["split region"] [keys="key 7480000000000000FF5400000000000000F8"] [region="id: 2 start_key: 7480000000000000FF5300000000000000F8 region_epoch { conf_ver: 1 version: 43 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.532 +00:00] [INFO] [endpoint.rs:158] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/08/06 12:14:05.532 +00:00] [INFO] [peer.rs:2411] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.532 +00:00] [INFO] [peer.rs:2476] ["insert new region"] [region="id: 88 start_key: 7480000000000000FF5300000000000000F8 end_key: 7480000000000000FF5400000000000000F8 region_epoch { conf_ver: 1 version: 44 } peers { id: 89 store_id: 1 }"] [region_id=88]
   > [2024/08/06 12:14:05.532 +00:00] [INFO] [peer.rs:219] ["create peer"] [peer_id=89] [region_id=88]
   > [2024/08/06 12:14:05.532 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=2] ["first at"=748000000000000054] ["first new region left"="{Id:88 StartKey:7480000000000000ff5300000000000000f8 EndKey:7480000000000000ff5400000000000000f8 RegionEpoch:{ConfVer:1 Version:44} Peers:[id:89 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/08/06 12:14:05.532 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[88]"]
   > [2024/08/06 12:14:05.532 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=748000000000000055]
   > [2024/08/06 12:14:05.532 +00:00] [INFO] [region.go:505] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF5300000000000000F8} -> {7480000000000000FF5400000000000000F8}, EndKey:{}"] [old-version=43] [new-version=44]
   > [2024/08/06 12:14:05.532 +00:00] [INFO] [cluster_worker.go:219] ["region batch split, generate new regions"] [region-id=2] [origin="id:88 start_key:\"7480000000000000FF5300000000000000F8\" end_key:\"7480000000000000FF5400000000000000F8\" region_epoch:<conf_ver:1 version:44 > peers:<id:89 store_id:1 >"] [total=1]
   > [2024/08/06 12:14:05.534 +00:00] [INFO] [raft.rs:2609] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {89} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=89] [region_id=88]
   > [2024/08/06 12:14:05.534 +00:00] [INFO] [raft.rs:1092] ["became follower at term 5"] [term=5] [raft_id=89] [region_id=88]
   > [2024/08/06 12:14:05.534 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {89} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=89] [region_id=88]
   > [2024/08/06 12:14:05.534 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 89."] [id=89] [raft_id=89] [region_id=88]
   > [2024/08/06 12:14:05.534 +00:00] [INFO] [raft.rs:1517] ["starting a new election"] [term=5] [raft_id=89] [region_id=88]
   > [2024/08/06 12:14:05.534 +00:00] [INFO] [raft.rs:1142] ["became pre-candidate at term 5"] [term=5] [raft_id=89] [region_id=88]
   > [2024/08/06 12:14:05.534 +00:00] [INFO] [raft.rs:1116] ["became candidate at term 6"] [term=6] [raft_id=89] [region_id=88]
   > [2024/08/06 12:14:05.534 +00:00] [INFO] [raft.rs:1200] ["became leader at term 6"] [term=6] [raft_id=89] [region_id=88]
   > [2024/08/06 12:14:05.534 +00:00] [INFO] [endpoint.rs:382] ["deregister observe region"] [observe_id=ObserveID(83)] [region_id=2] [store_id=Some(1)]
   > [2024/08/06 12:14:05.534 +00:00] [INFO] [peer.rs:3778] ["require updating max ts"] [initial_status=25769803864] [region_id=88]
   > [2024/08/06 12:14:05.535 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF5400000000000000F8 region_epoch { conf_ver: 1 version: 44 } peers { id: 3 store_id: 1 }"]
   > [2024/08/06 12:14:05.535 +00:00] [INFO] [pd.rs:1246] ["succeed to update max timestamp"] [region_id=88]
   > [2024/08/06 12:14:05.537 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56000] [split_keys="key 7480000000000000FF5500000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.538 +00:00] [INFO] [peer.rs:3911] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 43"] [prev_epoch="conf_ver: 1 version: 44"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.538 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 88 start_key: 7480000000000000FF5300000000000000F8 end_key: 7480000000000000FF5400000000000000F8 region_epoch { conf_ver: 1 version: 44 } peers { id: 89 store_id: 1 }"]
   > [2024/08/06 12:14:05.538 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=83] [observe_id=ObserveID(85)] [region=2]
   > [2024/08/06 12:14:05.538 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveID(86)] [region=88]
   > [2024/08/06 12:14:05.540 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56014] [split_keys="key 7480000000000000FF5500000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.541 +00:00] [INFO] [cluster_worker.go:127] ["alloc ids for region split"] [region-id=90] [peer-ids="[91]"]
   > [2024/08/06 12:14:05.541 +00:00] [INFO] [pd.rs:749] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF5400000000000000F8 region_epoch { conf_ver: 1 version: 44 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 90 new_peer_ids: 91]"] [region_id=2]
   > [2024/08/06 12:14:05.545 +00:00] [INFO] [apply.rs:1394] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF5500000000000000F8 new_region_id: 90 new_peer_ids: 91 } right_derive: true }"] [index=84] [term=6] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.545 +00:00] [INFO] [apply.rs:2242] ["split region"] [keys="key 7480000000000000FF5500000000000000F8"] [region="id: 2 start_key: 7480000000000000FF5400000000000000F8 region_epoch { conf_ver: 1 version: 44 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.548 +00:00] [INFO] [endpoint.rs:158] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/08/06 12:14:05.548 +00:00] [INFO] [peer.rs:2411] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.548 +00:00] [INFO] [peer.rs:2476] ["insert new region"] [region="id: 90 start_key: 7480000000000000FF5400000000000000F8 end_key: 7480000000000000FF5500000000000000F8 region_epoch { conf_ver: 1 version: 45 } peers { id: 91 store_id: 1 }"] [region_id=90]
   > [2024/08/06 12:14:05.549 +00:00] [INFO] [peer.rs:219] ["create peer"] [peer_id=91] [region_id=90]
   > [2024/08/06 12:14:05.549 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=2] ["first at"=748000000000000055] ["first new region left"="{Id:90 StartKey:7480000000000000ff5400000000000000f8 EndKey:7480000000000000ff5500000000000000f8 RegionEpoch:{ConfVer:1 Version:45} Peers:[id:91 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/08/06 12:14:05.549 +00:00] [INFO] [raft.rs:2609] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {91} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=91] [region_id=90]
   > [2024/08/06 12:14:05.549 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[90]"]
   > [2024/08/06 12:14:05.549 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=748000000000000056]
   > [2024/08/06 12:14:05.549 +00:00] [INFO] [raft.rs:1092] ["became follower at term 5"] [term=5] [raft_id=91] [region_id=90]
   > [2024/08/06 12:14:05.549 +00:00] [INFO] [region.go:505] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF5400000000000000F8} -> {7480000000000000FF5500000000000000F8}, EndKey:{}"] [old-version=44] [new-version=45]
   > [2024/08/06 12:14:05.549 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {91} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=91] [region_id=90]
   > [2024/08/06 12:14:05.549 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 91."] [id=91] [raft_id=91] [region_id=90]
   > [2024/08/06 12:14:05.549 +00:00] [INFO] [raft.rs:1517] ["starting a new election"] [term=5] [raft_id=91] [region_id=90]
   > [2024/08/06 12:14:05.549 +00:00] [INFO] [cluster_worker.go:219] ["region batch split, generate new regions"] [region-id=2] [origin="id:90 start_key:\"7480000000000000FF5400000000000000F8\" end_key:\"7480000000000000FF5500000000000000F8\" region_epoch:<conf_ver:1 version:45 > peers:<id:91 store_id:1 >"] [total=1]
   > [2024/08/06 12:14:05.549 +00:00] [INFO] [raft.rs:1142] ["became pre-candidate at term 5"] [term=5] [raft_id=91] [region_id=90]
   > [2024/08/06 12:14:05.550 +00:00] [INFO] [raft.rs:1116] ["became candidate at term 6"] [term=6] [raft_id=91] [region_id=90]
   > [2024/08/06 12:14:05.550 +00:00] [INFO] [raft.rs:1200] ["became leader at term 6"] [term=6] [raft_id=91] [region_id=90]
   > [2024/08/06 12:14:05.550 +00:00] [INFO] [peer.rs:3778] ["require updating max ts"] [initial_status=25769803866] [region_id=90]
   > [2024/08/06 12:14:05.550 +00:00] [INFO] [endpoint.rs:382] ["deregister observe region"] [observe_id=ObserveID(85)] [region_id=2] [store_id=Some(1)]
   > [2024/08/06 12:14:05.550 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF5500000000000000F8 region_epoch { conf_ver: 1 version: 45 } peers { id: 3 store_id: 1 }"]
   > [2024/08/06 12:14:05.550 +00:00] [INFO] [pd.rs:1246] ["succeed to update max timestamp"] [region_id=90]
   > [2024/08/06 12:14:05.550 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=84] [observe_id=ObserveID(87)] [region=2]
   > [2024/08/06 12:14:05.550 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56024] [split_keys="key 7480000000000000FF5600000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.550 +00:00] [INFO] [peer.rs:3911] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 44"] [prev_epoch="conf_ver: 1 version: 45"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.551 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 90 start_key: 7480000000000000FF5400000000000000F8 end_key: 7480000000000000FF5500000000000000F8 region_epoch { conf_ver: 1 version: 45 } peers { id: 91 store_id: 1 }"]
   > [2024/08/06 12:14:05.552 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveID(88)] [region=90]
   > [2024/08/06 12:14:05.553 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56032] [split_keys="key 7480000000000000FF5600000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.553 +00:00] [INFO] [cluster_worker.go:127] ["alloc ids for region split"] [region-id=92] [peer-ids="[93]"]
   > [2024/08/06 12:14:05.554 +00:00] [INFO] [pd.rs:749] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF5500000000000000F8 region_epoch { conf_ver: 1 version: 45 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 92 new_peer_ids: 93]"] [region_id=2]
   > [2024/08/06 12:14:05.556 +00:00] [INFO] [apply.rs:1394] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF5600000000000000F8 new_region_id: 92 new_peer_ids: 93 } right_derive: true }"] [index=85] [term=6] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.556 +00:00] [INFO] [apply.rs:2242] ["split region"] [keys="key 7480000000000000FF5600000000000000F8"] [region="id: 2 start_key: 7480000000000000FF5500000000000000F8 region_epoch { conf_ver: 1 version: 45 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.559 +00:00] [INFO] [endpoint.rs:158] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/08/06 12:14:05.559 +00:00] [INFO] [peer.rs:2411] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/08/06 12:14:05.559 +00:00] [INFO] [peer.rs:2476] ["insert new region"] [region="id: 92 start_key: 7480000000000000FF5500000000000000F8 end_key: 7480000000000000FF5600000000000000F8 region_epoch { conf_ver: 1 version: 46 } peers { id: 93 store_id: 1 }"] [region_id=92]
   > [2024/08/06 12:14:05.559 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=2] ["first at"=748000000000000056] ["first new region left"="{Id:92 StartKey:7480000000000000ff5500000000000000f8 EndKey:7480000000000000ff5600000000000000f8 RegionEpoch:{ConfVer:1 Version:46} Peers:[id:93 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/08/06 12:14:05.559 +00:00] [INFO] [peer.rs:219] ["create peer"] [peer_id=93] [region_id=92]
   > [2024/08/06 12:14:05.559 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[92]"]
   > [2024/08/06 12:14:05.559 +00:00] [INFO] [region.go:505] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF5500000000000000F8} -> {7480000000000000FF5600000000000000F8}, EndKey:{}"] [old-version=45] [new-version=46]
   > [2024/08/06 12:14:05.559 +00:00] [INFO] [cluster_worker.go:219] ["region batch split, generate new regions"] [region-id=2] [origin="id:92 start_key:\"7480000000000000FF5500000000000000F8\" end_key:\"7480000000000000FF5600000000000000F8\" region_epoch:<conf_ver:1 version:46 > peers:<id:93 store_id:1 >"] [total=1]
   > [2024/08/06 12:14:05.561 +00:00] [INFO] [raft.rs:2609] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {93} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=93] [region_id=92]
   > [2024/08/06 12:14:05.561 +00:00] [INFO] [raft.rs:1092] ["became follower at term 5"] [term=5] [raft_id=93] [region_id=92]
   > [2024/08/06 12:14:05.561 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {93} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=93] [region_id=92]
   > [2024/08/06 12:14:05.561 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 93."] [id=93] [raft_id=93] [region_id=92]
   > [2024/08/06 12:14:05.562 +00:00] [INFO] [raft.rs:1517] ["starting a new election"] [term=5] [raft_id=93] [region_id=92]
   > [2024/08/06 12:14:05.562 +00:00] [INFO] [raft.rs:1142] ["became pre-candidate at term 5"] [term=5] [raft_id=93] [region_id=92]
   > [2024/08/06 12:14:05.562 +00:00] [INFO] [raft.rs:1116] ["became candidate at term 6"] [term=6] [raft_id=93] [region_id=92]
   > [2024/08/06 12:14:05.562 +00:00] [INFO] [raft.rs:1200] ["became leader at term 6"] [term=6] [raft_id=93] [region_id=92]
   > [2024/08/06 12:14:05.562 +00:00] [INFO] [endpoint.rs:382] ["deregister observe region"] [observe_id=ObserveID(87)] [region_id=2] [store_id=Some(1)]
   > [2024/08/06 12:14:05.562 +00:00] [INFO] [peer.rs:3778] ["require updating max ts"] [initial_status=25769803868] [region_id=92]
   > [2024/08/06 12:14:05.562 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF5600000000000000F8 region_epoch { conf_ver: 1 version: 46 } peers { id: 3 store_id: 1 }"]
   > [2024/08/06 12:14:05.562 +00:00] [INFO] [pd.rs:1246] ["succeed to update max timestamp"] [region_id=92]
   > [2024/08/06 12:14:05.566 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 92 start_key: 7480000000000000FF5500000000000000F8 end_key: 7480000000000000FF5600000000000000F8 region_epoch { conf_ver: 1 version: 46 } peers { id: 93 store_id: 1 }"]
   > [2024/08/06 12:14:05.566 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=85] [observe_id=ObserveID(89)] [region=2]
   > [2024/08/06 12:14:05.566 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveID(90)] [region=92]
   > [2024/08/06 12:14:06.499 +00:00] [INFO] [set.go:127] ["set global var"] [conn=19] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/08/06 12:14:09.175 +00:00] [WARN] [endpoint.rs:632] [error-response] [err="Region error (will back off and retry) message: \"EpochNotMatch current epoch of region 2 is conf_ver: 1 version: 46, but you sent conf_ver: 1 version: 45\" epoch_not_match { current_regions { id: 2 start_key: 7480000000000000FF5600000000000000F8 region_epoch { conf_ver: 1 version: 46 } peers { id: 3 store_id: 1 } } current_regions { id: 92 start_key: 7480000000000000FF5500000000000000F8 end_key: 7480000000000000FF5600000000000000F8 region_epoch { conf_ver: 1 version: 46 } peers { id: 93 store_id: 1 } } }"]
   > [2024/08/06 12:14:09.175 +00:00] [WARN] [endpoint.rs:632] [error-response] [err="Region error (will back off and retry) message: \"EpochNotMatch current epoch of region 2 is conf_ver: 1 version: 46, but you sent conf_ver: 1 version: 45\" epoch_not_match { current_regions { id: 2 start_key: 7480000000000000FF5600000000000000F8 region_epoch { conf_ver: 1 version: 46 } peers { id: 3 store_id: 1 } } current_regions { id: 92 start_key: 7480000000000000FF5500000000000000F8 end_key: 7480000000000000FF5600000000000000F8 region_epoch { conf_ver: 1 version: 46 } peers { id: 93 store_id: 1 } } }"]
