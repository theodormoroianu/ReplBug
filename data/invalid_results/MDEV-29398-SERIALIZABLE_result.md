# Bug ID MDEV-29398-SERIALIZABLE

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-29398
Original isolation level: REPEATABLE READ
Tested isolation level:   SERIALIZABLE
Description:              Sometimes a different number of results are returned by SELECT.


## Details
 * Database: mariadb-10.8.3
 * Number of scenarios: 5
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
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
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 2
     - Affected rows / Warnings: 1 / 0
 * Instruction #3:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 3
     - Affected rows / Warnings: 1 / 0
 * Instruction #4:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 4
     - Affected rows / Warnings: 1 / 0
 * Instruction #5:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 5
     - Affected rows / Warnings: 1 / 0
 * Instruction #6:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 6
     - Affected rows / Warnings: 1 / 0
 * Instruction #7:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 7
     - Affected rows / Warnings: 1 / 0
 * Instruction #8:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 8
     - Affected rows / Warnings: 1 / 0
 * Instruction #9:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 9
     - Affected rows / Warnings: 1 / 0
 * Instruction #10:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 10
     - Affected rows / Warnings: 1 / 0
 * Instruction #11:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 11
     - Affected rows / Warnings: 1 / 0
 * Instruction #12:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 12
     - Affected rows / Warnings: 1 / 0
 * Instruction #13:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 13
     - Affected rows / Warnings: 1 / 0
 * Instruction #14:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 14
     - Affected rows / Warnings: 1 / 0
 * Instruction #15:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 15
     - Affected rows / Warnings: 1 / 0
 * Instruction #16:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 16
     - Affected rows / Warnings: 1 / 0
 * Instruction #17:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 17
     - Affected rows / Warnings: 1 / 0
 * Instruction #18:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 18
     - Affected rows / Warnings: 1 / 0
 * Instruction #19:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 19
     - Affected rows / Warnings: 1 / 0
 * Instruction #20:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 20
     - Affected rows / Warnings: 1 / 0
 * Instruction #21:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 21
     - Affected rows / Warnings: 1 / 0
 * Instruction #22:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 22
     - Affected rows / Warnings: 1 / 0
 * Instruction #23:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 23
     - Affected rows / Warnings: 1 / 0
 * Instruction #24:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 24
     - Affected rows / Warnings: 1 / 0
 * Instruction #25:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 25
     - Affected rows / Warnings: 1 / 0
 * Instruction #26:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 26
     - Affected rows / Warnings: 1 / 0
 * Instruction #27:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 27
     - Affected rows / Warnings: 1 / 0
 * Instruction #28:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 28
     - Affected rows / Warnings: 1 / 0
 * Instruction #29:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 29
     - Affected rows / Warnings: 1 / 0
 * Instruction #30:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 30
     - Affected rows / Warnings: 1 / 0
 * Instruction #31:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 31
     - Affected rows / Warnings: 1 / 0
 * Instruction #32:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 32
     - Affected rows / Warnings: 1 / 0
 * Instruction #33:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 33
     - Affected rows / Warnings: 1 / 0
 * Instruction #34:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 34
     - Affected rows / Warnings: 1 / 0
 * Instruction #35:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 35
     - Affected rows / Warnings: 1 / 0
 * Instruction #36:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 36
     - Affected rows / Warnings: 1 / 0
 * Instruction #37:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 37
     - Affected rows / Warnings: 1 / 0
 * Instruction #38:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 38
     - Affected rows / Warnings: 1 / 0
 * Instruction #39:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 39
     - Affected rows / Warnings: 1 / 0
 * Instruction #40:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 40
     - Affected rows / Warnings: 1 / 0
 * Instruction #41:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 41
     - Affected rows / Warnings: 1 / 0
 * Instruction #42:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 42
     - Affected rows / Warnings: 1 / 0
 * Instruction #43:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 43
     - Affected rows / Warnings: 1 / 0
 * Instruction #44:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 44
     - Affected rows / Warnings: 1 / 0
 * Instruction #45:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 45
     - Affected rows / Warnings: 1 / 0
 * Instruction #46:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 46
     - Affected rows / Warnings: 1 / 0
 * Instruction #47:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 47
     - Affected rows / Warnings: 1 / 0
 * Instruction #48:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 48
     - Affected rows / Warnings: 1 / 0
 * Instruction #49:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 49
     - Affected rows / Warnings: 1 / 0
 * Instruction #50:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 50
     - Affected rows / Warnings: 1 / 0
 * Instruction #51:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 51
     - Affected rows / Warnings: 1 / 0
 * Instruction #52:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 52
     - Affected rows / Warnings: 1 / 0
 * Instruction #53:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 53
     - Affected rows / Warnings: 1 / 0
 * Instruction #54:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 54
     - Affected rows / Warnings: 1 / 0
 * Instruction #55:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 55
     - Affected rows / Warnings: 1 / 0
 * Instruction #56:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 56
     - Affected rows / Warnings: 1 / 0
 * Instruction #57:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 57
     - Affected rows / Warnings: 1 / 0
 * Instruction #58:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 58
     - Affected rows / Warnings: 1 / 0
 * Instruction #59:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 59
     - Affected rows / Warnings: 1 / 0
 * Instruction #60:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 60
     - Affected rows / Warnings: 1 / 0
 * Instruction #61:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 61
     - Affected rows / Warnings: 1 / 0
 * Instruction #62:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 62
     - Affected rows / Warnings: 1 / 0
 * Instruction #63:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 63
     - Affected rows / Warnings: 1 / 0
 * Instruction #64:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 64
     - Affected rows / Warnings: 1 / 0
 * Instruction #65:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 65
     - Affected rows / Warnings: 1 / 0
 * Instruction #66:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 66
     - Affected rows / Warnings: 1 / 0
 * Instruction #67:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 67
     - Affected rows / Warnings: 1 / 0
 * Instruction #68:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 68
     - Affected rows / Warnings: 1 / 0
 * Instruction #69:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 69
     - Affected rows / Warnings: 1 / 0
 * Instruction #70:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 70
     - Affected rows / Warnings: 1 / 0
 * Instruction #71:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 71
     - Affected rows / Warnings: 1 / 0
 * Instruction #72:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 72
     - Affected rows / Warnings: 1 / 0
 * Instruction #73:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 73
     - Affected rows / Warnings: 1 / 0
 * Instruction #74:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 74
     - Affected rows / Warnings: 1 / 0
 * Instruction #75:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 75
     - Affected rows / Warnings: 1 / 0
 * Instruction #76:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 76
     - Affected rows / Warnings: 1 / 0
 * Instruction #77:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 77
     - Affected rows / Warnings: 1 / 0
 * Instruction #78:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 78
     - Affected rows / Warnings: 1 / 0
 * Instruction #79:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 79
     - Affected rows / Warnings: 1 / 0
 * Instruction #80:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 80
     - Affected rows / Warnings: 1 / 0
 * Instruction #81:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 81
     - Affected rows / Warnings: 1 / 0
 * Instruction #82:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 82
     - Affected rows / Warnings: 1 / 0
 * Instruction #83:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 83
     - Affected rows / Warnings: 1 / 0
 * Instruction #84:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 84
     - Affected rows / Warnings: 1 / 0
 * Instruction #85:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 85
     - Affected rows / Warnings: 1 / 0
 * Instruction #86:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 86
     - Affected rows / Warnings: 1 / 0
 * Instruction #87:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 87
     - Affected rows / Warnings: 1 / 0
 * Instruction #88:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 88
     - Affected rows / Warnings: 1 / 0
 * Instruction #89:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 89
     - Affected rows / Warnings: 1 / 0
 * Instruction #90:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 90
     - Affected rows / Warnings: 1 / 0
 * Instruction #91:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 91
     - Affected rows / Warnings: 1 / 0
 * Instruction #92:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 92
     - Affected rows / Warnings: 1 / 0
 * Instruction #93:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 93
     - Affected rows / Warnings: 1 / 0
 * Instruction #94:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 94
     - Affected rows / Warnings: 1 / 0
 * Instruction #95:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 95
     - Affected rows / Warnings: 1 / 0
 * Instruction #96:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 96
     - Affected rows / Warnings: 1 / 0
 * Instruction #97:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 97
     - Affected rows / Warnings: 1 / 0
 * Instruction #98:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 98
     - Affected rows / Warnings: 1 / 0
 * Instruction #99:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 99
     - Affected rows / Warnings: 1 / 0
 * Instruction #100:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 100
     - Affected rows / Warnings: 1 / 0
 * Instruction #101:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 101
     - Affected rows / Warnings: 1 / 0
 * Instruction #102:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 102
     - Affected rows / Warnings: 0 / 0

 * Container logs:
   No logs available.

