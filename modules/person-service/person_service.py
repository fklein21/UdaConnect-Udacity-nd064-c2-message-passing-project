import time
from concurrent import futures
import logging
from datetime import datetime, timedelta
from typing import Dict, List

from app import db
from app.udaconnect.models import Connection, Location, Person
from sqlalchemy.sql import Column, String, Integer

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("udaconnect_person_create")


import grpc
import person_create_pb2
import person_create_pb2_grpc





# class PersonService:
#     @staticmethod
#     def create(person: Dict) -> Person:
#         new_person = Person()
#         new_person.first_name = person["first_name"]
#         new_person.last_name = person["last_name"]
#         new_person.company_name = person["company_name"]

#         db.session.add(new_person)
#         db.session.commit()

#         return new_person

#     @staticmethod
#     def retrieve(person_id: int) -> Person:
#         person = db.session.query(Person).get(person_id)
#         return person

#     @staticmethod
#     def retrieve_all() -> List[Person]:
#         return db.session.query(Person).all()


class Person(db.Model):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    company_name = Column(String, nullable=False)



# class OrderServicer(order_pb2_grpc.OrderServiceServicer):
#     def Get(self, request, context):
#         first_order = order_pb2.OrderMessage(
#             id="2222",
#             created_by="USER123",
#             status=order_pb2.OrderMessage.Status.QUEUED,
#             created_at='2020-03-12',
#             equipment=[order_pb2.OrderMessage.Equipment.KEYBOARD]
#         )

#         second_order = order_pb2.OrderMessage(
#             id="3333",
#             created_by="USER123",
#             status=order_pb2.OrderMessage.Status.QUEUED,
#             created_at='2020-03-11',
#             equipment=[order_pb2.OrderMessage.Equipment.MOUSE]
#         )

#         result = order_pb2.OrderMessageList()
#         result.orders.extend([first_order, second_order])
#         return result

#     def Create(self, request, context):
#         print("Received a message!")

#         request_value = {
#             "id": request.id,
#             "created_by": request.created_by,
#             "status": request.status,
#             "created_at": request.created_at,
#             "equipment": ["KEYBOARD"]
#         }
#         print(request_value)

#         return order_pb2.OrderMessage(**request_value)


# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
person_create_pb2_grpc.add_PersonCreateServiceServicer_to_server(PersonCreateServiceServicer(), server)


print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)