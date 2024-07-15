# Bug ID TIDB-19063-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/19063
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              Duplicate key is ignored in insert The insert statement should fail.


## Details
 * Database: tidb-bdc59e6e.tikv
 * Number of scenarios: 2
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
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
   > [2024/07/15 15:21:04.526 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=8]
   > [2024/07/15 15:21:04.532 +00:00] [INFO] [server.go:388] ["new connection"] [conn=9] [remoteAddr=10.88.0.68:51678]
   > [2024/07/15 15:21:04.535 +00:00] [INFO] [session.go:2232] ["CRUCIAL OPERATION"] [conn=9] [schemaVersion=51] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.68]
   > [2024/07/15 15:21:04.542 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164730685390854] [commitTS=451164730685390855]
   > [2024/07/15 15:21:04.544 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:68, Type:drop schema, State:none, SchemaState:none, SchemaID:63, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 15:21:04.492 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/15 15:21:04.545 +00:00] [INFO] [ddl.go:475] ["[ddl] start DDL job"] [job="ID:68, Type:drop schema, State:none, SchemaState:none, SchemaID:63, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 15:21:04.492 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/15 15:21:04.547 +00:00] [INFO] [ddl_worker.go:586] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:68, Type:drop schema, State:none, SchemaState:none, SchemaID:63, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 15:21:04.492 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:21:04.553 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164730698760194] [commitTS=451164730698760195]
   > [2024/07/15 15:21:04.560 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=51] [neededSchemaVersion=52] ["start time"=919.541µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/15 15:21:04.609 +00:00] [INFO] [ddl_worker.go:778] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=52] ["take time"=53.75969ms] [job="ID:68, Type:drop schema, State:running, SchemaState:write only, SchemaID:63, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 15:21:04.492 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:21:04.611 +00:00] [INFO] [ddl_worker.go:586] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:68, Type:drop schema, State:running, SchemaState:write only, SchemaID:63, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 15:21:04.492 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:21:04.618 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164730711605249] [commitTS=451164730711605250]
   > [2024/07/15 15:21:04.626 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=52] [neededSchemaVersion=53] ["start time"=830.562µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/15 15:21:04.675 +00:00] [INFO] [ddl_worker.go:778] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=53] ["take time"=53.635371ms] [job="ID:68, Type:drop schema, State:running, SchemaState:delete only, SchemaID:63, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 15:21:04.492 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:21:04.677 +00:00] [INFO] [ddl_worker.go:586] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:68, Type:drop schema, State:running, SchemaState:delete only, SchemaID:63, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 15:21:04.492 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:21:04.685 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164730724712449] [commitTS=451164730724712450]
   > [2024/07/15 15:21:04.691 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=53] [neededSchemaVersion=54] ["start time"=563.417µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/15 15:21:04.741 +00:00] [INFO] [ddl_worker.go:778] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=54] ["take time"=53.187963ms] [job="ID:68, Type:drop schema, State:done, SchemaState:none, SchemaID:63, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 15:21:04.492 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:21:04.743 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=68] [jobType="drop schema"]
   > [2024/07/15 15:21:04.744 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:68, Type:drop schema, State:synced, SchemaState:none, SchemaID:63, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 15:21:04.492 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:21:04.749 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164730737819649] [commitTS=451164730750926850]
   > [2024/07/15 15:21:04.754 +00:00] [INFO] [ddl.go:507] ["[ddl] DDL job is finished"] [jobID=68]
   > [2024/07/15 15:21:04.754 +00:00] [INFO] [domain.go:643] ["performing DDL change, must reload"]
   > [2024/07/15 15:21:04.756 +00:00] [INFO] [session.go:2232] ["CRUCIAL OPERATION"] [conn=9] [schemaVersion=54] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.68]
   > [2024/07/15 15:21:04.761 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164730750926856] [commitTS=451164730750926857]
   > [2024/07/15 15:21:04.770 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164730750926858] [commitTS=451164730750926859]
   > [2024/07/15 15:21:04.773 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:70, Type:create schema, State:none, SchemaState:none, SchemaID:69, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-15 15:21:04.742 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/15 15:21:04.773 +00:00] [INFO] [ddl.go:475] ["[ddl] start DDL job"] [job="ID:70, Type:create schema, State:none, SchemaState:none, SchemaID:69, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-15 15:21:04.742 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/15 15:21:04.777 +00:00] [INFO] [ddl_worker.go:586] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:70, Type:create schema, State:none, SchemaState:none, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 15:21:04.742 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:21:04.783 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164730750926861] [commitTS=451164730750926862]
   > [2024/07/15 15:21:04.790 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=54] [neededSchemaVersion=55] ["start time"=1.056501ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/15 15:21:04.840 +00:00] [INFO] [ddl_worker.go:778] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=55] ["take time"=53.829463ms] [job="ID:70, Type:create schema, State:done, SchemaState:public, SchemaID:69, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-15 15:21:04.742 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:21:04.843 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:70, Type:create schema, State:synced, SchemaState:public, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 15:21:04.742 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:21:04.847 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164730764034049] [commitTS=451164730777141249]
   > [2024/07/15 15:21:04.852 +00:00] [INFO] [ddl.go:507] ["[ddl] DDL job is finished"] [jobID=70]
   > [2024/07/15 15:21:04.852 +00:00] [INFO] [domain.go:643] ["performing DDL change, must reload"]
   > [2024/07/15 15:21:04.855 +00:00] [INFO] [session.go:2232] ["CRUCIAL OPERATION"] [conn=9] [schemaVersion=55] [cur_db=testdb] [sql="create table t ( c_int int, c_string varchar(40) collate utf8mb4_bin , primary key (c_string), unique key (c_int));"] [user=root@10.88.0.68]
   > [2024/07/15 15:21:04.861 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164730777141256] [commitTS=451164730777141257]
   > [2024/07/15 15:21:04.868 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164730777141258] [commitTS=451164730777141259]
   > [2024/07/15 15:21:04.871 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:72, Type:create table, State:none, SchemaState:none, SchemaID:69, TableID:71, RowCount:0, ArgLen:1, start time: 2024-07-15 15:21:04.842 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/15 15:21:04.871 +00:00] [INFO] [ddl.go:475] ["[ddl] start DDL job"] [job="ID:72, Type:create table, State:none, SchemaState:none, SchemaID:69, TableID:71, RowCount:0, ArgLen:1, start time: 2024-07-15 15:21:04.842 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t ( c_int int, c_string varchar(40) collate utf8mb4_bin , primary key (c_string), unique key (c_int));"]
   > [2024/07/15 15:21:04.874 +00:00] [INFO] [ddl_worker.go:586] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:72, Type:create table, State:none, SchemaState:none, SchemaID:69, TableID:71, RowCount:0, ArgLen:0, start time: 2024-07-15 15:21:04.842 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:21:04.882 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164730777141261] [commitTS=451164730777141263]
   > [2024/07/15 15:21:04.890 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=55] [neededSchemaVersion=56] ["start time"=1.899286ms] [phyTblIDs="[71]"] [actionTypes="[8]"]
   > [2024/07/15 15:21:04.938 +00:00] [INFO] [ddl_worker.go:778] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=56] ["take time"=53.422702ms] [job="ID:72, Type:create table, State:done, SchemaState:public, SchemaID:69, TableID:71, RowCount:0, ArgLen:1, start time: 2024-07-15 15:21:04.842 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:21:04.942 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:72, Type:create table, State:synced, SchemaState:public, SchemaID:69, TableID:71, RowCount:0, ArgLen:0, start time: 2024-07-15 15:21:04.842 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:21:04.947 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164730790510595] [commitTS=451164730803355649]
   > [2024/07/15 15:21:04.952 +00:00] [INFO] [ddl.go:507] ["[ddl] DDL job is finished"] [jobID=72]
   > [2024/07/15 15:21:04.954 +00:00] [INFO] [domain.go:643] ["performing DDL change, must reload"]
   > [2024/07/15 15:21:04.954 +00:00] [INFO] [split_region.go:59] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=748000000000000047]
   > [2024/07/15 15:21:04.955 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:56416] [split_keys="key 7480000000000000FF4700000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/15 15:21:04.955 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=52] [peer-ids="[53]"]
   > [2024/07/15 15:21:04.955 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF4100000000000000F8 region_epoch { conf_ver: 1 version: 25 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 52 new_peer_ids: 53]"] [region_id=2]
   > [2024/07/15 15:21:04.956 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=9]
   > [2024/07/15 15:21:04.957 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF4700000000000000F8 new_region_id: 52 new_peer_ids: 53 } right_derive: true }"] [index=71] [term=6] [peer_id=3] [region_id=2]
   > [2024/07/15 15:21:04.957 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF4700000000000000F8"] [region="id: 2 start_key: 7480000000000000FF4100000000000000F8 region_epoch { conf_ver: 1 version: 25 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/07/15 15:21:04.959 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/15 15:21:04.959 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=2]
   > [2024/07/15 15:21:04.959 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/07/15 15:21:04.960 +00:00] [INFO] [split_region.go:156] ["batch split regions complete"] ["batch region ID"=2] ["first at"=748000000000000047] ["first new region left"="{Id:52 StartKey:7480000000000000ff4100000000000000f8 EndKey:7480000000000000ff4700000000000000f8 RegionEpoch:{ConfVer:1 Version:26} Peers:[id:53 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/15 15:21:04.960 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(47)] [region_id=2] [store_id=Some(1)]
   > [2024/07/15 15:21:04.960 +00:00] [INFO] [split_region.go:205] ["split regions complete"] ["region count"=1] ["region IDs"="[52]"]
   > [2024/07/15 15:21:04.960 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 52 start_key: 7480000000000000FF4100000000000000F8 end_key: 7480000000000000FF4700000000000000F8 region_epoch { conf_ver: 1 version: 26 } peers { id: 53 store_id: 1 }"] [region_id=52]
   > [2024/07/15 15:21:04.960 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF4100000000000000F8} -> {7480000000000000FF4700000000000000F8}, EndKey:{}"] [old-version=25] [new-version=26]
   > [2024/07/15 15:21:04.960 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF4700000000000000F8 region_epoch { conf_ver: 1 version: 26 } peers { id: 3 store_id: 1 }"]
   > [2024/07/15 15:21:04.960 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=53] [region_id=52]
   > [2024/07/15 15:21:04.960 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 2 start_key: 7480000000000000FF4700000000000000F8 region_epoch { conf_ver: 1 version: 26 } peers { id: 3 store_id: 1 } }"]
   > [2024/07/15 15:21:04.960 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=2] [origin="id:52 start_key:\"7480000000000000FF4100000000000000F8\" end_key:\"7480000000000000FF4700000000000000F8\" region_epoch:<conf_ver:1 version:26 > peers:<id:53 store_id:1 >"] [total=1]
   > [2024/07/15 15:21:04.960 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 2 start_key: 7480000000000000FF4700000000000000F8 region_epoch { conf_ver: 1 version: 26 } peers { id: 3 store_id: 1 }"]
   > [2024/07/15 15:21:04.960 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {53} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=53] [region_id=52]
   > [2024/07/15 15:21:04.960 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=53] [region_id=52]
   > [2024/07/15 15:21:04.960 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {53} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=53] [region_id=52]
   > [2024/07/15 15:21:04.960 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 53."] [id=53] [raft_id=53] [region_id=52]
   > [2024/07/15 15:21:04.960 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=53] [region_id=52]
   > [2024/07/15 15:21:04.961 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=53] [region_id=52]
   > [2024/07/15 15:21:04.961 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=53] [region_id=52]
   > [2024/07/15 15:21:04.961 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=53] [region_id=52]
   > [2024/07/15 15:21:04.961 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803828] [region_id=52]
   > [2024/07/15 15:21:04.961 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=71] [observe_id=ObserveId(49)] [region=2]
   > [2024/07/15 15:21:04.961 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=52]
   > [2024/07/15 15:21:04.962 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 52 start_key: 7480000000000000FF4100000000000000F8 end_key: 7480000000000000FF4700000000000000F8 region_epoch { conf_ver: 1 version: 26 } peers { id: 53 store_id: 1 }"]
   > [2024/07/15 15:21:04.962 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(50)] [region=52]
   > [2024/07/15 15:21:05.967 +00:00] [INFO] [server.go:388] ["new connection"] [conn=10] [remoteAddr=10.88.0.68:51682]
   > [2024/07/15 15:21:05.976 +00:00] [INFO] [set.go:216] ["set session var"] [conn=10] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/07/15 15:21:05.991 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164731065499657] [commitTS=451164731065499658]
   > [2024/07/15 15:21:06.001 +00:00] [INFO] [set.go:216] ["set global var"] [conn=10] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/07/15 15:21:06.009 +00:00] [INFO] [set.go:216] ["set global var"] [conn=10] [name=transaction_isolation] [val=READ-COMMITTED]
   > [2024/07/15 15:21:06.586 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164731223048193] [commitTS=451164731223048194]
   > [2024/07/15 15:21:08.369 +00:00] [INFO] [session.go:2232] ["CRUCIAL OPERATION"] [conn=10] [schemaVersion=56] [cur_db=testdb] [sql=" drop table t;"] [user=root@10.88.0.68]
   > [2024/07/15 15:21:08.377 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164731694907395] [commitTS=451164731694907396]
   > [2024/07/15 15:21:08.380 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:73, Type:drop table, State:none, SchemaState:none, SchemaID:69, TableID:71, RowCount:0, ArgLen:0, start time: 2024-07-15 15:21:08.343 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/15 15:21:08.381 +00:00] [INFO] [ddl.go:475] ["[ddl] start DDL job"] [job="ID:73, Type:drop table, State:none, SchemaState:none, SchemaID:69, TableID:71, RowCount:0, ArgLen:0, start time: 2024-07-15 15:21:08.343 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query=" drop table t;"]
   > [2024/07/15 15:21:08.385 +00:00] [INFO] [ddl_worker.go:586] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:73, Type:drop table, State:none, SchemaState:none, SchemaID:69, TableID:71, RowCount:0, ArgLen:0, start time: 2024-07-15 15:21:08.343 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:21:08.394 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164731694907398] [commitTS=451164731708014593]
   > [2024/07/15 15:21:08.402 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=56] [neededSchemaVersion=57] ["start time"=786.841µs] [phyTblIDs="[71]"] [actionTypes="[16]"]
   > [2024/07/15 15:21:08.452 +00:00] [INFO] [ddl_worker.go:778] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=57] ["take time"=54.6932ms] [job="ID:73, Type:drop table, State:running, SchemaState:write only, SchemaID:69, TableID:71, RowCount:0, ArgLen:0, start time: 2024-07-15 15:21:08.343 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:21:08.454 +00:00] [INFO] [ddl_worker.go:586] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:73, Type:drop table, State:running, SchemaState:write only, SchemaID:69, TableID:71, RowCount:0, ArgLen:0, start time: 2024-07-15 15:21:08.343 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:21:08.464 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164731721121793] [commitTS=451164731721121794]
   > [2024/07/15 15:21:08.471 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=57] [neededSchemaVersion=58] ["start time"=734.668µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/15 15:21:08.522 +00:00] [INFO] [ddl_worker.go:778] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=58] ["take time"=54.812071ms] [job="ID:73, Type:drop table, State:running, SchemaState:delete only, SchemaID:69, TableID:71, RowCount:0, ArgLen:0, start time: 2024-07-15 15:21:08.343 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:21:08.524 +00:00] [INFO] [ddl_worker.go:586] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:73, Type:drop table, State:running, SchemaState:delete only, SchemaID:69, TableID:71, RowCount:0, ArgLen:0, start time: 2024-07-15 15:21:08.343 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:21:08.535 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164731733966849] [commitTS=451164731733966850]
   > [2024/07/15 15:21:08.544 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=58] [neededSchemaVersion=59] ["start time"=459.98µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/15 15:21:08.595 +00:00] [INFO] [ddl_worker.go:778] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=59] ["take time"=56.834349ms] [job="ID:73, Type:drop table, State:done, SchemaState:none, SchemaID:69, TableID:71, RowCount:0, ArgLen:2, start time: 2024-07-15 15:21:08.343 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:21:08.596 +00:00] [INFO] [delete_range.go:350] ["[ddl] insert into delete-range table"] [jobID=73] [elementID=71]
   > [2024/07/15 15:21:08.601 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=73] [jobType="drop table"]
   > [2024/07/15 15:21:08.602 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:73, Type:drop table, State:synced, SchemaState:none, SchemaID:69, TableID:71, RowCount:0, ArgLen:2, start time: 2024-07-15 15:21:08.343 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:21:08.606 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164731760181249] [commitTS=451164731760181253]
   > [2024/07/15 15:21:08.610 +00:00] [INFO] [ddl.go:507] ["[ddl] DDL job is finished"] [jobID=73]
   > [2024/07/15 15:21:08.610 +00:00] [INFO] [domain.go:643] ["performing DDL change, must reload"]
   > [2024/07/15 15:21:18.672 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=10]

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
   > [2024/07/15 15:21:20.361 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=11]
   > [2024/07/15 15:21:20.363 +00:00] [INFO] [server.go:388] ["new connection"] [conn=12] [remoteAddr=10.88.0.68:54446]
   > [2024/07/15 15:21:20.365 +00:00] [INFO] [session.go:2232] ["CRUCIAL OPERATION"] [conn=12] [schemaVersion=67] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.68]
   > [2024/07/15 15:21:20.370 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164734840373254] [commitTS=451164734840373255]
   > [2024/07/15 15:21:20.373 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:80, Type:drop schema, State:none, SchemaState:none, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 15:21:20.342 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/15 15:21:20.373 +00:00] [INFO] [ddl.go:475] ["[ddl] start DDL job"] [job="ID:80, Type:drop schema, State:none, SchemaState:none, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 15:21:20.342 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/15 15:21:20.376 +00:00] [INFO] [ddl_worker.go:586] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:80, Type:drop schema, State:none, SchemaState:none, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 15:21:20.342 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:21:20.382 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164734840373257] [commitTS=451164734840373258]
   > [2024/07/15 15:21:20.389 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=67] [neededSchemaVersion=68] ["start time"=486.24µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/15 15:21:20.438 +00:00] [INFO] [ddl_worker.go:778] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=68] ["take time"=52.892112ms] [job="ID:80, Type:drop schema, State:running, SchemaState:write only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 15:21:20.342 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:21:20.439 +00:00] [INFO] [ddl_worker.go:586] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:80, Type:drop schema, State:running, SchemaState:write only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 15:21:20.342 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:21:20.447 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164734853480449] [commitTS=451164734866849793]
   > [2024/07/15 15:21:20.454 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=68] [neededSchemaVersion=69] ["start time"=766.028µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/15 15:21:20.504 +00:00] [INFO] [ddl_worker.go:778] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=69] ["take time"=53.505047ms] [job="ID:80, Type:drop schema, State:running, SchemaState:delete only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 15:21:20.342 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:21:20.506 +00:00] [INFO] [ddl_worker.go:586] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:80, Type:drop schema, State:running, SchemaState:delete only, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 15:21:20.342 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:21:20.519 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164734879694849] [commitTS=451164734879694850]
   > [2024/07/15 15:21:20.530 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=69] [neededSchemaVersion=70] ["start time"=1.165804ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/15 15:21:20.578 +00:00] [INFO] [ddl_worker.go:778] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=70] ["take time"=55.668055ms] [job="ID:80, Type:drop schema, State:done, SchemaState:none, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 15:21:20.342 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:21:20.580 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=80] [jobType="drop schema"]
   > [2024/07/15 15:21:20.581 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:80, Type:drop schema, State:synced, SchemaState:none, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 15:21:20.342 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:21:20.585 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164734893064193] [commitTS=451164734893064195]
   > [2024/07/15 15:21:20.590 +00:00] [INFO] [ddl.go:507] ["[ddl] DDL job is finished"] [jobID=80]
   > [2024/07/15 15:21:20.590 +00:00] [INFO] [domain.go:643] ["performing DDL change, must reload"]
   > [2024/07/15 15:21:20.591 +00:00] [INFO] [session.go:2232] ["CRUCIAL OPERATION"] [conn=12] [schemaVersion=70] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.68]
   > [2024/07/15 15:21:20.595 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164734905909249] [commitTS=451164734905909250]
   > [2024/07/15 15:21:20.602 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164734905909251] [commitTS=451164734905909252]
   > [2024/07/15 15:21:20.605 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:82, Type:create schema, State:none, SchemaState:none, SchemaID:81, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-15 15:21:20.592 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/15 15:21:20.605 +00:00] [INFO] [ddl.go:475] ["[ddl] start DDL job"] [job="ID:82, Type:create schema, State:none, SchemaState:none, SchemaID:81, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-15 15:21:20.592 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/15 15:21:20.608 +00:00] [INFO] [ddl_worker.go:586] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:82, Type:create schema, State:none, SchemaState:none, SchemaID:81, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 15:21:20.592 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:21:20.615 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164734905909254] [commitTS=451164734905909255]
   > [2024/07/15 15:21:20.627 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=70] [neededSchemaVersion=71] ["start time"=826.93µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/15 15:21:20.677 +00:00] [INFO] [ddl_worker.go:778] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=71] ["take time"=54.623008ms] [job="ID:82, Type:create schema, State:done, SchemaState:public, SchemaID:81, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-15 15:21:20.592 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:21:20.680 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:82, Type:create schema, State:synced, SchemaState:public, SchemaID:81, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 15:21:20.592 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:21:20.684 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164734919016449] [commitTS=451164734919016450]
   > [2024/07/15 15:21:20.688 +00:00] [INFO] [ddl.go:507] ["[ddl] DDL job is finished"] [jobID=82]
   > [2024/07/15 15:21:20.688 +00:00] [INFO] [domain.go:643] ["performing DDL change, must reload"]
   > [2024/07/15 15:21:20.691 +00:00] [INFO] [session.go:2232] ["CRUCIAL OPERATION"] [conn=12] [schemaVersion=71] [cur_db=testdb] [sql="create table t ( c_int int, c_string varchar(40) collate utf8mb4_bin , primary key (c_string), unique key (c_int));"] [user=root@10.88.0.68]
   > [2024/07/15 15:21:20.695 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164734919016457] [commitTS=451164734932385793]
   > [2024/07/15 15:21:20.703 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164734932385794] [commitTS=451164734932385795]
   > [2024/07/15 15:21:20.706 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:84, Type:create table, State:none, SchemaState:none, SchemaID:81, TableID:83, RowCount:0, ArgLen:1, start time: 2024-07-15 15:21:20.693 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/15 15:21:20.707 +00:00] [INFO] [ddl.go:475] ["[ddl] start DDL job"] [job="ID:84, Type:create table, State:none, SchemaState:none, SchemaID:81, TableID:83, RowCount:0, ArgLen:1, start time: 2024-07-15 15:21:20.693 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t ( c_int int, c_string varchar(40) collate utf8mb4_bin , primary key (c_string), unique key (c_int));"]
   > [2024/07/15 15:21:20.710 +00:00] [INFO] [ddl_worker.go:586] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:84, Type:create table, State:none, SchemaState:none, SchemaID:81, TableID:83, RowCount:0, ArgLen:0, start time: 2024-07-15 15:21:20.693 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:21:20.716 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164734932385797] [commitTS=451164734932385799]
   > [2024/07/15 15:21:20.725 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=71] [neededSchemaVersion=72] ["start time"=1.874841ms] [phyTblIDs="[83]"] [actionTypes="[8]"]
   > [2024/07/15 15:21:20.774 +00:00] [INFO] [ddl_worker.go:778] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=72] ["take time"=54.198857ms] [job="ID:84, Type:create table, State:done, SchemaState:public, SchemaID:81, TableID:83, RowCount:0, ArgLen:1, start time: 2024-07-15 15:21:20.693 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:21:20.777 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:84, Type:create table, State:synced, SchemaState:public, SchemaID:81, TableID:83, RowCount:0, ArgLen:0, start time: 2024-07-15 15:21:20.693 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:21:20.782 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164734945492993] [commitTS=451164734945492994]
   > [2024/07/15 15:21:20.787 +00:00] [INFO] [ddl.go:507] ["[ddl] DDL job is finished"] [jobID=84]
   > [2024/07/15 15:21:20.789 +00:00] [INFO] [domain.go:643] ["performing DDL change, must reload"]
   > [2024/07/15 15:21:20.789 +00:00] [INFO] [split_region.go:59] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=748000000000000053]
   > [2024/07/15 15:21:20.789 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:56376] [split_keys="key 7480000000000000FF5300000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/15 15:21:20.790 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=56] [peer-ids="[57]"]
   > [2024/07/15 15:21:20.790 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF4D00000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 56 new_peer_ids: 57]"] [region_id=2]
   > [2024/07/15 15:21:20.791 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=12]
   > [2024/07/15 15:21:20.792 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF5300000000000000F8 new_region_id: 56 new_peer_ids: 57 } right_derive: true }"] [index=80] [term=6] [peer_id=3] [region_id=2]
   > [2024/07/15 15:21:20.792 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF5300000000000000F8"] [region="id: 2 start_key: 7480000000000000FF4D00000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/07/15 15:21:20.794 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/15 15:21:20.794 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=2]
   > [2024/07/15 15:21:20.794 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/07/15 15:21:20.794 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(51)] [region_id=2] [store_id=Some(1)]
   > [2024/07/15 15:21:20.794 +00:00] [INFO] [split_region.go:156] ["batch split regions complete"] ["batch region ID"=2] ["first at"=748000000000000053] ["first new region left"="{Id:56 StartKey:7480000000000000ff4d00000000000000f8 EndKey:7480000000000000ff5300000000000000f8 RegionEpoch:{ConfVer:1 Version:28} Peers:[id:57 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/15 15:21:20.794 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF5300000000000000F8 region_epoch { conf_ver: 1 version: 28 } peers { id: 3 store_id: 1 }"]
   > [2024/07/15 15:21:20.794 +00:00] [INFO] [split_region.go:205] ["split regions complete"] ["region count"=1] ["region IDs"="[56]"]
   > [2024/07/15 15:21:20.794 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF4D00000000000000F8} -> {7480000000000000FF5300000000000000F8}, EndKey:{}"] [old-version=27] [new-version=28]
   > [2024/07/15 15:21:20.794 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 56 start_key: 7480000000000000FF4D00000000000000F8 end_key: 7480000000000000FF5300000000000000F8 region_epoch { conf_ver: 1 version: 28 } peers { id: 57 store_id: 1 }"] [region_id=56]
   > [2024/07/15 15:21:20.794 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=2] [origin="id:56 start_key:\"7480000000000000FF4D00000000000000F8\" end_key:\"7480000000000000FF5300000000000000F8\" region_epoch:<conf_ver:1 version:28 > peers:<id:57 store_id:1 >"] [total=1]
   > [2024/07/15 15:21:20.794 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=57] [region_id=56]
   > [2024/07/15 15:21:20.794 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 2 start_key: 7480000000000000FF5300000000000000F8 region_epoch { conf_ver: 1 version: 28 } peers { id: 3 store_id: 1 } }"]
   > [2024/07/15 15:21:20.794 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 2 start_key: 7480000000000000FF5300000000000000F8 region_epoch { conf_ver: 1 version: 28 } peers { id: 3 store_id: 1 }"]
   > [2024/07/15 15:21:20.795 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {57} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=57] [region_id=56]
   > [2024/07/15 15:21:20.795 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=57] [region_id=56]
   > [2024/07/15 15:21:20.795 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {57} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=57] [region_id=56]
   > [2024/07/15 15:21:20.795 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 57."] [id=57] [raft_id=57] [region_id=56]
   > [2024/07/15 15:21:20.795 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=57] [region_id=56]
   > [2024/07/15 15:21:20.795 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=57] [region_id=56]
   > [2024/07/15 15:21:20.795 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=57] [region_id=56]
   > [2024/07/15 15:21:20.795 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=57] [region_id=56]
   > [2024/07/15 15:21:20.795 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803832] [region_id=56]
   > [2024/07/15 15:21:20.795 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=80] [observe_id=ObserveId(53)] [region=2]
   > [2024/07/15 15:21:20.796 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=56]
   > [2024/07/15 15:21:20.796 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 56 start_key: 7480000000000000FF4D00000000000000F8 end_key: 7480000000000000FF5300000000000000F8 region_epoch { conf_ver: 1 version: 28 } peers { id: 57 store_id: 1 }"]
   > [2024/07/15 15:21:20.796 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(54)] [region=56]
   > [2024/07/15 15:21:21.802 +00:00] [INFO] [server.go:388] ["new connection"] [conn=13] [remoteAddr=10.88.0.68:54456]
   > [2024/07/15 15:21:21.814 +00:00] [INFO] [set.go:216] ["set session var"] [conn=13] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/07/15 15:21:21.834 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164735220744200] [commitTS=451164735220744201]
   > [2024/07/15 15:21:22.104 +00:00] [INFO] [tidb.go:217] ["rollbackTxn for ddl/autocommit failed"]
   > [2024/07/15 15:21:22.104 +00:00] [ERROR] [conn.go:744] ["command dispatched failed"] [conn=13] [connInfo="id:13, addr:10.88.0.68:54456 status:10, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:0, autocommit:1"] [sql=" insert into t values (21,'black warlock'), (22, 'dark sloth'), (21,  'cyan song') on duplicate key update c_int = c_int + 1, c_string = concat(c_int, ':', c_string);"] [txn_mode=PESSIMISTIC] [err="[kv:1062]Duplicate entry '22' for key 'c_int'"]
   > [2024/07/15 15:21:22.701 +00:00] [INFO] [session.go:2232] ["CRUCIAL OPERATION"] [conn=13] [schemaVersion=72] [cur_db=testdb] [sql=" drop table t;"] [user=root@10.88.0.68]
   > [2024/07/15 15:21:22.715 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164735456411651] [commitTS=451164735456411652]
   > [2024/07/15 15:21:22.718 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:85, Type:drop table, State:none, SchemaState:none, SchemaID:81, TableID:83, RowCount:0, ArgLen:0, start time: 2024-07-15 15:21:22.692 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/15 15:21:22.718 +00:00] [INFO] [ddl.go:475] ["[ddl] start DDL job"] [job="ID:85, Type:drop table, State:none, SchemaState:none, SchemaID:81, TableID:83, RowCount:0, ArgLen:0, start time: 2024-07-15 15:21:22.692 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query=" drop table t;"]
   > [2024/07/15 15:21:22.722 +00:00] [INFO] [ddl_worker.go:586] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:85, Type:drop table, State:none, SchemaState:none, SchemaID:81, TableID:83, RowCount:0, ArgLen:0, start time: 2024-07-15 15:21:22.692 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:21:22.732 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164735456411654] [commitTS=451164735456411655]
   > [2024/07/15 15:21:22.739 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=72] [neededSchemaVersion=73] ["start time"=763.234µs] [phyTblIDs="[83]"] [actionTypes="[16]"]
   > [2024/07/15 15:21:22.789 +00:00] [INFO] [ddl_worker.go:778] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=73] ["take time"=54.559033ms] [job="ID:85, Type:drop table, State:running, SchemaState:write only, SchemaID:81, TableID:83, RowCount:0, ArgLen:0, start time: 2024-07-15 15:21:22.692 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:21:22.792 +00:00] [INFO] [ddl_worker.go:586] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:85, Type:drop table, State:running, SchemaState:write only, SchemaID:81, TableID:83, RowCount:0, ArgLen:0, start time: 2024-07-15 15:21:22.692 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:21:22.802 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164735469518849] [commitTS=451164735482626049]
   > [2024/07/15 15:21:22.809 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=73] [neededSchemaVersion=74] ["start time"=653.093µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/15 15:21:22.860 +00:00] [INFO] [ddl_worker.go:778] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=74] ["take time"=54.629573ms] [job="ID:85, Type:drop table, State:running, SchemaState:delete only, SchemaID:81, TableID:83, RowCount:0, ArgLen:0, start time: 2024-07-15 15:21:22.692 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:21:22.862 +00:00] [INFO] [ddl_worker.go:586] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:85, Type:drop table, State:running, SchemaState:delete only, SchemaID:81, TableID:83, RowCount:0, ArgLen:0, start time: 2024-07-15 15:21:22.692 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:21:22.873 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164735495733249] [commitTS=451164735495733250]
   > [2024/07/15 15:21:22.880 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=74] [neededSchemaVersion=75] ["start time"=596.661µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/15 15:21:22.931 +00:00] [INFO] [ddl_worker.go:778] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=75] ["take time"=54.431082ms] [job="ID:85, Type:drop table, State:done, SchemaState:none, SchemaID:81, TableID:83, RowCount:0, ArgLen:2, start time: 2024-07-15 15:21:22.692 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:21:22.934 +00:00] [INFO] [delete_range.go:350] ["[ddl] insert into delete-range table"] [jobID=85] [elementID=83]
   > [2024/07/15 15:21:22.942 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=85] [jobType="drop table"]
   > [2024/07/15 15:21:22.944 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:85, Type:drop table, State:synced, SchemaState:none, SchemaID:81, TableID:83, RowCount:0, ArgLen:2, start time: 2024-07-15 15:21:22.692 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 15:21:22.950 +00:00] [WARN] [2pc.go:1024] ["schemaLeaseChecker is not set for this transaction, schema check skipped"] [connID=0] [startTS=451164735508840451] [commitTS=451164735521947649]
   > [2024/07/15 15:21:22.955 +00:00] [INFO] [ddl.go:507] ["[ddl] DDL job is finished"] [jobID=85]
   > [2024/07/15 15:21:22.955 +00:00] [INFO] [domain.go:643] ["performing DDL change, must reload"]
   > [2024/07/15 15:21:28.849 +00:00] [INFO] [store_config.go:201] ["sync the store config successful"] [store-address=127.0.0.1:20180] [store-config="{\n  \"coprocessor\": {\n    \"region-max-size\": \"144MiB\",\n    \"region-split-size\": \"96MiB\",\n    \"region-max-keys\": 1440000,\n    \"region-split-keys\": 960000,\n    \"enable-region-bucket\": false,\n    \"region-bucket-size\": \"96MiB\"\n  }\n}"]
   > [2024/07/15 15:21:33.005 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=13]
