# Bug ID MDEV-29243-READ_COMMITTED

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-29243
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED


## Details
 * Database: mariadb-10.8.3
 * Number of scenarios: 1
 * Initial setup script: /home/theodor/Projects/MasterThesis/data/sql/MDEV-29243_mysql_bk.sql

## Results
### Scenario 0
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
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
     - SQL:  delete from t_swbayb;
     - TID: 1
     - Output: None
 * Instruction #5:
     - SQL:  insert into t_swbayb (wkey, pkey) values (88, 74000);
     - TID: 0
     - Output: None
 * Instruction #6:
     - SQL:  insert into t_8fjoxb (wkey, pkey, c_yecif) values (110, 115000, case when exist...
     - TID: 1
     - Output: ERROR: 2013 (HY000): Lost connection to MySQL server during query
 * Instruction #7:
     - SQL:  insert into t_swbayb (wkey, pkey, c_ywdp4d) values (90, 83000, 'vyenkd');
     - TID: 0
     - Output: None
 * Instruction #8:
     - SQL:  COMMIT;
     - TID: 0
     - Output: None
 * Instruction #9:
     - SQL:  COMMIT;
     - TID: 1
     - Output: Skipped due to previous error.

 * Container logs:
   > mysqld: /server/server/sql/opt_range.cc:15436: virtual int QUICK_GROUP_MIN_MAX_SELECT::get_next(): Assertion `is_last_prefix <= 0' failed.
   > 240618 16:06:58 [ERROR] mysqld got signal 6 ;
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
   > thread_count=2
   > It is possible that mysqld could use up to 
   > key_buffer_size + (read_buffer_size + sort_buffer_size)*max_threads = 468121 K  bytes of memory
   > Hope that's ok; if not, decrease some variables in the equation.
   > Thread pointer: 0x7fb8a0000dc8
   > Attempting backtrace. You can use the following information to find out
   > where mysqld died. If you see no messages after this, something went
   > terribly wrong...
   > stack_bottom = 0x7fb91091dc78 thread_stack 0x49000
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x560731a7408f]
   > sql/signal_handler.cc:226(handle_fatal_signal)[0x56073116e65d]
   > ??:0(__sigaction)[0x7fb9136fa520]
   > ??:0(pthread_kill)[0x7fb91374e9fc]
   > ??:0(raise)[0x7fb9136fa476]
   > ??:0(abort)[0x7fb9136e07f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7fb9136e071b]
   > ??:0(__assert_fail)[0x7fb9136f1e96]
   > sql/opt_range.cc:15440(QUICK_GROUP_MIN_MAX_SELECT::get_next())[0x560730c39a8a]
   > sql/records.cc:403(rr_quick(READ_RECORD*))[0x560730c57d18]
   > sql/records.h:81(READ_RECORD::read_record())[0x560730c422bd]
   > sql/sql_select.cc:21182(sub_select(JOIN*, st_join_table*, bool))[0x560730e3c094]
   > sql/sql_select.cc:20708(do_select(JOIN*, Procedure*))[0x560730e3b434]
   > sql/sql_select.cc:4759(JOIN::exec_inner())[0x560730e0dae9]
   > sql/sql_select.cc:4538(JOIN::exec())[0x560730e0cb23]
   > sql/item_subselect.cc:4141(subselect_single_select_engine::exec())[0x560731291efd]
   > sql/item_subselect.cc:854(Item_subselect::exec())[0x560731284354]
   > sql/item_subselect.cc:1498(Item_singlerow_subselect::val_int())[0x560731286589]
   > sql/item.cc:6814(Item::save_int_in_field(Field*, bool))[0x5607311a8d0e]
   > sql/sql_type.cc:4364(Type_handler_int_result::Item_save_in_field(Item*, Field*, bool) const)[0x56073104506a]
   > sql/item.cc:6824(Item::save_in_field(Field*, bool))[0x5607311a8dc3]
   > sql/item.cc:1519(Item::save_in_field_no_warnings(Field*, bool))[0x5607311971b0]
   > sql/opt_range.cc:8964(Field::get_mm_leaf_int(RANGE_OPT_PARAM*, KEY_PART*, Item_bool_func const*, scalar_comparison_op, Item*, bool))[0x560730c29d75]
   > sql/field.h:2529(Field_int::get_mm_leaf(RANGE_OPT_PARAM*, KEY_PART*, Item_bool_func const*, scalar_comparison_op, Item*))[0x560730f570db]
   > sql/opt_range.cc:8807(Item_bool_func::get_mm_leaf(RANGE_OPT_PARAM*, Field*, KEY_PART*, Item_func::Functype, Item*))[0x560730c2929a]
   > sql/opt_range.cc:8642(Item_bool_func::get_mm_parts(RANGE_OPT_PARAM*, Field*, Item_func::Functype, Item*))[0x560730c2868b]
   > /usr/local/mysql/bin/mysqld(_ZN24Item_bool_func2_with_rev16get_func_mm_treeEP15RANGE_OPT_PARAMP5FieldP4Item+0xb8)[0x560730c40b22]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_bool_func21get_full_func_mm_treeEP15RANGE_OPT_PARAMP10Item_fieldP4Item+0x19e)[0x560730c27406]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_bool_func30get_full_func_mm_tree_for_argsEP15RANGE_OPT_PARAMP4ItemS3_+0xf2)[0x560730c40848]
   > sql/item_cmpfunc.h:499(Item_bool_func2_with_rev::get_func_mm_tree(RANGE_OPT_PARAM*, Field*, Item*))[0x560730c40cdf]
   > sql/opt_range.cc:8295(Item_bool_func::get_full_func_mm_tree(RANGE_OPT_PARAM*, Item_field*, Item*))[0x560730c18c74]
   > sql/item_cmpfunc.h:208(Item_bool_func::get_full_func_mm_tree_for_args(RANGE_OPT_PARAM*, Item*, Item*))[0x560730e0e774]
   > sql/opt_range.cc:2886(SQL_SELECT::test_quick_select(THD*, Bitmap<64u>, unsigned long long, unsigned long long, bool, bool, bool, bool))[0x560730e110eb]
   > sql/sql_select.cc:5061(get_quick_record_count(THD*, SQL_SELECT*, TABLE*, Bitmap<64u> const*, unsigned long long))[0x560730e04f60]
   > sql/sql_select.cc:5788(make_join_statistics(JOIN*, List<TABLE_LIST>&, st_dynamic_array*))[0x560730e02781]
   > sql/sql_select.cc:2476(JOIN::optimize_inner())[0x560730d61ed3]
   > sql/sql_select.cc:1818(JOIN::optimize())[0x560730d44288]
   > sql/sql_lex.cc:4942(st_select_lex::optimize_unflattened_subqueries(bool))[0x560730d9bb67]
   > sql/sql_insert.cc:852(mysql_insert(THD*, TABLE_LIST*, List<Item>&, List<List<Item> >&, List<Item>&, List<Item>&, enum_duplicates, bool, select_result*))[0x560730da786e]
   > sql/sql_parse.cc:4562(mysql_execute_command(THD*, bool))[0x560730d9375d]
   > sql/sql_parse.cc:8027(mysql_parse(THD*, char*, unsigned int, Parser_state*))[0x560730d920cf]
   > sql/sql_parse.cc:1896(dispatch_command(enum_server_command, THD*, char*, unsigned int, bool))[0x560730f747d3]
   > sql/sql_parse.cc:1407(do_command(THD*, bool))[0x560730f74460]
   > sql/sql_connect.cc:1418(do_handle_one_connection(CONNECT*, bool))[0x5607314a1e81]
   > ??:0(pthread_condattr_setpshared)[0x7fb91374cac3]
   > ??:0(__xmknodat)[0x7fb9137de850]
   > Trying to get some variables.
   > Some pointers may be invalid and cause the dump to abort.
   > Query (0x7fb8a0013cd0): insert into t_8fjoxb (wkey, pkey, c_yecif) values (110, 115000, case when exists ( select ref_0.wkey as c14 from t_swbayb as ref_0 where (ref_0.pkey > ( select distinct ref_1.wkey as c0 from t_swbayb as ref_1 ))) then 'vxg_w' else null end )
   > Connection ID (thread ID): 10
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
