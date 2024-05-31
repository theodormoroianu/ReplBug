# Build with docker build --tag mariadb-debug:10.8.3 --file mariadb-debug-10.8.3.Dockerfile .

FROM ubuntu:22.04

# Install dependencies.
run sed -i 's/^# deb-src/deb-src/' /etc/apt/sources.list
run apt update
run apt install -y build-essential bison libgnutls28-dev git cmake
run apt build-dep -y mariadb-server

# Clone the repo.
run git clone --depth 1 --branch mariadb-10.8.3 --single-branch https://github.com/MariaDB/server

# Build the server.
# Install the server in /usr/local/mysql
# and create the data directory in /usr/loca/mysql/data.
workdir /server
run cmake . -DCMAKE_BUILD_TYPE=Debug \
    && make -j8 \
    && make install \
    && make clean \
    && rm -rf /server

# Create the database.
workdir /usr/local/mysql
run ./scripts/mariadb-install-db --auth-root-authentication-method=normal


# Start the server.
EXPOSE 3306
cmd ["/usr/local/mysql/bin/mysqld", "--user=root", "--skip-grant-tables"]
