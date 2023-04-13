import datetime
from server import db
import json
from modules.payment.model import Payment
from utils.common import generate_response
from utils.http_code import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT, HTTP_401_UNAUTHORIZED


def create_payment(request):
    input_data = json.loads(request.data)

    new_data = Payment(**input_data)
    db.session.add(new_data)
    db.session.commit()

    return generate_response(None, "Payment created successfully", HTTP_200_OK)
