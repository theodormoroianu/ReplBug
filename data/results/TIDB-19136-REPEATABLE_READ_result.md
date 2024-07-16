# Bug ID TIDB-19136-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/19136
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              The second select should output the same table as the first one, but it doesn't.


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
   > [2024/07/16 14:03:26.477 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=8]
   > [2024/07/16 14:03:26.481 +00:00] [INFO] [server.go:388] ["new connection"] [conn=9] [remoteAddr=10.88.0.74:33522]
   > [2024/07/16 14:03:26.484 +00:00] [INFO] [session.go:2130] ["CRUCIAL OPERATION"] [conn=9] [schemaVersion=45] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.74]
   > [2024/07/16 14:03:26.498 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:66, Type:drop schema, State:none, SchemaState:none, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 14:03:26.448 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/16 14:03:26.498 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:66, Type:drop schema, State:none, SchemaState:none, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 14:03:26.448 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/16 14:03:26.501 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:drop schema, State:none, SchemaState:none, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 14:03:26.448 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 14:03:26.518 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=45] [neededSchemaVersion=46] ["start time"=339.572µs] [tblIDs="[]"]
   > [2024/07/16 14:03:26.568 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=46] ["take time"=52.071987ms] [job="ID:66, Type:drop schema, State:running, SchemaState:write only, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 14:03:26.448 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 14:03:26.570 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:drop schema, State:running, SchemaState:write only, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 14:03:26.448 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 14:03:26.591 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=46] [neededSchemaVersion=47] ["start time"=625.785µs] [tblIDs="[]"]
   > [2024/07/16 14:03:26.648 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=47] ["take time"=59.822008ms] [job="ID:66, Type:drop schema, State:running, SchemaState:delete only, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 14:03:26.448 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 14:03:26.650 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:drop schema, State:running, SchemaState:delete only, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 14:03:26.448 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 14:03:26.673 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=47] [neededSchemaVersion=48] ["start time"=675.302µs] [tblIDs="[]"]
   > [2024/07/16 14:03:26.723 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=48] ["take time"=52.327399ms] [job="ID:66, Type:drop schema, State:done, SchemaState:none, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 14:03:26.448 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 14:03:26.725 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=66] [jobType="drop schema"]
   > [2024/07/16 14:03:26.726 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:drop schema, State:synced, SchemaState:none, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 14:03:26.448 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 14:03:26.743 +00:00] [INFO] [ddl.go:509] ["[ddl] DDL job is finished"] [jobID=66]
   > [2024/07/16 14:03:26.743 +00:00] [INFO] [domain.go:624] ["performing DDL change, must reload"]
   > [2024/07/16 14:03:26.745 +00:00] [INFO] [session.go:2130] ["CRUCIAL OPERATION"] [conn=9] [schemaVersion=48] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.74]
   > [2024/07/16 14:03:26.781 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:68, Type:create schema, State:none, SchemaState:none, SchemaID:67, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-16 14:03:26.748 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/16 14:03:26.781 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:68, Type:create schema, State:none, SchemaState:none, SchemaID:67, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-16 14:03:26.748 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/16 14:03:26.784 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:68, Type:create schema, State:none, SchemaState:none, SchemaID:67, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 14:03:26.748 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 14:03:26.804 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=48] [neededSchemaVersion=49] ["start time"=1.106158ms] [tblIDs="[]"]
   > [2024/07/16 14:03:26.853 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=49] ["take time"=52.115638ms] [job="ID:68, Type:create schema, State:done, SchemaState:public, SchemaID:67, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-16 14:03:26.748 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 14:03:26.857 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:68, Type:create schema, State:synced, SchemaState:public, SchemaID:67, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 14:03:26.748 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 14:03:26.873 +00:00] [INFO] [ddl.go:509] ["[ddl] DDL job is finished"] [jobID=68]
   > [2024/07/16 14:03:26.873 +00:00] [INFO] [domain.go:624] ["performing DDL change, must reload"]
   > [2024/07/16 14:03:26.876 +00:00] [INFO] [session.go:2130] ["CRUCIAL OPERATION"] [conn=9] [schemaVersion=49] [cur_db=testdb] [sql="create table t ( c_int int, c_str varchar(40), primary key(c_int, c_str) );"] [user=root@10.88.0.74]
   > [2024/07/16 14:03:26.912 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:70, Type:create table, State:none, SchemaState:none, SchemaID:67, TableID:69, RowCount:0, ArgLen:1, start time: 2024-07-16 14:03:26.848 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/16 14:03:26.912 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:70, Type:create table, State:none, SchemaState:none, SchemaID:67, TableID:69, RowCount:0, ArgLen:1, start time: 2024-07-16 14:03:26.848 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t ( c_int int, c_str varchar(40), primary key(c_int, c_str) );"]
   > [2024/07/16 14:03:26.915 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:70, Type:create table, State:none, SchemaState:none, SchemaID:67, TableID:69, RowCount:0, ArgLen:0, start time: 2024-07-16 14:03:26.848 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 14:03:26.944 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=49] [neededSchemaVersion=50] ["start time"=1.440492ms] [tblIDs="[69]"]
   > [2024/07/16 14:03:26.996 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=50] ["take time"=55.141544ms] [job="ID:70, Type:create table, State:done, SchemaState:public, SchemaID:67, TableID:69, RowCount:0, ArgLen:1, start time: 2024-07-16 14:03:26.848 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 14:03:26.999 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:70, Type:create table, State:synced, SchemaState:public, SchemaID:67, TableID:69, RowCount:0, ArgLen:0, start time: 2024-07-16 14:03:26.848 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 14:03:27.015 +00:00] [INFO] [ddl.go:509] ["[ddl] DDL job is finished"] [jobID=70]
   > [2024/07/16 14:03:27.016 +00:00] [INFO] [domain.go:624] ["performing DDL change, must reload"]
   > [2024/07/16 14:03:27.017 +00:00] [INFO] [split_region.go:56] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=748000000000000045]
   > [2024/07/16 14:03:27.017 +00:00] [INFO] [peer.rs:458] ["on split"] [split_keys="key 7480000000000000FF4500000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/16 14:03:27.017 +00:00] [INFO] [cluster_worker.go:131] ["alloc ids for region split"] [region-id=52] [peer-ids="[53]"]
   > [2024/07/16 14:03:27.017 +00:00] [INFO] [pd.rs:499] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF3F00000000000000F8 region_epoch { conf_ver: 1 version: 25 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 52 new_peer_ids: 53]"] [region_id=2]
   > [2024/07/16 14:03:27.018 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=9]
   > [2024/07/16 14:03:27.023 +00:00] [INFO] [apply.rs:1144] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF4500000000000000F8 new_region_id: 52 new_peer_ids: 53 } right_derive: true }"] [index=74] [term=6] [peer_id=3] [region_id=2]
   > [2024/07/16 14:03:27.023 +00:00] [INFO] [apply.rs:1712] ["split region"] [keys="key 7480000000000000FF4500000000000000F8"] [region="id: 2 start_key: 7480000000000000FF3F00000000000000F8 region_epoch { conf_ver: 1 version: 25 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/07/16 14:03:27.029 +00:00] [INFO] [peer.rs:1727] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/07/16 14:03:27.029 +00:00] [INFO] [peer.rs:1769] ["insert new region"] [region="id: 52 start_key: 7480000000000000FF3F00000000000000F8 end_key: 7480000000000000FF4500000000000000F8 region_epoch { conf_ver: 1 version: 26 } peers { id: 53 store_id: 1 }"] [region_id=52]
   > [2024/07/16 14:03:27.029 +00:00] [INFO] [peer.rs:158] ["create peer"] [peer_id=53] [region_id=52]
   > [2024/07/16 14:03:27.029 +00:00] [INFO] [raft.rs:783] ["became follower at term 5"] [term=5] [raft_id=53] [region_id=52]
   > [2024/07/16 14:03:27.029 +00:00] [INFO] [split_region.go:153] ["batch split regions complete"] ["batch region ID"=2] ["first at"=748000000000000045] ["first new region left"="{Id:52 StartKey:7480000000000000ff3f00000000000000f8 EndKey:7480000000000000ff4500000000000000f8 RegionEpoch:{ConfVer:1 Version:26} Peers:[id:53 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/16 14:03:27.029 +00:00] [INFO] [split_region.go:205] ["split regions complete"] ["region count"=1] ["region IDs"="[52]"]
   > [2024/07/16 14:03:27.029 +00:00] [INFO] [cluster.go:478] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF3F00000000000000F8} -> {7480000000000000FF4500000000000000F8}, EndKey:{}"] [old-version=25] [new-version=26]
   > [2024/07/16 14:03:27.029 +00:00] [INFO] [raft.rs:285] [newRaft] [peers="[(53, Progress { matched: 5, next_idx: 6, state: Probe, paused: false, pending_snapshot: 0, pending_request_snapshot: 0, recent_active: false, ins: Inflights { start: 0, count: 0, buffer: [] } })]"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=53] [region_id=52]
   > [2024/07/16 14:03:27.029 +00:00] [INFO] [raw_node.rs:222] ["RawNode created with id 53."] [id=53] [raft_id=53] [region_id=52]
   > [2024/07/16 14:03:27.029 +00:00] [INFO] [cluster_worker.go:218] ["region batch split, generate new regions"] [region-id=2] [origin="id:52 start_key:\"7480000000000000FF3F00000000000000F8\" end_key:\"7480000000000000FF4500000000000000F8\" region_epoch:<conf_ver:1 version:26 > peers:<id:53 store_id:1 >"] [total=1]
   > [2024/07/16 14:03:27.029 +00:00] [INFO] [raft.rs:1177] ["starting a new election"] [term=5] [raft_id=53] [region_id=52]
   > [2024/07/16 14:03:27.030 +00:00] [INFO] [raft.rs:833] ["became pre-candidate at term 5"] [term=5] [raft_id=53] [region_id=52]
   > [2024/07/16 14:03:27.030 +00:00] [INFO] [raft.rs:902] ["53 received message from 53"] [term=5] [msg=MsgRequestPreVote] [from=53] [id=53] [raft_id=53] [region_id=52]
   > [2024/07/16 14:03:27.030 +00:00] [INFO] [raft.rs:807] ["became candidate at term 6"] [term=6] [raft_id=53] [region_id=52]
   > [2024/07/16 14:03:27.030 +00:00] [INFO] [raft.rs:902] ["53 received message from 53"] [term=6] [msg=MsgRequestVote] [from=53] [id=53] [raft_id=53] [region_id=52]
   > [2024/07/16 14:03:27.030 +00:00] [INFO] [raft.rs:874] ["became leader at term 6"] [term=6] [raft_id=53] [region_id=52]
   > [2024/07/16 14:03:28.029 +00:00] [INFO] [server.go:388] ["new connection"] [conn=10] [remoteAddr=10.88.0.74:33528]
   > [2024/07/16 14:03:28.037 +00:00] [INFO] [set.go:207] ["set session var"] [conn=10] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/07/16 14:03:28.646 +00:00] [INFO] [process.rs:145] ["get snapshot failed"] [err="Request(message: \"EpochNotMatch current epoch of region 2 is conf_ver: 1 version: 26, but you sent conf_ver: 1 version: 25\" epoch_not_match { current_regions { id: 2 start_key: 7480000000000000FF4500000000000000F8 region_epoch { conf_ver: 1 version: 26 } peers { id: 3 store_id: 1 } } current_regions { id: 52 start_key: 7480000000000000FF3F00000000000000F8 end_key: 7480000000000000FF4500000000000000F8 region_epoch { conf_ver: 1 version: 26 } peers { id: 53 store_id: 1 } } })"] [cid=447]
   > [2024/07/16 14:03:39.833 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=10]
