# Bug ID MDEV-25297-READ_COMMITTED

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-25297
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              A rollback makes the database crash.


## Details
 * Database: mariadb-356c1496-debug
 * Number of scenarios: 2
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 0 / 0
 * Instruction #1:
     - Instruction:  BEGIN;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  SET sql_mode='';
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 0 / 0
 * Instruction #3:
     - Instruction:  SET unique_checks=0;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 0 / 0
 * Instruction #4:
     - Instruction:  SET foreign_key_checks=0;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows / Warnings: 0 / 0
 * Instruction #5:
     - Instruction:  CREATE TABLE ti (b INT,c INT,e INT,id INT,KEY (b),KEY (e),PRIMARY KEY(id));
     - Transaction: conn_0
     - Output: None
     - Executed order: 5
     - Affected rows / Warnings: 0 / 0
 * Instruction #6:
     - Instruction:  INSERT INTO ti VALUES(0,0,0,0);
     - Transaction: conn_0
     - Output: None
     - Executed order: 6
     - Affected rows / Warnings: 1 / 0
 * Instruction #7:
     - Instruction:  ALTER TABLE ti CHANGE COLUMN c c BINARY (1);
     - Transaction: conn_0
     - Output: None
     - Executed order: 7
     - Affected rows / Warnings: 1 / 0
 * Instruction #8:
     - Instruction:  XA START 'a';
     - Transaction: conn_0
     - Output: None
     - Executed order: 8
     - Affected rows / Warnings: 0 / 0
 * Instruction #9:
     - Instruction:  CREATE TEMPORARY TABLE t(a INT);
     - Transaction: conn_0
     - Output: None
     - Executed order: 9
     - Affected rows / Warnings: 0 / 0
 * Instruction #10:
     - Instruction:  INSERT INTO t VALUES(1);
     - Transaction: conn_0
     - Output: None
     - Executed order: 10
     - Affected rows / Warnings: 1 / 0
 * Instruction #11:
     - Instruction:  SAVEPOINT a3;
     - Transaction: conn_0
     - Output: None
     - Executed order: 11
     - Affected rows / Warnings: 0 / 0
 * Instruction #12:
     - Instruction:  CREATE OR REPLACE TEMPORARY TABLE t (a INT,b INT);
     - Transaction: conn_0
     - Output: None
     - Executed order: 12
     - Affected rows / Warnings: 0 / 0
 * Instruction #13:
     - Instruction:  INSERT INTO t VALUES(0,0);
     - Transaction: conn_0
     - Output: None
     - Executed order: 13
     - Affected rows / Warnings: 1 / 0
 * Instruction #14:
     - Instruction:  INSERT INTO ti VALUES(0,0,0,0);
     - Transaction: conn_0
     - Output: ERROR: 1062 (23000): Duplicate entry '0' for key 'PRIMARY'
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #15:
     - Instruction:  ROLLBACK TO SAVEPOINT a3;
     - Transaction: conn_0
     - Output: ERROR: 2013 (HY000): Lost connection to MySQL server during query
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #16:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: ERROR: MySQL Connection not available.
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0

 * Container logs:
   > 2024-07-22 12:22:44 0x7f31383ed700  InnoDB: Assertion failure in file /server/server/storage/innobase/trx/trx0roll.cc line 869
   > InnoDB: Failing assertion: trx->roll_limit <= trx->undo_no
   > InnoDB: We intentionally generate a memory trap.
   > InnoDB: Submit a detailed bug report to https://jira.mariadb.org/
   > InnoDB: If you get repeated assertion failures or crashes, even
   > InnoDB: immediately after the mysqld startup, there may be
   > InnoDB: corruption in the InnoDB tablespace. Please refer to
   > InnoDB: https://mariadb.com/kb/en/library/innodb-recovery-modes/
   > InnoDB: about forcing recovery.
   > 240722 12:22:44 [ERROR] mysqld got signal 6 ;
   > This could be because you hit a bug. It is also possible that this binary
   > or one of the libraries it was linked against is corrupt, improperly built,
   > or misconfigured. This error can also be caused by malfunctioning hardware.
   > To report this bug, see https://mariadb.com/kb/en/reporting-bugs
   > We will try our best to scrape up some info that will hopefully help
   > diagnose the problem, but since we have already crashed, 
   > something is definitely wrong and this may fail.
   > Server version: 10.6.0-MariaDB-debug
   > key_buffer_size=134217728
   > read_buffer_size=131072
   > max_used_connections=1
   > max_threads=153
   > thread_count=1
   > It is possible that mysqld could use up to 
   > key_buffer_size + (read_buffer_size + sort_buffer_size)*max_threads = 468024 K  bytes of memory
   > Hope that's ok; if not, decrease some variables in the equation.
   > Thread pointer: 0x62b000070288
   > Attempting backtrace. You can use the following information to find out
   > where mysqld died. If you see no messages after this, something went
   > terribly wrong...
   > stack_bottom = 0x7f31383eccd0 thread_stack 0x100000
   > ??:0(__interceptor_sched_getaffinity)[0x7f315a8298c0]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x55e35f2ed557]
   > sql/signal_handler.cc:212(handle_fatal_signal)[0x55e35dea0050]
   > ??:0(__restore_rt)[0x7f3158eff980]
   > linux/raise.c:51(__GI_raise)[0x7f3157ff7e87]
   > stdlib/abort.c:81(__GI_abort)[0x7f3157ff97f1]
   > ut/ut0dbg.cc:60(_GLOBAL__sub_D_00099_0_ut0dbg.cc)[0x55e35ee02a86]
   > trx/trx0roll.cc:871(trx_rollback_start(trx_t*, unsigned long))[0x55e35edbdf06]
   > trx/trx0roll.cc:935(trx_rollback_step(que_thr_t*))[0x55e35edbe2e1]
   > que/que0que.cc:659(que_thr_step(que_thr_t*))[0x55e35ebabbad]
   > que/que0que.cc:709(que_run_threads_low(que_thr_t*))[0x55e35ebabf04]
   > que/que0que.cc:731(que_run_threads(que_thr_t*))[0x55e35ebac0a2]
   > trx/trx0roll.cc:117(trx_t::rollback_low(trx_savept_t*))[0x55e35edbfe9c]
   > trx/trx0roll.cc:165(trx_t::rollback(trx_savept_t*))[0x55e35edb8d4f]
   > trx/trx0roll.cc:419(trx_rollback_to_savepoint_for_mysql_low(trx_t*, trx_named_savept_t*, long*))[0x55e35edbb01b]
   > trx/trx0roll.cc:479(trx_rollback_to_savepoint_for_mysql(trx_t*, char const*, long*))[0x55e35edbb365]
   > handler/ha_innodb.cc:4388(innobase_rollback_to_savepoint(handlerton*, THD*, void*))[0x55e35e8e5a73]
   > sql/handler.cc:2503(ha_rollback_to_savepoint(THD*, st_savepoint*))[0x55e35deb3db0]
   > sql/transaction.cc:697(trans_rollback_to_savepoint(THD*, st_mysql_const_lex_string))[0x55e35db35b6a]
   > sql/sql_parse.cc:5670(mysql_execute_command(THD*))[0x55e35d6d8ddd]
   > sql/sql_parse.cc:8004(mysql_parse(THD*, char*, unsigned int, Parser_state*))[0x55e35d6e847e]
   > sql/sql_parse.cc:1890(dispatch_command(enum_server_command, THD*, char*, unsigned int, bool))[0x55e35d6bf0e6]
   > sql/sql_parse.cc:1399(do_command(THD*, bool))[0x55e35d6bbd90]
   > sql/sql_connect.cc:1410(do_handle_one_connection(CONNECT*, bool))[0x55e35daf351e]
   > sql/sql_connect.cc:1314(handle_one_connection)[0x55e35daf2e70]
   > perfschema/pfs.cc:2203(pfs_spawn_thread)[0x55e35e70746d]
   > nptl/pthread_create.c:463(start_thread)[0x7f3158ef46db]
   > x86_64/clone.S:97(clone)[0x7f31580da61f]
   > Trying to get some variables.
   > Some pointers may be invalid and cause the dump to abort.
   > Query (0x62b0000772a8): ROLLBACK TO SAVEPOINT a3
   > Connection ID (thread ID): 5
   > Status: NOT_KILLED
   > Optimizer switch: index_merge=on,index_merge_union=on,index_merge_sort_union=on,index_merge_intersection=on,index_merge_sort_intersection=off,engine_condition_pushdown=off,index_condition_pushdown=on,derived_merge=on,derived_with_keys=on,firstmatch=on,loosescan=on,materialization=on,in_to_exists=on,semijoin=on,partial_match_rowid_merge=on,partial_match_table_scan=on,subquery_cache=on,mrr=off,mrr_cost_based=off,mrr_sort_keys=off,outer_join_with_cache=on,semijoin_with_cache=on,join_cache_incremental=on,join_cache_hashed=on,join_cache_bka=on,optimize_join_buffer_size=on,table_elimination=on,extended_keys=on,exists_to_in=on,orderby_uses_equalities=on,condition_pushdown_for_derived=on,split_materialized=on,condition_pushdown_for_subquery=on,rowid_filter=on,condition_pushdown_from_having=on,not_null_range_scan=off
   > The manual page at https://mariadb.com/kb/en/how-to-produce-a-full-stack-trace-for-mysqld/ contains
   > information that should help you find out what is causing the crash.
   > Writing a core file...
   > Working directory at /usr/local/mysql/data
   > Resource Limits:
   > Limit                     Soft Limit           Hard Limit           Units     
   > Max cpu time              unlimited            unlimited            seconds   
   > Max file size             unlimited            unlimited            bytes     
   > Max data size             unlimited            unlimited            bytes     
   > Max stack size            8388608              unlimited            bytes     
   > Max core file size        0                    0                    bytes     
   > Max resident set          unlimited            unlimited            bytes     
   > Max processes             61160                61160                processes 
   > Max open files            524288               524288               files     
   > Max locked memory         8388608              8388608              bytes     
   > Max address space         unlimited            unlimited            bytes     
   > Max file locks            unlimited            unlimited            locks     
   > Max pending signals       61160                61160                signals   
   > Max msgqueue size         819200               819200               bytes     
   > Max nice priority         0                    0                    
   > Max realtime priority     0                    0                    
   > Max realtime timeout      200000               200000               us        
   > Core pattern: |/usr/lib/systemd/systemd-coredump %P %u %g %s %t %c %h
   > ASAN:DEADLYSIGNAL
   > =================================================================
   > ==1==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x7f3157ff98e0 bp 0x7f31383ea580 sp 0x7f31383ea430 T12)
   > ==1==The signal is caused by a READ memory access.
   > ==1==Hint: address points to the zero page.
   >     #0 0x7f3157ff98df in abort (/lib/x86_64-linux-gnu/libc.so.6+0x408df)
   >     #1 0x55e35ee02a85 in ut_dbg_assertion_failed(char const*, char const*, unsigned int) /server/server/storage/innobase/ut/ut0dbg.cc:60
   >     #2 0x55e35edbdf05 in trx_rollback_start /server/server/storage/innobase/trx/trx0roll.cc:869
   >     #3 0x55e35edbe2e0 in trx_rollback_step(que_thr_t*) /server/server/storage/innobase/trx/trx0roll.cc:935
   >     #4 0x55e35ebabbac in que_thr_step /server/server/storage/innobase/que/que0que.cc:659
   >     #5 0x55e35ebabf03 in que_run_threads_low /server/server/storage/innobase/que/que0que.cc:709
   >     #6 0x55e35ebac0a1 in que_run_threads(que_thr_t*) /server/server/storage/innobase/que/que0que.cc:729
   >     #7 0x55e35edbfe9b in trx_t::rollback_low(trx_savept_t*) /server/server/storage/innobase/trx/trx0roll.cc:116
   >     #8 0x55e35edb8d4e in trx_t::rollback(trx_savept_t*) /server/server/storage/innobase/trx/trx0roll.cc:164
   >     #9 0x55e35edbb01a in trx_rollback_to_savepoint_for_mysql_low /server/server/storage/innobase/trx/trx0roll.cc:419
   >     #10 0x55e35edbb364 in trx_rollback_to_savepoint_for_mysql(trx_t*, char const*, long*) /server/server/storage/innobase/trx/trx0roll.cc:479
   >     #11 0x55e35e8e5a72 in innobase_rollback_to_savepoint /server/server/storage/innobase/handler/ha_innodb.cc:4388
   >     #12 0x55e35deb3daf in ha_rollback_to_savepoint(THD*, st_savepoint*) /server/server/sql/handler.cc:2503
   >     #13 0x55e35db35b69 in trans_rollback_to_savepoint(THD*, st_mysql_const_lex_string) /server/server/sql/transaction.cc:697
   >     #14 0x55e35d6d8ddc in mysql_execute_command(THD*) /server/server/sql/sql_parse.cc:5670
   >     #15 0x55e35d6e847d in mysql_parse(THD*, char*, unsigned int, Parser_state*) /server/server/sql/sql_parse.cc:8004
   >     #16 0x55e35d6bf0e5 in dispatch_command(enum_server_command, THD*, char*, unsigned int, bool) /server/server/sql/sql_parse.cc:1888
   >     #17 0x55e35d6bbd8f in do_command(THD*, bool) /server/server/sql/sql_parse.cc:1399
   >     #18 0x55e35daf351d in do_handle_one_connection(CONNECT*, bool) /server/server/sql/sql_connect.cc:1410
   >     #19 0x55e35daf2e6f in handle_one_connection /server/server/sql/sql_connect.cc:1312
   >     #20 0x55e35e70746c in pfs_spawn_thread /server/server/storage/perfschema/pfs.cc:2201
   >     #21 0x7f3158ef46da in start_thread (/lib/x86_64-linux-gnu/libpthread.so.0+0x76da)
   >     #22 0x7f31580da61e in __clone (/lib/x86_64-linux-gnu/libc.so.6+0x12161e)
   > AddressSanitizer can not provide additional info.
   > SUMMARY: AddressSanitizer: SEGV (/lib/x86_64-linux-gnu/libc.so.6+0x408df) in abort
   > Thread T12 created by T0 here:
   >     #0 0x7f315a80bd2f in __interceptor_pthread_create (/usr/lib/x86_64-linux-gnu/libasan.so.4+0x37d2f)
   >     #1 0x55e35e7021be in my_thread_create /server/server/storage/perfschema/my_thread.h:38
   >     #2 0x55e35e70785b in pfs_spawn_thread_v1 /server/server/storage/perfschema/pfs.cc:2252
   >     #3 0x55e35d3c0703 in inline_mysql_thread_create /server/server/include/mysql/psi/mysql_thread.h:1139
   >     #4 0x55e35d3d6019 in create_thread_to_handle_connection(CONNECT*) /server/server/sql/mysqld.cc:5737
   >     #5 0x55e35d3d667a in create_new_thread(CONNECT*) /server/server/sql/mysqld.cc:5796
   >     #6 0x55e35d3d69ad in handle_accepted_socket(st_mysql_socket, st_mysql_socket) /server/server/sql/mysqld.cc:5858
   >     #7 0x55e35d3d727d in handle_connections_sockets() /server/server/sql/mysqld.cc:5982
   >     #8 0x55e35d3d5861 in mysqld_main(int, char**) /server/server/sql/mysqld.cc:5632
   >     #9 0x55e35d3bf909 in main /server/server/sql/main.cc:25
   >     #10 0x7f3157fdac86 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21c86)
   > ==1==ABORTING

