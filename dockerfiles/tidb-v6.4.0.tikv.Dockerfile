FROM ubuntu:20.04

# Set non-interative mode
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && apt-get install -y \
    curl \
    tar \
    && apt-get clean

# Install TiDB
ARG VERSION=v6.4.0
ARG GOOS=linux
ARG GOARCH=amd64
RUN curl -O  "https://tiup-mirrors.pingcap.com/tikv-$VERSION-$GOOS-$GOARCH.tar.gz" \
    && curl -O  "https://tiup-mirrors.pingcap.com/pd-$VERSION-$GOOS-$GOARCH.tar.gz" \
    && curl -O  "https://tiup-mirrors.pingcap.com/tidb-$VERSION-$GOOS-$GOARCH.tar.gz" \
    && tar -xzf "tikv-$VERSION-$GOOS-$GOARCH.tar.gz" \
    && tar -xzf "pd-$VERSION-$GOOS-$GOARCH.tar.gz" \
    && tar -xzf "tidb-$VERSION-$GOOS-$GOARCH.tar.gz" \
    && rm "tikv-$VERSION-$GOOS-$GOARCH.tar.gz" \
    && rm "pd-$VERSION-$GOOS-$GOARCH.tar.gz" \
    && rm "tidb-$VERSION-$GOOS-$GOARCH.tar.gz" \
    && mv tikv-server /usr/local/bin/tikv-server \
    && mv pd-server /usr/local/bin/pd-server \
    && mv tidb-server /usr/local/bin/tidb-server

# Expose ports for TiDB, TiKV, and PD
EXPOSE 2379 2380 20160 4000

# Set the working directory to /usr/local/bin
WORKDIR /usr/local/bin

# Copy entrypoint script
COPY tidb-tikv-entrypoint.sh /usr/local/bin/entrypoint.sh

# Make entrypoint script executable
RUN chmod +x /usr/local/bin/entrypoint.sh

# Start the PD, TiKV, and TiDB servers
CMD ["/usr/local/bin/entrypoint.sh"]
