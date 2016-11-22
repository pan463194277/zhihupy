from pymongo import MongoClient

'''
    mongodb工具
    api: http://api.mongodb.com/python/current/
    tutorial: http://api.mongodb.com/python/current/tutorial.html
'''

class MongoManager:
    def __init__(self):
        self._client = MongoClient('172.16.1.55', 30000)
        self._db = self._client.pqh#自动生成pqh数据库
        self._tbroundtable = self._db.roundtable #圆桌专题
        self._tbquestion = self._db.question #每个专题对应的问题
        self._tbanswer = self._db.answer  # 每个问题对应的回答
        #db.add_user('')
        #db.authenticate()
    def getRoundtable(self):
        return self._tbroundtable
    def getQuestionCollection(self):
        return self._tbquestion
    def getAnswerCollection(self):
        return self._tbanswer
    def saveOne (self, one, collection=None, instanceCheck =object):
        if collection is None:
            raise Exception("the document assigned is None ")
        if isinstance(one,dict):
            return collection.insert_one(one)
        elif isinstance(one,instanceCheck):
            return collection.insert_one(one.__dict__)
        else: raise TypeError(str(one) +" is not a supported type")

    def saveList(self, l, collection=None):
        if collection is None:
            raise Exception("the document assigned is "+str(collection))
        if type(l)==list:
            l2 = []
            for one in l :
                if not isinstance(one,object) :raise TypeError(str(one) +" is not a supported type")
                l2.append(one if isinstance(one,dict) else one.__dict__ )
            return collection.insert_many(l2)
        return None

#client = MongoManager()
#client._tbquestion.insert ({"_id":1,'name':'name1'})