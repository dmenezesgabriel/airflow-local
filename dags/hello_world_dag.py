import logging
from pathlib import Path
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


_logger = logging.getLogger("Hello World DAG")

module_name = "-".join(Path(__file__).parts[3:]).replace('.py', '')

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2020, 7, 6, 21, 10),
    'retries': 1,
    "retry_delay": timedelta(minutes=5)
}

dag = DAG(
    dag_id=module_name,
    default_args=default_args,
    schedule_interval=timedelta(minutes=5),
    dagrun_timeout=timedelta(minutes=60),
    max_active_runs=1
)

with dag:
    BashOperator(
        task_id='print_hello',
        bash_command='echo "Hello World!"',
        dag=dag
    )
