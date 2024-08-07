# Bug ID TIDB-22345-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/22345
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              "Select For Update" in decorrelated subquery return WriteConflictError in pessimistic mode.


## Details
 * Database: tidb-v4.0.0-beta.2.tikv
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
     - Instruction:  begin pessimistic;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows: 0
 * Instruction #2:
     - Instruction:  select * from t;
     - Transaction: conn_0
     - Output: [(1, 10), (2, 20)]
     - Executed order: 2
     - Affected rows: 2
 * Instruction #3:
     - Instruction:  update t set v = v * 10;
     - Transaction: conn_1
     - Output: None
     - Executed order: 3
     - Affected rows: 2
 * Instruction #4:
     - Instruction:  select (select v from t where id = 2 for update) from dual;
     - Transaction: conn_0
     - Output: ERROR: 9007 (HY000): Write conflict, txnStartTS=451680375986454529, conflictStartTS=451680376156848134, conflictCommitTS=451680376156848135, key={tableID=47, handle=2} primary={tableID=47, handle=2} [try again later]
     - Executed order: Not executed
     - Affected rows: -1

 * Container logs:
   > [2024/08/07 09:44:53.600 +00:00] [INFO] [server.go:388] ["new connection"] [conn=2] [remoteAddr=127.0.0.1:54188]
   > [2024/08/07 09:44:53.602 +00:00] [INFO] [session.go:2210] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=22] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/08/07 09:44:53.603 +00:00] [INFO] [session.go:2210] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=22] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/08/07 09:44:53.635 +00:00] [INFO] [ddl_worker.go:253] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-07 09:44:53.612 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/07 09:44:53.636 +00:00] [INFO] [ddl.go:500] ["[ddl] start DDL job"] [job="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-07 09:44:53.612 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/08/07 09:44:53.639 +00:00] [INFO] [ddl_worker.go:568] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-07 09:44:53.612 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 09:44:53.664 +00:00] [INFO] [domain.go:126] ["diff load InfoSchema success"] [usedSchemaVersion=22] [neededSchemaVersion=23] ["start time"=1.279297ms] [tblIDs="[]"]
   > [2024/08/07 09:44:53.714 +00:00] [INFO] [ddl_worker.go:759] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=23] ["take time"=58.701039ms] [job="ID:46, Type:create schema, State:done, SchemaState:public, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-07 09:44:53.612 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 09:44:53.718 +00:00] [INFO] [ddl_worker.go:359] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:46, Type:create schema, State:synced, SchemaState:public, SchemaID:45, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-07 09:44:53.612 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 09:44:53.736 +00:00] [INFO] [ddl.go:532] ["[ddl] DDL job is finished"] [jobID=46]
   > [2024/08/07 09:44:53.736 +00:00] [INFO] [domain.go:631] ["performing DDL change, must reload"]
   > [2024/08/07 09:44:53.740 +00:00] [INFO] [session.go:2210] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=23] [cur_db=testdb] [sql="create table t(id int primary key, v int);"] [user=root@127.0.0.1]
   > [2024/08/07 09:44:53.775 +00:00] [INFO] [ddl_worker.go:253] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-08-07 09:44:53.712 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/07 09:44:53.775 +00:00] [INFO] [ddl.go:500] ["[ddl] start DDL job"] [job="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-08-07 09:44:53.712 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t(id int primary key, v int);"]
   > [2024/08/07 09:44:53.779 +00:00] [INFO] [ddl_worker.go:568] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-08-07 09:44:53.712 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 09:44:53.812 +00:00] [INFO] [conn.go:497] ["wait handshake response fail due to connection has be closed by client-side"] [conn=3]
   > [2024/08/07 09:44:53.816 +00:00] [INFO] [domain.go:126] ["diff load InfoSchema success"] [usedSchemaVersion=23] [neededSchemaVersion=24] ["start time"=1.371557ms] [tblIDs="[47]"]
   > [2024/08/07 09:44:53.866 +00:00] [INFO] [ddl_worker.go:759] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=24] ["take time"=61.644531ms] [job="ID:48, Type:create table, State:done, SchemaState:public, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-08-07 09:44:53.712 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 09:44:53.870 +00:00] [INFO] [ddl_worker.go:359] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:48, Type:create table, State:synced, SchemaState:public, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-08-07 09:44:53.712 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 09:44:53.887 +00:00] [INFO] [ddl.go:532] ["[ddl] DDL job is finished"] [jobID=48]
   > [2024/08/07 09:44:53.888 +00:00] [INFO] [domain.go:631] ["performing DDL change, must reload"]
   > [2024/08/07 09:44:53.889 +00:00] [INFO] [split_region.go:56] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=74800000000000002f]
   > [2024/08/07 09:44:53.889 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:54630] [split_keys="key 7480000000000000FF2F00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/07 09:44:53.889 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=44] [peer-ids="[45]"]
   > [2024/08/07 09:44:53.890 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF2B00000000000000F8 region_epoch { conf_ver: 1 version: 21 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 44 new_peer_ids: 45]"] [region_id=2]
   > [2024/08/07 09:44:53.899 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF2F00000000000000F8 new_region_id: 44 new_peer_ids: 45 } right_derive: true }"] [index=52] [term=6] [peer_id=3] [region_id=2]
   > [2024/08/07 09:44:53.899 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF2F00000000000000F8"] [region="id: 2 start_key: 7480000000000000FF2B00000000000000F8 region_epoch { conf_ver: 1 version: 21 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/08/07 09:44:53.909 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/08/07 09:44:53.909 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=2]
   > [2024/08/07 09:44:53.909 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/08/07 09:44:53.909 +00:00] [INFO] [split_region.go:153] ["batch split regions complete"] ["batch region ID"=2] ["first at"=74800000000000002f] ["first new region left"="{Id:44 StartKey:7480000000000000ff2b00000000000000f8 EndKey:7480000000000000ff2f00000000000000f8 RegionEpoch:{ConfVer:1 Version:22} Peers:[id:45 store_id:1 ]}"] ["new region count"=1]
   > [2024/08/07 09:44:53.909 +00:00] [INFO] [split_region.go:205] ["split regions complete"] ["region count"=1] ["region IDs"="[44]"]
   > [2024/08/07 09:44:53.909 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(39)] [region_id=2] [store_id=Some(1)]
   > [2024/08/07 09:44:53.909 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 3 store_id: 1 }"]
   > [2024/08/07 09:44:53.909 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 44 start_key: 7480000000000000FF2B00000000000000F8 end_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 45 store_id: 1 }"] [region_id=44]
   > [2024/08/07 09:44:53.909 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=45] [region_id=44]
   > [2024/08/07 09:44:53.909 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF2B00000000000000F8} -> {7480000000000000FF2F00000000000000F8}, EndKey:{}"] [old-version=21] [new-version=22]
   > [2024/08/07 09:44:53.909 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 2 start_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 3 store_id: 1 } }"]
   > [2024/08/07 09:44:53.909 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 2 start_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 3 store_id: 1 }"]
   > [2024/08/07 09:44:53.909 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=2] [origin="id:44 start_key:\"7480000000000000FF2B00000000000000F8\" end_key:\"7480000000000000FF2F00000000000000F8\" region_epoch:<conf_ver:1 version:22 > peers:<id:45 store_id:1 >"] [total=1]
   > [2024/08/07 09:44:53.909 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {45} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=45] [region_id=44]
   > [2024/08/07 09:44:53.909 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=45] [region_id=44]
   > [2024/08/07 09:44:53.910 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {45} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=45] [region_id=44]
   > [2024/08/07 09:44:53.910 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 45."] [id=45] [raft_id=45] [region_id=44]
   > [2024/08/07 09:44:53.910 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=45] [region_id=44]
   > [2024/08/07 09:44:53.910 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=45] [region_id=44]
   > [2024/08/07 09:44:53.910 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=45] [region_id=44]
   > [2024/08/07 09:44:53.910 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=45] [region_id=44]
   > [2024/08/07 09:44:53.910 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803820] [region_id=44]
   > [2024/08/07 09:44:53.910 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=44]
   > [2024/08/07 09:44:53.910 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=52] [observe_id=ObserveId(41)] [region=2]
   > [2024/08/07 09:44:53.915 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 44 start_key: 7480000000000000FF2B00000000000000F8 end_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 45 store_id: 1 }"]
   > [2024/08/07 09:44:53.915 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(42)] [region=44]
   > [2024/08/07 09:44:53.932 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=2]
   > [2024/08/07 09:44:54.949 +00:00] [INFO] [server.go:388] ["new connection"] [conn=4] [remoteAddr=127.0.0.1:54216]
   > [2024/08/07 09:44:54.952 +00:00] [INFO] [set.go:207] ["set session var"] [conn=4] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/08/07 09:44:55.858 +00:00] [INFO] [server.go:388] ["new connection"] [conn=5] [remoteAddr=127.0.0.1:54232]
   > [2024/08/07 09:44:55.870 +00:00] [INFO] [set.go:207] ["set session var"] [conn=5] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/08/07 09:44:56.159 +00:00] [WARN] [session.go:1144] ["compile SQL failed"] [conn=4] [error="[kv:9007]Write conflict, txnStartTS=451680375986454529, conflictStartTS=451680376156848134, conflictCommitTS=451680376156848135, key={tableID=47, handle=2} primary={tableID=47, handle=2} [try again later]"] [SQL=" select (select v from t where id = 2 for update) from dual;"]
   > [2024/08/07 09:44:56.160 +00:00] [ERROR] [conn.go:730] ["command dispatched failed"] [conn=4] [connInfo="id:4, addr:127.0.0.1:54216 status:11, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:1, autocommit:1"] [sql=" select (select v from t where id = 2 for update) from dual;"] [txn_mode=PESSIMISTIC] [err="[kv:9007]Write conflict, txnStartTS=451680375986454529, conflictStartTS=451680376156848134, conflictCommitTS=451680376156848135, key={tableID=47, handle=2} primary={tableID=47, handle=2} [try again later]"]
   > [2024/08/07 09:44:56.558 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=5]
   > [2024/08/07 09:44:56.558 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=4]
