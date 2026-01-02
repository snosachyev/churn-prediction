# tests/conftest.py
import pytest
import pandas as pd
from churn import build_features, FEATURE_COLUMNS, train_model

# -------------------------------
# Пример фикстуры для тестового DataFrame
# -------------------------------
@pytest.fixture
def sample_df():
    """Возвращает небольшой DataFrame с фичами для тестов."""
    return pd.DataFrame([
        {"total_events": 10, "days_active": 5, "last_event_days_ago": 1, "churn": 1},
        {"total_events": 5, "days_active": 3, "last_event_days_ago": 2, "churn": 0},
        {"total_events": 8, "days_active": 4, "last_event_days_ago": 1, "churn": 1},
    ])

# -------------------------------
# Фикстура для обученной модели
# -------------------------------
@pytest.fixture
def trained_model(sample_df):
    """Возвращает обученную модель для тестов."""
    return train_model(sample_df)

# -------------------------------
# Можно добавить фикстуры для MLflow, API и других общих объектов
# -------------------------------
