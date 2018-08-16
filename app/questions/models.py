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
from datetime import datetime
from config import BaseConfig
from ..utils import db_config


class ModelTable:
    def __init__(self):
        self.config = db_config(BaseConfig.SQLALCHEMY_DATABASE_URI)
        self.table = 'questions'

    def save(self, data):
        con = psycopg2.connect(**self.config)
        cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
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
            return None
        con.close()
        return data

    def query(self):
        con = psycopg2.connect(**self.config)
        cur = con.cursor(cursor_factory=psycopg2.extensions.cursor)
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

    def update(self, instance_id, data=None):
        pass

    def delete(self, instance_id):
        pass


Table = ModelTable()



