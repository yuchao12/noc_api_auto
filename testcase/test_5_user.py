#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2021年5月24日
@author: yuchao
'''

import allure
import pytest
import time
from common.assert_case import ResponseAssert
from common.consolefmt import ConsoleFmt
from common.get_log import get_log
from common.send_request import RequestsUtil
from common.yaml_util import yamlUtil

@allure.feature('接入设备详情模块')
#@pytest.mark.skip(reason="由于某种原因这个测试用例暂时不执行")
@pytest.mark.user_info
@pytest.mark.run(order=5)
@pytest.mark.parametrize('caseinfo',yamlUtil().read_testcase_yml('test_5_user.yml'))
class Test_station_info():
    def test_station_info(self,caseinfo):
        time.sleep(2)
        get_log().info('接入设备详情模块')
        name=caseinfo['name']
        method = caseinfo['request']['method']
        url = caseinfo['request']['url']
        if caseinfo['header'] is None:
            caseinfo['header'] = yamlUtil().read_extract_yml('cookies')
        header = {'cookie': '_cookie=' + caseinfo['header']}
        if caseinfo['request']['data']['t'] is None:
             caseinfo['request']['data']['t'] = str(int(time.time()))
        data = caseinfo['request']['data']
        rep = RequestsUtil().send_request(method,url,data,headers=header)
        status_code=rep.status_code
        if 'total' in str(rep.json()):
            actual = rep.json()
            expect = caseinfo['assert']['T']
        else:
            actual = rep.json()
            expect = caseinfo['assert']['F']
        ConsoleFmt().all_console_fmt(name=name,url=url,method=method, data=data,
        response=rep.json(),status_code=status_code,cookie=header)
        ResponseAssert().assert_in(expect,actual)

