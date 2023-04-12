from flask_restful import Api
from constants import CONSTANTS
from modules.season.views import SeasonCreate


def create_season_routes(api: Api):
    api.add_resource(SeasonCreate, CONSTANTS['API_PREFIX'] + '/season/createSeason')
