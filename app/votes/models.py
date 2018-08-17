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
        self.table = 'votes'

    def vote_exists(self, answer_id=None):
        """
        Checks if vote for a particular answer
        is voted by current user
        :param answer_id: Answer foreign key
        :return: True if vote exist else False
        """
        con = psycopg2.connect(**self.config)
        cur = con.cursor(cursor_factory=RealDictCursor)
        cur.execute(
            """ SELECT user_id, vote_id FROM votes WHERE 
                answer_id=""" + answer_id + """
            AND 
                user_id=""" + str(session.get('user_id')) + """
            """
        )
        queryset_list = cur.fetchall()
        if len(queryset_list) < 1:
            return False
        return True

    def create_vote(self, answer_id=None, data=None):
        """
        Insert a vote in votes table
        :param answer_id: string: answer id
        :param data: dict: votes values
        :return: True if record values are inserted successfully else false
        """
        con = psycopg2.connect(**self.config)
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute(
                """
                INSERT INTO 
                    votes(user_id, answer_id, vote)
                values(
                    """ + str(session.get('user_id')) + """,
                    """ + str(answer_id) + """,
                    """ + str(data.get('vote')) + """
                )
                """
            )
            con.commit()
        except Exception as e:
            print(e)
            con.close()
            return False
        return True

    def update_vote(self, answer_id=None, data=None):
        """
        Modify record from votes table
        :param answer_id: string: answer id
        :param data: raw data value to for updating column values
        :return:
        """
        try:
            con = psycopg2.connect(**self.config)
            cur = con.cursor(cursor_factory=RealDictCursor)
            cur.execute(
                """
                UPDATE votes SET 
                    vote='""" + data.get('vote') + """'
                WHERE 
                    answer_id=""" + answer_id + """
                AND 
                    user_id=""" + str(session.get('user_id')) + """
                """
            )
            con.commit()
        except Exception as e:
            print(e)
            con.close()
            return False
        return True

    def vote(self, answer_id=None, data=None):
        """
        Switch bus for updating or creating a vote
        :param answer_id: string: answer id
        :param data: dict: raw vote values
        :return: bool: True if transaction is
                       completed successfully else false
        """
        if self.vote_exists(answer_id):
            return self.update_vote(answer_id, data)
        return self.create_vote(answer_id, data)

    def delete(self, instance_id):
        pass

    def save(self):
        pass


Table = ModelTable()



