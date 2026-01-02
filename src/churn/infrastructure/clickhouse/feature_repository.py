import requests

import pandahouse

from churn.domain.entities.user_features import UserFeatures
from churn.domain.entities.schema import UserFeaturesSchema
from churn.domain.interfaces.feature_repository import FeatureRepository

from core.config import settings



class ClickHouseFeatureRepository(FeatureRepository):

    def __init__(self):
        self.schema = UserFeaturesSchema()
        self.base_url = f"http://{settings.clickhouse_host}:8123"


    def get_by_user_id(self, user_id: int) -> UserFeatures | None:
        cols = ", ".join(self.schema.columns)

        query = f"""
        SELECT {cols}
        FROM {self.schema.table}
        WHERE user_id = %(user_id)s
        LIMIT 1
        """

        df = pandahouse.read_clickhouse(
            query,
            connection=self.connection,
            params={"user_id": user_id},
        )

        if df.empty:
            return None

        return UserFeatures(**df.iloc[0].to_dict())
