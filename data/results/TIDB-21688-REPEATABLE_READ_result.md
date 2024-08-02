# Bug ID TIDB-21688-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/21688
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              Locking is different depending on whether the queried column is part of a point or a table scan.


## Details
 * Database: tidb-v4.0.7.tikv
 * Number of scenarios: 2
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
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
   > [2024/08/02 13:40:04.970 +00:00] [INFO] [server.go:394] ["new connection"] [conn=2] [remoteAddr=127.0.0.1:57140]
   > [2024/08/02 13:40:04.972 +00:00] [INFO] [session.go:2159] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=22] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/08/02 13:40:04.973 +00:00] [INFO] [session.go:2159] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=22] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/08/02 13:40:05.003 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-02 13:40:04.94 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/02 13:40:05.004 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-02 13:40:04.94 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/08/02 13:40:05.007 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:04.94 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:05.027 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=22] [neededSchemaVersion=23] ["start time"=1.11824ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/02 13:40:05.076 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=23] ["take time"=52.416294ms] [job="ID:46, Type:create schema, State:done, SchemaState:public, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-02 13:40:04.94 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:05.079 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:46, Type:create schema, State:synced, SchemaState:public, SchemaID:45, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:04.94 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:05.095 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=46]
   > [2024/08/02 13:40:05.095 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/08/02 13:40:05.099 +00:00] [INFO] [session.go:2159] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=23] [cur_db=testdb] [sql="drop table if exists t;"] [user=root@127.0.0.1]
   > [2024/08/02 13:40:05.100 +00:00] [INFO] [session.go:2159] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=23] [cur_db=testdb] [sql="create table t (k1 int, k2 int, v int, unique key (k1));"] [user=root@127.0.0.1]
   > [2024/08/02 13:40:05.132 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-08-02 13:40:05.09 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/02 13:40:05.132 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-08-02 13:40:05.09 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t (k1 int, k2 int, v int, unique key (k1));"]
   > [2024/08/02 13:40:05.135 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:05.09 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:05.170 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=23] [neededSchemaVersion=24] ["start time"=1.894116ms] [phyTblIDs="[47]"] [actionTypes="[8]"]
   > [2024/08/02 13:40:05.218 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=24] ["take time"=52.344428ms] [job="ID:48, Type:create table, State:done, SchemaState:public, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-08-02 13:40:05.09 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:05.221 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:48, Type:create table, State:synced, SchemaState:public, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:05.09 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:05.247 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=48]
   > [2024/08/02 13:40:05.249 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/08/02 13:40:05.250 +00:00] [INFO] [split_region.go:58] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=74800000000000002f]
   > [2024/08/02 13:40:05.250 +00:00] [INFO] [peer.rs:469] ["on split"] [split_keys="key 7480000000000000FF2F00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/02 13:40:05.251 +00:00] [INFO] [cluster_worker.go:131] ["alloc ids for region split"] [region-id=44] [peer-ids="[45]"]
   > [2024/08/02 13:40:05.251 +00:00] [INFO] [pd.rs:499] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF2B00000000000000F8 region_epoch { conf_ver: 1 version: 21 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 44 new_peer_ids: 45]"] [region_id=2]
   > [2024/08/02 13:40:05.260 +00:00] [INFO] [apply.rs:1162] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF2F00000000000000F8 new_region_id: 44 new_peer_ids: 45 } right_derive: true }"] [index=53] [term=6] [peer_id=3] [region_id=2]
   > [2024/08/02 13:40:05.261 +00:00] [INFO] [apply.rs:1742] ["split region"] [keys="key 7480000000000000FF2F00000000000000F8"] [region="id: 2 start_key: 7480000000000000FF2B00000000000000F8 region_epoch { conf_ver: 1 version: 21 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/08/02 13:40:05.270 +00:00] [INFO] [peer.rs:1731] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/08/02 13:40:05.270 +00:00] [INFO] [peer.rs:1773] ["insert new region"] [region="id: 44 start_key: 7480000000000000FF2B00000000000000F8 end_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 45 store_id: 1 }"] [region_id=44]
   > [2024/08/02 13:40:05.270 +00:00] [INFO] [peer.rs:159] ["create peer"] [peer_id=45] [region_id=44]
   > [2024/08/02 13:40:05.271 +00:00] [INFO] [split_region.go:155] ["batch split regions complete"] ["batch region ID"=2] ["first at"=74800000000000002f] ["first new region left"="{Id:44 StartKey:7480000000000000ff2b00000000000000f8 EndKey:7480000000000000ff2f00000000000000f8 RegionEpoch:{ConfVer:1 Version:22} Peers:[id:45 store_id:1 ]}"] ["new region count"=1]
   > [2024/08/02 13:40:05.271 +00:00] [INFO] [raft.rs:783] ["became follower at term 5"] [term=5] [raft_id=45] [region_id=44]
   > [2024/08/02 13:40:05.271 +00:00] [INFO] [split_region.go:207] ["split regions complete"] ["region count"=1] ["region IDs"="[44]"]
   > [2024/08/02 13:40:05.271 +00:00] [INFO] [raft.rs:285] [newRaft] [peers="[(45, Progress { matched: 5, next_idx: 6, state: Probe, paused: false, pending_snapshot: 0, pending_request_snapshot: 0, recent_active: false, ins: Inflights { start: 0, count: 0, buffer: [] } })]"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=45] [region_id=44]
   > [2024/08/02 13:40:05.271 +00:00] [INFO] [cluster.go:542] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF2B00000000000000F8} -> {7480000000000000FF2F00000000000000F8}, EndKey:{}"] [old-version=21] [new-version=22]
   > [2024/08/02 13:40:05.271 +00:00] [INFO] [raw_node.rs:222] ["RawNode created with id 45."] [id=45] [raft_id=45] [region_id=44]
   > [2024/08/02 13:40:05.271 +00:00] [INFO] [raft.rs:1177] ["starting a new election"] [term=5] [raft_id=45] [region_id=44]
   > [2024/08/02 13:40:05.271 +00:00] [INFO] [raft.rs:833] ["became pre-candidate at term 5"] [term=5] [raft_id=45] [region_id=44]
   > [2024/08/02 13:40:05.271 +00:00] [INFO] [cluster_worker.go:223] ["region batch split, generate new regions"] [region-id=2] [origin="id:44 start_key:\"7480000000000000FF2B00000000000000F8\" end_key:\"7480000000000000FF2F00000000000000F8\" region_epoch:<conf_ver:1 version:22 > peers:<id:45 store_id:1 >"] [total=1]
   > [2024/08/02 13:40:05.271 +00:00] [INFO] [raft.rs:902] ["45 received message from 45"] [term=5] [msg=MsgRequestPreVote] [from=45] [id=45] [raft_id=45] [region_id=44]
   > [2024/08/02 13:40:05.271 +00:00] [INFO] [raft.rs:807] ["became candidate at term 6"] [term=6] [raft_id=45] [region_id=44]
   > [2024/08/02 13:40:05.271 +00:00] [INFO] [raft.rs:902] ["45 received message from 45"] [term=6] [msg=MsgRequestVote] [from=45] [id=45] [raft_id=45] [region_id=44]
   > [2024/08/02 13:40:05.271 +00:00] [INFO] [raft.rs:874] ["became leader at term 6"] [term=6] [raft_id=45] [region_id=44]
   > [2024/08/02 13:40:05.281 +00:00] [INFO] [process.rs:145] ["get snapshot failed"] [err="Request(message: \"EpochNotMatch current epoch of region 2 is conf_ver: 1 version: 22, but you sent conf_ver: 1 version: 21\" epoch_not_match { current_regions { id: 2 start_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 3 store_id: 1 } } current_regions { id: 44 start_key: 7480000000000000FF2B00000000000000F8 end_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 45 store_id: 1 } } })"] [cid=256]
   > [2024/08/02 13:40:05.301 +00:00] [INFO] [server.go:397] ["connection closed"] [conn=2]
   > [2024/08/02 13:40:06.319 +00:00] [INFO] [server.go:394] ["new connection"] [conn=4] [remoteAddr=127.0.0.1:57156]
   > [2024/08/02 13:40:06.322 +00:00] [INFO] [set.go:216] ["set session var"] [conn=4] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/08/02 13:40:06.325 +00:00] [INFO] [set.go:216] ["set global var"] [conn=4] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/08/02 13:40:06.327 +00:00] [INFO] [set.go:216] ["set global var"] [conn=4] [name=transaction_isolation] [val=REPEATABLE-READ]
   > [2024/08/02 13:40:06.927 +00:00] [INFO] [server.go:394] ["new connection"] [conn=5] [remoteAddr=127.0.0.1:57160]
   > [2024/08/02 13:40:06.937 +00:00] [INFO] [set.go:216] ["set session var"] [conn=5] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/08/02 13:40:07.844 +00:00] [INFO] [adapter.go:611] ["pessimistic write conflict, retry statement"] [conn=5] [txn=451570829070172168] [forUpdateTS=451570829227458561] [err="[kv:9007]Write conflict, txnStartTS=451570829070172168, conflictStartTS=451570828991528961, conflictCommitTS=451570829319208961, key={tableID=47, handle=1} primary={tableID=47, handle=1} [try again later]"]
   > [2024/08/02 13:40:08.529 +00:00] [INFO] [server.go:397] ["connection closed"] [conn=5]
   > [2024/08/02 13:40:08.529 +00:00] [INFO] [server.go:397] ["connection closed"] [conn=4]

