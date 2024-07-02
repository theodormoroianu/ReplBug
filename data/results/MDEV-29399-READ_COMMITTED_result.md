# Bug ID MDEV-29399-READ_COMMITTED

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-29399
Original isolation level: REPEATABLE READ
Tested isolation level:   READ COMMITTED


## Details
 * Database: mariadb-10.8.3
 * Number of scenarios: 2
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
 * Instruction #1:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
 * Instruction #2:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_2
     - Output: None
     - Executed order: 2
 * Instruction #3:
     - Instruction:  update t_j_eqsc set wkey = 37, c_fm792b = PI();
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
 * Instruction #4:
     - Instruction:  COMMIT;
     - Transaction: conn_0
     - Output: None
     - Executed order: 4
 * Instruction #5:
     - Instruction:  START TRANSACTION;
     - Transaction: conn_1
     - Output: None
     - Executed order: 5
 * Instruction #6:
     - Instruction:  insert into t_j_eqsc (wkey, pkey) values (79, 162000);
     - Transaction: conn_2
     - Output: None
     - Executed order: 6
 * Instruction #7:
     - Instruction:  ROLLBACK;
     - Transaction: conn_2
     - Output: None
     - Executed order: 7
 * Instruction #8:
     - Instruction:  select * from t_j_eqsc where t_j_eqsc.c_fm792b not in ( select PI() as c0 from ...
     - Transaction: conn_1
     - Output: [(37, 32000, 92, 3.141592653589793, 59, '8kef5d', 4, None), (37, 33000, 40, 3.141592653589793, 20, 'optfvc', 66, 'ikzfdd'), (37, 34000, 83, 3.141592653589793, 60, 'z7bs6c', 69, 'f_58sb'), (37, 35000, 12, 3.141592653589793, 31, 'j45ne', 28, None), (37, 36000, 73, 3.141592653589793, 19, 'nm4by', 87, None), (37, 37000, 86, 3.141592653589793, 43, '_y9uo', 50, None), (37, 51000, None, 3.141592653589793, 8, None, None, None), (37, 52000, None, 3.141592653589793, 94, 'goiqgb', None, None), (37, 53000, None, 3.141592653589793, 73, 'scio7b', None, None), (37, 54000, None, 3.141592653589793, 60, 'huom8', None, None)]
     - Executed order: 8
 * Instruction #9:
     - Instruction:  COMMIT;
     - Transaction: conn_1
     - Output: None
     - Executed order: 9

 * Container logs:
   No logs available.

### Scenario 1
 * Instruction #0:
     - Instruction:  update t_j_eqsc set wkey = 37, c_fm792b = PI();
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
 * Instruction #1:
     - Instruction:  select * from t_j_eqsc where t_j_eqsc.c_fm792b not in ( select PI() as c0 from ...
     - Transaction: conn_0
     - Output: []
     - Executed order: 1

 * Container logs:
   No logs available.
