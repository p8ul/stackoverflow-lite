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
from flask import session
from flask import session
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

    def update(self, question_id, answer_id, data=None):
        """
        Update an answer column
        :param question_id: string: question id
        :param answer_id: string: answer id
        :param data: dict: updated values
        :return: dict: if column updated else None
        """
        con = psycopg2.connect(**self.config)
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute(
                """
                UPDATE answers SET 
                    answer_body='""" + data.get('body') + """',
                    accepted='""" + data.get('accepted') + """'
                WHERE 
                    answer_id=""" + answer_id + """
                AND question_id=""" + question_id + """
                """
            )

            con.commit()
        except Exception as e:
            print(e)
            return None
        con.close()
        return data

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
            """
            SELECT 
                user_id, vote_id
            FROM
                votes               
            WHERE 
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


Table = ModelTable()