### Scenario 1
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
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
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 2
     - Affected rows / Warnings: 1 / 0
 * Instruction #3:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 3
     - Affected rows / Warnings: 1 / 0
 * Instruction #4:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 4
     - Affected rows / Warnings: 1 / 0
 * Instruction #5:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 5
     - Affected rows / Warnings: 1 / 0
 * Instruction #6:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 6
     - Affected rows / Warnings: 1 / 0
 * Instruction #7:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 7
     - Affected rows / Warnings: 1 / 0
 * Instruction #8:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 8
     - Affected rows / Warnings: 1 / 0
 * Instruction #9:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 9
     - Affected rows / Warnings: 1 / 0
 * Instruction #10:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 10
     - Affected rows / Warnings: 1 / 0
 * Instruction #11:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 11
     - Affected rows / Warnings: 1 / 0
 * Instruction #12:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 12
     - Affected rows / Warnings: 1 / 0
 * Instruction #13:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 13
     - Affected rows / Warnings: 1 / 0
 * Instruction #14:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 14
     - Affected rows / Warnings: 1 / 0
 * Instruction #15:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 15
     - Affected rows / Warnings: 1 / 0
 * Instruction #16:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 16
     - Affected rows / Warnings: 1 / 0
 * Instruction #17:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 17
     - Affected rows / Warnings: 1 / 0
 * Instruction #18:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 18
     - Affected rows / Warnings: 1 / 0
 * Instruction #19:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 19
     - Affected rows / Warnings: 1 / 0
 * Instruction #20:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 20
     - Affected rows / Warnings: 1 / 0
 * Instruction #21:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 21
     - Affected rows / Warnings: 1 / 0
 * Instruction #22:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 22
     - Affected rows / Warnings: 1 / 0
 * Instruction #23:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 23
     - Affected rows / Warnings: 1 / 0
 * Instruction #24:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 24
     - Affected rows / Warnings: 1 / 0
 * Instruction #25:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 25
     - Affected rows / Warnings: 1 / 0
 * Instruction #26:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 26
     - Affected rows / Warnings: 1 / 0
 * Instruction #27:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 27
     - Affected rows / Warnings: 1 / 0
 * Instruction #28:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 28
     - Affected rows / Warnings: 1 / 0
 * Instruction #29:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 29
     - Affected rows / Warnings: 1 / 0
 * Instruction #30:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 30
     - Affected rows / Warnings: 1 / 0
 * Instruction #31:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 31
     - Affected rows / Warnings: 1 / 0
 * Instruction #32:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 32
     - Affected rows / Warnings: 1 / 0
 * Instruction #33:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 33
     - Affected rows / Warnings: 1 / 0
 * Instruction #34:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 34
     - Affected rows / Warnings: 1 / 0
 * Instruction #35:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 35
     - Affected rows / Warnings: 1 / 0
 * Instruction #36:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 36
     - Affected rows / Warnings: 1 / 0
 * Instruction #37:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 37
     - Affected rows / Warnings: 1 / 0
 * Instruction #38:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 38
     - Affected rows / Warnings: 1 / 0
 * Instruction #39:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 39
     - Affected rows / Warnings: 1 / 0
 * Instruction #40:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 40
     - Affected rows / Warnings: 1 / 0
 * Instruction #41:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 41
     - Affected rows / Warnings: 1 / 0
 * Instruction #42:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 42
     - Affected rows / Warnings: 1 / 0
 * Instruction #43:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 43
     - Affected rows / Warnings: 1 / 0
 * Instruction #44:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 44
     - Affected rows / Warnings: 1 / 0
 * Instruction #45:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 45
     - Affected rows / Warnings: 1 / 0
 * Instruction #46:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 46
     - Affected rows / Warnings: 1 / 0
 * Instruction #47:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 47
     - Affected rows / Warnings: 1 / 0
 * Instruction #48:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 48
     - Affected rows / Warnings: 1 / 0
 * Instruction #49:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 49
     - Affected rows / Warnings: 1 / 0
 * Instruction #50:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 50
     - Affected rows / Warnings: 1 / 0
 * Instruction #51:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 51
     - Affected rows / Warnings: 1 / 0
 * Instruction #52:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 52
     - Affected rows / Warnings: 1 / 0
 * Instruction #53:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 53
     - Affected rows / Warnings: 1 / 0
 * Instruction #54:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 54
     - Affected rows / Warnings: 1 / 0
 * Instruction #55:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 55
     - Affected rows / Warnings: 1 / 0
 * Instruction #56:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 56
     - Affected rows / Warnings: 1 / 0
 * Instruction #57:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 57
     - Affected rows / Warnings: 1 / 0
 * Instruction #58:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 58
     - Affected rows / Warnings: 1 / 0
 * Instruction #59:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 59
     - Affected rows / Warnings: 1 / 0
 * Instruction #60:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 60
     - Affected rows / Warnings: 1 / 0
 * Instruction #61:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 61
     - Affected rows / Warnings: 1 / 0
 * Instruction #62:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 62
     - Affected rows / Warnings: 1 / 0
 * Instruction #63:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 63
     - Affected rows / Warnings: 1 / 0
 * Instruction #64:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 64
     - Affected rows / Warnings: 1 / 0
 * Instruction #65:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 65
     - Affected rows / Warnings: 1 / 0
 * Instruction #66:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 66
     - Affected rows / Warnings: 1 / 0
 * Instruction #67:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 67
     - Affected rows / Warnings: 1 / 0
 * Instruction #68:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 68
     - Affected rows / Warnings: 1 / 0
 * Instruction #69:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 69
     - Affected rows / Warnings: 1 / 0
 * Instruction #70:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 70
     - Affected rows / Warnings: 1 / 0
 * Instruction #71:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 71
     - Affected rows / Warnings: 1 / 0
 * Instruction #72:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 72
     - Affected rows / Warnings: 1 / 0
 * Instruction #73:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 73
     - Affected rows / Warnings: 1 / 0
 * Instruction #74:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 74
     - Affected rows / Warnings: 1 / 0
 * Instruction #75:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 75
     - Affected rows / Warnings: 1 / 0
 * Instruction #76:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 76
     - Affected rows / Warnings: 1 / 0
 * Instruction #77:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 77
     - Affected rows / Warnings: 1 / 0
 * Instruction #78:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 78
     - Affected rows / Warnings: 1 / 0
 * Instruction #79:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 79
     - Affected rows / Warnings: 1 / 0
 * Instruction #80:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 80
     - Affected rows / Warnings: 1 / 0
 * Instruction #81:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 81
     - Affected rows / Warnings: 1 / 0
 * Instruction #82:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 82
     - Affected rows / Warnings: 1 / 0
 * Instruction #83:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 83
     - Affected rows / Warnings: 1 / 0
 * Instruction #84:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 84
     - Affected rows / Warnings: 1 / 0
 * Instruction #85:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 85
     - Affected rows / Warnings: 1 / 0
 * Instruction #86:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 86
     - Affected rows / Warnings: 1 / 0
 * Instruction #87:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 87
     - Affected rows / Warnings: 1 / 0
 * Instruction #88:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 88
     - Affected rows / Warnings: 1 / 0
 * Instruction #89:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 89
     - Affected rows / Warnings: 1 / 0
 * Instruction #90:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 90
     - Affected rows / Warnings: 1 / 0
 * Instruction #91:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 91
     - Affected rows / Warnings: 1 / 0
 * Instruction #92:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 92
     - Affected rows / Warnings: 1 / 0
 * Instruction #93:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 93
     - Affected rows / Warnings: 1 / 0
 * Instruction #94:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 94
     - Affected rows / Warnings: 1 / 0
 * Instruction #95:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 95
     - Affected rows / Warnings: 1 / 0
 * Instruction #96:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 96
     - Affected rows / Warnings: 1 / 0
 * Instruction #97:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 97
     - Affected rows / Warnings: 1 / 0
 * Instruction #98:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 98
     - Affected rows / Warnings: 1 / 0
 * Instruction #99:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 99
     - Affected rows / Warnings: 1 / 0
 * Instruction #100:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 100
     - Affected rows / Warnings: 1 / 0
 * Instruction #101:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 101
     - Affected rows / Warnings: 1 / 0
 * Instruction #102:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 102
     - Affected rows / Warnings: 0 / 0

 * Container logs:
   No logs available.

