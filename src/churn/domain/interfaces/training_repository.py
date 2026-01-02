from abc import ABC, abstractmethod
import pandas as pd

class TrainingRepository(ABC):

    @abstractmethod
    def get_training_dataset(self) -> pd.DataFrame:
        pass
