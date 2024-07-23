# Bug ID TIDB-20002-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/20002
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              admin check table t should work


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
     - Instruction:  begin;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  update t set c_str = 'amazing herschel' where c_int = 3;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 1 / 0
 * Instruction #3:
     - Instruction:  select c_int, c_str, c_datetime from t where c_datetime between '2020-01-09 22:...
     - Transaction: conn_0
     - Output: [(3, 'amazing herschel', datetime.datetime(2020, 3, 10, 11, 49)), (2, 'sharp yalow', datetime.datetime(2020, 4, 1, 5, 53, 36))]
     - Executed order: 3
     - Affected rows / Warnings: 2 / 0
 * Instruction #4:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows / Warnings: 0 / 0
 * Instruction #5:
     - Instruction:  admin check table t;
     - Transaction: conn_0
     - Output: ERROR: 8003 (HY000): t err:[admin:8223]index:<nil> != record:&admin.RecordData{Handle:(*kv.CommonHandle)(0xc0019ff080), Values:[]types.Datum{types.Datum{k:0xd, decimal:0x0, length:0x0, i:0, collation:"", b:[]uint8(nil), x:types.Time{coreTime:0x1f90d4bc40000000}}}}
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #6:
     - Instruction:  select * from t where c_datetime = '2020-03-10 11:49:00';
     - Transaction: conn_0
     - Output: []
     - Executed order: 5
     - Affected rows / Warnings: 0 / 0

 * Container logs:
   > [2024/07/23 14:56:04.402 +00:00] [INFO] [session.go:2271] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=24] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.7]
   > [2024/07/23 14:56:04.404 +00:00] [INFO] [session.go:2271] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=24] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.7]
   > [2024/07/23 14:56:04.418 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:50, Type:create schema, State:none, SchemaState:none, SchemaID:49, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 14:56:04.382 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/23 14:56:04.418 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:50, Type:create schema, State:none, SchemaState:none, SchemaID:49, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 14:56:04.382 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/23 14:56:04.421 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:50, Type:create schema, State:none, SchemaState:none, SchemaID:49, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:04.382 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:04.436 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=24] [neededSchemaVersion=25] ["start time"=1.197582ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 14:56:04.485 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=25] ["take time"=55.419812ms] [job="ID:50, Type:create schema, State:done, SchemaState:public, SchemaID:49, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 14:56:04.382 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:04.489 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:50, Type:create schema, State:synced, SchemaState:public, SchemaID:49, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:04.382 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:04.499 +00:00] [INFO] [ddl.go:517] ["[ddl] DDL job is finished"] [jobID=50]
   > [2024/07/23 14:56:04.499 +00:00] [INFO] [domain.go:646] ["performing DDL change, must reload"]
   > [2024/07/23 14:56:04.503 +00:00] [INFO] [session.go:2271] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=25] [cur_db=testdb] [sql="create table t ( c_int int, c_str varchar(40), c_datetime datetime, primary key(c_str) , unique key(c_int), unique key(c_datetime)  );"] [user=root@10.88.0.7]
   > [2024/07/23 14:56:04.516 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:52, Type:create table, State:none, SchemaState:none, SchemaID:49, TableID:51, RowCount:0, ArgLen:1, start time: 2024-07-23 14:56:04.481 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/23 14:56:04.517 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:52, Type:create table, State:none, SchemaState:none, SchemaID:49, TableID:51, RowCount:0, ArgLen:1, start time: 2024-07-23 14:56:04.481 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t ( c_int int, c_str varchar(40), c_datetime datetime, primary key(c_str) , unique key(c_int), unique key(c_datetime)  );"]
   > [2024/07/23 14:56:04.519 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:52, Type:create table, State:none, SchemaState:none, SchemaID:49, TableID:51, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:04.481 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:04.533 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=25] [neededSchemaVersion=26] ["start time"=1.662102ms] [phyTblIDs="[51]"] [actionTypes="[8]"]
   > [2024/07/23 14:56:04.582 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=26] ["take time"=53.715666ms] [job="ID:52, Type:create table, State:done, SchemaState:public, SchemaID:49, TableID:51, RowCount:0, ArgLen:1, start time: 2024-07-23 14:56:04.481 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:04.586 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:52, Type:create table, State:synced, SchemaState:public, SchemaID:49, TableID:51, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:04.481 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:04.595 +00:00] [INFO] [ddl.go:517] ["[ddl] DDL job is finished"] [jobID=52]
   > [2024/07/23 14:56:04.598 +00:00] [INFO] [domain.go:646] ["performing DDL change, must reload"]
   > [2024/07/23 14:56:04.598 +00:00] [INFO] [split_region.go:61] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=748000000000000033]
   > [2024/07/23 14:56:04.598 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:43744] [split_keys="key 7480000000000000FF3300000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/23 14:56:04.598 +00:00] [INFO] [peer.rs:5566] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 22"] [prev_epoch="conf_ver: 1 version: 23"] [peer_id=3] [region_id=2]
   > [2024/07/23 14:56:04.602 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:43720] [split_keys="key 7480000000000000FF3300000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/23 14:56:04.603 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=48] [peer-ids="[49]"]
   > [2024/07/23 14:56:04.603 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 23 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 48 new_peer_ids: 49]"] [region_id=2]
   > [2024/07/23 14:56:04.605 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF3300000000000000F8 new_region_id: 48 new_peer_ids: 49 } right_derive: true }"] [index=56] [term=6] [peer_id=3] [region_id=2]
   > [2024/07/23 14:56:04.605 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF3300000000000000F8"] [region="id: 2 start_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 23 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/07/23 14:56:04.608 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=2]
   > [2024/07/23 14:56:04.608 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/07/23 14:56:04.608 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 48 start_key: 7480000000000000FF2F00000000000000F8 end_key: 7480000000000000FF3300000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 49 store_id: 1 }"] [region_id=48]
   > [2024/07/23 14:56:04.608 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/23 14:56:04.609 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=49] [region_id=48]
   > [2024/07/23 14:56:04.608 +00:00] [INFO] [split_region.go:158] ["batch split regions complete"] ["batch region ID"=2] ["first at"=748000000000000033] ["first new region left"="{Id:48 StartKey:7480000000000000ff2f00000000000000f8 EndKey:7480000000000000ff3300000000000000f8 RegionEpoch:{ConfVer:1 Version:24} Peers:[id:49 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/23 14:56:04.609 +00:00] [INFO] [split_region.go:207] ["split regions complete"] ["region count"=1] ["region IDs"="[48]"]
   > [2024/07/23 14:56:04.609 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(43)] [region_id=2] [store_id=Some(1)]
   > [2024/07/23 14:56:04.609 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF2F00000000000000F8} -> {7480000000000000FF3300000000000000F8}, EndKey:{}"] [old-version=23] [new-version=24]
   > [2024/07/23 14:56:04.609 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF3300000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 3 store_id: 1 }"]
   > [2024/07/23 14:56:04.609 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 2 start_key: 7480000000000000FF3300000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 3 store_id: 1 } }"]
   > [2024/07/23 14:56:04.609 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=2] [origin="id:48 start_key:\"7480000000000000FF2F00000000000000F8\" end_key:\"7480000000000000FF3300000000000000F8\" region_epoch:<conf_ver:1 version:24 > peers:<id:49 store_id:1 >"] [total=1]
   > [2024/07/23 14:56:04.609 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 2 start_key: 7480000000000000FF3300000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 3 store_id: 1 }"]
   > [2024/07/23 14:56:04.609 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {49} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=49] [region_id=48]
   > [2024/07/23 14:56:04.609 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=49] [region_id=48]
   > [2024/07/23 14:56:04.609 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {49} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=49] [region_id=48]
   > [2024/07/23 14:56:04.609 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 49."] [id=49] [raft_id=49] [region_id=48]
   > [2024/07/23 14:56:04.609 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=49] [region_id=48]
   > [2024/07/23 14:56:04.609 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=49] [region_id=48]
   > [2024/07/23 14:56:04.610 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=49] [region_id=48]
   > [2024/07/23 14:56:04.610 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=49] [region_id=48]
   > [2024/07/23 14:56:04.610 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803824] [region_id=48]
   > [2024/07/23 14:56:04.610 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=48]
   > [2024/07/23 14:56:04.610 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 48 start_key: 7480000000000000FF2F00000000000000F8 end_key: 7480000000000000FF3300000000000000F8 region_epoch { conf_ver: 1 version: 24 } peers { id: 49 store_id: 1 }"]
   > [2024/07/23 14:56:04.610 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=56] [observe_id=ObserveId(45)] [region=2]
   > [2024/07/23 14:56:04.610 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(46)] [region=48]
   > [2024/07/23 14:56:05.639 +00:00] [INFO] [set.go:216] ["set global var"] [conn=3] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/07/23 14:56:05.641 +00:00] [INFO] [set.go:216] ["set global var"] [conn=3] [name=transaction_isolation] [val=REPEATABLE-READ]
   > [2024/07/23 14:56:07.154 +00:00] [INFO] [domain.go:146] ["full load InfoSchema success"] [usedSchemaVersion=0] [neededSchemaVersion=26] ["start time"=18.759646ms]
   > [2024/07/23 14:56:07.167 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=26]
   > [2024/07/23 14:56:07.168 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=26]
   > [2024/07/23 14:56:07.187 +00:00] [INFO] [domain.go:146] ["full load InfoSchema success"] [usedSchemaVersion=0] [neededSchemaVersion=26] ["start time"=16.346533ms]
   > [2024/07/23 14:56:07.194 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=26]
   > [2024/07/23 14:56:07.194 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=26]
   > [2024/07/23 14:56:07.196 +00:00] [INFO] [admin.go:333] ["check indices count"] [table=t] [cnt=3] [index="\"PRIMARY\""] [cnt=3]
   > [2024/07/23 14:56:07.212 +00:00] [INFO] [domain.go:146] ["full load InfoSchema success"] [usedSchemaVersion=0] [neededSchemaVersion=26] ["start time"=15.507171ms]
   > [2024/07/23 14:56:07.221 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=26]
   > [2024/07/23 14:56:07.221 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=26]
   > [2024/07/23 14:56:07.222 +00:00] [INFO] [admin.go:333] ["check indices count"] [table=t] [cnt=3] [index="\"c_int\""] [cnt=3]
   > [2024/07/23 14:56:07.233 +00:00] [INFO] [domain.go:146] ["full load InfoSchema success"] [usedSchemaVersion=0] [neededSchemaVersion=26] ["start time"=10.129333ms]
   > [2024/07/23 14:56:07.240 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=26]
   > [2024/07/23 14:56:07.240 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=26]
   > [2024/07/23 14:56:07.241 +00:00] [INFO] [admin.go:333] ["check indices count"] [table=t] [cnt=3] [index="\"c_datetime\""] [cnt=2]
   > [2024/07/23 14:56:07.242 +00:00] [INFO] [tidb.go:217] ["rollbackTxn for ddl/autocommit failed"]
   > [2024/07/23 14:56:07.242 +00:00] [WARN] [session.go:1175] ["run statement failed"] [conn=3] [schemaVersion=26] [error="[executor:8003]t err:[admin:8223]index:<nil> != record:&admin.RecordData{Handle:(*kv.CommonHandle)(0xc0019ff080), Values:[]types.Datum{types.Datum{k:0xd, decimal:0x0, length:0x0, i:0, collation:\"\", b:[]uint8(nil), x:types.Time{coreTime:0x1f90d4bc40000000}}}}"] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 3,\n  \"status\": 2,\n  \"strictMode\": true,\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"10.88.0.7\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/07/23 14:56:07.243 +00:00] [INFO] [conn.go:793] ["command dispatched failed"] [conn=3] [connInfo="id:3, addr:10.88.0.7:46890 status:10, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:0, autocommit:1"] [sql=" admin check table t;"] [txn_mode=PESSIMISTIC] [err="[executor:8003]t err:[admin:8223]index:<nil> != record:&admin.RecordData{Handle:(*kv.CommonHandle)(0xc0019ff080), Values:[]types.Datum{types.Datum{k:0xd, decimal:0x0, length:0x0, i:0, collation:\"\", b:[]uint8(nil), x:types.Time{coreTime:0x1f90d4bc40000000}}}}\ngithub.com/pingcap/errors.AddStack\n\t/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.20200902104258-eba4f1d8f6de/errors.go:174\ngithub.com/pingcap/errors.(*Error).GenWithStack\n\t/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.20200902104258-eba4f1d8f6de/terror_error.go:152\ngithub.com/pingcap/tidb/executor.(*CheckTableExec).Next\n\t/go/src/github.com/pingcap/tidb/executor/executor.go:747\ngithub.com/pingcap/tidb/executor.Next\n\t/go/src/github.com/pingcap/tidb/executor/executor.go:268\ngithub.com/pingcap/tidb/executor.(*ExecStmt).handleNoDelayExecutor\n\t/go/src/github.com/pingcap/tidb/executor/adapter.go:518\ngithub.com/pingcap/tidb/executor.(*ExecStmt).handleNoDelay\n\t/go/src/github.com/pingcap/tidb/executor/adapter.go:400\ngithub.com/pingcap/tidb/executor.(*ExecStmt).Exec\n\t/go/src/github.com/pingcap/tidb/executor/adapter.go:353\ngithub.com/pingcap/tidb/session.runStmt\n\t/go/src/github.com/pingcap/tidb/session/session.go:1207\ngithub.com/pingcap/tidb/session.(*session).ExecuteStmt\n\t/go/src/github.com/pingcap/tidb/session/session.go:1172\ngithub.com/pingcap/tidb/server.(*TiDBContext).ExecuteStmt\n\t/go/src/github.com/pingcap/tidb/server/driver_tidb.go:198\ngithub.com/pingcap/tidb/server.(*clientConn).handleStmt\n\t/go/src/github.com/pingcap/tidb/server/conn.go:1505\ngithub.com/pingcap/tidb/server.(*clientConn).handleQuery\n\t/go/src/github.com/pingcap/tidb/server/conn.go:1397\ngithub.com/pingcap/tidb/server.(*clientConn).dispatch\n\t/go/src/github.com/pingcap/tidb/server/conn.go:984\ngithub.com/pingcap/tidb/server.(*clientConn).Run\n\t/go/src/github.com/pingcap/tidb/server/conn.go:776\ngithub.com/pingcap/tidb/server.(*Server).onConn\n\t/go/src/github.com/pingcap/tidb/server/server.go:421\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1594"]

### Scenario 1
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 0 / 0
 * Instruction #1:
     - Instruction:  update t set c_str = 'amazing herschel' where c_int = 3;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 1 / 0
 * Instruction #2:
     - Instruction:  select c_int, c_str, c_datetime from t where c_datetime between '2020-01-09 22:...
     - Transaction: conn_0
     - Output: [(3, 'amazing herschel', datetime.datetime(2020, 3, 10, 11, 49)), (2, 'sharp yalow', datetime.datetime(2020, 4, 1, 5, 53, 36))]
     - Executed order: 2
     - Affected rows / Warnings: 2 / 0
 * Instruction #3:
     - Instruction:  admin check table t;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 0 / 0
 * Instruction #4:
     - Instruction:  select * from t where c_datetime = '2020-03-10 11:49:00';
     - Transaction: conn_0
     - Output: [(3, 'amazing herschel', datetime.datetime(2020, 3, 10, 11, 49))]
     - Executed order: 4
     - Affected rows / Warnings: 1 / 0

 * Container logs:
   > [2024/07/23 14:56:09.713 +00:00] [INFO] [session.go:2271] ["CRUCIAL OPERATION"] [conn=6] [schemaVersion=34] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.7]
   > [2024/07/23 14:56:09.738 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:59, Type:drop schema, State:none, SchemaState:none, SchemaID:54, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:09.681 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/23 14:56:09.738 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:59, Type:drop schema, State:none, SchemaState:none, SchemaID:54, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:09.681 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/23 14:56:09.742 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:59, Type:drop schema, State:none, SchemaState:none, SchemaID:54, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:09.681 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:09.770 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=34] [neededSchemaVersion=35] ["start time"=789.076µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 14:56:09.821 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=35] ["take time"=58.124026ms] [job="ID:59, Type:drop schema, State:running, SchemaState:write only, SchemaID:54, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:09.681 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:09.822 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:59, Type:drop schema, State:running, SchemaState:write only, SchemaID:54, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:09.681 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:09.850 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=35] [neededSchemaVersion=36] ["start time"=636.331µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 14:56:09.899 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=36] ["take time"=57.860792ms] [job="ID:59, Type:drop schema, State:running, SchemaState:delete only, SchemaID:54, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:09.681 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:09.901 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:59, Type:drop schema, State:running, SchemaState:delete only, SchemaID:54, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:09.681 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:09.930 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=36] [neededSchemaVersion=37] ["start time"=754.713µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 14:56:09.980 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=37] ["take time"=57.688143ms] [job="ID:59, Type:drop schema, State:done, SchemaState:none, SchemaID:54, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:09.681 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:09.983 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=59] [jobType="drop schema"]
   > [2024/07/23 14:56:09.984 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:59, Type:drop schema, State:synced, SchemaState:none, SchemaID:54, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:09.681 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:10.002 +00:00] [INFO] [ddl.go:517] ["[ddl] DDL job is finished"] [jobID=59]
   > [2024/07/23 14:56:10.002 +00:00] [INFO] [domain.go:646] ["performing DDL change, must reload"]
   > [2024/07/23 14:56:10.004 +00:00] [INFO] [session.go:2271] ["CRUCIAL OPERATION"] [conn=6] [schemaVersion=37] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.7]
   > [2024/07/23 14:56:10.041 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:61, Type:create schema, State:none, SchemaState:none, SchemaID:60, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 14:56:09.981 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/23 14:56:10.041 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:61, Type:create schema, State:none, SchemaState:none, SchemaID:60, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 14:56:09.981 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/23 14:56:10.045 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:61, Type:create schema, State:none, SchemaState:none, SchemaID:60, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:09.981 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:10.072 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=37] [neededSchemaVersion=38] ["start time"=1.627739ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 14:56:10.121 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=38] ["take time"=58.155385ms] [job="ID:61, Type:create schema, State:done, SchemaState:public, SchemaID:60, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 14:56:09.981 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:10.124 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:61, Type:create schema, State:synced, SchemaState:public, SchemaID:60, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:09.981 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:10.142 +00:00] [INFO] [ddl.go:517] ["[ddl] DDL job is finished"] [jobID=61]
   > [2024/07/23 14:56:10.142 +00:00] [INFO] [domain.go:646] ["performing DDL change, must reload"]
   > [2024/07/23 14:56:10.146 +00:00] [INFO] [session.go:2271] ["CRUCIAL OPERATION"] [conn=6] [schemaVersion=38] [cur_db=testdb] [sql="create table t ( c_int int, c_str varchar(40), c_datetime datetime, primary key(c_str) , unique key(c_int), unique key(c_datetime)  );"] [user=root@10.88.0.7]
   > [2024/07/23 14:56:10.180 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:63, Type:create table, State:none, SchemaState:none, SchemaID:60, TableID:62, RowCount:0, ArgLen:1, start time: 2024-07-23 14:56:10.131 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/23 14:56:10.180 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:63, Type:create table, State:none, SchemaState:none, SchemaID:60, TableID:62, RowCount:0, ArgLen:1, start time: 2024-07-23 14:56:10.131 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t ( c_int int, c_str varchar(40), c_datetime datetime, primary key(c_str) , unique key(c_int), unique key(c_datetime)  );"]
   > [2024/07/23 14:56:10.184 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:63, Type:create table, State:none, SchemaState:none, SchemaID:60, TableID:62, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:10.131 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:10.218 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=38] [neededSchemaVersion=39] ["start time"=2.322947ms] [phyTblIDs="[62]"] [actionTypes="[8]"]
   > [2024/07/23 14:56:10.267 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=39] ["take time"=62.087144ms] [job="ID:63, Type:create table, State:done, SchemaState:public, SchemaID:60, TableID:62, RowCount:0, ArgLen:1, start time: 2024-07-23 14:56:10.131 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:10.271 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:63, Type:create table, State:synced, SchemaState:public, SchemaID:60, TableID:62, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:10.131 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:10.289 +00:00] [INFO] [ddl.go:517] ["[ddl] DDL job is finished"] [jobID=63]
   > [2024/07/23 14:56:10.292 +00:00] [INFO] [domain.go:646] ["performing DDL change, must reload"]
   > [2024/07/23 14:56:10.292 +00:00] [INFO] [split_region.go:61] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=74800000000000003e]
   > [2024/07/23 14:56:10.293 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:43736] [split_keys="key 7480000000000000FF3E00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/23 14:56:10.293 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=52] [peer-ids="[53]"]
   > [2024/07/23 14:56:10.293 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF3800000000000000F8 region_epoch { conf_ver: 1 version: 25 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 52 new_peer_ids: 53]"] [region_id=2]
   > [2024/07/23 14:56:10.300 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF3E00000000000000F8 new_region_id: 52 new_peer_ids: 53 } right_derive: true }"] [index=66] [term=6] [peer_id=3] [region_id=2]
   > [2024/07/23 14:56:10.300 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF3E00000000000000F8"] [region="id: 2 start_key: 7480000000000000FF3800000000000000F8 region_epoch { conf_ver: 1 version: 25 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/07/23 14:56:10.307 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/23 14:56:10.307 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=2]
   > [2024/07/23 14:56:10.307 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/07/23 14:56:10.307 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(47)] [region_id=2] [store_id=Some(1)]
   > [2024/07/23 14:56:10.307 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF3E00000000000000F8 region_epoch { conf_ver: 1 version: 26 } peers { id: 3 store_id: 1 }"]
   > [2024/07/23 14:56:10.307 +00:00] [INFO] [split_region.go:158] ["batch split regions complete"] ["batch region ID"=2] ["first at"=74800000000000003e] ["first new region left"="{Id:52 StartKey:7480000000000000ff3800000000000000f8 EndKey:7480000000000000ff3e00000000000000f8 RegionEpoch:{ConfVer:1 Version:26} Peers:[id:53 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/23 14:56:10.307 +00:00] [INFO] [split_region.go:207] ["split regions complete"] ["region count"=1] ["region IDs"="[52]"]
   > [2024/07/23 14:56:10.307 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 52 start_key: 7480000000000000FF3800000000000000F8 end_key: 7480000000000000FF3E00000000000000F8 region_epoch { conf_ver: 1 version: 26 } peers { id: 53 store_id: 1 }"] [region_id=52]
   > [2024/07/23 14:56:10.307 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=53] [region_id=52]
   > [2024/07/23 14:56:10.307 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 2 start_key: 7480000000000000FF3E00000000000000F8 region_epoch { conf_ver: 1 version: 26 } peers { id: 3 store_id: 1 } }"]
   > [2024/07/23 14:56:10.307 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 2 start_key: 7480000000000000FF3E00000000000000F8 region_epoch { conf_ver: 1 version: 26 } peers { id: 3 store_id: 1 }"]
   > [2024/07/23 14:56:10.308 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {53} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=53] [region_id=52]
   > [2024/07/23 14:56:10.308 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF3800000000000000F8} -> {7480000000000000FF3E00000000000000F8}, EndKey:{}"] [old-version=25] [new-version=26]
   > [2024/07/23 14:56:10.308 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=53] [region_id=52]
   > [2024/07/23 14:56:10.308 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=2] [origin="id:52 start_key:\"7480000000000000FF3800000000000000F8\" end_key:\"7480000000000000FF3E00000000000000F8\" region_epoch:<conf_ver:1 version:26 > peers:<id:53 store_id:1 >"] [total=1]
   > [2024/07/23 14:56:10.308 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {53} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=53] [region_id=52]
   > [2024/07/23 14:56:10.308 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 53."] [id=53] [raft_id=53] [region_id=52]
   > [2024/07/23 14:56:10.308 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=53] [region_id=52]
   > [2024/07/23 14:56:10.308 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=53] [region_id=52]
   > [2024/07/23 14:56:10.308 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=53] [region_id=52]
   > [2024/07/23 14:56:10.308 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=53] [region_id=52]
   > [2024/07/23 14:56:10.308 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803828] [region_id=52]
   > [2024/07/23 14:56:10.309 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=66] [observe_id=ObserveId(49)] [region=2]
   > [2024/07/23 14:56:10.309 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=52]
   > [2024/07/23 14:56:10.314 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 52 start_key: 7480000000000000FF3800000000000000F8 end_key: 7480000000000000FF3E00000000000000F8 region_epoch { conf_ver: 1 version: 26 } peers { id: 53 store_id: 1 }"]
   > [2024/07/23 14:56:10.314 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(50)] [region=52]
   > [2024/07/23 14:56:11.356 +00:00] [INFO] [set.go:216] ["set global var"] [conn=7] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/07/23 14:56:11.359 +00:00] [INFO] [set.go:216] ["set global var"] [conn=7] [name=transaction_isolation] [val=REPEATABLE-READ]
   > [2024/07/23 14:56:12.259 +00:00] [INFO] [domain.go:146] ["full load InfoSchema success"] [usedSchemaVersion=0] [neededSchemaVersion=39] ["start time"=16.322018ms]
   > [2024/07/23 14:56:12.272 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=39]
   > [2024/07/23 14:56:12.273 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=39]
   > [2024/07/23 14:56:12.292 +00:00] [INFO] [domain.go:146] ["full load InfoSchema success"] [usedSchemaVersion=0] [neededSchemaVersion=39] ["start time"=16.013736ms]
   > [2024/07/23 14:56:12.304 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=39]
   > [2024/07/23 14:56:12.305 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=39]
   > [2024/07/23 14:56:12.306 +00:00] [INFO] [admin.go:333] ["check indices count"] [table=t] [cnt=3] [index="\"PRIMARY\""] [cnt=3]
   > [2024/07/23 14:56:12.322 +00:00] [INFO] [domain.go:146] ["full load InfoSchema success"] [usedSchemaVersion=0] [neededSchemaVersion=39] ["start time"=15.634704ms]
   > [2024/07/23 14:56:12.329 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=39]
   > [2024/07/23 14:56:12.330 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=39]
   > [2024/07/23 14:56:12.331 +00:00] [INFO] [admin.go:333] ["check indices count"] [table=t] [cnt=3] [index="\"c_int\""] [cnt=3]
   > [2024/07/23 14:56:12.348 +00:00] [INFO] [domain.go:146] ["full load InfoSchema success"] [usedSchemaVersion=0] [neededSchemaVersion=39] ["start time"=15.449901ms]
   > [2024/07/23 14:56:12.354 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=39]
   > [2024/07/23 14:56:12.355 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=39]
   > [2024/07/23 14:56:12.356 +00:00] [INFO] [admin.go:333] ["check indices count"] [table=t] [cnt=3] [index="\"c_datetime\""] [cnt=3]