### Scenario 2
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
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
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 2
     - Affected rows / Warnings: 1 / 0
 * Instruction #3:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 3
     - Affected rows / Warnings: 1 / 0
 * Instruction #4:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 4
     - Affected rows / Warnings: 1 / 0
 * Instruction #5:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 5
     - Affected rows / Warnings: 1 / 0
 * Instruction #6:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 6
     - Affected rows / Warnings: 1 / 0
 * Instruction #7:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 7
     - Affected rows / Warnings: 1 / 0
 * Instruction #8:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 8
     - Affected rows / Warnings: 1 / 0
 * Instruction #9:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 9
     - Affected rows / Warnings: 1 / 0
 * Instruction #10:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 10
     - Affected rows / Warnings: 1 / 0
 * Instruction #11:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 11
     - Affected rows / Warnings: 1 / 0
 * Instruction #12:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 12
     - Affected rows / Warnings: 1 / 0
 * Instruction #13:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 13
     - Affected rows / Warnings: 1 / 0
 * Instruction #14:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 14
     - Affected rows / Warnings: 1 / 0
 * Instruction #15:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 15
     - Affected rows / Warnings: 1 / 0
 * Instruction #16:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 16
     - Affected rows / Warnings: 1 / 0
 * Instruction #17:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 17
     - Affected rows / Warnings: 1 / 0
 * Instruction #18:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 18
     - Affected rows / Warnings: 1 / 0
 * Instruction #19:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 19
     - Affected rows / Warnings: 1 / 0
 * Instruction #20:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 20
     - Affected rows / Warnings: 1 / 0
 * Instruction #21:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 21
     - Affected rows / Warnings: 1 / 0
 * Instruction #22:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 22
     - Affected rows / Warnings: 1 / 0
 * Instruction #23:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 23
     - Affected rows / Warnings: 1 / 0
 * Instruction #24:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 24
     - Affected rows / Warnings: 1 / 0
 * Instruction #25:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 25
     - Affected rows / Warnings: 1 / 0
 * Instruction #26:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 26
     - Affected rows / Warnings: 1 / 0
 * Instruction #27:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 27
     - Affected rows / Warnings: 1 / 0
 * Instruction #28:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 28
     - Affected rows / Warnings: 1 / 0
 * Instruction #29:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 29
     - Affected rows / Warnings: 1 / 0
 * Instruction #30:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 30
     - Affected rows / Warnings: 1 / 0
 * Instruction #31:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 31
     - Affected rows / Warnings: 1 / 0
 * Instruction #32:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 32
     - Affected rows / Warnings: 1 / 0
 * Instruction #33:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 33
     - Affected rows / Warnings: 1 / 0
 * Instruction #34:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 34
     - Affected rows / Warnings: 1 / 0
 * Instruction #35:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 35
     - Affected rows / Warnings: 1 / 0
 * Instruction #36:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 36
     - Affected rows / Warnings: 1 / 0
 * Instruction #37:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 37
     - Affected rows / Warnings: 1 / 0
 * Instruction #38:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 38
     - Affected rows / Warnings: 1 / 0
 * Instruction #39:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 39
     - Affected rows / Warnings: 1 / 0
 * Instruction #40:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 40
     - Affected rows / Warnings: 1 / 0
 * Instruction #41:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 41
     - Affected rows / Warnings: 1 / 0
 * Instruction #42:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 42
     - Affected rows / Warnings: 1 / 0
 * Instruction #43:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 43
     - Affected rows / Warnings: 1 / 0
 * Instruction #44:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 44
     - Affected rows / Warnings: 1 / 0
 * Instruction #45:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 45
     - Affected rows / Warnings: 1 / 0
 * Instruction #46:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 46
     - Affected rows / Warnings: 1 / 0
 * Instruction #47:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 47
     - Affected rows / Warnings: 1 / 0
 * Instruction #48:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 48
     - Affected rows / Warnings: 1 / 0
 * Instruction #49:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 49
     - Affected rows / Warnings: 1 / 0
 * Instruction #50:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 50
     - Affected rows / Warnings: 1 / 0
 * Instruction #51:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 51
     - Affected rows / Warnings: 1 / 0
 * Instruction #52:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 52
     - Affected rows / Warnings: 1 / 0
 * Instruction #53:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 53
     - Affected rows / Warnings: 1 / 0
 * Instruction #54:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 54
     - Affected rows / Warnings: 1 / 0
 * Instruction #55:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 55
     - Affected rows / Warnings: 1 / 0
 * Instruction #56:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 56
     - Affected rows / Warnings: 1 / 0
 * Instruction #57:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 57
     - Affected rows / Warnings: 1 / 0
 * Instruction #58:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 58
     - Affected rows / Warnings: 1 / 0
 * Instruction #59:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 59
     - Affected rows / Warnings: 1 / 0
 * Instruction #60:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 60
     - Affected rows / Warnings: 1 / 0
 * Instruction #61:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 61
     - Affected rows / Warnings: 1 / 0
 * Instruction #62:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 62
     - Affected rows / Warnings: 1 / 0
 * Instruction #63:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 63
     - Affected rows / Warnings: 1 / 0
 * Instruction #64:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 64
     - Affected rows / Warnings: 1 / 0
 * Instruction #65:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 65
     - Affected rows / Warnings: 1 / 0
 * Instruction #66:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 66
     - Affected rows / Warnings: 1 / 0
 * Instruction #67:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 67
     - Affected rows / Warnings: 1 / 0
 * Instruction #68:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 68
     - Affected rows / Warnings: 1 / 0
 * Instruction #69:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 69
     - Affected rows / Warnings: 1 / 0
 * Instruction #70:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 70
     - Affected rows / Warnings: 1 / 0
 * Instruction #71:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 71
     - Affected rows / Warnings: 1 / 0
 * Instruction #72:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 72
     - Affected rows / Warnings: 1 / 0
 * Instruction #73:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 73
     - Affected rows / Warnings: 1 / 0
 * Instruction #74:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 74
     - Affected rows / Warnings: 1 / 0
 * Instruction #75:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 75
     - Affected rows / Warnings: 1 / 0
 * Instruction #76:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 76
     - Affected rows / Warnings: 1 / 0
 * Instruction #77:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 77
     - Affected rows / Warnings: 1 / 0
 * Instruction #78:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 78
     - Affected rows / Warnings: 1 / 0
 * Instruction #79:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 79
     - Affected rows / Warnings: 1 / 0
 * Instruction #80:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 80
     - Affected rows / Warnings: 1 / 0
 * Instruction #81:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 81
     - Affected rows / Warnings: 1 / 0
 * Instruction #82:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 82
     - Affected rows / Warnings: 1 / 0
 * Instruction #83:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 83
     - Affected rows / Warnings: 1 / 0
 * Instruction #84:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 84
     - Affected rows / Warnings: 1 / 0
 * Instruction #85:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 85
     - Affected rows / Warnings: 1 / 0
 * Instruction #86:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 86
     - Affected rows / Warnings: 1 / 0
 * Instruction #87:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 87
     - Affected rows / Warnings: 1 / 0
 * Instruction #88:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 88
     - Affected rows / Warnings: 1 / 0
 * Instruction #89:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 89
     - Affected rows / Warnings: 1 / 0
 * Instruction #90:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 90
     - Affected rows / Warnings: 1 / 0
 * Instruction #91:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 91
     - Affected rows / Warnings: 1 / 0
 * Instruction #92:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 92
     - Affected rows / Warnings: 1 / 0
 * Instruction #93:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 93
     - Affected rows / Warnings: 1 / 0
 * Instruction #94:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 94
     - Affected rows / Warnings: 1 / 0
 * Instruction #95:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 95
     - Affected rows / Warnings: 1 / 0
 * Instruction #96:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 96
     - Affected rows / Warnings: 1 / 0
 * Instruction #97:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 97
     - Affected rows / Warnings: 1 / 0
 * Instruction #98:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 98
     - Affected rows / Warnings: 1 / 0
 * Instruction #99:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 99
     - Affected rows / Warnings: 1 / 0
 * Instruction #100:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 100
     - Affected rows / Warnings: 1 / 0
 * Instruction #101:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 101
     - Affected rows / Warnings: 1 / 0
 * Instruction #102:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 102
     - Affected rows / Warnings: 0 / 0

 * Container logs:
   No logs available.

