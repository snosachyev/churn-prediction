from datetime import datetime
from pydantic import BaseModel


class UserFeatures(BaseModel):
    user_id: int
    days_active: int
    total_events: int
    avg_events_per_day: float
    last_event_days_ago: int
