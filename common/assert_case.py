#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2021年5月22日
@author: yuchao
'''

from common.get_log import get_log
class ResponseAssert:
    def assert_equ(self,excepct,actual):
        if str(excepct) == str(actual):
            get_log().info(f"断言检查点：预期响应结果 {excepct}")
            get_log().info(f"断言检查点：实际结果响应结果 {actual}")
            get_log().info("测试结果：预期结果和实际结果相同，测试用例通过")
            assert True
        else:
            get_log().error(f"断言检查点：预期响应结果 {excepct}")
            get_log().error(f"断言检查点：实际结果响应结果 {actual}")
            get_log().error("测试结果：预期结果和实际结果不同，测试用例失败")
            assert False

    def assert_in(self,excepct,actual):
        if '{' in str(excepct):
            if  (str(excepct).split('{')[1].split('}')[0]) in str(actual):
                get_log().info(f"断言检查点：预期响应结果 {excepct}")
                get_log().info(f"断言检查点：实际结果响应结果 {actual}")
                get_log().info("测试结果：预期结果包含在实际结果内，测试用例通过")
                assert True
            else:
                get_log().error(f"断言检查点：预期响应结果 {excepct}")
                get_log().error(f"断言检查点：实际结果响应结果 {actual}")
                get_log().error("测试结果：实际结果不包含在预期结果内，测试用例失败")
                assert False
        else:
            if str(excepct) in str(actual):
                get_log().info(f"断言检查点：预期响应结果 {excepct}")
                get_log().info(f"断言检查点：实际结果响应结果 {actual}")
                get_log().info("测试结果：预期结果包含在实际结果内，测试用例通过")
                assert True
            else:
                get_log().error(f"断言检查点：预期响应结果 {excepct}")
                get_log().error(f"断言检查点：实际结果响应结果 {actual}")
                get_log().error("测试结果：实际结果不包含在预期结果内，测试用例失败")
                assert False

    def assert_not_in(self,excepct,actual):
        if '{' in str(excepct):
            if  (str(excepct).split('{')[1].split('}')[0]) not in str(actual):
                get_log().info(f"断言检查点：预期响应结果 {excepct}")
                get_log().info(f"断言检查点：实际结果响应结果 {actual}")
                get_log().info("测试结果：实际结果不包含预期结果，测试用例通过")
                assert True
            else:
                get_log().error(f"断言检查点：预期响应结果 {excepct}")
                get_log().error(f"断言检查点：实际结果响应结果 {actual}")
                get_log().error("测试结果：实际结果包含预期结果，测试用例失败")
                assert False
        else:
            if str(excepct) not in  str(actual):
                get_log().info(f"断言检查点：预期响应结果 {excepct}")
                get_log().info(f"断言检查点：实际结果响应结果 {actual}")
                get_log().info("测试结果：实际结果不包含预期结果，测试用例通过")
                assert True
            else:
                get_log().error(f"断言检查点：预期响应结果 {excepct}")
                get_log().error(f"断言检查点：实际结果响应结果 {actual}")
                get_log().error("测试结果：实际结果包含预期结果，测试用例失败")
                assert False