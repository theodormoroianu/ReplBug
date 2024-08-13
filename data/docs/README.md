# Data Analysis

## Motivation

The aim of this work is finding hidden corelations between bugs and isolation levels.

The vast majority of the replicated bugs manifest under all 4 isolation levels (or 2 in the case of TiDB), so we further explore in detail the few bugs that manifest under some isolation levels but not others, which we call "interesting" bugs.

## Data Collection

The data is collected from the replicated bugs (see [here](../../src/testcase/bug_list/) the code for the bugs). The bugs themselves are taken from multiple sources, but most of them are taken from the papers mentioned [here](../../README.md).

Our tool is able to automatically generate reports, which contain information such as the output of SQL instructions or their effective execution order, for each isolation level.

## Interesting Bug Analysis

Each of the interesting bugs is analyzed individually, analysing the following:

 - How the bug manifests (understanding the bug).
 - The isolation levels that trigger the bug.
 - If the bug does not manifest under specific isolation levels because:
    * The isolation level is more permissive, and the buggy behaviour is actually the indented one.
    * The isolation level does not allow the bug to manifest (e.g. due to concurent transactions locking).
    * The buggy logic is not triggered under the isolation level.
 - How (and if) the bug is fixed in the latest version of the database.

## Resuls

 - [MDEV-19535](./interesting_bugs/MDEV-19535.md).
 - [MDEV-26642](./interesting_bugs/MDEV-26642.md).
 - [MDEV-26643](./interesting_bugs/MDEV-26643.md).
 - [MDEV-29243](./interesting_bugs/MDEV-29243.md).
 - [MDEV-29565](./interesting_bugs/MDEV-29565.md).
 - [MYSQL-100293](./interesting_bugs/MYSQL-100293.md).
 - [MYSQL-104245](./interesting_bugs/MYSQL-104245.md).
 - [MYSQL-108528](./interesting_bugs/MYSQL-108528.md).
 - [MYSQL-114389](./interesting_bugs/MYSQL-114389.md).
 - [MYSQL-93806](./interesting_bugs/MYSQL-93806.md).
 - [MYSQL-94338](./interesting_bugs/MYSQL-94338.md).
 - [TIDB-21151](./interesting_bugs/TIDB-21151.md).