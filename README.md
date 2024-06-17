# Master Thesis

This repository contains the source code of a Python application, able to deploy arbitrary versions of the _MySQL_, _MariaDB_ and _TiDB_ DBMSs.

## Bugs

### TxCheck

 * Need to add some way to handle bugs that don't occur every time.
    - https://jira.mariadb.org/browse/MDEV-29398
    - https://jira.mariadb.org/browse/MDEV-29400
    - https://jira.mariadb.org/browse/MDEV-29494

 * Not sure if we should consider those
    - https://github.com/pingcap/tidb/issues/30413
    

## Installation

To install the _Python_ dependencies, run the following command: `pip3 install -r requirements.txt`.

We do not offer an exact list of the required system packages, as it depends on the operating system. You do **not** need to install the DBMSs manually, as the application will take care of that. Moreover, no other instance of the DBMSs should be running on the system.

## Usage

 * Configure the `.env` file with the desired settings.
 * Start the application by running the following command: `./src/main.py`. Use the `help` command in the CLI to get a list of all available commands.

## Running the Databases in Docker

The application uses _Podman_ to manage versions of _MySQL_, _MariaDB_ and _TiDB_ DBMSs. The docker images are pulled from their respective official repositories. The application uses the following images:

 * `mysql:{version}`
 * `mariadb:{version}`
 * `pingcap/tidb:v{version}`

## Running the Databases manually

The application can also run the DBMSs without using _Podman_. The application will download the DBMSs from the official websites and extract them to the `{CACHE_FOLDER_PATH}/databases/` directory (by default `.cache/databases/`). The application will then start the DBMSs using the extracted binaries.
All downloaded assets are placed in the `{CACHE_FOLDER_PATH}` directory (from `.env`). The application downloads the DBMSs from the official websites, and the URLs are hardcoded in the source code. The application downloads the following DBMSs:

### MySQL

The application downloads the _MySQL_ DBMS from the official website's archives. The URLs where the binaries are downloaded from are:

 * `https://dev.mysql.com/get/Downloads/MySQL-{version}/mysql-{version}-linux-glibc2.12-x86_64.tar.xz`, or
 * `https://dev.mysql.com/get/Downloads/MySQL-{version}/mysql-{version}-linux-glibc2.12-x86_64.tar.gz`.

### MariaDB

 * `https://mirror.mva-n.net/mariadb/mariadb-{version}/bintar-linux-systemd-x86_64/mariadb-{version}-linux-systemd-x86_64.tar.gz`, or
 * `https://archive.mariadb.org/mariadb-{version}/bintar-linux-systemd-x86_64/mariadb-{version}-linux-systemd-x86_64.tar.gz`.

### TiDB

We use the `tiup` tool to download and install the _TiDB_ DBMS.

The tools are downloaded from [here](https://docs.pingcap.com/tidb/stable/quick-start-with-tidb#simulate-production-deployment-on-a-single-machine).

## Logging

The application logs most of the actions in the `{CACHE_FOLDER_PATH}/logs/` directory (by default `.cache/logs/`). A new log file is created for each run of the application.



