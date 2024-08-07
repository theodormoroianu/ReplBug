# Bug ID TIDB-23380-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/23380
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              processlist.txnstart is missing when tidb_snapshot is set


## Details
 * Database: tidb-9c48b24c.tikv
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
     - Instruction:  set tidb_snapshot=now();
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows: 0
 * Instruction #3:
     - Instruction:  begin;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows: 0
 * Instruction #4:
     - Instruction:  select txnstart from information_schema.processlist;
     - Transaction: conn_0
     - Output: [('',)]
     - Executed order: 4
     - Affected rows: 1

 * Container logs:
   > [2024/08/07 14:15:10.266 +00:00] [INFO] [session.go:2718] ["CRUCIAL OPERATION"] [conn=13] [schemaVersion=35] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/08/07 14:15:10.292 +00:00] [INFO] [ddl_worker.go:297] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:61, Type:drop schema, State:none, SchemaState:none, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-07 14:15:10.247 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/07 14:15:10.292 +00:00] [INFO] [ddl.go:535] ["[ddl] start DDL job"] [job="ID:61, Type:drop schema, State:none, SchemaState:none, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-07 14:15:10.247 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/08/07 14:15:10.296 +00:00] [INFO] [ddl_worker.go:678] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:61, Type:drop schema, State:none, SchemaState:none, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-07 14:15:10.247 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 14:15:10.335 +00:00] [INFO] [domain.go:137] ["diff load InfoSchema success"] [usedSchemaVersion=35] [neededSchemaVersion=36] ["start time"=653.305µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/07 14:15:10.401 +00:00] [INFO] [ddl_worker.go:861] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=36] ["take time"=78.195518ms] [job="ID:61, Type:drop schema, State:running, SchemaState:write only, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-07 14:15:10.247 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 14:15:10.403 +00:00] [INFO] [ddl_worker.go:678] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:61, Type:drop schema, State:running, SchemaState:write only, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-07 14:15:10.247 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 14:15:10.439 +00:00] [INFO] [domain.go:137] ["diff load InfoSchema success"] [usedSchemaVersion=36] [neededSchemaVersion=37] ["start time"=583.113µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/07 14:15:10.489 +00:00] [INFO] [ddl_worker.go:861] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=37] ["take time"=61.363606ms] [job="ID:61, Type:drop schema, State:running, SchemaState:delete only, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-07 14:15:10.247 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 14:15:10.491 +00:00] [INFO] [ddl_worker.go:678] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:61, Type:drop schema, State:running, SchemaState:delete only, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-07 14:15:10.247 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 14:15:10.525 +00:00] [INFO] [domain.go:137] ["diff load InfoSchema success"] [usedSchemaVersion=37] [neededSchemaVersion=38] ["start time"=567.678µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/07 14:15:10.575 +00:00] [INFO] [ddl_worker.go:861] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=38] ["take time"=60.774068ms] [job="ID:61, Type:drop schema, State:done, SchemaState:none, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-07 14:15:10.247 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 14:15:10.578 +00:00] [INFO] [delete_range.go:106] ["[ddl] add job into delete-range table"] [jobID=61] [jobType="drop schema"]
   > [2024/08/07 14:15:10.579 +00:00] [INFO] [ddl_worker.go:402] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:61, Type:drop schema, State:synced, SchemaState:none, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-07 14:15:10.247 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 14:15:10.602 +00:00] [INFO] [ddl.go:590] ["[ddl] DDL job is finished"] [jobID=61]
   > [2024/08/07 14:15:10.602 +00:00] [INFO] [domain.go:661] ["performing DDL change, must reload"]
   > [2024/08/07 14:15:10.605 +00:00] [INFO] [session.go:2718] ["CRUCIAL OPERATION"] [conn=13] [schemaVersion=38] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/08/07 14:15:10.648 +00:00] [INFO] [ddl_worker.go:297] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:63, Type:create schema, State:none, SchemaState:none, SchemaID:62, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-07 14:15:10.596 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/07 14:15:10.648 +00:00] [INFO] [ddl.go:535] ["[ddl] start DDL job"] [job="ID:63, Type:create schema, State:none, SchemaState:none, SchemaID:62, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-07 14:15:10.596 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/08/07 14:15:10.651 +00:00] [INFO] [ddl_worker.go:678] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:63, Type:create schema, State:none, SchemaState:none, SchemaID:62, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-07 14:15:10.596 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 14:15:10.682 +00:00] [INFO] [domain.go:137] ["diff load InfoSchema success"] [usedSchemaVersion=38] [neededSchemaVersion=39] ["start time"=1.401874ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/07 14:15:10.731 +00:00] [INFO] [ddl_worker.go:861] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=39] ["take time"=57.484289ms] [job="ID:63, Type:create schema, State:done, SchemaState:public, SchemaID:62, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-07 14:15:10.596 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 14:15:10.734 +00:00] [INFO] [ddl_worker.go:402] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:63, Type:create schema, State:synced, SchemaState:public, SchemaID:62, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-07 14:15:10.596 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 14:15:10.755 +00:00] [INFO] [ddl.go:590] ["[ddl] DDL job is finished"] [jobID=63]
   > [2024/08/07 14:15:10.755 +00:00] [INFO] [domain.go:661] ["performing DDL change, must reload"]
   > [2024/08/07 14:15:10.757 +00:00] [INFO] [session.go:2718] ["CRUCIAL OPERATION"] [conn=13] [schemaVersion=39] [cur_db=testdb] [sql="create table t (id int primary key, v int, index iv (v));"] [user=root@127.0.0.1]
   > [2024/08/07 14:15:10.800 +00:00] [INFO] [ddl_worker.go:297] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:65, Type:create table, State:none, SchemaState:none, SchemaID:62, TableID:64, RowCount:0, ArgLen:1, start time: 2024-08-07 14:15:10.747 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/07 14:15:10.800 +00:00] [INFO] [ddl.go:535] ["[ddl] start DDL job"] [job="ID:65, Type:create table, State:none, SchemaState:none, SchemaID:62, TableID:64, RowCount:0, ArgLen:1, start time: 2024-08-07 14:15:10.747 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t (id int primary key, v int, index iv (v));"]
   > [2024/08/07 14:15:10.804 +00:00] [INFO] [ddl_worker.go:678] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:create table, State:none, SchemaState:none, SchemaID:62, TableID:64, RowCount:0, ArgLen:0, start time: 2024-08-07 14:15:10.747 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 14:15:10.846 +00:00] [INFO] [domain.go:137] ["diff load InfoSchema success"] [usedSchemaVersion=39] [neededSchemaVersion=40] ["start time"=2.264355ms] [phyTblIDs="[64]"] [actionTypes="[8]"]
   > [2024/08/07 14:15:10.894 +00:00] [INFO] [ddl_worker.go:861] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=40] ["take time"=61.54366ms] [job="ID:65, Type:create table, State:done, SchemaState:public, SchemaID:62, TableID:64, RowCount:0, ArgLen:1, start time: 2024-08-07 14:15:10.747 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 14:15:10.898 +00:00] [INFO] [ddl_worker.go:402] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:create table, State:synced, SchemaState:public, SchemaID:62, TableID:64, RowCount:0, ArgLen:0, start time: 2024-08-07 14:15:10.747 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 14:15:10.923 +00:00] [INFO] [ddl.go:590] ["[ddl] DDL job is finished"] [jobID=65]
   > [2024/08/07 14:15:10.926 +00:00] [INFO] [domain.go:661] ["performing DDL change, must reload"]
   > [2024/08/07 14:15:10.926 +00:00] [INFO] [split_region.go:59] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=748000000000000040]
   > [2024/08/07 14:15:10.926 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:42562] [split_keys="key 7480000000000000FF4000000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/07 14:15:10.927 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=54] [peer-ids="[55]"]
   > [2024/08/07 14:15:10.927 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF3A00000000000000F8 region_epoch { conf_ver: 1 version: 26 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 54 new_peer_ids: 55]"] [region_id=2]
   > [2024/08/07 14:15:10.937 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF4000000000000000F8 new_region_id: 54 new_peer_ids: 55 } right_derive: true }"] [index=64] [term=6] [peer_id=3] [region_id=2]
   > [2024/08/07 14:15:10.937 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF4000000000000000F8"] [region="id: 2 start_key: 7480000000000000FF3A00000000000000F8 region_epoch { conf_ver: 1 version: 26 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/08/07 14:15:10.948 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/08/07 14:15:10.948 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=2]
   > [2024/08/07 14:15:10.948 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/08/07 14:15:10.948 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(49)] [region_id=2] [store_id=Some(1)]
   > [2024/08/07 14:15:10.948 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF4000000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 3 store_id: 1 }"]
   > [2024/08/07 14:15:10.948 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 54 start_key: 7480000000000000FF3A00000000000000F8 end_key: 7480000000000000FF4000000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 55 store_id: 1 }"] [region_id=54]
   > [2024/08/07 14:15:10.948 +00:00] [INFO] [split_region.go:160] ["batch split regions complete"] ["batch region ID"=2] ["first at"=748000000000000040] ["first new region left"="{Id:54 StartKey:7480000000000000ff3a00000000000000f8 EndKey:7480000000000000ff4000000000000000f8 RegionEpoch:{ConfVer:1 Version:27} Peers:[id:55 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/08/07 14:15:10.949 +00:00] [INFO] [split_region.go:204] ["split regions complete"] ["region count"=1] ["region IDs"="[54]"]
   > [2024/08/07 14:15:10.948 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=55] [region_id=54]
   > [2024/08/07 14:15:10.949 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF3A00000000000000F8} -> {7480000000000000FF4000000000000000F8}, EndKey:{}"] [old-version=26] [new-version=27]
   > [2024/08/07 14:15:10.949 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 2 start_key: 7480000000000000FF4000000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 3 store_id: 1 } }"]
   > [2024/08/07 14:15:10.949 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 2 start_key: 7480000000000000FF4000000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 3 store_id: 1 }"]
   > [2024/08/07 14:15:10.949 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=2] [origin="id:54 start_key:\"7480000000000000FF3A00000000000000F8\" end_key:\"7480000000000000FF4000000000000000F8\" region_epoch:<conf_ver:1 version:27 > peers:<id:55 store_id:1 >"] [total=1]
   > [2024/08/07 14:15:10.949 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {55} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=55] [region_id=54]
   > [2024/08/07 14:15:10.949 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=55] [region_id=54]
   > [2024/08/07 14:15:10.949 +00:00] [WARN] [2pc.go:1382] ["schemaLeaseChecker is not set for this transaction"] [conn=13] [sessionID=13] [startTS=451684626830721031] [commitTS=451684626843828225]
   > [2024/08/07 14:15:10.949 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {55} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=55] [region_id=54]
   > [2024/08/07 14:15:10.949 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 55."] [id=55] [raft_id=55] [region_id=54]
   > [2024/08/07 14:15:10.949 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=55] [region_id=54]
   > [2024/08/07 14:15:10.949 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=55] [region_id=54]
   > [2024/08/07 14:15:10.949 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=55] [region_id=54]
   > [2024/08/07 14:15:10.949 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=55] [region_id=54]
   > [2024/08/07 14:15:10.949 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803830] [region_id=54]
   > [2024/08/07 14:15:10.950 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=64] [observe_id=ObserveId(51)] [region=2]
   > [2024/08/07 14:15:10.950 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=54]
   > [2024/08/07 14:15:10.959 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 54 start_key: 7480000000000000FF3A00000000000000F8 end_key: 7480000000000000FF4000000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 55 store_id: 1 }"]
   > [2024/08/07 14:15:10.960 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(52)] [region=54]
   > [2024/08/07 14:15:10.971 +00:00] [INFO] [scheduler.rs:640] ["get snapshot failed"] [err="Error(Request(message: \"EpochNotMatch current epoch of region 2 is conf_ver: 1 version: 27, but you sent conf_ver: 1 version: 26\" epoch_not_match { current_regions { id: 2 start_key: 7480000000000000FF4000000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 3 store_id: 1 } } current_regions { id: 54 start_key: 7480000000000000FF3A00000000000000F8 end_key: 7480000000000000FF4000000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 55 store_id: 1 } } }))"] [cid=379]
   > [2024/08/07 14:15:12.050 +00:00] [INFO] [set.go:209] ["set global var"] [conn=15] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/08/07 14:15:12.070 +00:00] [INFO] [set.go:209] ["set global var"] [conn=15] [name=transaction_isolation] [val=READ-COMMITTED]
   > [2024/08/07 14:15:12.601 +00:00] [INFO] [set.go:312] ["load snapshot info schema"] [conn=15] [SnapshotTS=451684627120128000]
   > [2024/08/07 14:15:12.620 +00:00] [INFO] [domain.go:161] ["full load InfoSchema success"] [usedSchemaVersion=0] [neededSchemaVersion=40] ["start time"=18.43081ms]
   > [2024/08/07 14:15:12.899 +00:00] [INFO] [infoschema.go:401] ["use snapshot schema"] [conn=15] [schemaVersion=40]
   > [2024/08/07 14:15:13.199 +00:00] [INFO] [infoschema.go:401] ["use snapshot schema"] [conn=15] [schemaVersion=40]
   > [2024/08/07 14:15:13.200 +00:00] [INFO] [infoschema.go:401] ["use snapshot schema"] [conn=15] [schemaVersion=40]
