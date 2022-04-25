#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2021年5月23日
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

@allure.feature('设备数量统计模块')
@pytest.mark.count
#@pytest.mark.run(order=5)
@pytest.mark.parametrize('caseinfo',yamlUtil().read_testcase_yml('test_2_station_count.yml'))
class Test_station_count():
    def test_station_count(self,caseinfo):
        get_log().info('设备数量统计模块')
        name=caseinfo['name']
        method = caseinfo['request']['method']
        url = caseinfo['request']['url']
        if caseinfo['header'] is None:
            caseinfo['header'] = yamlUtil().read_extract_yml('cookies')
        header={'cookie': '_cookie='+caseinfo['header']}
        if caseinfo['request']['data']['t'] is None:
            caseinfo['request']['data']['t'] = str(int(time.time()))
        data = caseinfo['request']['data']
        rep = RequestsUtil().send_request(method,url,data,headers=header)
        status_code=rep.status_code
        expect = caseinfo['assert']
        actual = rep.json()
        ConsoleFmt().all_console_fmt(name=name,url=url,cookie=header,
        method=method, data=data, response=rep.json(),status_code=status_code)
        ResponseAssert().assert_in(expect,actual)




