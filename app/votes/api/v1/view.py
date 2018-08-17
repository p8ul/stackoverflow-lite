from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView
from ...models import Table
from ....utils import jwt_required

votes_blueprint = Blueprint('votes', __name__)


class VoteAPIView(MethodView):
    """ Update Instance api resource """

    @jwt_required
    def post(self, answer_id=None):
        post_data = request.get_json(force=True)
        response = Table.vote(str(answer_id), data=post_data)
        if response:
            response_object = {
                'status': 'success',
                'message': 'Your vote was successful'
            }
            return make_response(jsonify(response_object)), 201

        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return make_response(jsonify(response_object)), 400


# Define the API resources
vote_view = VoteAPIView.as_view('vote_api')

# Add Rules for API Endpoints
votes_blueprint.add_url_rule(
    '/api/v1/questions/answers/vote/<string:answer_id>',
    view_func=vote_view,
    methods=['POST']
)
