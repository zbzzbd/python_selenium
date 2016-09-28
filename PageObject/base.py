# -*- coding:utf-8 -*-
"""
页面基类，用于所有页面的继承类
"""
class GG_BasePage(object):

    def __init__(self,selenium_driver,base_url,parent=None):
        self.base_url=base_url
        self.driver = selenium_driver
        self.timeout =30
        self.parent =parent

    def open(self):
        self._open(self.url)

    def _open(self,url):
        self.url =self.base_url+url
        self.driver.get(url)
        assert self.on_page(),'did not loan on %s' %url

    def on_page(self):
        return self.driver.current_url == (self.base_url +self.url)

    def according_type_find_element(self, driver, str, value):
        if str == 'xpath':
            return driver.find_element_by_xpath(value)
        if str == 'css':
            return driver.find_element_by_class_name(value)
