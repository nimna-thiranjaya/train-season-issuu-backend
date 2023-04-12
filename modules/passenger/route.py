from flask_restful import Api
from constants import CONSTANTS

from modules.passenger.views import PassengerGet


def create_passenger_routes(api: Api):
    api.add_resource(PassengerGet, CONSTANTS['API_PREFIX'] + '/passenger/getPassenger/<p_id>')