# Bug ID MDEV-29489-SERIALIZABLE

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-29489
Original isolation level: REPEATABLE READ
Tested isolation level:   SERIALIZABLE


## Details
 * Database: mariadb-debug-10.10.1
 * Number of scenarios: 1
 * Initial setup script: /home/theodor/Projects/MasterThesis/data/sql/MDEV-29489_mysql_bk.sql

## Results
### Scenario 0
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
     - TID: 1
     - Output: None
 * Instruction #2:
     - SQL:  START TRANSACTION;
     - TID: 1
     - Output: None
 * Instruction #3:
     - SQL:  START TRANSACTION;
     - TID: 0
     - Output: None
 * Instruction #4:
     - SQL:  update t_yfrkzd set wkey = 80;
     - TID: 1
     - Output: None
 * Instruction #5:
     - SQL:  delete from t_yfrkzd where t_yfrkzd.c_n1makd between t_yfrkzd.c_n1makd and t_yf...
     - TID: 1
     - Output: None
 * Instruction #6:
     - SQL:  delete from t_ywo4_b where t_ywo4_b.c_hlsgr not in ( select ref_0.pkey as c0 fr...
     - TID: 0
     - Output: ERROR: 2013 (HY000): Lost connection to MySQL server during query
 * Instruction #7:
     - SQL:  delete from t_yfrkzd where (t_yfrkzd.c_aob5e not in ( select ref_1.c_k4lijb as ...
     - TID: 1
     - Output: ERROR: 2013 (HY000): Lost connection to MySQL server during query
 * Instruction #8:
     - SQL:  ROLLBACK;
     - TID: 1
     - Output: Skipped due to previous error.
 * Instruction #9:
     - SQL:  ROLLBACK;
     - TID: 0
     - Output: Skipped due to previous error.

 * Container logs:
   > mysqld: /server/server/storage/innobase/lock/lock0lock.cc:6025: bool lock_trx_has_expl_x_lock(const trx_t&, const dict_table_t&, page_id_t, ulint): Assertion `lock_table_has(&trx, &table, LOCK_IX)' failed.
   > 240618 11:55:01 [ERROR] mysqld got signal 6 ;
   > This could be because you hit a bug. It is also possible that this binary
   > or one of the libraries it was linked against is corrupt, improperly built,
   > or misconfigured. This error can also be caused by malfunctioning hardware.
   > To report this bug, see https://mariadb.com/kb/en/reporting-bugs
   > We will try our best to scrape up some info that will hopefully help
   > diagnose the problem, but since we have already crashed, 
   > something is definitely wrong and this may fail.
   > Server version: 10.10.1-MariaDB-debug
   > key_buffer_size=134217728
   > read_buffer_size=131072
   > max_used_connections=2
   > max_threads=153
   > thread_count=2
   > It is possible that mysqld could use up to 
   > key_buffer_size + (read_buffer_size + sort_buffer_size)*max_threads = 468134 K  bytes of memory
   > Hope that's ok; if not, decrease some variables in the equation.
   > Thread pointer: 0x62b00011f288
   > Attempting backtrace. You can use the following information to find out
   > where mysqld died. If you see no messages after this, something went
   > terribly wrong...
   > stack_bottom = 0x7fad8cbfeab0 thread_stack 0x100000
   > /lib/x86_64-linux-gnu/libasan.so.6(+0x45c0e)[0x7fadab3aac0e]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x5635bfbadc8f]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x5635be73eb8d]
   > ??:0(__sigaction)[0x7fadaa743520]
   > ??:0(pthread_kill)[0x7fadaa7979fc]
   > ??:0(raise)[0x7fadaa743476]
   > ??:0(abort)[0x7fadaa7297f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7fadaa72971b]
   > ??:0(__assert_fail)[0x7fadaa73ae96]
   > lock/lock0lock.cc:6026(lock_trx_has_expl_x_lock(trx_t const&, dict_table_t const&, page_id_t, unsigned long))[0x5635bf30a9d1]
   > row/row0upd.cc:2662(row_upd_clust_step(upd_node_t*, que_thr_t*))[0x5635bf5d5e5b]
   > row/row0upd.cc:2791(row_upd(upd_node_t*, que_thr_t*))[0x5635bf5d6de0]
   > row/row0upd.cc:2933(row_upd_step(que_thr_t*))[0x5635bf5d7d47]
   > row/row0mysql.cc:1691(row_update_for_mysql(row_prebuilt_t*))[0x5635bf52fa6e]
   > /usr/local/mysql/bin/mysqld(+0x2f488db)[0x5635bf14e8db]
   > handler/ha_innodb.cc:8706(ha_innobase::delete_row(unsigned char const*))[0x5635be784a5e]
   > sql/handler.cc:7716(handler::ha_delete_row(unsigned char const*))[0x5635bdd5674c]
   > sql/sql_delete.cc:281(TABLE::delete_row())[0x5635bdd4b466]
   > sql/sql_delete.cc:842(mysql_delete(THD*, TABLE_LIST*, Item*, SQL_I_List<st_order>*, unsigned long long, unsigned long long, select_result*))[0x5635bde4b394]
   > sql/sql_parse.cc:4805(mysql_execute_command(THD*, bool))[0x5635bde61a28]
   > sql/sql_parse.cc:8035(mysql_parse(THD*, char*, unsigned int, Parser_state*))[0x5635bde374af]
   > sql/sql_parse.cc:1896(dispatch_command(enum_server_command, THD*, char*, unsigned int, bool))[0x5635bde341c2]
   > sql/sql_parse.cc:1407(do_command(THD*, bool))[0x5635be2f790e]
   > sql/sql_connect.cc:1418(do_handle_one_connection(CONNECT*, bool))[0x5635be2f71b8]
   > sql/sql_connect.cc:1314(handle_one_connection)[0x5635bef4451a]
   > ??:0(pthread_condattr_setpshared)[0x7fadaa795ac3]
   > ??:0(__xmknodat)[0x7fadaa827850]
   > Trying to get some variables.
   > Some pointers may be invalid and cause the dump to abort.
   > Query (0x6290000872a8): delete from t_ywo4_b where t_ywo4_b.c_hlsgr not in ( select ref_0.pkey as c0 from (t_yfrkzd as ref_0 inner join (select ref_1.wkey as c0 from t_yfrkzd as ref_1 ) as subq_0 on (ref_0.wkey = subq_0.c0 )))
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
   > Max core file size        0                    unlimited            bytes     
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
   > Max realtime timeout      unlimited            unlimited            us        
   > Core pattern: |/usr/lib/systemd/systemd-coredump %P %u %g %s %t %c %h
   > Kernel version: Linux version 6.8.11-300.fc40.x86_64 (mockbuild@f09cc32e12c24ed6a1a66c2a2e9f1728) (gcc (GCC) 14.1.1 20240522 (Red Hat 14.1.1-4), GNU ld version 2.41-37.fc40) #1 SMP PREEMPT_DYNAMIC Mon May 27 14:53:33 UTC 2024
   > Fatal signal 11 while backtracing
