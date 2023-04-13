from flask_restful import Api
from constants import CONSTANTS

from modules.payment.views import PaymentCreate


def create_payment_routes(api: Api):
    api.add_resource(PaymentCreate, CONSTANTS['API_PREFIX'] + '/payment/createPayment')
