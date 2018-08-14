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
from datetime import datetime


class Table:
    def __init__(self):
        self.data = [
            {
                'id': 1,
                'title': 'Test data',
                'body': 'qwertyu asdfg asdfg',
                'user': 'p4ul',
                'email': 'pkinuthia10@gmail.com',
                'created_at': self.now(),
                'tags': ['Rust', 'Python'],
                'answers': [
                    {
                        'answer': 'Sample Answer',
                        'user': 'P8ul',
                        'created_at': self.now(),
                    },
                ]
            }
        ]

    def query(self):
        return self.data

    def filter_by(self, instance_id):
        # filter by instance by id
        item_ = next((item for item in self.data if item.get('id') == int(instance_id)), {})
        return item_

    def update(self, instance_id, data=None):
        item = self.filter_by(instance_id)
        if item:
            # remove found instance
            self.delete(instance_id)
        else:
            return None
        item['title'] = data.get('title') if data.get('title') else item.get('title')
        item['body'] = data.get('body') if data.get('body') else item.get('body')
        self.data.append(item)
        return item

    def delete(self, instance_id):
        for i in range(len(self.data)):
            if self.data[i].get('id') == int(instance_id):
                self.data.pop(i)
                instance_id = None
                break
        if not instance_id:
            return True
        return False

    def answer(self, instance_id=None, answer=None):
        if instance_id and answer:
            for i in range(len(self.data)):
                if self.data[i].get('id') == int(instance_id):
                    answer = {
                        'answer': answer,
                        'created_at': self.now()
                    }
                    self.data[i]['answers'].append(answer)
                    break
        try:
            if not answer.get('created_at'):
                return None
        except Exception as e:
            # log e
            print(e)
            return None
        return answer

    def save(self, data):
        new_entry = dict()
        new_entry['title'] = str(data.get('title'))
        new_entry['body'] = str(data.get('body'))
        new_entry['user'] = str(data.get('user'))
        new_entry['answers'] = []
        new_entry['created_at'] = self.now()

        """ Ensure table id column value is unique """
        try:
            new_entry['id'] = int(self.data[-1].get('id')) + 1
        except Exception as e:
            new_entry['id'] = 1
            print(e)
        self.data.append(new_entry)
        return new_entry

    def now(self):
        return datetime.now().isoformat()



