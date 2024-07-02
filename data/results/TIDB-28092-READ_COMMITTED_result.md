# Bug ID TIDB-28092-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/28092
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              Should not throw an error.


## Details
 * Database: tidb-v5.2.1
 * Number of scenarios: 2
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
 * Instruction #1:
     - Instruction:  begin;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
 * Instruction #2:
     - Instruction:  update t set b = 'test' where a;
     - Transaction: conn_0
     - Output: ERROR: 1292 (22007): Truncated incorrect DOUBLE value: ''
     - Executed order: Not executed
 * Instruction #3:
     - Instruction:  rollback;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2

 * Container logs:
   > [2024/07/02 12:12:19.112 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=49] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/07/02 12:12:19.113 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:74, Type:drop schema, State:none, SchemaState:queueing, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:12:19.112 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 12:12:19.113 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:74, Type:drop schema, State:none, SchemaState:queueing, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:12:19.112 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/02 12:12:19.113 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:74, Type:drop schema, State:none, SchemaState:queueing, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:12:19.112 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:12:19.114 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=49] [neededSchemaVersion=50] ["start time"=70.191µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 12:12:19.116 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=50] ["take time"=2.185847ms] [job="ID:74, Type:drop schema, State:running, SchemaState:write only, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:12:19.112 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:12:19.116 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:74, Type:drop schema, State:running, SchemaState:write only, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:12:19.112 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:12:19.117 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=50] [neededSchemaVersion=51] ["start time"=46.864µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 12:12:19.119 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=51] ["take time"=2.553147ms] [job="ID:74, Type:drop schema, State:running, SchemaState:delete only, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:12:19.112 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:12:19.119 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:74, Type:drop schema, State:running, SchemaState:delete only, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:12:19.112 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:12:19.121 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=51] [neededSchemaVersion=52] ["start time"=141.989µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 12:12:19.123 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=52] ["take time"=2.106786ms] [job="ID:74, Type:drop schema, State:done, SchemaState:queueing, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:12:19.112 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:12:19.123 +00:00] [INFO] [delete_range.go:106] ["[ddl] add job into delete-range table"] [jobID=74] [jobType="drop schema"]
   > [2024/07/02 12:12:19.123 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:74, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:69, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:12:19.112 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:12:19.124 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=74]
   > [2024/07/02 12:12:19.124 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/07/02 12:12:19.125 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=52] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/07/02 12:12:19.127 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:76, Type:create schema, State:none, SchemaState:queueing, SchemaID:75, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 12:12:19.126 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 12:12:19.127 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:76, Type:create schema, State:none, SchemaState:queueing, SchemaID:75, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 12:12:19.126 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/02 12:12:19.128 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:76, Type:create schema, State:none, SchemaState:queueing, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:12:19.126 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:12:19.129 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=52] [neededSchemaVersion=53] ["start time"=119.919µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 12:12:19.131 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=53] ["take time"=2.77294ms] [job="ID:76, Type:create schema, State:done, SchemaState:public, SchemaID:75, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 12:12:19.126 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:12:19.131 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:76, Type:create schema, State:synced, SchemaState:public, SchemaID:75, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:12:19.126 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:12:19.132 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=76]
   > [2024/07/02 12:12:19.132 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/07/02 12:12:19.134 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=53] [cur_db=testdb] [sql="create table t(a blob not null, b text);"] [user=root@127.0.0.1]
   > [2024/07/02 12:12:19.135 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:78, Type:create table, State:none, SchemaState:queueing, SchemaID:75, TableID:77, RowCount:0, ArgLen:1, start time: 2024-07-02 12:12:19.134 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 12:12:19.135 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:78, Type:create table, State:none, SchemaState:queueing, SchemaID:75, TableID:77, RowCount:0, ArgLen:1, start time: 2024-07-02 12:12:19.134 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t(a blob not null, b text);"]
   > [2024/07/02 12:12:19.135 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:78, Type:create table, State:none, SchemaState:queueing, SchemaID:75, TableID:77, RowCount:0, ArgLen:0, start time: 2024-07-02 12:12:19.134 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:12:19.136 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=53] [neededSchemaVersion=54] ["start time"=202.612µs] [phyTblIDs="[77]"] [actionTypes="[8]"]
   > [2024/07/02 12:12:19.138 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=54] ["take time"=2.323925ms] [job="ID:78, Type:create table, State:done, SchemaState:public, SchemaID:75, TableID:77, RowCount:0, ArgLen:1, start time: 2024-07-02 12:12:19.134 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:12:19.139 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:78, Type:create table, State:synced, SchemaState:public, SchemaID:75, TableID:77, RowCount:0, ArgLen:0, start time: 2024-07-02 12:12:19.134 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:12:19.139 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=78]
   > [2024/07/02 12:12:19.139 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/07/02 12:12:19.139 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=58] ["first split key"=74800000000000004d]
   > [2024/07/02 12:12:19.140 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=58] ["first at"=74800000000000004d] ["first new region left"="{Id:58 StartKey:7480000000000000ff4700000000000000f8 EndKey:7480000000000000ff4d00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:59 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/02 12:12:19.140 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[58]"]
   > [2024/07/02 12:12:19.140 +00:00] [WARN] [2pc.go:1598] ["schemaLeaseChecker is not set for this transaction"] [sessionID=17] [startTS=450867321671516160] [commitTS=450867321671516161]
   > [2024/07/02 12:12:20.206 +00:00] [INFO] [set.go:127] ["set global var"] [conn=19] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/07/02 12:12:20.790 +00:00] [WARN] [session.go:1683] ["run statement failed"] [conn=19] [schemaVersion=54] [error="[tikv:1292]Truncated incorrect DOUBLE value: ''"] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 19,\n  \"status\": 3,\n  \"strictMode\": true,\n  \"txn\": \"450867322024886272\",\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"127.0.0.1\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/07/02 12:12:20.790 +00:00] [INFO] [conn.go:995] ["command dispatched failed"] [conn=19] [connInfo="id:19, addr:127.0.0.1:50602 status:11, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:1, autocommit:1"] [sql=" update t set b = 'test' where a;"] [txn_mode=OPTIMISTIC] [err="[tikv:1292]Truncated incorrect DOUBLE value: ''"]

### Scenario 1
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
 * Instruction #1:
     - Instruction:  begin;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
 * Instruction #2:
     - Instruction:  update t set b = 'def';
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
 * Instruction #3:
     - Instruction:  update t set b = 'test' where a;
     - Transaction: conn_0
     - Output: ERROR: 1292 (22007): Truncated incorrect DOUBLE value: ''
     - Executed order: Not executed
 * Instruction #4:
     - Instruction:  rollback;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3

 * Container logs:
   > [2024/07/02 12:12:22.777 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=23] [schemaVersion=62] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/07/02 12:12:22.778 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:85, Type:drop schema, State:none, SchemaState:queueing, SchemaID:80, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:12:22.777 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 12:12:22.778 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:85, Type:drop schema, State:none, SchemaState:queueing, SchemaID:80, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:12:22.777 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/02 12:12:22.779 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:85, Type:drop schema, State:none, SchemaState:queueing, SchemaID:80, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:12:22.777 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:12:22.780 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=62] [neededSchemaVersion=63] ["start time"=133.608µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 12:12:22.782 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=63] ["take time"=2.214623ms] [job="ID:85, Type:drop schema, State:running, SchemaState:write only, SchemaID:80, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:12:22.777 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:12:22.782 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:85, Type:drop schema, State:running, SchemaState:write only, SchemaID:80, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:12:22.777 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:12:22.783 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=63] [neededSchemaVersion=64] ["start time"=69.982µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 12:12:22.785 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=64] ["take time"=2.430435ms] [job="ID:85, Type:drop schema, State:running, SchemaState:delete only, SchemaID:80, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:12:22.777 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:12:22.785 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:85, Type:drop schema, State:running, SchemaState:delete only, SchemaID:80, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:12:22.777 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:12:22.786 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=64] [neededSchemaVersion=65] ["start time"=54.337µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 12:12:22.788 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=65] ["take time"=2.192204ms] [job="ID:85, Type:drop schema, State:done, SchemaState:queueing, SchemaID:80, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:12:22.777 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:12:22.788 +00:00] [INFO] [delete_range.go:106] ["[ddl] add job into delete-range table"] [jobID=85] [jobType="drop schema"]
   > [2024/07/02 12:12:22.789 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:85, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:80, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:12:22.777 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:12:22.789 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=85]
   > [2024/07/02 12:12:22.790 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/07/02 12:12:22.791 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=23] [schemaVersion=65] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/07/02 12:12:22.791 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:87, Type:create schema, State:none, SchemaState:queueing, SchemaID:86, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 12:12:22.791 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 12:12:22.791 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:87, Type:create schema, State:none, SchemaState:queueing, SchemaID:86, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 12:12:22.791 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/02 12:12:22.792 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:87, Type:create schema, State:none, SchemaState:queueing, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:12:22.791 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:12:22.792 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=65] [neededSchemaVersion=66] ["start time"=69.213µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/02 12:12:22.794 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=66] ["take time"=2.168806ms] [job="ID:87, Type:create schema, State:done, SchemaState:public, SchemaID:86, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-02 12:12:22.791 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:12:22.794 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:87, Type:create schema, State:synced, SchemaState:public, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-02 12:12:22.791 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:12:22.795 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=87]
   > [2024/07/02 12:12:22.795 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/07/02 12:12:22.797 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=23] [schemaVersion=66] [cur_db=testdb] [sql="create table t(a blob not null, b text);"] [user=root@127.0.0.1]
   > [2024/07/02 12:12:22.799 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:89, Type:create table, State:none, SchemaState:queueing, SchemaID:86, TableID:88, RowCount:0, ArgLen:1, start time: 2024-07-02 12:12:22.798 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/02 12:12:22.799 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:89, Type:create table, State:none, SchemaState:queueing, SchemaID:86, TableID:88, RowCount:0, ArgLen:1, start time: 2024-07-02 12:12:22.798 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create table t(a blob not null, b text);"]
   > [2024/07/02 12:12:22.799 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:89, Type:create table, State:none, SchemaState:queueing, SchemaID:86, TableID:88, RowCount:0, ArgLen:0, start time: 2024-07-02 12:12:22.798 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:12:22.801 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=66] [neededSchemaVersion=67] ["start time"=392.791µs] [phyTblIDs="[88]"] [actionTypes="[8]"]
   > [2024/07/02 12:12:22.803 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=67] ["take time"=2.260299ms] [job="ID:89, Type:create table, State:done, SchemaState:public, SchemaID:86, TableID:88, RowCount:0, ArgLen:1, start time: 2024-07-02 12:12:22.798 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:12:22.804 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:89, Type:create table, State:synced, SchemaState:public, SchemaID:86, TableID:88, RowCount:0, ArgLen:0, start time: 2024-07-02 12:12:22.798 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/02 12:12:22.805 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=89]
   > [2024/07/02 12:12:22.805 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/07/02 12:12:22.805 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=62] ["first split key"=748000000000000058]
   > [2024/07/02 12:12:22.806 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=62] ["first at"=748000000000000058] ["first new region left"="{Id:62 StartKey:7480000000000000ff5200000000000000f8 EndKey:7480000000000000ff5800000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:63 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/02 12:12:22.806 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[62]"]
   > [2024/07/02 12:12:22.806 +00:00] [WARN] [2pc.go:1598] ["schemaLeaseChecker is not set for this transaction"] [sessionID=23] [startTS=450867322632536064] [commitTS=450867322632536065]
   > [2024/07/02 12:12:23.877 +00:00] [INFO] [set.go:127] ["set global var"] [conn=25] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/07/02 12:12:24.759 +00:00] [WARN] [session.go:1683] ["run statement failed"] [conn=25] [schemaVersion=67] [error="[types:1292]Truncated incorrect DOUBLE value: ''"] [session="{\n  \"currDBName\": \"testdb\",\n  \"id\": 25,\n  \"status\": 3,\n  \"strictMode\": true,\n  \"txn\": \"450867322986954752\",\n  \"user\": {\n    \"Username\": \"root\",\n    \"Hostname\": \"127.0.0.1\",\n    \"CurrentUser\": false,\n    \"AuthUsername\": \"root\",\n    \"AuthHostname\": \"%\"\n  }\n}"]
   > [2024/07/02 12:12:24.760 +00:00] [INFO] [conn.go:995] ["command dispatched failed"] [conn=25] [connInfo="id:25, addr:127.0.0.1:50634 status:11, collation:utf8mb4_0900_ai_ci, user:root"] [command=Query] [status="inTxn:1, autocommit:1"] [sql=" update t set b = 'test' where a;"] [txn_mode=OPTIMISTIC] [err="[types:1292]Truncated incorrect DOUBLE value: ''\ngithub.com/pingcap/errors.AddStack\n\t/nfs/cache/mod/github.com/pingcap/errors@v0.11.5-0.20210425183316-da1aaba5fb63/errors.go:174\ngithub.com/pingcap/errors.(*Error).GenWithStackByArgs\n\t/nfs/cache/mod/github.com/pingcap/errors@v0.11.5-0.20210425183316-da1aaba5fb63/normalize.go:159\ngithub.com/pingcap/tidb/types.getValidFloatPrefix\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/types/convert.go:713\ngithub.com/pingcap/tidb/types.StrToFloat\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/types/convert.go:527\ngithub.com/pingcap/tidb/types.(*Datum).ToBool\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/types/datum.go:1597\ngithub.com/pingcap/tidb/expression.EvalBool\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/expression/expression.go:258\ngithub.com/pingcap/tidb/executor.(*memTableReader).getMemRows.func1\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/mem_reader.go:209\ngithub.com/pingcap/tidb/executor.iterTxnMemBuffer\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/mem_reader.go:349\ngithub.com/pingcap/tidb/executor.(*memTableReader).getMemRows\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/mem_reader.go:202\ngithub.com/pingcap/tidb/executor.(*UnionScanExec).open\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/union_scan.go:95\ngithub.com/pingcap/tidb/executor.(*UnionScanExec).Open\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/union_scan.go:65\ngithub.com/pingcap/tidb/executor.(*UpdateExec).Open\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/update.go:428\ngithub.com/pingcap/tidb/executor.(*ExecStmt).Exec\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/executor/adapter.go:388\ngithub.com/pingcap/tidb/session.runStmt\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/session/session.go:1786\ngithub.com/pingcap/tidb/session.(*session).ExecuteStmt\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/session/session.go:1680\ngithub.com/pingcap/tidb/server.(*TiDBContext).ExecuteStmt\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/driver_tidb.go:218\ngithub.com/pingcap/tidb/server.(*clientConn).handleStmt\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/conn.go:1818\ngithub.com/pingcap/tidb/server.(*clientConn).handleQuery\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/conn.go:1690\ngithub.com/pingcap/tidb/server.(*clientConn).dispatch\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/conn.go:1215\ngithub.com/pingcap/tidb/server.(*clientConn).Run\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/conn.go:978\ngithub.com/pingcap/tidb/server.(*Server).onConn\n\t/home/jenkins/agent/workspace/optimization-build-tidb-linux-amd/go/src/github.com/pingcap/tidb/server/server.go:501\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1371"]
