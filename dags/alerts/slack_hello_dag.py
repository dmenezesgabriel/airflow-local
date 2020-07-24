import logging
from pathlib import Path
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from alerts.utils.messages import send_message


_logger = logging.getLogger("Hello World DAG")

module_name = "-".join(Path(__file__).parts[3:]).replace('.py', '')

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2020, 7, 6, 22, 15),
    'retries': 1,
    "retry_delay": timedelta(minutes=5)
}

dag = DAG(
    dag_id=module_name,
    default_args=default_args,
    schedule_interval=timedelta(minutes=1),
    dagrun_timeout=timedelta(minutes=60),
    max_active_runs=1
)

with dag:
    send_slack_message = PythonOperator(
        task_id='slack_hello',
        provide_context=True,
        python_callable=send_message
    )

send_slack_message
