#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2021年5月22日
@author: yuchao
'''

import json
title_filepath = r"C:\Project\noc_api_auto\report\widgets\summary.json"
# 获取 summary.json 文件的数据内容
def get_json_data(name):
    # 定义为只读模型，并定义名称为f
    with open(title_filepath, 'rb') as f:
        # 加载json文件中的内容给params
        params = json.load(f)
        # 修改内容
        params['reportName'] = name
        # 将修改后的内容保存在dict中
        dict = params
    # 关闭json读模式
    f.close()
    # 返回dict字典内容
    return dict

# 写入json文件
def write_json_data(dict):
    # 定义为写模式，名称定义为r
    with open(title_filepath, 'w', encoding="utf-8") as r:
        # 将dict写入名称为r的文件中
        json.dump(dict, r, ensure_ascii=False, indent=4)
    # 关闭json写模式
    r.close()
# 设置报告窗口的标题

def set_windos_title(new_title):
    """  设置打开的 Allure 报告的浏览器窗口标题文案
    @param new_title:  需要更改的标题文案 【 原文案为：Allure Report 】
    @return: 没有返回内容，调用此方法传入需要更改的文案即可修改窗体标题温拿
    """
    # report_title_filepath：这里主要是去拿到你的HTML测试报告的绝对路径【记得换成你自己的】
    report_title_filepath = r"C:\Project\noc_api_auto\report\index.html"
    # 定义为只读模型，并定义名称为: f
    with open(report_title_filepath, 'r+',encoding="utf-8") as f:
        # 读取当前文件的所有内容
        all_the_lines = f.readlines()
        f.seek(0)
        f.truncate()
        # 循环遍历每一行的内容，将 "Allure Report" 全部替换为 → new_title(新文案)
        for line in all_the_lines:
            f.write(line.replace("Allure Report", new_title))
        # 关闭文件
        f.close()



