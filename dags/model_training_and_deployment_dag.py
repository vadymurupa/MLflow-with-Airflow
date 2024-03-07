from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Assuming these functions are defined elsewhere in your codebase
def train_model(ti):
    model_path = train_and_save_model()
    ti.xcom_push(key='model_path', value=model_path)

def deploy_model(ti):
    model_path = ti.xcom_pull(key='model_path', task_ids='train_model')
    deploy_trained_model(model_path)

# Define the DAG
dag = DAG(
    'mlops_dag',
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
)

train_model_task = PythonOperator(
    task_id='train_model',
    python_callable=train_model,
    dag=dag,
)

deploy_model_task = PythonOperator(
    task_id='deploy_model',
    python_callable=deploy_model,
    dag=dag,
)

train_model_task >> deploy_model_task

