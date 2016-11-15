
import zhclient
from constant import *
from bs4 import BeautifulSoup
import re
class RoundTableQuestion:
    def __init__(self ,belong,title,href):
        self._belong = belong  #所属圆桌专栏的名字
        self._title = title
        self._href = href
        return
    '''
        获取某一专栏的所有问题
    '''
    @staticmethod
    def getQuestionListByParent(parent): #parent = RoundTableListItem
        list =[]
        if parent._href is not None:
            client = zhclient.ClientInstance
            client.loginByCookie()
            offset = 0
            while (offset >=0):
                l,offset=RoundTableQuestion.getNextPage(parent,offset)
                list.extend(l)
        else : print (str(parent._guid) + ": href ==None")
        return list
    @staticmethod
    def getNextPage(parent,offset):
        list = []
        client = zhclient.ClientInstance
        params = {
            "offset":offset
        }
        url = ROUNDTABLE_QUESTION_NEXTURL.format(parent._engname)
        j = client.get(url,params).json()
        html = j["htmls"]  if "htmls" in j else []  # list<str>
        for item in html:
            a = BeautifulSoup(item,"html.parser").find("a",class_=re.compile("link|js-title-link"))
            if a is not None:
                list.append(RoundTableQuestion(belong =parent._engname,
                                           title =a.string,
                                           href =a["href"]))
        if 'paging' in j and 'next' in j['paging']:
            s = j['paging']['next']
            offset2 = int(s[s.find('offset=') + len('offset='):])  # 截取"/r/roundtables?offset=42"中的offset值
            # print(offset2)
        else : offset2 =-1
        print (offset)
        return list, offset2

'''
parent = RoundTableQuestion("1","2","3")
parent._href = ROUNDTABLE_QUESTION_NEXTURL.format("biz-school")+"?offset=0"
parent._guid =123
parent._engname="biz-school"
list =RoundTableQuestion.getQuestionListByParent(parent)
for i in list:
    print (i._title)

'''