# Bug ID MDEV-29120-READ_UNCOMMITTED

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-29120
Original isolation level: REPETABLE READ
Tested isolation level:   IsolationLevel.READ_UNCOMMITTED


## Details
 * Database: mariadb-debug-10.8.3
 * Number of scenarios: 1
 * Initial setup script: /home/theodor/Projects/MasterThesis/data/sql/MDEV-29120_mysql_bk.sql

## Results
### Scenario 0
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
     - TID: 1
     - Output: None
 * Instruction #2:
     - SQL:  START TRANSACTION;
     - TID: 0
     - Output: None
 * Instruction #3:
     - SQL:  START TRANSACTION;
     - TID: 1
     - Output: None
 * Instruction #4:
     - SQL:  insert into t_yynypc (wkey, pkey, c_acfajc) values (89, 188000, 40), (89, 18900...
     - TID: 1
     - Output: None
 * Instruction #5:
     - SQL:  delete from t_qrsdpb where exists ( select ref_0.c_bkmkf as c2 from t_zefkic as...
     - TID: 0
     - Output: Error: 2013 (HY000): Lost connection to MySQL server during query
 * Instruction #6:
     - SQL:  update t_zefkic set wkey = 99;
     - TID: 1
     - Output: None
 * Instruction #7:
     - SQL:  ROLLBACK;
     - TID: 0
     - Output: Error: MySQL Connection not available.
 * Instruction #8:
     - SQL:  ROLLBACK;
     - TID: 1
     - Output: None

 * Container logs:
   > mysqld: /server/server/storage/innobase/row/row0sel.cc:4614: dberr_t row_search_mvcc(byte*, page_cur_mode_t, row_prebuilt_t*, ulint, ulint): Assertion `prebuilt->sql_stat_start || prebuilt->table->no_rollback()' failed.
   > 240605 19:00:07 [ERROR] mysqld got signal 6 ;
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
   > Thread pointer: 0x7fceec000dc8
   > Attempting backtrace. You can use the following information to find out
   > where mysqld died. If you see no messages after this, something went
   > terribly wrong...
   > stack_bottom = 0x7fcf60dfec78 thread_stack 0x49000
   > mysys/stacktrace.c:212(my_print_stacktrace)[0x55f5f847908f]
   > sql/signal_handler.cc:226(handle_fatal_signal)[0x55f5f7b7365d]
   > ??:0(__sigaction)[0x7fcf63b89520]
   > ??:0(pthread_kill)[0x7fcf63bdd9fc]
   > ??:0(raise)[0x7fcf63b89476]
   > ??:0(abort)[0x7fcf63b6f7f3]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7fcf63b6f71b]
   > ??:0(__assert_fail)[0x7fcf63b80e96]
   > row/row0sel.cc:4618(row_search_mvcc(unsigned char*, page_cur_mode_t, row_prebuilt_t*, unsigned long, unsigned long))[0x55f5f81adeac]
   > handler/ha_innodb.cc:8990(ha_innobase::index_read(unsigned char*, unsigned char const*, unsigned int, ha_rkey_function))[0x55f5f7f91411]
   > handler/ha_innodb.cc:9359(ha_innobase::index_first(unsigned char*))[0x55f5f7f924c6]
   > handler/ha_innodb.cc:9452(ha_innobase::rnd_next(unsigned char*))[0x55f5f7f926be]
   > sql/handler.cc:3414(handler::ha_rnd_next(unsigned char*))[0x55f5f7b7f481]
   > sql/records.cc:519(rr_sequential(READ_RECORD*))[0x55f5f765cf42]
   > /usr/local/mysql/bin/mysqld(_ZN11READ_RECORD11read_recordEv+0x21)[0x55f5f76472bd]
   > /usr/local/mysql/bin/mysqld(_Z21join_init_read_recordP13st_join_table+0x31b)[0x55f5f784367f]
   > sql/records.h:81(READ_RECORD::read_record())[0x55f5f7840f8f]
   > sql/sql_select.cc:22157(join_init_read_record(st_join_table*))[0x55f5f7840434]
   > sql/sql_select.cc:21160(sub_select(JOIN*, st_join_table*, bool))[0x55f5f7812ae9]
   > sql/sql_select.cc:20708(do_select(JOIN*, Procedure*))[0x55f5f7811b23]
   > sql/sql_select.cc:4759(JOIN::exec_inner())[0x55f5f7c96efd]
   > sql/sql_select.cc:4538(JOIN::exec())[0x55f5f7c89354]
   > sql/item_subselect.cc:4141(subselect_single_select_engine::exec())[0x55f5f7c8cfc7]
   > sql/item_subselect.cc:854(Item_subselect::exec())[0x55f5f7739fe9]
   > sql/item_subselect.cc:1832(Item_exists_subselect::val_int())[0x55f5f7733da1]
   > sql/opt_range.h:1905(SQL_SELECT::skip_record(THD*))[0x55f5f7736232]
   > sql/sql_delete.cc:221(record_should_be_deleted(THD*, TABLE*, SQL_SELECT*, Explain_delete*, bool))[0x55f5f77a1bec]
   > sql/sql_delete.cc:805(mysql_delete(THD*, TABLE_LIST*, Item*, SQL_I_List<st_order>*, unsigned long long, unsigned long long, select_result*))[0x55f5f77ac86e]
   > sql/sql_parse.cc:4804(mysql_execute_command(THD*, bool))[0x55f5f779875d]
   > sql/sql_parse.cc:8027(mysql_parse(THD*, char*, unsigned int, Parser_state*))[0x55f5f77970cf]
   > sql/sql_parse.cc:1896(dispatch_command(enum_server_command, THD*, char*, unsigned int, bool))[0x55f5f79797d3]
   > sql/sql_parse.cc:1407(do_command(THD*, bool))[0x55f5f7979460]
   > sql/sql_connect.cc:1418(do_handle_one_connection(CONNECT*, bool))[0x55f5f7ea6e81]
   > ??:0(pthread_condattr_setpshared)[0x7fcf63bdbac3]
   > ??:0(__xmknodat)[0x7fcf63c6d850]
   > Trying to get some variables.
   > Some pointers may be invalid and cause the dump to abort.
   > Query (0x7fceec013cd0): delete from t_qrsdpb where exists ( select ref_0.c_bkmkf as c2 from t_zefkic as ref_0 where t_qrsdpb.c_hhsy0b not in ( select ref_3.wkey as c0 from (t_yynypc as ref_2 left outer join t_zefkic as ref_3 on (ref_2.wkey = ref_3.wkey )) where ref_3.pkey >= ref_2.wkey))
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
   > Max realtime timeout      200000               200000               us        
   > Core pattern: |/usr/lib/systemd/systemd-coredump %P %u %g %s %t %c %h
   > Fatal signal 11 while backtracing
