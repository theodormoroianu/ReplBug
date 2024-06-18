# Docker Images

# MariaDB
docker build --tag mariadb:10.8.3 --file mariadb-10.8.3.Dockerfile .
docker build --tag mariadb:10.10.1 --file mariadb-10.10.1.Dockerfile .

# TiDB
docker build --tag tidb:v5.4.0 --file tidb-v5.4.0.Dockerfile .
docker build --tag tidb:v6.1.0 --file tidb-v6.1.0.Dockerfile .
