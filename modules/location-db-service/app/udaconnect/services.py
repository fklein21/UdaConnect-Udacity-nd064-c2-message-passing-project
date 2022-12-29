import logging
import os
import json
from typing import Dict
import psycopg2
from kafka import KafkaConsumer

# Instruction about setting up the Kafka service
# and the producer and consumers taken from 
# https://b-nova.com/home/content/heres-how-you-can-setup-kafka-with-strimzi-on-kubernetes-in-only-five-minutes


DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"]


def write_to_db(location: Dict):
    logger.info(f"Write to location database: {str(locatin)}")

    session = psycopg2.connect(dbname=DB_NAME, port=DB_PORT, user=DB_USERNAME, password=DB_PASSWORD, host=DB_HOST)
    cursor = session.cursor()
    cursor.execute("""
            INSERT INTO location (person_id, coordinate)
            VALUES ({}, ST_Point({}, {}));'
    """.format(int(location['person_id']), float(location["latitude"]), float(location['longitude']))

    )

    new_location = Location()
    new_location.person_id = location["person_id"]
    new_location.creation_time = location["creation_time"]
    new_location.coordinate = ST_Point(location["latitude"], location["longitude"])
    db.session.add(new_location)
    db.session.commit()

    return new_location

def write_to_db(location):
    pass



format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"  # (1)
logging.basicConfig(format=format, level=logging.INFO)
logger = logging.getLogger("udaconnect-location-ingestion-service")

# # Set up a Kafka producer
KAFKA_SERVER = 'my-cluster-kafka-bootstrap.kafka.svc.cluster.local:9092'
KAFKA_TOPIC = "location"
serializer = lambda x: json.dumps(x).encode('utf-8')
producer = KafkaConsumer(KAFKA_TOPIC,
                         bootstrap_servers=KAFKA_SERVER,)














# Content taken (and modified) from this sources
# (1) - https://java2blog.com/log-to-stdout-python/