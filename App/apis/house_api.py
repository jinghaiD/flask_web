from flask_restful import Resource, fields, marshal_with, reqparse
from App.models.house import House
from App.reposition.house_reposition import HouseReposition

house_fields = {
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
    'price': fields.Integer
}

back_fields = {
    'data': fields.Nested(house_fields)
}

back_house_fields = {
    'data': fields.List(fields.Nested(house_fields))
}

house_parser = reqparse.RequestParser()
house_parser.add_argument('id', type=int, required=True)

class HouseResource(Resource):

    @marshal_with(back_house_fields)
    def get(self):

        houses = HouseReposition().find_first()

        data = {
            'data': houses
        }

        return data

    @marshal_with(back_house_fields)
    def post(self):

        args = house_parser.parse_args()
        id = args.get('id')
        house = HouseReposition().select_by_id(id)
        data = {
            'data': house
        }
        return data