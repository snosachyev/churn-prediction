FROM apache/airflow:2.9.3-python3.9

USER root


# Обновляем system deps, если нужно
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER airflow

COPY src /opt/airflow/src

# Обновляем pip и устанавливаем mlflow 2.9.2 + зависимости
RUN pip install --upgrade pip \
    && pip install mlflow==2.9.2 scikit-learn pandas numpy pandahouse boto3
