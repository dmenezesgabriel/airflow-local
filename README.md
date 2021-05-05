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

## Defaults

- Login: airflow
- Password: airflow

## Command Line

### Database

**Initializing database**:

Once the webserver container is up

```sh
docker-compose exec airflow-webserver /bin/sh
```

And the command line type:

```sh
airflow db init
```

_to update database schemas run_:

```
airflow db upgrade
```

**Drop database**:

Once the webserver container is up

```sh
docker-compose exec airflow-webserver /bin/sh
```

And the command line type:

```sh
airflow db reset
```

### User commands

- **Start webserver**:

```sh
airflow webserver
```

- **Start scheduler**:

```sh
airflow scheduler
```

- **Start worker**:

```sh
airflow worker
```

- **Pause dags**:

```sh
airflow dags pause
```

- **Unpause dags**:

```sh
airflow dags unpause
```

- **List dags**:

```sh
airflow dags list
```

- **List tasks of an DAG**:

```sh
airflow tasks list <dag_id>
```

- **Test tasks of an DAG**:

```sh
airflow tasks test <dag_id> <task_id> <yyyy-mm-dd(execution_past_date)>
```

- **Rerun past DAG runs**:

```sh
airflow dags backfill -s <yyyy-mm-dd(start_date)> -e <yyyy-mm-dd(end_date)> --reset_dagruns(optional) <dag_id>
```

## API usage

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
