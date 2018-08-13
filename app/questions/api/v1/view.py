from flask_restful import Resource, Api
from flask import Blueprint, request

api = Blueprint('api', __name__, url_prefix='/api/v1')
api_wrap = Api(api)

""" Create an instance of a Question `table` (Class) """


class ListRetrieveAPIView(Resource):
    def get(self, question_id=None):
        return {"status": "success", "data": []}, 200

    def post(self, question_id=None):
        return {"status": "success", "data": []}, 201

    def put(self, question_id):
        return {"status": "success", "data": []}, 200

    def delete(self, question_id):
        return {"status": "error", "data": "Question Not Found"}, 404


api_wrap.add_resource(
    ListRetrieveAPIView,
    '/questions/',
    '/questions/<string:question_id>',
    '/questions/<string:question_id>/',
    '/questions/<string:question_id>/answer',
    '/questions/<string:question_id>/answer/',
    '/questions/<int:question_id>'
)
