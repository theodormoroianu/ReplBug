# Bug ID TIDB-20773-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/20773
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              The update should block, but it doesn't.


## Details
 * Database: tidb-v4.0.8.tikv
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
     - Instruction:  begin;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  insert into t values (6, '0004');
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 1 / 0
 * Instruction #3:
     - Instruction:  insert into t values (7, null);
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 1 / 0
 * Instruction #4:
     - Instruction:  alter table t add c_str_new varchar(20);
     - Transaction: conn_1
     - Output: None
     - Executed order: 5
     - Affected rows / Warnings: 0 / 0
 * Instruction #5:
     - Instruction:  update t set c_str = '0005' where id = 1;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows / Warnings: 1 / 0
 * Instruction #6:
     - Instruction:  update t set c_str = null where id = 2;
     - Transaction: conn_0
     - Output: None
     - Executed order: 6
     - Affected rows / Warnings: 1 / 0
 * Instruction #7:
     - Instruction:  update t set c_str = '0006' where id = 3;
     - Transaction: conn_0
     - Output: None
     - Executed order: 7
     - Affected rows / Warnings: 1 / 0
 * Instruction #8:
     - Instruction:  delete from t where id = 4;
     - Transaction: conn_0
     - Output: None
     - Executed order: 8
     - Affected rows / Warnings: 1 / 0
 * Instruction #9:
     - Instruction:  delete from t where id = 5;
     - Transaction: conn_0
     - Output: None
     - Executed order: 9
     - Affected rows / Warnings: 1 / 0
 * Instruction #10:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: ERROR: 8028 (HY000): Information schema is changed during the execution of the statement(for example, table definition may be updated by other DDL ran in parallel). If you see this error often, try increasing `tidb_max_delta_schema_count`. [try again later]
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0

 * Container logs:
   > [2024/07/17 13:10:42.426 +00:00] [INFO] [session.go:2161] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=22] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.199]
   > [2024/07/17 13:10:42.428 +00:00] [INFO] [session.go:2161] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=22] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.199]
   > [2024/07/17 13:10:42.454 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-17 13:10:42.44 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/17 13:10:42.455 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-17 13:10:42.44 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/17 13:10:42.458 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-17 13:10:42.44 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 13:10:42.475 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=22] [neededSchemaVersion=23] ["start time"=1.198419ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/17 13:10:42.525 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=23] ["take time"=52.653186ms] [job="ID:46, Type:create schema, State:done, SchemaState:public, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-17 13:10:42.44 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 13:10:42.528 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:46, Type:create schema, State:synced, SchemaState:public, SchemaID:45, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-17 13:10:42.44 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 13:10:42.542 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=46]
   > [2024/07/17 13:10:42.542 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/07/17 13:10:42.545 +00:00] [INFO] [session.go:2161] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=23] [cur_db=testdb] [sql="create table t (id int primary key, c_str varchar(20));"] [user=root@10.88.0.199]
   > [2024/07/17 13:10:42.569 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-07-17 13:10:42.539 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/17 13:10:42.569 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-07-17 13:10:42.539 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t (id int primary key, c_str varchar(20));"]
   > [2024/07/17 13:10:42.573 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-17 13:10:42.539 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 13:10:42.594 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=23] [neededSchemaVersion=24] ["start time"=1.904242ms] [phyTblIDs="[47]"] [actionTypes="[8]"]
   > [2024/07/17 13:10:42.642 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=24] ["take time"=52.140965ms] [job="ID:48, Type:create table, State:done, SchemaState:public, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-07-17 13:10:42.539 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 13:10:42.646 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:48, Type:create table, State:synced, SchemaState:public, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-17 13:10:42.539 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 13:10:42.659 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=48]
   > [2024/07/17 13:10:42.661 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/07/17 13:10:42.661 +00:00] [INFO] [split_region.go:60] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=2] ["first split key"=74800000000000002f]
   > [2024/07/17 13:10:42.662 +00:00] [INFO] [peer.rs:469] ["on split"] [split_keys="key 7480000000000000FF2F00000000000000F8"] [peer_id=3] [region_id=2]
   > [2024/07/17 13:10:42.662 +00:00] [INFO] [cluster_worker.go:125] ["alloc ids for region split"] [region-id=44] [peer-ids="[45]"]
   > [2024/07/17 13:10:42.663 +00:00] [INFO] [pd.rs:507] ["try to batch split region"] [task=batch_split] [region="id: 2 start_key: 7480000000000000FF2B00000000000000F8 region_epoch { conf_ver: 1 version: 21 } peers { id: 3 store_id: 1 }"] [new_region_ids="[new_region_id: 44 new_peer_ids: 45]"] [region_id=2]
   > [2024/07/17 13:10:42.667 +00:00] [INFO] [apply.rs:1172] ["execute admin command"] [command="cmd_type: BatchSplit splits { requests { split_key: 7480000000000000FF2F00000000000000F8 new_region_id: 44 new_peer_ids: 45 } right_derive: true }"] [index=55] [term=6] [peer_id=3] [region_id=2]
   > [2024/07/17 13:10:42.667 +00:00] [INFO] [apply.rs:1752] ["split region"] [keys="key 7480000000000000FF2F00000000000000F8"] [region="id: 2 start_key: 7480000000000000FF2B00000000000000F8 region_epoch { conf_ver: 1 version: 21 } peers { id: 3 store_id: 1 }"] [peer_id=3] [region_id=2]
   > [2024/07/17 13:10:42.674 +00:00] [INFO] [peer.rs:1758] ["notify pd with split"] [split_count=2] [peer_id=3] [region_id=2]
   > [2024/07/17 13:10:42.674 +00:00] [INFO] [peer.rs:1800] ["insert new region"] [region="id: 44 start_key: 7480000000000000FF2B00000000000000F8 end_key: 7480000000000000FF2F00000000000000F8 region_epoch { conf_ver: 1 version: 22 } peers { id: 45 store_id: 1 }"] [region_id=44]
   > [2024/07/17 13:10:42.674 +00:00] [INFO] [peer.rs:159] ["create peer"] [peer_id=45] [region_id=44]
   > [2024/07/17 13:10:42.674 +00:00] [INFO] [split_region.go:157] ["batch split regions complete"] ["batch region ID"=2] ["first at"=74800000000000002f] ["first new region left"="{Id:44 StartKey:7480000000000000ff2b00000000000000f8 EndKey:7480000000000000ff2f00000000000000f8 RegionEpoch:{ConfVer:1 Version:22} Peers:[id:45 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/17 13:10:42.674 +00:00] [INFO] [raft.rs:783] ["became follower at term 5"] [term=5] [raft_id=45] [region_id=44]
   > [2024/07/17 13:10:42.674 +00:00] [INFO] [split_region.go:209] ["split regions complete"] ["region count"=1] ["region IDs"="[44]"]
   > [2024/07/17 13:10:42.674 +00:00] [INFO] [cluster.go:542] ["region Version changed"] [region-id=2] [detail="StartKey Changed:{7480000000000000FF2B00000000000000F8} -> {7480000000000000FF2F00000000000000F8}, EndKey:{}"] [old-version=21] [new-version=22]
   > [2024/07/17 13:10:42.674 +00:00] [INFO] [raft.rs:285] [newRaft] [peers="[(45, Progress { matched: 5, next_idx: 6, state: Probe, paused: false, pending_snapshot: 0, pending_request_snapshot: 0, recent_active: false, ins: Inflights { start: 0, count: 0, buffer: [] } })]"] ["last term"=5] ["last index"=5] [applied=5] [commit=5] [term=5] [raft_id=45] [region_id=44]
   > [2024/07/17 13:10:42.674 +00:00] [INFO] [raw_node.rs:222] ["RawNode created with id 45."] [id=45] [raft_id=45] [region_id=44]
   > [2024/07/17 13:10:42.674 +00:00] [INFO] [cluster_worker.go:217] ["region batch split, generate new regions"] [region-id=2] [origin="id:44 start_key:\"7480000000000000FF2B00000000000000F8\" end_key:\"7480000000000000FF2F00000000000000F8\" region_epoch:<conf_ver:1 version:22 > peers:<id:45 store_id:1 >"] [total=1]
   > [2024/07/17 13:10:42.675 +00:00] [INFO] [raft.rs:1177] ["starting a new election"] [term=5] [raft_id=45] [region_id=44]
   > [2024/07/17 13:10:42.675 +00:00] [INFO] [raft.rs:833] ["became pre-candidate at term 5"] [term=5] [raft_id=45] [region_id=44]
   > [2024/07/17 13:10:42.675 +00:00] [INFO] [raft.rs:902] ["45 received message from 45"] [term=5] [msg=MsgRequestPreVote] [from=45] [id=45] [raft_id=45] [region_id=44]
   > [2024/07/17 13:10:42.675 +00:00] [INFO] [raft.rs:807] ["became candidate at term 6"] [term=6] [raft_id=45] [region_id=44]
   > [2024/07/17 13:10:42.675 +00:00] [INFO] [raft.rs:902] ["45 received message from 45"] [term=6] [msg=MsgRequestVote] [from=45] [id=45] [raft_id=45] [region_id=44]
   > [2024/07/17 13:10:42.675 +00:00] [INFO] [raft.rs:874] ["became leader at term 6"] [term=6] [raft_id=45] [region_id=44]
   > [2024/07/17 13:10:43.716 +00:00] [INFO] [set.go:216] ["set global var"] [conn=4] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/07/17 13:10:43.718 +00:00] [INFO] [set.go:216] ["set global var"] [conn=4] [name=transaction_isolation] [val=REPEATABLE-READ]
   > [2024/07/17 13:10:44.934 +00:00] [INFO] [session.go:2161] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=24] [cur_db=testdb] [sql=" alter table t add c_str_new varchar(20);"] [user=root@10.88.0.199]
   > [2024/07/17 13:10:44.956 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:49, Type:add column, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:3, start time: 2024-07-17 13:10:44.89 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/17 13:10:44.956 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:49, Type:add column, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:3, start time: 2024-07-17 13:10:44.89 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query=" alter table t add c_str_new varchar(20);"]
   > [2024/07/17 13:10:44.961 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:49, Type:add column, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-17 13:10:44.89 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 13:10:44.964 +00:00] [INFO] [column.go:184] ["[ddl] run add column job"] [job="ID:49, Type:add column, State:running, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:3, start time: 2024-07-17 13:10:44.89 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [columnInfo="{\"id\":3,\"name\":{\"O\":\"c_str_new\",\"L\":\"c_str_new\"},\"offset\":2,\"origin_default\":null,\"origin_default_bit\":null,\"default\":null,\"default_bit\":null,\"default_is_expr\":false,\"generated_expr_string\":\"\",\"generated_stored\":false,\"dependences\":null,\"type\":{\"Tp\":15,\"Flag\":0,\"Flen\":20,\"Decimal\":0,\"Charset\":\"utf8mb4\",\"Collate\":\"utf8mb4_bin\",\"Elems\":null},\"state\":0,\"comment\":\"\",\"hidden\":false,\"version\":2}"] [offset=2]
   > [2024/07/17 13:10:44.985 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=24] [neededSchemaVersion=25] ["start time"=2.006561ms] [phyTblIDs="[47]"] [actionTypes="[32]"]
   > [2024/07/17 13:10:45.033 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=25] ["take time"=52.908458ms] [job="ID:49, Type:add column, State:running, SchemaState:delete only, SchemaID:45, TableID:47, RowCount:0, ArgLen:3, start time: 2024-07-17 13:10:44.89 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 13:10:45.036 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:49, Type:add column, State:running, SchemaState:delete only, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-17 13:10:44.89 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 13:10:45.057 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=25] [neededSchemaVersion=26] ["start time"=2.38294ms] [phyTblIDs="[47]"] [actionTypes="[32]"]
   > [2024/07/17 13:10:45.106 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=26] ["take time"=53.079781ms] [job="ID:49, Type:add column, State:running, SchemaState:write only, SchemaID:45, TableID:47, RowCount:0, ArgLen:3, start time: 2024-07-17 13:10:44.89 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 13:10:45.108 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:49, Type:add column, State:running, SchemaState:write only, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-17 13:10:44.89 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 13:10:45.130 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=26] [neededSchemaVersion=27] ["start time"=2.331815ms] [phyTblIDs="[47]"] [actionTypes="[32]"]
   > [2024/07/17 13:10:45.178 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=27] ["take time"=52.810959ms] [job="ID:49, Type:add column, State:running, SchemaState:write reorganization, SchemaID:45, TableID:47, RowCount:0, ArgLen:3, start time: 2024-07-17 13:10:44.89 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 13:10:45.181 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:49, Type:add column, State:running, SchemaState:write reorganization, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-17 13:10:44.89 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 13:10:45.204 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=27] [neededSchemaVersion=28] ["start time"=2.356958ms] [phyTblIDs="[47]"] [actionTypes="[32]"]
   > [2024/07/17 13:10:45.252 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=28] ["take time"=52.826604ms] [job="ID:49, Type:add column, State:done, SchemaState:public, SchemaID:45, TableID:47, RowCount:0, ArgLen:3, start time: 2024-07-17 13:10:44.89 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 13:10:45.256 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:49, Type:add column, State:synced, SchemaState:public, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-17 13:10:44.89 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/17 13:10:45.271 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=49]
   > [2024/07/17 13:10:45.271 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/07/17 13:10:46.734 +00:00] [WARN] [session.go:472] ["can not retry txn"] [conn=4] [label=general] [error="[domain:8028]Information schema is changed during the execution of the statement(for example, table definition may be updated by other DDL ran in parallel). If you see this error often, try increasing `tidb_max_delta_schema_count`. [try again later]"] [IsBatchInsert=false] [IsPessimistic=true] [InRestrictedSQL=false] [tidb_retry_limit=10] [tidb_disable_txn_auto_retry=true]
   > [2024/07/17 13:10:46.734 +00:00] [WARN] [session.go:487] ["commit failed"] [conn=4] ["finished txn"="Txn{state=invalid}"] [error="[domain:8028]Information schema is changed during the execution of the statement(for example, table definition may be updated by other DDL ran in parallel). If you see this error often, try increasing `tidb_max_delta_schema_count`. [try again later]"]
   > [2024/07/17 13:10:46.734 +00:00] [WARN] [session.go:1066] ["run statement failed"] [conn=4] [schemaVersion=24] [error="previous statement:  delete from t where id = 5;: [domain:8028]Information schema is changed during the execution of the statement(for example, table definition may be updated by other DDL ran in parallel). If you see this error often, try increasing `tidb_max_delta_schema_count`. [try again later]"] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 4,\n  \"status\": 2,\n  \"strictMode\": true,\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"10.88.0.199\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/07/17 13:10:46.735 +00:00] [INFO] [conn.go:787] ["command dispatched failed"] [conn=4] [connInfo="id:4, addr:10.88.0.199:37078 status:10, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:0, autocommit:1"] [sql=" commit;"] [txn_mode=PESSIMISTIC] [err="[domain:8028]Information schema is changed during the execution of the statement(for example, table definition may be updated by other DDL ran in parallel). If you see this error often, try increasing `tidb_max_delta_schema_count`. [try again later]\ngithub.com/pingcap/errors.AddStack\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.20200917111840-a15ef68f753d/errors.go:174\ngithub.com/pingcap/errors.Trace\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.20200917111840-a15ef68f753d/juju_adaptor.go:15\ngithub.com/pingcap/tidb/store/tikv.(*twoPhaseCommitter).checkSchemaValid\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/store/tikv/2pc.go:1554\ngithub.com/pingcap/tidb/store/tikv.(*twoPhaseCommitter).execute\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/store/tikv/2pc.go:1377\ngithub.com/pingcap/tidb/store/tikv.(*tikvTxn).Commit\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/store/tikv/txn.go:308\ngithub.com/pingcap/tidb/session.(*TxnState).Commit\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/session/txn.go:279\ngithub.com/pingcap/tidb/session.(*session).doCommit\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/session/session.go:432\ngithub.com/pingcap/tidb/session.(*session).doCommitWithRetry\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/session/session.go:452\ngithub.com/pingcap/tidb/session.(*session).CommitTxn\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/session/session.go:510\ngithub.com/pingcap/tidb/session.autoCommitAfterStmt\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/session/tidb.go:230\ngithub.com/pingcap/tidb/session.finishStmt\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/session/tidb.go:196\ngithub.com/pingcap/tidb/session.runStmt\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/session/tidb.go:316\ngithub.com/pingcap/tidb/session.(*session).executeStatement\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/session/session.go:1063\ngithub.com/pingcap/tidb/session.(*session).execute\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/session/session.go:1175\ngithub.com/pingcap/tidb/session.(*session).Execute\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/session/session.go:1106\ngithub.com/pingcap/tidb/server.(*TiDBContext).Execute\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/server/driver_tidb.go:248\ngithub.com/pingcap/tidb/server.(*clientConn).handleQuery\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/server/conn.go:1354\ngithub.com/pingcap/tidb/server.(*clientConn).dispatch\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/server/conn.go:985\ngithub.com/pingcap/tidb/server.(*clientConn).Run\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/server/conn.go:772\ngithub.com/pingcap/tidb/server.(*Server).onConn\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/server/server.go:421\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1357\nprevious statement:  delete from t where id = 5;"]
   > [2024/07/17 13:10:46.740 +00:00] [INFO] [2pc.go:1305] ["2PC clean up done"] [conn=4] [txnStartTS=451207979070914561]
