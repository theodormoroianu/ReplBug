#!/bin/bash


# Start PD server
pd-server --name=pd --data-dir=/tmp/pd/data --client-urls="http://0.0.0.0:2379" --peer-urls="http://0.0.0.0:2380" &

sleep 3

# Start TiKV server
tikv-server --pd="127.0.0.1:2379" --data-dir=/tmp/tikv/data &

sleep 3

# Start TiDB server
tidb-server --store=tikv --path="127.0.0.1:2379"
