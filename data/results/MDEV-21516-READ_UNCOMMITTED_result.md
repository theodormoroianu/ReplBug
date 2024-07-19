# Bug ID MDEV-21516-READ_UNCOMMITTED

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-21516
Original isolation level: REPEATABLE READ
Tested isolation level:   READ UNCOMMITTED
Description:              MariaDB crashes.


## Details
 * Database: mariadb-10.6.0-debug
 * Number of scenarios: 1
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 0 / 0
 * Instruction #1:
     - Instruction:  SET @save_limit = @@innodb_limit_optimistic_insert_debug;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  create table t1(a serial, b geometry not null, spatial index(b)) engine=innodb;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 0 / 0
 * Instruction #3:
     - Instruction:  SET GLOBAL innodb_limit_optimistic_insert_debug = 2;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 0 / 0
 * Instruction #4:
     - Instruction:  begin;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows / Warnings: 0 / 0
 * Instruction #5:
     - Instruction:  insert into t1 select seq, Point(1,1) from seq_1_to_5;
     - Transaction: conn_0
     - Output: None
     - Executed order: 5
     - Affected rows / Warnings: 5 / 0
 * Instruction #6:
     - Instruction:  rollback;
     - Transaction: conn_0
     - Output: ERROR: 2013 (HY000): Lost connection to MySQL server during query
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #7:
     - Instruction:  check table t1;
     - Transaction: conn_0
     - Output: ERROR: MySQL Connection not available.
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #8:
     - Instruction:  drop table t1;
     - Transaction: conn_0
     - Output: ERROR: MySQL Connection not available.
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #9:
     - Instruction:  SET GLOBAL innodb_limit_optimistic_insert_debug = @save_limit;
     - Transaction: conn_0
     - Output: ERROR: MySQL Connection not available.
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0

 * Container logs:
   > mysqld: /server/server/storage/innobase/gis/gis0sea.cc:1128: void rtr_rebuild_path(rtr_info_t*, ulint): Assertion `new_path->size() == before_size - 1' failed.
   > 240719 12:46:56 [ERROR] mysqld got signal 6 ;
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
   > key_buffer_size + (read_buffer_size + sort_buffer_size)*max_threads = 468088 K  bytes of memory
   > Hope that's ok; if not, decrease some variables in the equation.
   > Thread pointer: 0x62b000070288
   > Attempting backtrace. You can use the following information to find out
   > where mysqld died. If you see no messages after this, something went
   > terribly wrong...
   > stack_bottom = 0x7f5d19feccd0 thread_stack 0x100000
   > ??:0(__interceptor_sched_getaffinity)[0x7f5d3c3918c0]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x561a5e9305e4]
   > sql/signal_handler.cc:224(handle_fatal_signal)[0x561a5d4d3ae4]
   > ??:0(__restore_rt)[0x7f5d3aa67980]
   > linux/raise.c:51(__GI_raise)[0x7f5d39b5fe87]
   > stdlib/abort.c:81(__GI_abort)[0x7f5d39b617f1]
   > assert/assert.c:89(__assert_fail_base)[0x7f5d39b513fa]
   > ??:0(__assert_fail)[0x7f5d39b51472]
   > gis/gis0sea.cc:1130(rtr_rebuild_path(rtr_info*, unsigned long))[0x561a5e70ec64]
   > gis/gis0sea.cc:1182(rtr_check_discard_page(dict_index_t*, btr_cur_t*, buf_block_t*))[0x561a5e70f80f]
   > btr/btr0btr.cc:3383(btr_lift_page_up(dict_index_t*, buf_block_t*, mtr_t*))[0x561a5e46c3ec]
   > btr/btr0btr.cc:4130(btr_discard_page(btr_cur_t*, mtr_t*))[0x561a5e4719b8]
   > btr/btr0cur.cc:5809(btr_cur_pessimistic_delete(dberr_t*, unsigned long, btr_cur_t*, unsigned long, bool, mtr_t*))[0x561a5e4c30b5]
   > gis/gis0rtree.cc:1635(rtr_node_ptr_delete(btr_cur_t*, mtr_t*))[0x561a5e6fe3f0]
   > btr/btr0btr.cc:4084(btr_discard_page(btr_cur_t*, mtr_t*))[0x561a5e471705]
   > btr/btr0cur.cc:5809(btr_cur_pessimistic_delete(dberr_t*, unsigned long, btr_cur_t*, unsigned long, bool, mtr_t*))[0x561a5e4c30b5]
   > row/row0uins.cc:289(row_undo_ins_remove_sec_low(unsigned long, dict_index_t*, dtuple_t*, que_thr_t*))[0x561a5e7375b7]
   > row/row0uins.cc:327(row_undo_ins_remove_sec(dict_index_t*, dtuple_t*, que_thr_t*))[0x561a5e7377cd]
   > row/row0uins.cc:511(row_undo_ins_remove_sec_rec(undo_node_t*, que_thr_t*))[0x561a5e738c52]
   > row/row0uins.cc:563(row_undo_ins(undo_node_t*, que_thr_t*))[0x561a5e7390b3]
   > row/row0undo.cc:440(row_undo(undo_node_t*, que_thr_t*))[0x561a5e35d6f1]
   > row/row0undo.cc:496(row_undo_step(que_thr_t*))[0x561a5e35dbab]
   > que/que0que.cc:651(que_thr_step(que_thr_t*))[0x561a5e1e8614]
   > que/que0que.cc:709(que_run_threads_low(que_thr_t*))[0x561a5e1e89d8]
   > que/que0que.cc:731(que_run_threads(que_thr_t*))[0x561a5e1e8b76]
   > trx/trx0roll.cc:120(trx_t::rollback_low(trx_savept_t*))[0x561a5e3fff9b]
   > trx/trx0roll.cc:186(trx_rollback_for_mysql_low(trx_t*))[0x561a5e3f8eaa]
   > trx/trx0roll.cc:214(trx_rollback_for_mysql(trx_t*))[0x561a5e3f986c]
   > handler/ha_innodb.cc:4178(innobase_rollback(handlerton*, THD*, bool))[0x561a5df20d70]
   > sql/handler.cc:2056(ha_rollback_trans(THD*, bool))[0x561a5d4e4139]
   > sql/transaction.cc:372(trans_rollback(THD*))[0x561a5d15644b]
   > sql/sql_parse.cc:5651(mysql_execute_command(THD*))[0x561a5ccf8aa7]
   > sql/sql_parse.cc:8018(mysql_parse(THD*, char*, unsigned int, Parser_state*))[0x561a5cd083f9]
   > sql/sql_parse.cc:1899(dispatch_command(enum_server_command, THD*, char*, unsigned int, bool))[0x561a5ccdec7d]
   > sql/sql_parse.cc:1406(do_command(THD*, bool))[0x561a5ccdb919]
   > sql/sql_connect.cc:1410(do_handle_one_connection(CONNECT*, bool))[0x561a5d116603]
   > sql/sql_connect.cc:1314(handle_one_connection)[0x561a5d115f55]
   > perfschema/pfs.cc:2203(pfs_spawn_thread)[0x561a5dd3e647]
   > nptl/pthread_create.c:463(start_thread)[0x7f5d3aa5c6db]
   > x86_64/clone.S:97(clone)[0x7f5d39c4261f]
   > Trying to get some variables.
   > Some pointers may be invalid and cause the dump to abort.
   > Query (0x62b0000772a8): rollback
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
   > ==1==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x7f5d39b618e0 bp 0x7f5d39cd86c0 sp 0x7f5d19fe7c40 T12)
   > ==1==The signal is caused by a READ memory access.
   > ==1==Hint: address points to the zero page.
   >     #0 0x7f5d39b618df in abort (/lib/x86_64-linux-gnu/libc.so.6+0x408df)
   >     #1 0x7f5d39b513f9  (/lib/x86_64-linux-gnu/libc.so.6+0x303f9)
   >     #2 0x7f5d39b51471 in __assert_fail (/lib/x86_64-linux-gnu/libc.so.6+0x30471)
   >     #3 0x561a5e70ec63 in rtr_rebuild_path /server/server/storage/innobase/gis/gis0sea.cc:1128
   >     #4 0x561a5e70f80e in rtr_check_discard_page(dict_index_t*, btr_cur_t*, buf_block_t*) /server/server/storage/innobase/gis/gis0sea.cc:1181
   >     #5 0x561a5e46c3eb in btr_lift_page_up(dict_index_t*, buf_block_t*, mtr_t*) /server/server/storage/innobase/btr/btr0btr.cc:3379
   >     #6 0x561a5e4719b7 in btr_discard_page(btr_cur_t*, mtr_t*) /server/server/storage/innobase/btr/btr0btr.cc:4130
   >     #7 0x561a5e4c30b4 in btr_cur_pessimistic_delete(dberr_t*, unsigned long, btr_cur_t*, unsigned long, bool, mtr_t*) /server/server/storage/innobase/btr/btr0cur.cc:5807
   >     #8 0x561a5e6fe3ef in rtr_node_ptr_delete(btr_cur_t*, mtr_t*) /server/server/storage/innobase/gis/gis0rtree.cc:1635
   >     #9 0x561a5e471704 in btr_discard_page(btr_cur_t*, mtr_t*) /server/server/storage/innobase/btr/btr0btr.cc:4084
   >     #10 0x561a5e4c30b4 in btr_cur_pessimistic_delete(dberr_t*, unsigned long, btr_cur_t*, unsigned long, bool, mtr_t*) /server/server/storage/innobase/btr/btr0cur.cc:5807
   >     #11 0x561a5e7375b6 in row_undo_ins_remove_sec_low /server/server/storage/innobase/row/row0uins.cc:289
   >     #12 0x561a5e7377cc in row_undo_ins_remove_sec /server/server/storage/innobase/row/row0uins.cc:327
   >     #13 0x561a5e738c51 in row_undo_ins_remove_sec_rec /server/server/storage/innobase/row/row0uins.cc:511
   >     #14 0x561a5e7390b2 in row_undo_ins(undo_node_t*, que_thr_t*) /server/server/storage/innobase/row/row0uins.cc:563
   >     #15 0x561a5e35d6f0 in row_undo /server/server/storage/innobase/row/row0undo.cc:440
   >     #16 0x561a5e35dbaa in row_undo_step(que_thr_t*) /server/server/storage/innobase/row/row0undo.cc:496
   >     #17 0x561a5e1e8613 in que_thr_step /server/server/storage/innobase/que/que0que.cc:651
   >     #18 0x561a5e1e89d7 in que_run_threads_low /server/server/storage/innobase/que/que0que.cc:709
   >     #19 0x561a5e1e8b75 in que_run_threads(que_thr_t*) /server/server/storage/innobase/que/que0que.cc:729
   >     #20 0x561a5e3fff9a in trx_t::rollback_low(trx_savept_t*) /server/server/storage/innobase/trx/trx0roll.cc:117
   >     #21 0x561a5e3f8ea9 in trx_rollback_for_mysql_low /server/server/storage/innobase/trx/trx0roll.cc:184
   >     #22 0x561a5e3f986b in trx_rollback_for_mysql(trx_t*) /server/server/storage/innobase/trx/trx0roll.cc:214
   >     #23 0x561a5df20d6f in innobase_rollback /server/server/storage/innobase/handler/ha_innodb.cc:4178
   >     #24 0x561a5d4e4138 in ha_rollback_trans(THD*, bool) /server/server/sql/handler.cc:2056
   >     #25 0x561a5d15644a in trans_rollback(THD*) /server/server/sql/transaction.cc:372
   >     #26 0x561a5ccf8aa6 in mysql_execute_command(THD*) /server/server/sql/sql_parse.cc:5651
   >     #27 0x561a5cd083f8 in mysql_parse(THD*, char*, unsigned int, Parser_state*) /server/server/sql/sql_parse.cc:8018
   >     #28 0x561a5ccdec7c in dispatch_command(enum_server_command, THD*, char*, unsigned int, bool) /server/server/sql/sql_parse.cc:1897
   >     #29 0x561a5ccdb918 in do_command(THD*, bool) /server/server/sql/sql_parse.cc:1406
   >     #30 0x561a5d116602 in do_handle_one_connection(CONNECT*, bool) /server/server/sql/sql_connect.cc:1410
   >     #31 0x561a5d115f54 in handle_one_connection /server/server/sql/sql_connect.cc:1312
   >     #32 0x561a5dd3e646 in pfs_spawn_thread /server/server/storage/perfschema/pfs.cc:2201
   >     #33 0x7f5d3aa5c6da in start_thread (/lib/x86_64-linux-gnu/libpthread.so.0+0x76da)
   >     #34 0x7f5d39c4261e in __clone (/lib/x86_64-linux-gnu/libc.so.6+0x12161e)
   > AddressSanitizer can not provide additional info.
   > SUMMARY: AddressSanitizer: SEGV (/lib/x86_64-linux-gnu/libc.so.6+0x408df) in abort
   > Thread T12 created by T0 here:
   >     #0 0x7f5d3c373d2f in __interceptor_pthread_create (/usr/lib/x86_64-linux-gnu/libasan.so.4+0x37d2f)
   >     #1 0x561a5dd393a0 in my_thread_create /server/server/storage/perfschema/my_thread.h:38
   >     #2 0x561a5dd3ea35 in pfs_spawn_thread_v1 /server/server/storage/perfschema/pfs.cc:2252
   >     #3 0x561a5c9dd6f3 in inline_mysql_thread_create /server/server/include/mysql/psi/mysql_thread.h:1139
   >     #4 0x561a5c9f44a9 in create_thread_to_handle_connection(CONNECT*) /server/server/sql/mysqld.cc:5886
   >     #5 0x561a5c9f4b0a in create_new_thread(CONNECT*) /server/server/sql/mysqld.cc:5945
   >     #6 0x561a5c9f4e3d in handle_accepted_socket(st_mysql_socket, st_mysql_socket) /server/server/sql/mysqld.cc:6007
   >     #7 0x561a5c9f570d in handle_connections_sockets() /server/server/sql/mysqld.cc:6131
   >     #8 0x561a5c9f3cf1 in mysqld_main(int, char**) /server/server/sql/mysqld.cc:5781
   >     #9 0x561a5c9dc8f9 in main /server/server/sql/main.cc:25
   >     #10 0x7f5d39b42c86 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21c86)
   > ==1==ABORTING
