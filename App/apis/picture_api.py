from flask_restful import Resource, abort, fields, marshal_with, reqparse
from App.reposition.PictureReposition import PictureReposition


pic = reqparse.RequestParser()
pic.add_argument('houseid', type=int, required=True)

pic_fields = {
    'houseid': fields.Integer,
    'picture': fields.String
}
back_pic_fields = {
    'data': fields.List(fields.Nested(pic_fields))
}

class PictureResource(Resource):

    @marshal_with(back_pic_fields)
    def post(self):

        args = pic.parse_args()
        houseid = args.get('houseid')
        pics = PictureReposition().select_pics(houseid)
        data = {
            'data': pics
        }
        return data