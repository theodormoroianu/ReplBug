# Bug ID MDEV-16675-SERIALIZABLE

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-16675
Original isolation level: REPEATABLE READ
Tested isolation level:   SERIALIZABLE
Description:              In this test, there is no conflict, and the DELETE statement should not convert the implicit lock into an explicit one. But, the function lock_rec_convert_impl_to_expl_for_trx() is being invoked during the test.


## Details
 * Database: mariadb-10.3.8-debug
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
     - Instruction:  BEGIN;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  INSERT INTO t1 VALUES(1,1,'a'),(2,9999,'b'),(3,10000,'c'),(4,4,'d');
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows / Warnings: 4 / 0
 * Instruction #3:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 0 / 0

 * Container logs:
   > 2024-07-18 19:06:05 0 [Warning] lock_rec_convert_impl_to_expl_for_trx was called for index 18, trx 144
   > 2024-07-18 19:06:05 0 [Warning] lock_rec_convert_impl_to_expl_for_trx was called for index 18, trx 144
   > 2024-07-18 19:06:05 0 [Warning] lock_rec_convert_impl_to_expl_for_trx was called for index 19, trx 146
   > 2024-07-18 19:06:05 0 [Warning] lock_rec_convert_impl_to_expl_for_trx was called for index 19, trx 146
   > 2024-07-18 19:06:05 0 [Warning] lock_rec_convert_impl_to_expl_for_trx was called for index 19, trx 146
   > 2024-07-18 19:06:05 0 [Warning] lock_rec_convert_impl_to_expl_for_trx was called for index 19, trx 146
   > 2024-07-18 19:06:05 0 [Warning] lock_rec_convert_impl_to_expl_for_trx was called for index 19, trx 146
   > 2024-07-18 19:06:05 0 [Warning] lock_rec_convert_impl_to_expl_for_trx was called for index 19, trx 146
   > 2024-07-18 19:06:05 0 [Warning] lock_rec_convert_impl_to_expl_for_trx was called for index 19, trx 146
   > 2024-07-18 19:06:05 0 [Warning] lock_rec_convert_impl_to_expl_for_trx was called for index 19, trx 146
   > 2024-07-18 19:06:05 0 [Warning] lock_rec_convert_impl_to_expl_for_trx was called for index 19, trx 146
   > 2024-07-18 19:06:05 0 [Warning] lock_rec_convert_impl_to_expl_for_trx was called for index 19, trx 146
   > 2024-07-18 19:06:05 0 [Warning] lock_rec_convert_impl_to_expl_for_trx was called for index 19, trx 146
   > 2024-07-18 19:06:05 0 [Warning] lock_rec_convert_impl_to_expl_for_trx was called for index 19, trx 146
   > 2024-07-18 19:06:05 0 [Warning] lock_rec_convert_impl_to_expl_for_trx was called for index 19, trx 146
   > 2024-07-18 19:06:05 0 [Warning] lock_rec_convert_impl_to_expl_for_trx was called for index 19, trx 146