### Scenario 1
 * Instruction #0:
     - Instruction:  SET sql_mode='';
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 0 / 0
 * Instruction #1:
     - Instruction:  SET unique_checks=0;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  SET foreign_key_checks=0;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 0 / 0
 * Instruction #3:
     - Instruction:  CREATE TABLE ti (b INT,c INT,e INT,id INT,KEY (b),KEY (e),PRIMARY KEY(id));
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 0 / 0
 * Instruction #4:
     - Instruction:  INSERT INTO ti VALUES(0,0,0,0);
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows / Warnings: 1 / 0
 * Instruction #5:
     - Instruction:  ALTER TABLE ti CHANGE COLUMN c c BINARY (1);
     - Transaction: conn_0
     - Output: None
     - Executed order: 5
     - Affected rows / Warnings: 1 / 0
 * Instruction #6:
     - Instruction:  XA START 'a';
     - Transaction: conn_0
     - Output: None
     - Executed order: 6
     - Affected rows / Warnings: 0 / 0
 * Instruction #7:
     - Instruction:  CREATE TEMPORARY TABLE t(a INT);
     - Transaction: conn_0
     - Output: None
     - Executed order: 7
     - Affected rows / Warnings: 0 / 0
 * Instruction #8:
     - Instruction:  INSERT INTO t VALUES(1);
     - Transaction: conn_0
     - Output: None
     - Executed order: 8
     - Affected rows / Warnings: 1 / 0
 * Instruction #9:
     - Instruction:  SAVEPOINT a3;
     - Transaction: conn_0
     - Output: None
     - Executed order: 9
     - Affected rows / Warnings: 0 / 0
 * Instruction #10:
     - Instruction:  CREATE OR REPLACE TEMPORARY TABLE t (a INT,b INT);
     - Transaction: conn_0
     - Output: None
     - Executed order: 10
     - Affected rows / Warnings: 0 / 0
 * Instruction #11:
     - Instruction:  INSERT INTO t VALUES(0,0);
     - Transaction: conn_0
     - Output: None
     - Executed order: 11
     - Affected rows / Warnings: 1 / 0
 * Instruction #12:
     - Instruction:  INSERT INTO ti VALUES(0,0,0,0);
     - Transaction: conn_0
     - Output: ERROR: 1062 (23000): Duplicate entry '0' for key 'PRIMARY'
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #13:
     - Instruction:  ROLLBACK TO SAVEPOINT a3;
     - Transaction: conn_0
     - Output: ERROR: 2013 (HY000): Lost connection to MySQL server during query
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0

 * Container logs:
   > 2024-07-22 12:22:52 0x7f29afded700  InnoDB: Assertion failure in file /server/server/storage/innobase/trx/trx0roll.cc line 869
   > InnoDB: Failing assertion: trx->roll_limit <= trx->undo_no
   > InnoDB: We intentionally generate a memory trap.
   > InnoDB: Submit a detailed bug report to https://jira.mariadb.org/
   > InnoDB: If you get repeated assertion failures or crashes, even
   > InnoDB: immediately after the mysqld startup, there may be
   > InnoDB: corruption in the InnoDB tablespace. Please refer to
   > InnoDB: https://mariadb.com/kb/en/library/innodb-recovery-modes/
   > InnoDB: about forcing recovery.
   > 240722 12:22:52 [ERROR] mysqld got signal 6 ;
   > This could be because you hit a bug. It is also possible that this binary
   > or one of the libraries it was linked against is corrupt, improperly built,
   > or misconfigured. This error can also be caused by malfunctioning hardware.
   > To report this bug, see https://mariadb.com/kb/en/reporting-bugs
   > We will try our best to scrape up some info that will hopefully help
   > diagnose the problem, but since we have already crashed, 
   > something is definitely wrong and this may fail.
   > Server version: 10.6.0-MariaDB-debug
   > key_buffer_size=134217728
   > read_buffer_size=131072
   > max_used_connections=1
   > max_threads=153
   > thread_count=1
   > It is possible that mysqld could use up to 
   > key_buffer_size + (read_buffer_size + sort_buffer_size)*max_threads = 468024 K  bytes of memory
   > Hope that's ok; if not, decrease some variables in the equation.
   > Thread pointer: 0x62b000070288
   > Attempting backtrace. You can use the following information to find out
   > where mysqld died. If you see no messages after this, something went
   > terribly wrong...
   > stack_bottom = 0x7f29afdeccd0 thread_stack 0x100000
   > ??:0(__interceptor_sched_getaffinity)[0x7f29d222f8c0]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x5568a42ed557]
   > sql/signal_handler.cc:212(handle_fatal_signal)[0x5568a2ea0050]
   > ??:0(__restore_rt)[0x7f29d0905980]
   > linux/raise.c:51(__GI_raise)[0x7f29cf9fde87]
   > stdlib/abort.c:81(__GI_abort)[0x7f29cf9ff7f1]
   > ut/ut0dbg.cc:60(_GLOBAL__sub_D_00099_0_ut0dbg.cc)[0x5568a3e02a86]
   > trx/trx0roll.cc:871(trx_rollback_start(trx_t*, unsigned long))[0x5568a3dbdf06]
   > trx/trx0roll.cc:935(trx_rollback_step(que_thr_t*))[0x5568a3dbe2e1]
   > que/que0que.cc:659(que_thr_step(que_thr_t*))[0x5568a3babbad]
   > que/que0que.cc:709(que_run_threads_low(que_thr_t*))[0x5568a3babf04]
   > que/que0que.cc:731(que_run_threads(que_thr_t*))[0x5568a3bac0a2]
   > trx/trx0roll.cc:117(trx_t::rollback_low(trx_savept_t*))[0x5568a3dbfe9c]
   > trx/trx0roll.cc:165(trx_t::rollback(trx_savept_t*))[0x5568a3db8d4f]
   > trx/trx0roll.cc:419(trx_rollback_to_savepoint_for_mysql_low(trx_t*, trx_named_savept_t*, long*))[0x5568a3dbb01b]
   > trx/trx0roll.cc:479(trx_rollback_to_savepoint_for_mysql(trx_t*, char const*, long*))[0x5568a3dbb365]
   > handler/ha_innodb.cc:4388(innobase_rollback_to_savepoint(handlerton*, THD*, void*))[0x5568a38e5a73]
   > sql/handler.cc:2503(ha_rollback_to_savepoint(THD*, st_savepoint*))[0x5568a2eb3db0]
   > sql/transaction.cc:697(trans_rollback_to_savepoint(THD*, st_mysql_const_lex_string))[0x5568a2b35b6a]
   > sql/sql_parse.cc:5670(mysql_execute_command(THD*))[0x5568a26d8ddd]
   > sql/sql_parse.cc:8004(mysql_parse(THD*, char*, unsigned int, Parser_state*))[0x5568a26e847e]
   > sql/sql_parse.cc:1890(dispatch_command(enum_server_command, THD*, char*, unsigned int, bool))[0x5568a26bf0e6]
   > sql/sql_parse.cc:1399(do_command(THD*, bool))[0x5568a26bbd90]
   > sql/sql_connect.cc:1410(do_handle_one_connection(CONNECT*, bool))[0x5568a2af351e]
   > sql/sql_connect.cc:1314(handle_one_connection)[0x5568a2af2e70]
   > perfschema/pfs.cc:2203(pfs_spawn_thread)[0x5568a370746d]
   > nptl/pthread_create.c:463(start_thread)[0x7f29d08fa6db]
   > x86_64/clone.S:97(clone)[0x7f29cfae061f]
   > Trying to get some variables.
   > Some pointers may be invalid and cause the dump to abort.
   > Query (0x62b0000772a8): ROLLBACK TO SAVEPOINT a3
   > Connection ID (thread ID): 5
   > Status: NOT_KILLED
   > Optimizer switch: index_merge=on,index_merge_union=on,index_merge_sort_union=on,index_merge_intersection=on,index_merge_sort_intersection=off,engine_condition_pushdown=off,index_condition_pushdown=on,derived_merge=on,derived_with_keys=on,firstmatch=on,loosescan=on,materialization=on,in_to_exists=on,semijoin=on,partial_match_rowid_merge=on,partial_match_table_scan=on,subquery_cache=on,mrr=off,mrr_cost_based=off,mrr_sort_keys=off,outer_join_with_cache=on,semijoin_with_cache=on,join_cache_incremental=on,join_cache_hashed=on,join_cache_bka=on,optimize_join_buffer_size=on,table_elimination=on,extended_keys=on,exists_to_in=on,orderby_uses_equalities=on,condition_pushdown_for_derived=on,split_materialized=on,condition_pushdown_for_subquery=on,rowid_filter=on,condition_pushdown_from_having=on,not_null_range_scan=off
   > The manual page at https://mariadb.com/kb/en/how-to-produce-a-full-stack-trace-for-mysqld/ contains
   > information that should help you find out what is causing the crash.
   > Writing a core file...
   > Working directory at /usr/local/mysql/data
   > Resource Limits:
   > Limit                     Soft Limit           Hard Limit           Units     
   > Max cpu time              unlimited            unlimited            seconds   
   > Max file size             unlimited            unlimited            bytes     
   > Max data size             unlimited            unlimited            bytes     
   > Max stack size            8388608              unlimited            bytes     
   > Max core file size        0                    0                    bytes     
   > Max resident set          unlimited            unlimited            bytes     
   > Max processes             61160                61160                processes 
   > Max open files            524288               524288               files     
   > Max locked memory         8388608              8388608              bytes     
   > Max address space         unlimited            unlimited            bytes     
   > Max file locks            unlimited            unlimited            locks     
   > Max pending signals       61160                61160                signals   
   > Max msgqueue size         819200               819200               bytes     
   > Max nice priority         0                    0                    
   > Max realtime priority     0                    0                    
   > Max realtime timeout      200000               200000               us        
   > Core pattern: |/usr/lib/systemd/systemd-coredump %P %u %g %s %t %c %h
   > ASAN:DEADLYSIGNAL
   > =================================================================
   > ==1==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x7f29cf9ff8e0 bp 0x7f29afdea580 sp 0x7f29afdea430 T12)
   > ==1==The signal is caused by a READ memory access.
   > ==1==Hint: address points to the zero page.
   >     #0 0x7f29cf9ff8df in abort (/lib/x86_64-linux-gnu/libc.so.6+0x408df)
   >     #1 0x5568a3e02a85 in ut_dbg_assertion_failed(char const*, char const*, unsigned int) /server/server/storage/innobase/ut/ut0dbg.cc:60
   >     #2 0x5568a3dbdf05 in trx_rollback_start /server/server/storage/innobase/trx/trx0roll.cc:869
   >     #3 0x5568a3dbe2e0 in trx_rollback_step(que_thr_t*) /server/server/storage/innobase/trx/trx0roll.cc:935
   >     #4 0x5568a3babbac in que_thr_step /server/server/storage/innobase/que/que0que.cc:659
   >     #5 0x5568a3babf03 in que_run_threads_low /server/server/storage/innobase/que/que0que.cc:709
   >     #6 0x5568a3bac0a1 in que_run_threads(que_thr_t*) /server/server/storage/innobase/que/que0que.cc:729
   >     #7 0x5568a3dbfe9b in trx_t::rollback_low(trx_savept_t*) /server/server/storage/innobase/trx/trx0roll.cc:116
   >     #8 0x5568a3db8d4e in trx_t::rollback(trx_savept_t*) /server/server/storage/innobase/trx/trx0roll.cc:164
   >     #9 0x5568a3dbb01a in trx_rollback_to_savepoint_for_mysql_low /server/server/storage/innobase/trx/trx0roll.cc:419
   >     #10 0x5568a3dbb364 in trx_rollback_to_savepoint_for_mysql(trx_t*, char const*, long*) /server/server/storage/innobase/trx/trx0roll.cc:479
   >     #11 0x5568a38e5a72 in innobase_rollback_to_savepoint /server/server/storage/innobase/handler/ha_innodb.cc:4388
   >     #12 0x5568a2eb3daf in ha_rollback_to_savepoint(THD*, st_savepoint*) /server/server/sql/handler.cc:2503
   >     #13 0x5568a2b35b69 in trans_rollback_to_savepoint(THD*, st_mysql_const_lex_string) /server/server/sql/transaction.cc:697
   >     #14 0x5568a26d8ddc in mysql_execute_command(THD*) /server/server/sql/sql_parse.cc:5670
   >     #15 0x5568a26e847d in mysql_parse(THD*, char*, unsigned int, Parser_state*) /server/server/sql/sql_parse.cc:8004
   >     #16 0x5568a26bf0e5 in dispatch_command(enum_server_command, THD*, char*, unsigned int, bool) /server/server/sql/sql_parse.cc:1888
   >     #17 0x5568a26bbd8f in do_command(THD*, bool) /server/server/sql/sql_parse.cc:1399
   >     #18 0x5568a2af351d in do_handle_one_connection(CONNECT*, bool) /server/server/sql/sql_connect.cc:1410
   >     #19 0x5568a2af2e6f in handle_one_connection /server/server/sql/sql_connect.cc:1312
   >     #20 0x5568a370746c in pfs_spawn_thread /server/server/storage/perfschema/pfs.cc:2201
   >     #21 0x7f29d08fa6da in start_thread (/lib/x86_64-linux-gnu/libpthread.so.0+0x76da)
   >     #22 0x7f29cfae061e in __clone (/lib/x86_64-linux-gnu/libc.so.6+0x12161e)
   > AddressSanitizer can not provide additional info.
   > SUMMARY: AddressSanitizer: SEGV (/lib/x86_64-linux-gnu/libc.so.6+0x408df) in abort
   > Thread T12 created by T0 here:
   >     #0 0x7f29d2211d2f in __interceptor_pthread_create (/usr/lib/x86_64-linux-gnu/libasan.so.4+0x37d2f)
   >     #1 0x5568a37021be in my_thread_create /server/server/storage/perfschema/my_thread.h:38
   >     #2 0x5568a370785b in pfs_spawn_thread_v1 /server/server/storage/perfschema/pfs.cc:2252
   >     #3 0x5568a23c0703 in inline_mysql_thread_create /server/server/include/mysql/psi/mysql_thread.h:1139
   >     #4 0x5568a23d6019 in create_thread_to_handle_connection(CONNECT*) /server/server/sql/mysqld.cc:5737
   >     #5 0x5568a23d667a in create_new_thread(CONNECT*) /server/server/sql/mysqld.cc:5796
   >     #6 0x5568a23d69ad in handle_accepted_socket(st_mysql_socket, st_mysql_socket) /server/server/sql/mysqld.cc:5858
   >     #7 0x5568a23d727d in handle_connections_sockets() /server/server/sql/mysqld.cc:5982
   >     #8 0x5568a23d5861 in mysqld_main(int, char**) /server/server/sql/mysqld.cc:5632
   >     #9 0x5568a23bf909 in main /server/server/sql/main.cc:25
   >     #10 0x7f29cf9e0c86 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21c86)
   > ==1==ABORTING
