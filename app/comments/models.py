"""
    Comments model
"""
import psycopg2
import psycopg2.extensions
from psycopg2.extras import RealDictCursor
from flask import session
from ..utils import db_config


class Comment:
    def __init__(self, data={}):
        self.config = db_config()
        self.table = 'comments'
        self.answer_id = data.get('answer_id')
        self.question_id = data.get('question_id')
        self.comment_body = data.get('comment_body')

    def save(self):
        """
        Insert a comment in comments table
        :return: True if record values are inserted successfully else false
        """
        con = psycopg2.connect(**self.config)
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            query = "INSERT INTO comments(user_id, answer_id, comment_body) values(%s, %s, %s) "
            cur.execute(query, (session.get('user_id'), self.answer_id, self.comment_body))
            con.commit()
        except Exception as e:
            print(e)
            con.close()
            return False
        return True
