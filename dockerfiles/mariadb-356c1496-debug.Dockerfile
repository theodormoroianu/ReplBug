FROM ubuntu:18.04

# Install dependencies.
RUN apt-get update \
    && apt-get install -y \
        git \
        gzip \
        tar \
        gcc \
        g++ \
        make \
        bison \
        libncurses5-dev \
        zlib1g-dev \
        libevent-dev \
        cmake \
        libgnutls28-dev \
        libssl-dev \
        libjemalloc-dev \
        libsnappy-dev \
        valgrind \
        libcurl4-openssl-dev \
        libxml2-dev \
        libboost-all-dev \
        libaio-dev \
        libsystemd-dev \
        libpcre2-dev \
        ccache \
    && apt-get clean

# Set env variables to suppress warnings.
ENV CFLAGS "-w"
ENV CXXFLAGS "-w"

ARG COMMIT=356c149603285086d964c8a51107be97b981c15c

# Clone the repo, build the server, and install the server in /usr/local/mysql.
WORKDIR /server
RUN git clone --depth 1 --single-branch https://github.com/MariaDB/server \
    && cd server \
    && git fetch --depth 1 origin "$COMMIT" \
    && git checkout "$COMMIT" \
    && cmake . -DCMAKE_BUILD_TYPE=Debug -DWITH_ASAN=ON \
    && make -j15 \
    && make install \
    && make clean \
    && rm -rf /server

# Create the database.
WORKDIR /usr/local/mysql
RUN ./scripts/mysql_install_db --auth-root-authentication-method=normal

# Start the server.
EXPOSE 3306
CMD ["/usr/local/mysql/bin/mysqld", "--user=root", "--skip-grant-tables"]
