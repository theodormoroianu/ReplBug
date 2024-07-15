# Bug ID TIDB-17797-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/17797
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              The error message is not correct.


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
     - Affected rows / Warnings: 0 / 0
 * Instruction #1:
     - Instruction:  BEGIN PESSIMISTIC;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  BEGIN PESSIMISTIC;
     - Transaction: conn_1
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 0 / 0
 * Instruction #3:
     - Instruction:  UPDATE t1 SET t='new...' WHERE id = 1;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 1 / 0
 * Instruction #4:
     - Instruction:  UPDATE t1 SET t='newval' WHERE id = 1;
     - Transaction: conn_1
     - Output: ERROR: 1205 (HY000): Lock wait timeout exceeded; try restarting transaction
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0

 * Container logs:
   > [2024/07/15 12:50:53.800 +00:00] [INFO] [server.go:388] ["new connection"] [conn=3] [remoteAddr=10.88.0.53:45464]
   > [2024/07/15 12:50:53.801 +00:00] [INFO] [session.go:2210] ["CRUCIAL OPERATION"] [conn=3] [schemaVersion=22] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.53]
   > [2024/07/15 12:50:53.802 +00:00] [INFO] [session.go:2210] ["CRUCIAL OPERATION"] [conn=3] [schemaVersion=22] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.53]
   > [2024/07/15 12:50:53.842 +00:00] [INFO] [ddl_worker.go:253] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-15 12:50:53.815 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/15 12:50:53.842 +00:00] [INFO] [ddl.go:500] ["[ddl] start DDL job"] [job="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-15 12:50:53.815 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/15 12:50:53.847 +00:00] [INFO] [ddl_worker.go:568] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 12:50:53.815 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 12:50:53.869 +00:00] [INFO] [domain.go:126] ["diff load InfoSchema success"] [usedSchemaVersion=22] [neededSchemaVersion=23] ["start time"=1.432811ms] [tblIDs="[]"]
   > [2024/07/15 12:50:53.880 +00:00] [INFO] [hot_region_config.go:441] ["query supported changed"] [last-query-support=false] [cluster-version=6.4.0] [config="{\"min-hot-byte-rate\":100,\"min-hot-key-rate\":10,\"min-hot-query-rate\":10,\"max-zombie-rounds\":3,\"max-peer-number\":1000,\"byte-rate-rank-step-ratio\":0.05,\"key-rate-rank-step-ratio\":0.05,\"query-rate-rank-step-ratio\":0.05,\"count-rank-step-ratio\":0.01,\"great-dec-ratio\":0.95,\"minor-dec-ratio\":0.99,\"src-tolerance-ratio\":1.05,\"dst-tolerance-ratio\":1.05,\"write-leader-priorities\":[\"query\",\"byte\"],\"write-peer-priorities\":[\"byte\",\"key\"],\"read-priorities\":[\"query\",\"byte\"],\"strict-picking-store\":\"true\",\"enable-for-tiflash\":\"true\",\"rank-formula-version\":\"v2\",\"forbid-rw-type\":\"none\"}"] [valid-config="{\"min-hot-byte-rate\":100,\"min-hot-key-rate\":10,\"min-hot-query-rate\":10,\"max-zombie-rounds\":3,\"max-peer-number\":1000,\"byte-rate-rank-step-ratio\":0.05,\"key-rate-rank-step-ratio\":0.05,\"query-rate-rank-step-ratio\":0.05,\"count-rank-step-ratio\":0.01,\"great-dec-ratio\":0.95,\"minor-dec-ratio\":0.99,\"src-tolerance-ratio\":1.05,\"dst-tolerance-ratio\":1.05,\"write-leader-priorities\":[\"key\",\"byte\"],\"write-peer-priorities\":[\"byte\",\"key\"],\"read-priorities\":[\"byte\",\"key\"],\"strict-picking-store\":\"true\",\"enable-for-tiflash\":\"true\",\"rank-formula-version\":\"v2\"}"]
   > [2024/07/15 12:50:53.918 +00:00] [INFO] [ddl_worker.go:759] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=23] ["take time"=56.181148ms] [job="ID:46, Type:create schema, State:done, SchemaState:public, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-15 12:50:53.815 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 12:50:53.921 +00:00] [INFO] [ddl_worker.go:359] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:46, Type:create schema, State:synced, SchemaState:public, SchemaID:45, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-15 12:50:53.815 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 12:50:53.935 +00:00] [INFO] [ddl.go:532] ["[ddl] DDL job is finished"] [jobID=46]
   > [2024/07/15 12:50:53.935 +00:00] [INFO] [domain.go:631] ["performing DDL change, must reload"]
   > [2024/07/15 12:50:53.938 +00:00] [INFO] [session.go:2210] ["CRUCIAL OPERATION"] [conn=3] [schemaVersion=23] [cur_db=testdb] [sql="CREATE TABLE t1 (\n id int not null primary key auto_increment,\n t varchar(100)\n);"] [user=root@10.88.0.53]
   > [2024/07/15 12:50:53.965 +00:00] [INFO] [ddl_worker.go:253] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-07-15 12:50:53.916 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/15 12:50:53.965 +00:00] [INFO] [ddl.go:500] ["[ddl] start DDL job"] [job="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-07-15 12:50:53.916 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE t1 (\n id int not null primary key auto_increment,\n t varchar(100)\n);"]
   > [2024/07/15 12:50:53.969 +00:00] [INFO] [ddl_worker.go:568] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-15 12:50:53.916 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 12:50:53.999 +00:00] [INFO] [domain.go:126] ["diff load InfoSchema success"] [usedSchemaVersion=23] [neededSchemaVersion=24] ["start time"=1.380081ms] [tblIDs="[47]"]
   > [2024/07/15 12:50:54.049 +00:00] [INFO] [ddl_worker.go:759] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=24] ["take time"=57.268729ms] [job="ID:48, Type:create table, State:done, SchemaState:public, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-07-15 12:50:53.916 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 12:50:54.052 +00:00] [INFO] [ddl_worker.go:359] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:48, Type:create table, State:synced, SchemaState:public, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-15 12:50:53.916 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/15 12:50:54.066 +00:00] [INFO] [ddl.go:532] ["[ddl] DDL job is finished"] [jobID=48]
   > [2024/07/15 12:50:54.068 +00:00] [INFO] [domain.go:631] ["performing DDL change, must reload"]
   > [2024/07/15 12:50:54.068 +00:00] [INFO] [split_region.go:56] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=74800000000000002f]
   > [2024/07/15 12:50:54.069 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:47598] [split_keys="key 7480000000000000FF2F00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/15 12:50:54.070 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=44] [peer-ids="[45]"]
   > [2024/07/15 12:50:54.070 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF2B00000000000000F8 region_epoch { conf_ver: 1 version: 21 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 44 new_peer_ids: 45]"] [region_id=2]
   > [2024/07/15 12:50:54.074 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF2F00000000000000F8 new_region_id: 44 new_peer_ids: 45 } right_derive: true }"] [index=52] [term=6] [peer_id=3] [region_id=2]
   > [2024/07/15 12:50:54.074 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF2F00000000000000F8"] [region="id: 2 start_key: 7480000000000000FF2B00000000000000F8 region_epoch { conf_ver: 1 version: 21 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/07/15 12:50:54.079 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/15 12:50:54.079 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=2]
   > [2024/07/15 12:50:54.079 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(39)] [region_id=2] [store_id=Some(1)]
   > [2024/07/15 12:50:54.079 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/07/15 12:50:54.079 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 3 store_id: 1 }"]
   > [2024/07/15 12:50:54.079 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 44 start_key: 7480000000000000FF2B00000000000000F8 end_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 45 store_id: 1 }"] [region_id=44]
   > [2024/07/15 12:50:54.079 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=45] [region_id=44]
   > [2024/07/15 12:50:54.079 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 2 start_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 3 store_id: 1 } }"]
   > [2024/07/15 12:50:54.079 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 2 start_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 3 store_id: 1 }"]
   > [2024/07/15 12:50:54.079 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {45} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=45] [region_id=44]
   > [2024/07/15 12:50:54.079 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=45] [region_id=44]
   > [2024/07/15 12:50:54.079 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF2B00000000000000F8} -> {7480000000000000FF2F00000000000000F8}, EndKey:{}"] [old-version=21] [new-version=22]
   > [2024/07/15 12:50:54.079 +00:00] [INFO] [split_region.go:153] ["batch split regions complete"] ["batch region ID"=2] ["first at"=74800000000000002f] ["first new region left"="{Id:44 StartKey:7480000000000000ff2b00000000000000f8 EndKey:7480000000000000ff2f00000000000000f8 RegionEpoch:{ConfVer:1 Version:22} Peers:[id:45 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/15 12:50:54.079 +00:00] [INFO] [split_region.go:205] ["split regions complete"] ["region count"=1] ["region IDs"="[44]"]
   > [2024/07/15 12:50:54.079 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {45} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=45] [region_id=44]
   > [2024/07/15 12:50:54.080 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 45."] [id=45] [raft_id=45] [region_id=44]
   > [2024/07/15 12:50:54.080 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=45] [region_id=44]
   > [2024/07/15 12:50:54.080 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=45] [region_id=44]
   > [2024/07/15 12:50:54.080 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=45] [region_id=44]
   > [2024/07/15 12:50:54.080 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=2] [origin="id:44 start_key:\"7480000000000000FF2B00000000000000F8\" end_key:\"7480000000000000FF2F00000000000000F8\" region_epoch:<conf_ver:1 version:22 > peers:<id:45 store_id:1 >"] [total=1]
   > [2024/07/15 12:50:54.080 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=45] [region_id=44]
   > [2024/07/15 12:50:54.080 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803820] [region_id=44]
   > [2024/07/15 12:50:54.080 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=52] [observe_id=ObserveId(41)] [region=2]
   > [2024/07/15 12:50:54.080 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=44]
   > [2024/07/15 12:50:54.084 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 44 start_key: 7480000000000000FF2B00000000000000F8 end_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 45 store_id: 1 }"]
   > [2024/07/15 12:50:54.084 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(42)] [region=44]
   > [2024/07/15 12:50:54.088 +00:00] [INFO] [scheduler.rs:640] ["get snapshot failed"] [err="Error(Request(message: \"EpochNotMatch current epoch of region 2 is conf_ver: 1 version: 22, but you sent conf_ver: 1 version: 21\" epoch_not_match { current_regions { id: 2 start_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 3 store_id: 1 } } current_regions { id: 44 start_key: 7480000000000000FF2B00000000000000F8 end_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 45 store_id: 1 } } }))"] [cid=252]
   > [2024/07/15 12:50:54.105 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=3]
   > [2024/07/15 12:50:55.119 +00:00] [INFO] [server.go:388] ["new connection"] [conn=4] [remoteAddr=10.88.0.53:45476]
   > [2024/07/15 12:50:55.121 +00:00] [INFO] [set.go:207] ["set session var"] [conn=4] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/07/15 12:50:55.730 +00:00] [INFO] [server.go:388] ["new connection"] [conn=5] [remoteAddr=10.88.0.53:45488]
   > [2024/07/15 12:50:55.739 +00:00] [INFO] [set.go:207] ["set session var"] [conn=5] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/07/15 12:50:59.335 +00:00] [WARN] [session.go:1162] ["run statement failed"] [conn=5] [schemaVersion=24] [error="[tikv:1205]Lock wait timeout exceeded; try restarting transaction"] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 5,\n  \"status\": 3,\n  \"strictMode\": true,\n  \"txn\": \"451162369088815111\",\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"10.88.0.53\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/07/15 12:50:59.343 +00:00] [ERROR] [conn.go:730] ["command dispatched failed"] [conn=5] [connInfo="id:5, addr:10.88.0.53:45488 status:11, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:1, autocommit:1"] [sql=" UPDATE t1 SET t='newval' WHERE id = 1;"] [txn_mode=PESSIMISTIC] [err="[tikv:1205]Lock wait timeout exceeded; try restarting transaction\ngithub.com/pingcap/errors.AddStack\n\t/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.20190809092503-95897b64e011/errors.go:174\ngithub.com/pingcap/errors.Trace\n\t/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.20190809092503-95897b64e011/juju_adaptor.go:15\ngithub.com/pingcap/tidb/store/tikv.actionPessimisticLock.handleSingleBatch\n\t/go/src/github.com/pingcap/tidb/store/tikv/2pc.go:875\ngithub.com/pingcap/tidb/store/tikv.(*twoPhaseCommitter).doActionOnBatches\n\t/go/src/github.com/pingcap/tidb/store/tikv/2pc.go:530\ngithub.com/pingcap/tidb/store/tikv.(*twoPhaseCommitter).doActionOnMutations\n\t/go/src/github.com/pingcap/tidb/store/tikv/2pc.go:495\ngithub.com/pingcap/tidb/store/tikv.(*twoPhaseCommitter).pessimisticLockMutations\n\t/go/src/github.com/pingcap/tidb/store/tikv/2pc.go:1123\ngithub.com/pingcap/tidb/store/tikv.(*tikvTxn).LockKeys\n\t/go/src/github.com/pingcap/tidb/store/tikv/txn.go:385\ngithub.com/pingcap/tidb/executor.doLockKeys\n\t/go/src/github.com/pingcap/tidb/executor/executor.go:981\ngithub.com/pingcap/tidb/executor.(*PointGetExecutor).lockKeyIfNeeded\n\t/go/src/github.com/pingcap/tidb/executor/point_get.go:252\ngithub.com/pingcap/tidb/executor.(*PointGetExecutor).getAndLock\n\t/go/src/github.com/pingcap/tidb/executor/point_get.go:235\ngithub.com/pingcap/tidb/executor.(*PointGetExecutor).Next\n\t/go/src/github.com/pingcap/tidb/executor/point_get.go:194\ngithub.com/pingcap/tidb/executor.Next\n\t/go/src/github.com/pingcap/tidb/executor/executor.go:249\ngithub.com/pingcap/tidb/executor.(*UpdateExec).updateRows\n\t/go/src/github.com/pingcap/tidb/executor/update.go:157\ngithub.com/pingcap/tidb/executor.(*UpdateExec).Next\n\t/go/src/github.com/pingcap/tidb/executor/update.go:125\ngithub.com/pingcap/tidb/executor.Next\n\t/go/src/github.com/pingcap/tidb/executor/executor.go:249\ngithub.com/pingcap/tidb/executor.(*ExecStmt).handleNoDelayExecutor\n\t/go/src/github.com/pingcap/tidb/executor/adapter.go:510\ngithub.com/pingcap/tidb/executor.(*ExecStmt).handlePessimisticDML\n\t/go/src/github.com/pingcap/tidb/executor/adapter.go:529\ngithub.com/pingcap/tidb/executor.(*ExecStmt).handleNoDelay\n\t/go/src/github.com/pingcap/tidb/executor/adapter.go:392\ngithub.com/pingcap/tidb/executor.(*ExecStmt).Exec\n\t/go/src/github.com/pingcap/tidb/executor/adapter.go:362\ngithub.com/pingcap/tidb/session.runStmt\n\t/go/src/github.com/pingcap/tidb/session/tidb.go:276\ngithub.com/pingcap/tidb/session.(*session).ExecuteStmt\n\t/go/src/github.com/pingcap/tidb/session/session.go:1159\ngithub.com/pingcap/tidb/server.(*TiDBContext).ExecuteStmt\n\t/go/src/github.com/pingcap/tidb/server/driver_tidb.go:248\ngithub.com/pingcap/tidb/server.(*clientConn).handleStmt\n\t/go/src/github.com/pingcap/tidb/server/conn.go:1290\ngithub.com/pingcap/tidb/server.(*clientConn).handleQuery\n\t/go/src/github.com/pingcap/tidb/server/conn.go:1278\ngithub.com/pingcap/tidb/server.(*clientConn).dispatch\n\t/go/src/github.com/pingcap/tidb/server/conn.go:901\ngithub.com/pingcap/tidb/server.(*clientConn).Run\n\t/go/src/github.com/pingcap/tidb/server/conn.go:715\ngithub.com/pingcap/tidb/server.(*Server).onConn\n\t/go/src/github.com/pingcap/tidb/server/server.go:415\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1594"]
   > [2024/07/15 12:50:59.859 +00:00] [INFO] [cluster.go:1469] ["store has changed to serving"] [store-id=1] [store-address=127.0.0.1:20160]
   > [2024/07/15 12:50:59.888 +00:00] [INFO] [client.rs:789] ["set cluster version to 6.4.0"]
   > [2024/07/15 12:51:06.032 +00:00] [INFO] [2pc.go:748] ["send TxnHeartBeat"] [startTS=451162369010171905] [newTTL=30599]
   > [2024/07/15 12:51:06.632 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=5]
   > [2024/07/15 12:51:06.645 +00:00] [INFO] [server.go:391] ["connection closed"] [conn=4]
