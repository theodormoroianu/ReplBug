FROM golang:1.19-alpine AS builder

# Install git and other dependencies
RUN apk add --no-cache git make bash gcc wget binutils-gold musl-dev curl tar

# Set the working directory inside the container and create necessary directories
RUN mkdir -p /go/src/github.com/pingcap
WORKDIR /go/src/github.com/pingcap

ARG BRANCH=b0c3fe7ba3acf8864709c825af681e5b35a111f2
ARG VERSION=v6.4.0
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
    
# Download the TiKV binaries.
RUN mkdir -p /tmp/binaries
WORKDIR /tmp/binaries

# Install TiDB
RUN curl -O  "https://tiup-mirrors.pingcap.com/tikv-$VERSION-$GOOS-$GOARCH.tar.gz" \
    && curl -O  "https://tiup-mirrors.pingcap.com/pd-$VERSION-$GOOS-$GOARCH.tar.gz" \
    && tar -xzf "tikv-$VERSION-$GOOS-$GOARCH.tar.gz" \
    && tar -xzf "pd-$VERSION-$GOOS-$GOARCH.tar.gz" \
    && rm "tikv-$VERSION-$GOOS-$GOARCH.tar.gz" \
    && rm "pd-$VERSION-$GOOS-$GOARCH.tar.gz" \
    && mv tikv-server /usr/local/bin/tikv-server \
    && mv pd-server /usr/local/bin/pd-server

# Now create the final image
FROM ubuntu:20.04

# Set non-interative mode
ENV DEBIAN_FRONTEND=noninteractive

# Install musl for compatibility with the TiDB binaries
RUN apt-get update && apt-get install -y musl && apt-get clean

# Copy binaries from the builder image
COPY --from=builder /usr/local/bin/tidb-server /usr/local/bin/tidb-server
COPY --from=builder /usr/local/bin/tikv-server /usr/local/bin/tikv-server
COPY --from=builder /usr/local/bin/pd-server /usr/local/bin/pd-server

# Copy entrypoint script
COPY tidb-tikv-entrypoint.sh /usr/local/bin/entrypoint.sh

# Make entrypoint script executable
RUN chmod +x /usr/local/bin/entrypoint.sh

# Expose ports for TiDB, TiKV, and PD
EXPOSE 2379 2380 20160 4000

WORKDIR /usr/local/bin

# Start the TiDB server
CMD ["/usr/local/bin/entrypoint.sh"]
