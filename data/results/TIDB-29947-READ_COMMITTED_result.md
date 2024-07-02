# Bug ID TIDB-29947-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/29947
Original isolation level: IsolationLevel.REPEATABLE_READ
Tested isolation level:   IsolationLevel.READ_COMMITTED


## Details
 * Database: tidb-v5.4.0
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
     - Instruction:  delete from t_tir89b where t_tir89b.c_3pcik >= t_tir89b.c_sroc_c;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
 * Instruction #2:
     - Instruction:  select * from (select count(*) over (partition by ref_0.c_0b6nxb order by ref_0...
     - Transaction: conn_0
     - Output: [(2,), (3,)]
     - Executed order: 2

 * Container logs:
   > [2024/07/01 15:12:06.627 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=17] [user=root] [host=]
   > [2024/07/01 15:12:06.631 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=53] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/07/01 15:12:06.632 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:82, Type:drop schema, State:none, SchemaState:queueing, SchemaID:77, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:06.631 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:12:06.632 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:82, Type:drop schema, State:none, SchemaState:queueing, SchemaID:77, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:06.631 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/01 15:12:06.632 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:82, Type:drop schema, State:none, SchemaState:queueing, SchemaID:77, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:06.631 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:06.634 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=53] [neededSchemaVersion=54] ["start time"=116.776µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:12:06.636 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=54] ["take time"=2.220766ms] [job="ID:82, Type:drop schema, State:running, SchemaState:write only, SchemaID:77, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:06.631 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:06.636 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:82, Type:drop schema, State:running, SchemaState:write only, SchemaID:77, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:06.631 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:06.637 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=54] [neededSchemaVersion=55] ["start time"=99.036µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:12:06.639 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=55] ["take time"=2.14345ms] [job="ID:82, Type:drop schema, State:running, SchemaState:delete only, SchemaID:77, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:06.631 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:06.639 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:82, Type:drop schema, State:running, SchemaState:delete only, SchemaID:77, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:06.631 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:06.640 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=55] [neededSchemaVersion=56] ["start time"=101.969µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:12:06.643 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=56] ["take time"=2.256525ms] [job="ID:82, Type:drop schema, State:done, SchemaState:queueing, SchemaID:77, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:06.631 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:06.643 +00:00] [INFO] [delete_range.go:107] ["[ddl] add job into delete-range table"] [jobID=82] [jobType="drop schema"]
   > [2024/07/01 15:12:06.643 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:82, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:77, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:06.631 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:06.644 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=82]
   > [2024/07/01 15:12:06.644 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:12:06.645 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=56] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/07/01 15:12:06.647 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:84, Type:create schema, State:none, SchemaState:queueing, SchemaID:83, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:06.646 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:12:06.647 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:84, Type:create schema, State:none, SchemaState:queueing, SchemaID:83, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:06.646 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/01 15:12:06.647 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:84, Type:create schema, State:none, SchemaState:queueing, SchemaID:83, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:06.646 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:06.648 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=56] [neededSchemaVersion=57] ["start time"=101.48µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:12:06.650 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=57] ["take time"=2.248982ms] [job="ID:84, Type:create schema, State:done, SchemaState:public, SchemaID:83, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:06.646 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:06.651 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:84, Type:create schema, State:synced, SchemaState:public, SchemaID:83, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:06.646 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:06.652 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=84]
   > [2024/07/01 15:12:06.652 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:12:06.655 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=57] [cur_db=testdb] [sql="drop table if exists t_tir89b, t_vejdy;"] [user=root@127.0.0.1]
   > [2024/07/01 15:12:06.656 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=57] [cur_db=testdb] [sql="\nCREATE TABLE `t_tir89b` (\n`c_3pcik` int(11) DEFAULT NULL,\n`c_0b6nxb` text DEFAULT NULL,\n`c_qytrlc` double NOT NULL,\n`c_sroc_c` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_qytrlc`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/07/01 15:12:06.658 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:86, Type:create table, State:none, SchemaState:queueing, SchemaID:83, TableID:85, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:06.657 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:12:06.658 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:86, Type:create table, State:none, SchemaState:queueing, SchemaID:83, TableID:85, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:06.657 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="\nCREATE TABLE `t_tir89b` (\n`c_3pcik` int(11) DEFAULT NULL,\n`c_0b6nxb` text DEFAULT NULL,\n`c_qytrlc` double NOT NULL,\n`c_sroc_c` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_qytrlc`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/01 15:12:06.658 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:86, Type:create table, State:none, SchemaState:queueing, SchemaID:83, TableID:85, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:06.657 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:06.660 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=57] [neededSchemaVersion=58] ["start time"=417.236µs] [phyTblIDs="[85]"] [actionTypes="[8]"]
   > [2024/07/01 15:12:06.662 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=58] ["take time"=2.273775ms] [job="ID:86, Type:create table, State:done, SchemaState:public, SchemaID:83, TableID:85, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:06.657 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:06.663 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:86, Type:create table, State:synced, SchemaState:public, SchemaID:83, TableID:85, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:06.657 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:06.664 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=86]
   > [2024/07/01 15:12:06.664 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:12:06.664 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=66] ["first split key"=748000000000000055]
   > [2024/07/01 15:12:06.665 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=66] ["first at"=748000000000000055] ["first new region left"="{Id:66 StartKey:7480000000000000ff4f00000000000000f8 EndKey:7480000000000000ff5500000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:67 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/01 15:12:06.665 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[66]"]
   > [2024/07/01 15:12:06.665 +00:00] [WARN] [2pc.go:1596] ["schemaLeaseChecker is not set for this transaction"] [sessionID=17] [startTS=450847500314869761] [commitTS=450847500314869762]
   > [2024/07/01 15:12:06.668 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=58] [cur_db=testdb] [sql="\nCREATE TABLE `t_vejdy` (\n`c_iovir` int(11) NOT NULL,\n`c_r_mw3d` double DEFAULT NULL,\n`c_uxhghb` int(11) DEFAULT NULL,\n`c_rb7otb` int(11) NOT NULL,\n`c_dplyac` int(11) DEFAULT NULL,\n`c_lmcqed` double DEFAULT NULL,\n`c_ayaoed` text DEFAULT NULL,\n`c__zbqr` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_iovir`,`c_rb7otb`) /*T![clustered_index] NONCLUSTERED */,\nKEY `t_e1ejcd` (`c_uxhghb`),\nKEY `t_o6ui_b` (`c_iovir`,`c_r_mw3d`,`c_uxhghb`,`c_rb7otb`,`c_dplyac`,`c_lmcqed`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/07/01 15:12:06.670 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:88, Type:create table, State:none, SchemaState:queueing, SchemaID:83, TableID:87, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:06.669 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:12:06.670 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:88, Type:create table, State:none, SchemaState:queueing, SchemaID:83, TableID:87, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:06.669 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="\nCREATE TABLE `t_vejdy` (\n`c_iovir` int(11) NOT NULL,\n`c_r_mw3d` double DEFAULT NULL,\n`c_uxhghb` int(11) DEFAULT NULL,\n`c_rb7otb` int(11) NOT NULL,\n`c_dplyac` int(11) DEFAULT NULL,\n`c_lmcqed` double DEFAULT NULL,\n`c_ayaoed` text DEFAULT NULL,\n`c__zbqr` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_iovir`,`c_rb7otb`) /*T![clustered_index] NONCLUSTERED */,\nKEY `t_e1ejcd` (`c_uxhghb`),\nKEY `t_o6ui_b` (`c_iovir`,`c_r_mw3d`,`c_uxhghb`,`c_rb7otb`,`c_dplyac`,`c_lmcqed`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/01 15:12:06.671 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:88, Type:create table, State:none, SchemaState:queueing, SchemaID:83, TableID:87, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:06.669 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:06.674 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=58] [neededSchemaVersion=59] ["start time"=831.817µs] [phyTblIDs="[87]"] [actionTypes="[8]"]
   > [2024/07/01 15:12:06.675 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=59] ["take time"=2.242276ms] [job="ID:88, Type:create table, State:done, SchemaState:public, SchemaID:83, TableID:87, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:06.669 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:06.676 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:88, Type:create table, State:synced, SchemaState:public, SchemaID:83, TableID:87, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:06.669 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:06.677 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=88]
   > [2024/07/01 15:12:06.677 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:12:06.677 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=68] ["first split key"=748000000000000057]
   > [2024/07/01 15:12:06.678 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=68] ["first at"=748000000000000057] ["first new region left"="{Id:68 StartKey:7480000000000000ff5500000000000000f8 EndKey:7480000000000000ff5700000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:69 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/01 15:12:06.678 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[68]"]
   > [2024/07/01 15:12:06.678 +00:00] [WARN] [2pc.go:1596] ["schemaLeaseChecker is not set for this transaction"] [sessionID=17] [startTS=450847500318277633] [commitTS=450847500318277634]
   > [2024/07/01 15:12:07.785 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=19] [user=root] [host=]
   > [2024/07/01 15:12:07.804 +00:00] [INFO] [set.go:139] ["set global var"] [conn=19] [name=tx_isolation] [val=READ-COMMITTED]

### Scenario 1
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
 * Instruction #1:
     - Instruction:  start transaction;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
 * Instruction #2:
     - Instruction:  delete from t_tir89b where t_tir89b.c_3pcik >= t_tir89b.c_sroc_c;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
 * Instruction #3:
     - Instruction:  select * from (select count(*) over (partition by ref_0.c_0b6nxb order by ref_0...
     - Transaction: conn_0
     - Output: []
     - Executed order: 3
 * Instruction #4:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4

 * Container logs:
   > [2024/07/01 15:12:09.277 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=23] [user=root] [host=]
   > [2024/07/01 15:12:09.281 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=23] [schemaVersion=67] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/07/01 15:12:09.282 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:95, Type:drop schema, State:none, SchemaState:queueing, SchemaID:90, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:09.281 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:12:09.282 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:95, Type:drop schema, State:none, SchemaState:queueing, SchemaID:90, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:09.281 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/01 15:12:09.282 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:95, Type:drop schema, State:none, SchemaState:queueing, SchemaID:90, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:09.281 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:09.283 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=67] [neededSchemaVersion=68] ["start time"=113.912µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:12:09.285 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=68] ["take time"=2.254918ms] [job="ID:95, Type:drop schema, State:running, SchemaState:write only, SchemaID:90, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:09.281 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:09.286 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:95, Type:drop schema, State:running, SchemaState:write only, SchemaID:90, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:09.281 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:09.287 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=68] [neededSchemaVersion=69] ["start time"=96.801µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:12:09.289 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=69] ["take time"=2.199673ms] [job="ID:95, Type:drop schema, State:running, SchemaState:delete only, SchemaID:90, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:09.281 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:09.289 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:95, Type:drop schema, State:running, SchemaState:delete only, SchemaID:90, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:09.281 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:09.290 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=69] [neededSchemaVersion=70] ["start time"=95.264µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:12:09.292 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=70] ["take time"=2.254149ms] [job="ID:95, Type:drop schema, State:done, SchemaState:queueing, SchemaID:90, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:09.281 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:09.292 +00:00] [INFO] [delete_range.go:107] ["[ddl] add job into delete-range table"] [jobID=95] [jobType="drop schema"]
   > [2024/07/01 15:12:09.293 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:95, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:90, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:09.281 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:09.294 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=95]
   > [2024/07/01 15:12:09.294 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:12:09.295 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=23] [schemaVersion=70] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/07/01 15:12:09.297 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:97, Type:create schema, State:none, SchemaState:queueing, SchemaID:96, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:09.296 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:12:09.297 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:97, Type:create schema, State:none, SchemaState:queueing, SchemaID:96, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:09.296 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/01 15:12:09.297 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:97, Type:create schema, State:none, SchemaState:queueing, SchemaID:96, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:09.296 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:09.298 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=70] [neededSchemaVersion=71] ["start time"=181.728µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:12:09.300 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=71] ["take time"=2.320919ms] [job="ID:97, Type:create schema, State:done, SchemaState:public, SchemaID:96, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:09.296 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:09.301 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:97, Type:create schema, State:synced, SchemaState:public, SchemaID:96, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:09.296 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:09.302 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=97]
   > [2024/07/01 15:12:09.302 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:12:09.306 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=23] [schemaVersion=71] [cur_db=testdb] [sql="drop table if exists t_tir89b, t_vejdy;"] [user=root@127.0.0.1]
   > [2024/07/01 15:12:09.307 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=23] [schemaVersion=71] [cur_db=testdb] [sql="\nCREATE TABLE `t_tir89b` (\n`c_3pcik` int(11) DEFAULT NULL,\n`c_0b6nxb` text DEFAULT NULL,\n`c_qytrlc` double NOT NULL,\n`c_sroc_c` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_qytrlc`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/07/01 15:12:09.308 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:99, Type:create table, State:none, SchemaState:queueing, SchemaID:96, TableID:98, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:09.307 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:12:09.308 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:99, Type:create table, State:none, SchemaState:queueing, SchemaID:96, TableID:98, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:09.307 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="\nCREATE TABLE `t_tir89b` (\n`c_3pcik` int(11) DEFAULT NULL,\n`c_0b6nxb` text DEFAULT NULL,\n`c_qytrlc` double NOT NULL,\n`c_sroc_c` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_qytrlc`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/01 15:12:09.309 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:99, Type:create table, State:none, SchemaState:queueing, SchemaID:96, TableID:98, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:09.307 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:09.311 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=71] [neededSchemaVersion=72] ["start time"=412.626µs] [phyTblIDs="[98]"] [actionTypes="[8]"]
   > [2024/07/01 15:12:09.312 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=72] ["take time"=2.087856ms] [job="ID:99, Type:create table, State:done, SchemaState:public, SchemaID:96, TableID:98, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:09.307 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:09.313 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:99, Type:create table, State:synced, SchemaState:public, SchemaID:96, TableID:98, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:09.307 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:09.314 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=99]
   > [2024/07/01 15:12:09.314 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:12:09.314 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=72] ["first split key"=748000000000000062]
   > [2024/07/01 15:12:09.315 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=72] ["first at"=748000000000000062] ["first new region left"="{Id:72 StartKey:7480000000000000ff5c00000000000000f8 EndKey:7480000000000000ff6200000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:73 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/01 15:12:09.315 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[72]"]
   > [2024/07/01 15:12:09.316 +00:00] [WARN] [2pc.go:1596] ["schemaLeaseChecker is not set for this transaction"] [sessionID=23] [startTS=450847501009551361] [commitTS=450847501009813504]
   > [2024/07/01 15:12:09.318 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=23] [schemaVersion=72] [cur_db=testdb] [sql="\nCREATE TABLE `t_vejdy` (\n`c_iovir` int(11) NOT NULL,\n`c_r_mw3d` double DEFAULT NULL,\n`c_uxhghb` int(11) DEFAULT NULL,\n`c_rb7otb` int(11) NOT NULL,\n`c_dplyac` int(11) DEFAULT NULL,\n`c_lmcqed` double DEFAULT NULL,\n`c_ayaoed` text DEFAULT NULL,\n`c__zbqr` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_iovir`,`c_rb7otb`) /*T![clustered_index] NONCLUSTERED */,\nKEY `t_e1ejcd` (`c_uxhghb`),\nKEY `t_o6ui_b` (`c_iovir`,`c_r_mw3d`,`c_uxhghb`,`c_rb7otb`,`c_dplyac`,`c_lmcqed`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/07/01 15:12:09.320 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:101, Type:create table, State:none, SchemaState:queueing, SchemaID:96, TableID:100, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:09.319 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:12:09.320 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:101, Type:create table, State:none, SchemaState:queueing, SchemaID:96, TableID:100, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:09.319 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="\nCREATE TABLE `t_vejdy` (\n`c_iovir` int(11) NOT NULL,\n`c_r_mw3d` double DEFAULT NULL,\n`c_uxhghb` int(11) DEFAULT NULL,\n`c_rb7otb` int(11) NOT NULL,\n`c_dplyac` int(11) DEFAULT NULL,\n`c_lmcqed` double DEFAULT NULL,\n`c_ayaoed` text DEFAULT NULL,\n`c__zbqr` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_iovir`,`c_rb7otb`) /*T![clustered_index] NONCLUSTERED */,\nKEY `t_e1ejcd` (`c_uxhghb`),\nKEY `t_o6ui_b` (`c_iovir`,`c_r_mw3d`,`c_uxhghb`,`c_rb7otb`,`c_dplyac`,`c_lmcqed`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/01 15:12:09.321 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:101, Type:create table, State:none, SchemaState:queueing, SchemaID:96, TableID:100, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:09.319 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:09.324 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=72] [neededSchemaVersion=73] ["start time"=622.642µs] [phyTblIDs="[100]"] [actionTypes="[8]"]
   > [2024/07/01 15:12:09.325 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=73] ["take time"=2.223559ms] [job="ID:101, Type:create table, State:done, SchemaState:public, SchemaID:96, TableID:100, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:09.319 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:09.327 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:101, Type:create table, State:synced, SchemaState:public, SchemaID:96, TableID:100, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:09.319 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:09.329 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=101]
   > [2024/07/01 15:12:09.329 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:12:09.329 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=74] ["first split key"=748000000000000064]
   > [2024/07/01 15:12:09.329 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=74] ["first at"=748000000000000064] ["first new region left"="{Id:74 StartKey:7480000000000000ff6200000000000000f8 EndKey:7480000000000000ff6400000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:75 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/01 15:12:09.329 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[74]"]
   > [2024/07/01 15:12:09.331 +00:00] [WARN] [2pc.go:1596] ["schemaLeaseChecker is not set for this transaction"] [sessionID=23] [startTS=450847501013483521] [commitTS=450847501013745664]
   > [2024/07/01 15:12:10.449 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=25] [user=root] [host=]
   > [2024/07/01 15:12:10.472 +00:00] [INFO] [set.go:139] ["set global var"] [conn=25] [name=tx_isolation] [val=READ-COMMITTED]
