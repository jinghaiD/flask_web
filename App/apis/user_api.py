from flask_restful import Resource, abort, fields, marshal_with, reqparse
from App.models.user import User
from App.reposition.UserReposition import UserReposition


people_check = reqparse.RequestParser()
people_check.add_argument('username', type=str, required=True)

people_signin = reqparse.RequestParser()
people_signin.add_argument('username', type=str, required=True)
people_signin.add_argument('password', type=str, required=True)


class UserResource(Resource):

    def post(self):

        args = people_check.parse_args()
        username = args.get('username')
        check = UserReposition().username_exist(username)
        return check


class UserSigninResource(Resource):

    def post(self):

        args = people_signin.parse_args()
        username = args.get('username')
        password = args.get('password')
        UserReposition().create(username, password)
        return


class UserSignupResource(Resource):

    def post(self):

        args = people_signin.parse_args()
        username = args.get('username')
        password = args.get('password')
        status = UserReposition().signup_check(username, password)
        return status
# people_fields = {
#     'name': fields.String,
#     'age': fields.Integer,
# }
#
# back_fields = {
#     'data': fields.Nested(people_fields)
# }
#
# back_peoples_fields = {
#     "data": fields.List(fields.Nested(people_fields))
# }
#
#
# parser = reqparse.RequestParser()
# parser.add_argument("name", type=str, required=True, help="please input a name")
# parser.add_argument("age", type=int)
# # action=append 获取多个值，变成列表，dest=name 获取别名
# # location=cookies/form/header/params获取固定位置的参数
#
#
# class UserResource(Resource):
#
#     @marshal_with(back_peoples_fields)
#     def get(self):
#
#         peoples = People.query.all()
#
#         data = {
#             'data': peoples
#         }
#
#         return data
#
#     # @marshal_with(back_fields)
#     def post(self):
#
#         args = parser.parse_args()
#         name = args.get('name')
#         age = args.get('age')
#         people_reposition = PeopleReposition()
#         people = people_reposition.create(name, age)
#         # people = People(name, age)
#         data = {
#             "data": people
#         }
#
#         return data
