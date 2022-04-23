#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2021年5月23日
@author: yuchao
'''

import allure
import pytest
from common.assert_case import ResponseAssert
from common.consolefmt import ConsoleFmt
from common.get_log import get_log
from common.send_request import RequestsUtil
from common.yaml_util import yamlUtil


@allure.feature('登录模块')
@pytest.mark.login
@pytest.mark.run(order=1)
@pytest.mark.parametrize('caseinfo', yamlUtil().read_testcase_yml('test_1_login.yml'))
# 自行选择是否显示用例标题
# @allure.title(yamlUtil().read_testcase_yml('test_1_login.yml')[0]['name'])
class Test_login():
    def test_login(self,caseinfo):
        get_log().info('登录模块')
        #可以自行选择是否写步骤
        #with allure.step('输入登录用户名和密码'):
        name=caseinfo['name']
        method = caseinfo['request']['method']
        url = caseinfo['request']['url']
        data = caseinfo['request']['data']
        rep = RequestsUtil().send_request(method,url,data)
        status_code=rep.status_code
        expect = caseinfo['assert']
        if 'error' in rep.json():
            actual = rep.json()['error'] #可以选择直接使用返回的json做对比
        else:
            actual = rep.json()['role']
        ConsoleFmt().all_console_fmt(name=name,url=url,
        method=method, data=data, response=rep.json(),status_code=status_code)
        ResponseAssert().assert_in(expect,actual)








