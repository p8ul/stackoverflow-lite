# APIs Resources

# Author: P8ul
# https://github.com/p8ul

from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView
from ...models import Table
from ....utils import jwt_required

answers_blueprint = Blueprint('answers', __name__)


class CreateAPIView(MethodView):
    """ Update Instance api resource """

    @jwt_required
    def put(self, question_id=None, answer_id=None):
        data = request.get_json(force=True)
        response = Table.update(question_id, answer_id, data)
        if response == 200:
            response_object = {
                'status': 'success',
                'message': 'Update successful'
            }
            return make_response(jsonify(response_object)), 200
        if response == 302:
            response_object = {
                'status': 'fail',
                'message': 'Please provide correct answer and question id'
            }
            return make_response(jsonify(response_object)), 400
        if response == 203:
            response_object = {
                'status': 'fail',
                'message': 'Unauthorized request.'
            }
            return make_response(jsonify(response_object)), 401

        else:
            response_object = {
                'status': 'fail',
                'message': 'Please provide correct answer and question id'
            }
            return make_response(jsonify(response_object)), 400


    """
    Create API Resource
    """
    @jwt_required
    def post(self, question_id=None):
        # get the post data
        post_data = request.get_json(force=True)
        response = Table.save(str(question_id), data=post_data)
        if response:
            response_object = {
                'status': 'success',
                'message': response
            }
            return make_response(jsonify(response_object)), 201

        response_object = {
            'status': 'fail',
            'message': 'Unknown question id. Try a different id.'
        }
        return make_response(jsonify(response_object)), 400


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
answers_blueprint.add_url_rule(
    '/api/v1/questions/<int:question_id>/answers',
    view_func=create_view,
    methods=['POST']
)

answers_blueprint.add_url_rule(
    '/api/v1/questions/<string:question_id>/answers/<string:answer_id>',
    view_func=create_view,
    methods=['PUT']
)

answers_blueprint.add_url_rule(
    '/api/v1/questions/answers',
    view_func=list_view,
    methods=['GET']
)
