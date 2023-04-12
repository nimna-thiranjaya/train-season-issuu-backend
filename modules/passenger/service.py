import json
from server import db
from modules.passenger.model import Passenger
from utils.common import generate_response
from utils.http_code import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT


def get_passenger(request, p_id):

    passenger = Passenger.query.filter_by(p_id=p_id).first()

    if passenger is None:
        return generate_response(None, "Passenger not found", HTTP_400_BAD_REQUEST)

    passenger_data = passenger.__dict__
    del passenger_data["_sa_instance_state"]

    return generate_response(passenger_data, "Passenger found", HTTP_200_OK)