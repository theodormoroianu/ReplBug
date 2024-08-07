# Bug ID TIDB-21498-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/21498
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              transaction sees inconsistent data when there are concurrent DDLs


## Details
 * Database: tidb-3a32bd2d.tikv
 * Number of scenarios: 1
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
     - Instruction:  SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
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
     - Output: [(1, 11)]
     - Executed order: 9
     - Affected rows: 1

 * Container logs:
   > [2024/08/07 13:33:08.521 +00:00] [INFO] [session.go:2469] ["CRUCIAL OPERATION"] [conn=1946964612930863119] [schemaVersion=38] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/08/07 13:33:08.544 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:60, Type:drop schema, State:none, SchemaState:none, SchemaID:55, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-07 13:33:08.477 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/07 13:33:08.544 +00:00] [INFO] [ddl.go:538] ["[ddl] start DDL job"] [job="ID:60, Type:drop schema, State:none, SchemaState:none, SchemaID:55, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-07 13:33:08.477 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/08/07 13:33:08.548 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:60, Type:drop schema, State:none, SchemaState:none, SchemaID:55, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-07 13:33:08.477 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:33:08.587 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=38] [neededSchemaVersion=39] ["start time"=726.427µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/07 13:33:08.637 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=39] ["take time"=61.891451ms] [job="ID:60, Type:drop schema, State:running, SchemaState:write only, SchemaID:55, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-07 13:33:08.477 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:33:08.639 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:60, Type:drop schema, State:running, SchemaState:write only, SchemaID:55, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-07 13:33:08.477 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:33:08.683 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=39] [neededSchemaVersion=40] ["start time"=687.944µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/07 13:33:08.733 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=40] ["take time"=66.908899ms] [job="ID:60, Type:drop schema, State:running, SchemaState:delete only, SchemaID:55, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-07 13:33:08.477 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:33:08.735 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:60, Type:drop schema, State:running, SchemaState:delete only, SchemaID:55, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-07 13:33:08.477 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:33:08.773 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=40] [neededSchemaVersion=41] ["start time"=704.635µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/07 13:33:08.823 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=41] ["take time"=61.28627ms] [job="ID:60, Type:drop schema, State:done, SchemaState:none, SchemaID:55, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-07 13:33:08.477 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:33:08.825 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=60] [jobType="drop schema"]
   > [2024/08/07 13:33:08.827 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:60, Type:drop schema, State:synced, SchemaState:none, SchemaID:55, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-07 13:33:08.477 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:33:08.865 +00:00] [INFO] [ddl.go:594] ["[ddl] DDL job is finished"] [jobID=60]
   > [2024/08/07 13:33:08.865 +00:00] [INFO] [domain.go:659] ["performing DDL change, must reload"]
   > [2024/08/07 13:33:08.867 +00:00] [INFO] [session.go:2469] ["CRUCIAL OPERATION"] [conn=1946964612930863119] [schemaVersion=41] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/08/07 13:33:08.913 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:62, Type:create schema, State:none, SchemaState:none, SchemaID:61, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-07 13:33:08.877 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/07 13:33:08.913 +00:00] [INFO] [ddl.go:538] ["[ddl] start DDL job"] [job="ID:62, Type:create schema, State:none, SchemaState:none, SchemaID:61, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-07 13:33:08.877 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/08/07 13:33:08.917 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:62, Type:create schema, State:none, SchemaState:none, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-07 13:33:08.877 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:33:08.951 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=41] [neededSchemaVersion=42] ["start time"=1.37882ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/07 13:33:08.999 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=42] ["take time"=60.666422ms] [job="ID:62, Type:create schema, State:done, SchemaState:public, SchemaID:61, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-07 13:33:08.877 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:33:09.003 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:62, Type:create schema, State:synced, SchemaState:public, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-07 13:33:08.877 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:33:09.024 +00:00] [INFO] [ddl.go:594] ["[ddl] DDL job is finished"] [jobID=62]
   > [2024/08/07 13:33:09.024 +00:00] [INFO] [domain.go:659] ["performing DDL change, must reload"]
   > [2024/08/07 13:33:09.027 +00:00] [INFO] [session.go:2469] ["CRUCIAL OPERATION"] [conn=1946964612930863119] [schemaVersion=42] [cur_db=testdb] [sql="create table t (id int primary key, v int, index iv (v));"] [user=root@127.0.0.1]
   > [2024/08/07 13:33:09.074 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:64, Type:create table, State:none, SchemaState:none, SchemaID:61, TableID:63, RowCount:0, ArgLen:1, start time: 2024-08-07 13:33:09.027 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/07 13:33:09.074 +00:00] [INFO] [ddl.go:538] ["[ddl] start DDL job"] [job="ID:64, Type:create table, State:none, SchemaState:none, SchemaID:61, TableID:63, RowCount:0, ArgLen:1, start time: 2024-08-07 13:33:09.027 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t (id int primary key, v int, index iv (v));"]
   > [2024/08/07 13:33:09.078 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:64, Type:create table, State:none, SchemaState:none, SchemaID:61, TableID:63, RowCount:0, ArgLen:0, start time: 2024-08-07 13:33:09.027 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:33:09.122 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=42] [neededSchemaVersion=43] ["start time"=2.173552ms] [phyTblIDs="[63]"] [actionTypes="[8]"]
   > [2024/08/07 13:33:09.170 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=43] ["take time"=61.574997ms] [job="ID:64, Type:create table, State:done, SchemaState:public, SchemaID:61, TableID:63, RowCount:0, ArgLen:1, start time: 2024-08-07 13:33:09.027 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:33:09.174 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:64, Type:create table, State:synced, SchemaState:public, SchemaID:61, TableID:63, RowCount:0, ArgLen:0, start time: 2024-08-07 13:33:09.027 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:33:09.196 +00:00] [INFO] [ddl.go:594] ["[ddl] DDL job is finished"] [jobID=64]
   > [2024/08/07 13:33:09.199 +00:00] [INFO] [domain.go:659] ["performing DDL change, must reload"]
   > [2024/08/07 13:33:09.199 +00:00] [INFO] [split_region.go:61] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=74800000000000003f]
   > [2024/08/07 13:33:09.200 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:56982] [split_keys="key 7480000000000000FF3F00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/07 13:33:09.200 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=52] [peer-ids="[53]"]
   > [2024/08/07 13:33:09.201 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF3900000000000000F8 region_epoch { conf_ver: 1 version: 25 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 52 new_peer_ids: 53]"] [region_id=2]
   > [2024/08/07 13:33:09.210 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF3F00000000000000F8 new_region_id: 52 new_peer_ids: 53 } right_derive: true }"] [index=64] [term=6] [peer_id=3] [region_id=2]
   > [2024/08/07 13:33:09.211 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF3F00000000000000F8"] [region="id: 2 start_key: 7480000000000000FF3900000000000000F8 region_epoch { conf_ver: 1 version: 25 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/08/07 13:33:09.220 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=2]
   > [2024/08/07 13:33:09.220 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/08/07 13:33:09.220 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(47)] [region_id=2] [store_id=Some(1)]
   > [2024/08/07 13:33:09.220 +00:00] [INFO] [split_region.go:158] ["batch split regions complete"] ["batch region ID"=2] ["first at"=74800000000000003f] ["first new region left"="{Id:52 StartKey:7480000000000000ff3900000000000000f8 EndKey:7480000000000000ff3f00000000000000f8 RegionEpoch:{ConfVer:1 Version:26} Peers:[id:53 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/08/07 13:33:09.220 +00:00] [INFO] [split_region.go:207] ["split regions complete"] ["region count"=1] ["region IDs"="[52]"]
   > [2024/08/07 13:33:09.220 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/08/07 13:33:09.220 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF3F00000000000000F8 region_epoch { conf_ver: 1 version: 26 } peers { id: 3 store_id: 1 }"]
   > [2024/08/07 13:33:09.220 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 52 start_key: 7480000000000000FF3900000000000000F8 end_key: 7480000000000000FF3F00000000000000F8 region_epoch { conf_ver: 1 version: 26 } peers { id: 53 store_id: 1 }"] [region_id=52]
   > [2024/08/07 13:33:09.221 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=53] [region_id=52]
   > [2024/08/07 13:33:09.221 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF3900000000000000F8} -> {7480000000000000FF3F00000000000000F8}, EndKey:{}"] [old-version=25] [new-version=26]
   > [2024/08/07 13:33:09.221 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 2 start_key: 7480000000000000FF3F00000000000000F8 region_epoch { conf_ver: 1 version: 26 } peers { id: 3 store_id: 1 } }"]
   > [2024/08/07 13:33:09.221 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 2 start_key: 7480000000000000FF3F00000000000000F8 region_epoch { conf_ver: 1 version: 26 } peers { id: 3 store_id: 1 }"]
   > [2024/08/07 13:33:09.221 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=2] [origin="id:52 start_key:\"7480000000000000FF3900000000000000F8\" end_key:\"7480000000000000FF3F00000000000000F8\" region_epoch:<conf_ver:1 version:26 > peers:<id:53 store_id:1 >"] [total=1]
   > [2024/08/07 13:33:09.221 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {53} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=53] [region_id=52]
   > [2024/08/07 13:33:09.221 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=53] [region_id=52]
   > [2024/08/07 13:33:09.221 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {53} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=53] [region_id=52]
   > [2024/08/07 13:33:09.221 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 53."] [id=53] [raft_id=53] [region_id=52]
   > [2024/08/07 13:33:09.221 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=53] [region_id=52]
   > [2024/08/07 13:33:09.221 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=53] [region_id=52]
   > [2024/08/07 13:33:09.221 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=53] [region_id=52]
   > [2024/08/07 13:33:09.221 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=53] [region_id=52]
   > [2024/08/07 13:33:09.222 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803828] [region_id=52]
   > [2024/08/07 13:33:09.222 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=64] [observe_id=ObserveId(49)] [region=2]
   > [2024/08/07 13:33:09.222 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=52]
   > [2024/08/07 13:33:09.230 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 52 start_key: 7480000000000000FF3900000000000000F8 end_key: 7480000000000000FF3F00000000000000F8 region_epoch { conf_ver: 1 version: 26 } peers { id: 53 store_id: 1 }"]
   > [2024/08/07 13:33:09.230 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(50)] [region=52]
   > [2024/08/07 13:33:10.315 +00:00] [INFO] [set.go:217] ["set global var"] [conn=1946964612930863121] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/08/07 13:33:10.335 +00:00] [INFO] [set.go:217] ["set global var"] [conn=1946964612930863121] [name=transaction_isolation] [val=READ-COMMITTED]
   > [2024/08/07 13:33:11.777 +00:00] [INFO] [session.go:2469] ["CRUCIAL OPERATION"] [conn=1946964612930863123] [schemaVersion=43] [cur_db=testdb] [sql=" alter table t drop index iv;"] [user=root@127.0.0.1]
   > [2024/08/07 13:33:11.800 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:65, Type:drop index, State:none, SchemaState:none, SchemaID:61, TableID:63, RowCount:0, ArgLen:1, start time: 2024-08-07 13:33:11.777 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/07 13:33:11.800 +00:00] [INFO] [ddl.go:538] ["[ddl] start DDL job"] [job="ID:65, Type:drop index, State:none, SchemaState:none, SchemaID:61, TableID:63, RowCount:0, ArgLen:1, start time: 2024-08-07 13:33:11.777 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query=" alter table t drop index iv;"]
   > [2024/08/07 13:33:11.804 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:drop index, State:none, SchemaState:none, SchemaID:61, TableID:63, RowCount:0, ArgLen:0, start time: 2024-08-07 13:33:11.777 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:33:11.843 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=43] [neededSchemaVersion=44] ["start time"=2.420863ms] [phyTblIDs="[63]"] [actionTypes="[256]"]
   > [2024/08/07 13:33:11.892 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=44] ["take time"=61.243317ms] [job="ID:65, Type:drop index, State:running, SchemaState:write only, SchemaID:61, TableID:63, RowCount:0, ArgLen:1, start time: 2024-08-07 13:33:11.777 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:33:11.894 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:drop index, State:running, SchemaState:write only, SchemaID:61, TableID:63, RowCount:0, ArgLen:0, start time: 2024-08-07 13:33:11.777 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:33:11.931 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=44] [neededSchemaVersion=45] ["start time"=2.125501ms] [phyTblIDs="[63]"] [actionTypes="[256]"]
   > [2024/08/07 13:33:11.989 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=45] ["take time"=69.522176ms] [job="ID:65, Type:drop index, State:running, SchemaState:delete only, SchemaID:61, TableID:63, RowCount:0, ArgLen:1, start time: 2024-08-07 13:33:11.777 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:33:11.991 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:drop index, State:running, SchemaState:delete only, SchemaID:61, TableID:63, RowCount:0, ArgLen:0, start time: 2024-08-07 13:33:11.777 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:33:12.029 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=45] [neededSchemaVersion=46] ["start time"=2.204633ms] [phyTblIDs="[63]"] [actionTypes="[256]"]
   > [2024/08/07 13:33:12.077 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=46] ["take time"=61.352201ms] [job="ID:65, Type:drop index, State:running, SchemaState:delete reorganization, SchemaID:61, TableID:63, RowCount:0, ArgLen:1, start time: 2024-08-07 13:33:11.777 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:33:12.079 +00:00] [INFO] [ddl_worker.go:593] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:drop index, State:running, SchemaState:delete reorganization, SchemaID:61, TableID:63, RowCount:0, ArgLen:0, start time: 2024-08-07 13:33:11.777 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:33:12.118 +00:00] [INFO] [domain.go:136] ["diff load InfoSchema success"] [usedSchemaVersion=46] [neededSchemaVersion=47] ["start time"=2.239204ms] [phyTblIDs="[63]"] [actionTypes="[256]"]
   > [2024/08/07 13:33:12.167 +00:00] [INFO] [ddl_worker.go:796] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=47] ["take time"=61.046991ms] [job="ID:65, Type:drop index, State:done, SchemaState:none, SchemaID:61, TableID:63, RowCount:0, ArgLen:3, start time: 2024-08-07 13:33:11.777 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:33:12.170 +00:00] [INFO] [delete_range.go:421] ["[ddl] insert into delete-range table"] [jobID=65] [elementID=1]
   > [2024/08/07 13:33:12.187 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=65] [jobType="drop index"]
   > [2024/08/07 13:33:12.189 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:drop index, State:synced, SchemaState:none, SchemaID:61, TableID:63, RowCount:0, ArgLen:3, start time: 2024-08-07 13:33:11.777 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:33:12.210 +00:00] [INFO] [ddl.go:594] ["[ddl] DDL job is finished"] [jobID=65]
   > [2024/08/07 13:33:12.210 +00:00] [INFO] [domain.go:659] ["performing DDL change, must reload"]
