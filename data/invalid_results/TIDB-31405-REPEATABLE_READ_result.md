# Bug ID TIDB-31405-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/31405
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              Error on the first scenario


## Details
 * Database: tidb-v5.3.0
 * Number of scenarios: 1
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  INSERT INTO t0 VALUES(1.0);
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 1 / 0
 * Instruction #1:
     - Instruction:  UPDATE t0 SET c0 = c0 + 1 WHERE c0 > 'a';
     - Transaction: conn_0
     - Output: ERROR: 1105 (HY000): Bad Number
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0

 * Container logs:
   > [2024/07/04 10:55:17.121 +00:00] [INFO] [session.go:2834] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=27] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/07/04 10:55:17.122 +00:00] [INFO] [session.go:2834] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=27] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/07/04 10:55:17.123 +00:00] [INFO] [ddl_worker.go:319] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:56, Type:create schema, State:none, SchemaState:queueing, SchemaID:55, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-04 10:55:17.123 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/04 10:55:17.123 +00:00] [INFO] [ddl.go:549] ["[ddl] start DDL job"] [job="ID:56, Type:create schema, State:none, SchemaState:queueing, SchemaID:55, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-04 10:55:17.123 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/04 10:55:17.123 +00:00] [INFO] [ddl_worker.go:728] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:56, Type:create schema, State:none, SchemaState:queueing, SchemaID:55, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-04 10:55:17.123 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 10:55:17.124 +00:00] [INFO] [domain.go:130] ["diff load InfoSchema success"] [currentSchemaVersion=27] [neededSchemaVersion=28] ["start time"=70.75µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/04 10:55:17.126 +00:00] [INFO] [ddl_worker.go:919] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=28] ["take time"=2.198348ms] [job="ID:56, Type:create schema, State:done, SchemaState:public, SchemaID:55, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-04 10:55:17.123 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 10:55:17.126 +00:00] [INFO] [ddl_worker.go:424] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:56, Type:create schema, State:synced, SchemaState:public, SchemaID:55, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-04 10:55:17.123 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 10:55:17.127 +00:00] [INFO] [ddl.go:604] ["[ddl] DDL job is finished"] [jobID=56]
   > [2024/07/04 10:55:17.127 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/04 10:55:17.130 +00:00] [INFO] [session.go:2834] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=28] [cur_db=testdb] [sql="DROP TABLE IF EXISTS t0;"] [user=root@127.0.0.1]
   > [2024/07/04 10:55:17.130 +00:00] [INFO] [session.go:2834] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=28] [cur_db=testdb] [sql="CREATE TABLE t0(c0 DECIMAL);"] [user=root@127.0.0.1]
   > [2024/07/04 10:55:17.132 +00:00] [INFO] [ddl_worker.go:319] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:58, Type:create table, State:none, SchemaState:queueing, SchemaID:55, TableID:57, RowCount:0, ArgLen:1, start time: 2024-07-04 10:55:17.131 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/04 10:55:17.132 +00:00] [INFO] [ddl.go:549] ["[ddl] start DDL job"] [job="ID:58, Type:create table, State:none, SchemaState:queueing, SchemaID:55, TableID:57, RowCount:0, ArgLen:1, start time: 2024-07-04 10:55:17.131 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE t0(c0 DECIMAL);"]
   > [2024/07/04 10:55:17.132 +00:00] [INFO] [ddl_worker.go:728] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:58, Type:create table, State:none, SchemaState:queueing, SchemaID:55, TableID:57, RowCount:0, ArgLen:0, start time: 2024-07-04 10:55:17.131 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 10:55:17.134 +00:00] [INFO] [domain.go:130] ["diff load InfoSchema success"] [currentSchemaVersion=28] [neededSchemaVersion=29] ["start time"=243.888µs] [phyTblIDs="[57]"] [actionTypes="[8]"]
   > [2024/07/04 10:55:17.136 +00:00] [INFO] [ddl_worker.go:919] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=29] ["take time"=2.059921ms] [job="ID:58, Type:create table, State:done, SchemaState:public, SchemaID:55, TableID:57, RowCount:0, ArgLen:1, start time: 2024-07-04 10:55:17.131 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 10:55:17.136 +00:00] [INFO] [ddl_worker.go:424] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:58, Type:create table, State:synced, SchemaState:public, SchemaID:55, TableID:57, RowCount:0, ArgLen:0, start time: 2024-07-04 10:55:17.131 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/04 10:55:17.137 +00:00] [INFO] [ddl.go:604] ["[ddl] DDL job is finished"] [jobID=58]
   > [2024/07/04 10:55:17.137 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/04 10:55:17.137 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=52] ["first split key"=748000000000000039]
   > [2024/07/04 10:55:17.137 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=52] ["first at"=748000000000000039] ["first new region left"="{Id:52 StartKey:7480000000000000ff3500000000000000f8 EndKey:7480000000000000ff3900000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:53 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/04 10:55:17.137 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[52]"]
   > [2024/07/04 10:55:18.271 +00:00] [WARN] [2pc.go:1601] ["schemaLeaseChecker is not set for this transaction"] [sessionID=7] [startTS=450911408821633025] [commitTS=450911408821633026]
   > [2024/07/04 10:55:18.492 +00:00] [INFO] [tidb.go:243] ["rollbackTxn called due to ddl/autocommit failure"]
   > [2024/07/04 10:55:18.492 +00:00] [WARN] [session.go:1571] ["run statement failed"] [conn=7] [schemaVersion=29] [error="[tikv:8029]Bad Number"] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 7,\n  \"status\": 2,\n  \"strictMode\": true,\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"127.0.0.1\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/07/04 10:55:18.492 +00:00] [INFO] [conn.go:997] ["command dispatched failed"] [conn=7] [connInfo="id:7, addr:127.0.0.1:60466 status:10, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:0, autocommit:1"] [sql=" UPDATE t0 SET c0 = c0 + 1 WHERE c0 > 'a';"] [txn_mode=OPTIMISTIC] [err="[tikv:8029]Bad Number"]
