# Bug ID MDEV-29565-SERIALIZABLE

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-29565
Original isolation level: REPEATABLE READ
Tested isolation level:   SERIALIZABLE
Description:              The two returned selects have different number of entries.


## Details
 * Database: mariadb-10.8.3
 * Number of scenarios: 1
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
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
     - Transaction: conn_1
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_1
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 0 / 0
 * Instruction #3:
     - Instruction:  update t_g6ckkb set wkey = 162;
     - Transaction: conn_1
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 2 / 0
 * Instruction #4:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows / Warnings: 0 / 0
 * Instruction #5:
     - Instruction:  select * from t_g6ckkb;
     - Transaction: conn_0
     - Output: [(162, 234000, None, 'aarauc', 'btldnb', 37.9, '7wa_b', None, 32.5), (162, 327000, 65, 'kavsib', 'ga9slb', 54.9, None, 'xlbvfd', 79.9)]
     - Executed order: 5
     - Affected rows / Warnings: 2 / 0
 * Instruction #6:
     - Instruction:  COMMIT;
     - Transaction: conn_1
     - Output: None
     - Executed order: 6
     - Affected rows / Warnings: 0 / 0
 * Instruction #7:
     - Instruction:  select * from t_rpjlsd where t_rpjlsd.c_pfd8ab <= (select min(wkey) from t_g6ck...
     - Transaction: conn_0
     - Output: [(43, 243000, 30, None, 8, None, 70, None, 'awnrab', 39.83), (57, 332000, 68, '_pqr1c', 53, '9g7bt', None, 75, 'tb1ugc', 7.62)]
     - Executed order: 7
     - Affected rows / Warnings: 2 / 0
 * Instruction #8:
     - Instruction:  update t_rpjlsd set wkey = 63 where t_rpjlsd.c_pfd8ab <= (select min(wkey) from...
     - Transaction: conn_0
     - Output: None
     - Executed order: 8
     - Affected rows / Warnings: 2 / 0
 * Instruction #9:
     - Instruction:  select * from t_rpjlsd where wkey = 63;
     - Transaction: conn_0
     - Output: [(63, 243000, 30, None, 8, None, 70, None, 'awnrab', 39.83), (63, 332000, 68, '_pqr1c', 53, '9g7bt', None, 75, 'tb1ugc', 7.62)]
     - Executed order: 9
     - Affected rows / Warnings: 2 / 0
 * Instruction #10:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 10
     - Affected rows / Warnings: 0 / 0

 * Container logs:
   No logs available.
