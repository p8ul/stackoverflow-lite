from datetime import datetime


class Table:
    def __init__(self, data={}):
        self.title = data.get('title')
        self.body = data.get('body')
        self.answers = []

    def query(self):
        return {
            "title": self.title,
            "body": self.body,
            'answers': self.answers
        }
