#-*- coding:utf-8 -*-
import requests
import urllib.request
import os
import time

#被注释掉的部分为检测wifi部分，如果是有线连接的话则不需要这部分代码

while 1:
    #i = os.popen('netsh').read()   #此处为windows获取wifi名称的方法
    #if 'i-HDU' in i or 'i_HDU' in i:
        i = os.system('ping www.baidu.com')
        print(i)
        if i == 0:
            print("have connected")
        else:
            url = 'http://2.2.2.2/ac_portal/20170407143720/pc.html'
            s = requests.session()
            r = s.get(url)
            r.encoding = r.apparent_encoding
            text = r.text

            postDict = {
                'opr':'pwdLogin',
                'userName': 'studentID',
                'pwd':'passwd',
                'rememberPwd':'0',
            }
            r = s.post('http://2.2.2.2/ac_portal/login.php',postDict)
            print("succeed")
            time.sleep(1)
    #else:
        #print("NO_iHDU")

