# Bug ID MYSQL-92993-REPEATABLE_READ

## Description

Link:                     https://bugs.mysql.com/bug.php?id=92993
Original isolation level: REPEATABLE READ
Tested isolation level:   REPEATABLE READ
Description:              Running 'xa rollback' makes the database crash.


## Details
 * Database: mysql-8.0.13-debug
 * Number of scenarios: 1
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows: 0
 * Instruction #1:
     - Instruction:  SET GLOBAL general_log=ON;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows: 0
 * Instruction #2:
     - Instruction:  create table t1(a1 int)partition by range (a1) (partition p0 values less than (...
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows: 0
 * Instruction #3:
     - Instruction:  drop table mysql.general_log;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows: 0
 * Instruction #4:
     - Instruction:  xa start 'test1';
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows: 0
 * Instruction #5:
     - Instruction:  INSERT INTO t1 VALUES();
     - Transaction: conn_0
     - Output: None
     - Executed order: 5
     - Affected rows: 1
 * Instruction #6:
     - Instruction:  XA END 'test1';
     - Transaction: conn_0
     - Output: None
     - Executed order: 6
     - Affected rows: 0
 * Instruction #7:
     - Instruction:  XA PREPARE 'test1';
     - Transaction: conn_0
     - Output: None
     - Executed order: 7
     - Affected rows: 0
 * Instruction #8:
     - Instruction:  SET @@global.log_output='TABLE';
     - Transaction: conn_0
     - Output: None
     - Executed order: 8
     - Affected rows: 0
 * Instruction #9:
     - Instruction:  xa rollback 'tx1';
     - Transaction: conn_0
     - Output: ERROR: 2013 (HY000): Lost connection to MySQL server during query
     - Executed order: Not executed
     - Affected rows: -1

 * Container logs:
   > 2024-07-26T15:31:26.823650Z 0 [System] [MY-011323] [Server] X Plugin ready for connections. Socket: '/tmp/mysqlx.sock' bind-address: '::' port: 33060
   > mysqld: /mysql-server/sql/binlog.cc:2286: virtual int MYSQL_BIN_LOG::rollback(THD*, bool): Assertion `all || !xs->is_binlogged() || (!xs->is_in_recovery() && thd->is_error())' failed.
   > 15:31:30 UTC - mysqld got signal 6 ;
   > This could be because you hit a bug. It is also possible that this binary
   > or one of the libraries it was linked against is corrupt, improperly built,
   > or misconfigured. This error can also be caused by malfunctioning hardware.
   > Attempting to collect some information that could help diagnose the problem.
   > As this is a crash and something is definitely wrong, the information
   > collection process might fail.
   > key_buffer_size=8388608
   > read_buffer_size=131072
   > max_used_connections=1
   > max_threads=151
   > thread_count=2
   > connection_count=1
   > It is possible that mysqld could use up to 
   > key_buffer_size + (read_buffer_size + sort_buffer_size)*max_threads = 67877 K  bytes of memory
   > Hope that's ok; if not, decrease some variables in the equation.
   > Thread pointer: 0x626000204100
   > Attempting backtrace. You can use the following information to find out
   > where mysqld died. If you see no messages after this, something went
   > terribly wrong...
   > stack_bottom = 7fc5141e0c90 thread_stack 0x46000
   > /lib/x86_64-linux-gnu/libasan.so.5(+0x6cd40) [0x7fc53b083d40]
   > /usr/local/mysql/bin/mysqld(my_print_stacktrace(unsigned char*, unsigned long)+0xd1) [0x558d7e0a484b]
   > /usr/local/mysql/bin/mysqld(handle_fatal_signal+0x7e1) [0x558d7be890a7]
   > /lib/x86_64-linux-gnu/libpthread.so.0(+0x14420) [0x7fc53b008420]
   > /lib/x86_64-linux-gnu/libc.so.6(gsignal+0xcb) [0x7fc53a72e00b]
   > /lib/x86_64-linux-gnu/libc.so.6(abort+0x12b) [0x7fc53a70d859]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x22729) [0x7fc53a70d729]
   > /lib/x86_64-linux-gnu/libc.so.6(+0x33fd6) [0x7fc53a71efd6]
   > /usr/local/mysql/bin/mysqld(MYSQL_BIN_LOG::rollback(THD*, bool)+0x449) [0x558d7d9254e7]
   > /usr/local/mysql/bin/mysqld(trans_rollback_stmt(THD*)+0x172) [0x558d7bdfa494]
   > /usr/local/mysql/bin/mysqld(open_ltable(THD*, TABLE_LIST*, thr_lock_type, unsigned int)+0x271) [0x558d7ba644cb]
   > /usr/local/mysql/bin/mysqld(open_log_table(THD*, TABLE_LIST*, Open_tables_backup*)+0x130) [0x558d7ba64b19]
   > /usr/local/mysql/bin/mysqld(Log_to_csv_event_handler::log_general(THD*, unsigned long long, char const*, unsigned long, unsigned int, char const*, unsigned long, char const*, unsigned long, CHARSET_INFO const*)+0x2b0) [0x558d7c45686c]
   > /usr/local/mysql/bin/mysqld(Query_logger::general_log_write(THD*, enum_server_command, char const*, unsigned long)+0x384) [0x558d7c450be8]
   > /usr/local/mysql/bin/mysqld(mysql_parse(THD*, Parser_state*, bool)+0x709) [0x558d7bb851c4]
   > /usr/local/mysql/bin/mysqld(dispatch_command(THD*, COM_DATA const*, enum_server_command)+0x210c) [0x558d7bb87d90]
   > /usr/local/mysql/bin/mysqld(do_command(THD*)+0x8bd) [0x558d7bb8a8a1]
   > /usr/local/mysql/bin/mysqld(+0x38877b8) [0x558d7be677b8]
   > /usr/local/mysql/bin/mysqld(+0x65cd6bd) [0x558d7ebad6bd]
   > /lib/x86_64-linux-gnu/libpthread.so.0(+0x8609) [0x7fc53affc609]
   > /lib/x86_64-linux-gnu/libc.so.6(clone+0x43) [0x7fc53a80a353]
   > Trying to get some variables.
   > Some pointers may be invalid and cause the dump to abort.
   > Query (6060004f4748): is an invalid pointer
   > Connection ID (thread ID): 10
   > Status: NOT_KILLED
   > The manual page at http://dev.mysql.com/doc/mysql/en/crashing.html contains
   > information that should help you find out what is causing the crash.
