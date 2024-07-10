FROM ubuntu:22.04

# Install dependencies.
RUN sed -i 's/^# deb-src/deb-src/' /etc/apt/sources.list
RUN apt update \
    && apt install -y build-essential bison libgnutls28-dev git cmake \
    && apt build-dep -y mariadb-server \
    && apt clean

# Clone the repo, build the server, and install the server in /usr/local/mysql.
WORKDIR /server
RUN git clone --depth 1 --branch mariadb-10.8.4 --single-branch https://github.com/MariaDB/server \
    && cd server \
    && cmake . -DCMAKE_BUILD_TYPE=Debug \
    && make -j8 \
    && make install \
    && make clean \
    && rm -rf /server

# Create the database.
WORKDIR /usr/local/mysql
RUN ./scripts/mariadb-install-db --auth-root-authentication-method=normal


# Start the server.
EXPOSE 3306
CMD ["/usr/local/mysql/bin/mysqld", "--user=root", "--skip-grant-tables"]
