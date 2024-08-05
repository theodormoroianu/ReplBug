# Bug ID TIDB-25176-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/25176
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              Setting tidb_snapshot breaks the isolation guarantees.


## Details
 * Database: tidb-v4.0.7.tikv
 * Number of scenarios: 1
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;
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
     - Affected rows: 0
 * Instruction #3:
     - Instruction:  set @@tidb_snapshot=TIMESTAMP(NOW());
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows: 0
 * Instruction #4:
     - Instruction:  select a from test.ttt where id=1;
     - Transaction: conn_0
     - Output: [(2,)]
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
   > [2024/08/05 07:08:32.162 +00:00] [INFO] [server.go:397] ["connection closed"] [conn=6]
   > [2024/08/05 07:08:32.167 +00:00] [INFO] [server.go:394] ["new connection"] [conn=7] [remoteAddr=127.0.0.1:44866]
   > [2024/08/05 07:08:32.171 +00:00] [INFO] [session.go:2159] ["CRUCIAL OPERATION"] [conn=7] [schemaVersion=32] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/08/05 07:08:32.185 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:55, Type:drop schema, State:none, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-05 07:08:32.159 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/05 07:08:32.185 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:55, Type:drop schema, State:none, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-05 07:08:32.159 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/08/05 07:08:32.189 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:55, Type:drop schema, State:none, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-05 07:08:32.159 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/05 07:08:32.205 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=32] [neededSchemaVersion=33] ["start time"=571.029µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/05 07:08:32.254 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=33] ["take time"=52.029951ms] [job="ID:55, Type:drop schema, State:running, SchemaState:write only, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-05 07:08:32.159 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/05 07:08:32.256 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:55, Type:drop schema, State:running, SchemaState:write only, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-05 07:08:32.159 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/05 07:08:32.285 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=33] [neededSchemaVersion=34] ["start time"=749.895µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/05 07:08:32.334 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=34] ["take time"=62.492234ms] [job="ID:55, Type:drop schema, State:running, SchemaState:delete only, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-05 07:08:32.159 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/05 07:08:32.337 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:55, Type:drop schema, State:running, SchemaState:delete only, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-05 07:08:32.159 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/05 07:08:32.356 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=34] [neededSchemaVersion=35] ["start time"=623.83µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/05 07:08:32.406 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=35] ["take time"=52.124726ms] [job="ID:55, Type:drop schema, State:done, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-05 07:08:32.159 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/05 07:08:32.408 +00:00] [INFO] [delete_range.go:105] ["[ddl] add job into delete-range table"] [jobID=55] [jobType="drop schema"]
   > [2024/08/05 07:08:32.410 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:55, Type:drop schema, State:synced, SchemaState:none, SchemaID:50, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-05 07:08:32.159 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/05 07:08:32.424 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=55]
   > [2024/08/05 07:08:32.424 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/08/05 07:08:32.426 +00:00] [INFO] [session.go:2159] ["CRUCIAL OPERATION"] [conn=7] [schemaVersion=35] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/08/05 07:08:32.454 +00:00] [INFO] [ddl_worker.go:261] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:57, Type:create schema, State:none, SchemaState:none, SchemaID:56, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-05 07:08:32.409 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/05 07:08:32.454 +00:00] [INFO] [ddl.go:487] ["[ddl] start DDL job"] [job="ID:57, Type:create schema, State:none, SchemaState:none, SchemaID:56, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-05 07:08:32.409 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/08/05 07:08:32.458 +00:00] [INFO] [ddl_worker.go:588] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:57, Type:create schema, State:none, SchemaState:none, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-05 07:08:32.409 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/05 07:08:32.484 +00:00] [INFO] [domain.go:127] ["diff load InfoSchema success"] [usedSchemaVersion=35] [neededSchemaVersion=36] ["start time"=1.710992ms] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/05 07:08:32.532 +00:00] [INFO] [ddl_worker.go:777] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=36] ["take time"=52.106358ms] [job="ID:57, Type:create schema, State:done, SchemaState:public, SchemaID:56, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-05 07:08:32.409 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/05 07:08:32.536 +00:00] [INFO] [ddl_worker.go:367] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:57, Type:create schema, State:synced, SchemaState:public, SchemaID:56, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-05 07:08:32.409 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/05 07:08:32.550 +00:00] [INFO] [ddl.go:519] ["[ddl] DDL job is finished"] [jobID=57]
   > [2024/08/05 07:08:32.550 +00:00] [INFO] [domain.go:632] ["performing DDL change, must reload"]
   > [2024/08/05 07:08:32.554 +00:00] [INFO] [session.go:2159] ["CRUCIAL OPERATION"] [conn=7] [schemaVersion=36] [cur_db=testdb] [sql="create table test.ttt (id int primary key, a int);"] [user=root@127.0.0.1]
   > [2024/08/05 07:08:32.554 +00:00] [INFO] [tidb.go:218] ["rollbackTxn for ddl/autocommit failed"]
   > [2024/08/05 07:08:32.554 +00:00] [WARN] [session.go:1064] ["run statement failed"] [conn=7] [schemaVersion=36] [error="[schema:1050]Table 'test.ttt' already exists"] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 7,\n  \"status\": 2,\n  \"strictMode\": true,\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"127.0.0.1\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/08/05 07:08:32.554 +00:00] [INFO] [conn.go:780] ["command dispatched failed"] [conn=7] [connInfo="id:7, addr:127.0.0.1:44866 status:10, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:0, autocommit:1"] [sql="\ncreate table test.ttt (id int primary key, a int);\ninsert into test.ttt values (1, 1);\n"] [txn_mode=PESSIMISTIC] [err="[schema:1050]Table 'test.ttt' already exists\ngithub.com/pingcap/errors.AddStack\n\t/home/jenkins/agent/workspace/tidb_v4.0.7/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.20200917111840-a15ef68f753d/errors.go:174\ngithub.com/pingcap/errors.(*Error).GenWithStackByArgs\n\t/home/jenkins/agent/workspace/tidb_v4.0.7/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.20200917111840-a15ef68f753d/terror_error.go:204\ngithub.com/pingcap/tidb/ddl.(*ddl).CreateTableWithInfo\n\t/home/jenkins/agent/workspace/tidb_v4.0.7/go/src/github.com/pingcap/tidb/ddl/ddl_api.go:1524\ngithub.com/pingcap/tidb/ddl.(*ddl).CreateTable\n\t/home/jenkins/agent/workspace/tidb_v4.0.7/go/src/github.com/pingcap/tidb/ddl/ddl_api.go:1506\ngithub.com/pingcap/tidb/executor.(*DDLExec).executeCreateTable\n\t/home/jenkins/agent/workspace/tidb_v4.0.7/go/src/github.com/pingcap/tidb/executor/ddl.go:195\ngithub.com/pingcap/tidb/executor.(*DDLExec).Next\n\t/home/jenkins/agent/workspace/tidb_v4.0.7/go/src/github.com/pingcap/tidb/executor/ddl.go:92\ngithub.com/pingcap/tidb/executor.Next\n\t/home/jenkins/agent/workspace/tidb_v4.0.7/go/src/github.com/pingcap/tidb/executor/executor.go:253\ngithub.com/pingcap/tidb/executor.(*ExecStmt).handleNoDelayExecutor\n\t/home/jenkins/agent/workspace/tidb_v4.0.7/go/src/github.com/pingcap/tidb/executor/adapter.go:514\ngithub.com/pingcap/tidb/executor.(*ExecStmt).handleNoDelay\n\t/home/jenkins/agent/workspace/tidb_v4.0.7/go/src/github.com/pingcap/tidb/executor/adapter.go:396\ngithub.com/pingcap/tidb/executor.(*ExecStmt).Exec\n\t/home/jenkins/agent/workspace/tidb_v4.0.7/go/src/github.com/pingcap/tidb/executor/adapter.go:352\ngithub.com/pingcap/tidb/session.runStmt\n\t/home/jenkins/agent/workspace/tidb_v4.0.7/go/src/github.com/pingcap/tidb/session/tidb.go:286\ngithub.com/pingcap/tidb/session.(*session).executeStatement\n\t/home/jenkins/agent/workspace/tidb_v4.0.7/go/src/github.com/pingcap/tidb/session/session.go:1061\ngithub.com/pingcap/tidb/session.(*session).execute\n\t/home/jenkins/agent/workspace/tidb_v4.0.7/go/src/github.com/pingcap/tidb/session/session.go:1173\ngithub.com/pingcap/tidb/session.(*session).Execute\n\t/home/jenkins/agent/workspace/tidb_v4.0.7/go/src/github.com/pingcap/tidb/session/session.go:1104\ngithub.com/pingcap/tidb/server.(*TiDBContext).Execute\n\t/home/jenkins/agent/workspace/tidb_v4.0.7/go/src/github.com/pingcap/tidb/server/driver_tidb.go:248\ngithub.com/pingcap/tidb/server.(*clientConn).handleQuery\n\t/home/jenkins/agent/workspace/tidb_v4.0.7/go/src/github.com/pingcap/tidb/server/conn.go:1335\ngithub.com/pingcap/tidb/server.(*clientConn).dispatch\n\t/home/jenkins/agent/workspace/tidb_v4.0.7/go/src/github.com/pingcap/tidb/server/conn.go:966\ngithub.com/pingcap/tidb/server.(*clientConn).Run\n\t/home/jenkins/agent/workspace/tidb_v4.0.7/go/src/github.com/pingcap/tidb/server/conn.go:765\ngithub.com/pingcap/tidb/server.(*Server).onConn\n\t/home/jenkins/agent/workspace/tidb_v4.0.7/go/src/github.com/pingcap/tidb/server/server.go:421\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1357"]
   > [2024/08/05 07:08:32.555 +00:00] [INFO] [server.go:397] ["connection closed"] [conn=7]
   > [2024/08/05 07:08:33.566 +00:00] [INFO] [server.go:394] ["new connection"] [conn=8] [remoteAddr=127.0.0.1:44872]
   > [2024/08/05 07:08:33.574 +00:00] [INFO] [set.go:216] ["set session var"] [conn=8] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/08/05 07:08:33.575 +00:00] [INFO] [set.go:216] ["set session var"] [conn=8] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/08/05 07:08:33.575 +00:00] [INFO] [set.go:216] ["set session var"] [conn=8] [name=transaction_isolation] [val=READ-COMMITTED]
   > [2024/08/05 07:08:34.179 +00:00] [INFO] [server.go:394] ["new connection"] [conn=9] [remoteAddr=127.0.0.1:44882]
   > [2024/08/05 07:08:34.182 +00:00] [INFO] [set.go:216] ["set session var"] [conn=9] [name=innodb_lock_wait_timeout] [val=3]
   > [2024/08/05 07:08:34.480 +00:00] [INFO] [set.go:317] ["load snapshot info schema"] [conn=8] [SnapshotTS=451632618274816000]
   > [2024/08/05 07:08:34.491 +00:00] [INFO] [domain.go:146] ["full load InfoSchema success"] [usedSchemaVersion=0] [neededSchemaVersion=36] ["start time"=9.962143ms]
   > [2024/08/05 07:08:34.492 +00:00] [INFO] [set.go:216] ["set session var"] [conn=8] [name=tidb_snapshot] [val="2024-08-05 07:08:34"]
   > [2024/08/05 07:08:34.778 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=8] [schemaVersion=36]
   > [2024/08/05 07:08:35.079 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=8] [schemaVersion=36]
   > [2024/08/05 07:08:35.379 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=8] [schemaVersion=36]
   > [2024/08/05 07:08:35.680 +00:00] [INFO] [infoschema.go:387] ["use snapshot schema"] [conn=8] [schemaVersion=36]
   > [2024/08/05 07:08:36.080 +00:00] [INFO] [server.go:397] ["connection closed"] [conn=8]
   > [2024/08/05 07:08:36.081 +00:00] [INFO] [server.go:397] ["connection closed"] [conn=9]
