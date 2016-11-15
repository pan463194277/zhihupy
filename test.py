'''
    Created by pqh on 2016/8/27.
'''


from roundtable import RoundTable
from roundtableQuestion import RoundTableQuestion
import json


r= RoundTable ()
r.loadRoundTableList()
f = open("result.txt",'w')
for i in r._list:
    list =  RoundTableQuestion.getQuestionListByParent(i)
    json.dump(json.dumps(i.__dict__),f)
    f.write("----------------------------\n")
    for j in list :
        json.dump(json.dumps(j.__dict__), f)
    f.write("\n\n\n")
    #print (i._name ,i._href)


#list ,offset = r.getNextJsonPage (126)
#print (list )
#print (offset)
