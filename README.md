# Airflow Local

## Description

Custom airflow base for local routines automation

### What is Airflow?

Open Source platform to programmatically _author_, _schedule_ and _monitor_ workflows.

- Orchestrator

### What Airflow is not.

Not a Streaming or a data processing framework.

### Why Airflow?

- Automatic retry on fail
- Manage complex tasks
- Monitor tasks
- User interface
  - UI
  - CLI
  - REST API

### Advantages

- Dynamic
- Scalable
- Interactive
- Extensible

### Disadvantages

Not meant to process terabytes of data.

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

**Running**:

```sh
docker compose up
```

Or simple

```sh
Make run
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
