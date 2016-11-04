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

    #切换窗口
    def switch_window(self):
        current_window=self.get_current_window()
        self.driver.implicitly_wait(10)
        all_handles=self.get_all_handles()
        print all_handles
        for handle in all_handles:
            if handle !=current_window:
                self.driver.switch_to.window(handle)
                print self.driver.title
        return current_window

    #却换到主窗口
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

    def according_type_switch_method(self,find_type,value):
        if find_type =='id':
            return (By.ID,value)
        if find_type =='xpath':
            return (By.XPATH,value)
        if find_type == 'css':
            return (By.CLASS_NAME,value)
        if find_type == 'name':
            return (By.NAME,value)
        if find_type == 'link_text':
            return (By.LINK_TEXT,value)

    #封装元素的等待时间为60秒，如果超过60秒则进行抛出异常
    def wait_until_element(self,driver,locator):
        element= WebDriverWait(driver,60,0.5).until(EC.presence_of_element_located(locator))
        if element is None:
            raise AssertionError("timeout in 60s can not find")
        return element

    def accept_alert(self):
        self.driver.switch_to_alert().accept()

    def mouse_on_element(self,element):
        ActionChains(self.driver).move_to_element(element).perform()


    def get_cookiesValue_by_name(self,driver,name):
        return driver.get_cookies()

    #判断是否包含某段文字
    def page_should_be_contain_text(self,text):
        page=self.driver.page_source
        flage=None
        if isinstance(page,unicode):
            str2=page.encode("utf-8")
            flage= True if str2.find(text)>=0 else None
            return  flage
        return flage

    #封装根据传入的locatr,进行查找相关元素，并进行返回
    def find_element_by_locator(self, locator):
        find_type, value = self.get_type_locator(locator)
        element = self.wait_until_element(self.driver, self.according_type_switch_method(find_type, value))
        if element is None:
            raise AssertionError("未成功找到元素")
        return element

    #封装方法，此方法专门用来定位元素，并进行点击元素进行使用
    def _click_element(self, locator):
        element = self.find_element_by_locator(locator)
        if element is None:
            raise ValueError("元素未找到")
        element.click()

    #封装方法，此方法专门在输入文本框进行使用
    def _input_text(self, locator, text):
        element = self.find_element_by_locator(locator)
        if element is None:
            raise ValueError("未成功定位到此元素")
        element.clear()
        element.send_keys(text)
