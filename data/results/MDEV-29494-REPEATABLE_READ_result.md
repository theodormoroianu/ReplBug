# Bug ID MDEV-29494-REPEATABLE_READ

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-29494
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              The server should crash.


## Details
 * Database: mariadb-10.10.1
 * Number of scenarios: 10
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
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  select subq_0.c0 as c0 from (select ref_0.c_s7edob as c0 from t_dmvax as ref_0 ...
     - Transaction: conn_0
     - Output: ERROR: 2013 (HY000): Lost connection to MySQL server during query
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #3:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: ERROR: MySQL Connection not available.
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0

 * Container logs:
   > mysqld: /server/server/sql/item.cc:10699: virtual longlong Item_type_holder::val_int(): Assertion `0' failed.
   > 240716 17:37:43 [ERROR] mysqld got signal 6 ;
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
   > max_used_connections=1
   > max_threads=153
   > thread_count=1
   > It is possible that mysqld could use up to 
   > key_buffer_size + (read_buffer_size + sort_buffer_size)*max_threads = 468134 K  bytes of memory
   > Hope that's ok; if not, decrease some variables in the equation.
   > Thread pointer: 0x7f12b4000dc8
   > Attempting backtrace. You can use the following information to find out
   > where mysqld died. If you see no messages after this, something went
   > terribly wrong...
   > stack_bottom = 0x7f13201cdb78 thread_stack 0x49000
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x5565a1e1a3ce]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x5565a151a3f7]
   > ??:0(__sigaction)[0x7f1322144520]
   > ??:0(pthread_kill)[0x7f13221989fc]
   > ??:0(raise)[0x7f1322144476]
   > ??:0(abort)[0x7f132212a7f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7f132212a71b]
   > ??:0(__assert_fail)[0x7f132213be96]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x5565a1561bf3]
   > /usr/local/mysql/bin/mysqld(+0x861cbf)[0x5565a0fa4cbf]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x51)[0x5565a155f553]
   > /usr/local/mysql/bin/mysqld(+0xcca9e2)[0x5565a140d9e2]
   > /usr/local/mysql/bin/mysqld(+0xccaaaa)[0x5565a140daaa]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x69)[0x5565a1647149]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0x576)[0x5565a1637486]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x18e)[0x5565a16399c4]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0xd8)[0x5565a139c292]
   > /usr/local/mysql/bin/mysqld(+0xa6e44d)[0x5565a11b144d]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x20a4)[0x5565a11a43f0]
   > sql/item.h:1779(Item::val_int_result())[0x5565a11a1c09]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x5565a11002d9]
   > sql/item.h:7099(Item_cache::has_value())[0x5565a139a0c4]
   > sql/item.h:7108(Item_cache::is_null())[0x5565a11a6774]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x5565a11a44f3]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x5565a11a1c09]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x5565a11adab2]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x5565a119c6a3]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x5565a1141137]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x5565a11381c1]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x5565a1146134]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x5565a1131f6e]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x5565a11308e0]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x5565a1318bbb]
   > sql/sql_select.cc:2550(JOIN::optimize_inner())[0x5565a1318848]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x5565a184fad1]
   > ??:0(pthread_condattr_setpshared)[0x7f1322196ac3]
   > ??:0(__xmknodat)[0x7f1322228850]
   > Trying to get some variables.
   > Some pointers may be invalid and cause the dump to abort.
   > Query (0x7f12b4014ec0): select subq_0.c0 as c0 from (select ref_0.c_s7edob as c0 from t_dmvax as ref_0 where ref_0.c_s7edob not in ( select ref_1.c_wwyiz as c0 from t_dmvax as ref_1) ) as subq_0 where subq_0.c0 = ( select ref_3.c_wwyiz as c0 from (t_dmvax as ref_2 cross join t_dmvax as ref_3) union select ref_4.c_wwyiz as c0 from t_dmvax as ref_4)
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

### Scenario 1
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 0 / 0
 * Instruction #1:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  select subq_0.c0 as c0 from (select ref_0.c_s7edob as c0 from t_dmvax as ref_0 ...
     - Transaction: conn_0
     - Output: ERROR: 2013 (HY000): Lost connection to MySQL server during query
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #3:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: ERROR: MySQL Connection not available.
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0

 * Container logs:
   > mysqld: /server/server/sql/item.cc:10699: virtual longlong Item_type_holder::val_int(): Assertion `0' failed.
   > 240716 17:37:53 [ERROR] mysqld got signal 6 ;
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
   > max_used_connections=1
   > max_threads=153
   > thread_count=1
   > It is possible that mysqld could use up to 
   > key_buffer_size + (read_buffer_size + sort_buffer_size)*max_threads = 468134 K  bytes of memory
   > Hope that's ok; if not, decrease some variables in the equation.
   > Thread pointer: 0x7fb1b4000dc8
   > Attempting backtrace. You can use the following information to find out
   > where mysqld died. If you see no messages after this, something went
   > terribly wrong...
   > stack_bottom = 0x7fb22dd4cb78 thread_stack 0x49000
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x557b1cd223ce]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x557b1c4223f7]
   > ??:0(__sigaction)[0x7fb230294520]
   > ??:0(pthread_kill)[0x7fb2302e89fc]
   > ??:0(raise)[0x7fb230294476]
   > ??:0(abort)[0x7fb23027a7f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7fb23027a71b]
   > ??:0(__assert_fail)[0x7fb23028be96]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x557b1c469bf3]
   > /usr/local/mysql/bin/mysqld(+0x861cbf)[0x557b1beaccbf]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x51)[0x557b1c467553]
   > /usr/local/mysql/bin/mysqld(+0xcca9e2)[0x557b1c3159e2]
   > /usr/local/mysql/bin/mysqld(+0xccaaaa)[0x557b1c315aaa]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x69)[0x557b1c54f149]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0x576)[0x557b1c53f486]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x18e)[0x557b1c5419c4]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0xd8)[0x557b1c2a4292]
   > /usr/local/mysql/bin/mysqld(+0xa6e44d)[0x557b1c0b944d]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x20a4)[0x557b1c0ac3f0]
   > sql/item.h:1779(Item::val_int_result())[0x557b1c0a9c09]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x557b1c0082d9]
   > sql/item.h:7099(Item_cache::has_value())[0x557b1c2a20c4]
   > sql/item.h:7108(Item_cache::is_null())[0x557b1c0ae774]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x557b1c0ac4f3]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x557b1c0a9c09]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x557b1c0b5ab2]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x557b1c0a46a3]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x557b1c049137]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x557b1c0401c1]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x557b1c04e134]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x557b1c039f6e]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x557b1c0388e0]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x557b1c220bbb]
   > sql/sql_select.cc:2550(JOIN::optimize_inner())[0x557b1c220848]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x557b1c757ad1]
   > ??:0(pthread_condattr_setpshared)[0x7fb2302e6ac3]
   > ??:0(__xmknodat)[0x7fb230378850]
   > Trying to get some variables.
   > Some pointers may be invalid and cause the dump to abort.
   > Query (0x7fb1b4014ec0): select subq_0.c0 as c0 from (select ref_0.c_s7edob as c0 from t_dmvax as ref_0 where ref_0.c_s7edob not in ( select ref_1.c_wwyiz as c0 from t_dmvax as ref_1) ) as subq_0 where subq_0.c0 = ( select ref_3.c_wwyiz as c0 from (t_dmvax as ref_2 cross join t_dmvax as ref_3) union select ref_4.c_wwyiz as c0 from t_dmvax as ref_4)
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

