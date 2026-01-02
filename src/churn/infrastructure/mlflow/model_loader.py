import mlflow.pyfunc
import pandas as pd
from churn.domain.interfaces.model_repository import ModelRepository
from churn.domain.entities.user_features import UserFeatures
from core.config import settings

from churn import user_features_to_df



class MlflowModelRepository(ModelRepository):

    def __init__(self):
        self.model = mlflow.pyfunc.load_model(
            model_uri=f"models:/{settings.model_name}/{settings.model_stage}"
        )

    def predict_churn_proba(self, features: UserFeatures) -> float:
        # Берём только нужные признаки
        X = user_features_to_df(features)
        proba = self.model.predict(X)
        return float(proba[0])