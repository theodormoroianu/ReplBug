# Bug ID TIDB-23179-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/23179
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              point-get + pessimistic txn + overflow in secondary index may panic


## Details
 * Database: tidb-v4.0.11
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
   > [2024/07/24 12:37:29.713 +00:00] [INFO] [session.go:2288] ["CRUCIAL OPERATION"] [conn=8] [schemaVersion=45] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.81]
   > [2024/07/24 12:37:29.714 +00:00] [INFO] [ddl_worker.go:262] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:66, Type:drop schema, State:none, SchemaState:none, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:29.713 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 12:37:29.714 +00:00] [INFO] [ddl.go:537] ["[ddl] start DDL job"] [job="ID:66, Type:drop schema, State:none, SchemaState:none, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:29.713 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/24 12:37:29.714 +00:00] [INFO] [ddl_worker.go:596] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:drop schema, State:none, SchemaState:none, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:29.713 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:29.715 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [usedSchemaVersion=45] [neededSchemaVersion=46] ["start time"=104.833µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:37:29.717 +00:00] [INFO] [ddl_worker.go:790] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=46] ["take time"=2.181375ms] [job="ID:66, Type:drop schema, State:running, SchemaState:write only, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:29.713 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:29.718 +00:00] [INFO] [ddl_worker.go:596] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:drop schema, State:running, SchemaState:write only, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:29.713 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:29.719 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [usedSchemaVersion=46] [neededSchemaVersion=47] ["start time"=84.928µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:37:29.721 +00:00] [INFO] [ddl_worker.go:790] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=47] ["take time"=2.196041ms] [job="ID:66, Type:drop schema, State:running, SchemaState:delete only, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:29.713 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:29.721 +00:00] [INFO] [ddl_worker.go:596] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:drop schema, State:running, SchemaState:delete only, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:29.713 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:29.723 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [usedSchemaVersion=47] [neededSchemaVersion=48] ["start time"=82.973µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:37:29.725 +00:00] [INFO] [ddl_worker.go:790] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=48] ["take time"=2.171248ms] [job="ID:66, Type:drop schema, State:done, SchemaState:none, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:29.713 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:29.725 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=66] [jobType="drop schema"]
   > [2024/07/24 12:37:29.726 +00:00] [INFO] [ddl_worker.go:368] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:drop schema, State:synced, SchemaState:none, SchemaID:61, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:29.713 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:29.727 +00:00] [INFO] [ddl.go:573] ["[ddl] DDL job is finished"] [jobID=66]
   > [2024/07/24 12:37:29.727 +00:00] [INFO] [domain.go:635] ["performing DDL change, must reload"]
   > [2024/07/24 12:37:29.729 +00:00] [INFO] [session.go:2288] ["CRUCIAL OPERATION"] [conn=8] [schemaVersion=48] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.81]
   > [2024/07/24 12:37:29.731 +00:00] [INFO] [ddl_worker.go:262] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:68, Type:create schema, State:none, SchemaState:none, SchemaID:67, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:37:29.73 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 12:37:29.731 +00:00] [INFO] [ddl.go:537] ["[ddl] start DDL job"] [job="ID:68, Type:create schema, State:none, SchemaState:none, SchemaID:67, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:37:29.73 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/24 12:37:29.732 +00:00] [INFO] [ddl_worker.go:596] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:68, Type:create schema, State:none, SchemaState:none, SchemaID:67, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:29.73 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:29.733 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [usedSchemaVersion=48] [neededSchemaVersion=49] ["start time"=175.233µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:37:29.735 +00:00] [INFO] [ddl_worker.go:790] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=49] ["take time"=2.177813ms] [job="ID:68, Type:create schema, State:done, SchemaState:public, SchemaID:67, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:37:29.73 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:29.736 +00:00] [INFO] [ddl_worker.go:368] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:68, Type:create schema, State:synced, SchemaState:public, SchemaID:67, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:29.73 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:29.738 +00:00] [INFO] [ddl.go:573] ["[ddl] DDL job is finished"] [jobID=68]
   > [2024/07/24 12:37:29.738 +00:00] [INFO] [domain.go:635] ["performing DDL change, must reload"]
   > [2024/07/24 12:37:29.740 +00:00] [INFO] [session.go:2288] ["CRUCIAL OPERATION"] [conn=8] [schemaVersion=49] [cur_db=testdb] [sql="create table t(k tinyint, v int, unique key(k));"] [user=root@10.88.0.81]
   > [2024/07/24 12:37:29.742 +00:00] [INFO] [ddl_worker.go:262] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:70, Type:create table, State:none, SchemaState:none, SchemaID:67, TableID:69, RowCount:0, ArgLen:1, start time: 2024-07-24 12:37:29.741 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 12:37:29.742 +00:00] [INFO] [ddl.go:537] ["[ddl] start DDL job"] [job="ID:70, Type:create table, State:none, SchemaState:none, SchemaID:67, TableID:69, RowCount:0, ArgLen:1, start time: 2024-07-24 12:37:29.741 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t(k tinyint, v int, unique key(k));"]
   > [2024/07/24 12:37:29.743 +00:00] [INFO] [ddl_worker.go:596] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:70, Type:create table, State:none, SchemaState:none, SchemaID:67, TableID:69, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:29.741 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:29.745 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [usedSchemaVersion=49] [neededSchemaVersion=50] ["start time"=353.749µs] [phyTblIDs="[69]"] [actionTypes="[8]"]
   > [2024/07/24 12:37:29.747 +00:00] [INFO] [ddl_worker.go:790] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=50] ["take time"=2.14401ms] [job="ID:70, Type:create table, State:done, SchemaState:public, SchemaID:67, TableID:69, RowCount:0, ArgLen:1, start time: 2024-07-24 12:37:29.741 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:29.748 +00:00] [INFO] [ddl_worker.go:368] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:70, Type:create table, State:synced, SchemaState:public, SchemaID:67, TableID:69, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:29.741 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:29.750 +00:00] [INFO] [ddl.go:573] ["[ddl] DDL job is finished"] [jobID=70]
   > [2024/07/24 12:37:29.751 +00:00] [INFO] [domain.go:635] ["performing DDL change, must reload"]
   > [2024/07/24 12:37:29.751 +00:00] [INFO] [split_region.go:60] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=50] ["first split key"=748000000000000045]
   > [2024/07/24 12:37:29.751 +00:00] [INFO] [split_region.go:157] ["batch split regions complete"] ["batch region ID"=50] ["first at"=748000000000000045] ["first new region left"="{Id:50 StartKey:7480000000000000ff3f00000000000000f8 EndKey: RegionEpoch:{ConfVer:0 Version:1} Peers:[id:51 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/24 12:37:29.751 +00:00] [INFO] [split_region.go:209] ["split regions complete"] ["region count"=1] ["region IDs"="[50]"]
   > [2024/07/24 12:37:30.770 +00:00] [INFO] [set.go:213] ["set global var"] [conn=9] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/07/24 12:37:30.770 +00:00] [INFO] [set.go:213] ["set global var"] [conn=9] [name=transaction_isolation] [val=READ-COMMITTED]
   > [2024/07/24 12:37:31.364 +00:00] [ERROR] [conn.go:724] ["connection running loop panic"] [conn=9] [lastSQL=" update t set v = 100 where k = -200;"] [err="runtime error: index out of range [0] with length 0"] [stack="goroutine 783 [running]:\ngithub.com/pingcap/tidb/server.(*clientConn).Run.func1(0x38ac040, 0xc0010a0d20, 0xc001603700)\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/conn.go:722 +0xee\npanic(0x31559a0, 0xc00151f740)\n\t/usr/local/go/src/runtime/panic.go:679 +0x1b2\ngithub.com/pingcap/tidb/executor.(*ExecStmt).Exec.func1(0xc001507ad0, 0xc0012d4ba0, 0xc0012d4b80)\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/adapter.go:300 +0x50c\npanic(0x31559a0, 0xc00151f740)\n\t/usr/local/go/src/runtime/panic.go:679 +0x1b2\ngithub.com/pingcap/tidb/store/tikv.(*twoPhaseCommitter).primary(...)\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/store/tikv/2pc.go:467\ngithub.com/pingcap/tidb/store/tikv.(*twoPhaseCommitter).appendBatchMutationsBySize(0xc00159c840, 0x0, 0x0, 0x0, 0x3, 0x0, 0x1, 0x0, 0x0, 0x0, ...)\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/store/tikv/2pc.go:1817 +0x5d7\ngithub.com/pingcap/tidb/store/tikv.(*twoPhaseCommitter).doActionOnGroupMutations(0xc00159c840, 0xc0012e4b80, 0x38a1180, 0xc0012e4b00, 0xc0012e4c00, 0x1, 0x1, 0x1, 0x0)\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/store/tikv/2pc.go:604 +0x265\ngithub.com/pingcap/tidb/store/tikv.(*twoPhaseCommitter).doActionOnMutations(0xc00159c840, 0xc0012e4b80, 0x38a1180, 0xc0012e4b00, 0x0, 0x0, 0x0, 0xc00116bec0, 0x1, 0x1, ...)\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/store/tikv/2pc.go:536 +0x1c2\ngithub.com/pingcap/tidb/store/tikv.(*twoPhaseCommitter).pessimisticLockMutations(0xc00159c840, 0xc0012e4b80, 0xc0012e4b00, 0x0, 0x0, 0x0, 0xc00116bec0, 0x1, 0x1, 0x0, ...)\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/store/tikv/2pc.go:1365 +0x88\ngithub.com/pingcap/tidb/store/tikv.(*tikvTxn).LockKeys(0xc00105bdc0, 0x38ac040, 0xc0019033b0, 0xc0012e4b00, 0xc00116bea0, 0x1, 0x1, 0x0, 0x0)\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/store/tikv/txn.go:480 +0x601\ngithub.com/pingcap/tidb/executor.doLockKeys(0x38ac040, 0xc001903020, 0x38f2b60, 0xc00116cfc0, 0xc0012e4b00, 0xc00116bea0, 0x1, 0x1, 0x11af8db, 0xc0012d4038)\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/executor.go:990 +0x191\ngithub.com/pingcap/tidb/executor.(*PointGetExecutor).lockKeyIfNeeded(0xc00159c6e0, 0x38ac040, 0xc001903020, 0x0, 0x0, 0x0, 0x0, 0x0)\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/point_get.go:279 +0x17a\ngithub.com/pingcap/tidb/executor.(*PointGetExecutor).Next(0xc00159c6e0, 0x38ac040, 0xc001903020, 0xc0015371d0, 0x11b3368, 0x70)\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/point_get.go:189 +0x802\ngithub.com/pingcap/tidb/executor.Next(0x38ac040, 0xc001903020, 0x38b6100, 0xc00159c6e0, 0xc0015371d0, 0x0, 0x0)\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/executor.go:262 +0x225\ngithub.com/pingcap/tidb/executor.(*UpdateExec).updateRows(0xc00133afc0, 0x38ac040, 0xc001903020, 0x0, 0x0, 0x0)\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/update.go:162 +0x57a\ngithub.com/pingcap/tidb/executor.(*UpdateExec).Next(0xc00133afc0, 0x38ac040, 0xc001903020, 0xc001537180, 0x48, 0x31344c0)\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/update.go:130 +0x6c\ngithub.com/pingcap/tidb/executor.Next(0x38ac040, 0xc001903020, 0x38b6940, 0xc00133afc0, 0xc001537180, 0x0, 0x0)\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/executor.go:262 +0x225\ngithub.com/pingcap/tidb/executor.(*ExecStmt).handleNoDelayExecutor(0xc001507ad0, 0x38ac040,"]

