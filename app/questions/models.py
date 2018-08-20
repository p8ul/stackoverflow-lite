from datetime import datetime


class Question:
    def __init__(self, data={}):
        self.title = data.get('title')
        self.body = data.get('body')

    def query(self):
        return {
            "title": self.title,
            "body": self.body
        }


class Answer(Question):

    def __init__(self, data={}):
        Question.__init__(self, data)
        self.answer = data.get('answer')
