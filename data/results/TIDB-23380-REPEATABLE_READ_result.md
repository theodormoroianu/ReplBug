# Bug ID TIDB-23380-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/23380
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              processlist.txnstart is missing when tidb_snapshot is set


## Details
 * Database: tidb-9c48b24c.tikv
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
   > [2024/08/07 14:15:05.317 +00:00] [INFO] [session.go:2718] ["CRUCIAL OPERATION"] [conn=7] [schemaVersion=25] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/08/07 14:15:05.318 +00:00] [INFO] [session.go:2718] ["CRUCIAL OPERATION"] [conn=7] [schemaVersion=25] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/08/07 14:15:05.357 +00:00] [INFO] [ddl_worker.go:297] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:52, Type:create schema, State:none, SchemaState:none, SchemaID:51, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-07 14:15:05.297 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/07 14:15:05.357 +00:00] [INFO] [ddl.go:535] ["[ddl] start DDL job"] [job="ID:52, Type:create schema, State:none, SchemaState:none, SchemaID:51, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-07 14:15:05.297 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/08/07 14:15:05.361 +00:00] [INFO] [ddl_worker.go:678] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:52, Type:create schema, State:none, SchemaState:none, SchemaID:51, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-07 14:15:05.297 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 14:15:05.393 +00:00] [INFO] [domain.go:137] ["diff load InfoSchema success"] [usedSchemaVersion=25] [neededSchemaVersion=26] ["start time"=1.582276ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/07 14:15:05.441 +00:00] [INFO] [ddl_worker.go:861] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=26] ["take time"=60.025779ms] [job="ID:52, Type:create schema, State:done, SchemaState:public, SchemaID:51, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-07 14:15:05.297 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 14:15:05.444 +00:00] [INFO] [ddl_worker.go:402] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:52, Type:create schema, State:synced, SchemaState:public, SchemaID:51, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-07 14:15:05.297 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 14:15:05.465 +00:00] [INFO] [ddl.go:590] ["[ddl] DDL job is finished"] [jobID=52]
   > [2024/08/07 14:15:05.465 +00:00] [INFO] [domain.go:661] ["performing DDL change, must reload"]
   > [2024/08/07 14:15:05.469 +00:00] [INFO] [session.go:2718] ["CRUCIAL OPERATION"] [conn=7] [schemaVersion=26] [cur_db=testdb] [sql="create table t (id int primary key, v int, index iv (v));"] [user=root@127.0.0.1]
   > [2024/08/07 14:15:05.508 +00:00] [INFO] [ddl_worker.go:297] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:54, Type:create table, State:none, SchemaState:none, SchemaID:51, TableID:53, RowCount:0, ArgLen:1, start time: 2024-08-07 14:15:05.447 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/07 14:15:05.508 +00:00] [INFO] [ddl.go:535] ["[ddl] start DDL job"] [job="ID:54, Type:create table, State:none, SchemaState:none, SchemaID:51, TableID:53, RowCount:0, ArgLen:1, start time: 2024-08-07 14:15:05.447 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t (id int primary key, v int, index iv (v));"]
   > [2024/08/07 14:15:05.512 +00:00] [INFO] [ddl_worker.go:678] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:54, Type:create table, State:none, SchemaState:none, SchemaID:51, TableID:53, RowCount:0, ArgLen:0, start time: 2024-08-07 14:15:05.447 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 14:15:05.563 +00:00] [INFO] [domain.go:137] ["diff load InfoSchema success"] [usedSchemaVersion=26] [neededSchemaVersion=27] ["start time"=2.675168ms] [phyTblIDs="[53]"] [actionTypes="[8]"]
   > [2024/08/07 14:15:05.611 +00:00] [INFO] [ddl_worker.go:861] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=27] ["take time"=61.653243ms] [job="ID:54, Type:create table, State:done, SchemaState:public, SchemaID:51, TableID:53, RowCount:0, ArgLen:1, start time: 2024-08-07 14:15:05.447 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 14:15:05.615 +00:00] [INFO] [ddl_worker.go:402] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:54, Type:create table, State:synced, SchemaState:public, SchemaID:51, TableID:53, RowCount:0, ArgLen:0, start time: 2024-08-07 14:15:05.447 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 14:15:05.662 +00:00] [INFO] [ddl.go:590] ["[ddl] DDL job is finished"] [jobID=54]
   > [2024/08/07 14:15:05.664 +00:00] [INFO] [domain.go:661] ["performing DDL change, must reload"]
   > [2024/08/07 14:15:05.664 +00:00] [INFO] [split_region.go:59] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=748000000000000035]
   > [2024/08/07 14:15:05.665 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:42530] [split_keys="key 7480000000000000FF3500000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/07 14:15:05.665 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=50] [peer-ids="[51]"]
   > [2024/08/07 14:15:05.665 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF3100000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 50 new_peer_ids: 51]"] [region_id=2]
   > [2024/08/07 14:15:05.678 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF3500000000000000F8 new_region_id: 50 new_peer_ids: 51 } right_derive: true }"] [index=59] [term=6] [peer_id=3] [region_id=2]
   > [2024/08/07 14:15:05.678 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF3500000000000000F8"] [region="id: 2 start_key: 7480000000000000FF3100000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/08/07 14:15:05.688 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=2]
   > [2024/08/07 14:15:05.689 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/08/07 14:15:05.689 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(45)] [region_id=2] [store_id=Some(1)]
   > [2024/08/07 14:15:05.689 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF3500000000000000F8 region_epoch { conf_ver: 1 version: 25 } peers { id: 3 store_id: 1 }"]
   > [2024/08/07 14:15:05.689 +00:00] [INFO] [split_region.go:160] ["batch split regions complete"] ["batch region ID"=2] ["first at"=748000000000000035] ["first new region left"="{Id:50 StartKey:7480000000000000ff3100000000000000f8 EndKey:7480000000000000ff3500000000000000f8 RegionEpoch:{ConfVer:1 Version:25} Peers:[id:51 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/08/07 14:15:05.689 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/08/07 14:15:05.689 +00:00] [INFO] [split_region.go:204] ["split regions complete"] ["region count"=1] ["region IDs"="[50]"]
   > [2024/08/07 14:15:05.689 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 50 start_key: 7480000000000000FF3100000000000000F8 end_key: 7480000000000000FF3500000000000000F8 region_epoch { conf_ver: 1 version: 25 } peers { id: 51 store_id: 1 }"] [region_id=50]
   > [2024/08/07 14:15:05.689 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=51] [region_id=50]
   > [2024/08/07 14:15:05.689 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF3100000000000000F8} -> {7480000000000000FF3500000000000000F8}, EndKey:{}"] [old-version=24] [new-version=25]
   > [2024/08/07 14:15:05.689 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 2 start_key: 7480000000000000FF3500000000000000F8 region_epoch { conf_ver: 1 version: 25 } peers { id: 3 store_id: 1 } }"]
   > [2024/08/07 14:15:05.689 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=2] [origin="id:50 start_key:\"7480000000000000FF3100000000000000F8\" end_key:\"7480000000000000FF3500000000000000F8\" region_epoch:<conf_ver:1 version:25 > peers:<id:51 store_id:1 >"] [total=1]
   > [2024/08/07 14:15:05.689 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 2 start_key: 7480000000000000FF3500000000000000F8 region_epoch { conf_ver: 1 version: 25 } peers { id: 3 store_id: 1 }"]
   > [2024/08/07 14:15:05.698 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {51} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=51] [region_id=50]
   > [2024/08/07 14:15:05.698 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=51] [region_id=50]
   > [2024/08/07 14:15:05.698 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {51} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=51] [region_id=50]
   > [2024/08/07 14:15:05.698 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 51."] [id=51] [raft_id=51] [region_id=50]
   > [2024/08/07 14:15:05.698 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=51] [region_id=50]
   > [2024/08/07 14:15:05.698 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=51] [region_id=50]
   > [2024/08/07 14:15:05.698 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=51] [region_id=50]
   > [2024/08/07 14:15:05.699 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=51] [region_id=50]
   > [2024/08/07 14:15:05.699 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803826] [region_id=50]
   > [2024/08/07 14:15:05.699 +00:00] [WARN] [2pc.go:1382] ["schemaLeaseChecker is not set for this transaction"] [conn=7] [sessionID=7] [startTS=451684625454727174] [commitTS=451684625467834370]
   > [2024/08/07 14:15:05.699 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=59] [observe_id=ObserveId(47)] [region=2]
   > [2024/08/07 14:15:05.699 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=50]
   > [2024/08/07 14:15:05.717 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 50 start_key: 7480000000000000FF3100000000000000F8 end_key: 7480000000000000FF3500000000000000F8 region_epoch { conf_ver: 1 version: 25 } peers { id: 51 store_id: 1 }"]
   > [2024/08/07 14:15:05.717 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(48)] [region=50]
   > [2024/08/07 14:15:05.728 +00:00] [INFO] [scheduler.rs:640] ["get snapshot failed"] [err="Error(Request(message: \"EpochNotMatch current epoch of region 2 is conf_ver: 1 version: 25, but you sent conf_ver: 1 version: 24\" epoch_not_match { current_regions { id: 2 start_key: 7480000000000000FF3500000000000000F8 region_epoch { conf_ver: 1 version: 25 } peers { id: 3 store_id: 1 } } current_regions { id: 50 start_key: 7480000000000000FF3100000000000000F8 end_key: 7480000000000000FF3500000000000000F8 region_epoch { conf_ver: 1 version: 25 } peers { id: 51 store_id: 1 } } }))"] [cid=287]
   > [2024/08/07 14:15:06.773 +00:00] [INFO] [set.go:209] ["set global var"] [conn=9] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/08/07 14:15:06.775 +00:00] [INFO] [set.go:209] ["set global var"] [conn=9] [name=transaction_isolation] [val=REPEATABLE-READ]
   > [2024/08/07 14:15:07.363 +00:00] [INFO] [set.go:312] ["load snapshot info schema"] [conn=9] [SnapshotTS=451684625809408000]
   > [2024/08/07 14:15:07.381 +00:00] [INFO] [domain.go:161] ["full load InfoSchema success"] [usedSchemaVersion=0] [neededSchemaVersion=27] ["start time"=17.576081ms]
   > [2024/08/07 14:15:07.443 +00:00] [INFO] [cluster.go:1469] ["store has changed to serving"] [store-id=1] [store-address=127.0.0.1:20160]
   > [2024/08/07 14:15:07.492 +00:00] [INFO] [client.rs:789] ["set cluster version to 6.4.0"]
   > [2024/08/07 14:15:07.660 +00:00] [INFO] [infoschema.go:401] ["use snapshot schema"] [conn=9] [schemaVersion=27]
   > [2024/08/07 14:15:07.961 +00:00] [INFO] [infoschema.go:401] ["use snapshot schema"] [conn=9] [schemaVersion=27]
   > [2024/08/07 14:15:07.962 +00:00] [INFO] [infoschema.go:401] ["use snapshot schema"] [conn=9] [schemaVersion=27]
