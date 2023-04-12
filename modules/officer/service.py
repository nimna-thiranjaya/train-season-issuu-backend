import json
import jwt
import datetime
from server import db
from os import environ
from modules.officer.model import Officer
from flask_bcrypt import generate_password_hash, check_password_hash
from utils.common import generate_response, TokenGenerator
from modules.officer.validation import CreateSignupInputSchema
from utils.http_code import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, \
    HTTP_409_CONFLICT


def create_user(request, input_data):
    officer_validate = CreateSignupInputSchema()
    errors = officer_validate.validate(input_data)
    if errors:
        return generate_response(None, errors, HTTP_400_BAD_REQUEST)
    check_email_exist = Officer.query.filter_by(email=input_data["email"]).first()
    if check_email_exist:
        return generate_response(None, "Email already exists", HTTP_409_CONFLICT)

    new_officer = Officer(**input_data)  # **input_data is the same as email=input_data["email"], ect
    new_officer.hash_password()
    db.session.add(new_officer)
    db.session.commit()
    del input_data["password"]
    return generate_response(input_data, "Officer created successfully", HTTP_201_CREATED)


def login_user(request, input_data):
    get_user = Officer.query.filter_by(email=input_data["email"]).first()

    if get_user is None:
        return generate_response(None, "Invalid email!", HTTP_401_UNAUTHORIZED)

    if get_user.check_password(input_data["password"]):
        token = jwt.encode(
            {
                "id": get_user.off_id,
                "email": get_user.email,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(days=7),
            },
            environ.get("SECRET_KEY"),
        )
        input_data["token"] = token
        return generate_response(input_data, "Login successful", HTTP_200_OK)
    else:
        return generate_response(None, "Invalid password!", HTTP_401_UNAUTHORIZED)


def user_Profile(request, auth):
    if auth:
        try:
            token = auth.split(" ")[1]
            is_token_valid = TokenGenerator.check_token(token)
            if is_token_valid:
                decode_token = TokenGenerator.decode_token(token)

                get_user = Officer.query.filter_by(off_id=decode_token["id"]).first()

                officer = {
                    "off_id": get_user.off_id,
                    "email": get_user.email,
                    "name": get_user.name,
                    "contact": get_user.contact,
                    "nic": get_user.nic,
                }

                return generate_response(officer, "User profile fletched", HTTP_200_OK)
            else:
                return generate_response(None, "Invalid token!", HTTP_401_UNAUTHORIZED)
        except:
            return generate_response(None, "Invalid token!", HTTP_401_UNAUTHORIZED)
    else:
        return generate_response(None, "Token required!", HTTP_401_UNAUTHORIZED)


def user_delete(request, auth):
    if auth:
        try:
            token = auth.split(" ")[1]
            is_token_valid = TokenGenerator.check_token(token)
            if is_token_valid:
                decode_token = TokenGenerator.decode_token(token)

                get_user = Officer.query.filter_by(off_id=decode_token["id"]).first()
                db.session.delete(get_user)
                db.session.commit()
                return generate_response(None, "User deleted", HTTP_200_OK)
            else:
                return generate_response(None, "Invalid token!", HTTP_401_UNAUTHORIZED)
        except:
            return generate_response(None, "Invalid token!", HTTP_401_UNAUTHORIZED)
    else:
        return generate_response(None, "Token required!", HTTP_401_UNAUTHORIZED)
