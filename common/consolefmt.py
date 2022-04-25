#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2021年5月22日
@author: yuchao
'''

from common.get_log import get_log
class ConsoleFmt:
    def all_console_fmt(self, name=None, url=None, method=None, data=None,response=None,
                        status_code=None,cookie=None):
        get_log().info(f"【开始执行测试用例：{name}】")
        get_log().info(f"请求url：{url}")
        get_log().info(f"请求方法：{method}")
        get_log().info(f"请求参数：{data}")
        get_log().info(f"请求cookie值：{cookie}")
        get_log().info(f"响应结果：{response}")
        get_log().info(f"响应状态码：{status_code}")


