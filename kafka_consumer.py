from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'dbserver1.inventory.products',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='cdc-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Connected. Waiting for messages...")

for message in consumer:
    print("Received:")
    print(message.value)
