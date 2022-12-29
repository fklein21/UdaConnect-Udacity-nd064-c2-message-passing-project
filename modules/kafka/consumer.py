import json
from kafka import KafkaConsumer


# TOPIC_NAME = 'items'

# consumer = KafkaConsumer(TOPIC_NAME)
# for message in consumer:
#     print (message)

KAFKA_SERVER = 'my-cluster-kafka-bootstrap.kafka.svc.cluster.local:9092'
KAFKA_SERVER = '10.43.122.186:9092'
KAFKA_TOPIC = "location"
serializer = lambda x: json.dumps(x).encode('utf-8')
consumer = KafkaConsumer(KAFKA_TOPIC,
                         bootstrap_servers=KAFKA_SERVER)