### Scenario 2
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 0 / 0
 * Instruction #1:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  select subq_0.c0 as c0 from (select ref_0.c_s7edob as c0 from t_dmvax as ref_0 ...
     - Transaction: conn_0
     - Output: ERROR: 2013 (HY000): Lost connection to MySQL server during query
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #3:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: ERROR: MySQL Connection not available.
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0

 * Container logs:
   > mysqld: /server/server/sql/item.cc:10699: virtual longlong Item_type_holder::val_int(): Assertion `0' failed.
   > 240716 17:38:04 [ERROR] mysqld got signal 6 ;
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
   > max_used_connections=1
   > max_threads=153
   > thread_count=1
   > It is possible that mysqld could use up to 
   > key_buffer_size + (read_buffer_size + sort_buffer_size)*max_threads = 468134 K  bytes of memory
   > Hope that's ok; if not, decrease some variables in the equation.
   > Thread pointer: 0x7fd220000dc8
   > Attempting backtrace. You can use the following information to find out
   > where mysqld died. If you see no messages after this, something went
   > terribly wrong...
   > stack_bottom = 0x7fd290968b78 thread_stack 0x49000
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x5598d45203ce]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x5598d3c203f7]
   > ??:0(__sigaction)[0x7fd2936d0520]
   > ??:0(pthread_kill)[0x7fd2937249fc]
   > ??:0(raise)[0x7fd2936d0476]
   > ??:0(abort)[0x7fd2936b67f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7fd2936b671b]
   > ??:0(__assert_fail)[0x7fd2936c7e96]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x5598d3c67bf3]
   > /usr/local/mysql/bin/mysqld(+0x861cbf)[0x5598d36aacbf]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x51)[0x5598d3c65553]
   > /usr/local/mysql/bin/mysqld(+0xcca9e2)[0x5598d3b139e2]
   > /usr/local/mysql/bin/mysqld(+0xccaaaa)[0x5598d3b13aaa]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x69)[0x5598d3d4d149]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0x576)[0x5598d3d3d486]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x18e)[0x5598d3d3f9c4]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0xd8)[0x5598d3aa2292]
   > /usr/local/mysql/bin/mysqld(+0xa6e44d)[0x5598d38b744d]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x20a4)[0x5598d38aa3f0]
   > sql/item.h:1779(Item::val_int_result())[0x5598d38a7c09]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x5598d38062d9]
   > sql/item.h:7099(Item_cache::has_value())[0x5598d3aa00c4]
   > sql/item.h:7108(Item_cache::is_null())[0x5598d38ac774]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x5598d38aa4f3]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x5598d38a7c09]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x5598d38b3ab2]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x5598d38a26a3]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x5598d3847137]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x5598d383e1c1]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x5598d384c134]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x5598d3837f6e]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x5598d38368e0]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x5598d3a1ebbb]
   > sql/sql_select.cc:2550(JOIN::optimize_inner())[0x5598d3a1e848]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x5598d3f55ad1]
   > ??:0(pthread_condattr_setpshared)[0x7fd293722ac3]
   > ??:0(__xmknodat)[0x7fd2937b4850]
   > Trying to get some variables.
   > Some pointers may be invalid and cause the dump to abort.
   > Query (0x7fd220014ec0): select subq_0.c0 as c0 from (select ref_0.c_s7edob as c0 from t_dmvax as ref_0 where ref_0.c_s7edob not in ( select ref_1.c_wwyiz as c0 from t_dmvax as ref_1) ) as subq_0 where subq_0.c0 = ( select ref_3.c_wwyiz as c0 from (t_dmvax as ref_2 cross join t_dmvax as ref_3) union select ref_4.c_wwyiz as c0 from t_dmvax as ref_4)
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

### Scenario 3
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 0 / 0
 * Instruction #1:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  select subq_0.c0 as c0 from (select ref_0.c_s7edob as c0 from t_dmvax as ref_0 ...
     - Transaction: conn_0
     - Output: ERROR: 2013 (HY000): Lost connection to MySQL server during query
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #3:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: ERROR: MySQL Connection not available.
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0

 * Container logs:
   > mysqld: /server/server/sql/item.cc:10699: virtual longlong Item_type_holder::val_int(): Assertion `0' failed.
   > 240716 17:38:14 [ERROR] mysqld got signal 6 ;
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
   > max_used_connections=1
   > max_threads=153
   > thread_count=1
   > It is possible that mysqld could use up to 
   > key_buffer_size + (read_buffer_size + sort_buffer_size)*max_threads = 468134 K  bytes of memory
   > Hope that's ok; if not, decrease some variables in the equation.
   > Thread pointer: 0x7fc878000dc8
   > Attempting backtrace. You can use the following information to find out
   > where mysqld died. If you see no messages after this, something went
   > terribly wrong...
   > stack_bottom = 0x7fc8e8e70b78 thread_stack 0x49000
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x5615119653ce]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x5615110653f7]
   > ??:0(__sigaction)[0x7fc8e946c520]
   > ??:0(pthread_kill)[0x7fc8e94c09fc]
   > ??:0(raise)[0x7fc8e946c476]
   > ??:0(abort)[0x7fc8e94527f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7fc8e945271b]
   > ??:0(__assert_fail)[0x7fc8e9463e96]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x5615110acbf3]
   > /usr/local/mysql/bin/mysqld(+0x861cbf)[0x561510aefcbf]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x51)[0x5615110aa553]
   > /usr/local/mysql/bin/mysqld(+0xcca9e2)[0x561510f589e2]
   > /usr/local/mysql/bin/mysqld(+0xccaaaa)[0x561510f58aaa]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x69)[0x561511192149]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0x576)[0x561511182486]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x18e)[0x5615111849c4]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0xd8)[0x561510ee7292]
   > /usr/local/mysql/bin/mysqld(+0xa6e44d)[0x561510cfc44d]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x20a4)[0x561510cef3f0]
   > sql/item.h:1779(Item::val_int_result())[0x561510cecc09]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x561510c4b2d9]
   > sql/item.h:7099(Item_cache::has_value())[0x561510ee50c4]
   > sql/item.h:7108(Item_cache::is_null())[0x561510cf1774]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x561510cef4f3]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x561510cecc09]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x561510cf8ab2]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x561510ce76a3]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x561510c8c137]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x561510c831c1]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x561510c91134]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x561510c7cf6e]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x561510c7b8e0]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x561510e63bbb]
   > sql/sql_select.cc:2550(JOIN::optimize_inner())[0x561510e63848]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x56151139aad1]
   > ??:0(pthread_condattr_setpshared)[0x7fc8e94beac3]
   > ??:0(__xmknodat)[0x7fc8e9550850]
   > Trying to get some variables.
   > Some pointers may be invalid and cause the dump to abort.
   > Query (0x7fc878014ec0): select subq_0.c0 as c0 from (select ref_0.c_s7edob as c0 from t_dmvax as ref_0 where ref_0.c_s7edob not in ( select ref_1.c_wwyiz as c0 from t_dmvax as ref_1) ) as subq_0 where subq_0.c0 = ( select ref_3.c_wwyiz as c0 from (t_dmvax as ref_2 cross join t_dmvax as ref_3) union select ref_4.c_wwyiz as c0 from t_dmvax as ref_4)
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

