from flask import Blueprint, request, make_response, jsonify, session
from flask.views import MethodView
from app.questions.models import Question
from ....utils import jwt_required

question_blueprint = Blueprint('questions', __name__)


class CreateQuestionAPIView(MethodView):
    """
    Create API Resource
    """
    @jwt_required
    def get(self, question_id):
        response = Question({'question_id': question_id}).filter_by()
        if not response:
            response_object = {
                'status': 'fail',
                'results': 'Question Not found'
            }
            return make_response(jsonify(response_object)), 404

        response_object = {
            'status': 'success',
            'results': response
        }
        return make_response(jsonify(response_object)), 200

    @jwt_required
    def post(self):
        # get the post data
        data = request.get_json(force=True)
        data['user_id'] = session.get('user_id')
        row = Question(data).save()
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
        result = Question(data).update()
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
        response = Question(data).delete()
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


class QuestionsListAPIView(MethodView):
    """ List API Resource """
    @jwt_required
    def get(self):
        data = dict()
        data['user_id'] = session.get('user_id')
        response_object = {
            'results': Question({'q': request.args.get('q')}).query(), 'status': 'success'
        }
        return (jsonify(response_object)), 200


# Define the API resources
create_view = CreateQuestionAPIView.as_view('create_api')
list_view = QuestionsListAPIView.as_view('list_api')

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
    methods=['PUT', 'GET']
)

question_blueprint.add_url_rule(
    '/api/v1/questions/',
    view_func=list_view,
    methods=['GET']
)

