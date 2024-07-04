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
   > 240704 13:19:17 [ERROR] mysqld got signal 6 ;
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
   > stack_bottom = 0x7f2ca41feab0 thread_stack 0x100000
   > /lib/x86_64-linux-gnu/libasan.so.6(+0x45c0e)[0x7f2cc2877c0e]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x5590dec26c8f]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x5590dd7b7b8d]
   > ??:0(__sigaction)[0x7f2cc1c10520]
   > ??:0(pthread_kill)[0x7f2cc1c649fc]
   > ??:0(raise)[0x7f2cc1c10476]
   > ??:0(abort)[0x7f2cc1bf67f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7f2cc1bf671b]
   > ??:0(__assert_fail)[0x7f2cc1c07e96]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x5590dd86dff0]
   > /usr/local/mysql/bin/mysqld(+0x188bb72)[0x5590dcb0ab72]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x112)[0x5590dd867c58]
   > /usr/local/mysql/bin/mysqld(+0x2312a5c)[0x5590dd591a5c]
   > /usr/local/mysql/bin/mysqld(+0x2312c5c)[0x5590dd591c5c]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x13d)[0x5590dda87b61]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0xd4f)[0x5590dda5e2d1]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x3ab)[0x5590dda63ed9]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0x2b0)[0x5590dd49be02]
   > /usr/local/mysql/bin/mysqld(+0x1d686ad)[0x5590dcfe76ad]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x596e)[0x5590dcfc314a]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN8optimizeEv+0x424)[0x5590dcfbc0ce]
   > sql/item.h:1779(Item::val_int_result())[0x5590dce42875]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x5590dd495fcb]
   > sql/item.h:7099(Item_cache::has_value())[0x5590dcfc97b9]
   > sql/item.h:7108(Item_cache::is_null())[0x5590dcfc345b]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x5590dcfbc0ce]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x5590dcfdddad]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x5590dcfad9c1]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x5590dcecf656]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x5590dcebde57]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x5590dcedaa28]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x5590dceb04af]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x5590dcead1c2]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x5590dd37090e]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x5590dd3701b8]
   > sql/sql_select.cc:2550(JOIN::optimize_inner())[0x5590ddfbd51a]
   > ??:0(pthread_condattr_setpshared)[0x7f2cc1c62ac3]
   > ??:0(__xmknodat)[0x7f2cc1cf4850]
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
   > 240704 13:19:30 [ERROR] mysqld got signal 6 ;
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
   > stack_bottom = 0x7fc0447feab0 thread_stack 0x100000
   > /lib/x86_64-linux-gnu/libasan.so.6(+0x45c0e)[0x7fc062f86c0e]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x5572b16dcc8f]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x5572b026db8d]
   > ??:0(__sigaction)[0x7fc06231f520]
   > ??:0(pthread_kill)[0x7fc0623739fc]
   > ??:0(raise)[0x7fc06231f476]
   > ??:0(abort)[0x7fc0623057f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7fc06230571b]
   > ??:0(__assert_fail)[0x7fc062316e96]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x5572b0323ff0]
   > /usr/local/mysql/bin/mysqld(+0x188bb72)[0x5572af5c0b72]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x112)[0x5572b031dc58]
   > /usr/local/mysql/bin/mysqld(+0x2312a5c)[0x5572b0047a5c]
   > /usr/local/mysql/bin/mysqld(+0x2312c5c)[0x5572b0047c5c]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x13d)[0x5572b053db61]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0xd4f)[0x5572b05142d1]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x3ab)[0x5572b0519ed9]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0x2b0)[0x5572aff51e02]
   > /usr/local/mysql/bin/mysqld(+0x1d686ad)[0x5572afa9d6ad]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x596e)[0x5572afa7914a]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN8optimizeEv+0x424)[0x5572afa720ce]
   > sql/item.h:1779(Item::val_int_result())[0x5572af8f8875]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x5572aff4bfcb]
   > sql/item.h:7099(Item_cache::has_value())[0x5572afa7f7b9]
   > sql/item.h:7108(Item_cache::is_null())[0x5572afa7945b]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x5572afa720ce]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x5572afa93dad]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x5572afa639c1]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x5572af985656]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x5572af973e57]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x5572af990a28]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x5572af9664af]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x5572af9631c2]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x5572afe2690e]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x5572afe261b8]
   > sql/sql_select.cc:2550(JOIN::optimize_inner())[0x5572b0a7351a]
   > ??:0(pthread_condattr_setpshared)[0x7fc062371ac3]
   > ??:0(__xmknodat)[0x7fc062403850]
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
   > 240704 13:19:43 [ERROR] mysqld got signal 6 ;
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
   > stack_bottom = 0x7f9a6d7feab0 thread_stack 0x100000
   > /lib/x86_64-linux-gnu/libasan.so.6(+0x45c0e)[0x7f9a8b63cc0e]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x55e671e51c8f]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x55e6709e2b8d]
   > ??:0(__sigaction)[0x7f9a8a9d5520]
   > ??:0(pthread_kill)[0x7f9a8aa299fc]
   > ??:0(raise)[0x7f9a8a9d5476]
   > ??:0(abort)[0x7f9a8a9bb7f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7f9a8a9bb71b]
   > ??:0(__assert_fail)[0x7f9a8a9cce96]
   > /usr/local/mysql/bin/mysqld(_ZN16Item_type_holder7val_intEv+0x64)[0x55e670a98ff0]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x55e66fd35b72]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x112)[0x55e670a92c58]
   > /usr/local/mysql/bin/mysqld(+0x2312a5c)[0x55e6707bca5c]
   > /usr/local/mysql/bin/mysqld(+0x2312c5c)[0x55e6707bcc5c]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x13d)[0x55e670cb2b61]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0xd4f)[0x55e670c892d1]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x3ab)[0x55e670c8eed9]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0x2b0)[0x55e6706c6e02]
   > /usr/local/mysql/bin/mysqld(+0x1d686ad)[0x55e6702126ad]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x596e)[0x55e6701ee14a]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN8optimizeEv+0x424)[0x55e6701e70ce]
   > /usr/local/mysql/bin/mysqld(_ZN13st_select_lex31optimize_unflattened_subqueriesEb+0x5a9)[0x55e67006d875]
   > sql/item.h:1779(Item::val_int_result())[0x55e6706c0fcb]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x55e6701f47b9]
   > sql/item.h:7099(Item_cache::has_value())[0x55e6701ee45b]
   > sql/item.h:7108(Item_cache::is_null())[0x55e6701e70ce]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x55e670208dad]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x55e6701d89c1]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x55e6700fa656]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x55e6700e8e57]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x55e670105a28]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x55e6700db4af]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x55e6700d81c2]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x55e67059b90e]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x55e67059b1b8]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x55e6711e851a]
   > ??:0(pthread_condattr_setpshared)[0x7f9a8aa27ac3]
   > ??:0(__xmknodat)[0x7f9a8aab9850]
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
   > 240704 13:19:56 [ERROR] mysqld got signal 6 ;
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
   > stack_bottom = 0x7f6ae81feab0 thread_stack 0x100000
   > /lib/x86_64-linux-gnu/libasan.so.6(+0x45c0e)[0x7f6b06957c0e]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x55a6a715ac8f]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x55a6a5cebb8d]
   > ??:0(__sigaction)[0x7f6b05cf0520]
   > ??:0(pthread_kill)[0x7f6b05d449fc]
   > ??:0(raise)[0x7f6b05cf0476]
   > ??:0(abort)[0x7f6b05cd67f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7f6b05cd671b]
   > ??:0(__assert_fail)[0x7f6b05ce7e96]
   > /usr/local/mysql/bin/mysqld(_ZN16Item_type_holder7val_intEv+0x64)[0x55a6a5da1ff0]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x55a6a503eb72]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x112)[0x55a6a5d9bc58]
   > /usr/local/mysql/bin/mysqld(+0x2312a5c)[0x55a6a5ac5a5c]
   > /usr/local/mysql/bin/mysqld(+0x2312c5c)[0x55a6a5ac5c5c]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x13d)[0x55a6a5fbbb61]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0xd4f)[0x55a6a5f922d1]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x3ab)[0x55a6a5f97ed9]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0x2b0)[0x55a6a59cfe02]
   > /usr/local/mysql/bin/mysqld(+0x1d686ad)[0x55a6a551b6ad]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x596e)[0x55a6a54f714a]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN8optimizeEv+0x424)[0x55a6a54f00ce]
   > /usr/local/mysql/bin/mysqld(_ZN13st_select_lex31optimize_unflattened_subqueriesEb+0x5a9)[0x55a6a5376875]
   > sql/item.h:1779(Item::val_int_result())[0x55a6a59c9fcb]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x55a6a54fd7b9]
   > sql/item.h:7099(Item_cache::has_value())[0x55a6a54f745b]
   > sql/item.h:7108(Item_cache::is_null())[0x55a6a54f00ce]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x55a6a5511dad]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x55a6a54e19c1]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x55a6a5403656]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x55a6a53f1e57]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x55a6a540ea28]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x55a6a53e44af]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x55a6a53e11c2]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x55a6a58a490e]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x55a6a58a41b8]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x55a6a64f151a]
   > ??:0(pthread_condattr_setpshared)[0x7f6b05d42ac3]
   > ??:0(__xmknodat)[0x7f6b05dd4850]
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
   > 240704 13:20:09 [ERROR] mysqld got signal 6 ;
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
   > stack_bottom = 0x7f8ae77feab0 thread_stack 0x100000
   > /lib/x86_64-linux-gnu/libasan.so.6(+0x45c0e)[0x7f8b05e84c0e]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x562da82f5c8f]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x562da6e86b8d]
   > ??:0(__sigaction)[0x7f8b0521d520]
   > ??:0(pthread_kill)[0x7f8b052719fc]
   > ??:0(raise)[0x7f8b0521d476]
   > ??:0(abort)[0x7f8b052037f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7f8b0520371b]
   > ??:0(__assert_fail)[0x7f8b05214e96]
   > /usr/local/mysql/bin/mysqld(_ZN16Item_type_holder7val_intEv+0x64)[0x562da6f3cff0]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x562da61d9b72]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x112)[0x562da6f36c58]
   > /usr/local/mysql/bin/mysqld(+0x2312a5c)[0x562da6c60a5c]
   > /usr/local/mysql/bin/mysqld(+0x2312c5c)[0x562da6c60c5c]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x13d)[0x562da7156b61]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0xd4f)[0x562da712d2d1]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x3ab)[0x562da7132ed9]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0x2b0)[0x562da6b6ae02]
   > /usr/local/mysql/bin/mysqld(+0x1d686ad)[0x562da66b66ad]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x596e)[0x562da669214a]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN8optimizeEv+0x424)[0x562da668b0ce]
   > sql/item.h:1779(Item::val_int_result())[0x562da6511875]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x562da6b64fcb]
   > sql/item.h:7099(Item_cache::has_value())[0x562da66987b9]
   > sql/item.h:7108(Item_cache::is_null())[0x562da669245b]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x562da668b0ce]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x562da66acdad]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x562da667c9c1]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x562da659e656]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x562da658ce57]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x562da65a9a28]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x562da657f4af]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x562da657c1c2]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x562da6a3f90e]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x562da6a3f1b8]
   > sql/sql_select.cc:2550(JOIN::optimize_inner())[0x562da768c51a]
   > ??:0(pthread_condattr_setpshared)[0x7f8b0526fac3]
   > ??:0(__xmknodat)[0x7f8b05301850]
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
   > 240704 13:20:22 [ERROR] mysqld got signal 6 ;
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
   > stack_bottom = 0x7f45bf5feab0 thread_stack 0x100000
   > /lib/x86_64-linux-gnu/libasan.so.6(+0x45c0e)[0x7f45ddcacc0e]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x559d5e7e5c8f]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x559d5d376b8d]
   > ??:0(__sigaction)[0x7f45dd045520]
   > ??:0(pthread_kill)[0x7f45dd0999fc]
   > ??:0(raise)[0x7f45dd045476]
   > ??:0(abort)[0x7f45dd02b7f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7f45dd02b71b]
   > ??:0(__assert_fail)[0x7f45dd03ce96]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x559d5d42cff0]
   > /usr/local/mysql/bin/mysqld(+0x188bb72)[0x559d5c6c9b72]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x112)[0x559d5d426c58]
   > /usr/local/mysql/bin/mysqld(+0x2312a5c)[0x559d5d150a5c]
   > /usr/local/mysql/bin/mysqld(+0x2312c5c)[0x559d5d150c5c]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x13d)[0x559d5d646b61]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0xd4f)[0x559d5d61d2d1]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x3ab)[0x559d5d622ed9]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0x2b0)[0x559d5d05ae02]
   > /usr/local/mysql/bin/mysqld(+0x1d686ad)[0x559d5cba66ad]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x596e)[0x559d5cb8214a]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN8optimizeEv+0x424)[0x559d5cb7b0ce]
   > sql/item.h:1779(Item::val_int_result())[0x559d5ca01875]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x559d5d054fcb]
   > sql/item.h:7099(Item_cache::has_value())[0x559d5cb887b9]
   > sql/item.h:7108(Item_cache::is_null())[0x559d5cb8245b]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x559d5cb7b0ce]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x559d5cb9cdad]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x559d5cb6c9c1]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x559d5ca8e656]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x559d5ca7ce57]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x559d5ca99a28]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x559d5ca6f4af]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x559d5ca6c1c2]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x559d5cf2f90e]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x559d5cf2f1b8]
   > sql/sql_select.cc:2550(JOIN::optimize_inner())[0x559d5db7c51a]
   > ??:0(pthread_condattr_setpshared)[0x7f45dd097ac3]
   > ??:0(__xmknodat)[0x7f45dd129850]
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
   > 240704 13:20:35 [ERROR] mysqld got signal 6 ;
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
   > stack_bottom = 0x7efe949feab0 thread_stack 0x100000
   > /lib/x86_64-linux-gnu/libasan.so.6(+0x45c0e)[0x7efeb31d0c0e]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x5646dff43c8f]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x5646dead4b8d]
   > ??:0(__sigaction)[0x7efeb2569520]
   > ??:0(pthread_kill)[0x7efeb25bd9fc]
   > ??:0(raise)[0x7efeb2569476]
   > ??:0(abort)[0x7efeb254f7f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7efeb254f71b]
   > ??:0(__assert_fail)[0x7efeb2560e96]
   > /usr/local/mysql/bin/mysqld(_ZN16Item_type_holder7val_intEv+0x64)[0x5646deb8aff0]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x5646dde27b72]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x112)[0x5646deb84c58]
   > /usr/local/mysql/bin/mysqld(+0x2312a5c)[0x5646de8aea5c]
   > /usr/local/mysql/bin/mysqld(+0x2312c5c)[0x5646de8aec5c]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x13d)[0x5646deda4b61]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0xd4f)[0x5646ded7b2d1]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x3ab)[0x5646ded80ed9]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0x2b0)[0x5646de7b8e02]
   > /usr/local/mysql/bin/mysqld(+0x1d686ad)[0x5646de3046ad]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x596e)[0x5646de2e014a]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN8optimizeEv+0x424)[0x5646de2d90ce]
   > /usr/local/mysql/bin/mysqld(_ZN13st_select_lex31optimize_unflattened_subqueriesEb+0x5a9)[0x5646de15f875]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN31optimize_unflattened_subqueriesEv+0x4f)[0x5646de7b2fcb]
   > sql/item.h:1779(Item::val_int_result())[0x5646de2e67b9]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x5646de2e045b]
   > sql/item.h:7099(Item_cache::has_value())[0x5646de2d90ce]
   > sql/item.h:7108(Item_cache::is_null())[0x5646de2fadad]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x5646de2ca9c1]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x5646de1ec656]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x5646de1dae57]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x5646de1f7a28]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x5646de1cd4af]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x5646de1ca1c2]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x5646de68d90e]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x5646de68d1b8]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x5646df2da51a]
   > ??:0(pthread_condattr_setpshared)[0x7efeb25bbac3]
   > ??:0(__xmknodat)[0x7efeb264d850]
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
   > 240704 13:20:48 [ERROR] mysqld got signal 6 ;
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
   > stack_bottom = 0x7fb0d3ffeab0 thread_stack 0x100000
   > /lib/x86_64-linux-gnu/libasan.so.6(+0x45c0e)[0x7fb0f26d8c0e]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x5565fa72bc8f]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x5565f92bcb8d]
   > ??:0(__sigaction)[0x7fb0f1a71520]
   > ??:0(pthread_kill)[0x7fb0f1ac59fc]
   > ??:0(raise)[0x7fb0f1a71476]
   > ??:0(abort)[0x7fb0f1a577f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7fb0f1a5771b]
   > ??:0(__assert_fail)[0x7fb0f1a68e96]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x5565f9372ff0]
   > /usr/local/mysql/bin/mysqld(+0x188bb72)[0x5565f860fb72]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x112)[0x5565f936cc58]
   > /usr/local/mysql/bin/mysqld(+0x2312a5c)[0x5565f9096a5c]
   > /usr/local/mysql/bin/mysqld(+0x2312c5c)[0x5565f9096c5c]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x13d)[0x5565f958cb61]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0xd4f)[0x5565f95632d1]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x3ab)[0x5565f9568ed9]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0x2b0)[0x5565f8fa0e02]
   > /usr/local/mysql/bin/mysqld(+0x1d686ad)[0x5565f8aec6ad]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x596e)[0x5565f8ac814a]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN8optimizeEv+0x424)[0x5565f8ac10ce]
   > sql/item.h:1779(Item::val_int_result())[0x5565f8947875]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x5565f8f9afcb]
   > sql/item.h:7099(Item_cache::has_value())[0x5565f8ace7b9]
   > sql/item.h:7108(Item_cache::is_null())[0x5565f8ac845b]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x5565f8ac10ce]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x5565f8ae2dad]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x5565f8ab29c1]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x5565f89d4656]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x5565f89c2e57]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x5565f89dfa28]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x5565f89b54af]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x5565f89b21c2]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x5565f8e7590e]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x5565f8e751b8]
   > sql/sql_select.cc:2550(JOIN::optimize_inner())[0x5565f9ac251a]
   > ??:0(pthread_condattr_setpshared)[0x7fb0f1ac3ac3]
   > ??:0(__xmknodat)[0x7fb0f1b55850]
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
   > 240704 13:21:01 [ERROR] mysqld got signal 6 ;
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
   > stack_bottom = 0x7f80dadfeab0 thread_stack 0x100000
   > /lib/x86_64-linux-gnu/libasan.so.6(+0x45c0e)[0x7f80f95a7c0e]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x5555f1871c8f]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x5555f0402b8d]
   > ??:0(__sigaction)[0x7f80f8940520]
   > ??:0(pthread_kill)[0x7f80f89949fc]
   > ??:0(raise)[0x7f80f8940476]
   > ??:0(abort)[0x7f80f89267f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7f80f892671b]
   > ??:0(__assert_fail)[0x7f80f8937e96]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x5555f04b8ff0]
   > /usr/local/mysql/bin/mysqld(+0x188bb72)[0x5555ef755b72]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x112)[0x5555f04b2c58]
   > /usr/local/mysql/bin/mysqld(+0x2312a5c)[0x5555f01dca5c]
   > /usr/local/mysql/bin/mysqld(+0x2312c5c)[0x5555f01dcc5c]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x13d)[0x5555f06d2b61]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0xd4f)[0x5555f06a92d1]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x3ab)[0x5555f06aeed9]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0x2b0)[0x5555f00e6e02]
   > /usr/local/mysql/bin/mysqld(+0x1d686ad)[0x5555efc326ad]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x596e)[0x5555efc0e14a]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN8optimizeEv+0x424)[0x5555efc070ce]
   > /usr/local/mysql/bin/mysqld(_ZN13st_select_lex31optimize_unflattened_subqueriesEb+0x5a9)[0x5555efa8d875]
   > sql/item.h:1779(Item::val_int_result())[0x5555f00e0fcb]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x5555efc147b9]
   > sql/item.h:7099(Item_cache::has_value())[0x5555efc0e45b]
   > sql/item.h:7108(Item_cache::is_null())[0x5555efc070ce]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x5555efc28dad]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x5555efbf89c1]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x5555efb1a656]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x5555efb08e57]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x5555efb25a28]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x5555efafb4af]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x5555efaf81c2]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x5555effbb90e]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x5555effbb1b8]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x5555f0c0851a]
   > ??:0(pthread_condattr_setpshared)[0x7f80f8992ac3]
   > ??:0(__xmknodat)[0x7f80f8a24850]
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
   > 240704 13:21:14 [ERROR] mysqld got signal 6 ;
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
   > stack_bottom = 0x7f57017feab0 thread_stack 0x100000
   > /lib/x86_64-linux-gnu/libasan.so.6(+0x45c0e)[0x7f571fe9ac0e]
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x55fd1e5c5c8f]
   > sql/signal_handler.cc:236(handle_fatal_signal)[0x55fd1d156b8d]
   > ??:0(__sigaction)[0x7f571f233520]
   > ??:0(pthread_kill)[0x7f571f2879fc]
   > ??:0(raise)[0x7f571f233476]
   > ??:0(abort)[0x7f571f2197f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7f571f21971b]
   > ??:0(__assert_fail)[0x7f571f22ae96]
   > /usr/local/mysql/bin/mysqld(_ZN16Item_type_holder7val_intEv+0x64)[0x55fd1d20cff0]
   > sql/item.cc:10700(Item_type_holder::val_int())[0x55fd1c4a9b72]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x112)[0x55fd1d206c58]
   > /usr/local/mysql/bin/mysqld(+0x2312a5c)[0x55fd1cf30a5c]
   > /usr/local/mysql/bin/mysqld(+0x2312c5c)[0x55fd1cf30c5c]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect43disable_cond_guard_for_const_null_left_exprEi+0x13d)[0x55fd1d426b61]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect31create_single_in_to_exists_condEP4JOINPP4ItemS4_+0xd4f)[0x55fd1d3fd2d1]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24create_in_to_exists_condEP4JOIN+0x3ab)[0x55fd1d402ed9]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN20choose_subquery_planEy+0x2b0)[0x55fd1ce3ae02]
   > /usr/local/mysql/bin/mysqld(+0x1d686ad)[0x55fd1c9866ad]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN14optimize_innerEv+0x596e)[0x55fd1c96214a]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN8optimizeEv+0x424)[0x55fd1c95b0ce]
   > /usr/local/mysql/bin/mysqld(_ZN13st_select_lex31optimize_unflattened_subqueriesEb+0x5a9)[0x55fd1c7e1875]
   > sql/item.h:1779(Item::val_int_result())[0x55fd1ce34fcb]
   > sql/item.cc:10125(Item_cache_int::cache_value())[0x55fd1c9687b9]
   > sql/item.h:7099(Item_cache::has_value())[0x55fd1c96245b]
   > sql/item.h:7108(Item_cache::is_null())[0x55fd1c95b0ce]
   > sql/item_subselect.h:670(Item_in_subselect::disable_cond_guard_for_const_null_left_expr(int))[0x55fd1c97cdad]
   > sql/item_subselect.cc:2402(Item_in_subselect::create_single_in_to_exists_cond(JOIN*, Item**, Item**))[0x55fd1c94c9c1]
   > sql/item_subselect.cc:2807(Item_in_subselect::create_in_to_exists_cond(JOIN*))[0x55fd1c86e656]
   > sql/opt_subselect.cc:6522(JOIN::choose_subquery_plan(unsigned long long))[0x55fd1c85ce57]
   > sql/sql_select.cc:6020(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x55fd1c879a28]
   > sql/sql_select.cc:2524(JOIN::optimize_inner())[0x55fd1c84f4af]
   > sql/sql_select.cc:1863(JOIN::optimize())[0x55fd1c84c1c2]
   > sql/sql_lex.cc:4915(st_select_lex::optimize_unflattened_subqueries(bool))[0x55fd1cd0f90e]
   > sql/opt_subselect.cc:5656(JOIN::optimize_unflattened_subqueries())[0x55fd1cd0f1b8]
   > sql/sql_select.cc:3125(JOIN::optimize_stage2())[0x55fd1d95c51a]
   > ??:0(pthread_condattr_setpshared)[0x7f571f285ac3]
   > ??:0(__xmknodat)[0x7f571f317850]
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
