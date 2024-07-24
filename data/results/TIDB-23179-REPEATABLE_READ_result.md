# Bug ID TIDB-23179-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/23179
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              point-get + pessimistic txn + overflow in secondary index may panic


## Details
 * Database: tidb-v4.0.11
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
     - Instruction:  begin pessimistic;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows: 0
 * Instruction #2:
     - Instruction:  update t set v = 100 where k = -200;
     - Transaction: conn_0
     - Output: ERROR: 1105 (HY000): runtime error: index out of range [0] with length 0
     - Executed order: Not executed
     - Affected rows: -1

 * Container logs:
   > [2024/07/24 12:37:25.305 +00:00] [INFO] [session.go:2288] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=22] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.81]
   > [2024/07/24 12:37:25.305 +00:00] [INFO] [session.go:2288] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=22] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.81]
   > [2024/07/24 12:37:25.307 +00:00] [INFO] [ddl_worker.go:262] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:37:25.306 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 12:37:25.307 +00:00] [INFO] [ddl.go:537] ["[ddl] start DDL job"] [job="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:37:25.306 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/24 12:37:25.307 +00:00] [INFO] [ddl_worker.go:596] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:46, Type:create schema, State:none, SchemaState:none, SchemaID:45, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:25.306 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:25.309 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [usedSchemaVersion=22] [neededSchemaVersion=23] ["start time"=151.696µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:37:25.311 +00:00] [INFO] [ddl_worker.go:790] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=23] ["take time"=2.163844ms] [job="ID:46, Type:create schema, State:done, SchemaState:public, SchemaID:45, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:37:25.306 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:25.311 +00:00] [INFO] [ddl_worker.go:368] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:46, Type:create schema, State:synced, SchemaState:public, SchemaID:45, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:25.306 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:25.312 +00:00] [INFO] [ddl.go:573] ["[ddl] DDL job is finished"] [jobID=46]
   > [2024/07/24 12:37:25.312 +00:00] [INFO] [domain.go:635] ["performing DDL change, must reload"]
   > [2024/07/24 12:37:25.315 +00:00] [INFO] [session.go:2288] ["CRUCIAL OPERATION"] [conn=2] [schemaVersion=23] [cur_db=testdb] [sql="create table t(k tinyint, v int, unique key(k));"] [user=root@10.88.0.81]
   > [2024/07/24 12:37:25.317 +00:00] [INFO] [ddl_worker.go:262] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-07-24 12:37:25.316 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 12:37:25.317 +00:00] [INFO] [ddl.go:537] ["[ddl] start DDL job"] [job="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-07-24 12:37:25.316 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t(k tinyint, v int, unique key(k));"]
   > [2024/07/24 12:37:25.318 +00:00] [INFO] [ddl_worker.go:596] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:48, Type:create table, State:none, SchemaState:none, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:25.316 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:25.319 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [usedSchemaVersion=23] [neededSchemaVersion=24] ["start time"=200.376µs] [phyTblIDs="[47]"] [actionTypes="[8]"]
   > [2024/07/24 12:37:25.321 +00:00] [INFO] [ddl_worker.go:790] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=24] ["take time"=2.10818ms] [job="ID:48, Type:create table, State:done, SchemaState:public, SchemaID:45, TableID:47, RowCount:0, ArgLen:1, start time: 2024-07-24 12:37:25.316 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:25.321 +00:00] [INFO] [ddl_worker.go:368] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:48, Type:create table, State:synced, SchemaState:public, SchemaID:45, TableID:47, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:25.316 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:25.323 +00:00] [INFO] [ddl.go:573] ["[ddl] DDL job is finished"] [jobID=48]
   > [2024/07/24 12:37:25.323 +00:00] [INFO] [domain.go:635] ["performing DDL change, must reload"]
   > [2024/07/24 12:37:25.323 +00:00] [INFO] [split_region.go:60] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=42] ["first split key"=74800000000000002f]
   > [2024/07/24 12:37:25.323 +00:00] [INFO] [split_region.go:157] ["batch split regions complete"] ["batch region ID"=42] ["first at"=74800000000000002f] ["first new region left"="{Id:42 StartKey:7480000000000000ff2b00000000000000f8 EndKey: RegionEpoch:{ConfVer:0 Version:1} Peers:[id:43 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/24 12:37:25.323 +00:00] [INFO] [split_region.go:209] ["split regions complete"] ["region count"=1] ["region IDs"="[42]"]
   > [2024/07/24 12:37:26.348 +00:00] [INFO] [set.go:213] ["set global var"] [conn=3] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/07/24 12:37:26.348 +00:00] [INFO] [set.go:213] ["set global var"] [conn=3] [name=transaction_isolation] [val=REPEATABLE-READ]
   > [2024/07/24 12:37:26.944 +00:00] [ERROR] [conn.go:724] ["connection running loop panic"] [conn=3] [lastSQL=" update t set v = 100 where k = -200;"] [err="runtime error: index out of range [0] with length 0"] [stack="goroutine 479 [running]:\ngithub.com/pingcap/tidb/server.(*clientConn).Run.func1(0x38ac040, 0xc0016e5380, 0xc001606500)\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/conn.go:722 +0xee\npanic(0x31559a0, 0xc00173a5e0)\n\t/usr/local/go/src/runtime/panic.go:679 +0x1b2\ngithub.com/pingcap/tidb/executor.(*ExecStmt).Exec.func1(0xc0016f58c0, 0xc001758ba0, 0xc001758b80)\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/adapter.go:300 +0x50c\npanic(0x31559a0, 0xc00173a5e0)\n\t/usr/local/go/src/runtime/panic.go:679 +0x1b2\ngithub.com/pingcap/tidb/store/tikv.(*twoPhaseCommitter).primary(...)\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/store/tikv/2pc.go:467\ngithub.com/pingcap/tidb/store/tikv.(*twoPhaseCommitter).appendBatchMutationsBySize(0xc0014c7ce0, 0x0, 0x0, 0x0, 0x3, 0x0, 0x1, 0x0, 0x0, 0x0, ...)\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/store/tikv/2pc.go:1817 +0x5d7\ngithub.com/pingcap/tidb/store/tikv.(*twoPhaseCommitter).doActionOnGroupMutations(0xc0014c7ce0, 0xc0016ef980, 0x38a1180, 0xc0016ef900, 0xc0016efa00, 0x1, 0x1, 0x1, 0x0)\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/store/tikv/2pc.go:604 +0x265\ngithub.com/pingcap/tidb/store/tikv.(*twoPhaseCommitter).doActionOnMutations(0xc0014c7ce0, 0xc0016ef980, 0x38a1180, 0xc0016ef900, 0x0, 0x0, 0x0, 0xc0012127a0, 0x1, 0x1, ...)\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/store/tikv/2pc.go:536 +0x1c2\ngithub.com/pingcap/tidb/store/tikv.(*twoPhaseCommitter).pessimisticLockMutations(0xc0014c7ce0, 0xc0016ef980, 0xc0016ef900, 0x0, 0x0, 0x0, 0xc0012127a0, 0x1, 0x1, 0x0, ...)\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/store/tikv/2pc.go:1365 +0x88\ngithub.com/pingcap/tidb/store/tikv.(*tikvTxn).LockKeys(0xc0005d9c00, 0x38ac040, 0xc00173c960, 0xc0016ef900, 0xc001212780, 0x1, 0x1, 0x0, 0x0)\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/store/tikv/txn.go:480 +0x601\ngithub.com/pingcap/tidb/executor.doLockKeys(0x38ac040, 0xc00173c5d0, 0x38f2b60, 0xc00161f680, 0xc0016ef900, 0xc001212780, 0x1, 0x1, 0x11af8db, 0xc001758038)\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/executor.go:990 +0x191\ngithub.com/pingcap/tidb/executor.(*PointGetExecutor).lockKeyIfNeeded(0xc0014c7b80, 0x38ac040, 0xc00173c5d0, 0x0, 0x0, 0x0, 0x0, 0x0)\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/point_get.go:279 +0x17a\ngithub.com/pingcap/tidb/executor.(*PointGetExecutor).Next(0xc0014c7b80, 0x38ac040, 0xc00173c5d0, 0xc0016f6b40, 0x11b3368, 0x70)\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/point_get.go:189 +0x802\ngithub.com/pingcap/tidb/executor.Next(0x38ac040, 0xc00173c5d0, 0x38b6100, 0xc0014c7b80, 0xc0016f6b40, 0x0, 0x0)\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/executor.go:262 +0x225\ngithub.com/pingcap/tidb/executor.(*UpdateExec).updateRows(0xc0005d9ce0, 0x38ac040, 0xc00173c5d0, 0x0, 0x0, 0x0)\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/update.go:162 +0x57a\ngithub.com/pingcap/tidb/executor.(*UpdateExec).Next(0xc0005d9ce0, 0x38ac040, 0xc00173c5d0, 0xc0016f6af0, 0x48, 0x31344c0)\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/update.go:130 +0x6c\ngithub.com/pingcap/tidb/executor.Next(0x38ac040, 0xc00173c5d0, 0x38b6940, 0xc0005d9ce0, 0xc0016f6af0, 0x0, 0x0)\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/executor.go:262 +0x225\ngithub.com/pingcap/tidb/executor.(*ExecStmt).handleNoDelayExecutor(0xc0016f58c0, 0x38ac040,"]

