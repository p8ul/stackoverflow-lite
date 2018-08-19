# APIs Resources

# Author: P8ul
# https://github.com/p8ul

from flask import Blueprint, request, make_response, jsonify, session
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
        data = request.get_json(force=True)
        data['user_id'] = session.get('user_id')
        row = Table(data).save()
        if row:
            response_object = {
                'status': 'success',
                'results': row
            }
            return make_response(jsonify(response_object)), 201

        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return make_response(jsonify(response_object)), 401

    """ UPDATE QUESTION """
    @jwt_required
    def put(self, question_id=None):
        # get the post data
        data = request.get_json(force=True)
        data['question_id'] = question_id
        data['user_id'] = session.get('user_id')
        result = Table(data).update()
        if result:
            response_object = {
                'status': 'success',
                'results': data
            }
            return make_response(jsonify(response_object)), 201

        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return make_response(jsonify(response_object)), 401

    """ DELETE QUESTION """
    @jwt_required
    def delete(self, question_id=None):
        data = dict()
        data['user_id'], data['question_id'] = session.get('user_id'), question_id
        response = Table(data).delete()
        if response == 401:
            response_object = {
                'status': 'fail',
                'message': 'Unauthorized, You cannot delete this question!.'
            }
            return make_response(jsonify(response_object)), 401
        if response == 404:
            response_object = {'status': 'fail', 'message': 'Some error occurred. Question Not Found!.'}
            return make_response(jsonify(response_object)), 404
        if not response:
            response_object = {
                'status': 'fail',
                'message': 'Some error occurred. Please try again.'
            }
            return make_response(jsonify(response_object)), 400
        response_object = {
            'status': 'success',
            'message': 'Question deleted successfully'
        }
        return make_response(jsonify(response_object)), 200


class ListAPIView(MethodView):
    """ List API Resource """
    @jwt_required
    def get(self, instance_id=None, user_id=None):
        data = dict()
        data['question_id'] = instance_id
        data['user_id'] = session.get('user_id')
        if user_id:
            results = Table({}).filter_by_user()
            if results:
                response_object = {'results': results, 'status': 'success'}
                return (jsonify(response_object)), 200
        if instance_id:
            results = Table(data).filter_by()
            if not results:
                response_object = {'status': 'fail', 'message': 'Bad request.'}
                return make_response(jsonify(response_object)), 400
            if len(results) < 1:
                response_object = {'results': 'Question not found', 'status': 'error'}
                return make_response(jsonify(response_object)), 404
            response_object = {'results': results, 'status': 'success'}
            return (jsonify(response_object)), 200
        response_object = {
            'results': Table({'q': request.args.get('q')}).query(), 'status': 'success'
        }
        return (jsonify(response_object)), 200


class UserQuestionsListAPIView(MethodView):
    """
    List API Resource
    """
    @jwt_required
    def get(self, user):
        data = {'user_id': session.get('user_id')}
        results = Table(data).filter_by_user()
        if results:
            response_object = {'results': results, 'status': 'success'}
            return (jsonify(response_object)), 200

        response_object = {'results': 'Bad Request'}
        return (jsonify(response_object)), 400


# Define the API resources
create_view = CreateAPIView.as_view('create_api')
list_view = ListAPIView.as_view('list_api')
user_questions_list_view = ListAPIView.as_view('user_questions_api')

# Add Rules for API Endpoints
question_blueprint.add_url_rule(
    '/api/v1/questions/',
    view_func=create_view,
    methods=['POST']
)

question_blueprint.add_url_rule(
    '/api/v1/questions/<string:question_id>',
    view_func=create_view,
    methods=['DELETE']
)

question_blueprint.add_url_rule(
    '/api/v1/questions/<string:question_id>',
    view_func=create_view,
    methods=['PUT']
)

question_blueprint.add_url_rule(
    '/api/v1/questions/',
    view_func=list_view,
    methods=['GET']
)

question_blueprint.add_url_rule(
    '/api/v1/questions/user/<string:user_id>',
    view_func=user_questions_list_view,
    methods=['GET']
)

question_blueprint.add_url_rule(
    '/api/v1/questions/<string:instance_id>',
    view_func=list_view,
    methods=['GET']
)
