# Bug ID TIDB-29947-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/29947
Original isolation level: IsolationLevel.REPEATABLE_READ
Tested isolation level:   IsolationLevel.REPEATABLE_READ


## Details
 * Database: tidb-5.2.1
 * Number of scenarios: 2
 * Initial setup script: /home/theodor/Projects/MasterThesis/data/sql/TIDB-29947_mysql_bk.sql

## Results
### Scenario 0
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  delete from t_tir89b where t_tir89b.c_3pcik >= t_tir89b.c_sroc_c;
     - TID: 0
     - Output: None
 * Instruction #2:
     - SQL:  select * from (select count(*) over (partition by ref_0.c_0b6nxb order by ref_0...
     - TID: 0
     - Output: [(2,), (3,)]

 * Container logs:
   > [2024/06/18 11:58:10.733 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=26] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:10.734 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=26] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:10.735 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:54, Type:create schema, State:none, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:10.735 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 11:58:10.735 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:54, Type:create schema, State:none, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:10.735 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/18 11:58:10.736 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:54, Type:create schema, State:none, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:10.735 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:10.737 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=26] [neededSchemaVersion=27] ["start time"=112.027µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 11:58:10.739 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=27] ["take time"=2.328533ms] [job="ID:54, Type:create schema, State:done, SchemaState:public, SchemaID:53, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:10.735 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:10.739 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:54, Type:create schema, State:synced, SchemaState:public, SchemaID:53, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:10.735 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:10.740 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=54]
   > [2024/06/18 11:58:10.740 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/18 11:58:10.744 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=27] [cur_db=testdb] [sql="drop table if exists t_tir89b, t_vejdy;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:10.745 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=27] [cur_db=testdb] [sql="\nCREATE TABLE `t_tir89b` (\n`c_3pcik` int(11) DEFAULT NULL,\n`c_0b6nxb` text DEFAULT NULL,\n`c_qytrlc` double NOT NULL,\n`c_sroc_c` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_qytrlc`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:10.747 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:56, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:55, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:10.746 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 11:58:10.747 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:56, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:55, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:10.746 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="\nCREATE TABLE `t_tir89b` (\n`c_3pcik` int(11) DEFAULT NULL,\n`c_0b6nxb` text DEFAULT NULL,\n`c_qytrlc` double NOT NULL,\n`c_sroc_c` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_qytrlc`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/18 11:58:10.747 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:56, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:55, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:10.746 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:10.749 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=27] [neededSchemaVersion=28] ["start time"=381.058µs] [phyTblIDs="[55]"] [actionTypes="[8]"]
   > [2024/06/18 11:58:10.751 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=28] ["take time"=2.035336ms] [job="ID:56, Type:create table, State:done, SchemaState:public, SchemaID:53, TableID:55, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:10.746 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:10.752 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:56, Type:create table, State:synced, SchemaState:public, SchemaID:53, TableID:55, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:10.746 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:10.753 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=56]
   > [2024/06/18 11:58:10.754 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/18 11:58:10.754 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=50] ["first split key"=748000000000000037]
   > [2024/06/18 11:58:10.754 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=50] ["first at"=748000000000000037] ["first new region left"="{Id:50 StartKey:7480000000000000ff3300000000000000f8 EndKey:7480000000000000ff3700000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:51 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/18 11:58:10.754 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[50]"]
   > [2024/06/18 11:58:10.756 +00:00] [WARN] [2pc.go:1598] ["schemaLeaseChecker is not set for this transaction"] [sessionID=5] [startTS=450550009890078721] [commitTS=450550009890340864]
   > [2024/06/18 11:58:10.758 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=28] [cur_db=testdb] [sql="\nCREATE TABLE `t_vejdy` (\n`c_iovir` int(11) NOT NULL,\n`c_r_mw3d` double DEFAULT NULL,\n`c_uxhghb` int(11) DEFAULT NULL,\n`c_rb7otb` int(11) NOT NULL,\n`c_dplyac` int(11) DEFAULT NULL,\n`c_lmcqed` double DEFAULT NULL,\n`c_ayaoed` text DEFAULT NULL,\n`c__zbqr` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_iovir`,`c_rb7otb`) /*T![clustered_index] NONCLUSTERED */,\nKEY `t_e1ejcd` (`c_uxhghb`),\nKEY `t_o6ui_b` (`c_iovir`,`c_r_mw3d`,`c_uxhghb`,`c_rb7otb`,`c_dplyac`,`c_lmcqed`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:10.760 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:58, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:57, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:10.759 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 11:58:10.760 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:58, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:57, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:10.759 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="\nCREATE TABLE `t_vejdy` (\n`c_iovir` int(11) NOT NULL,\n`c_r_mw3d` double DEFAULT NULL,\n`c_uxhghb` int(11) DEFAULT NULL,\n`c_rb7otb` int(11) NOT NULL,\n`c_dplyac` int(11) DEFAULT NULL,\n`c_lmcqed` double DEFAULT NULL,\n`c_ayaoed` text DEFAULT NULL,\n`c__zbqr` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_iovir`,`c_rb7otb`) /*T![clustered_index] NONCLUSTERED */,\nKEY `t_e1ejcd` (`c_uxhghb`),\nKEY `t_o6ui_b` (`c_iovir`,`c_r_mw3d`,`c_uxhghb`,`c_rb7otb`,`c_dplyac`,`c_lmcqed`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/18 11:58:10.760 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:58, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:57, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:10.759 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:10.762 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=28] [neededSchemaVersion=29] ["start time"=509.078µs] [phyTblIDs="[57]"] [actionTypes="[8]"]
   > [2024/06/18 11:58:10.764 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=29] ["take time"=2.077171ms] [job="ID:58, Type:create table, State:done, SchemaState:public, SchemaID:53, TableID:57, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:10.759 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:10.765 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:58, Type:create table, State:synced, SchemaState:public, SchemaID:53, TableID:57, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:10.759 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:10.766 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=58]
   > [2024/06/18 11:58:10.766 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/18 11:58:10.766 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=52] ["first split key"=748000000000000039]
   > [2024/06/18 11:58:10.766 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=52] ["first at"=748000000000000039] ["first new region left"="{Id:52 StartKey:7480000000000000ff3700000000000000f8 EndKey:7480000000000000ff3900000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:53 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/18 11:58:10.766 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[52]"]
   > [2024/06/18 11:58:10.767 +00:00] [WARN] [2pc.go:1598] ["schemaLeaseChecker is not set for this transaction"] [sessionID=5] [startTS=450550009893224449] [commitTS=450550009893224450]
   > [2024/06/18 11:58:11.820 +00:00] [INFO] [set.go:127] ["set global var"] [conn=7] [name=tx_isolation] [val=REPEATABLE-READ]

### Scenario 1
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  start transaction;
     - TID: 0
     - Output: None
 * Instruction #2:
     - SQL:  delete from t_tir89b where t_tir89b.c_3pcik >= t_tir89b.c_sroc_c;
     - TID: 0
     - Output: None
 * Instruction #3:
     - SQL:  select * from (select count(*) over (partition by ref_0.c_0b6nxb order by ref_0...
     - TID: 0
     - Output: []
 * Instruction #4:
     - SQL:  commit;
     - TID: 0
     - Output: None

 * Container logs:
   > [2024/06/18 11:58:14.059 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=37] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:14.060 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:65, Type:drop schema, State:none, SchemaState:queueing, SchemaID:60, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:14.059 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 11:58:14.060 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:65, Type:drop schema, State:none, SchemaState:queueing, SchemaID:60, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:14.059 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/06/18 11:58:14.061 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:drop schema, State:none, SchemaState:queueing, SchemaID:60, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:14.059 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:14.062 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=37] [neededSchemaVersion=38] ["start time"=100.713µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 11:58:14.064 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=38] ["take time"=2.293052ms] [job="ID:65, Type:drop schema, State:running, SchemaState:write only, SchemaID:60, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:14.059 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:14.064 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:drop schema, State:running, SchemaState:write only, SchemaID:60, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:14.059 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:14.065 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=38] [neededSchemaVersion=39] ["start time"=97.36µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 11:58:14.068 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=39] ["take time"=3.045041ms] [job="ID:65, Type:drop schema, State:running, SchemaState:delete only, SchemaID:60, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:14.059 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:14.069 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:drop schema, State:running, SchemaState:delete only, SchemaID:60, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:14.059 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:14.070 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=39] [neededSchemaVersion=40] ["start time"=94.915µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 11:58:14.073 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=40] ["take time"=2.844595ms] [job="ID:65, Type:drop schema, State:done, SchemaState:queueing, SchemaID:60, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:14.059 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:14.073 +00:00] [INFO] [delete_range.go:106] ["[ddl] add job into delete-range table"] [jobID=65] [jobType="drop schema"]
   > [2024/06/18 11:58:14.073 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:60, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:14.059 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:14.075 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=65]
   > [2024/06/18 11:58:14.075 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/18 11:58:14.076 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=40] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:14.078 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:67, Type:create schema, State:none, SchemaState:queueing, SchemaID:66, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:14.077 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 11:58:14.078 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:67, Type:create schema, State:none, SchemaState:queueing, SchemaID:66, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:14.077 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/18 11:58:14.078 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:create schema, State:none, SchemaState:queueing, SchemaID:66, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:14.077 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:14.079 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=40] [neededSchemaVersion=41] ["start time"=152.046µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 11:58:14.081 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=41] ["take time"=2.16154ms] [job="ID:67, Type:create schema, State:done, SchemaState:public, SchemaID:66, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:14.077 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:14.082 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:67, Type:create schema, State:synced, SchemaState:public, SchemaID:66, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:14.077 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:14.082 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=67]
   > [2024/06/18 11:58:14.083 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/18 11:58:14.086 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=41] [cur_db=testdb] [sql="drop table if exists t_tir89b, t_vejdy;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:14.086 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=41] [cur_db=testdb] [sql="\nCREATE TABLE `t_tir89b` (\n`c_3pcik` int(11) DEFAULT NULL,\n`c_0b6nxb` text DEFAULT NULL,\n`c_qytrlc` double NOT NULL,\n`c_sroc_c` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_qytrlc`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:14.088 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:69, Type:create table, State:none, SchemaState:queueing, SchemaID:66, TableID:68, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:14.087 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 11:58:14.088 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:69, Type:create table, State:none, SchemaState:queueing, SchemaID:66, TableID:68, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:14.087 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="\nCREATE TABLE `t_tir89b` (\n`c_3pcik` int(11) DEFAULT NULL,\n`c_0b6nxb` text DEFAULT NULL,\n`c_qytrlc` double NOT NULL,\n`c_sroc_c` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_qytrlc`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/18 11:58:14.089 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:69, Type:create table, State:none, SchemaState:queueing, SchemaID:66, TableID:68, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:14.087 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:14.090 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=41] [neededSchemaVersion=42] ["start time"=371.559µs] [phyTblIDs="[68]"] [actionTypes="[8]"]
   > [2024/06/18 11:58:14.092 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=42] ["take time"=2.077241ms] [job="ID:69, Type:create table, State:done, SchemaState:public, SchemaID:66, TableID:68, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:14.087 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:14.093 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:69, Type:create table, State:synced, SchemaState:public, SchemaID:66, TableID:68, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:14.087 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:14.093 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=69]
   > [2024/06/18 11:58:14.093 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/18 11:58:14.094 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=56] ["first split key"=748000000000000044]
   > [2024/06/18 11:58:14.094 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=56] ["first at"=748000000000000044] ["first new region left"="{Id:56 StartKey:7480000000000000ff3e00000000000000f8 EndKey:7480000000000000ff4400000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:57 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/18 11:58:14.094 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[56]"]
   > [2024/06/18 11:58:14.095 +00:00] [WARN] [2pc.go:1598] ["schemaLeaseChecker is not set for this transaction"] [sessionID=11] [startTS=450550010765639681] [commitTS=450550010765639682]
   > [2024/06/18 11:58:14.098 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=42] [cur_db=testdb] [sql="\nCREATE TABLE `t_vejdy` (\n`c_iovir` int(11) NOT NULL,\n`c_r_mw3d` double DEFAULT NULL,\n`c_uxhghb` int(11) DEFAULT NULL,\n`c_rb7otb` int(11) NOT NULL,\n`c_dplyac` int(11) DEFAULT NULL,\n`c_lmcqed` double DEFAULT NULL,\n`c_ayaoed` text DEFAULT NULL,\n`c__zbqr` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_iovir`,`c_rb7otb`) /*T![clustered_index] NONCLUSTERED */,\nKEY `t_e1ejcd` (`c_uxhghb`),\nKEY `t_o6ui_b` (`c_iovir`,`c_r_mw3d`,`c_uxhghb`,`c_rb7otb`,`c_dplyac`,`c_lmcqed`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:14.099 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:71, Type:create table, State:none, SchemaState:queueing, SchemaID:66, TableID:70, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:14.098 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 11:58:14.099 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:71, Type:create table, State:none, SchemaState:queueing, SchemaID:66, TableID:70, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:14.098 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="\nCREATE TABLE `t_vejdy` (\n`c_iovir` int(11) NOT NULL,\n`c_r_mw3d` double DEFAULT NULL,\n`c_uxhghb` int(11) DEFAULT NULL,\n`c_rb7otb` int(11) NOT NULL,\n`c_dplyac` int(11) DEFAULT NULL,\n`c_lmcqed` double DEFAULT NULL,\n`c_ayaoed` text DEFAULT NULL,\n`c__zbqr` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_iovir`,`c_rb7otb`) /*T![clustered_index] NONCLUSTERED */,\nKEY `t_e1ejcd` (`c_uxhghb`),\nKEY `t_o6ui_b` (`c_iovir`,`c_r_mw3d`,`c_uxhghb`,`c_rb7otb`,`c_dplyac`,`c_lmcqed`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/18 11:58:14.100 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:71, Type:create table, State:none, SchemaState:queueing, SchemaID:66, TableID:70, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:14.098 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:14.102 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=42] [neededSchemaVersion=43] ["start time"=585.276µs] [phyTblIDs="[70]"] [actionTypes="[8]"]
   > [2024/06/18 11:58:14.104 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=43] ["take time"=2.251007ms] [job="ID:71, Type:create table, State:done, SchemaState:public, SchemaID:66, TableID:70, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:14.098 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:14.106 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:71, Type:create table, State:synced, SchemaState:public, SchemaID:66, TableID:70, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:14.098 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:14.107 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=71]
   > [2024/06/18 11:58:14.107 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/18 11:58:14.108 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=58] ["first split key"=748000000000000046]
   > [2024/06/18 11:58:14.108 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=58] ["first at"=748000000000000046] ["first new region left"="{Id:58 StartKey:7480000000000000ff4400000000000000f8 EndKey:7480000000000000ff4600000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:59 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/18 11:58:14.108 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[58]"]
   > [2024/06/18 11:58:14.110 +00:00] [WARN] [2pc.go:1598] ["schemaLeaseChecker is not set for this transaction"] [sessionID=11] [startTS=450550010769309697] [commitTS=450550010769309698]
   > [2024/06/18 11:58:15.161 +00:00] [INFO] [set.go:127] ["set global var"] [conn=13] [name=tx_isolation] [val=REPEATABLE-READ]
