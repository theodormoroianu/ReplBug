# Bug ID MDEV-29232-SERIALIZABLE

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-29232
Original isolation level: REPEATABLE READ
Tested isolation level:   SERIALIZABLE


## Details
 * Database: mariadb-debug-10.8.3
 * Number of scenarios: 1
 * Initial setup script: /home/theodor/Projects/MasterThesis/data/sql/MDEV-29232_mysql_bk.sql

## Results
### Scenario 0
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  START TRANSACTION;
     - TID: 0
     - Output: None
 * Instruction #2:
     - SQL:  select case when case when PI() in ( select 85.45 as c0 from t_g2kscc as ref_0 ...
     - TID: 0
     - Output: ERROR: Timeout for this transaction.

 * Container logs:
   > mysqld: /server/server/sql/item_subselect.cc:1980: virtual bool Item_in_subselect::val_bool(): Assertion `(engine->uncacheable() & ~8) || ! engine->is_executed() || with_recursive_reference' failed.
   > 240618 11:52:58 [ERROR] mysqld got signal 6 ;
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
   > max_used_connections=1
   > max_threads=153
   > thread_count=1
   > It is possible that mysqld could use up to 
   > key_buffer_size + (read_buffer_size + sort_buffer_size)*max_threads = 468121 K  bytes of memory
   > Hope that's ok; if not, decrease some variables in the equation.
   > Thread pointer: 0x7fb5a8000dc8
   > Attempting backtrace. You can use the following information to find out
   > where mysqld died. If you see no messages after this, something went
   > terribly wrong...
   > stack_bottom = 0x7fb6101b3c78 thread_stack 0x49000
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x5646c2b4108f]
   > sql/signal_handler.cc:226(handle_fatal_signal)[0x5646c223b65d]
   > ??:0(__sigaction)[0x7fb6119df520]
   > ??:0(pthread_kill)[0x7fb611a339fc]
   > ??:0(raise)[0x7fb6119df476]
   > ??:0(abort)[0x7fb6119c57f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7fb6119c571b]
   > ??:0(__assert_fail)[0x7fb6119d6e96]
   > sql/item_subselect.cc:1982(Item_in_subselect::val_bool())[0x5646c2355d86]
   > /usr/local/mysql/bin/mysqld(+0x845c45)[0x5646c1cd5c45]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_optimizer7val_intEv+0x41f)[0x5646c229284b]
   > /usr/local/mysql/bin/mysqld(_ZNK23Type_handler_int_result13Item_val_boolEP4Item+0x2d)[0x5646c2113917]
   > /usr/local/mysql/bin/mysqld(+0x845a68)[0x5646c1cd5a68]
   > /usr/local/mysql/bin/mysqld(_ZN23Item_func_case_searched9find_itemEv+0x64)[0x5646c2297fda]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_func_case6int_opEv+0xb2)[0x5646c2298326]
   > /usr/local/mysql/bin/mysqld(_ZN27Item_func_hybrid_field_type19val_int_from_int_opEv+0x29)[0x5646c212cdeb]
   > /usr/local/mysql/bin/mysqld(_ZNK23Type_handler_int_result35Item_func_hybrid_field_type_val_intEP27Item_func_hybrid_field_type+0x20)[0x5646c2114b96]
   > /usr/local/mysql/bin/mysqld(_ZN27Item_func_hybrid_field_type7val_intEv+0xbe)[0x5646c1e49c4a]
   > /usr/local/mysql/bin/mysqld(+0x845bad)[0x5646c1cd5bad]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x51)[0x5646c2280689]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_optimizer8fix_leftEP3THD+0x6c4)[0x5646c2291bb0]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24single_value_transformerEP4JOIN+0x454)[0x5646c2356544]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect26select_in_like_transformerEP4JOIN+0x2a7)[0x5646c235c97d]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect18select_transformerEP4JOIN+0x27)[0x5646c2359acf]
   > sql/item.h:1783(Item::val_bool_result())[0x5646c20b42f3]
   > sql/item_cmpfunc.cc:1637(Item_in_optimizer::val_int())[0x5646c1ece429]
   > sql/sql_type.cc:5104(Type_handler_int_result::Item_val_bool(Item*) const)[0x5646c235e28b]
   > sql/item.h:1688(Item::val_bool())[0x5646c234fa60]
   > sql/item_cmpfunc.cc:3000(Item_func_case_searched::find_item())[0x5646c235d06f]
   > sql/item_cmpfunc.cc:3050(Item_func_case::int_op())[0x5646c1d32d48]
   > sql/item_func.h:850(Item_func_hybrid_field_type::val_int_from_int_op())[0x5646c22cd960]
   > sql/sql_type.cc:5428(Type_handler_int_result::Item_func_hybrid_field_type_val_int(Item_func_hybrid_field_type*) const)[0x5646c22a3cd5]
   > sql/item_func.h:906(Item_func_hybrid_field_type::val_int())[0x5646c1d32d48]
   > sql/item.h:1779(Item::val_int_result())[0x5646c22cd960]
   > sql/item.cc:10087(Item_cache_int::cache_value())[0x5646c229890f]
   > sql/item_cmpfunc.cc:1337(Item_in_optimizer::fix_left(THD*))[0x5646c1d32d48]
   > sql/item_subselect.cc:2104(Item_in_subselect::single_value_transformer(JOIN*))[0x5646c1d32d81]
   > sql/item_subselect.cc:3477(Item_in_subselect::select_in_like_transformer(JOIN*))[0x5646c1dba03a]
   > sql/item_subselect.cc:2767(Item_in_subselect::select_transformer(JOIN*))[0x5646c1ecdc59]
   > sql/opt_subselect.cc:745(check_and_do_in_subquery_rewrites(JOIN*))[0x5646c1edb3f1]
   > sql/sql_select.cc:1511(JOIN::prepare(TABLE_LIST*, Item*, unsigned int, st_order*, bool, st_order*, Item*, st_order*, st_select_lex*, st_select_lex_unit*))[0x5646c1eca2ae]
   > sql/item_subselect.cc:3923(subselect_single_select_engine::prepare(THD*))[0x5646c1e6f866]
   > sql/item_subselect.cc:295(Item_subselect::fix_fields(THD*, Item**))[0x5646c1e669aa]
   > sql/item_subselect.cc:3582(Item_in_subselect::fix_fields(THD*, Item**))[0x5646c1e7486e]
   > /usr/local/mysql/bin/mysqld(_Z16dispatch_command19enum_server_commandP3THDPcjb+0x10d4)[0x5646c1e6075d]
   > sql/item.h:1144(Item::fix_fields_if_needed(THD*, Item**))[0x5646c1e5f0cf]
   > sql/item_func.cc:347(Item_func::fix_fields(THD*, Item**))[0x5646c20417d3]
   > sql/item_cmpfunc.cc:6456(Item_func_not::fix_fields(THD*, Item**))[0x5646c2041460]
   > sql/item.h:1144(Item::fix_fields_if_needed(THD*, Item**))[0x5646c256ee81]
   > ??:0(pthread_condattr_setpshared)[0x7fb611a31ac3]
   > ??:0(__xmknodat)[0x7fb611ac3850]
   > Trying to get some variables.
   > Some pointers may be invalid and cause the dump to abort.
   > Query (0x7fb5a8013cd0): select case when case when PI() in ( select 85.45 as c0 from t_g2kscc as ref_0 where (ref_0.pkey <= ( select ref_1.wkey as c0 from t_g2kscc as ref_1)) ) then 60 else 10 end not in ( select ref_4.c_tlumg as c0 from t_d0pt_c as ref_4 ) then 65.4 else 44.96 end
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
   > Fatal signal 11 while backtracing
