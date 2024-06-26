# Master Thesis

## Introduction

This repository contains the source code of a Python application, able to deploy arbitrary versions of the _MySQL_, _MariaDB_ and _TiDB_ DBMSs in order to replicate bugs mentioned in the following papers:

* OSDI 2023: _Detecting Transactional Bugs in Database Engines via Graph-Based Oracle Construction_

  - This paper presents _TxCheck_, a tool for automatically generating multiple equivalent testcases and running them on database systems for detecting mismatches.
  - The paper can be found [here](./papers/OSDI2023%20Detecting%20Transactional%20Bugs%20in%20Database%20Engines%20via%20Graph-Based%20Oracle%20Construction.pdf).
  - The bugs found by _TxCheck_ are listed [here](https://github.com/JZuming/TxCheck/tree/main/docs).
  - The repository of _TxCheck_ can be found [here](https://github.com/JZuming/TxCheck/).
* ASE 2022: _Differentially Testing Database Transactions for Fun and Profit_

  - This paper presents _DT2_, a tool for automatically running testcases on different database systems and comparing the results.
  - The paper can be found [here](./papers/ASE2022%20Differentially%20Testing%20Database%20Transactions%20for%20Fun%20and%20Profit.pdf).
  - The bugs found by _DT2_ are listed [here](./papers/ASE2022_DT2_bug_list.csv).
  - The repository of _DT2_ can be found [here](https://github.com/tcse-iscas/DT2).

## Bugs Not Added Yet

### OSDI 2023 - TxCheck

* Need to add some way to handle bugs that don't occur every time.

  - https://jira.mariadb.org/browse/MDEV-29398
  - https://jira.mariadb.org/browse/MDEV-29400
  - https://jira.mariadb.org/browse/MDEV-29494
* Not sure if we should consider those

  - https://github.com/pingcap/tidb/issues/30413

### ASE 2022

 * Some bugs are false positive, not considering them.
 * Some bugs are marked as intentional. Not considering them either.
    - https://jira.mariadb.org/browse/MDEV-27922
 * Some are not confirmed. Not sure what to do with them.
    - https://jira.mariadb.org/browse/MDEV-28040
    - https://jira.mariadb.org/browse/MDEV-28142
 * Some bugs can't be reproduced
    - https://github.com/pingcap/tidb/issues/28095


## Installation

To install the _Python_ dependencies, run the following command: `pip3 install -r requirements.txt`.

The system needs to have `podman` installed in order to run the databases in containers.

## Usage

* Configure the `.env` file with the desired settings.
* Start the application by running the following command: `./src/main.py`. Use the `help` command in the CLI to get a list of all available commands.

## Running the Databases in Docker

The application uses _Podman_ to manage versions of _MySQL_, _MariaDB_ and _TiDB_ DBMSs. The docker images are pulled from their respective official repositories or built locally by running `(cd dockerfiles && ./build)`. The application uses the following images:

* `mysql:{version}`
* `mariadb:{version}`
* `pingcap/tidb:v{version}`
