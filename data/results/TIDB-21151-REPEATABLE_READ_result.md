# Bug ID TIDB-21151-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/21151
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              SELECT returns different values if using NO_INDEX_MERGE


## Details
 * Database: tidb-v4.0.8.tikv
 * Number of scenarios: 1
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL repeatable read;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows: 0
 * Instruction #1:
     - Instruction:  SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows: 0
 * Instruction #2:
     - Instruction:  BEGIN;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows: 0
 * Instruction #3:
     - Instruction:  select /*+ NO_INDEX_MERGE() */ * from t where a > 3 or b > 3;
     - Transaction: conn_0
     - Output: [(2, 10, 4, 4)]
     - Executed order: 3
     - Affected rows: 1
 * Instruction #4:
     - Instruction:  select /*+ USE_INDEX_MERGE(t, ia, ib) */ * from t where a > 3 or b > 3;
     - Transaction: conn_0
     - Output: [(2, 10, 4, 4)]
     - Executed order: 4
     - Affected rows: 1
 * Instruction #5:
     - Instruction:  BEGIN;
     - Transaction: conn_1
     - Output: None
     - Executed order: 5
     - Affected rows: 0
 * Instruction #6:
     - Instruction:  update t set value = 11 where id = 2;
     - Transaction: conn_1
     - Output: None
     - Executed order: 6
     - Affected rows: 1
 * Instruction #7:
     - Instruction:  COMMIT;
     - Transaction: conn_1
     - Output: None
     - Executed order: 7
     - Affected rows: 0
 * Instruction #8:
     - Instruction:  select /*+ NO_INDEX_MERGE() */ * from t where a > 3 or b > 3;
     - Transaction: conn_0
     - Output: [(2, 10, 4, 4)]
     - Executed order: 8
     - Affected rows: 1
 * Instruction #9:
     - Instruction:  select /*+ USE_INDEX_MERGE(t, ia, ib) */ * from t where a > 3 or b > 3;
     - Transaction: conn_0
     - Output: [(2, 10, 4, 4)]
     - Executed order: 9
     - Affected rows: 1
 * Instruction #10:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 10
     - Affected rows: 0

 * Container logs:
   > [2024/08/13 13:42:30.157 +00:00] [INFO] [session.go:2161] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=22] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/08/13 13:42:30.159 +00:00] [INFO] [session.go:2161] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=22] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/08/13 13:42:30.198 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-13 13:42:30.142 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/13 13:42:30.198 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-13 13:42:30.142 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/08/13 13:42:30.202 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-13 13:42:30.142 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/13 13:42:30.232 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=22] [neededSchemaVersion=23] ["start time"=1.075637ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/13 13:42:30.281 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=23] ["take time"=52.048636ms] [job="ID:46, Type:create schema, State:done, SchemaState:public, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-13 13:42:30.142 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/13 13:42:30.284 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:46, Type:create schema, State:synced, SchemaState:public, SchemaID:45, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-13 13:42:30.142 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/13 13:42:30.305 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=46]
   > [2024/08/13 13:42:30.305 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/08/13 13:42:30.308 +00:00] [INFO] [session.go:2161] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=23] [cur_db=testdb] [sql="create table t (id int primary key, value int, a int not null, b int not null,\n    index ia (a),  index ib (b));"] [user=root@127.0.0.1]
   > [2024/08/13 13:42:30.352 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-08-13 13:42:30.292 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/13 13:42:30.352 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-08-13 13:42:30.292 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t (id int primary key, value int, a int not null, b int not null,\n    index ia (a),  index ib (b));"]
   > [2024/08/13 13:42:30.356 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-08-13 13:42:30.292 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/13 13:42:30.394 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=23] [neededSchemaVersion=24] ["start time"=1.951735ms] [phyTblIDs="[47]"] [actionTypes="[8]"]
   > [2024/08/13 13:42:30.442 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=24] ["take time"=52.086211ms] [job="ID:48, Type:create table, State:done, SchemaState:public, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-08-13 13:42:30.292 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/13 13:42:30.446 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:48, Type:create table, State:synced, SchemaState:public, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-08-13 13:42:30.292 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/13 13:42:30.480 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=48]
   > [2024/08/13 13:42:30.482 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/08/13 13:42:30.483 +00:00] [INFO] [split_region.go:60] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=74800000000000002f]
   > [2024/08/13 13:42:30.483 +00:00] [INFO] [peer.rs:469] ["on split"] [split_keys="key 7480000000000000FF2F00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/13 13:42:30.483 +00:00] [INFO] [cluster_worker.go:125] ["alloc ids for region split"] [region-id=44] [peer-ids="[45]"]
   > [2024/08/13 13:42:30.484 +00:00] [INFO] [pd.rs:507] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF2B00000000000000F8 region_epoch { conf_ver: 1 version: 21 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 44 new_peer_ids: 45]"] [region_id=2]
   > [2024/08/13 13:42:30.499 +00:00] [INFO] [apply.rs:1172] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF2F00000000000000F8 new_region_id: 44 new_peer_ids: 45 } right_derive: true }"] [index=54] [term=6] [peer_id=3] [region_id=2]
   > [2024/08/13 13:42:30.499 +00:00] [INFO] [apply.rs:1752] ["split region"] [keys="key 7480000000000000FF2F00000000000000F8"] [region="id: 2 start_key: 7480000000000000FF2B00000000000000F8 region_epoch { conf_ver: 1 version: 21 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/08/13 13:42:30.510 +00:00] [INFO] [split_region.go:157] ["batch split regions complete"] ["batch region ID"=2] ["first at"=74800000000000002f] ["first new region left"="{Id:44 StartKey:7480000000000000ff2b00000000000000f8 EndKey:7480000000000000ff2f00000000000000f8 RegionEpoch:{ConfVer:1 Version:22} Peers:[id:45 store_id:1 ]}"] ["new region count"=1]
   > [2024/08/13 13:42:30.510 +00:00] [INFO] [split_region.go:209] ["split regions complete"] ["region count"=1] ["region IDs"="[44]"]
   > [2024/08/13 13:42:30.519 +00:00] [INFO] [peer.rs:1758] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/08/13 13:42:30.520 +00:00] [INFO] [peer.rs:1800] ["insert new region"] [region="id: 44 start_key: 7480000000000000FF2B00000000000000F8 end_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 45 store_id: 1 }"] [region_id=44]
   > [2024/08/13 13:42:30.520 +00:00] [INFO] [peer.rs:159] ["create peer"] [peer_id=45] [region_id=44]
   > [2024/08/13 13:42:30.520 +00:00] [INFO] [cluster.go:542] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF2B00000000000000F8} -> {7480000000000000FF2F00000000000000F8}, EndKey:{}"] [old-version=21] [new-version=22]
   > [2024/08/13 13:42:30.520 +00:00] [INFO] [cluster_worker.go:217] ["region batch split, generate new regions"] [region-id=2] [origin="id:44 start_key:\"7480000000000000FF2B00000000000000F8\" end_key:\"7480000000000000FF2F00000000000000F8\" region_epoch:<conf_ver:1 version:22 > peers:<id:45 store_id:1 >"] [total=1]
   > [2024/08/13 13:42:30.530 +00:00] [INFO] [raft.rs:783] ["became follower at term 5"] [term=5] [raft_id=45] [region_id=44]
   > [2024/08/13 13:42:30.530 +00:00] [INFO] [raft.rs:285] [newRaft] [peers="[(45, Progress { matched: 5, next_idx: 6, state: Probe, paused: false, pending_snapshot: 0, pending_request_snapshot: 0, recent_active: false, ins: Inflights { start: 0, count: 0, buffer: [] } })]"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=45] [region_id=44]
   > [2024/08/13 13:42:30.530 +00:00] [INFO] [raw_node.rs:222] ["RawNode created with id 45."] [id=45] [raft_id=45] [region_id=44]
   > [2024/08/13 13:42:30.530 +00:00] [INFO] [raft.rs:1177] ["starting a new election"] [term=5] [raft_id=45] [region_id=44]
   > [2024/08/13 13:42:30.530 +00:00] [INFO] [raft.rs:833] ["became pre-candidate at term 5"] [term=5] [raft_id=45] [region_id=44]
   > [2024/08/13 13:42:30.531 +00:00] [INFO] [raft.rs:902] ["45 received message from 45"] [term=5] [msg=MsgRequestPreVote] [from=45] [id=45] [raft_id=45] [region_id=44]
   > [2024/08/13 13:42:30.531 +00:00] [INFO] [raft.rs:807] ["became candidate at term 6"] [term=6] [raft_id=45] [region_id=44]
   > [2024/08/13 13:42:30.531 +00:00] [INFO] [raft.rs:902] ["45 received message from 45"] [term=6] [msg=MsgRequestVote] [from=45] [id=45] [raft_id=45] [region_id=44]
   > [2024/08/13 13:42:30.531 +00:00] [INFO] [raft.rs:874] ["became leader at term 6"] [term=6] [raft_id=45] [region_id=44]
   > [2024/08/13 13:42:31.593 +00:00] [INFO] [set.go:216] ["set global var"] [conn=4] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/08/13 13:42:31.595 +00:00] [INFO] [set.go:216] ["set global var"] [conn=4] [name=transaction_isolation] [val=REPEATABLE-READ]
