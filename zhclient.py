'''
    Created by pqh on 2016/8/27.

    客户端类，用于登录
'''

import requests
import os
import json
import time
import pickle
from urllib.parse import urlencode
from constant import *




class ZHclient:

    def __init__(self):
        self._session = requests.Session()
        self._session.headers.update(DEFAULT_HEADER)
    '''根据用户名密码登录'''
    def loginByAccount (self ,email,password):

        with open ('captcha.gif','wb') as f:
            captchaFile = self.getCaptcha()
            f.write(captchaFile)
        captcha = input('please input the validation code \n')
        self.login (email,password,captcha)

    '''获取验证码信息'''
    def getCaptcha(self):
        params = {
            'r': str(int(time.time() * 1000)),
            'type': 'login',
        }
        resp = self._session.get(CAPTCHA_URL+"?"+urlencode(params))  # ,"r":1
        return  resp.content

    def login(self, email, password, captcha ,remember_me= True ,saveCookies=True ,cookieFilename="cookies.json"):
        data = {"email": email, "password": password, "captcha": captcha, "remember_me":remember_me}
        resp = self._session.post(LOGIN_URL,data)
        j = resp.json()
        '''为0时表示登录成功'''
        if int(j['r']) !=0:
            print("login error : "+j['msg']+"\n")
            return
        else:
            print(j['msg'])
        if saveCookies ==True:
           with open(cookieFilename,'w') as f:
               cookie_dict = requests.utils.dict_from_cookiejar(resp.cookies)
               cookies_str = json.dumps(cookie_dict)
               f.write(cookies_str)

        #print (j['r'])
        return

    '''
        根据cookie登录
        @:cookie 表示文件名'''

    def loginByCookie(self, cookieFile='cookies.json'):
        if cookieFile is not None:
            if os.path.isfile(cookieFile):
                with open(cookieFile, 'r', -1, 'utf-8') as f:
                    cookies = f.read()
            cookies_dict = json.loads(cookies)
            self._session.cookies.update(cookies_dict)



