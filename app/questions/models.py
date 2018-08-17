# Custom Model

# Author: P8ul
# https://github.com/p8ul

"""

    This class will connect to a Database and perform crud actions
    Has relevant getters, setters & mutation methods
    Methods:
        __init__()
            Initializes default class data/Methods

        save(title=None)
            Takes in a title and save it in the class data variable
            Generates unique id for each instance
            :returns saved object (dict)

        query()
            Queries all the data (dict) stored in the class data variable
            :returns dictionary

        filter_by(instance_id=None)
            :param instance_id :int Id of instance to be edited
            Filters class data by id

        update(instance_id, title)
            :param instance_id: :int Id of instance to be edited
            :param title: :string New title used to replace original title
        answer(instance_id, answer=None)
            :param instance_id: :int Id of instance to be edited
            :param answer :string Answer to a question
            :returns answer from the argument and created_at timestamp

        delete(instance_id)
            :param instance_id :int
            destroys instance data from class data variable

"""
import psycopg2
import psycopg2.extensions
from psycopg2.extras import RealDictCursor
from config import BaseConfig
from ..utils import db_config


class ModelTable:
    def __init__(self):
        self.config = db_config(BaseConfig.SQLALCHEMY_DATABASE_URI)
        self.table = 'questions'

    def save(self, data):
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

    def query(self):
        con = psycopg2.connect(**self.config)
        cur = con.cursor(cursor_factory=RealDictCursor)
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
        queryset_list = cur.fetchall()
        con.close()
        return queryset_list

    def filter_by(self, instance_id=None):
        try:
            con = psycopg2.connect(**self.config)
            cur = con.cursor(cursor_factory=RealDictCursor)
            cur2 = con.cursor(cursor_factory=RealDictCursor)
            cur.execute(
                """
                select * from questions
                WHERE questions.question_id=""" + instance_id + """
                ORDER BY questions.created_at
                """
            )
            questions_queryset_list = cur.fetchall()
            cur2.execute(
                """
                select * from answers
                WHERE answers.question_id=""" + instance_id + """
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

    def update(self, instance_id, data=None):
        pass

    def delete(self, instance_id):
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
