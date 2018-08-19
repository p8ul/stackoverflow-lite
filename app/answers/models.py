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
from config import BaseConfig
from ..utils import db_config


class Table:
    def __init__(self, data={}):
        self.config = db_config(BaseConfig.DATABASE_URI)
        self.table = 'answers'
        self.answer_body = data.get('answer_body')
        self.question_id = data.get('question_id')
        self.answer_id = data.get('answer_id')
        self.accepted = data.get('accepted')
        self.user_id = data.get('user_id')

    def save(self):
        """
        Creates an answer record in answers table
        :return: None of inserted record
        """
        con, response = psycopg2.connect(**self.config), None
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            query = "INSERT INTO answers (user_id, answer_body, question_id) VALUES (%s, %s, %s) RETURNING *; "
            cur.execute(query, (self.user_id, self.answer_body, self.question_id))
            con.commit()
            response = cur.fetchone()
        except Exception as e:
            print(e)
        con.close()
        return response

    def query(self):
        """
        Fetch all records from a answers table
        :return: list: query set
        """
        con = psycopg2.connect(**self.config)
        cur = con.cursor(cursor_factory=RealDictCursor)
        cur.execute(
            """ SELECT *, ( SELECT  count(*) from votes 
                WHERE votes.answer_id=answers.answer_id AND vote=true ) as upVotes,
                ( SELECT count(*) from votes WHERE votes.answer_id=answers.answer_id
                AND vote=false ) as downVotes FROM  answers
            """
        )
        queryset_list = cur.fetchall()
        con.close()
        return queryset_list

    def filter_by(self):
        """
        Select a column(s) from answer table
        :return: list: queryset list
        """
        try:
            con = psycopg2.connect(**self.config)
            cur = con.cursor(cursor_factory=RealDictCursor)
            query = "SELECT * FROM answers WHERE answer_id=%s"
            cur.execute(query, self.answer_id)
            queryset_list = cur.fetchall()
            con.close()
            return queryset_list
        except:
            return []

    def question_author(self):
        con = psycopg2.connect(**self.config)
        try:
            cur = con.cursor(cursor_factory=RealDictCursor)
            query = "SELECT user_id FROM questions WHERE question_id=%s"
            cur.execute(query, self.question_id)
            return cur.fetchall()

        except Exception as e:
            print(e)
        con.close()
        return False

    def answer_author(self):
        try:
            con = psycopg2.connect(**self.config)
            cur = con.cursor(cursor_factory=RealDictCursor)
            query = "SELECT user_id FROM answers WHERE answer_id=%s"
            cur.execute(query, self.answer_id)
            queryset_list = cur.fetchall()
            con.close()
            return queryset_list
        except Exception as e:
            return False

    def update(self):
        try:
            answer_author = self.answer_author()[0].get('user_id')
            question_author = self.question_author()[0].get('user_id')
            # current user is the answer author
            if answer_author == self.user_id:
                # update answer
                response = 200 if self.update_answer() else 304
                return response

            # current user is question author
            elif question_author == self.user_id:
                # mark it as accepted
                response = self.update_accept_field()
                response = 200 if response else 304
                return response

            # other users
            else:
                return 203
        except:
            return 404

    def update_accept_field(self):
        """
        Update an answer column
        :return: bool:
        """
        con, result = psycopg2.connect(**self.config), True
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            query = "UPDATE answers SET accepted=%s WHERE answer_id=%s AND question_id=%s"
            cur.execute(query, (self.accepted, self.answer_id, self.question_id))
            con.commit()
        except Exception as e:
            print(e)
            result = False
        con.close()
        return result

    def update_answer(self):
        """
        Update an answer column
        :return: bool:
        """
        con = psycopg2.connect(**self.config)
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            query = "UPDATE answers SET answer_body=%s WHERE answer_id=%s"
            cur.execute(query, (self.answer_body, self.answer_id))
            con.commit()
        except Exception as e:
            print(e)
            con.close()
            return False
        con.close()
        return True

    def delete(self):
        pass



