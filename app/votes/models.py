"""
    Votes model
"""
import psycopg2
import psycopg2.extensions
from psycopg2.extras import RealDictCursor
from ..utils import db_config


class Vote:
    def __init__(self, data={}):
        self.config = db_config()
        self.table, self.answer_id = 'votes', data.get('answer_id')
        self.vote_value, self.user_id = data.get('vote'), data.get('user_id')

    def vote_exists(self):
        """
        Checks if vote for a particular answer
        is voted by current user
        :return: True if vote exist else False
        """
        con = psycopg2.connect(**self.config)
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            query = "SELECT user_id, vote_id FROM votes WHERE answer_id=%s AND user_id=%s"
            cur.execute(query, (self.answer_id, self.user_id))
            queryset_list = cur.fetchall()
            con.close()
            if len(queryset_list) < 1:
                return False
            return True
        except Exception as e:
            print(e)
            con.close()
            return False

    def create_vote(self):
        """
        Insert a vote in votes table
        :return: True if record values are inserted successfully else false
        """
        con = psycopg2.connect(**self.config)
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            query = "INSERT INTO votes(user_id, answer_id, vote) VALUES(%s, %s, %s)"
            cur.execute(query, (self.user_id, self.answer_id, self.vote_value))
            con.commit()
        except Exception as e:
            print(e)
            con.close()
            return False
        return True

    def update_vote(self):
        """
        Modify record from votes table
        :return:
        """
        if not self.answer_id:
            return False
        try:
            con = psycopg2.connect(**self.config)
            cur = con.cursor(cursor_factory=RealDictCursor)
            query = "UPDATE votes SET vote=%s WHERE answer_id=%s AND user_id=%s"
            cur.execute(query, (self.vote_value, self.answer_id, self.user_id))
            con.commit()
        except Exception as e:
            print(e)
            con.close()
            return False
        return True

    def vote(self):
        """
        Switch bus for updating or creating a vote
        :return: bool: True if transaction is
                       completed successfully else false
        """
        if self.vote_exists():
            return self.update_vote()
        return self.create_vote()