### Scenario 1
 * Instruction #0:
     - Instruction:  update t set v = 100 where k = -200;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows: 0

 * Container logs:
   > [2024/07/24 12:37:32.309 +00:00] [INFO] [session.go:2288] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=58] [cur_db=] [sql="drop database if exists testdb;"] [user=root@10.88.0.81]
   > [2024/07/24 12:37:32.310 +00:00] [INFO] [ddl_worker.go:262] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:77, Type:drop schema, State:none, SchemaState:none, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:32.309 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 12:37:32.310 +00:00] [INFO] [ddl.go:537] ["[ddl] start DDL job"] [job="ID:77, Type:drop schema, State:none, SchemaState:none, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:32.309 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/24 12:37:32.311 +00:00] [INFO] [ddl_worker.go:596] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:none, SchemaState:none, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:32.309 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:32.312 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [usedSchemaVersion=58] [neededSchemaVersion=59] ["start time"=68.794µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:37:32.314 +00:00] [INFO] [ddl_worker.go:790] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=59] ["take time"=2.146105ms] [job="ID:77, Type:drop schema, State:running, SchemaState:write only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:32.309 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:32.315 +00:00] [INFO] [ddl_worker.go:596] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:running, SchemaState:write only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:32.309 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:32.317 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [usedSchemaVersion=59] [neededSchemaVersion=60] ["start time"=110.699µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:37:32.319 +00:00] [INFO] [ddl_worker.go:790] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=60] ["take time"=2.171666ms] [job="ID:77, Type:drop schema, State:running, SchemaState:delete only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:32.309 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:32.319 +00:00] [INFO] [ddl_worker.go:596] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:running, SchemaState:delete only, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:32.309 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:32.321 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [usedSchemaVersion=60] [neededSchemaVersion=61] ["start time"=72.846µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:37:32.323 +00:00] [INFO] [ddl_worker.go:790] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=61] ["take time"=2.175019ms] [job="ID:77, Type:drop schema, State:done, SchemaState:none, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:32.309 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:32.323 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=77] [jobType="drop schema"]
   > [2024/07/24 12:37:32.324 +00:00] [INFO] [ddl_worker.go:368] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:drop schema, State:synced, SchemaState:none, SchemaID:72, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:32.309 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:32.325 +00:00] [INFO] [ddl.go:573] ["[ddl] DDL job is finished"] [jobID=77]
   > [2024/07/24 12:37:32.325 +00:00] [INFO] [domain.go:635] ["performing DDL change, must reload"]
   > [2024/07/24 12:37:32.326 +00:00] [INFO] [session.go:2288] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=61] [cur_db=] [sql="create database testdb;"] [user=root@10.88.0.81]
   > [2024/07/24 12:37:32.327 +00:00] [INFO] [ddl_worker.go:262] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:79, Type:create schema, State:none, SchemaState:none, SchemaID:78, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:37:32.326 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 12:37:32.327 +00:00] [INFO] [ddl.go:537] ["[ddl] start DDL job"] [job="ID:79, Type:create schema, State:none, SchemaState:none, SchemaID:78, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:37:32.326 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/24 12:37:32.328 +00:00] [INFO] [ddl_worker.go:596] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:79, Type:create schema, State:none, SchemaState:none, SchemaID:78, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:32.326 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:32.329 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [usedSchemaVersion=61] [neededSchemaVersion=62] ["start time"=158.542µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/24 12:37:32.331 +00:00] [INFO] [ddl_worker.go:790] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=62] ["take time"=2.178301ms] [job="ID:79, Type:create schema, State:done, SchemaState:public, SchemaID:78, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-24 12:37:32.326 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:32.333 +00:00] [INFO] [ddl_worker.go:368] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:79, Type:create schema, State:synced, SchemaState:public, SchemaID:78, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:32.326 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:32.335 +00:00] [INFO] [ddl.go:573] ["[ddl] DDL job is finished"] [jobID=79]
   > [2024/07/24 12:37:32.335 +00:00] [INFO] [domain.go:635] ["performing DDL change, must reload"]
   > [2024/07/24 12:37:32.337 +00:00] [INFO] [session.go:2288] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=62] [cur_db=testdb] [sql="create table t(k tinyint, v int, unique key(k));"] [user=root@10.88.0.81]
   > [2024/07/24 12:37:32.339 +00:00] [INFO] [ddl_worker.go:262] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:81, Type:create table, State:none, SchemaState:none, SchemaID:78, TableID:80, RowCount:0, ArgLen:1, start time: 2024-07-24 12:37:32.338 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/24 12:37:32.339 +00:00] [INFO] [ddl.go:537] ["[ddl] start DDL job"] [job="ID:81, Type:create table, State:none, SchemaState:none, SchemaID:78, TableID:80, RowCount:0, ArgLen:1, start time: 2024-07-24 12:37:32.338 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t(k tinyint, v int, unique key(k));"]
   > [2024/07/24 12:37:32.339 +00:00] [INFO] [ddl_worker.go:596] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:81, Type:create table, State:none, SchemaState:none, SchemaID:78, TableID:80, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:32.338 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:32.340 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [usedSchemaVersion=62] [neededSchemaVersion=63] ["start time"=229.92µs] [phyTblIDs="[80]"] [actionTypes="[8]"]
   > [2024/07/24 12:37:32.342 +00:00] [INFO] [ddl_worker.go:790] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=63] ["take time"=2.128574ms] [job="ID:81, Type:create table, State:done, SchemaState:public, SchemaID:78, TableID:80, RowCount:0, ArgLen:1, start time: 2024-07-24 12:37:32.338 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:32.344 +00:00] [INFO] [ddl_worker.go:368] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:81, Type:create table, State:synced, SchemaState:public, SchemaID:78, TableID:80, RowCount:0, ArgLen:0, start time: 2024-07-24 12:37:32.338 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/24 12:37:32.345 +00:00] [INFO] [ddl.go:573] ["[ddl] DDL job is finished"] [jobID=81]
   > [2024/07/24 12:37:32.346 +00:00] [INFO] [domain.go:635] ["performing DDL change, must reload"]
   > [2024/07/24 12:37:32.346 +00:00] [INFO] [split_region.go:60] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=54] ["first split key"=748000000000000050]
   > [2024/07/24 12:37:32.346 +00:00] [INFO] [split_region.go:157] ["batch split regions complete"] ["batch region ID"=54] ["first at"=748000000000000050] ["first new region left"="{Id:54 StartKey:7480000000000000ff4a00000000000000f8 EndKey: RegionEpoch:{ConfVer:0 Version:1} Peers:[id:55 store_id:1 ]}"] ["new region count"=1]
   > [2024/07/24 12:37:32.346 +00:00] [INFO] [split_region.go:209] ["split regions complete"] ["region count"=1] ["region IDs"="[54]"]
