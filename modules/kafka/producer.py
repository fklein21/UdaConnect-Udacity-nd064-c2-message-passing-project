
from kafka import KafkaProducer


TOPIC_NAME = 'items'
KAFKA_SERVER = 'localhost:9092'
KAFKA_SERVER = 'my-cluster-kafka-bootstrap.kafka.svc.cluster.local:9092'
KAFKA_TOPIC = "location"
serializer = lambda x: json.dumps(x).encode('utf-8')
consumer = KafkaConsumer(KAFKA_TOPIC,
                         bootstrap_servers=KAFKA_SERVER)

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

producer.send(TOPIC_NAME, b'Test Message!!!')
producer.flush()