FROM golang:1.19-alpine AS builder

# Install git and other dependencies
RUN apk add --no-cache git make bash gcc wget binutils-gold musl-dev

# Set the working directory inside the container and create necessary directories
RUN mkdir -p /go/src/github.com/pingcap
WORKDIR /go/src/github.com/pingcap

# Clone the TiDB repository
RUN git clone --depth 1 --branch v6.3.0-alpha --single-branch https://github.com/pingcap/tidb.git \
    && cd tidb \
    && make -j \
    && mv bin/tidb-server /usr/local/bin/tidb-server \
    && cd .. \
    && rm -rf tidb

# Expose the TiDB server port
EXPOSE 4000

WORKDIR /usr/local/bin

# Start the TiDB server
CMD ["./tidb-server", "-P", "4000"]