### Scenario 1
 * Instruction #0:
     - Instruction:  update t set v = 100 where k = -200;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows: 0

 * Container logs:
   > [2024/07/24 12:37:27.803 +00:00] [INFO] [session.go:2288] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=32] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.81]
   > [2024/07/24 12:37:27.804 +00:00] [INFO] [ddl_worker.go:262] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:55, Type:drop schema, State:none, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:27.803 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 12:37:27.804 +00:00] [INFO] [ddl.go:537] ["[ddl] start DDL job"] [job="ID:55, Type:drop schema, State:none, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:27.803 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/24 12:37:27.805 +00:00] [INFO] [ddl_worker.go:596] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:55, Type:drop schema, State:none, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:27.803 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:27.806 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [usedSchemaVersion=32] [neededSchemaVersion=33] ["start time"=165.316µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:37:27.808 +00:00] [INFO] [ddl_worker.go:790] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=33] ["take time"=2.171178ms] [job="ID:55, Type:drop schema, State:running, SchemaState:write only, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:27.803 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:27.809 +00:00] [INFO] [ddl_worker.go:596] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:55, Type:drop schema, State:running, SchemaState:write only, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:27.803 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:27.810 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [usedSchemaVersion=33] [neededSchemaVersion=34] ["start time"=106.299µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:37:27.812 +00:00] [INFO] [ddl_worker.go:790] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=34] ["take time"=2.153438ms] [job="ID:55, Type:drop schema, State:running, SchemaState:delete only, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:27.803 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:27.812 +00:00] [INFO] [ddl_worker.go:596] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:55, Type:drop schema, State:running, SchemaState:delete only, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:27.803 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:27.814 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [usedSchemaVersion=34] [neededSchemaVersion=35] ["start time"=89.677µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:37:27.816 +00:00] [INFO] [ddl_worker.go:790] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=35] ["take time"=2.135977ms] [job="ID:55, Type:drop schema, State:done, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:27.803 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:27.816 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=55] [jobType="drop schema"]
   > [2024/07/24 12:37:27.816 +00:00] [INFO] [ddl_worker.go:368] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:55, Type:drop schema, State:synced, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:27.803 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:27.817 +00:00] [INFO] [ddl.go:573] ["[ddl] DDL job is finished"] [jobID=55]
   > [2024/07/24 12:37:27.817 +00:00] [INFO] [domain.go:635] ["performing DDL change, must reload"]
   > [2024/07/24 12:37:27.818 +00:00] [INFO] [session.go:2288] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=35] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.81]
   > [2024/07/24 12:37:27.819 +00:00] [INFO] [ddl_worker.go:262] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:57, Type:create schema, State:none, SchemaState:none, SchemaID:56, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:37:27.819 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 12:37:27.820 +00:00] [INFO] [ddl.go:537] ["[ddl] start DDL job"] [job="ID:57, Type:create schema, State:none, SchemaState:none, SchemaID:56, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:37:27.819 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/24 12:37:27.820 +00:00] [INFO] [ddl_worker.go:596] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:57, Type:create schema, State:none, SchemaState:none, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:27.819 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:27.821 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [usedSchemaVersion=35] [neededSchemaVersion=36] ["start time"=106.928µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:37:27.823 +00:00] [INFO] [ddl_worker.go:790] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=36] ["take time"=2.123475ms] [job="ID:57, Type:create schema, State:done, SchemaState:public, SchemaID:56, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:37:27.819 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:27.823 +00:00] [INFO] [ddl_worker.go:368] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:57, Type:create schema, State:synced, SchemaState:public, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:27.819 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:27.824 +00:00] [INFO] [ddl.go:573] ["[ddl] DDL job is finished"] [jobID=57]
   > [2024/07/24 12:37:27.824 +00:00] [INFO] [domain.go:635] ["performing DDL change, must reload"]
   > [2024/07/24 12:37:27.826 +00:00] [INFO] [session.go:2288] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=36] [cur_db=testdb] [sql="create table t(k tinyint, v int, unique key(k));"] [user=root@10.88.0.81]
   > [2024/07/24 12:37:27.827 +00:00] [INFO] [ddl_worker.go:262] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:59, Type:create table, State:none, SchemaState:none, SchemaID:56, TableID:58, RowCount:0, ArgLen:1, start time: 2024-07-24 12:37:27.826 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 12:37:27.827 +00:00] [INFO] [ddl.go:537] ["[ddl] start DDL job"] [job="ID:59, Type:create table, State:none, SchemaState:none, SchemaID:56, TableID:58, RowCount:0, ArgLen:1, start time: 2024-07-24 12:37:27.826 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t(k tinyint, v int, unique key(k));"]
   > [2024/07/24 12:37:27.827 +00:00] [INFO] [ddl_worker.go:596] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:59, Type:create table, State:none, SchemaState:none, SchemaID:56, TableID:58, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:27.826 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:27.829 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [usedSchemaVersion=36] [neededSchemaVersion=37] ["start time"=240.535µs] [phyTblIDs="[58]"] [actionTypes="[8]"]
   > [2024/07/24 12:37:27.831 +00:00] [INFO] [ddl_worker.go:790] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=37] ["take time"=2.150155ms] [job="ID:59, Type:create table, State:done, SchemaState:public, SchemaID:56, TableID:58, RowCount:0, ArgLen:1, start time: 2024-07-24 12:37:27.826 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:27.831 +00:00] [INFO] [ddl_worker.go:368] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:59, Type:create table, State:synced, SchemaState:public, SchemaID:56, TableID:58, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:27.826 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:27.832 +00:00] [INFO] [ddl.go:573] ["[ddl] DDL job is finished"] [jobID=59]
   > [2024/07/24 12:37:27.833 +00:00] [INFO] [domain.go:635] ["performing DDL change, must reload"]
   > [2024/07/24 12:37:27.833 +00:00] [INFO] [split_region.go:60] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=46] ["first split key"=74800000000000003a]
   > [2024/07/24 12:37:27.833 +00:00] [INFO] [split_region.go:157] ["batch split regions complete"] ["batch region ID"=46] ["first at"=74800000000000003a] ["first new region left"="{Id:46 StartKey:7480000000000000ff3400000000000000f8 EndKey: RegionEpoch:{ConfVer:0 Version:1} Peers:[id:47 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/24 12:37:27.833 +00:00] [INFO] [split_region.go:209] ["split regions complete"] ["region count"=1] ["region IDs"="[46]"]
