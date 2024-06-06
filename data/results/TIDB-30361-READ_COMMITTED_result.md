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
     - SQL:  select ref_14.c_qpjzzd as c1 from t_q_zw9c as ref_14;
     - TID: 1
     - Output: [(0,)]
 * Instruction #7:
     - SQL:  commit;
     - TID: 1
     - Output: None

 * Container logs:
   > [2024/06/06 13:21:58.158 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=26] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/06/06 13:21:58.158 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=26] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/06/06 13:21:58.159 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:54, Type:create schema, State:none, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-06 13:21:58.159 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/06 13:21:58.159 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:54, Type:create schema, State:none, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-06 13:21:58.159 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/06 13:21:58.160 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:54, Type:create schema, State:none, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-06 13:21:58.159 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/06 13:21:58.161 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=26] [neededSchemaVersion=27] ["start time"=124.878µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/06 13:21:58.163 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=27] ["take time"=2.596528ms] [job="ID:54, Type:create schema, State:done, SchemaState:public, SchemaID:53, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-06 13:21:58.159 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/06 13:21:58.164 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:54, Type:create schema, State:synced, SchemaState:public, SchemaID:53, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-06 13:21:58.159 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/06 13:21:58.165 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=54]
   > [2024/06/06 13:21:58.165 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/06 13:21:58.168 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=27] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_q_zw9c`\n--\n\nDROP TABLE IF EXISTS `t_q_zw9c`;"] [user=root@127.0.0.1]
   > [2024/06/06 13:21:58.168 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=27] [cur_db=testdb] [sql="CREATE TABLE `t_q_zw9c` (\n  `c_qpjzzd` int(11) NOT NULL,\n  `c_1mp0eb` int(11) DEFAULT NULL,\n  `c_3dcuc` double DEFAULT NULL,\n  PRIMARY KEY (`c_qpjzzd`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/06/06 13:21:58.169 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:56, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:55, RowCount:0, ArgLen:1, start time: 2024-06-06 13:21:58.169 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/06 13:21:58.169 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:56, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:55, RowCount:0, ArgLen:1, start time: 2024-06-06 13:21:58.169 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_q_zw9c` (\n  `c_qpjzzd` int(11) NOT NULL,\n  `c_1mp0eb` int(11) DEFAULT NULL,\n  `c_3dcuc` double DEFAULT NULL,\n  PRIMARY KEY (`c_qpjzzd`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/06 13:21:58.170 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:56, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:55, RowCount:0, ArgLen:0, start time: 2024-06-06 13:21:58.169 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/06 13:21:58.171 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=27] [neededSchemaVersion=28] ["start time"=224.753µs] [phyTblIDs="[55]"] [actionTypes="[8]"]
   > [2024/06/06 13:21:58.173 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=28] ["take time"=2.112521ms] [job="ID:56, Type:create table, State:done, SchemaState:public, SchemaID:53, TableID:55, RowCount:0, ArgLen:1, start time: 2024-06-06 13:21:58.169 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/06 13:21:58.173 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:56, Type:create table, State:synced, SchemaState:public, SchemaID:53, TableID:55, RowCount:0, ArgLen:0, start time: 2024-06-06 13:21:58.169 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/06 13:21:58.174 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=56]
   > [2024/06/06 13:21:58.174 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/06 13:21:58.175 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=50] ["first split key"=748000000000000037]
   > [2024/06/06 13:21:58.175 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=50] ["first at"=748000000000000037] ["first new region left"="{Id:50 StartKey:7480000000000000ff3300000000000000f8 EndKey:7480000000000000ff3700000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:51 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/06 13:21:58.175 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[50]"]
   > [2024/06/06 13:21:58.175 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=28] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_q_zw9c` DISABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/06/06 13:21:58.177 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=28] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_q_zw9c` ENABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/06/06 13:21:59.434 +00:00] [INFO] [set.go:127] ["set global var"] [conn=7] [name=tx_isolation] [val=READ-COMMITTED]
