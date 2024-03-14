import config
from kafka import KafkaConsumer

consumer = KafkaConsumer(config.TOPIC,
                         bootstrap_servers=config.SERVER,
                        #  group_id='test', # 同group的消费者只有一个能消费到信息
                         auto_offset_reset='earliest')
print('consumer start')
for msg in consumer:
    print(msg.value)