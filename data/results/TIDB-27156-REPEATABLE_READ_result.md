# Bug ID TIDB-27156-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/27156
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              Playing with lock_wait_timeout and txn_mode makes the same commit succeed / fail.


## Details
 * Database: tidb-v5.2.0-alpha-26237b35.tikv
 * Number of scenarios: 1
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
     - Output: [(3, 3, 3, 3), (4, 4, 4, 4)]
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
   > [2024/08/06 12:13:56.556 +00:00] [INFO] [session.go:2945] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=26] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/08/06 12:13:56.557 +00:00] [INFO] [session.go:2945] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=26] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/08/06 12:13:56.598 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:54, Type:create schema, State:none, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-06 12:13:56.568 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/06 12:13:56.598 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:54, Type:create schema, State:none, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-06 12:13:56.568 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/08/06 12:13:56.602 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:54, Type:create schema, State:none, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-06 12:13:56.568 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 12:13:56.627 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=26] [neededSchemaVersion=27] ["start time"=1.689828ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/06 12:13:56.675 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=27] ["take time"=52.400749ms] [job="ID:54, Type:create schema, State:done, SchemaState:public, SchemaID:53, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-06 12:13:56.568 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 12:13:56.678 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:54, Type:create schema, State:synced, SchemaState:public, SchemaID:53, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-06 12:13:56.568 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 12:13:56.703 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=54]
   > [2024/08/06 12:13:56.703 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/08/06 12:13:56.706 +00:00] [INFO] [session.go:2945] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=27] [cur_db=testdb] [sql="create table t2(c1 int primary key, c2 int, c3 int, c4 int, key k2(c2), key k3(c3)) partition by hash(c1) partitions 10;"] [user=root@127.0.0.1]
   > [2024/08/06 12:13:56.771 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:66, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:55, RowCount:0, ArgLen:1, start time: 2024-08-06 12:13:56.718 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/06 12:13:56.771 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:66, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:55, RowCount:0, ArgLen:1, start time: 2024-08-06 12:13:56.718 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t2(c1 int primary key, c2 int, c3 int, c4 int, key k2(c2), key k3(c3)) partition by hash(c1) partitions 10;"]
   > [2024/08/06 12:13:56.776 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:55, RowCount:0, ArgLen:0, start time: 2024-08-06 12:13:56.718 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 12:13:56.824 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=27] [neededSchemaVersion=28] ["start time"=8.921345ms] [phyTblIDs="[55,56,57,58,59,60,61,62,63,64,65]"] [actionTypes="[8,8,8,8,8,8,8,8,8,8,8]"]
   > [2024/08/06 12:13:56.866 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=28] ["take time"=52.496224ms] [job="ID:66, Type:create table, State:done, SchemaState:public, SchemaID:53, TableID:55, RowCount:0, ArgLen:1, start time: 2024-08-06 12:13:56.718 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 12:13:56.869 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:create table, State:synced, SchemaState:public, SchemaID:53, TableID:55, RowCount:0, ArgLen:0, start time: 2024-08-06 12:13:56.718 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 12:13:56.910 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=66]
   > [2024/08/06 12:13:56.910 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/08/06 12:13:56.910 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=748000000000000038]
   > [2024/08/06 12:13:56.910 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56014] [split_keys="key 7480000000000000FF3800000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:56.911 +00:00] [INFO] [cluster_worker.go:127] ["alloc ids for region split"] [region-id=52] [peer-ids="[53]"]
   > [2024/08/06 12:13:56.911 +00:00] [INFO] [pd.rs:749] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF3300000000000000F8 region_epoch { conf_ver: 1 version: 25 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 52 new_peer_ids: 53]"] [region_id=2]
   > [2024/08/06 12:13:56.930 +00:00] [INFO] [apply.rs:1394] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF3800000000000000F8 new_region_id: 52 new_peer_ids: 53 } right_derive: true }"] [index=60] [term=6] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:56.930 +00:00] [INFO] [apply.rs:2242] ["split region"] [keys="key 7480000000000000FF3800000000000000F8"] [region="id: 2 start_key: 7480000000000000FF3300000000000000F8 region_epoch { conf_ver: 1 version: 25 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:56.941 +00:00] [INFO] [endpoint.rs:158] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/08/06 12:13:56.941 +00:00] [INFO] [peer.rs:2411] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:56.941 +00:00] [INFO] [peer.rs:2476] ["insert new region"] [region="id: 52 start_key: 7480000000000000FF3300000000000000F8 end_key: 7480000000000000FF3800000000000000F8 region_epoch { conf_ver: 1 version: 26 } peers { id: 53 store_id: 1 }"] [region_id=52]
   > [2024/08/06 12:13:56.941 +00:00] [INFO] [peer.rs:219] ["create peer"] [peer_id=53] [region_id=52]
   > [2024/08/06 12:13:56.941 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=2] ["first at"=748000000000000038] ["first new region left"="{Id:52 StartKey:7480000000000000ff3300000000000000f8 EndKey:7480000000000000ff3800000000000000f8 RegionEpoch:{ConfVer:1 Version:26} Peers:[id:53 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/08/06 12:13:56.941 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[52]"]
   > [2024/08/06 12:13:56.941 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=748000000000000039]
   > [2024/08/06 12:13:56.941 +00:00] [INFO] [region.go:505] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF3300000000000000F8} -> {7480000000000000FF3800000000000000F8}, EndKey:{}"] [old-version=25] [new-version=26]
   > [2024/08/06 12:13:56.941 +00:00] [INFO] [cluster_worker.go:219] ["region batch split, generate new regions"] [region-id=2] [origin="id:52 start_key:\"7480000000000000FF3300000000000000F8\" end_key:\"7480000000000000FF3800000000000000F8\" region_epoch:<conf_ver:1 version:26 > peers:<id:53 store_id:1 >"] [total=1]
   > [2024/08/06 12:13:56.951 +00:00] [INFO] [raft.rs:2609] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {53} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=53] [region_id=52]
   > [2024/08/06 12:13:56.951 +00:00] [INFO] [raft.rs:1092] ["became follower at term 5"] [term=5] [raft_id=53] [region_id=52]
   > [2024/08/06 12:13:56.951 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {53} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=53] [region_id=52]
   > [2024/08/06 12:13:56.951 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 53."] [id=53] [raft_id=53] [region_id=52]
   > [2024/08/06 12:13:56.951 +00:00] [INFO] [raft.rs:1517] ["starting a new election"] [term=5] [raft_id=53] [region_id=52]
   > [2024/08/06 12:13:56.951 +00:00] [INFO] [raft.rs:1142] ["became pre-candidate at term 5"] [term=5] [raft_id=53] [region_id=52]
   > [2024/08/06 12:13:56.951 +00:00] [INFO] [raft.rs:1116] ["became candidate at term 6"] [term=6] [raft_id=53] [region_id=52]
   > [2024/08/06 12:13:56.952 +00:00] [INFO] [raft.rs:1200] ["became leader at term 6"] [term=6] [raft_id=53] [region_id=52]
   > [2024/08/06 12:13:56.952 +00:00] [INFO] [peer.rs:3778] ["require updating max ts"] [initial_status=25769803828] [region_id=52]
   > [2024/08/06 12:13:56.952 +00:00] [INFO] [endpoint.rs:382] ["deregister observe region"] [observe_id=ObserveID(47)] [region_id=2] [store_id=Some(1)]
   > [2024/08/06 12:13:56.952 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF3800000000000000F8 region_epoch { conf_ver: 1 version: 26 } peers { id: 3 store_id: 1 }"]
   > [2024/08/06 12:13:56.952 +00:00] [INFO] [pd.rs:1246] ["succeed to update max timestamp"] [region_id=52]
   > [2024/08/06 12:13:56.971 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56024] [split_keys="key 7480000000000000FF3900000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:56.972 +00:00] [INFO] [peer.rs:3911] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 25"] [prev_epoch="conf_ver: 1 version: 26"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:56.972 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 52 start_key: 7480000000000000FF3300000000000000F8 end_key: 7480000000000000FF3800000000000000F8 region_epoch { conf_ver: 1 version: 26 } peers { id: 53 store_id: 1 }"]
   > [2024/08/06 12:13:56.972 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=60] [observe_id=ObserveID(49)] [region=2]
   > [2024/08/06 12:13:56.972 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveID(50)] [region=52]
   > [2024/08/06 12:13:56.993 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56032] [split_keys="key 7480000000000000FF3900000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:56.994 +00:00] [INFO] [cluster_worker.go:127] ["alloc ids for region split"] [region-id=54] [peer-ids="[55]"]
   > [2024/08/06 12:13:56.994 +00:00] [INFO] [pd.rs:749] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF3800000000000000F8 region_epoch { conf_ver: 1 version: 26 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 54 new_peer_ids: 55]"] [region_id=2]
   > [2024/08/06 12:13:57.024 +00:00] [INFO] [apply.rs:1394] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF3900000000000000F8 new_region_id: 54 new_peer_ids: 55 } right_derive: true }"] [index=62] [term=6] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.024 +00:00] [INFO] [apply.rs:2242] ["split region"] [keys="key 7480000000000000FF3900000000000000F8"] [region="id: 2 start_key: 7480000000000000FF3800000000000000F8 region_epoch { conf_ver: 1 version: 26 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.035 +00:00] [INFO] [endpoint.rs:158] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/08/06 12:13:57.035 +00:00] [INFO] [peer.rs:2411] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.035 +00:00] [INFO] [peer.rs:2476] ["insert new region"] [region="id: 54 start_key: 7480000000000000FF3800000000000000F8 end_key: 7480000000000000FF3900000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 55 store_id: 1 }"] [region_id=54]
   > [2024/08/06 12:13:57.035 +00:00] [INFO] [peer.rs:219] ["create peer"] [peer_id=55] [region_id=54]
   > [2024/08/06 12:13:57.036 +00:00] [INFO] [region.go:505] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF3800000000000000F8} -> {7480000000000000FF3900000000000000F8}, EndKey:{}"] [old-version=26] [new-version=27]
   > [2024/08/06 12:13:57.036 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=2] ["first at"=748000000000000039] ["first new region left"="{Id:54 StartKey:7480000000000000ff3800000000000000f8 EndKey:7480000000000000ff3900000000000000f8 RegionEpoch:{ConfVer:1 Version:27} Peers:[id:55 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/08/06 12:13:57.036 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[54]"]
   > [2024/08/06 12:13:57.036 +00:00] [INFO] [cluster_worker.go:219] ["region batch split, generate new regions"] [region-id=2] [origin="id:54 start_key:\"7480000000000000FF3800000000000000F8\" end_key:\"7480000000000000FF3900000000000000F8\" region_epoch:<conf_ver:1 version:27 > peers:<id:55 store_id:1 >"] [total=1]
   > [2024/08/06 12:13:57.036 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=74800000000000003a]
   > [2024/08/06 12:13:57.045 +00:00] [INFO] [raft.rs:2609] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {55} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=55] [region_id=54]
   > [2024/08/06 12:13:57.045 +00:00] [INFO] [raft.rs:1092] ["became follower at term 5"] [term=5] [raft_id=55] [region_id=54]
   > [2024/08/06 12:13:57.045 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {55} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=55] [region_id=54]
   > [2024/08/06 12:13:57.045 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 55."] [id=55] [raft_id=55] [region_id=54]
   > [2024/08/06 12:13:57.045 +00:00] [INFO] [raft.rs:1517] ["starting a new election"] [term=5] [raft_id=55] [region_id=54]
   > [2024/08/06 12:13:57.046 +00:00] [INFO] [raft.rs:1142] ["became pre-candidate at term 5"] [term=5] [raft_id=55] [region_id=54]
   > [2024/08/06 12:13:57.046 +00:00] [INFO] [raft.rs:1116] ["became candidate at term 6"] [term=6] [raft_id=55] [region_id=54]
   > [2024/08/06 12:13:57.046 +00:00] [INFO] [raft.rs:1200] ["became leader at term 6"] [term=6] [raft_id=55] [region_id=54]
   > [2024/08/06 12:13:57.046 +00:00] [INFO] [peer.rs:3778] ["require updating max ts"] [initial_status=25769803830] [region_id=54]
   > [2024/08/06 12:13:57.046 +00:00] [INFO] [endpoint.rs:382] ["deregister observe region"] [observe_id=ObserveID(49)] [region_id=2] [store_id=Some(1)]
   > [2024/08/06 12:13:57.046 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF3900000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 3 store_id: 1 }"]
   > [2024/08/06 12:13:57.046 +00:00] [INFO] [pd.rs:1246] ["succeed to update max timestamp"] [region_id=54]
   > [2024/08/06 12:13:57.064 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56000] [split_keys="key 7480000000000000FF3A00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.064 +00:00] [INFO] [peer.rs:3911] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 26"] [prev_epoch="conf_ver: 1 version: 27"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.065 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 54 start_key: 7480000000000000FF3800000000000000F8 end_key: 7480000000000000FF3900000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 55 store_id: 1 }"]
   > [2024/08/06 12:13:57.065 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=62] [observe_id=ObserveID(51)] [region=2]
   > [2024/08/06 12:13:57.065 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveID(52)] [region=54]
   > [2024/08/06 12:13:57.067 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56014] [split_keys="key 7480000000000000FF3A00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.068 +00:00] [INFO] [cluster_worker.go:127] ["alloc ids for region split"] [region-id=56] [peer-ids="[57]"]
   > [2024/08/06 12:13:57.068 +00:00] [INFO] [pd.rs:749] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF3900000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 56 new_peer_ids: 57]"] [region_id=2]
   > [2024/08/06 12:13:57.085 +00:00] [INFO] [apply.rs:1394] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF3A00000000000000F8 new_region_id: 56 new_peer_ids: 57 } right_derive: true }"] [index=63] [term=6] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.085 +00:00] [INFO] [apply.rs:2242] ["split region"] [keys="key 7480000000000000FF3A00000000000000F8"] [region="id: 2 start_key: 7480000000000000FF3900000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.095 +00:00] [INFO] [endpoint.rs:158] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/08/06 12:13:57.095 +00:00] [INFO] [peer.rs:2411] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.095 +00:00] [INFO] [peer.rs:2476] ["insert new region"] [region="id: 56 start_key: 7480000000000000FF3900000000000000F8 end_key: 7480000000000000FF3A00000000000000F8 region_epoch { conf_ver: 1 version: 28 } peers { id: 57 store_id: 1 }"] [region_id=56]
   > [2024/08/06 12:13:57.095 +00:00] [INFO] [peer.rs:219] ["create peer"] [peer_id=57] [region_id=56]
   > [2024/08/06 12:13:57.095 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=2] ["first at"=74800000000000003a] ["first new region left"="{Id:56 StartKey:7480000000000000ff3900000000000000f8 EndKey:7480000000000000ff3a00000000000000f8 RegionEpoch:{ConfVer:1 Version:28} Peers:[id:57 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/08/06 12:13:57.096 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[56]"]
   > [2024/08/06 12:13:57.096 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=74800000000000003b]
   > [2024/08/06 12:13:57.096 +00:00] [INFO] [region.go:505] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF3900000000000000F8} -> {7480000000000000FF3A00000000000000F8}, EndKey:{}"] [old-version=27] [new-version=28]
   > [2024/08/06 12:13:57.096 +00:00] [INFO] [cluster_worker.go:219] ["region batch split, generate new regions"] [region-id=2] [origin="id:56 start_key:\"7480000000000000FF3900000000000000F8\" end_key:\"7480000000000000FF3A00000000000000F8\" region_epoch:<conf_ver:1 version:28 > peers:<id:57 store_id:1 >"] [total=1]
   > [2024/08/06 12:13:57.105 +00:00] [INFO] [raft.rs:2609] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {57} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=57] [region_id=56]
   > [2024/08/06 12:13:57.105 +00:00] [INFO] [raft.rs:1092] ["became follower at term 5"] [term=5] [raft_id=57] [region_id=56]
   > [2024/08/06 12:13:57.105 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {57} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=57] [region_id=56]
   > [2024/08/06 12:13:57.106 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 57."] [id=57] [raft_id=57] [region_id=56]
   > [2024/08/06 12:13:57.106 +00:00] [INFO] [raft.rs:1517] ["starting a new election"] [term=5] [raft_id=57] [region_id=56]
   > [2024/08/06 12:13:57.106 +00:00] [INFO] [raft.rs:1142] ["became pre-candidate at term 5"] [term=5] [raft_id=57] [region_id=56]
   > [2024/08/06 12:13:57.106 +00:00] [INFO] [raft.rs:1116] ["became candidate at term 6"] [term=6] [raft_id=57] [region_id=56]
   > [2024/08/06 12:13:57.106 +00:00] [INFO] [raft.rs:1200] ["became leader at term 6"] [term=6] [raft_id=57] [region_id=56]
   > [2024/08/06 12:13:57.106 +00:00] [INFO] [endpoint.rs:382] ["deregister observe region"] [observe_id=ObserveID(51)] [region_id=2] [store_id=Some(1)]
   > [2024/08/06 12:13:57.106 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF3A00000000000000F8 region_epoch { conf_ver: 1 version: 28 } peers { id: 3 store_id: 1 }"]
   > [2024/08/06 12:13:57.106 +00:00] [INFO] [peer.rs:3778] ["require updating max ts"] [initial_status=25769803832] [region_id=56]
   > [2024/08/06 12:13:57.106 +00:00] [INFO] [pd.rs:1246] ["succeed to update max timestamp"] [region_id=56]
   > [2024/08/06 12:13:57.124 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56024] [split_keys="key 7480000000000000FF3B00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.124 +00:00] [INFO] [peer.rs:3911] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 27"] [prev_epoch="conf_ver: 1 version: 28"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.125 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 56 start_key: 7480000000000000FF3900000000000000F8 end_key: 7480000000000000FF3A00000000000000F8 region_epoch { conf_ver: 1 version: 28 } peers { id: 57 store_id: 1 }"]
   > [2024/08/06 12:13:57.125 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=63] [observe_id=ObserveID(53)] [region=2]
   > [2024/08/06 12:13:57.125 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveID(54)] [region=56]
   > [2024/08/06 12:13:57.128 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56032] [split_keys="key 7480000000000000FF3B00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.128 +00:00] [INFO] [cluster_worker.go:127] ["alloc ids for region split"] [region-id=58] [peer-ids="[59]"]
   > [2024/08/06 12:13:57.128 +00:00] [INFO] [pd.rs:749] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF3A00000000000000F8 region_epoch { conf_ver: 1 version: 28 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 58 new_peer_ids: 59]"] [region_id=2]
   > [2024/08/06 12:13:57.144 +00:00] [INFO] [apply.rs:1394] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF3B00000000000000F8 new_region_id: 58 new_peer_ids: 59 } right_derive: true }"] [index=64] [term=6] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.144 +00:00] [INFO] [apply.rs:2242] ["split region"] [keys="key 7480000000000000FF3B00000000000000F8"] [region="id: 2 start_key: 7480000000000000FF3A00000000000000F8 region_epoch { conf_ver: 1 version: 28 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.154 +00:00] [INFO] [endpoint.rs:158] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/08/06 12:13:57.154 +00:00] [INFO] [peer.rs:2411] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.154 +00:00] [INFO] [peer.rs:2476] ["insert new region"] [region="id: 58 start_key: 7480000000000000FF3A00000000000000F8 end_key: 7480000000000000FF3B00000000000000F8 region_epoch { conf_ver: 1 version: 29 } peers { id: 59 store_id: 1 }"] [region_id=58]
   > [2024/08/06 12:13:57.154 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=2] ["first at"=74800000000000003b] ["first new region left"="{Id:58 StartKey:7480000000000000ff3a00000000000000f8 EndKey:7480000000000000ff3b00000000000000f8 RegionEpoch:{ConfVer:1 Version:29} Peers:[id:59 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/08/06 12:13:57.154 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[58]"]
   > [2024/08/06 12:13:57.154 +00:00] [INFO] [peer.rs:219] ["create peer"] [peer_id=59] [region_id=58]
   > [2024/08/06 12:13:57.154 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=74800000000000003c]
   > [2024/08/06 12:13:57.155 +00:00] [INFO] [region.go:505] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF3A00000000000000F8} -> {7480000000000000FF3B00000000000000F8}, EndKey:{}"] [old-version=28] [new-version=29]
   > [2024/08/06 12:13:57.155 +00:00] [INFO] [cluster_worker.go:219] ["region batch split, generate new regions"] [region-id=2] [origin="id:58 start_key:\"7480000000000000FF3A00000000000000F8\" end_key:\"7480000000000000FF3B00000000000000F8\" region_epoch:<conf_ver:1 version:29 > peers:<id:59 store_id:1 >"] [total=1]
   > [2024/08/06 12:13:57.163 +00:00] [INFO] [raft.rs:2609] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {59} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=59] [region_id=58]
   > [2024/08/06 12:13:57.164 +00:00] [INFO] [raft.rs:1092] ["became follower at term 5"] [term=5] [raft_id=59] [region_id=58]
   > [2024/08/06 12:13:57.164 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {59} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=59] [region_id=58]
   > [2024/08/06 12:13:57.164 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 59."] [id=59] [raft_id=59] [region_id=58]
   > [2024/08/06 12:13:57.164 +00:00] [INFO] [raft.rs:1517] ["starting a new election"] [term=5] [raft_id=59] [region_id=58]
   > [2024/08/06 12:13:57.164 +00:00] [INFO] [raft.rs:1142] ["became pre-candidate at term 5"] [term=5] [raft_id=59] [region_id=58]
   > [2024/08/06 12:13:57.164 +00:00] [INFO] [raft.rs:1116] ["became candidate at term 6"] [term=6] [raft_id=59] [region_id=58]
   > [2024/08/06 12:13:57.164 +00:00] [INFO] [raft.rs:1200] ["became leader at term 6"] [term=6] [raft_id=59] [region_id=58]
   > [2024/08/06 12:13:57.164 +00:00] [INFO] [endpoint.rs:382] ["deregister observe region"] [observe_id=ObserveID(53)] [region_id=2] [store_id=Some(1)]
   > [2024/08/06 12:13:57.164 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF3B00000000000000F8 region_epoch { conf_ver: 1 version: 29 } peers { id: 3 store_id: 1 }"]
   > [2024/08/06 12:13:57.164 +00:00] [INFO] [peer.rs:3778] ["require updating max ts"] [initial_status=25769803834] [region_id=58]
   > [2024/08/06 12:13:57.165 +00:00] [INFO] [pd.rs:1246] ["succeed to update max timestamp"] [region_id=58]
   > [2024/08/06 12:13:57.184 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56000] [split_keys="key 7480000000000000FF3C00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.184 +00:00] [INFO] [peer.rs:3911] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 28"] [prev_epoch="conf_ver: 1 version: 29"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.184 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 58 start_key: 7480000000000000FF3A00000000000000F8 end_key: 7480000000000000FF3B00000000000000F8 region_epoch { conf_ver: 1 version: 29 } peers { id: 59 store_id: 1 }"]
   > [2024/08/06 12:13:57.184 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=64] [observe_id=ObserveID(55)] [region=2]
   > [2024/08/06 12:13:57.184 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveID(56)] [region=58]
   > [2024/08/06 12:13:57.187 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56014] [split_keys="key 7480000000000000FF3C00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.187 +00:00] [INFO] [cluster_worker.go:127] ["alloc ids for region split"] [region-id=60] [peer-ids="[61]"]
   > [2024/08/06 12:13:57.188 +00:00] [INFO] [pd.rs:749] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF3B00000000000000F8 region_epoch { conf_ver: 1 version: 29 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 60 new_peer_ids: 61]"] [region_id=2]
   > [2024/08/06 12:13:57.203 +00:00] [INFO] [apply.rs:1394] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF3C00000000000000F8 new_region_id: 60 new_peer_ids: 61 } right_derive: true }"] [index=65] [term=6] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.203 +00:00] [INFO] [apply.rs:2242] ["split region"] [keys="key 7480000000000000FF3C00000000000000F8"] [region="id: 2 start_key: 7480000000000000FF3B00000000000000F8 region_epoch { conf_ver: 1 version: 29 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.213 +00:00] [INFO] [endpoint.rs:158] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/08/06 12:13:57.213 +00:00] [INFO] [peer.rs:2411] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.214 +00:00] [INFO] [peer.rs:2476] ["insert new region"] [region="id: 60 start_key: 7480000000000000FF3B00000000000000F8 end_key: 7480000000000000FF3C00000000000000F8 region_epoch { conf_ver: 1 version: 30 } peers { id: 61 store_id: 1 }"] [region_id=60]
   > [2024/08/06 12:13:57.214 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=2] ["first at"=74800000000000003c] ["first new region left"="{Id:60 StartKey:7480000000000000ff3b00000000000000f8 EndKey:7480000000000000ff3c00000000000000f8 RegionEpoch:{ConfVer:1 Version:30} Peers:[id:61 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/08/06 12:13:57.214 +00:00] [INFO] [peer.rs:219] ["create peer"] [peer_id=61] [region_id=60]
   > [2024/08/06 12:13:57.214 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[60]"]
   > [2024/08/06 12:13:57.214 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=74800000000000003d]
   > [2024/08/06 12:13:57.214 +00:00] [INFO] [region.go:505] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF3B00000000000000F8} -> {7480000000000000FF3C00000000000000F8}, EndKey:{}"] [old-version=29] [new-version=30]
   > [2024/08/06 12:13:57.214 +00:00] [INFO] [cluster_worker.go:219] ["region batch split, generate new regions"] [region-id=2] [origin="id:60 start_key:\"7480000000000000FF3B00000000000000F8\" end_key:\"7480000000000000FF3C00000000000000F8\" region_epoch:<conf_ver:1 version:30 > peers:<id:61 store_id:1 >"] [total=1]
   > [2024/08/06 12:13:57.223 +00:00] [INFO] [raft.rs:2609] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {61} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=61] [region_id=60]
   > [2024/08/06 12:13:57.223 +00:00] [INFO] [raft.rs:1092] ["became follower at term 5"] [term=5] [raft_id=61] [region_id=60]
   > [2024/08/06 12:13:57.223 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {61} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=61] [region_id=60]
   > [2024/08/06 12:13:57.223 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 61."] [id=61] [raft_id=61] [region_id=60]
   > [2024/08/06 12:13:57.223 +00:00] [INFO] [raft.rs:1517] ["starting a new election"] [term=5] [raft_id=61] [region_id=60]
   > [2024/08/06 12:13:57.223 +00:00] [INFO] [raft.rs:1142] ["became pre-candidate at term 5"] [term=5] [raft_id=61] [region_id=60]
   > [2024/08/06 12:13:57.224 +00:00] [INFO] [raft.rs:1116] ["became candidate at term 6"] [term=6] [raft_id=61] [region_id=60]
   > [2024/08/06 12:13:57.224 +00:00] [INFO] [raft.rs:1200] ["became leader at term 6"] [term=6] [raft_id=61] [region_id=60]
   > [2024/08/06 12:13:57.224 +00:00] [INFO] [endpoint.rs:382] ["deregister observe region"] [observe_id=ObserveID(55)] [region_id=2] [store_id=Some(1)]
   > [2024/08/06 12:13:57.224 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF3C00000000000000F8 region_epoch { conf_ver: 1 version: 30 } peers { id: 3 store_id: 1 }"]
   > [2024/08/06 12:13:57.224 +00:00] [INFO] [peer.rs:3778] ["require updating max ts"] [initial_status=25769803836] [region_id=60]
   > [2024/08/06 12:13:57.224 +00:00] [INFO] [pd.rs:1246] ["succeed to update max timestamp"] [region_id=60]
   > [2024/08/06 12:13:57.242 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56024] [split_keys="key 7480000000000000FF3D00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.242 +00:00] [INFO] [peer.rs:3911] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 29"] [prev_epoch="conf_ver: 1 version: 30"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.242 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=65] [observe_id=ObserveID(57)] [region=2]
   > [2024/08/06 12:13:57.252 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56032] [split_keys="key 7480000000000000FF3D00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.252 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 60 start_key: 7480000000000000FF3B00000000000000F8 end_key: 7480000000000000FF3C00000000000000F8 region_epoch { conf_ver: 1 version: 30 } peers { id: 61 store_id: 1 }"]
   > [2024/08/06 12:13:57.252 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveID(58)] [region=60]
   > [2024/08/06 12:13:57.252 +00:00] [INFO] [cluster_worker.go:127] ["alloc ids for region split"] [region-id=62] [peer-ids="[63]"]
   > [2024/08/06 12:13:57.253 +00:00] [INFO] [pd.rs:749] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF3C00000000000000F8 region_epoch { conf_ver: 1 version: 30 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 62 new_peer_ids: 63]"] [region_id=2]
   > [2024/08/06 12:13:57.281 +00:00] [INFO] [apply.rs:1394] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF3D00000000000000F8 new_region_id: 62 new_peer_ids: 63 } right_derive: true }"] [index=66] [term=6] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.281 +00:00] [INFO] [apply.rs:2242] ["split region"] [keys="key 7480000000000000FF3D00000000000000F8"] [region="id: 2 start_key: 7480000000000000FF3C00000000000000F8 region_epoch { conf_ver: 1 version: 30 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.291 +00:00] [INFO] [endpoint.rs:158] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/08/06 12:13:57.291 +00:00] [INFO] [peer.rs:2411] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.291 +00:00] [INFO] [peer.rs:2476] ["insert new region"] [region="id: 62 start_key: 7480000000000000FF3C00000000000000F8 end_key: 7480000000000000FF3D00000000000000F8 region_epoch { conf_ver: 1 version: 31 } peers { id: 63 store_id: 1 }"] [region_id=62]
   > [2024/08/06 12:13:57.291 +00:00] [INFO] [peer.rs:219] ["create peer"] [peer_id=63] [region_id=62]
   > [2024/08/06 12:13:57.291 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=2] ["first at"=74800000000000003d] ["first new region left"="{Id:62 StartKey:7480000000000000ff3c00000000000000f8 EndKey:7480000000000000ff3d00000000000000f8 RegionEpoch:{ConfVer:1 Version:31} Peers:[id:63 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/08/06 12:13:57.291 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[62]"]
   > [2024/08/06 12:13:57.291 +00:00] [INFO] [raft.rs:2609] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {63} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=63] [region_id=62]
   > [2024/08/06 12:13:57.291 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=74800000000000003e]
   > [2024/08/06 12:13:57.291 +00:00] [INFO] [raft.rs:1092] ["became follower at term 5"] [term=5] [raft_id=63] [region_id=62]
   > [2024/08/06 12:13:57.291 +00:00] [INFO] [region.go:505] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF3C00000000000000F8} -> {7480000000000000FF3D00000000000000F8}, EndKey:{}"] [old-version=30] [new-version=31]
   > [2024/08/06 12:13:57.291 +00:00] [INFO] [cluster_worker.go:219] ["region batch split, generate new regions"] [region-id=2] [origin="id:62 start_key:\"7480000000000000FF3C00000000000000F8\" end_key:\"7480000000000000FF3D00000000000000F8\" region_epoch:<conf_ver:1 version:31 > peers:<id:63 store_id:1 >"] [total=1]
   > [2024/08/06 12:13:57.291 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {63} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=63] [region_id=62]
   > [2024/08/06 12:13:57.292 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 63."] [id=63] [raft_id=63] [region_id=62]
   > [2024/08/06 12:13:57.292 +00:00] [INFO] [raft.rs:1517] ["starting a new election"] [term=5] [raft_id=63] [region_id=62]
   > [2024/08/06 12:13:57.292 +00:00] [INFO] [raft.rs:1142] ["became pre-candidate at term 5"] [term=5] [raft_id=63] [region_id=62]
   > [2024/08/06 12:13:57.292 +00:00] [INFO] [raft.rs:1116] ["became candidate at term 6"] [term=6] [raft_id=63] [region_id=62]
   > [2024/08/06 12:13:57.292 +00:00] [INFO] [raft.rs:1200] ["became leader at term 6"] [term=6] [raft_id=63] [region_id=62]
   > [2024/08/06 12:13:57.292 +00:00] [INFO] [peer.rs:3778] ["require updating max ts"] [initial_status=25769803838] [region_id=62]
   > [2024/08/06 12:13:57.292 +00:00] [INFO] [endpoint.rs:382] ["deregister observe region"] [observe_id=ObserveID(57)] [region_id=2] [store_id=Some(1)]
   > [2024/08/06 12:13:57.292 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF3D00000000000000F8 region_epoch { conf_ver: 1 version: 31 } peers { id: 3 store_id: 1 }"]
   > [2024/08/06 12:13:57.292 +00:00] [INFO] [pd.rs:1246] ["succeed to update max timestamp"] [region_id=62]
   > [2024/08/06 12:13:57.300 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56000] [split_keys="key 7480000000000000FF3E00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.301 +00:00] [INFO] [peer.rs:3911] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 30"] [prev_epoch="conf_ver: 1 version: 31"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.301 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=66] [observe_id=ObserveID(59)] [region=2]
   > [2024/08/06 12:13:57.310 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56014] [split_keys="key 7480000000000000FF3E00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.311 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 62 start_key: 7480000000000000FF3C00000000000000F8 end_key: 7480000000000000FF3D00000000000000F8 region_epoch { conf_ver: 1 version: 31 } peers { id: 63 store_id: 1 }"]
   > [2024/08/06 12:13:57.311 +00:00] [INFO] [cluster_worker.go:127] ["alloc ids for region split"] [region-id=64] [peer-ids="[65]"]
   > [2024/08/06 12:13:57.311 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveID(60)] [region=62]
   > [2024/08/06 12:13:57.311 +00:00] [INFO] [pd.rs:749] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF3D00000000000000F8 region_epoch { conf_ver: 1 version: 31 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 64 new_peer_ids: 65]"] [region_id=2]
   > [2024/08/06 12:13:57.330 +00:00] [INFO] [apply.rs:1394] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF3E00000000000000F8 new_region_id: 64 new_peer_ids: 65 } right_derive: true }"] [index=67] [term=6] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.330 +00:00] [INFO] [apply.rs:2242] ["split region"] [keys="key 7480000000000000FF3E00000000000000F8"] [region="id: 2 start_key: 7480000000000000FF3D00000000000000F8 region_epoch { conf_ver: 1 version: 31 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.340 +00:00] [INFO] [endpoint.rs:158] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/08/06 12:13:57.340 +00:00] [INFO] [peer.rs:2411] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.340 +00:00] [INFO] [peer.rs:2476] ["insert new region"] [region="id: 64 start_key: 7480000000000000FF3D00000000000000F8 end_key: 7480000000000000FF3E00000000000000F8 region_epoch { conf_ver: 1 version: 32 } peers { id: 65 store_id: 1 }"] [region_id=64]
   > [2024/08/06 12:13:57.340 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=2] ["first at"=74800000000000003e] ["first new region left"="{Id:64 StartKey:7480000000000000ff3d00000000000000f8 EndKey:7480000000000000ff3e00000000000000f8 RegionEpoch:{ConfVer:1 Version:32} Peers:[id:65 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/08/06 12:13:57.340 +00:00] [INFO] [peer.rs:219] ["create peer"] [peer_id=65] [region_id=64]
   > [2024/08/06 12:13:57.340 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[64]"]
   > [2024/08/06 12:13:57.340 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=74800000000000003f]
   > [2024/08/06 12:13:57.341 +00:00] [INFO] [region.go:505] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF3D00000000000000F8} -> {7480000000000000FF3E00000000000000F8}, EndKey:{}"] [old-version=31] [new-version=32]
   > [2024/08/06 12:13:57.341 +00:00] [INFO] [cluster_worker.go:219] ["region batch split, generate new regions"] [region-id=2] [origin="id:64 start_key:\"7480000000000000FF3D00000000000000F8\" end_key:\"7480000000000000FF3E00000000000000F8\" region_epoch:<conf_ver:1 version:32 > peers:<id:65 store_id:1 >"] [total=1]
   > [2024/08/06 12:13:57.349 +00:00] [INFO] [raft.rs:2609] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {65} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=65] [region_id=64]
   > [2024/08/06 12:13:57.349 +00:00] [INFO] [raft.rs:1092] ["became follower at term 5"] [term=5] [raft_id=65] [region_id=64]
   > [2024/08/06 12:13:57.349 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {65} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=65] [region_id=64]
   > [2024/08/06 12:13:57.349 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 65."] [id=65] [raft_id=65] [region_id=64]
   > [2024/08/06 12:13:57.349 +00:00] [INFO] [raft.rs:1517] ["starting a new election"] [term=5] [raft_id=65] [region_id=64]
   > [2024/08/06 12:13:57.350 +00:00] [INFO] [raft.rs:1142] ["became pre-candidate at term 5"] [term=5] [raft_id=65] [region_id=64]
   > [2024/08/06 12:13:57.350 +00:00] [INFO] [raft.rs:1116] ["became candidate at term 6"] [term=6] [raft_id=65] [region_id=64]
   > [2024/08/06 12:13:57.350 +00:00] [INFO] [raft.rs:1200] ["became leader at term 6"] [term=6] [raft_id=65] [region_id=64]
   > [2024/08/06 12:13:57.350 +00:00] [INFO] [endpoint.rs:382] ["deregister observe region"] [observe_id=ObserveID(59)] [region_id=2] [store_id=Some(1)]
   > [2024/08/06 12:13:57.350 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF3E00000000000000F8 region_epoch { conf_ver: 1 version: 32 } peers { id: 3 store_id: 1 }"]
   > [2024/08/06 12:13:57.350 +00:00] [INFO] [peer.rs:3778] ["require updating max ts"] [initial_status=25769803840] [region_id=64]
   > [2024/08/06 12:13:57.350 +00:00] [INFO] [pd.rs:1246] ["succeed to update max timestamp"] [region_id=64]
   > [2024/08/06 12:13:57.368 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56024] [split_keys="key 7480000000000000FF3F00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.368 +00:00] [INFO] [peer.rs:3911] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 31"] [prev_epoch="conf_ver: 1 version: 32"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.368 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 64 start_key: 7480000000000000FF3D00000000000000F8 end_key: 7480000000000000FF3E00000000000000F8 region_epoch { conf_ver: 1 version: 32 } peers { id: 65 store_id: 1 }"]
   > [2024/08/06 12:13:57.368 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=67] [observe_id=ObserveID(61)] [region=2]
   > [2024/08/06 12:13:57.369 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveID(62)] [region=64]
   > [2024/08/06 12:13:57.371 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56032] [split_keys="key 7480000000000000FF3F00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.372 +00:00] [INFO] [cluster_worker.go:127] ["alloc ids for region split"] [region-id=66] [peer-ids="[67]"]
   > [2024/08/06 12:13:57.373 +00:00] [INFO] [pd.rs:749] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF3E00000000000000F8 region_epoch { conf_ver: 1 version: 32 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 66 new_peer_ids: 67]"] [region_id=2]
   > [2024/08/06 12:13:57.379 +00:00] [INFO] [apply.rs:1394] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF3F00000000000000F8 new_region_id: 66 new_peer_ids: 67 } right_derive: true }"] [index=68] [term=6] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.379 +00:00] [INFO] [apply.rs:2242] ["split region"] [keys="key 7480000000000000FF3F00000000000000F8"] [region="id: 2 start_key: 7480000000000000FF3E00000000000000F8 region_epoch { conf_ver: 1 version: 32 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.388 +00:00] [INFO] [endpoint.rs:158] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/08/06 12:13:57.388 +00:00] [INFO] [peer.rs:2411] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.388 +00:00] [INFO] [peer.rs:2476] ["insert new region"] [region="id: 66 start_key: 7480000000000000FF3E00000000000000F8 end_key: 7480000000000000FF3F00000000000000F8 region_epoch { conf_ver: 1 version: 33 } peers { id: 67 store_id: 1 }"] [region_id=66]
   > [2024/08/06 12:13:57.388 +00:00] [INFO] [peer.rs:219] ["create peer"] [peer_id=67] [region_id=66]
   > [2024/08/06 12:13:57.388 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=2] ["first at"=74800000000000003f] ["first new region left"="{Id:66 StartKey:7480000000000000ff3e00000000000000f8 EndKey:7480000000000000ff3f00000000000000f8 RegionEpoch:{ConfVer:1 Version:33} Peers:[id:67 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/08/06 12:13:57.389 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[66]"]
   > [2024/08/06 12:13:57.389 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=748000000000000040]
   > [2024/08/06 12:13:57.389 +00:00] [INFO] [region.go:505] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF3E00000000000000F8} -> {7480000000000000FF3F00000000000000F8}, EndKey:{}"] [old-version=32] [new-version=33]
   > [2024/08/06 12:13:57.389 +00:00] [INFO] [cluster_worker.go:219] ["region batch split, generate new regions"] [region-id=2] [origin="id:66 start_key:\"7480000000000000FF3E00000000000000F8\" end_key:\"7480000000000000FF3F00000000000000F8\" region_epoch:<conf_ver:1 version:33 > peers:<id:67 store_id:1 >"] [total=1]
   > [2024/08/06 12:13:57.393 +00:00] [INFO] [raft.rs:2609] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {67} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=67] [region_id=66]
   > [2024/08/06 12:13:57.393 +00:00] [INFO] [raft.rs:1092] ["became follower at term 5"] [term=5] [raft_id=67] [region_id=66]
   > [2024/08/06 12:13:57.393 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {67} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=67] [region_id=66]
   > [2024/08/06 12:13:57.393 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 67."] [id=67] [raft_id=67] [region_id=66]
   > [2024/08/06 12:13:57.393 +00:00] [INFO] [raft.rs:1517] ["starting a new election"] [term=5] [raft_id=67] [region_id=66]
   > [2024/08/06 12:13:57.393 +00:00] [INFO] [raft.rs:1142] ["became pre-candidate at term 5"] [term=5] [raft_id=67] [region_id=66]
   > [2024/08/06 12:13:57.394 +00:00] [INFO] [raft.rs:1116] ["became candidate at term 6"] [term=6] [raft_id=67] [region_id=66]
   > [2024/08/06 12:13:57.394 +00:00] [INFO] [raft.rs:1200] ["became leader at term 6"] [term=6] [raft_id=67] [region_id=66]
   > [2024/08/06 12:13:57.394 +00:00] [INFO] [endpoint.rs:382] ["deregister observe region"] [observe_id=ObserveID(61)] [region_id=2] [store_id=Some(1)]
   > [2024/08/06 12:13:57.394 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF3F00000000000000F8 region_epoch { conf_ver: 1 version: 33 } peers { id: 3 store_id: 1 }"]
   > [2024/08/06 12:13:57.394 +00:00] [INFO] [peer.rs:3778] ["require updating max ts"] [initial_status=25769803842] [region_id=66]
   > [2024/08/06 12:13:57.394 +00:00] [INFO] [pd.rs:1246] ["succeed to update max timestamp"] [region_id=66]
   > [2024/08/06 12:13:57.402 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56000] [split_keys="key 7480000000000000FF4000000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.403 +00:00] [INFO] [peer.rs:3911] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 32"] [prev_epoch="conf_ver: 1 version: 33"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.403 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=68] [observe_id=ObserveID(63)] [region=2]
   > [2024/08/06 12:13:57.403 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 66 start_key: 7480000000000000FF3E00000000000000F8 end_key: 7480000000000000FF3F00000000000000F8 region_epoch { conf_ver: 1 version: 33 } peers { id: 67 store_id: 1 }"]
   > [2024/08/06 12:13:57.403 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveID(64)] [region=66]
   > [2024/08/06 12:13:57.406 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56014] [split_keys="key 7480000000000000FF4000000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.406 +00:00] [INFO] [cluster_worker.go:127] ["alloc ids for region split"] [region-id=68] [peer-ids="[69]"]
   > [2024/08/06 12:13:57.407 +00:00] [INFO] [pd.rs:749] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF3F00000000000000F8 region_epoch { conf_ver: 1 version: 33 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 68 new_peer_ids: 69]"] [region_id=2]
   > [2024/08/06 12:13:57.421 +00:00] [INFO] [apply.rs:1394] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF4000000000000000F8 new_region_id: 68 new_peer_ids: 69 } right_derive: true }"] [index=69] [term=6] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.422 +00:00] [INFO] [apply.rs:2242] ["split region"] [keys="key 7480000000000000FF4000000000000000F8"] [region="id: 2 start_key: 7480000000000000FF3F00000000000000F8 region_epoch { conf_ver: 1 version: 33 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.431 +00:00] [INFO] [endpoint.rs:158] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/08/06 12:13:57.431 +00:00] [INFO] [peer.rs:2411] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.431 +00:00] [INFO] [peer.rs:2476] ["insert new region"] [region="id: 68 start_key: 7480000000000000FF3F00000000000000F8 end_key: 7480000000000000FF4000000000000000F8 region_epoch { conf_ver: 1 version: 34 } peers { id: 69 store_id: 1 }"] [region_id=68]
   > [2024/08/06 12:13:57.431 +00:00] [INFO] [peer.rs:219] ["create peer"] [peer_id=69] [region_id=68]
   > [2024/08/06 12:13:57.431 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=2] ["first at"=748000000000000040] ["first new region left"="{Id:68 StartKey:7480000000000000ff3f00000000000000f8 EndKey:7480000000000000ff4000000000000000f8 RegionEpoch:{ConfVer:1 Version:34} Peers:[id:69 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/08/06 12:13:57.431 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[68]"]
   > [2024/08/06 12:13:57.431 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=748000000000000041]
   > [2024/08/06 12:13:57.431 +00:00] [INFO] [region.go:505] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF3F00000000000000F8} -> {7480000000000000FF4000000000000000F8}, EndKey:{}"] [old-version=33] [new-version=34]
   > [2024/08/06 12:13:57.431 +00:00] [INFO] [cluster_worker.go:219] ["region batch split, generate new regions"] [region-id=2] [origin="id:68 start_key:\"7480000000000000FF3F00000000000000F8\" end_key:\"7480000000000000FF4000000000000000F8\" region_epoch:<conf_ver:1 version:34 > peers:<id:69 store_id:1 >"] [total=1]
   > [2024/08/06 12:13:57.440 +00:00] [INFO] [raft.rs:2609] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {69} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=69] [region_id=68]
   > [2024/08/06 12:13:57.440 +00:00] [INFO] [raft.rs:1092] ["became follower at term 5"] [term=5] [raft_id=69] [region_id=68]
   > [2024/08/06 12:13:57.441 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {69} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=69] [region_id=68]
   > [2024/08/06 12:13:57.441 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 69."] [id=69] [raft_id=69] [region_id=68]
   > [2024/08/06 12:13:57.441 +00:00] [INFO] [raft.rs:1517] ["starting a new election"] [term=5] [raft_id=69] [region_id=68]
   > [2024/08/06 12:13:57.441 +00:00] [INFO] [raft.rs:1142] ["became pre-candidate at term 5"] [term=5] [raft_id=69] [region_id=68]
   > [2024/08/06 12:13:57.441 +00:00] [INFO] [raft.rs:1116] ["became candidate at term 6"] [term=6] [raft_id=69] [region_id=68]
   > [2024/08/06 12:13:57.441 +00:00] [INFO] [raft.rs:1200] ["became leader at term 6"] [term=6] [raft_id=69] [region_id=68]
   > [2024/08/06 12:13:57.441 +00:00] [INFO] [peer.rs:3778] ["require updating max ts"] [initial_status=25769803844] [region_id=68]
   > [2024/08/06 12:13:57.441 +00:00] [INFO] [endpoint.rs:382] ["deregister observe region"] [observe_id=ObserveID(63)] [region_id=2] [store_id=Some(1)]
   > [2024/08/06 12:13:57.441 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF4000000000000000F8 region_epoch { conf_ver: 1 version: 34 } peers { id: 3 store_id: 1 }"]
   > [2024/08/06 12:13:57.441 +00:00] [INFO] [pd.rs:1246] ["succeed to update max timestamp"] [region_id=68]
   > [2024/08/06 12:13:57.460 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56024] [split_keys="key 7480000000000000FF4100000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.460 +00:00] [INFO] [peer.rs:3911] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 33"] [prev_epoch="conf_ver: 1 version: 34"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.460 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 68 start_key: 7480000000000000FF3F00000000000000F8 end_key: 7480000000000000FF4000000000000000F8 region_epoch { conf_ver: 1 version: 34 } peers { id: 69 store_id: 1 }"]
   > [2024/08/06 12:13:57.460 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=69] [observe_id=ObserveID(65)] [region=2]
   > [2024/08/06 12:13:57.460 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveID(66)] [region=68]
   > [2024/08/06 12:13:57.463 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56032] [split_keys="key 7480000000000000FF4100000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.464 +00:00] [INFO] [cluster_worker.go:127] ["alloc ids for region split"] [region-id=70] [peer-ids="[71]"]
   > [2024/08/06 12:13:57.464 +00:00] [INFO] [pd.rs:749] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF4000000000000000F8 region_epoch { conf_ver: 1 version: 34 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 70 new_peer_ids: 71]"] [region_id=2]
   > [2024/08/06 12:13:57.479 +00:00] [INFO] [apply.rs:1394] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF4100000000000000F8 new_region_id: 70 new_peer_ids: 71 } right_derive: true }"] [index=70] [term=6] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.479 +00:00] [INFO] [apply.rs:2242] ["split region"] [keys="key 7480000000000000FF4100000000000000F8"] [region="id: 2 start_key: 7480000000000000FF4000000000000000F8 region_epoch { conf_ver: 1 version: 34 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.489 +00:00] [INFO] [endpoint.rs:158] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/08/06 12:13:57.489 +00:00] [INFO] [peer.rs:2411] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/08/06 12:13:57.489 +00:00] [INFO] [peer.rs:2476] ["insert new region"] [region="id: 70 start_key: 7480000000000000FF4000000000000000F8 end_key: 7480000000000000FF4100000000000000F8 region_epoch { conf_ver: 1 version: 35 } peers { id: 71 store_id: 1 }"] [region_id=70]
   > [2024/08/06 12:13:57.489 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=2] ["first at"=748000000000000041] ["first new region left"="{Id:70 StartKey:7480000000000000ff4000000000000000f8 EndKey:7480000000000000ff4100000000000000f8 RegionEpoch:{ConfVer:1 Version:35} Peers:[id:71 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/08/06 12:13:57.489 +00:00] [INFO] [peer.rs:219] ["create peer"] [peer_id=71] [region_id=70]
   > [2024/08/06 12:13:57.489 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[70]"]
   > [2024/08/06 12:13:57.489 +00:00] [INFO] [region.go:505] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF4000000000000000F8} -> {7480000000000000FF4100000000000000F8}, EndKey:{}"] [old-version=34] [new-version=35]
   > [2024/08/06 12:13:57.489 +00:00] [INFO] [cluster_worker.go:219] ["region batch split, generate new regions"] [region-id=2] [origin="id:70 start_key:\"7480000000000000FF4000000000000000F8\" end_key:\"7480000000000000FF4100000000000000F8\" region_epoch:<conf_ver:1 version:35 > peers:<id:71 store_id:1 >"] [total=1]
   > [2024/08/06 12:13:57.498 +00:00] [INFO] [raft.rs:2609] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {71} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=71] [region_id=70]
   > [2024/08/06 12:13:57.498 +00:00] [INFO] [raft.rs:1092] ["became follower at term 5"] [term=5] [raft_id=71] [region_id=70]
   > [2024/08/06 12:13:57.498 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {71} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=71] [region_id=70]
   > [2024/08/06 12:13:57.499 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 71."] [id=71] [raft_id=71] [region_id=70]
   > [2024/08/06 12:13:57.499 +00:00] [INFO] [raft.rs:1517] ["starting a new election"] [term=5] [raft_id=71] [region_id=70]
   > [2024/08/06 12:13:57.499 +00:00] [INFO] [raft.rs:1142] ["became pre-candidate at term 5"] [term=5] [raft_id=71] [region_id=70]
   > [2024/08/06 12:13:57.499 +00:00] [INFO] [raft.rs:1116] ["became candidate at term 6"] [term=6] [raft_id=71] [region_id=70]
   > [2024/08/06 12:13:57.499 +00:00] [INFO] [raft.rs:1200] ["became leader at term 6"] [term=6] [raft_id=71] [region_id=70]
   > [2024/08/06 12:13:57.499 +00:00] [INFO] [peer.rs:3778] ["require updating max ts"] [initial_status=25769803846] [region_id=70]
   > [2024/08/06 12:13:57.499 +00:00] [INFO] [endpoint.rs:382] ["deregister observe region"] [observe_id=ObserveID(65)] [region_id=2] [store_id=Some(1)]
   > [2024/08/06 12:13:57.499 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF4100000000000000F8 region_epoch { conf_ver: 1 version: 35 } peers { id: 3 store_id: 1 }"]
   > [2024/08/06 12:13:57.499 +00:00] [INFO] [pd.rs:1246] ["succeed to update max timestamp"] [region_id=70]
   > [2024/08/06 12:13:57.523 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=70] [observe_id=ObserveID(67)] [region=2]
   > [2024/08/06 12:13:57.536 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 70 start_key: 7480000000000000FF4000000000000000F8 end_key: 7480000000000000FF4100000000000000F8 region_epoch { conf_ver: 1 version: 35 } peers { id: 71 store_id: 1 }"]
   > [2024/08/06 12:13:57.536 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveID(68)] [region=70]
   > [2024/08/06 12:13:57.540 +00:00] [WARN] [grpclogger.go:81] ["grpc: Server.Serve failed to create ServerTransport: connection error: desc = \"transport: http2Server.HandleStreams failed to receive the preface from client: EOF\""] [system=grpc] [grpc_log=true]
   > [2024/08/06 12:13:57.829 +00:00] [INFO] [client.rs:700] ["set cluster version to 5.2.0"]
   > [2024/08/06 12:13:58.039 +00:00] [INFO] [set.go:127] ["set global var"] [conn=9] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/08/06 12:13:58.271 +00:00] [WARN] [endpoint.rs:632] [error-response] [err="Key is locked (will clean up) primary_lock: 7480000000000000155F698000000000000002038000000000000037 lock_version: 451660071074004993 key: 7480000000000000155F6980000000000000010406449E710F98000103800000000000000B lock_ttl: 3087 txn_size: 3 lock_for_update_ts: 451660071074004993 use_async_commit: true min_commit_ts: 451660071100219394"]
   > [2024/08/06 12:14:00.740 +00:00] [WARN] [endpoint.rs:632] [error-response] [err="Region error (will back off and retry) message: \"EpochNotMatch current epoch of region 2 is conf_ver: 1 version: 35, but you sent conf_ver: 1 version: 34\" epoch_not_match { current_regions { id: 2 start_key: 7480000000000000FF4100000000000000F8 region_epoch { conf_ver: 1 version: 35 } peers { id: 3 store_id: 1 } } current_regions { id: 70 start_key: 7480000000000000FF4000000000000000F8 end_key: 7480000000000000FF4100000000000000F8 region_epoch { conf_ver: 1 version: 35 } peers { id: 71 store_id: 1 } } }"]
   > [2024/08/06 12:14:00.740 +00:00] [WARN] [endpoint.rs:632] [error-response] [err="Region error (will back off and retry) message: \"EpochNotMatch current epoch of region 2 is conf_ver: 1 version: 35, but you sent conf_ver: 1 version: 34\" epoch_not_match { current_regions { id: 2 start_key: 7480000000000000FF4100000000000000F8 region_epoch { conf_ver: 1 version: 35 } peers { id: 3 store_id: 1 } } current_regions { id: 70 start_key: 7480000000000000FF4000000000000000F8 end_key: 7480000000000000FF4100000000000000F8 region_epoch { conf_ver: 1 version: 35 } peers { id: 71 store_id: 1 } } }"]
