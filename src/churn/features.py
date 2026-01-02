# src/features/churn_features.py

import pandas as pd

from churn.domain.entities.user_features import UserFeatures
from churn.domain.entities.schema import UserFeaturesSchema


FEATURE_COLUMNS = [
    "avg_events_per_day",
    "days_active",
    "last_event_days_ago",
    "total_events",
]


def user_features_to_df(features: UserFeatures) -> pd.DataFrame:
    df = pd.DataFrame([features.model_dump()])
    return build_features(df)


def build_user_features():
    import pandahouse
    conn = {"host": "http://clickhouse:8123", "database": "churn"}

    pandahouse.execute(
        f"TRUNCATE TABLE churn.{UserFeaturesSchema.table}",
        conn
    )

    query = f"""
    INSERT INTO churn.{UserFeaturesSchema.table}
    SELECT
        user_id,
        countDistinct(toDate(event_time)) AS days_active,
        count(*) AS total_events,
        count(*) / greatest(days_active, 1) AS avg_events_per_day,
        dateDiff('day', max(event_time), now()) AS last_event_days_ago
    FROM churn.events
    GROUP BY user_id
    """

    pandahouse.execute(query, conn)


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    features = pd.DataFrame(index=df.index)

    features["avg_events_per_day"] = (
        df["total_events"] / df["days_active"].clip(lower=1)
    )
    features["days_active"] = df["days_active"]
    features["last_event_days_ago"] = df["last_event_days_ago"]
    features["total_events"] = df["total_events"]

    return features[list(UserFeaturesSchema.feature_fields)]
