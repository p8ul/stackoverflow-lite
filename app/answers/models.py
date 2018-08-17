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

        filter_by(instance_id)
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
        self.table = 'answers'

    def save(self, question_id, data):
        con = psycopg2.connect(**self.config)
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute(
                """
                INSERT INTO answers (user_id, answer_body, question_id)
                values(
                    '""" + data.get('user_id') + """',
                    '""" + data.get('answer_body') + """',
                    '""" + question_id + """'
                )
                """
            )

            con.commit()
        except Exception as e:
            print(e)
            return None
        con.close()
        return data

    def query(self):
        con = psycopg2.connect(**self.config)
        cur = con.cursor(cursor_factory=RealDictCursor)
        cur.execute('select * from {}'.format(self.table))
        queryset_list = cur.fetchall()
        con.close()
        return queryset_list

    def filter_by(self, instance_id=None, user_id=None):
        filter_column = 'question_id' if instance_id else 'user_id'
        filter_value = instance_id if instance_id else user_id
        con = psycopg2.connect(**self.config)
        cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("select * from {} WHERE {}= '{}'".format(self.table, filter_column, filter_value))
        queryset_list = cur.fetchall()
        con.close()
        return queryset_list

    def update(self, question_id, answer_id, data=None):
        con = psycopg2.connect(**self.config)
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute(
                """
                UPDATE answers SET 
                body='""" + data.get('body') + """',
                accepted='""" + data.get('accepted') + """'
                WHERE 
                answer_id=""" + answer_id + """
                """
            )

            con.commit()
        except Exception as e:
            print(e)
            return None
        con.close()
        return data

    def delete(self, instance_id):
        pass


Table = ModelTable()



