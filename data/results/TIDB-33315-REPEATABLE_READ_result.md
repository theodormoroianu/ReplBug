# Bug ID TIDB-33315-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/33315
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              conn 1 should get an empty set


## Details
 * Database: tidb-v5.4.0
 * Number of scenarios: 1
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
 * Instruction #1:
     - Instruction:  BEGIN PESSIMISTIC;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
 * Instruction #2:
     - Instruction:  UPDATE t SET c1=2, c2=2;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
 * Instruction #3:
     - Instruction:  BEGIN PESSIMISTIC;
     - Transaction: conn_1
     - Output: None
     - Executed order: 3
 * Instruction #4:
     - Instruction:  DELETE FROM t;
     - Transaction: conn_1
     - Output: None
     - Executed order: 5
 * Instruction #5:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
 * Instruction #6:
     - Instruction:  SELECT * FROM t;
     - Transaction: conn_1
     - Output: [(1, 1)]
     - Executed order: 6
 * Instruction #7:
     - Instruction:  COMMIT;
     - Transaction: conn_1
     - Output: None
     - Executed order: 7

 * Container logs:
   > [2024/07/01 15:14:21.832 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=117] [user=root] [host=]
   > [2024/07/01 15:14:21.835 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=117] [schemaVersion=385] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/07/01 15:14:21.836 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:396, Type:drop schema, State:none, SchemaState:queueing, SchemaID:391, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:14:21.835 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:14:21.836 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:396, Type:drop schema, State:none, SchemaState:queueing, SchemaID:391, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:14:21.835 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/01 15:14:21.836 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:396, Type:drop schema, State:none, SchemaState:queueing, SchemaID:391, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:14:21.835 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:14:21.837 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=385] [neededSchemaVersion=386] ["start time"=60.064µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:14:21.839 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=386] ["take time"=2.229286ms] [job="ID:396, Type:drop schema, State:running, SchemaState:write only, SchemaID:391, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:14:21.835 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:14:21.839 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:396, Type:drop schema, State:running, SchemaState:write only, SchemaID:391, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:14:21.835 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:14:21.840 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=386] [neededSchemaVersion=387] ["start time"=88.211µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:14:21.842 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=387] ["take time"=2.263229ms] [job="ID:396, Type:drop schema, State:running, SchemaState:delete only, SchemaID:391, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:14:21.835 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:14:21.842 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:396, Type:drop schema, State:running, SchemaState:delete only, SchemaID:391, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:14:21.835 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:14:21.843 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=387] [neededSchemaVersion=388] ["start time"=83.95µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:14:21.845 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=388] ["take time"=2.186333ms] [job="ID:396, Type:drop schema, State:done, SchemaState:queueing, SchemaID:391, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:14:21.835 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:14:21.846 +00:00] [INFO] [delete_range.go:107] ["[ddl] add job into delete-range table"] [jobID=396] [jobType="drop schema"]
   > [2024/07/01 15:14:21.846 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:396, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:391, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:14:21.835 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:14:21.846 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=396]
   > [2024/07/01 15:14:21.846 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:14:21.847 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=117] [schemaVersion=388] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/07/01 15:14:21.848 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:398, Type:create schema, State:none, SchemaState:queueing, SchemaID:397, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:14:21.848 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:14:21.849 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:398, Type:create schema, State:none, SchemaState:queueing, SchemaID:397, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:14:21.848 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/01 15:14:21.849 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:398, Type:create schema, State:none, SchemaState:queueing, SchemaID:397, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:14:21.848 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:14:21.849 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=388] [neededSchemaVersion=389] ["start time"=75.15µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:14:21.851 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=389] ["take time"=2.225095ms] [job="ID:398, Type:create schema, State:done, SchemaState:public, SchemaID:397, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:14:21.848 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:14:21.852 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:398, Type:create schema, State:synced, SchemaState:public, SchemaID:397, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:14:21.848 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:14:21.852 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=398]
   > [2024/07/01 15:14:21.852 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:14:21.854 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=117] [schemaVersion=389] [cur_db=testdb] [sql="CREATE TABLE t (c1 INT PRIMARY KEY, c2 INT);"] [user=root@127.0.0.1]
   > [2024/07/01 15:14:21.855 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:400, Type:create table, State:none, SchemaState:queueing, SchemaID:397, TableID:399, RowCount:0, ArgLen:1, start time: 2024-07-01 15:14:21.854 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:14:21.855 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:400, Type:create table, State:none, SchemaState:queueing, SchemaID:397, TableID:399, RowCount:0, ArgLen:1, start time: 2024-07-01 15:14:21.854 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE t (c1 INT PRIMARY KEY, c2 INT);"]
   > [2024/07/01 15:14:21.855 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:400, Type:create table, State:none, SchemaState:queueing, SchemaID:397, TableID:399, RowCount:0, ArgLen:0, start time: 2024-07-01 15:14:21.854 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:14:21.856 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=389] [neededSchemaVersion=390] ["start time"=162.103µs] [phyTblIDs="[399]"] [actionTypes="[8]"]
   > [2024/07/01 15:14:21.858 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=390] ["take time"=2.2362ms] [job="ID:400, Type:create table, State:done, SchemaState:public, SchemaID:397, TableID:399, RowCount:0, ArgLen:1, start time: 2024-07-01 15:14:21.854 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:14:21.859 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:400, Type:create table, State:synced, SchemaState:public, SchemaID:397, TableID:399, RowCount:0, ArgLen:0, start time: 2024-07-01 15:14:21.854 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:14:21.859 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=400]
   > [2024/07/01 15:14:21.860 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:14:21.860 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=158] ["first split key"=74800000000000018f]
   > [2024/07/01 15:14:21.860 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=158] ["first at"=74800000000000018f] ["first new region left"="{Id:158 StartKey:7480000000000001ff8900000000000000f8 EndKey:7480000000000001ff8f00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:159 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/01 15:14:21.860 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[158]"]
   > [2024/07/01 15:14:22.937 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=119] [user=root] [host=]
   > [2024/07/01 15:14:22.950 +00:00] [INFO] [set.go:139] ["set global var"] [conn=119] [name=tx_isolation] [val=REPEATABLE-READ]
   > [2024/07/01 15:14:23.890 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=121] [user=root] [host=]
   > [2024/07/01 15:14:26.600 +00:00] [WARN] [memory_usage_alarm.go:140] ["tidb-server has the risk of OOM. Running SQLs and heap profile will be recorded in record path"] ["is server-memory-quota set"=false] ["system memory total"=16091959296] ["system memory usage"=13088641024] ["tidb-server memory usage"=8023672064] [memory-usage-alarm-ratio=0.8] ["record path"="/tmp/0_tidb/MC4wLjAuMDo0MDAwLzAuMC4wLjA6MTAwODA=/tmp-storage/record"]
