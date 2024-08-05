# Bug ID TIDB-26973-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/26973
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              The name of tables and handles are not parsed in DEBUG table.


## Details
 * Database: tidb-v5.2.0-alpha-1a54708a7.tikv
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
     - Instruction:  begin;
     - Transaction: conn_1
     - Output: None
     - Executed order: 2
     - Affected rows: 0
 * Instruction #3:
     - Instruction:  update t set a=10 where a=1;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows: 1
 * Instruction #4:
     - Instruction:  update t set b=11 where a=2;
     - Transaction: conn_1
     - Output: None
     - Executed order: 4
     - Affected rows: 1
 * Instruction #5:
     - Instruction:  update t set b=12 where a=2;
     - Transaction: conn_0
     - Output: None
     - Executed order: 5
     - Affected rows: 1
 * Instruction #6:
     - Instruction:  update t set b=13 where a=1;
     - Transaction: conn_1
     - Output: ERROR: 1213 (40001): Deadlock found when trying to get lock; try restarting transaction
     - Executed order: Not executed
     - Affected rows: -1
 * Instruction #7:
     - Instruction:  SELECT * FROM INFORMATION_SCHEMA.DEADLOCKS;
     - Transaction: conn_0
     - Output: [(1, datetime.datetime(2024, 8, 5, 8, 6, 50, 452353), 0, 451633534448697345, '4e310bd4576c5e689f6fdf93dcd99ed34eaac181d66067073ebb0dcff3a7bea7', 'update `t` set `b` = ? where `a` = ? ;', '7480000000000000395F728000000000000002', '{"table_id":57,"handle_type":"int","handle_value":"2"}', 451633534527078406), (1, datetime.datetime(2024, 8, 5, 8, 6, 50, 452353), 0, 451633534527078406, '4e310bd4576c5e689f6fdf93dcd99ed34eaac181d66067073ebb0dcff3a7bea7', 'update `t` set `b` = ? where `a` = ? ;', '7480000000000000385F728000000000000001', '{"table_id":56,"handle_type":"int","handle_value":"1"}', 451633534448697345)]
     - Executed order: 6
     - Affected rows: 2

 * Container logs:
   > [2024/08/05 08:06:47.274 +00:00] [INFO] [session.go:2920] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=26] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/08/05 08:06:47.276 +00:00] [INFO] [session.go:2920] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=26] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/08/05 08:06:47.320 +00:00] [INFO] [ddl_worker.go:316] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:54, Type:create schema, State:none, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-05 08:06:47.275 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/05 08:06:47.320 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:54, Type:create schema, State:none, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-05 08:06:47.275 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/08/05 08:06:47.324 +00:00] [INFO] [ddl_worker.go:715] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:54, Type:create schema, State:none, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-05 08:06:47.275 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/05 08:06:47.346 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=26] [neededSchemaVersion=27] ["start time"=1.528354ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/05 08:06:47.395 +00:00] [INFO] [ddl_worker.go:900] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=27] ["take time"=52.570561ms] [job="ID:54, Type:create schema, State:done, SchemaState:public, SchemaID:53, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-05 08:06:47.275 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/05 08:06:47.399 +00:00] [INFO] [ddl_worker.go:421] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:54, Type:create schema, State:synced, SchemaState:public, SchemaID:53, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-05 08:06:47.275 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/05 08:06:47.417 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=54]
   > [2024/08/05 08:06:47.417 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/08/05 08:06:47.421 +00:00] [INFO] [session.go:2920] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=27] [cur_db=testdb] [sql="create table t (a int primary key, b int) partition by range(a) (PARTITION p0 VALUES LESS THAN (2), PARTITION p1 VALUES LESS THAN (4),\n    PARTITION p2 VALUES LESS THAN (MAXVALUE));"] [user=root@127.0.0.1]
   > [2024/08/05 08:06:47.473 +00:00] [INFO] [ddl_worker.go:316] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:59, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:55, RowCount:0, ArgLen:1, start time: 2024-08-05 08:06:47.426 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/05 08:06:47.473 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:59, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:55, RowCount:0, ArgLen:1, start time: 2024-08-05 08:06:47.426 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t (a int primary key, b int) partition by range(a) (PARTITION p0 VALUES LESS THAN (2), PARTITION p1 VALUES LESS THAN (4),\n    PARTITION p2 VALUES LESS THAN (MAXVALUE));"]
   > [2024/08/05 08:06:47.477 +00:00] [INFO] [ddl_worker.go:715] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:59, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:55, RowCount:0, ArgLen:0, start time: 2024-08-05 08:06:47.426 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/05 08:06:47.507 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=27] [neededSchemaVersion=28] ["start time"=3.460536ms] [phyTblIDs="[55,56,57,58]"] [actionTypes="[8,8,8,8]"]
   > [2024/08/05 08:06:47.554 +00:00] [INFO] [ddl_worker.go:900] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=28] ["take time"=52.592003ms] [job="ID:59, Type:create table, State:done, SchemaState:public, SchemaID:53, TableID:55, RowCount:0, ArgLen:1, start time: 2024-08-05 08:06:47.426 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/05 08:06:47.558 +00:00] [INFO] [ddl_worker.go:421] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:59, Type:create table, State:synced, SchemaState:public, SchemaID:53, TableID:55, RowCount:0, ArgLen:0, start time: 2024-08-05 08:06:47.426 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/05 08:06:47.580 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=59]
   > [2024/08/05 08:06:47.580 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/08/05 08:06:47.580 +00:00] [INFO] [split_region.go:84] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=748000000000000038]
   > [2024/08/05 08:06:47.584 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56576] [split_keys="key 7480000000000000FF3800000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/05 08:06:47.584 +00:00] [INFO] [cluster_worker.go:127] ["alloc ids for region split"] [region-id=52] [peer-ids="[53]"]
   > [2024/08/05 08:06:47.585 +00:00] [INFO] [pd.rs:749] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF3300000000000000F8 region_epoch { conf_ver: 1 version: 25 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 52 new_peer_ids: 53]"] [region_id=2]
   > [2024/08/05 08:06:47.617 +00:00] [INFO] [apply.rs:1394] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF3800000000000000F8 new_region_id: 52 new_peer_ids: 53 } right_derive: true }"] [index=60] [term=6] [peer_id=3] [region_id=2]
   > [2024/08/05 08:06:47.617 +00:00] [INFO] [apply.rs:2242] ["split region"] [keys="key 7480000000000000FF3800000000000000F8"] [region="id: 2 start_key: 7480000000000000FF3300000000000000F8 region_epoch { conf_ver: 1 version: 25 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/08/05 08:06:47.629 +00:00] [INFO] [endpoint.rs:158] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/08/05 08:06:47.629 +00:00] [INFO] [peer.rs:2411] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/08/05 08:06:47.629 +00:00] [INFO] [peer.rs:2476] ["insert new region"] [region="id: 52 start_key: 7480000000000000FF3300000000000000F8 end_key: 7480000000000000FF3800000000000000F8 region_epoch { conf_ver: 1 version: 26 } peers { id: 53 store_id: 1 }"] [region_id=52]
   > [2024/08/05 08:06:47.629 +00:00] [INFO] [peer.rs:219] ["create peer"] [peer_id=53] [region_id=52]
   > [2024/08/05 08:06:47.629 +00:00] [INFO] [raft.rs:2609] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {53} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=53] [region_id=52]
   > [2024/08/05 08:06:47.629 +00:00] [INFO] [region.go:505] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF3300000000000000F8} -> {7480000000000000FF3800000000000000F8}, EndKey:{}"] [old-version=25] [new-version=26]
   > [2024/08/05 08:06:47.629 +00:00] [INFO] [split_region.go:185] ["batch split regions complete"] ["batch region ID"=2] ["first at"=748000000000000038] ["first new region left"="{Id:52 StartKey:7480000000000000ff3300000000000000f8 EndKey:7480000000000000ff3800000000000000f8 RegionEpoch:{ConfVer:1 Version:26} Peers:[id:53 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/08/05 08:06:47.629 +00:00] [INFO] [split_region.go:234] ["split regions complete"] ["region count"=1] ["region IDs"="[52]"]
   > [2024/08/05 08:06:47.629 +00:00] [INFO] [split_region.go:84] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=748000000000000039]
   > [2024/08/05 08:06:47.629 +00:00] [INFO] [raft.rs:1092] ["became follower at term 5"] [term=5] [raft_id=53] [region_id=52]
   > [2024/08/05 08:06:47.629 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {53} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=53] [region_id=52]
   > [2024/08/05 08:06:47.630 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 53."] [id=53] [raft_id=53] [region_id=52]
   > [2024/08/05 08:06:47.630 +00:00] [INFO] [raft.rs:1517] ["starting a new election"] [term=5] [raft_id=53] [region_id=52]
   > [2024/08/05 08:06:47.630 +00:00] [INFO] [raft.rs:1142] ["became pre-candidate at term 5"] [term=5] [raft_id=53] [region_id=52]
   > [2024/08/05 08:06:47.630 +00:00] [INFO] [raft.rs:1116] ["became candidate at term 6"] [term=6] [raft_id=53] [region_id=52]
   > [2024/08/05 08:06:47.630 +00:00] [INFO] [raft.rs:1200] ["became leader at term 6"] [term=6] [raft_id=53] [region_id=52]
   > [2024/08/05 08:06:47.630 +00:00] [INFO] [endpoint.rs:382] ["deregister observe region"] [observe_id=ObserveID(47)] [region_id=2] [store_id=Some(1)]
   > [2024/08/05 08:06:47.630 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF3800000000000000F8 region_epoch { conf_ver: 1 version: 26 } peers { id: 3 store_id: 1 }"]
   > [2024/08/05 08:06:47.630 +00:00] [INFO] [cluster_worker.go:219] ["region batch split, generate new regions"] [region-id=2] [origin="id:52 start_key:\"7480000000000000FF3300000000000000F8\" end_key:\"7480000000000000FF3800000000000000F8\" region_epoch:<conf_ver:1 version:26 > peers:<id:53 store_id:1 >"] [total=1]
   > [2024/08/05 08:06:47.630 +00:00] [INFO] [peer.rs:3778] ["require updating max ts"] [initial_status=25769803828] [region_id=52]
   > [2024/08/05 08:06:47.630 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=60] [observe_id=ObserveID(49)] [region=2]
   > [2024/08/05 08:06:47.630 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56550] [split_keys="key 7480000000000000FF3900000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/05 08:06:47.630 +00:00] [INFO] [peer.rs:3911] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 25"] [prev_epoch="conf_ver: 1 version: 26"] [peer_id=3] [region_id=2]
   > [2024/08/05 08:06:47.630 +00:00] [INFO] [pd.rs:1246] ["succeed to update max timestamp"] [region_id=52]
   > [2024/08/05 08:06:47.636 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56566] [split_keys="key 7480000000000000FF3900000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/05 08:06:47.636 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 52 start_key: 7480000000000000FF3300000000000000F8 end_key: 7480000000000000FF3800000000000000F8 region_epoch { conf_ver: 1 version: 26 } peers { id: 53 store_id: 1 }"]
   > [2024/08/05 08:06:47.636 +00:00] [INFO] [cluster_worker.go:127] ["alloc ids for region split"] [region-id=54] [peer-ids="[55]"]
   > [2024/08/05 08:06:47.636 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveID(50)] [region=52]
   > [2024/08/05 08:06:47.637 +00:00] [INFO] [pd.rs:749] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF3800000000000000F8 region_epoch { conf_ver: 1 version: 26 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 54 new_peer_ids: 55]"] [region_id=2]
   > [2024/08/05 08:06:47.652 +00:00] [INFO] [apply.rs:1394] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF3900000000000000F8 new_region_id: 54 new_peer_ids: 55 } right_derive: true }"] [index=61] [term=6] [peer_id=3] [region_id=2]
   > [2024/08/05 08:06:47.652 +00:00] [INFO] [apply.rs:2242] ["split region"] [keys="key 7480000000000000FF3900000000000000F8"] [region="id: 2 start_key: 7480000000000000FF3800000000000000F8 region_epoch { conf_ver: 1 version: 26 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/08/05 08:06:47.663 +00:00] [INFO] [endpoint.rs:158] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/08/05 08:06:47.663 +00:00] [INFO] [peer.rs:2411] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/08/05 08:06:47.663 +00:00] [INFO] [peer.rs:2476] ["insert new region"] [region="id: 54 start_key: 7480000000000000FF3800000000000000F8 end_key: 7480000000000000FF3900000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 55 store_id: 1 }"] [region_id=54]
   > [2024/08/05 08:06:47.663 +00:00] [INFO] [peer.rs:219] ["create peer"] [peer_id=55] [region_id=54]
   > [2024/08/05 08:06:47.663 +00:00] [INFO] [split_region.go:185] ["batch split regions complete"] ["batch region ID"=2] ["first at"=748000000000000039] ["first new region left"="{Id:54 StartKey:7480000000000000ff3800000000000000f8 EndKey:7480000000000000ff3900000000000000f8 RegionEpoch:{ConfVer:1 Version:27} Peers:[id:55 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/08/05 08:06:47.663 +00:00] [INFO] [split_region.go:234] ["split regions complete"] ["region count"=1] ["region IDs"="[54]"]
   > [2024/08/05 08:06:47.663 +00:00] [INFO] [split_region.go:84] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=74800000000000003a]
   > [2024/08/05 08:06:47.664 +00:00] [INFO] [region.go:505] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF3800000000000000F8} -> {7480000000000000FF3900000000000000F8}, EndKey:{}"] [old-version=26] [new-version=27]
   > [2024/08/05 08:06:47.664 +00:00] [INFO] [cluster_worker.go:219] ["region batch split, generate new regions"] [region-id=2] [origin="id:54 start_key:\"7480000000000000FF3800000000000000F8\" end_key:\"7480000000000000FF3900000000000000F8\" region_epoch:<conf_ver:1 version:27 > peers:<id:55 store_id:1 >"] [total=1]
   > [2024/08/05 08:06:47.668 +00:00] [INFO] [raft.rs:2609] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {55} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=55] [region_id=54]
   > [2024/08/05 08:06:47.668 +00:00] [INFO] [raft.rs:1092] ["became follower at term 5"] [term=5] [raft_id=55] [region_id=54]
   > [2024/08/05 08:06:47.669 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {55} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=55] [region_id=54]
   > [2024/08/05 08:06:47.669 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 55."] [id=55] [raft_id=55] [region_id=54]
   > [2024/08/05 08:06:47.669 +00:00] [INFO] [raft.rs:1517] ["starting a new election"] [term=5] [raft_id=55] [region_id=54]
   > [2024/08/05 08:06:47.669 +00:00] [INFO] [raft.rs:1142] ["became pre-candidate at term 5"] [term=5] [raft_id=55] [region_id=54]
   > [2024/08/05 08:06:47.669 +00:00] [INFO] [raft.rs:1116] ["became candidate at term 6"] [term=6] [raft_id=55] [region_id=54]
   > [2024/08/05 08:06:47.669 +00:00] [INFO] [raft.rs:1200] ["became leader at term 6"] [term=6] [raft_id=55] [region_id=54]
   > [2024/08/05 08:06:47.669 +00:00] [INFO] [endpoint.rs:382] ["deregister observe region"] [observe_id=ObserveID(49)] [region_id=2] [store_id=Some(1)]
   > [2024/08/05 08:06:47.669 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF3900000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 3 store_id: 1 }"]
   > [2024/08/05 08:06:47.669 +00:00] [INFO] [peer.rs:3778] ["require updating max ts"] [initial_status=25769803830] [region_id=54]
   > [2024/08/05 08:06:47.669 +00:00] [INFO] [pd.rs:1246] ["succeed to update max timestamp"] [region_id=54]
   > [2024/08/05 08:06:47.681 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56574] [split_keys="key 7480000000000000FF3A00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/05 08:06:47.681 +00:00] [INFO] [peer.rs:3911] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 26"] [prev_epoch="conf_ver: 1 version: 27"] [peer_id=3] [region_id=2]
   > [2024/08/05 08:06:47.681 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=61] [observe_id=ObserveID(51)] [region=2]
   > [2024/08/05 08:06:47.691 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56576] [split_keys="key 7480000000000000FF3A00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/05 08:06:47.691 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 54 start_key: 7480000000000000FF3800000000000000F8 end_key: 7480000000000000FF3900000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 55 store_id: 1 }"]
   > [2024/08/05 08:06:47.692 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveID(52)] [region=54]
   > [2024/08/05 08:06:47.692 +00:00] [INFO] [cluster_worker.go:127] ["alloc ids for region split"] [region-id=56] [peer-ids="[57]"]
   > [2024/08/05 08:06:47.692 +00:00] [INFO] [pd.rs:749] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF3900000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 56 new_peer_ids: 57]"] [region_id=2]
   > [2024/08/05 08:06:47.707 +00:00] [INFO] [apply.rs:1394] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF3A00000000000000F8 new_region_id: 56 new_peer_ids: 57 } right_derive: true }"] [index=62] [term=6] [peer_id=3] [region_id=2]
   > [2024/08/05 08:06:47.707 +00:00] [INFO] [apply.rs:2242] ["split region"] [keys="key 7480000000000000FF3A00000000000000F8"] [region="id: 2 start_key: 7480000000000000FF3900000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/08/05 08:06:47.713 +00:00] [INFO] [endpoint.rs:158] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/08/05 08:06:47.713 +00:00] [INFO] [peer.rs:2411] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/08/05 08:06:47.713 +00:00] [INFO] [peer.rs:2476] ["insert new region"] [region="id: 56 start_key: 7480000000000000FF3900000000000000F8 end_key: 7480000000000000FF3A00000000000000F8 region_epoch { conf_ver: 1 version: 28 } peers { id: 57 store_id: 1 }"] [region_id=56]
   > [2024/08/05 08:06:47.713 +00:00] [INFO] [peer.rs:219] ["create peer"] [peer_id=57] [region_id=56]
   > [2024/08/05 08:06:47.714 +00:00] [INFO] [split_region.go:185] ["batch split regions complete"] ["batch region ID"=2] ["first at"=74800000000000003a] ["first new region left"="{Id:56 StartKey:7480000000000000ff3900000000000000f8 EndKey:7480000000000000ff3a00000000000000f8 RegionEpoch:{ConfVer:1 Version:28} Peers:[id:57 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/08/05 08:06:47.714 +00:00] [INFO] [raft.rs:2609] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {57} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=57] [region_id=56]
   > [2024/08/05 08:06:47.714 +00:00] [INFO] [split_region.go:234] ["split regions complete"] ["region count"=1] ["region IDs"="[56]"]
   > [2024/08/05 08:06:47.714 +00:00] [INFO] [raft.rs:1092] ["became follower at term 5"] [term=5] [raft_id=57] [region_id=56]
   > [2024/08/05 08:06:47.714 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {57} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=57] [region_id=56]
   > [2024/08/05 08:06:47.714 +00:00] [INFO] [region.go:505] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF3900000000000000F8} -> {7480000000000000FF3A00000000000000F8}, EndKey:{}"] [old-version=27] [new-version=28]
   > [2024/08/05 08:06:47.714 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 57."] [id=57] [raft_id=57] [region_id=56]
   > [2024/08/05 08:06:47.714 +00:00] [INFO] [raft.rs:1517] ["starting a new election"] [term=5] [raft_id=57] [region_id=56]
   > [2024/08/05 08:06:47.714 +00:00] [INFO] [cluster_worker.go:219] ["region batch split, generate new regions"] [region-id=2] [origin="id:56 start_key:\"7480000000000000FF3900000000000000F8\" end_key:\"7480000000000000FF3A00000000000000F8\" region_epoch:<conf_ver:1 version:28 > peers:<id:57 store_id:1 >"] [total=1]
   > [2024/08/05 08:06:47.714 +00:00] [INFO] [raft.rs:1142] ["became pre-candidate at term 5"] [term=5] [raft_id=57] [region_id=56]
   > [2024/08/05 08:06:47.714 +00:00] [INFO] [raft.rs:1116] ["became candidate at term 6"] [term=6] [raft_id=57] [region_id=56]
   > [2024/08/05 08:06:47.714 +00:00] [INFO] [raft.rs:1200] ["became leader at term 6"] [term=6] [raft_id=57] [region_id=56]
   > [2024/08/05 08:06:47.714 +00:00] [INFO] [peer.rs:3778] ["require updating max ts"] [initial_status=25769803832] [region_id=56]
   > [2024/08/05 08:06:47.714 +00:00] [INFO] [endpoint.rs:382] ["deregister observe region"] [observe_id=ObserveID(51)] [region_id=2] [store_id=Some(1)]
   > [2024/08/05 08:06:47.714 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF3A00000000000000F8 region_epoch { conf_ver: 1 version: 28 } peers { id: 3 store_id: 1 }"]
   > [2024/08/05 08:06:47.715 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=62] [observe_id=ObserveID(53)] [region=2]
   > [2024/08/05 08:06:47.715 +00:00] [INFO] [pd.rs:1246] ["succeed to update max timestamp"] [region_id=56]
   > [2024/08/05 08:06:47.720 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 56 start_key: 7480000000000000FF3900000000000000F8 end_key: 7480000000000000FF3A00000000000000F8 region_epoch { conf_ver: 1 version: 28 } peers { id: 57 store_id: 1 }"]
   > [2024/08/05 08:06:47.720 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveID(54)] [region=56]
   > [2024/08/05 08:06:47.769 +00:00] [WARN] [grpclogger.go:81] ["grpc: Server.Serve failed to create ServerTransport: connection error: desc = \"transport: http2Server.HandleStreams failed to receive the preface from client: EOF\""] [system=grpc] [grpc_log=true]
   > [2024/08/05 08:06:49.551 +00:00] [INFO] [scheduler.rs:453] ["get snapshot failed"] [err="Error(Request(message: \"EpochNotMatch current epoch of region 2 is conf_ver: 1 version: 28, but you sent conf_ver: 1 version: 27\" epoch_not_match { current_regions { id: 2 start_key: 7480000000000000FF3A00000000000000F8 region_epoch { conf_ver: 1 version: 28 } peers { id: 3 store_id: 1 } } current_regions { id: 56 start_key: 7480000000000000FF3900000000000000F8 end_key: 7480000000000000FF3A00000000000000F8 region_epoch { conf_ver: 1 version: 28 } peers { id: 57 store_id: 1 } } }))"] [cid=309]
   > [2024/08/05 08:06:50.452 +00:00] [WARN] [errors.rs:293] ["txn deadlocks"] [err="Error(Txn(Error(Mvcc(Error(Deadlock { start_ts: TimeStamp(451633534527078406), lock_ts: TimeStamp(451633534448697345), lock_key: [116, 128, 0, 0, 0, 0, 0, 0, 56, 95, 114, 128, 0, 0, 0, 0, 0, 0, 1], deadlock_key_hash: 17139637628381125069, wait_chain: [txn: 451633534448697345 wait_for_txn: 451633534527078406 key_hash: 17139637628381125069 key: 7480000000000000395F728000000000000002 resource_group_tag: 0A204E310BD4576C5E689F6FDF93DCD99ED34EAAC181D66067073EBB0DCFF3A7BEA7, txn: 451633534527078406 wait_for_txn: 451633534448697345 key_hash: 10448634786545745333 key: 7480000000000000385F728000000000000001 resource_group_tag: 0A204E310BD4576C5E689F6FDF93DCD99ED34EAAC181D66067073EBB0DCFF3A7BEA7] })))))"]
   > [2024/08/05 08:06:50.454 +00:00] [INFO] [tidb.go:246] ["rollbackTxn for deadlock"] [txn=451633534527078406]
   > [2024/08/05 08:06:50.462 +00:00] [WARN] [session.go:1656] ["run statement failed"] [conn=11] [schemaVersion=28] [error="[executor:1213]Deadlock found when trying to get lock; try restarting transaction"] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 11,\n  \"status\": 2,\n  \"strictMode\": true,\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"127.0.0.1\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/08/05 08:06:50.462 +00:00] [INFO] [conn.go:995] ["command dispatched failed"] [conn=11] [connInfo="id:11, addr:127.0.0.1:38514 status:10, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:0, autocommit:1"] [sql=" update t set b=13 where a=1;"] [txn_mode=PESSIMISTIC] [err="[executor:1213]Deadlock found when trying to get lock; try restarting transaction"]
   > [2024/08/05 08:06:50.753 +00:00] [WARN] [keydecoder.go:98] ["no table found in infoschema"] [tableID=57] []
   > [2024/08/05 08:06:50.753 +00:00] [WARN] [keydecoder.go:98] ["no table found in infoschema"] [tableID=56] []
