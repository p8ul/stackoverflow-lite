from flask import Blueprint, jsonify, session
from flask.views import MethodView
from app.questions.models import Question
from ....utils import jwt_required

users_blueprint = Blueprint('users', __name__)


class UsersListAPIView(MethodView):
    """ Update Instance api resource """
    @jwt_required
    def get(self):
        data = {'user_id': session.get('user_id')}
        response_object = {
            'results': Question(data).filter_by_user()
        }
        return (jsonify(response_object)), 200


class UsersStatsAPIView(MethodView):
    """ Update Instance api resource """
    @jwt_required
    def get(self):
        data = {'user_id': session.get('user_id')}
        response_object = {
            'results': Question(data).user_statistics()
        }
        return (jsonify(response_object)), 200


# Define the API resources
user_view = UsersListAPIView.as_view('user_api')
stats_view = UsersStatsAPIView.as_view('stats_view')

# Add Rules for API Endpoints
users_blueprint.add_url_rule(
    '/api/v1/users/questions',
    view_func=user_view,
    methods=['GET']
)

users_blueprint.add_url_rule(
    '/api/v1/users/stats',
    view_func=stats_view,
    methods=['GET']
)
