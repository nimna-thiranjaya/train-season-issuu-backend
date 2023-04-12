import json
from server import db
from modules.season.model import Season
from modules.passenger.model import Passenger
from utils.common import generate_response
from utils.http_code import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT


def create_season(request, input_data):
    input_data = json.loads(request.data)

    check_nic_exist = Passenger.query.filter_by(nic=input_data["nic"]).first()
    if check_nic_exist:
        return generate_response(None, "Passenger already exists", HTTP_409_CONFLICT)

    try:
        new_passenger = Passenger(**input_data)
        db.session.add(new_passenger)
        db.session.commit()
        input_data["p_id"] = new_passenger.p_id
        new_season = Season(**input_data)
        db.session.add(new_season)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return generate_response(None, e , HTTP_400_BAD_REQUEST)

    return generate_response(None, "Season created successfully", HTTP_200_OK)
