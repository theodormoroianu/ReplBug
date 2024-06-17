FROM ubuntu:22.04

# Install dependencies.
run sed -i 's/^# deb-src/deb-src/' /etc/apt/sources.list
run apt update
run apt install -y build-essential bison libgnutls28-dev git cmake
run apt build-dep -y mariadb-server

# Clone the repo, build the server, and install the server in /usr/local/mysql.
workdir /server
run git clone --depth 1 --branch mariadb-10.10.1 --single-branch https://github.com/MariaDB/server \
    && cd server \
    && cmake . -DCMAKE_BUILD_TYPE=Debug -DWITH_ASAN=ON \
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
