# Bug ID TIDB-20975-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/20975
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              Unexpected "Information schema is changed" when commits


## Details
 * Database: tidb-fa6baa9f.tikv
 * Number of scenarios: 2
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 0 / 0
 * Instruction #1:
     - Instruction:  begin pessimistic;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  update t1 set a=a;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 0 / 0
 * Instruction #3:
     - Instruction:  create table t2(a int);
     - Transaction: conn_1
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 0 / 0
 * Instruction #4:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: ERROR: 8028 (HY000): Information schema is changed during the execution of the statement(for example, table definition may be updated by other DDL ran in parallel). If you see this error often, try increasing `tidb_max_delta_schema_count`. [try again later]
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0

 * Container logs:
   > [2024/07/23 15:31:58.667 +00:00] [INFO] [session.go:2271] ["CRUCIAL OPERATION"] [conn=3] [schemaVersion=24] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.19]
   > [2024/07/23 15:31:58.668 +00:00] [INFO] [session.go:2271] ["CRUCIAL OPERATION"] [conn=3] [schemaVersion=24] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.19]
   > [2024/07/23 15:31:58.682 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:50, Type:create schema, State:none, SchemaState:none, SchemaID:49, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 15:31:58.638 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/23 15:31:58.683 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:50, Type:create schema, State:none, SchemaState:none, SchemaID:49, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 15:31:58.638 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/23 15:31:58.686 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:50, Type:create schema, State:none, SchemaState:none, SchemaID:49, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:31:58.638 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:31:58.700 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=24] [neededSchemaVersion=25] ["start time"=1.386574ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 15:31:58.749 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=25] ["take time"=53.482234ms] [job="ID:50, Type:create schema, State:done, SchemaState:public, SchemaID:49, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 15:31:58.638 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:31:58.753 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:50, Type:create schema, State:synced, SchemaState:public, SchemaID:49, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:31:58.638 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:31:58.763 +00:00] [INFO] [ddl.go:517] ["[ddl] DDL job is finished"] [jobID=50]
   > [2024/07/23 15:31:58.763 +00:00] [INFO] [domain.go:646] ["performing DDL change, must reload"]
   > [2024/07/23 15:31:58.766 +00:00] [INFO] [session.go:2271] ["CRUCIAL OPERATION"] [conn=3] [schemaVersion=25] [cur_db=testdb] [sql="create table t1(a int);"] [user=root@10.88.0.19]
   > [2024/07/23 15:31:58.785 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:52, Type:create table, State:none, SchemaState:none, SchemaID:49, TableID:51, RowCount:0, ArgLen:1, start time: 2024-07-23 15:31:58.739 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/23 15:31:58.785 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:52, Type:create table, State:none, SchemaState:none, SchemaID:49, TableID:51, RowCount:0, ArgLen:1, start time: 2024-07-23 15:31:58.739 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t1(a int);"]
   > [2024/07/23 15:31:58.789 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:52, Type:create table, State:none, SchemaState:none, SchemaID:49, TableID:51, RowCount:0, ArgLen:0, start time: 2024-07-23 15:31:58.739 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:31:58.809 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=25] [neededSchemaVersion=26] ["start time"=1.921564ms] [phyTblIDs="[51]"] [actionTypes="[8]"]
   > [2024/07/23 15:31:58.857 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=26] ["take time"=53.706426ms] [job="ID:52, Type:create table, State:done, SchemaState:public, SchemaID:49, TableID:51, RowCount:0, ArgLen:1, start time: 2024-07-23 15:31:58.739 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:31:58.860 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:52, Type:create table, State:synced, SchemaState:public, SchemaID:49, TableID:51, RowCount:0, ArgLen:0, start time: 2024-07-23 15:31:58.739 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:31:58.870 +00:00] [INFO] [ddl.go:517] ["[ddl] DDL job is finished"] [jobID=52]
   > [2024/07/23 15:31:58.872 +00:00] [INFO] [domain.go:646] ["performing DDL change, must reload"]
   > [2024/07/23 15:31:58.872 +00:00] [INFO] [split_region.go:61] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=748000000000000033]
   > [2024/07/23 15:31:58.873 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:32934] [split_keys="key 7480000000000000FF3300000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/23 15:31:58.873 +00:00] [INFO] [peer.rs:5566] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 22"] [prev_epoch="conf_ver: 1 version: 23"] [peer_id=3] [region_id=2]
   > [2024/07/23 15:31:58.876 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:32906] [split_keys="key 7480000000000000FF3300000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/23 15:31:58.877 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=48] [peer-ids="[49]"]
   > [2024/07/23 15:31:58.877 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 23 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 48 new_peer_ids: 49]"] [region_id=2]
   > [2024/07/23 15:31:58.879 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF3300000000000000F8 new_region_id: 48 new_peer_ids: 49 } right_derive: true }"] [index=56] [term=6] [peer_id=3] [region_id=2]
   > [2024/07/23 15:31:58.880 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF3300000000000000F8"] [region="id: 2 start_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 23 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/07/23 15:31:58.883 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/23 15:31:58.884 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=2]
   > [2024/07/23 15:31:58.884 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(43)] [region_id=2] [store_id=Some(1)]
   > [2024/07/23 15:31:58.884 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/07/23 15:31:58.884 +00:00] [INFO] [split_region.go:158] ["batch split regions complete"] ["batch region ID"=2] ["first at"=748000000000000033] ["first new region left"="{Id:48 StartKey:7480000000000000ff2f00000000000000f8 EndKey:7480000000000000ff3300000000000000f8 RegionEpoch:{ConfVer:1 Version:24} Peers:[id:49 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/23 15:31:58.884 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF3300000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 3 store_id: 1 }"]
   > [2024/07/23 15:31:58.884 +00:00] [INFO] [split_region.go:207] ["split regions complete"] ["region count"=1] ["region IDs"="[48]"]
   > [2024/07/23 15:31:58.884 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 48 start_key: 7480000000000000FF2F00000000000000F8 end_key: 7480000000000000FF3300000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 49 store_id: 1 }"] [region_id=48]
   > [2024/07/23 15:31:58.884 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF2F00000000000000F8} -> {7480000000000000FF3300000000000000F8}, EndKey:{}"] [old-version=23] [new-version=24]
   > [2024/07/23 15:31:58.884 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=49] [region_id=48]
   > [2024/07/23 15:31:58.884 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 2 start_key: 7480000000000000FF3300000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 3 store_id: 1 } }"]
   > [2024/07/23 15:31:58.884 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=2] [origin="id:48 start_key:\"7480000000000000FF2F00000000000000F8\" end_key:\"7480000000000000FF3300000000000000F8\" region_epoch:<conf_ver:1 version:24 > peers:<id:49 store_id:1 >"] [total=1]
   > [2024/07/23 15:31:58.884 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 2 start_key: 7480000000000000FF3300000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 3 store_id: 1 }"]
   > [2024/07/23 15:31:58.884 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {49} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=49] [region_id=48]
   > [2024/07/23 15:31:58.884 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=49] [region_id=48]
   > [2024/07/23 15:31:58.884 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {49} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=49] [region_id=48]
   > [2024/07/23 15:31:58.885 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 49."] [id=49] [raft_id=49] [region_id=48]
   > [2024/07/23 15:31:58.885 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=49] [region_id=48]
   > [2024/07/23 15:31:58.885 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=49] [region_id=48]
   > [2024/07/23 15:31:58.885 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=49] [region_id=48]
   > [2024/07/23 15:31:58.885 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=49] [region_id=48]
   > [2024/07/23 15:31:58.885 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803824] [region_id=48]
   > [2024/07/23 15:31:58.885 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=56] [observe_id=ObserveId(45)] [region=2]
   > [2024/07/23 15:31:58.885 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=48]
   > [2024/07/23 15:31:58.886 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 48 start_key: 7480000000000000FF2F00000000000000F8 end_key: 7480000000000000FF3300000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 49 store_id: 1 }"]
   > [2024/07/23 15:31:58.886 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(46)] [region=48]
   > [2024/07/23 15:31:58.889 +00:00] [INFO] [scheduler.rs:640] ["get snapshot failed"] [err="Error(Request(message: \"EpochNotMatch current epoch of region 2 is conf_ver: 1 version: 24, but you sent conf_ver: 1 version: 23\" epoch_not_match { current_regions { id: 2 start_key: 7480000000000000FF3300000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 3 store_id: 1 } } current_regions { id: 48 start_key: 7480000000000000FF2F00000000000000F8 end_key: 7480000000000000FF3300000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 49 store_id: 1 } } }))"] [cid=270]
   > [2024/07/23 15:31:59.923 +00:00] [INFO] [set.go:216] ["set global var"] [conn=4] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/07/23 15:31:59.925 +00:00] [INFO] [set.go:216] ["set global var"] [conn=4] [name=transaction_isolation] [val=REPEATABLE-READ]
   > [2024/07/23 15:32:00.837 +00:00] [INFO] [session.go:2271] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=26] [cur_db=testdb] [sql=" create table t2(a int);"] [user=root@10.88.0.19]
   > [2024/07/23 15:32:00.855 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:54, Type:create table, State:none, SchemaState:none, SchemaID:49, TableID:53, RowCount:0, ArgLen:1, start time: 2024-07-23 15:32:00.839 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/23 15:32:00.855 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:54, Type:create table, State:none, SchemaState:none, SchemaID:49, TableID:53, RowCount:0, ArgLen:1, start time: 2024-07-23 15:32:00.839 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query=" create table t2(a int);"]
   > [2024/07/23 15:32:00.859 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:54, Type:create table, State:none, SchemaState:none, SchemaID:49, TableID:53, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:00.839 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:00.879 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=26] [neededSchemaVersion=27] ["start time"=2.26358ms] [phyTblIDs="[53]"] [actionTypes="[8]"]
   > [2024/07/23 15:32:00.927 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=27] ["take time"=54.365456ms] [job="ID:54, Type:create table, State:done, SchemaState:public, SchemaID:49, TableID:53, RowCount:0, ArgLen:1, start time: 2024-07-23 15:32:00.839 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:00.931 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:54, Type:create table, State:synced, SchemaState:public, SchemaID:49, TableID:53, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:00.839 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:00.941 +00:00] [INFO] [ddl.go:517] ["[ddl] DDL job is finished"] [jobID=54]
   > [2024/07/23 15:32:00.944 +00:00] [INFO] [domain.go:646] ["performing DDL change, must reload"]
   > [2024/07/23 15:32:00.944 +00:00] [INFO] [split_region.go:61] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=748000000000000035]
   > [2024/07/23 15:32:00.944 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:32912] [split_keys="key 7480000000000000FF3500000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/23 15:32:00.945 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=50] [peer-ids="[51]"]
   > [2024/07/23 15:32:00.945 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF3300000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 50 new_peer_ids: 51]"] [region_id=2]
   > [2024/07/23 15:32:00.947 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF3500000000000000F8 new_region_id: 50 new_peer_ids: 51 } right_derive: true }"] [index=60] [term=6] [peer_id=3] [region_id=2]
   > [2024/07/23 15:32:00.948 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF3500000000000000F8"] [region="id: 2 start_key: 7480000000000000FF3300000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/07/23 15:32:00.950 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/23 15:32:00.950 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=2]
   > [2024/07/23 15:32:00.950 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/07/23 15:32:00.950 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(45)] [region_id=2] [store_id=Some(1)]
   > [2024/07/23 15:32:00.950 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF3500000000000000F8 region_epoch { conf_ver: 1 version: 25 } peers { id: 3 store_id: 1 }"]
   > [2024/07/23 15:32:00.950 +00:00] [INFO] [split_region.go:158] ["batch split regions complete"] ["batch region ID"=2] ["first at"=748000000000000035] ["first new region left"="{Id:50 StartKey:7480000000000000ff3300000000000000f8 EndKey:7480000000000000ff3500000000000000f8 RegionEpoch:{ConfVer:1 Version:25} Peers:[id:51 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/23 15:32:00.950 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 50 start_key: 7480000000000000FF3300000000000000F8 end_key: 7480000000000000FF3500000000000000F8 region_epoch { conf_ver: 1 version: 25 } peers { id: 51 store_id: 1 }"] [region_id=50]
   > [2024/07/23 15:32:00.950 +00:00] [INFO] [split_region.go:207] ["split regions complete"] ["region count"=1] ["region IDs"="[50]"]
   > [2024/07/23 15:32:00.950 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=51] [region_id=50]
   > [2024/07/23 15:32:00.950 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 2 start_key: 7480000000000000FF3500000000000000F8 region_epoch { conf_ver: 1 version: 25 } peers { id: 3 store_id: 1 } }"]
   > [2024/07/23 15:32:00.951 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 2 start_key: 7480000000000000FF3500000000000000F8 region_epoch { conf_ver: 1 version: 25 } peers { id: 3 store_id: 1 }"]
   > [2024/07/23 15:32:00.951 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF3300000000000000F8} -> {7480000000000000FF3500000000000000F8}, EndKey:{}"] [old-version=24] [new-version=25]
   > [2024/07/23 15:32:00.951 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {51} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=51] [region_id=50]
   > [2024/07/23 15:32:00.951 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=2] [origin="id:50 start_key:\"7480000000000000FF3300000000000000F8\" end_key:\"7480000000000000FF3500000000000000F8\" region_epoch:<conf_ver:1 version:25 > peers:<id:51 store_id:1 >"] [total=1]
   > [2024/07/23 15:32:00.951 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=51] [region_id=50]
   > [2024/07/23 15:32:00.951 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {51} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=51] [region_id=50]
   > [2024/07/23 15:32:00.951 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 51."] [id=51] [raft_id=51] [region_id=50]
   > [2024/07/23 15:32:00.951 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=51] [region_id=50]
   > [2024/07/23 15:32:00.951 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=51] [region_id=50]
   > [2024/07/23 15:32:00.951 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=51] [region_id=50]
   > [2024/07/23 15:32:00.951 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=51] [region_id=50]
   > [2024/07/23 15:32:00.951 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803826] [region_id=50]
   > [2024/07/23 15:32:00.951 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=60] [observe_id=ObserveId(47)] [region=2]
   > [2024/07/23 15:32:00.952 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=50]
   > [2024/07/23 15:32:00.953 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 50 start_key: 7480000000000000FF3300000000000000F8 end_key: 7480000000000000FF3500000000000000F8 region_epoch { conf_ver: 1 version: 25 } peers { id: 51 store_id: 1 }"]
   > [2024/07/23 15:32:00.954 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(48)] [region=50]
   > [2024/07/23 15:32:01.127 +00:00] [INFO] [scheduler.rs:640] ["get snapshot failed"] [err="Error(Request(message: \"EpochNotMatch current epoch of region 2 is conf_ver: 1 version: 25, but you sent conf_ver: 1 version: 24\" epoch_not_match { current_regions { id: 2 start_key: 7480000000000000FF3500000000000000F8 region_epoch { conf_ver: 1 version: 25 } peers { id: 3 store_id: 1 } } current_regions { id: 50 start_key: 7480000000000000FF3300000000000000F8 end_key: 7480000000000000FF3500000000000000F8 region_epoch { conf_ver: 1 version: 25 } peers { id: 51 store_id: 1 } } }))"] [cid=288]
   > [2024/07/23 15:32:01.140 +00:00] [INFO] [schema_validator.go:232] ["the related physical table ID is empty"] [schemaVer=26] [latestSchemaVer=27]
   > [2024/07/23 15:32:01.140 +00:00] [WARN] [session.go:490] ["can not retry txn"] [conn=4] [label=general] [error="[domain:8028]Information schema is changed during the execution of the statement(for example, table definition may be updated by other DDL ran in parallel). If you see this error often, try increasing `tidb_max_delta_schema_count`. [try again later]"] [IsBatchInsert=false] [IsPessimistic=true] [InRestrictedSQL=false] [tidb_retry_limit=10] [tidb_disable_txn_auto_retry=true]
   > [2024/07/23 15:32:01.140 +00:00] [WARN] [session.go:506] ["commit failed"] [conn=4] ["finished txn"="Txn{state=invalid}"] [error="[domain:8028]Information schema is changed during the execution of the statement(for example, table definition may be updated by other DDL ran in parallel). If you see this error often, try increasing `tidb_max_delta_schema_count`. [try again later]"]
   > [2024/07/23 15:32:01.140 +00:00] [WARN] [session.go:1175] ["run statement failed"] [conn=4] [schemaVersion=26] [error="previous statement:  update t1 set a=a;: [domain:8028]Information schema is changed during the execution of the statement(for example, table definition may be updated by other DDL ran in parallel). If you see this error often, try increasing `tidb_max_delta_schema_count`. [try again later]"] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 4,\n  \"status\": 2,\n  \"strictMode\": true,\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"10.88.0.19\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/07/23 15:32:01.140 +00:00] [INFO] [conn.go:793] ["command dispatched failed"] [conn=4] [connInfo="id:4, addr:10.88.0.19:60406 status:10, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:0, autocommit:1"] [sql=" commit;"] [txn_mode=PESSIMISTIC] [err="[domain:8028]Information schema is changed during the execution of the statement(for example, table definition may be updated by other DDL ran in parallel). If you see this error often, try increasing `tidb_max_delta_schema_count`. [try again later]\ngithub.com/pingcap/errors.AddStack\n\t/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.20200902104258-eba4f1d8f6de/errors.go:174\ngithub.com/pingcap/errors.Trace\n\t/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.20200902104258-eba4f1d8f6de/juju_adaptor.go:15\ngithub.com/pingcap/tidb/store/tikv.(*twoPhaseCommitter).checkSchemaValid\n\t/go/src/github.com/pingcap/tidb/store/tikv/2pc.go:1037\ngithub.com/pingcap/tidb/store/tikv.(*twoPhaseCommitter).execute\n\t/go/src/github.com/pingcap/tidb/store/tikv/2pc.go:831\ngithub.com/pingcap/tidb/store/tikv.(*tikvTxn).Commit\n\t/go/src/github.com/pingcap/tidb/store/tikv/txn.go:274\ngithub.com/pingcap/tidb/session.(*TxnState).Commit\n\t/go/src/github.com/pingcap/tidb/session/txn.go:244\ngithub.com/pingcap/tidb/session.(*session).doCommit\n\t/go/src/github.com/pingcap/tidb/session/session.go:450\ngithub.com/pingcap/tidb/session.(*session).doCommitWithRetry\n\t/go/src/github.com/pingcap/tidb/session/session.go:470\ngithub.com/pingcap/tidb/session.(*session).CommitTxn\n\t/go/src/github.com/pingcap/tidb/session/session.go:529\ngithub.com/pingcap/tidb/session.autoCommitAfterStmt\n\t/go/src/github.com/pingcap/tidb/session/tidb.go:229\ngithub.com/pingcap/tidb/session.finishStmt\n\t/go/src/github.com/pingcap/tidb/session/tidb.go:195\ngithub.com/pingcap/tidb/session.runStmt\n\t/go/src/github.com/pingcap/tidb/session/session.go:1232\ngithub.com/pingcap/tidb/session.(*session).ExecuteStmt\n\t/go/src/github.com/pingcap/tidb/session/session.go:1172\ngithub.com/pingcap/tidb/server.(*TiDBContext).ExecuteStmt\n\t/go/src/github.com/pingcap/tidb/server/driver_tidb.go:198\ngithub.com/pingcap/tidb/server.(*clientConn).handleStmt\n\t/go/src/github.com/pingcap/tidb/server/conn.go:1505\ngithub.com/pingcap/tidb/server.(*clientConn).handleQuery\n\t/go/src/github.com/pingcap/tidb/server/conn.go:1397\ngithub.com/pingcap/tidb/server.(*clientConn).dispatch\n\t/go/src/github.com/pingcap/tidb/server/conn.go:984\ngithub.com/pingcap/tidb/server.(*clientConn).Run\n\t/go/src/github.com/pingcap/tidb/server/conn.go:776\ngithub.com/pingcap/tidb/server.(*Server).onConn\n\t/go/src/github.com/pingcap/tidb/server/server.go:421\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1594\nprevious statement:  update t1 set a=a;"]
   > [2024/07/23 15:32:01.144 +00:00] [INFO] [2pc.go:725] ["2PC clean up done"] [conn=4] [txnStartTS=451346096505225217]

### Scenario 1
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 0 / 0
 * Instruction #1:
     - Instruction:  update t1 set a=a;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  create table t2(a int);
     - Transaction: conn_1
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 0 / 0

 * Container logs:
   > [2024/07/23 15:32:03.025 +00:00] [INFO] [session.go:2271] ["CRUCIAL OPERATION"] [conn=7] [schemaVersion=35] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.19]
   > [2024/07/23 15:32:03.048 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:61, Type:drop schema, State:none, SchemaState:none, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:02.989 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/23 15:32:03.048 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:61, Type:drop schema, State:none, SchemaState:none, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:02.989 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/23 15:32:03.052 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:61, Type:drop schema, State:none, SchemaState:none, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:02.989 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:03.067 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=35] [neededSchemaVersion=36] ["start time"=541.975µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 15:32:03.119 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=36] ["take time"=56.756079ms] [job="ID:61, Type:drop schema, State:running, SchemaState:write only, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:02.989 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:03.123 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:61, Type:drop schema, State:running, SchemaState:write only, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:02.989 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:03.144 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=36] [neededSchemaVersion=37] ["start time"=815.824µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 15:32:03.190 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=37] ["take time"=54.184076ms] [job="ID:61, Type:drop schema, State:running, SchemaState:delete only, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:02.989 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:03.192 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:61, Type:drop schema, State:running, SchemaState:delete only, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:02.989 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:03.205 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=37] [neededSchemaVersion=38] ["start time"=1.645548ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 15:32:03.254 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=38] ["take time"=53.346531ms] [job="ID:61, Type:drop schema, State:done, SchemaState:none, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:02.989 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:03.256 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=61] [jobType="drop schema"]
   > [2024/07/23 15:32:03.257 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:61, Type:drop schema, State:synced, SchemaState:none, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:02.989 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:03.266 +00:00] [INFO] [ddl.go:517] ["[ddl] DDL job is finished"] [jobID=61]
   > [2024/07/23 15:32:03.266 +00:00] [INFO] [domain.go:646] ["performing DDL change, must reload"]
   > [2024/07/23 15:32:03.267 +00:00] [INFO] [session.go:2271] ["CRUCIAL OPERATION"] [conn=7] [schemaVersion=38] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.19]
   > [2024/07/23 15:32:03.282 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:63, Type:create schema, State:none, SchemaState:none, SchemaID:62, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 15:32:03.239 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/23 15:32:03.282 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:63, Type:create schema, State:none, SchemaState:none, SchemaID:62, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 15:32:03.239 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/23 15:32:03.285 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:63, Type:create schema, State:none, SchemaState:none, SchemaID:62, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:03.239 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:03.297 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=38] [neededSchemaVersion=39] ["start time"=928.689µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 15:32:03.347 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=39] ["take time"=53.628274ms] [job="ID:63, Type:create schema, State:done, SchemaState:public, SchemaID:62, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 15:32:03.239 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:03.350 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:63, Type:create schema, State:synced, SchemaState:public, SchemaID:62, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:03.239 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:03.361 +00:00] [INFO] [ddl.go:517] ["[ddl] DDL job is finished"] [jobID=63]
   > [2024/07/23 15:32:03.361 +00:00] [INFO] [domain.go:646] ["performing DDL change, must reload"]
   > [2024/07/23 15:32:03.364 +00:00] [INFO] [session.go:2271] ["CRUCIAL OPERATION"] [conn=7] [schemaVersion=39] [cur_db=testdb] [sql="create table t1(a int);"] [user=root@10.88.0.19]
   > [2024/07/23 15:32:03.383 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:65, Type:create table, State:none, SchemaState:none, SchemaID:62, TableID:64, RowCount:0, ArgLen:1, start time: 2024-07-23 15:32:03.339 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/23 15:32:03.383 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:65, Type:create table, State:none, SchemaState:none, SchemaID:62, TableID:64, RowCount:0, ArgLen:1, start time: 2024-07-23 15:32:03.339 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t1(a int);"]
   > [2024/07/23 15:32:03.386 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:create table, State:none, SchemaState:none, SchemaID:62, TableID:64, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:03.339 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:03.402 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=39] [neededSchemaVersion=40] ["start time"=1.510194ms] [phyTblIDs="[64]"] [actionTypes="[8]"]
   > [2024/07/23 15:32:03.451 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=40] ["take time"=53.938861ms] [job="ID:65, Type:create table, State:done, SchemaState:public, SchemaID:62, TableID:64, RowCount:0, ArgLen:1, start time: 2024-07-23 15:32:03.339 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:03.454 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:create table, State:synced, SchemaState:public, SchemaID:62, TableID:64, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:03.339 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:03.463 +00:00] [INFO] [ddl.go:517] ["[ddl] DDL job is finished"] [jobID=65]
   > [2024/07/23 15:32:03.465 +00:00] [INFO] [domain.go:646] ["performing DDL change, must reload"]
   > [2024/07/23 15:32:03.465 +00:00] [INFO] [split_region.go:61] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=748000000000000040]
   > [2024/07/23 15:32:03.465 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:32934] [split_keys="key 7480000000000000FF4000000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/23 15:32:03.466 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=54] [peer-ids="[55]"]
   > [2024/07/23 15:32:03.466 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF3A00000000000000F8 region_epoch { conf_ver: 1 version: 26 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 54 new_peer_ids: 55]"] [region_id=2]
   > [2024/07/23 15:32:03.468 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF4000000000000000F8 new_region_id: 54 new_peer_ids: 55 } right_derive: true }"] [index=66] [term=6] [peer_id=3] [region_id=2]
   > [2024/07/23 15:32:03.468 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF4000000000000000F8"] [region="id: 2 start_key: 7480000000000000FF3A00000000000000F8 region_epoch { conf_ver: 1 version: 26 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/07/23 15:32:03.469 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=2]
   > [2024/07/23 15:32:03.469 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/23 15:32:03.469 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(49)] [region_id=2] [store_id=Some(1)]
   > [2024/07/23 15:32:03.469 +00:00] [INFO] [split_region.go:158] ["batch split regions complete"] ["batch region ID"=2] ["first at"=748000000000000040] ["first new region left"="{Id:54 StartKey:7480000000000000ff3a00000000000000f8 EndKey:7480000000000000ff4000000000000000f8 RegionEpoch:{ConfVer:1 Version:27} Peers:[id:55 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/23 15:32:03.469 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/07/23 15:32:03.469 +00:00] [INFO] [split_region.go:207] ["split regions complete"] ["region count"=1] ["region IDs"="[54]"]
   > [2024/07/23 15:32:03.469 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF4000000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 3 store_id: 1 }"]
   > [2024/07/23 15:32:03.470 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF3A00000000000000F8} -> {7480000000000000FF4000000000000000F8}, EndKey:{}"] [old-version=26] [new-version=27]
   > [2024/07/23 15:32:03.470 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 54 start_key: 7480000000000000FF3A00000000000000F8 end_key: 7480000000000000FF4000000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 55 store_id: 1 }"] [region_id=54]
   > [2024/07/23 15:32:03.470 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=2] [origin="id:54 start_key:\"7480000000000000FF3A00000000000000F8\" end_key:\"7480000000000000FF4000000000000000F8\" region_epoch:<conf_ver:1 version:27 > peers:<id:55 store_id:1 >"] [total=1]
   > [2024/07/23 15:32:03.470 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=55] [region_id=54]
   > [2024/07/23 15:32:03.470 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 2 start_key: 7480000000000000FF4000000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 3 store_id: 1 } }"]
   > [2024/07/23 15:32:03.470 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 2 start_key: 7480000000000000FF4000000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 3 store_id: 1 }"]
   > [2024/07/23 15:32:03.471 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {55} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=55] [region_id=54]
   > [2024/07/23 15:32:03.471 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=55] [region_id=54]
   > [2024/07/23 15:32:03.471 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {55} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=55] [region_id=54]
   > [2024/07/23 15:32:03.471 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 55."] [id=55] [raft_id=55] [region_id=54]
   > [2024/07/23 15:32:03.471 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=55] [region_id=54]
   > [2024/07/23 15:32:03.471 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=55] [region_id=54]
   > [2024/07/23 15:32:03.471 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=55] [region_id=54]
   > [2024/07/23 15:32:03.471 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=55] [region_id=54]
   > [2024/07/23 15:32:03.471 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803830] [region_id=54]
   > [2024/07/23 15:32:03.471 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=66] [observe_id=ObserveId(51)] [region=2]
   > [2024/07/23 15:32:03.471 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=54]
   > [2024/07/23 15:32:03.473 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 54 start_key: 7480000000000000FF3A00000000000000F8 end_key: 7480000000000000FF4000000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 55 store_id: 1 }"]
   > [2024/07/23 15:32:03.473 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(52)] [region=54]
   > [2024/07/23 15:32:03.475 +00:00] [INFO] [scheduler.rs:640] ["get snapshot failed"] [err="Error(Request(message: \"EpochNotMatch current epoch of region 2 is conf_ver: 1 version: 27, but you sent conf_ver: 1 version: 26\" epoch_not_match { current_regions { id: 2 start_key: 7480000000000000FF4000000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 3 store_id: 1 } } current_regions { id: 54 start_key: 7480000000000000FF3A00000000000000F8 end_key: 7480000000000000FF4000000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 55 store_id: 1 } } }))"] [cid=379]
   > [2024/07/23 15:32:04.502 +00:00] [INFO] [set.go:216] ["set global var"] [conn=8] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/07/23 15:32:04.504 +00:00] [INFO] [set.go:216] ["set global var"] [conn=8] [name=transaction_isolation] [val=REPEATABLE-READ]
   > [2024/07/23 15:32:05.118 +00:00] [INFO] [session.go:2271] ["CRUCIAL OPERATION"] [conn=9] [schemaVersion=40] [cur_db=testdb] [sql=" create table t2(a int);"] [user=root@10.88.0.19]
   > [2024/07/23 15:32:05.143 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:67, Type:create table, State:none, SchemaState:none, SchemaID:62, TableID:66, RowCount:0, ArgLen:1, start time: 2024-07-23 15:32:05.089 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/23 15:32:05.143 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:67, Type:create table, State:none, SchemaState:none, SchemaID:62, TableID:66, RowCount:0, ArgLen:1, start time: 2024-07-23 15:32:05.089 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query=" create table t2(a int);"]
   > [2024/07/23 15:32:05.147 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:create table, State:none, SchemaState:none, SchemaID:62, TableID:66, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:05.089 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:05.168 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=40] [neededSchemaVersion=41] ["start time"=1.982955ms] [phyTblIDs="[66]"] [actionTypes="[8]"]
   > [2024/07/23 15:32:05.216 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=41] ["take time"=54.254267ms] [job="ID:67, Type:create table, State:done, SchemaState:public, SchemaID:62, TableID:66, RowCount:0, ArgLen:1, start time: 2024-07-23 15:32:05.089 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:05.219 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:create table, State:synced, SchemaState:public, SchemaID:62, TableID:66, RowCount:0, ArgLen:0, start time: 2024-07-23 15:32:05.089 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 15:32:05.229 +00:00] [INFO] [ddl.go:517] ["[ddl] DDL job is finished"] [jobID=67]
   > [2024/07/23 15:32:05.231 +00:00] [INFO] [domain.go:646] ["performing DDL change, must reload"]
   > [2024/07/23 15:32:05.231 +00:00] [INFO] [split_region.go:61] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=748000000000000042]
   > [2024/07/23 15:32:05.231 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:32906] [split_keys="key 7480000000000000FF4200000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/23 15:32:05.232 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=56] [peer-ids="[57]"]
   > [2024/07/23 15:32:05.232 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF4000000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 56 new_peer_ids: 57]"] [region_id=2]
   > [2024/07/23 15:32:05.233 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF4200000000000000F8 new_region_id: 56 new_peer_ids: 57 } right_derive: true }"] [index=69] [term=6] [peer_id=3] [region_id=2]
   > [2024/07/23 15:32:05.233 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF4200000000000000F8"] [region="id: 2 start_key: 7480000000000000FF4000000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/07/23 15:32:05.235 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/23 15:32:05.235 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=2]
   > [2024/07/23 15:32:05.235 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(51)] [region_id=2] [store_id=Some(1)]
   > [2024/07/23 15:32:05.235 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF4200000000000000F8 region_epoch { conf_ver: 1 version: 28 } peers { id: 3 store_id: 1 }"]
   > [2024/07/23 15:32:05.235 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/07/23 15:32:05.235 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 56 start_key: 7480000000000000FF4000000000000000F8 end_key: 7480000000000000FF4200000000000000F8 region_epoch { conf_ver: 1 version: 28 } peers { id: 57 store_id: 1 }"] [region_id=56]
   > [2024/07/23 15:32:05.235 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=57] [region_id=56]
   > [2024/07/23 15:32:05.235 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 2 start_key: 7480000000000000FF4200000000000000F8 region_epoch { conf_ver: 1 version: 28 } peers { id: 3 store_id: 1 } }"]
   > [2024/07/23 15:32:05.235 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 2 start_key: 7480000000000000FF4200000000000000F8 region_epoch { conf_ver: 1 version: 28 } peers { id: 3 store_id: 1 }"]
   > [2024/07/23 15:32:05.235 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {57} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=57] [region_id=56]
   > [2024/07/23 15:32:05.235 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=57] [region_id=56]
   > [2024/07/23 15:32:05.235 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {57} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=57] [region_id=56]
   > [2024/07/23 15:32:05.235 +00:00] [INFO] [split_region.go:158] ["batch split regions complete"] ["batch region ID"=2] ["first at"=748000000000000042] ["first new region left"="{Id:56 StartKey:7480000000000000ff4000000000000000f8 EndKey:7480000000000000ff4200000000000000f8 RegionEpoch:{ConfVer:1 Version:28} Peers:[id:57 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/23 15:32:05.235 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 57."] [id=57] [raft_id=57] [region_id=56]
   > [2024/07/23 15:32:05.235 +00:00] [INFO] [split_region.go:207] ["split regions complete"] ["region count"=1] ["region IDs"="[56]"]
   > [2024/07/23 15:32:05.235 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=57] [region_id=56]
   > [2024/07/23 15:32:05.236 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=57] [region_id=56]
   > [2024/07/23 15:32:05.236 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=57] [region_id=56]
   > [2024/07/23 15:32:05.236 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=57] [region_id=56]
   > [2024/07/23 15:32:05.236 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF4000000000000000F8} -> {7480000000000000FF4200000000000000F8}, EndKey:{}"] [old-version=27] [new-version=28]
   > [2024/07/23 15:32:05.236 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803832] [region_id=56]
   > [2024/07/23 15:32:05.236 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=69] [observe_id=ObserveId(53)] [region=2]
   > [2024/07/23 15:32:05.236 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=2] [origin="id:56 start_key:\"7480000000000000FF4000000000000000F8\" end_key:\"7480000000000000FF4200000000000000F8\" region_epoch:<conf_ver:1 version:28 > peers:<id:57 store_id:1 >"] [total=1]
   > [2024/07/23 15:32:05.236 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=56]
   > [2024/07/23 15:32:05.237 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 56 start_key: 7480000000000000FF4000000000000000F8 end_key: 7480000000000000FF4200000000000000F8 region_epoch { conf_ver: 1 version: 28 } peers { id: 57 store_id: 1 }"]
   > [2024/07/23 15:32:05.237 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(54)] [region=56]
