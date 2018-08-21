from flask import Blueprint, jsonify, session
from flask.views import MethodView
from ....questions.models import Question
from ....utils import jwt_required

users_blueprint = Blueprint('users', __name__)


class ListAPIView(MethodView):
    """ Update Instance api resource """
    @jwt_required
    def get(self):
        data = {'user_id': session.get('user_id')}
        response_object = {
            'results': Question(data).filter_by_user(),
            'status': 'success'
        }
        return (jsonify(response_object)), 200


# Define the API resources
comment_view = ListAPIView.as_view('user_api')

# Add Rules for API Endpoints
users_blueprint.add_url_rule(
    '/api/v1/users/questions',
    view_func=comment_view,
    methods=['GET']
)
