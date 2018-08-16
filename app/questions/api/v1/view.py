# APIs Resources

# Author: P8ul
# https://github.com/p8ul

from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView
from ...models import Table
from ....utils import jwt_required

question_blueprint = Blueprint('questions', __name__)


class CreateAPIView(MethodView):
    """
    Create API Resource
    """
    @jwt_required
    def post(self):
        # get the post data
        post_data = request.get_json(force=True)
        instance = Table.save(data=post_data)
        if instance:
            response_object = {
                'status': 'success',
                'message': instance
            }
            return make_response(jsonify(response_object)), 201

        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return make_response(jsonify(response_object)), 401


class ListAPIView(MethodView):
    """
    List API Resource
    """
    @jwt_required
    def get(self, instance_id=None, user_id=None):
        if instance_id:
            query = {
                'instance_id': instance_id,
                'user_id': user_id
            }
            results = Table.filter_by(**query)
            if len(results) < 1:
                response_object = {
                    'results': 'Instance not found',
                    'status': 'error'
                }
                return make_response(jsonify(response_object)), 404
            response_object = {
                'results': results,
                'status': 'success'
            }
            return (jsonify(response_object)), 200

        response_object = {
            'results': Table.query(),
            'status': 'success'
        }
        return (jsonify(response_object)), 200


# Define the API resources
create_view = CreateAPIView.as_view('create_api')
list_view = ListAPIView.as_view('list_api')

# Add Rules for API Endpoints
question_blueprint.add_url_rule(
    '/api/v1/questions/',
    view_func=create_view,
    methods=['POST']
)

question_blueprint.add_url_rule(
    '/api/v1/questions/',
    view_func=list_view,
    methods=['GET']
)

question_blueprint.add_url_rule(
    '/api/v1/questions/<int:instance_id>',
    view_func=list_view,
    methods=['GET']
)
