from flask_restful import Resource
from flask import request, make_response
from modules.passenger.service import get_passenger
from flask import Response


class PassengerGet(Resource):
    @staticmethod
    def get(p_id) -> Response:
        """
        GET response method for getting passenger.

        :return: JSON object
        """
        response, status = get_passenger(request, p_id)
        return make_response(response, status)
