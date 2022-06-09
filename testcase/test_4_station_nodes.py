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

@allure.feature('接入设备详情模块')
#@pytest.mark.flaky(reruns=3, reruns_delay=2)
@pytest.mark.station_nodes
@pytest.mark.run(order=2)
@pytest.mark.parametrize('caseinfo',yamlUtil().read_testcase_yml('test_4_station_nodes.yml'))
class Test_station_info():
    def test_station_info(self,caseinfo):
        get_log().info('接入设备详情模块')
        name=caseinfo['name']
        method = caseinfo['request']['method']
        if caseinfo['request']['station'] is None:
            url = caseinfo['request']['url']+'nodes'
        else:
            url = caseinfo['request']['url']+caseinfo['request']['station']+'/nodes'
        if caseinfo['header'] is None:
            caseinfo['header'] = yamlUtil().read_extract_yml('cookies')
        header = {'cookie': '_cookie=' + caseinfo['header']}
        if caseinfo['request']['data']['t'] is None:
             caseinfo['request']['data']['t'] = str(int(time.time()))
        data = caseinfo['request']['data']
        rep = RequestsUtil().send_request(method,url,data,headers=header)
        status_code=rep.status_code
        try:
            if caseinfo['assert']['sn'] is None:
                caseinfo['assert']['sn']=caseinfo['request']['station']
        except:
            pass
        expect= caseinfo['assert']
        actual = rep.json()
        ConsoleFmt().all_console_fmt(name=name,url=url,method=method, data=data,
        response=rep.json(),status_code=status_code,cookie=header)
        ResponseAssert().assert_in(expect,actual)