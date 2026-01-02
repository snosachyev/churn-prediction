from abc import ABC, abstractmethod
from churn.domain.entities.user_features import UserFeatures


class FeatureRepository(ABC):

    @abstractmethod
    def get_by_user_id(self, user_id: int) -> UserFeatures | None:
        pass
