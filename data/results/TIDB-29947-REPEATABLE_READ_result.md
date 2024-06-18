# Bug ID TIDB-29947-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/29947
Original isolation level: IsolationLevel.REPEATABLE_READ
Tested isolation level:   IsolationLevel.REPEATABLE_READ


## Details
 * Database: tidb-v5.4.0
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
   > [2024/06/18 16:11:29.822 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=5] [user=root] [host=]
   > [2024/06/18 16:11:29.825 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=28] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/06/18 16:11:29.826 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=28] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/06/18 16:11:29.827 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:58, Type:create schema, State:none, SchemaState:queueing, SchemaID:57, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 16:11:29.826 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 16:11:29.827 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:58, Type:create schema, State:none, SchemaState:queueing, SchemaID:57, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 16:11:29.826 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/18 16:11:29.827 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:58, Type:create schema, State:none, SchemaState:queueing, SchemaID:57, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:11:29.826 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:11:29.828 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=28] [neededSchemaVersion=29] ["start time"=70.191µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 16:11:29.830 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=29] ["take time"=2.197022ms] [job="ID:58, Type:create schema, State:done, SchemaState:public, SchemaID:57, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 16:11:29.826 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:11:29.830 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:58, Type:create schema, State:synced, SchemaState:public, SchemaID:57, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:11:29.826 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:11:29.831 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=58]
   > [2024/06/18 16:11:29.831 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 16:11:29.833 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=29] [cur_db=testdb] [sql="drop table if exists t_tir89b, t_vejdy;"] [user=root@127.0.0.1]
   > [2024/06/18 16:11:29.833 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=29] [cur_db=testdb] [sql="\nCREATE TABLE `t_tir89b` (\n`c_3pcik` int(11) DEFAULT NULL,\n`c_0b6nxb` text DEFAULT NULL,\n`c_qytrlc` double NOT NULL,\n`c_sroc_c` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_qytrlc`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/06/18 16:11:29.834 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:60, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:59, RowCount:0, ArgLen:1, start time: 2024-06-18 16:11:29.833 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 16:11:29.834 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:60, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:59, RowCount:0, ArgLen:1, start time: 2024-06-18 16:11:29.833 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="\nCREATE TABLE `t_tir89b` (\n`c_3pcik` int(11) DEFAULT NULL,\n`c_0b6nxb` text DEFAULT NULL,\n`c_qytrlc` double NOT NULL,\n`c_sroc_c` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_qytrlc`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/18 16:11:29.834 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:60, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:59, RowCount:0, ArgLen:0, start time: 2024-06-18 16:11:29.833 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:11:29.835 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=29] [neededSchemaVersion=30] ["start time"=153.513µs] [phyTblIDs="[59]"] [actionTypes="[8]"]
   > [2024/06/18 16:11:29.837 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=30] ["take time"=2.133186ms] [job="ID:60, Type:create table, State:done, SchemaState:public, SchemaID:57, TableID:59, RowCount:0, ArgLen:1, start time: 2024-06-18 16:11:29.833 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:11:29.837 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:60, Type:create table, State:synced, SchemaState:public, SchemaID:57, TableID:59, RowCount:0, ArgLen:0, start time: 2024-06-18 16:11:29.833 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:11:29.837 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=60]
   > [2024/06/18 16:11:29.838 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 16:11:29.838 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=52] ["first split key"=74800000000000003b]
   > [2024/06/18 16:11:29.838 +00:00] [WARN] [2pc.go:1596] ["schemaLeaseChecker is not set for this transaction"] [sessionID=5] [startTS=450553994238492674] [commitTS=450553994238492675]
   > [2024/06/18 16:11:29.839 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=30] [cur_db=testdb] [sql="\nCREATE TABLE `t_vejdy` (\n`c_iovir` int(11) NOT NULL,\n`c_r_mw3d` double DEFAULT NULL,\n`c_uxhghb` int(11) DEFAULT NULL,\n`c_rb7otb` int(11) NOT NULL,\n`c_dplyac` int(11) DEFAULT NULL,\n`c_lmcqed` double DEFAULT NULL,\n`c_ayaoed` text DEFAULT NULL,\n`c__zbqr` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_iovir`,`c_rb7otb`) /*T![clustered_index] NONCLUSTERED */,\nKEY `t_e1ejcd` (`c_uxhghb`),\nKEY `t_o6ui_b` (`c_iovir`,`c_r_mw3d`,`c_uxhghb`,`c_rb7otb`,`c_dplyac`,`c_lmcqed`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/06/18 16:11:29.840 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:62, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:61, RowCount:0, ArgLen:1, start time: 2024-06-18 16:11:29.84 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 16:11:29.840 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=54] ["first at"=74800000000000003b] ["first new region left"="{Id:54 StartKey:7480000000000000ff3700000000000000f8 EndKey:7480000000000000ff3b00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:55 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/18 16:11:29.840 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[54]"]
   > [2024/06/18 16:11:29.840 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:62, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:61, RowCount:0, ArgLen:1, start time: 2024-06-18 16:11:29.84 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="\nCREATE TABLE `t_vejdy` (\n`c_iovir` int(11) NOT NULL,\n`c_r_mw3d` double DEFAULT NULL,\n`c_uxhghb` int(11) DEFAULT NULL,\n`c_rb7otb` int(11) NOT NULL,\n`c_dplyac` int(11) DEFAULT NULL,\n`c_lmcqed` double DEFAULT NULL,\n`c_ayaoed` text DEFAULT NULL,\n`c__zbqr` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_iovir`,`c_rb7otb`) /*T![clustered_index] NONCLUSTERED */,\nKEY `t_e1ejcd` (`c_uxhghb`),\nKEY `t_o6ui_b` (`c_iovir`,`c_r_mw3d`,`c_uxhghb`,`c_rb7otb`,`c_dplyac`,`c_lmcqed`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/18 16:11:29.840 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:62, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-06-18 16:11:29.84 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:11:29.842 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=30] [neededSchemaVersion=31] ["start time"=431.973µs] [phyTblIDs="[61]"] [actionTypes="[8]"]
   > [2024/06/18 16:11:29.844 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=31] ["take time"=2.21588ms] [job="ID:62, Type:create table, State:done, SchemaState:public, SchemaID:57, TableID:61, RowCount:0, ArgLen:1, start time: 2024-06-18 16:11:29.84 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:11:29.845 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:62, Type:create table, State:synced, SchemaState:public, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-06-18 16:11:29.84 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:11:29.846 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=62]
   > [2024/06/18 16:11:29.846 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 16:11:29.846 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=54] ["first split key"=74800000000000003d]
   > [2024/06/18 16:11:29.848 +00:00] [WARN] [2pc.go:1596] ["schemaLeaseChecker is not set for this transaction"] [sessionID=5] [startTS=450553994240851969] [commitTS=450553994241114112]
   > [2024/06/18 16:11:29.849 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=56] ["first at"=74800000000000003d] ["first new region left"="{Id:56 StartKey:7480000000000000ff3b00000000000000f8 EndKey:7480000000000000ff3d00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:57 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/18 16:11:29.849 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[56]"]
   > [2024/06/18 16:11:30.915 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=7] [user=root] [host=]
   > [2024/06/18 16:11:30.929 +00:00] [INFO] [set.go:139] ["set global var"] [conn=7] [name=tx_isolation] [val=REPEATABLE-READ]

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
   > [2024/06/18 16:11:33.205 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=11] [user=root] [host=]
   > [2024/06/18 16:11:33.208 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=39] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/06/18 16:11:33.209 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:69, Type:drop schema, State:none, SchemaState:queueing, SchemaID:64, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:11:33.208 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 16:11:33.209 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:69, Type:drop schema, State:none, SchemaState:queueing, SchemaID:64, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:11:33.208 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/06/18 16:11:33.209 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:69, Type:drop schema, State:none, SchemaState:queueing, SchemaID:64, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:11:33.208 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:11:33.210 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=39] [neededSchemaVersion=40] ["start time"=54.337µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 16:11:33.212 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=40] ["take time"=2.212178ms] [job="ID:69, Type:drop schema, State:running, SchemaState:write only, SchemaID:64, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:11:33.208 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:11:33.212 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:69, Type:drop schema, State:running, SchemaState:write only, SchemaID:64, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:11:33.208 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:11:33.213 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=40] [neededSchemaVersion=41] ["start time"=78.502µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 16:11:33.215 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=41] ["take time"=2.444053ms] [job="ID:69, Type:drop schema, State:running, SchemaState:delete only, SchemaID:64, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:11:33.208 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:11:33.216 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:69, Type:drop schema, State:running, SchemaState:delete only, SchemaID:64, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:11:33.208 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:11:33.217 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=41] [neededSchemaVersion=42] ["start time"=106.37µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 16:11:33.219 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=42] ["take time"=2.245562ms] [job="ID:69, Type:drop schema, State:done, SchemaState:queueing, SchemaID:64, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:11:33.208 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:11:33.219 +00:00] [INFO] [delete_range.go:107] ["[ddl] add job into delete-range table"] [jobID=69] [jobType="drop schema"]
   > [2024/06/18 16:11:33.219 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:69, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:64, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:11:33.208 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:11:33.220 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=69]
   > [2024/06/18 16:11:33.220 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 16:11:33.222 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=42] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/06/18 16:11:33.223 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:71, Type:create schema, State:none, SchemaState:queueing, SchemaID:70, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 16:11:33.222 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 16:11:33.223 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:71, Type:create schema, State:none, SchemaState:queueing, SchemaID:70, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 16:11:33.222 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/18 16:11:33.224 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:71, Type:create schema, State:none, SchemaState:queueing, SchemaID:70, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:11:33.222 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:11:33.225 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=42] [neededSchemaVersion=43] ["start time"=151.977µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 16:11:33.227 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=43] ["take time"=2.241302ms] [job="ID:71, Type:create schema, State:done, SchemaState:public, SchemaID:70, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 16:11:33.222 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:11:33.227 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:71, Type:create schema, State:synced, SchemaState:public, SchemaID:70, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 16:11:33.222 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:11:33.228 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=71]
   > [2024/06/18 16:11:33.228 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 16:11:33.231 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=43] [cur_db=testdb] [sql="drop table if exists t_tir89b, t_vejdy;"] [user=root@127.0.0.1]
   > [2024/06/18 16:11:33.232 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=43] [cur_db=testdb] [sql="\nCREATE TABLE `t_tir89b` (\n`c_3pcik` int(11) DEFAULT NULL,\n`c_0b6nxb` text DEFAULT NULL,\n`c_qytrlc` double NOT NULL,\n`c_sroc_c` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_qytrlc`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/06/18 16:11:33.233 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:73, Type:create table, State:none, SchemaState:queueing, SchemaID:70, TableID:72, RowCount:0, ArgLen:1, start time: 2024-06-18 16:11:33.233 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 16:11:33.234 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:73, Type:create table, State:none, SchemaState:queueing, SchemaID:70, TableID:72, RowCount:0, ArgLen:1, start time: 2024-06-18 16:11:33.233 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="\nCREATE TABLE `t_tir89b` (\n`c_3pcik` int(11) DEFAULT NULL,\n`c_0b6nxb` text DEFAULT NULL,\n`c_qytrlc` double NOT NULL,\n`c_sroc_c` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_qytrlc`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/18 16:11:33.234 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:73, Type:create table, State:none, SchemaState:queueing, SchemaID:70, TableID:72, RowCount:0, ArgLen:0, start time: 2024-06-18 16:11:33.233 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:11:33.237 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=43] [neededSchemaVersion=44] ["start time"=861.293µs] [phyTblIDs="[72]"] [actionTypes="[8]"]
   > [2024/06/18 16:11:33.238 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=44] ["take time"=2.027166ms] [job="ID:73, Type:create table, State:done, SchemaState:public, SchemaID:70, TableID:72, RowCount:0, ArgLen:1, start time: 2024-06-18 16:11:33.233 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:11:33.239 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:73, Type:create table, State:synced, SchemaState:public, SchemaID:70, TableID:72, RowCount:0, ArgLen:0, start time: 2024-06-18 16:11:33.233 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:11:33.240 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=73]
   > [2024/06/18 16:11:33.240 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 16:11:33.240 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=60] ["first split key"=748000000000000048]
   > [2024/06/18 16:11:33.241 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=60] ["first at"=748000000000000048] ["first new region left"="{Id:60 StartKey:7480000000000000ff4200000000000000f8 EndKey:7480000000000000ff4800000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:61 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/18 16:11:33.241 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[60]"]
   > [2024/06/18 16:11:33.242 +00:00] [WARN] [2pc.go:1596] ["schemaLeaseChecker is not set for this transaction"] [sessionID=11] [startTS=450553995130830848] [commitTS=450553995130830849]
   > [2024/06/18 16:11:33.245 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=44] [cur_db=testdb] [sql="\nCREATE TABLE `t_vejdy` (\n`c_iovir` int(11) NOT NULL,\n`c_r_mw3d` double DEFAULT NULL,\n`c_uxhghb` int(11) DEFAULT NULL,\n`c_rb7otb` int(11) NOT NULL,\n`c_dplyac` int(11) DEFAULT NULL,\n`c_lmcqed` double DEFAULT NULL,\n`c_ayaoed` text DEFAULT NULL,\n`c__zbqr` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_iovir`,`c_rb7otb`) /*T![clustered_index] NONCLUSTERED */,\nKEY `t_e1ejcd` (`c_uxhghb`),\nKEY `t_o6ui_b` (`c_iovir`,`c_r_mw3d`,`c_uxhghb`,`c_rb7otb`,`c_dplyac`,`c_lmcqed`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/06/18 16:11:33.246 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:75, Type:create table, State:none, SchemaState:queueing, SchemaID:70, TableID:74, RowCount:0, ArgLen:1, start time: 2024-06-18 16:11:33.245 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 16:11:33.246 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:75, Type:create table, State:none, SchemaState:queueing, SchemaID:70, TableID:74, RowCount:0, ArgLen:1, start time: 2024-06-18 16:11:33.245 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="\nCREATE TABLE `t_vejdy` (\n`c_iovir` int(11) NOT NULL,\n`c_r_mw3d` double DEFAULT NULL,\n`c_uxhghb` int(11) DEFAULT NULL,\n`c_rb7otb` int(11) NOT NULL,\n`c_dplyac` int(11) DEFAULT NULL,\n`c_lmcqed` double DEFAULT NULL,\n`c_ayaoed` text DEFAULT NULL,\n`c__zbqr` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_iovir`,`c_rb7otb`) /*T![clustered_index] NONCLUSTERED */,\nKEY `t_e1ejcd` (`c_uxhghb`),\nKEY `t_o6ui_b` (`c_iovir`,`c_r_mw3d`,`c_uxhghb`,`c_rb7otb`,`c_dplyac`,`c_lmcqed`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/18 16:11:33.246 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:75, Type:create table, State:none, SchemaState:queueing, SchemaID:70, TableID:74, RowCount:0, ArgLen:0, start time: 2024-06-18 16:11:33.245 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:11:33.247 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=44] [neededSchemaVersion=45] ["start time"=266.238µs] [phyTblIDs="[74]"] [actionTypes="[8]"]
   > [2024/06/18 16:11:33.249 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=45] ["take time"=2.190317ms] [job="ID:75, Type:create table, State:done, SchemaState:public, SchemaID:70, TableID:74, RowCount:0, ArgLen:1, start time: 2024-06-18 16:11:33.245 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:11:33.250 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:75, Type:create table, State:synced, SchemaState:public, SchemaID:70, TableID:74, RowCount:0, ArgLen:0, start time: 2024-06-18 16:11:33.245 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 16:11:33.251 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=75]
   > [2024/06/18 16:11:33.251 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 16:11:33.252 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=62] ["first split key"=74800000000000004a]
   > [2024/06/18 16:11:33.252 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=62] ["first at"=74800000000000004a] ["first new region left"="{Id:62 StartKey:7480000000000000ff4800000000000000f8 EndKey:7480000000000000ff4a00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:63 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/18 16:11:33.252 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[62]"]
   > [2024/06/18 16:11:33.253 +00:00] [WARN] [2pc.go:1596] ["schemaLeaseChecker is not set for this transaction"] [sessionID=11] [startTS=450553995133452289] [commitTS=450553995133714432]
   > [2024/06/18 16:11:34.354 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=13] [user=root] [host=]
   > [2024/06/18 16:11:34.371 +00:00] [INFO] [set.go:139] ["set global var"] [conn=13] [name=tx_isolation] [val=REPEATABLE-READ]
