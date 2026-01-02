docker compose exec kafka /bin/bash -c '
for topic in events_login events_purchase events_click events; do
  kafka-topics \
    --bootstrap-server kafka:9092 \
    --create \
    --if-not-exists \
    --topic $topic \
    --partitions 1 \
    --replication-factor 1
done
'
