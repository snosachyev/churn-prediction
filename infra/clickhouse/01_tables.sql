-- =========================
-- Raw events
-- =========================
CREATE TABLE IF NOT EXISTS churn.events
(
    user_id UInt64,
    event_time DateTime,
    event_type String,
    session_id String
)
ENGINE = MergeTree
PARTITION BY toYYYYMM(event_time)
ORDER BY (user_id, event_time);

-- =========================
-- Aggregated features
-- =========================
CREATE TABLE IF NOT EXISTS churn.user_features
(
    user_id UInt64,
    days_active UInt32,
    total_events UInt32,
    avg_events_per_day Float32,
    last_event_days_ago UInt32
)
ENGINE = MergeTree
ORDER BY user_id;
