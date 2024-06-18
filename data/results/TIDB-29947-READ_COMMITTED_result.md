# Bug ID TIDB-29947-READ_COMMITTED

## Description

Link:                     https://github.com/pingcap/tidb/issues/29947
Original isolation level: IsolationLevel.REPEATABLE_READ
Tested isolation level:   IsolationLevel.READ_COMMITTED


## Details
 * Database: tidb-5.2.1
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
   > [2024/06/18 11:58:18.079 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=51] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:18.080 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:78, Type:drop schema, State:none, SchemaState:queueing, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:18.079 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 11:58:18.080 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:78, Type:drop schema, State:none, SchemaState:queueing, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:18.079 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/06/18 11:58:18.081 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:78, Type:drop schema, State:none, SchemaState:queueing, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:18.079 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:18.082 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=51] [neededSchemaVersion=52] ["start time"=89.049µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 11:58:18.084 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=52] ["take time"=2.174042ms] [job="ID:78, Type:drop schema, State:running, SchemaState:write only, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:18.079 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:18.085 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:78, Type:drop schema, State:running, SchemaState:write only, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:18.079 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:18.086 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=52] [neededSchemaVersion=53] ["start time"=105.95µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 11:58:18.089 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=53] ["take time"=3.08967ms] [job="ID:78, Type:drop schema, State:running, SchemaState:delete only, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:18.079 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:18.089 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:78, Type:drop schema, State:running, SchemaState:delete only, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:18.079 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:18.091 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=53] [neededSchemaVersion=54] ["start time"=177.818µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 11:58:18.093 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=54] ["take time"=2.288932ms] [job="ID:78, Type:drop schema, State:done, SchemaState:queueing, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:18.079 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:18.093 +00:00] [INFO] [delete_range.go:106] ["[ddl] add job into delete-range table"] [jobID=78] [jobType="drop schema"]
   > [2024/06/18 11:58:18.093 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:78, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:73, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:18.079 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:18.094 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=78]
   > [2024/06/18 11:58:18.094 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/18 11:58:18.096 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=54] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:18.098 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:80, Type:create schema, State:none, SchemaState:queueing, SchemaID:79, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:18.097 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 11:58:18.099 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:80, Type:create schema, State:none, SchemaState:queueing, SchemaID:79, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:18.097 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/18 11:58:18.099 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:80, Type:create schema, State:none, SchemaState:queueing, SchemaID:79, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:18.097 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:18.101 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=54] [neededSchemaVersion=55] ["start time"=287.19µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 11:58:18.103 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=55] ["take time"=2.303599ms] [job="ID:80, Type:create schema, State:done, SchemaState:public, SchemaID:79, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:18.097 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:18.104 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:80, Type:create schema, State:synced, SchemaState:public, SchemaID:79, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:18.097 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:18.105 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=80]
   > [2024/06/18 11:58:18.105 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/18 11:58:18.109 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=55] [cur_db=testdb] [sql="drop table if exists t_tir89b, t_vejdy;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:18.110 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=55] [cur_db=testdb] [sql="\nCREATE TABLE `t_tir89b` (\n`c_3pcik` int(11) DEFAULT NULL,\n`c_0b6nxb` text DEFAULT NULL,\n`c_qytrlc` double NOT NULL,\n`c_sroc_c` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_qytrlc`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:18.112 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:82, Type:create table, State:none, SchemaState:queueing, SchemaID:79, TableID:81, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:18.111 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 11:58:18.112 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:82, Type:create table, State:none, SchemaState:queueing, SchemaID:79, TableID:81, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:18.111 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="\nCREATE TABLE `t_tir89b` (\n`c_3pcik` int(11) DEFAULT NULL,\n`c_0b6nxb` text DEFAULT NULL,\n`c_qytrlc` double NOT NULL,\n`c_sroc_c` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_qytrlc`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/18 11:58:18.113 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:82, Type:create table, State:none, SchemaState:queueing, SchemaID:79, TableID:81, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:18.111 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:18.115 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=55] [neededSchemaVersion=56] ["start time"=489.662µs] [phyTblIDs="[81]"] [actionTypes="[8]"]
   > [2024/06/18 11:58:18.117 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=56] ["take time"=2.064181ms] [job="ID:82, Type:create table, State:done, SchemaState:public, SchemaID:79, TableID:81, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:18.111 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:18.118 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:82, Type:create table, State:synced, SchemaState:public, SchemaID:79, TableID:81, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:18.111 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:18.119 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=82]
   > [2024/06/18 11:58:18.119 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/18 11:58:18.120 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=62] ["first split key"=748000000000000051]
   > [2024/06/18 11:58:18.121 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=62] ["first at"=748000000000000051] ["first new region left"="{Id:62 StartKey:7480000000000000ff4b00000000000000f8 EndKey:7480000000000000ff5100000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:63 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/18 11:58:18.121 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[62]"]
   > [2024/06/18 11:58:18.122 +00:00] [WARN] [2pc.go:1598] ["schemaLeaseChecker is not set for this transaction"] [sessionID=17] [startTS=450550011821293569] [commitTS=450550011821293570]
   > [2024/06/18 11:58:18.126 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=17] [schemaVersion=56] [cur_db=testdb] [sql="\nCREATE TABLE `t_vejdy` (\n`c_iovir` int(11) NOT NULL,\n`c_r_mw3d` double DEFAULT NULL,\n`c_uxhghb` int(11) DEFAULT NULL,\n`c_rb7otb` int(11) NOT NULL,\n`c_dplyac` int(11) DEFAULT NULL,\n`c_lmcqed` double DEFAULT NULL,\n`c_ayaoed` text DEFAULT NULL,\n`c__zbqr` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_iovir`,`c_rb7otb`) /*T![clustered_index] NONCLUSTERED */,\nKEY `t_e1ejcd` (`c_uxhghb`),\nKEY `t_o6ui_b` (`c_iovir`,`c_r_mw3d`,`c_uxhghb`,`c_rb7otb`,`c_dplyac`,`c_lmcqed`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:18.128 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:84, Type:create table, State:none, SchemaState:queueing, SchemaID:79, TableID:83, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:18.127 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 11:58:18.128 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:84, Type:create table, State:none, SchemaState:queueing, SchemaID:79, TableID:83, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:18.127 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="\nCREATE TABLE `t_vejdy` (\n`c_iovir` int(11) NOT NULL,\n`c_r_mw3d` double DEFAULT NULL,\n`c_uxhghb` int(11) DEFAULT NULL,\n`c_rb7otb` int(11) NOT NULL,\n`c_dplyac` int(11) DEFAULT NULL,\n`c_lmcqed` double DEFAULT NULL,\n`c_ayaoed` text DEFAULT NULL,\n`c__zbqr` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_iovir`,`c_rb7otb`) /*T![clustered_index] NONCLUSTERED */,\nKEY `t_e1ejcd` (`c_uxhghb`),\nKEY `t_o6ui_b` (`c_iovir`,`c_r_mw3d`,`c_uxhghb`,`c_rb7otb`,`c_dplyac`,`c_lmcqed`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/18 11:58:18.129 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:84, Type:create table, State:none, SchemaState:queueing, SchemaID:79, TableID:83, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:18.127 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:18.132 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=56] [neededSchemaVersion=57] ["start time"=700.026µs] [phyTblIDs="[83]"] [actionTypes="[8]"]
   > [2024/06/18 11:58:18.134 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=57] ["take time"=2.513823ms] [job="ID:84, Type:create table, State:done, SchemaState:public, SchemaID:79, TableID:83, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:18.127 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:18.136 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:84, Type:create table, State:synced, SchemaState:public, SchemaID:79, TableID:83, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:18.127 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:18.138 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=84]
   > [2024/06/18 11:58:18.138 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/18 11:58:18.138 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=64] ["first split key"=748000000000000053]
   > [2024/06/18 11:58:18.139 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=64] ["first at"=748000000000000053] ["first new region left"="{Id:64 StartKey:7480000000000000ff5100000000000000f8 EndKey:7480000000000000ff5300000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:65 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/18 11:58:18.139 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[64]"]
   > [2024/06/18 11:58:18.140 +00:00] [WARN] [2pc.go:1598] ["schemaLeaseChecker is not set for this transaction"] [sessionID=17] [startTS=450550011826012161] [commitTS=450550011826012162]
   > [2024/06/18 11:58:19.187 +00:00] [INFO] [set.go:127] ["set global var"] [conn=19] [name=tx_isolation] [val=READ-COMMITTED]

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
   > [2024/06/18 11:58:21.590 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=23] [schemaVersion=65] [cur_db=] [sql="drop database if exists testdb;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:21.591 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:91, Type:drop schema, State:none, SchemaState:queueing, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:21.59 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 11:58:21.591 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:91, Type:drop schema, State:none, SchemaState:queueing, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:21.59 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="drop database if exists testdb;"]
   > [2024/06/18 11:58:21.591 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:91, Type:drop schema, State:none, SchemaState:queueing, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:21.59 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:21.592 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=65] [neededSchemaVersion=66] ["start time"=56.782µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 11:58:21.594 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=66] ["take time"=2.156232ms] [job="ID:91, Type:drop schema, State:running, SchemaState:write only, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:21.59 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:21.594 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:91, Type:drop schema, State:running, SchemaState:write only, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:21.59 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:21.595 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=66] [neededSchemaVersion=67] ["start time"=74.312µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 11:58:21.597 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=67] ["take time"=2.133045ms] [job="ID:91, Type:drop schema, State:running, SchemaState:delete only, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:21.59 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:21.597 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:91, Type:drop schema, State:running, SchemaState:delete only, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:21.59 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:21.599 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=67] [neededSchemaVersion=68] ["start time"=100.083µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 11:58:21.601 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=68] ["take time"=3.026464ms] [job="ID:91, Type:drop schema, State:done, SchemaState:queueing, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:21.59 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:21.602 +00:00] [INFO] [delete_range.go:106] ["[ddl] add job into delete-range table"] [jobID=91] [jobType="drop schema"]
   > [2024/06/18 11:58:21.602 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:91, Type:drop schema, State:synced, SchemaState:queueing, SchemaID:86, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:21.59 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:21.603 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=91]
   > [2024/06/18 11:58:21.603 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/18 11:58:21.604 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=23] [schemaVersion=68] [cur_db=] [sql="create database testdb;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:21.605 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:93, Type:create schema, State:none, SchemaState:queueing, SchemaID:92, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:21.604 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 11:58:21.605 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:93, Type:create schema, State:none, SchemaState:queueing, SchemaID:92, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:21.604 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="create database testdb;"]
   > [2024/06/18 11:58:21.605 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:93, Type:create schema, State:none, SchemaState:queueing, SchemaID:92, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:21.604 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:21.606 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=68] [neededSchemaVersion=69] ["start time"=211.971µs] [phyTblIDs="[]"] [actionTypes="[]"]
   > [2024/06/18 11:58:21.608 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=69] ["take time"=2.306602ms] [job="ID:93, Type:create schema, State:done, SchemaState:public, SchemaID:92, TableID:0, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:21.604 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:21.609 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:93, Type:create schema, State:synced, SchemaState:public, SchemaID:92, TableID:0, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:21.604 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:21.610 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=93]
   > [2024/06/18 11:58:21.610 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/18 11:58:21.613 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=23] [schemaVersion=69] [cur_db=testdb] [sql="drop table if exists t_tir89b, t_vejdy;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:21.614 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=23] [schemaVersion=69] [cur_db=testdb] [sql="\nCREATE TABLE `t_tir89b` (\n`c_3pcik` int(11) DEFAULT NULL,\n`c_0b6nxb` text DEFAULT NULL,\n`c_qytrlc` double NOT NULL,\n`c_sroc_c` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_qytrlc`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:21.615 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:95, Type:create table, State:none, SchemaState:queueing, SchemaID:92, TableID:94, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:21.615 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 11:58:21.615 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:95, Type:create table, State:none, SchemaState:queueing, SchemaID:92, TableID:94, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:21.615 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="\nCREATE TABLE `t_tir89b` (\n`c_3pcik` int(11) DEFAULT NULL,\n`c_0b6nxb` text DEFAULT NULL,\n`c_qytrlc` double NOT NULL,\n`c_sroc_c` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_qytrlc`) /*T![clustered_index] NONCLUSTERED */\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/18 11:58:21.616 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:95, Type:create table, State:none, SchemaState:queueing, SchemaID:92, TableID:94, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:21.615 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:21.618 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=69] [neededSchemaVersion=70] ["start time"=410.042µs] [phyTblIDs="[94]"] [actionTypes="[8]"]
   > [2024/06/18 11:58:21.619 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=70] ["take time"=2.02912ms] [job="ID:95, Type:create table, State:done, SchemaState:public, SchemaID:92, TableID:94, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:21.615 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:21.620 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:95, Type:create table, State:synced, SchemaState:public, SchemaID:92, TableID:94, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:21.615 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:21.622 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=95]
   > [2024/06/18 11:58:21.622 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/18 11:58:21.622 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=68] ["first split key"=74800000000000005e]
   > [2024/06/18 11:58:21.622 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=68] ["first at"=74800000000000005e] ["first new region left"="{Id:68 StartKey:7480000000000000ff5800000000000000f8 EndKey:7480000000000000ff5e00000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:69 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/18 11:58:21.622 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[68]"]
   > [2024/06/18 11:58:21.623 +00:00] [WARN] [2pc.go:1598] ["schemaLeaseChecker is not set for this transaction"] [sessionID=23] [startTS=450550012739059713] [commitTS=450550012739059714]
   > [2024/06/18 11:58:21.626 +00:00] [INFO] [session.go:2948] ["CRUCIAL OPERATION"] [conn=23] [schemaVersion=70] [cur_db=testdb] [sql="\nCREATE TABLE `t_vejdy` (\n`c_iovir` int(11) NOT NULL,\n`c_r_mw3d` double DEFAULT NULL,\n`c_uxhghb` int(11) DEFAULT NULL,\n`c_rb7otb` int(11) NOT NULL,\n`c_dplyac` int(11) DEFAULT NULL,\n`c_lmcqed` double DEFAULT NULL,\n`c_ayaoed` text DEFAULT NULL,\n`c__zbqr` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_iovir`,`c_rb7otb`) /*T![clustered_index] NONCLUSTERED */,\nKEY `t_e1ejcd` (`c_uxhghb`),\nKEY `t_o6ui_b` (`c_iovir`,`c_r_mw3d`,`c_uxhghb`,`c_rb7otb`,`c_dplyac`,`c_lmcqed`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"] [user=root@127.0.0.1]
   > [2024/06/18 11:58:21.628 +00:00] [INFO] [ddl_worker.go:318] ["[ddl] add DDL jobs"] ["batch count"=1] [jobs="ID:97, Type:create table, State:none, SchemaState:queueing, SchemaID:92, TableID:96, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:21.627 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0; "]
   > [2024/06/18 11:58:21.628 +00:00] [INFO] [ddl.go:546] ["[ddl] start DDL job"] [job="ID:97, Type:create table, State:none, SchemaState:queueing, SchemaID:92, TableID:96, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:21.627 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"] [query="\nCREATE TABLE `t_vejdy` (\n`c_iovir` int(11) NOT NULL,\n`c_r_mw3d` double DEFAULT NULL,\n`c_uxhghb` int(11) DEFAULT NULL,\n`c_rb7otb` int(11) NOT NULL,\n`c_dplyac` int(11) DEFAULT NULL,\n`c_lmcqed` double DEFAULT NULL,\n`c_ayaoed` text DEFAULT NULL,\n`c__zbqr` int(11) DEFAULT NULL,\nPRIMARY KEY (`c_iovir`,`c_rb7otb`) /*T![clustered_index] NONCLUSTERED */,\nKEY `t_e1ejcd` (`c_uxhghb`),\nKEY `t_o6ui_b` (`c_iovir`,`c_r_mw3d`,`c_uxhghb`,`c_rb7otb`,`c_dplyac`,`c_lmcqed`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"]
   > [2024/06/18 11:58:21.629 +00:00] [INFO] [ddl_worker.go:727] ["[ddl] run DDL job"] [worker="worker 3, tp general"] [job="ID:97, Type:create table, State:none, SchemaState:queueing, SchemaID:92, TableID:96, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:21.627 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:21.632 +00:00] [INFO] [domain.go:129] ["diff load InfoSchema success"] [currentSchemaVersion=70] [neededSchemaVersion=71] ["start time"=589.467µs] [phyTblIDs="[96]"] [actionTypes="[8]"]
   > [2024/06/18 11:58:21.633 +00:00] [INFO] [ddl_worker.go:912] ["[ddl] wait latest schema version changed"] [worker="worker 3, tp general"] [ver=71] ["take time"=2.259389ms] [job="ID:97, Type:create table, State:done, SchemaState:public, SchemaID:92, TableID:96, RowCount:0, ArgLen:1, start time: 2024-06-18 11:58:21.627 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:21.635 +00:00] [INFO] [ddl_worker.go:423] ["[ddl] finish DDL job"] [worker="worker 3, tp general"] [job="ID:97, Type:create table, State:synced, SchemaState:public, SchemaID:92, TableID:96, RowCount:0, ArgLen:0, start time: 2024-06-18 11:58:21.627 +0000 UTC, Err:<nil>, ErrCount:0, SnapshotVersion:0"]
   > [2024/06/18 11:58:21.636 +00:00] [INFO] [ddl.go:601] ["[ddl] DDL job is finished"] [jobID=97]
   > [2024/06/18 11:58:21.636 +00:00] [INFO] [callback.go:106] ["performing DDL change, must reload"]
   > [2024/06/18 11:58:21.636 +00:00] [INFO] [split_region.go:83] ["split batch regions request"] ["split key count"=1] ["batch count"=1] ["first batch, region ID"=70] ["first split key"=748000000000000060]
   > [2024/06/18 11:58:21.637 +00:00] [INFO] [split_region.go:184] ["batch split regions complete"] ["batch region ID"=70] ["first at"=748000000000000060] ["first new region left"="{Id:70 StartKey:7480000000000000ff5e00000000000000f8 EndKey:7480000000000000ff6000000000000000f8 RegionEpoch:{ConfVer:1 Version:2} Peers:[id:71 store_id:1 ] EncryptionMeta:<nil>}"] ["new region count"=1]
   > [2024/06/18 11:58:21.637 +00:00] [INFO] [split_region.go:233] ["split regions complete"] ["region count"=1] ["region IDs"="[70]"]
   > [2024/06/18 11:58:21.638 +00:00] [WARN] [2pc.go:1598] ["schemaLeaseChecker is not set for this transaction"] [sessionID=23] [startTS=450550012742991872] [commitTS=450550012742991873]
   > [2024/06/18 11:58:22.687 +00:00] [INFO] [set.go:127] ["set global var"] [conn=25] [name=tx_isolation] [val=READ-COMMITTED]
