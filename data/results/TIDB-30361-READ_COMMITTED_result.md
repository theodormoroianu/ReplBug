# Bug ID TIDB-30361-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/30361
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED


## Details
 * Database: tidb-5.2.1
 * Number of scenarios: 1
 * Initial setup script: /home/theodor/Projects/MasterThesis/data/sql/TIDB-30361_mysql_bk.sql

## Results
### Scenario 0
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  start transaction;
     - TID: 0
     - Output: None
 * Instruction #2:
     - SQL:  start transaction;
     - TID: 1
     - Output: None
 * Instruction #3:
     - SQL:  select ref_14.c_qpjzzd as c1 from t_q_zw9c as ref_14 order by c1 desc;
     - TID: 0
     - Output: [(0,)]
 * Instruction #4:
     - SQL:  delete from t_q_zw9c;
     - TID: 0
     - Output: None
 * Instruction #5:
     - SQL:  commit;
     - TID: 0
     - Output: None
 * Instruction #6:
     - SQL:  select ref_14.c_qpjzzd as c1 from t_q_zw9c as ref_14 order by c1 desc;
     - TID: 1
     - Output: []
 * Instruction #7:
     - SQL:  commit;
     - TID: 1
     - Output: None

 * Container logs:
   > [2024/06/18 11:59:02.525 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=13] [schemaVersion=36] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/06/18 11:59:02.526 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:63, Type:drop schema, State:none, SchemaState:queueing, SchemaID:58, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:59:02.525 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 11:59:02.526 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:63, Type:drop schema, State:none, SchemaState:queueing, SchemaID:58, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:59:02.525 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/06/18 11:59:02.527 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:63, Type:drop schema, State:none, SchemaState:queueing, SchemaID:58, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:59:02.525 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:59:02.528 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=36] [neededSchemaVersion=37] ["start time"=109.791µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 11:59:02.530 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=37] ["take time"=2.182842ms] [job="ID:63, Type:drop schema, State:running, SchemaState:write only, SchemaID:58, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:59:02.525 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:59:02.530 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:63, Type:drop schema, State:running, SchemaState:write only, SchemaID:58, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:59:02.525 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:59:02.531 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=37] [neededSchemaVersion=38] ["start time"=85.347µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 11:59:02.533 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=38] ["take time"=2.548535ms] [job="ID:63, Type:drop schema, State:running, SchemaState:delete only, SchemaID:58, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:59:02.525 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:59:02.533 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:63, Type:drop schema, State:running, SchemaState:delete only, SchemaID:58, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:59:02.525 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:59:02.535 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=38] [neededSchemaVersion=39] ["start time"=123.691µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 11:59:02.537 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=39] ["take time"=2.961929ms] [job="ID:63, Type:drop schema, State:done, SchemaState:queueing, SchemaID:58, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:59:02.525 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:59:02.538 +00:00] [INFO] [delete_range.go:106] ["[ddl] add job into delete-range table"] [jobID=63] [jobType="drop schema"]
   > [2024/06/18 11:59:02.538 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:63, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:58, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:59:02.525 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:59:02.539 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=63]
   > [2024/06/18 11:59:02.539 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/18 11:59:02.541 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=13] [schemaVersion=39] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/06/18 11:59:02.542 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:65, Type:create schema, State:none, SchemaState:queueing, SchemaID:64, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 11:59:02.541 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 11:59:02.542 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:65, Type:create schema, State:none, SchemaState:queueing, SchemaID:64, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 11:59:02.541 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/18 11:59:02.542 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:create schema, State:none, SchemaState:queueing, SchemaID:64, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:59:02.541 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:59:02.543 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=39] [neededSchemaVersion=40] ["start time"=165.665µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 11:59:02.545 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=40] ["take time"=2.246608ms] [job="ID:65, Type:create schema, State:done, SchemaState:public, SchemaID:64, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 11:59:02.541 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:59:02.546 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:create schema, State:synced, SchemaState:public, SchemaID:64, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:59:02.541 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:59:02.547 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=65]
   > [2024/06/18 11:59:02.547 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/18 11:59:02.551 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=13] [schemaVersion=40] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_q_zw9c`\n--\n\nDROP TABLE IF EXISTS `t_q_zw9c`;"] [user=root@127.0.0.1]
   > [2024/06/18 11:59:02.552 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=13] [schemaVersion=40] [cur_db=testdb] [sql="CREATE TABLE `t_q_zw9c` (\n  `c_qpjzzd` int(11) NOT NULL,\n  `c_1mp0eb` int(11) DEFAULT NULL,\n  `c_3dcuc` double DEFAULT NULL,\n  PRIMARY KEY (`c_qpjzzd`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/06/18 11:59:02.554 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:67, Type:create table, State:none, SchemaState:queueing, SchemaID:64, TableID:66, RowCount:0, ArgLen:1, start time: 2024-06-18 11:59:02.553 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 11:59:02.554 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:67, Type:create table, State:none, SchemaState:queueing, SchemaID:64, TableID:66, RowCount:0, ArgLen:1, start time: 2024-06-18 11:59:02.553 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_q_zw9c` (\n  `c_qpjzzd` int(11) NOT NULL,\n  `c_1mp0eb` int(11) DEFAULT NULL,\n  `c_3dcuc` double DEFAULT NULL,\n  PRIMARY KEY (`c_qpjzzd`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/18 11:59:02.555 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:create table, State:none, SchemaState:queueing, SchemaID:64, TableID:66, RowCount:0, ArgLen:0, start time: 2024-06-18 11:59:02.553 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:59:02.557 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=40] [neededSchemaVersion=41] ["start time"=329.096µs] [phyTblIDs="[66]"] [actionTypes="[8]"]
   > [2024/06/18 11:59:02.558 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=41] ["take time"=2.110066ms] [job="ID:67, Type:create table, State:done, SchemaState:public, SchemaID:64, TableID:66, RowCount:0, ArgLen:1, start time: 2024-06-18 11:59:02.553 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:59:02.559 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:create table, State:synced, SchemaState:public, SchemaID:64, TableID:66, RowCount:0, ArgLen:0, start time: 2024-06-18 11:59:02.553 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:59:02.561 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=67]
   > [2024/06/18 11:59:02.561 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/18 11:59:02.561 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=54] ["first split key"=748000000000000042]
   > [2024/06/18 11:59:02.561 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=54] ["first at"=748000000000000042] ["first new region left"="{Id:54 StartKey:7480000000000000ff3c00000000000000f8 EndKey:7480000000000000ff4200000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:55 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/18 11:59:02.561 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[54]"]
   > [2024/06/18 11:59:02.562 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=13] [schemaVersion=41] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_q_zw9c` DISABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/06/18 11:59:02.563 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=13] [schemaVersion=41] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_q_zw9c` ENABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/06/18 11:59:03.634 +00:00] [INFO] [set.go:127] ["set global var"] [conn=15] [name=tx_isolation] [val=READ-COMMITTED]
