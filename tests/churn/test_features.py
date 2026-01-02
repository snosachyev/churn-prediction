import pandas as pd
from churn import build_features

def raw_df():
    return pd.DataFrame([{
        "total_events": 10,
        "days_active": 5,
        "last_event_days_ago": 2,
    }])

def test_features_schema():
    X = build_features(raw_df())
    assert list(X.columns) == [
        "avg_events_per_day",
        "days_active",
        "last_event_days_ago",
        "total_events",
    ]

def test_features_values():
    X = build_features(raw_df())
    assert X["avg_events_per_day"].iloc[0] == 2.0
