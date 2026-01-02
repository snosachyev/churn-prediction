import logging

from datetime import datetime


from airflow import DAG
from airflow.operators.python import PythonOperator

from src.churn import generate_events, build_user_features, train



logger = logging.getLogger("airflow.task")



# -----------------------------
# DAG definition
# -----------------------------
with DAG(
    dag_id="churn_pipeline",
    start_date=datetime(2025, 12, 25),
    schedule_interval="@daily",
    catchup=False,
    tags=["churn", "ml"]
) as dag:
    
    # -----------------------------
    # Step 1: Load or generate events
    # -----------------------------
    generate = PythonOperator(
        task_id="generate_events",
        python_callable=generate_events
    )

    # -----------------------------
    # Step 2: ETL / Aggregate features in ClickHouse
    # -----------------------------
    # ETL -> создаем таблицу features_table в ClickHouse
    features = PythonOperator(
        task_id="build_user_features",
        python_callable=build_user_features
    )

    # -----------------------------
    # Step 3: Train model and log in MLflow
    # -----------------------------
    train = PythonOperator(
        task_id="train_model",
        python_callable=train
    )

    generate >> features >> train
