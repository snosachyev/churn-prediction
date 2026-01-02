import random

from datetime import datetime

import pandahouse  # ClickHouse driver

import pandas as pd


def generate_events():
    # NOTE: utility for demo / data generation, not production ingestion
    import logging
    logger = logging.getLogger(__name__)

    conn = {"host": "http://clickhouse:8123",  "database": "churn"}

    #pandahouse.execute("USE churn", conn)

    events = []
    for user_id in range(1, 501):
        for _ in range(random.randint(5, 40)):
            events.append({
                "user_id": user_id,
                "event_time": datetime.now(),
                "event_type": random.choice(["login", "click", "purchase"]),
                "session_id": str(random.randint(1, 100000))
            })

    df = pd.DataFrame(events)
    df["event_time"] = pd.to_datetime(df["event_time"]).dt.floor("S")
    logger.info(f"Generated {len(df)} events")

    pandahouse.to_clickhouse(
    df,
    table="events",
    connection=conn,
    index=False
)
    cnt = pandahouse.read_clickhouse(
        "SELECT count(*) FROM churn.events",
        connection=conn
    )
    logger.info(f"Rows in churn.events: {cnt}")
