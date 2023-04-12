from flask import Response
from flask_restful import Resource
from flask import request, make_response
from modules.officer.service import create_user, login_user, user_Profile, user_delete


class OfficerSignUp(Resource):
    @staticmethod
    def post() -> Response:
        """
        POST response method for creating user.

        :return: JSON object
        """
        input_data = request.get_json()
        response, status = create_user(request, input_data)
        return make_response(response, status)


class OfficerLogin(Resource):
    @staticmethod
    def post() -> Response:
        """
        POST response method for creating user.

        :return: JSON object
        """
        input_data = request.get_json()
        response, status = login_user(request, input_data)
        return make_response(response, status)


class OfficerProfile(Resource):
    @staticmethod
    def get() -> Response:
        """
        GET response using auth header user.

        :return: JSON object
        """
        auth = request.headers.get("Authorization")
        response, status = user_Profile(request, auth)
        return make_response(response, status)


class OfficerDelete(Resource):
    @staticmethod
    def delete() -> Response:
        """
        DELETE response using auth header user.

        :return: JSON object
        """
        auth = request.headers.get("Authorization")
        response, status = user_delete(request, auth)
        return make_response(response, status)
