# Airflow DAG skeleton (not executed here)
from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG("dummy_dag", start_date=datetime(2026,1,1), schedule="@daily", catchup=False) as dag:
    t1 = BashOperator(task_id="hello", bash_command="echo hello airflow")
