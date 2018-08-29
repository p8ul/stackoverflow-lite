
"""  Auth model """
import psycopg2
import psycopg2.extras
from psycopg2.extras import RealDictCursor
from ..utils import db_config, is_blacklisted


class Blacklist:
    def __init__(self, data={}):
        self.config = db_config()
        self.token = data.get('token')

    def blacklist_token(self):
        if is_blacklisted(self.token):
            return {
                'message': 'Token already in blacklist',
                'status': 'fail'
            }
        con, response = psycopg2.connect(**self.config), None
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            query = "INSERT INTO token_blacklist (token) values('{}') RETURNING *"
            cur.execute(query.format(self.token))
            con.commit()
            response = cur.fetchone()
        except Exception as e:
            print(e)
        con.close()
        return response
