from flask_restful import Api

from App.apis.people_api import UserResource

api = Api()


def init_apis(app):
    api.init_app(app)


api.add_resource(UserResource, '/people/')
