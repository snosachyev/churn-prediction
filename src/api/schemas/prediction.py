from datetime import datetime
from pydantic import BaseModel


class PredictionResponse(BaseModel):
    user_id: int
    churn_probability: float
    model_version: str
    timestamp: datetime
