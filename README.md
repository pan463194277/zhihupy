


zhihupy用于抓取知乎数据（主要为圆桌数据）

zhclient.py:
    知乎登录类api，第一次使用loginByAccount方法登录，之后可用loginByCookie进行登录
roundtable.py:
    圆桌专题类api,可获取圆桌专题信息
roundtableQuestion:
    问题类api，获取圆桌某专题的问题信息
roundtableQuestionAnswer:
    回答类api,获取某问题的回答信息
mongotool.py:
    Mongodb工具类
constant.py:
    常量信息
test.py:
    测试方法

环境为python3.5.2 ，依赖requests , beautifulSoup,pymongo模块

