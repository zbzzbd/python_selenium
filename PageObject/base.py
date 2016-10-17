# -*- coding:utf-8 -*-
"""
页面基类，用于所有页面的继承类
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

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

    def get_current_window(self):
        return self.driver.current_window_handle

    def get_all_handles(self):
        return self.driver.window_handles

    def switch_window(self):
        current_window=self.get_current_window()
        all_handles=self.get_all_handles()
        print all_handles
        for handle in all_handles:
            if handle !=current_window:
                self.driver.switch_to.window(handle)
                print self.driver.title
        return current_window
    def switch_main_window(self,main_window):
        self.driver.switch_to.window(main_window)



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

    def according_type_switch_method(self,str,value):
        if str =='id':
            return (By.ID,value)
        if str =='xpath':
            return (By.XPATH,value)
        if str == 'css':
            return (By.CLASS_NAME,value)
        if str == 'name':
            return (By.NAME,value)
        if str == 'link_text':
            return (By.LINK_TEXT,value)

    #def find_element(self,*locator):
    #    return self.driver.find_element(*locator)

    def wait_until_element(self,driver,locator):
        element= WebDriverWait(driver,60,0.5).until(EC.presence_of_element_located(locator))
        return element

    def accept_alert(self):
        self.driver.switch_to_alert().accept()

    def mouse_on_element(self,element):
        ActionChains(self.driver).move_to_element(element)