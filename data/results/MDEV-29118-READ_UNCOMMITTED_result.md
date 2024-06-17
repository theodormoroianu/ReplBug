# Bug ID MDEV-29118-READ_UNCOMMITTED

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-29118
Original isolation level: REPEATABLE READ
Tested isolation level:   READ UNCOMMITTED


## Details
 * Database: mariadb-debug-10.8.3
 * Number of scenarios: 1
 * Initial setup script: /home/theodor/Projects/MasterThesis/data/sql/MDEV-29118_mysql_bk.sql

## Results
### Scenario 0
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
     - TID: 1
     - Output: None
 * Instruction #2:
     - SQL:  START TRANSACTION;
     - TID: 0
     - Output: None
 * Instruction #3:
     - SQL:  delete from t_davsbd;
     - TID: 0
     - Output: None
 * Instruction #4:
     - SQL:  START TRANSACTION;
     - TID: 1
     - Output: None
 * Instruction #5:
     - SQL:  insert into t_iqij_c (wkey, pkey, c_svp9sc, c_anyvkb) values (115, 222000, ASCI...
     - TID: 1
     - Output: Error: 2013 (HY000): Lost connection to MySQL server during query
 * Instruction #6:
     - SQL:  update t_j4mbqd set wkey = 190;
     - TID: 0
     - Output: Error: 2013 (HY000): Lost connection to MySQL server during query
 * Instruction #7:
     - SQL:  ROLLBACK;
     - TID: 0
     - Output: Error: MySQL Connection not available.
 * Instruction #8:
     - SQL:  ROLLBACK;
     - TID: 1
     - Output: Error: MySQL Connection not available.

 * Container logs:
   > mysqld: /server/server/storage/innobase/lock/lock0lock.cc:4972: dberr_t lock_rec_insert_check_and_lock(const rec_t*, buf_block_t*, dict_index_t*, que_thr_t*, mtr_t*, bool*): Assertion `lock_table_has(trx, index->table, LOCK_IX)' failed.
   > 240606 13:58:39 [ERROR] mysqld got signal 6 ;
   > This could be because you hit a bug. It is also possible that this binary
   > or one of the libraries it was linked against is corrupt, improperly built,
   > or misconfigured. This error can also be caused by malfunctioning hardware.
   > To report this bug, see https://mariadb.com/kb/en/reporting-bugs
   > We will try our best to scrape up some info that will hopefully help
   > diagnose the problem, but since we have already crashed, 
   > something is definitely wrong and this may fail.
   > Server version: 10.8.3-MariaDB-debug
   > key_buffer_size=134217728
   > read_buffer_size=131072
   > max_used_connections=2
   > max_threads=153
   > thread_count=3
   > It is possible that mysqld could use up to 
   > key_buffer_size + (read_buffer_size + sort_buffer_size)*max_threads = 468121 K  bytes of memory
   > Hope that's ok; if not, decrease some variables in the equation.
   > Thread pointer: 0x7f6b3c000dc8
   > Attempting backtrace. You can use the following information to find out
   > where mysqld died. If you see no messages after this, something went
   > terribly wrong...
   > stack_bottom = 0x7f6bb01fec78 thread_stack 0x49000
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x558744dbd08f]
   > sql/signal_handler.cc:226(handle_fatal_signal)[0x5587444b765d]
   > ??:0(__sigaction)[0x7f6bb23a1520]
   > ??:0(pthread_kill)[0x7f6bb23f59fc]
   > ??:0(raise)[0x7f6bb23a1476]
   > ??:0(abort)[0x7f6bb23877f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7f6bb238771b]
   > ??:0(__assert_fail)[0x7f6bb2398e96]
   > lock/lock0lock.cc:4974(lock_rec_insert_check_and_lock(unsigned char const*, buf_block_t*, dict_index_t*, que_thr_t*, mtr_t*, bool*))[0x55874499972a]
   > btr/btr0cur.cc:3268(btr_cur_ins_lock_and_undo(unsigned long, btr_cur_t*, dtuple_t*, que_thr_t*, mtr_t*, bool*))[0x558744baff9f]
   > btr/btr0cur.cc:3513(btr_cur_optimistic_insert(unsigned long, btr_cur_t*, unsigned short**, mem_block_info_t**, dtuple_t*, unsigned char**, big_rec_t**, unsigned long, que_thr_t*, mtr_t*))[0x558744bb0e67]
   > row/row0ins.cc:2754(row_ins_clust_index_entry_low(unsigned long, unsigned long, dict_index_t*, unsigned long, dtuple_t*, unsigned long, que_thr_t*))[0x558744a87004]
   > row/row0ins.cc:3156(row_ins_clust_index_entry(dict_index_t*, dtuple_t*, que_thr_t*, unsigned long))[0x558744a88694]
   > row/row0ins.cc:3293(row_ins_index_entry(dict_index_t*, dtuple_t*, que_thr_t*))[0x558744a88cf3]
   > row/row0ins.cc:3461(row_ins_index_entry_step(ins_node_t*, que_thr_t*))[0x558744a89649]
   > row/row0ins.cc:3608(row_ins(ins_node_t*, que_thr_t*))[0x558744a89bc2]
   > row/row0ins.cc:3754(row_ins_step(que_thr_t*))[0x558744a8a5a2]
   > row/row0mysql.cc:1320(row_insert_for_mysql(unsigned char const*, row_prebuilt_t*, ins_mode_t))[0x558744aaf6b2]
   > handler/ha_innodb.cc:7842(ha_innobase::write_row(unsigned char const*))[0x5587448d25b3]
   > sql/handler.cc:7549(handler::ha_write_row(unsigned char const*))[0x5587444d1d63]
   > sql/sql_insert.cc:2161(write_record(THD*, TABLE*, st_copy_info*, select_result*))[0x5587440913e2]
   > sql/sql_insert.cc:1132(mysql_insert(THD*, TABLE_LIST*, List<Item>&, List<List<Item> >&, List<Item>&, List<Item>&, enum_duplicates, bool, select_result*))[0x55874408df05]
   > sql/sql_parse.cc:4562(mysql_execute_command(THD*, bool))[0x5587440e4b67]
   > sql/sql_parse.cc:8027(mysql_parse(THD*, char*, unsigned int, Parser_state*))[0x5587440f086e]
   > sql/sql_parse.cc:1896(dispatch_command(enum_server_command, THD*, char*, unsigned int, bool))[0x5587440dc75d]
   > sql/sql_parse.cc:1407(do_command(THD*, bool))[0x5587440db0cf]
   > sql/sql_connect.cc:1418(do_handle_one_connection(CONNECT*, bool))[0x5587442bd7d3]
   > sql/sql_connect.cc:1314(handle_one_connection)[0x5587442bd460]
   > perfschema/pfs.cc:2203(pfs_spawn_thread)[0x5587447eae81]
   > ??:0(pthread_condattr_setpshared)[0x7f6bb23f3ac3]
   > ??:0(__xmknodat)[0x7f6bb2485850]
   > Trying to get some variables.
   > Some pointers may be invalid and cause the dump to abort.
   > Query (0x7f6b3c013cd0): insert into t_iqij_c (wkey, pkey, c_svp9sc, c_anyvkb) values (115, 222000, ASCII('w_3pab'), null), (115, 223000, CHAR_LENGTH( case when ((select wkey from t_j4mbqd order by wkey limit 1 offset 34) in (select ref_0.pkey as c0 from t_davsbd as ref_0)) then 'k0hpvb' else 'sss' end), null)
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
   > Max core file size        unlimited            unlimited            bytes     
   > Max resident set          unlimited            unlimited            bytes     
   > Max processes             61166                61166                processes 
   > Max open files            524288               524288               files     
   > Max locked memory         8388608              8388608              bytes     
   > Max address space         unlimited            unlimited            bytes     
   > Max file locks            unlimited            unlimited            locks     
   > Max pending signals       61166                61166                signals   
   > Max msgqueue size         819200               819200               bytes     
   > Max nice priority         0                    0                    
   > Max realtime priority     0                    0                    
   > Max realtime timeout      200000               200000               us        
   > Core pattern: |/usr/lib/systemd/systemd-coredump %P %u %g %s %t %c %h
   > Fatal signal 11 while backtracing
