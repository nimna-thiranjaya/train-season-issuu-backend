from flask import Response
from flask_restful import Resource
from flask import request, make_response
from modules.season.service import create_season, get_one_season, get_all_seasons, renew_season


class SeasonCreate(Resource):
    @staticmethod
    def post() -> Response:
        """
        POST response method for creating user.

        :return: JSON object
        """
        input_data = request.get_json()
        auth = request.headers.get("Authorization")
        response, status = create_season(request, input_data, auth)
        return make_response(response, status)


class SeasonGetOne(Resource):
    @staticmethod
    def get(s_id) -> Response:
        """
        GET response method for getting season.

        :return: JSON object
        """
        response, status = get_one_season(request, s_id)
        return make_response(response, status)


class SeasonGetAll(Resource):
    @staticmethod
    def get() -> Response:
        """
        GET response method for getting all seasons.

        :return: JSON object
        """
        response, status = get_all_seasons(request)
        return make_response(response, status)

class RenewSeason(Resource):
    @staticmethod
    def patch(s_id) -> Response:
        """
        PATCH response method for renewing season.

        :return: JSON object
        """
        input_data = request.get_json()
        response, status = renew_season(request, input_data, s_id)
        return make_response(response, status)