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

@allure.feature('查询设备详细信息模块')
@pytest.mark.station_info
@pytest.mark.run(order=3)
@pytest.mark.usefixtures('login')
@pytest.mark.parametrize('caseinfo',yamlUtil().read_testcase_yml('test_3_station_info.yml'))
class Test_station_info():
    def test_station_info(self,caseinfo):
        get_log().info('查询设备详细信息模块')
        name=caseinfo['name']
        print(name)
        # method = caseinfo['request']['method']
        # url = str(caseinfo['request']['url'])+str(caseinfo['request']['station'])
        # print(url)
        # if caseinfo['header'] is None:
        #     caseinfo['header'] = yamlUtil().read_extract_yml('cookies')
        # header={'cookie': '_cookie='+caseinfo['header']}
        # if caseinfo['request']['data']['t'] is None:
        #     caseinfo['request']['data']['t'] = str(int(time.time()))
        # data = caseinfo['request']['data']
        # rep = RequestsUtil().send_request(method,url,data,headers=header)
        # status_code=rep.status_code
        # print(rep.json())
        # if 'Unauthorized' in str(rep.json()):
        #     actual = rep.json()['detail']
        #     expect = caseinfo['assert']['T']
        # else:
        #     actual = rep.json()
        #     expect = caseinfo['assert']['F']
        # ConsoleFmt().all_console_fmt(name=name,url=url,
        # method=method, data=data, response=rep.json(),status_code=status_code)
        # get_log().info('cookie值为 {}'.format(caseinfo['header']))
        # ResponseAssert().assert_in(expect,actual)

