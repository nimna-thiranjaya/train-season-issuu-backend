from flask_restful import Resource
from flask import request, make_response
from modules.payment.service import create_payment
from flask import Response

class PaymentCreate(Resource):
    @staticmethod
    def post() -> Response:
        """
        POST response method for creating payment.

        :return: JSON object
        """
        response, status = create_payment(request)
        return make_response(response, status)