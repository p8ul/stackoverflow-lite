from flask import Blueprint, request, make_response, jsonify, session
from flask.views import MethodView
from flask_bcrypt import Bcrypt
from app.auth.models import User
from ....utils import jwt_required, encode_auth_token
from app.auth.validatons import validate_user_details

b_crypt = Bcrypt()
auth_blueprint = Blueprint('auth', __name__)


class RegisterAPI(MethodView):
    """ User Signup API Resource """
    def post(self):
        # get the post data
        data = request.get_json(force=True)
        data['user_id'] = session.get('user_id')
        data['user'] = User(data).filter_by_email()
        # check if user already exists
        errors = validate_user_details(data)
        if len(errors) > 0:
            response_object = {
                'status': 'fail', 'errors': errors
            }
            return make_response(jsonify(response_object)), 401
        try:
            user = User(data).save()
            auth_token = encode_auth_token(user.get('id')).decode()
            response_object = {
                'status': 'success',
                'message': 'Successfully registered.',
                'id': user.get('id'), 'auth_token': auth_token
            }
            return make_response(jsonify(response_object)), 201
        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail', 'message': 'Some error occurred. Please try again.'
            }
            return make_response(jsonify(response_object)), 401

    def delete(self, user_id=None):
        data = request.get_json(force=True)
        data['user_id'] = user_id
        User(data).delete()
        response_object = {
            'status': 'success', 'message': 'User deleted successfully.',
        }
        return make_response(jsonify(response_object)), 200


class LoginAPI(MethodView):
    """ User Login API Resource """
    def post(self):
        data = request.get_json(force=True)
        data['user_id'] = session.get('user_id')
        try:
            user = User(data).filter_by_email()
            if len(user) >= 1 and data.get('password'):
                if b_crypt.check_password_hash(user[0].get('password'), data.get('password')):
                    auth_token = encode_auth_token(user[0].get('user_id'))
                else:
                    response_object = {'status': 'fail', 'message': 'Password or email do not match.'}
                    return make_response(jsonify(response_object)), 401
                try:
                    if auth_token:
                        response_object = {
                            'status': 'success', 'id': user[0].get('user_id'),
                            'message': 'Successfully logged in.',
                            'auth_token': auth_token.decode()
                        }
                        return make_response(jsonify(response_object)), 200
                except Exception as e:
                    return {"message": 'Error decoding token'}, 401
            else:
                response_object = {'status': 'fail', 'message': 'User does not exist.'}
                return make_response(jsonify(response_object)), 404
        except Exception as e:
            print(e)
            response_object = {'status': 'fail', 'message': 'Try again'}
            return make_response(jsonify(response_object)), 500


class UserListAPI(MethodView):
    """ User List Api Resource """
    @jwt_required
    def get(self, user_id=None):
        if user_id:
            user = User({"user_id": user_id}).filter_by()
            response_object = {'results': 'User not found', 'status': 'fail'}
            try:
                if len(user) < 1:
                    return make_response(jsonify(response_object)), 404
            except:
                return make_response(jsonify(response_object)), 404
            response_object = {
                'results': user,
                'status': 'success'
            }
            return (jsonify(response_object)), 200

        response_object = {
            'results': User().query(),
            'status': 'success'
        }
        return (jsonify(response_object)), 200


class LogoutAPI(MethodView):
    """ Logout Resource """
    def post(self):
        # get auth token
        auth_header = request.headers.get('Authorization')
        return auth_header


# Define the API resources
registration_view = RegisterAPI.as_view('register_api')
login_view = LoginAPI.as_view('login_api')
user_view = UserListAPI.as_view('user_api')
logout_view = LogoutAPI.as_view('logout_api')

# Add Rules for API Endpoints
auth_blueprint.add_url_rule(
    '/api/v1/auth/signup',
    view_func=registration_view,
    methods=['POST']
)

# Add Rules for API Endpoints
auth_blueprint.add_url_rule(
    '/api/v1/auth/delete',
    view_func=registration_view,
    methods=['DELETE']
)
auth_blueprint.add_url_rule(
    '/api/v1/auth/login',
    view_func=login_view,
    methods=['POST']
)
auth_blueprint.add_url_rule(
    '/api/v1/auth/users',
    view_func=user_view,
    methods=['GET']
)
auth_blueprint.add_url_rule(
    '/api/v1/auth/users/<string:user_id>',
    view_func=user_view,
    methods=['GET']
)
auth_blueprint.add_url_rule(
    '/api/v1/auth/logout',
    view_func=logout_view,
    methods=['POST']
)
