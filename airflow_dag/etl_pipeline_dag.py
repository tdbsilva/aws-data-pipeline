# etl_pipeline_dag.py
"""
Simulação de DAG no Airflow para pipeline AWS.
Autor: Thiago Diniz
"""

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

def extract():
    print("Extraindo dados (simulação)...")

def transform():
    print("Transformando dados (simulação)...")

def load():
    print("Carregando dados para Redshift (simulação)...")

with DAG(
    dag_id="etl_pipeline_simulado",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    default_args={"retries": 1, "retry_delay": timedelta(minutes=5)},
    tags=["aws", "data-engineering", "simulation"]
) as dag:

    extract_task = PythonOperator(task_id="extract", python_callable=extract)
    transform_task = PythonOperator(task_id="transform", python_callable=transform)
    load_task = PythonOperator(task_id="load", python_callable=load)

    extract_task >> transform_task >> load_task
