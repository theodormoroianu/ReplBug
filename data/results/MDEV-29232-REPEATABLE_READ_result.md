# Bug ID MDEV-29232-REPEATABLE_READ

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-29232
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ


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
 * Instruction #1:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
 * Instruction #2:
     - Instruction:  select case when case when PI() in ( select 85.45 as c0 from t_g2kscc as ref_0 ...
     - Transaction: conn_0
     - Output: ERROR: Timeout for this transaction.
     - Executed order: Not executed

 * Container logs:
   > mysqld: /server/server/sql/item_subselect.cc:1980: virtual bool Item_in_subselect::val_bool(): Assertion `(engine->uncacheable() & ~8) || ! engine->is_executed() || with_recursive_reference' failed.
   > 240701 15:06:16 [ERROR] mysqld got signal 6 ;
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
   > Thread pointer: 0x7fb1f8000dc8
   > Attempting backtrace. You can use the following information to find out
   > where mysqld died. If you see no messages after this, something went
   > terribly wrong...
   > stack_bottom = 0x7fb27011dc78 thread_stack 0x49000
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x557a0736f08f]
   > sql/signal_handler.cc:226(handle_fatal_signal)[0x557a06a6965d]
   > ??:0(__sigaction)[0x7fb2722c1520]
   > ??:0(pthread_kill)[0x7fb2723159fc]
   > ??:0(raise)[0x7fb2722c1476]
   > ??:0(abort)[0x7fb2722a77f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7fb2722a771b]
   > ??:0(__assert_fail)[0x7fb2722b8e96]
   > sql/item_subselect.cc:1982(Item_in_subselect::val_bool())[0x557a06b83d86]
   > /usr/local/mysql/bin/mysqld(+0x845c45)[0x557a06503c45]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_optimizer7val_intEv+0x41f)[0x557a06ac084b]
   > /usr/local/mysql/bin/mysqld(_ZNK23Type_handler_int_result13Item_val_boolEP4Item+0x2d)[0x557a06941917]
   > /usr/local/mysql/bin/mysqld(+0x845a68)[0x557a06503a68]
   > /usr/local/mysql/bin/mysqld(_ZN23Item_func_case_searched9find_itemEv+0x64)[0x557a06ac5fda]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_func_case6int_opEv+0xb2)[0x557a06ac6326]
   > /usr/local/mysql/bin/mysqld(_ZN27Item_func_hybrid_field_type19val_int_from_int_opEv+0x29)[0x557a0695adeb]
   > /usr/local/mysql/bin/mysqld(_ZNK23Type_handler_int_result35Item_func_hybrid_field_type_val_intEP27Item_func_hybrid_field_type+0x20)[0x557a06942b96]
   > /usr/local/mysql/bin/mysqld(_ZN27Item_func_hybrid_field_type7val_intEv+0xbe)[0x557a06677c4a]
   > /usr/local/mysql/bin/mysqld(+0x845bad)[0x557a06503bad]
   > /usr/local/mysql/bin/mysqld(_ZN14Item_cache_int11cache_valueEv+0x51)[0x557a06aae689]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_optimizer8fix_leftEP3THD+0x6c4)[0x557a06abfbb0]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect24single_value_transformerEP4JOIN+0x454)[0x557a06b84544]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect26select_in_like_transformerEP4JOIN+0x2a7)[0x557a06b8a97d]
   > /usr/local/mysql/bin/mysqld(_ZN17Item_in_subselect18select_transformerEP4JOIN+0x27)[0x557a06b87acf]
   > /usr/local/mysql/bin/mysqld(_Z33check_and_do_in_subquery_rewritesP4JOIN+0x8b0)[0x557a068e22f3]
   > /usr/local/mysql/bin/mysqld(_ZN4JOIN7prepareEP10TABLE_LISTP4ItemjP8st_orderbS5_S3_S5_P13st_select_lexP18st_select_lex_unit+0x1115)[0x557a066fc429]
   > /usr/local/mysql/bin/mysqld(_ZN30subselect_single_select_engine7prepareEP3THD+0x1d3)[0x557a06b8c28b]
   > sql/item.h:1783(Item::val_bool_result())[0x557a06b7da60]
   > sql/item_cmpfunc.cc:1637(Item_in_optimizer::val_int())[0x557a06b8b06f]
   > sql/sql_type.cc:5104(Type_handler_int_result::Item_val_bool(Item*) const)[0x557a06560d48]
   > sql/item.h:1688(Item::val_bool())[0x557a06afb960]
   > sql/item_cmpfunc.cc:3000(Item_func_case_searched::find_item())[0x557a06ad1cd5]
   > sql/item_cmpfunc.cc:3050(Item_func_case::int_op())[0x557a06560d48]
   > sql/item_func.h:850(Item_func_hybrid_field_type::val_int_from_int_op())[0x557a06afb960]
   > sql/sql_type.cc:5428(Type_handler_int_result::Item_func_hybrid_field_type_val_int(Item_func_hybrid_field_type*) const)[0x557a06ac690f]
   > sql/item_func.h:906(Item_func_hybrid_field_type::val_int())[0x557a06560d48]
   > sql/item.h:1779(Item::val_int_result())[0x557a06560d81]
   > sql/item.cc:10087(Item_cache_int::cache_value())[0x557a065e803a]
   > sql/item_cmpfunc.cc:1337(Item_in_optimizer::fix_left(THD*))[0x557a066fbc59]
   > sql/item_subselect.cc:2104(Item_in_subselect::single_value_transformer(JOIN*))[0x557a067093f1]
   > sql/item_subselect.cc:3477(Item_in_subselect::select_in_like_transformer(JOIN*))[0x557a066f82ae]
   > sql/item_subselect.cc:2767(Item_in_subselect::select_transformer(JOIN*))[0x557a0669d866]
   > sql/opt_subselect.cc:745(check_and_do_in_subquery_rewrites(JOIN*))[0x557a066949aa]
   > sql/sql_select.cc:1511(JOIN::prepare(TABLE_LIST*, Item*, unsigned int, st_order*, bool, st_order*, Item*, st_order*, st_select_lex*, st_select_lex_unit*))[0x557a066a286e]
   > sql/item_subselect.cc:3923(subselect_single_select_engine::prepare(THD*))[0x557a0668e75d]
   > sql/item_subselect.cc:295(Item_subselect::fix_fields(THD*, Item**))[0x557a0668d0cf]
   > sql/item_subselect.cc:3582(Item_in_subselect::fix_fields(THD*, Item**))[0x557a0686f7d3]
