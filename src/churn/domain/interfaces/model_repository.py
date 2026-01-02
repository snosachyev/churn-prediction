from abc import ABC, abstractmethod
import pandas as pd


class ModelRepository(ABC):

    @abstractmethod
    def predict_churn_proba(self, features: pd.DataFrame) -> float:
        pass
