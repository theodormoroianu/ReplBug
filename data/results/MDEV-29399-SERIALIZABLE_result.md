# Bug ID MDEV-29399-SERIALIZABLE

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-29399
Original isolation level: REPEATABLE READ
Tested isolation level:   SERIALIZABLE


## Details
 * Database: mariadb-10.8.3
 * Number of scenarios: 2
 * Initial setup script: /home/theodor/Projects/MasterThesis/data/sql/MDEV-29399_mysql_bk.sql

## Results
### Scenario 0
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  START TRANSACTION;
     - TID: 0
     - Output: None
 * Instruction #2:
     - SQL:  START TRANSACTION;
     - TID: 2
     - Output: None
 * Instruction #3:
     - SQL:  update t_j_eqsc set wkey = 37, c_fm792b = PI();
     - TID: 0
     - Output: None
 * Instruction #4:
     - SQL:  COMMIT;
     - TID: 0
     - Output: None
 * Instruction #5:
     - SQL:  START TRANSACTION;
     - TID: 1
     - Output: None
 * Instruction #6:
     - SQL:  insert into t_j_eqsc (wkey, pkey) values (79, 162000);
     - TID: 2
     - Output: None
 * Instruction #7:
     - SQL:  ROLLBACK;
     - TID: 2
     - Output: None
 * Instruction #8:
     - SQL:  select * from t_j_eqsc where t_j_eqsc.c_fm792b not in ( select PI() as c0 from ...
     - TID: 1
     - Output: [(37, 32000, 92, 3.141592653589793, 59, '8kef5d', 4, None), (37, 33000, 40, 3.141592653589793, 20, 'optfvc', 66, 'ikzfdd'), (37, 34000, 83, 3.141592653589793, 60, 'z7bs6c', 69, 'f_58sb'), (37, 35000, 12, 3.141592653589793, 31, 'j45ne', 28, None), (37, 36000, 73, 3.141592653589793, 19, 'nm4by', 87, None), (37, 37000, 86, 3.141592653589793, 43, '_y9uo', 50, None), (37, 51000, None, 3.141592653589793, 8, None, None, None), (37, 52000, None, 3.141592653589793, 94, 'goiqgb', None, None), (37, 53000, None, 3.141592653589793, 73, 'scio7b', None, None), (37, 54000, None, 3.141592653589793, 60, 'huom8', None, None)]
 * Instruction #9:
     - SQL:  COMMIT;
     - TID: 1
     - Output: None

 * Container logs:
   No logs available.

### Scenario 1
 * Instruction #0:
     - SQL:  update t_j_eqsc set wkey = 37, c_fm792b = PI();
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  select * from t_j_eqsc where t_j_eqsc.c_fm792b not in ( select PI() as c0 from ...
     - TID: 0
     - Output: []

 * Container logs:
   No logs available.
