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
    print(new_officer)
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
