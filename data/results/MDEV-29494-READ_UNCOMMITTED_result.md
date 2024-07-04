# Bug ID MDEV-29494-READ_UNCOMMITTED

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-29494
Original isolation level: REPEATABLE READ
Tested isolation level:   READ UNCOMMITTED
Description:              The server should crash.


## Details
 * Database: mariadb-10.10.1
 * Number of scenarios: 10
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
   > 240704 13:23:37 [ERROR] mysqld got signal 6 ;
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
   > stack_bottom = 0x7fd8481feab0 thread_stack 0x100000
   > /lib/x86_64-linux-gnu/libasan.so.6(+0x45c0e)[0x7fd86691bc0e]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x56119af96c8f]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x561199b27b8d]
   > ??:0(__sigaction)[0x7fd865cb4520]
   > ??:0(pthread_kill)[0x7fd865d089fc]
   > ??:0(raise)[0x7fd865cb4476]
   > ??:0(abort)[0x7fd865c9a7f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7fd865c9a71b]
   > ??:0(__assert_fail)[0x7fd865cabe96]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x561199bddff0]
   > /usr/local/mysql/bin/mysqld(+0x188bb72)[0x561198e7ab72]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x112)[0x561199bd7c58]
   > /usr/local/mysql/bin/mysqld(+0x2312a5c)[0x561199901a5c]
   > /usr/local/mysql/bin/mysqld(+0x2312c5c)[0x561199901c5c]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x13d)[0x561199df7b61]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0xd4f)[0x561199dce2d1]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x3ab)[0x561199dd3ed9]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0x2b0)[0x56119980be02]
   > /usr/local/mysql/bin/mysqld(+0x1d686ad)[0x5611993576ad]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x596e)[0x56119933314a]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN8optimizeEv+0x424)[0x56119932c0ce]
   > sql/item.h:1779(Item::val_int_result())[0x5611991b2875]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x561199805fcb]
   > sql/item.h:7099(Item_cache::has_value())[0x5611993397b9]
   > sql/item.h:7108(Item_cache::is_null())[0x56119933345b]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x56119932c0ce]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x56119934ddad]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x56119931d9c1]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x56119923f656]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x56119922de57]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x56119924aa28]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x5611992204af]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x56119921d1c2]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x5611996e090e]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x5611996e01b8]
   > sql/sql_select.cc:2550(JOIN::optimize_inner())[0x56119a32d51a]
   > ??:0(pthread_condattr_setpshared)[0x7fd865d06ac3]
   > ??:0(__xmknodat)[0x7fd865d98850]
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
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
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
   > 240704 13:23:50 [ERROR] mysqld got signal 6 ;
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
   > stack_bottom = 0x7fbc2bffeab0 thread_stack 0x100000
   > /lib/x86_64-linux-gnu/libasan.so.6(+0x45c0e)[0x7fbc4a6b0c0e]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x5621e19fec8f]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x5621e058fb8d]
   > ??:0(__sigaction)[0x7fbc49a49520]
   > ??:0(pthread_kill)[0x7fbc49a9d9fc]
   > ??:0(raise)[0x7fbc49a49476]
   > ??:0(abort)[0x7fbc49a2f7f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7fbc49a2f71b]
   > ??:0(__assert_fail)[0x7fbc49a40e96]
   > /usr/local/mysql/bin/mysqld(_ZN16Item_type_holder7val_intEv+0x64)[0x5621e0645ff0]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x5621df8e2b72]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x112)[0x5621e063fc58]
   > /usr/local/mysql/bin/mysqld(+0x2312a5c)[0x5621e0369a5c]
   > /usr/local/mysql/bin/mysqld(+0x2312c5c)[0x5621e0369c5c]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x13d)[0x5621e085fb61]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0xd4f)[0x5621e08362d1]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x3ab)[0x5621e083bed9]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0x2b0)[0x5621e0273e02]
   > /usr/local/mysql/bin/mysqld(+0x1d686ad)[0x5621dfdbf6ad]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x596e)[0x5621dfd9b14a]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN8optimizeEv+0x424)[0x5621dfd940ce]
   > /usr/local/mysql/bin/mysqld(_ZN13st_select_lex31optimize_unflattened_subqueriesEb+0x5a9)[0x5621dfc1a875]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN31optimize_unflattened_subqueriesEv+0x4f)[0x5621e026dfcb]
   > sql/item.h:1779(Item::val_int_result())[0x5621dfda17b9]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x5621dfd9b45b]
   > sql/item.h:7099(Item_cache::has_value())[0x5621dfd940ce]
   > sql/item.h:7108(Item_cache::is_null())[0x5621dfdb5dad]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x5621dfd859c1]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x5621dfca7656]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x5621dfc95e57]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x5621dfcb2a28]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x5621dfc884af]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x5621dfc851c2]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x5621e014890e]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x5621e01481b8]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x5621e0d9551a]
   > ??:0(pthread_condattr_setpshared)[0x7fbc49a9bac3]
   > ??:0(__xmknodat)[0x7fbc49b2d850]
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
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
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
   > 240704 13:24:03 [ERROR] mysqld got signal 6 ;
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
   > stack_bottom = 0x7f9eb2ffeab0 thread_stack 0x100000
   > /lib/x86_64-linux-gnu/libasan.so.6(+0x45c0e)[0x7f9ed16bfc0e]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x560df16a8c8f]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x560df0239b8d]
   > ??:0(__sigaction)[0x7f9ed0a58520]
   > ??:0(pthread_kill)[0x7f9ed0aac9fc]
   > ??:0(raise)[0x7f9ed0a58476]
   > ??:0(abort)[0x7f9ed0a3e7f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7f9ed0a3e71b]
   > ??:0(__assert_fail)[0x7f9ed0a4fe96]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x560df02efff0]
   > /usr/local/mysql/bin/mysqld(+0x188bb72)[0x560def58cb72]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x112)[0x560df02e9c58]
   > /usr/local/mysql/bin/mysqld(+0x2312a5c)[0x560df0013a5c]
   > /usr/local/mysql/bin/mysqld(+0x2312c5c)[0x560df0013c5c]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x13d)[0x560df0509b61]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0xd4f)[0x560df04e02d1]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x3ab)[0x560df04e5ed9]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0x2b0)[0x560deff1de02]
   > /usr/local/mysql/bin/mysqld(+0x1d686ad)[0x560defa696ad]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x596e)[0x560defa4514a]
   > sql/item.h:1779(Item::val_int_result())[0x560defa3e0ce]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x560def8c4875]
   > sql/item.h:7099(Item_cache::has_value())[0x560deff17fcb]
   > sql/item.h:7108(Item_cache::is_null())[0x560defa4b7b9]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x560defa4545b]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x560defa3e0ce]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x560defa5fdad]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x560defa2f9c1]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x560def951656]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x560def93fe57]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x560def95ca28]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x560def9324af]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x560def92f1c2]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x560defdf290e]
   > sql/sql_select.cc:2550(JOIN::optimize_inner())[0x560defdf21b8]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x560df0a3f51a]
   > ??:0(pthread_condattr_setpshared)[0x7f9ed0aaaac3]
   > ??:0(__xmknodat)[0x7f9ed0b3c850]
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
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
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
   > 240704 13:24:15 [ERROR] mysqld got signal 6 ;
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
   > stack_bottom = 0x7f427a3feab0 thread_stack 0x100000
   > /lib/x86_64-linux-gnu/libasan.so.6(+0x45c0e)[0x7f4298a59c0e]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x558906acdc8f]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x55890565eb8d]
   > ??:0(__sigaction)[0x7f4297df2520]
   > ??:0(pthread_kill)[0x7f4297e469fc]
   > ??:0(raise)[0x7f4297df2476]
   > ??:0(abort)[0x7f4297dd87f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7f4297dd871b]
   > ??:0(__assert_fail)[0x7f4297de9e96]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x558905714ff0]
   > /usr/local/mysql/bin/mysqld(+0x188bb72)[0x5589049b1b72]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x112)[0x55890570ec58]
   > /usr/local/mysql/bin/mysqld(+0x2312a5c)[0x558905438a5c]
   > /usr/local/mysql/bin/mysqld(+0x2312c5c)[0x558905438c5c]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x13d)[0x55890592eb61]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0xd4f)[0x5589059052d1]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x3ab)[0x55890590aed9]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0x2b0)[0x558905342e02]
   > /usr/local/mysql/bin/mysqld(+0x1d686ad)[0x558904e8e6ad]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x596e)[0x558904e6a14a]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN8optimizeEv+0x424)[0x558904e630ce]
   > sql/item.h:1779(Item::val_int_result())[0x558904ce9875]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x55890533cfcb]
   > sql/item.h:7099(Item_cache::has_value())[0x558904e707b9]
   > sql/item.h:7108(Item_cache::is_null())[0x558904e6a45b]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x558904e630ce]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x558904e84dad]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x558904e549c1]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x558904d76656]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x558904d64e57]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x558904d81a28]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x558904d574af]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x558904d541c2]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x55890521790e]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x5589052171b8]
   > sql/sql_select.cc:2550(JOIN::optimize_inner())[0x558905e6451a]
   > ??:0(pthread_condattr_setpshared)[0x7f4297e44ac3]
   > ??:0(__xmknodat)[0x7f4297ed6850]
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
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
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
   > 240704 13:24:28 [ERROR] mysqld got signal 6 ;
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
   > stack_bottom = 0x7fc156bfeab0 thread_stack 0x100000
   > /lib/x86_64-linux-gnu/libasan.so.6(+0x45c0e)[0x7fc1752c0c0e]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x55f05ccb7c8f]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x55f05b848b8d]
   > ??:0(__sigaction)[0x7fc174659520]
   > ??:0(pthread_kill)[0x7fc1746ad9fc]
   > ??:0(raise)[0x7fc174659476]
   > ??:0(abort)[0x7fc17463f7f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7fc17463f71b]
   > ??:0(__assert_fail)[0x7fc174650e96]
   > /usr/local/mysql/bin/mysqld(_ZN16Item_type_holder7val_intEv+0x64)[0x55f05b8feff0]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x55f05ab9bb72]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x112)[0x55f05b8f8c58]
   > /usr/local/mysql/bin/mysqld(+0x2312a5c)[0x55f05b622a5c]
   > /usr/local/mysql/bin/mysqld(+0x2312c5c)[0x55f05b622c5c]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x13d)[0x55f05bb18b61]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0xd4f)[0x55f05baef2d1]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x3ab)[0x55f05baf4ed9]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0x2b0)[0x55f05b52ce02]
   > /usr/local/mysql/bin/mysqld(+0x1d686ad)[0x55f05b0786ad]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x596e)[0x55f05b05414a]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN8optimizeEv+0x424)[0x55f05b04d0ce]
   > /usr/local/mysql/bin/mysqld(_ZN13st_select_lex31optimize_unflattened_subqueriesEb+0x5a9)[0x55f05aed3875]
   > sql/item.h:1779(Item::val_int_result())[0x55f05b526fcb]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x55f05b05a7b9]
   > sql/item.h:7099(Item_cache::has_value())[0x55f05b05445b]
   > sql/item.h:7108(Item_cache::is_null())[0x55f05b04d0ce]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x55f05b06edad]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x55f05b03e9c1]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x55f05af60656]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x55f05af4ee57]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x55f05af6ba28]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x55f05af414af]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x55f05af3e1c2]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x55f05b40190e]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x55f05b4011b8]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x55f05c04e51a]
   > ??:0(pthread_condattr_setpshared)[0x7fc1746abac3]
   > ??:0(__xmknodat)[0x7fc17473d850]
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
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
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
   > 240704 13:24:41 [ERROR] mysqld got signal 6 ;
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
   > stack_bottom = 0x7fdfc59feab0 thread_stack 0x100000
   > /lib/x86_64-linux-gnu/libasan.so.6(+0x45c0e)[0x7fdfe4213c0e]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x563e8cd61c8f]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x563e8b8f2b8d]
   > ??:0(__sigaction)[0x7fdfe35ac520]
   > ??:0(pthread_kill)[0x7fdfe36009fc]
   > ??:0(raise)[0x7fdfe35ac476]
   > ??:0(abort)[0x7fdfe35927f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7fdfe359271b]
   > ??:0(__assert_fail)[0x7fdfe35a3e96]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x563e8b9a8ff0]
   > /usr/local/mysql/bin/mysqld(+0x188bb72)[0x563e8ac45b72]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x112)[0x563e8b9a2c58]
   > /usr/local/mysql/bin/mysqld(+0x2312a5c)[0x563e8b6cca5c]
   > /usr/local/mysql/bin/mysqld(+0x2312c5c)[0x563e8b6ccc5c]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x13d)[0x563e8bbc2b61]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0xd4f)[0x563e8bb992d1]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x3ab)[0x563e8bb9eed9]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0x2b0)[0x563e8b5d6e02]
   > /usr/local/mysql/bin/mysqld(+0x1d686ad)[0x563e8b1226ad]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x596e)[0x563e8b0fe14a]
   > sql/item.h:1779(Item::val_int_result())[0x563e8b0f70ce]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x563e8af7d875]
   > sql/item.h:7099(Item_cache::has_value())[0x563e8b5d0fcb]
   > sql/item.h:7108(Item_cache::is_null())[0x563e8b1047b9]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x563e8b0fe45b]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x563e8b0f70ce]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x563e8b118dad]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x563e8b0e89c1]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x563e8b00a656]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x563e8aff8e57]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x563e8b015a28]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x563e8afeb4af]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x563e8afe81c2]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x563e8b4ab90e]
   > sql/sql_select.cc:2550(JOIN::optimize_inner())[0x563e8b4ab1b8]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x563e8c0f851a]
   > ??:0(pthread_condattr_setpshared)[0x7fdfe35feac3]
   > ??:0(__xmknodat)[0x7fdfe3690850]
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
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
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
   > 240704 13:24:53 [ERROR] mysqld got signal 6 ;
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
   > stack_bottom = 0x7f0c435feab0 thread_stack 0x100000
   > /lib/x86_64-linux-gnu/libasan.so.6(+0x45c0e)[0x7f0c6143ec0e]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x5634f64a2c8f]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x5634f5033b8d]
   > ??:0(__sigaction)[0x7f0c607d7520]
   > ??:0(pthread_kill)[0x7f0c6082b9fc]
   > ??:0(raise)[0x7f0c607d7476]
   > ??:0(abort)[0x7f0c607bd7f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7f0c607bd71b]
   > ??:0(__assert_fail)[0x7f0c607cee96]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x5634f50e9ff0]
   > /usr/local/mysql/bin/mysqld(+0x188bb72)[0x5634f4386b72]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x112)[0x5634f50e3c58]
   > /usr/local/mysql/bin/mysqld(+0x2312a5c)[0x5634f4e0da5c]
   > /usr/local/mysql/bin/mysqld(+0x2312c5c)[0x5634f4e0dc5c]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x13d)[0x5634f5303b61]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0xd4f)[0x5634f52da2d1]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x3ab)[0x5634f52dfed9]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0x2b0)[0x5634f4d17e02]
   > /usr/local/mysql/bin/mysqld(+0x1d686ad)[0x5634f48636ad]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x596e)[0x5634f483f14a]
   > sql/item.h:1779(Item::val_int_result())[0x5634f48380ce]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x5634f46be875]
   > sql/item.h:7099(Item_cache::has_value())[0x5634f4d11fcb]
   > sql/item.h:7108(Item_cache::is_null())[0x5634f48457b9]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x5634f483f45b]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x5634f48380ce]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x5634f4859dad]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x5634f48299c1]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x5634f474b656]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x5634f4739e57]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x5634f4756a28]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x5634f472c4af]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x5634f47291c2]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x5634f4bec90e]
   > sql/sql_select.cc:2550(JOIN::optimize_inner())[0x5634f4bec1b8]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x5634f583951a]
   > ??:0(pthread_condattr_setpshared)[0x7f0c60829ac3]
   > ??:0(__xmknodat)[0x7f0c608bb850]
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
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
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
   > 240704 13:25:05 [ERROR] mysqld got signal 6 ;
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
   > stack_bottom = 0x7f07debfeab0 thread_stack 0x100000
   > /lib/x86_64-linux-gnu/libasan.so.6(+0x45c0e)[0x7f07fd2c7c0e]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x55c6b64d7c8f]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x55c6b5068b8d]
   > ??:0(__sigaction)[0x7f07fc660520]
   > ??:0(pthread_kill)[0x7f07fc6b49fc]
   > ??:0(raise)[0x7f07fc660476]
   > ??:0(abort)[0x7f07fc6467f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7f07fc64671b]
   > ??:0(__assert_fail)[0x7f07fc657e96]
   > /usr/local/mysql/bin/mysqld(_ZN16Item_type_holder7val_intEv+0x64)[0x55c6b511eff0]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x55c6b43bbb72]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x112)[0x55c6b5118c58]
   > /usr/local/mysql/bin/mysqld(+0x2312a5c)[0x55c6b4e42a5c]
   > /usr/local/mysql/bin/mysqld(+0x2312c5c)[0x55c6b4e42c5c]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x13d)[0x55c6b5338b61]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0xd4f)[0x55c6b530f2d1]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x3ab)[0x55c6b5314ed9]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0x2b0)[0x55c6b4d4ce02]
   > /usr/local/mysql/bin/mysqld(+0x1d686ad)[0x55c6b48986ad]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x596e)[0x55c6b487414a]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN8optimizeEv+0x424)[0x55c6b486d0ce]
   > sql/item.h:1779(Item::val_int_result())[0x55c6b46f3875]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x55c6b4d46fcb]
   > sql/item.h:7099(Item_cache::has_value())[0x55c6b487a7b9]
   > sql/item.h:7108(Item_cache::is_null())[0x55c6b487445b]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x55c6b486d0ce]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x55c6b488edad]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x55c6b485e9c1]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x55c6b4780656]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x55c6b476ee57]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x55c6b478ba28]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x55c6b47614af]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x55c6b475e1c2]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x55c6b4c2190e]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x55c6b4c211b8]
   > sql/sql_select.cc:2550(JOIN::optimize_inner())[0x55c6b586e51a]
   > ??:0(pthread_condattr_setpshared)[0x7f07fc6b2ac3]
   > ??:0(__xmknodat)[0x7f07fc744850]
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
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
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
   > 240704 13:25:18 [ERROR] mysqld got signal 6 ;
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
   > stack_bottom = 0x7f7d875feab0 thread_stack 0x100000
   > /lib/x86_64-linux-gnu/libasan.so.6(+0x45c0e)[0x7f7da5cc5c0e]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x56119042ec8f]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x56118efbfb8d]
   > ??:0(__sigaction)[0x7f7da505e520]
   > ??:0(pthread_kill)[0x7f7da50b29fc]
   > ??:0(raise)[0x7f7da505e476]
   > ??:0(abort)[0x7f7da50447f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7f7da504471b]
   > ??:0(__assert_fail)[0x7f7da5055e96]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x56118f075ff0]
   > /usr/local/mysql/bin/mysqld(+0x188bb72)[0x56118e312b72]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x112)[0x56118f06fc58]
   > /usr/local/mysql/bin/mysqld(+0x2312a5c)[0x56118ed99a5c]
   > /usr/local/mysql/bin/mysqld(+0x2312c5c)[0x56118ed99c5c]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x13d)[0x56118f28fb61]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0xd4f)[0x56118f2662d1]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x3ab)[0x56118f26bed9]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0x2b0)[0x56118eca3e02]
   > /usr/local/mysql/bin/mysqld(+0x1d686ad)[0x56118e7ef6ad]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x596e)[0x56118e7cb14a]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN8optimizeEv+0x424)[0x56118e7c40ce]
   > sql/item.h:1779(Item::val_int_result())[0x56118e64a875]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x56118ec9dfcb]
   > sql/item.h:7099(Item_cache::has_value())[0x56118e7d17b9]
   > sql/item.h:7108(Item_cache::is_null())[0x56118e7cb45b]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x56118e7c40ce]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x56118e7e5dad]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x56118e7b59c1]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x56118e6d7656]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x56118e6c5e57]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x56118e6e2a28]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x56118e6b84af]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x56118e6b51c2]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x56118eb7890e]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x56118eb781b8]
   > sql/sql_select.cc:2550(JOIN::optimize_inner())[0x56118f7c551a]
   > ??:0(pthread_condattr_setpshared)[0x7f7da50b0ac3]
   > ??:0(__xmknodat)[0x7f7da5142850]
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
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
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
   > 240704 13:25:31 [ERROR] mysqld got signal 6 ;
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
   > stack_bottom = 0x7fe8a81feab0 thread_stack 0x100000
   > /lib/x86_64-linux-gnu/libasan.so.6(+0x45c0e)[0x7fe8c69bbc0e]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x56089e72fc8f]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x56089d2c0b8d]
   > ??:0(__sigaction)[0x7fe8c5d54520]
   > ??:0(pthread_kill)[0x7fe8c5da89fc]
   > ??:0(raise)[0x7fe8c5d54476]
   > ??:0(abort)[0x7fe8c5d3a7f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7fe8c5d3a71b]
   > ??:0(__assert_fail)[0x7fe8c5d4be96]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x56089d376ff0]
   > /usr/local/mysql/bin/mysqld(+0x188bb72)[0x56089c613b72]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x112)[0x56089d370c58]
   > /usr/local/mysql/bin/mysqld(+0x2312a5c)[0x56089d09aa5c]
   > /usr/local/mysql/bin/mysqld(+0x2312c5c)[0x56089d09ac5c]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x13d)[0x56089d590b61]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0xd4f)[0x56089d5672d1]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x3ab)[0x56089d56ced9]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0x2b0)[0x56089cfa4e02]
   > /usr/local/mysql/bin/mysqld(+0x1d686ad)[0x56089caf06ad]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x596e)[0x56089cacc14a]
   > sql/item.h:1779(Item::val_int_result())[0x56089cac50ce]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x56089c94b875]
   > sql/item.h:7099(Item_cache::has_value())[0x56089cf9efcb]
   > sql/item.h:7108(Item_cache::is_null())[0x56089cad27b9]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x56089cacc45b]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x56089cac50ce]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x56089cae6dad]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x56089cab69c1]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x56089c9d8656]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x56089c9c6e57]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x56089c9e3a28]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x56089c9b94af]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x56089c9b61c2]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x56089ce7990e]
   > sql/sql_select.cc:2550(JOIN::optimize_inner())[0x56089ce791b8]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x56089dac651a]
   > ??:0(pthread_condattr_setpshared)[0x7fe8c5da6ac3]
   > ??:0(__xmknodat)[0x7fe8c5e38850]
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
