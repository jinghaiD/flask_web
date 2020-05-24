from flask_restful import Resource, abort, fields, marshal_with, reqparse
from App.reposition.history_reposition import HistoryReposition
from App.reposition.house_reposition import HouseReposition


history = reqparse.RequestParser()
history.add_argument('houseid', type=int, required=True)
history.add_argument('username', type=str, required=True)

select_history = reqparse.RequestParser()
select_history.add_argument('username', type=str, required=True)


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


class HistoryResource(Resource):


    def post(self):

        args = history.parse_args()
        houseid = args.get('houseid')
        username = args.get('username')
        HistoryReposition().create(username, houseid)
        return


class SelectHistoryResource(Resource):

    @marshal_with(back_house_fields)
    def post(self):
        args = select_history.parse_args()
        username = args.get('username')
        history = HistoryReposition().select_history(username)
        houses = []
        for item in history:
            house = HouseReposition().select_by_id(item.houseid)
            houses.append(house)
        data = {
            'data': houses
        }
        return data