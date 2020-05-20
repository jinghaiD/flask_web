from flask_restful import Api

from App.apis.user_api import UserResource,UserSigninResource,UserSignupResource
from App.apis.house_api import HouseSimpleResource,HouseResource
from App.apis.picture_api import PictureResource

api = Api()


def init_apis(app):
    api.init_app(app)


api.add_resource(UserResource, '/usercheck/')
api.add_resource(UserSigninResource, '/usersignin/')
api.add_resource(UserSignupResource, '/usersignup/')
api.add_resource(HouseSimpleResource, '/housesimple/')
api.add_resource(HouseResource, '/house/')
api.add_resource(PictureResource, '/pics/')