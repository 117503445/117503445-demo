import json
import time
import datetime
import config
from kafka import KafkaProducer


producer = KafkaProducer(bootstrap_servers=config.SERVER,
                         value_serializer=lambda m: json.dumps(m).encode())

for i in range(100):
    data = {'num': i, 'ts': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    producer.send(config.TOPIC, data)
    time.sleep(1)