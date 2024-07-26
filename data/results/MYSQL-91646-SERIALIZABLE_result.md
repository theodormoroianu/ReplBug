# Bug ID MYSQL-91646-SERIALIZABLE

## Description

Link:                     https://bugs.mysql.com/bug.php?id=91646
Original isolation level: REPEATABLE READ
Tested isolation level:   SERIALIZABLE
Description:              When super_read_only is true, all xa commands will still return OK, but normal transactions return ERROR when doing 'commit'.


## Details
 * Database: mysql-5.7.22
 * Number of scenarios: 2
 * Initial setup script: Yes

## Results
### Scenario 0
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows: 0
 * Instruction #1:
     - Instruction:  xa start '1';
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows: 0
 * Instruction #2:
     - Instruction:  insert into xatable values (1);
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows: 1
 * Instruction #3:
     - Instruction:  xa end '1';
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows: 0
 * Instruction #4:
     - Instruction:  set global super_read_only=on;
     - Transaction: conn_1
     - Output: None
     - Executed order: 4
     - Affected rows: 0
 * Instruction #5:
     - Instruction:  xa prepare '1';
     - Transaction: conn_0
     - Output: None
     - Executed order: 5
     - Affected rows: 0
 * Instruction #6:
     - Instruction:  xa commit '1';
     - Transaction: conn_0
     - Output: None
     - Executed order: 6
     - Affected rows: 0

 * Container logs:
   No logs available.

### Scenario 1
 * Instruction #0:
     - Instruction:  SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
     - Transaction: conn_0
     - Output: None
     - Executed order: 0
     - Affected rows: 0
 * Instruction #1:
     - Instruction:  set global super_read_only=off;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows: 0
 * Instruction #2:
     - Instruction:  begin;
     - Transaction: conn_0
     - Output: None
     - Executed order: 2
     - Affected rows: 0
 * Instruction #3:
     - Instruction:  insert into xatable values(11);
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows: 1
 * Instruction #4:
     - Instruction:  set global super_read_only=on;
     - Transaction: conn_1
     - Output: None
     - Executed order: 4
     - Affected rows: 0
 * Instruction #5:
     - Instruction:  commit; -- throws an error
     - Transaction: conn_0
     - Output: ERROR: 1290 (HY000): The MySQL server is running with the --super-read-only option so it cannot execute this statement
     - Executed order: Not executed
     - Affected rows: -1
 * Instruction #6:
     - Instruction:  set global super_read_only=off;
     - Transaction: conn_1
     - Output: None
     - Executed order: 5
     - Affected rows: 0
 * Instruction #7:
     - Instruction:  commit;
     - Transaction: conn_0
     - Output: None
     - Executed order: 6
     - Affected rows: 0

 * Container logs:
   No logs available.
