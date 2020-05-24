from flask_restful import Resource, fields, marshal_with, reqparse
from App.reposition.house_reposition import HouseReposition
from App.reposition.sub_reposition import SubReposition

sub_parser = reqparse.RequestParser()
sub_parser.add_argument('username', type=str, required=True)
sub_parser.add_argument('houseid', type=int, required=True)


select_sub = reqparse.RequestParser()
select_sub.add_argument('username', type=str, required=True)


house_fields = {
    'id': fields.Integer,
    'jingdu': fields.String,
    'weidu': fields.String,
    'name': fields.String,
    'province': fields.String,
    'city': fields.String,
    'type': fields.String,
    'guest': fields.Integer,
    'room': fields.Integer,
    'bed': fields.Integer,
    'toilet': fields.Integer,
    'introduction': fields.String,
    'price': fields.Integer,
    'booktime': fields.Integer,
    'status': fields.Integer
}
back_house_fields = {
    'data': fields.List(fields.Nested(house_fields))
}


class SubAddResource(Resource):

    def post(self):

        args = sub_parser.parse_args()
        username = args.get('username')
        houseid = args.get('houseid')
        SubReposition().create(username, houseid)
        HouseReposition().sub_add(houseid)
        return


class SubFinishResource(Resource):

    def post(self):
        args = sub_parser.parse_args()
        username = args.get('username')
        houseid = args.get('houseid')
        SubReposition().finish(username, houseid)
        HouseReposition().sub_finish(houseid)
        return


class SubPassResource(Resource):

    def post(self):
        args = sub_parser.parse_args()
        username = args.get('username')
        houseid = args.get('houseid')
        HouseReposition().sub_finish(houseid)
        return


class SubJudgeResource(Resource):

    def post(self):
        args = sub_parser.parse_args()
        username = args.get('username')
        houseid = args.get('houseid')
        HouseReposition().sub_judge(houseid)
        return


class SelectSubResource(Resource):

    @marshal_with(back_house_fields)
    def post(self):
        args = select_sub.parse_args()
        username = args.get('username')
        subs = SubReposition().select_sub(username)
        houses = []
        for item in subs:
            house = HouseReposition().select_by_id(item.houseid)
            houses.append(house)
        data = {
            'data': houses
        }
        return data