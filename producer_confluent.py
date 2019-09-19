from time import sleep
from json import dumps
from confluent_kafka import Producer

producer = Producer({
                        'bootstrap.servers': 'localhost:9092',
                        'broker.version.fallback': '0.10.1',
                        'api.version.fallback.ms': 0,
                        'security.protocol': 'PLAINTEXT',
                        'group.id': 'dev',
                        'queue.buffering.max.ms': 10,
                        'batch.num.messages': 5,
                        'auto.offset.reset': 'earliest',
})

for e in range(10):
    data = {'number' : e}
    producer.produce(topic='numtest', value=dumps(data).encode('utf-8'))
    sleep(1)

producer.flush()