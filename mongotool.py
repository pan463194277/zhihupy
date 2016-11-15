from pymongo import MongoClient

'''
    mongodb工具
    api : http://api.mongodb.com/python/current/
'''

class MongoManager:
    def __init__(self):
        self._client = MongoClient('172.16.1.55', 30000)
        self._db = self._client.pqh
        self._tbquestion = self._db.question
        #db.add_user('')
        #db.authenticate()



client = MongoManager()
client._tbquestion.insert ({"_id":1,'name':'name1'})