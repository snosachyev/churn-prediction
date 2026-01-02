import pandas as pd
from churn import train_model

def test_training_returns_fitted_model(sample_df):
    model = train_model(sample_df)
    assert hasattr(model, "predict_proba")
