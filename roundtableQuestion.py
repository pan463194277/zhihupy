'''
    Created by pqh on 2016/8/28.

    客户端类，用于登录
'''
import zhclient
from constant import *
from bs4 import BeautifulSoup
import re
from time import sleep

'''
    圆桌专题下的questionAPI
    用beautifulSoup代替re,在操作上有一定的简化
'''
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
                sleep(0.5)
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
        print(url)
        j =None
        try:
            resp = client.get(url,params)
            j = resp.json()
        except Exception as e:
            print('[error]:{0} , data= {1}'.format(e,resp.content))
            raise
        html = j["htmls"]  if "htmls" in j else []  # list<str>
        for item in html:
            a = BeautifulSoup(item,"html.parser").find("a",class_=re.compile("link|js-title-link"))
            if a is not None:
                list.append(RoundTableQuestion(belong =parent._engname,
                                           title =a.string,#string为标签内的字符串内容
                                           href =a["href"]))
                #print(a.string)
        if 'paging' in j and 'next' in j['paging']:
            s = j['paging']['next']
            offset2 = int(s[s.find('offset=') + len('offset='):])  # 截取"/r/roundtables?offset=42"中的offset值
            # print(offset2)
        else : offset2 =-1
        #print (offset)
        return list, offset2

