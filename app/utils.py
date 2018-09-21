from urllib.parse import urlparse
import datetime
import os
import re
from functools import wraps
from flask import request, make_response, jsonify, session
import jwt
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor
from config import BaseConfig


def db_config(database_uri=None):
    """ This function extracts postgres url
    and return database login information
    :param database_uri: database Configuration uri
    :return: database login information
    """
    load_dotenv()
    if os.environ.get('DATABASE_URL'):
        database_uri = os.environ.get('DATABASE_URL')

    result = urlparse(database_uri)
    config = {
        'database': result.path[1:],
        'user': result.username,
        'password': result.password,
        'host': result.hostname
    }

    if os.environ.get('APP_SETTINGS') == 'TESTING':
        config['database'] = BaseConfig.TEST_DB
    return config


def is_blacklisted(token):
    """ Checks whether a token is blacklisted """
    con, queryset_list = psycopg2.connect(**db_config()), None
    cur = con.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute("select * from token_blacklist WHERE token='{}'".format(token))
        queryset_list = cur.fetchall()
    except Exception as e:
        print(e)
    con.close()
    return queryset_list


def jwt_required(f):
    """ Ensure jwt token is provided and valid
        :param f: function to decorated
        :return: decorated function
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            auth_header = request.headers.get('Authorization').split(' ')[-1]
        except Exception as e:
            print(e)
            return make_response(jsonify({"message": 'Unauthorized. Please login'})), 401
        result = decode_auth_token(auth_header)
        try:
            if int(result):
                pass
        except Exception as e:
            print(e)
            if not result:
                result = 'Unauthorized. Please login'
            return make_response(jsonify({"message": result})), 401
        return f(*args, **kwargs)
    return decorated_function


def encode_auth_token(user_id, username=None):
    """
    Encodes a payload to generate JWT Token
    :param user_id: Logged in user Id
    :param username: string: Logged in username
    :return: JWT token
    :TODO add secret key to app configuration
    """
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=31, seconds=130),
        'iat': datetime.datetime.utcnow(),
        'sub': user_id,
        'username': username
    }
    return jwt.encode(
        payload,
        'SECRET_KEY',
        algorithm='HS256'
    )


def decode_auth_token(auth_token):
    """ Validates the auth token
    :param auth_token:
    :return: integer|string
    """
    try:
        if is_blacklisted(auth_token):
            return 'Token has been blacklisted. Please log in again'
        payload = jwt.decode(auth_token, 'SECRET_KEY', algorithm='HS256')
        session['user_id'] = str(payload.get('sub'))
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Token Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'


def valid_email(email):
    """  Validate email """
    try:
        if email.count('@') > 1:
            return False
        last_part = email.split('@'[-1])[-1]
        if last_part.count('.com') > 1:
            return False
        return re.match(r'^.+@([?)[a-zA-Z0-9-.])+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$', email)
    except Exception as e:
        print(e)
        return False
