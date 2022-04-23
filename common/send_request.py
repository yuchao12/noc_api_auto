#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2021年5月22日
@author: yuchao
'''

import json
import requests

class RequestsUtil:
    session = requests.session()
    def send_request(self,method,url,data,**kwargs):
        method = str(method).lower()
        # rep = None
        # #全部转换成小写
        # if method == 'get':
        #     rep = RequestsUtil.session.request(method, url=url, params=data,**kwargs)
        # else:
        #     #data = json.dumps(data)
        #     #全部转换成json
        rep = RequestsUtil.session.request(method, url=url, data=data,**kwargs)
        return rep

