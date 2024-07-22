# Bug ID MDEV-25457-SERIALIZABLE

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-25457
Original isolation level: REPEATABLE READ
Tested isolation level:   SERIALIZABLE
Description:              An update makes the DB server crash.


## Details
 * Database: mariadb-10.2.37-debug
 * Number of scenarios: 2
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 0 / 0
 * Instruction #1:
     - Instruction:  CREATE TEMPORARY TABLE t (a INT) ENGINE=InnoDB;
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
     - Instruction:  START TRANSACTION READ ONLY;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 0 / 0
 * Instruction #4:
     - Instruction:  UPDATE t SET a = NULL;
     - Transaction: conn_0
     - Output: ERROR: 2013 (HY000): Lost connection to MySQL server during query
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #5:
     - Instruction:  ROLLBACK;
     - Transaction: conn_0
     - Output: ERROR: MySQL Connection not available.
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0

 * Container logs:
   > mysqld: /server/server/storage/innobase/btr/btr0cur.cc:4021: dberr_t btr_cur_optimistic_update(ulint, btr_cur_t*, rec_offs**, mem_heap_t**, const upd_t*, ulint, que_thr_t*, trx_id_t, mtr_t*): Assertion `trx_id > 0 || (flags & BTR_KEEP_SYS_FLAG)' failed.
   > 240722 13:57:10 [ERROR] mysqld got signal 6 ;
   > This could be because you hit a bug. It is also possible that this binary
   > or one of the libraries it was linked against is corrupt, improperly built,
   > or misconfigured. This error can also be caused by malfunctioning hardware.
   > To report this bug, see https://mariadb.com/kb/en/reporting-bugs
   > We will try our best to scrape up some info that will hopefully help
   > diagnose the problem, but since we have already crashed, 
   > something is definitely wrong and this may fail.
   > Server version: 10.2.37-MariaDB-debug
   > key_buffer_size=134217728
   > read_buffer_size=131072
   > max_used_connections=1
   > max_threads=153
   > thread_count=6
   > It is possible that mysqld could use up to 
   > key_buffer_size + (read_buffer_size + sort_buffer_size)*max_threads = 467328 K  bytes of memory
   > Hope that's ok; if not, decrease some variables in the equation.
   > Thread pointer: 0x62a000048270
   > Attempting backtrace. You can use the following information to find out
   > where mysqld died. If you see no messages after this, something went
   > terribly wrong...
   > stack_bottom = 0x7f8a999fecc0 thread_stack 0x5b000
   > /usr/lib/x86_64-linux-gnu/libasan.so.2(+0x4a077)[0x7f8ab3e5b077]
   > maria/ma_pagecache.c:4406(flush_cached_blocks)[0x1e3c4db]
   > sql/sql_table.cc:275(explain_filename(THD*, char const*, char*, unsigned int, enum_explain_filename_mode))[0xe1693b]
   > /lib/x86_64-linux-gnu/libpthread.so.0(+0x11390)[0x7f8ab28ed390]
   > linux/raise.c:54(__GI_raise)[0x7f8ab1ca6438]
   > stdlib/abort.c:91(__GI_abort)[0x7f8ab1ca803a]
   > assert/assert.c:92(__assert_fail_base)[0x7f8ab1c9ebe7]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2dc92)[0x7f8ab1c9ec92]
   > sql/multi_range_read.h:411(Mrr_reader_factory::Mrr_reader_factory())[0x173c9f9]
   > sql/sql_partition.cc:1596(fix_partition_func(THD*, TABLE*, bool))[0x1608b72]
   > sql/sql_partition.cc:1871(add_partition_options(String*, partition_element*))[0x160a453]
   > sql/sql_partition.cc:2005(add_column_list_values(String*, partition_info*, p_elem_val*, HA_CREATE_INFO*, Alter_info*))[0x160ad3b]
   > sql/sql_partition.cc:2124(add_partition_values(String*, partition_info*, partition_element*, HA_CREATE_INFO*, Alter_info*))[0x160ba9e]
   > sql/opt_range.cc:9102(key_and(RANGE_OPT_PARAM*, SEL_ARG*, SEL_ARG*, unsigned int))[0x15666aa]
   > sql/item.h:5922(Item_cache_str_for_nullif::Item_cache_str_for_nullif(Item_cache_str_for_nullif const&))[0x1302452]
   > sql/sql_table.cc:6898(fill_alter_inplace_info(THD*, TABLE*, bool, Alter_inplace_info*))[0xe3f283]
   > sql/slave.cc:6298(queue_event(Master_info*, char const*, unsigned long))[0xa8abd0]
   > /usr/local/mysql/bin/mysqld(_Z21mysql_execute_commandP3THD+0x5f66)[0x83c893]
   > /usr/local/mysql/bin/mysqld(_Z11mysql_parseP3THDPcjP12Parser_statebb+0x6a2)[0x85439c]
   > /usr/local/mysql/bin/mysqld(_Z16dispatch_command19enum_server_commandP3THDPcjbb+0x1eb8)[0x8307c7]
   > /usr/local/mysql/bin/mysqld(_Z10do_commandP3THD+0x1108)[0x82d978]
   > sql/sql_cache.cc:3911(Query_cache::move_to_query_list_end(Query_cache_block*))[0xb6be34]
   > sql/sql_cache.cc:3872(Query_cache::insert_into_free_memory_list(Query_cache_block*))[0xb6b818]
   > /lib/x86_64-linux-gnu/libpthread.so.0(+0x76ba)[0x7f8ab28e36ba]
   > x86_64/clone.S:111(clone)[0x7f8ab1d7851d]
   > Trying to get some variables.
   > Some pointers may be invalid and cause the dump to abort.
   > Query (0x62b000000290): UPDATE t SET a = NULL
   > Connection ID (thread ID): 13
   > Status: NOT_KILLED
   > Optimizer switch: index_merge=on,index_merge_union=on,index_merge_sort_union=on,index_merge_intersection=on,index_merge_sort_intersection=off,engine_condition_pushdown=off,index_condition_pushdown=on,derived_merge=on,derived_with_keys=on,firstmatch=on,loosescan=on,materialization=on,in_to_exists=on,semijoin=on,partial_match_rowid_merge=on,partial_match_table_scan=on,subquery_cache=on,mrr=off,mrr_cost_based=off,mrr_sort_keys=off,outer_join_with_cache=on,semijoin_with_cache=on,join_cache_incremental=on,join_cache_hashed=on,join_cache_bka=on,optimize_join_buffer_size=off,table_elimination=on,extended_keys=on,exists_to_in=on,orderby_uses_equalities=on,condition_pushdown_for_derived=on
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
   > ASAN:SIGSEGV
   > =================================================================
   > ==1==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x7f8ab1ca81a6 bp 0x000002511780 sp 0x7f8a999fa870 T31)
   >     #0 0x7f8ab1ca81a5 in abort (/lib/x86_64-linux-gnu/libc.so.6+0x371a5)
   >     #1 0x7f8ab1c9ebe6  (/lib/x86_64-linux-gnu/libc.so.6+0x2dbe6)
   >     #2 0x7f8ab1c9ec91 in __assert_fail (/lib/x86_64-linux-gnu/libc.so.6+0x2dc91)
   >     #3 0x173c9f8 in btr_cur_optimistic_update(unsigned long, btr_cur_t*, unsigned short**, mem_block_info_t**, upd_t const*, unsigned long, que_thr_t*, unsigned long, mtr_t*) /server/server/storage/innobase/btr/btr0cur.cc:4021
   >     #4 0x1608b71 in row_upd_clust_rec /server/server/storage/innobase/row/row0upd.cc:2891
   >     #5 0x160a452 in row_upd_clust_step /server/server/storage/innobase/row/row0upd.cc:3215
   >     #6 0x160ad3a in row_upd /server/server/storage/innobase/row/row0upd.cc:3315
   >     #7 0x160ba9d in row_upd_step(que_thr_t*) /server/server/storage/innobase/row/row0upd.cc:3461
   >     #8 0x15666a9 in row_update_for_mysql(row_prebuilt_t*) /server/server/storage/innobase/row/row0mysql.cc:1825
   >     #9 0x1302451 in ha_innobase::update_row(unsigned char const*, unsigned char*) /server/server/storage/innobase/handler/ha_innodb.cc:8945
   >     #10 0xe3f282 in handler::ha_update_row(unsigned char const*, unsigned char*) /server/server/sql/handler.cc:6150
   >     #11 0xa8abcf in mysql_update(THD*, TABLE_LIST*, List<Item>&, List<Item>&, Item*, unsigned int, st_order*, unsigned long long, enum_duplicates, bool, unsigned long long*, unsigned long long*) /server/server/sql/sql_update.cc:819
   >     #12 0x83c892 in mysql_execute_command(THD*) /server/server/sql/sql_parse.cc:4041
   >     #13 0x85439b in mysql_parse(THD*, char*, unsigned int, Parser_state*, bool, bool) /server/server/sql/sql_parse.cc:7763
   >     #14 0x8307c6 in dispatch_command(enum_server_command, THD*, char*, unsigned int, bool, bool) /server/server/sql/sql_parse.cc:1828
   >     #15 0x82d977 in do_command(THD*) /server/server/sql/sql_parse.cc:1382
   >     #16 0xb6be33 in do_handle_one_connection(CONNECT*) /server/server/sql/sql_connect.cc:1336
   >     #17 0xb6b817 in handle_one_connection /server/server/sql/sql_connect.cc:1241
   >     #18 0x7f8ab28e36b9 in start_thread (/lib/x86_64-linux-gnu/libpthread.so.0+0x76b9)
   >     #19 0x7f8ab1d7851c in clone (/lib/x86_64-linux-gnu/libc.so.6+0x10751c)
   > AddressSanitizer can not provide additional info.
   > SUMMARY: AddressSanitizer: SEGV ??:0 abort
   > Thread T31 created by T0 here:
   >     #0 0x7f8ab3e47253 in pthread_create (/usr/lib/x86_64-linux-gnu/libasan.so.2+0x36253)
   >     #1 0x1e85ebf in spawn_thread_noop /server/server/mysys/psi_noop.c:187
   >     #2 0x605676 in inline_mysql_thread_create /server/server/include/mysql/psi/mysql_thread.h:1246
   >     #3 0x61a742 in create_thread_to_handle_connection(CONNECT*) /server/server/sql/mysqld.cc:6573
   >     #4 0x61ae66 in create_new_thread /server/server/sql/mysqld.cc:6643
   >     #5 0x61bdc8 in handle_connections_sockets() /server/server/sql/mysqld.cc:6901
   >     #6 0x619c01 in mysqld_main(int, char**) /server/server/sql/mysqld.cc:6192
   >     #7 0x6039b5 in main /server/server/sql/main.cc:25
   >     #8 0x7f8ab1c9183f in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x2083f)
   > ==1==ABORTING

### Scenario 1
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 0 / 0
 * Instruction #1:
     - Instruction:  CREATE TEMPORARY TABLE t (a INT) ENGINE=InnoDB;
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
     - Instruction:  UPDATE t SET a = NULL;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 1 / 0

 * Container logs:
   No logs available.
