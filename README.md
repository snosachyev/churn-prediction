# Churn Prediction ML Platform

ML-платформа для предсказания оттока пользователей (churn) на основе пользовательских событий.  
Проект демонстрирует полный ML lifecycle: ingestion → feature engineering → training → registry → inference.

Стек: **ClickHouse, Kafka, Airflow, MLflow, FastAPI, MinIO, Docker Compose**

---

## 📌 Архитектура (кратко)

Kafka → ClickHouse → Airflow → MLflow → FastAPI
↑ ↓
Feature Store Model Registry

markdown

- **Kafka** — поток пользовательских событий  
- **ClickHouse** — хранилище событий и агрегированных фич  
- **Airflow** — оркестрация ETL и обучения модели  
- **MLflow** — трекинг экспериментов и registry моделей  
- **MinIO** — S3-compatible хранилище артефактов  
- **FastAPI** — сервис онлайн-предсказаний  

---

## 📂 Структура проекта

    .
    ├── infra
    │   ├── airflow
    │   └── clickhouse
    │
    ├── services
    │   ├── api
    │   ├── airflow
    │   ├── jupyter
    │   └── mlflow
    │
    ├── src
    │   ├── api
    │   ├── churn
    │   │   ├── domain
    │   │   ├── application
    │   │   ├── infrastructure
    │   │   ├── features.py
    │   │   ├── training.py
    │   │   └── model.py
    │   └── core
    │
    ├── tests
    ├── docker-compose.yml
    ├── README.md
    └── .env.example

---

## ⚙️ Переменные окружения

Создать `.env` на основе `.env.example`:

```env
  MLFLOW_TRACKING_URI=http://mlflow:5000
  MLFLOW_S3_ENDPOINT_URL=http://minio:9000

  AWS_ACCESS_KEY_ID=minioadmin
  AWS_SECRET_ACCESS_KEY=minioadmin
```

## 🚀 Запуск проекта
  1️⃣ Сборка и старт сервисов
    docker compose up --build

  2️⃣ Доступные интерфейсы
    Сервис	URL
    FastAPI	http://localhost:8000
    Airflow	http://localhost:8080
    MLflow	http://localhost:5000
    MinIO	http://localhost:9002
    Jupyter	http://localhost:8888

## 🛠 Инициализация Airflow
  docker compose run --rm airflow-webserver airflow db init

  docker compose run --rm airflow-webserver airflow users create \
    --username admin \
    --password admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com

## 🧩 Kafka

  ### Создание топика
    docker compose exec kafka kafka-topics \
      --bootstrap-server kafka:9092 \
      --create \
      --topic events \
      --partitions 1 \
      --replication-factor 1

  ### Добавление событий
    docker compose exec -it kafka kafka-console-producer \
      --bootstrap-server kafka:9092 \
      --topic events
    Пример сообщений:
      {"user_id":2,"event_time":"2025-12-26 18:00:00","event_type":"login","session_id":"abc"}
      {"user_id":2,"event_time":"2025-12-26 18:05:00","event_type":"purchase","session_id":"def"}

  ### Чтение событий
  docker compose exec kafka kafka-console-consumer \
    --bootstrap-server kafka:9092 \
    --topic events_login \
    --from-beginning

## 🗄 ClickHouse
  Raw события: churn.events
  Агрегированные фичи: churn.user_features
  Агрегация выполняется Airflow задачей build_user_features.

## 🧠 ML Pipeline (Airflow)
  DAG: churn_pipeline
    Шаги:
      generate_events — генерация демо-событий
      build_user_features — агрегация фич в ClickHouse
      train_model — обучение модели и логирование в MLflow

    Запуск вручную:
      docker compose exec airflow-scheduler \
        airflow dags trigger churn_pipeline

## 📈 MLflow
  Эксперименты: churn_prediction
  Модель: churn_model
  Registry: Production / latest
  Артефакты хранятся в MinIO (s3://mlflow-artifacts)

## 🔮 FastAPI — предсказание
  Endpoint
  POST /predict?user_id=123

  Пример запроса
  curl -X POST "http://localhost:8000/predict?user_id=42"

  Пример ответа
  json
  {
    "user_id": 42,
    "churn_probability": 0.73,
    "model_version": "1.0.0",
    "timestamp": "2026-01-01T12:00:00Z"
  }

## 🧪 Тестирование
  python -m venv .venv
  source .venv/bin/activate
  pip install -e .
  pip install -r dev-requirements.txt
  pytest -q

## 🧭 Принципы проекта
  DDD-подход для ML (domain / application / infrastructure)

  Feature Store в ClickHouse

  MLflow как единый источник моделей

  Airflow как orchestrator, не как бизнес-логика

  API не знает о ClickHouse напрямую

## 📌 Ограничения и TODO
  Нет интеграционных тестов API
  Нет моков ClickHouse / MLflow
  Kafka используется как демо-ingestion
  Генерация событий — утилита, не продакшн ingestion

## 📄 Лицензия
MIT License