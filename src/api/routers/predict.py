from datetime import datetime
from fastapi import APIRouter, Depends
from api.schemas.prediction import PredictionResponse
from churn.application.services.churn_prediction import ChurnPredictionService
from core.config import settings
from core.dependencies import get_churn_service

router = APIRouter()


@router.post("/predict", response_model=PredictionResponse)
def predict(
    user_id: int,
    service: ChurnPredictionService = Depends(get_churn_service)
):
    probability = service.predict(user_id)

    return PredictionResponse(
        user_id=user_id,
        churn_probability=probability,
        model_version=settings.model_version,
        timestamp=datetime.utcnow()
    )
