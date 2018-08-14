### Custom Model

# Author: P8ul Kinuthia
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

        filter_by(instance_id)
            :param instance_id :int Id of instance to be edited
            Filters class data by id

        update(instance_id, title)
            :param instance_id: :int Id of instance to be edited
            :param title: :string New title used to replace original title
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
                'username': 'p4ul',
                'email': 'pkinuthia10@gmail.com',
                'password': 'sds3@#SDF#SFSDF##@',
                'created_at': self.now(),
                'badges': ['Teacher', 'Reviewer'],
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
        item['username'] = data.get('username') if data.get('username') else item.get('username')
        item['email'] = data.get('email') if data.get('email') else item.get('email')
        item['password'] = data.get('password') if data.get('password') else item.get('password')
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

    def save(self, data):
        new_entry = dict()
        new_entry['email'] = str(data.get('email'))
        new_entry['username'] = str(data.get('username'))
        new_entry['password'] = str(data.get('password'))
        new_entry['badges'] = []
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



