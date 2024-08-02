# Bug ID TIDB-21688-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/21688
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              Locking is different depending on whether the queried column is part of a point or a table scan.


## Details
 * Database: tidb-v4.0.7.tikv
 * Number of scenarios: 2
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
     - Instruction:  begin;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows: 0
 * Instruction #2:
     - Instruction:  begin;
     - Transaction: conn_1
     - Output: None
     - Executed order: 2
     - Affected rows: 0
 * Instruction #3:
     - Instruction:  update t set v = 10 where (k1, v) in ((1, null)); -- 0 row affected (point get)
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows: 0
 * Instruction #4:
     - Instruction:  update t set v = 11 where (k1, v) in ((1, null)); -- blocked
     - Transaction: conn_1
     - Output: None
     - Executed order: 5
     - Affected rows: 0
 * Instruction #5:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows: 0
 * Instruction #6:
     - Instruction:  commit;
     - Transaction: conn_1
     - Output: None
     - Executed order: 6
     - Affected rows: 0

 * Container logs:
   > [2024/08/02 13:40:15.168 +00:00] [INFO] [server.go:397] ["connection closed"] [conn=10]
   > [2024/08/02 13:40:15.172 +00:00] [INFO] [server.go:394] ["new connection"] [conn=11] [remoteAddr=127.0.0.1:48804]
   > [2024/08/02 13:40:15.175 +00:00] [INFO] [session.go:2159] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=45] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/08/02 13:40:15.185 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:66, Type:drop schema, State:none, SchemaState:none, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:15.14 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/02 13:40:15.185 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:66, Type:drop schema, State:none, SchemaState:none, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:15.14 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/08/02 13:40:15.187 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:drop schema, State:none, SchemaState:none, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:15.14 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:15.201 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=45] [neededSchemaVersion=46] ["start time"=1.863594ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/02 13:40:15.249 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=46] ["take time"=51.858886ms] [job="ID:66, Type:drop schema, State:running, SchemaState:write only, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:15.14 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:15.251 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:drop schema, State:running, SchemaState:write only, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:15.14 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:15.263 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=46] [neededSchemaVersion=47] ["start time"=422.893µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/02 13:40:15.313 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=47] ["take time"=51.876555ms] [job="ID:66, Type:drop schema, State:running, SchemaState:delete only, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:15.14 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:15.314 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:drop schema, State:running, SchemaState:delete only, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:15.14 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:15.329 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=47] [neededSchemaVersion=48] ["start time"=550.983µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/02 13:40:15.379 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=48] ["take time"=52.380606ms] [job="ID:66, Type:drop schema, State:done, SchemaState:none, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:15.14 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:15.381 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=66] [jobType="drop schema"]
   > [2024/08/02 13:40:15.382 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:drop schema, State:synced, SchemaState:none, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:15.14 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:15.390 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=66]
   > [2024/08/02 13:40:15.390 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/08/02 13:40:15.392 +00:00] [INFO] [session.go:2159] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=48] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/08/02 13:40:15.410 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:68, Type:create schema, State:none, SchemaState:none, SchemaID:67, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-02 13:40:15.39 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/02 13:40:15.410 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:68, Type:create schema, State:none, SchemaState:none, SchemaID:67, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-02 13:40:15.39 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/08/02 13:40:15.413 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:68, Type:create schema, State:none, SchemaState:none, SchemaID:67, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:15.39 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:15.427 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=48] [neededSchemaVersion=49] ["start time"=1.240604ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/02 13:40:15.476 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=49] ["take time"=52.675967ms] [job="ID:68, Type:create schema, State:done, SchemaState:public, SchemaID:67, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-02 13:40:15.39 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:15.480 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:68, Type:create schema, State:synced, SchemaState:public, SchemaID:67, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:15.39 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:15.489 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=68]
   > [2024/08/02 13:40:15.489 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/08/02 13:40:15.493 +00:00] [INFO] [session.go:2159] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=49] [cur_db=testdb] [sql="drop table if exists t;"] [user=root@127.0.0.1]
   > [2024/08/02 13:40:15.494 +00:00] [INFO] [session.go:2159] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=49] [cur_db=testdb] [sql="create table t (k1 int, k2 int, v int, unique key (k1));"] [user=root@127.0.0.1]
   > [2024/08/02 13:40:15.513 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:70, Type:create table, State:none, SchemaState:none, SchemaID:67, TableID:69, RowCount:0, ArgLen:1, start time: 2024-08-02 13:40:15.49 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/02 13:40:15.513 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:70, Type:create table, State:none, SchemaState:none, SchemaID:67, TableID:69, RowCount:0, ArgLen:1, start time: 2024-08-02 13:40:15.49 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t (k1 int, k2 int, v int, unique key (k1));"]
   > [2024/08/02 13:40:15.516 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:70, Type:create table, State:none, SchemaState:none, SchemaID:67, TableID:69, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:15.49 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:15.533 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=49] [neededSchemaVersion=50] ["start time"=1.61342ms] [phyTblIDs="[69]"] [actionTypes="[8]"]
   > [2024/08/02 13:40:15.582 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=50] ["take time"=52.026506ms] [job="ID:70, Type:create table, State:done, SchemaState:public, SchemaID:67, TableID:69, RowCount:0, ArgLen:1, start time: 2024-08-02 13:40:15.49 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:15.585 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:70, Type:create table, State:synced, SchemaState:public, SchemaID:67, TableID:69, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:15.49 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:15.596 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=70]
   > [2024/08/02 13:40:15.598 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/08/02 13:40:15.598 +00:00] [INFO] [split_region.go:58] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=748000000000000045]
   > [2024/08/02 13:40:15.598 +00:00] [INFO] [peer.rs:469] ["on split"] [split_keys="key 7480000000000000FF4500000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/02 13:40:15.599 +00:00] [INFO] [cluster_worker.go:131] ["alloc ids for region split"] [region-id=52] [peer-ids="[53]"]
   > [2024/08/02 13:40:15.599 +00:00] [INFO] [pd.rs:499] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF3F00000000000000F8 region_epoch { conf_ver: 1 version: 25 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 52 new_peer_ids: 53]"] [region_id=2]
   > [2024/08/02 13:40:15.602 +00:00] [INFO] [apply.rs:1162] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF4500000000000000F8 new_region_id: 52 new_peer_ids: 53 } right_derive: true }"] [index=74] [term=6] [peer_id=3] [region_id=2]
   > [2024/08/02 13:40:15.602 +00:00] [INFO] [apply.rs:1742] ["split region"] [keys="key 7480000000000000FF4500000000000000F8"] [region="id: 2 start_key: 7480000000000000FF3F00000000000000F8 region_epoch { conf_ver: 1 version: 25 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/08/02 13:40:15.605 +00:00] [INFO] [peer.rs:1731] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/08/02 13:40:15.605 +00:00] [INFO] [peer.rs:1773] ["insert new region"] [region="id: 52 start_key: 7480000000000000FF3F00000000000000F8 end_key: 7480000000000000FF4500000000000000F8 region_epoch { conf_ver: 1 version: 26 } peers { id: 53 store_id: 1 }"] [region_id=52]
   > [2024/08/02 13:40:15.605 +00:00] [INFO] [split_region.go:155] ["batch split regions complete"] ["batch region ID"=2] ["first at"=748000000000000045] ["first new region left"="{Id:52 StartKey:7480000000000000ff3f00000000000000f8 EndKey:7480000000000000ff4500000000000000f8 RegionEpoch:{ConfVer:1 Version:26} Peers:[id:53 store_id:1 ]}"] ["new region count"=1]
   > [2024/08/02 13:40:15.605 +00:00] [INFO] [split_region.go:207] ["split regions complete"] ["region count"=1] ["region IDs"="[52]"]
   > [2024/08/02 13:40:15.605 +00:00] [INFO] [peer.rs:159] ["create peer"] [peer_id=53] [region_id=52]
   > [2024/08/02 13:40:15.605 +00:00] [INFO] [raft.rs:783] ["became follower at term 5"] [term=5] [raft_id=53] [region_id=52]
   > [2024/08/02 13:40:15.606 +00:00] [INFO] [cluster.go:542] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF3F00000000000000F8} -> {7480000000000000FF4500000000000000F8}, EndKey:{}"] [old-version=25] [new-version=26]
   > [2024/08/02 13:40:15.606 +00:00] [INFO] [raft.rs:285] [newRaft] [peers="[(53, Progress { matched: 5, next_idx: 6, state: Probe, paused: false, pending_snapshot: 0, pending_request_snapshot: 0, recent_active: false, ins: Inflights { start: 0, count: 0, buffer: [] } })]"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=53] [region_id=52]
   > [2024/08/02 13:40:15.606 +00:00] [INFO] [raw_node.rs:222] ["RawNode created with id 53."] [id=53] [raft_id=53] [region_id=52]
   > [2024/08/02 13:40:15.606 +00:00] [INFO] [cluster_worker.go:223] ["region batch split, generate new regions"] [region-id=2] [origin="id:52 start_key:\"7480000000000000FF3F00000000000000F8\" end_key:\"7480000000000000FF4500000000000000F8\" region_epoch:<conf_ver:1 version:26 > peers:<id:53 store_id:1 >"] [total=1]
   > [2024/08/02 13:40:15.606 +00:00] [INFO] [raft.rs:1177] ["starting a new election"] [term=5] [raft_id=53] [region_id=52]
   > [2024/08/02 13:40:15.606 +00:00] [INFO] [raft.rs:833] ["became pre-candidate at term 5"] [term=5] [raft_id=53] [region_id=52]
   > [2024/08/02 13:40:15.606 +00:00] [INFO] [raft.rs:902] ["53 received message from 53"] [term=5] [msg=MsgRequestPreVote] [from=53] [id=53] [raft_id=53] [region_id=52]
   > [2024/08/02 13:40:15.606 +00:00] [INFO] [raft.rs:807] ["became candidate at term 6"] [term=6] [raft_id=53] [region_id=52]
   > [2024/08/02 13:40:15.606 +00:00] [INFO] [raft.rs:902] ["53 received message from 53"] [term=6] [msg=MsgRequestVote] [from=53] [id=53] [raft_id=53] [region_id=52]
   > [2024/08/02 13:40:15.606 +00:00] [INFO] [raft.rs:874] ["became leader at term 6"] [term=6] [raft_id=53] [region_id=52]
   > [2024/08/02 13:40:15.611 +00:00] [INFO] [process.rs:145] ["get snapshot failed"] [err="Request(message: \"EpochNotMatch current epoch of region 2 is conf_ver: 1 version: 26, but you sent conf_ver: 1 version: 25\" epoch_not_match { current_regions { id: 2 start_key: 7480000000000000FF4500000000000000F8 region_epoch { conf_ver: 1 version: 26 } peers { id: 3 store_id: 1 } } current_regions { id: 52 start_key: 7480000000000000FF3F00000000000000F8 end_key: 7480000000000000FF4500000000000000F8 region_epoch { conf_ver: 1 version: 26 } peers { id: 53 store_id: 1 } } })"] [cid=449]
   > [2024/08/02 13:40:15.663 +00:00] [INFO] [server.go:397] ["connection closed"] [conn=11]
   > [2024/08/02 13:40:16.674 +00:00] [INFO] [server.go:394] ["new connection"] [conn=12] [remoteAddr=127.0.0.1:48812]
   > [2024/08/02 13:40:16.683 +00:00] [INFO] [set.go:216] ["set session var"] [conn=12] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/08/02 13:40:16.704 +00:00] [INFO] [set.go:216] ["set global var"] [conn=12] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/08/02 13:40:16.712 +00:00] [INFO] [set.go:216] ["set global var"] [conn=12] [name=transaction_isolation] [val=READ-COMMITTED]
   > [2024/08/02 13:40:17.284 +00:00] [INFO] [server.go:394] ["new connection"] [conn=13] [remoteAddr=127.0.0.1:48826]
   > [2024/08/02 13:40:17.288 +00:00] [INFO] [set.go:216] ["set session var"] [conn=13] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/08/02 13:40:18.195 +00:00] [INFO] [adapter.go:611] ["pessimistic write conflict, retry statement"] [conn=13] [txn=451570831783362568] [forUpdateTS=451570831940648961] [err="[kv:9007]Write conflict, txnStartTS=451570831783362568, conflictStartTS=451570831704719361, conflictCommitTS=451570832032399361, key={tableID=69, handle=1} primary={tableID=69, handle=1} [try again later]"]
   > [2024/08/02 13:40:18.884 +00:00] [INFO] [server.go:397] ["connection closed"] [conn=13]
   > [2024/08/02 13:40:18.885 +00:00] [INFO] [server.go:397] ["connection closed"] [conn=12]

