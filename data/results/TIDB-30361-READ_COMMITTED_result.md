# Bug ID TIDB-30361-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/30361
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED


## Details
 * Database: tidb-v5.4.0
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
   > [2024/06/18 16:12:21.852 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=13] [user=root] [host=]
   > [2024/06/18 16:12:21.855 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=13] [schemaVersion=38] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/06/18 16:12:21.856 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:67, Type:drop schema, State:none, SchemaState:queueing, SchemaID:62, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:21.855 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 16:12:21.856 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:67, Type:drop schema, State:none, SchemaState:queueing, SchemaID:62, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:21.855 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/06/18 16:12:21.857 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:drop schema, State:none, SchemaState:queueing, SchemaID:62, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:21.855 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:21.858 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=38] [neededSchemaVersion=39] ["start time"=88.979µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 16:12:21.860 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=39] ["take time"=2.055313ms] [job="ID:67, Type:drop schema, State:running, SchemaState:write only, SchemaID:62, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:21.855 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:21.860 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:drop schema, State:running, SchemaState:write only, SchemaID:62, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:21.855 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:21.861 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=39] [neededSchemaVersion=40] ["start time"=100.642µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 16:12:21.863 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=40] ["take time"=2.035059ms] [job="ID:67, Type:drop schema, State:running, SchemaState:delete only, SchemaID:62, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:21.855 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:21.863 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:drop schema, State:running, SchemaState:delete only, SchemaID:62, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:21.855 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:21.864 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=40] [neededSchemaVersion=41] ["start time"=120.198µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 16:12:21.866 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=41] ["take time"=2.23816ms] [job="ID:67, Type:drop schema, State:done, SchemaState:queueing, SchemaID:62, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:21.855 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:21.866 +00:00] [INFO] [delete_range.go:107] ["[ddl] add job into delete-range table"] [jobID=67] [jobType="drop schema"]
   > [2024/06/18 16:12:21.866 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:62, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:21.855 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:21.867 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=67]
   > [2024/06/18 16:12:21.867 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 16:12:21.869 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=13] [schemaVersion=41] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/06/18 16:12:21.869 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:69, Type:create schema, State:none, SchemaState:queueing, SchemaID:68, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 16:12:21.869 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 16:12:21.869 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:69, Type:create schema, State:none, SchemaState:queueing, SchemaID:68, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 16:12:21.869 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/18 16:12:21.869 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:69, Type:create schema, State:none, SchemaState:queueing, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:21.869 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:21.870 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=41] [neededSchemaVersion=42] ["start time"=70.75µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 16:12:21.872 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=42] ["take time"=2.18913ms] [job="ID:69, Type:create schema, State:done, SchemaState:public, SchemaID:68, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 16:12:21.869 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:21.872 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:69, Type:create schema, State:synced, SchemaState:public, SchemaID:68, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:21.869 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:21.873 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=69]
   > [2024/06/18 16:12:21.873 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 16:12:21.876 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=13] [schemaVersion=42] [cur_db=testdb] [sql="\n--\n-- Table structure for table `t_q_zw9c`\n--\n\nDROP TABLE IF EXISTS `t_q_zw9c`;"] [user=root@127.0.0.1]
   > [2024/06/18 16:12:21.876 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=13] [schemaVersion=42] [cur_db=testdb] [sql="CREATE TABLE `t_q_zw9c` (\n  `c_qpjzzd` int(11) NOT NULL,\n  `c_1mp0eb` int(11) DEFAULT NULL,\n  `c_3dcuc` double DEFAULT NULL,\n  PRIMARY KEY (`c_qpjzzd`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/06/18 16:12:21.877 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:71, Type:create table, State:none, SchemaState:queueing, SchemaID:68, TableID:70, RowCount:0, ArgLen:1, start time: 2024-06-18 16:12:21.877 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 16:12:21.877 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:71, Type:create table, State:none, SchemaState:queueing, SchemaID:68, TableID:70, RowCount:0, ArgLen:1, start time: 2024-06-18 16:12:21.877 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="CREATE TABLE `t_q_zw9c` (\n  `c_qpjzzd` int(11) NOT NULL,\n  `c_1mp0eb` int(11) DEFAULT NULL,\n  `c_3dcuc` double DEFAULT NULL,\n  PRIMARY KEY (`c_qpjzzd`) /*T![clustered_index] CLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/18 16:12:21.877 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:71, Type:create table, State:none, SchemaState:queueing, SchemaID:68, TableID:70, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:21.877 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:21.878 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=42] [neededSchemaVersion=43] ["start time"=137.659µs] [phyTblIDs="[70]"] [actionTypes="[8]"]
   > [2024/06/18 16:12:21.880 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=43] ["take time"=2.029821ms] [job="ID:71, Type:create table, State:done, SchemaState:public, SchemaID:68, TableID:70, RowCount:0, ArgLen:1, start time: 2024-06-18 16:12:21.877 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:21.881 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:71, Type:create table, State:synced, SchemaState:public, SchemaID:68, TableID:70, RowCount:0, ArgLen:0, start time: 2024-06-18 16:12:21.877 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:12:21.881 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=71]
   > [2024/06/18 16:12:21.881 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 16:12:21.882 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=58] ["first split key"=748000000000000046]
   > [2024/06/18 16:12:21.882 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=13] [schemaVersion=43] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_q_zw9c` DISABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/06/18 16:12:21.882 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=58] ["first at"=748000000000000046] ["first new region left"="{Id:58 StartKey:7480000000000000ff4000000000000000f8 EndKey:7480000000000000ff4600000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:59 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/18 16:12:21.882 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[58]"]
   > [2024/06/18 16:12:21.883 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=13] [schemaVersion=43] [cur_db=testdb] [sql="/*!40000 ALTER TABLE `t_q_zw9c` ENABLE KEYS */;"] [user=root@127.0.0.1]
   > [2024/06/18 16:12:23.003 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=15] [user=root] [host=]
   > [2024/06/18 16:12:23.027 +00:00] [INFO] [set.go:139] ["set global var"] [conn=15] [name=tx_isolation] [val=READ-COMMITTED]
   > [2024/06/18 16:12:23.618 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=17] [user=root] [host=]
