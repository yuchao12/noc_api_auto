#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2021年5月22日
@author: yuchao
'''
from time import sleep
import pytest
from common.set_report import set_windos_title, get_json_data, write_json_data
from Email.send_email import *

if __name__ == '__main__':
    pytest.main()
    os.system('allure generate ./temp -o ./report  --clean')
    # 自定义测试报告标题
    set_windos_title(" NOC 接口自动化测试报告")
    report_title = get_json_data(" NOC 接口自动化测试报告")
    write_json_data(report_title)
    #send().make_zip('./report','测试报告文件.zip')
    #send().send_emial()
#sssssssssssss

