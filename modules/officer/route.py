from flask_restful import Api
from constants import CONSTANTS
from modules.officer.views import OfficerSignUp, OfficerLogin, OfficerProfile, OfficerDelete


def create_officer_routes(api: Api):
    api.add_resource(OfficerSignUp, CONSTANTS['API_PREFIX'] + '/officer/signup')
    api.add_resource(OfficerLogin, CONSTANTS['API_PREFIX'] + '/officer/login')
    api.add_resource(OfficerProfile, CONSTANTS['API_PREFIX'] + '/officer/profile')
    api.add_resource(OfficerDelete, CONSTANTS['API_PREFIX'] + '/officer/deleteOfficer')