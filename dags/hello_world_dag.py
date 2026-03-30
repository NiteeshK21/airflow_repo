from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'hello_world_dag',
    default_args=default_args,
    description='A simple hello world DAG',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['example'],
) as dag:

    def print_hello():
        print("Hello World from Python!")
        return 'Hello World'

    hello_task = PythonOperator(
        task_id='hello_task',
        python_callable=print_hello,
    )

    bash_task = BashOperator(
        task_id='bash_task',
        bash_command='echo "Hello World from Bash!"',
    )

    hello_task >> bash_task
