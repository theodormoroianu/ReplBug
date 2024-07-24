# Bug ID TIDB-21284-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/21284
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              transaction retry may cause panic


## Details
 * Database: tidb-v4.0.8
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
   > [2024/07/24 11:15:25.774 +00:00] [INFO] [session.go:2161] ["CRUCIAL OPERATION"] [conn=10] [schemaVersion=45] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.58]
   > [2024/07/24 11:15:25.776 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:66, Type:drop schema, State:none, SchemaState:none, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:25.774 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 11:15:25.776 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:66, Type:drop schema, State:none, SchemaState:none, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:25.774 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/24 11:15:25.776 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:drop schema, State:none, SchemaState:none, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:25.774 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:25.778 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=45] [neededSchemaVersion=46] ["start time"=91.982µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 11:15:25.780 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=46] ["take time"=2.168242ms] [job="ID:66, Type:drop schema, State:running, SchemaState:write only, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:25.774 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:25.781 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:drop schema, State:running, SchemaState:write only, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:25.774 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:25.782 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=46] [neededSchemaVersion=47] ["start time"=87.791µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 11:15:25.784 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=47] ["take time"=2.233474ms] [job="ID:66, Type:drop schema, State:running, SchemaState:delete only, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:25.774 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:25.785 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:drop schema, State:running, SchemaState:delete only, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:25.774 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:25.787 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=47] [neededSchemaVersion=48] ["start time"=138.217µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 11:15:25.789 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=48] ["take time"=2.197016ms] [job="ID:66, Type:drop schema, State:done, SchemaState:none, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:25.774 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:25.790 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=66] [jobType="drop schema"]
   > [2024/07/24 11:15:25.791 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:drop schema, State:synced, SchemaState:none, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:25.774 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:25.793 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=66]
   > [2024/07/24 11:15:25.793 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/07/24 11:15:25.795 +00:00] [INFO] [session.go:2161] ["CRUCIAL OPERATION"] [conn=10] [schemaVersion=48] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.58]
   > [2024/07/24 11:15:25.797 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:68, Type:create schema, State:none, SchemaState:none, SchemaID:67, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 11:15:25.796 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 11:15:25.797 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:68, Type:create schema, State:none, SchemaState:none, SchemaID:67, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 11:15:25.796 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/24 11:15:25.798 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:68, Type:create schema, State:none, SchemaState:none, SchemaID:67, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:25.796 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:25.800 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=48] [neededSchemaVersion=49] ["start time"=255.97µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 11:15:25.802 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=49] ["take time"=2.206934ms] [job="ID:68, Type:create schema, State:done, SchemaState:public, SchemaID:67, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 11:15:25.796 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:25.803 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:68, Type:create schema, State:synced, SchemaState:public, SchemaID:67, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:25.796 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:25.805 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=68]
   > [2024/07/24 11:15:25.805 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/07/24 11:15:25.808 +00:00] [INFO] [session.go:2161] ["CRUCIAL OPERATION"] [conn=10] [schemaVersion=49] [cur_db=testdb] [sql="create table t (a int);"] [user=root@10.88.0.58]
   > [2024/07/24 11:15:25.810 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:70, Type:create table, State:none, SchemaState:none, SchemaID:67, TableID:69, RowCount:0, ArgLen:1, start time: 2024-07-24 11:15:25.809 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 11:15:25.810 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:70, Type:create table, State:none, SchemaState:none, SchemaID:67, TableID:69, RowCount:0, ArgLen:1, start time: 2024-07-24 11:15:25.809 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t (a int);"]
   > [2024/07/24 11:15:25.811 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:70, Type:create table, State:none, SchemaState:none, SchemaID:67, TableID:69, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:25.809 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:25.814 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=49] [neededSchemaVersion=50] ["start time"=900.122µs] [phyTblIDs="[69]"] [actionTypes="[8]"]
   > [2024/07/24 11:15:25.815 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=50] ["take time"=2.160838ms] [job="ID:70, Type:create table, State:done, SchemaState:public, SchemaID:67, TableID:69, RowCount:0, ArgLen:1, start time: 2024-07-24 11:15:25.809 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:25.816 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:70, Type:create table, State:synced, SchemaState:public, SchemaID:67, TableID:69, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:25.809 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:25.818 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=70]
   > [2024/07/24 11:15:25.818 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/07/24 11:15:25.819 +00:00] [INFO] [split_region.go:60] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=50] ["first split key"=748000000000000045]
   > [2024/07/24 11:15:25.819 +00:00] [INFO] [split_region.go:157] ["batch split regions complete"] ["batch region ID"=50] ["first at"=748000000000000045] ["first new region left"="{Id:50 StartKey:7480000000000000ff3f00000000000000f8 EndKey: RegionEpoch:{ConfVer:0 Version:1} Peers:[id:51 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/24 11:15:25.819 +00:00] [INFO] [split_region.go:209] ["split regions complete"] ["region count"=1] ["region IDs"="[50]"]
   > [2024/07/24 11:15:26.845 +00:00] [INFO] [set.go:216] ["set global var"] [conn=11] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/07/24 11:15:26.846 +00:00] [INFO] [set.go:216] ["set global var"] [conn=11] [name=transaction_isolation] [val=READ-COMMITTED]
   > [2024/07/24 11:15:28.952 +00:00] [WARN] [session.go:462] [sql] [conn=11] [label=general] [error="[kv:9007]Write conflict, txnStartTS=451364710708412416, conflictStartTS=451364710871465984, conflictCommitTS=451364710871728128, key={tableID=69, handle=1} primary=[]byte(nil) [try again later]"] [txn="Txn{state=invalid}"]
   > [2024/07/24 11:15:28.953 +00:00] [WARN] [session.go:662] [retrying] [conn=11] [schemaVersion=50] [retryCnt=0] [queryNum=0] [sql=" SET SQL_SELECT_LIMIT=DEFAULT;"]
   > [2024/07/24 11:15:28.953 +00:00] [INFO] [2pc.go:1305] ["2PC clean up done"] [conn=11] [txnStartTS=451364710708412416]
   > [2024/07/24 11:15:28.953 +00:00] [ERROR] [conn.go:717] ["connection running loop panic"] [conn=11] [lastSQL=" commit;"] [err="runtime error: invalid memory address or nil pointer dereference"] [stack="goroutine 529 [running]:\ngithub.com/pingcap/tidb/server.(*clientConn).Run.func1(0x3778a60, 0xc0001b4540, 0xc0002d2780)\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/server/conn.go:715 +0xee\npanic(0x2e82400, 0x4d78fb0)\n\t/usr/local/go/src/runtime/panic.go:679 +0x1b2\ngithub.com/pingcap/tidb/session.(*session).StmtCommit(0xc001538240, 0x0, 0x0, 0x0)\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/session/txn.go:585 +0x970\ngithub.com/pingcap/tidb/session.(*session).retry(0xc001538240, 0x3778a60, 0xc0014ed3b0, 0xa, 0x0, 0x0)\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/session/session.go:681 +0x7e7\ngithub.com/pingcap/tidb/session.(*session).doCommitWithRetry(0xc001538240, 0x3778a60, 0xc0014ed3b0, 0x0, 0x0)\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/session/session.go:470 +0x15c1\ngithub.com/pingcap/tidb/session.(*session).CommitTxn(0xc001538240, 0x3778a60, 0xc0014ed170, 0x0, 0x0)\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/session/session.go:510 +0x12b\ngithub.com/pingcap/tidb/session.autoCommitAfterStmt(0x3778a60, 0xc0014ed170, 0xc001538240, 0x0, 0x0, 0x37938e0, 0xc001efc210, 0x0, 0x0)\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/session/tidb.go:230 +0x38e\ngithub.com/pingcap/tidb/session.finishStmt(0x3778a60, 0xc0014ed170, 0xc001538240, 0x0, 0x0, 0x37938e0, 0xc001efc210, 0x4, 0x0)\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/session/tidb.go:196 +0x71\ngithub.com/pingcap/tidb/session.runStmt(0x3778a60, 0xc0014ed170, 0x37bcaa0, 0xc001538240, 0x37938e0, 0xc001efc210, 0x0, 0x0, 0x0, 0x0)\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/session/tidb.go:316 +0x433\ngithub.com/pingcap/tidb/session.(*session).executeStatement(0xc001538240, 0x3778a60, 0xc0014ed170, 0xc001efc210, 0x0, 0x0, 0x0, 0x0, 0xb, 0xc0017be250, ...)\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/session/session.go:1063 +0xa7\ngithub.com/pingcap/tidb/session.(*session).execute(0xc001538240, 0x3778a60, 0xc0014ed170, 0xc000756555, 0x8, 0xc00180a998, 0x203000, 0x12fa97f, 0xc00180a980, 0x203000)\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/session/session.go:1175 +0x737\ngithub.com/pingcap/tidb/session.(*session).Execute(0xc001538240, 0x3778a60, 0xc0014ed170, 0xc000756555, 0x8, 0x0, 0x0, 0x0, 0x0, 0x0)\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/session/session.go:1106 +0xdb\ngithub.com/pingcap/tidb/server.(*TiDBContext).Execute(0xc0001b48d0, 0x3778a60, 0xc0014ed170, 0xc000756555, 0x8, 0xc0010fad50, 0x3778a60, 0xc0014ed170, 0xc000e6d290, 0x2a4b4b6)\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/server/driver_tidb.go:248 +0x7c\ngithub.com/pingcap/tidb/server.(*clientConn).handleQuery(0xc0002d2780, 0x3778a60, 0xc0014ed170, 0xc000756555, 0x8, 0x0, 0x0)\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/server/conn.go:1354 +0x164\ngithub.com/pingcap/tidb/server.(*clientConn).dispatch(0xc0002d2780, 0x37789a0, 0xc0010534c0, 0xc000756555, 0x9, 0x8, 0x0, 0x0)\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/server/conn.go:985 +0x6f3\ngithub.com/pingcap/tidb/server.(*clientConn).Run(0xc0002d2780, 0x3778a60, 0xc0001b4540)\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/server/conn.go:772 +0x27f\ngithub.com/pingcap/tidb/server.(*Server).onConn(0xc0013cde40, 0xc0002d2780)\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/server/server.go:421 +0xb12\ncreated by github.com/pingcap/tidb/server.(*Server).Run\n\t/home/jenkins/agent/workspace/tidb_v4.0.8/go/src/github.com/pingcap/tidb/server/server.go:339 +0x709\n"]

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
   > [2024/07/24 11:15:29.956 +00:00] [INFO] [session.go:2161] ["CRUCIAL OPERATION"] [conn=14] [schemaVersion=58] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.58]
   > [2024/07/24 11:15:29.958 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:77, Type:drop schema, State:none, SchemaState:none, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:29.956 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 11:15:29.958 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:77, Type:drop schema, State:none, SchemaState:none, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:29.956 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/24 11:15:29.959 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:none, SchemaState:none, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:29.956 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:29.961 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=58] [neededSchemaVersion=59] ["start time"=130.674µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 11:15:29.963 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=59] ["take time"=2.183607ms] [job="ID:77, Type:drop schema, State:running, SchemaState:write only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:29.956 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:29.963 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:running, SchemaState:write only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:29.956 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:29.965 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=59] [neededSchemaVersion=60] ["start time"=99.735µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 11:15:29.967 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=60] ["take time"=2.201346ms] [job="ID:77, Type:drop schema, State:running, SchemaState:delete only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:29.956 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:29.968 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:running, SchemaState:delete only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:29.956 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:29.970 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=60] [neededSchemaVersion=61] ["start time"=126.414µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 11:15:29.972 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=61] ["take time"=2.265531ms] [job="ID:77, Type:drop schema, State:done, SchemaState:none, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:29.956 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:29.973 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=77] [jobType="drop schema"]
   > [2024/07/24 11:15:29.973 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:synced, SchemaState:none, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:29.956 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:29.975 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=77]
   > [2024/07/24 11:15:29.976 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/07/24 11:15:29.978 +00:00] [INFO] [session.go:2161] ["CRUCIAL OPERATION"] [conn=14] [schemaVersion=61] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.58]
   > [2024/07/24 11:15:29.981 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:79, Type:create schema, State:none, SchemaState:none, SchemaID:78, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 11:15:29.979 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 11:15:29.981 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:79, Type:create schema, State:none, SchemaState:none, SchemaID:78, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 11:15:29.979 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/24 11:15:29.982 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:79, Type:create schema, State:none, SchemaState:none, SchemaID:78, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:29.979 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:29.984 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=61] [neededSchemaVersion=62] ["start time"=210.434µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 11:15:29.986 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=62] ["take time"=2.184864ms] [job="ID:79, Type:create schema, State:done, SchemaState:public, SchemaID:78, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 11:15:29.979 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:29.987 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:79, Type:create schema, State:synced, SchemaState:public, SchemaID:78, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:29.979 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:29.988 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=79]
   > [2024/07/24 11:15:29.988 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/07/24 11:15:29.991 +00:00] [INFO] [session.go:2161] ["CRUCIAL OPERATION"] [conn=14] [schemaVersion=62] [cur_db=testdb] [sql="create table t (a int);"] [user=root@10.88.0.58]
   > [2024/07/24 11:15:29.994 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:81, Type:create table, State:none, SchemaState:none, SchemaID:78, TableID:80, RowCount:0, ArgLen:1, start time: 2024-07-24 11:15:29.992 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 11:15:29.994 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:81, Type:create table, State:none, SchemaState:none, SchemaID:78, TableID:80, RowCount:0, ArgLen:1, start time: 2024-07-24 11:15:29.992 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t (a int);"]
   > [2024/07/24 11:15:29.995 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:81, Type:create table, State:none, SchemaState:none, SchemaID:78, TableID:80, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:29.992 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:29.998 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=62] [neededSchemaVersion=63] ["start time"=839.569µs] [phyTblIDs="[80]"] [actionTypes="[8]"]
   > [2024/07/24 11:15:29.999 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=63] ["take time"=2.15574ms] [job="ID:81, Type:create table, State:done, SchemaState:public, SchemaID:78, TableID:80, RowCount:0, ArgLen:1, start time: 2024-07-24 11:15:29.992 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:30.000 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:81, Type:create table, State:synced, SchemaState:public, SchemaID:78, TableID:80, RowCount:0, ArgLen:0, start time: 2024-07-24 11:15:29.992 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 11:15:30.002 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=81]
   > [2024/07/24 11:15:30.002 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/07/24 11:15:30.002 +00:00] [INFO] [split_region.go:60] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=54] ["first split key"=748000000000000050]
   > [2024/07/24 11:15:30.002 +00:00] [INFO] [split_region.go:157] ["batch split regions complete"] ["batch region ID"=54] ["first at"=748000000000000050] ["first new region left"="{Id:54 StartKey:7480000000000000ff4a00000000000000f8 EndKey: RegionEpoch:{ConfVer:0 Version:1} Peers:[id:55 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/24 11:15:30.002 +00:00] [INFO] [split_region.go:209] ["split regions complete"] ["region count"=1] ["region IDs"="[54]"]
