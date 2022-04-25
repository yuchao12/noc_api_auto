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
from common import get_log
from common.yaml_util import yamlUtil
@pytest.fixture(scope='session')
def database():
    get_log.get_log().info('连接数据库')
    yield
    get_log.get_log().info('关闭数据库')

@pytest.fixture(scope='session',autouse=True)
def login():
    url = "https://noc-test.merckuwifi.com/api/users/actions/login"
    payload = {'username':'yuchao','password':'12345678'}
    response = requests.request("POST", url, data=payload)
    yamlUtil().write_extract_yml({'cookies': response.cookies.values()[0]})
    get_log.get_log().info('cookie值提取成功')

@pytest.fixture(scope='session')
def get_userid():
    url = "https://noc-test.merckuwifi.com/api/endusers"
    header = {'cookie': '_cookie=' + str(yamlUtil().read_extract_yml('cookies'))}
    payload={}
    response = requests.request("GET", url, data=payload,headers=header)
    yamlUtil().write_extract_yml({'user_id1': response.json()['items'][0]['id']})
    yamlUtil().write_extract_yml({'user_id2': response.json()['items'][1]['id']})
    get_log.get_log().info('userid提取成功')

@pytest.fixture(scope='session',autouse=True)
def clean_yaml():
    get_log.get_log().info('清空关联接口数据')
    yamlUtil().delete_extract_yml()

@pytest.fixture(scope='session',autouse=True)
def delet_log():
    try:
        os.remove('./Logger/logs/'+datetime.now().strftime('%Y-%m-%d')+ '-all'+ '.log')
        os.remove('./Logger/logs/'+datetime.now().strftime('%Y-%m-%d')+ '-error'+ '.log')
        os.remove('./测试报告文件.zip')
        get_log.get_log().info("清空日志文件")
    except(FileNotFoundError):
        get_log.get_log().info("没有日志文件，直接写入")


