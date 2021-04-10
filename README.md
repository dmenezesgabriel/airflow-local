# Airflow Local

## Description

Custom airflow base for local routines automation

## Usage

> On Linux, the mounted volumes in container use the native Linux filesystem user/group permissions, so you have to make sure the container and host computer have matching file permissions.
> `echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env`
>
> [Airflow official docs](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html)

**Database migrations**:

```sh
docker-compose up airflow-init
```

**Airflow CLI info**:

On terminal:

```sh
docker-compose run airflow-worker airflow info
```

with script `airflow.sh`:

```sh
# Permissions
chmod +x airflow.sh
# Example
./airflow.sh info
```

**API usage**

Example:

```sh
ENDPOINT_URL="http://localhost:8081/"
curl -X GET  \
    --user "airflow:airflow" \
    "${ENDPOINT_URL}/api/v1/pools"
```

**Clean all**:

```sh
docker-compose down --volumes --rmi all
```