### Scenario 3
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
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
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 2
     - Affected rows / Warnings: 1 / 0
 * Instruction #3:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 3
     - Affected rows / Warnings: 1 / 0
 * Instruction #4:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 4
     - Affected rows / Warnings: 1 / 0
 * Instruction #5:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 5
     - Affected rows / Warnings: 1 / 0
 * Instruction #6:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 6
     - Affected rows / Warnings: 1 / 0
 * Instruction #7:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 7
     - Affected rows / Warnings: 1 / 0
 * Instruction #8:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 8
     - Affected rows / Warnings: 1 / 0
 * Instruction #9:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 9
     - Affected rows / Warnings: 1 / 0
 * Instruction #10:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 10
     - Affected rows / Warnings: 1 / 0
 * Instruction #11:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 11
     - Affected rows / Warnings: 1 / 0
 * Instruction #12:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 12
     - Affected rows / Warnings: 1 / 0
 * Instruction #13:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 13
     - Affected rows / Warnings: 1 / 0
 * Instruction #14:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 14
     - Affected rows / Warnings: 1 / 0
 * Instruction #15:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 15
     - Affected rows / Warnings: 1 / 0
 * Instruction #16:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 16
     - Affected rows / Warnings: 1 / 0
 * Instruction #17:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 17
     - Affected rows / Warnings: 1 / 0
 * Instruction #18:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 18
     - Affected rows / Warnings: 1 / 0
 * Instruction #19:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 19
     - Affected rows / Warnings: 1 / 0
 * Instruction #20:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 20
     - Affected rows / Warnings: 1 / 0
 * Instruction #21:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 21
     - Affected rows / Warnings: 1 / 0
 * Instruction #22:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 22
     - Affected rows / Warnings: 1 / 0
 * Instruction #23:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 23
     - Affected rows / Warnings: 1 / 0
 * Instruction #24:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 24
     - Affected rows / Warnings: 1 / 0
 * Instruction #25:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 25
     - Affected rows / Warnings: 1 / 0
 * Instruction #26:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 26
     - Affected rows / Warnings: 1 / 0
 * Instruction #27:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 27
     - Affected rows / Warnings: 1 / 0
 * Instruction #28:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 28
     - Affected rows / Warnings: 1 / 0
 * Instruction #29:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 29
     - Affected rows / Warnings: 1 / 0
 * Instruction #30:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 30
     - Affected rows / Warnings: 1 / 0
 * Instruction #31:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 31
     - Affected rows / Warnings: 1 / 0
 * Instruction #32:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 32
     - Affected rows / Warnings: 1 / 0
 * Instruction #33:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 33
     - Affected rows / Warnings: 1 / 0
 * Instruction #34:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 34
     - Affected rows / Warnings: 1 / 0
 * Instruction #35:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 35
     - Affected rows / Warnings: 1 / 0
 * Instruction #36:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 36
     - Affected rows / Warnings: 1 / 0
 * Instruction #37:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 37
     - Affected rows / Warnings: 1 / 0
 * Instruction #38:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 38
     - Affected rows / Warnings: 1 / 0
 * Instruction #39:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 39
     - Affected rows / Warnings: 1 / 0
 * Instruction #40:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 40
     - Affected rows / Warnings: 1 / 0
 * Instruction #41:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 41
     - Affected rows / Warnings: 1 / 0
 * Instruction #42:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 42
     - Affected rows / Warnings: 1 / 0
 * Instruction #43:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 43
     - Affected rows / Warnings: 1 / 0
 * Instruction #44:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 44
     - Affected rows / Warnings: 1 / 0
 * Instruction #45:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 45
     - Affected rows / Warnings: 1 / 0
 * Instruction #46:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 46
     - Affected rows / Warnings: 1 / 0
 * Instruction #47:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 47
     - Affected rows / Warnings: 1 / 0
 * Instruction #48:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 48
     - Affected rows / Warnings: 1 / 0
 * Instruction #49:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 49
     - Affected rows / Warnings: 1 / 0
 * Instruction #50:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 50
     - Affected rows / Warnings: 1 / 0
 * Instruction #51:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 51
     - Affected rows / Warnings: 1 / 0
 * Instruction #52:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 52
     - Affected rows / Warnings: 1 / 0
 * Instruction #53:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 53
     - Affected rows / Warnings: 1 / 0
 * Instruction #54:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 54
     - Affected rows / Warnings: 1 / 0
 * Instruction #55:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 55
     - Affected rows / Warnings: 1 / 0
 * Instruction #56:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 56
     - Affected rows / Warnings: 1 / 0
 * Instruction #57:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 57
     - Affected rows / Warnings: 1 / 0
 * Instruction #58:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 58
     - Affected rows / Warnings: 1 / 0
 * Instruction #59:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 59
     - Affected rows / Warnings: 1 / 0
 * Instruction #60:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 60
     - Affected rows / Warnings: 1 / 0
 * Instruction #61:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 61
     - Affected rows / Warnings: 1 / 0
 * Instruction #62:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 62
     - Affected rows / Warnings: 1 / 0
 * Instruction #63:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 63
     - Affected rows / Warnings: 1 / 0
 * Instruction #64:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 64
     - Affected rows / Warnings: 1 / 0
 * Instruction #65:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 65
     - Affected rows / Warnings: 1 / 0
 * Instruction #66:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 66
     - Affected rows / Warnings: 1 / 0
 * Instruction #67:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 67
     - Affected rows / Warnings: 1 / 0
 * Instruction #68:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 68
     - Affected rows / Warnings: 1 / 0
 * Instruction #69:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 69
     - Affected rows / Warnings: 1 / 0
 * Instruction #70:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 70
     - Affected rows / Warnings: 1 / 0
 * Instruction #71:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 71
     - Affected rows / Warnings: 1 / 0
 * Instruction #72:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 72
     - Affected rows / Warnings: 1 / 0
 * Instruction #73:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 73
     - Affected rows / Warnings: 1 / 0
 * Instruction #74:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 74
     - Affected rows / Warnings: 1 / 0
 * Instruction #75:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 75
     - Affected rows / Warnings: 1 / 0
 * Instruction #76:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 76
     - Affected rows / Warnings: 1 / 0
 * Instruction #77:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 77
     - Affected rows / Warnings: 1 / 0
 * Instruction #78:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 78
     - Affected rows / Warnings: 1 / 0
 * Instruction #79:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 79
     - Affected rows / Warnings: 1 / 0
 * Instruction #80:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 80
     - Affected rows / Warnings: 1 / 0
 * Instruction #81:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 81
     - Affected rows / Warnings: 1 / 0
 * Instruction #82:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 82
     - Affected rows / Warnings: 1 / 0
 * Instruction #83:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 83
     - Affected rows / Warnings: 1 / 0
 * Instruction #84:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 84
     - Affected rows / Warnings: 1 / 0
 * Instruction #85:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 85
     - Affected rows / Warnings: 1 / 0
 * Instruction #86:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 86
     - Affected rows / Warnings: 1 / 0
 * Instruction #87:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 87
     - Affected rows / Warnings: 1 / 0
 * Instruction #88:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 88
     - Affected rows / Warnings: 1 / 0
 * Instruction #89:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 89
     - Affected rows / Warnings: 1 / 0
 * Instruction #90:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 90
     - Affected rows / Warnings: 1 / 0
 * Instruction #91:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 91
     - Affected rows / Warnings: 1 / 0
 * Instruction #92:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 92
     - Affected rows / Warnings: 1 / 0
 * Instruction #93:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 93
     - Affected rows / Warnings: 1 / 0
 * Instruction #94:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 94
     - Affected rows / Warnings: 1 / 0
 * Instruction #95:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 95
     - Affected rows / Warnings: 1 / 0
 * Instruction #96:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 96
     - Affected rows / Warnings: 1 / 0
 * Instruction #97:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 97
     - Affected rows / Warnings: 1 / 0
 * Instruction #98:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 98
     - Affected rows / Warnings: 1 / 0
 * Instruction #99:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 99
     - Affected rows / Warnings: 1 / 0
 * Instruction #100:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 100
     - Affected rows / Warnings: 1 / 0
 * Instruction #101:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 101
     - Affected rows / Warnings: 1 / 0
 * Instruction #102:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 102
     - Affected rows / Warnings: 0 / 0

 * Container logs:
   No logs available.

