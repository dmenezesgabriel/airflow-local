# Architectures

## Single node

All the components run at the same machine.

- Web Server
- Scheduler
- Metastore
- Executor

## Multiple nodes (Celery)

**Node 1**:

- Web Server
- Scheduler
- Executor

**Node 2**:

- Metastore
- Queue

**Worker node 1**:

- Airflow Worker

**Worker node 2**:

- Airflow Worker

**Worker node 3**:

- Airflow Worker

_Web Server => Metastore => Scheduler => Executor => Queue => Workers_
