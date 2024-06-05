# Bug ID tidb-29947-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/29947
Original isolation level: IsolationLevel.REPEATABLE_READ
Tested isolation level:   IsolationLevel.REPEATABLE_READ


## Details
 * Database: tidb-5.2.1
 * Number of scenarios: 2
 * Initial setup script: /home/theodor/Projects/MasterThesis/data/sql/tidb-29947_mysql_bk.sql

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
   > [2024/06/05 19:02:04.044 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=26] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/06/05 19:02:04.045 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=26] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/06/05 19:02:04.046 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:54, Type:create schema, State:none, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-05 19:02:04.045 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/05 19:02:04.046 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:54, Type:create schema, State:none, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-05 19:02:04.045 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/05 19:02:04.047 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:54, Type:create schema, State:none, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:04.045 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:04.048 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=26] [neededSchemaVersion=27] ["start time"=139.195µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/05 19:02:04.049 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=27] ["take time"=2.025283ms] [job="ID:54, Type:create schema, State:done, SchemaState:public, SchemaID:53, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-05 19:02:04.045 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:04.050 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:54, Type:create schema, State:synced, SchemaState:public, SchemaID:53, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:04.045 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:04.050 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=54]
   > [2024/06/05 19:02:04.051 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/05 19:02:04.053 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=27] [cur_db=testdb] [sql="drop table if exists t_tir89b, t_vejdy;"] [user=root@127.0.0.1]
   > [2024/06/05 19:02:04.053 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=27] [cur_db=testdb] [sql="\nCREATE TABLE `t_tir89b` (\n`c_3pcik` int(11) DEFAULT NULL,\n`c_0b6nxb` text DEFAULT NULL,\n`c_qytrlc` double NOT NULL,\n`c_sroc_c` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_qytrlc`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/06/05 19:02:04.055 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:56, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:55, RowCount:0, ArgLen:1, start time: 2024-06-05 19:02:04.054 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/05 19:02:04.055 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:56, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:55, RowCount:0, ArgLen:1, start time: 2024-06-05 19:02:04.054 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="\nCREATE TABLE `t_tir89b` (\n`c_3pcik` int(11) DEFAULT NULL,\n`c_0b6nxb` text DEFAULT NULL,\n`c_qytrlc` double NOT NULL,\n`c_sroc_c` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_qytrlc`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/05 19:02:04.055 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:56, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:55, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:04.054 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:04.057 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=27] [neededSchemaVersion=28] ["start time"=369.046µs] [phyTblIDs="[55]"] [actionTypes="[8]"]
   > [2024/06/05 19:02:04.059 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=28] ["take time"=2.212739ms] [job="ID:56, Type:create table, State:done, SchemaState:public, SchemaID:53, TableID:55, RowCount:0, ArgLen:1, start time: 2024-06-05 19:02:04.054 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:04.060 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:56, Type:create table, State:synced, SchemaState:public, SchemaID:53, TableID:55, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:04.054 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:04.061 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=56]
   > [2024/06/05 19:02:04.061 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/05 19:02:04.061 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=50] ["first split key"=748000000000000037]
   > [2024/06/05 19:02:04.061 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=50] ["first at"=748000000000000037] ["first new region left"="{Id:50 StartKey:7480000000000000ff3300000000000000f8 EndKey:7480000000000000ff3700000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:51 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/05 19:02:04.061 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[50]"]
   > [2024/06/05 19:02:04.062 +00:00] [WARN] [2pc.go:1598] ["schemaLeaseChecker is not set for this transaction"] [sessionID=5] [startTS=450262236938108929] [commitTS=450262236938108930]
   > [2024/06/05 19:02:04.065 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=28] [cur_db=testdb] [sql="\nCREATE TABLE `t_vejdy` (\n`c_iovir` int(11) NOT NULL,\n`c_r_mw3d` double DEFAULT NULL,\n`c_uxhghb` int(11) DEFAULT NULL,\n`c_rb7otb` int(11) NOT NULL,\n`c_dplyac` int(11) DEFAULT NULL,\n`c_lmcqed` double DEFAULT NULL,\n`c_ayaoed` text DEFAULT NULL,\n`c__zbqr` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_iovir`,`c_rb7otb`) /*T![clustered_index] NONCLUSTERED */,\nKEY `t_e1ejcd` (`c_uxhghb`),\nKEY `t_o6ui_b` (`c_iovir`,`c_r_mw3d`,`c_uxhghb`,`c_rb7otb`,`c_dplyac`,`c_lmcqed`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/06/05 19:02:04.066 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:58, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:57, RowCount:0, ArgLen:1, start time: 2024-06-05 19:02:04.066 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/05 19:02:04.066 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:58, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:57, RowCount:0, ArgLen:1, start time: 2024-06-05 19:02:04.066 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="\nCREATE TABLE `t_vejdy` (\n`c_iovir` int(11) NOT NULL,\n`c_r_mw3d` double DEFAULT NULL,\n`c_uxhghb` int(11) DEFAULT NULL,\n`c_rb7otb` int(11) NOT NULL,\n`c_dplyac` int(11) DEFAULT NULL,\n`c_lmcqed` double DEFAULT NULL,\n`c_ayaoed` text DEFAULT NULL,\n`c__zbqr` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_iovir`,`c_rb7otb`) /*T![clustered_index] NONCLUSTERED */,\nKEY `t_e1ejcd` (`c_uxhghb`),\nKEY `t_o6ui_b` (`c_iovir`,`c_r_mw3d`,`c_uxhghb`,`c_rb7otb`,`c_dplyac`,`c_lmcqed`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/05 19:02:04.067 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:58, Type:create table, State:none, SchemaState:queueing, SchemaID:53, TableID:57, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:04.066 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:04.070 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=28] [neededSchemaVersion=29] ["start time"=431.834µs] [phyTblIDs="[57]"] [actionTypes="[8]"]
   > [2024/06/05 19:02:04.071 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=29] ["take time"=2.034223ms] [job="ID:58, Type:create table, State:done, SchemaState:public, SchemaID:53, TableID:57, RowCount:0, ArgLen:1, start time: 2024-06-05 19:02:04.066 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:04.073 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:58, Type:create table, State:synced, SchemaState:public, SchemaID:53, TableID:57, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:04.066 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:04.074 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=58]
   > [2024/06/05 19:02:04.074 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/05 19:02:04.074 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=52] ["first split key"=748000000000000039]
   > [2024/06/05 19:02:04.075 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=52] ["first at"=748000000000000039] ["first new region left"="{Id:52 StartKey:7480000000000000ff3700000000000000f8 EndKey:7480000000000000ff3900000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:53 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/05 19:02:04.075 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[52]"]
   > [2024/06/05 19:02:04.076 +00:00] [WARN] [2pc.go:1598] ["schemaLeaseChecker is not set for this transaction"] [sessionID=5] [startTS=450262236941778945] [commitTS=450262236941778946]
   > [2024/06/05 19:02:05.313 +00:00] [INFO] [set.go:127] ["set global var"] [conn=7] [name=tx_isolation] [val=REPEATABLE-READ]

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
   > [2024/06/05 19:02:05.951 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=29] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/06/05 19:02:05.951 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:59, Type:drop schema, State:none, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:05.951 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/05 19:02:05.951 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:59, Type:drop schema, State:none, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:05.951 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/06/05 19:02:05.952 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:59, Type:drop schema, State:none, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:05.951 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:05.953 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=29] [neededSchemaVersion=30] ["start time"=113.214µs] [phyTblIDs="[55,57]"] [actionTypes="[4,4]"]
   > [2024/06/05 19:02:05.955 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=30] ["take time"=2.253177ms] [job="ID:59, Type:drop schema, State:running, SchemaState:write only, SchemaID:53, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:05.951 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:05.955 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:59, Type:drop schema, State:running, SchemaState:write only, SchemaID:53, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:05.951 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:05.957 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=30] [neededSchemaVersion=31] ["start time"=118.383µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/05 19:02:05.959 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=31] ["take time"=2.264073ms] [job="ID:59, Type:drop schema, State:running, SchemaState:delete only, SchemaID:53, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:05.951 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:05.959 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:59, Type:drop schema, State:running, SchemaState:delete only, SchemaID:53, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:05.951 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:05.961 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=31] [neededSchemaVersion=32] ["start time"=110.141µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/05 19:02:05.963 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=32] ["take time"=2.15442ms] [job="ID:59, Type:drop schema, State:done, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-05 19:02:05.951 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:05.963 +00:00] [INFO] [delete_range.go:439] ["[ddl] batch insert into delete-range table"] [jobID=59] [elementIDs="[55,57]"]
   > [2024/06/05 19:02:05.965 +00:00] [INFO] [delete_range.go:106] ["[ddl] add job into delete-range table"] [jobID=59] [jobType="drop schema"]
   > [2024/06/05 19:02:05.966 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:59, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:53, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-05 19:02:05.951 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:05.967 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=59]
   > [2024/06/05 19:02:05.967 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/05 19:02:05.968 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=32] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/06/05 19:02:05.969 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:61, Type:create schema, State:none, SchemaState:queueing, SchemaID:60, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-05 19:02:05.969 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/05 19:02:05.969 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:61, Type:create schema, State:none, SchemaState:queueing, SchemaID:60, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-05 19:02:05.969 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/05 19:02:05.970 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:61, Type:create schema, State:none, SchemaState:queueing, SchemaID:60, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:05.969 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:05.970 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=32] [neededSchemaVersion=33] ["start time"=154.84µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/05 19:02:05.972 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=33] ["take time"=2.077455ms] [job="ID:61, Type:create schema, State:done, SchemaState:public, SchemaID:60, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-05 19:02:05.969 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:05.973 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:61, Type:create schema, State:synced, SchemaState:public, SchemaID:60, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:05.969 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:05.974 +00:00] [INFO] [delete_range.go:236] ["[ddl] delRange emulator complete task"] [jobID=59] [elementID=55]
   > [2024/06/05 19:02:05.974 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=61]
   > [2024/06/05 19:02:05.974 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/05 19:02:05.977 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=33] [cur_db=testdb] [sql="drop table if exists t_tir89b, t_vejdy;"] [user=root@127.0.0.1]
   > [2024/06/05 19:02:05.977 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=33] [cur_db=testdb] [sql="\nCREATE TABLE `t_tir89b` (\n`c_3pcik` int(11) DEFAULT NULL,\n`c_0b6nxb` text DEFAULT NULL,\n`c_qytrlc` double NOT NULL,\n`c_sroc_c` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_qytrlc`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/06/05 19:02:05.979 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:63, Type:create table, State:none, SchemaState:queueing, SchemaID:60, TableID:62, RowCount:0, ArgLen:1, start time: 2024-06-05 19:02:05.978 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/05 19:02:05.979 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:63, Type:create table, State:none, SchemaState:queueing, SchemaID:60, TableID:62, RowCount:0, ArgLen:1, start time: 2024-06-05 19:02:05.978 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="\nCREATE TABLE `t_tir89b` (\n`c_3pcik` int(11) DEFAULT NULL,\n`c_0b6nxb` text DEFAULT NULL,\n`c_qytrlc` double NOT NULL,\n`c_sroc_c` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_qytrlc`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/05 19:02:05.979 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:63, Type:create table, State:none, SchemaState:queueing, SchemaID:60, TableID:62, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:05.978 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:05.981 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=33] [neededSchemaVersion=34] ["start time"=348.302µs] [phyTblIDs="[62]"] [actionTypes="[8]"]
   > [2024/06/05 19:02:05.981 +00:00] [INFO] [delete_range.go:236] ["[ddl] delRange emulator complete task"] [jobID=59] [elementID=57]
   > [2024/06/05 19:02:05.983 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=34] ["take time"=2.141081ms] [job="ID:63, Type:create table, State:done, SchemaState:public, SchemaID:60, TableID:62, RowCount:0, ArgLen:1, start time: 2024-06-05 19:02:05.978 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:05.983 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:63, Type:create table, State:synced, SchemaState:public, SchemaID:60, TableID:62, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:05.978 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:05.984 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=63]
   > [2024/06/05 19:02:05.984 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/05 19:02:05.985 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=54] ["first split key"=74800000000000003e]
   > [2024/06/05 19:02:05.985 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=54] ["first at"=74800000000000003e] ["first new region left"="{Id:54 StartKey:7480000000000000ff3900000000000000f8 EndKey:7480000000000000ff3e00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:55 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/05 19:02:05.985 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[54]"]
   > [2024/06/05 19:02:05.986 +00:00] [WARN] [2pc.go:1598] ["schemaLeaseChecker is not set for this transaction"] [sessionID=11] [startTS=450262237442473985] [commitTS=450262237442473986]
   > [2024/06/05 19:02:05.988 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=34] [cur_db=testdb] [sql="\nCREATE TABLE `t_vejdy` (\n`c_iovir` int(11) NOT NULL,\n`c_r_mw3d` double DEFAULT NULL,\n`c_uxhghb` int(11) DEFAULT NULL,\n`c_rb7otb` int(11) NOT NULL,\n`c_dplyac` int(11) DEFAULT NULL,\n`c_lmcqed` double DEFAULT NULL,\n`c_ayaoed` text DEFAULT NULL,\n`c__zbqr` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_iovir`,`c_rb7otb`) /*T![clustered_index] NONCLUSTERED */,\nKEY `t_e1ejcd` (`c_uxhghb`),\nKEY `t_o6ui_b` (`c_iovir`,`c_r_mw3d`,`c_uxhghb`,`c_rb7otb`,`c_dplyac`,`c_lmcqed`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/06/05 19:02:05.990 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:65, Type:create table, State:none, SchemaState:queueing, SchemaID:60, TableID:64, RowCount:0, ArgLen:1, start time: 2024-06-05 19:02:05.989 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/05 19:02:05.990 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:65, Type:create table, State:none, SchemaState:queueing, SchemaID:60, TableID:64, RowCount:0, ArgLen:1, start time: 2024-06-05 19:02:05.989 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="\nCREATE TABLE `t_vejdy` (\n`c_iovir` int(11) NOT NULL,\n`c_r_mw3d` double DEFAULT NULL,\n`c_uxhghb` int(11) DEFAULT NULL,\n`c_rb7otb` int(11) NOT NULL,\n`c_dplyac` int(11) DEFAULT NULL,\n`c_lmcqed` double DEFAULT NULL,\n`c_ayaoed` text DEFAULT NULL,\n`c__zbqr` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_iovir`,`c_rb7otb`) /*T![clustered_index] NONCLUSTERED */,\nKEY `t_e1ejcd` (`c_uxhghb`),\nKEY `t_o6ui_b` (`c_iovir`,`c_r_mw3d`,`c_uxhghb`,`c_rb7otb`,`c_dplyac`,`c_lmcqed`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/05 19:02:05.991 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:create table, State:none, SchemaState:queueing, SchemaID:60, TableID:64, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:05.989 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:05.993 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=34] [neededSchemaVersion=35] ["start time"=633.328µs] [phyTblIDs="[64]"] [actionTypes="[8]"]
   > [2024/06/05 19:02:05.995 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=35] ["take time"=2.252759ms] [job="ID:65, Type:create table, State:done, SchemaState:public, SchemaID:60, TableID:64, RowCount:0, ArgLen:1, start time: 2024-06-05 19:02:05.989 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:05.996 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:65, Type:create table, State:synced, SchemaState:public, SchemaID:60, TableID:64, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:05.989 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:05.998 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=65]
   > [2024/06/05 19:02:05.998 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/05 19:02:05.998 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=56] ["first split key"=748000000000000040]
   > [2024/06/05 19:02:05.998 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=56] ["first at"=748000000000000040] ["first new region left"="{Id:56 StartKey:7480000000000000ff3e00000000000000f8 EndKey:7480000000000000ff4000000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:57 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/05 19:02:05.998 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[56]"]
   > [2024/06/05 19:02:06.000 +00:00] [WARN] [2pc.go:1598] ["schemaLeaseChecker is not set for this transaction"] [sessionID=11] [startTS=450262237445881857] [commitTS=450262237446144000]
   > [2024/06/05 19:02:07.241 +00:00] [INFO] [set.go:127] ["set global var"] [conn=13] [name=tx_isolation] [val=REPEATABLE-READ]
