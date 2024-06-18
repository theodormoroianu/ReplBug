# Bug ID MDEV-29483-READ_UNCOMMITTED

## Description

Link:                     https://jira.mariadb.org/browse/MDEV-29483
Original isolation level: REPEATABLE READ
Tested isolation level:   READ UNCOMMITTED


## Details
 * Database: mariadb-10.8.3
 * Number of scenarios: 1
 * Initial setup script: /home/theodor/Projects/MasterThesis/data/sql/MDEV-29483_mysql_bk.sql

## Results
### Scenario 0
 * Instruction #0:
     - SQL:  SET GLOBAL TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
     - TID: 0
     - Output: None
 * Instruction #1:
     - SQL:  select coalesce(subq_0.c0, LAST_VALUE( subq_0.c0) over (partition by subq_0.c1 ...
     - TID: 0
     - Output: [('k9c7o',), ('iysxxc',), ('6f610b',), ('olzb8',), ('b7_6l',), ('3rzvv',), ('rrpi9b',), (None,), ('x21w7',), ('gmxcbb',), ('qtplab',), (None,), ('mtdvdb',), ('venphc',), ('o54sbd',), (None,), ('_cq7f',), ('dhlvzc',), ('4wccm',), ('imarq',), ('db8zj',), (None,), ('77o6sc',), ('8gfgz',), (None,), ('_xghd',), ('prxd1d',), ('xkplyd',), ('tyefa',), ('1vhbk',), ('hcrasb',), ('5hqikd',), ('fosv3d',), ('flqltc',), (None,), ('hvlnnd',), ('jpbzgd',), ('s0byd',), ('8qgjf',), ('ys4vw',), ('slexob',), ('msedad',), (None,), ('napmgc',), ('wh4d7b',), (None,), ('d6uzhd',), ('y9hfmb',), ('8q66j',)]

 * Container logs:
   No logs available.
