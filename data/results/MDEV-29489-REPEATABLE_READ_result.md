# Bug ID MDEV-29489-REPEATABLE_READ

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-29489
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              MariaDB crashes.


## Details
 * Database: mariadb-10.10.1
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
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_1
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_1
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 0 / 0
 * Instruction #3:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 0 / 0
 * Instruction #4:
     - Instruction:  update t_yfrkzd set wkey = 80;
     - Transaction: conn_1
     - Output: None
     - Executed order: 4
     - Affected rows / Warnings: 31 / 0
 * Instruction #5:
     - Instruction:  delete from t_yfrkzd where t_yfrkzd.c_n1makd between t_yfrkzd.c_n1makd and t_yf...
     - Transaction: conn_1
     - Output: None
     - Executed order: 5
     - Affected rows / Warnings: 15 / 0
 * Instruction #6:
     - Instruction:  delete from t_ywo4_b where t_ywo4_b.c_hlsgr not in ( select ref_0.pkey as c0 fr...
     - Transaction: conn_0
     - Output: ERROR: 2013 (HY000): Lost connection to MySQL server during query
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #7:
     - Instruction:  delete from t_yfrkzd where (t_yfrkzd.c_aob5e not in ( select ref_1.c_k4lijb as ...
     - Transaction: conn_1
     - Output: ERROR: 2013 (HY000): Lost connection to MySQL server during query
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #8:
     - Instruction:  ROLLBACK;
     - Transaction: conn_1
     - Output: ERROR: MySQL Connection not available.
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #9:
     - Instruction:  ROLLBACK;
     - Transaction: conn_0
     - Output: ERROR: MySQL Connection not available.
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0

 * Container logs:
   > mysqld: /server/server/storage/innobase/lock/lock0lock.cc:6025: bool lock_trx_has_expl_x_lock(const trx_t&, const dict_table_t&, page_id_t, ulint): Assertion `lock_table_has(&trx, &table, LOCK_IX)' failed.
   > 240716 17:37:16 [ERROR] mysqld got signal 6 ;
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
   > Thread pointer: 0x7f30fc000dc8
   > Attempting backtrace. You can use the following information to find out
   > where mysqld died. If you see no messages after this, something went
   > terribly wrong...
   > stack_bottom = 0x7f315c0b9b78 thread_stack 0x49000
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x55805ef303ce]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x55805e6303f7]
   > ??:0(__sigaction)[0x7f315c89b520]
   > ??:0(pthread_kill)[0x7f315c8ef9fc]
   > ??:0(raise)[0x7f315c89b476]
   > ??:0(abort)[0x7f315c8817f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7f315c88171b]
   > ??:0(__assert_fail)[0x7f315c892e96]
   > lock/lock0lock.cc:6026(lock_trx_has_expl_x_lock(trx_t const&, dict_table_t const&, page_id_t, unsigned long))[0x55805eb1a32a]
   > row/row0upd.cc:2662(row_upd_clust_step(upd_node_t*, que_thr_t*))[0x55805ec87a72]
   > row/row0upd.cc:2791(row_upd(upd_node_t*, que_thr_t*))[0x55805ec881f2]
   > row/row0upd.cc:2933(row_upd_step(que_thr_t*))[0x55805ec887e0]
   > row/row0mysql.cc:1691(row_update_for_mysql(row_prebuilt_t*))[0x55805ec31454]
   > handler/ha_innodb.cc:8706(ha_innobase::delete_row(unsigned char const*))[0x55805ea51632]
   > sql/handler.cc:7716(handler::ha_delete_row(unsigned char const*))[0x55805e64baf9]
   > sql/sql_delete.cc:281(TABLE::delete_row())[0x55805e1e9261]
   > sql/sql_delete.cc:842(mysql_delete(THD*, TABLE_LIST*, Item*, SQL_I_List<st_order>*, unsigned long long, unsigned long long, select_result*))[0x55805e1e516d]
   > sql/sql_parse.cc:4805(mysql_execute_command(THD*, bool))[0x55805e2513e7]
   > sql/sql_parse.cc:8035(mysql_parse(THD*, char*, unsigned int, Parser_state*))[0x55805e25c134]
   > sql/sql_parse.cc:1896(dispatch_command(enum_server_command, THD*, char*, unsigned int, bool))[0x55805e247f6e]
   > sql/sql_parse.cc:1407(do_command(THD*, bool))[0x55805e2468e0]
   > sql/sql_connect.cc:1418(do_handle_one_connection(CONNECT*, bool))[0x55805e42ebbb]
   > sql/sql_connect.cc:1314(handle_one_connection)[0x55805e42e848]
   > perfschema/pfs.cc:2203(pfs_spawn_thread)[0x55805e965ad1]
   > ??:0(pthread_condattr_setpshared)[0x7f315c8edac3]
   > ??:0(__xmknodat)[0x7f315c97f850]
   > Trying to get some variables.
   > Some pointers may be invalid and cause the dump to abort.
   > Query (0x7f30fc014ec0): delete from t_ywo4_b where t_ywo4_b.c_hlsgr not in ( select ref_0.pkey as c0 from (t_yfrkzd as ref_0 inner join (select ref_1.wkey as c0 from t_yfrkzd as ref_1 ) as subq_0 on (ref_0.wkey = subq_0.c0 )))
   > Connection ID (thread ID): 17
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
   > Kernel version: Linux version 6.9.7-200.fc40.x86_64 (mockbuild@8d858239ee7c403c892e8a84096b3ce3) (gcc (GCC) 14.1.1 20240620 (Red Hat 14.1.1-6), GNU ld version 2.41-37.fc40) #1 SMP PREEMPT_DYNAMIC Thu Jun 27 18:11:45 UTC 2024
   > Fatal signal 11 while backtracing
