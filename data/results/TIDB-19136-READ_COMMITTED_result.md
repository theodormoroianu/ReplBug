# Bug ID TIDB-19136-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/19136
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              The second select should output the same table as the first one, but it doesn't.


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
   > [2024/07/16 14:03:41.560 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=11]
   > [2024/07/16 14:03:41.565 +00:00] [INFO] [server.go:388] ["new connection"] [conn=12] [remoteAddr=10.88.0.74:43208]
   > [2024/07/16 14:03:41.567 +00:00] [INFO] [session.go:2130] ["CRUCIAL OPERATION"] [conn=12] [schemaVersion=58] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.74]
   > [2024/07/16 14:03:41.582 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:77, Type:drop schema, State:none, SchemaState:none, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 14:03:41.548 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/16 14:03:41.582 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:77, Type:drop schema, State:none, SchemaState:none, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 14:03:41.548 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/16 14:03:41.586 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:none, SchemaState:none, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 14:03:41.548 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 14:03:41.607 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=58] [neededSchemaVersion=59] ["start time"=522.977µs] [tblIDs="[]"]
   > [2024/07/16 14:03:41.657 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=59] ["take time"=52.284377ms] [job="ID:77, Type:drop schema, State:running, SchemaState:write only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 14:03:41.548 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 14:03:41.658 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:running, SchemaState:write only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 14:03:41.548 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 14:03:41.676 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=59] [neededSchemaVersion=60] ["start time"=630.814µs] [tblIDs="[]"]
   > [2024/07/16 14:03:41.726 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=60] ["take time"=52.270128ms] [job="ID:77, Type:drop schema, State:running, SchemaState:delete only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 14:03:41.548 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 14:03:41.728 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:running, SchemaState:delete only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 14:03:41.548 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 14:03:41.749 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=60] [neededSchemaVersion=61] ["start time"=731.595µs] [tblIDs="[]"]
   > [2024/07/16 14:03:41.799 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=61] ["take time"=52.180102ms] [job="ID:77, Type:drop schema, State:done, SchemaState:none, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 14:03:41.548 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 14:03:41.801 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=77] [jobType="drop schema"]
   > [2024/07/16 14:03:41.803 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:synced, SchemaState:none, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 14:03:41.548 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 14:03:41.823 +00:00] [INFO] [ddl.go:509] ["[ddl] DDL job is finished"] [jobID=77]
   > [2024/07/16 14:03:41.823 +00:00] [INFO] [domain.go:624] ["performing DDL change, must reload"]
   > [2024/07/16 14:03:41.825 +00:00] [INFO] [session.go:2130] ["CRUCIAL OPERATION"] [conn=12] [schemaVersion=61] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.74]
   > [2024/07/16 14:03:41.854 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:79, Type:create schema, State:none, SchemaState:none, SchemaID:78, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-16 14:03:41.798 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/16 14:03:41.854 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:79, Type:create schema, State:none, SchemaState:none, SchemaID:78, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-16 14:03:41.798 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/16 14:03:41.857 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:79, Type:create schema, State:none, SchemaState:none, SchemaID:78, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 14:03:41.798 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 14:03:41.877 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=61] [neededSchemaVersion=62] ["start time"=1.1892ms] [tblIDs="[]"]
   > [2024/07/16 14:03:41.928 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=62] ["take time"=53.724798ms] [job="ID:79, Type:create schema, State:done, SchemaState:public, SchemaID:78, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-16 14:03:41.798 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 14:03:41.930 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:79, Type:create schema, State:synced, SchemaState:public, SchemaID:78, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-16 14:03:41.798 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 14:03:41.946 +00:00] [INFO] [ddl.go:509] ["[ddl] DDL job is finished"] [jobID=79]
   > [2024/07/16 14:03:41.946 +00:00] [INFO] [domain.go:624] ["performing DDL change, must reload"]
   > [2024/07/16 14:03:41.949 +00:00] [INFO] [session.go:2130] ["CRUCIAL OPERATION"] [conn=12] [schemaVersion=62] [cur_db=testdb] [sql="create table t ( c_int int, c_str varchar(40), primary key(c_int, c_str) );"] [user=root@10.88.0.74]
   > [2024/07/16 14:03:41.977 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:81, Type:create table, State:none, SchemaState:none, SchemaID:78, TableID:80, RowCount:0, ArgLen:1, start time: 2024-07-16 14:03:41.948 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/16 14:03:41.977 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:81, Type:create table, State:none, SchemaState:none, SchemaID:78, TableID:80, RowCount:0, ArgLen:1, start time: 2024-07-16 14:03:41.948 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t ( c_int int, c_str varchar(40), primary key(c_int, c_str) );"]
   > [2024/07/16 14:03:41.981 +00:00] [INFO] [ddl_worker.go:584] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:81, Type:create table, State:none, SchemaState:none, SchemaID:78, TableID:80, RowCount:0, ArgLen:0, start time: 2024-07-16 14:03:41.948 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 14:03:42.005 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=62] [neededSchemaVersion=63] ["start time"=1.387203ms] [tblIDs="[80]"]
   > [2024/07/16 14:03:42.053 +00:00] [INFO] [ddl_worker.go:773] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=63] ["take time"=51.716979ms] [job="ID:81, Type:create table, State:done, SchemaState:public, SchemaID:78, TableID:80, RowCount:0, ArgLen:1, start time: 2024-07-16 14:03:41.948 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 14:03:42.056 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:81, Type:create table, State:synced, SchemaState:public, SchemaID:78, TableID:80, RowCount:0, ArgLen:0, start time: 2024-07-16 14:03:41.948 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/16 14:03:42.072 +00:00] [INFO] [ddl.go:509] ["[ddl] DDL job is finished"] [jobID=81]
   > [2024/07/16 14:03:42.074 +00:00] [INFO] [domain.go:624] ["performing DDL change, must reload"]
   > [2024/07/16 14:03:42.074 +00:00] [INFO] [split_region.go:56] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=748000000000000050]
   > [2024/07/16 14:03:42.075 +00:00] [INFO] [peer.rs:458] ["on split"] [split_keys="key 7480000000000000FF5000000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/16 14:03:42.075 +00:00] [INFO] [cluster_worker.go:131] ["alloc ids for region split"] [region-id=56] [peer-ids="[57]"]
   > [2024/07/16 14:03:42.076 +00:00] [INFO] [pd.rs:499] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF4A00000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 56 new_peer_ids: 57]"] [region_id=2]
   > [2024/07/16 14:03:42.076 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=12]
   > [2024/07/16 14:03:42.081 +00:00] [INFO] [apply.rs:1144] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF5000000000000000F8 new_region_id: 56 new_peer_ids: 57 } right_derive: true }"] [index=82] [term=6] [peer_id=3] [region_id=2]
   > [2024/07/16 14:03:42.081 +00:00] [INFO] [apply.rs:1712] ["split region"] [keys="key 7480000000000000FF5000000000000000F8"] [region="id: 2 start_key: 7480000000000000FF4A00000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/07/16 14:03:42.087 +00:00] [INFO] [peer.rs:1727] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/07/16 14:03:42.087 +00:00] [INFO] [peer.rs:1769] ["insert new region"] [region="id: 56 start_key: 7480000000000000FF4A00000000000000F8 end_key: 7480000000000000FF5000000000000000F8 region_epoch { conf_ver: 1 version: 28 } peers { id: 57 store_id: 1 }"] [region_id=56]
   > [2024/07/16 14:03:42.087 +00:00] [INFO] [peer.rs:158] ["create peer"] [peer_id=57] [region_id=56]
   > [2024/07/16 14:03:42.087 +00:00] [INFO] [split_region.go:153] ["batch split regions complete"] ["batch region ID"=2] ["first at"=748000000000000050] ["first new region left"="{Id:56 StartKey:7480000000000000ff4a00000000000000f8 EndKey:7480000000000000ff5000000000000000f8 RegionEpoch:{ConfVer:1 Version:28} Peers:[id:57 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/16 14:03:42.087 +00:00] [INFO] [raft.rs:783] ["became follower at term 5"] [term=5] [raft_id=57] [region_id=56]
   > [2024/07/16 14:03:42.087 +00:00] [INFO] [split_region.go:205] ["split regions complete"] ["region count"=1] ["region IDs"="[56]"]
   > [2024/07/16 14:03:42.087 +00:00] [INFO] [cluster.go:478] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF4A00000000000000F8} -> {7480000000000000FF5000000000000000F8}, EndKey:{}"] [old-version=27] [new-version=28]
   > [2024/07/16 14:03:42.087 +00:00] [INFO] [raft.rs:285] [newRaft] [peers="[(57, Progress { matched: 5, next_idx: 6, state: Probe, paused: false, pending_snapshot: 0, pending_request_snapshot: 0, recent_active: false, ins: Inflights { start: 0, count: 0, buffer: [] } })]"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=57] [region_id=56]
   > [2024/07/16 14:03:42.087 +00:00] [INFO] [raw_node.rs:222] ["RawNode created with id 57."] [id=57] [raft_id=57] [region_id=56]
   > [2024/07/16 14:03:42.087 +00:00] [INFO] [raft.rs:1177] ["starting a new election"] [term=5] [raft_id=57] [region_id=56]
   > [2024/07/16 14:03:42.087 +00:00] [INFO] [cluster_worker.go:218] ["region batch split, generate new regions"] [region-id=2] [origin="id:56 start_key:\"7480000000000000FF4A00000000000000F8\" end_key:\"7480000000000000FF5000000000000000F8\" region_epoch:<conf_ver:1 version:28 > peers:<id:57 store_id:1 >"] [total=1]
   > [2024/07/16 14:03:42.087 +00:00] [INFO] [raft.rs:833] ["became pre-candidate at term 5"] [term=5] [raft_id=57] [region_id=56]
   > [2024/07/16 14:03:42.087 +00:00] [INFO] [raft.rs:902] ["57 received message from 57"] [term=5] [msg=MsgRequestPreVote] [from=57] [id=57] [raft_id=57] [region_id=56]
   > [2024/07/16 14:03:42.087 +00:00] [INFO] [raft.rs:807] ["became candidate at term 6"] [term=6] [raft_id=57] [region_id=56]
   > [2024/07/16 14:03:42.088 +00:00] [INFO] [raft.rs:902] ["57 received message from 57"] [term=6] [msg=MsgRequestVote] [from=57] [id=57] [raft_id=57] [region_id=56]
   > [2024/07/16 14:03:42.088 +00:00] [INFO] [raft.rs:874] ["became leader at term 6"] [term=6] [raft_id=57] [region_id=56]
   > [2024/07/16 14:03:43.084 +00:00] [INFO] [server.go:388] ["new connection"] [conn=13] [remoteAddr=10.88.0.74:59322]
   > [2024/07/16 14:03:43.091 +00:00] [INFO] [set.go:207] ["set session var"] [conn=13] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/07/16 14:03:43.707 +00:00] [INFO] [process.rs:145] ["get snapshot failed"] [err="Request(message: \"EpochNotMatch current epoch of region 2 is conf_ver: 1 version: 28, but you sent conf_ver: 1 version: 27\" epoch_not_match { current_regions { id: 2 start_key: 7480000000000000FF5000000000000000F8 region_epoch { conf_ver: 1 version: 28 } peers { id: 3 store_id: 1 } } current_regions { id: 56 start_key: 7480000000000000FF4A00000000000000F8 end_key: 7480000000000000FF5000000000000000F8 region_epoch { conf_ver: 1 version: 28 } peers { id: 57 store_id: 1 } } })"] [cid=543]
   > [2024/07/16 14:03:54.888 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=13]
