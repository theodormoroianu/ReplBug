# Bug ID TIDB-21722-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/21722
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              execute DDL statement in transaction reports 'invalid transaction'.


## Details
 * Database: tidb-49b926ed
 * Number of scenarios: 1
 * Initial setup script: No

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows: 0
 * Instruction #1:
     - Instruction:  create table t (c_int int, c_str varchar(40));
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows: 0
 * Instruction #2:
     - Instruction:  insert into t values (1, 'quizzical hofstadter');
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows: 1
 * Instruction #3:
     - Instruction:  begin;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows: 0
 * Instruction #4:
     - Instruction:  select c_int from t where c_str is not null for update;
     - Transaction: conn_0
     - Output: [(1,)]
     - Executed order: 4
     - Affected rows: 1
 * Instruction #5:
     - Instruction:  alter table t add index idx_4 (c_str);
     - Transaction: conn_0
     - Output: ERROR: 8024 (HY000): invalid transaction
     - Executed order: Not executed
     - Affected rows: -1

 * Container logs:
   > [2024/08/07 13:02:57.649 +00:00] [INFO] [session.go:2461] ["CRUCIAL OPERATION"] [conn=2199023255563] [schemaVersion=34] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/08/07 13:02:57.649 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:59, Type:drop schema, State:none, SchemaState:none, SchemaID:54, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-07 13:02:57.649 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/07 13:02:57.649 +00:00] [INFO] [ddl.go:538] ["[ddl] start DDL job"] [job="ID:59, Type:drop schema, State:none, SchemaState:none, SchemaID:54, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-07 13:02:57.649 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/08/07 13:02:57.650 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:59, Type:drop schema, State:none, SchemaState:none, SchemaID:54, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-07 13:02:57.649 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:02:57.651 +00:00] [INFO] [domain.go:137] ["diff load InfoSchema success"] [usedSchemaVersion=34] [neededSchemaVersion=35] ["start time"=66.769µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/07 13:02:57.653 +00:00] [INFO] [ddl_worker.go:795] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=35] ["take time"=2.211126ms] [job="ID:59, Type:drop schema, State:running, SchemaState:write only, SchemaID:54, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-07 13:02:57.649 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:02:57.653 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:59, Type:drop schema, State:running, SchemaState:write only, SchemaID:54, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-07 13:02:57.649 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:02:57.654 +00:00] [INFO] [domain.go:137] ["diff load InfoSchema success"] [usedSchemaVersion=35] [neededSchemaVersion=36] ["start time"=78.572µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/07 13:02:57.656 +00:00] [INFO] [ddl_worker.go:795] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=36] ["take time"=2.354441ms] [job="ID:59, Type:drop schema, State:running, SchemaState:delete only, SchemaID:54, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-07 13:02:57.649 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:02:57.656 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:59, Type:drop schema, State:running, SchemaState:delete only, SchemaID:54, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-07 13:02:57.649 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:02:57.657 +00:00] [INFO] [domain.go:137] ["diff load InfoSchema success"] [usedSchemaVersion=36] [neededSchemaVersion=37] ["start time"=55.664µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/07 13:02:57.659 +00:00] [INFO] [ddl_worker.go:795] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=37] ["take time"=2.188567ms] [job="ID:59, Type:drop schema, State:done, SchemaState:none, SchemaID:54, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-07 13:02:57.649 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:02:57.660 +00:00] [INFO] [delete_range.go:106] ["[ddl] add job into delete-range table"] [jobID=59] [jobType="drop schema"]
   > [2024/08/07 13:02:57.660 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:59, Type:drop schema, State:synced, SchemaState:none, SchemaID:54, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-07 13:02:57.649 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:02:57.660 +00:00] [INFO] [ddl.go:593] ["[ddl] DDL job is finished"] [jobID=59]
   > [2024/08/07 13:02:57.660 +00:00] [INFO] [domain.go:660] ["performing DDL change, must reload"]
   > [2024/08/07 13:02:57.661 +00:00] [INFO] [session.go:2461] ["CRUCIAL OPERATION"] [conn=2199023255563] [schemaVersion=37] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/08/07 13:02:57.663 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:61, Type:create schema, State:none, SchemaState:none, SchemaID:60, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-07 13:02:57.662 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/07 13:02:57.663 +00:00] [INFO] [ddl.go:538] ["[ddl] start DDL job"] [job="ID:61, Type:create schema, State:none, SchemaState:none, SchemaID:60, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-07 13:02:57.662 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/08/07 13:02:57.663 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:61, Type:create schema, State:none, SchemaState:none, SchemaID:60, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-07 13:02:57.662 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:02:57.664 +00:00] [INFO] [domain.go:137] ["diff load InfoSchema success"] [usedSchemaVersion=37] [neededSchemaVersion=38] ["start time"=88.141µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/07 13:02:57.666 +00:00] [INFO] [ddl_worker.go:795] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=38] ["take time"=2.268466ms] [job="ID:61, Type:create schema, State:done, SchemaState:public, SchemaID:60, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-07 13:02:57.662 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:02:57.666 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:61, Type:create schema, State:synced, SchemaState:public, SchemaID:60, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-07 13:02:57.662 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:02:57.667 +00:00] [INFO] [ddl.go:593] ["[ddl] DDL job is finished"] [jobID=61]
   > [2024/08/07 13:02:57.667 +00:00] [INFO] [domain.go:660] ["performing DDL change, must reload"]
   > [2024/08/07 13:02:58.686 +00:00] [INFO] [set.go:217] ["set global var"] [conn=2199023255565] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/08/07 13:02:58.687 +00:00] [INFO] [set.go:217] ["set global var"] [conn=2199023255565] [name=transaction_isolation] [val=READ-COMMITTED]
   > [2024/08/07 13:02:58.978 +00:00] [INFO] [session.go:2461] ["CRUCIAL OPERATION"] [conn=2199023255565] [schemaVersion=38] [cur_db=testdb] [sql=" create table t (c_int int, c_str varchar(40));"] [user=root@127.0.0.1]
   > [2024/08/07 13:02:58.979 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:63, Type:create table, State:none, SchemaState:none, SchemaID:60, TableID:62, RowCount:0, ArgLen:1, start time: 2024-08-07 13:02:58.979 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/07 13:02:58.979 +00:00] [INFO] [ddl.go:538] ["[ddl] start DDL job"] [job="ID:63, Type:create table, State:none, SchemaState:none, SchemaID:60, TableID:62, RowCount:0, ArgLen:1, start time: 2024-08-07 13:02:58.979 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query=" create table t (c_int int, c_str varchar(40));"]
   > [2024/08/07 13:02:58.980 +00:00] [INFO] [ddl_worker.go:592] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:63, Type:create table, State:none, SchemaState:none, SchemaID:60, TableID:62, RowCount:0, ArgLen:0, start time: 2024-08-07 13:02:58.979 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:02:58.981 +00:00] [INFO] [domain.go:137] ["diff load InfoSchema success"] [usedSchemaVersion=38] [neededSchemaVersion=39] ["start time"=303.813µs] [phyTblIDs="[62]"] [actionTypes="[8]"]
   > [2024/08/07 13:02:58.983 +00:00] [INFO] [ddl_worker.go:795] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=39] ["take time"=2.266581ms] [job="ID:63, Type:create table, State:done, SchemaState:public, SchemaID:60, TableID:62, RowCount:0, ArgLen:1, start time: 2024-08-07 13:02:58.979 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:02:58.984 +00:00] [INFO] [ddl_worker.go:366] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:63, Type:create table, State:synced, SchemaState:public, SchemaID:60, TableID:62, RowCount:0, ArgLen:0, start time: 2024-08-07 13:02:58.979 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/07 13:02:58.985 +00:00] [INFO] [ddl.go:593] ["[ddl] DDL job is finished"] [jobID=63]
   > [2024/08/07 13:02:58.985 +00:00] [INFO] [domain.go:660] ["performing DDL change, must reload"]
   > [2024/08/07 13:02:58.985 +00:00] [INFO] [split_region.go:61] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=50] ["first split key"=74800000000000003e]
   > [2024/08/07 13:02:58.985 +00:00] [INFO] [split_region.go:158] ["batch split regions complete"] ["batch region ID"=50] ["first at"=74800000000000003e] ["first new region left"="{Id:50 StartKey:7480000000000000ff3800000000000000f8 EndKey:7480000000000000ff3e00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:51 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/08/07 13:02:58.985 +00:00] [INFO] [split_region.go:207] ["split regions complete"] ["region count"=1] ["region IDs"="[50]"]
   > [2024/08/07 13:03:00.180 +00:00] [INFO] [session.go:2461] ["CRUCIAL OPERATION"] [conn=2199023255565] [schemaVersion=39] [cur_db=testdb] [sql=" alter table t add index idx_4 (c_str);"] [user=root@127.0.0.1]
   > [2024/08/07 13:03:00.180 +00:00] [ERROR] [txn.go:215] ["the code should never run here"] [TxnState="Txn{state=valid, txnStartTS=451683491401957376}"] ["staging handler"=1] ["something must be wrong"="github.com/pingcap/tidb/session.(*TxnState).Commit\n\t/go/src/github.com/pingcap/tidb/session/txn.go:218\ngithub.com/pingcap/tidb/session.(*session).doCommit\n\t/go/src/github.com/pingcap/tidb/session/session.go:478\ngithub.com/pingcap/tidb/session.(*session).doCommitWithRetry\n\t/go/src/github.com/pingcap/tidb/session/session.go:499\ngithub.com/pingcap/tidb/session.(*session).CommitTxn\n\t/go/src/github.com/pingcap/tidb/session/session.go:559\ngithub.com/pingcap/tidb/session.(*session).NewTxn\n\t/go/src/github.com/pingcap/tidb/session/session.go:1627\ngithub.com/pingcap/tidb/executor.(*DDLExec).Next\n\t/go/src/github.com/pingcap/tidb/executor/ddl.go:77\ngithub.com/pingcap/tidb/executor.Next\n\t/go/src/github.com/pingcap/tidb/executor/executor.go:278\ngithub.com/pingcap/tidb/executor.(*ExecStmt).handleNoDelayExecutor\n\t/go/src/github.com/pingcap/tidb/executor/adapter.go:524\ngithub.com/pingcap/tidb/executor.(*ExecStmt).handleNoDelay\n\t/go/src/github.com/pingcap/tidb/executor/adapter.go:405\ngithub.com/pingcap/tidb/executor.(*ExecStmt).Exec\n\t/go/src/github.com/pingcap/tidb/executor/adapter.go:355\ngithub.com/pingcap/tidb/session.runStmt\n\t/go/src/github.com/pingcap/tidb/session/session.go:1310\ngithub.com/pingcap/tidb/session.(*session).ExecuteStmt\n\t/go/src/github.com/pingcap/tidb/session/session.go:1254\ngithub.com/pingcap/tidb/server.(*TiDBContext).ExecuteStmt\n\t/go/src/github.com/pingcap/tidb/server/driver_tidb.go:212\ngithub.com/pingcap/tidb/server.(*clientConn).handleStmt\n\t/go/src/github.com/pingcap/tidb/server/conn.go:1561\ngithub.com/pingcap/tidb/server.(*clientConn).handleQuery\n\t/go/src/github.com/pingcap/tidb/server/conn.go:1453\ngithub.com/pingcap/tidb/server.(*clientConn).dispatch\n\t/go/src/github.com/pingcap/tidb/server/conn.go:1027\ngithub.com/pingcap/tidb/server.(*clientConn).Run\n\t/go/src/github.com/pingcap/tidb/server/conn.go:792\ngithub.com/pingcap/tidb/server.(*Server).onConn\n\t/go/src/github.com/pingcap/tidb/server/server.go:461"]
   > [2024/08/07 13:03:00.180 +00:00] [WARN] [session.go:519] ["can not retry txn"] [conn=2199023255565] [label=general] [error="[kv:8024]invalid transaction"] [IsBatchInsert=false] [IsPessimistic=false] [InRestrictedSQL=false] [tidb_retry_limit=10] [tidb_disable_txn_auto_retry=true]
   > [2024/08/07 13:03:00.180 +00:00] [WARN] [session.go:534] ["commit failed"] [conn=2199023255565] ["finished txn"="Txn{state=invalid}"] [error="[kv:8024]invalid transaction"]
   > [2024/08/07 13:03:00.180 +00:00] [INFO] [tidb.go:222] ["rollbackTxn for ddl/autocommit failed"]
   > [2024/08/07 13:03:00.180 +00:00] [WARN] [session.go:1257] ["run statement failed"] [conn=2199023255565] [schemaVersion=39] [error="[kv:8024]invalid transaction"] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 2199023255565,\n  \"status\": 2,\n  \"strictMode\": true,\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"127.0.0.1\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/08/07 13:03:00.180 +00:00] [INFO] [conn.go:809] ["command dispatched failed"] [conn=2199023255565] [connInfo="id:2199023255565, addr:127.0.0.1:60586 status:10, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:0, autocommit:1"] [sql=" alter table t add index idx_4 (c_str);"] [txn_mode=OPTIMISTIC] [err="[kv:8024]invalid transaction\ngithub.com/pingcap/errors.AddStack\n\t/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.20201126102027-b0a155152ca3/errors.go:174\ngithub.com/pingcap/errors.Trace\n\t/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.20201126102027-b0a155152ca3/juju_adaptor.go:15\ngithub.com/pingcap/tidb/session.(*TxnState).Commit\n\t/go/src/github.com/pingcap/tidb/session/txn.go:219\ngithub.com/pingcap/tidb/session.(*session).doCommit\n\t/go/src/github.com/pingcap/tidb/session/session.go:478\ngithub.com/pingcap/tidb/session.(*session).doCommitWithRetry\n\t/go/src/github.com/pingcap/tidb/session/session.go:499\ngithub.com/pingcap/tidb/session.(*session).CommitTxn\n\t/go/src/github.com/pingcap/tidb/session/session.go:559\ngithub.com/pingcap/tidb/session.(*session).NewTxn\n\t/go/src/github.com/pingcap/tidb/session/session.go:1627\ngithub.com/pingcap/tidb/executor.(*DDLExec).Next\n\t/go/src/github.com/pingcap/tidb/executor/ddl.go:77\ngithub.com/pingcap/tidb/executor.Next\n\t/go/src/github.com/pingcap/tidb/executor/executor.go:278\ngithub.com/pingcap/tidb/executor.(*ExecStmt).handleNoDelayExecutor\n\t/go/src/github.com/pingcap/tidb/executor/adapter.go:524\ngithub.com/pingcap/tidb/executor.(*ExecStmt).handleNoDelay\n\t/go/src/github.com/pingcap/tidb/executor/adapter.go:405\ngithub.com/pingcap/tidb/executor.(*ExecStmt).Exec\n\t/go/src/github.com/pingcap/tidb/executor/adapter.go:355\ngithub.com/pingcap/tidb/session.runStmt\n\t/go/src/github.com/pingcap/tidb/session/session.go:1310\ngithub.com/pingcap/tidb/session.(*session).ExecuteStmt\n\t/go/src/github.com/pingcap/tidb/session/session.go:1254\ngithub.com/pingcap/tidb/server.(*TiDBContext).ExecuteStmt\n\t/go/src/github.com/pingcap/tidb/server/driver_tidb.go:212\ngithub.com/pingcap/tidb/server.(*clientConn).handleStmt\n\t/go/src/github.com/pingcap/tidb/server/conn.go:1561\ngithub.com/pingcap/tidb/server.(*clientConn).handleQuery\n\t/go/src/github.com/pingcap/tidb/server/conn.go:1453\ngithub.com/pingcap/tidb/server.(*clientConn).dispatch\n\t/go/src/github.com/pingcap/tidb/server/conn.go:1027\ngithub.com/pingcap/tidb/server.(*clientConn).Run\n\t/go/src/github.com/pingcap/tidb/server/conn.go:792\ngithub.com/pingcap/tidb/server.(*Server).onConn\n\t/go/src/github.com/pingcap/tidb/server/server.go:461\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1594"]
