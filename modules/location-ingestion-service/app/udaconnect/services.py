import logging
import time
import json
import grpc 
import location_pb2
import location_pb2_grpc
from concurrent import futures
from kafka import KafkaProducer

# Instruction about setting up the Kafka service
# and the producer and consumers taken from 
# https://b-nova.com/home/content/heres-how-you-can-setup-kafka-with-strimzi-on-kubernetes-in-only-five-minutes


class LocationServicer(location_pb2_grpc.LocationServiceServicer):

    def Create(self, request, context):
        logger.info("Received message")
        request_value = {
            "person_id": request.person_id,
            "latitude": request.latitude,
            "longitude": request.longitude,
        }
        logger.info(str(request_value))
        producer.send(KAFKA_TOPIC, request_value)
        producer.flush()
        return location_pb2.LocationMessage(**request_value)


format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"  # (1)
logging.basicConfig(format=format, level=logging.INFO)
logger = logging.getLogger("udaconnect-location-ingestion-service")

# # Set up a Kafka producer
KAFKA_SERVER = 'my-cluster-kafka-bootstrap.kafka.svc.cluster.local:9092'
KAFKA_TOPIC = "location"
serializer = lambda x: json.dumps(x).encode('utf-8')
producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER,
                         value_serializer=serializer)

# Initializes the gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
location_pb2_grpc.add_LocationServiceServicer_to_server(LocationServicer(), server)

print("Server starting on port 5555..")
server.add_insecure_port("[::]:5555")
server.start()

# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)



# Content taken (and modified) from this sources
# (1) - https://java2blog.com/log-to-stdout-python/