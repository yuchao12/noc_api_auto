#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2021年5月22日
@author: yuchao
'''

import os
import yaml

class yamlUtil():
    def read_extract_yml(self,key):
        #读取extract.yml文件,key是写入的变量名
        with open(os.getcwd()+"./testcase/extract.yml",mode='r',encoding='utf8') as f:
            value=yaml.load(stream=f,Loader=yaml.FullLoader)
            return value[key]

    def write_extract_yml(self,data):
        #写入extract.yml文件
        with open(os.getcwd()+"./testcase/extract.yml",mode='a',encoding='utf8') as f:
            yaml.dump(data=data,stream=f,allow_unicode=True)

    def delete_extract_yml(self):
        #清除extract.yml文件
        with open(os.getcwd()+"./testcase/extract.yml",mode='w',encoding='utf8') as f:
            f.truncate()

    def read_testcase_yml(self,yml_name):
        #读取测试用例yml文件
        with open(os.getcwd()+"./testcase/"+yml_name,mode='r',encoding='utf8') as f:
            value=yaml.load(stream=f,Loader=yaml.FullLoader)
            return value
