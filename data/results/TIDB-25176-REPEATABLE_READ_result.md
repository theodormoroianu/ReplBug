# Bug ID TIDB-25176-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/25176
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              Setting tidb_snapshot breaks the isolation guarantees.


## Details
 * Database: tidb-v4.0.7.tikv
 * Number of scenarios: 1
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows: 0
 * Instruction #1:
     - Instruction:  begin;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows: 0
 * Instruction #2:
     - Instruction:  update test.ttt set a=2 where id=1;
     - Transaction: conn_1
     - Output: None
     - Executed order: 2
     - Affected rows: 1
 * Instruction #3:
     - Instruction:  set @@tidb_snapshot=TIMESTAMP(NOW());
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows: 0
 * Instruction #4:
     - Instruction:  select a from test.ttt where id=1;
     - Transaction: conn_0
     - Output: [(1,)]
     - Executed order: 4
     - Affected rows: 1
 * Instruction #5:
     - Instruction:  select a from test.ttt where id=1 for update;
     - Transaction: conn_0
     - Output: [(2,)]
     - Executed order: 5
     - Affected rows: 1
 * Instruction #6:
     - Instruction:  select a from test.ttt where id=1;
     - Transaction: conn_0
     - Output: [(2,)]
     - Executed order: 6
     - Affected rows: 1
 * Instruction #7:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: None
     - Executed order: 7
     - Affected rows: 0

 * Container logs:
   > [2024/08/05 07:08:26.794 +00:00] [INFO] [server.go:394] ["new connection"] [conn=2] [remoteAddr=127.0.0.1:40774]
   > [2024/08/05 07:08:26.797 +00:00] [INFO] [session.go:2159] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=22] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/08/05 07:08:26.798 +00:00] [INFO] [session.go:2159] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=22] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/08/05 07:08:26.829 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-05 07:08:26.809 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/05 07:08:26.829 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-05 07:08:26.809 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/08/05 07:08:26.833 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-05 07:08:26.809 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/05 07:08:26.851 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=22] [neededSchemaVersion=23] ["start time"=1.231387ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/05 07:08:26.900 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=23] ["take time"=52.494052ms] [job="ID:46, Type:create schema, State:done, SchemaState:public, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-05 07:08:26.809 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/05 07:08:26.903 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:46, Type:create schema, State:synced, SchemaState:public, SchemaID:45, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-05 07:08:26.809 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/05 07:08:26.916 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=46]
   > [2024/08/05 07:08:26.916 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/08/05 07:08:26.919 +00:00] [INFO] [session.go:2159] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=23] [cur_db=testdb] [sql="create table test.ttt (id int primary key, a int);"] [user=root@127.0.0.1]
   > [2024/08/05 07:08:26.945 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:1, TableID:47, RowCount:0, ArgLen:1, start time: 2024-08-05 07:08:26.909 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/05 07:08:26.945 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:1, TableID:47, RowCount:0, ArgLen:1, start time: 2024-08-05 07:08:26.909 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table test.ttt (id int primary key, a int);"]
   > [2024/08/05 07:08:26.949 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:1, TableID:47, RowCount:0, ArgLen:0, start time: 2024-08-05 07:08:26.909 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/05 07:08:26.971 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=23] [neededSchemaVersion=24] ["start time"=2.163989ms] [phyTblIDs="[47]"] [actionTypes="[8]"]
   > [2024/08/05 07:08:27.019 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=24] ["take time"=52.339911ms] [job="ID:48, Type:create table, State:done, SchemaState:public, SchemaID:1, TableID:47, RowCount:0, ArgLen:1, start time: 2024-08-05 07:08:26.909 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/05 07:08:27.021 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:48, Type:create table, State:synced, SchemaState:public, SchemaID:1, TableID:47, RowCount:0, ArgLen:0, start time: 2024-08-05 07:08:26.909 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/05 07:08:27.035 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=48]
   > [2024/08/05 07:08:27.037 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/08/05 07:08:27.037 +00:00] [INFO] [split_region.go:58] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=74800000000000002f]
   > [2024/08/05 07:08:27.038 +00:00] [INFO] [peer.rs:469] ["on split"] [split_keys="key 7480000000000000FF2F00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/08/05 07:08:27.038 +00:00] [INFO] [cluster_worker.go:131] ["alloc ids for region split"] [region-id=44] [peer-ids="[45]"]
   > [2024/08/05 07:08:27.039 +00:00] [INFO] [pd.rs:499] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF2B00000000000000F8 region_epoch { conf_ver: 1 version: 21 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 44 new_peer_ids: 45]"] [region_id=2]
   > [2024/08/05 07:08:27.043 +00:00] [INFO] [apply.rs:1162] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF2F00000000000000F8 new_region_id: 44 new_peer_ids: 45 } right_derive: true }"] [index=53] [term=6] [peer_id=3] [region_id=2]
   > [2024/08/05 07:08:27.043 +00:00] [INFO] [apply.rs:1742] ["split region"] [keys="key 7480000000000000FF2F00000000000000F8"] [region="id: 2 start_key: 7480000000000000FF2B00000000000000F8 region_epoch { conf_ver: 1 version: 21 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/08/05 07:08:27.050 +00:00] [INFO] [peer.rs:1731] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/08/05 07:08:27.050 +00:00] [INFO] [peer.rs:1773] ["insert new region"] [region="id: 44 start_key: 7480000000000000FF2B00000000000000F8 end_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 45 store_id: 1 }"] [region_id=44]
   > [2024/08/05 07:08:27.051 +00:00] [INFO] [peer.rs:159] ["create peer"] [peer_id=45] [region_id=44]
   > [2024/08/05 07:08:27.051 +00:00] [INFO] [raft.rs:783] ["became follower at term 5"] [term=5] [raft_id=45] [region_id=44]
   > [2024/08/05 07:08:27.051 +00:00] [INFO] [raft.rs:285] [newRaft] [peers="[(45, Progress { matched: 5, next_idx: 6, state: Probe, paused: false, pending_snapshot: 0, pending_request_snapshot: 0, recent_active: false, ins: Inflights { start: 0, count: 0, buffer: [] } })]"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=45] [region_id=44]
   > [2024/08/05 07:08:27.051 +00:00] [INFO] [raw_node.rs:222] ["RawNode created with id 45."] [id=45] [raft_id=45] [region_id=44]
   > [2024/08/05 07:08:27.051 +00:00] [INFO] [raft.rs:1177] ["starting a new election"] [term=5] [raft_id=45] [region_id=44]
   > [2024/08/05 07:08:27.051 +00:00] [INFO] [cluster.go:542] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF2B00000000000000F8} -> {7480000000000000FF2F00000000000000F8}, EndKey:{}"] [old-version=21] [new-version=22]
   > [2024/08/05 07:08:27.051 +00:00] [INFO] [raft.rs:833] ["became pre-candidate at term 5"] [term=5] [raft_id=45] [region_id=44]
   > [2024/08/05 07:08:27.051 +00:00] [INFO] [cluster_worker.go:223] ["region batch split, generate new regions"] [region-id=2] [origin="id:44 start_key:\"7480000000000000FF2B00000000000000F8\" end_key:\"7480000000000000FF2F00000000000000F8\" region_epoch:<conf_ver:1 version:22 > peers:<id:45 store_id:1 >"] [total=1]
   > [2024/08/05 07:08:27.051 +00:00] [INFO] [raft.rs:902] ["45 received message from 45"] [term=5] [msg=MsgRequestPreVote] [from=45] [id=45] [raft_id=45] [region_id=44]
   > [2024/08/05 07:08:27.051 +00:00] [INFO] [split_region.go:155] ["batch split regions complete"] ["batch region ID"=2] ["first at"=74800000000000002f] ["first new region left"="{Id:44 StartKey:7480000000000000ff2b00000000000000f8 EndKey:7480000000000000ff2f00000000000000f8 RegionEpoch:{ConfVer:1 Version:22} Peers:[id:45 store_id:1 ]}"] ["new region count"=1]
   > [2024/08/05 07:08:27.051 +00:00] [INFO] [split_region.go:207] ["split regions complete"] ["region count"=1] ["region IDs"="[44]"]
   > [2024/08/05 07:08:27.051 +00:00] [INFO] [raft.rs:807] ["became candidate at term 6"] [term=6] [raft_id=45] [region_id=44]
   > [2024/08/05 07:08:27.051 +00:00] [INFO] [raft.rs:902] ["45 received message from 45"] [term=6] [msg=MsgRequestVote] [from=45] [id=45] [raft_id=45] [region_id=44]
   > [2024/08/05 07:08:27.052 +00:00] [INFO] [raft.rs:874] ["became leader at term 6"] [term=6] [raft_id=45] [region_id=44]
   > [2024/08/05 07:08:27.066 +00:00] [INFO] [server.go:397] ["connection closed"] [conn=2]
   > [2024/08/05 07:08:28.094 +00:00] [INFO] [server.go:394] ["new connection"] [conn=4] [remoteAddr=127.0.0.1:40786]
   > [2024/08/05 07:08:28.103 +00:00] [INFO] [set.go:216] ["set session var"] [conn=4] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/08/05 07:08:28.105 +00:00] [INFO] [set.go:216] ["set session var"] [conn=4] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/08/05 07:08:28.105 +00:00] [INFO] [set.go:216] ["set session var"] [conn=4] [name=transaction_isolation] [val=REPEATABLE-READ]
   > [2024/08/05 07:08:28.703 +00:00] [INFO] [server.go:394] ["new connection"] [conn=5] [remoteAddr=127.0.0.1:44850]
   > [2024/08/05 07:08:28.707 +00:00] [INFO] [set.go:216] ["set session var"] [conn=5] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/08/05 07:08:29.005 +00:00] [INFO] [set.go:317] ["load snapshot info schema"] [conn=4] [SnapshotTS=451632616964096000]
   > [2024/08/05 07:08:29.019 +00:00] [INFO] [domain.go:146] ["full load InfoSchema success"] [usedSchemaVersion=0] [neededSchemaVersion=24] ["start time"=13.432041ms]
   > [2024/08/05 07:08:29.020 +00:00] [INFO] [set.go:216] ["set session var"] [conn=4] [name=tidb_snapshot] [val="2024-08-05 07:08:29"]
   > [2024/08/05 07:08:29.303 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=4] [schemaVersion=24]
   > [2024/08/05 07:08:29.603 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=4] [schemaVersion=24]
   > [2024/08/05 07:08:29.605 +00:00] [INFO] [adapter.go:611] ["pessimistic write conflict, retry statement"] [conn=4] [txn=451632616796061697] [forUpdateTS=451632616796061697] [err="[kv:9007]Write conflict, txnStartTS=451632616796061697, conflictStartTS=451632616874704902, conflictCommitTS=451632616887549953, key={tableID=47, handle=1} primary={tableID=47, handle=1} [try again later]"]
   > [2024/08/05 07:08:29.904 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=4] [schemaVersion=24]
   > [2024/08/05 07:08:30.204 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=4] [schemaVersion=24]
   > [2024/08/05 07:08:30.605 +00:00] [INFO] [server.go:397] ["connection closed"] [conn=4]
   > [2024/08/05 07:08:30.605 +00:00] [INFO] [server.go:397] ["connection closed"] [conn=5]
