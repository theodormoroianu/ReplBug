# Bug ID TIDB-26973-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/26973
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              The name of tables and handles are not parsed in DEBUG table.


## Details
 * Database: tidb-v5.2.0-alpha-1a54708a7.tikv
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
     - Output: [(1, datetime.datetime(2024, 8, 5, 8, 6, 50, 452353), 0, 451633534448697345, '4e310bd4576c5e689f6fdf93dcd99ed34eaac181d66067073ebb0dcff3a7bea7', 'update `t` set `b` = ? where `a` = ? ;', '7480000000000000395F728000000000000002', '{"table_id":57,"handle_type":"int","handle_value":"2"}', 451633534527078406), (1, datetime.datetime(2024, 8, 5, 8, 6, 50, 452353), 0, 451633534527078406, '4e310bd4576c5e689f6fdf93dcd99ed34eaac181d66067073ebb0dcff3a7bea7', 'update `t` set `b` = ? where `a` = ? ;', '7480000000000000385F728000000000000001', '{"table_id":56,"handle_type":"int","handle_value":"1"}', 451633534448697345), (2, datetime.datetime(2024, 8, 5, 8, 6, 56, 626872), 0, 451633536060882945, '4e310bd4576c5e689f6fdf93dcd99ed34eaac181d66067073ebb0dcff3a7bea7', 'update `t` set `b` = ? where `a` = ? ;', '7480000000000000475F728000000000000002', '{"table_id":71,"handle_type":"int","handle_value":"2"}', 451633536152371206), (2, datetime.datetime(2024, 8, 5, 8, 6, 56, 626872), 0, 451633536152371206, '4e310bd4576c5e689f6fdf93dcd99ed34eaac181d66067073ebb0dcff3a7bea7', 'update `t` set `b` = ? where `a` = ? ;', '7480000000000000465F728000000000000001', '{"table_id":70,"handle_type":"int","handle_value":"1"}', 451633536060882945)]
     - Executed order: 6
     - Affected rows: 4

 * Container logs:
   > [2024/08/05 08:06:53.163 +00:00] [INFO] [session.go:2920] ["CRUCIAL OPERATION"] [conn=15] [schemaVersion=36] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/08/05 08:06:53.181 +00:00] [INFO] [ddl_worker.go:316] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:66, Type:drop schema, State:none, SchemaState:queueing, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-05 08:06:53.126 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/05 08:06:53.181 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:66, Type:drop schema, State:none, SchemaState:queueing, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-05 08:06:53.126 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/08/05 08:06:53.184 +00:00] [INFO] [ddl_worker.go:715] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:drop schema, State:none, SchemaState:queueing, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-05 08:06:53.126 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/05 08:06:53.206 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=36] [neededSchemaVersion=37] ["start time"=697.164µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/05 08:06:53.256 +00:00] [INFO] [ddl_worker.go:900] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=37] ["take time"=52.733782ms] [job="ID:66, Type:drop schema, State:running, SchemaState:write only, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-05 08:06:53.126 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/05 08:06:53.258 +00:00] [INFO] [ddl_worker.go:715] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:drop schema, State:running, SchemaState:write only, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-05 08:06:53.126 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/05 08:06:53.292 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=37] [neededSchemaVersion=38] ["start time"=727.196µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/05 08:06:53.341 +00:00] [INFO] [ddl_worker.go:900] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=38] ["take time"=64.448466ms] [job="ID:66, Type:drop schema, State:running, SchemaState:delete only, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-05 08:06:53.126 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/05 08:06:53.343 +00:00] [INFO] [ddl_worker.go:715] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:drop schema, State:running, SchemaState:delete only, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-05 08:06:53.126 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/05 08:06:53.370 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=38] [neededSchemaVersion=39] ["start time"=688.643µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/05 08:06:53.419 +00:00] [INFO] [ddl_worker.go:900] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=39] ["take time"=52.170716ms] [job="ID:66, Type:drop schema, State:done, SchemaState:queueing, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-05 08:06:53.126 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/05 08:06:53.422 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=66] [jobType="drop schema"]
   > [2024/08/05 08:06:53.423 +00:00] [INFO] [ddl_worker.go:421] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-05 08:06:53.126 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/05 08:06:53.440 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=66]
   > [2024/08/05 08:06:53.440 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/08/05 08:06:53.443 +00:00] [INFO] [session.go:2920] ["CRUCIAL OPERATION"] [conn=15] [schemaVersion=39] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/08/05 08:06:53.475 +00:00] [INFO] [ddl_worker.go:316] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:68, Type:create schema, State:none, SchemaState:queueing, SchemaID:67, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-05 08:06:53.425 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/05 08:06:53.475 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:68, Type:create schema, State:none, SchemaState:queueing, SchemaID:67, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-05 08:06:53.425 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/08/05 08:06:53.479 +00:00] [INFO] [ddl_worker.go:715] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:68, Type:create schema, State:none, SchemaState:queueing, SchemaID:67, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-05 08:06:53.425 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/05 08:06:53.500 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=39] [neededSchemaVersion=40] ["start time"=1.268961ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/05 08:06:53.549 +00:00] [INFO] [ddl_worker.go:900] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=40] ["take time"=52.343784ms] [job="ID:68, Type:create schema, State:done, SchemaState:public, SchemaID:67, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-05 08:06:53.425 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/05 08:06:53.553 +00:00] [INFO] [ddl_worker.go:421] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:68, Type:create schema, State:synced, SchemaState:public, SchemaID:67, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-05 08:06:53.425 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/05 08:06:53.569 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=68]
   > [2024/08/05 08:06:53.569 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/08/05 08:06:53.573 +00:00] [INFO] [session.go:2920] ["CRUCIAL OPERATION"] [conn=15] [schemaVersion=40] [cur_db=testdb] [sql="create table t (a int primary key, b int) partition by range(a) (PARTITION p0 VALUES LESS THAN (2), PARTITION p1 VALUES LESS THAN (4),\n    PARTITION p2 VALUES LESS THAN (MAXVALUE));"] [user=root@127.0.0.1]
   > [2024/08/05 08:06:53.622 +00:00] [INFO] [ddl_worker.go:316] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:73, Type:create table, State:none, SchemaState:queueing, SchemaID:67, TableID:69, RowCount:0, ArgLen:1, start time: 2024-08-05 08:06:53.575 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/05 08:06:53.622 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:73, Type:create table, State:none, SchemaState:queueing, SchemaID:67, TableID:69, RowCount:0, ArgLen:1, start time: 2024-08-05 08:06:53.575 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t (a int primary key, b int) partition by range(a) (PARTITION p0 VALUES LESS THAN (2), PARTITION p1 VALUES LESS THAN (4),\n    PARTITION p2 VALUES LESS THAN (MAXVALUE));"]
   > [2024/08/05 08:06:53.626 +00:00] [INFO] [ddl_worker.go:715] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:73, Type:create table, State:none, SchemaState:queueing, SchemaID:67, TableID:69, RowCount:0, ArgLen:0, start time: 2024-08-05 08:06:53.575 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/05 08:06:53.662 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=40] [neededSchemaVersion=41] ["start time"=3.729847ms] [phyTblIDs="[69,70,71,72]"] [actionTypes="[8,8,8,8]"]
   > [2024/08/05 08:06:53.708 +00:00] [INFO] [ddl_worker.go:900] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=41] ["take time"=52.653952ms] [job="ID:73, Type:create table, State:done, SchemaState:public, SchemaID:67, TableID:69, RowCount:0, ArgLen:1, start time: 2024-08-05 08:06:53.575 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/05 08:06:53.712 +00:00] [INFO] [ddl_worker.go:421] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:73, Type:create table, State:synced, SchemaState:public, SchemaID:67, TableID:69, RowCount:0, ArgLen:0, start time: 2024-08-05 08:06:53.575 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/05 08:06:53.739 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=73]
   > [2024/08/05 08:06:53.739 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/08/05 08:06:53.739 +00:00] [INFO] [split_region.go:84] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=748000000000000046]
   > [2024/08/05 08:06:53.740 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56550] [split_keys="key 7480000000000000FF4600000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/05 08:06:53.740 +00:00] [INFO] [cluster_worker.go:127] ["alloc ids for region split"] [region-id=60] [peer-ids="[61]"]
   > [2024/08/05 08:06:53.741 +00:00] [INFO] [pd.rs:749] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF3F00000000000000F8 region_epoch { conf_ver: 1 version: 29 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 60 new_peer_ids: 61]"] [region_id=2]
   > [2024/08/05 08:06:53.756 +00:00] [INFO] [apply.rs:1394] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF4600000000000000F8 new_region_id: 60 new_peer_ids: 61 } right_derive: true }"] [index=68] [term=6] [peer_id=3] [region_id=2]
   > [2024/08/05 08:06:53.756 +00:00] [INFO] [apply.rs:2242] ["split region"] [keys="key 7480000000000000FF4600000000000000F8"] [region="id: 2 start_key: 7480000000000000FF3F00000000000000F8 region_epoch { conf_ver: 1 version: 29 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/08/05 08:06:53.767 +00:00] [INFO] [endpoint.rs:158] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/08/05 08:06:53.767 +00:00] [INFO] [peer.rs:2411] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/08/05 08:06:53.767 +00:00] [INFO] [peer.rs:2476] ["insert new region"] [region="id: 60 start_key: 7480000000000000FF3F00000000000000F8 end_key: 7480000000000000FF4600000000000000F8 region_epoch { conf_ver: 1 version: 30 } peers { id: 61 store_id: 1 }"] [region_id=60]
   > [2024/08/05 08:06:53.767 +00:00] [INFO] [peer.rs:219] ["create peer"] [peer_id=61] [region_id=60]
   > [2024/08/05 08:06:53.768 +00:00] [INFO] [split_region.go:185] ["batch split regions complete"] ["batch region ID"=2] ["first at"=748000000000000046] ["first new region left"="{Id:60 StartKey:7480000000000000ff3f00000000000000f8 EndKey:7480000000000000ff4600000000000000f8 RegionEpoch:{ConfVer:1 Version:30} Peers:[id:61 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/08/05 08:06:53.768 +00:00] [INFO] [split_region.go:234] ["split regions complete"] ["region count"=1] ["region IDs"="[60]"]
   > [2024/08/05 08:06:53.768 +00:00] [INFO] [split_region.go:84] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=748000000000000047]
   > [2024/08/05 08:06:53.768 +00:00] [INFO] [region.go:505] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF3F00000000000000F8} -> {7480000000000000FF4600000000000000F8}, EndKey:{}"] [old-version=29] [new-version=30]
   > [2024/08/05 08:06:53.768 +00:00] [INFO] [cluster_worker.go:219] ["region batch split, generate new regions"] [region-id=2] [origin="id:60 start_key:\"7480000000000000FF3F00000000000000F8\" end_key:\"7480000000000000FF4600000000000000F8\" region_epoch:<conf_ver:1 version:30 > peers:<id:61 store_id:1 >"] [total=1]
   > [2024/08/05 08:06:53.772 +00:00] [INFO] [raft.rs:2609] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {61} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=61] [region_id=60]
   > [2024/08/05 08:06:53.772 +00:00] [INFO] [raft.rs:1092] ["became follower at term 5"] [term=5] [raft_id=61] [region_id=60]
   > [2024/08/05 08:06:53.773 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {61} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=61] [region_id=60]
   > [2024/08/05 08:06:53.773 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 61."] [id=61] [raft_id=61] [region_id=60]
   > [2024/08/05 08:06:53.773 +00:00] [INFO] [raft.rs:1517] ["starting a new election"] [term=5] [raft_id=61] [region_id=60]
   > [2024/08/05 08:06:53.773 +00:00] [INFO] [raft.rs:1142] ["became pre-candidate at term 5"] [term=5] [raft_id=61] [region_id=60]
   > [2024/08/05 08:06:53.773 +00:00] [INFO] [raft.rs:1116] ["became candidate at term 6"] [term=6] [raft_id=61] [region_id=60]
   > [2024/08/05 08:06:53.773 +00:00] [INFO] [raft.rs:1200] ["became leader at term 6"] [term=6] [raft_id=61] [region_id=60]
   > [2024/08/05 08:06:53.773 +00:00] [INFO] [endpoint.rs:382] ["deregister observe region"] [observe_id=ObserveID(55)] [region_id=2] [store_id=Some(1)]
   > [2024/08/05 08:06:53.773 +00:00] [INFO] [peer.rs:3778] ["require updating max ts"] [initial_status=25769803836] [region_id=60]
   > [2024/08/05 08:06:53.773 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF4600000000000000F8 region_epoch { conf_ver: 1 version: 30 } peers { id: 3 store_id: 1 }"]
   > [2024/08/05 08:06:53.774 +00:00] [INFO] [pd.rs:1246] ["succeed to update max timestamp"] [region_id=60]
   > [2024/08/05 08:06:53.784 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56566] [split_keys="key 7480000000000000FF4700000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/05 08:06:53.784 +00:00] [INFO] [peer.rs:3911] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 29"] [prev_epoch="conf_ver: 1 version: 30"] [peer_id=3] [region_id=2]
   > [2024/08/05 08:06:53.785 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 60 start_key: 7480000000000000FF3F00000000000000F8 end_key: 7480000000000000FF4600000000000000F8 region_epoch { conf_ver: 1 version: 30 } peers { id: 61 store_id: 1 }"]
   > [2024/08/05 08:06:53.785 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=68] [observe_id=ObserveID(57)] [region=2]
   > [2024/08/05 08:06:53.790 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56574] [split_keys="key 7480000000000000FF4700000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/05 08:06:53.790 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveID(58)] [region=60]
   > [2024/08/05 08:06:53.791 +00:00] [INFO] [cluster_worker.go:127] ["alloc ids for region split"] [region-id=62] [peer-ids="[63]"]
   > [2024/08/05 08:06:53.791 +00:00] [INFO] [pd.rs:749] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF4600000000000000F8 region_epoch { conf_ver: 1 version: 30 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 62 new_peer_ids: 63]"] [region_id=2]
   > [2024/08/05 08:06:53.813 +00:00] [INFO] [apply.rs:1394] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF4700000000000000F8 new_region_id: 62 new_peer_ids: 63 } right_derive: true }"] [index=70] [term=6] [peer_id=3] [region_id=2]
   > [2024/08/05 08:06:53.813 +00:00] [INFO] [apply.rs:2242] ["split region"] [keys="key 7480000000000000FF4700000000000000F8"] [region="id: 2 start_key: 7480000000000000FF4600000000000000F8 region_epoch { conf_ver: 1 version: 30 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/08/05 08:06:53.819 +00:00] [INFO] [endpoint.rs:158] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/08/05 08:06:53.819 +00:00] [INFO] [peer.rs:2411] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/08/05 08:06:53.819 +00:00] [INFO] [peer.rs:2476] ["insert new region"] [region="id: 62 start_key: 7480000000000000FF4600000000000000F8 end_key: 7480000000000000FF4700000000000000F8 region_epoch { conf_ver: 1 version: 31 } peers { id: 63 store_id: 1 }"] [region_id=62]
   > [2024/08/05 08:06:53.819 +00:00] [INFO] [peer.rs:219] ["create peer"] [peer_id=63] [region_id=62]
   > [2024/08/05 08:06:53.819 +00:00] [INFO] [split_region.go:185] ["batch split regions complete"] ["batch region ID"=2] ["first at"=748000000000000047] ["first new region left"="{Id:62 StartKey:7480000000000000ff4600000000000000f8 EndKey:7480000000000000ff4700000000000000f8 RegionEpoch:{ConfVer:1 Version:31} Peers:[id:63 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/08/05 08:06:53.819 +00:00] [INFO] [raft.rs:2609] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {63} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=63] [region_id=62]
   > [2024/08/05 08:06:53.820 +00:00] [INFO] [split_region.go:234] ["split regions complete"] ["region count"=1] ["region IDs"="[62]"]
   > [2024/08/05 08:06:53.820 +00:00] [INFO] [split_region.go:84] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=748000000000000048]
   > [2024/08/05 08:06:53.820 +00:00] [INFO] [raft.rs:1092] ["became follower at term 5"] [term=5] [raft_id=63] [region_id=62]
   > [2024/08/05 08:06:53.820 +00:00] [INFO] [region.go:505] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF4600000000000000F8} -> {7480000000000000FF4700000000000000F8}, EndKey:{}"] [old-version=30] [new-version=31]
   > [2024/08/05 08:06:53.820 +00:00] [INFO] [cluster_worker.go:219] ["region batch split, generate new regions"] [region-id=2] [origin="id:62 start_key:\"7480000000000000FF4600000000000000F8\" end_key:\"7480000000000000FF4700000000000000F8\" region_epoch:<conf_ver:1 version:31 > peers:<id:63 store_id:1 >"] [total=1]
   > [2024/08/05 08:06:53.820 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {63} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=63] [region_id=62]
   > [2024/08/05 08:06:53.820 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 63."] [id=63] [raft_id=63] [region_id=62]
   > [2024/08/05 08:06:53.820 +00:00] [INFO] [raft.rs:1517] ["starting a new election"] [term=5] [raft_id=63] [region_id=62]
   > [2024/08/05 08:06:53.820 +00:00] [INFO] [raft.rs:1142] ["became pre-candidate at term 5"] [term=5] [raft_id=63] [region_id=62]
   > [2024/08/05 08:06:53.820 +00:00] [INFO] [raft.rs:1116] ["became candidate at term 6"] [term=6] [raft_id=63] [region_id=62]
   > [2024/08/05 08:06:53.820 +00:00] [INFO] [raft.rs:1200] ["became leader at term 6"] [term=6] [raft_id=63] [region_id=62]
   > [2024/08/05 08:06:53.820 +00:00] [INFO] [endpoint.rs:382] ["deregister observe region"] [observe_id=ObserveID(57)] [region_id=2] [store_id=Some(1)]
   > [2024/08/05 08:06:53.820 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF4700000000000000F8 region_epoch { conf_ver: 1 version: 31 } peers { id: 3 store_id: 1 }"]
   > [2024/08/05 08:06:53.820 +00:00] [INFO] [peer.rs:3778] ["require updating max ts"] [initial_status=25769803838] [region_id=62]
   > [2024/08/05 08:06:53.821 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56576] [split_keys="key 7480000000000000FF4800000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/05 08:06:53.821 +00:00] [INFO] [peer.rs:3911] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 30"] [prev_epoch="conf_ver: 1 version: 31"] [peer_id=3] [region_id=2]
   > [2024/08/05 08:06:53.821 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=70] [observe_id=ObserveID(59)] [region=2]
   > [2024/08/05 08:06:53.821 +00:00] [INFO] [pd.rs:1246] ["succeed to update max timestamp"] [region_id=62]
   > [2024/08/05 08:06:53.824 +00:00] [INFO] [peer.rs:3828] ["on split"] [source=ipv4:127.0.0.1:56550] [split_keys="key 7480000000000000FF4800000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/05 08:06:53.825 +00:00] [INFO] [cluster_worker.go:127] ["alloc ids for region split"] [region-id=64] [peer-ids="[65]"]
   > [2024/08/05 08:06:53.825 +00:00] [INFO] [pd.rs:749] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF4700000000000000F8 region_epoch { conf_ver: 1 version: 31 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 64 new_peer_ids: 65]"] [region_id=2]
   > [2024/08/05 08:06:53.826 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 62 start_key: 7480000000000000FF4600000000000000F8 end_key: 7480000000000000FF4700000000000000F8 region_epoch { conf_ver: 1 version: 31 } peers { id: 63 store_id: 1 }"]
   > [2024/08/05 08:06:53.826 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveID(60)] [region=62]
   > [2024/08/05 08:06:53.831 +00:00] [INFO] [apply.rs:1394] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF4800000000000000F8 new_region_id: 64 new_peer_ids: 65 } right_derive: true }"] [index=71] [term=6] [peer_id=3] [region_id=2]
   > [2024/08/05 08:06:53.832 +00:00] [INFO] [apply.rs:2242] ["split region"] [keys="key 7480000000000000FF4800000000000000F8"] [region="id: 2 start_key: 7480000000000000FF4700000000000000F8 region_epoch { conf_ver: 1 version: 31 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/08/05 08:06:53.837 +00:00] [INFO] [endpoint.rs:158] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/08/05 08:06:53.837 +00:00] [INFO] [peer.rs:2411] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/08/05 08:06:53.837 +00:00] [INFO] [peer.rs:2476] ["insert new region"] [region="id: 64 start_key: 7480000000000000FF4700000000000000F8 end_key: 7480000000000000FF4800000000000000F8 region_epoch { conf_ver: 1 version: 32 } peers { id: 65 store_id: 1 }"] [region_id=64]
   > [2024/08/05 08:06:53.837 +00:00] [INFO] [peer.rs:219] ["create peer"] [peer_id=65] [region_id=64]
   > [2024/08/05 08:06:53.837 +00:00] [INFO] [split_region.go:185] ["batch split regions complete"] ["batch region ID"=2] ["first at"=748000000000000048] ["first new region left"="{Id:64 StartKey:7480000000000000ff4700000000000000f8 EndKey:7480000000000000ff4800000000000000f8 RegionEpoch:{ConfVer:1 Version:32} Peers:[id:65 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/08/05 08:06:53.837 +00:00] [INFO] [raft.rs:2609] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {65} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=65] [region_id=64]
   > [2024/08/05 08:06:53.837 +00:00] [INFO] [split_region.go:234] ["split regions complete"] ["region count"=1] ["region IDs"="[64]"]
   > [2024/08/05 08:06:53.837 +00:00] [INFO] [raft.rs:1092] ["became follower at term 5"] [term=5] [raft_id=65] [region_id=64]
   > [2024/08/05 08:06:53.838 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {65} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=65] [region_id=64]
   > [2024/08/05 08:06:53.838 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 65."] [id=65] [raft_id=65] [region_id=64]
   > [2024/08/05 08:06:53.838 +00:00] [INFO] [region.go:505] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF4700000000000000F8} -> {7480000000000000FF4800000000000000F8}, EndKey:{}"] [old-version=31] [new-version=32]
   > [2024/08/05 08:06:53.838 +00:00] [INFO] [cluster_worker.go:219] ["region batch split, generate new regions"] [region-id=2] [origin="id:64 start_key:\"7480000000000000FF4700000000000000F8\" end_key:\"7480000000000000FF4800000000000000F8\" region_epoch:<conf_ver:1 version:32 > peers:<id:65 store_id:1 >"] [total=1]
   > [2024/08/05 08:06:53.838 +00:00] [INFO] [raft.rs:1517] ["starting a new election"] [term=5] [raft_id=65] [region_id=64]
   > [2024/08/05 08:06:53.838 +00:00] [INFO] [raft.rs:1142] ["became pre-candidate at term 5"] [term=5] [raft_id=65] [region_id=64]
   > [2024/08/05 08:06:53.838 +00:00] [INFO] [raft.rs:1116] ["became candidate at term 6"] [term=6] [raft_id=65] [region_id=64]
   > [2024/08/05 08:06:53.838 +00:00] [INFO] [raft.rs:1200] ["became leader at term 6"] [term=6] [raft_id=65] [region_id=64]
   > [2024/08/05 08:06:53.838 +00:00] [INFO] [peer.rs:3778] ["require updating max ts"] [initial_status=25769803840] [region_id=64]
   > [2024/08/05 08:06:53.838 +00:00] [INFO] [endpoint.rs:382] ["deregister observe region"] [observe_id=ObserveID(59)] [region_id=2] [store_id=Some(1)]
   > [2024/08/05 08:06:53.838 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF4800000000000000F8 region_epoch { conf_ver: 1 version: 32 } peers { id: 3 store_id: 1 }"]
   > [2024/08/05 08:06:53.838 +00:00] [INFO] [pd.rs:1246] ["succeed to update max timestamp"] [region_id=64]
   > [2024/08/05 08:06:53.844 +00:00] [INFO] [endpoint.rs:309] ["register observe region"] [region="id: 64 start_key: 7480000000000000FF4700000000000000F8 end_key: 7480000000000000FF4800000000000000F8 region_epoch { conf_ver: 1 version: 32 } peers { id: 65 store_id: 1 }"]
   > [2024/08/05 08:06:53.844 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=71] [observe_id=ObserveID(61)] [region=2]
   > [2024/08/05 08:06:53.844 +00:00] [INFO] [endpoint.rs:233] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveID(62)] [region=64]
   > [2024/08/05 08:06:55.728 +00:00] [INFO] [scheduler.rs:453] ["get snapshot failed"] [err="Error(Request(message: \"EpochNotMatch current epoch of region 2 is conf_ver: 1 version: 32, but you sent conf_ver: 1 version: 31\" epoch_not_match { current_regions { id: 2 start_key: 7480000000000000FF4800000000000000F8 region_epoch { conf_ver: 1 version: 32 } peers { id: 3 store_id: 1 } } current_regions { id: 64 start_key: 7480000000000000FF4700000000000000F8 end_key: 7480000000000000FF4800000000000000F8 region_epoch { conf_ver: 1 version: 32 } peers { id: 65 store_id: 1 } } }))"] [cid=425]
   > [2024/08/05 08:06:56.626 +00:00] [WARN] [errors.rs:293] ["txn deadlocks"] [err="Error(Txn(Error(Mvcc(Error(Deadlock { start_ts: TimeStamp(451633536152371206), lock_ts: TimeStamp(451633536060882945), lock_key: [116, 128, 0, 0, 0, 0, 0, 0, 70, 95, 114, 128, 0, 0, 0, 0, 0, 0, 1], deadlock_key_hash: 5707591179443765641, wait_chain: [txn: 451633536060882945 wait_for_txn: 451633536152371206 key_hash: 5707591179443765641 key: 7480000000000000475F728000000000000002 resource_group_tag: 0A204E310BD4576C5E689F6FDF93DCD99ED34EAAC181D66067073EBB0DCFF3A7BEA7, txn: 451633536152371206 wait_for_txn: 451633536060882945 key_hash: 17164398476904587090 key: 7480000000000000465F728000000000000001 resource_group_tag: 0A204E310BD4576C5E689F6FDF93DCD99ED34EAAC181D66067073EBB0DCFF3A7BEA7] })))))"]
   > [2024/08/05 08:06:56.627 +00:00] [INFO] [tidb.go:246] ["rollbackTxn for deadlock"] [txn=451633536152371206]
   > [2024/08/05 08:06:56.635 +00:00] [WARN] [session.go:1656] ["run statement failed"] [conn=19] [schemaVersion=41] [error="[executor:1213]Deadlock found when trying to get lock; try restarting transaction"] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 19,\n  \"status\": 2,\n  \"strictMode\": true,\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"127.0.0.1\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/08/05 08:06:56.635 +00:00] [INFO] [conn.go:995] ["command dispatched failed"] [conn=19] [connInfo="id:19, addr:127.0.0.1:38552 status:10, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:0, autocommit:1"] [sql=" update t set b=13 where a=1;"] [txn_mode=PESSIMISTIC] [err="[executor:1213]Deadlock found when trying to get lock; try restarting transaction"]
   > [2024/08/05 08:06:56.928 +00:00] [WARN] [keydecoder.go:98] ["no table found in infoschema"] [tableID=57] []
   > [2024/08/05 08:06:56.928 +00:00] [WARN] [keydecoder.go:98] ["no table found in infoschema"] [tableID=56] []
   > [2024/08/05 08:06:56.928 +00:00] [WARN] [keydecoder.go:98] ["no table found in infoschema"] [tableID=71] []
   > [2024/08/05 08:06:56.928 +00:00] [WARN] [keydecoder.go:98] ["no table found in infoschema"] [tableID=70] []
