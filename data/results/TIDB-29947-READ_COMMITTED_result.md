# Bug ID TIDB-29947-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/29947
Original isolation level: IsolationLevel.REPEATABLE_READ
Tested isolation level:   IsolationLevel.READ_COMMITTED


## Details
 * Database: tidb-v5.4.0-local
 * Number of scenarios: 2
 * Initial setup script: /home/theodor/Projects/MasterThesis/data/sql/TIDB-29947_mysql_bk.sql

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
   > [2024/06/18 13:41:52.692 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=17] [user=root] [host=]
   > [2024/06/18 13:41:52.695 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=53] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/06/18 13:41:52.696 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:82, Type:drop schema, State:none, SchemaState:queueing, SchemaID:77, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 13:41:52.696 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 13:41:52.696 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:82, Type:drop schema, State:none, SchemaState:queueing, SchemaID:77, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 13:41:52.696 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/06/18 13:41:52.697 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:82, Type:drop schema, State:none, SchemaState:queueing, SchemaID:77, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 13:41:52.696 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:41:52.698 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=53] [neededSchemaVersion=54] ["start time"=94.426µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 13:41:52.700 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=54] ["take time"=2.235086ms] [job="ID:82, Type:drop schema, State:running, SchemaState:write only, SchemaID:77, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 13:41:52.696 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:41:52.700 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:82, Type:drop schema, State:running, SchemaState:write only, SchemaID:77, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 13:41:52.696 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:41:52.701 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=54] [neededSchemaVersion=55] ["start time"=96.382µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 13:41:52.703 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=55] ["take time"=2.229079ms] [job="ID:82, Type:drop schema, State:running, SchemaState:delete only, SchemaID:77, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 13:41:52.696 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:41:52.703 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:82, Type:drop schema, State:running, SchemaState:delete only, SchemaID:77, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 13:41:52.696 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:41:52.705 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=55] [neededSchemaVersion=56] ["start time"=111.608µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 13:41:52.707 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=56] ["take time"=2.213993ms] [job="ID:82, Type:drop schema, State:done, SchemaState:queueing, SchemaID:77, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 13:41:52.696 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:41:52.707 +00:00] [INFO] [delete_range.go:107] ["[ddl] add job into delete-range table"] [jobID=82] [jobType="drop schema"]
   > [2024/06/18 13:41:52.707 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:82, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:77, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 13:41:52.696 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:41:52.708 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=82]
   > [2024/06/18 13:41:52.708 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 13:41:52.709 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=56] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/06/18 13:41:52.711 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:84, Type:create schema, State:none, SchemaState:queueing, SchemaID:83, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 13:41:52.71 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 13:41:52.711 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:84, Type:create schema, State:none, SchemaState:queueing, SchemaID:83, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 13:41:52.71 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/18 13:41:52.712 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:84, Type:create schema, State:none, SchemaState:queueing, SchemaID:83, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 13:41:52.71 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:41:52.713 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=56] [neededSchemaVersion=57] ["start time"=180.193µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 13:41:52.715 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=57] ["take time"=2.267632ms] [job="ID:84, Type:create schema, State:done, SchemaState:public, SchemaID:83, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 13:41:52.71 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:41:52.715 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:84, Type:create schema, State:synced, SchemaState:public, SchemaID:83, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 13:41:52.71 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:41:52.716 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=84]
   > [2024/06/18 13:41:52.716 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 13:41:52.720 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=57] [cur_db=testdb] [sql="drop table if exists t_tir89b, t_vejdy;"] [user=root@127.0.0.1]
   > [2024/06/18 13:41:52.721 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=57] [cur_db=testdb] [sql="\nCREATE TABLE `t_tir89b` (\n`c_3pcik` int(11) DEFAULT NULL,\n`c_0b6nxb` text DEFAULT NULL,\n`c_qytrlc` double NOT NULL,\n`c_sroc_c` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_qytrlc`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/06/18 13:41:52.723 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:86, Type:create table, State:none, SchemaState:queueing, SchemaID:83, TableID:85, RowCount:0, ArgLen:1, start time: 2024-06-18 13:41:52.722 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 13:41:52.723 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:86, Type:create table, State:none, SchemaState:queueing, SchemaID:83, TableID:85, RowCount:0, ArgLen:1, start time: 2024-06-18 13:41:52.722 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="\nCREATE TABLE `t_tir89b` (\n`c_3pcik` int(11) DEFAULT NULL,\n`c_0b6nxb` text DEFAULT NULL,\n`c_qytrlc` double NOT NULL,\n`c_sroc_c` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_qytrlc`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/18 13:41:52.723 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:86, Type:create table, State:none, SchemaState:queueing, SchemaID:83, TableID:85, RowCount:0, ArgLen:0, start time: 2024-06-18 13:41:52.722 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:41:52.725 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=57] [neededSchemaVersion=58] ["start time"=385.598µs] [phyTblIDs="[85]"] [actionTypes="[8]"]
   > [2024/06/18 13:41:52.727 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=58] ["take time"=2.092887ms] [job="ID:86, Type:create table, State:done, SchemaState:public, SchemaID:83, TableID:85, RowCount:0, ArgLen:1, start time: 2024-06-18 13:41:52.722 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:41:52.728 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:86, Type:create table, State:synced, SchemaState:public, SchemaID:83, TableID:85, RowCount:0, ArgLen:0, start time: 2024-06-18 13:41:52.722 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:41:52.729 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=86]
   > [2024/06/18 13:41:52.729 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 13:41:52.729 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=66] ["first split key"=748000000000000055]
   > [2024/06/18 13:41:52.729 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=66] ["first at"=748000000000000055] ["first new region left"="{Id:66 StartKey:7480000000000000ff4f00000000000000f8 EndKey:7480000000000000ff5500000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:67 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/18 13:41:52.729 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[66]"]
   > [2024/06/18 13:41:52.731 +00:00] [WARN] [2pc.go:1596] ["schemaLeaseChecker is not set for this transaction"] [sessionID=17] [startTS=450551640943493121] [commitTS=450551640943755264]
   > [2024/06/18 13:41:52.733 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=58] [cur_db=testdb] [sql="\nCREATE TABLE `t_vejdy` (\n`c_iovir` int(11) NOT NULL,\n`c_r_mw3d` double DEFAULT NULL,\n`c_uxhghb` int(11) DEFAULT NULL,\n`c_rb7otb` int(11) NOT NULL,\n`c_dplyac` int(11) DEFAULT NULL,\n`c_lmcqed` double DEFAULT NULL,\n`c_ayaoed` text DEFAULT NULL,\n`c__zbqr` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_iovir`,`c_rb7otb`) /*T![clustered_index] NONCLUSTERED */,\nKEY `t_e1ejcd` (`c_uxhghb`),\nKEY `t_o6ui_b` (`c_iovir`,`c_r_mw3d`,`c_uxhghb`,`c_rb7otb`,`c_dplyac`,`c_lmcqed`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/06/18 13:41:52.735 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:88, Type:create table, State:none, SchemaState:queueing, SchemaID:83, TableID:87, RowCount:0, ArgLen:1, start time: 2024-06-18 13:41:52.734 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 13:41:52.735 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:88, Type:create table, State:none, SchemaState:queueing, SchemaID:83, TableID:87, RowCount:0, ArgLen:1, start time: 2024-06-18 13:41:52.734 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="\nCREATE TABLE `t_vejdy` (\n`c_iovir` int(11) NOT NULL,\n`c_r_mw3d` double DEFAULT NULL,\n`c_uxhghb` int(11) DEFAULT NULL,\n`c_rb7otb` int(11) NOT NULL,\n`c_dplyac` int(11) DEFAULT NULL,\n`c_lmcqed` double DEFAULT NULL,\n`c_ayaoed` text DEFAULT NULL,\n`c__zbqr` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_iovir`,`c_rb7otb`) /*T![clustered_index] NONCLUSTERED */,\nKEY `t_e1ejcd` (`c_uxhghb`),\nKEY `t_o6ui_b` (`c_iovir`,`c_r_mw3d`,`c_uxhghb`,`c_rb7otb`,`c_dplyac`,`c_lmcqed`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/18 13:41:52.735 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:88, Type:create table, State:none, SchemaState:queueing, SchemaID:83, TableID:87, RowCount:0, ArgLen:0, start time: 2024-06-18 13:41:52.734 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:41:52.738 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=58] [neededSchemaVersion=59] ["start time"=561.531µs] [phyTblIDs="[87]"] [actionTypes="[8]"]
   > [2024/06/18 13:41:52.740 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=59] ["take time"=2.249193ms] [job="ID:88, Type:create table, State:done, SchemaState:public, SchemaID:83, TableID:87, RowCount:0, ArgLen:1, start time: 2024-06-18 13:41:52.734 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:41:52.741 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:88, Type:create table, State:synced, SchemaState:public, SchemaID:83, TableID:87, RowCount:0, ArgLen:0, start time: 2024-06-18 13:41:52.734 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:41:52.742 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=88]
   > [2024/06/18 13:41:52.743 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 13:41:52.743 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=68] ["first split key"=748000000000000057]
   > [2024/06/18 13:41:52.743 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=68] ["first at"=748000000000000057] ["first new region left"="{Id:68 StartKey:7480000000000000ff5500000000000000f8 EndKey:7480000000000000ff5700000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:69 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/18 13:41:52.743 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[68]"]
   > [2024/06/18 13:41:52.744 +00:00] [WARN] [2pc.go:1596] ["schemaLeaseChecker is not set for this transaction"] [sessionID=17] [startTS=450551640947163137] [commitTS=450551640947163138]
   > [2024/06/18 13:41:53.806 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=19] [user=root] [host=]
   > [2024/06/18 13:41:53.829 +00:00] [INFO] [set.go:139] ["set global var"] [conn=19] [name=tx_isolation] [val=READ-COMMITTED]

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
   > [2024/06/18 13:41:56.245 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=23] [user=root] [host=]
   > [2024/06/18 13:41:56.249 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=23] [schemaVersion=67] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/06/18 13:41:56.250 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:95, Type:drop schema, State:none, SchemaState:queueing, SchemaID:90, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 13:41:56.249 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 13:41:56.250 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:95, Type:drop schema, State:none, SchemaState:queueing, SchemaID:90, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 13:41:56.249 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/06/18 13:41:56.251 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:95, Type:drop schema, State:none, SchemaState:queueing, SchemaID:90, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 13:41:56.249 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:41:56.252 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=67] [neededSchemaVersion=68] ["start time"=123.481µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 13:41:56.254 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=68] ["take time"=2.211828ms] [job="ID:95, Type:drop schema, State:running, SchemaState:write only, SchemaID:90, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 13:41:56.249 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:41:56.254 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:95, Type:drop schema, State:running, SchemaState:write only, SchemaID:90, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 13:41:56.249 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:41:56.255 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=68] [neededSchemaVersion=69] ["start time"=93.937µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 13:41:56.257 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=69] ["take time"=2.262254ms] [job="ID:95, Type:drop schema, State:running, SchemaState:delete only, SchemaID:90, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 13:41:56.249 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:41:56.257 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:95, Type:drop schema, State:running, SchemaState:delete only, SchemaID:90, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 13:41:56.249 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:41:56.258 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=69] [neededSchemaVersion=70] ["start time"=98.757µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 13:41:56.260 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=70] ["take time"=2.267842ms] [job="ID:95, Type:drop schema, State:done, SchemaState:queueing, SchemaID:90, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 13:41:56.249 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:41:56.261 +00:00] [INFO] [delete_range.go:107] ["[ddl] add job into delete-range table"] [jobID=95] [jobType="drop schema"]
   > [2024/06/18 13:41:56.261 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:95, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:90, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 13:41:56.249 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:41:56.262 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=95]
   > [2024/06/18 13:41:56.262 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 13:41:56.263 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=23] [schemaVersion=70] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/06/18 13:41:56.265 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:97, Type:create schema, State:none, SchemaState:queueing, SchemaID:96, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 13:41:56.264 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 13:41:56.265 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:97, Type:create schema, State:none, SchemaState:queueing, SchemaID:96, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 13:41:56.264 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/18 13:41:56.265 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:97, Type:create schema, State:none, SchemaState:queueing, SchemaID:96, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 13:41:56.264 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:41:56.266 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=70] [neededSchemaVersion=71] ["start time"=182.148µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 13:41:56.268 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=71] ["take time"=2.253175ms] [job="ID:97, Type:create schema, State:done, SchemaState:public, SchemaID:96, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 13:41:56.264 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:41:56.269 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:97, Type:create schema, State:synced, SchemaState:public, SchemaID:96, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 13:41:56.264 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:41:56.270 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=97]
   > [2024/06/18 13:41:56.270 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 13:41:56.274 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=23] [schemaVersion=71] [cur_db=testdb] [sql="drop table if exists t_tir89b, t_vejdy;"] [user=root@127.0.0.1]
   > [2024/06/18 13:41:56.274 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=23] [schemaVersion=71] [cur_db=testdb] [sql="\nCREATE TABLE `t_tir89b` (\n`c_3pcik` int(11) DEFAULT NULL,\n`c_0b6nxb` text DEFAULT NULL,\n`c_qytrlc` double NOT NULL,\n`c_sroc_c` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_qytrlc`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/06/18 13:41:56.276 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:99, Type:create table, State:none, SchemaState:queueing, SchemaID:96, TableID:98, RowCount:0, ArgLen:1, start time: 2024-06-18 13:41:56.275 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 13:41:56.276 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:99, Type:create table, State:none, SchemaState:queueing, SchemaID:96, TableID:98, RowCount:0, ArgLen:1, start time: 2024-06-18 13:41:56.275 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="\nCREATE TABLE `t_tir89b` (\n`c_3pcik` int(11) DEFAULT NULL,\n`c_0b6nxb` text DEFAULT NULL,\n`c_qytrlc` double NOT NULL,\n`c_sroc_c` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_qytrlc`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/18 13:41:56.277 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:99, Type:create table, State:none, SchemaState:queueing, SchemaID:96, TableID:98, RowCount:0, ArgLen:0, start time: 2024-06-18 13:41:56.275 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:41:56.279 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=71] [neededSchemaVersion=72] ["start time"=520.183µs] [phyTblIDs="[98]"] [actionTypes="[8]"]
   > [2024/06/18 13:41:56.280 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=72] ["take time"=2.041064ms] [job="ID:99, Type:create table, State:done, SchemaState:public, SchemaID:96, TableID:98, RowCount:0, ArgLen:1, start time: 2024-06-18 13:41:56.275 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:41:56.281 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:99, Type:create table, State:synced, SchemaState:public, SchemaID:96, TableID:98, RowCount:0, ArgLen:0, start time: 2024-06-18 13:41:56.275 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:41:56.282 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=99]
   > [2024/06/18 13:41:56.282 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 13:41:56.283 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=72] ["first split key"=748000000000000062]
   > [2024/06/18 13:41:56.283 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=72] ["first at"=748000000000000062] ["first new region left"="{Id:72 StartKey:7480000000000000ff5c00000000000000f8 EndKey:7480000000000000ff6200000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:73 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/18 13:41:56.283 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[72]"]
   > [2024/06/18 13:41:56.284 +00:00] [WARN] [2pc.go:1596] ["schemaLeaseChecker is not set for this transaction"] [sessionID=23] [startTS=450551641875152897] [commitTS=450551641875152898]
   > [2024/06/18 13:41:56.287 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=23] [schemaVersion=72] [cur_db=testdb] [sql="\nCREATE TABLE `t_vejdy` (\n`c_iovir` int(11) NOT NULL,\n`c_r_mw3d` double DEFAULT NULL,\n`c_uxhghb` int(11) DEFAULT NULL,\n`c_rb7otb` int(11) NOT NULL,\n`c_dplyac` int(11) DEFAULT NULL,\n`c_lmcqed` double DEFAULT NULL,\n`c_ayaoed` text DEFAULT NULL,\n`c__zbqr` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_iovir`,`c_rb7otb`) /*T![clustered_index] NONCLUSTERED */,\nKEY `t_e1ejcd` (`c_uxhghb`),\nKEY `t_o6ui_b` (`c_iovir`,`c_r_mw3d`,`c_uxhghb`,`c_rb7otb`,`c_dplyac`,`c_lmcqed`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/06/18 13:41:56.288 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:101, Type:create table, State:none, SchemaState:queueing, SchemaID:96, TableID:100, RowCount:0, ArgLen:1, start time: 2024-06-18 13:41:56.287 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 13:41:56.288 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:101, Type:create table, State:none, SchemaState:queueing, SchemaID:96, TableID:100, RowCount:0, ArgLen:1, start time: 2024-06-18 13:41:56.287 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="\nCREATE TABLE `t_vejdy` (\n`c_iovir` int(11) NOT NULL,\n`c_r_mw3d` double DEFAULT NULL,\n`c_uxhghb` int(11) DEFAULT NULL,\n`c_rb7otb` int(11) NOT NULL,\n`c_dplyac` int(11) DEFAULT NULL,\n`c_lmcqed` double DEFAULT NULL,\n`c_ayaoed` text DEFAULT NULL,\n`c__zbqr` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_iovir`,`c_rb7otb`) /*T![clustered_index] NONCLUSTERED */,\nKEY `t_e1ejcd` (`c_uxhghb`),\nKEY `t_o6ui_b` (`c_iovir`,`c_r_mw3d`,`c_uxhghb`,`c_rb7otb`,`c_dplyac`,`c_lmcqed`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/18 13:41:56.289 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:101, Type:create table, State:none, SchemaState:queueing, SchemaID:96, TableID:100, RowCount:0, ArgLen:0, start time: 2024-06-18 13:41:56.287 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:41:56.292 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=72] [neededSchemaVersion=73] ["start time"=609.861µs] [phyTblIDs="[100]"] [actionTypes="[8]"]
   > [2024/06/18 13:41:56.294 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=73] ["take time"=2.275454ms] [job="ID:101, Type:create table, State:done, SchemaState:public, SchemaID:96, TableID:100, RowCount:0, ArgLen:1, start time: 2024-06-18 13:41:56.287 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:41:56.295 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:101, Type:create table, State:synced, SchemaState:public, SchemaID:96, TableID:100, RowCount:0, ArgLen:0, start time: 2024-06-18 13:41:56.287 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 13:41:56.296 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=101]
   > [2024/06/18 13:41:56.296 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/06/18 13:41:56.297 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=74] ["first split key"=748000000000000064]
   > [2024/06/18 13:41:56.297 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=74] ["first at"=748000000000000064] ["first new region left"="{Id:74 StartKey:7480000000000000ff6200000000000000f8 EndKey:7480000000000000ff6400000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:75 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/18 13:41:56.297 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[74]"]
   > [2024/06/18 13:41:56.298 +00:00] [WARN] [2pc.go:1596] ["schemaLeaseChecker is not set for this transaction"] [sessionID=23] [startTS=450551641878822913] [commitTS=450551641878822914]
   > [2024/06/18 13:41:57.401 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=25] [user=root] [host=]
   > [2024/06/18 13:41:57.415 +00:00] [INFO] [set.go:139] ["set global var"] [conn=25] [name=tx_isolation] [val=READ-COMMITTED]
