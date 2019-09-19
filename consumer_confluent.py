from confluent_kafka import Consumer
from json import loads

consumer = Consumer({
                        'bootstrap.servers': 'localhost:9092',
                        'broker.version.fallback': '0.10.1',
                        'api.version.fallback.ms': 0,
                        'security.protocol': 'PLAINTEXT',
                        'group.id': 'dev',
                        'queue.buffering.max.ms': 10,
                        'batch.num.messages': 5,
                        'auto.offset.reset': 'earliest',
})

consumer.subscribe(['numtest'])

try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            print(msg.error())
        else:
            # Proper message
            print(loads(msg.value()))

except KeyboardInterrupt:
    print('Aborted by user')

finally:
    # Close down consumer to commit final offsets.
    consumer.close()
