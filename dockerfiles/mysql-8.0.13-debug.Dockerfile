FROM ubuntu:20.04

# Make debian non-interactive.
ENV DEBIAN_FRONTEND noninteractive

# Install dependencies.
RUN apt-get update \
    && apt-get install -y \
        build-essential python-dev autotools-dev libicu-dev libbz2-dev \
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
        wget \
    && apt-get clean

# Set env variables to suppress warnings.
ENV CFLAGS "-w"
ENV CXXFLAGS "-w"

# Download boost
RUN wget https://archives.boost.io/release/1.67.0/source/boost_1_67_0_rc1.tar.gz \
    && tar -xzf boost_1_67_0_rc1.tar.gz \
    && rm boost_1_67_0_rc1.tar.gz

WORKDIR /boost_1_67_0

RUN ./bootstrap.sh --with-libraries=all --with-toolset=gcc \
    && ./b2 -j15 install

WORKDIR /

# Clone the repo, build the server, and install the server in /usr/local/mysql.
RUN git clone --depth 1 --branch mysql-8.0.13 --single-branch https://github.com/mysql/mysql-server
WORKDIR /mysql-server

RUN cmake . -DCMAKE_BUILD_TYPE=Debug -DWITH_ASAN=ON \
    && make -j15 \
    && make install \
    && make clean \
    && rm -rf /mysql-server

# Create the database.
WORKDIR /usr/local/mysql
RUN useradd mysql
RUN /usr/local/mysql/bin/mysqld --initialize-insecure --user=root --datadir=/var/lib/mysql
RUN chown -R mysql:mysql /var/lib/mysql

# Start the server.
EXPOSE 3306
CMD ["/usr/local/mysql/bin/mysqld", "--user=mysql", "--datadir=/var/lib/mysql", "--bind-address=0.0.0.0"]