### Scenario 1
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows: 0
 * Instruction #1:
     - Instruction:  begin;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows: 0
 * Instruction #2:
     - Instruction:  begin;
     - Transaction: conn_1
     - Output: None
     - Executed order: 2
     - Affected rows: 0
 * Instruction #3:
     - Instruction:  update t set v = 10 where (k2, v) in ((1, null)); -- 0 row affected (table scan...
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows: 0
 * Instruction #4:
     - Instruction:  update t set v = 11 where (k2, v) in ((1, null)); -- won't be blocked
     - Transaction: conn_1
     - Output: None
     - Executed order: 4
     - Affected rows: 0
 * Instruction #5:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: None
     - Executed order: 5
     - Affected rows: 0
 * Instruction #6:
     - Instruction:  commit;
     - Transaction: conn_1
     - Output: None
     - Executed order: 6
     - Affected rows: 0

 * Container logs:
   > [2024/08/02 13:40:20.479 +00:00] [INFO] [server.go:397] ["connection closed"] [conn=14]
   > [2024/08/02 13:40:20.480 +00:00] [INFO] [server.go:394] ["new connection"] [conn=15] [remoteAddr=127.0.0.1:55084]
   > [2024/08/02 13:40:20.482 +00:00] [INFO] [session.go:2159] ["CRUCIAL OPERATION"] [conn=15] [schemaVersion=58] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/08/02 13:40:20.498 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:77, Type:drop schema, State:none, SchemaState:none, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:20.44 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/02 13:40:20.498 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:77, Type:drop schema, State:none, SchemaState:none, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:20.44 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/08/02 13:40:20.501 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:none, SchemaState:none, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:20.44 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:20.514 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=58] [neededSchemaVersion=59] ["start time"=478.278µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/02 13:40:20.564 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=59] ["take time"=52.161162ms] [job="ID:77, Type:drop schema, State:running, SchemaState:write only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:20.44 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:20.566 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:running, SchemaState:write only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:20.44 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:20.578 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=59] [neededSchemaVersion=60] ["start time"=577.733µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/02 13:40:20.628 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=60] ["take time"=51.903375ms] [job="ID:77, Type:drop schema, State:running, SchemaState:delete only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:20.44 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:20.629 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:running, SchemaState:delete only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:20.44 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:20.645 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=60] [neededSchemaVersion=61] ["start time"=625.645µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/02 13:40:20.694 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=61] ["take time"=51.980481ms] [job="ID:77, Type:drop schema, State:done, SchemaState:none, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:20.44 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:20.696 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=77] [jobType="drop schema"]
   > [2024/08/02 13:40:20.697 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:synced, SchemaState:none, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:20.44 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:20.707 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=77]
   > [2024/08/02 13:40:20.707 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/08/02 13:40:20.709 +00:00] [INFO] [session.go:2159] ["CRUCIAL OPERATION"] [conn=15] [schemaVersion=61] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/08/02 13:40:20.726 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:79, Type:create schema, State:none, SchemaState:none, SchemaID:78, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-02 13:40:20.69 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/02 13:40:20.726 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:79, Type:create schema, State:none, SchemaState:none, SchemaID:78, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-02 13:40:20.69 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/08/02 13:40:20.730 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:79, Type:create schema, State:none, SchemaState:none, SchemaID:78, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:20.69 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:20.743 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=61] [neededSchemaVersion=62] ["start time"=1.140939ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/02 13:40:20.792 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=62] ["take time"=52.148171ms] [job="ID:79, Type:create schema, State:done, SchemaState:public, SchemaID:78, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-02 13:40:20.69 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:20.795 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:79, Type:create schema, State:synced, SchemaState:public, SchemaID:78, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:20.69 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:20.803 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=79]
   > [2024/08/02 13:40:20.803 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/08/02 13:40:20.807 +00:00] [INFO] [session.go:2159] ["CRUCIAL OPERATION"] [conn=15] [schemaVersion=62] [cur_db=testdb] [sql="drop table if exists t;"] [user=root@127.0.0.1]
   > [2024/08/02 13:40:20.808 +00:00] [INFO] [session.go:2159] ["CRUCIAL OPERATION"] [conn=15] [schemaVersion=62] [cur_db=testdb] [sql="create table t (k1 int, k2 int, v int, unique key (k1));"] [user=root@127.0.0.1]
   > [2024/08/02 13:40:20.825 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:81, Type:create table, State:none, SchemaState:none, SchemaID:78, TableID:80, RowCount:0, ArgLen:1, start time: 2024-08-02 13:40:20.79 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/02 13:40:20.825 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:81, Type:create table, State:none, SchemaState:none, SchemaID:78, TableID:80, RowCount:0, ArgLen:1, start time: 2024-08-02 13:40:20.79 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t (k1 int, k2 int, v int, unique key (k1));"]
   > [2024/08/02 13:40:20.828 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:81, Type:create table, State:none, SchemaState:none, SchemaID:78, TableID:80, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:20.79 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:20.842 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=62] [neededSchemaVersion=63] ["start time"=1.594284ms] [phyTblIDs="[80]"] [actionTypes="[8]"]
   > [2024/08/02 13:40:20.891 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=63] ["take time"=52.410498ms] [job="ID:81, Type:create table, State:done, SchemaState:public, SchemaID:78, TableID:80, RowCount:0, ArgLen:1, start time: 2024-08-02 13:40:20.79 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:20.894 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:81, Type:create table, State:synced, SchemaState:public, SchemaID:78, TableID:80, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:20.79 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:20.905 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=81]
   > [2024/08/02 13:40:20.907 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/08/02 13:40:20.907 +00:00] [INFO] [split_region.go:58] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=748000000000000050]
   > [2024/08/02 13:40:20.908 +00:00] [INFO] [peer.rs:469] ["on split"] [split_keys="key 7480000000000000FF5000000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/02 13:40:20.908 +00:00] [INFO] [cluster_worker.go:131] ["alloc ids for region split"] [region-id=56] [peer-ids="[57]"]
   > [2024/08/02 13:40:20.909 +00:00] [INFO] [pd.rs:499] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF4A00000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 56 new_peer_ids: 57]"] [region_id=2]
   > [2024/08/02 13:40:20.911 +00:00] [INFO] [apply.rs:1162] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF5000000000000000F8 new_region_id: 56 new_peer_ids: 57 } right_derive: true }"] [index=87] [term=6] [peer_id=3] [region_id=2]
   > [2024/08/02 13:40:20.911 +00:00] [INFO] [apply.rs:1742] ["split region"] [keys="key 7480000000000000FF5000000000000000F8"] [region="id: 2 start_key: 7480000000000000FF4A00000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/08/02 13:40:20.914 +00:00] [INFO] [peer.rs:1731] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/08/02 13:40:20.914 +00:00] [INFO] [peer.rs:1773] ["insert new region"] [region="id: 56 start_key: 7480000000000000FF4A00000000000000F8 end_key: 7480000000000000FF5000000000000000F8 region_epoch { conf_ver: 1 version: 28 } peers { id: 57 store_id: 1 }"] [region_id=56]
   > [2024/08/02 13:40:20.914 +00:00] [INFO] [peer.rs:159] ["create peer"] [peer_id=57] [region_id=56]
   > [2024/08/02 13:40:20.914 +00:00] [INFO] [split_region.go:155] ["batch split regions complete"] ["batch region ID"=2] ["first at"=748000000000000050] ["first new region left"="{Id:56 StartKey:7480000000000000ff4a00000000000000f8 EndKey:7480000000000000ff5000000000000000f8 RegionEpoch:{ConfVer:1 Version:28} Peers:[id:57 store_id:1 ]}"] ["new region count"=1]
   > [2024/08/02 13:40:20.914 +00:00] [INFO] [split_region.go:207] ["split regions complete"] ["region count"=1] ["region IDs"="[56]"]
   > [2024/08/02 13:40:20.914 +00:00] [INFO] [cluster.go:542] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF4A00000000000000F8} -> {7480000000000000FF5000000000000000F8}, EndKey:{}"] [old-version=27] [new-version=28]
   > [2024/08/02 13:40:20.914 +00:00] [INFO] [cluster_worker.go:223] ["region batch split, generate new regions"] [region-id=2] [origin="id:56 start_key:\"7480000000000000FF4A00000000000000F8\" end_key:\"7480000000000000FF5000000000000000F8\" region_epoch:<conf_ver:1 version:28 > peers:<id:57 store_id:1 >"] [total=1]
   > [2024/08/02 13:40:20.915 +00:00] [INFO] [raft.rs:783] ["became follower at term 5"] [term=5] [raft_id=57] [region_id=56]
   > [2024/08/02 13:40:20.915 +00:00] [INFO] [raft.rs:285] [newRaft] [peers="[(57, Progress { matched: 5, next_idx: 6, state: Probe, paused: false, pending_snapshot: 0, pending_request_snapshot: 0, recent_active: false, ins: Inflights { start: 0, count: 0, buffer: [] } })]"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=57] [region_id=56]
   > [2024/08/02 13:40:20.916 +00:00] [INFO] [raw_node.rs:222] ["RawNode created with id 57."] [id=57] [raft_id=57] [region_id=56]
   > [2024/08/02 13:40:20.916 +00:00] [INFO] [raft.rs:1177] ["starting a new election"] [term=5] [raft_id=57] [region_id=56]
   > [2024/08/02 13:40:20.916 +00:00] [INFO] [raft.rs:833] ["became pre-candidate at term 5"] [term=5] [raft_id=57] [region_id=56]
   > [2024/08/02 13:40:20.916 +00:00] [INFO] [raft.rs:902] ["57 received message from 57"] [term=5] [msg=MsgRequestPreVote] [from=57] [id=57] [raft_id=57] [region_id=56]
   > [2024/08/02 13:40:20.916 +00:00] [INFO] [raft.rs:807] ["became candidate at term 6"] [term=6] [raft_id=57] [region_id=56]
   > [2024/08/02 13:40:20.916 +00:00] [INFO] [raft.rs:902] ["57 received message from 57"] [term=6] [msg=MsgRequestVote] [from=57] [id=57] [raft_id=57] [region_id=56]
   > [2024/08/02 13:40:20.916 +00:00] [INFO] [raft.rs:874] ["became leader at term 6"] [term=6] [raft_id=57] [region_id=56]
   > [2024/08/02 13:40:20.920 +00:00] [INFO] [process.rs:145] ["get snapshot failed"] [err="Request(message: \"EpochNotMatch current epoch of region 2 is conf_ver: 1 version: 28, but you sent conf_ver: 1 version: 27\" epoch_not_match { current_regions { id: 2 start_key: 7480000000000000FF5000000000000000F8 region_epoch { conf_ver: 1 version: 28 } peers { id: 3 store_id: 1 } } current_regions { id: 56 start_key: 7480000000000000FF4A00000000000000F8 end_key: 7480000000000000FF5000000000000000F8 region_epoch { conf_ver: 1 version: 28 } peers { id: 57 store_id: 1 } } })"] [cid=554]
   > [2024/08/02 13:40:20.931 +00:00] [INFO] [server.go:397] ["connection closed"] [conn=15]
   > [2024/08/02 13:40:21.941 +00:00] [INFO] [server.go:394] ["new connection"] [conn=16] [remoteAddr=127.0.0.1:55100]
   > [2024/08/02 13:40:21.951 +00:00] [INFO] [set.go:216] ["set session var"] [conn=16] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/08/02 13:40:21.954 +00:00] [INFO] [set.go:216] ["set global var"] [conn=16] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/08/02 13:40:21.956 +00:00] [INFO] [set.go:216] ["set global var"] [conn=16] [name=transaction_isolation] [val=READ-COMMITTED]
   > [2024/08/02 13:40:22.551 +00:00] [INFO] [server.go:394] ["new connection"] [conn=17] [remoteAddr=127.0.0.1:55104]
   > [2024/08/02 13:40:22.555 +00:00] [INFO] [set.go:216] ["set session var"] [conn=17] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/08/02 13:40:24.152 +00:00] [INFO] [server.go:397] ["connection closed"] [conn=16]
   > [2024/08/02 13:40:24.152 +00:00] [INFO] [server.go:397] ["connection closed"] [conn=17]
