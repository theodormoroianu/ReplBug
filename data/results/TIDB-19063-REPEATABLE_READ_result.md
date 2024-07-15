# Bug ID TIDB-19063-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/19063
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              Duplicate key is ignored in insert The insert statement should fail.


## Details
 * Database: tidb-bdc59e6e.tikv
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
     - Instruction:  begin;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  replace into t values (22, 'gold witch'), (24, 'gray singer'), (21, 'silver sig...
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 3 / 0
 * Instruction #3:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 0 / 0
 * Instruction #4:
     - Instruction:  begin;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows / Warnings: 0 / 0
 * Instruction #5:
     - Instruction:  insert into t values (21,'black warlock'), (22, 'dark sloth'), (21, 'cyan song'...
     - Transaction: conn_0
     - Output: None
     - Executed order: 5
     - Affected rows / Warnings: 5 / 0
 * Instruction #6:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: None
     - Executed order: 6
     - Affected rows / Warnings: 0 / 0
 * Instruction #7:
     - Instruction:  select * from t;
     - Transaction: conn_0
     - Output: [(22, 'gold witch'), (24, 'gray singer'), (23, '23:22:silver sight'), (21, 'cyan song')]
     - Executed order: 7
     - Affected rows / Warnings: 4 / 0
 * Instruction #8:
     - Instruction:  drop table t;
     - Transaction: conn_0
     - Output: None
     - Executed order: 8
     - Affected rows / Warnings: 0 / 0

 * Container logs:
   > [2024/07/15 15:20:34.731 +00:00] [INFO] [server.go:388] ["new connection"] [conn=3] [remoteAddr=10.88.0.68:37394]
   > [2024/07/15 15:20:34.734 +00:00] [INFO] [session.go:2232] ["CRUCIAL OPERATION"] [conn=3] [schemaVersion=22] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.68]
   > [2024/07/15 15:20:34.735 +00:00] [INFO] [session.go:2232] ["CRUCIAL OPERATION"] [conn=3] [schemaVersion=22] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.68]
   > [2024/07/15 15:20:34.746 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164722873761800] [commitTS=451164722886606849]
   > [2024/07/15 15:20:34.756 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164722886606850] [commitTS=451164722886606851]
   > [2024/07/15 15:20:34.759 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-15 15:20:34.742 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/15 15:20:34.759 +00:00] [INFO] [ddl.go:475] ["[ddl] start DDL job"] [job="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-15 15:20:34.742 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/15 15:20:34.763 +00:00] [INFO] [ddl_worker.go:586] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 15:20:34.742 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:20:34.772 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164722886606853] [commitTS=451164722886606854]
   > [2024/07/15 15:20:34.781 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=22] [neededSchemaVersion=23] ["start time"=1.518297ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/15 15:20:34.830 +00:00] [INFO] [ddl_worker.go:778] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=23] ["take time"=54.408314ms] [job="ID:46, Type:create schema, State:done, SchemaState:public, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-15 15:20:34.742 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:20:34.833 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:46, Type:create schema, State:synced, SchemaState:public, SchemaID:45, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 15:20:34.742 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:20:34.839 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164722899976193] [commitTS=451164722899976194]
   > [2024/07/15 15:20:34.844 +00:00] [INFO] [ddl.go:507] ["[ddl] DDL job is finished"] [jobID=46]
   > [2024/07/15 15:20:34.844 +00:00] [INFO] [domain.go:643] ["performing DDL change, must reload"]
   > [2024/07/15 15:20:34.848 +00:00] [INFO] [session.go:2232] ["CRUCIAL OPERATION"] [conn=3] [schemaVersion=23] [cur_db=testdb] [sql="create table t ( c_int int, c_string varchar(40) collate utf8mb4_bin , primary key (c_string), unique key (c_int));"] [user=root@10.88.0.68]
   > [2024/07/15 15:20:34.853 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164722912821255] [commitTS=451164722912821256]
   > [2024/07/15 15:20:34.863 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164722912821257] [commitTS=451164722912821258]
   > [2024/07/15 15:20:34.867 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-07-15 15:20:34.842 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/15 15:20:34.867 +00:00] [INFO] [ddl.go:475] ["[ddl] start DDL job"] [job="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-07-15 15:20:34.842 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t ( c_int int, c_string varchar(40) collate utf8mb4_bin , primary key (c_string), unique key (c_int));"]
   > [2024/07/15 15:20:34.871 +00:00] [INFO] [ddl_worker.go:586] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-15 15:20:34.842 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:20:34.879 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164722912821262] [commitTS=451164722912821265]
   > [2024/07/15 15:20:34.882 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164722912821264] [commitTS=451164722912821266]
   > [2024/07/15 15:20:34.889 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=23] [neededSchemaVersion=24] ["start time"=1.812472ms] [phyTblIDs="[47]"] [actionTypes="[8]"]
   > [2024/07/15 15:20:34.894 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164722912821268] [commitTS=451164722925928449]
   > [2024/07/15 15:20:34.939 +00:00] [INFO] [ddl_worker.go:778] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=24] ["take time"=54.979342ms] [job="ID:48, Type:create table, State:done, SchemaState:public, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-07-15 15:20:34.842 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:20:34.942 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:48, Type:create table, State:synced, SchemaState:public, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-15 15:20:34.842 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:20:34.946 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164722925928451] [commitTS=451164722939035649]
   > [2024/07/15 15:20:34.951 +00:00] [INFO] [ddl.go:507] ["[ddl] DDL job is finished"] [jobID=48]
   > [2024/07/15 15:20:34.954 +00:00] [INFO] [domain.go:643] ["performing DDL change, must reload"]
   > [2024/07/15 15:20:34.954 +00:00] [INFO] [split_region.go:59] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=74800000000000002f]
   > [2024/07/15 15:20:34.954 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:56416] [split_keys="key 7480000000000000FF2F00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/15 15:20:34.955 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=44] [peer-ids="[45]"]
   > [2024/07/15 15:20:34.955 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF2B00000000000000F8 region_epoch { conf_ver: 1 version: 21 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 44 new_peer_ids: 45]"] [region_id=2]
   > [2024/07/15 15:20:34.956 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=3]
   > [2024/07/15 15:20:34.958 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF2F00000000000000F8 new_region_id: 44 new_peer_ids: 45 } right_derive: true }"] [index=54] [term=6] [peer_id=3] [region_id=2]
   > [2024/07/15 15:20:34.958 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF2F00000000000000F8"] [region="id: 2 start_key: 7480000000000000FF2B00000000000000F8 region_epoch { conf_ver: 1 version: 21 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/07/15 15:20:34.961 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/15 15:20:34.961 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=2]
   > [2024/07/15 15:20:34.961 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/07/15 15:20:34.961 +00:00] [INFO] [split_region.go:156] ["batch split regions complete"] ["batch region ID"=2] ["first at"=74800000000000002f] ["first new region left"="{Id:44 StartKey:7480000000000000ff2b00000000000000f8 EndKey:7480000000000000ff2f00000000000000f8 RegionEpoch:{ConfVer:1 Version:22} Peers:[id:45 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/15 15:20:34.962 +00:00] [INFO] [split_region.go:205] ["split regions complete"] ["region count"=1] ["region IDs"="[44]"]
   > [2024/07/15 15:20:34.962 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(39)] [region_id=2] [store_id=Some(1)]
   > [2024/07/15 15:20:34.962 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF2B00000000000000F8} -> {7480000000000000FF2F00000000000000F8}, EndKey:{}"] [old-version=21] [new-version=22]
   > [2024/07/15 15:20:34.962 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 44 start_key: 7480000000000000FF2B00000000000000F8 end_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 45 store_id: 1 }"] [region_id=44]
   > [2024/07/15 15:20:34.962 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=2] [origin="id:44 start_key:\"7480000000000000FF2B00000000000000F8\" end_key:\"7480000000000000FF2F00000000000000F8\" region_epoch:<conf_ver:1 version:22 > peers:<id:45 store_id:1 >"] [total=1]
   > [2024/07/15 15:20:34.962 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 3 store_id: 1 }"]
   > [2024/07/15 15:20:34.962 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=45] [region_id=44]
   > [2024/07/15 15:20:34.962 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 2 start_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 3 store_id: 1 } }"]
   > [2024/07/15 15:20:34.962 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 2 start_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 3 store_id: 1 }"]
   > [2024/07/15 15:20:34.962 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {45} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=45] [region_id=44]
   > [2024/07/15 15:20:34.962 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=45] [region_id=44]
   > [2024/07/15 15:20:34.962 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {45} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=45] [region_id=44]
   > [2024/07/15 15:20:34.962 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 45."] [id=45] [raft_id=45] [region_id=44]
   > [2024/07/15 15:20:34.962 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=45] [region_id=44]
   > [2024/07/15 15:20:34.962 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=45] [region_id=44]
   > [2024/07/15 15:20:34.963 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=45] [region_id=44]
   > [2024/07/15 15:20:34.963 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=45] [region_id=44]
   > [2024/07/15 15:20:34.963 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803820] [region_id=44]
   > [2024/07/15 15:20:34.963 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=54] [observe_id=ObserveId(41)] [region=2]
   > [2024/07/15 15:20:34.963 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=44]
   > [2024/07/15 15:20:34.964 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 44 start_key: 7480000000000000FF2B00000000000000F8 end_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 45 store_id: 1 }"]
   > [2024/07/15 15:20:34.964 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(42)] [region=44]
   > [2024/07/15 15:20:35.975 +00:00] [INFO] [server.go:388] ["new connection"] [conn=4] [remoteAddr=10.88.0.68:37400]
   > [2024/07/15 15:20:35.978 +00:00] [INFO] [set.go:216] ["set session var"] [conn=4] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/07/15 15:20:35.981 +00:00] [INFO] [set.go:216] ["set global var"] [conn=4] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/07/15 15:20:35.983 +00:00] [INFO] [set.go:216] ["set global var"] [conn=4] [name=transaction_isolation] [val=REPEATABLE-READ]
   > [2024/07/15 15:20:36.595 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164723358466049] [commitTS=451164723371573249]
   > [2024/07/15 15:20:38.379 +00:00] [INFO] [session.go:2232] ["CRUCIAL OPERATION"] [conn=4] [schemaVersion=24] [cur_db=testdb] [sql=" drop table t;"] [user=root@10.88.0.68]
   > [2024/07/15 15:20:38.387 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164723830325251] [commitTS=451164723830325252]
   > [2024/07/15 15:20:38.390 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:49, Type:drop table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-15 15:20:38.342 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/15 15:20:38.390 +00:00] [INFO] [ddl.go:475] ["[ddl] start DDL job"] [job="ID:49, Type:drop table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-15 15:20:38.342 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query=" drop table t;"]
   > [2024/07/15 15:20:38.395 +00:00] [INFO] [ddl_worker.go:586] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:49, Type:drop table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-15 15:20:38.342 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:20:38.405 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164723843432449] [commitTS=451164723843432450]
   > [2024/07/15 15:20:38.413 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=24] [neededSchemaVersion=25] ["start time"=763.374µs] [phyTblIDs="[47]"] [actionTypes="[16]"]
   > [2024/07/15 15:20:38.463 +00:00] [INFO] [ddl_worker.go:778] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=25] ["take time"=54.280782ms] [job="ID:49, Type:drop table, State:running, SchemaState:write only, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-15 15:20:38.342 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:20:38.465 +00:00] [INFO] [ddl_worker.go:586] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:49, Type:drop table, State:running, SchemaState:write only, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-15 15:20:38.342 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:20:38.475 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164723856539649] [commitTS=451164723856539650]
   > [2024/07/15 15:20:38.483 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=25] [neededSchemaVersion=26] ["start time"=731.246µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/15 15:20:38.533 +00:00] [INFO] [ddl_worker.go:778] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=26] ["take time"=54.819265ms] [job="ID:49, Type:drop table, State:running, SchemaState:delete only, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-15 15:20:38.342 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:20:38.536 +00:00] [INFO] [ddl_worker.go:586] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:49, Type:drop table, State:running, SchemaState:delete only, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-15 15:20:38.342 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:20:38.545 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164723869908993] [commitTS=451164723883016193]
   > [2024/07/15 15:20:38.553 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=26] [neededSchemaVersion=27] ["start time"=756.18µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/15 15:20:38.603 +00:00] [INFO] [ddl_worker.go:778] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=27] ["take time"=54.924866ms] [job="ID:49, Type:drop table, State:done, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:2, start time: 2024-07-15 15:20:38.342 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:20:38.606 +00:00] [INFO] [delete_range.go:350] ["[ddl] insert into delete-range table"] [jobID=49] [elementID=47]
   > [2024/07/15 15:20:38.616 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164723895861252] [commitTS=451164723895861253]
   > [2024/07/15 15:20:38.627 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=49] [jobType="drop table"]
   > [2024/07/15 15:20:38.629 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:49, Type:drop table, State:synced, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:2, start time: 2024-07-15 15:20:38.342 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:20:38.635 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164723895861249] [commitTS=451164723895861255]
   > [2024/07/15 15:20:38.640 +00:00] [INFO] [ddl.go:507] ["[ddl] DDL job is finished"] [jobID=49]
   > [2024/07/15 15:20:38.640 +00:00] [INFO] [domain.go:643] ["performing DDL change, must reload"]
   > [2024/07/15 15:20:38.847 +00:00] [INFO] [cluster.go:1469] ["store has changed to serving"] [store-id=1] [store-address=127.0.0.1:20160]
   > [2024/07/15 15:20:38.862 +00:00] [INFO] [client.rs:789] ["set cluster version to 6.4.0"]
   > [2024/07/15 15:20:48.682 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=4]

### Scenario 1
 * Instruction #0:
     - Instruction:  replace into t values (22, 'gold witch'), (24, 'gray singer'), (21, 'silver sig...
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 3 / 0
 * Instruction #1:
     - Instruction:  insert into t values (21,'black warlock'), (22, 'dark sloth'), (21, 'cyan song'...
     - Transaction: conn_0
     - Output: ERROR: 1062 (23000): Duplicate entry '22' for key 'c_int'
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #2:
     - Instruction:  select * from t;
     - Transaction: conn_0
     - Output: [(22, 'gold witch'), (24, 'gray singer'), (21, 'silver sight')]
     - Executed order: 1
     - Affected rows / Warnings: 3 / 0
 * Instruction #3:
     - Instruction:  drop table t;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 0 / 0

 * Container logs:
   > [2024/07/15 15:20:50.235 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=5]
   > [2024/07/15 15:20:50.237 +00:00] [INFO] [server.go:388] ["new connection"] [conn=6] [remoteAddr=10.88.0.68:58188]
   > [2024/07/15 15:20:50.240 +00:00] [INFO] [session.go:2232] ["CRUCIAL OPERATION"] [conn=6] [schemaVersion=35] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.68]
   > [2024/07/15 15:20:50.253 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164726936731654] [commitTS=451164726949838849]
   > [2024/07/15 15:20:50.257 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:56, Type:drop schema, State:none, SchemaState:none, SchemaID:51, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 15:20:50.192 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/15 15:20:50.257 +00:00] [INFO] [ddl.go:475] ["[ddl] start DDL job"] [job="ID:56, Type:drop schema, State:none, SchemaState:none, SchemaID:51, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 15:20:50.192 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/15 15:20:50.261 +00:00] [INFO] [ddl_worker.go:586] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:56, Type:drop schema, State:none, SchemaState:none, SchemaID:51, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 15:20:50.192 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:20:50.270 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164726949838851] [commitTS=451164726949838852]
   > [2024/07/15 15:20:50.279 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=35] [neededSchemaVersion=36] ["start time"=904.455µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/15 15:20:50.329 +00:00] [INFO] [ddl_worker.go:778] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=36] ["take time"=54.815842ms] [job="ID:56, Type:drop schema, State:running, SchemaState:write only, SchemaID:51, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 15:20:50.192 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:20:50.331 +00:00] [INFO] [ddl_worker.go:586] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:56, Type:drop schema, State:running, SchemaState:write only, SchemaID:51, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 15:20:50.192 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:20:50.340 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164726962946049] [commitTS=451164726962946050]
   > [2024/07/15 15:20:50.348 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=36] [neededSchemaVersion=37] ["start time"=730.758µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/15 15:20:50.398 +00:00] [INFO] [ddl_worker.go:778] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=37] ["take time"=54.277849ms] [job="ID:56, Type:drop schema, State:running, SchemaState:delete only, SchemaID:51, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 15:20:50.192 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:20:50.400 +00:00] [INFO] [ddl_worker.go:586] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:56, Type:drop schema, State:running, SchemaState:delete only, SchemaID:51, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 15:20:50.192 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:20:50.411 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164726989160449] [commitTS=451164726989160450]
   > [2024/07/15 15:20:50.421 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=37] [neededSchemaVersion=38] ["start time"=605.461µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/15 15:20:50.471 +00:00] [INFO] [ddl_worker.go:778] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=38] ["take time"=56.421651ms] [job="ID:56, Type:drop schema, State:done, SchemaState:none, SchemaID:51, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 15:20:50.192 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:20:50.474 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=56] [jobType="drop schema"]
   > [2024/07/15 15:20:50.475 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:56, Type:drop schema, State:synced, SchemaState:none, SchemaID:51, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 15:20:50.192 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:20:50.480 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164727002267649] [commitTS=451164727002267651]
   > [2024/07/15 15:20:50.485 +00:00] [INFO] [ddl.go:507] ["[ddl] DDL job is finished"] [jobID=56]
   > [2024/07/15 15:20:50.485 +00:00] [INFO] [domain.go:643] ["performing DDL change, must reload"]
   > [2024/07/15 15:20:50.487 +00:00] [INFO] [session.go:2232] ["CRUCIAL OPERATION"] [conn=6] [schemaVersion=38] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.68]
   > [2024/07/15 15:20:50.493 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164727002267657] [commitTS=451164727015374849]
   > [2024/07/15 15:20:50.503 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164727015374850] [commitTS=451164727015374851]
   > [2024/07/15 15:20:50.507 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:58, Type:create schema, State:none, SchemaState:none, SchemaID:57, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-15 15:20:50.492 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/15 15:20:50.507 +00:00] [INFO] [ddl.go:475] ["[ddl] start DDL job"] [job="ID:58, Type:create schema, State:none, SchemaState:none, SchemaID:57, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-15 15:20:50.492 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/15 15:20:50.511 +00:00] [INFO] [ddl_worker.go:586] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:58, Type:create schema, State:none, SchemaState:none, SchemaID:57, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 15:20:50.492 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:20:50.519 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164727015374853] [commitTS=451164727015374854]
   > [2024/07/15 15:20:50.530 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=38] [neededSchemaVersion=39] ["start time"=1.355425ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/15 15:20:50.579 +00:00] [INFO] [ddl_worker.go:778] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=39] ["take time"=55.431011ms] [job="ID:58, Type:create schema, State:done, SchemaState:public, SchemaID:57, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-15 15:20:50.492 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:20:50.583 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:58, Type:create schema, State:synced, SchemaState:public, SchemaID:57, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 15:20:50.492 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:20:50.589 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164727028482049] [commitTS=451164727028482050]
   > [2024/07/15 15:20:50.594 +00:00] [INFO] [ddl.go:507] ["[ddl] DDL job is finished"] [jobID=58]
   > [2024/07/15 15:20:50.594 +00:00] [INFO] [domain.go:643] ["performing DDL change, must reload"]
   > [2024/07/15 15:20:50.597 +00:00] [INFO] [session.go:2232] ["CRUCIAL OPERATION"] [conn=6] [schemaVersion=39] [cur_db=testdb] [sql="create table t ( c_int int, c_string varchar(40) collate utf8mb4_bin , primary key (c_string), unique key (c_int));"] [user=root@10.88.0.68]
   > [2024/07/15 15:20:50.603 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164727041589255] [commitTS=451164727041589256]
   > [2024/07/15 15:20:50.613 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164727041589257] [commitTS=451164727041589258]
   > [2024/07/15 15:20:50.615 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:60, Type:create table, State:none, SchemaState:none, SchemaID:57, TableID:59, RowCount:0, ArgLen:1, start time: 2024-07-15 15:20:50.592 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/15 15:20:50.615 +00:00] [INFO] [ddl.go:475] ["[ddl] start DDL job"] [job="ID:60, Type:create table, State:none, SchemaState:none, SchemaID:57, TableID:59, RowCount:0, ArgLen:1, start time: 2024-07-15 15:20:50.592 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t ( c_int int, c_string varchar(40) collate utf8mb4_bin , primary key (c_string), unique key (c_int));"]
   > [2024/07/15 15:20:50.619 +00:00] [INFO] [ddl_worker.go:586] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:60, Type:create table, State:none, SchemaState:none, SchemaID:57, TableID:59, RowCount:0, ArgLen:0, start time: 2024-07-15 15:20:50.592 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:20:50.626 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164727041589260] [commitTS=451164727041589262]
   > [2024/07/15 15:20:50.635 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=39] [neededSchemaVersion=40] ["start time"=2.028214ms] [phyTblIDs="[59]"] [actionTypes="[8]"]
   > [2024/07/15 15:20:50.684 +00:00] [INFO] [ddl_worker.go:778] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=40] ["take time"=54.184749ms] [job="ID:60, Type:create table, State:done, SchemaState:public, SchemaID:57, TableID:59, RowCount:0, ArgLen:1, start time: 2024-07-15 15:20:50.592 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:20:50.688 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:60, Type:create table, State:synced, SchemaState:public, SchemaID:57, TableID:59, RowCount:0, ArgLen:0, start time: 2024-07-15 15:20:50.592 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:20:50.693 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164727054696449] [commitTS=451164727067803649]
   > [2024/07/15 15:20:50.699 +00:00] [INFO] [ddl.go:507] ["[ddl] DDL job is finished"] [jobID=60]
   > [2024/07/15 15:20:50.701 +00:00] [INFO] [domain.go:643] ["performing DDL change, must reload"]
   > [2024/07/15 15:20:50.701 +00:00] [INFO] [split_region.go:59] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=74800000000000003b]
   > [2024/07/15 15:20:50.702 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:56376] [split_keys="key 7480000000000000FF3B00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/15 15:20:50.702 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=48] [peer-ids="[49]"]
   > [2024/07/15 15:20:50.702 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF3500000000000000F8 region_epoch { conf_ver: 1 version: 23 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 48 new_peer_ids: 49]"] [region_id=2]
   > [2024/07/15 15:20:50.703 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=6]
   > [2024/07/15 15:20:50.705 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF3B00000000000000F8 new_region_id: 48 new_peer_ids: 49 } right_derive: true }"] [index=65] [term=6] [peer_id=3] [region_id=2]
   > [2024/07/15 15:20:50.705 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF3B00000000000000F8"] [region="id: 2 start_key: 7480000000000000FF3500000000000000F8 region_epoch { conf_ver: 1 version: 23 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/07/15 15:20:50.708 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/15 15:20:50.708 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=2]
   > [2024/07/15 15:20:50.708 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(43)] [region_id=2] [store_id=Some(1)]
   > [2024/07/15 15:20:50.708 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF3B00000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 3 store_id: 1 }"]
   > [2024/07/15 15:20:50.708 +00:00] [INFO] [split_region.go:156] ["batch split regions complete"] ["batch region ID"=2] ["first at"=74800000000000003b] ["first new region left"="{Id:48 StartKey:7480000000000000ff3500000000000000f8 EndKey:7480000000000000ff3b00000000000000f8 RegionEpoch:{ConfVer:1 Version:24} Peers:[id:49 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/15 15:20:50.708 +00:00] [INFO] [split_region.go:205] ["split regions complete"] ["region count"=1] ["region IDs"="[48]"]
   > [2024/07/15 15:20:50.708 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/07/15 15:20:50.708 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 48 start_key: 7480000000000000FF3500000000000000F8 end_key: 7480000000000000FF3B00000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 49 store_id: 1 }"] [region_id=48]
   > [2024/07/15 15:20:50.708 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=49] [region_id=48]
   > [2024/07/15 15:20:50.708 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 2 start_key: 7480000000000000FF3B00000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 3 store_id: 1 } }"]
   > [2024/07/15 15:20:50.708 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF3500000000000000F8} -> {7480000000000000FF3B00000000000000F8}, EndKey:{}"] [old-version=23] [new-version=24]
   > [2024/07/15 15:20:50.708 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 2 start_key: 7480000000000000FF3B00000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 3 store_id: 1 }"]
   > [2024/07/15 15:20:50.708 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=2] [origin="id:48 start_key:\"7480000000000000FF3500000000000000F8\" end_key:\"7480000000000000FF3B00000000000000F8\" region_epoch:<conf_ver:1 version:24 > peers:<id:49 store_id:1 >"] [total=1]
   > [2024/07/15 15:20:50.708 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {49} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=49] [region_id=48]
   > [2024/07/15 15:20:50.708 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=49] [region_id=48]
   > [2024/07/15 15:20:50.708 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {49} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=49] [region_id=48]
   > [2024/07/15 15:20:50.709 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 49."] [id=49] [raft_id=49] [region_id=48]
   > [2024/07/15 15:20:50.709 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=49] [region_id=48]
   > [2024/07/15 15:20:50.709 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=49] [region_id=48]
   > [2024/07/15 15:20:50.709 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=49] [region_id=48]
   > [2024/07/15 15:20:50.709 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=49] [region_id=48]
   > [2024/07/15 15:20:50.709 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803824] [region_id=48]
   > [2024/07/15 15:20:50.709 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=65] [observe_id=ObserveId(45)] [region=2]
   > [2024/07/15 15:20:50.709 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=48]
   > [2024/07/15 15:20:50.711 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 48 start_key: 7480000000000000FF3500000000000000F8 end_key: 7480000000000000FF3B00000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 49 store_id: 1 }"]
   > [2024/07/15 15:20:50.711 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(46)] [region=48]
   > [2024/07/15 15:20:51.714 +00:00] [INFO] [server.go:388] ["new connection"] [conn=7] [remoteAddr=10.88.0.68:58198]
   > [2024/07/15 15:20:51.723 +00:00] [INFO] [set.go:216] ["set session var"] [conn=7] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/07/15 15:20:51.740 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164727329947656] [commitTS=451164727329947657]
   > [2024/07/15 15:20:52.017 +00:00] [INFO] [tidb.go:217] ["rollbackTxn for ddl/autocommit failed"]
   > [2024/07/15 15:20:52.017 +00:00] [ERROR] [conn.go:744] ["command dispatched failed"] [conn=7] [connInfo="id:7, addr:10.88.0.68:58198 status:10, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:0, autocommit:1"] [sql=" insert into t values (21,'black warlock'), (22, 'dark sloth'), (21,  'cyan song') on duplicate key update c_int = c_int + 1, c_string = concat(c_int, ':', c_string);"] [txn_mode=PESSIMISTIC] [err="[kv:1062]Duplicate entry '22' for key 'c_int'"]
   > [2024/07/15 15:20:52.615 +00:00] [INFO] [session.go:2232] ["CRUCIAL OPERATION"] [conn=7] [schemaVersion=40] [cur_db=testdb] [sql=" drop table t;"] [user=root@10.88.0.68]
   > [2024/07/15 15:20:52.629 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164727565877251] [commitTS=451164727565877252]
   > [2024/07/15 15:20:52.633 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:61, Type:drop table, State:none, SchemaState:none, SchemaID:57, TableID:59, RowCount:0, ArgLen:0, start time: 2024-07-15 15:20:52.592 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/15 15:20:52.633 +00:00] [INFO] [ddl.go:475] ["[ddl] start DDL job"] [job="ID:61, Type:drop table, State:none, SchemaState:none, SchemaID:57, TableID:59, RowCount:0, ArgLen:0, start time: 2024-07-15 15:20:52.592 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query=" drop table t;"]
   > [2024/07/15 15:20:52.637 +00:00] [INFO] [ddl_worker.go:586] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:61, Type:drop table, State:none, SchemaState:none, SchemaID:57, TableID:59, RowCount:0, ArgLen:0, start time: 2024-07-15 15:20:52.592 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:20:52.647 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164727565877254] [commitTS=451164727578984449]
   > [2024/07/15 15:20:52.655 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=40] [neededSchemaVersion=41] ["start time"=733.901µs] [phyTblIDs="[59]"] [actionTypes="[16]"]
   > [2024/07/15 15:20:52.705 +00:00] [INFO] [ddl_worker.go:778] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=41] ["take time"=54.17986ms] [job="ID:61, Type:drop table, State:running, SchemaState:write only, SchemaID:57, TableID:59, RowCount:0, ArgLen:0, start time: 2024-07-15 15:20:52.592 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:20:52.707 +00:00] [INFO] [ddl_worker.go:586] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:61, Type:drop table, State:running, SchemaState:write only, SchemaID:57, TableID:59, RowCount:0, ArgLen:0, start time: 2024-07-15 15:20:52.592 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:20:52.717 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164727592091649] [commitTS=451164727592091650]
   > [2024/07/15 15:20:52.726 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=41] [neededSchemaVersion=42] ["start time"=746.472µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/15 15:20:52.775 +00:00] [INFO] [ddl_worker.go:778] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=42] ["take time"=53.713804ms] [job="ID:61, Type:drop table, State:running, SchemaState:delete only, SchemaID:57, TableID:59, RowCount:0, ArgLen:0, start time: 2024-07-15 15:20:52.592 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:20:52.777 +00:00] [INFO] [ddl_worker.go:586] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:61, Type:drop table, State:running, SchemaState:delete only, SchemaID:57, TableID:59, RowCount:0, ArgLen:0, start time: 2024-07-15 15:20:52.592 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:20:52.788 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164727605198849] [commitTS=451164727605198850]
   > [2024/07/15 15:20:52.797 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=42] [neededSchemaVersion=43] ["start time"=775.387µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/15 15:20:52.847 +00:00] [INFO] [ddl_worker.go:778] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=43] ["take time"=54.554283ms] [job="ID:61, Type:drop table, State:done, SchemaState:none, SchemaID:57, TableID:59, RowCount:0, ArgLen:2, start time: 2024-07-15 15:20:52.592 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:20:52.849 +00:00] [INFO] [delete_range.go:350] ["[ddl] insert into delete-range table"] [jobID=61] [elementID=59]
   > [2024/07/15 15:20:52.859 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=61] [jobType="drop table"]
   > [2024/07/15 15:20:52.861 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:61, Type:drop table, State:synced, SchemaState:none, SchemaID:57, TableID:59, RowCount:0, ArgLen:2, start time: 2024-07-15 15:20:52.592 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:20:52.866 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164727631413249] [commitTS=451164727631413253]
   > [2024/07/15 15:20:52.872 +00:00] [INFO] [ddl.go:507] ["[ddl] DDL job is finished"] [jobID=61]
   > [2024/07/15 15:20:52.872 +00:00] [INFO] [domain.go:643] ["performing DDL change, must reload"]
   > [2024/07/15 15:21:01.682 +00:00] [WARN] [grpclog.go:60] ["transport: http2Server.HandleStreams failed to read frame: read tcp 127.0.0.1:2379->127.0.0.1:53228: read: connection reset by peer"]
   > [2024/07/15 15:21:02.918 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=7]