### Scenario 4
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 0 / 0
 * Instruction #1:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  select subq_0.c0 as c0 from (select ref_0.c_s7edob as c0 from t_dmvax as ref_0 ...
     - Transaction: conn_0
     - Output: ERROR: 2013 (HY000): Lost connection to MySQL server during query
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #3:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: ERROR: MySQL Connection not available.
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0

 * Container logs:
   > mysqld: /server/server/sql/item.cc:10699: virtual longlong Item_type_holder::val_int(): Assertion `0' failed.
   > 240716 17:38:25 [ERROR] mysqld got signal 6 ;
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
   > max_used_connections=1
   > max_threads=153
   > thread_count=1
   > It is possible that mysqld could use up to 
   > key_buffer_size + (read_buffer_size + sort_buffer_size)*max_threads = 468134 K  bytes of memory
   > Hope that's ok; if not, decrease some variables in the equation.
   > Thread pointer: 0x7fdcec000dc8
   > Attempting backtrace. You can use the following information to find out
   > where mysqld died. If you see no messages after this, something went
   > terribly wrong...
   > stack_bottom = 0x7fdd52dd6b78 thread_stack 0x49000
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x5643ddc1c3ce]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x5643dd31c3f7]
   > ??:0(__sigaction)[0x7fdd533d2520]
   > ??:0(pthread_kill)[0x7fdd534269fc]
   > ??:0(raise)[0x7fdd533d2476]
   > ??:0(abort)[0x7fdd533b87f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7fdd533b871b]
   > ??:0(__assert_fail)[0x7fdd533c9e96]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x5643dd363bf3]
   > /usr/local/mysql/bin/mysqld(+0x861cbf)[0x5643dcda6cbf]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x51)[0x5643dd361553]
   > /usr/local/mysql/bin/mysqld(+0xcca9e2)[0x5643dd20f9e2]
   > /usr/local/mysql/bin/mysqld(+0xccaaaa)[0x5643dd20faaa]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x69)[0x5643dd449149]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0x576)[0x5643dd439486]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x18e)[0x5643dd43b9c4]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0xd8)[0x5643dd19e292]
   > /usr/local/mysql/bin/mysqld(+0xa6e44d)[0x5643dcfb344d]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x20a4)[0x5643dcfa63f0]
   > sql/item.h:1779(Item::val_int_result())[0x5643dcfa3c09]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x5643dcf022d9]
   > sql/item.h:7099(Item_cache::has_value())[0x5643dd19c0c4]
   > sql/item.h:7108(Item_cache::is_null())[0x5643dcfa8774]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x5643dcfa64f3]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x5643dcfa3c09]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x5643dcfafab2]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x5643dcf9e6a3]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x5643dcf43137]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x5643dcf3a1c1]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x5643dcf48134]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x5643dcf33f6e]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x5643dcf328e0]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x5643dd11abbb]
   > sql/sql_select.cc:2550(JOIN::optimize_inner())[0x5643dd11a848]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x5643dd651ad1]
   > ??:0(pthread_condattr_setpshared)[0x7fdd53424ac3]
   > ??:0(__xmknodat)[0x7fdd534b6850]
   > Trying to get some variables.
   > Some pointers may be invalid and cause the dump to abort.
   > Query (0x7fdcec014ec0): select subq_0.c0 as c0 from (select ref_0.c_s7edob as c0 from t_dmvax as ref_0 where ref_0.c_s7edob not in ( select ref_1.c_wwyiz as c0 from t_dmvax as ref_1) ) as subq_0 where subq_0.c0 = ( select ref_3.c_wwyiz as c0 from (t_dmvax as ref_2 cross join t_dmvax as ref_3) union select ref_4.c_wwyiz as c0 from t_dmvax as ref_4)
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

### Scenario 5
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 0 / 0
 * Instruction #1:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  select subq_0.c0 as c0 from (select ref_0.c_s7edob as c0 from t_dmvax as ref_0 ...
     - Transaction: conn_0
     - Output: ERROR: 2013 (HY000): Lost connection to MySQL server during query
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #3:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: ERROR: MySQL Connection not available.
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0

 * Container logs:
   > mysqld: /server/server/sql/item.cc:10699: virtual longlong Item_type_holder::val_int(): Assertion `0' failed.
   > 240716 17:38:35 [ERROR] mysqld got signal 6 ;
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
   > max_used_connections=1
   > max_threads=153
   > thread_count=1
   > It is possible that mysqld could use up to 
   > key_buffer_size + (read_buffer_size + sort_buffer_size)*max_threads = 468134 K  bytes of memory
   > Hope that's ok; if not, decrease some variables in the equation.
   > Thread pointer: 0x7fb80c000dc8
   > Attempting backtrace. You can use the following information to find out
   > where mysqld died. If you see no messages after this, something went
   > terribly wrong...
   > stack_bottom = 0x7fb884768b78 thread_stack 0x49000
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x5614b78243ce]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x5614b6f243f7]
   > ??:0(__sigaction)[0x7fb885d70520]
   > ??:0(pthread_kill)[0x7fb885dc49fc]
   > ??:0(raise)[0x7fb885d70476]
   > ??:0(abort)[0x7fb885d567f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7fb885d5671b]
   > ??:0(__assert_fail)[0x7fb885d67e96]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x5614b6f6bbf3]
   > /usr/local/mysql/bin/mysqld(+0x861cbf)[0x5614b69aecbf]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x51)[0x5614b6f69553]
   > /usr/local/mysql/bin/mysqld(+0xcca9e2)[0x5614b6e179e2]
   > /usr/local/mysql/bin/mysqld(+0xccaaaa)[0x5614b6e17aaa]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x69)[0x5614b7051149]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0x576)[0x5614b7041486]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x18e)[0x5614b70439c4]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0xd8)[0x5614b6da6292]
   > /usr/local/mysql/bin/mysqld(+0xa6e44d)[0x5614b6bbb44d]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x20a4)[0x5614b6bae3f0]
   > sql/item.h:1779(Item::val_int_result())[0x5614b6babc09]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x5614b6b0a2d9]
   > sql/item.h:7099(Item_cache::has_value())[0x5614b6da40c4]
   > sql/item.h:7108(Item_cache::is_null())[0x5614b6bb0774]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x5614b6bae4f3]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x5614b6babc09]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x5614b6bb7ab2]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x5614b6ba66a3]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x5614b6b4b137]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x5614b6b421c1]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x5614b6b50134]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x5614b6b3bf6e]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x5614b6b3a8e0]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x5614b6d22bbb]
   > sql/sql_select.cc:2550(JOIN::optimize_inner())[0x5614b6d22848]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x5614b7259ad1]
   > ??:0(pthread_condattr_setpshared)[0x7fb885dc2ac3]
   > ??:0(__xmknodat)[0x7fb885e54850]
   > Trying to get some variables.
   > Some pointers may be invalid and cause the dump to abort.
   > Query (0x7fb80c014ec0): select subq_0.c0 as c0 from (select ref_0.c_s7edob as c0 from t_dmvax as ref_0 where ref_0.c_s7edob not in ( select ref_1.c_wwyiz as c0 from t_dmvax as ref_1) ) as subq_0 where subq_0.c0 = ( select ref_3.c_wwyiz as c0 from (t_dmvax as ref_2 cross join t_dmvax as ref_3) union select ref_4.c_wwyiz as c0 from t_dmvax as ref_4)
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

