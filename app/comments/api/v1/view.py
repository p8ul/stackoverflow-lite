from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView
from ...models import Table
from ....utils import jwt_required

comments_blueprint = Blueprint('comments', __name__)


class ListAPIView(MethodView):
    """ Update Instance api resource """

    @jwt_required
    def post(self, answer_id=None):
        post_data = request.get_json(force=True)
        response = Table.save(answer_id, data=post_data)
        if response:
            response_object = {
                'status': 'success',
                'message': 'Your comment was successful'
            }
            return make_response(jsonify(response_object)), 201

        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return make_response(jsonify(response_object)), 400


# Define the API resources
comment_view = ListAPIView.as_view('comment_api')

# Add Rules for API Endpoints
comments_blueprint.add_url_rule(
    '/api/v1/questions/answers/comment/<string:answer_id>',
    view_func=comment_view,
    methods=['POST']
)
