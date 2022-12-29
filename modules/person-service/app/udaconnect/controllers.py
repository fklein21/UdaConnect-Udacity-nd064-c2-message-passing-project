import logging
from app.udaconnect.models import Person
from app.udaconnect.schemas import (PersonSchema)
from app.udaconnect.services import PersonService
from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import List

DATE_FORMAT = "%Y-%m-%d"
api = Namespace("UdaConnect", description="Connections via geolocation.")  # noqa


format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"  # (1)
logging.basicConfig(format=format, level=logging.INFO)
logger = logging.getLogger("udaconnect-person-service")


@api.route("/persons")
class PersonsResource(Resource):
    @accepts(schema=PersonSchema)
    @responds(schema=PersonSchema)
    def post(self) -> Person:
        logging.info("Request (post) to persons route")
        payload = request.get_json()
        new_person: Person = PersonService.create(payload)
        return new_person

    @responds(schema=PersonSchema, many=True)
    def get(self) -> List[Person]:
        logging.info("Request (get) to persons route")
        persons: List[Person] = PersonService.retrieve_all()
        return persons


@api.route("/persons/<person_id>")
@api.param("person_id", "Unique ID for a given Person", _in="query")
class PersonResource(Resource):
    @responds(schema=PersonSchema)
    def get(self, person_id) -> Person:
        logging.info("Request (post) to persons/<person_id> route")
        person: Person = PersonService.retrieve(person_id)
        return person




# Content taken (and modified) from this sources
# (1) - https://java2blog.com/log-to-stdout-python/