### Scenario 6
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 0 / 0
 * Instruction #1:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  select subq_0.c0 as c0 from (select ref_0.c_s7edob as c0 from t_dmvax as ref_0 ...
     - Transaction: conn_0
     - Output: ERROR: 2013 (HY000): Lost connection to MySQL server during query
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #3:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: ERROR: MySQL Connection not available.
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0

 * Container logs:
   > mysqld: /server/server/sql/item.cc:10699: virtual longlong Item_type_holder::val_int(): Assertion `0' failed.
   > 240716 17:38:46 [ERROR] mysqld got signal 6 ;
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
   > max_used_connections=1
   > max_threads=153
   > thread_count=1
   > It is possible that mysqld could use up to 
   > key_buffer_size + (read_buffer_size + sort_buffer_size)*max_threads = 468134 K  bytes of memory
   > Hope that's ok; if not, decrease some variables in the equation.
   > Thread pointer: 0x7fe3ac000dc8
   > Attempting backtrace. You can use the following information to find out
   > where mysqld died. If you see no messages after this, something went
   > terribly wrong...
   > stack_bottom = 0x7fe421901b78 thread_stack 0x49000
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x561f816533ce]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x561f80d533f7]
   > ??:0(__sigaction)[0x7fe423e65520]
   > ??:0(pthread_kill)[0x7fe423eb99fc]
   > ??:0(raise)[0x7fe423e65476]
   > ??:0(abort)[0x7fe423e4b7f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7fe423e4b71b]
   > ??:0(__assert_fail)[0x7fe423e5ce96]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x561f80d9abf3]
   > /usr/local/mysql/bin/mysqld(+0x861cbf)[0x561f807ddcbf]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x51)[0x561f80d98553]
   > /usr/local/mysql/bin/mysqld(+0xcca9e2)[0x561f80c469e2]
   > /usr/local/mysql/bin/mysqld(+0xccaaaa)[0x561f80c46aaa]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x69)[0x561f80e80149]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0x576)[0x561f80e70486]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x18e)[0x561f80e729c4]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0xd8)[0x561f80bd5292]
   > /usr/local/mysql/bin/mysqld(+0xa6e44d)[0x561f809ea44d]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x20a4)[0x561f809dd3f0]
   > sql/item.h:1779(Item::val_int_result())[0x561f809dac09]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x561f809392d9]
   > sql/item.h:7099(Item_cache::has_value())[0x561f80bd30c4]
   > sql/item.h:7108(Item_cache::is_null())[0x561f809df774]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x561f809dd4f3]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x561f809dac09]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x561f809e6ab2]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x561f809d56a3]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x561f8097a137]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x561f809711c1]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x561f8097f134]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x561f8096af6e]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x561f809698e0]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x561f80b51bbb]
   > sql/sql_select.cc:2550(JOIN::optimize_inner())[0x561f80b51848]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x561f81088ad1]
   > ??:0(pthread_condattr_setpshared)[0x7fe423eb7ac3]
   > ??:0(__xmknodat)[0x7fe423f49850]
   > Trying to get some variables.
   > Some pointers may be invalid and cause the dump to abort.
   > Query (0x7fe3ac014ec0): select subq_0.c0 as c0 from (select ref_0.c_s7edob as c0 from t_dmvax as ref_0 where ref_0.c_s7edob not in ( select ref_1.c_wwyiz as c0 from t_dmvax as ref_1) ) as subq_0 where subq_0.c0 = ( select ref_3.c_wwyiz as c0 from (t_dmvax as ref_2 cross join t_dmvax as ref_3) union select ref_4.c_wwyiz as c0 from t_dmvax as ref_4)
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

### Scenario 7
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 0 / 0
 * Instruction #1:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  select subq_0.c0 as c0 from (select ref_0.c_s7edob as c0 from t_dmvax as ref_0 ...
     - Transaction: conn_0
     - Output: ERROR: 2013 (HY000): Lost connection to MySQL server during query
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #3:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: ERROR: MySQL Connection not available.
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0

 * Container logs:
   > mysqld: /server/server/sql/item.cc:10699: virtual longlong Item_type_holder::val_int(): Assertion `0' failed.
   > 240716 17:38:56 [ERROR] mysqld got signal 6 ;
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
   > max_used_connections=1
   > max_threads=153
   > thread_count=1
   > It is possible that mysqld could use up to 
   > key_buffer_size + (read_buffer_size + sort_buffer_size)*max_threads = 468134 K  bytes of memory
   > Hope that's ok; if not, decrease some variables in the equation.
   > Thread pointer: 0x7f58c4000dc8
   > Attempting backtrace. You can use the following information to find out
   > where mysqld died. If you see no messages after this, something went
   > terribly wrong...
   > stack_bottom = 0x7f59444c6b78 thread_stack 0x49000
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x56066e2523ce]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x56066d9523f7]
   > ??:0(__sigaction)[0x7f5944ca8520]
   > ??:0(pthread_kill)[0x7f5944cfc9fc]
   > ??:0(raise)[0x7f5944ca8476]
   > ??:0(abort)[0x7f5944c8e7f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7f5944c8e71b]
   > ??:0(__assert_fail)[0x7f5944c9fe96]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x56066d999bf3]
   > /usr/local/mysql/bin/mysqld(+0x861cbf)[0x56066d3dccbf]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x51)[0x56066d997553]
   > /usr/local/mysql/bin/mysqld(+0xcca9e2)[0x56066d8459e2]
   > /usr/local/mysql/bin/mysqld(+0xccaaaa)[0x56066d845aaa]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x69)[0x56066da7f149]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0x576)[0x56066da6f486]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x18e)[0x56066da719c4]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0xd8)[0x56066d7d4292]
   > /usr/local/mysql/bin/mysqld(+0xa6e44d)[0x56066d5e944d]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x20a4)[0x56066d5dc3f0]
   > sql/item.h:1779(Item::val_int_result())[0x56066d5d9c09]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x56066d5382d9]
   > sql/item.h:7099(Item_cache::has_value())[0x56066d7d20c4]
   > sql/item.h:7108(Item_cache::is_null())[0x56066d5de774]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x56066d5dc4f3]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x56066d5d9c09]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x56066d5e5ab2]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x56066d5d46a3]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x56066d579137]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x56066d5701c1]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x56066d57e134]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x56066d569f6e]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x56066d5688e0]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x56066d750bbb]
   > sql/sql_select.cc:2550(JOIN::optimize_inner())[0x56066d750848]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x56066dc87ad1]
   > ??:0(pthread_condattr_setpshared)[0x7f5944cfaac3]
   > ??:0(__xmknodat)[0x7f5944d8c850]
   > Trying to get some variables.
   > Some pointers may be invalid and cause the dump to abort.
   > Query (0x7f58c4014ec0): select subq_0.c0 as c0 from (select ref_0.c_s7edob as c0 from t_dmvax as ref_0 where ref_0.c_s7edob not in ( select ref_1.c_wwyiz as c0 from t_dmvax as ref_1) ) as subq_0 where subq_0.c0 = ( select ref_3.c_wwyiz as c0 from (t_dmvax as ref_2 cross join t_dmvax as ref_3) union select ref_4.c_wwyiz as c0 from t_dmvax as ref_4)
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

