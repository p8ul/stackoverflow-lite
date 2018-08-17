# Custom Model

# Author: P8ul
# https://github.com/p8ul

"""
    This class will connect to a Database and perform crud actions
    Has relevant getters, setters & mutation methods
    Methods:
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
        self.table = 'questions'

    def save(self, data):
        """
        Create a question record in questions table
        :param data: dict: question values
        :return: None or record values
        """
        con = psycopg2.connect(**self.config)
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute(
                """
                INSERT INTO questions(title, body, user_id)
                values(
                    '""" + data.get('title') + """',
                    '""" + data.get('body') + """',
                    '""" + data.get('user') + """'
                )
                """
            )

            con.commit()
        except Exception as e:
            print(e)
            con.close()
            return None
        con.close()
        return data

    def query(self, q):
        """
        Query the data in question table
        :return: list: query set list
        """
        con = psycopg2.connect(**self.config)
        cur = con.cursor(cursor_factory=RealDictCursor)
        if not q:
            cur.execute(
                """
                SELECT
                   *,
                   ( 
                    select count(*) from answers 
                    where answers.question_id=questions.question_id
                    ) as answers_count
                FROM 
                    questions
                """
            )
        else:
            cur.execute(
                """
                SELECT
                   *,
                   ( 
                    select count(*) from answers 
                    where answers.question_id=questions.question_id
                    ) as answers_count
                FROM 
                    questions
                WHERE
                    body LIKE 
                    '%""" + q + """%'
                OR
                    title LIKE 
                    '%""" + q + """%'
                
                """
            )
        queryset_list = cur.fetchall()
        con.close()
        return queryset_list

    def filter_by(self, instance_id=None):
        """
        Selects a question by id
        :param instance_id: string: question id
        :return: False if record is not found else query list of found record
        """
        try:
            con = psycopg2.connect(**self.config)
            cur = con.cursor(cursor_factory=RealDictCursor)
            cur2 = con.cursor(cursor_factory=RealDictCursor)
            cur.execute(
                """
                SELECT * FROM
                    questions
                WHERE 
                    questions.question_id=""" + instance_id + """
                ORDER BY questions.created_at
                """
            )
            questions_queryset_list = cur.fetchall()
            cur2.execute(
                """
                SELECT * FROM
                    answers
                WHERE 
                    answers.question_id=""" + instance_id + """
                """
            )
            answers_queryset_list = cur2.fetchall()
            result = {
                'question': questions_queryset_list,
                'answers': answers_queryset_list
            }
        except Exception as e:
            print(e)
            con.close()
            return False
        con.close()
        return result

    def filter_by_user(self, user_id=None):
        """
        Selects question for specific user:default filters by current logged in user
        :param user_id: string: question id
        :return: False if record is not found else query list of found record
        """
        if not user_id:
            user_id = session.get('user_id')
        try:
            con = psycopg2.connect(**self.config)
            cur = con.cursor(cursor_factory=RealDictCursor)
            cur.execute(
                """
                SELECT * FROM
                    questions
                WHERE 
                    questions.user_id=""" + user_id + """
                ORDER BY questions.created_at
                """
            )
            questions_queryset_list = cur.fetchall()

            result = {
                'question': questions_queryset_list
            }
        except Exception as e:
            print(e)
            con.close()
            return False
        con.close()
        return result

    def update(self, instance_id, data=None):
        pass

    def delete(self, instance_id):
        """
        Delete a table records
        :param instance_id: string: question id
        :return: bool
        """
        try:
            exist = self.filter_by(instance_id)
            if not len(exist) > 0:
                return 404
            con = psycopg2.connect(**self.config)
            cur = con.cursor(cursor_factory=RealDictCursor)
            cur.execute("DELETE from {} WHERE {}= '{}'".format(self.table, 'question_id', instance_id))
            con.commit()
        except Exception as e:
            print(e)
            con.close()
            return False
        con.close()
        return True


Table = ModelTable()
