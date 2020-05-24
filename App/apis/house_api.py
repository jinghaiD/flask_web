from flask_restful import Resource, fields, marshal_with, reqparse
from App.models.house import House
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

house_simple_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'type': fields.String,
    'bed': fields.Integer,
    'price': fields.Integer,
}
back_house_simple_fields = {
    'data': fields.List(fields.Nested(house_simple_fields))
}

owner_parser = reqparse.RequestParser()
owner_parser.add_argument('owner', type=str, required=True)

house_parser = reqparse.RequestParser()
house_parser.add_argument('id', type=int, required=True)

house_city_parser = reqparse.RequestParser()
house_city_parser.add_argument('city', type=str, required=True)

house_add = reqparse.RequestParser()
house_add.add_argument('jingdu', type=str, required=True)
house_add.add_argument('weidu', type=str, required=True)
house_add.add_argument('name', type=str, required=True)
house_add.add_argument('province', type=str, required=True)
house_add.add_argument('city', type=str, required=True)
house_add.add_argument('type', type=str, required=True)
house_add.add_argument('guest', type=int, required=True)
house_add.add_argument('room', type=int, required=True)
house_add.add_argument('bed', type=int, required=True)
house_add.add_argument('toilet', type=int, required=True)
house_add.add_argument('introduction', type=str, required=True)
house_add.add_argument('price', type=float, required=True)
house_add.add_argument('owner', type=str, required=True)


house_search = reqparse.RequestParser()
house_search.add_argument('people', type=int, required=True)
house_search.add_argument('bed', type=int, required=True)
house_search.add_argument('room', type=int, required=True)
house_search.add_argument('min', type=int, required=True)
house_search.add_argument('max', type=int, required=True)
house_search.add_argument('city', type=str, required=True)


class HouseSearchResource(Resource):

    @marshal_with(back_house_fields)
    def post(self):
        args = house_search.parse_args()
        people = args.get('people')
        bed = args.get('bed')
        room = args.get('room')
        min = args.get('min')
        max = args.get('max')
        city = args.get('city')
        house = HouseReposition().search(people,room,bed,min,max,city)
        data = {
            'data':house
        }
        return data


class HouseOwnerResource(Resource):

    @marshal_with(back_house_fields)
    def post(self):
        args = owner_parser.parse_args()
        owner = args.get('owner')
        house = HouseReposition().select_by_owner(owner)
        data={
            'data': house
        }
        return data


class HouseSimpleResource(Resource):

    @marshal_with(back_house_fields)
    def get(self):

        houses = HouseReposition().find_first()

        data = {
            'data': houses
        }

        return data

    @marshal_with(back_house_simple_fields)
    def post(self):

        args = house_parser.parse_args()
        id = args.get('id')
        house = HouseReposition().select_by_id(id)
        data = {
            'data': house
        }
        return data


class HouseResource(Resource):

    @marshal_with(back_house_fields)
    def post(self):

        args = house_parser.parse_args()
        houseid = args.get('id')
        house = HouseReposition().select_by_id(houseid)
        data = {
            'data': house
        }
        return data


class HouseCityResource(Resource):

    @marshal_with(back_house_fields)
    def post(self):

        args = house_city_parser.parse_args()
        city = args.get('city')
        house = HouseReposition().select_by_city(city)
        data = {
            'data': house
        }
        return data


class AddHouseResource(Resource):

    def post(self):
        args = house_add.parse_args()
        jingdu = args.get('jingdu')
        weidu = args.get('weidu')
        name = args.get('name')
        province = args.get('province')
        city = args.get('city')
        type = args.get('type')
        guest = args.get('guest')
        room = args.get('room')
        bed = args.get('bed')
        toilet = args.get('toilet')
        introduction = args.get('introduction')
        price = args.get('price')
        owner = args.get('owner')
        HouseReposition().add_house(jingdu,weidu,name,province,city,type,guest,room,bed,toilet,introduction,price,owner)
        return


class HouseJudgeResource(Resource):

    def post(self):

        args = house_city_parser.parse_args()
        houseid = args.get('houseid')
        HouseReposition().sub_judge(houseid)
        return