# Bug ID TIDB-21498-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/21498
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              transaction sees inconsistent data when there are concurrent DDLs


## Details
 * Database: tidb-3a32bd2d.tikv
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
     - Instruction:  SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows: 0
 * Instruction #2:
     - Instruction:  begin;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows: 0
 * Instruction #3:
     - Instruction:  explain select * from t where v = 10;
     - Transaction: conn_0
     - Output: [('IndexReader_6', '10.00', 'root', '', 'index:IndexRangeScan_5'), ('└─IndexRangeScan_5', '10.00', 'cop[tikv]', 'table:t, index:iv(v)', 'range:[10,10], keep order:false, stats:pseudo')]
     - Executed order: 3
     - Affected rows: 2
 * Instruction #4:
     - Instruction:  select * from t where v = 10;
     - Transaction: conn_0
     - Output: [(1, 10)]
     - Executed order: 4
     - Affected rows: 1
 * Instruction #5:
     - Instruction:  alter table t drop index iv;
     - Transaction: conn_1
     - Output: None
     - Executed order: 5
     - Affected rows: 0
 * Instruction #6:
     - Instruction:  update t set v = 11 where id = 1;
     - Transaction: conn_1
     - Output: None
     - Executed order: 6
     - Affected rows: 1
 * Instruction #7:
     - Instruction:  explain select * from t where v = 10;
     - Transaction: conn_0
     - Output: [('IndexReader_6', '10.00', 'root', '', 'index:IndexRangeScan_5'), ('└─IndexRangeScan_5', '10.00', 'cop[tikv]', 'table:t, index:iv(v)', 'range:[10,10], keep order:false, stats:pseudo')]
     - Executed order: 7
     - Affected rows: 2
 * Instruction #8:
     - Instruction:  select * from t where v = 10;
     - Transaction: conn_0
     - Output: [(1, 10)]
     - Executed order: 8
     - Affected rows: 1
 * Instruction #9:
     - Instruction:  select * from t where id = 1;
     - Transaction: conn_0
     - Output: [(1, 10)]
     - Executed order: 9
     - Affected rows: 1

 * Container logs:
   > [2024/08/07 13:33:01.944 +00:00] [INFO] [session.go:2469] ["CRUCIAL OPERATION"] [conn=1946964612930863111] [schemaVersion=24] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/08/07 13:33:01.945 +00:00] [INFO] [session.go:2469] ["CRUCIAL OPERATION"] [conn=1946964612930863111] [schemaVersion=24] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/08/07 13:33:01.986 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:50, Type:create schema, State:none, SchemaState:none, SchemaID:49, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-07 13:33:01.927 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/07 13:33:01.986 +00:00] [INFO] [ddl.go:538] ["[ddl] start DDL job"] [job="ID:50, Type:create schema, State:none, SchemaState:none, SchemaID:49, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-07 13:33:01.927 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/08/07 13:33:01.990 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:50, Type:create schema, State:none, SchemaState:none, SchemaID:49, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-07 13:33:01.927 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:33:02.022 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=24] [neededSchemaVersion=25] ["start time"=1.467311ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/07 13:33:02.071 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=25] ["take time"=60.454312ms] [job="ID:50, Type:create schema, State:done, SchemaState:public, SchemaID:49, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-07 13:33:01.927 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:33:02.074 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:50, Type:create schema, State:synced, SchemaState:public, SchemaID:49, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-07 13:33:01.927 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:33:02.095 +00:00] [INFO] [ddl.go:594] ["[ddl] DDL job is finished"] [jobID=50]
   > [2024/08/07 13:33:02.095 +00:00] [INFO] [domain.go:659] ["performing DDL change, must reload"]
   > [2024/08/07 13:33:02.098 +00:00] [INFO] [session.go:2469] ["CRUCIAL OPERATION"] [conn=1946964612930863111] [schemaVersion=25] [cur_db=testdb] [sql="create table t (id int primary key, v int, index iv (v));"] [user=root@127.0.0.1]
   > [2024/08/07 13:33:02.140 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:52, Type:create table, State:none, SchemaState:none, SchemaID:49, TableID:51, RowCount:0, ArgLen:1, start time: 2024-08-07 13:33:02.077 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/07 13:33:02.140 +00:00] [INFO] [ddl.go:538] ["[ddl] start DDL job"] [job="ID:52, Type:create table, State:none, SchemaState:none, SchemaID:49, TableID:51, RowCount:0, ArgLen:1, start time: 2024-08-07 13:33:02.077 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t (id int primary key, v int, index iv (v));"]
   > [2024/08/07 13:33:02.144 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:52, Type:create table, State:none, SchemaState:none, SchemaID:49, TableID:51, RowCount:0, ArgLen:0, start time: 2024-08-07 13:33:02.077 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:33:02.188 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=25] [neededSchemaVersion=26] ["start time"=1.855352ms] [phyTblIDs="[51]"] [actionTypes="[8]"]
   > [2024/08/07 13:33:02.255 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=26] ["take time"=79.941553ms] [job="ID:52, Type:create table, State:done, SchemaState:public, SchemaID:49, TableID:51, RowCount:0, ArgLen:1, start time: 2024-08-07 13:33:02.077 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:33:02.259 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:52, Type:create table, State:synced, SchemaState:public, SchemaID:49, TableID:51, RowCount:0, ArgLen:0, start time: 2024-08-07 13:33:02.077 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:33:02.296 +00:00] [INFO] [ddl.go:594] ["[ddl] DDL job is finished"] [jobID=52]
   > [2024/08/07 13:33:02.299 +00:00] [INFO] [domain.go:659] ["performing DDL change, must reload"]
   > [2024/08/07 13:33:02.299 +00:00] [INFO] [split_region.go:61] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=748000000000000033]
   > [2024/08/07 13:33:02.299 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:56996] [split_keys="key 7480000000000000FF3300000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/07 13:33:02.300 +00:00] [INFO] [peer.rs:5566] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 22"] [prev_epoch="conf_ver: 1 version: 23"] [peer_id=3] [region_id=2]
   > [2024/08/07 13:33:02.315 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:56966] [split_keys="key 7480000000000000FF3300000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/07 13:33:02.315 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=48] [peer-ids="[49]"]
   > [2024/08/07 13:33:02.316 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 23 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 48 new_peer_ids: 49]"] [region_id=2]
   > [2024/08/07 13:33:02.325 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF3300000000000000F8 new_region_id: 48 new_peer_ids: 49 } right_derive: true }"] [index=56] [term=6] [peer_id=3] [region_id=2]
   > [2024/08/07 13:33:02.325 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF3300000000000000F8"] [region="id: 2 start_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 23 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/08/07 13:33:02.335 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=2]
   > [2024/08/07 13:33:02.335 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/08/07 13:33:02.335 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(43)] [region_id=2] [store_id=Some(1)]
   > [2024/08/07 13:33:02.335 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/08/07 13:33:02.335 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF2F00000000000000F8} -> {7480000000000000FF3300000000000000F8}, EndKey:{}"] [old-version=23] [new-version=24]
   > [2024/08/07 13:33:02.335 +00:00] [INFO] [split_region.go:158] ["batch split regions complete"] ["batch region ID"=2] ["first at"=748000000000000033] ["first new region left"="{Id:48 StartKey:7480000000000000ff2f00000000000000f8 EndKey:7480000000000000ff3300000000000000f8 RegionEpoch:{ConfVer:1 Version:24} Peers:[id:49 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/08/07 13:33:02.335 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF3300000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 3 store_id: 1 }"]
   > [2024/08/07 13:33:02.335 +00:00] [INFO] [split_region.go:207] ["split regions complete"] ["region count"=1] ["region IDs"="[48]"]
   > [2024/08/07 13:33:02.335 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 48 start_key: 7480000000000000FF2F00000000000000F8 end_key: 7480000000000000FF3300000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 49 store_id: 1 }"] [region_id=48]
   > [2024/08/07 13:33:02.335 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=49] [region_id=48]
   > [2024/08/07 13:33:02.335 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {49} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=49] [region_id=48]
   > [2024/08/07 13:33:02.335 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=49] [region_id=48]
   > [2024/08/07 13:33:02.336 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {49} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=49] [region_id=48]
   > [2024/08/07 13:33:02.335 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=2] [origin="id:48 start_key:\"7480000000000000FF2F00000000000000F8\" end_key:\"7480000000000000FF3300000000000000F8\" region_epoch:<conf_ver:1 version:24 > peers:<id:49 store_id:1 >"] [total=1]
   > [2024/08/07 13:33:02.336 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 49."] [id=49] [raft_id=49] [region_id=48]
   > [2024/08/07 13:33:02.336 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=49] [region_id=48]
   > [2024/08/07 13:33:02.336 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=49] [region_id=48]
   > [2024/08/07 13:33:02.336 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=49] [region_id=48]
   > [2024/08/07 13:33:02.336 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 2 start_key: 7480000000000000FF3300000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 3 store_id: 1 } }"]
   > [2024/08/07 13:33:02.336 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 2 start_key: 7480000000000000FF3300000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 3 store_id: 1 }"]
   > [2024/08/07 13:33:02.336 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=49] [region_id=48]
   > [2024/08/07 13:33:02.336 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803824] [region_id=48]
   > [2024/08/07 13:33:02.336 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=48]
   > [2024/08/07 13:33:02.345 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=56] [observe_id=ObserveId(45)] [region=2]
   > [2024/08/07 13:33:02.345 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 48 start_key: 7480000000000000FF2F00000000000000F8 end_key: 7480000000000000FF3300000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 49 store_id: 1 }"]
   > [2024/08/07 13:33:02.345 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(46)] [region=48]
   > [2024/08/07 13:33:03.381 +00:00] [INFO] [set.go:217] ["set global var"] [conn=1946964612930863113] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/08/07 13:33:03.383 +00:00] [INFO] [set.go:217] ["set global var"] [conn=1946964612930863113] [name=transaction_isolation] [val=REPEATABLE-READ]
   > [2024/08/07 13:33:04.131 +00:00] [INFO] [cluster.go:1469] ["store has changed to serving"] [store-id=1] [store-address=127.0.0.1:20160]
   > [2024/08/07 13:33:04.189 +00:00] [INFO] [client.rs:789] ["set cluster version to 6.4.0"]
   > [2024/08/07 13:33:04.884 +00:00] [INFO] [session.go:2469] ["CRUCIAL OPERATION"] [conn=1946964612930863115] [schemaVersion=26] [cur_db=testdb] [sql=" alter table t drop index iv;"] [user=root@127.0.0.1]
   > [2024/08/07 13:33:04.909 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:53, Type:drop index, State:none, SchemaState:none, SchemaID:49, TableID:51, RowCount:0, ArgLen:1, start time: 2024-08-07 13:33:04.877 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/07 13:33:04.909 +00:00] [INFO] [ddl.go:538] ["[ddl] start DDL job"] [job="ID:53, Type:drop index, State:none, SchemaState:none, SchemaID:49, TableID:51, RowCount:0, ArgLen:1, start time: 2024-08-07 13:33:04.877 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query=" alter table t drop index iv;"]
   > [2024/08/07 13:33:04.913 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:53, Type:drop index, State:none, SchemaState:none, SchemaID:49, TableID:51, RowCount:0, ArgLen:0, start time: 2024-08-07 13:33:04.877 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:33:04.948 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=26] [neededSchemaVersion=27] ["start time"=2.162936ms] [phyTblIDs="[51]"] [actionTypes="[256]"]
   > [2024/08/07 13:33:04.997 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=27] ["take time"=61.217127ms] [job="ID:53, Type:drop index, State:running, SchemaState:write only, SchemaID:49, TableID:51, RowCount:0, ArgLen:1, start time: 2024-08-07 13:33:04.877 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:33:04.999 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:53, Type:drop index, State:running, SchemaState:write only, SchemaID:49, TableID:51, RowCount:0, ArgLen:0, start time: 2024-08-07 13:33:04.877 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:33:05.036 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=27] [neededSchemaVersion=28] ["start time"=2.249191ms] [phyTblIDs="[51]"] [actionTypes="[256]"]
   > [2024/08/07 13:33:05.090 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=28] ["take time"=66.646223ms] [job="ID:53, Type:drop index, State:running, SchemaState:delete only, SchemaID:49, TableID:51, RowCount:0, ArgLen:1, start time: 2024-08-07 13:33:04.877 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:33:05.092 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:53, Type:drop index, State:running, SchemaState:delete only, SchemaID:49, TableID:51, RowCount:0, ArgLen:0, start time: 2024-08-07 13:33:04.877 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:33:05.128 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=28] [neededSchemaVersion=29] ["start time"=2.023811ms] [phyTblIDs="[51]"] [actionTypes="[256]"]
   > [2024/08/07 13:33:05.177 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=29] ["take time"=61.419249ms] [job="ID:53, Type:drop index, State:running, SchemaState:delete reorganization, SchemaID:49, TableID:51, RowCount:0, ArgLen:1, start time: 2024-08-07 13:33:04.877 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:33:05.179 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:53, Type:drop index, State:running, SchemaState:delete reorganization, SchemaID:49, TableID:51, RowCount:0, ArgLen:0, start time: 2024-08-07 13:33:04.877 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:33:05.219 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=29] [neededSchemaVersion=30] ["start time"=2.263858ms] [phyTblIDs="[51]"] [actionTypes="[256]"]
   > [2024/08/07 13:33:05.267 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=30] ["take time"=61.632267ms] [job="ID:53, Type:drop index, State:done, SchemaState:none, SchemaID:49, TableID:51, RowCount:0, ArgLen:3, start time: 2024-08-07 13:33:04.877 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:33:05.269 +00:00] [INFO] [delete_range.go:421] ["[ddl] insert into delete-range table"] [jobID=53] [elementID=1]
   > [2024/08/07 13:33:05.315 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=53] [jobType="drop index"]
   > [2024/08/07 13:33:05.317 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:53, Type:drop index, State:synced, SchemaState:none, SchemaID:49, TableID:51, RowCount:0, ArgLen:3, start time: 2024-08-07 13:33:04.877 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:33:05.338 +00:00] [INFO] [ddl.go:594] ["[ddl] DDL job is finished"] [jobID=53]
   > [2024/08/07 13:33:05.338 +00:00] [INFO] [domain.go:659] ["performing DDL change, must reload"]
