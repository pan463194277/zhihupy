'''
    Created by pqh on 2016/8/27.
     定义一些常量
'''

DEFAULT_HEADER = {
                'Host': 'www.zhihu.com',
                'X-Requested-With': 'XMLHttpRequest',
                'Referer': 'http://www.zhihu.com',
                'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2873.0 Safari/537.36',
                'Accept-Encoding': 'gzip, deflate, sdch, br'
                 }
MAIN_URL = 'https://www.zhihu.com'
LOGIN_URL = MAIN_URL + '/login/email'
CAPTCHA_URL = MAIN_URL + '/captcha.gif'


ROUNDTABLE_URL=MAIN_URL +'/roundtable'