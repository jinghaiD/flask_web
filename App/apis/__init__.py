from flask_restful import Api

from App.apis.people_api import UserResource
from App.apis.house_api import HouseResource

api = Api()


def init_apis(app):
    api.init_app(app)


api.add_resource(UserResource, '/people/')
api.add_resource(HouseResource, '/house/')