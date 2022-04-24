#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2021年5月22日
@author: yuchao
'''

import os
from datetime import datetime
import pytest
import requests
from common.yaml_util import yamlUtil
@pytest.fixture(scope='session')
def database():
    print('连接数据库')
    yield
    print('关闭数据库')

@pytest.fixture(scope='session')
def login():
    url = "https://noc-test.merckuwifi.com/api/users/actions/login"
    payload = {'username':'yuchao','password':'12345678'}
    response = requests.request("POST", url, data=payload)
    yamlUtil().write_extract_yml({'cookies': response.cookies.values()[0]})
    print('cookie值提取成功')

@pytest.fixture(scope='session',autouse=True)
def clean_yaml():
    print('清空关联接口数据')
    yamlUtil().delete_extract_yml()

@pytest.fixture(scope='session',autouse=True)
def delet_log():
    try:
        os.remove('./Logger/logs/'+datetime.now().strftime('%Y-%m-%d')+ '-all'+ '.log')
        os.remove('./Logger/logs/'+datetime.now().strftime('%Y-%m-%d')+ '-error'+ '.log')
        os.remove('./测试报告文件.zip')
        print("清空日志文件")
    except(FileNotFoundError):
        print("没有日志文件，直接写入")


