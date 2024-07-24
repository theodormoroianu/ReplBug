# Bug ID TIDB-21447-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/21447
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              read using different executors in transaction result in different results


## Details
 * Database: tidb-v4.0.8.tikv
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
     - Instruction:  select * from t1 where id = 1; -- the result is "1 abc" before the update commi...
     - Transaction: conn_1
     - Output: [(1, 'abc')]
     - Executed order: 3
     - Affected rows: 1
 * Instruction #4:
     - Instruction:  UPDATE t1 SET name='xyz' WHERE id=1;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows: 1
 * Instruction #5:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: None
     - Executed order: 5
     - Affected rows: 0
 * Instruction #6:
     - Instruction:  UPDATE t1 SET name='xyz' WHERE id=1; -- update the same row with same value usi...
     - Transaction: conn_1
     - Output: None
     - Executed order: 6
     - Affected rows: 0
 * Instruction #7:
     - Instruction:  select * from t1;        -- the result is "1, abc"
     - Transaction: conn_1
     - Output: [(1, 'abc')]
     - Executed order: 7
     - Affected rows: 1
 * Instruction #8:
     - Instruction:  select * from t1 where id = 1 ; -- the result is "1, xyz"
     - Transaction: conn_1
     - Output: [(1, 'xyz')]
     - Executed order: 8
     - Affected rows: 1
 * Instruction #9:
     - Instruction:  commit;
     - Transaction: conn_1
     - Output: None
     - Executed order: 9
     - Affected rows: 0

 * Container logs:
   > [2024/07/24 11:27:35.624 +00:00] [INFO] [session.go:2161] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=45] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.62]
   > [2024/07/24 11:27:35.647 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:66, Type:drop schema, State:none, SchemaState:none, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:27:35.6 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 11:27:35.647 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:66, Type:drop schema, State:none, SchemaState:none, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:27:35.6 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/24 11:27:35.650 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:drop schema, State:none, SchemaState:none, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:27:35.6 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:27:35.674 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=45] [neededSchemaVersion=46] ["start time"=638.215µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 11:27:35.724 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=46] ["take time"=52.741345ms] [job="ID:66, Type:drop schema, State:running, SchemaState:write only, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:27:35.6 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:27:35.725 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:drop schema, State:running, SchemaState:write only, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:27:35.6 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:27:35.747 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=46] [neededSchemaVersion=47] ["start time"=656.305µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 11:27:35.797 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=47] ["take time"=52.18645ms] [job="ID:66, Type:drop schema, State:running, SchemaState:delete only, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:27:35.6 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:27:35.799 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:drop schema, State:running, SchemaState:delete only, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:27:35.6 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:27:35.822 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=47] [neededSchemaVersion=48] ["start time"=786.35µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 11:27:35.871 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=48] ["take time"=52.008353ms] [job="ID:66, Type:drop schema, State:done, SchemaState:none, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:27:35.6 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:27:35.874 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=66] [jobType="drop schema"]
   > [2024/07/24 11:27:35.875 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:drop schema, State:synced, SchemaState:none, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:27:35.6 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:27:35.897 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=66]
   > [2024/07/24 11:27:35.897 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/07/24 11:27:35.899 +00:00] [INFO] [session.go:2161] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=48] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.62]
   > [2024/07/24 11:27:35.933 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:68, Type:create schema, State:none, SchemaState:none, SchemaID:67, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 11:27:35.901 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 11:27:35.933 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:68, Type:create schema, State:none, SchemaState:none, SchemaID:67, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 11:27:35.901 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/24 11:27:35.936 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:68, Type:create schema, State:none, SchemaState:none, SchemaID:67, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:27:35.901 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:27:35.959 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=48] [neededSchemaVersion=49] ["start time"=1.265047ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 11:27:36.008 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=49] ["take time"=52.352744ms] [job="ID:68, Type:create schema, State:done, SchemaState:public, SchemaID:67, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 11:27:35.901 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:27:36.011 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:68, Type:create schema, State:synced, SchemaState:public, SchemaID:67, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:27:35.901 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:27:36.028 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=68]
   > [2024/07/24 11:27:36.028 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/07/24 11:27:36.031 +00:00] [INFO] [session.go:2161] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=49] [cur_db=testdb] [sql="CREATE TABLE `t1` ( `id` int(11) primary key, `name` varchar(20) DEFAULT NULL );"] [user=root@10.88.0.62]
   > [2024/07/24 11:27:36.064 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:70, Type:create table, State:none, SchemaState:none, SchemaID:67, TableID:69, RowCount:0, ArgLen:1, start time: 2024-07-24 11:27:36.001 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 11:27:36.064 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:70, Type:create table, State:none, SchemaState:none, SchemaID:67, TableID:69, RowCount:0, ArgLen:1, start time: 2024-07-24 11:27:36.001 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t1` ( `id` int(11) primary key, `name` varchar(20) DEFAULT NULL );"]
   > [2024/07/24 11:27:36.068 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:70, Type:create table, State:none, SchemaState:none, SchemaID:67, TableID:69, RowCount:0, ArgLen:0, start time: 2024-07-24 11:27:36.001 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:27:36.095 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=49] [neededSchemaVersion=50] ["start time"=2.003486ms] [phyTblIDs="[69]"] [actionTypes="[8]"]
   > [2024/07/24 11:27:36.143 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=50] ["take time"=52.009191ms] [job="ID:70, Type:create table, State:done, SchemaState:public, SchemaID:67, TableID:69, RowCount:0, ArgLen:1, start time: 2024-07-24 11:27:36.001 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:27:36.146 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:70, Type:create table, State:synced, SchemaState:public, SchemaID:67, TableID:69, RowCount:0, ArgLen:0, start time: 2024-07-24 11:27:36.001 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:27:36.167 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=70]
   > [2024/07/24 11:27:36.169 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/07/24 11:27:36.169 +00:00] [INFO] [split_region.go:60] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=748000000000000045]
   > [2024/07/24 11:27:36.170 +00:00] [INFO] [peer.rs:469] ["on split"] [split_keys="key 7480000000000000FF4500000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/24 11:27:36.170 +00:00] [INFO] [cluster_worker.go:125] ["alloc ids for region split"] [region-id=52] [peer-ids="[53]"]
   > [2024/07/24 11:27:36.170 +00:00] [INFO] [pd.rs:507] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF3F00000000000000F8 region_epoch { conf_ver: 1 version: 25 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 52 new_peer_ids: 53]"] [region_id=2]
   > [2024/07/24 11:27:36.176 +00:00] [INFO] [apply.rs:1172] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF4500000000000000F8 new_region_id: 52 new_peer_ids: 53 } right_derive: true }"] [index=80] [term=6] [peer_id=3] [region_id=2]
   > [2024/07/24 11:27:36.177 +00:00] [INFO] [apply.rs:1752] ["split region"] [keys="key 7480000000000000FF4500000000000000F8"] [region="id: 2 start_key: 7480000000000000FF3F00000000000000F8 region_epoch { conf_ver: 1 version: 25 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/07/24 11:27:36.187 +00:00] [INFO] [peer.rs:1758] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/07/24 11:27:36.187 +00:00] [INFO] [peer.rs:1800] ["insert new region"] [region="id: 52 start_key: 7480000000000000FF3F00000000000000F8 end_key: 7480000000000000FF4500000000000000F8 region_epoch { conf_ver: 1 version: 26 } peers { id: 53 store_id: 1 }"] [region_id=52]
   > [2024/07/24 11:27:36.187 +00:00] [INFO] [peer.rs:159] ["create peer"] [peer_id=53] [region_id=52]
   > [2024/07/24 11:27:36.187 +00:00] [INFO] [raft.rs:783] ["became follower at term 5"] [term=5] [raft_id=53] [region_id=52]
   > [2024/07/24 11:27:36.187 +00:00] [INFO] [split_region.go:157] ["batch split regions complete"] ["batch region ID"=2] ["first at"=748000000000000045] ["first new region left"="{Id:52 StartKey:7480000000000000ff3f00000000000000f8 EndKey:7480000000000000ff4500000000000000f8 RegionEpoch:{ConfVer:1 Version:26} Peers:[id:53 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/24 11:27:36.187 +00:00] [INFO] [split_region.go:209] ["split regions complete"] ["region count"=1] ["region IDs"="[52]"]
   > [2024/07/24 11:27:36.187 +00:00] [INFO] [raft.rs:285] [newRaft] [peers="[(53, Progress { matched: 5, next_idx: 6, state: Probe, paused: false, pending_snapshot: 0, pending_request_snapshot: 0, recent_active: false, ins: Inflights { start: 0, count: 0, buffer: [] } })]"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=53] [region_id=52]
   > [2024/07/24 11:27:36.188 +00:00] [INFO] [raw_node.rs:222] ["RawNode created with id 53."] [id=53] [raft_id=53] [region_id=52]
   > [2024/07/24 11:27:36.188 +00:00] [INFO] [cluster.go:542] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF3F00000000000000F8} -> {7480000000000000FF4500000000000000F8}, EndKey:{}"] [old-version=25] [new-version=26]
   > [2024/07/24 11:27:36.188 +00:00] [INFO] [raft.rs:1177] ["starting a new election"] [term=5] [raft_id=53] [region_id=52]
   > [2024/07/24 11:27:36.188 +00:00] [INFO] [cluster_worker.go:217] ["region batch split, generate new regions"] [region-id=2] [origin="id:52 start_key:\"7480000000000000FF3F00000000000000F8\" end_key:\"7480000000000000FF4500000000000000F8\" region_epoch:<conf_ver:1 version:26 > peers:<id:53 store_id:1 >"] [total=1]
   > [2024/07/24 11:27:36.188 +00:00] [INFO] [raft.rs:833] ["became pre-candidate at term 5"] [term=5] [raft_id=53] [region_id=52]
   > [2024/07/24 11:27:36.188 +00:00] [INFO] [raft.rs:902] ["53 received message from 53"] [term=5] [msg=MsgRequestPreVote] [from=53] [id=53] [raft_id=53] [region_id=52]
   > [2024/07/24 11:27:36.188 +00:00] [INFO] [raft.rs:807] ["became candidate at term 6"] [term=6] [raft_id=53] [region_id=52]
   > [2024/07/24 11:27:36.188 +00:00] [INFO] [raft.rs:902] ["53 received message from 53"] [term=6] [msg=MsgRequestVote] [from=53] [id=53] [raft_id=53] [region_id=52]
   > [2024/07/24 11:27:36.188 +00:00] [INFO] [raft.rs:874] ["became leader at term 6"] [term=6] [raft_id=53] [region_id=52]
   > [2024/07/24 11:27:37.296 +00:00] [INFO] [set.go:216] ["set global var"] [conn=12] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/07/24 11:27:37.314 +00:00] [INFO] [set.go:216] ["set global var"] [conn=12] [name=transaction_isolation] [val=READ-COMMITTED]
   > [2024/07/24 11:27:39.031 +00:00] [INFO] [adapter.go:618] ["pessimistic write conflict, retry statement"] [conn=13] [txn=451364902089785350] [forUpdateTS=451364902089785350] [err="[kv:9007]Write conflict, txnStartTS=451364902089785350, conflictStartTS=451364902010880001, conflictCommitTS=451364902325714945, key={tableID=69, handle=1} primary={tableID=69, handle=1} [try again later]"]

### Scenario 1
 * Instruction #0:
     - Instruction:  select * from t1 where id = 1; -- the result is "1 abc" before the update commi...
     - Transaction: conn_1
     - Output: [(1, 'abc')]
     - Executed order: 0
     - Affected rows: 1
 * Instruction #1:
     - Instruction:  UPDATE t1 SET name='xyz' WHERE id=1;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows: 1
 * Instruction #2:
     - Instruction:  UPDATE t1 SET name='xyz' WHERE id=1; -- update the same row with same value usi...
     - Transaction: conn_1
     - Output: None
     - Executed order: 2
     - Affected rows: 0
 * Instruction #3:
     - Instruction:  select * from t1;        -- the result is "1, abc"
     - Transaction: conn_1
     - Output: [(1, 'xyz')]
     - Executed order: 3
     - Affected rows: 1
 * Instruction #4:
     - Instruction:  select * from t1 where id = 1 ; -- the result is "1, xyz"
     - Transaction: conn_1
     - Output: [(1, 'xyz')]
     - Executed order: 4
     - Affected rows: 1

 * Container logs:
   > [2024/07/24 11:27:42.217 +00:00] [INFO] [session.go:2161] ["CRUCIAL OPERATION"] [conn=15] [schemaVersion=58] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.62]
   > [2024/07/24 11:27:42.233 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:77, Type:drop schema, State:none, SchemaState:none, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:27:42.2 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 11:27:42.233 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:77, Type:drop schema, State:none, SchemaState:none, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:27:42.2 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/24 11:27:42.236 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:none, SchemaState:none, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:27:42.2 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:27:42.257 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=58] [neededSchemaVersion=59] ["start time"=632.559µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 11:27:42.306 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=59] ["take time"=52.192038ms] [job="ID:77, Type:drop schema, State:running, SchemaState:write only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:27:42.2 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:27:42.308 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:running, SchemaState:write only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:27:42.2 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:27:42.328 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=59] [neededSchemaVersion=60] ["start time"=610.977µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 11:27:42.378 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=60] ["take time"=52.093909ms] [job="ID:77, Type:drop schema, State:running, SchemaState:delete only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:27:42.2 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:27:42.379 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:running, SchemaState:delete only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:27:42.2 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:27:42.406 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=60] [neededSchemaVersion=61] ["start time"=587.86µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 11:27:42.457 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=61] ["take time"=52.719833ms] [job="ID:77, Type:drop schema, State:done, SchemaState:none, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:27:42.2 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:27:42.459 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=77] [jobType="drop schema"]
   > [2024/07/24 11:27:42.461 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:synced, SchemaState:none, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:27:42.2 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:27:42.480 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=77]
   > [2024/07/24 11:27:42.480 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/07/24 11:27:42.482 +00:00] [INFO] [session.go:2161] ["CRUCIAL OPERATION"] [conn=15] [schemaVersion=61] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.62]
   > [2024/07/24 11:27:42.520 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:79, Type:create schema, State:none, SchemaState:none, SchemaID:78, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 11:27:42.451 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 11:27:42.520 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:79, Type:create schema, State:none, SchemaState:none, SchemaID:78, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 11:27:42.451 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/24 11:27:42.523 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:79, Type:create schema, State:none, SchemaState:none, SchemaID:78, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:27:42.451 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:27:42.543 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=61] [neededSchemaVersion=62] ["start time"=1.336146ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 11:27:42.592 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=62] ["take time"=52.250286ms] [job="ID:79, Type:create schema, State:done, SchemaState:public, SchemaID:78, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 11:27:42.451 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:27:42.595 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:79, Type:create schema, State:synced, SchemaState:public, SchemaID:78, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:27:42.451 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:27:42.612 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=79]
   > [2024/07/24 11:27:42.612 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/07/24 11:27:42.616 +00:00] [INFO] [session.go:2161] ["CRUCIAL OPERATION"] [conn=15] [schemaVersion=62] [cur_db=testdb] [sql="CREATE TABLE `t1` ( `id` int(11) primary key, `name` varchar(20) DEFAULT NULL );"] [user=root@10.88.0.62]
   > [2024/07/24 11:27:42.650 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:81, Type:create table, State:none, SchemaState:none, SchemaID:78, TableID:80, RowCount:0, ArgLen:1, start time: 2024-07-24 11:27:42.601 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 11:27:42.651 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:81, Type:create table, State:none, SchemaState:none, SchemaID:78, TableID:80, RowCount:0, ArgLen:1, start time: 2024-07-24 11:27:42.601 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t1` ( `id` int(11) primary key, `name` varchar(20) DEFAULT NULL );"]
   > [2024/07/24 11:27:42.654 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:81, Type:create table, State:none, SchemaState:none, SchemaID:78, TableID:80, RowCount:0, ArgLen:0, start time: 2024-07-24 11:27:42.601 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:27:42.682 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=62] [neededSchemaVersion=63] ["start time"=1.919047ms] [phyTblIDs="[80]"] [actionTypes="[8]"]
   > [2024/07/24 11:27:42.740 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=63] ["take time"=62.842304ms] [job="ID:81, Type:create table, State:done, SchemaState:public, SchemaID:78, TableID:80, RowCount:0, ArgLen:1, start time: 2024-07-24 11:27:42.601 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:27:42.744 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:81, Type:create table, State:synced, SchemaState:public, SchemaID:78, TableID:80, RowCount:0, ArgLen:0, start time: 2024-07-24 11:27:42.601 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:27:42.760 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=81]
   > [2024/07/24 11:27:42.762 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/07/24 11:27:42.762 +00:00] [INFO] [split_region.go:60] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=748000000000000050]
   > [2024/07/24 11:27:42.763 +00:00] [INFO] [peer.rs:469] ["on split"] [split_keys="key 7480000000000000FF5000000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/24 11:27:42.764 +00:00] [INFO] [cluster_worker.go:125] ["alloc ids for region split"] [region-id=56] [peer-ids="[57]"]
   > [2024/07/24 11:27:42.764 +00:00] [INFO] [pd.rs:507] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF4A00000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 56 new_peer_ids: 57]"] [region_id=2]
   > [2024/07/24 11:27:42.770 +00:00] [INFO] [apply.rs:1172] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF5000000000000000F8 new_region_id: 56 new_peer_ids: 57 } right_derive: true }"] [index=94] [term=6] [peer_id=3] [region_id=2]
   > [2024/07/24 11:27:42.770 +00:00] [INFO] [apply.rs:1752] ["split region"] [keys="key 7480000000000000FF5000000000000000F8"] [region="id: 2 start_key: 7480000000000000FF4A00000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/07/24 11:27:42.776 +00:00] [INFO] [peer.rs:1758] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/07/24 11:27:42.776 +00:00] [INFO] [peer.rs:1800] ["insert new region"] [region="id: 56 start_key: 7480000000000000FF4A00000000000000F8 end_key: 7480000000000000FF5000000000000000F8 region_epoch { conf_ver: 1 version: 28 } peers { id: 57 store_id: 1 }"] [region_id=56]
   > [2024/07/24 11:27:42.776 +00:00] [INFO] [peer.rs:159] ["create peer"] [peer_id=57] [region_id=56]
   > [2024/07/24 11:27:42.776 +00:00] [INFO] [split_region.go:157] ["batch split regions complete"] ["batch region ID"=2] ["first at"=748000000000000050] ["first new region left"="{Id:56 StartKey:7480000000000000ff4a00000000000000f8 EndKey:7480000000000000ff5000000000000000f8 RegionEpoch:{ConfVer:1 Version:28} Peers:[id:57 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/24 11:27:42.776 +00:00] [INFO] [raft.rs:783] ["became follower at term 5"] [term=5] [raft_id=57] [region_id=56]
   > [2024/07/24 11:27:42.776 +00:00] [INFO] [split_region.go:209] ["split regions complete"] ["region count"=1] ["region IDs"="[56]"]
   > [2024/07/24 11:27:42.776 +00:00] [INFO] [raft.rs:285] [newRaft] [peers="[(57, Progress { matched: 5, next_idx: 6, state: Probe, paused: false, pending_snapshot: 0, pending_request_snapshot: 0, recent_active: false, ins: Inflights { start: 0, count: 0, buffer: [] } })]"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=57] [region_id=56]
   > [2024/07/24 11:27:42.776 +00:00] [INFO] [cluster.go:542] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF4A00000000000000F8} -> {7480000000000000FF5000000000000000F8}, EndKey:{}"] [old-version=27] [new-version=28]
   > [2024/07/24 11:27:42.776 +00:00] [INFO] [raw_node.rs:222] ["RawNode created with id 57."] [id=57] [raft_id=57] [region_id=56]
   > [2024/07/24 11:27:42.776 +00:00] [INFO] [cluster_worker.go:217] ["region batch split, generate new regions"] [region-id=2] [origin="id:56 start_key:\"7480000000000000FF4A00000000000000F8\" end_key:\"7480000000000000FF5000000000000000F8\" region_epoch:<conf_ver:1 version:28 > peers:<id:57 store_id:1 >"] [total=1]
   > [2024/07/24 11:27:42.776 +00:00] [INFO] [raft.rs:1177] ["starting a new election"] [term=5] [raft_id=57] [region_id=56]
   > [2024/07/24 11:27:42.776 +00:00] [INFO] [raft.rs:833] ["became pre-candidate at term 5"] [term=5] [raft_id=57] [region_id=56]
   > [2024/07/24 11:27:42.776 +00:00] [INFO] [raft.rs:902] ["57 received message from 57"] [term=5] [msg=MsgRequestPreVote] [from=57] [id=57] [raft_id=57] [region_id=56]
   > [2024/07/24 11:27:42.777 +00:00] [INFO] [raft.rs:807] ["became candidate at term 6"] [term=6] [raft_id=57] [region_id=56]
   > [2024/07/24 11:27:42.777 +00:00] [INFO] [raft.rs:902] ["57 received message from 57"] [term=6] [msg=MsgRequestVote] [from=57] [id=57] [raft_id=57] [region_id=56]
   > [2024/07/24 11:27:42.777 +00:00] [INFO] [raft.rs:874] ["became leader at term 6"] [term=6] [raft_id=57] [region_id=56]
