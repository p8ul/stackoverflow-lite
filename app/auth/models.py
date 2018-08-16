# Custom Model

# Author: P8ul
# https://github.com/p8ul

"""
    This class will act as a table in a Database (Inspired by MongoDB)
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

        filter_by(email, user_id)
            :param user_id :int Id of instance to be edited
            Filters class data by id

"""
import psycopg2
import psycopg2.extras
from config import BaseConfig
from ..utils import db_config


class ModelTable:
    def __init__(self):
        self.config = db_config(BaseConfig.SQLALCHEMY_DATABASE_URI)
        self.table = 'users'

    def query(self):
        con = psycopg2.connect(**self.config)
        cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("select * from {}".format(self.table))
        queryset_list = cur.fetchall()
        con.close()
        return [item for item in queryset_list]

    def filter_by(self, email=None, user_id=None):
        # filter user by email or id
        filter_column = 'user_id' if user_id else 'email'
        filter_value = user_id if user_id else email
        con = psycopg2.connect(**self.config)
        cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("select * from {} WHERE {}='{}'".format(self.table, filter_column, filter_value))
        queryset_list = cur.fetchall()
        con.close()
        return queryset_list

    def update(self, instance_id, data=None):
        pass

    def delete(self, instance_id):
        pass

    def save(self, data):
        con = psycopg2.connect(**self.config)
        cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cur.execute(
            """
            INSERT INTO users (username, email, password)
            values(
                '""" + data.get('username') + """',
                '""" + data.get('email') + """',
                '""" + data.get('password') + """'
            )
            """
        )
        con.commit()
        con.close()
        return data


Table = ModelTable()
