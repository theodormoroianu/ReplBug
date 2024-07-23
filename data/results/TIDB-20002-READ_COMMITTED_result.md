# Bug ID TIDB-20002-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/20002
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              admin check table t should work


## Details
 * Database: tidb-fa6baa9f.tikv
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
     - Output: ERROR: 8003 (HY000): t err:[admin:8223]index:<nil> != record:&admin.RecordData{Handle:(*kv.CommonHandle)(0xc000fa8d50), Values:[]types.Datum{types.Datum{k:0xd, decimal:0x0, length:0x0, i:0, collation:"", b:[]uint8(nil), x:types.Time{coreTime:0x1f90d4bc40000000}}}}
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #6:
     - Instruction:  select * from t where c_datetime = '2020-03-10 11:49:00';
     - Transaction: conn_0
     - Output: []
     - Executed order: 5
     - Affected rows / Warnings: 0 / 0

 * Container logs:
   > [2024/07/23 14:56:14.831 +00:00] [INFO] [session.go:2271] ["CRUCIAL OPERATION"] [conn=9] [schemaVersion=47] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.7]
   > [2024/07/23 14:56:14.848 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:70, Type:drop schema, State:none, SchemaState:none, SchemaID:65, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:14.831 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/23 14:56:14.848 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:70, Type:drop schema, State:none, SchemaState:none, SchemaID:65, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:14.831 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/23 14:56:14.853 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:70, Type:drop schema, State:none, SchemaState:none, SchemaID:65, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:14.831 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:14.879 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=47] [neededSchemaVersion=48] ["start time"=717.488µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 14:56:14.929 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=48] ["take time"=58.289622ms] [job="ID:70, Type:drop schema, State:running, SchemaState:write only, SchemaID:65, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:14.831 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:14.931 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:70, Type:drop schema, State:running, SchemaState:write only, SchemaID:65, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:14.831 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:14.963 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=48] [neededSchemaVersion=49] ["start time"=690.249µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 14:56:15.012 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=49] ["take time"=60.942852ms] [job="ID:70, Type:drop schema, State:running, SchemaState:delete only, SchemaID:65, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:14.831 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:15.015 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:70, Type:drop schema, State:running, SchemaState:delete only, SchemaID:65, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:14.831 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:15.044 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=49] [neededSchemaVersion=50] ["start time"=819.876µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 14:56:15.093 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=50] ["take time"=57.676618ms] [job="ID:70, Type:drop schema, State:done, SchemaState:none, SchemaID:65, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:14.831 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:15.096 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=70] [jobType="drop schema"]
   > [2024/07/23 14:56:15.097 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:70, Type:drop schema, State:synced, SchemaState:none, SchemaID:65, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:14.831 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:15.115 +00:00] [INFO] [ddl.go:517] ["[ddl] DDL job is finished"] [jobID=70]
   > [2024/07/23 14:56:15.115 +00:00] [INFO] [domain.go:646] ["performing DDL change, must reload"]
   > [2024/07/23 14:56:15.117 +00:00] [INFO] [session.go:2271] ["CRUCIAL OPERATION"] [conn=9] [schemaVersion=50] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.7]
   > [2024/07/23 14:56:15.153 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:72, Type:create schema, State:none, SchemaState:none, SchemaID:71, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 14:56:15.131 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/23 14:56:15.153 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:72, Type:create schema, State:none, SchemaState:none, SchemaID:71, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 14:56:15.131 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/23 14:56:15.157 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:72, Type:create schema, State:none, SchemaState:none, SchemaID:71, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:15.131 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:15.184 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=50] [neededSchemaVersion=51] ["start time"=1.433298ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 14:56:15.233 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=51] ["take time"=57.929446ms] [job="ID:72, Type:create schema, State:done, SchemaState:public, SchemaID:71, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 14:56:15.131 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:15.236 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:72, Type:create schema, State:synced, SchemaState:public, SchemaID:71, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:15.131 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:15.254 +00:00] [INFO] [ddl.go:517] ["[ddl] DDL job is finished"] [jobID=72]
   > [2024/07/23 14:56:15.254 +00:00] [INFO] [domain.go:646] ["performing DDL change, must reload"]
   > [2024/07/23 14:56:15.257 +00:00] [INFO] [session.go:2271] ["CRUCIAL OPERATION"] [conn=9] [schemaVersion=51] [cur_db=testdb] [sql="create table t ( c_int int, c_str varchar(40), c_datetime datetime, primary key(c_str) , unique key(c_int), unique key(c_datetime)  );"] [user=root@10.88.0.7]
   > [2024/07/23 14:56:15.292 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:74, Type:create table, State:none, SchemaState:none, SchemaID:71, TableID:73, RowCount:0, ArgLen:1, start time: 2024-07-23 14:56:15.231 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/23 14:56:15.292 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:74, Type:create table, State:none, SchemaState:none, SchemaID:71, TableID:73, RowCount:0, ArgLen:1, start time: 2024-07-23 14:56:15.231 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t ( c_int int, c_str varchar(40), c_datetime datetime, primary key(c_str) , unique key(c_int), unique key(c_datetime)  );"]
   > [2024/07/23 14:56:15.296 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:74, Type:create table, State:none, SchemaState:none, SchemaID:71, TableID:73, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:15.231 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:15.329 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=51] [neededSchemaVersion=52] ["start time"=2.627807ms] [phyTblIDs="[73]"] [actionTypes="[8]"]
   > [2024/07/23 14:56:15.376 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=52] ["take time"=60.878178ms] [job="ID:74, Type:create table, State:done, SchemaState:public, SchemaID:71, TableID:73, RowCount:0, ArgLen:1, start time: 2024-07-23 14:56:15.231 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:15.380 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:74, Type:create table, State:synced, SchemaState:public, SchemaID:71, TableID:73, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:15.231 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:15.400 +00:00] [INFO] [ddl.go:517] ["[ddl] DDL job is finished"] [jobID=74]
   > [2024/07/23 14:56:15.402 +00:00] [INFO] [domain.go:646] ["performing DDL change, must reload"]
   > [2024/07/23 14:56:15.402 +00:00] [INFO] [split_region.go:61] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=748000000000000049]
   > [2024/07/23 14:56:15.403 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:43720] [split_keys="key 7480000000000000FF4900000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/23 14:56:15.403 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=56] [peer-ids="[57]"]
   > [2024/07/23 14:56:15.404 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF4300000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 56 new_peer_ids: 57]"] [region_id=2]
   > [2024/07/23 14:56:15.409 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF4900000000000000F8 new_region_id: 56 new_peer_ids: 57 } right_derive: true }"] [index=74] [term=6] [peer_id=3] [region_id=2]
   > [2024/07/23 14:56:15.409 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF4900000000000000F8"] [region="id: 2 start_key: 7480000000000000FF4300000000000000F8 region_epoch { conf_ver: 1 version: 27 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/07/23 14:56:15.415 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/23 14:56:15.415 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=2]
   > [2024/07/23 14:56:15.415 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/07/23 14:56:15.415 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(51)] [region_id=2] [store_id=Some(1)]
   > [2024/07/23 14:56:15.415 +00:00] [INFO] [split_region.go:158] ["batch split regions complete"] ["batch region ID"=2] ["first at"=748000000000000049] ["first new region left"="{Id:56 StartKey:7480000000000000ff4300000000000000f8 EndKey:7480000000000000ff4900000000000000f8 RegionEpoch:{ConfVer:1 Version:28} Peers:[id:57 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/23 14:56:15.415 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 56 start_key: 7480000000000000FF4300000000000000F8 end_key: 7480000000000000FF4900000000000000F8 region_epoch { conf_ver: 1 version: 28 } peers { id: 57 store_id: 1 }"] [region_id=56]
   > [2024/07/23 14:56:15.415 +00:00] [INFO] [split_region.go:207] ["split regions complete"] ["region count"=1] ["region IDs"="[56]"]
   > [2024/07/23 14:56:15.415 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=57] [region_id=56]
   > [2024/07/23 14:56:15.415 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF4300000000000000F8} -> {7480000000000000FF4900000000000000F8}, EndKey:{}"] [old-version=27] [new-version=28]
   > [2024/07/23 14:56:15.415 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF4900000000000000F8 region_epoch { conf_ver: 1 version: 28 } peers { id: 3 store_id: 1 }"]
   > [2024/07/23 14:56:15.415 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 2 start_key: 7480000000000000FF4900000000000000F8 region_epoch { conf_ver: 1 version: 28 } peers { id: 3 store_id: 1 } }"]
   > [2024/07/23 14:56:15.416 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 2 start_key: 7480000000000000FF4900000000000000F8 region_epoch { conf_ver: 1 version: 28 } peers { id: 3 store_id: 1 }"]
   > [2024/07/23 14:56:15.415 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=2] [origin="id:56 start_key:\"7480000000000000FF4300000000000000F8\" end_key:\"7480000000000000FF4900000000000000F8\" region_epoch:<conf_ver:1 version:28 > peers:<id:57 store_id:1 >"] [total=1]
   > [2024/07/23 14:56:15.416 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {57} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=57] [region_id=56]
   > [2024/07/23 14:56:15.416 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=57] [region_id=56]
   > [2024/07/23 14:56:15.416 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {57} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=57] [region_id=56]
   > [2024/07/23 14:56:15.416 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 57."] [id=57] [raft_id=57] [region_id=56]
   > [2024/07/23 14:56:15.416 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=57] [region_id=56]
   > [2024/07/23 14:56:15.416 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=57] [region_id=56]
   > [2024/07/23 14:56:15.416 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=57] [region_id=56]
   > [2024/07/23 14:56:15.416 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=57] [region_id=56]
   > [2024/07/23 14:56:15.416 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803832] [region_id=56]
   > [2024/07/23 14:56:15.417 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=74] [observe_id=ObserveId(53)] [region=2]
   > [2024/07/23 14:56:15.417 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=56]
   > [2024/07/23 14:56:15.421 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 56 start_key: 7480000000000000FF4300000000000000F8 end_key: 7480000000000000FF4900000000000000F8 region_epoch { conf_ver: 1 version: 28 } peers { id: 57 store_id: 1 }"]
   > [2024/07/23 14:56:15.422 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(54)] [region=56]
   > [2024/07/23 14:56:16.489 +00:00] [INFO] [set.go:216] ["set global var"] [conn=10] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/07/23 14:56:16.505 +00:00] [INFO] [set.go:216] ["set global var"] [conn=10] [name=transaction_isolation] [val=READ-COMMITTED]
   > [2024/07/23 14:56:17.963 +00:00] [INFO] [domain.go:146] ["full load InfoSchema success"] [usedSchemaVersion=0] [neededSchemaVersion=52] ["start time"=16.447246ms]
   > [2024/07/23 14:56:17.974 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=52]
   > [2024/07/23 14:56:17.974 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=52]
   > [2024/07/23 14:56:17.993 +00:00] [INFO] [domain.go:146] ["full load InfoSchema success"] [usedSchemaVersion=0] [neededSchemaVersion=52] ["start time"=15.968688ms]
   > [2024/07/23 14:56:17.999 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=52]
   > [2024/07/23 14:56:18.000 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=52]
   > [2024/07/23 14:56:18.001 +00:00] [INFO] [admin.go:333] ["check indices count"] [table=t] [cnt=3] [index="\"PRIMARY\""] [cnt=3]
   > [2024/07/23 14:56:18.013 +00:00] [INFO] [domain.go:146] ["full load InfoSchema success"] [usedSchemaVersion=0] [neededSchemaVersion=52] ["start time"=10.693726ms]
   > [2024/07/23 14:56:18.019 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=52]
   > [2024/07/23 14:56:18.020 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=52]
   > [2024/07/23 14:56:18.021 +00:00] [INFO] [admin.go:333] ["check indices count"] [table=t] [cnt=3] [index="\"c_int\""] [cnt=3]
   > [2024/07/23 14:56:18.038 +00:00] [INFO] [domain.go:146] ["full load InfoSchema success"] [usedSchemaVersion=0] [neededSchemaVersion=52] ["start time"=15.794292ms]
   > [2024/07/23 14:56:18.044 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=52]
   > [2024/07/23 14:56:18.044 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=52]
   > [2024/07/23 14:56:18.046 +00:00] [INFO] [admin.go:333] ["check indices count"] [table=t] [cnt=3] [index="\"c_datetime\""] [cnt=2]
   > [2024/07/23 14:56:18.047 +00:00] [INFO] [tidb.go:217] ["rollbackTxn for ddl/autocommit failed"]
   > [2024/07/23 14:56:18.047 +00:00] [WARN] [session.go:1175] ["run statement failed"] [conn=10] [schemaVersion=52] [error="[executor:8003]t err:[admin:8223]index:<nil> != record:&admin.RecordData{Handle:(*kv.CommonHandle)(0xc000fa8d50), Values:[]types.Datum{types.Datum{k:0xd, decimal:0x0, length:0x0, i:0, collation:\"\", b:[]uint8(nil), x:types.Time{coreTime:0x1f90d4bc40000000}}}}"] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 10,\n  \"status\": 2,\n  \"strictMode\": true,\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"10.88.0.7\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/07/23 14:56:18.047 +00:00] [INFO] [conn.go:793] ["command dispatched failed"] [conn=10] [connInfo="id:10, addr:10.88.0.7:50954 status:10, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:0, autocommit:1"] [sql=" admin check table t;"] [txn_mode=PESSIMISTIC] [err="[executor:8003]t err:[admin:8223]index:<nil> != record:&admin.RecordData{Handle:(*kv.CommonHandle)(0xc000fa8d50), Values:[]types.Datum{types.Datum{k:0xd, decimal:0x0, length:0x0, i:0, collation:\"\", b:[]uint8(nil), x:types.Time{coreTime:0x1f90d4bc40000000}}}}\ngithub.com/pingcap/errors.AddStack\n\t/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.20200902104258-eba4f1d8f6de/errors.go:174\ngithub.com/pingcap/errors.(*Error).GenWithStack\n\t/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.20200902104258-eba4f1d8f6de/terror_error.go:152\ngithub.com/pingcap/tidb/executor.(*CheckTableExec).Next\n\t/go/src/github.com/pingcap/tidb/executor/executor.go:747\ngithub.com/pingcap/tidb/executor.Next\n\t/go/src/github.com/pingcap/tidb/executor/executor.go:268\ngithub.com/pingcap/tidb/executor.(*ExecStmt).handleNoDelayExecutor\n\t/go/src/github.com/pingcap/tidb/executor/adapter.go:518\ngithub.com/pingcap/tidb/executor.(*ExecStmt).handleNoDelay\n\t/go/src/github.com/pingcap/tidb/executor/adapter.go:400\ngithub.com/pingcap/tidb/executor.(*ExecStmt).Exec\n\t/go/src/github.com/pingcap/tidb/executor/adapter.go:353\ngithub.com/pingcap/tidb/session.runStmt\n\t/go/src/github.com/pingcap/tidb/session/session.go:1207\ngithub.com/pingcap/tidb/session.(*session).ExecuteStmt\n\t/go/src/github.com/pingcap/tidb/session/session.go:1172\ngithub.com/pingcap/tidb/server.(*TiDBContext).ExecuteStmt\n\t/go/src/github.com/pingcap/tidb/server/driver_tidb.go:198\ngithub.com/pingcap/tidb/server.(*clientConn).handleStmt\n\t/go/src/github.com/pingcap/tidb/server/conn.go:1505\ngithub.com/pingcap/tidb/server.(*clientConn).handleQuery\n\t/go/src/github.com/pingcap/tidb/server/conn.go:1397\ngithub.com/pingcap/tidb/server.(*clientConn).dispatch\n\t/go/src/github.com/pingcap/tidb/server/conn.go:984\ngithub.com/pingcap/tidb/server.(*clientConn).Run\n\t/go/src/github.com/pingcap/tidb/server/conn.go:776\ngithub.com/pingcap/tidb/server.(*Server).onConn\n\t/go/src/github.com/pingcap/tidb/server/server.go:421\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1594"]

### Scenario 1
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
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
   > [2024/07/23 14:56:20.570 +00:00] [INFO] [session.go:2271] ["CRUCIAL OPERATION"] [conn=12] [schemaVersion=60] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.7]
   > [2024/07/23 14:56:20.594 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:81, Type:drop schema, State:none, SchemaState:none, SchemaID:76, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:20.531 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/23 14:56:20.594 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:81, Type:drop schema, State:none, SchemaState:none, SchemaID:76, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:20.531 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/23 14:56:20.598 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:81, Type:drop schema, State:none, SchemaState:none, SchemaID:76, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:20.531 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:20.624 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=60] [neededSchemaVersion=61] ["start time"=733.342µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 14:56:20.673 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=61] ["take time"=57.095043ms] [job="ID:81, Type:drop schema, State:running, SchemaState:write only, SchemaID:76, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:20.531 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:20.675 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:81, Type:drop schema, State:running, SchemaState:write only, SchemaID:76, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:20.531 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:20.709 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=61] [neededSchemaVersion=62] ["start time"=468.501µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 14:56:20.758 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=62] ["take time"=60.090709ms] [job="ID:81, Type:drop schema, State:running, SchemaState:delete only, SchemaID:76, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:20.531 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:20.760 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:81, Type:drop schema, State:running, SchemaState:delete only, SchemaID:76, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:20.531 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:20.789 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=62] [neededSchemaVersion=63] ["start time"=765.469µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 14:56:20.839 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=63] ["take time"=58.029251ms] [job="ID:81, Type:drop schema, State:done, SchemaState:none, SchemaID:76, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:20.531 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:20.842 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=81] [jobType="drop schema"]
   > [2024/07/23 14:56:20.843 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:81, Type:drop schema, State:synced, SchemaState:none, SchemaID:76, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:20.531 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:20.859 +00:00] [INFO] [ddl.go:517] ["[ddl] DDL job is finished"] [jobID=81]
   > [2024/07/23 14:56:20.859 +00:00] [INFO] [domain.go:646] ["performing DDL change, must reload"]
   > [2024/07/23 14:56:20.861 +00:00] [INFO] [session.go:2271] ["CRUCIAL OPERATION"] [conn=12] [schemaVersion=63] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.7]
   > [2024/07/23 14:56:20.890 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:83, Type:create schema, State:none, SchemaState:none, SchemaID:82, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 14:56:20.831 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/23 14:56:20.890 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:83, Type:create schema, State:none, SchemaState:none, SchemaID:82, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 14:56:20.831 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/23 14:56:20.892 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:83, Type:create schema, State:none, SchemaState:none, SchemaID:82, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:20.831 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:20.915 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=63] [neededSchemaVersion=64] ["start time"=833.076µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/23 14:56:20.964 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=64] ["take time"=56.850597ms] [job="ID:83, Type:create schema, State:done, SchemaState:public, SchemaID:82, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-23 14:56:20.831 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:20.968 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:83, Type:create schema, State:synced, SchemaState:public, SchemaID:82, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:20.831 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:20.987 +00:00] [INFO] [ddl.go:517] ["[ddl] DDL job is finished"] [jobID=83]
   > [2024/07/23 14:56:20.987 +00:00] [INFO] [domain.go:646] ["performing DDL change, must reload"]
   > [2024/07/23 14:56:20.990 +00:00] [INFO] [session.go:2271] ["CRUCIAL OPERATION"] [conn=12] [schemaVersion=64] [cur_db=testdb] [sql="create table t ( c_int int, c_str varchar(40), c_datetime datetime, primary key(c_str) , unique key(c_int), unique key(c_datetime)  );"] [user=root@10.88.0.7]
   > [2024/07/23 14:56:21.024 +00:00] [INFO] [ddl_worker.go:260] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:85, Type:create table, State:none, SchemaState:none, SchemaID:82, TableID:84, RowCount:0, ArgLen:1, start time: 2024-07-23 14:56:20.981 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/23 14:56:21.024 +00:00] [INFO] [ddl.go:477] ["[ddl] start DDL job"] [job="ID:85, Type:create table, State:none, SchemaState:none, SchemaID:82, TableID:84, RowCount:0, ArgLen:1, start time: 2024-07-23 14:56:20.981 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t ( c_int int, c_str varchar(40), c_datetime datetime, primary key(c_str) , unique key(c_int), unique key(c_datetime)  );"]
   > [2024/07/23 14:56:21.028 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:85, Type:create table, State:none, SchemaState:none, SchemaID:82, TableID:84, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:20.981 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:21.061 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=64] [neededSchemaVersion=65] ["start time"=1.890206ms] [phyTblIDs="[84]"] [actionTypes="[8]"]
   > [2024/07/23 14:56:21.110 +00:00] [INFO] [ddl_worker.go:786] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=65] ["take time"=61.672422ms] [job="ID:85, Type:create table, State:done, SchemaState:public, SchemaID:82, TableID:84, RowCount:0, ArgLen:1, start time: 2024-07-23 14:56:20.981 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:21.114 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:85, Type:create table, State:synced, SchemaState:public, SchemaID:82, TableID:84, RowCount:0, ArgLen:0, start time: 2024-07-23 14:56:20.981 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/23 14:56:21.132 +00:00] [INFO] [ddl.go:517] ["[ddl] DDL job is finished"] [jobID=85]
   > [2024/07/23 14:56:21.136 +00:00] [INFO] [domain.go:646] ["performing DDL change, must reload"]
   > [2024/07/23 14:56:21.137 +00:00] [INFO] [split_region.go:61] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=748000000000000054]
   > [2024/07/23 14:56:21.137 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:43736] [split_keys="key 7480000000000000FF5400000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/23 14:56:21.137 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=60] [peer-ids="[61]"]
   > [2024/07/23 14:56:21.138 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF4E00000000000000F8 region_epoch { conf_ver: 1 version: 29 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 60 new_peer_ids: 61]"] [region_id=2]
   > [2024/07/23 14:56:21.144 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF5400000000000000F8 new_region_id: 60 new_peer_ids: 61 } right_derive: true }"] [index=82] [term=6] [peer_id=3] [region_id=2]
   > [2024/07/23 14:56:21.145 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF5400000000000000F8"] [region="id: 2 start_key: 7480000000000000FF4E00000000000000F8 region_epoch { conf_ver: 1 version: 29 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/07/23 14:56:21.150 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/23 14:56:21.150 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=2]
   > [2024/07/23 14:56:21.150 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/07/23 14:56:21.150 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(55)] [region_id=2] [store_id=Some(1)]
   > [2024/07/23 14:56:21.150 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 2 start_key: 7480000000000000FF5400000000000000F8 region_epoch { conf_ver: 1 version: 30 } peers { id: 3 store_id: 1 }"]
   > [2024/07/23 14:56:21.150 +00:00] [INFO] [split_region.go:158] ["batch split regions complete"] ["batch region ID"=2] ["first at"=748000000000000054] ["first new region left"="{Id:60 StartKey:7480000000000000ff4e00000000000000f8 EndKey:7480000000000000ff5400000000000000f8 RegionEpoch:{ConfVer:1 Version:30} Peers:[id:61 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/23 14:56:21.150 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 60 start_key: 7480000000000000FF4E00000000000000F8 end_key: 7480000000000000FF5400000000000000F8 region_epoch { conf_ver: 1 version: 30 } peers { id: 61 store_id: 1 }"] [region_id=60]
   > [2024/07/23 14:56:21.151 +00:00] [INFO] [split_region.go:207] ["split regions complete"] ["region count"=1] ["region IDs"="[60]"]
   > [2024/07/23 14:56:21.151 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=61] [region_id=60]
   > [2024/07/23 14:56:21.151 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF4E00000000000000F8} -> {7480000000000000FF5400000000000000F8}, EndKey:{}"] [old-version=29] [new-version=30]
   > [2024/07/23 14:56:21.151 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 2 start_key: 7480000000000000FF5400000000000000F8 region_epoch { conf_ver: 1 version: 30 } peers { id: 3 store_id: 1 } }"]
   > [2024/07/23 14:56:21.151 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 2 start_key: 7480000000000000FF5400000000000000F8 region_epoch { conf_ver: 1 version: 30 } peers { id: 3 store_id: 1 }"]
   > [2024/07/23 14:56:21.151 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {61} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=61] [region_id=60]
   > [2024/07/23 14:56:21.151 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=61] [region_id=60]
   > [2024/07/23 14:56:21.151 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=2] [origin="id:60 start_key:\"7480000000000000FF4E00000000000000F8\" end_key:\"7480000000000000FF5400000000000000F8\" region_epoch:<conf_ver:1 version:30 > peers:<id:61 store_id:1 >"] [total=1]
   > [2024/07/23 14:56:21.151 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {61} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=61] [region_id=60]
   > [2024/07/23 14:56:21.151 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 61."] [id=61] [raft_id=61] [region_id=60]
   > [2024/07/23 14:56:21.151 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=61] [region_id=60]
   > [2024/07/23 14:56:21.151 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=61] [region_id=60]
   > [2024/07/23 14:56:21.151 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=61] [region_id=60]
   > [2024/07/23 14:56:21.151 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=61] [region_id=60]
   > [2024/07/23 14:56:21.152 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803836] [region_id=60]
   > [2024/07/23 14:56:21.152 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=82] [observe_id=ObserveId(57)] [region=2]
   > [2024/07/23 14:56:21.152 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=60]
   > [2024/07/23 14:56:21.156 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 60 start_key: 7480000000000000FF4E00000000000000F8 end_key: 7480000000000000FF5400000000000000F8 region_epoch { conf_ver: 1 version: 30 } peers { id: 61 store_id: 1 }"]
   > [2024/07/23 14:56:21.157 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(58)] [region=60]
   > [2024/07/23 14:56:22.199 +00:00] [INFO] [set.go:216] ["set global var"] [conn=13] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/07/23 14:56:22.201 +00:00] [INFO] [set.go:216] ["set global var"] [conn=13] [name=transaction_isolation] [val=READ-COMMITTED]
   > [2024/07/23 14:56:23.094 +00:00] [INFO] [domain.go:146] ["full load InfoSchema success"] [usedSchemaVersion=0] [neededSchemaVersion=65] ["start time"=10.124025ms]
   > [2024/07/23 14:56:23.100 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=65]
   > [2024/07/23 14:56:23.101 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=65]
   > [2024/07/23 14:56:23.119 +00:00] [INFO] [domain.go:146] ["full load InfoSchema success"] [usedSchemaVersion=0] [neededSchemaVersion=65] ["start time"=16.318736ms]
   > [2024/07/23 14:56:23.126 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=65]
   > [2024/07/23 14:56:23.126 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=65]
   > [2024/07/23 14:56:23.128 +00:00] [INFO] [admin.go:333] ["check indices count"] [table=t] [cnt=3] [index="\"PRIMARY\""] [cnt=3]
   > [2024/07/23 14:56:23.144 +00:00] [INFO] [domain.go:146] ["full load InfoSchema success"] [usedSchemaVersion=0] [neededSchemaVersion=65] ["start time"=15.598175ms]
   > [2024/07/23 14:56:23.151 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=65]
   > [2024/07/23 14:56:23.151 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=65]
   > [2024/07/23 14:56:23.153 +00:00] [INFO] [admin.go:333] ["check indices count"] [table=t] [cnt=3] [index="\"c_int\""] [cnt=3]
   > [2024/07/23 14:56:23.170 +00:00] [INFO] [domain.go:146] ["full load InfoSchema success"] [usedSchemaVersion=0] [neededSchemaVersion=65] ["start time"=15.726685ms]
   > [2024/07/23 14:56:23.176 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=65]
   > [2024/07/23 14:56:23.176 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=0] [schemaVersion=65]
   > [2024/07/23 14:56:23.178 +00:00] [INFO] [admin.go:333] ["check indices count"] [table=t] [cnt=3] [index="\"c_datetime\""] [cnt=3]
