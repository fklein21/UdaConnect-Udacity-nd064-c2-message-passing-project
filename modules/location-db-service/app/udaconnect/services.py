import logging
import os
import json
from typing import Dict
import psycopg2
from kafka import KafkaConsumer

# Instruction about setting up the Kafka service
# and the producer and consumers taken from 
# https://b-nova.com/home/content/heres-how-you-can-setup-kafka-with-strimzi-on-kubernetes-in-only-five-minutes


# Database credentials
DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"]


# Write new location to the database
def write_to_db(new_location: Dict):
    logger.info(f"Write to location database: {str(new_location)}")

    session = psycopg2.connect(dbname=DB_NAME, port=DB_PORT, user=DB_USERNAME, password=DB_PASSWORD, host=DB_HOST)
    cursor = session.cursor()
    cursor.execute("""
            INSERT INTO location (person_id, coordinate)
            VALUES ({}, ST_Point({}, {}));
    """.format(int(new_location['person_id']), float(new_location["latitude"]), float(new_location['longitude']))
    )
    session.commit()
    cursor.close()
    session.close()

    logger.info(f"Location successfully saved")
    return new_location



format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"  # (1)
logging.basicConfig(format=format, level=logging.INFO)
logger = logging.getLogger("udaconnect-location-db-service")

# # Set up a Kafka producer
KAFKA_SERVER = 'my-cluster-kafka-bootstrap.kafka.svc.cluster.local:9092'
KAFKA_TOPIC = "location"
serializer = lambda x: json.dumps(x).encode('utf-8')
consumer = KafkaConsumer(KAFKA_TOPIC,
                         bootstrap_servers=KAFKA_SERVER)


def consume_message():
    for message in consumer:
        logger.info("Received message from Kafka")
        location = json.loads(message.value.decode("utf-8"))
        write_to_db(location)

consume_message()















# Content taken (and modified) from this sources
# (1) - https://java2blog.com/log-to-stdout-python/