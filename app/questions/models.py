"""
    Question Model
"""
import psycopg2
import psycopg2.extensions
from psycopg2.extras import RealDictCursor
from ..utils import db_config


class Question:
    def __init__(self, data={}):
        self.config = db_config()
        self.table, self.title = 'questions', data.get('title')
        self.body, self.q = data.get('body'), data.get('q')
        self.question_id = data.get('question_id')
        self.user_id = data.get('user_id')

    def save(self):
        """ Create a question record in questions table
        :return: None or record values
        """
        con = psycopg2.connect(**self.config)
        cur, response = con.cursor(cursor_factory=RealDictCursor), None
        try:
            query = "INSERT INTO questions (title, body, user_id) VALUES (%s, %s, %s) RETURNING *"
            cur.execute(query, (self.title, self.body, self.user_id))
            con.commit()
            response = cur.fetchone()
        except Exception as e:
            print(e)
        con.close()
        return response

    def query(self):
        """Query the data in question table :return: list: query set list"""
        con, queryset_list = psycopg2.connect(**self.config), None
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            if not self.q:
                cur.execute(
                    " SELECT *,( SELECT count(*) FROM "
                    "answers WHERE answers.question_id=questions.question_id ) as "
                    "answers_count FROM questions "
                    " ORDER BY questions.created_at DESC"
                )
            else:
                query = "SELECT *, ( SELECT count(*) FROM answers WHERE "
                query += " answers.question_id=questions.question_id ) as answers_count "
                query += " FROM questions WHERE  body LIKE %s OR title LIKE %s  "
                query += " ORDER BY questions.created_at"
                cur.execute(query, (self.q, self.q))
            queryset_list = cur.fetchall()
        except Exception as e:
            print(e)
        con.close()
        return queryset_list

    def filter_by(self):
        """
        Selects a question by id
        :return: False if record is not found else query list of found record
        """
        con, queryset_list = psycopg2.connect(**self.config), None
        cur = con.cursor(cursor_factory=RealDictCursor)
        cur2 = con.cursor(cursor_factory=RealDictCursor)

        try:
            query = """ SELECT * FROM questions WHERE questions.question_id=%s ORDER BY questions.created_at"""
            cur.execute(query % self.question_id)
            questions_queryset_list = cur.fetchall()
            cur2.execute("SELECT * FROM answers WHERE answers.question_id=%s" % self.question_id)
            answers_queryset_list = cur2.fetchall()
            queryset_list = {
                'question': questions_queryset_list,
                'answers': answers_queryset_list
            }
        except Exception as e:
            print(e)
        con.close()
        return queryset_list

    def filter_by_user(self):
        """
        Selects question for specific user:default filters by current logged in user
        :return: False if record is not found else query list of found record
        """
        con, queryset_list = psycopg2.connect(**self.config), None
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute(
                """ SELECT * FROM questions 
                    WHERE questions.user_id=""" + self.user_id + """ ORDER BY questions.created_at """
            )
            questions_queryset_list = cur.fetchall()
            queryset_list = {'question': questions_queryset_list}
        except Exception as e:
            print(e)
        con.close()
        return queryset_list

    def update(self):
        """
        Update an question column
        :return: bool:
        """
        con, result = psycopg2.connect(**self.config), True
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            query = "UPDATE questions SET title=%s, body=%s WHERE question_id=%s"
            cur.execute(query, (self.title, self.body, self.question_id))
            con.commit()
        except Exception as e:
            print(e)
            result = False
        con.close()
        return result

    def record_exists(self):
        """
        checks whether a question was asked by the user
        :return: bool: False if record is not found else True
        """
        con, exists = psycopg2.connect(**self.config), False
        cur, queryset_list = con.cursor(cursor_factory=RealDictCursor), None
        try:
            query = "SELECT question_id, user_id FROM questions WHERE question_id=%s AND user_id=%s"
            cur.execute(query, (self.question_id, self.user_id))
            queryset_list = cur.fetchall()
            con.close()
            exists = True if len(queryset_list) >= 1 else False
        except Exception as e:
            print(e)
        return exists

    def delete(self):
        """ Delete a table records
        :return: bool
        """
        con = psycopg2.connect(**self.config)
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            exist = self.filter_by()['question']
            if not len(exist) > 0:
                return 404
            if not self.record_exists():
                return 401
            cur.execute("DELETE from {} WHERE {}= '{}'".format(self.table, 'question_id', self.question_id))
            con.commit()
        except Exception as e:
            print(e)
            con.close()
            return False
        con.close()
        return True
