# -*- coding:utf-8 -*-
from selenium.webdriver import  remote
from selenium import  webdriver
"""
定义驱动文件，驱动主要抽取出来主要是方便进行使用哪个浏览器，哪个服务器的浏览器进行配置
"""
def browser():
    driver =webdriver.Firefox()
    return driver

if __name__ =="__main__":
    dr =browser()
    dr.get("http://www.baidu.com")
    dr.quit()
