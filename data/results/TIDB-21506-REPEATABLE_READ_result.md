# Bug ID TIDB-21506-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/21506
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              Inserting data twice when another transaction is updating the data does not fail.


## Details
 * Database: tidb-v4.0.7.tikv
 * Number of scenarios: 1
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ;
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
   > [2024/08/02 11:44:35.649 +00:00] [INFO] [server.go:394] ["new connection"] [conn=2] [remoteAddr=127.0.0.1:58626]
   > [2024/08/02 11:44:35.654 +00:00] [INFO] [session.go:2159] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=22] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/08/02 11:44:35.656 +00:00] [INFO] [session.go:2159] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=22] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/08/02 11:44:35.692 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-02 11:44:35.68 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/02 11:44:35.692 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-02 11:44:35.68 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/08/02 11:44:35.695 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 11:44:35.68 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 11:44:35.709 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=22] [neededSchemaVersion=23] ["start time"=1.259251ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/02 11:44:35.758 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=23] ["take time"=52.62194ms] [job="ID:46, Type:create schema, State:done, SchemaState:public, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-02 11:44:35.68 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 11:44:35.762 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:46, Type:create schema, State:synced, SchemaState:public, SchemaID:45, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-02 11:44:35.68 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 11:44:35.772 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=46]
   > [2024/08/02 11:44:35.772 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/08/02 11:44:35.775 +00:00] [INFO] [session.go:2159] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=23] [cur_db=testdb] [sql="create table t1 (id int primary key, v int);"] [user=root@127.0.0.1]
   > [2024/08/02 11:44:35.793 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-08-02 11:44:35.78 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/02 11:44:35.793 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-08-02 11:44:35.78 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t1 (id int primary key, v int);"]
   > [2024/08/02 11:44:35.797 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-08-02 11:44:35.78 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 11:44:35.814 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=23] [neededSchemaVersion=24] ["start time"=2.001951ms] [phyTblIDs="[47]"] [actionTypes="[8]"]
   > [2024/08/02 11:44:35.862 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=24] ["take time"=51.942378ms] [job="ID:48, Type:create table, State:done, SchemaState:public, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-08-02 11:44:35.78 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 11:44:35.866 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:48, Type:create table, State:synced, SchemaState:public, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-08-02 11:44:35.78 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 11:44:35.876 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=48]
   > [2024/08/02 11:44:35.878 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/08/02 11:44:35.878 +00:00] [INFO] [split_region.go:58] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=74800000000000002f]
   > [2024/08/02 11:44:35.879 +00:00] [INFO] [peer.rs:469] ["on split"] [split_keys="key 7480000000000000FF2F00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/02 11:44:35.879 +00:00] [INFO] [cluster_worker.go:131] ["alloc ids for region split"] [region-id=44] [peer-ids="[45]"]
   > [2024/08/02 11:44:35.879 +00:00] [INFO] [session.go:2159] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=24] [cur_db=testdb] [sql="create table t2 (id int primary key, v int);"] [user=root@127.0.0.1]
   > [2024/08/02 11:44:35.880 +00:00] [INFO] [pd.rs:499] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF2B00000000000000F8 region_epoch { conf_ver: 1 version: 21 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 44 new_peer_ids: 45]"] [region_id=2]
   > [2024/08/02 11:44:35.882 +00:00] [INFO] [apply.rs:1162] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF2F00000000000000F8 new_region_id: 44 new_peer_ids: 45 } right_derive: true }"] [index=53] [term=6] [peer_id=3] [region_id=2]
   > [2024/08/02 11:44:35.883 +00:00] [INFO] [apply.rs:1742] ["split region"] [keys="key 7480000000000000FF2F00000000000000F8"] [region="id: 2 start_key: 7480000000000000FF2B00000000000000F8 region_epoch { conf_ver: 1 version: 21 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/08/02 11:44:35.886 +00:00] [INFO] [peer.rs:1731] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/08/02 11:44:35.887 +00:00] [INFO] [peer.rs:1773] ["insert new region"] [region="id: 44 start_key: 7480000000000000FF2B00000000000000F8 end_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 45 store_id: 1 }"] [region_id=44]
   > [2024/08/02 11:44:35.887 +00:00] [INFO] [peer.rs:159] ["create peer"] [peer_id=45] [region_id=44]
   > [2024/08/02 11:44:35.887 +00:00] [INFO] [raft.rs:783] ["became follower at term 5"] [term=5] [raft_id=45] [region_id=44]
   > [2024/08/02 11:44:35.887 +00:00] [INFO] [split_region.go:155] ["batch split regions complete"] ["batch region ID"=2] ["first at"=74800000000000002f] ["first new region left"="{Id:44 StartKey:7480000000000000ff2b00000000000000f8 EndKey:7480000000000000ff2f00000000000000f8 RegionEpoch:{ConfVer:1 Version:22} Peers:[id:45 store_id:1 ]}"] ["new region count"=1]
   > [2024/08/02 11:44:35.887 +00:00] [INFO] [split_region.go:207] ["split regions complete"] ["region count"=1] ["region IDs"="[44]"]
   > [2024/08/02 11:44:35.887 +00:00] [INFO] [raft.rs:285] [newRaft] [peers="[(45, Progress { matched: 5, next_idx: 6, state: Probe, paused: false, pending_snapshot: 0, pending_request_snapshot: 0, recent_active: false, ins: Inflights { start: 0, count: 0, buffer: [] } })]"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=45] [region_id=44]
   > [2024/08/02 11:44:35.887 +00:00] [INFO] [cluster.go:542] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF2B00000000000000F8} -> {7480000000000000FF2F00000000000000F8}, EndKey:{}"] [old-version=21] [new-version=22]
   > [2024/08/02 11:44:35.887 +00:00] [INFO] [raw_node.rs:222] ["RawNode created with id 45."] [id=45] [raft_id=45] [region_id=44]
   > [2024/08/02 11:44:35.887 +00:00] [INFO] [cluster_worker.go:223] ["region batch split, generate new regions"] [region-id=2] [origin="id:44 start_key:\"7480000000000000FF2B00000000000000F8\" end_key:\"7480000000000000FF2F00000000000000F8\" region_epoch:<conf_ver:1 version:22 > peers:<id:45 store_id:1 >"] [total=1]
   > [2024/08/02 11:44:35.887 +00:00] [INFO] [raft.rs:1177] ["starting a new election"] [term=5] [raft_id=45] [region_id=44]
   > [2024/08/02 11:44:35.887 +00:00] [INFO] [raft.rs:833] ["became pre-candidate at term 5"] [term=5] [raft_id=45] [region_id=44]
   > [2024/08/02 11:44:35.887 +00:00] [INFO] [raft.rs:902] ["45 received message from 45"] [term=5] [msg=MsgRequestPreVote] [from=45] [id=45] [raft_id=45] [region_id=44]
   > [2024/08/02 11:44:35.887 +00:00] [INFO] [raft.rs:807] ["became candidate at term 6"] [term=6] [raft_id=45] [region_id=44]
   > [2024/08/02 11:44:35.888 +00:00] [INFO] [raft.rs:902] ["45 received message from 45"] [term=6] [msg=MsgRequestVote] [from=45] [id=45] [raft_id=45] [region_id=44]
   > [2024/08/02 11:44:35.888 +00:00] [INFO] [raft.rs:874] ["became leader at term 6"] [term=6] [raft_id=45] [region_id=44]
   > [2024/08/02 11:44:35.899 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:50, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:49, RowCount:0, ArgLen:1, start time: 2024-08-02 11:44:35.88 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/02 11:44:35.899 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:50, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:49, RowCount:0, ArgLen:1, start time: 2024-08-02 11:44:35.88 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t2 (id int primary key, v int);"]
   > [2024/08/02 11:44:35.903 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:50, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:49, RowCount:0, ArgLen:0, start time: 2024-08-02 11:44:35.88 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 11:44:35.918 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=24] [neededSchemaVersion=25] ["start time"=1.773847ms] [phyTblIDs="[49]"] [actionTypes="[8]"]
   > [2024/08/02 11:44:35.966 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=25] ["take time"=52.297804ms] [job="ID:50, Type:create table, State:done, SchemaState:public, SchemaID:45, TableID:49, RowCount:0, ArgLen:1, start time: 2024-08-02 11:44:35.88 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 11:44:35.969 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:50, Type:create table, State:synced, SchemaState:public, SchemaID:45, TableID:49, RowCount:0, ArgLen:0, start time: 2024-08-02 11:44:35.88 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/02 11:44:35.979 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=50]
   > [2024/08/02 11:44:35.981 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/08/02 11:44:35.981 +00:00] [INFO] [split_region.go:58] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=748000000000000031]
   > [2024/08/02 11:44:35.982 +00:00] [INFO] [peer.rs:469] ["on split"] [split_keys="key 7480000000000000FF3100000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/02 11:44:35.982 +00:00] [INFO] [peer.rs:2921] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 21"] [prev_epoch="conf_ver: 1 version: 22"] [peer_id=3] [region_id=2]
   > [2024/08/02 11:44:35.986 +00:00] [INFO] [peer.rs:469] ["on split"] [split_keys="key 7480000000000000FF3100000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/02 11:44:35.987 +00:00] [INFO] [cluster_worker.go:131] ["alloc ids for region split"] [region-id=46] [peer-ids="[47]"]
   > [2024/08/02 11:44:35.987 +00:00] [INFO] [pd.rs:499] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 46 new_peer_ids: 47]"] [region_id=2]
   > [2024/08/02 11:44:35.990 +00:00] [INFO] [apply.rs:1162] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF3100000000000000F8 new_region_id: 46 new_peer_ids: 47 } right_derive: true }"] [index=55] [term=6] [peer_id=3] [region_id=2]
   > [2024/08/02 11:44:35.990 +00:00] [INFO] [apply.rs:1742] ["split region"] [keys="key 7480000000000000FF3100000000000000F8"] [region="id: 2 start_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/08/02 11:44:35.992 +00:00] [INFO] [peer.rs:1731] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/08/02 11:44:35.993 +00:00] [INFO] [peer.rs:1773] ["insert new region"] [region="id: 46 start_key: 7480000000000000FF2F00000000000000F8 end_key: 7480000000000000FF3100000000000000F8 region_epoch { conf_ver: 1 version: 23 } peers { id: 47 store_id: 1 }"] [region_id=46]
   > [2024/08/02 11:44:35.993 +00:00] [INFO] [peer.rs:159] ["create peer"] [peer_id=47] [region_id=46]
   > [2024/08/02 11:44:35.993 +00:00] [INFO] [raft.rs:783] ["became follower at term 5"] [term=5] [raft_id=47] [region_id=46]
   > [2024/08/02 11:44:35.993 +00:00] [INFO] [split_region.go:155] ["batch split regions complete"] ["batch region ID"=2] ["first at"=748000000000000031] ["first new region left"="{Id:46 StartKey:7480000000000000ff2f00000000000000f8 EndKey:7480000000000000ff3100000000000000f8 RegionEpoch:{ConfVer:1 Version:23} Peers:[id:47 store_id:1 ]}"] ["new region count"=1]
   > [2024/08/02 11:44:35.993 +00:00] [INFO] [cluster.go:542] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF2F00000000000000F8} -> {7480000000000000FF3100000000000000F8}, EndKey:{}"] [old-version=22] [new-version=23]
   > [2024/08/02 11:44:35.993 +00:00] [INFO] [split_region.go:207] ["split regions complete"] ["region count"=1] ["region IDs"="[46]"]
   > [2024/08/02 11:44:35.993 +00:00] [INFO] [raft.rs:285] [newRaft] [peers="[(47, Progress { matched: 5, next_idx: 6, state: Probe, paused: false, pending_snapshot: 0, pending_request_snapshot: 0, recent_active: false, ins: Inflights { start: 0, count: 0, buffer: [] } })]"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=47] [region_id=46]
   > [2024/08/02 11:44:35.993 +00:00] [INFO] [raw_node.rs:222] ["RawNode created with id 47."] [id=47] [raft_id=47] [region_id=46]
   > [2024/08/02 11:44:35.993 +00:00] [INFO] [raft.rs:1177] ["starting a new election"] [term=5] [raft_id=47] [region_id=46]
   > [2024/08/02 11:44:35.993 +00:00] [INFO] [cluster_worker.go:223] ["region batch split, generate new regions"] [region-id=2] [origin="id:46 start_key:\"7480000000000000FF2F00000000000000F8\" end_key:\"7480000000000000FF3100000000000000F8\" region_epoch:<conf_ver:1 version:23 > peers:<id:47 store_id:1 >"] [total=1]
   > [2024/08/02 11:44:35.993 +00:00] [INFO] [raft.rs:833] ["became pre-candidate at term 5"] [term=5] [raft_id=47] [region_id=46]
   > [2024/08/02 11:44:35.993 +00:00] [INFO] [raft.rs:902] ["47 received message from 47"] [term=5] [msg=MsgRequestPreVote] [from=47] [id=47] [raft_id=47] [region_id=46]
   > [2024/08/02 11:44:35.994 +00:00] [INFO] [raft.rs:807] ["became candidate at term 6"] [term=6] [raft_id=47] [region_id=46]
   > [2024/08/02 11:44:35.994 +00:00] [INFO] [raft.rs:902] ["47 received message from 47"] [term=6] [msg=MsgRequestVote] [from=47] [id=47] [raft_id=47] [region_id=46]
   > [2024/08/02 11:44:35.994 +00:00] [INFO] [raft.rs:874] ["became leader at term 6"] [term=6] [raft_id=47] [region_id=46]
   > [2024/08/02 11:44:36.005 +00:00] [INFO] [server.go:397] ["connection closed"] [conn=2]
   > [2024/08/02 11:44:37.021 +00:00] [INFO] [server.go:394] ["new connection"] [conn=4] [remoteAddr=127.0.0.1:58650]
   > [2024/08/02 11:44:37.024 +00:00] [INFO] [set.go:216] ["set session var"] [conn=4] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/08/02 11:44:37.025 +00:00] [INFO] [set.go:216] ["set session var"] [conn=4] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/08/02 11:44:37.025 +00:00] [INFO] [set.go:216] ["set session var"] [conn=4] [name=transaction_isolation] [val=REPEATABLE-READ]
   > [2024/08/02 11:44:37.929 +00:00] [INFO] [server.go:394] ["new connection"] [conn=5] [remoteAddr=127.0.0.1:58664]
   > [2024/08/02 11:44:37.938 +00:00] [INFO] [set.go:216] ["set session var"] [conn=5] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/08/02 11:44:39.138 +00:00] [INFO] [server.go:394] ["new connection"] [conn=6] [remoteAddr=127.0.0.1:57860]
   > [2024/08/02 11:44:39.142 +00:00] [INFO] [set.go:216] ["set session var"] [conn=6] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/08/02 11:44:39.840 +00:00] [INFO] [server.go:397] ["connection closed"] [conn=4]
   > [2024/08/02 11:44:39.840 +00:00] [INFO] [server.go:397] ["connection closed"] [conn=5]
   > [2024/08/02 11:44:39.840 +00:00] [INFO] [server.go:397] ["connection closed"] [conn=6]