### Scenario 8
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 0 / 0
 * Instruction #1:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  select subq_0.c0 as c0 from (select ref_0.c_s7edob as c0 from t_dmvax as ref_0 ...
     - Transaction: conn_0
     - Output: ERROR: 2013 (HY000): Lost connection to MySQL server during query
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #3:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: ERROR: MySQL Connection not available.
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0

 * Container logs:
   > mysqld: /server/server/sql/item.cc:10699: virtual longlong Item_type_holder::val_int(): Assertion `0' failed.
   > 240716 17:39:06 [ERROR] mysqld got signal 6 ;
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
   > max_used_connections=1
   > max_threads=153
   > thread_count=1
   > It is possible that mysqld could use up to 
   > key_buffer_size + (read_buffer_size + sort_buffer_size)*max_threads = 468134 K  bytes of memory
   > Hope that's ok; if not, decrease some variables in the equation.
   > Thread pointer: 0x7f7934000dc8
   > Attempting backtrace. You can use the following information to find out
   > where mysqld died. If you see no messages after this, something went
   > terribly wrong...
   > stack_bottom = 0x7f799d247b78 thread_stack 0x49000
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x55d3dda213ce]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x55d3dd1213f7]
   > ??:0(__sigaction)[0x7f799d843520]
   > ??:0(pthread_kill)[0x7f799d8979fc]
   > ??:0(raise)[0x7f799d843476]
   > ??:0(abort)[0x7f799d8297f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7f799d82971b]
   > ??:0(__assert_fail)[0x7f799d83ae96]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x55d3dd168bf3]
   > /usr/local/mysql/bin/mysqld(+0x861cbf)[0x55d3dcbabcbf]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x51)[0x55d3dd166553]
   > /usr/local/mysql/bin/mysqld(+0xcca9e2)[0x55d3dd0149e2]
   > /usr/local/mysql/bin/mysqld(+0xccaaaa)[0x55d3dd014aaa]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x69)[0x55d3dd24e149]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0x576)[0x55d3dd23e486]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x18e)[0x55d3dd2409c4]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0xd8)[0x55d3dcfa3292]
   > /usr/local/mysql/bin/mysqld(+0xa6e44d)[0x55d3dcdb844d]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x20a4)[0x55d3dcdab3f0]
   > sql/item.h:1779(Item::val_int_result())[0x55d3dcda8c09]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x55d3dcd072d9]
   > sql/item.h:7099(Item_cache::has_value())[0x55d3dcfa10c4]
   > sql/item.h:7108(Item_cache::is_null())[0x55d3dcdad774]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x55d3dcdab4f3]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x55d3dcda8c09]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x55d3dcdb4ab2]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x55d3dcda36a3]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x55d3dcd48137]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x55d3dcd3f1c1]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x55d3dcd4d134]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x55d3dcd38f6e]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x55d3dcd378e0]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x55d3dcf1fbbb]
   > sql/sql_select.cc:2550(JOIN::optimize_inner())[0x55d3dcf1f848]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x55d3dd456ad1]
   > ??:0(pthread_condattr_setpshared)[0x7f799d895ac3]
   > ??:0(__xmknodat)[0x7f799d927850]
   > Trying to get some variables.
   > Some pointers may be invalid and cause the dump to abort.
   > Query (0x7f7934014ec0): select subq_0.c0 as c0 from (select ref_0.c_s7edob as c0 from t_dmvax as ref_0 where ref_0.c_s7edob not in ( select ref_1.c_wwyiz as c0 from t_dmvax as ref_1) ) as subq_0 where subq_0.c0 = ( select ref_3.c_wwyiz as c0 from (t_dmvax as ref_2 cross join t_dmvax as ref_3) union select ref_4.c_wwyiz as c0 from t_dmvax as ref_4)
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

### Scenario 9
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows / Warnings: 0 / 0
 * Instruction #1:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  select subq_0.c0 as c0 from (select ref_0.c_s7edob as c0 from t_dmvax as ref_0 ...
     - Transaction: conn_0
     - Output: ERROR: 2013 (HY000): Lost connection to MySQL server during query
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0
 * Instruction #3:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: ERROR: MySQL Connection not available.
     - Executed order: Not executed
     - Affected rows / Warnings: -1 / 0

 * Container logs:
   > mysqld: /server/server/sql/item.cc:10699: virtual longlong Item_type_holder::val_int(): Assertion `0' failed.
   > 240716 17:39:16 [ERROR] mysqld got signal 6 ;
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
   > max_used_connections=1
   > max_threads=153
   > thread_count=1
   > It is possible that mysqld could use up to 
   > key_buffer_size + (read_buffer_size + sort_buffer_size)*max_threads = 468134 K  bytes of memory
   > Hope that's ok; if not, decrease some variables in the equation.
   > Thread pointer: 0x7efde0000dc8
   > Attempting backtrace. You can use the following information to find out
   > where mysqld died. If you see no messages after this, something went
   > terribly wrong...
   > stack_bottom = 0x7efe48168b78 thread_stack 0x49000
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x5591d8b583ce]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x5591d82583f7]
   > ??:0(__sigaction)[0x7efe4939a520]
   > ??:0(pthread_kill)[0x7efe493ee9fc]
   > ??:0(raise)[0x7efe4939a476]
   > ??:0(abort)[0x7efe493807f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7efe4938071b]
   > ??:0(__assert_fail)[0x7efe49391e96]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x5591d829fbf3]
   > /usr/local/mysql/bin/mysqld(+0x861cbf)[0x5591d7ce2cbf]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x51)[0x5591d829d553]
   > /usr/local/mysql/bin/mysqld(+0xcca9e2)[0x5591d814b9e2]
   > /usr/local/mysql/bin/mysqld(+0xccaaaa)[0x5591d814baaa]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x69)[0x5591d8385149]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0x576)[0x5591d8375486]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x18e)[0x5591d83779c4]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0xd8)[0x5591d80da292]
   > /usr/local/mysql/bin/mysqld(+0xa6e44d)[0x5591d7eef44d]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x20a4)[0x5591d7ee23f0]
   > sql/item.h:1779(Item::val_int_result())[0x5591d7edfc09]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x5591d7e3e2d9]
   > sql/item.h:7099(Item_cache::has_value())[0x5591d80d80c4]
   > sql/item.h:7108(Item_cache::is_null())[0x5591d7ee4774]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x5591d7ee24f3]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x5591d7edfc09]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x5591d7eebab2]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x5591d7eda6a3]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x5591d7e7f137]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x5591d7e761c1]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x5591d7e84134]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x5591d7e6ff6e]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x5591d7e6e8e0]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x5591d8056bbb]
   > sql/sql_select.cc:2550(JOIN::optimize_inner())[0x5591d8056848]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x5591d858dad1]
   > ??:0(pthread_condattr_setpshared)[0x7efe493ecac3]
   > ??:0(__xmknodat)[0x7efe4947e850]
   > Trying to get some variables.
   > Some pointers may be invalid and cause the dump to abort.
   > Query (0x7efde0014ec0): select subq_0.c0 as c0 from (select ref_0.c_s7edob as c0 from t_dmvax as ref_0 where ref_0.c_s7edob not in ( select ref_1.c_wwyiz as c0 from t_dmvax as ref_1) ) as subq_0 where subq_0.c0 = ( select ref_3.c_wwyiz as c0 from (t_dmvax as ref_2 cross join t_dmvax as ref_3) union select ref_4.c_wwyiz as c0 from t_dmvax as ref_4)
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
