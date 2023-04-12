from flask_restful import Api
from constants import CONSTANTS
from modules.season.views import SeasonCreate, SeasonGetOne, SeasonGetAll, RenewSeason


def create_season_routes(api: Api):
    api.add_resource(SeasonCreate, CONSTANTS['API_PREFIX'] + '/season/createSeason')
    api.add_resource(SeasonGetOne, CONSTANTS['API_PREFIX'] + '/season/getSeason/<s_id>')
    api.add_resource(SeasonGetAll, CONSTANTS['API_PREFIX'] + '/season/getAllSeasons')
    api.add_resource(RenewSeason, CONSTANTS['API_PREFIX'] + '/season/renewSeason/<s_id>')