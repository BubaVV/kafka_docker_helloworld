from time import sleep
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'),
                         api_version=(0, 10, 1),
                         security_protocol='PLAINTEXT')

for e in range(10):
    data = {'number' : e}
    producer.send('numtest', value=data)
    sleep(1)