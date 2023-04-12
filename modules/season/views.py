from flask import Response
from flask_restful import Resource
from flask import request, make_response
from modules.season.service import create_season


class SeasonCreate(Resource):
    @staticmethod
    def post() -> Response:
        """
        POST response method for creating user.

        :return: JSON object
        """
        input_data = request.get_json()
        response, status = create_season(request, input_data)
        return make_response(response, status)
