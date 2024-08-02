# Bug ID TIDB-21506-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/21506
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              Inserting data twice when another transaction is updating the data does not fail.


## Details
 * Database: tidb-v4.0.7.tikv
 * Number of scenarios: 1
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;
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
     - Instruction:  insert into t2 select * from t1;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows: 2
 * Instruction #3:
     - Instruction:  update t1 set id = id + 2;
     - Transaction: conn_1
     - Output: None
     - Executed order: 3
     - Affected rows: 2
 * Instruction #4:
     - Instruction:  insert into t2 select * from t1; -- succeed
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows: 2
 * Instruction #5:
     - Instruction:  select * from t2; -- (1, 10), (2, 20), (3, 10), (4, 20)
     - Transaction: conn_0
     - Output: [(1, 10), (2, 20), (3, 10), (4, 20)]
     - Executed order: 5
     - Affected rows: 4
 * Instruction #6:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: None
     - Executed order: 6
     - Affected rows: 0
 * Instruction #7:
     - Instruction:  select * from t1;
     - Transaction: conn_2
     - Output: [(3, 10), (4, 20)]
     - Executed order: 7
     - Affected rows: 2
 * Instruction #8:
     - Instruction:  select * from t2;
     - Transaction: conn_2
     - Output: [(1, 10), (2, 20), (3, 10), (4, 20)]
     - Executed order: 8
     - Affected rows: 4

 * Container logs:
   > [2024/08/02 11:44:41.318 +00:00] [INFO] [server.go:397] ["connection closed"] [conn=7]
   > [2024/08/02 11:44:41.329 +00:00] [INFO] [server.go:394] ["new connection"] [conn=8] [remoteAddr=127.0.0.1:57878]
   > [2024/08/02 11:44:41.332 +00:00] [INFO] [session.go:2159] ["CRUCIAL OPERATION"] [conn=8] [schemaVersion=33] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/08/02 11:44:41.343 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:57, Type:drop schema, State:none, SchemaState:none, SchemaID:52, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 11:44:41.33 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/02 11:44:41.344 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:57, Type:drop schema, State:none, SchemaState:none, SchemaID:52, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 11:44:41.33 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/08/02 11:44:41.347 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:57, Type:drop schema, State:none, SchemaState:none, SchemaID:52, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 11:44:41.33 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 11:44:41.361 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=33] [neededSchemaVersion=34] ["start time"=765.468µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/02 11:44:41.410 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=34] ["take time"=52.416466ms] [job="ID:57, Type:drop schema, State:running, SchemaState:write only, SchemaID:52, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 11:44:41.33 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 11:44:41.412 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:57, Type:drop schema, State:running, SchemaState:write only, SchemaID:52, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 11:44:41.33 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 11:44:41.427 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=34] [neededSchemaVersion=35] ["start time"=737.81µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/02 11:44:41.476 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=35] ["take time"=52.335239ms] [job="ID:57, Type:drop schema, State:running, SchemaState:delete only, SchemaID:52, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 11:44:41.33 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 11:44:41.478 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:57, Type:drop schema, State:running, SchemaState:delete only, SchemaID:52, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 11:44:41.33 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 11:44:41.495 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=35] [neededSchemaVersion=36] ["start time"=567.466µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/02 11:44:41.544 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=36] ["take time"=52.217835ms] [job="ID:57, Type:drop schema, State:done, SchemaState:none, SchemaID:52, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 11:44:41.33 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 11:44:41.547 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=57] [jobType="drop schema"]
   > [2024/08/02 11:44:41.548 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:57, Type:drop schema, State:synced, SchemaState:none, SchemaID:52, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 11:44:41.33 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 11:44:41.559 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=57]
   > [2024/08/02 11:44:41.559 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/08/02 11:44:41.561 +00:00] [INFO] [session.go:2159] ["CRUCIAL OPERATION"] [conn=8] [schemaVersion=36] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/08/02 11:44:41.579 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:59, Type:create schema, State:none, SchemaState:none, SchemaID:58, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-02 11:44:41.53 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/02 11:44:41.579 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:59, Type:create schema, State:none, SchemaState:none, SchemaID:58, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-02 11:44:41.53 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/08/02 11:44:41.582 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:59, Type:create schema, State:none, SchemaState:none, SchemaID:58, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 11:44:41.53 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 11:44:41.598 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=36] [neededSchemaVersion=37] ["start time"=1.316521ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/02 11:44:41.647 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=37] ["take time"=54.241784ms] [job="ID:59, Type:create schema, State:done, SchemaState:public, SchemaID:58, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-02 11:44:41.53 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 11:44:41.650 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:59, Type:create schema, State:synced, SchemaState:public, SchemaID:58, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 11:44:41.53 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 11:44:41.660 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=59]
   > [2024/08/02 11:44:41.660 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/08/02 11:44:41.663 +00:00] [INFO] [session.go:2159] ["CRUCIAL OPERATION"] [conn=8] [schemaVersion=37] [cur_db=testdb] [sql="create table t1 (id int primary key, v int);"] [user=root@127.0.0.1]
   > [2024/08/02 11:44:41.680 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:61, Type:create table, State:none, SchemaState:none, SchemaID:58, TableID:60, RowCount:0, ArgLen:1, start time: 2024-08-02 11:44:41.631 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/02 11:44:41.680 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:61, Type:create table, State:none, SchemaState:none, SchemaID:58, TableID:60, RowCount:0, ArgLen:1, start time: 2024-08-02 11:44:41.631 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t1 (id int primary key, v int);"]
   > [2024/08/02 11:44:41.683 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:61, Type:create table, State:none, SchemaState:none, SchemaID:58, TableID:60, RowCount:0, ArgLen:0, start time: 2024-08-02 11:44:41.631 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 11:44:41.698 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=37] [neededSchemaVersion=38] ["start time"=1.874768ms] [phyTblIDs="[60]"] [actionTypes="[8]"]
   > [2024/08/02 11:44:41.746 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=38] ["take time"=52.182215ms] [job="ID:61, Type:create table, State:done, SchemaState:public, SchemaID:58, TableID:60, RowCount:0, ArgLen:1, start time: 2024-08-02 11:44:41.631 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 11:44:41.750 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:61, Type:create table, State:synced, SchemaState:public, SchemaID:58, TableID:60, RowCount:0, ArgLen:0, start time: 2024-08-02 11:44:41.631 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 11:44:41.759 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=61]
   > [2024/08/02 11:44:41.761 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/08/02 11:44:41.761 +00:00] [INFO] [split_region.go:58] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=74800000000000003c]
   > [2024/08/02 11:44:41.762 +00:00] [INFO] [peer.rs:469] ["on split"] [split_keys="key 7480000000000000FF3C00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/02 11:44:41.762 +00:00] [INFO] [cluster_worker.go:131] ["alloc ids for region split"] [region-id=50] [peer-ids="[51]"]
   > [2024/08/02 11:44:41.763 +00:00] [INFO] [session.go:2159] ["CRUCIAL OPERATION"] [conn=8] [schemaVersion=38] [cur_db=testdb] [sql="create table t2 (id int primary key, v int);"] [user=root@127.0.0.1]
   > [2024/08/02 11:44:41.763 +00:00] [INFO] [pd.rs:499] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF3600000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 50 new_peer_ids: 51]"] [region_id=2]
   > [2024/08/02 11:44:41.764 +00:00] [INFO] [apply.rs:1162] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF3C00000000000000F8 new_region_id: 50 new_peer_ids: 51 } right_derive: true }"] [index=66] [term=6] [peer_id=3] [region_id=2]
   > [2024/08/02 11:44:41.765 +00:00] [INFO] [apply.rs:1742] ["split region"] [keys="key 7480000000000000FF3C00000000000000F8"] [region="id: 2 start_key: 7480000000000000FF3600000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/08/02 11:44:41.767 +00:00] [INFO] [peer.rs:1731] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/08/02 11:44:41.767 +00:00] [INFO] [peer.rs:1773] ["insert new region"] [region="id: 50 start_key: 7480000000000000FF3600000000000000F8 end_key: 7480000000000000FF3C00000000000000F8 region_epoch { conf_ver: 1 version: 25 } peers { id: 51 store_id: 1 }"] [region_id=50]
   > [2024/08/02 11:44:41.767 +00:00] [INFO] [peer.rs:159] ["create peer"] [peer_id=51] [region_id=50]
   > [2024/08/02 11:44:41.768 +00:00] [INFO] [raft.rs:783] ["became follower at term 5"] [term=5] [raft_id=51] [region_id=50]
   > [2024/08/02 11:44:41.768 +00:00] [INFO] [split_region.go:155] ["batch split regions complete"] ["batch region ID"=2] ["first at"=74800000000000003c] ["first new region left"="{Id:50 StartKey:7480000000000000ff3600000000000000f8 EndKey:7480000000000000ff3c00000000000000f8 RegionEpoch:{ConfVer:1 Version:25} Peers:[id:51 store_id:1 ]}"] ["new region count"=1]
   > [2024/08/02 11:44:41.768 +00:00] [INFO] [raft.rs:285] [newRaft] [peers="[(51, Progress { matched: 5, next_idx: 6, state: Probe, paused: false, pending_snapshot: 0, pending_request_snapshot: 0, recent_active: false, ins: Inflights { start: 0, count: 0, buffer: [] } })]"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=51] [region_id=50]
   > [2024/08/02 11:44:41.768 +00:00] [INFO] [split_region.go:207] ["split regions complete"] ["region count"=1] ["region IDs"="[50]"]
   > [2024/08/02 11:44:41.768 +00:00] [INFO] [cluster.go:542] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF3600000000000000F8} -> {7480000000000000FF3C00000000000000F8}, EndKey:{}"] [old-version=24] [new-version=25]
   > [2024/08/02 11:44:41.768 +00:00] [INFO] [raw_node.rs:222] ["RawNode created with id 51."] [id=51] [raft_id=51] [region_id=50]
   > [2024/08/02 11:44:41.768 +00:00] [INFO] [raft.rs:1177] ["starting a new election"] [term=5] [raft_id=51] [region_id=50]
   > [2024/08/02 11:44:41.768 +00:00] [INFO] [raft.rs:833] ["became pre-candidate at term 5"] [term=5] [raft_id=51] [region_id=50]
   > [2024/08/02 11:44:41.768 +00:00] [INFO] [raft.rs:902] ["51 received message from 51"] [term=5] [msg=MsgRequestPreVote] [from=51] [id=51] [raft_id=51] [region_id=50]
   > [2024/08/02 11:44:41.768 +00:00] [INFO] [raft.rs:807] ["became candidate at term 6"] [term=6] [raft_id=51] [region_id=50]
   > [2024/08/02 11:44:41.768 +00:00] [INFO] [cluster_worker.go:223] ["region batch split, generate new regions"] [region-id=2] [origin="id:50 start_key:\"7480000000000000FF3600000000000000F8\" end_key:\"7480000000000000FF3C00000000000000F8\" region_epoch:<conf_ver:1 version:25 > peers:<id:51 store_id:1 >"] [total=1]
   > [2024/08/02 11:44:41.768 +00:00] [INFO] [raft.rs:902] ["51 received message from 51"] [term=6] [msg=MsgRequestVote] [from=51] [id=51] [raft_id=51] [region_id=50]
   > [2024/08/02 11:44:41.768 +00:00] [INFO] [raft.rs:874] ["became leader at term 6"] [term=6] [raft_id=51] [region_id=50]
   > [2024/08/02 11:44:41.780 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:63, Type:create table, State:none, SchemaState:none, SchemaID:58, TableID:62, RowCount:0, ArgLen:1, start time: 2024-08-02 11:44:41.731 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/02 11:44:41.780 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:63, Type:create table, State:none, SchemaState:none, SchemaID:58, TableID:62, RowCount:0, ArgLen:1, start time: 2024-08-02 11:44:41.731 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t2 (id int primary key, v int);"]
   > [2024/08/02 11:44:41.784 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:63, Type:create table, State:none, SchemaState:none, SchemaID:58, TableID:62, RowCount:0, ArgLen:0, start time: 2024-08-02 11:44:41.731 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 11:44:41.802 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=38] [neededSchemaVersion=39] ["start time"=1.779364ms] [phyTblIDs="[62]"] [actionTypes="[8]"]
   > [2024/08/02 11:44:41.851 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=39] ["take time"=52.336216ms] [job="ID:63, Type:create table, State:done, SchemaState:public, SchemaID:58, TableID:62, RowCount:0, ArgLen:1, start time: 2024-08-02 11:44:41.731 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 11:44:41.855 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:63, Type:create table, State:synced, SchemaState:public, SchemaID:58, TableID:62, RowCount:0, ArgLen:0, start time: 2024-08-02 11:44:41.731 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 11:44:41.864 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=63]
   > [2024/08/02 11:44:41.866 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/08/02 11:44:41.866 +00:00] [INFO] [split_region.go:58] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=74800000000000003e]
   > [2024/08/02 11:44:41.867 +00:00] [INFO] [peer.rs:469] ["on split"] [split_keys="key 7480000000000000FF3E00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/02 11:44:41.867 +00:00] [INFO] [peer.rs:2921] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 24"] [prev_epoch="conf_ver: 1 version: 25"] [peer_id=3] [region_id=2]
   > [2024/08/02 11:44:41.871 +00:00] [INFO] [peer.rs:469] ["on split"] [split_keys="key 7480000000000000FF3E00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/02 11:44:41.871 +00:00] [INFO] [cluster_worker.go:131] ["alloc ids for region split"] [region-id=52] [peer-ids="[53]"]
   > [2024/08/02 11:44:41.872 +00:00] [INFO] [pd.rs:499] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF3C00000000000000F8 region_epoch { conf_ver: 1 version: 25 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 52 new_peer_ids: 53]"] [region_id=2]
   > [2024/08/02 11:44:41.874 +00:00] [INFO] [apply.rs:1162] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF3E00000000000000F8 new_region_id: 52 new_peer_ids: 53 } right_derive: true }"] [index=68] [term=6] [peer_id=3] [region_id=2]
   > [2024/08/02 11:44:41.874 +00:00] [INFO] [apply.rs:1742] ["split region"] [keys="key 7480000000000000FF3E00000000000000F8"] [region="id: 2 start_key: 7480000000000000FF3C00000000000000F8 region_epoch { conf_ver: 1 version: 25 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/08/02 11:44:41.876 +00:00] [INFO] [peer.rs:1731] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/08/02 11:44:41.877 +00:00] [INFO] [peer.rs:1773] ["insert new region"] [region="id: 52 start_key: 7480000000000000FF3C00000000000000F8 end_key: 7480000000000000FF3E00000000000000F8 region_epoch { conf_ver: 1 version: 26 } peers { id: 53 store_id: 1 }"] [region_id=52]
   > [2024/08/02 11:44:41.877 +00:00] [INFO] [peer.rs:159] ["create peer"] [peer_id=53] [region_id=52]
   > [2024/08/02 11:44:41.877 +00:00] [INFO] [split_region.go:155] ["batch split regions complete"] ["batch region ID"=2] ["first at"=74800000000000003e] ["first new region left"="{Id:52 StartKey:7480000000000000ff3c00000000000000f8 EndKey:7480000000000000ff3e00000000000000f8 RegionEpoch:{ConfVer:1 Version:26} Peers:[id:53 store_id:1 ]}"] ["new region count"=1]
   > [2024/08/02 11:44:41.877 +00:00] [INFO] [raft.rs:783] ["became follower at term 5"] [term=5] [raft_id=53] [region_id=52]
   > [2024/08/02 11:44:41.877 +00:00] [INFO] [split_region.go:207] ["split regions complete"] ["region count"=1] ["region IDs"="[52]"]
   > [2024/08/02 11:44:41.877 +00:00] [INFO] [cluster.go:542] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF3C00000000000000F8} -> {7480000000000000FF3E00000000000000F8}, EndKey:{}"] [old-version=25] [new-version=26]
   > [2024/08/02 11:44:41.877 +00:00] [INFO] [raft.rs:285] [newRaft] [peers="[(53, Progress { matched: 5, next_idx: 6, state: Probe, paused: false, pending_snapshot: 0, pending_request_snapshot: 0, recent_active: false, ins: Inflights { start: 0, count: 0, buffer: [] } })]"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=53] [region_id=52]
   > [2024/08/02 11:44:41.877 +00:00] [INFO] [raw_node.rs:222] ["RawNode created with id 53."] [id=53] [raft_id=53] [region_id=52]
   > [2024/08/02 11:44:41.877 +00:00] [INFO] [cluster_worker.go:223] ["region batch split, generate new regions"] [region-id=2] [origin="id:52 start_key:\"7480000000000000FF3C00000000000000F8\" end_key:\"7480000000000000FF3E00000000000000F8\" region_epoch:<conf_ver:1 version:26 > peers:<id:53 store_id:1 >"] [total=1]
   > [2024/08/02 11:44:41.877 +00:00] [INFO] [raft.rs:1177] ["starting a new election"] [term=5] [raft_id=53] [region_id=52]
   > [2024/08/02 11:44:41.877 +00:00] [INFO] [raft.rs:833] ["became pre-candidate at term 5"] [term=5] [raft_id=53] [region_id=52]
   > [2024/08/02 11:44:41.877 +00:00] [INFO] [raft.rs:902] ["53 received message from 53"] [term=5] [msg=MsgRequestPreVote] [from=53] [id=53] [raft_id=53] [region_id=52]
   > [2024/08/02 11:44:41.877 +00:00] [INFO] [raft.rs:807] ["became candidate at term 6"] [term=6] [raft_id=53] [region_id=52]
   > [2024/08/02 11:44:41.877 +00:00] [INFO] [raft.rs:902] ["53 received message from 53"] [term=6] [msg=MsgRequestVote] [from=53] [id=53] [raft_id=53] [region_id=52]
   > [2024/08/02 11:44:41.878 +00:00] [INFO] [raft.rs:874] ["became leader at term 6"] [term=6] [raft_id=53] [region_id=52]
   > [2024/08/02 11:44:41.887 +00:00] [INFO] [server.go:397] ["connection closed"] [conn=8]
   > [2024/08/02 11:44:42.898 +00:00] [INFO] [server.go:394] ["new connection"] [conn=9] [remoteAddr=127.0.0.1:57890]
   > [2024/08/02 11:44:42.907 +00:00] [INFO] [set.go:216] ["set session var"] [conn=9] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/08/02 11:44:42.908 +00:00] [INFO] [set.go:216] ["set session var"] [conn=9] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/08/02 11:44:42.908 +00:00] [INFO] [set.go:216] ["set session var"] [conn=9] [name=transaction_isolation] [val=READ-COMMITTED]
   > [2024/08/02 11:44:43.806 +00:00] [INFO] [server.go:394] ["new connection"] [conn=10] [remoteAddr=127.0.0.1:57892]
   > [2024/08/02 11:44:43.811 +00:00] [INFO] [set.go:216] ["set session var"] [conn=10] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/08/02 11:44:45.014 +00:00] [INFO] [server.go:394] ["new connection"] [conn=11] [remoteAddr=127.0.0.1:57906]
   > [2024/08/02 11:44:45.023 +00:00] [INFO] [set.go:216] ["set session var"] [conn=11] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/08/02 11:44:45.713 +00:00] [INFO] [server.go:397] ["connection closed"] [conn=9]
   > [2024/08/02 11:44:45.713 +00:00] [INFO] [server.go:397] ["connection closed"] [conn=10]
   > [2024/08/02 11:44:45.713 +00:00] [INFO] [server.go:397] ["connection closed"] [conn=11]
