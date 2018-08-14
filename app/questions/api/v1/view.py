### APIs Resources

# Author: P8ul Kinuthia
# https://github.com/p8ul

from flask_restful import Resource, Api
from flask import Blueprint, request
from ...models import Table

api = Blueprint('api', __name__, url_prefix='/api/v1')
api_wrap = Api(api)

""" Create an instance of a Question `table` (Class) """
global Table
Table = Table()


class ListRetrieveAPIView(Resource):
    def get(self, question_id=None):
        if question_id:
            response = Table.filter_by(int(question_id))
            if not response:
                return {"status": "error", "data": "Question Not Found"}, 404
        else:
            response = [instance for instance in Table.query()]
        return {"status": "success", "data": response}, 200

    def post(self, question_id=None):
        json_data = request.get_json(force=True)
        answer = json_data.get('answer')
        if question_id and answer:
            response = Table.answer(instance_id=question_id, answer=answer)
            if not response:
                return {"status": "error", "data": "Question Not Found"}, 404
        else:
            response = Table.save(data=json_data)
        return {"status": "success", "data": response}, 201

    def put(self, question_id):
        json_data = request.get_json(force=True)
        response = Table.update(instance_id=question_id, data=json_data)
        if not response:
            return {"status": "error", "data": "Question Not Found"}, 404
        return {"status": "success", "data": response}, 200

    def delete(self, question_id):
        response = Table.delete(question_id)
        if response:
            return {"status": "deleted", "data": 'Deleted successfully'}, 204
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
