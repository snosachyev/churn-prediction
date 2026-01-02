# churn/infrastructure/clickhouse/training_repository.py
import pandahouse
from churn.domain.interfaces.training_repository import TrainingRepository
from churn.config import get_clickhouse_config, pandahouse_connection

class ClickHouseTrainingRepository(TrainingRepository):

    def get_training_dataset(self):
        cfg = get_clickhouse_config()
        conn = pandahouse_connection(cfg)
        return pandahouse.read_clickhouse(
            "SELECT * FROM churn.user_features",
            connection=conn
        )
