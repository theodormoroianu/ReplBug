# Bug ID MDEV-29483-READ_UNCOMMITTED

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-29483
Original isolation level: REPEATABLE READ
Tested isolation level:   READ UNCOMMITTED
Description:              MariaDB crashes.


## Details
 * Database: mariadb-10.10.1
 * Number of scenarios: 1
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
 * Instruction #1:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
 * Instruction #2:
     - Instruction:  select coalesce(subq_0.c0, LAST_VALUE( subq_0.c0) over (partition by subq_0.c1 ...
     - Transaction: conn_0
     - Output: ERROR: 2013 (HY000): Lost connection to MySQL server during query
     - Executed order: Not executed
 * Instruction #3:
     - Instruction:  ROLLBACK;
     - Transaction: conn_0
     - Output: ERROR: MySQL Connection not available.
     - Executed order: Not executed

 * Container logs:
   > =================================================================
   > ==1==ERROR: AddressSanitizer: heap-use-after-free on address 0x6290002352a0 at pc 0x7f10792d5f37 bp 0x7f105abfb670 sp 0x7f105abfae18
   > READ of size 5 at 0x6290002352a0 thread T15
   >     #0 0x7f10792d5f36 in __interceptor_memmove ../../../../src/libsanitizer/sanitizer_common/sanitizer_common_interceptors.inc:810
   >     #1 0x5653ca2a4cb1 in Binary_string::copy(Binary_string const&) /server/server/sql/sql_string.cc:250
   >     #2 0x5653c9cce785 in String::copy(String const&) /server/server/sql/sql_string.h:885
   >     #3 0x5653ca9a4c49 in Item_cache_str::cache_value() /server/server/sql/item.cc:10489
   >     #4 0x5653ca9ced5a in Item_in_optimizer::val_int() /server/server/sql/item_cmpfunc.cc:1563
   >     #5 0x5653c9c43b71 in Item::val_int_result() /server/server/sql/item.h:1779
   >     #6 0x5653ca9a0c57 in Item_cache_int::cache_value() /server/server/sql/item.cc:10125
   >     #7 0x5653ca9b6a48 in Item_cache_wrapper::cache() /server/server/sql/item.cc:8881
   >     #8 0x5653ca997da9 in Item_cache_wrapper::val_bool() /server/server/sql/item.cc:9067
   >     #9 0x5653ca9f3226 in Item_cond_or::val_int() /server/server/sql/item_cmpfunc.cc:5448
   >     #10 0x5653ca190852 in evaluate_join_record /server/server/sql/sql_select.cc:21861
   >     #11 0x5653ca19013f in sub_select(JOIN*, st_join_table*, bool) /server/server/sql/sql_select.cc:21802
   >     #12 0x5653ca18dadc in do_select /server/server/sql/sql_select.cc:21308
   >     #13 0x5653ca11550c in JOIN::exec_inner() /server/server/sql/sql_select.cc:4812
   >     #14 0x5653ca1129d2 in JOIN::exec() /server/server/sql/sql_select.cc:4590
   >     #15 0x5653ca116f9c in mysql_select(THD*, TABLE_LIST*, List<Item>&, Item*, unsigned int, st_order*, st_order*, Item*, st_order*, unsigned long long, select_result*, st_select_lex_unit*, st_select_lex*) /server/server/sql/sql_select.cc:5070
   >     #16 0x5653ca0e69c0 in handle_select(THD*, LEX*, select_result*, unsigned long) /server/server/sql/sql_select.cc:581
   >     #17 0x5653ca008655 in execute_sqlcom_select /server/server/sql/sql_parse.cc:6261
   >     #18 0x5653c9ff6e56 in mysql_execute_command(THD*, bool) /server/server/sql/sql_parse.cc:3945
   >     #19 0x5653ca013a27 in mysql_parse(THD*, char*, unsigned int, Parser_state*) /server/server/sql/sql_parse.cc:8035
   >     #20 0x5653c9fe94ae in dispatch_command(enum_server_command, THD*, char*, unsigned int, bool) /server/server/sql/sql_parse.cc:1894
   >     #21 0x5653c9fe61c1 in do_command(THD*, bool) /server/server/sql/sql_parse.cc:1407
   >     #22 0x5653ca4a990d in do_handle_one_connection(CONNECT*, bool) /server/server/sql/sql_connect.cc:1418
   >     #23 0x5653ca4a91b7 in handle_one_connection /server/server/sql/sql_connect.cc:1312
   >     #24 0x5653cb0f6519 in pfs_spawn_thread /server/server/storage/perfschema/pfs.cc:2201
   >     #25 0x7f10786ccac2  (/lib/x86_64-linux-gnu/libc.so.6+0x94ac2)
   >     #26 0x7f107875e84f  (/lib/x86_64-linux-gnu/libc.so.6+0x12684f)
   > 0x6290002352a0 is located 160 bytes inside of 16536-byte region [0x629000235200,0x629000239298)
   > freed by thread T15 here:
   >     #0 0x7f1079350537 in __interceptor_free ../../../../src/libsanitizer/asan/asan_malloc_linux.cpp:127
   >     #1 0x5653cb35b5d9 in ut_allocator<unsigned char, true>::deallocate(unsigned char*, unsigned long) /server/server/storage/innobase/include/ut0new.h:424
   >     #2 0x5653cb552065 in mem_heap_block_free(mem_block_info_t*, mem_block_info_t*) /server/server/storage/innobase/mem/mem0mem.cc:416
   >     #3 0x5653cb6d43c9 in mem_heap_free /server/server/storage/innobase/include/mem0mem.inl:419
   >     #4 0x5653cb6d6ed3 in row_mysql_prebuilt_free_blob_heap(row_prebuilt_t*) /server/server/storage/innobase/row/row0mysql.cc:101
   >     #5 0x5653cb75335c in row_sel_store_mysql_rec /server/server/storage/innobase/row/row0sel.cc:3122
   >     #6 0x5653cb76400d in row_search_mvcc(unsigned char*, page_cur_mode_t, row_prebuilt_t*, unsigned long, unsigned long) /server/server/storage/innobase/row/row0sel.cc:5678
   >     #7 0x5653cb304e1b in ha_innobase::general_fetch(unsigned char*, unsigned int, unsigned int) /server/server/storage/innobase/handler/ha_innodb.cc:9262
   >     #8 0x5653cb305d0f in ha_innobase::rnd_next(unsigned char*) /server/server/storage/innobase/handler/ha_innodb.cc:9459
   >     #9 0x5653ca90cdc6 in handler::ha_rnd_next(unsigned char*) /server/server/sql/handler.cc:3415
   >     #10 0x5653c9d0d44d in rr_sequential(READ_RECORD*) /server/server/sql/records.cc:519
   >     #11 0x5653c9cd8b87 in READ_RECORD::read_record() /server/server/sql/records.h:81
   >     #12 0x5653ca18fd56 in sub_select(JOIN*, st_join_table*, bool) /server/server/sql/sql_select.cc:21782
   >     #13 0x5653ca18dadc in do_select /server/server/sql/sql_select.cc:21308
   >     #14 0x5653ca11550c in JOIN::exec_inner() /server/server/sql/sql_select.cc:4812
   >     #15 0x5653ca1129d2 in JOIN::exec() /server/server/sql/sql_select.cc:4590
   >     #16 0x5653ca116f9c in mysql_select(THD*, TABLE_LIST*, List<Item>&, Item*, unsigned int, st_order*, st_order*, Item*, st_order*, unsigned long long, select_result*, st_select_lex_unit*, st_select_lex*) /server/server/sql/sql_select.cc:5070
   >     #17 0x5653ca0e69c0 in handle_select(THD*, LEX*, select_result*, unsigned long) /server/server/sql/sql_select.cc:581
   >     #18 0x5653ca008655 in execute_sqlcom_select /server/server/sql/sql_parse.cc:6261
   >     #19 0x5653c9ff6e56 in mysql_execute_command(THD*, bool) /server/server/sql/sql_parse.cc:3945
   >     #20 0x5653ca013a27 in mysql_parse(THD*, char*, unsigned int, Parser_state*) /server/server/sql/sql_parse.cc:8035
   >     #21 0x5653c9fe94ae in dispatch_command(enum_server_command, THD*, char*, unsigned int, bool) /server/server/sql/sql_parse.cc:1894
   >     #22 0x5653c9fe61c1 in do_command(THD*, bool) /server/server/sql/sql_parse.cc:1407
   >     #23 0x5653ca4a990d in do_handle_one_connection(CONNECT*, bool) /server/server/sql/sql_connect.cc:1418
   >     #24 0x5653ca4a91b7 in handle_one_connection /server/server/sql/sql_connect.cc:1312
   >     #25 0x5653cb0f6519 in pfs_spawn_thread /server/server/storage/perfschema/pfs.cc:2201
   >     #26 0x7f10786ccac2  (/lib/x86_64-linux-gnu/libc.so.6+0x94ac2)
   > previously allocated by thread T15 here:
   >     #0 0x7f1079350887 in __interceptor_malloc ../../../../src/libsanitizer/asan/asan_malloc_linux.cpp:145
   >     #1 0x5653cb35b0a2 in ut_allocator<unsigned char, true>::allocate(unsigned long, unsigned char const*, unsigned int, bool, bool) /server/server/storage/innobase/include/ut0new.h:375
   >     #2 0x5653cb5512e1 in mem_heap_create_block_func(mem_block_info_t*, unsigned long, char const*, unsigned int, unsigned long) /server/server/storage/innobase/mem/mem0mem.cc:277
   >     #3 0x5653cb73bd38 in mem_heap_create_func /server/server/storage/innobase/include/mem0mem.inl:377
   >     #4 0x5653cb752be9 in row_sel_store_mysql_field /server/server/storage/innobase/row/row0sel.cc:3063
   >     #5 0x5653cb753d07 in row_sel_store_mysql_rec /server/server/storage/innobase/row/row0sel.cc:3209
   >     #6 0x5653cb76400d in row_search_mvcc(unsigned char*, page_cur_mode_t, row_prebuilt_t*, unsigned long, unsigned long) /server/server/storage/innobase/row/row0sel.cc:5678
   >     #7 0x5653cb304e1b in ha_innobase::general_fetch(unsigned char*, unsigned int, unsigned int) /server/server/storage/innobase/handler/ha_innodb.cc:9262
   >     #8 0x5653cb305d0f in ha_innobase::rnd_next(unsigned char*) /server/server/storage/innobase/handler/ha_innodb.cc:9459
   >     #9 0x5653ca90cdc6 in handler::ha_rnd_next(unsigned char*) /server/server/sql/handler.cc:3415
   >     #10 0x5653c9d0d44d in rr_sequential(READ_RECORD*) /server/server/sql/records.cc:519
   >     #11 0x5653c9cd8b87 in READ_RECORD::read_record() /server/server/sql/records.h:81
   >     #12 0x5653ca18fd56 in sub_select(JOIN*, st_join_table*, bool) /server/server/sql/sql_select.cc:21782
   >     #13 0x5653ca18dadc in do_select /server/server/sql/sql_select.cc:21308
   >     #14 0x5653ca11550c in JOIN::exec_inner() /server/server/sql/sql_select.cc:4812
   >     #15 0x5653ca1129d2 in JOIN::exec() /server/server/sql/sql_select.cc:4590
   >     #16 0x5653ca116f9c in mysql_select(THD*, TABLE_LIST*, List<Item>&, Item*, unsigned int, st_order*, st_order*, Item*, st_order*, unsigned long long, select_result*, st_select_lex_unit*, st_select_lex*) /server/server/sql/sql_select.cc:5070
   >     #17 0x5653ca0e69c0 in handle_select(THD*, LEX*, select_result*, unsigned long) /server/server/sql/sql_select.cc:581
   >     #18 0x5653ca008655 in execute_sqlcom_select /server/server/sql/sql_parse.cc:6261
   >     #19 0x5653c9ff6e56 in mysql_execute_command(THD*, bool) /server/server/sql/sql_parse.cc:3945
   >     #20 0x5653ca013a27 in mysql_parse(THD*, char*, unsigned int, Parser_state*) /server/server/sql/sql_parse.cc:8035
   >     #21 0x5653c9fe94ae in dispatch_command(enum_server_command, THD*, char*, unsigned int, bool) /server/server/sql/sql_parse.cc:1894
   >     #22 0x5653c9fe61c1 in do_command(THD*, bool) /server/server/sql/sql_parse.cc:1407
   >     #23 0x5653ca4a990d in do_handle_one_connection(CONNECT*, bool) /server/server/sql/sql_connect.cc:1418
   >     #24 0x5653ca4a91b7 in handle_one_connection /server/server/sql/sql_connect.cc:1312
   >     #25 0x5653cb0f6519 in pfs_spawn_thread /server/server/storage/perfschema/pfs.cc:2201
   >     #26 0x7f10786ccac2  (/lib/x86_64-linux-gnu/libc.so.6+0x94ac2)
   > Thread T15 created by T0 here:
   >     #0 0x7f10792f4685 in __interceptor_pthread_create ../../../../src/libsanitizer/asan/asan_interceptors.cpp:216
   >     #1 0x5653cb0f1fa6 in my_thread_create /server/server/storage/perfschema/my_thread.h:52
   >     #2 0x5653cb0f690c in pfs_spawn_thread_v1 /server/server/storage/perfschema/pfs.cc:2252
   >     #3 0x5653c9c18f04 in inline_mysql_thread_create /server/server/include/mysql/psi/mysql_thread.h:1139
   >     #4 0x5653c9c315bf in create_thread_to_handle_connection(CONNECT*) /server/server/sql/mysqld.cc:6018
   >     #5 0x5653c9c31c54 in create_new_thread(CONNECT*) /server/server/sql/mysqld.cc:6077
   >     #6 0x5653c9c31fc6 in handle_accepted_socket(st_mysql_socket, st_mysql_socket) /server/server/sql/mysqld.cc:6139
   >     #7 0x5653c9c329b0 in handle_connections_sockets() /server/server/sql/mysqld.cc:6263
   >     #8 0x5653c9c30d93 in mysqld_main(int, char**) /server/server/sql/mysqld.cc:5913
   >     #9 0x5653c9c1822c in main /server/server/sql/main.cc:34
   >     #10 0x7f1078661d8f  (/lib/x86_64-linux-gnu/libc.so.6+0x29d8f)
   > SUMMARY: AddressSanitizer: heap-use-after-free ../../../../src/libsanitizer/sanitizer_common/sanitizer_common_interceptors.inc:810 in __interceptor_memmove
   > Shadow bytes around the buggy address:
   >   0x0c528003ea00: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
   >   0x0c528003ea10: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
   >   0x0c528003ea20: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
   >   0x0c528003ea30: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
   >   0x0c528003ea40: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
   > =>0x0c528003ea50: fd fd fd fd[fd]fd fd fd fd fd fd fd fd fd fd fd
   >   0x0c528003ea60: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
   >   0x0c528003ea70: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
   >   0x0c528003ea80: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
   >   0x0c528003ea90: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
   >   0x0c528003eaa0: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
   > Shadow byte legend (one shadow byte represents 8 application bytes):
   >   Addressable:           00
   >   Partially addressable: 01 02 03 04 05 06 07 
   >   Heap left redzone:       fa
   >   Freed heap region:       fd
   >   Stack left redzone:      f1
   >   Stack mid redzone:       f2
   >   Stack right redzone:     f3
   >   Stack after return:      f5
   >   Stack use after scope:   f8
   >   Global redzone:          f9
   >   Global init order:       f6
   >   Poisoned by user:        f7
   >   Container overflow:      fc
   >   Array cookie:            ac
   >   Intra object redzone:    bb
   >   ASan internal:           fe
   >   Left alloca redzone:     ca
   >   Right alloca redzone:    cb
   >   Shadow gap:              cc
   > ==1==ABORTING
