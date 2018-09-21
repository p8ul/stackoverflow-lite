from flask import Blueprint, request, make_response, jsonify, session
from flask.views import MethodView
from app.answers.models import Answer
from app.questions.models import Question
from ....utils import jwt_required

answers_blueprint = Blueprint('answers', __name__)


class AnswersAPIView(MethodView):
    @jwt_required
    def put(self, question_id=None, answer_id=None):
        data = request.get_json(force=True)
        data['question_id'] = question_id
        data['answer_id'] = answer_id
        data['user_id'] = session.get('user_id')

        response = Answer(data).update()
        if response.get('errors'):
            response_object = {
                'message': response.get('errors')
            }
            return make_response(jsonify(response_object)), 400
        response_object = {
            'message': 'Update successful'
        }
        return make_response(jsonify(response_object)), 200

    @jwt_required
    def delete(self, question_id=None, answer_id=None):
        data = dict()
        data['question_id'] = question_id
        data['answer_id'] = answer_id
        data['user_id'] = session.get('user_id')

        answer = Answer(data)
        # check permission
        if len(answer.answer_author()) < 1:
            response_object = {
                'message': 'Unauthorized'
            }
            return make_response(jsonify(response_object)), 401

        response = answer.delete()
        if not response:
            response_object = {
                'message': 'Answer id does not exist'
            }
            return make_response(jsonify(response_object)), 400
        response_object = {
            'message': 'Answer deleted successful'
        }
        return make_response(jsonify(response_object)), 200

    @jwt_required
    def post(self, question_id=None):
        data = request.get_json(force=True)
        data['question_id'], data['user_id'] = question_id, session.get('user_id')
        answer = Answer(data)
        response = answer.save()
        if response:
            response_object = {'message': response}
            return make_response(jsonify(response_object)), 201
        response_object = {
            'message': 'Unknown question id. Try a different id.'
        }
        return make_response(jsonify(response_object)), 400


class AnswersListAPIView(MethodView):
    """
    List API Resource
    """
    def get(self, answer_id=None):
        data = dict()
        data['answer_id'] = answer_id
        data['user_id'] = session.get('user_id')
        if answer_id:
            results = Answer(data).filter_by()
            if len(results) < 1:
                response_object = {
                    'results': 'Answer not found'
                }
                return make_response(jsonify(response_object)), 404
            response_object = {
                'results': results
            }
            return (jsonify(response_object)), 200
        response_object = {'results': Answer(data).query()}
        return (jsonify(response_object)), 200


# Define the API resources
create_view = AnswersAPIView.as_view('create_api')
list_view = AnswersListAPIView.as_view('list_api')

# Add Rules for API Endpoints
answers_blueprint.add_url_rule(
    '/api/v1/questions/<string:question_id>/answers',
    view_func=create_view,
    methods=['POST']
)

answers_blueprint.add_url_rule(
    '/api/v1/questions/<string:question_id>/answers/<string:answer_id>',
    view_func=create_view,
    methods=['PUT', 'DELETE']
)

answers_blueprint.add_url_rule(
    '/api/v1/questions/answers/<string:answer_id>',
    view_func=create_view,
    methods=['PUT', 'DELETE']
)

answers_blueprint.add_url_rule(
    '/api/v1/questions/answers',
    view_func=list_view,
    methods=['GET']
)

answers_blueprint.add_url_rule(
    '/api/v1/questions/answers/<string:answer_id>',
    view_func=list_view,
    methods=['GET']
)
