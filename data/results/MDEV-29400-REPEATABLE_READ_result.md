# Bug ID MDEV-29400-REPEATABLE_READ

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-29400
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              Sometimes a different number of results are returned by SELECT.


## Details
 * Database: mariadb-10.8.3
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
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  insert into t_nva8p (wkey, pkey, c_k6oesd, c_zwobic) values (69, 41000, case wh...
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
   > mysqld: /server/server/sql/item_cmpfunc.cc:2584: virtual bool Item_func_nullif::fix_length_and_dec(): Assertion `args[0] == args[2] || thd->stmt_arena->is_stmt_execute()' failed.
   > 240716 17:36:31 [ERROR] mysqld got signal 6 ;
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
   > max_used_connections=3
   > max_threads=153
   > thread_count=3
   > It is possible that mysqld could use up to 
   > key_buffer_size + (read_buffer_size + sort_buffer_size)*max_threads = 468121 K  bytes of memory
   > Hope that's ok; if not, decrease some variables in the equation.
   > Thread pointer: 0x7f9bbc000dc8
   > Attempting backtrace. You can use the following information to find out
   > where mysqld died. If you see no messages after this, something went
   > terribly wrong...
   > stack_bottom = 0x7f9c308b6c78 thread_stack 0x49000
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x55558967a08f]
   > sql/signal_handler.cc:226(handle_fatal_signal)[0x555588d7465d]
   > ??:0(__sigaction)[0x7f9c32e7e520]
   > ??:0(pthread_kill)[0x7f9c32ed29fc]
   > ??:0(raise)[0x7f9c32e7e476]
   > ??:0(abort)[0x7f9c32e647f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7f9c32e6471b]
   > ??:0(__assert_fail)[0x7f9c32e75e96]
   > sql/item_cmpfunc.cc:2585(Item_func_nullif::fix_length_and_dec())[0x555588dcfe47]
   > sql/item_func.cc:359(Item_func::fix_fields(THD*, Item**))[0x555588e06a94]
   > /usr/local/mysql/bin/mysqld(_ZN4Item20fix_fields_if_neededEP3THDPPS_+0x52)[0x55558886bd48]
   > /usr/local/mysql/bin/mysqld(_ZN9Item_func10fix_fieldsEP3THDPP4Item+0x29c)[0x555588e06960]
   > /usr/local/mysql/bin/mysqld(_ZN13Item_str_func10fix_fieldsEP3THDPP4Item+0x2f)[0x555588e49a31]
   > /usr/local/mysql/bin/mysqld(_ZN4Item20fix_fields_if_neededEP3THDPPS_+0x52)[0x55558886bd48]
   > /usr/local/mysql/bin/mysqld(_ZN9Item_func10fix_fieldsEP3THDPP4Item+0x29c)[0x555588e06960]
   > sql/item.h:1144(Item::fix_fields_if_needed(THD*, Item**))[0x55558886bd48]
   > sql/item_func.cc:347(Item_func::fix_fields(THD*, Item**))[0x555588e06960]
   > sql/item_strfunc.cc:127(Item_str_func::fix_fields(THD*, Item**))[0x555588a09b94]
   > sql/item.h:1144(Item::fix_fields_if_needed(THD*, Item**))[0x555588a08781]
   > sql/item_func.cc:347(Item_func::fix_fields(THD*, Item**))[0x55558893e26c]
   > sql/item.h:1144(Item::fix_fields_if_needed(THD*, Item**))[0x55558893ba35]
   > sql/item_func.cc:347(Item_func::fix_fields(THD*, Item**))[0x555588a0a4ec]
   > sql/sql_select.cc:2173(JOIN::optimize_inner())[0x555588a08781]
   > sql/sql_select.cc:1818(JOIN::optimize())[0x555588967ed3]
   > sql/sql_derived.cc:1064(mysql_derived_optimize(THD*, LEX*, TABLE_LIST*))[0x55558894a288]
   > sql/sql_derived.cc:200(mysql_handle_single_derived(LEX*, TABLE_LIST*, unsigned int))[0x5555889a1b67]
   > sql/sql_select.cc:2294(JOIN::optimize_inner())[0x5555889ad86e]
   > sql/sql_select.cc:1818(JOIN::optimize())[0x55558899975d]
   > sql/sql_lex.cc:4942(st_select_lex::optimize_unflattened_subqueries(bool))[0x5555889980cf]
   > sql/sql_insert.cc:852(mysql_insert(THD*, TABLE_LIST*, List<Item>&, List<List<Item> >&, List<Item>&, List<Item>&, enum_duplicates, bool, select_result*))[0x555588b7a7d3]
   > sql/sql_parse.cc:4562(mysql_execute_command(THD*, bool))[0x555588b7a460]
   > sql/sql_parse.cc:8027(mysql_parse(THD*, char*, unsigned int, Parser_state*))[0x5555890a7e81]
   > ??:0(pthread_condattr_setpshared)[0x7f9c32ed0ac3]
   > ??:0(__xmknodat)[0x7f9c32f62850]
   > Trying to get some variables.
   > Some pointers may be invalid and cause the dump to abort.
   > Query (0x7f9bbc013d80): insert into t_nva8p (wkey, pkey, c_k6oesd, c_zwobic) values (69, 41000, case when exists ( select subq_0.c0 as c0, subq_0.c3 as c1, subq_0.c1 as c2, subq_0.c0 as c3 from (select distinct ref_0.c_sygi8d as c0, ref_0.c_edvqhb as c1, ref_0.c_sygi8d as c2, ref_0.c_ans1a as c3 from t__d8k3c as ref_0 ) as subq_0 where instr( subq_0.c1, subq_0.c1) < FIELD( subq_0.c1, nullif('h7hmnc', subq_0.c1), subq_0.c1, subq_0.c1)) then 86.38 else 24.15 end , 52.43)
   > Connection ID (thread ID): 41
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
   > Fatal signal 11 while backtracing