### Scenario 4
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
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
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 2
     - Affected rows / Warnings: 1 / 0
 * Instruction #3:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 3
     - Affected rows / Warnings: 1 / 0
 * Instruction #4:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 4
     - Affected rows / Warnings: 1 / 0
 * Instruction #5:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 5
     - Affected rows / Warnings: 1 / 0
 * Instruction #6:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 6
     - Affected rows / Warnings: 1 / 0
 * Instruction #7:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 7
     - Affected rows / Warnings: 1 / 0
 * Instruction #8:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 8
     - Affected rows / Warnings: 1 / 0
 * Instruction #9:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 9
     - Affected rows / Warnings: 1 / 0
 * Instruction #10:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 10
     - Affected rows / Warnings: 1 / 0
 * Instruction #11:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 11
     - Affected rows / Warnings: 1 / 0
 * Instruction #12:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 12
     - Affected rows / Warnings: 1 / 0
 * Instruction #13:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 13
     - Affected rows / Warnings: 1 / 0
 * Instruction #14:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 14
     - Affected rows / Warnings: 1 / 0
 * Instruction #15:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 15
     - Affected rows / Warnings: 1 / 0
 * Instruction #16:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 16
     - Affected rows / Warnings: 1 / 0
 * Instruction #17:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 17
     - Affected rows / Warnings: 1 / 0
 * Instruction #18:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 18
     - Affected rows / Warnings: 1 / 0
 * Instruction #19:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 19
     - Affected rows / Warnings: 1 / 0
 * Instruction #20:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 20
     - Affected rows / Warnings: 1 / 0
 * Instruction #21:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 21
     - Affected rows / Warnings: 1 / 0
 * Instruction #22:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 22
     - Affected rows / Warnings: 1 / 0
 * Instruction #23:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 23
     - Affected rows / Warnings: 1 / 0
 * Instruction #24:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 24
     - Affected rows / Warnings: 1 / 0
 * Instruction #25:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 25
     - Affected rows / Warnings: 1 / 0
 * Instruction #26:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 26
     - Affected rows / Warnings: 1 / 0
 * Instruction #27:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 27
     - Affected rows / Warnings: 1 / 0
 * Instruction #28:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 28
     - Affected rows / Warnings: 1 / 0
 * Instruction #29:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 29
     - Affected rows / Warnings: 1 / 0
 * Instruction #30:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 30
     - Affected rows / Warnings: 1 / 0
 * Instruction #31:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 31
     - Affected rows / Warnings: 1 / 0
 * Instruction #32:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 32
     - Affected rows / Warnings: 1 / 0
 * Instruction #33:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 33
     - Affected rows / Warnings: 1 / 0
 * Instruction #34:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 34
     - Affected rows / Warnings: 1 / 0
 * Instruction #35:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 35
     - Affected rows / Warnings: 1 / 0
 * Instruction #36:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 36
     - Affected rows / Warnings: 1 / 0
 * Instruction #37:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 37
     - Affected rows / Warnings: 1 / 0
 * Instruction #38:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 38
     - Affected rows / Warnings: 1 / 0
 * Instruction #39:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 39
     - Affected rows / Warnings: 1 / 0
 * Instruction #40:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 40
     - Affected rows / Warnings: 1 / 0
 * Instruction #41:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 41
     - Affected rows / Warnings: 1 / 0
 * Instruction #42:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 42
     - Affected rows / Warnings: 1 / 0
 * Instruction #43:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 43
     - Affected rows / Warnings: 1 / 0
 * Instruction #44:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 44
     - Affected rows / Warnings: 1 / 0
 * Instruction #45:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 45
     - Affected rows / Warnings: 1 / 0
 * Instruction #46:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 46
     - Affected rows / Warnings: 1 / 0
 * Instruction #47:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 47
     - Affected rows / Warnings: 1 / 0
 * Instruction #48:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 48
     - Affected rows / Warnings: 1 / 0
 * Instruction #49:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 49
     - Affected rows / Warnings: 1 / 0
 * Instruction #50:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 50
     - Affected rows / Warnings: 1 / 0
 * Instruction #51:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 51
     - Affected rows / Warnings: 1 / 0
 * Instruction #52:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 52
     - Affected rows / Warnings: 1 / 0
 * Instruction #53:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 53
     - Affected rows / Warnings: 1 / 0
 * Instruction #54:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 54
     - Affected rows / Warnings: 1 / 0
 * Instruction #55:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 55
     - Affected rows / Warnings: 1 / 0
 * Instruction #56:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 56
     - Affected rows / Warnings: 1 / 0
 * Instruction #57:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 57
     - Affected rows / Warnings: 1 / 0
 * Instruction #58:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 58
     - Affected rows / Warnings: 1 / 0
 * Instruction #59:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 59
     - Affected rows / Warnings: 1 / 0
 * Instruction #60:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 60
     - Affected rows / Warnings: 1 / 0
 * Instruction #61:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 61
     - Affected rows / Warnings: 1 / 0
 * Instruction #62:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 62
     - Affected rows / Warnings: 1 / 0
 * Instruction #63:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 63
     - Affected rows / Warnings: 1 / 0
 * Instruction #64:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 64
     - Affected rows / Warnings: 1 / 0
 * Instruction #65:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 65
     - Affected rows / Warnings: 1 / 0
 * Instruction #66:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 66
     - Affected rows / Warnings: 1 / 0
 * Instruction #67:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 67
     - Affected rows / Warnings: 1 / 0
 * Instruction #68:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 68
     - Affected rows / Warnings: 1 / 0
 * Instruction #69:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 69
     - Affected rows / Warnings: 1 / 0
 * Instruction #70:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 70
     - Affected rows / Warnings: 1 / 0
 * Instruction #71:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 71
     - Affected rows / Warnings: 1 / 0
 * Instruction #72:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 72
     - Affected rows / Warnings: 1 / 0
 * Instruction #73:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 73
     - Affected rows / Warnings: 1 / 0
 * Instruction #74:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 74
     - Affected rows / Warnings: 1 / 0
 * Instruction #75:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 75
     - Affected rows / Warnings: 1 / 0
 * Instruction #76:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 76
     - Affected rows / Warnings: 1 / 0
 * Instruction #77:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 77
     - Affected rows / Warnings: 1 / 0
 * Instruction #78:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 78
     - Affected rows / Warnings: 1 / 0
 * Instruction #79:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 79
     - Affected rows / Warnings: 1 / 0
 * Instruction #80:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 80
     - Affected rows / Warnings: 1 / 0
 * Instruction #81:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 81
     - Affected rows / Warnings: 1 / 0
 * Instruction #82:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 82
     - Affected rows / Warnings: 1 / 0
 * Instruction #83:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 83
     - Affected rows / Warnings: 1 / 0
 * Instruction #84:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 84
     - Affected rows / Warnings: 1 / 0
 * Instruction #85:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 85
     - Affected rows / Warnings: 1 / 0
 * Instruction #86:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 86
     - Affected rows / Warnings: 1 / 0
 * Instruction #87:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 87
     - Affected rows / Warnings: 1 / 0
 * Instruction #88:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 88
     - Affected rows / Warnings: 1 / 0
 * Instruction #89:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 89
     - Affected rows / Warnings: 1 / 0
 * Instruction #90:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 90
     - Affected rows / Warnings: 1 / 0
 * Instruction #91:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 91
     - Affected rows / Warnings: 1 / 0
 * Instruction #92:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 92
     - Affected rows / Warnings: 1 / 0
 * Instruction #93:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 93
     - Affected rows / Warnings: 1 / 0
 * Instruction #94:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 94
     - Affected rows / Warnings: 1 / 0
 * Instruction #95:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 95
     - Affected rows / Warnings: 1 / 0
 * Instruction #96:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 96
     - Affected rows / Warnings: 1 / 0
 * Instruction #97:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 97
     - Affected rows / Warnings: 1 / 0
 * Instruction #98:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 98
     - Affected rows / Warnings: 1 / 0
 * Instruction #99:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 99
     - Affected rows / Warnings: 1 / 0
 * Instruction #100:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 100
     - Affected rows / Warnings: 1 / 0
 * Instruction #101:
     - Instruction:  select t_tu__yc.wkey as c0, t_tu__yc.pkey as c1, t_tu__yc.c_q03lu as c2, t_tu__...
     - Transaction: conn_0
     - Output: [(11, 60000, 70.67, 'evl_3b', '1epdod', 'uudutd', 75, None, None)]
     - Executed order: 101
     - Affected rows / Warnings: 1 / 0
 * Instruction #102:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 102
     - Affected rows / Warnings: 0 / 0

 * Container logs:
   No logs available.
