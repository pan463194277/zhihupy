'''
    Created by pqh on 2016/8/27.
'''


from zhclient import ZHclient

client = ZHclient()
client.loginByCookie()
resp = client._session.get('http://www.zhihu.com/roundtable')
with open ('res.txt','wb') as f :
    f.write(resp.content)