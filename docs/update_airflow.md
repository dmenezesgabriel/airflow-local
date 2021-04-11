# Update Airflow

1. [ ] Database Backup(snapshot).
2. [ ] Verify Deprecated features at the current DAGs.
3. [ ] Pause all DAGs and Make sure no tasks are running.
4. [ ] Upgrade Apache Airflow.

```sh
pip install "apache-airflow[any_extra]==2.0.1" --constraint <constraint-file>
```

5. [ ] Upgrade Database.

```sh
airflow db upgrade
```

6. [ ] Restart `Web Server`, `Scheduler` and `Workers`.
