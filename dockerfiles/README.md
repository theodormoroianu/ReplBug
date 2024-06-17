# Docker Images

For each version of the databases we wish to build in debug mode, we have a Dockerfile in this directory.

The dockerfiles must be built into an image, which can then be run as a container by the script.

Building an image can be done with the following command:

```bash
docker build --tag mariadb-debug:10.8.3 --file mariadb-debug-10.8.3.Dockerfile .
docker build --tag mariadb-debug:10.10.1 --file mariadb-debug-10.10.1.Dockerfile .
```