"""
    Author: P8ul
    https://github.com/p8ul

    This class will connect to a Database and perform crud actions
    Has relevant getters, setters & mutation methods
"""
import psycopg2
import psycopg2.extensions
from psycopg2.extras import RealDictCursor
from flask import session
from config import BaseConfig
from ..utils import db_config


class ModelTable:
    def __init__(self):
        self.config = db_config(BaseConfig.SQLALCHEMY_DATABASE_URI)
        self.table = 'comments'

    def save(self, answer_id=None, data=None):
        """
        Insert a comment in comments table
        :param answer_id: string: answer id
        :param data: dict: comment values
        :return: True if record values are inserted successfully else false
        """
        con = psycopg2.connect(**self.config)
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute(
                """
                INSERT INTO 
                    comments(user_id, answer_id, comment_body)
                values(
                    """ + str(session.get('user_id')) + """,
                    """ + str(answer_id) + """,
                    '""" + str(data.get('comment_body')) + """'
                )
                """
            )
            con.commit()
        except Exception as e:
            print(e)
            con.close()
            return False
        return True


Table = ModelTable()



