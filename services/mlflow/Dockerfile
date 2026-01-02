FROM ghcr.io/mlflow/mlflow

WORKDIR /app
COPY services/mlflow/requirements.txt .

RUN pip install --upgrade pip \
 && pip install --no-cache-dir --user -r requirements.txt
