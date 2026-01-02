import mlflow
import mlflow.sklearn

import pandas as pd

import pandahouse


from sklearn.model_selection import train_test_split


from churn import build_features

from churn.domain.entities.schema import UserFeaturesSchema
from churn.infrastructure.clickhouse.training_repository import ClickHouseTrainingRepository



def train_model(df: pd.DataFrame):
    from churn import create_model
    X = build_features(df)
    X = X[list(UserFeaturesSchema.feature_fields)]
    y = df['churn']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = create_model()  # LogisticRegression()
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    print("Model trained, accuracy:", score)
    return model


def train():  # для Airflow
    repo = ClickHouseTrainingRepository()
    raw_df = repo.get_training_dataset()

    model = train_model(raw_df)

    # логирование в MLflow
    mlflow.set_tracking_uri("http://mlflow:5000")
    mlflow.set_experiment("churn_prediction")

    with mlflow.start_run(run_name="churn_model"):
        mlflow.sklearn.log_model(model, artifact_path="model", registered_model_name="churn_model")
    
    return model
