import datetime
import json
from server import db
from modules.season.model import Season, IssuedDetails
from modules.passenger.model import Passenger
from utils.common import generate_response, TokenGenerator
from utils.http_code import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT, HTTP_401_UNAUTHORIZED
from datetime import date


def create_season(request, input_data, auth):
    input_data = json.loads(request.data)
    if auth:
        try:
            token = auth.split(" ")[1]
            is_token_valid = TokenGenerator.check_token(token)
            if is_token_valid:
                decode_token = TokenGenerator.decode_token(token)
                input_data["off_id"] = decode_token["id"]
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
                    input_data["s_id"] = new_season.s_id
                    input_data["date"] = datetime.datetime.now()
                    new_issued_details = IssuedDetails(**input_data)
                    db.session.add(new_issued_details)
                    db.session.commit()

                except Exception as e:
                    db.session.rollback()
                    return generate_response(None, e, HTTP_400_BAD_REQUEST)

                return generate_response(None, "Season created successfully", HTTP_200_OK)

            else:
                return generate_response(None, "Invalid token!", HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return generate_response(None, e, HTTP_401_UNAUTHORIZED)
    else:
        return generate_response(None, "Invalid required!", HTTP_401_UNAUTHORIZED)


def get_one_season(request, s_id):
    season = Season.query.filter_by(s_id=s_id).first()

    if season is None:
        return generate_response(None, "Season not found", HTTP_400_BAD_REQUEST)

    season_data = season.__dict__
    del season_data["_sa_instance_state"]

    return generate_response(season_data, "Season fletched!", HTTP_200_OK)


def get_all_seasons(request):
    seasons = Season.query.all()

    if seasons is None:
        return generate_response(None, "Seasons not found", HTTP_400_BAD_REQUEST)

    seasons_data = []
    for season in seasons:
        season_data = season.__dict__
        del season_data["_sa_instance_state"]
        seasons_data.append(season_data)

    return generate_response(seasons_data, "Seasons fletched!", HTTP_200_OK)


def renew_season(request, input_data, s_id, auth):
    if auth:
        try:
            token = auth.split(" ")[1]
            is_token_valid = TokenGenerator.check_token(token)
            if is_token_valid:
                decode_token = TokenGenerator.decode_token(token)
                input_data["off_id"] = decode_token["id"]
                season = Season.query.filter_by(s_id=s_id).first()
                # get issued details using s_id
                issued_details = IssuedDetails.query.filter_by(s_id=s_id).first()
                if season is None:
                    return generate_response(None, "Season not found", HTTP_400_BAD_REQUEST)

                try:
                    season.end_station = input_data["end_station"]
                    season.start_station = input_data["start_station"]
                    season.renewal_date = input_data["renewal_date"]
                    season.expiration_date = input_data["expiration_date"]
                    season.price = input_data["price"]

                    db.session.merge(season)
                    db.session.commit()

                    issued_details.s_id = s_id
                    issued_details.off_id = input_data["off_id"]
                    issued_details.date = datetime.datetime.now()

                    db.session.merge(issued_details)
                    db.session.commit()

                except Exception as e:
                    db.session.rollback()
                    return generate_response(None, e, HTTP_400_BAD_REQUEST)

                return generate_response(None, "Season renewed successfully", HTTP_200_OK)

            else:
                return generate_response(None, "Invalid token!", HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return generate_response(None, e, HTTP_401_UNAUTHORIZED)
    else:
        return generate_response(None, "Invalid required!", HTTP_401_UNAUTHORIZED)
