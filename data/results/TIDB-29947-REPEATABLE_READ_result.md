# Bug ID TIDB-29947-REPEATABLE_READ

## Description

Link:                     https://github.com/pingcap/tidb/issues/29947
Original isolation level: IsolationLevel.REPEATABLE_READ
Tested isolation level:   IsolationLevel.REPEATABLE_READ


## Details
 * Database: tidb-v5.4.0
 * Number of scenarios: 2
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
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
   > [2024/07/01 15:11:59.922 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=5] [user=root] [host=]
   > [2024/07/01 15:11:59.926 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=28] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/07/01 15:11:59.928 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=28] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/07/01 15:11:59.929 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:58, Type:create schema, State:none, SchemaState:queueing, SchemaID:57, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:11:59.928 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:11:59.929 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:58, Type:create schema, State:none, SchemaState:queueing, SchemaID:57, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:11:59.928 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/01 15:11:59.929 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:58, Type:create schema, State:none, SchemaState:queueing, SchemaID:57, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:11:59.928 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:11:59.931 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=28] [neededSchemaVersion=29] ["start time"=165.036µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:11:59.933 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=29] ["take time"=2.269096ms] [job="ID:58, Type:create schema, State:done, SchemaState:public, SchemaID:57, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:11:59.928 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:11:59.933 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:58, Type:create schema, State:synced, SchemaState:public, SchemaID:57, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:11:59.928 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:11:59.934 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=58]
   > [2024/07/01 15:11:59.934 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:11:59.938 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=29] [cur_db=testdb] [sql="drop table if exists t_tir89b, t_vejdy;"] [user=root@127.0.0.1]
   > [2024/07/01 15:11:59.939 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=29] [cur_db=testdb] [sql="\nCREATE TABLE `t_tir89b` (\n`c_3pcik` int(11) DEFAULT NULL,\n`c_0b6nxb` text DEFAULT NULL,\n`c_qytrlc` double NOT NULL,\n`c_sroc_c` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_qytrlc`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/07/01 15:11:59.940 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:60, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:59, RowCount:0, ArgLen:1, start time: 2024-07-01 15:11:59.939 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:11:59.940 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:60, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:59, RowCount:0, ArgLen:1, start time: 2024-07-01 15:11:59.939 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="\nCREATE TABLE `t_tir89b` (\n`c_3pcik` int(11) DEFAULT NULL,\n`c_0b6nxb` text DEFAULT NULL,\n`c_qytrlc` double NOT NULL,\n`c_sroc_c` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_qytrlc`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/01 15:11:59.941 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:60, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:59, RowCount:0, ArgLen:0, start time: 2024-07-01 15:11:59.939 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:11:59.942 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=29] [neededSchemaVersion=30] ["start time"=368.486µs] [phyTblIDs="[59]"] [actionTypes="[8]"]
   > [2024/07/01 15:11:59.944 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=30] ["take time"=2.023811ms] [job="ID:60, Type:create table, State:done, SchemaState:public, SchemaID:57, TableID:59, RowCount:0, ArgLen:1, start time: 2024-07-01 15:11:59.939 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:11:59.945 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:60, Type:create table, State:synced, SchemaState:public, SchemaID:57, TableID:59, RowCount:0, ArgLen:0, start time: 2024-07-01 15:11:59.939 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:11:59.946 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=60]
   > [2024/07/01 15:11:59.946 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:11:59.946 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=52] ["first split key"=74800000000000003b]
   > [2024/07/01 15:11:59.947 +00:00] [WARN] [2pc.go:1596] ["schemaLeaseChecker is not set for this transaction"] [sessionID=5] [startTS=450847498553786369] [commitTS=450847498553786370]
   > [2024/07/01 15:11:59.949 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=54] ["first at"=74800000000000003b] ["first new region left"="{Id:54 StartKey:7480000000000000ff3700000000000000f8 EndKey:7480000000000000ff3b00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:55 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/01 15:11:59.949 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[54]"]
   > [2024/07/01 15:11:59.950 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=5] [schemaVersion=30] [cur_db=testdb] [sql="\nCREATE TABLE `t_vejdy` (\n`c_iovir` int(11) NOT NULL,\n`c_r_mw3d` double DEFAULT NULL,\n`c_uxhghb` int(11) DEFAULT NULL,\n`c_rb7otb` int(11) NOT NULL,\n`c_dplyac` int(11) DEFAULT NULL,\n`c_lmcqed` double DEFAULT NULL,\n`c_ayaoed` text DEFAULT NULL,\n`c__zbqr` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_iovir`,`c_rb7otb`) /*T![clustered_index] NONCLUSTERED */,\nKEY `t_e1ejcd` (`c_uxhghb`),\nKEY `t_o6ui_b` (`c_iovir`,`c_r_mw3d`,`c_uxhghb`,`c_rb7otb`,`c_dplyac`,`c_lmcqed`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/07/01 15:11:59.951 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:62, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:61, RowCount:0, ArgLen:1, start time: 2024-07-01 15:11:59.95 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:11:59.951 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:62, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:61, RowCount:0, ArgLen:1, start time: 2024-07-01 15:11:59.95 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="\nCREATE TABLE `t_vejdy` (\n`c_iovir` int(11) NOT NULL,\n`c_r_mw3d` double DEFAULT NULL,\n`c_uxhghb` int(11) DEFAULT NULL,\n`c_rb7otb` int(11) NOT NULL,\n`c_dplyac` int(11) DEFAULT NULL,\n`c_lmcqed` double DEFAULT NULL,\n`c_ayaoed` text DEFAULT NULL,\n`c__zbqr` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_iovir`,`c_rb7otb`) /*T![clustered_index] NONCLUSTERED */,\nKEY `t_e1ejcd` (`c_uxhghb`),\nKEY `t_o6ui_b` (`c_iovir`,`c_r_mw3d`,`c_uxhghb`,`c_rb7otb`,`c_dplyac`,`c_lmcqed`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/01 15:11:59.952 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:62, Type:create table, State:none, SchemaState:queueing, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-07-01 15:11:59.95 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:11:59.954 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=30] [neededSchemaVersion=31] ["start time"=553.498µs] [phyTblIDs="[61]"] [actionTypes="[8]"]
   > [2024/07/01 15:11:59.956 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=31] ["take time"=2.188358ms] [job="ID:62, Type:create table, State:done, SchemaState:public, SchemaID:57, TableID:61, RowCount:0, ArgLen:1, start time: 2024-07-01 15:11:59.95 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:11:59.957 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:62, Type:create table, State:synced, SchemaState:public, SchemaID:57, TableID:61, RowCount:0, ArgLen:0, start time: 2024-07-01 15:11:59.95 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:11:59.959 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=62]
   > [2024/07/01 15:11:59.959 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:11:59.959 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=56] ["first split key"=74800000000000003d]
   > [2024/07/01 15:11:59.959 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=56] ["first at"=74800000000000003d] ["first new region left"="{Id:56 StartKey:7480000000000000ff3b00000000000000f8 EndKey:7480000000000000ff3d00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:57 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/01 15:11:59.960 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[56]"]
   > [2024/07/01 15:11:59.961 +00:00] [WARN] [2pc.go:1596] ["schemaLeaseChecker is not set for this transaction"] [sessionID=5] [startTS=450847498557194241] [commitTS=450847498557456384]
   > [2024/07/01 15:12:01.020 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=7] [user=root] [host=]
   > [2024/07/01 15:12:01.035 +00:00] [INFO] [set.go:139] ["set global var"] [conn=7] [name=tx_isolation] [val=REPEATABLE-READ]

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
   > [2024/07/01 15:12:03.443 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=11] [user=root] [host=]
   > [2024/07/01 15:12:03.446 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=39] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/07/01 15:12:03.447 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:69, Type:drop schema, State:none, SchemaState:queueing, SchemaID:64, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:03.446 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:12:03.447 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:69, Type:drop schema, State:none, SchemaState:queueing, SchemaID:64, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:03.446 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/07/01 15:12:03.448 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:69, Type:drop schema, State:none, SchemaState:queueing, SchemaID:64, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:03.446 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:03.449 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=39] [neededSchemaVersion=40] ["start time"=139.544µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:12:03.451 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=40] ["take time"=2.245489ms] [job="ID:69, Type:drop schema, State:running, SchemaState:write only, SchemaID:64, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:03.446 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:03.451 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:69, Type:drop schema, State:running, SchemaState:write only, SchemaID:64, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:03.446 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:03.452 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=40] [neededSchemaVersion=41] ["start time"=129.068µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:12:03.454 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=41] ["take time"=2.424774ms] [job="ID:69, Type:drop schema, State:running, SchemaState:delete only, SchemaID:64, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:03.446 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:03.455 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:69, Type:drop schema, State:running, SchemaState:delete only, SchemaID:64, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:03.446 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:03.456 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=41] [neededSchemaVersion=42] ["start time"=110.7µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:12:03.458 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=42] ["take time"=2.212524ms] [job="ID:69, Type:drop schema, State:done, SchemaState:queueing, SchemaID:64, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:03.446 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:03.458 +00:00] [INFO] [delete_range.go:107] ["[ddl] add job into delete-range table"] [jobID=69] [jobType="drop schema"]
   > [2024/07/01 15:12:03.458 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:69, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:64, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:03.446 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:03.459 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=69]
   > [2024/07/01 15:12:03.459 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:12:03.461 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=42] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/07/01 15:12:03.462 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:71, Type:create schema, State:none, SchemaState:queueing, SchemaID:70, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:03.462 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:12:03.462 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:71, Type:create schema, State:none, SchemaState:queueing, SchemaID:70, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:03.462 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/07/01 15:12:03.462 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:71, Type:create schema, State:none, SchemaState:queueing, SchemaID:70, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:03.462 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:03.463 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=42] [neededSchemaVersion=43] ["start time"=105.252µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/07/01 15:12:03.465 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=43] ["take time"=2.23627ms] [job="ID:71, Type:create schema, State:done, SchemaState:public, SchemaID:70, TableID:0, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:03.462 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:03.466 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:71, Type:create schema, State:synced, SchemaState:public, SchemaID:70, TableID:0, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:03.462 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:03.467 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=71]
   > [2024/07/01 15:12:03.467 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:12:03.471 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=43] [cur_db=testdb] [sql="drop table if exists t_tir89b, t_vejdy;"] [user=root@127.0.0.1]
   > [2024/07/01 15:12:03.471 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=43] [cur_db=testdb] [sql="\nCREATE TABLE `t_tir89b` (\n`c_3pcik` int(11) DEFAULT NULL,\n`c_0b6nxb` text DEFAULT NULL,\n`c_qytrlc` double NOT NULL,\n`c_sroc_c` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_qytrlc`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/07/01 15:12:03.473 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:73, Type:create table, State:none, SchemaState:queueing, SchemaID:70, TableID:72, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:03.472 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:12:03.473 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:73, Type:create table, State:none, SchemaState:queueing, SchemaID:70, TableID:72, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:03.472 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="\nCREATE TABLE `t_tir89b` (\n`c_3pcik` int(11) DEFAULT NULL,\n`c_0b6nxb` text DEFAULT NULL,\n`c_qytrlc` double NOT NULL,\n`c_sroc_c` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_qytrlc`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/01 15:12:03.473 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:73, Type:create table, State:none, SchemaState:queueing, SchemaID:70, TableID:72, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:03.472 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:03.475 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=43] [neededSchemaVersion=44] ["start time"=458.303µs] [phyTblIDs="[72]"] [actionTypes="[8]"]
   > [2024/07/01 15:12:03.477 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=44] ["take time"=2.051958ms] [job="ID:73, Type:create table, State:done, SchemaState:public, SchemaID:70, TableID:72, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:03.472 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:03.478 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:73, Type:create table, State:synced, SchemaState:public, SchemaID:70, TableID:72, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:03.472 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:03.479 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=73]
   > [2024/07/01 15:12:03.479 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:12:03.479 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=60] ["first split key"=748000000000000048]
   > [2024/07/01 15:12:03.479 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=60] ["first at"=748000000000000048] ["first new region left"="{Id:60 StartKey:7480000000000000ff4200000000000000f8 EndKey:7480000000000000ff4800000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:61 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/01 15:12:03.479 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[60]"]
   > [2024/07/01 15:12:03.480 +00:00] [WARN] [2pc.go:1596] ["schemaLeaseChecker is not set for this transaction"] [sessionID=11] [startTS=450847499479941120] [commitTS=450847499479941121]
   > [2024/07/01 15:12:03.482 +00:00] [INFO] [session.go:2865] ["CRUCIAL OPERATION"] [conn=11] [schemaVersion=44] [cur_db=testdb] [sql="\nCREATE TABLE `t_vejdy` (\n`c_iovir` int(11) NOT NULL,\n`c_r_mw3d` double DEFAULT NULL,\n`c_uxhghb` int(11) DEFAULT NULL,\n`c_rb7otb` int(11) NOT NULL,\n`c_dplyac` int(11) DEFAULT NULL,\n`c_lmcqed` double DEFAULT NULL,\n`c_ayaoed` text DEFAULT NULL,\n`c__zbqr` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_iovir`,`c_rb7otb`) /*T![clustered_index] NONCLUSTERED */,\nKEY `t_e1ejcd` (`c_uxhghb`),\nKEY `t_o6ui_b` (`c_iovir`,`c_r_mw3d`,`c_uxhghb`,`c_rb7otb`,`c_dplyac`,`c_lmcqed`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/07/01 15:12:03.484 +00:00] [INFO] [ddl_worker.go:313] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:75, Type:create table, State:none, SchemaState:queueing, SchemaID:70, TableID:74, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:03.483 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/07/01 15:12:03.484 +00:00] [INFO] [ddl.go:553] ["[ddl] start DDL job"] [job="ID:75, Type:create table, State:none, SchemaState:queueing, SchemaID:70, TableID:74, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:03.483 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="\nCREATE TABLE `t_vejdy` (\n`c_iovir` int(11) NOT NULL,\n`c_r_mw3d` double DEFAULT NULL,\n`c_uxhghb` int(11) DEFAULT NULL,\n`c_rb7otb` int(11) NOT NULL,\n`c_dplyac` int(11) DEFAULT NULL,\n`c_lmcqed` double DEFAULT NULL,\n`c_ayaoed` text DEFAULT NULL,\n`c__zbqr` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_iovir`,`c_rb7otb`) /*T![clustered_index] NONCLUSTERED */,\nKEY `t_e1ejcd` (`c_uxhghb`),\nKEY `t_o6ui_b` (`c_iovir`,`c_r_mw3d`,`c_uxhghb`,`c_rb7otb`,`c_dplyac`,`c_lmcqed`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/07/01 15:12:03.485 +00:00] [INFO] [ddl_worker.go:718] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:75, Type:create table, State:none, SchemaState:queueing, SchemaID:70, TableID:74, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:03.483 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:03.488 +00:00] [INFO] [domain.go:135] ["diff load InfoSchema success"] [currentSchemaVersion=44] [neededSchemaVersion=45] ["start time"=826.021µs] [phyTblIDs="[74]"] [actionTypes="[8]"]
   > [2024/07/01 15:12:03.489 +00:00] [INFO] [ddl_worker.go:921] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=45] ["take time"=2.250658ms] [job="ID:75, Type:create table, State:done, SchemaState:public, SchemaID:70, TableID:74, RowCount:0, ArgLen:1, start time: 2024-07-01 15:12:03.483 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:03.491 +00:00] [INFO] [ddl_worker.go:418] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:75, Type:create table, State:synced, SchemaState:public, SchemaID:70, TableID:74, RowCount:0, ArgLen:0, start time: 2024-07-01 15:12:03.483 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/07/01 15:12:03.492 +00:00] [INFO] [ddl.go:615] ["[ddl] DDL job is finished"] [jobID=75]
   > [2024/07/01 15:12:03.492 +00:00] [INFO] [callback.go:107] ["performing DDL change, must reload"]
   > [2024/07/01 15:12:03.492 +00:00] [INFO] [split_region.go:85] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=62] ["first split key"=74800000000000004a]
   > [2024/07/01 15:12:03.493 +00:00] [INFO] [split_region.go:186] ["batch split regions complete"] ["batch region ID"=62] ["first at"=74800000000000004a] ["first new region left"="{Id:62 StartKey:7480000000000000ff4800000000000000f8 EndKey:7480000000000000ff4a00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:63 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/07/01 15:12:03.493 +00:00] [INFO] [split_region.go:235] ["split regions complete"] ["region count"=1] ["region IDs"="[62]"]
   > [2024/07/01 15:12:03.494 +00:00] [WARN] [2pc.go:1596] ["schemaLeaseChecker is not set for this transaction"] [sessionID=11] [startTS=450847499483611137] [commitTS=450847499483611138]
   > [2024/07/01 15:12:04.610 +00:00] [WARN] [conn.go:858] ["No user plugin set, assuming MySQL Native Password"] [conn=13] [user=root] [host=]
   > [2024/07/01 15:12:04.632 +00:00] [INFO] [set.go:139] ["set global var"] [conn=13] [name=tx_isolation] [val=REPEATABLE-READ]
