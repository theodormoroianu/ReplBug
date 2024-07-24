# Bug ID TIDB-39972-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/39972
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              Select does not throw errors when running concurently.


## Details
 * Database: tidb-v6.4.0.tikv
 * Number of scenarios: 2
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
     - Instruction:  BEGIN;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows: 0
 * Instruction #2:
     - Instruction:  DELETE FROM t WHERE TRUE;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows: 1
 * Instruction #3:
     - Instruction:  UPDATE t SET c0=0 WHERE (CAST('a' AS SIGNED)); -- report an error
     - Transaction: conn_0
     - Output: ERROR: 1292 (22007): Truncated incorrect INTEGER value: 'a'
     - Executed order: Not executed
     - Affected rows: -1
 * Instruction #4:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows: 0

 * Container logs:
   > [2024/07/24 09:59:59.609 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/24 09:59:59.612 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=3100730542467842467] [schemaVersion=57] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/24 09:59:59.654 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:91, Type:drop schema, State:queueing, SchemaState:public, SchemaID:86, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 09:59:59.591 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 09:59:59.654 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:91, Type:drop schema, State:queueing, SchemaState:public, SchemaID:86, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 09:59:59.591 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/24 09:59:59.679 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:91, Type:drop schema, State:queueing, SchemaState:public, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:59:59.591 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:59:59.730 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=57] [neededSchemaVersion=58] ["start time"=1.433785ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 09:59:59.778 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=58] ["take time"=57.673238ms] [job="ID:91, Type:drop schema, State:running, SchemaState:write only, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:59:59.591 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:59:59.783 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:91, Type:drop schema, State:running, SchemaState:write only, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:59:59.591 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:59:59.839 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=58] [neededSchemaVersion=59] ["start time"=858.776µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 09:59:59.888 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=59] ["take time"=57.781563ms] [job="ID:91, Type:drop schema, State:running, SchemaState:delete only, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:59:59.591 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:59:59.893 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:91, Type:drop schema, State:running, SchemaState:delete only, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:59:59.591 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:59:59.942 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=59] [neededSchemaVersion=60] ["start time"=826.091µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 09:59:59.991 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=60] ["take time"=58.3836ms] [job="ID:91, Type:drop schema, State:done, SchemaState:none, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:59:59.591 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 09:59:59.999 +00:00] [INFO] [delete_range.go:109] ["[ddl] add job into delete-range table"] [jobID=91] [jobType="drop schema"]
   > [2024/07/24 10:00:00.003 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:91, Type:drop schema, State:synced, SchemaState:none, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 09:59:59.591 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 10:00:00.031 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=91]
   > [2024/07/24 10:00:00.031 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 10:00:00.032 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000005BFF0000000000000000F7 lock_version: 451363523786440706 key: 748000FFFFFFFFFFFE5F72800000000000005B lock_ttl: 3009 txn_size: 1 lock_type: Del min_commit_ts: 451363523786440707"]
   > [2024/07/24 10:00:00.032 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000005BFF0000000000000000F7 lock_version: 451363523786440706 key: 748000FFFFFFFFFFFE5F72800000000000005B lock_ttl: 3009 txn_size: 1 lock_type: Del min_commit_ts: 451363523786440707"]
   > [2024/07/24 10:00:00.034 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=3100730542467842467] [schemaVersion=60] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/24 10:00:00.037 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000005BFF0000000000000000F7 lock_version: 451363523786440706 key: 748000FFFFFFFFFFFE5F72800000000000005B lock_ttl: 3009 txn_size: 1 lock_type: Del min_commit_ts: 451363523786440707"]
   > [2024/07/24 10:00:00.037 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000005BFF0000000000000000F7 lock_version: 451363523786440706 key: 748000FFFFFFFFFFFE5F72800000000000005B lock_ttl: 3009 txn_size: 1 lock_type: Del min_commit_ts: 451363523786440707"]
   > [2024/07/24 10:00:00.092 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:93, Type:create schema, State:queueing, SchemaState:none, SchemaID:92, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 10:00:00.041 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 10:00:00.092 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:93, Type:create schema, State:queueing, SchemaState:none, SchemaID:92, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 10:00:00.041 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/24 10:00:00.116 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:93, Type:create schema, State:queueing, SchemaState:none, SchemaID:92, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 10:00:00.041 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 10:00:00.171 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=60] [neededSchemaVersion=61] ["start time"=1.485677ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 10:00:00.219 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=61] ["take time"=58.013788ms] [job="ID:93, Type:create schema, State:done, SchemaState:public, SchemaID:92, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 10:00:00.041 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 10:00:00.225 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:93, Type:create schema, State:synced, SchemaState:public, SchemaID:92, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 10:00:00.041 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 10:00:00.249 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=93]
   > [2024/07/24 10:00:00.249 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 10:00:00.250 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000005DFF0000000000000000F7 lock_version: 451363523838869506 key: 748000FFFFFFFFFFFE5F72800000000000005D lock_ttl: 3003 txn_size: 1 lock_type: Del min_commit_ts: 451363523838869507"]
   > [2024/07/24 10:00:00.250 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000005DFF0000000000000000F7 lock_version: 451363523838869506 key: 748000FFFFFFFFFFFE5F72800000000000005D lock_ttl: 3003 txn_size: 1 lock_type: Del min_commit_ts: 451363523838869507"]
   > [2024/07/24 10:00:00.253 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=3100730542467842467] [schemaVersion=61] [cur_db=testdb] [sql="CREATE TABLE t(c0 INT);"] [user=root@%]
   > [2024/07/24 10:00:00.255 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000005DFF0000000000000000F7 lock_version: 451363523838869506 key: 748000FFFFFFFFFFFE5F72800000000000005D lock_ttl: 3003 txn_size: 1 lock_type: Del min_commit_ts: 451363523838869507"]
   > [2024/07/24 10:00:00.256 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000005DFF0000000000000000F7 lock_version: 451363523838869506 key: 748000FFFFFFFFFFFE5F72800000000000005D lock_ttl: 3003 txn_size: 1 lock_type: Del min_commit_ts: 451363523838869507"]
   > [2024/07/24 10:00:00.312 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:95, Type:create table, State:queueing, SchemaState:none, SchemaID:92, TableID:94, RowCount:0, ArgLen:2, start time: 2024-07-24 10:00:00.241 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 10:00:00.312 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:95, Type:create table, State:queueing, SchemaState:none, SchemaID:92, TableID:94, RowCount:0, ArgLen:2, start time: 2024-07-24 10:00:00.241 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE t(c0 INT);"]
   > [2024/07/24 10:00:00.334 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:95, Type:create table, State:queueing, SchemaState:none, SchemaID:92, TableID:94, RowCount:0, ArgLen:0, start time: 2024-07-24 10:00:00.241 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 10:00:00.391 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=61] [neededSchemaVersion=62] ["start time"=2.088204ms] [phyTblIDs="[94]"] [actionTypes="[8]"]
   > [2024/07/24 10:00:00.439 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=62] ["take time"=60.982768ms] [job="ID:95, Type:create table, State:done, SchemaState:public, SchemaID:92, TableID:94, RowCount:0, ArgLen:2, start time: 2024-07-24 10:00:00.241 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 10:00:00.445 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:95, Type:create table, State:synced, SchemaState:public, SchemaID:92, TableID:94, RowCount:0, ArgLen:0, start time: 2024-07-24 10:00:00.241 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 10:00:00.475 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=95]
   > [2024/07/24 10:00:00.476 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 10:00:00.476 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=10] ["first split key"=74800000000000005e]
   > [2024/07/24 10:00:00.477 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000005FFF0000000000000000F7 lock_version: 451363523904405505 key: 748000FFFFFFFFFFFE5F72800000000000005F lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451363523904405506"]
   > [2024/07/24 10:00:00.477 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000005FFF0000000000000000F7 lock_version: 451363523904405505 key: 748000FFFFFFFFFFFE5F72800000000000005F lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451363523904405506"]
   > [2024/07/24 10:00:00.483 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000005FFF0000000000000000F7 lock_version: 451363523904405505 key: 748000FFFFFFFFFFFE5F72800000000000005F lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451363523904405506"]
   > [2024/07/24 10:00:00.483 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000005FFF0000000000000000F7 lock_version: 451363523904405505 key: 748000FFFFFFFFFFFE5F72800000000000005F lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451363523904405506"]
   > [2024/07/24 10:00:00.483 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:54900] [split_keys="key 7480000000000000FF5E00000000000000F8"] [peer_id=11] [region_id=10]
   > [2024/07/24 10:00:00.483 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=86] [peer-ids="[87]"]
   > [2024/07/24 10:00:00.484 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 10 start_key: 7480000000000000FF5800000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 42 } peers { id: 11 store_id: 1 }"] [new_region_ids="[new_region_id: 86 new_peer_ids: 87]"] [region_id=10]
   > [2024/07/24 10:00:00.499 +00:00] [WARN] [2pc.go:1873] ["schemaLeaseChecker is not set for this transaction"] [sessionID=3100730542467842467] [startTS=451363523904405512] [checkTS=451363523917512705]
   > [2024/07/24 10:00:00.503 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF5E00000000000000F8 new_region_id: 86 new_peer_ids: 87 } right_derive: true }"] [index=76] [term=6] [peer_id=11] [region_id=10]
   > [2024/07/24 10:00:00.504 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF5E00000000000000F8"] [region="id: 10 start_key: 7480000000000000FF5800000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 42 } peers { id: 11 store_id: 1 }"] [peer_id=11] [region_id=10]
   > [2024/07/24 10:00:00.514 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/24 10:00:00.514 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=10]
   > [2024/07/24 10:00:00.514 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=11] [region_id=10]
   > [2024/07/24 10:00:00.514 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(81)] [region_id=10] [store_id=Some(1)]
   > [2024/07/24 10:00:00.514 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 86 start_key: 7480000000000000FF5800000000000000F8 end_key: 7480000000000000FF5E00000000000000F8 region_epoch { conf_ver: 1 version: 43 } peers { id: 87 store_id: 1 }"] [region_id=86]
   > [2024/07/24 10:00:00.514 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=10] ["first at"=74800000000000005e] ["first new region left"="{Id:86 StartKey:7480000000000000ff5800000000000000f8 EndKey:7480000000000000ff5e00000000000000f8 RegionEpoch:{ConfVer:1 Version:43} Peers:[id:87 store_id:1 ] EncryptionMeta:<nil> IsInFlashback:false}"] ["new region count"=1]
   > [2024/07/24 10:00:00.514 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[86]"]
   > [2024/07/24 10:00:00.514 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=87] [region_id=86]
   > [2024/07/24 10:00:00.514 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 10 start_key: 7480000000000000FF5E00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 43 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 10:00:00.514 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {87} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=87] [region_id=86]
   > [2024/07/24 10:00:00.515 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=87] [region_id=86]
   > [2024/07/24 10:00:00.515 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=10] [detail="StartKey Changed:{7480000000000000FF5800000000000000F8} -> {7480000000000000FF5E00000000000000F8}, EndKey:{748000FFFFFFFFFFFFFB00000000000000F8}"] [old-version=42] [new-version=43]
   > [2024/07/24 10:00:00.515 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 10 start_key: 7480000000000000FF5E00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 43 } peers { id: 11 store_id: 1 } }"]
   > [2024/07/24 10:00:00.515 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=10] [origin="id:86 start_key:\"7480000000000000FF5800000000000000F8\" end_key:\"7480000000000000FF5E00000000000000F8\" region_epoch:<conf_ver:1 version:43 > peers:<id:87 store_id:1 >"] [total=1]
   > [2024/07/24 10:00:00.515 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {87} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=87] [region_id=86]
   > [2024/07/24 10:00:00.515 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 87."] [id=87] [raft_id=87] [region_id=86]
   > [2024/07/24 10:00:00.515 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 10 start_key: 7480000000000000FF5E00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 43 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 10:00:00.515 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=87] [region_id=86]
   > [2024/07/24 10:00:00.515 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=87] [region_id=86]
   > [2024/07/24 10:00:00.515 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=87] [region_id=86]
   > [2024/07/24 10:00:00.515 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=87] [region_id=86]
   > [2024/07/24 10:00:00.516 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803862] [region_id=86]
   > [2024/07/24 10:00:00.516 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=76] [observe_id=ObserveId(83)] [region=10]
   > [2024/07/24 10:00:00.516 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=86]
   > [2024/07/24 10:00:00.516 +00:00] [INFO] [scheduler.rs:640] ["get snapshot failed"] [err="Error(Request(message: \"EpochNotMatch current epoch of region 10 is conf_ver: 1 version: 43, but you sent conf_ver: 1 version: 42\" epoch_not_match { current_regions { id: 10 start_key: 7480000000000000FF5E00000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 43 } peers { id: 11 store_id: 1 } } current_regions { id: 86 start_key: 7480000000000000FF5800000000000000F8 end_key: 7480000000000000FF5E00000000000000F8 region_epoch { conf_ver: 1 version: 43 } peers { id: 87 store_id: 1 } } }))"] [cid=1427]
   > [2024/07/24 10:00:00.520 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 86 start_key: 7480000000000000FF5800000000000000F8 end_key: 7480000000000000FF5E00000000000000F8 region_epoch { conf_ver: 1 version: 43 } peers { id: 87 store_id: 1 }"]
   > [2024/07/24 10:00:00.521 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(84)] [region=86]
   > [2024/07/24 10:00:01.540 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/24 10:00:01.640 +00:00] [INFO] [set.go:141] ["set global var"] [conn=3100730542467842469] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/07/24 10:00:02.444 +00:00] [WARN] [session.go:2191] ["run statement failed"] [conn=3100730542467842469] [schemaVersion=62] [error="[tikv:1292]Truncated incorrect INTEGER value: 'a'"] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 3100730542467842469,\n  \"status\": 3,\n  \"strictMode\": true,\n  \"txn\": \"451363524258299905\",\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"10.88.0.52\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/07/24 10:00:02.444 +00:00] [INFO] [conn.go:1152] ["command dispatched failed"] [conn=3100730542467842469] [connInfo="id:3100730542467842469, addr:10.88.0.52:34360 status:11, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:1, autocommit:1"] [sql=" UPDATE t SET c0=0 WHERE (CAST('a' AS SIGNED)); -- report an error"] [txn_mode=PESSIMISTIC] [timestamp=451363524258299905] [err="[tikv:1292]Truncated incorrect INTEGER value: 'a'"]

### Scenario 1
 * Instruction #0:
     - Instruction:  DELETE FROM t WHERE TRUE;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows: 1
 * Instruction #1:
     - Instruction:  UPDATE t SET c0=0 WHERE (CAST('a' AS SIGNED)); -- report an error
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows: 0

 * Container logs:
   > [2024/07/24 10:00:06.042 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
   > [2024/07/24 10:00:06.045 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=3100730542467842473] [schemaVersion=70] [cur_db=] [sql="drop database if exists testdb;"] [user=root@%]
   > [2024/07/24 10:00:06.079 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:102, Type:drop schema, State:queueing, SchemaState:public, SchemaID:97, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 10:00:06.041 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 10:00:06.079 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:102, Type:drop schema, State:queueing, SchemaState:public, SchemaID:97, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 10:00:06.041 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/24 10:00:06.104 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:102, Type:drop schema, State:queueing, SchemaState:public, SchemaID:97, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 10:00:06.041 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 10:00:06.163 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=70] [neededSchemaVersion=71] ["start time"=802.903µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 10:00:06.212 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=71] ["take time"=68.497831ms] [job="ID:102, Type:drop schema, State:running, SchemaState:write only, SchemaID:97, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 10:00:06.041 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 10:00:06.218 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:102, Type:drop schema, State:running, SchemaState:write only, SchemaID:97, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 10:00:06.041 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 10:00:06.277 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=71] [neededSchemaVersion=72] ["start time"=609.022µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 10:00:06.326 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=72] ["take time"=67.097988ms] [job="ID:102, Type:drop schema, State:running, SchemaState:delete only, SchemaID:97, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 10:00:06.041 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 10:00:06.332 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:102, Type:drop schema, State:running, SchemaState:delete only, SchemaID:97, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 10:00:06.041 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 10:00:06.365 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D4442730000000000FA000000000000006844423A3937000000FC lock_version: 451363525437947906 key: 748000FFFFFFFFFFFE5F728000000000000066 lock_ttl: 3023 txn_size: 1 min_commit_ts: 451363525437947907"]
   > [2024/07/24 10:00:06.397 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=72] [neededSchemaVersion=73] ["start time"=697.302µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 10:00:06.445 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=73] ["take time"=61.297755ms] [job="ID:102, Type:drop schema, State:done, SchemaState:none, SchemaID:97, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 10:00:06.041 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 10:00:06.450 +00:00] [INFO] [delete_range.go:109] ["[ddl] add job into delete-range table"] [jobID=102] [jobType="drop schema"]
   > [2024/07/24 10:00:06.451 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:102, Type:drop schema, State:synced, SchemaState:none, SchemaID:97, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 10:00:06.041 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 10:00:06.498 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=102]
   > [2024/07/24 10:00:06.498 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 10:00:06.499 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000066FF0000000000000000F7 lock_version: 451363525477269506 key: 748000FFFFFFFFFFFE5F728000000000000066 lock_ttl: 3003 txn_size: 1 lock_type: Del min_commit_ts: 451363525477269507"]
   > [2024/07/24 10:00:06.500 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000066FF0000000000000000F7 lock_version: 451363525477269506 key: 748000FFFFFFFFFFFE5F728000000000000066 lock_ttl: 3003 txn_size: 1 lock_type: Del min_commit_ts: 451363525477269507"]
   > [2024/07/24 10:00:06.501 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=3100730542467842473] [schemaVersion=73] [cur_db=] [sql="create database testdb;"] [user=root@%]
   > [2024/07/24 10:00:06.503 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000066FF0000000000000000F7 lock_version: 451363525477269506 key: 748000FFFFFFFFFFFE5F728000000000000066 lock_ttl: 3003 txn_size: 1 lock_type: Del min_commit_ts: 451363525477269507"]
   > [2024/07/24 10:00:06.503 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000066FF0000000000000000F7 lock_version: 451363525477269506 key: 748000FFFFFFFFFFFE5F728000000000000066 lock_ttl: 3003 txn_size: 1 lock_type: Del min_commit_ts: 451363525477269507"]
   > [2024/07/24 10:00:06.559 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:104, Type:create schema, State:queueing, SchemaState:none, SchemaID:103, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 10:00:06.491 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 10:00:06.559 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:104, Type:create schema, State:queueing, SchemaState:none, SchemaID:103, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 10:00:06.491 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/24 10:00:06.583 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:104, Type:create schema, State:queueing, SchemaState:none, SchemaID:103, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 10:00:06.491 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 10:00:06.634 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=73] [neededSchemaVersion=74] ["start time"=1.361778ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 10:00:06.682 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=74] ["take time"=58.247338ms] [job="ID:104, Type:create schema, State:done, SchemaState:public, SchemaID:103, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 10:00:06.491 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 10:00:06.688 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:104, Type:create schema, State:synced, SchemaState:public, SchemaID:103, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 10:00:06.491 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 10:00:06.717 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=104]
   > [2024/07/24 10:00:06.717 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 10:00:06.718 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000068FF0000000000000000F7 lock_version: 451363525529698306 key: 748000FFFFFFFFFFFE5F728000000000000068 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451363525529698307"]
   > [2024/07/24 10:00:06.718 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000068FF0000000000000000F7 lock_version: 451363525529698306 key: 748000FFFFFFFFFFFE5F728000000000000068 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451363525529698307"]
   > [2024/07/24 10:00:06.721 +00:00] [INFO] [session.go:3313] ["CRUCIAL OPERATION"] [conn=3100730542467842473] [schemaVersion=74] [cur_db=testdb] [sql="CREATE TABLE t(c0 INT);"] [user=root@%]
   > [2024/07/24 10:00:06.724 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000068FF0000000000000000F7 lock_version: 451363525529698306 key: 748000FFFFFFFFFFFE5F728000000000000068 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451363525529698307"]
   > [2024/07/24 10:00:06.724 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC00000000000000680000000000000068FF0000000000000000F7 lock_version: 451363525529698306 key: 748000FFFFFFFFFFFE5F728000000000000068 lock_ttl: 3004 txn_size: 1 lock_type: Del min_commit_ts: 451363525529698307"]
   > [2024/07/24 10:00:06.781 +00:00] [INFO] [ddl_worker.go:314] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:106, Type:create table, State:queueing, SchemaState:none, SchemaID:103, TableID:105, RowCount:0, ArgLen:2, start time: 2024-07-24 10:00:06.741 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "] [table=true]
   > [2024/07/24 10:00:06.781 +00:00] [INFO] [ddl.go:1012] ["[ddl] start DDL job"] [job="ID:106, Type:create table, State:queueing, SchemaState:none, SchemaID:103, TableID:105, RowCount:0, ArgLen:2, start time: 2024-07-24 10:00:06.741 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE t(c0 INT);"]
   > [2024/07/24 10:00:06.807 +00:00] [INFO] [ddl_worker.go:1157] ["[ddl] run DDL job"] [worker="worker 10, tp general"] [job="ID:106, Type:create table, State:queueing, SchemaState:none, SchemaID:103, TableID:105, RowCount:0, ArgLen:0, start time: 2024-07-24 10:00:06.741 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 10:00:06.875 +00:00] [INFO] [domain.go:188] ["diff load InfoSchema success"] [currentSchemaVersion=74] [neededSchemaVersion=75] ["start time"=2.308835ms] [phyTblIDs="[105]"] [actionTypes="[8]"]
   > [2024/07/24 10:00:06.932 +00:00] [INFO] [ddl_worker.go:1362] ["[ddl] wait latest schema version changed(get the metadata lock if tidb_enable_metadata_lock is true)"] [ver=75] ["take time"=67.843691ms] [job="ID:106, Type:create table, State:done, SchemaState:public, SchemaID:103, TableID:105, RowCount:0, ArgLen:2, start time: 2024-07-24 10:00:06.741 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 10:00:06.938 +00:00] [INFO] [ddl_worker.go:632] ["[ddl] finish DDL job"] [worker="worker 10, tp general"] [job="ID:106, Type:create table, State:synced, SchemaState:public, SchemaID:103, TableID:105, RowCount:0, ArgLen:0, start time: 2024-07-24 10:00:06.741 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 10:00:06.963 +00:00] [INFO] [ddl.go:1105] ["[ddl] DDL job is finished"] [jobID=106]
   > [2024/07/24 10:00:06.964 +00:00] [INFO] [callback.go:121] ["performing DDL change, must reload"]
   > [2024/07/24 10:00:06.964 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=10] ["first split key"=748000000000000069]
   > [2024/07/24 10:00:06.965 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000006AFF0000000000000000F7 lock_version: 451363525595234306 key: 748000FFFFFFFFFFFE5F72800000000000006A lock_ttl: 3003 txn_size: 1 lock_type: Del min_commit_ts: 451363525595234307"]
   > [2024/07/24 10:00:06.965 +00:00] [WARN] [endpoint.rs:658] [error-response] [err="Key is locked (will clean up) primary_lock: 6D44444C4A6F624869FF73746F7279000000FC0000000000000068000000000000006AFF0000000000000000F7 lock_version: 451363525595234306 key: 748000FFFFFFFFFFFE5F72800000000000006A lock_ttl: 3003 txn_size: 1 lock_type: Del min_commit_ts: 451363525595234307"]
   > [2024/07/24 10:00:06.968 +00:00] [INFO] [peer.rs:5483] ["on split"] [source=ipv4:127.0.0.1:54902] [split_keys="key 7480000000000000FF6900000000000000F8"] [peer_id=11] [region_id=10]
   > [2024/07/24 10:00:06.969 +00:00] [INFO] [cluster_worker.go:145] ["alloc ids for region split"] [region-id=90] [peer-ids="[91]"]
   > [2024/07/24 10:00:06.969 +00:00] [INFO] [pd.rs:1082] ["try to batch split region"] [task=batch_split] [region="id: 10 start_key: 7480000000000000FF6300000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 44 } peers { id: 11 store_id: 1 }"] [new_region_ids="[new_region_id: 90 new_peer_ids: 91]"] [region_id=10]
   > [2024/07/24 10:00:06.980 +00:00] [INFO] [apply.rs:1562] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF6900000000000000F8 new_region_id: 90 new_peer_ids: 91 } right_derive: true }"] [index=81] [term=6] [peer_id=11] [region_id=10]
   > [2024/07/24 10:00:06.981 +00:00] [INFO] [apply.rs:2415] ["split region"] [keys="key 7480000000000000FF6900000000000000F8"] [region="id: 10 start_key: 7480000000000000FF6300000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 44 } peers { id: 11 store_id: 1 }"] [peer_id=11] [region_id=10]
   > [2024/07/24 10:00:06.991 +00:00] [INFO] [endpoint.rs:172] ["region met split/merge command, stop tracking since key range changed, wait for re-register"] [req_type=BatchSplit]
   > [2024/07/24 10:00:06.991 +00:00] [INFO] [peer.rs:3840] ["moving 0 locks to new regions"] [region_id=10]
   > [2024/07/24 10:00:06.991 +00:00] [INFO] [endpoint.rs:410] ["deregister observe region"] [observe_id=ObserveId(85)] [region_id=10] [store_id=Some(1)]
   > [2024/07/24 10:00:06.991 +00:00] [INFO] [peer.rs:3870] ["notify pd with split"] [split_count=2] [peer_id=11] [region_id=10]
   > [2024/07/24 10:00:06.992 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 10 start_key: 7480000000000000FF6900000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 45 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 10:00:06.992 +00:00] [INFO] [peer.rs:3935] ["insert new region"] [region="id: 90 start_key: 7480000000000000FF6300000000000000F8 end_key: 7480000000000000FF6900000000000000F8 region_epoch { conf_ver: 1 version: 45 } peers { id: 91 store_id: 1 }"] [region_id=90]
   > [2024/07/24 10:00:06.992 +00:00] [INFO] [peer.rs:262] ["create peer"] [peer_id=91] [region_id=90]
   > [2024/07/24 10:00:06.992 +00:00] [INFO] [subscription_manager.rs:395] ["backup stream: on_modify_observe"] [op="RefreshResolver { region: id: 10 start_key: 7480000000000000FF6900000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 45 } peers { id: 11 store_id: 1 } }"]
   > [2024/07/24 10:00:06.992 +00:00] [INFO] [region.go:617] ["region Version changed"] [region-id=10] [detail="StartKey Changed:{7480000000000000FF6300000000000000F8} -> {7480000000000000FF6900000000000000F8}, EndKey:{748000FFFFFFFFFFFFFB00000000000000F8}"] [old-version=44] [new-version=45]
   > [2024/07/24 10:00:06.992 +00:00] [INFO] [split_region.go:187] ["batch split regions complete"] ["batch region ID"=10] ["first at"=748000000000000069] ["first new region left"="{Id:90 StartKey:7480000000000000ff6300000000000000f8 EndKey:7480000000000000ff6900000000000000f8 RegionEpoch:{ConfVer:1 Version:45} Peers:[id:91 store_id:1 ] EncryptionMeta:<nil> IsInFlashback:false}"] ["new region count"=1]
   > [2024/07/24 10:00:06.992 +00:00] [WARN] [subscription_track.rs:159] ["backup stream observer refreshing void subscription."] [new_region="id: 10 start_key: 7480000000000000FF6900000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 45 } peers { id: 11 store_id: 1 }"]
   > [2024/07/24 10:00:06.992 +00:00] [INFO] [split_region.go:236] ["split regions complete"] ["region count"=1] ["region IDs"="[90]"]
   > [2024/07/24 10:00:06.992 +00:00] [INFO] [cluster_worker.go:237] ["region batch split, generate new regions"] [region-id=10] [origin="id:90 start_key:\"7480000000000000FF6300000000000000F8\" end_key:\"7480000000000000FF6900000000000000F8\" region_epoch:<conf_ver:1 version:45 > peers:<id:91 store_id:1 >"] [total=1]
   > [2024/07/24 10:00:06.992 +00:00] [INFO] [raft.rs:2646] ["switched to configuration"] [config="Configuration { voters: Configuration { incoming: Configuration { voters: {91} }, outgoing: Configuration { voters: {} } }, learners: {}, learners_next: {}, auto_leave: false }"] [raft_id=91] [region_id=90]
   > [2024/07/24 10:00:06.992 +00:00] [INFO] [raft.rs:1120] ["became follower at term 5"] [term=5] [raft_id=91] [region_id=90]
   > [2024/07/24 10:00:06.992 +00:00] [INFO] [raft.rs:384] [newRaft] [peers="Configuration { incoming: Configuration { voters: {91} }, outgoing: Configuration { voters: {} } }"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=91] [region_id=90]
   > [2024/07/24 10:00:06.992 +00:00] [WARN] [2pc.go:1873] ["schemaLeaseChecker is not set for this transaction"] [sessionID=3100730542467842473] [startTS=451363525608341510] [checkTS=451363525621448706]
   > [2024/07/24 10:00:06.992 +00:00] [INFO] [raw_node.rs:315] ["RawNode created with id 91."] [id=91] [raft_id=91] [region_id=90]
   > [2024/07/24 10:00:06.992 +00:00] [INFO] [raft.rs:1550] ["starting a new election"] [term=5] [raft_id=91] [region_id=90]
   > [2024/07/24 10:00:06.992 +00:00] [INFO] [raft.rs:1170] ["became pre-candidate at term 5"] [term=5] [raft_id=91] [region_id=90]
   > [2024/07/24 10:00:06.993 +00:00] [INFO] [raft.rs:1144] ["became candidate at term 6"] [term=6] [raft_id=91] [region_id=90]
   > [2024/07/24 10:00:06.993 +00:00] [INFO] [raft.rs:1228] ["became leader at term 6"] [term=6] [raft_id=91] [region_id=90]
   > [2024/07/24 10:00:06.993 +00:00] [INFO] [peer.rs:5357] ["require updating max ts"] [initial_status=25769803866] [region_id=90]
   > [2024/07/24 10:00:06.993 +00:00] [INFO] [pd.rs:1701] ["succeed to update max timestamp"] [region_id=90]
   > [2024/07/24 10:00:06.998 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=81] [observe_id=ObserveId(87)] [region=10]
   > [2024/07/24 10:00:06.998 +00:00] [INFO] [endpoint.rs:336] ["register observe region"] [region="id: 90 start_key: 7480000000000000FF6300000000000000F8 end_key: 7480000000000000FF6900000000000000F8 region_epoch { conf_ver: 1 version: 45 } peers { id: 91 store_id: 1 }"]
   > [2024/07/24 10:00:06.998 +00:00] [INFO] [endpoint.rs:253] ["Resolver initialized"] [pending_data_index=0] [snapshot_index=6] [observe_id=ObserveId(88)] [region=90]
   > [2024/07/24 10:00:07.005 +00:00] [INFO] [scheduler.rs:640] ["get snapshot failed"] [err="Error(Request(message: \"EpochNotMatch current epoch of region 10 is conf_ver: 1 version: 45, but you sent conf_ver: 1 version: 44\" epoch_not_match { current_regions { id: 10 start_key: 7480000000000000FF6900000000000000F8 end_key: 748000FFFFFFFFFFFFFB00000000000000F8 region_epoch { conf_ver: 1 version: 45 } peers { id: 11 store_id: 1 } } current_regions { id: 90 start_key: 7480000000000000FF6300000000000000F8 end_key: 7480000000000000FF6900000000000000F8 region_epoch { conf_ver: 1 version: 45 } peers { id: 91 store_id: 1 } } }))"] [cid=1667]
   > [2024/07/24 10:00:08.026 +00:00] [WARN] [collate.go:221] ["The collation utf8mb4_0900_ai_ci specified on connection is not supported when new collation is enabled, switch to the default collation: utf8mb4_bin"]
