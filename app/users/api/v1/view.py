from flask_restful import Resource, Api
from flask import Blueprint, request
from ...models import Table

api = Blueprint('user_api', __name__, url_prefix='/api/v1')
api_wrap = Api(api)

""" Create an instance of a User `table` (Class) """
global Table
Table = Table()


class ListRetrieveAPIView(Resource):
    def get(self, user_id=None):
        if user_id:
            response = Table.filter_by(int(user_id))
            if not response:
                return {"status": "error", "data": "User Not Found"}, 404
        else:
            response = [instance for instance in Table.query()]
        return {"status": "success", "data": response}, 200

    def post(self, user_id=None):
        json_data = request.get_json(force=True)
        response = Table.save(data=json_data)
        return {"status": "success", "data": response}, 201

    def put(self, user_id):
        json_data = request.get_json(force=True)
        response = Table.update(instance_id=user_id, data=json_data)
        if not response:
            return {"status": "error", "data": "User Not Found"}, 404
        return {"status": "success", "data": response}, 200

    def delete(self, user_id):
        response = Table.delete(user_id)
        if response:
            return {"status": "deleted", "data": 'Deleted successfully'}, 204
        return {"status": "error", "data": "User Not Found"}, 404


api_wrap.add_resource(
    ListRetrieveAPIView,
    '/users/',
    '/users/<string:user_id>',
    '/users/<string:user_id>/',
    '/users/<int:user_id>'
)
