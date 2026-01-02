from churn.application.services.churn_prediction import ChurnPredictionService
from src.churn.infrastructure.clickhouse.feature_repository import ClickHouseFeatureRepository
from churn.infrastructure.mlflow.model_loader import MlflowModelRepository


_feature_repo = ClickHouseFeatureRepository()
_model_repo = MlflowModelRepository()
_service = ChurnPredictionService(_feature_repo, _model_repo)


def get_churn_service() -> ChurnPredictionService:
    return _service
