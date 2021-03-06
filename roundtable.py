'''
    Created by pqh on 2016/8/28.

    知乎圆桌API，拉取圆桌数据
    用正则匹配有点繁琐，其他页面会用html工具进行解析
'''
import re
import zhclient
from constant import *
import uuid
from bs4 import BeautifulSoup
class RoundTable:
        def __init__(self):
            '''初始化、登录'''
            self._list = []
            self._client = zhclient.ClientInstance
            self._client.loginByCookie()

        def getRoundTableHtml(self):
            resp = self._client._session.get(ROUNDTABLE_URL)
            return resp.content.decode()

        def loadRoundTableList(self):
            firstHtml = self.getRoundTableHtml()
            self.getFirst(firstHtml)
            self.getNexts()

            #print(self._list)

        '''获取第一页html'''
        def getFirst(self ,html):
            all = re.findall("<div\\sclass=\"content\".*?href=\"/round.*?\".*?div>", html)
            for i in all:
                groups = re.search("href=\"(.*?)\".*?"
                                   "img src=\"(.*?)\".*?"
                                   "<span class=\"name\">(.*?)</span>.*?"
                                   "浏览\s(.*?)\s次", i)
                href = groups.group(1)
                img = groups.group(2)
                name = groups.group(3)
                visit = groups.group(4)
                #print(href, name, img, visit)
                self._list.append(RoundTableListItem(name,href,img,visit))

            return
        '''获取后续页面，以json格式返回'''
        def getNexts (self):
            offset = len(self._list)
            while offset !=-1 :
                list ,offset = self.getNextJsonPage(offset)
                self._list.extend(list)
            #print ("exit when list.length =" +str(len(self._list)))
            return
        '''获取后续加载的item ，格式为json
            = =当写到offset =0时突然想到getFirst是根本不用写的 ，测试了一下果然offset=0完全可以以更方便的方式获取第一页数据
        '''
        def getNextJsonPage (self ,offset = 0):
            list =[]
            param = {
                "offset": offset
            }
            offset2 =-1
            j = self._client.get(ROUNDTABLE_NEXTURL,param).json()

            html =j["htmls"]  if "htmls" in j else [] #list<str>
            for item in html :
                groups = re.search("href=\"(.*?)\".*?"
                                   "img\ssrc=\"(.*?)\".*?"
                                   "<span\sclass=\"name\">(.*?)</span>.*?"
                                   "浏览\s(.*?)\s次",item)
                if groups is None :
                    print ("error parsing jsonPage: " +item)
                href = groups.group(1)
                img = groups.group(2)
                name = groups.group(3)
                visit =groups.group(4)
                list.append(RoundTableListItem(name,href,img,visit))
            if 'paging' in j  and 'next' in j['paging']:
                s = j['paging']['next']
                offset2 = int(s[s.find('offset=')+len('offset='):]) #截取"/r/roundtables?offset=42"中的offset值
                #print(offset2)

            return list ,offset2



class RoundTableListItem:
    def __init__(self,name,href,img ,visit ,intro =None):
        #self._guid = uuid.uuid1()
        self._name = name
        # 例：/roundtable/online-education ,取online-education, Question类的访问地址需要用到这个参数,也可以把它作为唯一性标识去建立索引
        self._engname =href[len("/roundtable/"):]
        self._href = href
        self._img = img
        self._visit=visit
        self._intro = intro





