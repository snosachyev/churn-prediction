
from dataclasses import dataclass

@dataclass(frozen=True)
class UserFeaturesSchema:
    table: str = "user_features"

    columns: tuple[str, ...] = (
        "user_id",
        "days_active",
        "total_events",
        "avg_events_per_day",
        "last_event_days_ago",
    )