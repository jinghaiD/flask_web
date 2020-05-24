from flask_restful import Resource, abort, fields, marshal_with, reqparse
from App.reposition.house_reposition import HouseReposition


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


class Admin3Resource(Resource):

    @marshal_with(back_house_fields)
    def post(self):
        house = HouseReposition().select_by_status(3)
        data = {
            'data': house
        }
        return data


class Admin2Resource(Resource):

    @marshal_with(back_house_fields)
    def post(self):
        house = HouseReposition().select_by_status(2)
        data = {
            'data': house
        }
        return data
