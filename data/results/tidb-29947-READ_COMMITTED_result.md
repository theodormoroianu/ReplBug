# Bug ID tidb-29947-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/29947
Original isolation level: IsolationLevel.REPEATABLE_READ
Tested isolation level:   IsolationLevel.READ_COMMITTED


## Details
 * Database: tidb-5.2.1
 * Number of scenarios: 2
 * Initial setup script: /home/theodor/Projects/MasterThesis/data/sql/tidb-29947_mysql_bk.sql

## Results
### Scenario 0
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
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
   > [2024/06/05 19:02:08.323 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=35] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/06/05 19:02:08.324 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:66, Type:drop schema, State:none, SchemaState:queueing, SchemaID:60, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:08.323 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/05 19:02:08.324 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:66, Type:drop schema, State:none, SchemaState:queueing, SchemaID:60, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:08.323 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/06/05 19:02:08.324 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:drop schema, State:none, SchemaState:queueing, SchemaID:60, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:08.323 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:08.325 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=35] [neededSchemaVersion=36] ["start time"=52.032µs] [phyTblIDs="[62,64]"] [actionTypes="[4,4]"]
   > [2024/06/05 19:02:08.327 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=36] ["take time"=2.216999ms] [job="ID:66, Type:drop schema, State:running, SchemaState:write only, SchemaID:60, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:08.323 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:08.328 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:drop schema, State:running, SchemaState:write only, SchemaID:60, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:08.323 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:08.329 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=36] [neededSchemaVersion=37] ["start time"=119.43µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/05 19:02:08.332 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=37] ["take time"=3.041765ms] [job="ID:66, Type:drop schema, State:running, SchemaState:delete only, SchemaID:60, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:08.323 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:08.332 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:drop schema, State:running, SchemaState:delete only, SchemaID:60, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:08.323 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:08.334 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=37] [neededSchemaVersion=38] ["start time"=107.976µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/05 19:02:08.336 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=38] ["take time"=2.1459ms] [job="ID:66, Type:drop schema, State:done, SchemaState:queueing, SchemaID:60, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-05 19:02:08.323 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:08.336 +00:00] [INFO] [delete_range.go:439] ["[ddl] batch insert into delete-range table"] [jobID=66] [elementIDs="[62,64]"]
   > [2024/06/05 19:02:08.337 +00:00] [INFO] [delete_range.go:106] ["[ddl] add job into delete-range table"] [jobID=66] [jobType="drop schema"]
   > [2024/06/05 19:02:08.337 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:66, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:60, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-05 19:02:08.323 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:08.338 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=66]
   > [2024/06/05 19:02:08.338 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/05 19:02:08.339 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=38] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/06/05 19:02:08.341 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:68, Type:create schema, State:none, SchemaState:queueing, SchemaID:67, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-05 19:02:08.34 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/05 19:02:08.341 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:68, Type:create schema, State:none, SchemaState:queueing, SchemaID:67, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-05 19:02:08.34 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/05 19:02:08.341 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:68, Type:create schema, State:none, SchemaState:queueing, SchemaID:67, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:08.34 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:08.343 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=38] [neededSchemaVersion=39] ["start time"=157.843µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/05 19:02:08.345 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=39] ["take time"=2.135424ms] [job="ID:68, Type:create schema, State:done, SchemaState:public, SchemaID:67, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-05 19:02:08.34 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:08.345 +00:00] [INFO] [delete_range.go:236] ["[ddl] delRange emulator complete task"] [jobID=66] [elementID=62]
   > [2024/06/05 19:02:08.345 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:68, Type:create schema, State:synced, SchemaState:public, SchemaID:67, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:08.34 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:08.346 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=68]
   > [2024/06/05 19:02:08.346 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/05 19:02:08.348 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=39] [cur_db=testdb] [sql="drop table if exists t_tir89b, t_vejdy;"] [user=root@127.0.0.1]
   > [2024/06/05 19:02:08.348 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=39] [cur_db=testdb] [sql="\nCREATE TABLE `t_tir89b` (\n`c_3pcik` int(11) DEFAULT NULL,\n`c_0b6nxb` text DEFAULT NULL,\n`c_qytrlc` double NOT NULL,\n`c_sroc_c` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_qytrlc`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/06/05 19:02:08.350 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:70, Type:create table, State:none, SchemaState:queueing, SchemaID:67, TableID:69, RowCount:0, ArgLen:1, start time: 2024-06-05 19:02:08.349 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/05 19:02:08.350 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:70, Type:create table, State:none, SchemaState:queueing, SchemaID:67, TableID:69, RowCount:0, ArgLen:1, start time: 2024-06-05 19:02:08.349 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="\nCREATE TABLE `t_tir89b` (\n`c_3pcik` int(11) DEFAULT NULL,\n`c_0b6nxb` text DEFAULT NULL,\n`c_qytrlc` double NOT NULL,\n`c_sroc_c` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_qytrlc`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/05 19:02:08.350 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:70, Type:create table, State:none, SchemaState:queueing, SchemaID:67, TableID:69, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:08.349 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:08.350 +00:00] [INFO] [delete_range.go:236] ["[ddl] delRange emulator complete task"] [jobID=66] [elementID=64]
   > [2024/06/05 19:02:08.352 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=39] [neededSchemaVersion=40] ["start time"=269.661µs] [phyTblIDs="[69]"] [actionTypes="[8]"]
   > [2024/06/05 19:02:08.354 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=40] ["take time"=2.255063ms] [job="ID:70, Type:create table, State:done, SchemaState:public, SchemaID:67, TableID:69, RowCount:0, ArgLen:1, start time: 2024-06-05 19:02:08.349 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:08.355 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:70, Type:create table, State:synced, SchemaState:public, SchemaID:67, TableID:69, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:08.349 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:08.356 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=70]
   > [2024/06/05 19:02:08.356 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/05 19:02:08.356 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=58] ["first split key"=748000000000000045]
   > [2024/06/05 19:02:08.356 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=58] ["first at"=748000000000000045] ["first new region left"="{Id:58 StartKey:7480000000000000ff4000000000000000f8 EndKey:7480000000000000ff4500000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:59 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/05 19:02:08.356 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[58]"]
   > [2024/06/05 19:02:08.357 +00:00] [WARN] [2pc.go:1598] ["schemaLeaseChecker is not set for this transaction"] [sessionID=17] [startTS=450262238064017409] [commitTS=450262238064017410]
   > [2024/06/05 19:02:08.358 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=40] [cur_db=testdb] [sql="\nCREATE TABLE `t_vejdy` (\n`c_iovir` int(11) NOT NULL,\n`c_r_mw3d` double DEFAULT NULL,\n`c_uxhghb` int(11) DEFAULT NULL,\n`c_rb7otb` int(11) NOT NULL,\n`c_dplyac` int(11) DEFAULT NULL,\n`c_lmcqed` double DEFAULT NULL,\n`c_ayaoed` text DEFAULT NULL,\n`c__zbqr` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_iovir`,`c_rb7otb`) /*T![clustered_index] NONCLUSTERED */,\nKEY `t_e1ejcd` (`c_uxhghb`),\nKEY `t_o6ui_b` (`c_iovir`,`c_r_mw3d`,`c_uxhghb`,`c_rb7otb`,`c_dplyac`,`c_lmcqed`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/06/05 19:02:08.359 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:72, Type:create table, State:none, SchemaState:queueing, SchemaID:67, TableID:71, RowCount:0, ArgLen:1, start time: 2024-06-05 19:02:08.359 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/05 19:02:08.359 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:72, Type:create table, State:none, SchemaState:queueing, SchemaID:67, TableID:71, RowCount:0, ArgLen:1, start time: 2024-06-05 19:02:08.359 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="\nCREATE TABLE `t_vejdy` (\n`c_iovir` int(11) NOT NULL,\n`c_r_mw3d` double DEFAULT NULL,\n`c_uxhghb` int(11) DEFAULT NULL,\n`c_rb7otb` int(11) NOT NULL,\n`c_dplyac` int(11) DEFAULT NULL,\n`c_lmcqed` double DEFAULT NULL,\n`c_ayaoed` text DEFAULT NULL,\n`c__zbqr` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_iovir`,`c_rb7otb`) /*T![clustered_index] NONCLUSTERED */,\nKEY `t_e1ejcd` (`c_uxhghb`),\nKEY `t_o6ui_b` (`c_iovir`,`c_r_mw3d`,`c_uxhghb`,`c_rb7otb`,`c_dplyac`,`c_lmcqed`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/05 19:02:08.360 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:72, Type:create table, State:none, SchemaState:queueing, SchemaID:67, TableID:71, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:08.359 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:08.363 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=40] [neededSchemaVersion=41] ["start time"=607.696µs] [phyTblIDs="[71]"] [actionTypes="[8]"]
   > [2024/06/05 19:02:08.364 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=41] ["take time"=2.266517ms] [job="ID:72, Type:create table, State:done, SchemaState:public, SchemaID:67, TableID:71, RowCount:0, ArgLen:1, start time: 2024-06-05 19:02:08.359 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:08.366 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:72, Type:create table, State:synced, SchemaState:public, SchemaID:67, TableID:71, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:08.359 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:08.367 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=72]
   > [2024/06/05 19:02:08.367 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/05 19:02:08.367 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=60] ["first split key"=748000000000000047]
   > [2024/06/05 19:02:08.368 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=60] ["first at"=748000000000000047] ["first new region left"="{Id:60 StartKey:7480000000000000ff4500000000000000f8 EndKey:7480000000000000ff4700000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:61 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/05 19:02:08.368 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[60]"]
   > [2024/06/05 19:02:08.369 +00:00] [WARN] [2pc.go:1598] ["schemaLeaseChecker is not set for this transaction"] [sessionID=17] [startTS=450262238066900993] [commitTS=450262238067163136]
   > [2024/06/05 19:02:09.616 +00:00] [INFO] [set.go:127] ["set global var"] [conn=19] [name=tx_isolation] [val=READ-COMMITTED]

### Scenario 1
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
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
   > [2024/06/05 19:02:10.344 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=23] [schemaVersion=41] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/06/05 19:02:10.345 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:73, Type:drop schema, State:none, SchemaState:queueing, SchemaID:67, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:10.344 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/05 19:02:10.345 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:73, Type:drop schema, State:none, SchemaState:queueing, SchemaID:67, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:10.344 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/06/05 19:02:10.346 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:73, Type:drop schema, State:none, SchemaState:queueing, SchemaID:67, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:10.344 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:10.347 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=41] [neededSchemaVersion=42] ["start time"=142.897µs] [phyTblIDs="[69,71]"] [actionTypes="[4,4]"]
   > [2024/06/05 19:02:10.350 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=42] ["take time"=2.682148ms] [job="ID:73, Type:drop schema, State:running, SchemaState:write only, SchemaID:67, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:10.344 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:10.350 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:73, Type:drop schema, State:running, SchemaState:write only, SchemaID:67, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:10.344 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:10.351 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=42] [neededSchemaVersion=43] ["start time"=95.404µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/05 19:02:10.353 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=43] ["take time"=2.247869ms] [job="ID:73, Type:drop schema, State:running, SchemaState:delete only, SchemaID:67, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:10.344 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:10.354 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:73, Type:drop schema, State:running, SchemaState:delete only, SchemaID:67, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:10.344 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:10.355 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=43] [neededSchemaVersion=44] ["start time"=105.81µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/05 19:02:10.358 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=44] ["take time"=2.927224ms] [job="ID:73, Type:drop schema, State:done, SchemaState:queueing, SchemaID:67, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-05 19:02:10.344 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:10.358 +00:00] [INFO] [delete_range.go:439] ["[ddl] batch insert into delete-range table"] [jobID=73] [elementIDs="[69,71]"]
   > [2024/06/05 19:02:10.360 +00:00] [INFO] [delete_range.go:106] ["[ddl] add job into delete-range table"] [jobID=73] [jobType="drop schema"]
   > [2024/06/05 19:02:10.360 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:73, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:67, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-05 19:02:10.344 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:10.361 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=73]
   > [2024/06/05 19:02:10.361 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/05 19:02:10.362 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=23] [schemaVersion=44] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/06/05 19:02:10.363 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:75, Type:create schema, State:none, SchemaState:queueing, SchemaID:74, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-05 19:02:10.363 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/05 19:02:10.363 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:75, Type:create schema, State:none, SchemaState:queueing, SchemaID:74, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-05 19:02:10.363 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/05 19:02:10.364 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:75, Type:create schema, State:none, SchemaState:queueing, SchemaID:74, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:10.363 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:10.365 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=44] [neededSchemaVersion=45] ["start time"=142.688µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/05 19:02:10.367 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=45] ["take time"=2.121107ms] [job="ID:75, Type:create schema, State:done, SchemaState:public, SchemaID:74, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-05 19:02:10.363 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:10.367 +00:00] [INFO] [delete_range.go:236] ["[ddl] delRange emulator complete task"] [jobID=73] [elementID=69]
   > [2024/06/05 19:02:10.367 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:75, Type:create schema, State:synced, SchemaState:public, SchemaID:74, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:10.363 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:10.368 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=75]
   > [2024/06/05 19:02:10.368 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/05 19:02:10.370 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=23] [schemaVersion=45] [cur_db=testdb] [sql="drop table if exists t_tir89b, t_vejdy;"] [user=root@127.0.0.1]
   > [2024/06/05 19:02:10.370 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=23] [schemaVersion=45] [cur_db=testdb] [sql="\nCREATE TABLE `t_tir89b` (\n`c_3pcik` int(11) DEFAULT NULL,\n`c_0b6nxb` text DEFAULT NULL,\n`c_qytrlc` double NOT NULL,\n`c_sroc_c` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_qytrlc`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/06/05 19:02:10.371 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:77, Type:create table, State:none, SchemaState:queueing, SchemaID:74, TableID:76, RowCount:0, ArgLen:1, start time: 2024-06-05 19:02:10.371 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/05 19:02:10.371 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:77, Type:create table, State:none, SchemaState:queueing, SchemaID:74, TableID:76, RowCount:0, ArgLen:1, start time: 2024-06-05 19:02:10.371 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="\nCREATE TABLE `t_tir89b` (\n`c_3pcik` int(11) DEFAULT NULL,\n`c_0b6nxb` text DEFAULT NULL,\n`c_qytrlc` double NOT NULL,\n`c_sroc_c` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_qytrlc`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/05 19:02:10.371 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:create table, State:none, SchemaState:queueing, SchemaID:74, TableID:76, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:10.371 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:10.373 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=45] [neededSchemaVersion=46] ["start time"=263.794µs] [phyTblIDs="[76]"] [actionTypes="[8]"]
   > [2024/06/05 19:02:10.373 +00:00] [INFO] [delete_range.go:236] ["[ddl] delRange emulator complete task"] [jobID=73] [elementID=71]
   > [2024/06/05 19:02:10.375 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=46] ["take time"=2.246682ms] [job="ID:77, Type:create table, State:done, SchemaState:public, SchemaID:74, TableID:76, RowCount:0, ArgLen:1, start time: 2024-06-05 19:02:10.371 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:10.375 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:77, Type:create table, State:synced, SchemaState:public, SchemaID:74, TableID:76, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:10.371 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:10.376 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=77]
   > [2024/06/05 19:02:10.376 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/05 19:02:10.376 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=62] ["first split key"=74800000000000004c]
   > [2024/06/05 19:02:10.377 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=62] ["first at"=74800000000000004c] ["first new region left"="{Id:62 StartKey:7480000000000000ff4700000000000000f8 EndKey:7480000000000000ff4c00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:63 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/05 19:02:10.377 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[62]"]
   > [2024/06/05 19:02:10.377 +00:00] [WARN] [2pc.go:1598] ["schemaLeaseChecker is not set for this transaction"] [sessionID=23] [startTS=450262238593548289] [commitTS=450262238593548290]
   > [2024/06/05 19:02:10.379 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=23] [schemaVersion=46] [cur_db=testdb] [sql="\nCREATE TABLE `t_vejdy` (\n`c_iovir` int(11) NOT NULL,\n`c_r_mw3d` double DEFAULT NULL,\n`c_uxhghb` int(11) DEFAULT NULL,\n`c_rb7otb` int(11) NOT NULL,\n`c_dplyac` int(11) DEFAULT NULL,\n`c_lmcqed` double DEFAULT NULL,\n`c_ayaoed` text DEFAULT NULL,\n`c__zbqr` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_iovir`,`c_rb7otb`) /*T![clustered_index] NONCLUSTERED */,\nKEY `t_e1ejcd` (`c_uxhghb`),\nKEY `t_o6ui_b` (`c_iovir`,`c_r_mw3d`,`c_uxhghb`,`c_rb7otb`,`c_dplyac`,`c_lmcqed`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/06/05 19:02:10.380 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:79, Type:create table, State:none, SchemaState:queueing, SchemaID:74, TableID:78, RowCount:0, ArgLen:1, start time: 2024-06-05 19:02:10.38 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/05 19:02:10.380 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:79, Type:create table, State:none, SchemaState:queueing, SchemaID:74, TableID:78, RowCount:0, ArgLen:1, start time: 2024-06-05 19:02:10.38 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="\nCREATE TABLE `t_vejdy` (\n`c_iovir` int(11) NOT NULL,\n`c_r_mw3d` double DEFAULT NULL,\n`c_uxhghb` int(11) DEFAULT NULL,\n`c_rb7otb` int(11) NOT NULL,\n`c_dplyac` int(11) DEFAULT NULL,\n`c_lmcqed` double DEFAULT NULL,\n`c_ayaoed` text DEFAULT NULL,\n`c__zbqr` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_iovir`,`c_rb7otb`) /*T![clustered_index] NONCLUSTERED */,\nKEY `t_e1ejcd` (`c_uxhghb`),\nKEY `t_o6ui_b` (`c_iovir`,`c_r_mw3d`,`c_uxhghb`,`c_rb7otb`,`c_dplyac`,`c_lmcqed`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/05 19:02:10.381 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:79, Type:create table, State:none, SchemaState:queueing, SchemaID:74, TableID:78, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:10.38 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:10.383 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=46] [neededSchemaVersion=47] ["start time"=498.394µs] [phyTblIDs="[78]"] [actionTypes="[8]"]
   > [2024/06/05 19:02:10.384 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=47] ["take time"=2.032755ms] [job="ID:79, Type:create table, State:done, SchemaState:public, SchemaID:74, TableID:78, RowCount:0, ArgLen:1, start time: 2024-06-05 19:02:10.38 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:10.385 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:79, Type:create table, State:synced, SchemaState:public, SchemaID:74, TableID:78, RowCount:0, ArgLen:0, start time: 2024-06-05 19:02:10.38 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/05 19:02:10.386 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=79]
   > [2024/06/05 19:02:10.386 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/05 19:02:10.386 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=64] ["first split key"=74800000000000004e]
   > [2024/06/05 19:02:10.386 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=64] ["first at"=74800000000000004e] ["first new region left"="{Id:64 StartKey:7480000000000000ff4c00000000000000f8 EndKey:7480000000000000ff4e00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:65 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/05 19:02:10.386 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[64]"]
   > [2024/06/05 19:02:10.388 +00:00] [WARN] [2pc.go:1598] ["schemaLeaseChecker is not set for this transaction"] [sessionID=23] [startTS=450262238596169729] [commitTS=450262238596431872]
   > [2024/06/05 19:02:11.633 +00:00] [INFO] [set.go:127] ["set global var"] [conn=25] [name=tx_isolation] [val=READ-COMMITTED]
