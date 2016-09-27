# -*- coding:utf-8 -*-
"""
主要把setup 与teardown 方法进行提取，将他们抽象，撰写用例的时候不需要考虑这两个方法
"""
from selenium import  webdriver
from .driver import browser
import  unittest
import  os

class GangGangTestObject(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()


    def tearDown(self):
        self.driver.quit()