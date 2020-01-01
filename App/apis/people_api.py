from flask_restful import Resource, abort, fields, marshal_with, reqparse
from App.models.people import People
from App.reposition.people_reposition import PeopleReposition

people_fields = {
    'name': fields.String,
    'age': fields.Integer,
}

back_fields = {
    'data': fields.Nested(people_fields)
}

back_peoples_fields = {
    "data": fields.List(fields.Nested(people_fields))
}


parser = reqparse.RequestParser()
parser.add_argument("name", type=str, required=True, help="please input a name")
parser.add_argument("age", type=int)
# action=append 获取多个值，变成列表，dest=name 获取别名
# location=cookies/form/header/params获取固定位置的参数


class UserResource(Resource):

    @marshal_with(back_peoples_fields)
    def get(self):

        peoples = People.query.all()

        data = {
            'data': peoples
        }

        return data

    # @marshal_with(back_fields)
    def post(self):

        args = parser.parse_args()
        name = args.get('name')
        age = args.get('age')
        people_reposition = PeopleReposition()
        people = people_reposition.create(name, age)
        # people = People(name, age)
        data = {
            "data": people
        }

        return data
