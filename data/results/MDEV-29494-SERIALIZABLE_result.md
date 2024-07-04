# Bug ID MDEV-29494-SERIALIZABLE

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-29494
Original isolation level: REPEATABLE READ
Tested isolation level:   SERIALIZABLE
Description:              The server should crash.


## Details
 * Database: mariadb-10.10.1
 * Number of scenarios: 10
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
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  select subq_0.c0 as c0 from (select ref_0.c_s7edob as c0 from t_dmvax as ref_0 ...
     - Transaction: conn_0
     - Output: ERROR: Timeout for this transaction.
     - Executed order: Not executed
     - Affected rows / Warnings: None / None
 * Instruction #3:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: ERROR: Timeout for this transaction.
     - Executed order: Not executed
     - Affected rows / Warnings: None / None

 * Container logs:
   > mysqld: /server/server/sql/item.cc:10699: virtual longlong Item_type_holder::val_int(): Assertion `0' failed.
   > 240704 13:25:44 [ERROR] mysqld got signal 6 ;
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
   > Thread pointer: 0x62b00011f288
   > Attempting backtrace. You can use the following information to find out
   > where mysqld died. If you see no messages after this, something went
   > terribly wrong...
   > stack_bottom = 0x7f7e2dbfeab0 thread_stack 0x100000
   > /lib/x86_64-linux-gnu/libasan.so.6(+0x45c0e)[0x7f7e4c40dc0e]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x55e688b2ec8f]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x55e6876bfb8d]
   > ??:0(__sigaction)[0x7f7e4b7a6520]
   > ??:0(pthread_kill)[0x7f7e4b7fa9fc]
   > ??:0(raise)[0x7f7e4b7a6476]
   > ??:0(abort)[0x7f7e4b78c7f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7f7e4b78c71b]
   > ??:0(__assert_fail)[0x7f7e4b79de96]
   > /usr/local/mysql/bin/mysqld(_ZN16Item_type_holder7val_intEv+0x64)[0x55e687775ff0]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x55e686a12b72]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x112)[0x55e68776fc58]
   > /usr/local/mysql/bin/mysqld(+0x2312a5c)[0x55e687499a5c]
   > /usr/local/mysql/bin/mysqld(+0x2312c5c)[0x55e687499c5c]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x13d)[0x55e68798fb61]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0xd4f)[0x55e6879662d1]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x3ab)[0x55e68796bed9]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0x2b0)[0x55e6873a3e02]
   > /usr/local/mysql/bin/mysqld(+0x1d686ad)[0x55e686eef6ad]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x596e)[0x55e686ecb14a]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN8optimizeEv+0x424)[0x55e686ec40ce]
   > sql/item.h:1779(Item::val_int_result())[0x55e686d4a875]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x55e68739dfcb]
   > sql/item.h:7099(Item_cache::has_value())[0x55e686ed17b9]
   > sql/item.h:7108(Item_cache::is_null())[0x55e686ecb45b]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x55e686ec40ce]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x55e686ee5dad]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x55e686eb59c1]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x55e686dd7656]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x55e686dc5e57]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x55e686de2a28]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x55e686db84af]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x55e686db51c2]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x55e68727890e]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x55e6872781b8]
   > sql/sql_select.cc:2550(JOIN::optimize_inner())[0x55e687ec551a]
   > ??:0(pthread_condattr_setpshared)[0x7f7e4b7f8ac3]
   > ??:0(__xmknodat)[0x7f7e4b88a850]
   > Trying to get some variables.
   > Some pointers may be invalid and cause the dump to abort.
   > Query (0x6290000872a8): select subq_0.c0 as c0 from (select ref_0.c_s7edob as c0 from t_dmvax as ref_0 where ref_0.c_s7edob not in ( select ref_1.c_wwyiz as c0 from t_dmvax as ref_1) ) as subq_0 where subq_0.c0 = ( select ref_3.c_wwyiz as c0 from (t_dmvax as ref_2 cross join t_dmvax as ref_3) union select ref_4.c_wwyiz as c0 from t_dmvax as ref_4)
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
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
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
     - Output: ERROR: Timeout for this transaction.
     - Executed order: Not executed
     - Affected rows / Warnings: None / None
 * Instruction #3:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: ERROR: Timeout for this transaction.
     - Executed order: Not executed
     - Affected rows / Warnings: None / None

 * Container logs:
   > mysqld: /server/server/sql/item.cc:10699: virtual longlong Item_type_holder::val_int(): Assertion `0' failed.
   > 240704 13:25:57 [ERROR] mysqld got signal 6 ;
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
   > Thread pointer: 0x62b00011f288
   > Attempting backtrace. You can use the following information to find out
   > where mysqld died. If you see no messages after this, something went
   > terribly wrong...
   > stack_bottom = 0x7f13499feab0 thread_stack 0x100000
   > /lib/x86_64-linux-gnu/libasan.so.6(+0x45c0e)[0x7f13680e1c0e]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x55f13b36ec8f]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x55f139effb8d]
   > ??:0(__sigaction)[0x7f136747a520]
   > ??:0(pthread_kill)[0x7f13674ce9fc]
   > ??:0(raise)[0x7f136747a476]
   > ??:0(abort)[0x7f13674607f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7f136746071b]
   > ??:0(__assert_fail)[0x7f1367471e96]
   > /usr/local/mysql/bin/mysqld(_ZN16Item_type_holder7val_intEv+0x64)[0x55f139fb5ff0]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x55f139252b72]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x112)[0x55f139fafc58]
   > /usr/local/mysql/bin/mysqld(+0x2312a5c)[0x55f139cd9a5c]
   > /usr/local/mysql/bin/mysqld(+0x2312c5c)[0x55f139cd9c5c]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x13d)[0x55f13a1cfb61]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0xd4f)[0x55f13a1a62d1]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x3ab)[0x55f13a1abed9]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0x2b0)[0x55f139be3e02]
   > /usr/local/mysql/bin/mysqld(+0x1d686ad)[0x55f13972f6ad]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x596e)[0x55f13970b14a]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN8optimizeEv+0x424)[0x55f1397040ce]
   > /usr/local/mysql/bin/mysqld(_ZN13st_select_lex31optimize_unflattened_subqueriesEb+0x5a9)[0x55f13958a875]
   > sql/item.h:1779(Item::val_int_result())[0x55f139bddfcb]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x55f1397117b9]
   > sql/item.h:7099(Item_cache::has_value())[0x55f13970b45b]
   > sql/item.h:7108(Item_cache::is_null())[0x55f1397040ce]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x55f139725dad]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x55f1396f59c1]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x55f139617656]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x55f139605e57]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x55f139622a28]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x55f1395f84af]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x55f1395f51c2]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x55f139ab890e]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x55f139ab81b8]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x55f13a70551a]
   > ??:0(pthread_condattr_setpshared)[0x7f13674ccac3]
   > ??:0(__xmknodat)[0x7f136755e850]
   > Trying to get some variables.
   > Some pointers may be invalid and cause the dump to abort.
   > Query (0x6290000872a8): select subq_0.c0 as c0 from (select ref_0.c_s7edob as c0 from t_dmvax as ref_0 where ref_0.c_s7edob not in ( select ref_1.c_wwyiz as c0 from t_dmvax as ref_1) ) as subq_0 where subq_0.c0 = ( select ref_3.c_wwyiz as c0 from (t_dmvax as ref_2 cross join t_dmvax as ref_3) union select ref_4.c_wwyiz as c0 from t_dmvax as ref_4)
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
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
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
     - Output: ERROR: Timeout for this transaction.
     - Executed order: Not executed
     - Affected rows / Warnings: None / None
 * Instruction #3:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: ERROR: Timeout for this transaction.
     - Executed order: Not executed
     - Affected rows / Warnings: None / None

 * Container logs:
   > mysqld: /server/server/sql/item.cc:10699: virtual longlong Item_type_holder::val_int(): Assertion `0' failed.
   > 240704 13:26:09 [ERROR] mysqld got signal 6 ;
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
   > Thread pointer: 0x62b00011f288
   > Attempting backtrace. You can use the following information to find out
   > where mysqld died. If you see no messages after this, something went
   > terribly wrong...
   > stack_bottom = 0x7fb4151feab0 thread_stack 0x100000
   > /lib/x86_64-linux-gnu/libasan.so.6(+0x45c0e)[0x7fb433871c0e]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x55f1da8f1c8f]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x55f1d9482b8d]
   > ??:0(__sigaction)[0x7fb432c0a520]
   > ??:0(pthread_kill)[0x7fb432c5e9fc]
   > ??:0(raise)[0x7fb432c0a476]
   > ??:0(abort)[0x7fb432bf07f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7fb432bf071b]
   > ??:0(__assert_fail)[0x7fb432c01e96]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x55f1d9538ff0]
   > /usr/local/mysql/bin/mysqld(+0x188bb72)[0x55f1d87d5b72]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x112)[0x55f1d9532c58]
   > /usr/local/mysql/bin/mysqld(+0x2312a5c)[0x55f1d925ca5c]
   > /usr/local/mysql/bin/mysqld(+0x2312c5c)[0x55f1d925cc5c]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x13d)[0x55f1d9752b61]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0xd4f)[0x55f1d97292d1]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x3ab)[0x55f1d972eed9]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0x2b0)[0x55f1d9166e02]
   > /usr/local/mysql/bin/mysqld(+0x1d686ad)[0x55f1d8cb26ad]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x596e)[0x55f1d8c8e14a]
   > sql/item.h:1779(Item::val_int_result())[0x55f1d8c870ce]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x55f1d8b0d875]
   > sql/item.h:7099(Item_cache::has_value())[0x55f1d9160fcb]
   > sql/item.h:7108(Item_cache::is_null())[0x55f1d8c947b9]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x55f1d8c8e45b]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x55f1d8c870ce]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x55f1d8ca8dad]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x55f1d8c789c1]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x55f1d8b9a656]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x55f1d8b88e57]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x55f1d8ba5a28]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x55f1d8b7b4af]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x55f1d8b781c2]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x55f1d903b90e]
   > sql/sql_select.cc:2550(JOIN::optimize_inner())[0x55f1d903b1b8]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x55f1d9c8851a]
   > ??:0(pthread_condattr_setpshared)[0x7fb432c5cac3]
   > ??:0(__xmknodat)[0x7fb432cee850]
   > Trying to get some variables.
   > Some pointers may be invalid and cause the dump to abort.
   > Query (0x6290000872a8): select subq_0.c0 as c0 from (select ref_0.c_s7edob as c0 from t_dmvax as ref_0 where ref_0.c_s7edob not in ( select ref_1.c_wwyiz as c0 from t_dmvax as ref_1) ) as subq_0 where subq_0.c0 = ( select ref_3.c_wwyiz as c0 from (t_dmvax as ref_2 cross join t_dmvax as ref_3) union select ref_4.c_wwyiz as c0 from t_dmvax as ref_4)
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
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
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
   > 240704 13:26:22 [ERROR] mysqld got signal 6 ;
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
   > Thread pointer: 0x62b00011f288
   > Attempting backtrace. You can use the following information to find out
   > where mysqld died. If you see no messages after this, something went
   > terribly wrong...
   > stack_bottom = 0x7fcddfffeab0 thread_stack 0x100000
   > /lib/x86_64-linux-gnu/libasan.so.6(+0x45c0e)[0x7fcdfe774c0e]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x564687c6fc8f]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x564686800b8d]
   > ??:0(__sigaction)[0x7fcdfdb0d520]
   > ??:0(pthread_kill)[0x7fcdfdb619fc]
   > ??:0(raise)[0x7fcdfdb0d476]
   > ??:0(abort)[0x7fcdfdaf37f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7fcdfdaf371b]
   > ??:0(__assert_fail)[0x7fcdfdb04e96]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x5646868b6ff0]
   > /usr/local/mysql/bin/mysqld(+0x188bb72)[0x564685b53b72]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x112)[0x5646868b0c58]
   > /usr/local/mysql/bin/mysqld(+0x2312a5c)[0x5646865daa5c]
   > /usr/local/mysql/bin/mysqld(+0x2312c5c)[0x5646865dac5c]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x13d)[0x564686ad0b61]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0xd4f)[0x564686aa72d1]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x3ab)[0x564686aaced9]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0x2b0)[0x5646864e4e02]
   > /usr/local/mysql/bin/mysqld(+0x1d686ad)[0x5646860306ad]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x596e)[0x56468600c14a]
   > sql/item.h:1779(Item::val_int_result())[0x5646860050ce]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x564685e8b875]
   > sql/item.h:7099(Item_cache::has_value())[0x5646864defcb]
   > sql/item.h:7108(Item_cache::is_null())[0x5646860127b9]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x56468600c45b]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x5646860050ce]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x564686026dad]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x564685ff69c1]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x564685f18656]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x564685f06e57]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x564685f23a28]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x564685ef94af]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x564685ef61c2]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x5646863b990e]
   > sql/sql_select.cc:2550(JOIN::optimize_inner())[0x5646863b91b8]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x56468700651a]
   > ??:0(pthread_condattr_setpshared)[0x7fcdfdb5fac3]
   > ??:0(__xmknodat)[0x7fcdfdbf1850]
   > Trying to get some variables.
   > Some pointers may be invalid and cause the dump to abort.
   > Query (0x6290000872a8): select subq_0.c0 as c0 from (select ref_0.c_s7edob as c0 from t_dmvax as ref_0 where ref_0.c_s7edob not in ( select ref_1.c_wwyiz as c0 from t_dmvax as ref_1) ) as subq_0 where subq_0.c0 = ( select ref_3.c_wwyiz as c0 from (t_dmvax as ref_2 cross join t_dmvax as ref_3) union select ref_4.c_wwyiz as c0 from t_dmvax as ref_4)
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
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
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
   > 240704 13:26:34 [ERROR] mysqld got signal 6 ;
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
   > Thread pointer: 0x62b00011f288
   > Attempting backtrace. You can use the following information to find out
   > where mysqld died. If you see no messages after this, something went
   > terribly wrong...
   > stack_bottom = 0x7f69a97feab0 thread_stack 0x100000
   > /lib/x86_64-linux-gnu/libasan.so.6(+0x45c0e)[0x7f69c7650c0e]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x5626c9f58c8f]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x5626c8ae9b8d]
   > ??:0(__sigaction)[0x7f69c69e9520]
   > ??:0(pthread_kill)[0x7f69c6a3d9fc]
   > ??:0(raise)[0x7f69c69e9476]
   > ??:0(abort)[0x7f69c69cf7f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7f69c69cf71b]
   > ??:0(__assert_fail)[0x7f69c69e0e96]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x5626c8b9fff0]
   > /usr/local/mysql/bin/mysqld(+0x188bb72)[0x5626c7e3cb72]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x112)[0x5626c8b99c58]
   > /usr/local/mysql/bin/mysqld(+0x2312a5c)[0x5626c88c3a5c]
   > /usr/local/mysql/bin/mysqld(+0x2312c5c)[0x5626c88c3c5c]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x13d)[0x5626c8db9b61]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0xd4f)[0x5626c8d902d1]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x3ab)[0x5626c8d95ed9]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0x2b0)[0x5626c87cde02]
   > /usr/local/mysql/bin/mysqld(+0x1d686ad)[0x5626c83196ad]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x596e)[0x5626c82f514a]
   > sql/item.h:1779(Item::val_int_result())[0x5626c82ee0ce]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x5626c8174875]
   > sql/item.h:7099(Item_cache::has_value())[0x5626c87c7fcb]
   > sql/item.h:7108(Item_cache::is_null())[0x5626c82fb7b9]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x5626c82f545b]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x5626c82ee0ce]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x5626c830fdad]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x5626c82df9c1]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x5626c8201656]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x5626c81efe57]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x5626c820ca28]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x5626c81e24af]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x5626c81df1c2]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x5626c86a290e]
   > sql/sql_select.cc:2550(JOIN::optimize_inner())[0x5626c86a21b8]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x5626c92ef51a]
   > ??:0(pthread_condattr_setpshared)[0x7f69c6a3bac3]
   > ??:0(__xmknodat)[0x7f69c6acd850]
   > Trying to get some variables.
   > Some pointers may be invalid and cause the dump to abort.
   > Query (0x6290000872a8): select subq_0.c0 as c0 from (select ref_0.c_s7edob as c0 from t_dmvax as ref_0 where ref_0.c_s7edob not in ( select ref_1.c_wwyiz as c0 from t_dmvax as ref_1) ) as subq_0 where subq_0.c0 = ( select ref_3.c_wwyiz as c0 from (t_dmvax as ref_2 cross join t_dmvax as ref_3) union select ref_4.c_wwyiz as c0 from t_dmvax as ref_4)
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
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
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
   > 240704 13:26:46 [ERROR] mysqld got signal 6 ;
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
   > Thread pointer: 0x62b00011f288
   > Attempting backtrace. You can use the following information to find out
   > where mysqld died. If you see no messages after this, something went
   > terribly wrong...
   > stack_bottom = 0x7f89219feab0 thread_stack 0x100000
   > /lib/x86_64-linux-gnu/libasan.so.6(+0x45c0e)[0x7f893f828c0e]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x55a0af453c8f]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x55a0adfe4b8d]
   > ??:0(__sigaction)[0x7f893ebc1520]
   > ??:0(pthread_kill)[0x7f893ec159fc]
   > ??:0(raise)[0x7f893ebc1476]
   > ??:0(abort)[0x7f893eba77f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7f893eba771b]
   > ??:0(__assert_fail)[0x7f893ebb8e96]
   > /usr/local/mysql/bin/mysqld(_ZN16Item_type_holder7val_intEv+0x64)[0x55a0ae09aff0]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x55a0ad337b72]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x112)[0x55a0ae094c58]
   > /usr/local/mysql/bin/mysqld(+0x2312a5c)[0x55a0addbea5c]
   > /usr/local/mysql/bin/mysqld(+0x2312c5c)[0x55a0addbec5c]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x13d)[0x55a0ae2b4b61]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0xd4f)[0x55a0ae28b2d1]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x3ab)[0x55a0ae290ed9]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0x2b0)[0x55a0adcc8e02]
   > /usr/local/mysql/bin/mysqld(+0x1d686ad)[0x55a0ad8146ad]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x596e)[0x55a0ad7f014a]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN8optimizeEv+0x424)[0x55a0ad7e90ce]
   > sql/item.h:1779(Item::val_int_result())[0x55a0ad66f875]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x55a0adcc2fcb]
   > sql/item.h:7099(Item_cache::has_value())[0x55a0ad7f67b9]
   > sql/item.h:7108(Item_cache::is_null())[0x55a0ad7f045b]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x55a0ad7e90ce]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x55a0ad80adad]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x55a0ad7da9c1]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x55a0ad6fc656]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x55a0ad6eae57]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x55a0ad707a28]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x55a0ad6dd4af]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x55a0ad6da1c2]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x55a0adb9d90e]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x55a0adb9d1b8]
   > sql/sql_select.cc:2550(JOIN::optimize_inner())[0x55a0ae7ea51a]
   > ??:0(pthread_condattr_setpshared)[0x7f893ec13ac3]
   > ??:0(__xmknodat)[0x7f893eca5850]
   > Trying to get some variables.
   > Some pointers may be invalid and cause the dump to abort.
   > Query (0x6290000872a8): select subq_0.c0 as c0 from (select ref_0.c_s7edob as c0 from t_dmvax as ref_0 where ref_0.c_s7edob not in ( select ref_1.c_wwyiz as c0 from t_dmvax as ref_1) ) as subq_0 where subq_0.c0 = ( select ref_3.c_wwyiz as c0 from (t_dmvax as ref_2 cross join t_dmvax as ref_3) union select ref_4.c_wwyiz as c0 from t_dmvax as ref_4)
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
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
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
     - Output: ERROR: Timeout for this transaction.
     - Executed order: Not executed
     - Affected rows / Warnings: None / None
 * Instruction #3:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: ERROR: Timeout for this transaction.
     - Executed order: Not executed
     - Affected rows / Warnings: None / None

 * Container logs:
   > mysqld: /server/server/sql/item.cc:10699: virtual longlong Item_type_holder::val_int(): Assertion `0' failed.
   > 240704 13:26:58 [ERROR] mysqld got signal 6 ;
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
   > Thread pointer: 0x62b00011f288
   > Attempting backtrace. You can use the following information to find out
   > where mysqld died. If you see no messages after this, something went
   > terribly wrong...
   > stack_bottom = 0x7f3105bfeab0 thread_stack 0x100000
   > /lib/x86_64-linux-gnu/libasan.so.6(+0x45c0e)[0x7f3124411c0e]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x5640e0eeec8f]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x5640dfa7fb8d]
   > ??:0(__sigaction)[0x7f31237aa520]
   > ??:0(pthread_kill)[0x7f31237fe9fc]
   > ??:0(raise)[0x7f31237aa476]
   > ??:0(abort)[0x7f31237907f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7f312379071b]
   > ??:0(__assert_fail)[0x7f31237a1e96]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x5640dfb35ff0]
   > /usr/local/mysql/bin/mysqld(+0x188bb72)[0x5640dedd2b72]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x112)[0x5640dfb2fc58]
   > /usr/local/mysql/bin/mysqld(+0x2312a5c)[0x5640df859a5c]
   > /usr/local/mysql/bin/mysqld(+0x2312c5c)[0x5640df859c5c]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x13d)[0x5640dfd4fb61]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0xd4f)[0x5640dfd262d1]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x3ab)[0x5640dfd2bed9]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0x2b0)[0x5640df763e02]
   > /usr/local/mysql/bin/mysqld(+0x1d686ad)[0x5640df2af6ad]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x596e)[0x5640df28b14a]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN8optimizeEv+0x424)[0x5640df2840ce]
   > /usr/local/mysql/bin/mysqld(_ZN13st_select_lex31optimize_unflattened_subqueriesEb+0x5a9)[0x5640df10a875]
   > sql/item.h:1779(Item::val_int_result())[0x5640df75dfcb]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x5640df2917b9]
   > sql/item.h:7099(Item_cache::has_value())[0x5640df28b45b]
   > sql/item.h:7108(Item_cache::is_null())[0x5640df2840ce]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x5640df2a5dad]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x5640df2759c1]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x5640df197656]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x5640df185e57]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x5640df1a2a28]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x5640df1784af]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x5640df1751c2]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x5640df63890e]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x5640df6381b8]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x5640e028551a]
   > ??:0(pthread_condattr_setpshared)[0x7f31237fcac3]
   > ??:0(__xmknodat)[0x7f312388e850]
   > Trying to get some variables.
   > Some pointers may be invalid and cause the dump to abort.
   > Query (0x6290000872a8): select subq_0.c0 as c0 from (select ref_0.c_s7edob as c0 from t_dmvax as ref_0 where ref_0.c_s7edob not in ( select ref_1.c_wwyiz as c0 from t_dmvax as ref_1) ) as subq_0 where subq_0.c0 = ( select ref_3.c_wwyiz as c0 from (t_dmvax as ref_2 cross join t_dmvax as ref_3) union select ref_4.c_wwyiz as c0 from t_dmvax as ref_4)
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
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
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
     - Output: ERROR: Timeout for this transaction.
     - Executed order: Not executed
     - Affected rows / Warnings: None / None
 * Instruction #3:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: ERROR: Timeout for this transaction.
     - Executed order: Not executed
     - Affected rows / Warnings: None / None

 * Container logs:
   > mysqld: /server/server/sql/item.cc:10699: virtual longlong Item_type_holder::val_int(): Assertion `0' failed.
   > 240704 13:27:11 [ERROR] mysqld got signal 6 ;
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
   > Thread pointer: 0x62b00011f288
   > Attempting backtrace. You can use the following information to find out
   > where mysqld died. If you see no messages after this, something went
   > terribly wrong...
   > stack_bottom = 0x7f0e83ffeab0 thread_stack 0x100000
   > /lib/x86_64-linux-gnu/libasan.so.6(+0x45c0e)[0x7f0ea27f4c0e]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x564a57c91c8f]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x564a56822b8d]
   > ??:0(__sigaction)[0x7f0ea1b8d520]
   > ??:0(pthread_kill)[0x7f0ea1be19fc]
   > ??:0(raise)[0x7f0ea1b8d476]
   > ??:0(abort)[0x7f0ea1b737f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7f0ea1b7371b]
   > ??:0(__assert_fail)[0x7f0ea1b84e96]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x564a568d8ff0]
   > /usr/local/mysql/bin/mysqld(+0x188bb72)[0x564a55b75b72]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x112)[0x564a568d2c58]
   > /usr/local/mysql/bin/mysqld(+0x2312a5c)[0x564a565fca5c]
   > /usr/local/mysql/bin/mysqld(+0x2312c5c)[0x564a565fcc5c]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x13d)[0x564a56af2b61]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0xd4f)[0x564a56ac92d1]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x3ab)[0x564a56aceed9]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0x2b0)[0x564a56506e02]
   > /usr/local/mysql/bin/mysqld(+0x1d686ad)[0x564a560526ad]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x596e)[0x564a5602e14a]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN8optimizeEv+0x424)[0x564a560270ce]
   > sql/item.h:1779(Item::val_int_result())[0x564a55ead875]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x564a56500fcb]
   > sql/item.h:7099(Item_cache::has_value())[0x564a560347b9]
   > sql/item.h:7108(Item_cache::is_null())[0x564a5602e45b]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x564a560270ce]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x564a56048dad]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x564a560189c1]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x564a55f3a656]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x564a55f28e57]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x564a55f45a28]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x564a55f1b4af]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x564a55f181c2]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x564a563db90e]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x564a563db1b8]
   > sql/sql_select.cc:2550(JOIN::optimize_inner())[0x564a5702851a]
   > ??:0(pthread_condattr_setpshared)[0x7f0ea1bdfac3]
   > ??:0(__xmknodat)[0x7f0ea1c71850]
   > Trying to get some variables.
   > Some pointers may be invalid and cause the dump to abort.
   > Query (0x6290000872a8): select subq_0.c0 as c0 from (select ref_0.c_s7edob as c0 from t_dmvax as ref_0 where ref_0.c_s7edob not in ( select ref_1.c_wwyiz as c0 from t_dmvax as ref_1) ) as subq_0 where subq_0.c0 = ( select ref_3.c_wwyiz as c0 from (t_dmvax as ref_2 cross join t_dmvax as ref_3) union select ref_4.c_wwyiz as c0 from t_dmvax as ref_4)
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
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
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
   > 240704 13:27:24 [ERROR] mysqld got signal 6 ;
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
   > Thread pointer: 0x62b00011f288
   > Attempting backtrace. You can use the following information to find out
   > where mysqld died. If you see no messages after this, something went
   > terribly wrong...
   > stack_bottom = 0x7f13c4ffeab0 thread_stack 0x100000
   > /lib/x86_64-linux-gnu/libasan.so.6(+0x45c0e)[0x7f13e36c1c0e]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x55d329773c8f]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x55d328304b8d]
   > ??:0(__sigaction)[0x7f13e2a5a520]
   > ??:0(pthread_kill)[0x7f13e2aae9fc]
   > ??:0(raise)[0x7f13e2a5a476]
   > ??:0(abort)[0x7f13e2a407f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7f13e2a4071b]
   > ??:0(__assert_fail)[0x7f13e2a51e96]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x55d3283baff0]
   > /usr/local/mysql/bin/mysqld(+0x188bb72)[0x55d327657b72]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x112)[0x55d3283b4c58]
   > /usr/local/mysql/bin/mysqld(+0x2312a5c)[0x55d3280dea5c]
   > /usr/local/mysql/bin/mysqld(+0x2312c5c)[0x55d3280dec5c]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x13d)[0x55d3285d4b61]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0xd4f)[0x55d3285ab2d1]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x3ab)[0x55d3285b0ed9]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0x2b0)[0x55d327fe8e02]
   > /usr/local/mysql/bin/mysqld(+0x1d686ad)[0x55d327b346ad]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x596e)[0x55d327b1014a]
   > sql/item.h:1779(Item::val_int_result())[0x55d327b090ce]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x55d32798f875]
   > sql/item.h:7099(Item_cache::has_value())[0x55d327fe2fcb]
   > sql/item.h:7108(Item_cache::is_null())[0x55d327b167b9]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x55d327b1045b]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x55d327b090ce]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x55d327b2adad]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x55d327afa9c1]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x55d327a1c656]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x55d327a0ae57]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x55d327a27a28]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x55d3279fd4af]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x55d3279fa1c2]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x55d327ebd90e]
   > sql/sql_select.cc:2550(JOIN::optimize_inner())[0x55d327ebd1b8]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x55d328b0a51a]
   > ??:0(pthread_condattr_setpshared)[0x7f13e2aacac3]
   > ??:0(__xmknodat)[0x7f13e2b3e850]
   > Trying to get some variables.
   > Some pointers may be invalid and cause the dump to abort.
   > Query (0x6290000872a8): select subq_0.c0 as c0 from (select ref_0.c_s7edob as c0 from t_dmvax as ref_0 where ref_0.c_s7edob not in ( select ref_1.c_wwyiz as c0 from t_dmvax as ref_1) ) as subq_0 where subq_0.c0 = ( select ref_3.c_wwyiz as c0 from (t_dmvax as ref_2 cross join t_dmvax as ref_3) union select ref_4.c_wwyiz as c0 from t_dmvax as ref_4)
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
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
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
     - Output: ERROR: Timeout for this transaction.
     - Executed order: Not executed
     - Affected rows / Warnings: None / None
 * Instruction #3:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: ERROR: Timeout for this transaction.
     - Executed order: Not executed
     - Affected rows / Warnings: None / None

 * Container logs:
   > mysqld: /server/server/sql/item.cc:10699: virtual longlong Item_type_holder::val_int(): Assertion `0' failed.
   > 240704 13:27:36 [ERROR] mysqld got signal 6 ;
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
   > Thread pointer: 0x62b00011f288
   > Attempting backtrace. You can use the following information to find out
   > where mysqld died. If you see no messages after this, something went
   > terribly wrong...
   > stack_bottom = 0x7f4e97ffeab0 thread_stack 0x100000
   > /lib/x86_64-linux-gnu/libasan.so.6(+0x45c0e)[0x7f4eb5e20c0e]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x564d98b1bc8f]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x564d976acb8d]
   > ??:0(__sigaction)[0x7f4eb51b9520]
   > ??:0(pthread_kill)[0x7f4eb520d9fc]
   > ??:0(raise)[0x7f4eb51b9476]
   > ??:0(abort)[0x7f4eb519f7f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7f4eb519f71b]
   > ??:0(__assert_fail)[0x7f4eb51b0e96]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x564d97762ff0]
   > /usr/local/mysql/bin/mysqld(+0x188bb72)[0x564d969ffb72]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x112)[0x564d9775cc58]
   > /usr/local/mysql/bin/mysqld(+0x2312a5c)[0x564d97486a5c]
   > /usr/local/mysql/bin/mysqld(+0x2312c5c)[0x564d97486c5c]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x13d)[0x564d9797cb61]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0xd4f)[0x564d979532d1]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x3ab)[0x564d97958ed9]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0x2b0)[0x564d97390e02]
   > /usr/local/mysql/bin/mysqld(+0x1d686ad)[0x564d96edc6ad]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x596e)[0x564d96eb814a]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN8optimizeEv+0x424)[0x564d96eb10ce]
   > sql/item.h:1779(Item::val_int_result())[0x564d96d37875]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x564d9738afcb]
   > sql/item.h:7099(Item_cache::has_value())[0x564d96ebe7b9]
   > sql/item.h:7108(Item_cache::is_null())[0x564d96eb845b]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x564d96eb10ce]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x564d96ed2dad]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x564d96ea29c1]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x564d96dc4656]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x564d96db2e57]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x564d96dcfa28]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x564d96da54af]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x564d96da21c2]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x564d9726590e]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x564d972651b8]
   > sql/sql_select.cc:2550(JOIN::optimize_inner())[0x564d97eb251a]
   > ??:0(pthread_condattr_setpshared)[0x7f4eb520bac3]
   > ??:0(__xmknodat)[0x7f4eb529d850]
   > Trying to get some variables.
   > Some pointers may be invalid and cause the dump to abort.
   > Query (0x6290000872a8): select subq_0.c0 as c0 from (select ref_0.c_s7edob as c0 from t_dmvax as ref_0 where ref_0.c_s7edob not in ( select ref_1.c_wwyiz as c0 from t_dmvax as ref_1) ) as subq_0 where subq_0.c0 = ( select ref_3.c_wwyiz as c0 from (t_dmvax as ref_2 cross join t_dmvax as ref_3) union select ref_4.c_wwyiz as c0 from t_dmvax as ref_4)
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
