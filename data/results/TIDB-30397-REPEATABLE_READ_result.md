# Bug ID TIDB-30397-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/30397
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ


## Details
 * Database: tidb-v5.4.0
 * Number of scenarios: 2
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  update t_berydd set c_cdqetd = t_berydd.c_ioru4c;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
 * Instruction #1:
     - Instruction:  select count(c_mp6ko) from t_berydd;
     - Transaction: conn_0
     - Output: [(39,)]
     - Executed order: 1

 * Container logs:
   > [2024/07/01 15:12:55.521 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=21] [user=root] [host=]
   > [2024/07/01 15:12:55.526 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=21] [schemaVersion=51] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/07/01 15:12:55.526 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:78, Type:drop schema, State:none, SchemaState:queueing, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:55.526 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:12:55.527 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:78, Type:drop schema, State:none, SchemaState:queueing, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:55.526 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/01 15:12:55.527 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:78, Type:drop schema, State:none, SchemaState:queueing, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:55.526 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:55.528 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=51] [neededSchemaVersion=52] ["start time"=142.827µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:12:55.530 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=52] ["take time"=2.244163ms] [job="ID:78, Type:drop schema, State:running, SchemaState:write only, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:55.526 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:55.530 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:78, Type:drop schema, State:running, SchemaState:write only, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:55.526 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:55.531 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=52] [neededSchemaVersion=53] ["start time"=96.661µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:12:55.533 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=53] ["take time"=2.292633ms] [job="ID:78, Type:drop schema, State:running, SchemaState:delete only, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:55.526 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:55.534 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:78, Type:drop schema, State:running, SchemaState:delete only, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:55.526 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:55.535 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=53] [neededSchemaVersion=54] ["start time"=98.687µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:12:55.537 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=54] ["take time"=2.109646ms] [job="ID:78, Type:drop schema, State:done, SchemaState:queueing, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:55.526 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:55.537 +00:00] [INFO] [delete_range.go:107] ["[ddl] add job into delete-range table"] [jobID=78] [jobType="drop schema"]
   > [2024/07/01 15:12:55.537 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:78, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:55.526 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:55.538 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=78]
   > [2024/07/01 15:12:55.538 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:12:55.540 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=21] [schemaVersion=54] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/07/01 15:12:55.541 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:80, Type:create schema, State:none, SchemaState:queueing, SchemaID:79, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:55.54 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:12:55.541 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:80, Type:create schema, State:none, SchemaState:queueing, SchemaID:79, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:55.54 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/01 15:12:55.542 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:80, Type:create schema, State:none, SchemaState:queueing, SchemaID:79, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:55.54 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:55.543 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=54] [neededSchemaVersion=55] ["start time"=153.583µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:12:55.545 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=55] ["take time"=2.253801ms] [job="ID:80, Type:create schema, State:done, SchemaState:public, SchemaID:79, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:55.54 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:55.545 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:80, Type:create schema, State:synced, SchemaState:public, SchemaID:79, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:55.54 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:55.546 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=80]
   > [2024/07/01 15:12:55.546 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:12:55.553 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=21] [schemaVersion=55] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_berydd`\n--\n\nDROP TABLE IF EXISTS `t_berydd`;"] [user=root@127.0.0.1]
   > [2024/07/01 15:12:55.554 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=21] [schemaVersion=55] [cur_db=testdb] [sql="CREATE TABLE `t_berydd` (\n  `c_ymgvrd` int(11) DEFAULT NULL,\n  `c_ee5vqb` int(11) DEFAULT NULL,\n  `c_xsjoqb` int(11) DEFAULT NULL,\n  `c_xqizm` text DEFAULT NULL,\n  `c__3lu4b` int(11) DEFAULT NULL,\n  `c_mp6ko` double DEFAULT NULL,\n  `c_ndnhmc` double DEFAULT NULL,\n  `c_cdqetd` double DEFAULT NULL,\n  `c_ioru4c` double NOT NULL,\n  PRIMARY KEY (`c_ioru4c`) /*T![clustered_index] NONCLUSTERED */,\n  KEY `t_c1q7y` (`c_ymgvrd`,`c_ee5vqb`,`c_xsjoqb`,`c_mp6ko`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/07/01 15:12:55.556 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:82, Type:create table, State:none, SchemaState:queueing, SchemaID:79, TableID:81, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:55.555 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:12:55.556 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:82, Type:create table, State:none, SchemaState:queueing, SchemaID:79, TableID:81, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:55.555 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_berydd` (\n  `c_ymgvrd` int(11) DEFAULT NULL,\n  `c_ee5vqb` int(11) DEFAULT NULL,\n  `c_xsjoqb` int(11) DEFAULT NULL,\n  `c_xqizm` text DEFAULT NULL,\n  `c__3lu4b` int(11) DEFAULT NULL,\n  `c_mp6ko` double DEFAULT NULL,\n  `c_ndnhmc` double DEFAULT NULL,\n  `c_cdqetd` double DEFAULT NULL,\n  `c_ioru4c` double NOT NULL,\n  PRIMARY KEY (`c_ioru4c`) /*T![clustered_index] NONCLUSTERED */,\n  KEY `t_c1q7y` (`c_ymgvrd`,`c_ee5vqb`,`c_xsjoqb`,`c_mp6ko`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/01 15:12:55.557 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:82, Type:create table, State:none, SchemaState:queueing, SchemaID:79, TableID:81, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:55.555 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:55.560 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=55] [neededSchemaVersion=56] ["start time"=635.283µs] [phyTblIDs="[81]"] [actionTypes="[8]"]
   > [2024/07/01 15:12:55.561 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=56] ["take time"=2.291794ms] [job="ID:82, Type:create table, State:done, SchemaState:public, SchemaID:79, TableID:81, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:55.555 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:55.563 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:82, Type:create table, State:synced, SchemaState:public, SchemaID:79, TableID:81, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:55.555 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:55.564 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=82]
   > [2024/07/01 15:12:55.564 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:12:55.564 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=62] ["first split key"=748000000000000051]
   > [2024/07/01 15:12:55.565 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=62] ["first at"=748000000000000051] ["first new region left"="{Id:62 StartKey:7480000000000000ff4b00000000000000f8 EndKey:7480000000000000ff5100000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:63 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/01 15:12:55.565 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[62]"]
   > [2024/07/01 15:12:55.565 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=21] [schemaVersion=56] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_berydd` DISABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/07/01 15:12:55.567 +00:00] [WARN] [2pc.go:1596] ["schemaLeaseChecker is not set for this transaction"] [sessionID=21] [startTS=450847513133973505] [commitTS=450847513134235648]
   > [2024/07/01 15:12:55.570 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=21] [schemaVersion=56] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_berydd` ENABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/07/01 15:12:55.571 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=21] [schemaVersion=56] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_kqoy4`\n--\n\nDROP TABLE IF EXISTS `t_kqoy4`;"] [user=root@127.0.0.1]
   > [2024/07/01 15:12:55.572 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=21] [schemaVersion=56] [cur_db=testdb] [sql="CREATE TABLE `t_kqoy4` (\n  `c_embscb` int(11) DEFAULT NULL,\n  `c_gi3pxb` text DEFAULT NULL,\n  `c_fif_7c` text DEFAULT NULL,\n  `c_scsjqb` double DEFAULT NULL,\n  `c_cxqb1` text DEFAULT NULL,\n  `c_w1ibr` int(11) DEFAULT NULL,\n  `c_0lknib` double DEFAULT NULL,\n  `c_qfdzbd` double NOT NULL,\n  `c_7kdcs` double DEFAULT NULL,\n  PRIMARY KEY (`c_qfdzbd`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/07/01 15:12:55.573 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:84, Type:create table, State:none, SchemaState:queueing, SchemaID:79, TableID:83, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:55.572 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:12:55.573 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:84, Type:create table, State:none, SchemaState:queueing, SchemaID:79, TableID:83, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:55.572 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_kqoy4` (\n  `c_embscb` int(11) DEFAULT NULL,\n  `c_gi3pxb` text DEFAULT NULL,\n  `c_fif_7c` text DEFAULT NULL,\n  `c_scsjqb` double DEFAULT NULL,\n  `c_cxqb1` text DEFAULT NULL,\n  `c_w1ibr` int(11) DEFAULT NULL,\n  `c_0lknib` double DEFAULT NULL,\n  `c_qfdzbd` double NOT NULL,\n  `c_7kdcs` double DEFAULT NULL,\n  PRIMARY KEY (`c_qfdzbd`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/01 15:12:55.574 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:84, Type:create table, State:none, SchemaState:queueing, SchemaID:79, TableID:83, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:55.572 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:55.577 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=56] [neededSchemaVersion=57] ["start time"=683.124µs] [phyTblIDs="[83]"] [actionTypes="[8]"]
   > [2024/07/01 15:12:55.578 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=57] ["take time"=2.26756ms] [job="ID:84, Type:create table, State:done, SchemaState:public, SchemaID:79, TableID:83, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:55.572 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:55.580 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:84, Type:create table, State:synced, SchemaState:public, SchemaID:79, TableID:83, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:55.572 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:55.581 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=84]
   > [2024/07/01 15:12:55.581 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:12:55.581 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=64] ["first split key"=748000000000000053]
   > [2024/07/01 15:12:55.582 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=64] ["first at"=748000000000000053] ["first new region left"="{Id:64 StartKey:7480000000000000ff5100000000000000f8 EndKey:7480000000000000ff5300000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:65 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/01 15:12:55.582 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[64]"]
   > [2024/07/01 15:12:55.582 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=21] [schemaVersion=57] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_kqoy4` DISABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/07/01 15:12:55.583 +00:00] [WARN] [2pc.go:1596] ["schemaLeaseChecker is not set for this transaction"] [sessionID=21] [startTS=450847513138429953] [commitTS=450847513138429954]
   > [2024/07/01 15:12:55.585 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=21] [schemaVersion=57] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_kqoy4` ENABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/07/01 15:12:56.687 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=23] [user=root] [host=]

### Scenario 1
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
 * Instruction #1:
     - Instruction:  start transaction;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
 * Instruction #2:
     - Instruction:  update t_berydd set c_cdqetd = t_berydd.c_ioru4c;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
 * Instruction #3:
     - Instruction:  select count(c_mp6ko) from t_berydd;
     - Transaction: conn_0
     - Output: [(36,)]
     - Executed order: 3
 * Instruction #4:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4

 * Container logs:
   > [2024/07/01 15:12:58.868 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=27] [user=root] [host=]
   > [2024/07/01 15:12:58.872 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=27] [schemaVersion=65] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/07/01 15:12:58.872 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:91, Type:drop schema, State:none, SchemaState:queueing, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:58.872 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:12:58.873 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:91, Type:drop schema, State:none, SchemaState:queueing, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:58.872 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/01 15:12:58.873 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:91, Type:drop schema, State:none, SchemaState:queueing, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:58.872 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:58.874 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=65] [neededSchemaVersion=66] ["start time"=114.471µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:12:58.876 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=66] ["take time"=2.249959ms] [job="ID:91, Type:drop schema, State:running, SchemaState:write only, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:58.872 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:58.876 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:91, Type:drop schema, State:running, SchemaState:write only, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:58.872 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:58.877 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=66] [neededSchemaVersion=67] ["start time"=89.677µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:12:58.879 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=67] ["take time"=2.515219ms] [job="ID:91, Type:drop schema, State:running, SchemaState:delete only, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:58.872 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:58.880 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:91, Type:drop schema, State:running, SchemaState:delete only, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:58.872 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:58.881 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=67] [neededSchemaVersion=68] ["start time"=101.899µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:12:58.884 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=68] ["take time"=3.034843ms] [job="ID:91, Type:drop schema, State:done, SchemaState:queueing, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:58.872 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:58.884 +00:00] [INFO] [delete_range.go:107] ["[ddl] add job into delete-range table"] [jobID=91] [jobType="drop schema"]
   > [2024/07/01 15:12:58.884 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:91, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:58.872 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:58.885 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=91]
   > [2024/07/01 15:12:58.886 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:12:58.887 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=27] [schemaVersion=68] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/07/01 15:12:58.888 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:93, Type:create schema, State:none, SchemaState:queueing, SchemaID:92, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:58.888 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:12:58.888 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:93, Type:create schema, State:none, SchemaState:queueing, SchemaID:92, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:58.888 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/01 15:12:58.889 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:93, Type:create schema, State:none, SchemaState:queueing, SchemaID:92, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:58.888 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:58.890 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=68] [neededSchemaVersion=69] ["start time"=189.83µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:12:58.892 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=69] ["take time"=2.228098ms] [job="ID:93, Type:create schema, State:done, SchemaState:public, SchemaID:92, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:58.888 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:58.892 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:93, Type:create schema, State:synced, SchemaState:public, SchemaID:92, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:58.888 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:58.893 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=93]
   > [2024/07/01 15:12:58.893 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:12:58.899 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=27] [schemaVersion=69] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_berydd`\n--\n\nDROP TABLE IF EXISTS `t_berydd`;"] [user=root@127.0.0.1]
   > [2024/07/01 15:12:58.900 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=27] [schemaVersion=69] [cur_db=testdb] [sql="CREATE TABLE `t_berydd` (\n  `c_ymgvrd` int(11) DEFAULT NULL,\n  `c_ee5vqb` int(11) DEFAULT NULL,\n  `c_xsjoqb` int(11) DEFAULT NULL,\n  `c_xqizm` text DEFAULT NULL,\n  `c__3lu4b` int(11) DEFAULT NULL,\n  `c_mp6ko` double DEFAULT NULL,\n  `c_ndnhmc` double DEFAULT NULL,\n  `c_cdqetd` double DEFAULT NULL,\n  `c_ioru4c` double NOT NULL,\n  PRIMARY KEY (`c_ioru4c`) /*T![clustered_index] NONCLUSTERED */,\n  KEY `t_c1q7y` (`c_ymgvrd`,`c_ee5vqb`,`c_xsjoqb`,`c_mp6ko`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/07/01 15:12:58.902 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:95, Type:create table, State:none, SchemaState:queueing, SchemaID:92, TableID:94, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:58.901 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:12:58.902 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:95, Type:create table, State:none, SchemaState:queueing, SchemaID:92, TableID:94, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:58.901 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_berydd` (\n  `c_ymgvrd` int(11) DEFAULT NULL,\n  `c_ee5vqb` int(11) DEFAULT NULL,\n  `c_xsjoqb` int(11) DEFAULT NULL,\n  `c_xqizm` text DEFAULT NULL,\n  `c__3lu4b` int(11) DEFAULT NULL,\n  `c_mp6ko` double DEFAULT NULL,\n  `c_ndnhmc` double DEFAULT NULL,\n  `c_cdqetd` double DEFAULT NULL,\n  `c_ioru4c` double NOT NULL,\n  PRIMARY KEY (`c_ioru4c`) /*T![clustered_index] NONCLUSTERED */,\n  KEY `t_c1q7y` (`c_ymgvrd`,`c_ee5vqb`,`c_xsjoqb`,`c_mp6ko`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/01 15:12:58.903 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:95, Type:create table, State:none, SchemaState:queueing, SchemaID:92, TableID:94, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:58.901 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:58.906 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=69] [neededSchemaVersion=70] ["start time"=569.282µs] [phyTblIDs="[94]"] [actionTypes="[8]"]
   > [2024/07/01 15:12:58.907 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=70] ["take time"=2.268468ms] [job="ID:95, Type:create table, State:done, SchemaState:public, SchemaID:92, TableID:94, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:58.901 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:58.909 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:95, Type:create table, State:synced, SchemaState:public, SchemaID:92, TableID:94, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:58.901 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:58.910 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=95]
   > [2024/07/01 15:12:58.910 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:12:58.910 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=68] ["first split key"=74800000000000005e]
   > [2024/07/01 15:12:58.911 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=27] [schemaVersion=70] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_berydd` DISABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/07/01 15:12:58.911 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=68] ["first at"=74800000000000005e] ["first new region left"="{Id:68 StartKey:7480000000000000ff5800000000000000f8 EndKey:7480000000000000ff5e00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:69 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/01 15:12:58.911 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[68]"]
   > [2024/07/01 15:12:58.913 +00:00] [WARN] [2pc.go:1596] ["schemaLeaseChecker is not set for this transaction"] [sessionID=27] [startTS=450847514011369472] [commitTS=450847514011369473]
   > [2024/07/01 15:12:58.916 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=27] [schemaVersion=70] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_berydd` ENABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/07/01 15:12:58.917 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=27] [schemaVersion=70] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_kqoy4`\n--\n\nDROP TABLE IF EXISTS `t_kqoy4`;"] [user=root@127.0.0.1]
   > [2024/07/01 15:12:58.918 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=27] [schemaVersion=70] [cur_db=testdb] [sql="CREATE TABLE `t_kqoy4` (\n  `c_embscb` int(11) DEFAULT NULL,\n  `c_gi3pxb` text DEFAULT NULL,\n  `c_fif_7c` text DEFAULT NULL,\n  `c_scsjqb` double DEFAULT NULL,\n  `c_cxqb1` text DEFAULT NULL,\n  `c_w1ibr` int(11) DEFAULT NULL,\n  `c_0lknib` double DEFAULT NULL,\n  `c_qfdzbd` double NOT NULL,\n  `c_7kdcs` double DEFAULT NULL,\n  PRIMARY KEY (`c_qfdzbd`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/07/01 15:12:58.919 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:97, Type:create table, State:none, SchemaState:queueing, SchemaID:92, TableID:96, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:58.919 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:12:58.920 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:97, Type:create table, State:none, SchemaState:queueing, SchemaID:92, TableID:96, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:58.919 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_kqoy4` (\n  `c_embscb` int(11) DEFAULT NULL,\n  `c_gi3pxb` text DEFAULT NULL,\n  `c_fif_7c` text DEFAULT NULL,\n  `c_scsjqb` double DEFAULT NULL,\n  `c_cxqb1` text DEFAULT NULL,\n  `c_w1ibr` int(11) DEFAULT NULL,\n  `c_0lknib` double DEFAULT NULL,\n  `c_qfdzbd` double NOT NULL,\n  `c_7kdcs` double DEFAULT NULL,\n  PRIMARY KEY (`c_qfdzbd`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/01 15:12:58.920 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:97, Type:create table, State:none, SchemaState:queueing, SchemaID:92, TableID:96, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:58.919 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:58.923 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=70] [neededSchemaVersion=71] ["start time"=533.593µs] [phyTblIDs="[96]"] [actionTypes="[8]"]
   > [2024/07/01 15:12:58.924 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=71] ["take time"=2.265045ms] [job="ID:97, Type:create table, State:done, SchemaState:public, SchemaID:92, TableID:96, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:58.919 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:58.926 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:97, Type:create table, State:synced, SchemaState:public, SchemaID:92, TableID:96, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:58.919 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:58.927 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=97]
   > [2024/07/01 15:12:58.927 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:12:58.927 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=70] ["first split key"=748000000000000060]
   > [2024/07/01 15:12:58.928 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=70] ["first at"=748000000000000060] ["first new region left"="{Id:70 StartKey:7480000000000000ff5e00000000000000f8 EndKey:7480000000000000ff6000000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:71 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/01 15:12:58.928 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[70]"]
   > [2024/07/01 15:12:58.928 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=27] [schemaVersion=71] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_kqoy4` DISABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/07/01 15:12:58.929 +00:00] [WARN] [2pc.go:1596] ["schemaLeaseChecker is not set for this transaction"] [sessionID=27] [startTS=450847514015563777] [commitTS=450847514015563778]
   > [2024/07/01 15:12:58.931 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=27] [schemaVersion=71] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_kqoy4` ENABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/07/01 15:12:59.989 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=29] [user=root] [host=]
   > [2024/07/01 15:13:00.007 +00:00] [INFO] [set.go:139] ["set global var"] [conn=29] [name=tx_isolation] [val=REPEATABLE-READ]
