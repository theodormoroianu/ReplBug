# Bug ID TIDB-30410-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/30410
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              Lazy constraint check causes data inconsistency.


## Details
 * Database: tidb-v5.2.1
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
     - Instruction:  set tidb_constraint_check_in_place=0;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows: 0
 * Instruction #2:
     - Instruction:  begin optimistic;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows: 0
 * Instruction #3:
     - Instruction:  insert into t (c0, c1, c2) values (1, 'red', 'white');
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows: 1
 * Instruction #4:
     - Instruction:  delete from t where c1 is null;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows: 1
 * Instruction #5:
     - Instruction:  update t set c2 = 'green' where c2 between 'purple' and 'white';
     - Transaction: conn_0
     - Output: None
     - Executed order: 5
     - Affected rows: 1
 * Instruction #6:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: None
     - Executed order: 6
     - Affected rows: 0
 * Instruction #7:
     - Instruction:  admin check table t;
     - Transaction: conn_0
     - Output: ERROR: 8133 (HY000): handle 1, index:types.Datum{k:0x1, decimal:0x0, length:0x0, i:1, collation:"", b:[]uint8(nil), x:interface {}(nil)} != record:<nil>
     - Executed order: Not executed
     - Affected rows: -1

 * Container logs:
   > [2024/08/06 16:54:21.421 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=26] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/08/06 16:54:21.422 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=26] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/08/06 16:54:21.423 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:54, Type:create schema, State:none, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-06 16:54:21.423 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/06 16:54:21.423 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:54, Type:create schema, State:none, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-06 16:54:21.423 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/08/06 16:54:21.424 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:54, Type:create schema, State:none, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-06 16:54:21.423 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:54:21.424 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=26] [neededSchemaVersion=27] ["start time"=103.366µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/08/06 16:54:21.426 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=27] ["take time"=2.210234ms] [job="ID:54, Type:create schema, State:done, SchemaState:public, SchemaID:53, TableID:0, RowCount:0, ArgLen:1, start time: 2024-08-06 16:54:21.423 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:54:21.427 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:54, Type:create schema, State:synced, SchemaState:public, SchemaID:53, TableID:0, RowCount:0, ArgLen:0, start time: 2024-08-06 16:54:21.423 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:54:21.427 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=54]
   > [2024/08/06 16:54:21.427 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/08/06 16:54:21.429 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=27] [cur_db=testdb] [sql="drop table if exists t;"] [user=root@127.0.0.1]
   > [2024/08/06 16:54:21.429 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=27] [cur_db=testdb] [sql="create table t (c0 int, c1 varchar(20), c2 varchar(20), unique key(c0), key(c2));"] [user=root@127.0.0.1]
   > [2024/08/06 16:54:21.431 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:56, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:55, RowCount:0, ArgLen:1, start time: 2024-08-06 16:54:21.43 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/08/06 16:54:21.431 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:56, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:55, RowCount:0, ArgLen:1, start time: 2024-08-06 16:54:21.43 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t (c0 int, c1 varchar(20), c2 varchar(20), unique key(c0), key(c2));"]
   > [2024/08/06 16:54:21.431 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:56, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:55, RowCount:0, ArgLen:0, start time: 2024-08-06 16:54:21.43 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:54:21.432 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=27] [neededSchemaVersion=28] ["start time"=321.554µs] [phyTblIDs="[55]"] [actionTypes="[8]"]
   > [2024/08/06 16:54:21.434 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=28] ["take time"=2.043242ms] [job="ID:56, Type:create table, State:done, SchemaState:public, SchemaID:53, TableID:55, RowCount:0, ArgLen:1, start time: 2024-08-06 16:54:21.43 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:54:21.435 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:56, Type:create table, State:synced, SchemaState:public, SchemaID:53, TableID:55, RowCount:0, ArgLen:0, start time: 2024-08-06 16:54:21.43 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/08/06 16:54:21.436 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=56]
   > [2024/08/06 16:54:21.436 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/08/06 16:54:21.436 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=50] ["first split key"=748000000000000037]
   > [2024/08/06 16:54:21.436 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=50] ["first at"=748000000000000037] ["first new region left"="{Id:50 StartKey:7480000000000000ff3300000000000000f8 EndKey:7480000000000000ff3700000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:51 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/08/06 16:54:21.436 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[50]"]
   > [2024/08/06 16:54:21.436 +00:00] [WARN] [2pc.go:1598] ["schemaLeaseChecker is not set for this transaction"] [sessionID=5] [startTS=451664481205878786] [commitTS=451664481205878787]
   > [2024/08/06 16:54:22.507 +00:00] [INFO] [set.go:127] ["set global var"] [conn=7] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/08/06 16:54:24.584 +00:00] [INFO] [session.go:3107] ["use snapshot schema"] [conn=0] [schemaVersion=28]
   > [2024/08/06 16:54:24.584 +00:00] [INFO] [session.go:3107] ["use snapshot schema"] [conn=0] [schemaVersion=28]
   > [2024/08/06 16:54:24.585 +00:00] [INFO] [session.go:3107] ["use snapshot schema"] [conn=0] [schemaVersion=28]
   > [2024/08/06 16:54:24.585 +00:00] [INFO] [session.go:3107] ["use snapshot schema"] [conn=0] [schemaVersion=28]
   > [2024/08/06 16:54:24.585 +00:00] [INFO] [session.go:3107] ["use snapshot schema"] [conn=0] [schemaVersion=28]
   > [2024/08/06 16:54:24.586 +00:00] [INFO] [session.go:3107] ["use snapshot schema"] [conn=0] [schemaVersion=28]
   > [2024/08/06 16:54:24.586 +00:00] [INFO] [admin.go:354] ["check indices count"] [table=t] [cnt=1] [index="\"c0\""] [cnt=1]
   > [2024/08/06 16:54:24.586 +00:00] [INFO] [session.go:3107] ["use snapshot schema"] [conn=0] [schemaVersion=28]
   > [2024/08/06 16:54:24.586 +00:00] [INFO] [session.go:3107] ["use snapshot schema"] [conn=0] [schemaVersion=28]
   > [2024/08/06 16:54:24.587 +00:00] [INFO] [session.go:3107] ["use snapshot schema"] [conn=0] [schemaVersion=28]
   > [2024/08/06 16:54:24.587 +00:00] [INFO] [admin.go:354] ["check indices count"] [table=t] [cnt=1] [index="\"c2\""] [cnt=1]
   > [2024/08/06 16:54:24.588 +00:00] [INFO] [executor.go:780] ["check index handle failed"] [conn=7] [error="[executor:8133]handle 1, index:types.Datum{k:0x1, decimal:0x0, length:0x0, i:1, collation:\"\", b:[]uint8(nil), x:interface {}(nil)} != record:<nil>"]
   > [2024/08/06 16:54:24.589 +00:00] [INFO] [tidb.go:242] ["rollbackTxn called due to ddl/autocommit failure"]
   > [2024/08/06 16:54:24.589 +00:00] [WARN] [session.go:1683] ["run statement failed"] [conn=7] [schemaVersion=28] [error="[executor:8133]handle 1, index:types.Datum{k:0x1, decimal:0x0, length:0x0, i:1, collation:\"\", b:[]uint8(nil), x:interface {}(nil)} != record:<nil>"] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 7,\n  \"status\": 2,\n  \"strictMode\": true,\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"127.0.0.1\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/08/06 16:54:24.589 +00:00] [INFO] [conn.go:995] ["command dispatched failed"] [conn=7] [connInfo="id:7, addr:127.0.0.1:34510 status:10, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:0, autocommit:1"] [sql=" admin check table t;"] [txn_mode=OPTIMISTIC] [err="[executor:8133]handle 1, index:types.Datum{k:0x1, decimal:0x0, length:0x0, i:1, collation:\"\", b:[]uint8(nil), x:interface {}(nil)} != record:<nil>\ngithub.com/pingcap/errors.AddStack\n\t/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.20210425183316-da1aaba5fb63/errors.go:174\ngithub.com/pingcap/errors.(*Error).GenWithStackByArgs\n\t/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.20210425183316-da1aaba5fb63/normalize.go:159\ngithub.com/pingcap/tidb/executor.(*tableWorker).compareData.func1\n\t/go/src/github.com/pingcap/tidb/executor/distsql.go:1130\ngithub.com/pingcap/tidb/kv.(*HandleMap).Range\n\t/go/src/github.com/pingcap/tidb/kv/key.go:404\ngithub.com/pingcap/tidb/executor.(*tableWorker).compareData\n\t/go/src/github.com/pingcap/tidb/executor/distsql.go:1128\ngithub.com/pingcap/tidb/executor.(*tableWorker).executeTask\n\t/go/src/github.com/pingcap/tidb/executor/distsql.go:1189\ngithub.com/pingcap/tidb/executor.(*tableWorker).pickAndExecTask\n\t/go/src/github.com/pingcap/tidb/executor/distsql.go:1004\ngithub.com/pingcap/tidb/executor.(*IndexLookUpExecutor).startTableWorker.func1\n\t/go/src/github.com/pingcap/tidb/executor/distsql.go:633\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1594"]
