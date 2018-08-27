
"""  Auth model """
import psycopg2
import psycopg2.extras
from psycopg2.extras import RealDictCursor
from flask_bcrypt import Bcrypt
from ..utils import db_config


class User:
    def __init__(self, data={}):
        self.config = db_config()
        self.table, self.email = 'users', data.get('email')
        self.username = data.get('username')
        self.user_id = data.get('user_id')
        self.b_crypt = Bcrypt()
        if data.get('password'):
            self.password = self.b_crypt.generate_password_hash(data.get('password')).decode('utf-8')

    def query(self):
        con = psycopg2.connect(**self.config)
        cur = con.cursor(cursor_factory=RealDictCursor)
        cur.execute("select username, email, user_id, created_at from {}".format(self.table))
        queryset_list = cur.fetchall()
        con.close()
        return [item for item in queryset_list]

    def filter_by(self):
        con, queryset_list = psycopg2.connect(**self.config), None
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute("select username, email, created_at from {} WHERE user_id='{}'".format(self.table, self.user_id))
            queryset_list = cur.fetchall()
        except Exception as e:
            print(e)
        con.close()
        return queryset_list

    def filter_by_email(self):
        con, queryset_list = psycopg2.connect(**self.config), None
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute("select * from {} WHERE email='{}'".format(self.table, self.email))
            queryset_list = cur.fetchall()
        except Exception as e:
            print(e)
        con.close()
        return queryset_list

    def update(self):
        """
        Update an user column
        :return: bool:
        """
        con, result = psycopg2.connect(**self.config), True
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            query = "UPDATE users SET email=%s, username=%s WHERE user_id=%s"
            cur.execute(query, (self.email, self.username, self.user_id))
            con.commit()
        except Exception as e:
            print(e)
            result = False
        con.close()
        return result

    def delete(self):
        con = psycopg2.connect(**self.config)
        cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
        try:
            query = "DELETE FROM users WHERE email=%s"
            cur.execute(query, self.email)
            con.commit()
            con.close()
        except Exception as e:
            print(e)
            con.close()
            return False
        return True

    def save(self):
        con, response = psycopg2.connect(**self.config), None
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            query = "INSERT INTO users (username, email, password) values(%s, %s, %s) RETURNING *"
            cur.execute(query, (self.username, self.email, self.password))
            con.commit()
            response = cur.fetchone()
        except Exception as e:
            print(e)
        con.close()
        return response
