# Custom Model

# Author: P8ul
# https://github.com/p8ul

"""
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
        self.table = 'answers'

    def save(self, question_id, data):
        """
        Creates an answer record in answers table
        :param question_id: string: question id
        :param data: dict: answer values
        :return: None of inserted record
        """
        con = psycopg2.connect(**self.config)
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute(
                """
                INSERT INTO 
                    answers (user_id, answer_body, question_id)
                values(
                    '""" + str(session.get('user_id')) + """',
                    '""" + data.get('answer_body') + """',
                    '""" + question_id + """'
                )
                """
            )

            con.commit()
            con.close()
        except Exception as e:
            print(e)
            return None
        con.close()
        return data

    def query(self):
        """
        Fetch all records from a answers table
        :return: list: query set
        """
        con = psycopg2.connect(**self.config)
        cur = con.cursor(cursor_factory=RealDictCursor)
        cur.execute(
            """
            SELECT
               *,
               ( 
                SELECT 
                    count(*) from votes 
                WHERE 
                    votes.answer_id=answers.answer_id
                AND
                    vote=true
                ) as upVotes,
                ( 
                SELECT 
                    count(*) from votes 
                WHERE 
                    votes.answer_id=answers.answer_id
                AND
                    vote=false
                ) as downVotes
            FROM 
                answers
            """
        )
        queryset_list = cur.fetchall()
        con.close()
        return queryset_list

    def filter_by(self, instance_id=None, user_id=None):
        """
        Select a column(s) from answer table
        :param instance_id: string: answer id
        :param user_id: string: user id
        :return: list: queryset list
        """
        filter_column = 'question_id' if instance_id else 'user_id'
        filter_value = instance_id if instance_id else user_id
        con = psycopg2.connect(**self.config)
        cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("select * from {} WHERE {}= '{}'".format(self.table, filter_column, filter_value))
        queryset_list = cur.fetchall()
        con.close()
        return queryset_list

    def question_author(self, question_id):
        con = psycopg2.connect(**self.config)
        try:
            cur = con.cursor(cursor_factory=RealDictCursor)
            cur.execute(
                """ 
                SELECT 
                    user_id 
                FROM 
                    questions 
                WHERE 
                    question_id=""" + question_id + """
                """
            )
            return cur.fetchall()

        except Exception as e:
            print(e)
        con.close()
        return False

    def answer_author(self, answer_id):
        try:
            con = psycopg2.connect(**self.config)
            cur = con.cursor(cursor_factory=RealDictCursor)
            cur.execute(
                """ 
                SELECT 
                    user_id 
                FROM 
                    answers 
                WHERE 
                    answer_id=""" + answer_id + """
                """
            )
            queryset_list = cur.fetchall()
            con.close()
            return queryset_list
        except Exception as e:
            print(e)
            return False

    def update(self, question_id, answer_id, data=None):
        try:
            answer_author = self.answer_author(answer_id)[0].get('user_id')
            question_author = self.question_author(question_id)[0].get('user_id')
            # current user is the answer author
            if answer_author == session.get('user_id'):
                # update answer
                response = 200 if self.update_answer(answer_id, data) else 304
                return response

            # current user is question author
            elif question_author == session.get('user_id'):
                # mark it as accepted
                response = self.update_accept_field(question_id, answer_id, data)
                response = 200 if response else 304
                return response

            # other users
            else:
                return 203
        except:
            return 404

    def update_accept_field(self, question_id, answer_id, data=None):
        """
        Update an answer column
        :param question_id: string: question id
        :param answer_id: string: answer id
        :param data: dict: updated values
        :return: bool:
        """
        con = psycopg2.connect(**self.config)
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute(
                """
                UPDATE answers SET 
                    accepted='""" + data.get('accepted') + """'
                WHERE 
                    answer_id=""" + answer_id + """
                AND question_id=""" + question_id + """
                """
            )

            con.commit()
        except Exception as e:
            print(e)
            con.close()
            return False
        con.close()
        return True

    def update_answer(self, answer_id, data=None):
        """
        Update an answer column
        :param question_id: string: question id
        :param answer_id: string: answer id
        :param data: dict: updated values
        :return: bool:
        """
        con = psycopg2.connect(**self.config)
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute(
                """
                UPDATE answers SET 
                    answer_body='""" + data.get('body') + """'
                WHERE 
                    answer_id=""" + answer_id + """
                """
            )

            con.commit()
        except Exception as e:
            print(e)
            con.close()
            return False
        con.close()
        return True

    def delete(self, instance_id):
        pass


Table = ModelTable()



