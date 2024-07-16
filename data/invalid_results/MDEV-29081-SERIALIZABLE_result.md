# Bug ID MDEV-29081-SERIALIZABLE

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-29081
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
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 0 / 0
 * Instruction #3:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 0 / 0
 * Instruction #4:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows / Warnings: 0 / 0
 * Instruction #5:
     - Instruction:  delete from t__cwzpb where t__cwzpb.c__xujbd is not NULL;
     - Transaction: conn_0
     - Output: None
     - Executed order: 5
     - Affected rows / Warnings: 11 / 0
 * Instruction #6:
     - Instruction:  update t_khn17c set wkey = 187, c_ci0ked = coalesce(case when 54 <= t_khn17c.pk...
     - Transaction: conn_0
     - Output: None
     - Executed order: 6
     - Affected rows / Warnings: 37 / 0
 * Instruction #7:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 7
     - Affected rows / Warnings: 0 / 0
 * Instruction #8:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 8
     - Affected rows / Warnings: 0 / 0
 * Instruction #9:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 9
     - Affected rows / Warnings: 0 / 0
 * Instruction #10:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 10
     - Affected rows / Warnings: 0 / 0
 * Instruction #11:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 11
     - Affected rows / Warnings: 0 / 0
 * Instruction #12:
     - Instruction:  update t_khn17c set wkey = 231, c_ci0ked = 78.57, c_qdo5gb = t_khn17c.pkey wher...
     - Transaction: conn_0
     - Output: None
     - Executed order: 12
     - Affected rows / Warnings: 37 / 0
 * Instruction #13:
     - Instruction:  select ref_0.wkey as c0, ref_0.pkey as c1, ref_0.c_hzulvc as c2, ref_0.c_6udum ...
     - Transaction: conn_0
     - Output: [(1, 12000, 'k_my4b', 6, None, 'ecexid', None, 11, None, None, 91), (1, 14000, 'gx8rvc', 89, None, 'lowfcb', 'c9j0fc', 53, None, None, 62), (2, 19000, '61jaub', None, 'lzmyh', '5_ot1d', None, 33, None, None, 43), (2, 20000, 'avvyv', None, '3czzjc', 'xuhtec', None, 17, 21.56, None, 81), (2, 22000, 'nw3tv', None, 'c9sq1c', 'bsife', None, 47, 22.9, None, 86), (8, 55000, None, None, None, 'm2hh5c', '_k8tfb', 23, 22.79, 17, 56), (13, 85000, 'nojild', 95, 'mazn2d', 'q_y6ad', 'qvqasb', 27, 66.13, 47, 57)]
     - Executed order: 13
     - Affected rows / Warnings: 7 / 0
 * Instruction #14:
     - Instruction:  select ref_0.wkey as c0, ref_0.pkey as c1, ref_0.c__xujbd as c2, ref_0.c_hs9pic...
     - Transaction: conn_0
     - Output: [(14, 89000, None, 36, 73, 92.79, 'av3tu', None, 'cw1nn', None, 92.5), (14, 91000, None, 44, 38, 82.85, 'khn4z', 28.43, 'zolrj', None, 30.59)]
     - Executed order: 14
     - Affected rows / Warnings: 2 / 0
 * Instruction #15:
     - Instruction:  update t_khn17c set wkey = 239, c_qdo5gb = t_khn17c.pkey where exists ( select ...
     - Transaction: conn_0
     - Output: None
     - Executed order: 15
     - Affected rows / Warnings: 37 / 0
 * Instruction #16:
     - Instruction:  ROLLBACK;
     - Transaction: conn_0
     - Output: None
     - Executed order: 16
     - Affected rows / Warnings: 0 / 0
 * Instruction #17:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 17
     - Affected rows / Warnings: 0 / 0
 * Instruction #18:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 18
     - Affected rows / Warnings: 0 / 0
 * Instruction #19:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 19
     - Affected rows / Warnings: 0 / 0
 * Instruction #20:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 20
     - Affected rows / Warnings: 0 / 0
 * Instruction #21:
     - Instruction:  WITH cte_0 AS (select ref_0.wkey as c0, ref_0.pkey as c1, ref_0.c_ci0ked as c2,...
     - Transaction: conn_0
     - Output: []
     - Executed order: 21
     - Affected rows / Warnings: 0 / 3
 * Instruction #22:
     - Instruction:  update t_khn17c set wkey = 158, c_ci0ked = PI(), c_qdo5gb = t_khn17c.pkey where...
     - Transaction: conn_0
     - Output: None
     - Executed order: 22
     - Affected rows / Warnings: 37 / 0
 * Instruction #23:
     - Instruction:  insert into t_khn17c (wkey, pkey, c_ci0ked, c_qdo5gb) values (82, 152000, PI(),...
     - Transaction: conn_0
     - Output: None
     - Executed order: 23
     - Affected rows / Warnings: 8 / 0
 * Instruction #24:
     - Instruction:  insert into t_khn17c (wkey, pkey, c_ci0ked, c_qdo5gb) values (93, 219000, 8.29,...
     - Transaction: conn_0
     - Output: None
     - Executed order: 24
     - Affected rows / Warnings: 4 / 0
 * Instruction #25:
     - Instruction:  update t_khn17c set wkey = 96, c_qdo5gb = t_khn17c.pkey where t_khn17c.wkey bet...
     - Transaction: conn_0
     - Output: None
     - Executed order: 25
     - Affected rows / Warnings: 12 / 0
 * Instruction #26:
     - Instruction:  delete from t_khn17c where t_khn17c.wkey >= case when t_khn17c.pkey between t_k...
     - Transaction: conn_0
     - Output: None
     - Executed order: 26
     - Affected rows / Warnings: 49 / 0
 * Instruction #27:
     - Instruction:  update t_khn17c set wkey = 119, c_qdo5gb = t_khn17c.pkey where 1 = 1 and (t_khn...
     - Transaction: conn_0
     - Output: None
     - Executed order: 27
     - Affected rows / Warnings: 0 / 0
 * Instruction #28:
     - Instruction:  delete from t_2nqc_c where t_2nqc_c.c_ijrc5 not in ( t_2nqc_c.pkey, CHAR_LENGTH...
     - Transaction: conn_0
     - Output: None
     - Executed order: 28
     - Affected rows / Warnings: 15 / 0
 * Instruction #29:
     - Instruction:  ROLLBACK;
     - Transaction: conn_0
     - Output: None
     - Executed order: 29
     - Affected rows / Warnings: 0 / 0
 * Instruction #30:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 30
     - Affected rows / Warnings: 0 / 0
 * Instruction #31:
     - Instruction:  delete from t__cwzpb where t__cwzpb.c_vjulib is NULL;
     - Transaction: conn_0
     - Output: None
     - Executed order: 31
     - Affected rows / Warnings: 1 / 0
 * Instruction #32:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 32
     - Affected rows / Warnings: 0 / 0
 * Instruction #33:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 33
     - Affected rows / Warnings: 0 / 0
 * Instruction #34:
     - Instruction:  ROLLBACK;
     - Transaction: conn_0
     - Output: None
     - Executed order: 34
     - Affected rows / Warnings: 0 / 0
 * Instruction #35:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 35
     - Affected rows / Warnings: 0 / 0
 * Instruction #36:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 36
     - Affected rows / Warnings: 0 / 0
 * Instruction #37:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 37
     - Affected rows / Warnings: 0 / 0
 * Instruction #38:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 38
     - Affected rows / Warnings: 0 / 0
 * Instruction #39:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 39
     - Affected rows / Warnings: 0 / 0
 * Instruction #40:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 40
     - Affected rows / Warnings: 0 / 0
 * Instruction #41:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 41
     - Affected rows / Warnings: 0 / 0
 * Instruction #42:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 42
     - Affected rows / Warnings: 0 / 0
 * Instruction #43:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 43
     - Affected rows / Warnings: 0 / 0
 * Instruction #44:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 44
     - Affected rows / Warnings: 0 / 0
 * Instruction #45:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 45
     - Affected rows / Warnings: 0 / 0
 * Instruction #46:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 46
     - Affected rows / Warnings: 0 / 0
 * Instruction #47:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 47
     - Affected rows / Warnings: 0 / 0
 * Instruction #48:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 48
     - Affected rows / Warnings: 0 / 0
 * Instruction #49:
     - Instruction:  insert into t__cwzpb (wkey, pkey, c__xujbd, c_vlrpid, c_nagjcb, c_3eervc, c_enx...
     - Transaction: conn_0
     - Output: None
     - Executed order: 49
     - Affected rows / Warnings: 7 / 2
 * Instruction #50:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 50
     - Affected rows / Warnings: 0 / 0
 * Instruction #51:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 51
     - Affected rows / Warnings: 0 / 0
 * Instruction #52:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 52
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
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 0 / 0
 * Instruction #3:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 0 / 0
 * Instruction #4:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows / Warnings: 0 / 0
 * Instruction #5:
     - Instruction:  delete from t__cwzpb where t__cwzpb.c__xujbd is not NULL;
     - Transaction: conn_0
     - Output: None
     - Executed order: 5
     - Affected rows / Warnings: 11 / 0
 * Instruction #6:
     - Instruction:  update t_khn17c set wkey = 187, c_ci0ked = coalesce(case when 54 <= t_khn17c.pk...
     - Transaction: conn_0
     - Output: None
     - Executed order: 6
     - Affected rows / Warnings: 37 / 0
 * Instruction #7:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 7
     - Affected rows / Warnings: 0 / 0
 * Instruction #8:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 8
     - Affected rows / Warnings: 0 / 0
 * Instruction #9:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 9
     - Affected rows / Warnings: 0 / 0
 * Instruction #10:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 10
     - Affected rows / Warnings: 0 / 0
 * Instruction #11:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 11
     - Affected rows / Warnings: 0 / 0
 * Instruction #12:
     - Instruction:  update t_khn17c set wkey = 231, c_ci0ked = 78.57, c_qdo5gb = t_khn17c.pkey wher...
     - Transaction: conn_0
     - Output: None
     - Executed order: 12
     - Affected rows / Warnings: 37 / 0
 * Instruction #13:
     - Instruction:  select ref_0.wkey as c0, ref_0.pkey as c1, ref_0.c_hzulvc as c2, ref_0.c_6udum ...
     - Transaction: conn_0
     - Output: [(1, 12000, 'k_my4b', 6, None, 'ecexid', None, 11, None, None, 91), (1, 14000, 'gx8rvc', 89, None, 'lowfcb', 'c9j0fc', 53, None, None, 62), (2, 19000, '61jaub', None, 'lzmyh', '5_ot1d', None, 33, None, None, 43), (2, 20000, 'avvyv', None, '3czzjc', 'xuhtec', None, 17, 21.56, None, 81), (2, 22000, 'nw3tv', None, 'c9sq1c', 'bsife', None, 47, 22.9, None, 86), (8, 55000, None, None, None, 'm2hh5c', '_k8tfb', 23, 22.79, 17, 56), (13, 85000, 'nojild', 95, 'mazn2d', 'q_y6ad', 'qvqasb', 27, 66.13, 47, 57)]
     - Executed order: 13
     - Affected rows / Warnings: 7 / 0
 * Instruction #14:
     - Instruction:  select ref_0.wkey as c0, ref_0.pkey as c1, ref_0.c__xujbd as c2, ref_0.c_hs9pic...
     - Transaction: conn_0
     - Output: [(14, 89000, None, 36, 73, 92.79, 'av3tu', None, 'cw1nn', None, 92.5), (14, 91000, None, 44, 38, 82.85, 'khn4z', 28.43, 'zolrj', None, 30.59)]
     - Executed order: 14
     - Affected rows / Warnings: 2 / 0
 * Instruction #15:
     - Instruction:  update t_khn17c set wkey = 239, c_qdo5gb = t_khn17c.pkey where exists ( select ...
     - Transaction: conn_0
     - Output: None
     - Executed order: 15
     - Affected rows / Warnings: 37 / 0
 * Instruction #16:
     - Instruction:  ROLLBACK;
     - Transaction: conn_0
     - Output: None
     - Executed order: 16
     - Affected rows / Warnings: 0 / 0
 * Instruction #17:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 17
     - Affected rows / Warnings: 0 / 0
 * Instruction #18:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 18
     - Affected rows / Warnings: 0 / 0
 * Instruction #19:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 19
     - Affected rows / Warnings: 0 / 0
 * Instruction #20:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 20
     - Affected rows / Warnings: 0 / 0
 * Instruction #21:
     - Instruction:  WITH cte_0 AS (select ref_0.wkey as c0, ref_0.pkey as c1, ref_0.c_ci0ked as c2,...
     - Transaction: conn_0
     - Output: []
     - Executed order: 21
     - Affected rows / Warnings: 0 / 3
 * Instruction #22:
     - Instruction:  update t_khn17c set wkey = 158, c_ci0ked = PI(), c_qdo5gb = t_khn17c.pkey where...
     - Transaction: conn_0
     - Output: None
     - Executed order: 22
     - Affected rows / Warnings: 37 / 0
 * Instruction #23:
     - Instruction:  insert into t_khn17c (wkey, pkey, c_ci0ked, c_qdo5gb) values (82, 152000, PI(),...
     - Transaction: conn_0
     - Output: None
     - Executed order: 23
     - Affected rows / Warnings: 8 / 0
 * Instruction #24:
     - Instruction:  insert into t_khn17c (wkey, pkey, c_ci0ked, c_qdo5gb) values (93, 219000, 8.29,...
     - Transaction: conn_0
     - Output: None
     - Executed order: 24
     - Affected rows / Warnings: 4 / 0
 * Instruction #25:
     - Instruction:  update t_khn17c set wkey = 96, c_qdo5gb = t_khn17c.pkey where t_khn17c.wkey bet...
     - Transaction: conn_0
     - Output: None
     - Executed order: 25
     - Affected rows / Warnings: 12 / 0
 * Instruction #26:
     - Instruction:  delete from t_khn17c where t_khn17c.wkey >= case when t_khn17c.pkey between t_k...
     - Transaction: conn_0
     - Output: None
     - Executed order: 26
     - Affected rows / Warnings: 49 / 0
 * Instruction #27:
     - Instruction:  update t_khn17c set wkey = 119, c_qdo5gb = t_khn17c.pkey where 1 = 1 and (t_khn...
     - Transaction: conn_0
     - Output: None
     - Executed order: 27
     - Affected rows / Warnings: 0 / 0
 * Instruction #28:
     - Instruction:  delete from t_2nqc_c where t_2nqc_c.c_ijrc5 not in ( t_2nqc_c.pkey, CHAR_LENGTH...
     - Transaction: conn_0
     - Output: None
     - Executed order: 28
     - Affected rows / Warnings: 15 / 0
 * Instruction #29:
     - Instruction:  ROLLBACK;
     - Transaction: conn_0
     - Output: None
     - Executed order: 29
     - Affected rows / Warnings: 0 / 0
 * Instruction #30:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 30
     - Affected rows / Warnings: 0 / 0
 * Instruction #31:
     - Instruction:  delete from t__cwzpb where t__cwzpb.c_vjulib is NULL;
     - Transaction: conn_0
     - Output: None
     - Executed order: 31
     - Affected rows / Warnings: 1 / 0
 * Instruction #32:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 32
     - Affected rows / Warnings: 0 / 0
 * Instruction #33:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 33
     - Affected rows / Warnings: 0 / 0
 * Instruction #34:
     - Instruction:  ROLLBACK;
     - Transaction: conn_0
     - Output: None
     - Executed order: 34
     - Affected rows / Warnings: 0 / 0
 * Instruction #35:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 35
     - Affected rows / Warnings: 0 / 0
 * Instruction #36:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 36
     - Affected rows / Warnings: 0 / 0
 * Instruction #37:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 37
     - Affected rows / Warnings: 0 / 0
 * Instruction #38:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 38
     - Affected rows / Warnings: 0 / 0
 * Instruction #39:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 39
     - Affected rows / Warnings: 0 / 0
 * Instruction #40:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 40
     - Affected rows / Warnings: 0 / 0
 * Instruction #41:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 41
     - Affected rows / Warnings: 0 / 0
 * Instruction #42:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 42
     - Affected rows / Warnings: 0 / 0
 * Instruction #43:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 43
     - Affected rows / Warnings: 0 / 0
 * Instruction #44:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 44
     - Affected rows / Warnings: 0 / 0
 * Instruction #45:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 45
     - Affected rows / Warnings: 0 / 0
 * Instruction #46:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 46
     - Affected rows / Warnings: 0 / 0
 * Instruction #47:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 47
     - Affected rows / Warnings: 0 / 0
 * Instruction #48:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 48
     - Affected rows / Warnings: 0 / 0
 * Instruction #49:
     - Instruction:  insert into t__cwzpb (wkey, pkey, c__xujbd, c_vlrpid, c_nagjcb, c_3eervc, c_enx...
     - Transaction: conn_0
     - Output: None
     - Executed order: 49
     - Affected rows / Warnings: 7 / 2
 * Instruction #50:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 50
     - Affected rows / Warnings: 0 / 0
 * Instruction #51:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 51
     - Affected rows / Warnings: 0 / 0
 * Instruction #52:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 52
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
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 0 / 0
 * Instruction #3:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 0 / 0
 * Instruction #4:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows / Warnings: 0 / 0
 * Instruction #5:
     - Instruction:  delete from t__cwzpb where t__cwzpb.c__xujbd is not NULL;
     - Transaction: conn_0
     - Output: None
     - Executed order: 5
     - Affected rows / Warnings: 11 / 0
 * Instruction #6:
     - Instruction:  update t_khn17c set wkey = 187, c_ci0ked = coalesce(case when 54 <= t_khn17c.pk...
     - Transaction: conn_0
     - Output: None
     - Executed order: 6
     - Affected rows / Warnings: 37 / 0
 * Instruction #7:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 7
     - Affected rows / Warnings: 0 / 0
 * Instruction #8:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 8
     - Affected rows / Warnings: 0 / 0
 * Instruction #9:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 9
     - Affected rows / Warnings: 0 / 0
 * Instruction #10:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 10
     - Affected rows / Warnings: 0 / 0
 * Instruction #11:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 11
     - Affected rows / Warnings: 0 / 0
 * Instruction #12:
     - Instruction:  update t_khn17c set wkey = 231, c_ci0ked = 78.57, c_qdo5gb = t_khn17c.pkey wher...
     - Transaction: conn_0
     - Output: None
     - Executed order: 12
     - Affected rows / Warnings: 37 / 0
 * Instruction #13:
     - Instruction:  select ref_0.wkey as c0, ref_0.pkey as c1, ref_0.c_hzulvc as c2, ref_0.c_6udum ...
     - Transaction: conn_0
     - Output: [(1, 12000, 'k_my4b', 6, None, 'ecexid', None, 11, None, None, 91), (1, 14000, 'gx8rvc', 89, None, 'lowfcb', 'c9j0fc', 53, None, None, 62), (2, 19000, '61jaub', None, 'lzmyh', '5_ot1d', None, 33, None, None, 43), (2, 20000, 'avvyv', None, '3czzjc', 'xuhtec', None, 17, 21.56, None, 81), (2, 22000, 'nw3tv', None, 'c9sq1c', 'bsife', None, 47, 22.9, None, 86), (8, 55000, None, None, None, 'm2hh5c', '_k8tfb', 23, 22.79, 17, 56), (13, 85000, 'nojild', 95, 'mazn2d', 'q_y6ad', 'qvqasb', 27, 66.13, 47, 57)]
     - Executed order: 13
     - Affected rows / Warnings: 7 / 0
 * Instruction #14:
     - Instruction:  select ref_0.wkey as c0, ref_0.pkey as c1, ref_0.c__xujbd as c2, ref_0.c_hs9pic...
     - Transaction: conn_0
     - Output: [(14, 89000, None, 36, 73, 92.79, 'av3tu', None, 'cw1nn', None, 92.5), (14, 91000, None, 44, 38, 82.85, 'khn4z', 28.43, 'zolrj', None, 30.59)]
     - Executed order: 14
     - Affected rows / Warnings: 2 / 0
 * Instruction #15:
     - Instruction:  update t_khn17c set wkey = 239, c_qdo5gb = t_khn17c.pkey where exists ( select ...
     - Transaction: conn_0
     - Output: None
     - Executed order: 15
     - Affected rows / Warnings: 37 / 0
 * Instruction #16:
     - Instruction:  ROLLBACK;
     - Transaction: conn_0
     - Output: None
     - Executed order: 16
     - Affected rows / Warnings: 0 / 0
 * Instruction #17:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 17
     - Affected rows / Warnings: 0 / 0
 * Instruction #18:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 18
     - Affected rows / Warnings: 0 / 0
 * Instruction #19:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 19
     - Affected rows / Warnings: 0 / 0
 * Instruction #20:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 20
     - Affected rows / Warnings: 0 / 0
 * Instruction #21:
     - Instruction:  WITH cte_0 AS (select ref_0.wkey as c0, ref_0.pkey as c1, ref_0.c_ci0ked as c2,...
     - Transaction: conn_0
     - Output: []
     - Executed order: 21
     - Affected rows / Warnings: 0 / 3
 * Instruction #22:
     - Instruction:  update t_khn17c set wkey = 158, c_ci0ked = PI(), c_qdo5gb = t_khn17c.pkey where...
     - Transaction: conn_0
     - Output: None
     - Executed order: 22
     - Affected rows / Warnings: 37 / 0
 * Instruction #23:
     - Instruction:  insert into t_khn17c (wkey, pkey, c_ci0ked, c_qdo5gb) values (82, 152000, PI(),...
     - Transaction: conn_0
     - Output: None
     - Executed order: 23
     - Affected rows / Warnings: 8 / 0
 * Instruction #24:
     - Instruction:  insert into t_khn17c (wkey, pkey, c_ci0ked, c_qdo5gb) values (93, 219000, 8.29,...
     - Transaction: conn_0
     - Output: None
     - Executed order: 24
     - Affected rows / Warnings: 4 / 0
 * Instruction #25:
     - Instruction:  update t_khn17c set wkey = 96, c_qdo5gb = t_khn17c.pkey where t_khn17c.wkey bet...
     - Transaction: conn_0
     - Output: None
     - Executed order: 25
     - Affected rows / Warnings: 12 / 0
 * Instruction #26:
     - Instruction:  delete from t_khn17c where t_khn17c.wkey >= case when t_khn17c.pkey between t_k...
     - Transaction: conn_0
     - Output: None
     - Executed order: 26
     - Affected rows / Warnings: 49 / 0
 * Instruction #27:
     - Instruction:  update t_khn17c set wkey = 119, c_qdo5gb = t_khn17c.pkey where 1 = 1 and (t_khn...
     - Transaction: conn_0
     - Output: None
     - Executed order: 27
     - Affected rows / Warnings: 0 / 0
 * Instruction #28:
     - Instruction:  delete from t_2nqc_c where t_2nqc_c.c_ijrc5 not in ( t_2nqc_c.pkey, CHAR_LENGTH...
     - Transaction: conn_0
     - Output: None
     - Executed order: 28
     - Affected rows / Warnings: 15 / 0
 * Instruction #29:
     - Instruction:  ROLLBACK;
     - Transaction: conn_0
     - Output: None
     - Executed order: 29
     - Affected rows / Warnings: 0 / 0
 * Instruction #30:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 30
     - Affected rows / Warnings: 0 / 0
 * Instruction #31:
     - Instruction:  delete from t__cwzpb where t__cwzpb.c_vjulib is NULL;
     - Transaction: conn_0
     - Output: None
     - Executed order: 31
     - Affected rows / Warnings: 1 / 0
 * Instruction #32:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 32
     - Affected rows / Warnings: 0 / 0
 * Instruction #33:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 33
     - Affected rows / Warnings: 0 / 0
 * Instruction #34:
     - Instruction:  ROLLBACK;
     - Transaction: conn_0
     - Output: None
     - Executed order: 34
     - Affected rows / Warnings: 0 / 0
 * Instruction #35:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 35
     - Affected rows / Warnings: 0 / 0
 * Instruction #36:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 36
     - Affected rows / Warnings: 0 / 0
 * Instruction #37:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 37
     - Affected rows / Warnings: 0 / 0
 * Instruction #38:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 38
     - Affected rows / Warnings: 0 / 0
 * Instruction #39:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 39
     - Affected rows / Warnings: 0 / 0
 * Instruction #40:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 40
     - Affected rows / Warnings: 0 / 0
 * Instruction #41:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 41
     - Affected rows / Warnings: 0 / 0
 * Instruction #42:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 42
     - Affected rows / Warnings: 0 / 0
 * Instruction #43:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 43
     - Affected rows / Warnings: 0 / 0
 * Instruction #44:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 44
     - Affected rows / Warnings: 0 / 0
 * Instruction #45:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 45
     - Affected rows / Warnings: 0 / 0
 * Instruction #46:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 46
     - Affected rows / Warnings: 0 / 0
 * Instruction #47:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 47
     - Affected rows / Warnings: 0 / 0
 * Instruction #48:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 48
     - Affected rows / Warnings: 0 / 0
 * Instruction #49:
     - Instruction:  insert into t__cwzpb (wkey, pkey, c__xujbd, c_vlrpid, c_nagjcb, c_3eervc, c_enx...
     - Transaction: conn_0
     - Output: None
     - Executed order: 49
     - Affected rows / Warnings: 7 / 2
 * Instruction #50:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 50
     - Affected rows / Warnings: 0 / 0
 * Instruction #51:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 51
     - Affected rows / Warnings: 0 / 0
 * Instruction #52:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 52
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
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 0 / 0
 * Instruction #3:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 0 / 0
 * Instruction #4:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows / Warnings: 0 / 0
 * Instruction #5:
     - Instruction:  delete from t__cwzpb where t__cwzpb.c__xujbd is not NULL;
     - Transaction: conn_0
     - Output: None
     - Executed order: 5
     - Affected rows / Warnings: 11 / 0
 * Instruction #6:
     - Instruction:  update t_khn17c set wkey = 187, c_ci0ked = coalesce(case when 54 <= t_khn17c.pk...
     - Transaction: conn_0
     - Output: None
     - Executed order: 6
     - Affected rows / Warnings: 37 / 0
 * Instruction #7:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 7
     - Affected rows / Warnings: 0 / 0
 * Instruction #8:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 8
     - Affected rows / Warnings: 0 / 0
 * Instruction #9:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 9
     - Affected rows / Warnings: 0 / 0
 * Instruction #10:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 10
     - Affected rows / Warnings: 0 / 0
 * Instruction #11:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 11
     - Affected rows / Warnings: 0 / 0
 * Instruction #12:
     - Instruction:  update t_khn17c set wkey = 231, c_ci0ked = 78.57, c_qdo5gb = t_khn17c.pkey wher...
     - Transaction: conn_0
     - Output: None
     - Executed order: 12
     - Affected rows / Warnings: 37 / 0
 * Instruction #13:
     - Instruction:  select ref_0.wkey as c0, ref_0.pkey as c1, ref_0.c_hzulvc as c2, ref_0.c_6udum ...
     - Transaction: conn_0
     - Output: [(1, 12000, 'k_my4b', 6, None, 'ecexid', None, 11, None, None, 91), (1, 14000, 'gx8rvc', 89, None, 'lowfcb', 'c9j0fc', 53, None, None, 62), (2, 19000, '61jaub', None, 'lzmyh', '5_ot1d', None, 33, None, None, 43), (2, 20000, 'avvyv', None, '3czzjc', 'xuhtec', None, 17, 21.56, None, 81), (2, 22000, 'nw3tv', None, 'c9sq1c', 'bsife', None, 47, 22.9, None, 86), (8, 55000, None, None, None, 'm2hh5c', '_k8tfb', 23, 22.79, 17, 56), (13, 85000, 'nojild', 95, 'mazn2d', 'q_y6ad', 'qvqasb', 27, 66.13, 47, 57)]
     - Executed order: 13
     - Affected rows / Warnings: 7 / 0
 * Instruction #14:
     - Instruction:  select ref_0.wkey as c0, ref_0.pkey as c1, ref_0.c__xujbd as c2, ref_0.c_hs9pic...
     - Transaction: conn_0
     - Output: [(14, 89000, None, 36, 73, 92.79, 'av3tu', None, 'cw1nn', None, 92.5), (14, 91000, None, 44, 38, 82.85, 'khn4z', 28.43, 'zolrj', None, 30.59)]
     - Executed order: 14
     - Affected rows / Warnings: 2 / 0
 * Instruction #15:
     - Instruction:  update t_khn17c set wkey = 239, c_qdo5gb = t_khn17c.pkey where exists ( select ...
     - Transaction: conn_0
     - Output: None
     - Executed order: 15
     - Affected rows / Warnings: 37 / 0
 * Instruction #16:
     - Instruction:  ROLLBACK;
     - Transaction: conn_0
     - Output: None
     - Executed order: 16
     - Affected rows / Warnings: 0 / 0
 * Instruction #17:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 17
     - Affected rows / Warnings: 0 / 0
 * Instruction #18:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 18
     - Affected rows / Warnings: 0 / 0
 * Instruction #19:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 19
     - Affected rows / Warnings: 0 / 0
 * Instruction #20:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 20
     - Affected rows / Warnings: 0 / 0
 * Instruction #21:
     - Instruction:  WITH cte_0 AS (select ref_0.wkey as c0, ref_0.pkey as c1, ref_0.c_ci0ked as c2,...
     - Transaction: conn_0
     - Output: []
     - Executed order: 21
     - Affected rows / Warnings: 0 / 3
 * Instruction #22:
     - Instruction:  update t_khn17c set wkey = 158, c_ci0ked = PI(), c_qdo5gb = t_khn17c.pkey where...
     - Transaction: conn_0
     - Output: None
     - Executed order: 22
     - Affected rows / Warnings: 37 / 0
 * Instruction #23:
     - Instruction:  insert into t_khn17c (wkey, pkey, c_ci0ked, c_qdo5gb) values (82, 152000, PI(),...
     - Transaction: conn_0
     - Output: None
     - Executed order: 23
     - Affected rows / Warnings: 8 / 0
 * Instruction #24:
     - Instruction:  insert into t_khn17c (wkey, pkey, c_ci0ked, c_qdo5gb) values (93, 219000, 8.29,...
     - Transaction: conn_0
     - Output: None
     - Executed order: 24
     - Affected rows / Warnings: 4 / 0
 * Instruction #25:
     - Instruction:  update t_khn17c set wkey = 96, c_qdo5gb = t_khn17c.pkey where t_khn17c.wkey bet...
     - Transaction: conn_0
     - Output: None
     - Executed order: 25
     - Affected rows / Warnings: 12 / 0
 * Instruction #26:
     - Instruction:  delete from t_khn17c where t_khn17c.wkey >= case when t_khn17c.pkey between t_k...
     - Transaction: conn_0
     - Output: None
     - Executed order: 26
     - Affected rows / Warnings: 49 / 0
 * Instruction #27:
     - Instruction:  update t_khn17c set wkey = 119, c_qdo5gb = t_khn17c.pkey where 1 = 1 and (t_khn...
     - Transaction: conn_0
     - Output: None
     - Executed order: 27
     - Affected rows / Warnings: 0 / 0
 * Instruction #28:
     - Instruction:  delete from t_2nqc_c where t_2nqc_c.c_ijrc5 not in ( t_2nqc_c.pkey, CHAR_LENGTH...
     - Transaction: conn_0
     - Output: None
     - Executed order: 28
     - Affected rows / Warnings: 15 / 0
 * Instruction #29:
     - Instruction:  ROLLBACK;
     - Transaction: conn_0
     - Output: None
     - Executed order: 29
     - Affected rows / Warnings: 0 / 0
 * Instruction #30:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 30
     - Affected rows / Warnings: 0 / 0
 * Instruction #31:
     - Instruction:  delete from t__cwzpb where t__cwzpb.c_vjulib is NULL;
     - Transaction: conn_0
     - Output: None
     - Executed order: 31
     - Affected rows / Warnings: 1 / 0
 * Instruction #32:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 32
     - Affected rows / Warnings: 0 / 0
 * Instruction #33:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 33
     - Affected rows / Warnings: 0 / 0
 * Instruction #34:
     - Instruction:  ROLLBACK;
     - Transaction: conn_0
     - Output: None
     - Executed order: 34
     - Affected rows / Warnings: 0 / 0
 * Instruction #35:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 35
     - Affected rows / Warnings: 0 / 0
 * Instruction #36:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 36
     - Affected rows / Warnings: 0 / 0
 * Instruction #37:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 37
     - Affected rows / Warnings: 0 / 0
 * Instruction #38:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 38
     - Affected rows / Warnings: 0 / 0
 * Instruction #39:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 39
     - Affected rows / Warnings: 0 / 0
 * Instruction #40:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 40
     - Affected rows / Warnings: 0 / 0
 * Instruction #41:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 41
     - Affected rows / Warnings: 0 / 0
 * Instruction #42:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 42
     - Affected rows / Warnings: 0 / 0
 * Instruction #43:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 43
     - Affected rows / Warnings: 0 / 0
 * Instruction #44:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 44
     - Affected rows / Warnings: 0 / 0
 * Instruction #45:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 45
     - Affected rows / Warnings: 0 / 0
 * Instruction #46:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 46
     - Affected rows / Warnings: 0 / 0
 * Instruction #47:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 47
     - Affected rows / Warnings: 0 / 0
 * Instruction #48:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 48
     - Affected rows / Warnings: 0 / 0
 * Instruction #49:
     - Instruction:  insert into t__cwzpb (wkey, pkey, c__xujbd, c_vlrpid, c_nagjcb, c_3eervc, c_enx...
     - Transaction: conn_0
     - Output: None
     - Executed order: 49
     - Affected rows / Warnings: 7 / 2
 * Instruction #50:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 50
     - Affected rows / Warnings: 0 / 0
 * Instruction #51:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 51
     - Affected rows / Warnings: 0 / 0
 * Instruction #52:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 52
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
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 0 / 0
 * Instruction #3:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 0 / 0
 * Instruction #4:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
     - Affected rows / Warnings: 0 / 0
 * Instruction #5:
     - Instruction:  delete from t__cwzpb where t__cwzpb.c__xujbd is not NULL;
     - Transaction: conn_0
     - Output: None
     - Executed order: 5
     - Affected rows / Warnings: 11 / 0
 * Instruction #6:
     - Instruction:  update t_khn17c set wkey = 187, c_ci0ked = coalesce(case when 54 <= t_khn17c.pk...
     - Transaction: conn_0
     - Output: None
     - Executed order: 6
     - Affected rows / Warnings: 37 / 0
 * Instruction #7:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 7
     - Affected rows / Warnings: 0 / 0
 * Instruction #8:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 8
     - Affected rows / Warnings: 0 / 0
 * Instruction #9:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 9
     - Affected rows / Warnings: 0 / 0
 * Instruction #10:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 10
     - Affected rows / Warnings: 0 / 0
 * Instruction #11:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 11
     - Affected rows / Warnings: 0 / 0
 * Instruction #12:
     - Instruction:  update t_khn17c set wkey = 231, c_ci0ked = 78.57, c_qdo5gb = t_khn17c.pkey wher...
     - Transaction: conn_0
     - Output: None
     - Executed order: 12
     - Affected rows / Warnings: 37 / 0
 * Instruction #13:
     - Instruction:  select ref_0.wkey as c0, ref_0.pkey as c1, ref_0.c_hzulvc as c2, ref_0.c_6udum ...
     - Transaction: conn_0
     - Output: [(1, 12000, 'k_my4b', 6, None, 'ecexid', None, 11, None, None, 91), (1, 14000, 'gx8rvc', 89, None, 'lowfcb', 'c9j0fc', 53, None, None, 62), (2, 19000, '61jaub', None, 'lzmyh', '5_ot1d', None, 33, None, None, 43), (2, 20000, 'avvyv', None, '3czzjc', 'xuhtec', None, 17, 21.56, None, 81), (2, 22000, 'nw3tv', None, 'c9sq1c', 'bsife', None, 47, 22.9, None, 86), (8, 55000, None, None, None, 'm2hh5c', '_k8tfb', 23, 22.79, 17, 56), (13, 85000, 'nojild', 95, 'mazn2d', 'q_y6ad', 'qvqasb', 27, 66.13, 47, 57)]
     - Executed order: 13
     - Affected rows / Warnings: 7 / 0
 * Instruction #14:
     - Instruction:  select ref_0.wkey as c0, ref_0.pkey as c1, ref_0.c__xujbd as c2, ref_0.c_hs9pic...
     - Transaction: conn_0
     - Output: [(14, 89000, None, 36, 73, 92.79, 'av3tu', None, 'cw1nn', None, 92.5), (14, 91000, None, 44, 38, 82.85, 'khn4z', 28.43, 'zolrj', None, 30.59)]
     - Executed order: 14
     - Affected rows / Warnings: 2 / 0
 * Instruction #15:
     - Instruction:  update t_khn17c set wkey = 239, c_qdo5gb = t_khn17c.pkey where exists ( select ...
     - Transaction: conn_0
     - Output: None
     - Executed order: 15
     - Affected rows / Warnings: 37 / 0
 * Instruction #16:
     - Instruction:  ROLLBACK;
     - Transaction: conn_0
     - Output: None
     - Executed order: 16
     - Affected rows / Warnings: 0 / 0
 * Instruction #17:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 17
     - Affected rows / Warnings: 0 / 0
 * Instruction #18:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 18
     - Affected rows / Warnings: 0 / 0
 * Instruction #19:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 19
     - Affected rows / Warnings: 0 / 0
 * Instruction #20:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 20
     - Affected rows / Warnings: 0 / 0
 * Instruction #21:
     - Instruction:  WITH cte_0 AS (select ref_0.wkey as c0, ref_0.pkey as c1, ref_0.c_ci0ked as c2,...
     - Transaction: conn_0
     - Output: []
     - Executed order: 21
     - Affected rows / Warnings: 0 / 3
 * Instruction #22:
     - Instruction:  update t_khn17c set wkey = 158, c_ci0ked = PI(), c_qdo5gb = t_khn17c.pkey where...
     - Transaction: conn_0
     - Output: None
     - Executed order: 22
     - Affected rows / Warnings: 37 / 0
 * Instruction #23:
     - Instruction:  insert into t_khn17c (wkey, pkey, c_ci0ked, c_qdo5gb) values (82, 152000, PI(),...
     - Transaction: conn_0
     - Output: None
     - Executed order: 23
     - Affected rows / Warnings: 8 / 0
 * Instruction #24:
     - Instruction:  insert into t_khn17c (wkey, pkey, c_ci0ked, c_qdo5gb) values (93, 219000, 8.29,...
     - Transaction: conn_0
     - Output: None
     - Executed order: 24
     - Affected rows / Warnings: 4 / 0
 * Instruction #25:
     - Instruction:  update t_khn17c set wkey = 96, c_qdo5gb = t_khn17c.pkey where t_khn17c.wkey bet...
     - Transaction: conn_0
     - Output: None
     - Executed order: 25
     - Affected rows / Warnings: 12 / 0
 * Instruction #26:
     - Instruction:  delete from t_khn17c where t_khn17c.wkey >= case when t_khn17c.pkey between t_k...
     - Transaction: conn_0
     - Output: None
     - Executed order: 26
     - Affected rows / Warnings: 49 / 0
 * Instruction #27:
     - Instruction:  update t_khn17c set wkey = 119, c_qdo5gb = t_khn17c.pkey where 1 = 1 and (t_khn...
     - Transaction: conn_0
     - Output: None
     - Executed order: 27
     - Affected rows / Warnings: 0 / 0
 * Instruction #28:
     - Instruction:  delete from t_2nqc_c where t_2nqc_c.c_ijrc5 not in ( t_2nqc_c.pkey, CHAR_LENGTH...
     - Transaction: conn_0
     - Output: None
     - Executed order: 28
     - Affected rows / Warnings: 15 / 0
 * Instruction #29:
     - Instruction:  ROLLBACK;
     - Transaction: conn_0
     - Output: None
     - Executed order: 29
     - Affected rows / Warnings: 0 / 0
 * Instruction #30:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 30
     - Affected rows / Warnings: 0 / 0
 * Instruction #31:
     - Instruction:  delete from t__cwzpb where t__cwzpb.c_vjulib is NULL;
     - Transaction: conn_0
     - Output: None
     - Executed order: 31
     - Affected rows / Warnings: 1 / 0
 * Instruction #32:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 32
     - Affected rows / Warnings: 0 / 0
 * Instruction #33:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 33
     - Affected rows / Warnings: 0 / 0
 * Instruction #34:
     - Instruction:  ROLLBACK;
     - Transaction: conn_0
     - Output: None
     - Executed order: 34
     - Affected rows / Warnings: 0 / 0
 * Instruction #35:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 35
     - Affected rows / Warnings: 0 / 0
 * Instruction #36:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 36
     - Affected rows / Warnings: 0 / 0
 * Instruction #37:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 37
     - Affected rows / Warnings: 0 / 0
 * Instruction #38:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 38
     - Affected rows / Warnings: 0 / 0
 * Instruction #39:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 39
     - Affected rows / Warnings: 0 / 0
 * Instruction #40:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 40
     - Affected rows / Warnings: 0 / 0
 * Instruction #41:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 41
     - Affected rows / Warnings: 0 / 0
 * Instruction #42:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 42
     - Affected rows / Warnings: 0 / 0
 * Instruction #43:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 43
     - Affected rows / Warnings: 0 / 0
 * Instruction #44:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 44
     - Affected rows / Warnings: 0 / 0
 * Instruction #45:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 45
     - Affected rows / Warnings: 0 / 0
 * Instruction #46:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 46
     - Affected rows / Warnings: 0 / 0
 * Instruction #47:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 47
     - Affected rows / Warnings: 0 / 0
 * Instruction #48:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 48
     - Affected rows / Warnings: 0 / 0
 * Instruction #49:
     - Instruction:  insert into t__cwzpb (wkey, pkey, c__xujbd, c_vlrpid, c_nagjcb, c_3eervc, c_enx...
     - Transaction: conn_0
     - Output: None
     - Executed order: 49
     - Affected rows / Warnings: 7 / 2
 * Instruction #50:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 50
     - Affected rows / Warnings: 0 / 0
 * Instruction #51:
     - Instruction:  SELECT 1 WHERE 0 <> 0;
     - Transaction: conn_0
     - Output: []
     - Executed order: 51
     - Affected rows / Warnings: 0 / 0
 * Instruction #52:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 52
     - Affected rows / Warnings: 0 / 0

 * Container logs:
   No logs available.
