FROM golang:1.19-alpine AS builder

# Install git and other dependencies
RUN apk add --no-cache git make bash gcc wget binutils-gold musl-dev curl tar

# Set the working directory inside the container and create necessary directories
RUN mkdir -p /go/src/github.com/pingcap
WORKDIR /go/src/github.com/pingcap

ARG BRANCH=45571c5e9bcc63195bc06b0aab19ddaac5fd4d2a
ARG VERSION=v4.0.7
ARG GOOS=linux
ARG GOARCH=amd64

# Clone the TiDB repository
RUN git clone --depth 1 https://github.com/pingcap/tidb.git \
    && cd tidb \
    && git fetch --depth 1 origin "$BRANCH" \
    && git checkout "$BRANCH" \
    && make -j \
    && mv bin/tidb-server /usr/local/bin/tidb-server \
    && cd .. \
    && rm -rf tidb

EXPOSE 4000
WORKDIR /usr/local/bin
CMD ["./tidb-server", "-P", "4000"]