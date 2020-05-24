from flask_restful import Api

from App.apis.admin_api import Admin2Resource,Admin3Resource
from App.apis.hictory_api import HistoryResource,SelectHistoryResource
from App.apis.sub_api import SubAddResource,SubFinishResource,SubJudgeResource,SelectSubResource,SubPassResource
from App.apis.user_api import UserResource,UserSigninResource,UserSignupResource
from App.apis.house_api import HouseSimpleResource,HouseResource,HouseCityResource,AddHouseResource,HouseOwnerResource,HouseSearchResource
from App.apis.picture_api import PictureResource

api = Api()


def init_apis(app):
    api.init_app(app)


api.add_resource(Admin2Resource, '/admin2/')
api.add_resource(Admin3Resource, '/admin3/')
api.add_resource(UserResource, '/usercheck/')
api.add_resource(UserSigninResource, '/usersignin/')
api.add_resource(UserSignupResource, '/usersignup/')
api.add_resource(HouseSimpleResource, '/housesimple/')
api.add_resource(HouseResource, '/house/')
api.add_resource(PictureResource, '/pics/')
api.add_resource(HouseCityResource, '/housecity/')
api.add_resource(HistoryResource, '/history/')
api.add_resource(SelectHistoryResource, '/selecthistory/')
api.add_resource(SubAddResource, '/subadd/')
api.add_resource(SubFinishResource, '/subfinish/')
api.add_resource(SubJudgeResource, '/subjudge/')
api.add_resource(SelectSubResource, '/selectsub/')
api.add_resource(AddHouseResource, '/addhouse/')
api.add_resource(HouseOwnerResource, '/owner/')
api.add_resource(SubPassResource, '/subpass/')
api.add_resource(HouseSearchResource, '/search/')