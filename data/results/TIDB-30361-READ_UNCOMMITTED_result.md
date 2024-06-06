# Bug ID TIDB-30361-READ_UNCOMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/30361
Original isolation level: REPEATABLE READ
Tested isolation level:   READ UNCOMMITTED


## Details
 * Database: tidb-5.2.1
 * Number of scenarios: 1
 * Initial setup script: /home/theodor/Projects/MasterThesis/data/sql/TIDB-30361_mysql_bk.sql

## Results
### Scenario 0
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
     - TID: 0
     - Output: Error: 8048 (HY000): The isolation level 'READ-UNCOMMITTED' is not supported. Set tidb_skip_isolation_level_check=1 to skip this error
 * Instruction #1:
     - SQL:  start transaction;
     - TID: 0
     - Output: Skipped due to previous error.
 * Instruction #2:
     - SQL:  start transaction;
     - TID: 1
     - Output: Skipped due to previous error.
 * Instruction #3:
     - SQL:  select ref_14.c_qpjzzd as c1 from t_q_zw9c as ref_14 order by c1 desc;
     - TID: 0
     - Output: Skipped due to previous error.
 * Instruction #4:
     - SQL:  delete from t_q_zw9c;
     - TID: 0
     - Output: Skipped due to previous error.
 * Instruction #5:
     - SQL:  commit;
     - TID: 0
     - Output: Skipped due to previous error.
 * Instruction #6:
     - SQL:  select ref_14.c_qpjzzd as c1 from t_q_zw9c as ref_14;
     - TID: 1
     - Output: Skipped due to previous error.
 * Instruction #7:
     - SQL:  commit;
     - TID: 1
     - Output: Skipped due to previous error.

 * Container logs:
   > [2024/06/06 13:22:01.078 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=13] [schemaVersion=28] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/06/06 13:22:01.079 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:57, Type:drop schema, State:none, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-06 13:22:01.078 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/06 13:22:01.079 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:57, Type:drop schema, State:none, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-06 13:22:01.078 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/06/06 13:22:01.079 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:57, Type:drop schema, State:none, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-06 13:22:01.078 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/06 13:22:01.080 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=28] [neededSchemaVersion=29] ["start time"=121.036µs] [phyTblIDs="[55]"] [actionTypes="[4]"]
   > [2024/06/06 13:22:01.082 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=29] ["take time"=2.202817ms] [job="ID:57, Type:drop schema, State:running, SchemaState:write only, SchemaID:53, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-06 13:22:01.078 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/06 13:22:01.083 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:57, Type:drop schema, State:running, SchemaState:write only, SchemaID:53, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-06 13:22:01.078 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/06 13:22:01.083 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=29] [neededSchemaVersion=30] ["start time"=93.029µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/06 13:22:01.085 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=30] ["take time"=2.190385ms] [job="ID:57, Type:drop schema, State:running, SchemaState:delete only, SchemaID:53, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-06 13:22:01.078 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/06 13:22:01.086 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:57, Type:drop schema, State:running, SchemaState:delete only, SchemaID:53, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-06 13:22:01.078 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/06 13:22:01.087 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=30] [neededSchemaVersion=31] ["start time"=66.14µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/06 13:22:01.089 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=31] ["take time"=2.156372ms] [job="ID:57, Type:drop schema, State:done, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-06 13:22:01.078 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/06 13:22:01.089 +00:00] [INFO] [delete_range.go:439] ["[ddl] batch insert into delete-range table"] [jobID=57] [elementIDs="[55]"]
   > [2024/06/06 13:22:01.091 +00:00] [INFO] [delete_range.go:106] ["[ddl] add job into delete-range table"] [jobID=57] [jobType="drop schema"]
   > [2024/06/06 13:22:01.091 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:57, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-06 13:22:01.078 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/06 13:22:01.092 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=57]
   > [2024/06/06 13:22:01.092 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/06 13:22:01.093 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=13] [schemaVersion=31] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/06/06 13:22:01.094 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:59, Type:create schema, State:none, SchemaState:queueing, SchemaID:58, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-06 13:22:01.093 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/06 13:22:01.094 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:59, Type:create schema, State:none, SchemaState:queueing, SchemaID:58, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-06 13:22:01.093 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/06 13:22:01.095 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:59, Type:create schema, State:none, SchemaState:queueing, SchemaID:58, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-06 13:22:01.093 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/06 13:22:01.096 +00:00] [INFO] [delete_range.go:236] ["[ddl] delRange emulator complete task"] [jobID=57] [elementID=55]
   > [2024/06/06 13:22:01.096 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=31] [neededSchemaVersion=32] ["start time"=156.795µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/06 13:22:01.098 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=32] ["take time"=2.171877ms] [job="ID:59, Type:create schema, State:done, SchemaState:public, SchemaID:58, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-06 13:22:01.093 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/06 13:22:01.098 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:59, Type:create schema, State:synced, SchemaState:public, SchemaID:58, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-06 13:22:01.093 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/06 13:22:01.098 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=59]
   > [2024/06/06 13:22:01.099 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/06 13:22:01.102 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=13] [schemaVersion=32] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_q_zw9c`\n--\n\nDROP TABLE IF EXISTS `t_q_zw9c`;"] [user=root@127.0.0.1]
   > [2024/06/06 13:22:01.102 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=13] [schemaVersion=32] [cur_db=testdb] [sql="CREATE TABLE `t_q_zw9c` (\n  `c_qpjzzd` int(11) NOT NULL,\n  `c_1mp0eb` int(11) DEFAULT NULL,\n  `c_3dcuc` double DEFAULT NULL,\n  PRIMARY KEY (`c_qpjzzd`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/06/06 13:22:01.103 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:61, Type:create table, State:none, SchemaState:queueing, SchemaID:58, TableID:60, RowCount:0, ArgLen:1, start time: 2024-06-06 13:22:01.103 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/06 13:22:01.103 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:61, Type:create table, State:none, SchemaState:queueing, SchemaID:58, TableID:60, RowCount:0, ArgLen:1, start time: 2024-06-06 13:22:01.103 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_q_zw9c` (\n  `c_qpjzzd` int(11) NOT NULL,\n  `c_1mp0eb` int(11) DEFAULT NULL,\n  `c_3dcuc` double DEFAULT NULL,\n  PRIMARY KEY (`c_qpjzzd`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/06 13:22:01.103 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:61, Type:create table, State:none, SchemaState:queueing, SchemaID:58, TableID:60, RowCount:0, ArgLen:0, start time: 2024-06-06 13:22:01.103 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/06 13:22:01.104 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=32] [neededSchemaVersion=33] ["start time"=144.433µs] [phyTblIDs="[60]"] [actionTypes="[8]"]
   > [2024/06/06 13:22:01.106 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=33] ["take time"=2.244233ms] [job="ID:61, Type:create table, State:done, SchemaState:public, SchemaID:58, TableID:60, RowCount:0, ArgLen:1, start time: 2024-06-06 13:22:01.103 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/06 13:22:01.106 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:61, Type:create table, State:synced, SchemaState:public, SchemaID:58, TableID:60, RowCount:0, ArgLen:0, start time: 2024-06-06 13:22:01.103 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/06 13:22:01.107 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=61]
   > [2024/06/06 13:22:01.107 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/06 13:22:01.107 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=52] ["first split key"=74800000000000003c]
   > [2024/06/06 13:22:01.107 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=52] ["first at"=74800000000000003c] ["first new region left"="{Id:52 StartKey:7480000000000000ff3700000000000000f8 EndKey:7480000000000000ff3c00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:53 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/06 13:22:01.107 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[52]"]
   > [2024/06/06 13:22:01.107 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=13] [schemaVersion=33] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_q_zw9c` DISABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/06/06 13:22:01.108 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=13] [schemaVersion=33] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_q_zw9c` ENABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/06/06 13:22:02.352 +00:00] [INFO] [tidb.go:242] ["rollbackTxn called due to ddl/autocommit failure"]
   > [2024/06/06 13:22:02.352 +00:00] [WARN] [session.go:1683] ["run statement failed"] [conn=15] [schemaVersion=33] [error="[variable:8048]The isolation level 'READ-UNCOMMITTED' is not supported. Set tidb_skip_isolation_level_check=1 to skip this error"] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 15,\n  \"status\": 2,\n  \"strictMode\": true,\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"127.0.0.1\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/06/06 13:22:02.352 +00:00] [INFO] [conn.go:995] ["command dispatched failed"] [conn=15] [connInfo="id:15, addr:127.0.0.1:44442 status:10, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:0, autocommit:1"] [sql=" SET GLOBAL TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;"] [txn_mode=OPTIMISTIC] [err="[variable:8048]The isolation level 'READ-UNCOMMITTED' is not supported. Set tidb_skip_isolation_level_check=1 to skip this error\ngithub.com/pingcap/errors.AddStack\n\t/nfs/cache/mod/github.com/pingcap/errors@v0.11.5-0.20210425183316-da1aaba5fb63/errors.go:174\ngithub.com/pingcap/errors.(*Error).GenWithStackByArgs\n\t/nfs/cache/mod/github.com/pingcap/errors@v0.11.5-0.20210425183316-da1aaba5fb63/normalize.go:159\ngithub.com/pingcap/tidb/sessionctx/variable.checkIsolationLevel\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/sessionctx/variable/varsutil.go:155\ngithub.com/pingcap/tidb/sessionctx/variable.glob..func23\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/sessionctx/variable/sysvar.go:716\ngithub.com/pingcap/tidb/sessionctx/variable.(*SysVar).Validate\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/sessionctx/variable/sysvar.go:256\ngithub.com/pingcap/tidb/session.(*session).SetGlobalSysVar\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/session/session.go:1158\ngithub.com/pingcap/tidb/executor.(*SetExecutor).setSysVariable\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/set.go:116\ngithub.com/pingcap/tidb/executor.(*SetExecutor).Next\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/set.go:98\ngithub.com/pingcap/tidb/executor.Next\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/executor.go:285\ngithub.com/pingcap/tidb/executor.(*ExecStmt).handleNoDelayExecutor\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/adapter.go:590\ngithub.com/pingcap/tidb/executor.(*ExecStmt).handleNoDelay\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/adapter.go:471\ngithub.com/pingcap/tidb/executor.(*ExecStmt).Exec\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/adapter.go:420\ngithub.com/pingcap/tidb/session.runStmt\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/session/session.go:1786\ngithub.com/pingcap/tidb/session.(*session).ExecuteStmt\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/session/session.go:1680\ngithub.com/pingcap/tidb/server.(*TiDBContext).ExecuteStmt\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/driver_tidb.go:218\ngithub.com/pingcap/tidb/server.(*clientConn).handleStmt\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/conn.go:1818\ngithub.com/pingcap/tidb/server.(*clientConn).handleQuery\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/conn.go:1690\ngithub.com/pingcap/tidb/server.(*clientConn).dispatch\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/conn.go:1215\ngithub.com/pingcap/tidb/server.(*clientConn).Run\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/conn.go:978\ngithub.com/pingcap/tidb/server.(*Server).onConn\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/server.go:501\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1371"]
