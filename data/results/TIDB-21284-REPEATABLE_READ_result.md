# Bug ID TIDB-21284-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/21284
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              transaction retry may cause panic


## Details
 * Database: tidb-v4.0.8
 * Number of scenarios: 2
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows: 0
 * Instruction #1:
     - Instruction:  set @@tidb_disable_txn_auto_retry=0;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows: 0
 * Instruction #2:
     - Instruction:  set autocommit=0;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows: 0
 * Instruction #3:
     - Instruction:  select * from t;
     - Transaction: conn_0
     - Output: [(1,)]
     - Executed order: 3
     - Affected rows: 1
 * Instruction #4:
     - Instruction:  SET SQL_SELECT_LIMIT=DEFAULT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows: 0
 * Instruction #5:
     - Instruction:  update t set a=2;
     - Transaction: conn_1
     - Output: None
     - Executed order: 5
     - Affected rows: 1
 * Instruction #6:
     - Instruction:  update t set a=3;
     - Transaction: conn_0
     - Output: None
     - Executed order: 6
     - Affected rows: 1
 * Instruction #7:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: ERROR: 1105 (HY000): runtime error: invalid memory address or nil pointer dereference
     - Executed order: Not executed
     - Affected rows: -1

 * Container logs:
   > [2024/07/24 11:15:18.563 +00:00] [INFO] [session.go:2161] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=22] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.58]
   > [2024/07/24 11:15:18.565 +00:00] [INFO] [session.go:2161] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=22] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.58]
   > [2024/07/24 11:15:18.566 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 11:15:18.565 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 11:15:18.566 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 11:15:18.565 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/24 11:15:18.567 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:18.565 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:18.569 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=22] [neededSchemaVersion=23] ["start time"=172.37µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 11:15:18.571 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=23] ["take time"=2.158604ms] [job="ID:46, Type:create schema, State:done, SchemaState:public, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 11:15:18.565 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:18.571 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:46, Type:create schema, State:synced, SchemaState:public, SchemaID:45, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:18.565 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:18.572 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=46]
   > [2024/07/24 11:15:18.572 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/07/24 11:15:18.575 +00:00] [INFO] [session.go:2161] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=23] [cur_db=testdb] [sql="create table t (a int);"] [user=root@10.88.0.58]
   > [2024/07/24 11:15:18.577 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-07-24 11:15:18.576 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 11:15:18.577 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-07-24 11:15:18.576 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t (a int);"]
   > [2024/07/24 11:15:18.577 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:18.576 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:18.579 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=23] [neededSchemaVersion=24] ["start time"=396.493µs] [phyTblIDs="[47]"] [actionTypes="[8]"]
   > [2024/07/24 11:15:18.581 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=24] ["take time"=2.157276ms] [job="ID:48, Type:create table, State:done, SchemaState:public, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-07-24 11:15:18.576 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:18.582 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:48, Type:create table, State:synced, SchemaState:public, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:18.576 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:18.583 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=48]
   > [2024/07/24 11:15:18.583 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/07/24 11:15:18.583 +00:00] [INFO] [split_region.go:60] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=42] ["first split key"=74800000000000002f]
   > [2024/07/24 11:15:18.584 +00:00] [INFO] [split_region.go:157] ["batch split regions complete"] ["batch region ID"=42] ["first at"=74800000000000002f] ["first new region left"="{Id:42 StartKey:7480000000000000ff2b00000000000000f8 EndKey: RegionEpoch:{ConfVer:0 Version:1} Peers:[id:43 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/24 11:15:18.584 +00:00] [INFO] [split_region.go:209] ["split regions complete"] ["region count"=1] ["region IDs"="[42]"]
   > [2024/07/24 11:15:19.616 +00:00] [INFO] [set.go:216] ["set global var"] [conn=3] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/07/24 11:15:19.616 +00:00] [INFO] [set.go:216] ["set global var"] [conn=3] [name=transaction_isolation] [val=REPEATABLE-READ]
   > [2024/07/24 11:15:21.724 +00:00] [WARN] [session.go:462] [sql] [conn=3] [label=general] [error="[kv:9007]Write conflict, txnStartTS=451364708813635584, conflictStartTS=451364708976427008, conflictCommitTS=451364708976689152, key={tableID=47, handle=1} primary=[]byte(nil) [try again later]"] [txn="Txn{state=invalid}"]
   > [2024/07/24 11:15:21.724 +00:00] [WARN] [session.go:662] [retrying] [conn=3] [schemaVersion=24] [retryCnt=0] [queryNum=0] [sql=" SET SQL_SELECT_LIMIT=DEFAULT;"]
   > [2024/07/24 11:15:21.724 +00:00] [INFO] [2pc.go:1305] ["2PC clean up done"] [conn=3] [txnStartTS=451364708813635584]
   > [2024/07/24 11:15:21.725 +00:00] [ERROR] [conn.go:717] ["connection running loop panic"] [conn=3] [lastSQL=" commit;"] [err="runtime error: invalid memory address or nil pointer dereference"] [stack="goroutine 431 [running]:\ngithub.com/pingcap/tidb/server.(*clientConn).Run.func1(0x3778a60, 0xc00121ea50, 0xc00135a1e0)\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/server/conn.go:715 +0xee\npanic(0x2e82400, 0x4d78fb0)\n\t/usr/local/go/src/runtime/panic.go:679 +0x1b2\ngithub.com/pingcap/tidb/session.(*session).StmtCommit(0xc0017aac60, 0x0, 0x0, 0x0)\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/session/txn.go:585 +0x970\ngithub.com/pingcap/tidb/session.(*session).retry(0xc0017aac60, 0x3778a60, 0xc001673a10, 0xa, 0x0, 0x0)\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/session/session.go:681 +0x7e7\ngithub.com/pingcap/tidb/session.(*session).doCommitWithRetry(0xc0017aac60, 0x3778a60, 0xc001673a10, 0x0, 0x0)\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/session/session.go:470 +0x15c1\ngithub.com/pingcap/tidb/session.(*session).CommitTxn(0xc0017aac60, 0x3778a60, 0xc0016737d0, 0x0, 0x0)\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/session/session.go:510 +0x12b\ngithub.com/pingcap/tidb/session.autoCommitAfterStmt(0x3778a60, 0xc0016737d0, 0xc0017aac60, 0x0, 0x0, 0x37938e0, 0xc00153e000, 0x0, 0x0)\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/session/tidb.go:230 +0x38e\ngithub.com/pingcap/tidb/session.finishStmt(0x3778a60, 0xc0016737d0, 0xc0017aac60, 0x0, 0x0, 0x37938e0, 0xc00153e000, 0x4, 0x0)\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/session/tidb.go:196 +0x71\ngithub.com/pingcap/tidb/session.runStmt(0x3778a60, 0xc0016737d0, 0x37bcaa0, 0xc0017aac60, 0x37938e0, 0xc00153e000, 0x0, 0x0, 0x0, 0x0)\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/session/tidb.go:316 +0x433\ngithub.com/pingcap/tidb/session.(*session).executeStatement(0xc0017aac60, 0x3778a60, 0xc0016737d0, 0xc00153e000, 0x0, 0x0, 0x0, 0x0, 0xb, 0xc0013d3070, ...)\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/session/session.go:1063 +0xa7\ngithub.com/pingcap/tidb/session.(*session).execute(0xc0017aac60, 0x3778a60, 0xc0016737d0, 0xc00100f691, 0x8, 0x7ff8a0d91ae0, 0x203000, 0xaa, 0x80, 0x203000)\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/session/session.go:1175 +0x737\ngithub.com/pingcap/tidb/session.(*session).Execute(0xc0017aac60, 0x3778a60, 0xc0016737d0, 0xc00100f691, 0x8, 0x0, 0x0, 0x0, 0x0, 0x0)\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/session/session.go:1106 +0xdb\ngithub.com/pingcap/tidb/server.(*TiDBContext).Execute(0xc00121ede0, 0x3778a60, 0xc0016737d0, 0xc00100f691, 0x8, 0xc000f30240, 0x3778a60, 0xc0016737d0, 0xc001df3290, 0x2a4b4b6)\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/server/driver_tidb.go:248 +0x7c\ngithub.com/pingcap/tidb/server.(*clientConn).handleQuery(0xc00135a1e0, 0x3778a60, 0xc0016737d0, 0xc00100f691, 0x8, 0x0, 0x0)\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/server/conn.go:1354 +0x164\ngithub.com/pingcap/tidb/server.(*clientConn).dispatch(0xc00135a1e0, 0x37789a0, 0xc001052040, 0xc00100f691, 0x9, 0x8, 0x0, 0x0)\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/server/conn.go:985 +0x6f3\ngithub.com/pingcap/tidb/server.(*clientConn).Run(0xc00135a1e0, 0x3778a60, 0xc00121ea50)\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/server/conn.go:772 +0x27f\ngithub.com/pingcap/tidb/server.(*Server).onConn(0xc0013cde40, 0xc00135a1e0)\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/server/server.go:421 +0xb12\ncreated by github.com/pingcap/tidb/server.(*Server).Run\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/server/server.go:339 +0x709\n"]

### Scenario 1
 * Instruction #0:
     - Instruction:  set @@tidb_disable_txn_auto_retry=0;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows: 0
 * Instruction #1:
     - Instruction:  select * from t;
     - Transaction: conn_0
     - Output: [(1,)]
     - Executed order: 1
     - Affected rows: 1
 * Instruction #2:
     - Instruction:  SET SQL_SELECT_LIMIT=DEFAULT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows: 0
 * Instruction #3:
     - Instruction:  update t set a=2;
     - Transaction: conn_1
     - Output: None
     - Executed order: 3
     - Affected rows: 1
 * Instruction #4:
     - Instruction:  update t set a=3;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows: 1

 * Container logs:
   > [2024/07/24 11:15:22.569 +00:00] [INFO] [session.go:2161] ["CRUCIAL OPERATION"] [conn=6] [schemaVersion=32] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.58]
   > [2024/07/24 11:15:22.570 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:55, Type:drop schema, State:none, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:22.569 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 11:15:22.570 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:55, Type:drop schema, State:none, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:22.569 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/24 11:15:22.571 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:55, Type:drop schema, State:none, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:22.569 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:22.572 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=32] [neededSchemaVersion=33] ["start time"=94.426µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 11:15:22.574 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=33] ["take time"=2.180185ms] [job="ID:55, Type:drop schema, State:running, SchemaState:write only, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:22.569 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:22.575 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:55, Type:drop schema, State:running, SchemaState:write only, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:22.569 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:22.576 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=33] [neededSchemaVersion=34] ["start time"=84.509µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 11:15:22.578 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=34] ["take time"=2.171593ms] [job="ID:55, Type:drop schema, State:running, SchemaState:delete only, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:22.569 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:22.578 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:55, Type:drop schema, State:running, SchemaState:delete only, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:22.569 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:22.580 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=34] [neededSchemaVersion=35] ["start time"=132.56µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 11:15:22.582 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=35] ["take time"=2.269023ms] [job="ID:55, Type:drop schema, State:done, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:22.569 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:22.583 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=55] [jobType="drop schema"]
   > [2024/07/24 11:15:22.584 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:55, Type:drop schema, State:synced, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:22.569 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:22.585 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=55]
   > [2024/07/24 11:15:22.586 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/07/24 11:15:22.587 +00:00] [INFO] [session.go:2161] ["CRUCIAL OPERATION"] [conn=6] [schemaVersion=35] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.58]
   > [2024/07/24 11:15:22.589 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:57, Type:create schema, State:none, SchemaState:none, SchemaID:56, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 11:15:22.588 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 11:15:22.589 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:57, Type:create schema, State:none, SchemaState:none, SchemaID:56, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 11:15:22.588 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/24 11:15:22.590 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:57, Type:create schema, State:none, SchemaState:none, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:22.588 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:22.591 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=35] [neededSchemaVersion=36] ["start time"=175.303µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 11:15:22.593 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=36] ["take time"=2.136813ms] [job="ID:57, Type:create schema, State:done, SchemaState:public, SchemaID:56, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 11:15:22.588 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:22.594 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:57, Type:create schema, State:synced, SchemaState:public, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:22.588 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:22.595 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=57]
   > [2024/07/24 11:15:22.595 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/07/24 11:15:22.598 +00:00] [INFO] [session.go:2161] ["CRUCIAL OPERATION"] [conn=6] [schemaVersion=36] [cur_db=testdb] [sql="create table t (a int);"] [user=root@10.88.0.58]
   > [2024/07/24 11:15:22.601 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:59, Type:create table, State:none, SchemaState:none, SchemaID:56, TableID:58, RowCount:0, ArgLen:1, start time: 2024-07-24 11:15:22.6 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 11:15:22.601 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:59, Type:create table, State:none, SchemaState:none, SchemaID:56, TableID:58, RowCount:0, ArgLen:1, start time: 2024-07-24 11:15:22.6 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t (a int);"]
   > [2024/07/24 11:15:22.602 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:59, Type:create table, State:none, SchemaState:none, SchemaID:56, TableID:58, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:22.6 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:22.604 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=36] [neededSchemaVersion=37] ["start time"=525.909µs] [phyTblIDs="[58]"] [actionTypes="[8]"]
   > [2024/07/24 11:15:22.606 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=37] ["take time"=2.170476ms] [job="ID:59, Type:create table, State:done, SchemaState:public, SchemaID:56, TableID:58, RowCount:0, ArgLen:1, start time: 2024-07-24 11:15:22.6 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:22.606 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:59, Type:create table, State:synced, SchemaState:public, SchemaID:56, TableID:58, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:22.6 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:22.608 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=59]
   > [2024/07/24 11:15:22.608 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/07/24 11:15:22.608 +00:00] [INFO] [split_region.go:60] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=46] ["first split key"=74800000000000003a]
   > [2024/07/24 11:15:22.608 +00:00] [INFO] [split_region.go:157] ["batch split regions complete"] ["batch region ID"=46] ["first at"=74800000000000003a] ["first new region left"="{Id:46 StartKey:7480000000000000ff3400000000000000f8 EndKey: RegionEpoch:{ConfVer:0 Version:1} Peers:[id:47 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/24 11:15:22.608 +00:00] [INFO] [split_region.go:209] ["split regions complete"] ["region count"=1] ["region IDs"="[46]"]
