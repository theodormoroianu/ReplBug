# Bug ID TIDB-21618-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/21618
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              pessimistic lock doesn't work on the partition for subquery/joins


## Details
 * Database: tidb-v6.4.0.tikv
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
     - Instruction:  begin pessimistic;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows: 0
 * Instruction #2:
     - Instruction:  select * from t where d_int in (select d_int from t where c_int = 1) for update...
     - Transaction: conn_0
     - Output: [(1, 2)]
     - Executed order: 2
     - Affected rows: 1
     - Warnings: [('Warning', 1105, 'disable dynamic pruning due to t has no global stats'), ('Warning', 1105, 'disable dynamic pruning due to t has no global stats')]
 * Instruction #3:
     - Instruction:  begin pessimistic;
     - Transaction: conn_1
     - Output: None
     - Executed order: 3
     - Affected rows: 0
 * Instruction #4:
     - Instruction:  select * from t where d_int = 2 for update;
     - Transaction: conn_1
     - Output: [(1, 2)]
     - Executed order: 4
     - Affected rows: 1
     - Warnings: [('Warning', 1105, 'disable dynamic pruning due to t has no global stats')]
 * Instruction #5:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 5
     - Affected rows: 0
 * Instruction #6:
     - Instruction:  COMMIT;
     - Transaction: conn_1
     - Output: None
     - Executed order: 6
     - Affected rows: 0

 * Container logs:
   > [2024/07/24 12:12:21.157 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/24 12:12:21.160 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=6993195218841371039] [schemaVersion=44] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/24 12:12:21.197 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:84, Type:drop schema, State:queueing, SchemaState:public, SchemaID:79, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:12:21.132 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 12:12:21.197 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:84, Type:drop schema, State:queueing, SchemaState:public, SchemaID:79, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:12:21.132 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/24 12:12:21.222 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:84, Type:drop schema, State:queueing, SchemaState:public, SchemaID:79, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:12:21.132 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:12:21.277 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=44] [neededSchemaVersion=45] ["start time"=890.904µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:12:21.325 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=45] ["take time"=58.548337ms] [job="ID:84, Type:drop schema, State:running, SchemaState:write only, SchemaID:79, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:12:21.132 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:12:21.330 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:84, Type:drop schema, State:running, SchemaState:write only, SchemaID:79, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:12:21.132 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:12:21.390 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=45] [neededSchemaVersion=46] ["start time"=900.543µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:12:21.438 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=46] ["take time"=61.732713ms] [job="ID:84, Type:drop schema, State:running, SchemaState:delete only, SchemaID:79, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:12:21.132 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:12:21.444 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:84, Type:drop schema, State:running, SchemaState:delete only, SchemaID:79, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:12:21.132 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:12:21.504 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=46] [neededSchemaVersion=47] ["start time"=828.186µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:12:21.553 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=47] ["take time"=67.273977ms] [job="ID:84, Type:drop schema, State:done, SchemaState:none, SchemaID:79, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:12:21.132 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:12:21.559 +00:00] [INFO] [delete_range.go:109] ["[ddl] add job into delete-range table"] [jobID=84] [jobType="drop schema"]
   > [2024/07/24 12:12:21.560 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:84, Type:drop schema, State:synced, SchemaState:none, SchemaID:79, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:12:21.132 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:12:21.583 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000054FF0000000000000000F7 lock_version: 451365605613764610 key: 748000FFFFFFFFFFFE5F728000000000000054 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451365605613764611"]
   > [2024/07/24 12:12:21.587 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=84]
   > [2024/07/24 12:12:21.587 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 12:12:21.590 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000054FF0000000000000000F7 lock_version: 451365605613764610 key: 748000FFFFFFFFFFFE5F728000000000000054 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451365605613764611"]
   > [2024/07/24 12:12:21.590 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000054FF0000000000000000F7 lock_version: 451365605613764610 key: 748000FFFFFFFFFFFE5F728000000000000054 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451365605613764611"]
   > [2024/07/24 12:12:21.591 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=6993195218841371039] [schemaVersion=47] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/24 12:12:21.653 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:86, Type:create schema, State:queueing, SchemaState:none, SchemaID:85, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:12:21.582 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 12:12:21.653 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:86, Type:create schema, State:queueing, SchemaState:none, SchemaID:85, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:12:21.582 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/24 12:12:21.683 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:86, Type:create schema, State:queueing, SchemaState:none, SchemaID:85, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:12:21.582 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:12:21.738 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=47] [neededSchemaVersion=48] ["start time"=1.542461ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:12:21.786 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=48] ["take time"=64.581568ms] [job="ID:86, Type:create schema, State:done, SchemaState:public, SchemaID:85, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:12:21.582 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:12:21.792 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:86, Type:create schema, State:synced, SchemaState:public, SchemaID:85, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:12:21.582 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:12:21.819 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=86]
   > [2024/07/24 12:12:21.819 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 12:12:21.820 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000056FF0000000000000000F7 lock_version: 451365605679300610 key: 748000FFFFFFFFFFFE5F728000000000000056 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451365605679300611"]
   > [2024/07/24 12:12:21.820 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000056FF0000000000000000F7 lock_version: 451365605679300610 key: 748000FFFFFFFFFFFE5F728000000000000056 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451365605679300611"]
   > [2024/07/24 12:12:21.823 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=6993195218841371039] [schemaVersion=48] [cur_db=testdb] [sql="create table t (c_int int, d_int int, primary key (c_int), key(d_int)) partition by hash (c_int) partitions 4 ;"] [user=root@%]
   > [2024/07/24 12:12:21.825 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000056FF0000000000000000F7 lock_version: 451365605679300610 key: 748000FFFFFFFFFFFE5F728000000000000056 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451365605679300611"]
   > [2024/07/24 12:12:21.825 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000056FF0000000000000000F7 lock_version: 451365605679300610 key: 748000FFFFFFFFFFFE5F728000000000000056 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451365605679300611"]
   > [2024/07/24 12:12:21.903 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:92, Type:create table, State:queueing, SchemaState:none, SchemaID:85, TableID:87, RowCount:0, ArgLen:2, start time: 2024-07-24 12:12:21.832 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 12:12:21.903 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:92, Type:create table, State:queueing, SchemaState:none, SchemaID:85, TableID:87, RowCount:0, ArgLen:2, start time: 2024-07-24 12:12:21.832 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t (c_int int, d_int int, primary key (c_int), key(d_int)) partition by hash (c_int) partitions 4 ;"]
   > [2024/07/24 12:12:21.930 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:92, Type:create table, State:queueing, SchemaState:none, SchemaID:85, TableID:87, RowCount:0, ArgLen:0, start time: 2024-07-24 12:12:21.832 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:12:21.996 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=48] [neededSchemaVersion=49] ["start time"=3.046438ms] [phyTblIDs="[87,88,89,90,91]"] [actionTypes="[8,8,8,8,8]"]
   > [2024/07/24 12:12:22.042 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=49] ["take time"=62.250103ms] [job="ID:92, Type:create table, State:done, SchemaState:public, SchemaID:85, TableID:87, RowCount:0, ArgLen:2, start time: 2024-07-24 12:12:21.832 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:12:22.049 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:92, Type:create table, State:synced, SchemaState:public, SchemaID:85, TableID:87, RowCount:0, ArgLen:0, start time: 2024-07-24 12:12:21.832 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:12:22.089 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=92]
   > [2024/07/24 12:12:22.089 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 12:12:22.089 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=10] ["first split key"=748000000000000058]
   > [2024/07/24 12:12:22.090 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000005CFF0000000000000000F7 lock_version: 451365605744836612 key: 748000FFFFFFFFFFFE5F72800000000000005C lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451365605744836613"]
   > [2024/07/24 12:12:22.090 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000005CFF0000000000000000F7 lock_version: 451365605744836612 key: 748000FFFFFFFFFFFE5F72800000000000005C lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451365605744836613"]
   > [2024/07/24 12:12:22.092 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:60178] [split_keys="key 7480000000000000FF5800000000000000F8"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:22.093 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=88] [peer-ids="[89]"]
   > [2024/07/24 12:12:22.093 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 10 start_key: 7480000000000000FF5100000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 43 } peers { id: 11 store_id: 1 }"] [new_region_ids="[new_region_id: 88 new_peer_ids: 89]"] [region_id=10]
   > [2024/07/24 12:12:22.096 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000005CFF0000000000000000F7 lock_version: 451365605744836612 key: 748000FFFFFFFFFFFE5F72800000000000005C lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451365605744836613"]
   > [2024/07/24 12:12:22.097 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000005CFF0000000000000000F7 lock_version: 451365605744836612 key: 748000FFFFFFFFFFFE5F72800000000000005C lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451365605744836613"]
   > [2024/07/24 12:12:22.117 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF5800000000000000F8 new_region_id: 88 new_peer_ids: 89 } right_derive: true }"] [index=73] [term=6] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:22.117 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF5800000000000000F8"] [region="id: 10 start_key: 7480000000000000FF5100000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 43 } peers { id: 11 store_id: 1 }"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:22.123 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/24 12:12:22.123 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=10]
   > [2024/07/24 12:12:22.123 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(83)] [region_id=10] [store_id=Some(1)]
   > [2024/07/24 12:12:22.123 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:22.123 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 10 start_key: 7480000000000000FF5800000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 44 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 12:12:22.123 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 88 start_key: 7480000000000000FF5100000000000000F8 end_key: 7480000000000000FF5800000000000000F8 region_epoch { conf_ver: 1 version: 44 } peers { id: 89 store_id: 1 }"] [region_id=88]
   > [2024/07/24 12:12:22.123 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=89] [region_id=88]
   > [2024/07/24 12:12:22.123 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 10 start_key: 7480000000000000FF5800000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 44 } peers { id: 11 store_id: 1 } }"]
   > [2024/07/24 12:12:22.123 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 10 start_key: 7480000000000000FF5800000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 44 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 12:12:22.124 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {89} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=89] [region_id=88]
   > [2024/07/24 12:12:22.124 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=10] ["first at"=748000000000000058] ["first new region left"="{Id:88 StartKey:7480000000000000ff5100000000000000f8 EndKey:7480000000000000ff5800000000000000f8 RegionEpoch:{ConfVer:1 Version:44} Peers:[id:89 store_id:1 ] EncryptionMeta:<nil> IsInFlashback:false}"] ["new region count"=1]
   > [2024/07/24 12:12:22.124 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=10] [detail="StartKey Changed:{7480000000000000FF5100000000000000F8} -> {7480000000000000FF5800000000000000F8}, EndKey:{748000FFFFFFFFFFFFFB00000000000000F8}"] [old-version=43] [new-version=44]
   > [2024/07/24 12:12:22.124 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=89] [region_id=88]
   > [2024/07/24 12:12:22.124 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[88]"]
   > [2024/07/24 12:12:22.124 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=10] ["first split key"=748000000000000059]
   > [2024/07/24 12:12:22.124 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {89} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=89] [region_id=88]
   > [2024/07/24 12:12:22.124 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 89."] [id=89] [raft_id=89] [region_id=88]
   > [2024/07/24 12:12:22.124 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=10] [origin="id:88 start_key:\"7480000000000000FF5100000000000000F8\" end_key:\"7480000000000000FF5800000000000000F8\" region_epoch:<conf_ver:1 version:44 > peers:<id:89 store_id:1 >"] [total=1]
   > [2024/07/24 12:12:22.124 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=89] [region_id=88]
   > [2024/07/24 12:12:22.124 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=89] [region_id=88]
   > [2024/07/24 12:12:22.124 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=89] [region_id=88]
   > [2024/07/24 12:12:22.124 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=89] [region_id=88]
   > [2024/07/24 12:12:22.124 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803864] [region_id=88]
   > [2024/07/24 12:12:22.124 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=73] [observe_id=ObserveId(85)] [region=10]
   > [2024/07/24 12:12:22.125 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:60142] [split_keys="key 7480000000000000FF5900000000000000F8"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:22.125 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=88]
   > [2024/07/24 12:12:22.125 +00:00] [INFO] [peer.rs:5566] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 43"] [prev_epoch="conf_ver: 1 version: 44"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:22.128 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:60164] [split_keys="key 7480000000000000FF5900000000000000F8"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:22.128 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=90] [peer-ids="[91]"]
   > [2024/07/24 12:12:22.129 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 10 start_key: 7480000000000000FF5800000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 44 } peers { id: 11 store_id: 1 }"] [new_region_ids="[new_region_id: 90 new_peer_ids: 91]"] [region_id=10]
   > [2024/07/24 12:12:22.130 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 88 start_key: 7480000000000000FF5100000000000000F8 end_key: 7480000000000000FF5800000000000000F8 region_epoch { conf_ver: 1 version: 44 } peers { id: 89 store_id: 1 }"]
   > [2024/07/24 12:12:22.131 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(86)] [region=88]
   > [2024/07/24 12:12:22.136 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF5900000000000000F8 new_region_id: 90 new_peer_ids: 91 } right_derive: true }"] [index=74] [term=6] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:22.136 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF5900000000000000F8"] [region="id: 10 start_key: 7480000000000000FF5800000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 44 } peers { id: 11 store_id: 1 }"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:22.142 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/24 12:12:22.142 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=10]
   > [2024/07/24 12:12:22.143 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(85)] [region_id=10] [store_id=Some(1)]
   > [2024/07/24 12:12:22.143 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:22.143 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 10 start_key: 7480000000000000FF5900000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 45 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 12:12:22.143 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=10] ["first at"=748000000000000059] ["first new region left"="{Id:90 StartKey:7480000000000000ff5800000000000000f8 EndKey:7480000000000000ff5900000000000000f8 RegionEpoch:{ConfVer:1 Version:45} Peers:[id:91 store_id:1 ] EncryptionMeta:<nil> IsInFlashback:false}"] ["new region count"=1]
   > [2024/07/24 12:12:22.143 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[90]"]
   > [2024/07/24 12:12:22.143 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 10 start_key: 7480000000000000FF5900000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 45 } peers { id: 11 store_id: 1 } }"]
   > [2024/07/24 12:12:22.143 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=10] ["first split key"=74800000000000005a]
   > [2024/07/24 12:12:22.143 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 10 start_key: 7480000000000000FF5900000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 45 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 12:12:22.143 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 90 start_key: 7480000000000000FF5800000000000000F8 end_key: 7480000000000000FF5900000000000000F8 region_epoch { conf_ver: 1 version: 45 } peers { id: 91 store_id: 1 }"] [region_id=90]
   > [2024/07/24 12:12:22.143 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=91] [region_id=90]
   > [2024/07/24 12:12:22.143 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {91} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=91] [region_id=90]
   > [2024/07/24 12:12:22.143 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=10] [detail="StartKey Changed:{7480000000000000FF5800000000000000F8} -> {7480000000000000FF5900000000000000F8}, EndKey:{748000FFFFFFFFFFFFFB00000000000000F8}"] [old-version=44] [new-version=45]
   > [2024/07/24 12:12:22.143 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=91] [region_id=90]
   > [2024/07/24 12:12:22.143 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=10] [origin="id:90 start_key:\"7480000000000000FF5800000000000000F8\" end_key:\"7480000000000000FF5900000000000000F8\" region_epoch:<conf_ver:1 version:45 > peers:<id:91 store_id:1 >"] [total=1]
   > [2024/07/24 12:12:22.143 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {91} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=91] [region_id=90]
   > [2024/07/24 12:12:22.144 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 91."] [id=91] [raft_id=91] [region_id=90]
   > [2024/07/24 12:12:22.144 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=91] [region_id=90]
   > [2024/07/24 12:12:22.144 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=91] [region_id=90]
   > [2024/07/24 12:12:22.144 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=91] [region_id=90]
   > [2024/07/24 12:12:22.144 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=91] [region_id=90]
   > [2024/07/24 12:12:22.144 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803866] [region_id=90]
   > [2024/07/24 12:12:22.144 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=90]
   > [2024/07/24 12:12:22.150 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:60150] [split_keys="key 7480000000000000FF5A00000000000000F8"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:22.150 +00:00] [INFO] [peer.rs:5566] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 44"] [prev_epoch="conf_ver: 1 version: 45"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:22.150 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=74] [observe_id=ObserveId(87)] [region=10]
   > [2024/07/24 12:12:22.150 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 90 start_key: 7480000000000000FF5800000000000000F8 end_key: 7480000000000000FF5900000000000000F8 region_epoch { conf_ver: 1 version: 45 } peers { id: 91 store_id: 1 }"]
   > [2024/07/24 12:12:22.150 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(88)] [region=90]
   > [2024/07/24 12:12:22.153 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:60178] [split_keys="key 7480000000000000FF5A00000000000000F8"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:22.154 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=92] [peer-ids="[93]"]
   > [2024/07/24 12:12:22.154 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 10 start_key: 7480000000000000FF5900000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 45 } peers { id: 11 store_id: 1 }"] [new_region_ids="[new_region_id: 92 new_peer_ids: 93]"] [region_id=10]
   > [2024/07/24 12:12:22.161 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF5A00000000000000F8 new_region_id: 92 new_peer_ids: 93 } right_derive: true }"] [index=75] [term=6] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:22.162 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF5A00000000000000F8"] [region="id: 10 start_key: 7480000000000000FF5900000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 45 } peers { id: 11 store_id: 1 }"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:22.167 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/24 12:12:22.167 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=10]
   > [2024/07/24 12:12:22.168 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(87)] [region_id=10] [store_id=Some(1)]
   > [2024/07/24 12:12:22.168 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:22.168 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 10 start_key: 7480000000000000FF5A00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 46 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 12:12:22.168 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 92 start_key: 7480000000000000FF5900000000000000F8 end_key: 7480000000000000FF5A00000000000000F8 region_epoch { conf_ver: 1 version: 46 } peers { id: 93 store_id: 1 }"] [region_id=92]
   > [2024/07/24 12:12:22.168 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=93] [region_id=92]
   > [2024/07/24 12:12:22.168 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=10] ["first at"=74800000000000005a] ["first new region left"="{Id:92 StartKey:7480000000000000ff5900000000000000f8 EndKey:7480000000000000ff5a00000000000000f8 RegionEpoch:{ConfVer:1 Version:46} Peers:[id:93 store_id:1 ] EncryptionMeta:<nil> IsInFlashback:false}"] ["new region count"=1]
   > [2024/07/24 12:12:22.168 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[92]"]
   > [2024/07/24 12:12:22.168 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 10 start_key: 7480000000000000FF5A00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 46 } peers { id: 11 store_id: 1 } }"]
   > [2024/07/24 12:12:22.168 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=10] ["first split key"=74800000000000005b]
   > [2024/07/24 12:12:22.168 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 10 start_key: 7480000000000000FF5A00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 46 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 12:12:22.168 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=10] [detail="StartKey Changed:{7480000000000000FF5900000000000000F8} -> {7480000000000000FF5A00000000000000F8}, EndKey:{748000FFFFFFFFFFFFFB00000000000000F8}"] [old-version=45] [new-version=46]
   > [2024/07/24 12:12:22.168 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {93} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=93] [region_id=92]
   > [2024/07/24 12:12:22.168 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=10] [origin="id:92 start_key:\"7480000000000000FF5900000000000000F8\" end_key:\"7480000000000000FF5A00000000000000F8\" region_epoch:<conf_ver:1 version:46 > peers:<id:93 store_id:1 >"] [total=1]
   > [2024/07/24 12:12:22.168 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=93] [region_id=92]
   > [2024/07/24 12:12:22.168 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {93} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=93] [region_id=92]
   > [2024/07/24 12:12:22.169 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 93."] [id=93] [raft_id=93] [region_id=92]
   > [2024/07/24 12:12:22.169 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=93] [region_id=92]
   > [2024/07/24 12:12:22.169 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=93] [region_id=92]
   > [2024/07/24 12:12:22.169 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=93] [region_id=92]
   > [2024/07/24 12:12:22.169 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=93] [region_id=92]
   > [2024/07/24 12:12:22.169 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803868] [region_id=92]
   > [2024/07/24 12:12:22.169 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=75] [observe_id=ObserveId(89)] [region=10]
   > [2024/07/24 12:12:22.169 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:60142] [split_keys="key 7480000000000000FF5B00000000000000F8"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:22.169 +00:00] [INFO] [peer.rs:5566] ["epoch changed, retry later"] [epoch="conf_ver: 1 version: 45"] [prev_epoch="conf_ver: 1 version: 46"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:22.170 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=92]
   > [2024/07/24 12:12:22.173 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:60164] [split_keys="key 7480000000000000FF5B00000000000000F8"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:22.173 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=94] [peer-ids="[95]"]
   > [2024/07/24 12:12:22.174 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 10 start_key: 7480000000000000FF5A00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 46 } peers { id: 11 store_id: 1 }"] [new_region_ids="[new_region_id: 94 new_peer_ids: 95]"] [region_id=10]
   > [2024/07/24 12:12:22.175 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 92 start_key: 7480000000000000FF5900000000000000F8 end_key: 7480000000000000FF5A00000000000000F8 region_epoch { conf_ver: 1 version: 46 } peers { id: 93 store_id: 1 }"]
   > [2024/07/24 12:12:22.175 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(90)] [region=92]
   > [2024/07/24 12:12:22.180 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF5B00000000000000F8 new_region_id: 94 new_peer_ids: 95 } right_derive: true }"] [index=76] [term=6] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:22.181 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF5B00000000000000F8"] [region="id: 10 start_key: 7480000000000000FF5A00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 46 } peers { id: 11 store_id: 1 }"] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:22.186 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/24 12:12:22.186 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=10]
   > [2024/07/24 12:12:22.186 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=11] [region_id=10]
   > [2024/07/24 12:12:22.186 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 94 start_key: 7480000000000000FF5A00000000000000F8 end_key: 7480000000000000FF5B00000000000000F8 region_epoch { conf_ver: 1 version: 47 } peers { id: 95 store_id: 1 }"] [region_id=94]
   > [2024/07/24 12:12:22.187 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=10] ["first at"=74800000000000005b] ["first new region left"="{Id:94 StartKey:7480000000000000ff5a00000000000000f8 EndKey:7480000000000000ff5b00000000000000f8 RegionEpoch:{ConfVer:1 Version:47} Peers:[id:95 store_id:1 ] EncryptionMeta:<nil> IsInFlashback:false}"] ["new region count"=1]
   > [2024/07/24 12:12:22.187 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[94]"]
   > [2024/07/24 12:12:22.187 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=95] [region_id=94]
   > [2024/07/24 12:12:22.187 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=10] [detail="StartKey Changed:{7480000000000000FF5A00000000000000F8} -> {7480000000000000FF5B00000000000000F8}, EndKey:{748000FFFFFFFFFFFFFB00000000000000F8}"] [old-version=46] [new-version=47]
   > [2024/07/24 12:12:22.187 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(89)] [region_id=10] [store_id=Some(1)]
   > [2024/07/24 12:12:22.187 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=10] [origin="id:94 start_key:\"7480000000000000FF5A00000000000000F8\" end_key:\"7480000000000000FF5B00000000000000F8\" region_epoch:<conf_ver:1 version:47 > peers:<id:95 store_id:1 >"] [total=1]
   > [2024/07/24 12:12:22.187 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 10 start_key: 7480000000000000FF5B00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 47 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 12:12:22.187 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 10 start_key: 7480000000000000FF5B00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 47 } peers { id: 11 store_id: 1 } }"]
   > [2024/07/24 12:12:22.187 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 10 start_key: 7480000000000000FF5B00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 47 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 12:12:22.187 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {95} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=95] [region_id=94]
   > [2024/07/24 12:12:22.187 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=95] [region_id=94]
   > [2024/07/24 12:12:22.187 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {95} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=95] [region_id=94]
   > [2024/07/24 12:12:22.187 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 95."] [id=95] [raft_id=95] [region_id=94]
   > [2024/07/24 12:12:22.188 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=95] [region_id=94]
   > [2024/07/24 12:12:22.188 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=95] [region_id=94]
   > [2024/07/24 12:12:22.188 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=95] [region_id=94]
   > [2024/07/24 12:12:22.188 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=95] [region_id=94]
   > [2024/07/24 12:12:22.188 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803870] [region_id=94]
   > [2024/07/24 12:12:22.188 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=76] [observe_id=ObserveId(91)] [region=10]
   > [2024/07/24 12:12:22.188 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=94]
   > [2024/07/24 12:12:22.193 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 94 start_key: 7480000000000000FF5A00000000000000F8 end_key: 7480000000000000FF5B00000000000000F8 region_epoch { conf_ver: 1 version: 47 } peers { id: 95 store_id: 1 }"]
   > [2024/07/24 12:12:22.194 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(92)] [region=94]
   > [2024/07/24 12:12:23.116 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/24 12:12:23.209 +00:00] [INFO] [set.go:141] ["set global var"] [conn=6993195218841371041] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/07/24 12:12:23.722 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Region error (will back off and retry) message: \"EpochNotMatch current epoch of region 10 is conf_ver: 1 version: 47, but you sent conf_ver: 1 version: 46\" epoch_not_match { current_regions { id: 10 start_key: 7480000000000000FF5B00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 47 } peers { id: 11 store_id: 1 } } current_regions { id: 94 start_key: 7480000000000000FF5A00000000000000F8 end_key: 7480000000000000FF5B00000000000000F8 region_epoch { conf_ver: 1 version: 47 } peers { id: 95 store_id: 1 } } }"]
   > [2024/07/24 12:12:23.722 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Region error (will back off and retry) message: \"EpochNotMatch current epoch of region 10 is conf_ver: 1 version: 47, but you sent conf_ver: 1 version: 46\" epoch_not_match { current_regions { id: 10 start_key: 7480000000000000FF5B00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 47 } peers { id: 11 store_id: 1 } } current_regions { id: 94 start_key: 7480000000000000FF5A00000000000000F8 end_key: 7480000000000000FF5B00000000000000F8 region_epoch { conf_ver: 1 version: 47 } peers { id: 95 store_id: 1 } } }"]
   > [2024/07/24 12:12:24.028 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
