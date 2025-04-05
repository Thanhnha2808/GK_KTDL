from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import save  

default_args = {
    "owner": "airflow",
    "start_date": datetime(2025, 4, 5),
    "retries": 1,
}

dag = DAG(
    "news_pipeline",
    default_args=default_args,
    schedule_interval="0 10 * * *",  
)

task = PythonOperator(
    task_id="run_pipeline",
    python_callable=save.save_to_db,
    dag=dag,
)