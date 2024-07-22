# Bug ID MDEV-28944-REPEATABLE_READ

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-28944
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              The server crashes during an XA transaction rollback after a table is altered.


## Details
 * Database: mariadb-cb1f08bd-debug
 * Number of scenarios: 1
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 0 / 0
 * Instruction #1:
     - Instruction:  CREATE TABLE t (a INT) ENGINE=MyISAM;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  INSERT INTO t VALUES (1);
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 1 / 0
 * Instruction #3:
     - Instruction:  XA START 'xid';
     - Transaction: conn_1
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 0 / 0
 * Instruction #4:
     - Instruction:  SELECT * FROM t;
     - Transaction: conn_1
     - Output: [(1,)]
     - Executed order: 4
     - Affected rows / Warnings: 1 / 0
 * Instruction #5:
     - Instruction:  ALTER TABLE t NOWAIT ADD KEY (a);
     - Transaction: conn_0
     - Output: ERROR: 1205 (HY000): Lock wait timeout exceeded; try restarting transaction
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #6:
     - Instruction:  UPDATE t SET a = 2;
     - Transaction: conn_1
     - Output: None
     - Executed order: 5
     - Affected rows / Warnings: 1 / 0
 * Instruction #7:
     - Instruction:  XA END 'xid';
     - Transaction: conn_1
     - Output: None
     - Executed order: 6
     - Affected rows / Warnings: 0 / 0
 * Instruction #8:
     - Instruction:  XA ROLLBACK 'xid';
     - Transaction: conn_1
     - Output: ERROR: 2013 (HY000): Lost connection to MySQL server during query
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #9:
     - Instruction:  DROP TABLE t;
     - Transaction: conn_0
     - Output: ERROR: 2013 (HY000): Lost connection to MySQL server during query
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0

 * Container logs:
   > mysqld: /server/server/sql/log.cc:2383: int binlog_rollback(handlerton*, THD*, bool): Assertion `thd->lex->sql_command != SQLCOM_XA_ROLLBACK' failed.
   > 240722 15:26:12 [ERROR] mysqld got signal 6 ;
   > This could be because you hit a bug. It is also possible that this binary
   > or one of the libraries it was linked against is corrupt, improperly built,
   > or misconfigured. This error can also be caused by malfunctioning hardware.
   > To report this bug, see https://mariadb.com/kb/en/reporting-bugs
   > We will try our best to scrape up some info that will hopefully help
   > diagnose the problem, but since we have already crashed, 
   > something is definitely wrong and this may fail.
   > Server version: 10.10.0-MariaDB-debug
   > key_buffer_size=134217728
   > read_buffer_size=131072
   > max_used_connections=2
   > max_threads=153
   > thread_count=2
   > It is possible that mysqld could use up to 
   > key_buffer_size + (read_buffer_size + sort_buffer_size)*max_threads = 468133 K  bytes of memory
   > Hope that's ok; if not, decrease some variables in the equation.
   > Thread pointer: 0x62b00012d288
   > Attempting backtrace. You can use the following information to find out
   > where mysqld died. If you see no messages after this, something went
   > terribly wrong...
   > stack_bottom = 0x7fd4bd1fecd0 thread_stack 0x100000
   > ??:0(__interceptor_sched_getaffinity)[0x7fd4df3308c0]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x55c001cf1a96]
   > sql/signal_handler.cc:226(handle_fatal_signal)[0x55c000942416]
   > ??:0(__restore_rt)[0x7fd4ddc0e980]
   > linux/raise.c:51(__GI_raise)[0x7fd4dcd06e87]
   > stdlib/abort.c:81(__GI_abort)[0x7fd4dcd087f1]
   > assert/assert.c:89(__assert_fail_base)[0x7fd4dccf83fa]
   > ??:0(__assert_fail)[0x7fd4dccf8472]
   > sql/log.cc:2385(binlog_rollback(handlerton*, THD*, bool))[0x55c000c88804]
   > sql/handler.cc:2180(ha_rollback_trans(THD*, bool))[0x55c00095390e]
   > sql/xa.cc:393(xa_trans_force_rollback(THD*))[0x55c0007b1fac]
   > sql/xa.cc:821(trans_xa_rollback(THD*))[0x55c0007b5a14]
   > sql/sql_parse.cc:5879(mysql_execute_command(THD*, bool))[0x55c00009ac4f]
   > sql/sql_parse.cc:8036(mysql_parse(THD*, char*, unsigned int, Parser_state*))[0x55c0000a8da8]
   > sql/sql_parse.cc:1896(dispatch_command(enum_server_command, THD*, char*, unsigned int, bool))[0x55c00007efe6]
   > sql/sql_parse.cc:1407(do_command(THD*, bool))[0x55c00007bcd2]
   > sql/sql_connect.cc:1418(do_handle_one_connection(CONNECT*, bool))[0x55c00052636e]
   > sql/sql_connect.cc:1314(handle_one_connection)[0x55c000525bef]
   > perfschema/pfs.cc:2203(pfs_spawn_thread)[0x55c001115240]
   > nptl/pthread_create.c:463(start_thread)[0x7fd4ddc036db]
   > x86_64/clone.S:97(clone)[0x7fd4dcde961f]
   > Trying to get some variables.
   > Some pointers may be invalid and cause the dump to abort.
   > Query (0x6290000b92a8): XA ROLLBACK 'xid'
   > Connection ID (thread ID): 6
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
   > ==1==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x7fd4dcd088e0 bp 0x7fd4dce7f6c0 sp 0x7fd4bd1fc340 T12)
   > ==1==The signal is caused by a READ memory access.
   > ==1==Hint: address points to the zero page.
   >     #0 0x7fd4dcd088df in abort (/lib/x86_64-linux-gnu/libc.so.6+0x408df)
   >     #1 0x7fd4dccf83f9  (/lib/x86_64-linux-gnu/libc.so.6+0x303f9)
   >     #2 0x7fd4dccf8471 in __assert_fail (/lib/x86_64-linux-gnu/libc.so.6+0x30471)
   >     #3 0x55c000c88803 in binlog_rollback /server/server/sql/log.cc:2383
   >     #4 0x55c00095390d in ha_rollback_trans(THD*, bool) /server/server/sql/handler.cc:2180
   >     #5 0x55c0007b1fab in xa_trans_force_rollback(THD*) /server/server/sql/xa.cc:393
   >     #6 0x55c0007b5a13 in trans_xa_rollback(THD*) /server/server/sql/xa.cc:821
   >     #7 0x55c00009ac4e in mysql_execute_command(THD*, bool) /server/server/sql/sql_parse.cc:5879
   >     #8 0x55c0000a8da7 in mysql_parse(THD*, char*, unsigned int, Parser_state*) /server/server/sql/sql_parse.cc:8036
   >     #9 0x55c00007efe5 in dispatch_command(enum_server_command, THD*, char*, unsigned int, bool) /server/server/sql/sql_parse.cc:1894
   >     #10 0x55c00007bcd1 in do_command(THD*, bool) /server/server/sql/sql_parse.cc:1407
   >     #11 0x55c00052636d in do_handle_one_connection(CONNECT*, bool) /server/server/sql/sql_connect.cc:1418
   >     #12 0x55c000525bee in handle_one_connection /server/server/sql/sql_connect.cc:1312
   >     #13 0x55c00111523f in pfs_spawn_thread /server/server/storage/perfschema/pfs.cc:2201
   >     #14 0x7fd4ddc036da in start_thread (/lib/x86_64-linux-gnu/libpthread.so.0+0x76da)
   >     #15 0x7fd4dcde961e in __clone (/lib/x86_64-linux-gnu/libc.so.6+0x12161e)
   > AddressSanitizer can not provide additional info.
   > SUMMARY: AddressSanitizer: SEGV (/lib/x86_64-linux-gnu/libc.so.6+0x408df) in abort
   > Thread T12 created by T0 here:
   >     #0 0x7fd4df312d2f in __interceptor_pthread_create (/usr/lib/x86_64-linux-gnu/libasan.so.4+0x37d2f)
   >     #1 0x55c001110bba in my_thread_create /server/server/storage/perfschema/my_thread.h:52
   >     #2 0x55c00111562e in pfs_spawn_thread_v1 /server/server/storage/perfschema/pfs.cc:2252
   >     #3 0x55bfffccdd63 in inline_mysql_thread_create /server/server/include/mysql/psi/mysql_thread.h:1139
   >     #4 0x55bfffce569f in create_thread_to_handle_connection(CONNECT*) /server/server/sql/mysqld.cc:6015
   >     #5 0x55bfffce5cfd in create_new_thread(CONNECT*) /server/server/sql/mysqld.cc:6074
   >     #6 0x55bfffce6030 in handle_accepted_socket(st_mysql_socket, st_mysql_socket) /server/server/sql/mysqld.cc:6136
   >     #7 0x55bfffce691e in handle_connections_sockets() /server/server/sql/mysqld.cc:6260
   >     #8 0x55bfffce4ee7 in mysqld_main(int, char**) /server/server/sql/mysqld.cc:5910
   >     #9 0x55bfffcccf69 in main /server/server/sql/main.cc:34
   >     #10 0x7fd4dcce9c86 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21c86)
   > ==1==ABORTING
