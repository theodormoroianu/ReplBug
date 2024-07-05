# Master Thesis

## Introduction

This repository contains the source code and results of a Python application facilitating the deployment of arbitrary versions of the _MySQL_, _MariaDB_ and _TiDB_ DBMSs in order to replicate bugs mentioned in the following papers:

* OSDI 2023: _Detecting Transactional Bugs in Database Engines via Graph-Based Oracle Construction_

  - This paper presents _TxCheck_, a tool for automatically generating multiple equivalent testcases and running them on database systems for detecting mismatches.
  - The paper can be found [here](./data/papers/OSDI2023%20Detecting%20Transactional%20Bugs%20in%20Database%20Engines%20via%20Graph-Based%20Oracle%20Construction.pdf).
  - The bugs found by _TxCheck_ are listed [here](https://github.com/JZuming/TxCheck/tree/main/docs).
  - The repository of _TxCheck_ can be found [here](https://github.com/JZuming/TxCheck/).


* ASE 2022: _Differentially Testing Database Transactions for Fun and Profit_

  - This paper presents _DT2_, a tool for automatically running testcases on different database systems and comparing the results.
  - The paper can be found [here](.data/papers/ASE2022%20Differentially%20Testing%20Database%20Transactions%20for%20Fun%20and%20Profit.pdf).
  - The bugs found by _DT2_ are listed [here](./data/papers/ASE2022_DT2_bug_list.csv).
  - The repository of _DT2_ can be found [here](https://github.com/tcse-iscas/DT2).

* ICSE 2024: _Understanding Transaction Bugs in Database Systems_

  - Survey paper, analyses bugs reported for _MySQL_, _MariaDB_ and _TiDB_.
  - The reported bugs are listed [here](./data/papers/ICSE2024_bug_list.xlsx).


## Installation

To install the _Python_ dependencies, run the following command: `pip3 install -r requirements.txt`.

The system needs to have `podman` installed in order to run the databases in containers.

## Usage

* Configure the `.env` file with the desired settings.
* Build the custom docker containers by running the following command: `./src/main.py db build`.
* Start the application by running the following command: `./src/main.py`. Use the `help` command in the CLI to get a list of all available commands.

## Running the Databases in Podman

The application uses _Podman_ to manage versions of _MySQL_, _MariaDB_ and _TiDB_ DBMSs. The docker images are pulled from their respective official repositories or built locally. You can build them either by running `./src/main.py db build` or `(cd dockerfiles && ./build)`.

The application uses the following images:

* `mysql:{version}`
* `mariadb:{version}`
* `pingcap/tidb:v{version}`


## Results

The logs of the testcases can be seen in the [data/results](./data/results) directory.
The logs are stored in the following format: `{BUG_ID}-{TESTCASE}.md`.

A ferquent checkpoint of the Google Docs table with the results is available [here](./data/analysis/Exploring%20the%20Correlation%20between%20Transactional%20Bugs%20and%20Isolation%20Levels_5_jun.xlsx).

The up-to-date sheet is available [here](https://docs.google.com/spreadsheets/d/1As6S9c8yzeAzXjCYplpv2aqIEXkB6BhpMhJR2qYJ4sk/edit?usp=sharing) (online).
