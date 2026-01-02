CREATE TABLE IF NOT EXISTS churn.events_kafka (
    user_id UInt64,
    event_time DateTime,
    event_type String,
    session_id String
)
ENGINE = Kafka
SETTINGS
    kafka_broker_list = 'kafka:9092',
    kafka_topic_list = 'events',
    kafka_group_name = 'clickhouse_events',
    kafka_format = 'JSONEachRow';

CREATE MATERIALIZED VIEW IF NOT EXISTS churn.events_mv
TO churn.events
AS
SELECT *
FROM churn.events_kafka;

