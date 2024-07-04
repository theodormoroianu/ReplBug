# Bug ID MDEV-29494-READ_COMMITTED

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-29494
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED
Description:              The server should crash.


## Details
 * Database: mariadb-10.10.1
 * Number of scenarios: 10
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
   > 240704 13:21:27 [ERROR] mysqld got signal 6 ;
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
   > stack_bottom = 0x7f8e1a1feab0 thread_stack 0x100000
   > /lib/x86_64-linux-gnu/libasan.so.6(+0x45c0e)[0x7f8e38057c0e]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x55ed23e43c8f]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x55ed229d4b8d]
   > ??:0(__sigaction)[0x7f8e373f0520]
   > ??:0(pthread_kill)[0x7f8e374449fc]
   > ??:0(raise)[0x7f8e373f0476]
   > ??:0(abort)[0x7f8e373d67f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7f8e373d671b]
   > ??:0(__assert_fail)[0x7f8e373e7e96]
   > /usr/local/mysql/bin/mysqld(_ZN16Item_type_holder7val_intEv+0x64)[0x55ed22a8aff0]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x55ed21d27b72]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x112)[0x55ed22a84c58]
   > /usr/local/mysql/bin/mysqld(+0x2312a5c)[0x55ed227aea5c]
   > /usr/local/mysql/bin/mysqld(+0x2312c5c)[0x55ed227aec5c]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x13d)[0x55ed22ca4b61]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0xd4f)[0x55ed22c7b2d1]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x3ab)[0x55ed22c80ed9]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0x2b0)[0x55ed226b8e02]
   > /usr/local/mysql/bin/mysqld(+0x1d686ad)[0x55ed222046ad]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x596e)[0x55ed221e014a]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN8optimizeEv+0x424)[0x55ed221d90ce]
   > /usr/local/mysql/bin/mysqld(_ZN13st_select_lex31optimize_unflattened_subqueriesEb+0x5a9)[0x55ed2205f875]
   > sql/item.h:1779(Item::val_int_result())[0x55ed226b2fcb]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x55ed221e67b9]
   > sql/item.h:7099(Item_cache::has_value())[0x55ed221e045b]
   > sql/item.h:7108(Item_cache::is_null())[0x55ed221d90ce]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x55ed221fadad]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x55ed221ca9c1]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x55ed220ec656]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x55ed220dae57]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x55ed220f7a28]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x55ed220cd4af]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x55ed220ca1c2]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x55ed2258d90e]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x55ed2258d1b8]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x55ed231da51a]
   > ??:0(pthread_condattr_setpshared)[0x7f8e37442ac3]
   > ??:0(__xmknodat)[0x7f8e374d4850]
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
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
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
   > 240704 13:21:40 [ERROR] mysqld got signal 6 ;
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
   > stack_bottom = 0x7f81893feab0 thread_stack 0x100000
   > /lib/x86_64-linux-gnu/libasan.so.6(+0x45c0e)[0x7f81a7ae2c0e]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x55923a2d0c8f]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x559238e61b8d]
   > ??:0(__sigaction)[0x7f81a6e7b520]
   > ??:0(pthread_kill)[0x7f81a6ecf9fc]
   > ??:0(raise)[0x7f81a6e7b476]
   > ??:0(abort)[0x7f81a6e617f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7f81a6e6171b]
   > ??:0(__assert_fail)[0x7f81a6e72e96]
   > /usr/local/mysql/bin/mysqld(_ZN16Item_type_holder7val_intEv+0x64)[0x559238f17ff0]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x5592381b4b72]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x112)[0x559238f11c58]
   > /usr/local/mysql/bin/mysqld(+0x2312a5c)[0x559238c3ba5c]
   > /usr/local/mysql/bin/mysqld(+0x2312c5c)[0x559238c3bc5c]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x13d)[0x559239131b61]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0xd4f)[0x5592391082d1]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x3ab)[0x55923910ded9]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0x2b0)[0x559238b45e02]
   > /usr/local/mysql/bin/mysqld(+0x1d686ad)[0x5592386916ad]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x596e)[0x55923866d14a]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN8optimizeEv+0x424)[0x5592386660ce]
   > /usr/local/mysql/bin/mysqld(_ZN13st_select_lex31optimize_unflattened_subqueriesEb+0x5a9)[0x5592384ec875]
   > sql/item.h:1779(Item::val_int_result())[0x559238b3ffcb]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x5592386737b9]
   > sql/item.h:7099(Item_cache::has_value())[0x55923866d45b]
   > sql/item.h:7108(Item_cache::is_null())[0x5592386660ce]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x559238687dad]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x5592386579c1]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x559238579656]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x559238567e57]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x559238584a28]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x55923855a4af]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x5592385571c2]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x559238a1a90e]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x559238a1a1b8]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x55923966751a]
   > ??:0(pthread_condattr_setpshared)[0x7f81a6ecdac3]
   > ??:0(__xmknodat)[0x7f81a6f5f850]
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
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
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
   > 240704 13:21:53 [ERROR] mysqld got signal 6 ;
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
   > stack_bottom = 0x7fa55b9feab0 thread_stack 0x100000
   > /lib/x86_64-linux-gnu/libasan.so.6(+0x45c0e)[0x7fa57a13ac0e]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x55cedb7b8c8f]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x55ceda349b8d]
   > ??:0(__sigaction)[0x7fa5794d3520]
   > ??:0(pthread_kill)[0x7fa5795279fc]
   > ??:0(raise)[0x7fa5794d3476]
   > ??:0(abort)[0x7fa5794b97f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7fa5794b971b]
   > ??:0(__assert_fail)[0x7fa5794cae96]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x55ceda3ffff0]
   > /usr/local/mysql/bin/mysqld(+0x188bb72)[0x55ced969cb72]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x112)[0x55ceda3f9c58]
   > /usr/local/mysql/bin/mysqld(+0x2312a5c)[0x55ceda123a5c]
   > /usr/local/mysql/bin/mysqld(+0x2312c5c)[0x55ceda123c5c]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x13d)[0x55ceda619b61]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0xd4f)[0x55ceda5f02d1]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x3ab)[0x55ceda5f5ed9]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0x2b0)[0x55ceda02de02]
   > /usr/local/mysql/bin/mysqld(+0x1d686ad)[0x55ced9b796ad]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x596e)[0x55ced9b5514a]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN8optimizeEv+0x424)[0x55ced9b4e0ce]
   > sql/item.h:1779(Item::val_int_result())[0x55ced99d4875]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x55ceda027fcb]
   > sql/item.h:7099(Item_cache::has_value())[0x55ced9b5b7b9]
   > sql/item.h:7108(Item_cache::is_null())[0x55ced9b5545b]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x55ced9b4e0ce]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x55ced9b6fdad]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x55ced9b3f9c1]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x55ced9a61656]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x55ced9a4fe57]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x55ced9a6ca28]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x55ced9a424af]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x55ced9a3f1c2]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x55ced9f0290e]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x55ced9f021b8]
   > sql/sql_select.cc:2550(JOIN::optimize_inner())[0x55cedab4f51a]
   > ??:0(pthread_condattr_setpshared)[0x7fa579525ac3]
   > ??:0(__xmknodat)[0x7fa5795b7850]
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
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
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
   > 240704 13:22:07 [ERROR] mysqld got signal 6 ;
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
   > stack_bottom = 0x7feb6e1feab0 thread_stack 0x100000
   > /lib/x86_64-linux-gnu/libasan.so.6(+0x45c0e)[0x7feb8c8a8c0e]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x55995efa1c8f]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x55995db32b8d]
   > ??:0(__sigaction)[0x7feb8bc41520]
   > ??:0(pthread_kill)[0x7feb8bc959fc]
   > ??:0(raise)[0x7feb8bc41476]
   > ??:0(abort)[0x7feb8bc277f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7feb8bc2771b]
   > ??:0(__assert_fail)[0x7feb8bc38e96]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x55995dbe8ff0]
   > /usr/local/mysql/bin/mysqld(+0x188bb72)[0x55995ce85b72]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x112)[0x55995dbe2c58]
   > /usr/local/mysql/bin/mysqld(+0x2312a5c)[0x55995d90ca5c]
   > /usr/local/mysql/bin/mysqld(+0x2312c5c)[0x55995d90cc5c]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x13d)[0x55995de02b61]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0xd4f)[0x55995ddd92d1]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x3ab)[0x55995dddeed9]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0x2b0)[0x55995d816e02]
   > /usr/local/mysql/bin/mysqld(+0x1d686ad)[0x55995d3626ad]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x596e)[0x55995d33e14a]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN8optimizeEv+0x424)[0x55995d3370ce]
   > sql/item.h:1779(Item::val_int_result())[0x55995d1bd875]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x55995d810fcb]
   > sql/item.h:7099(Item_cache::has_value())[0x55995d3447b9]
   > sql/item.h:7108(Item_cache::is_null())[0x55995d33e45b]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x55995d3370ce]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x55995d358dad]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x55995d3289c1]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x55995d24a656]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x55995d238e57]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x55995d255a28]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x55995d22b4af]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x55995d2281c2]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x55995d6eb90e]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x55995d6eb1b8]
   > sql/sql_select.cc:2550(JOIN::optimize_inner())[0x55995e33851a]
   > ??:0(pthread_condattr_setpshared)[0x7feb8bc93ac3]
   > ??:0(__xmknodat)[0x7feb8bd25850]
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
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
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
   > 240704 13:22:20 [ERROR] mysqld got signal 6 ;
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
   > stack_bottom = 0x7f9c737feab0 thread_stack 0x100000
   > /lib/x86_64-linux-gnu/libasan.so.6(+0x45c0e)[0x7f9c9164fc0e]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x556b76cf1c8f]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x556b75882b8d]
   > ??:0(__sigaction)[0x7f9c909e8520]
   > ??:0(pthread_kill)[0x7f9c90a3c9fc]
   > ??:0(raise)[0x7f9c909e8476]
   > ??:0(abort)[0x7f9c909ce7f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7f9c909ce71b]
   > ??:0(__assert_fail)[0x7f9c909dfe96]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x556b75938ff0]
   > /usr/local/mysql/bin/mysqld(+0x188bb72)[0x556b74bd5b72]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x112)[0x556b75932c58]
   > /usr/local/mysql/bin/mysqld(+0x2312a5c)[0x556b7565ca5c]
   > /usr/local/mysql/bin/mysqld(+0x2312c5c)[0x556b7565cc5c]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x13d)[0x556b75b52b61]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0xd4f)[0x556b75b292d1]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x3ab)[0x556b75b2eed9]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0x2b0)[0x556b75566e02]
   > /usr/local/mysql/bin/mysqld(+0x1d686ad)[0x556b750b26ad]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x596e)[0x556b7508e14a]
   > sql/item.h:1779(Item::val_int_result())[0x556b750870ce]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x556b74f0d875]
   > sql/item.h:7099(Item_cache::has_value())[0x556b75560fcb]
   > sql/item.h:7108(Item_cache::is_null())[0x556b750947b9]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x556b7508e45b]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x556b750870ce]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x556b750a8dad]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x556b750789c1]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x556b74f9a656]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x556b74f88e57]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x556b74fa5a28]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x556b74f7b4af]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x556b74f781c2]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x556b7543b90e]
   > sql/sql_select.cc:2550(JOIN::optimize_inner())[0x556b7543b1b8]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x556b7608851a]
   > ??:0(pthread_condattr_setpshared)[0x7f9c90a3aac3]
   > ??:0(__xmknodat)[0x7f9c90acc850]
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
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
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
   > 240704 13:22:33 [ERROR] mysqld got signal 6 ;
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
   > stack_bottom = 0x7f7d5affeab0 thread_stack 0x100000
   > /lib/x86_64-linux-gnu/libasan.so.6(+0x45c0e)[0x7f7d79834c0e]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x557eb668bc8f]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x557eb521cb8d]
   > ??:0(__sigaction)[0x7f7d78bcd520]
   > ??:0(pthread_kill)[0x7f7d78c219fc]
   > ??:0(raise)[0x7f7d78bcd476]
   > ??:0(abort)[0x7f7d78bb37f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7f7d78bb371b]
   > ??:0(__assert_fail)[0x7f7d78bc4e96]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x557eb52d2ff0]
   > /usr/local/mysql/bin/mysqld(+0x188bb72)[0x557eb456fb72]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x112)[0x557eb52ccc58]
   > /usr/local/mysql/bin/mysqld(+0x2312a5c)[0x557eb4ff6a5c]
   > /usr/local/mysql/bin/mysqld(+0x2312c5c)[0x557eb4ff6c5c]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x13d)[0x557eb54ecb61]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0xd4f)[0x557eb54c32d1]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x3ab)[0x557eb54c8ed9]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0x2b0)[0x557eb4f00e02]
   > /usr/local/mysql/bin/mysqld(+0x1d686ad)[0x557eb4a4c6ad]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x596e)[0x557eb4a2814a]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN8optimizeEv+0x424)[0x557eb4a210ce]
   > sql/item.h:1779(Item::val_int_result())[0x557eb48a7875]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x557eb4efafcb]
   > sql/item.h:7099(Item_cache::has_value())[0x557eb4a2e7b9]
   > sql/item.h:7108(Item_cache::is_null())[0x557eb4a2845b]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x557eb4a210ce]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x557eb4a42dad]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x557eb4a129c1]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x557eb4934656]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x557eb4922e57]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x557eb493fa28]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x557eb49154af]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x557eb49121c2]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x557eb4dd590e]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x557eb4dd51b8]
   > sql/sql_select.cc:2550(JOIN::optimize_inner())[0x557eb5a2251a]
   > ??:0(pthread_condattr_setpshared)[0x7f7d78c1fac3]
   > ??:0(__xmknodat)[0x7f7d78cb1850]
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
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
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
   > 240704 13:22:46 [ERROR] mysqld got signal 6 ;
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
   > stack_bottom = 0x7efe6bdfeab0 thread_stack 0x100000
   > /lib/x86_64-linux-gnu/libasan.so.6(+0x45c0e)[0x7efe8a5d8c0e]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x55b00cb2dc8f]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x55b00b6beb8d]
   > ??:0(__sigaction)[0x7efe89971520]
   > ??:0(pthread_kill)[0x7efe899c59fc]
   > ??:0(raise)[0x7efe89971476]
   > ??:0(abort)[0x7efe899577f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7efe8995771b]
   > ??:0(__assert_fail)[0x7efe89968e96]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x55b00b774ff0]
   > /usr/local/mysql/bin/mysqld(+0x188bb72)[0x55b00aa11b72]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x112)[0x55b00b76ec58]
   > /usr/local/mysql/bin/mysqld(+0x2312a5c)[0x55b00b498a5c]
   > /usr/local/mysql/bin/mysqld(+0x2312c5c)[0x55b00b498c5c]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x13d)[0x55b00b98eb61]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0xd4f)[0x55b00b9652d1]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x3ab)[0x55b00b96aed9]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0x2b0)[0x55b00b3a2e02]
   > /usr/local/mysql/bin/mysqld(+0x1d686ad)[0x55b00aeee6ad]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x596e)[0x55b00aeca14a]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN8optimizeEv+0x424)[0x55b00aec30ce]
   > sql/item.h:1779(Item::val_int_result())[0x55b00ad49875]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x55b00b39cfcb]
   > sql/item.h:7099(Item_cache::has_value())[0x55b00aed07b9]
   > sql/item.h:7108(Item_cache::is_null())[0x55b00aeca45b]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x55b00aec30ce]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x55b00aee4dad]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x55b00aeb49c1]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x55b00add6656]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x55b00adc4e57]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x55b00ade1a28]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x55b00adb74af]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x55b00adb41c2]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x55b00b27790e]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x55b00b2771b8]
   > sql/sql_select.cc:2550(JOIN::optimize_inner())[0x55b00bec451a]
   > ??:0(pthread_condattr_setpshared)[0x7efe899c3ac3]
   > ??:0(__xmknodat)[0x7efe89a55850]
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
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
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
   > 240704 13:22:58 [ERROR] mysqld got signal 6 ;
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
   > stack_bottom = 0x7fd56e1feab0 thread_stack 0x100000
   > /lib/x86_64-linux-gnu/libasan.so.6(+0x45c0e)[0x7fd58c938c0e]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x562b5e52ac8f]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x562b5d0bbb8d]
   > ??:0(__sigaction)[0x7fd58bcd1520]
   > ??:0(pthread_kill)[0x7fd58bd259fc]
   > ??:0(raise)[0x7fd58bcd1476]
   > ??:0(abort)[0x7fd58bcb77f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7fd58bcb771b]
   > ??:0(__assert_fail)[0x7fd58bcc8e96]
   > /usr/local/mysql/bin/mysqld(_ZN16Item_type_holder7val_intEv+0x64)[0x562b5d171ff0]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x562b5c40eb72]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x112)[0x562b5d16bc58]
   > /usr/local/mysql/bin/mysqld(+0x2312a5c)[0x562b5ce95a5c]
   > /usr/local/mysql/bin/mysqld(+0x2312c5c)[0x562b5ce95c5c]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x13d)[0x562b5d38bb61]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0xd4f)[0x562b5d3622d1]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x3ab)[0x562b5d367ed9]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0x2b0)[0x562b5cd9fe02]
   > /usr/local/mysql/bin/mysqld(+0x1d686ad)[0x562b5c8eb6ad]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x596e)[0x562b5c8c714a]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN8optimizeEv+0x424)[0x562b5c8c00ce]
   > sql/item.h:1779(Item::val_int_result())[0x562b5c746875]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x562b5cd99fcb]
   > sql/item.h:7099(Item_cache::has_value())[0x562b5c8cd7b9]
   > sql/item.h:7108(Item_cache::is_null())[0x562b5c8c745b]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x562b5c8c00ce]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x562b5c8e1dad]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x562b5c8b19c1]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x562b5c7d3656]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x562b5c7c1e57]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x562b5c7dea28]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x562b5c7b44af]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x562b5c7b11c2]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x562b5cc7490e]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x562b5cc741b8]
   > sql/sql_select.cc:2550(JOIN::optimize_inner())[0x562b5d8c151a]
   > ??:0(pthread_condattr_setpshared)[0x7fd58bd23ac3]
   > ??:0(__xmknodat)[0x7fd58bdb5850]
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
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
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
   > 240704 13:23:11 [ERROR] mysqld got signal 6 ;
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
   > stack_bottom = 0x7fa6bfdfeab0 thread_stack 0x100000
   > /lib/x86_64-linux-gnu/libasan.so.6(+0x45c0e)[0x7fa6de5d7c0e]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x56153946ac8f]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x561537ffbb8d]
   > ??:0(__sigaction)[0x7fa6dd970520]
   > ??:0(pthread_kill)[0x7fa6dd9c49fc]
   > ??:0(raise)[0x7fa6dd970476]
   > ??:0(abort)[0x7fa6dd9567f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7fa6dd95671b]
   > ??:0(__assert_fail)[0x7fa6dd967e96]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x5615380b1ff0]
   > /usr/local/mysql/bin/mysqld(+0x188bb72)[0x56153734eb72]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x112)[0x5615380abc58]
   > /usr/local/mysql/bin/mysqld(+0x2312a5c)[0x561537dd5a5c]
   > /usr/local/mysql/bin/mysqld(+0x2312c5c)[0x561537dd5c5c]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x13d)[0x5615382cbb61]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0xd4f)[0x5615382a22d1]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x3ab)[0x5615382a7ed9]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0x2b0)[0x561537cdfe02]
   > /usr/local/mysql/bin/mysqld(+0x1d686ad)[0x56153782b6ad]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x596e)[0x56153780714a]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN8optimizeEv+0x424)[0x5615378000ce]
   > sql/item.h:1779(Item::val_int_result())[0x561537686875]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x561537cd9fcb]
   > sql/item.h:7099(Item_cache::has_value())[0x56153780d7b9]
   > sql/item.h:7108(Item_cache::is_null())[0x56153780745b]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x5615378000ce]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x561537821dad]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x5615377f19c1]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x561537713656]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x561537701e57]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x56153771ea28]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x5615376f44af]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x5615376f11c2]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x561537bb490e]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x561537bb41b8]
   > sql/sql_select.cc:2550(JOIN::optimize_inner())[0x56153880151a]
   > ??:0(pthread_condattr_setpshared)[0x7fa6dd9c2ac3]
   > ??:0(__xmknodat)[0x7fa6dda54850]
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
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
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
   > 240704 13:23:24 [ERROR] mysqld got signal 6 ;
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
   > stack_bottom = 0x7f95227feab0 thread_stack 0x100000
   > /lib/x86_64-linux-gnu/libasan.so.6(+0x45c0e)[0x7f9540fefc0e]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x55e8691b8c8f]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x55e867d49b8d]
   > ??:0(__sigaction)[0x7f9540388520]
   > ??:0(pthread_kill)[0x7f95403dc9fc]
   > ??:0(raise)[0x7f9540388476]
   > ??:0(abort)[0x7f954036e7f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7f954036e71b]
   > ??:0(__assert_fail)[0x7f954037fe96]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x55e867dffff0]
   > /usr/local/mysql/bin/mysqld(+0x188bb72)[0x55e86709cb72]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x112)[0x55e867df9c58]
   > /usr/local/mysql/bin/mysqld(+0x2312a5c)[0x55e867b23a5c]
   > /usr/local/mysql/bin/mysqld(+0x2312c5c)[0x55e867b23c5c]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x13d)[0x55e868019b61]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0xd4f)[0x55e867ff02d1]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x3ab)[0x55e867ff5ed9]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0x2b0)[0x55e867a2de02]
   > /usr/local/mysql/bin/mysqld(+0x1d686ad)[0x55e8675796ad]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x596e)[0x55e86755514a]
   > sql/item.h:1779(Item::val_int_result())[0x55e86754e0ce]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x55e8673d4875]
   > sql/item.h:7099(Item_cache::has_value())[0x55e867a27fcb]
   > sql/item.h:7108(Item_cache::is_null())[0x55e86755b7b9]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x55e86755545b]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x55e86754e0ce]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x55e86756fdad]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x55e86753f9c1]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x55e867461656]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x55e86744fe57]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x55e86746ca28]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x55e8674424af]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x55e86743f1c2]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x55e86790290e]
   > sql/sql_select.cc:2550(JOIN::optimize_inner())[0x55e8679021b8]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x55e86854f51a]
   > ??:0(pthread_condattr_setpshared)[0x7f95403daac3]
   > ??:0(__xmknodat)[0x7f954046c850]
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
