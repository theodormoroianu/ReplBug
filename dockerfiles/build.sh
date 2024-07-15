#! /bin/sh

# Builds an image passed as argument.
build_image() {
    echo "Building image $1 with versions $2"
    image_name=$1
    shift
    for version in "$@"; do
        docker build --tag ${image_name}:${version} --file ${image_name}-${version}.Dockerfile .
  done
}


# MariaDB versions
mariadb_versions="10.8.3 10.8.4 10.10.1"

# TiDB versions
tidb_versions="v5.2.1 v5.3.0 v5.4.0 v6.0.0 v6.1.0 v6.3.0 v4.0.0-beta.2"

# TiDB with TiKV versions
tidb_tikv_versions="v6.4.0.tikv v4.0.8.tikv v4.0.0-beta.2.tikv v4.0.4.tikv"

# Build images
build_image "mariadb" ${mariadb_versions}
build_image "tidb" ${tidb_versions}
build_image "tidb" ${tidb_tikv_versions}
