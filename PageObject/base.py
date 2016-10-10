# -*- coding:utf-8 -*-
"""
页面基类，用于所有页面的继承类
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

from until.Constant import *
class GG_BasePage(object):

    def __init__(self,selenium_driver,base_url,parent=None):
        self.base_url=base_url
        self.driver = selenium_driver
        self.timeout =30
        self.parent =parent

    def Read_elements_item(self,item):
        return Constant().Read_file_init(item)

    def open(self,url):
        self._open(url)

    def _open(self,url):
        self.driver.get(url)
        assert self.on_page(),'did not loan on %s' %url

    def on_page(self):
        return self.driver.current_url ==self.base_url

    def get_type_locator(self, str):
        find_type, value = Constant().pase_element_find_method(str)
        return find_type,value

    def according_type_find_element(self, driver, str, value):
        if str == 'xpath':
            return driver.find_element_by_xpath(value)
        if str == 'css':
            return driver.find_element_by_class_name(value)
        if str == 'id':
            return driver.find_element_by_id(value)

    def wait_until_element(self,driver,locator):
        element= WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located(locator))
        return element