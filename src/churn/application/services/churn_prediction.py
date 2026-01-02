import pandas as pd
from churn.domain.interfaces.feature_repository import FeatureRepository
from churn.domain.interfaces.model_repository import ModelRepository


class ChurnPredictionService:

    def __init__(
        self,
        feature_repo: FeatureRepository,
        model_repo: ModelRepository
    ):
        self.feature_repo = feature_repo
        self.model_repo = model_repo

    def predict(self, user_id: int) -> float:
        features = self.feature_repo.get_by_user_id(user_id)
        if not features:
            return 0.0
        
        
        return self.model_repo.predict_churn_proba(features)
