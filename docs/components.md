# Components

## Web Server

`Flask` server with `gunicorn` serving the user interface.

## Scheduler

Responsible to tirgger tasks

- It's possible to run multiple schedulers

## Database

Metadata database

- Any database that is used with SQLAlchemy can be used

## Executor

Defines how your tasks will be executed by airflow using a broker

- Celery Executor
- Kubernets Executor
- Local Executor

## Worker

Where your tasks will be executed
