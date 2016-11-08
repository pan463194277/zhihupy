
from client import ZhihuClient




#ZhihuClient().create_cookies('cookies.json',True)

client = ZhihuClient('cookies.json')

resp = client._session.get('https://www.zhihu.com')

with open('1.html', 'wb') as f:
    f.write(resp.content)