### Scenario 1
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
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
   > [2024/08/02 13:40:09.952 +00:00] [INFO] [server.go:397] ["connection closed"] [conn=6]
   > [2024/08/02 13:40:09.954 +00:00] [INFO] [server.go:394] ["new connection"] [conn=7] [remoteAddr=127.0.0.1:48768]
   > [2024/08/02 13:40:09.956 +00:00] [INFO] [session.go:2159] ["CRUCIAL OPERATION"] [conn=7] [schemaVersion=32] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/08/02 13:40:09.972 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:55, Type:drop schema, State:none, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:09.94 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/02 13:40:09.972 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:55, Type:drop schema, State:none, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:09.94 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/08/02 13:40:09.976 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:55, Type:drop schema, State:none, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:09.94 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:09.989 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=32] [neededSchemaVersion=33] ["start time"=629.277µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/02 13:40:10.039 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=33] ["take time"=52.511978ms] [job="ID:55, Type:drop schema, State:running, SchemaState:write only, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:09.94 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:10.040 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:55, Type:drop schema, State:running, SchemaState:write only, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:09.94 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:10.052 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=33] [neededSchemaVersion=34] ["start time"=610.978µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/02 13:40:10.102 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=34] ["take time"=52.174083ms] [job="ID:55, Type:drop schema, State:running, SchemaState:delete only, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:09.94 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:10.104 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:55, Type:drop schema, State:running, SchemaState:delete only, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:09.94 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:10.120 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=34] [neededSchemaVersion=35] ["start time"=638.216µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/02 13:40:10.169 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=35] ["take time"=52.417901ms] [job="ID:55, Type:drop schema, State:done, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:09.94 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:10.172 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=55] [jobType="drop schema"]
   > [2024/08/02 13:40:10.173 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:55, Type:drop schema, State:synced, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:09.94 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:10.182 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=55]
   > [2024/08/02 13:40:10.182 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/08/02 13:40:10.184 +00:00] [INFO] [session.go:2159] ["CRUCIAL OPERATION"] [conn=7] [schemaVersion=35] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/08/02 13:40:10.201 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:57, Type:create schema, State:none, SchemaState:none, SchemaID:56, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-02 13:40:10.19 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/02 13:40:10.201 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:57, Type:create schema, State:none, SchemaState:none, SchemaID:56, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-02 13:40:10.19 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/08/02 13:40:10.205 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:57, Type:create schema, State:none, SchemaState:none, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:10.19 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:10.217 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=35] [neededSchemaVersion=36] ["start time"=793.056µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/02 13:40:10.266 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=36] ["take time"=51.92789ms] [job="ID:57, Type:create schema, State:done, SchemaState:public, SchemaID:56, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-02 13:40:10.19 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:10.269 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:57, Type:create schema, State:synced, SchemaState:public, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:10.19 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:10.279 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=57]
   > [2024/08/02 13:40:10.279 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/08/02 13:40:10.282 +00:00] [INFO] [session.go:2159] ["CRUCIAL OPERATION"] [conn=7] [schemaVersion=36] [cur_db=testdb] [sql="drop table if exists t;"] [user=root@127.0.0.1]
   > [2024/08/02 13:40:10.283 +00:00] [INFO] [session.go:2159] ["CRUCIAL OPERATION"] [conn=7] [schemaVersion=36] [cur_db=testdb] [sql="create table t (k1 int, k2 int, v int, unique key (k1));"] [user=root@127.0.0.1]
   > [2024/08/02 13:40:10.300 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:59, Type:create table, State:none, SchemaState:none, SchemaID:56, TableID:58, RowCount:0, ArgLen:1, start time: 2024-08-02 13:40:10.29 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/02 13:40:10.300 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:59, Type:create table, State:none, SchemaState:none, SchemaID:56, TableID:58, RowCount:0, ArgLen:1, start time: 2024-08-02 13:40:10.29 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t (k1 int, k2 int, v int, unique key (k1));"]
   > [2024/08/02 13:40:10.303 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:59, Type:create table, State:none, SchemaState:none, SchemaID:56, TableID:58, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:10.29 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:10.319 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=36] [neededSchemaVersion=37] ["start time"=2.196671ms] [phyTblIDs="[58]"] [actionTypes="[8]"]
   > [2024/08/02 13:40:10.367 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=37] ["take time"=52.16193ms] [job="ID:59, Type:create table, State:done, SchemaState:public, SchemaID:56, TableID:58, RowCount:0, ArgLen:1, start time: 2024-08-02 13:40:10.29 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:10.370 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:59, Type:create table, State:synced, SchemaState:public, SchemaID:56, TableID:58, RowCount:0, ArgLen:0, start time: 2024-08-02 13:40:10.29 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 13:40:10.379 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=59]
   > [2024/08/02 13:40:10.381 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/08/02 13:40:10.381 +00:00] [INFO] [split_region.go:58] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=74800000000000003a]
   > [2024/08/02 13:40:10.382 +00:00] [INFO] [peer.rs:469] ["on split"] [split_keys="key 7480000000000000FF3A00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/02 13:40:10.382 +00:00] [INFO] [cluster_worker.go:131] ["alloc ids for region split"] [region-id=48] [peer-ids="[49]"]
   > [2024/08/02 13:40:10.382 +00:00] [INFO] [pd.rs:499] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF3400000000000000F8 region_epoch { conf_ver: 1 version: 23 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 48 new_peer_ids: 49]"] [region_id=2]
   > [2024/08/02 13:40:10.385 +00:00] [INFO] [apply.rs:1162] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF3A00000000000000F8 new_region_id: 48 new_peer_ids: 49 } right_derive: true }"] [index=67] [term=6] [peer_id=3] [region_id=2]
   > [2024/08/02 13:40:10.385 +00:00] [INFO] [apply.rs:1742] ["split region"] [keys="key 7480000000000000FF3A00000000000000F8"] [region="id: 2 start_key: 7480000000000000FF3400000000000000F8 region_epoch { conf_ver: 1 version: 23 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/08/02 13:40:10.387 +00:00] [INFO] [peer.rs:1731] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/08/02 13:40:10.387 +00:00] [INFO] [peer.rs:1773] ["insert new region"] [region="id: 48 start_key: 7480000000000000FF3400000000000000F8 end_key: 7480000000000000FF3A00000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 49 store_id: 1 }"] [region_id=48]
   > [2024/08/02 13:40:10.387 +00:00] [INFO] [peer.rs:159] ["create peer"] [peer_id=49] [region_id=48]
   > [2024/08/02 13:40:10.387 +00:00] [INFO] [split_region.go:155] ["batch split regions complete"] ["batch region ID"=2] ["first at"=74800000000000003a] ["first new region left"="{Id:48 StartKey:7480000000000000ff3400000000000000f8 EndKey:7480000000000000ff3a00000000000000f8 RegionEpoch:{ConfVer:1 Version:24} Peers:[id:49 store_id:1 ]}"] ["new region count"=1]
   > [2024/08/02 13:40:10.387 +00:00] [INFO] [split_region.go:207] ["split regions complete"] ["region count"=1] ["region IDs"="[48]"]
   > [2024/08/02 13:40:10.388 +00:00] [INFO] [cluster.go:542] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF3400000000000000F8} -> {7480000000000000FF3A00000000000000F8}, EndKey:{}"] [old-version=23] [new-version=24]
   > [2024/08/02 13:40:10.388 +00:00] [INFO] [cluster_worker.go:223] ["region batch split, generate new regions"] [region-id=2] [origin="id:48 start_key:\"7480000000000000FF3400000000000000F8\" end_key:\"7480000000000000FF3A00000000000000F8\" region_epoch:<conf_ver:1 version:24 > peers:<id:49 store_id:1 >"] [total=1]
   > [2024/08/02 13:40:10.389 +00:00] [INFO] [raft.rs:783] ["became follower at term 5"] [term=5] [raft_id=49] [region_id=48]
   > [2024/08/02 13:40:10.389 +00:00] [INFO] [raft.rs:285] [newRaft] [peers="[(49, Progress { matched: 5, next_idx: 6, state: Probe, paused: false, pending_snapshot: 0, pending_request_snapshot: 0, recent_active: false, ins: Inflights { start: 0, count: 0, buffer: [] } })]"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=49] [region_id=48]
   > [2024/08/02 13:40:10.389 +00:00] [INFO] [raw_node.rs:222] ["RawNode created with id 49."] [id=49] [raft_id=49] [region_id=48]
   > [2024/08/02 13:40:10.389 +00:00] [INFO] [raft.rs:1177] ["starting a new election"] [term=5] [raft_id=49] [region_id=48]
   > [2024/08/02 13:40:10.390 +00:00] [INFO] [raft.rs:833] ["became pre-candidate at term 5"] [term=5] [raft_id=49] [region_id=48]
   > [2024/08/02 13:40:10.390 +00:00] [INFO] [raft.rs:902] ["49 received message from 49"] [term=5] [msg=MsgRequestPreVote] [from=49] [id=49] [raft_id=49] [region_id=48]
   > [2024/08/02 13:40:10.390 +00:00] [INFO] [raft.rs:807] ["became candidate at term 6"] [term=6] [raft_id=49] [region_id=48]
   > [2024/08/02 13:40:10.390 +00:00] [INFO] [raft.rs:902] ["49 received message from 49"] [term=6] [msg=MsgRequestVote] [from=49] [id=49] [raft_id=49] [region_id=48]
   > [2024/08/02 13:40:10.390 +00:00] [INFO] [raft.rs:874] ["became leader at term 6"] [term=6] [raft_id=49] [region_id=48]
   > [2024/08/02 13:40:10.392 +00:00] [INFO] [process.rs:145] ["get snapshot failed"] [err="Request(message: \"EpochNotMatch current epoch of region 2 is conf_ver: 1 version: 24, but you sent conf_ver: 1 version: 23\" epoch_not_match { current_regions { id: 2 start_key: 7480000000000000FF3A00000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 3 store_id: 1 } } current_regions { id: 48 start_key: 7480000000000000FF3400000000000000F8 end_key: 7480000000000000FF3A00000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 49 store_id: 1 } } })"] [cid=357]
   > [2024/08/02 13:40:10.402 +00:00] [INFO] [server.go:397] ["connection closed"] [conn=7]
   > [2024/08/02 13:40:11.412 +00:00] [INFO] [server.go:394] ["new connection"] [conn=8] [remoteAddr=127.0.0.1:48782]
   > [2024/08/02 13:40:11.422 +00:00] [INFO] [set.go:216] ["set session var"] [conn=8] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/08/02 13:40:11.426 +00:00] [INFO] [set.go:216] ["set global var"] [conn=8] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/08/02 13:40:11.428 +00:00] [INFO] [set.go:216] ["set global var"] [conn=8] [name=transaction_isolation] [val=REPEATABLE-READ]
   > [2024/08/02 13:40:12.022 +00:00] [INFO] [server.go:394] ["new connection"] [conn=9] [remoteAddr=127.0.0.1:48784]
   > [2024/08/02 13:40:12.026 +00:00] [INFO] [set.go:216] ["set session var"] [conn=9] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/08/02 13:40:13.623 +00:00] [INFO] [server.go:397] ["connection closed"] [conn=8]
   > [2024/08/02 13:40:13.623 +00:00] [INFO] [server.go:397] ["connection closed"] [conn=9]
