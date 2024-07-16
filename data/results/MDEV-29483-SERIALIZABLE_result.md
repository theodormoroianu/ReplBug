# Bug ID MDEV-29483-SERIALIZABLE

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-29483
Original isolation level: REPEATABLE READ
Tested isolation level:   SERIALIZABLE
Description:              MariaDB crashes.


## Details
 * Database: mariadb-10.10.1
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
     - Instruction:  START TRANSACTION;
     - Transaction: conn_0
     - Output: None
     - Executed order: 1
     - Affected rows / Warnings: 0 / 0
 * Instruction #2:
     - Instruction:  select coalesce(subq_0.c0, LAST_VALUE( subq_0.c0) over (partition by subq_0.c1 ...
     - Transaction: conn_0
     - Output: [('k9c7o',), ('iysxxc',), ('6f610b',), ('olzb8',), ('b7_6l',), ('3rzvv',), ('rrpi9b',), (None,), ('x21w7',), ('gmxcbb',), ('qtplab',), (None,), ('mtdvdb',), ('venphc',), ('o54sbd',), (None,), ('_cq7f',), ('dhlvzc',), ('4wccm',), ('imarq',), ('db8zj',), (None,), ('77o6sc',), ('8gfgz',), (None,), ('_xghd',), ('prxd1d',), ('xkplyd',), ('tyefa',), ('1vhbk',), ('hcrasb',), ('5hqikd',), ('fosv3d',), ('flqltc',), (None,), ('hvlnnd',), ('jpbzgd',), ('s0byd',), ('8qgjf',), ('ys4vw',), ('slexob',), ('msedad',), (None,), ('napmgc',), ('wh4d7b',), (None,), ('d6uzhd',), ('y9hfmb',), ('8q66j',)]
     - Executed order: 2
     - Affected rows / Warnings: 49 / 0
 * Instruction #3:
     - Instruction:  ROLLBACK;
     - Transaction: conn_0
     - Output: None
     - Executed order: 3
     - Affected rows / Warnings: 0 / 0

 * Container logs:
   No logs available.
